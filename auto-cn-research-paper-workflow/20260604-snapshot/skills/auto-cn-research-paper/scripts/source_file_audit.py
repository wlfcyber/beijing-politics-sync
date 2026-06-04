#!/usr/bin/env python3
"""Audit whether recorded source files exist on the current machine."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath


FULLTEXT_STATUSES = ("PDF_or_user_exported", "full_text_read", "official_html_full_text")


@dataclass
class InventoryRow:
    source_file: str
    text_file: str
    evidence_status: str
    current_source: Path | None
    current_text: Path | None


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def split_md_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_windows_path(value: str) -> bool:
    return bool(re.match(r"^[A-Za-z]:\\", value)) or "\\" in value


def basename(value: str) -> str:
    value = value.strip().strip("`")
    if is_windows_path(value):
        return PureWindowsPath(value).name
    return Path(value).name


def parse_inventory(text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("| ---") or "Evidence status" in line:
            continue
        cells = split_md_row(line)
        if len(cells) < 6:
            continue
        evidence_status = cells[5]
        if any(status in evidence_status for status in FULLTEXT_STATUSES):
            rows.append((cells[0], cells[4], evidence_status))
    return rows


def record_file_candidates(record: str) -> list[str]:
    candidates: list[str] = []
    for value in re.findall(r"`([^`]+)`", record):
        if filename_has_source_or_text_extension(value):
            candidates.append(value)
    for value in re.findall(r"[A-Za-z]:\\[^`；;，,|]+", record):
        if filename_has_source_or_text_extension(value):
            candidates.append(value)
    return candidates


def normalized_name(value: str) -> str:
    return basename(value).lower()


def filename_has_source_or_text_extension(value: str) -> bool:
    name = basename(value).lower()
    return name.endswith((".pdf", ".caj", ".kdh", ".html", ".htm", ".txt"))


def parse_matrix_supplement(text: str, existing_names: set[str]) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| S-"):
            continue
        cells = split_md_row(line)
        if len(cells) < 12:
            continue
        status = cells[1]
        if not any(fulltext_status in status for fulltext_status in FULLTEXT_STATUSES):
            continue
        candidates = record_file_candidates(cells[11])
        source_candidates = [
            candidate for candidate in candidates if basename(candidate).lower().endswith((".pdf", ".caj", ".kdh", ".html", ".htm"))
        ]
        text_candidates = [candidate for candidate in candidates if basename(candidate).lower().endswith(".txt")]
        if not source_candidates and not text_candidates:
            continue
        candidate_names = {normalized_name(candidate) for candidate in [*source_candidates, *text_candidates]}
        if candidate_names & existing_names:
            continue
        source_file = source_candidates[-1] if source_candidates else ""
        text_file = text_candidates[-1] if text_candidates else ""
        rows.append((source_file, text_file, status))
    return rows


def collect_search_roots(run_dir: Path, explicit_roots: list[str]) -> list[Path]:
    roots = [run_dir, Path.cwd()]
    roots.extend(Path(root).expanduser().resolve() for root in explicit_roots)
    unique: list[Path] = []
    seen: set[str] = set()
    for root in roots:
        try:
            resolved = root.expanduser().resolve()
        except OSError:
            continue
        key = str(resolved)
        if key not in seen and resolved.exists():
            seen.add(key)
            unique.append(resolved)
    return unique


def find_current_path(recorded: str, run_dir: Path, search_roots: list[Path]) -> Path | None:
    recorded = recorded.strip().strip("`")
    if not recorded:
        return None
    if not is_windows_path(recorded):
        path = Path(recorded).expanduser()
        if not path.is_absolute():
            path = run_dir / path
        if path.exists():
            return path.resolve()
    wanted = basename(recorded)
    if not wanted:
        return None
    for root in search_roots:
        for candidate in root.rglob(wanted):
            if candidate.is_file():
                return candidate.resolve()
    return None


def audit_rows(run_dir: Path, search_roots: list[Path]) -> list[InventoryRow]:
    inventory_text = read(run_dir / "source_inventory.md")
    matrix_text = read(run_dir / "03_文献矩阵.md")
    parsed_inventory = parse_inventory(inventory_text)
    existing_names = {normalized_name(value) for source, text, _ in parsed_inventory for value in (source, text) if basename(value)}
    parsed_rows = [*parsed_inventory, *parse_matrix_supplement(matrix_text, existing_names)]
    rows: list[InventoryRow] = []
    for source_file, text_file, evidence_status in parsed_rows:
        rows.append(
            InventoryRow(
                source_file=source_file,
                text_file=text_file,
                evidence_status=evidence_status,
                current_source=find_current_path(source_file, run_dir, search_roots),
                current_text=find_current_path(text_file, run_dir, search_roots),
            )
        )
    return rows


def count_windows_paths(rows: list[InventoryRow]) -> int:
    count = 0
    for row in rows:
        count += int(is_windows_path(row.source_file))
        count += int(is_windows_path(row.text_file))
    return count


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Defaults to <run_dir>/23_材料文件迁移审计.md")
    parser.add_argument("--search-root", action="append", default=[], help="Extra directory to search by recorded filename.")
    parser.add_argument("--min-current-fulltext", type=int, default=8)
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "23_材料文件迁移审计.md"
    search_roots = collect_search_roots(run_dir, args.search_root)
    rows = audit_rows(run_dir, search_roots)

    current_source_count = sum(1 for row in rows if row.current_source)
    current_text_count = sum(1 for row in rows if row.current_text)
    windows_path_count = count_windows_paths(rows)
    issues: list[str] = []

    if not rows:
        issues.append("source_inventory.md has no full-text inventory rows")
    if current_text_count < args.min_current_fulltext:
        issues.append(f"current_text_count below required minimum: {current_text_count} < {args.min_current_fulltext}")
    for row in rows:
        if not row.current_source:
            issues.append(f"missing current source file: {row.source_file}")
        if not row.current_text:
            issues.append(f"missing current extracted text: {row.text_file}")
    if windows_path_count:
        issues.append("Windows-era paths are recorded; migrate files or re-extract them on this Mac")

    status = "PASS" if not issues else "INCOMPLETE"
    lines = [
        "# 材料文件迁移审计",
        "",
        "## Summary",
        "",
        f"- current_source_files_ready: {'yes' if status == 'PASS' else 'no'}",
        f"- inventory_row_count: {len(rows)}",
        f"- current_source_count: {current_source_count}",
        f"- current_text_count: {current_text_count}",
        f"- min_current_fulltext: {args.min_current_fulltext}",
        f"- windows_path_count: {windows_path_count}",
        "",
        "## Search Roots",
        "",
    ]
    lines.extend(f"- `{root}`" for root in search_roots)
    lines.extend(
        [
            "",
            "## Inventory Rows",
            "",
            "| Recorded source | Current source | Recorded text | Current text | Evidence status |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row.source_file,
                    str(row.current_source) if row.current_source else "missing",
                    row.text_file,
                    str(row.current_text) if row.current_text else "missing",
                    row.evidence_status,
                ]
            ).replace("\n", " ")
            + " |"
        )
    lines.extend(["", "## Issues", ""])
    if issues:
        lines.extend(f"- {issue}" for issue in issues)
    else:
        lines.append("- none")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"status={status}")
    print(f"inventory_row_count={len(rows)}")
    print(f"current_source_count={current_source_count}")
    print(f"current_text_count={current_text_count}")
    print(f"windows_path_count={windows_path_count}")
    print(f"out={out}")
    for issue in issues:
        print(f"- {issue}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
