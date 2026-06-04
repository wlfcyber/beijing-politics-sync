#!/usr/bin/env python3
"""Audit source-number freeze rules for a research-paper run.

This catches silent reuse of formal S-* IDs after a source has been demoted,
which is especially important when citation anchors and external reviews refer
to stable source numbers.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def split_md_row(line: str) -> list[str]:
    return [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]


def find_matrix_path(run_dir: Path) -> Path | None:
    candidates = sorted(run_dir.glob("03_*.md"))
    if not candidates:
        return None
    for path in candidates:
        if "文献" in path.name or "鐭╅樀" in path.name:
            return path
    return candidates[0]


def parse_rows(matrix_text: str) -> tuple[dict[str, str], list[str]]:
    rows: dict[str, str] = {}
    duplicates: list[str] = []
    for line in matrix_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("| "):
            continue
        cells = split_md_row(stripped)
        if not cells or not (cells[0].startswith("S-") or cells[0].startswith("C-")):
            continue
        source_id = cells[0]
        if source_id in rows:
            duplicates.append(source_id)
        rows[source_id] = stripped
    return rows, duplicates


def row_has(row: str, *terms: str) -> bool:
    return all(term in row for term in terms)


def audit_matrix(matrix_text: str) -> tuple[list[str], list[tuple[str, str, str]]]:
    rows, duplicates = parse_rows(matrix_text)
    issues: list[str] = []
    checks: list[tuple[str, str, str]] = []

    def add_check(rule: str, passed: bool, evidence: str) -> None:
        checks.append((rule, "PASS" if passed else "INCOMPLETE", evidence))
        if not passed:
            issues.append(f"{rule}: {evidence}")

    add_check(
        "no_duplicate_source_ids",
        not duplicates,
        "duplicates=" + ",".join(sorted(set(duplicates))) if duplicates else "no duplicates",
    )

    s008 = rows.get("S-008", "")
    add_check(
        "S-008_frozen_to_Ogburn_1922",
        row_has(s008, "Ogburn", "1922", "Social Change"),
        "S-008 must remain William F. Ogburn, Social Change, 1922",
    )
    add_check(
        "S-008_not_reused_for_demoted_policy_reprint_or_Simon",
        s008
        and all(term not in s008 for term in ["杨正军", "刘丛丛", "搜狐", "Simon", "Administrative Behavior"]),
        "S-008 must not contain demoted policy reprint or Simon material",
    )

    c006 = rows.get("C-006", "")
    add_check(
        "C-006_demoted_policy_reprint_stays_background",
        c006 and "public_reprint_background_not_formal" in c006,
        "C-006 must remain public_reprint_background_not_formal",
    )

    c007 = rows.get("C-007", "")
    add_check(
        "C-007_Simon_stays_background_until_page_version_fixed",
        c007 and ("Simon" in c007 or "Administrative Behavior" in c007) and "version_page_mismatch" in c007,
        "C-007 must keep Simon as background until publication/page version is fixed",
    )

    formal_rows = {source_id: row for source_id, row in rows.items() if source_id.startswith("S-")}
    forbidden_formal_terms = [
        "public_reprint_background_not_formal",
        "version_page_mismatch",
        "杨正军",
        "刘丛丛",
        "搜狐",
        "Herbert A. Simon",
        "Administrative Behavior",
    ]
    polluted = [
        f"{source_id}:{term}"
        for source_id, row in formal_rows.items()
        for term in forbidden_formal_terms
        if term in row
    ]
    add_check(
        "formal_S_rows_do_not_contain_demoted_sources",
        not polluted,
        "polluted=" + ",".join(polluted) if polluted else "no demoted source terms in formal S rows",
    )

    calibration_terms = ["编号校准", "S-008", "C-006", "C-007"]
    add_check(
        "matrix_contains_numbering_calibration_note",
        all(term in matrix_text for term in calibration_terms),
        "matrix should document S-008/C-006/C-007 freeze chain",
    )

    return issues, checks


def write_report(out: Path, matrix_path: Path | None, issues: list[str], checks: list[tuple[str, str, str]]) -> None:
    lines = [
        "# Source ID Freeze Audit",
        "",
        f"- status: {'PASS' if not issues else 'INCOMPLETE'}",
        f"- matrix_path: `{matrix_path}`" if matrix_path else "- matrix_path: missing",
        "",
        "| Rule | Status | Evidence |",
        "| --- | --- | --- |",
    ]
    for rule, status, evidence in checks:
        lines.append(f"| {rule} | {status} | {evidence.replace('|', '/')} |")
    if issues:
        lines.extend(["", "## Issues", ""])
        lines.extend(f"- {issue}" for issue in issues)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Markdown output path. Defaults to <run-dir>/source_id_freeze_audit.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "source_id_freeze_audit.md"
    matrix_path = find_matrix_path(run_dir)
    if matrix_path is None:
        issues = ["literature matrix file not found"]
        checks: list[tuple[str, str, str]] = []
    else:
        issues, checks = audit_matrix(read(matrix_path))

    write_report(out, matrix_path, issues, checks)
    print(f"status={'PASS' if not issues else 'INCOMPLETE'}")
    print(f"source_id_freeze_ready={'yes' if not issues else 'no'}")
    print(f"out={out}")
    for issue in issues:
        print(f"- {issue}")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
