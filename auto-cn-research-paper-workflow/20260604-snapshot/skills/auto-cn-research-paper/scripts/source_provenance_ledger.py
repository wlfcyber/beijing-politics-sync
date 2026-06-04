#!/usr/bin/env python3
"""Create and validate a source provenance ledger for verified paper sources."""

from __future__ import annotations

import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cell(value: str) -> str:
    return str(value or "").replace("|", "／").replace("\n", " ").replace("\r", " ").strip()


def split_row(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def verified_source_ids(matrix_text: str) -> dict[str, str]:
    sources: dict[str, str] = {}
    for line in matrix_text.splitlines():
        if not line.startswith("| S-"):
            continue
        parts = split_row(line)
        if not parts:
            continue
        status = " ".join(parts)
        if "PDF_or_user_exported" in status or "full_text_read" in status:
            sources[parts[0]] = status
    return sources


def parse_records(ledger_text: str) -> dict[str, list[str]]:
    records: dict[str, list[str]] = {}
    for line in ledger_text.splitlines():
        if not line.startswith("| S-"):
            continue
        parts = split_row(line)
        if len(parts) >= 11:
            records[parts[0]] = parts[:11]
        elif len(parts) >= 10:
            source_id, *rest = parts[:10]
            records[source_id] = [source_id, "legacy_missing_run_id", *rest]
    return records


def record_from_args(args: argparse.Namespace, run_dir: Path) -> list[str]:
    local_file = ""
    sha = ""
    size = ""
    if args.local_file:
        local_path = Path(args.local_file).expanduser().resolve()
        local_file = str(local_path)
        if local_path.exists():
            sha = f"sha256:{sha256_file(local_path)}"
            size = str(local_path.stat().st_size)
        else:
            sha = "missing_file"
            size = "missing_file"
    return [
        args.source_id,
        run_dir.name,
        args.title,
        args.database,
        args.route_url,
        args.method,
        local_file,
        sha,
        size,
        f"retrieved_at:{args.retrieved_at or datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        args.note,
    ]


def invalid_record(source_id: str, matrix_status: str, record: list[str], run_dir: Path) -> str:
    _source_id, run_id, _title, database, route_url, method, local_file, sha, _size, retrieved_at, _note = record
    if run_id != run_dir.name:
        return f"{source_id}: run_id mismatch: {run_id} != {run_dir.name}"
    if not retrieved_at:
        return f"{source_id}: missing retrieved_at"
    if not database:
        return f"{source_id}: missing database"
    if not route_url:
        return f"{source_id}: missing route_url"
    if "PDF_or_user_exported" in matrix_status or "PDF_or_user_exported" in method:
        if not local_file:
            return f"{source_id}: missing local_file for PDF/user-exported source"
        if not sha or sha == "missing_file":
            return f"{source_id}: missing sha256 for PDF/user-exported source"
    return ""


def build_output(run_dir: Path, records: dict[str, list[str]], matrix_text: str) -> tuple[str, bool, list[str]]:
    verified = verified_source_ids(matrix_text)
    missing = [source_id for source_id in sorted(verified) if source_id not in records]
    invalid = [
        issue
        for source_id, record in sorted(records.items())
        if source_id in verified
        for issue in [invalid_record(source_id, verified[source_id], record, run_dir)]
        if issue
    ]
    ready = not missing and not invalid and bool(verified)

    lines = [
        "# Source Provenance Ledger",
        "",
        "## Summary",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- verified_source_count: {len(verified)}",
        f"- ledger_record_count: {len(records)}",
        f"- missing_provenance_sources: {len(missing)}",
        f"- invalid_provenance_rows: {len(invalid)}",
        f"- provenance_ready: {'yes' if ready else 'no'}",
        "",
        "## Records",
        "",
        "| source_id | run_id | title | database | route_url | method | local_file | sha256 | file_size | retrieved_at | note |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in sorted(records.values(), key=lambda row: row[0]):
        lines.append("| " + " | ".join(cell(value) for value in record) + " |")
    if missing or invalid:
        lines.extend(["", "## Issues", ""])
        for source_id in missing:
            lines.append(f"- missing_provenance: {source_id}")
        for issue in invalid:
            lines.append(f"- invalid_provenance: {issue}")
    return "\n".join(lines) + "\n", ready, [*missing, *invalid]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Defaults to <run_dir>/source_provenance_ledger.md")
    parser.add_argument("--add", action="store_true", help="Add or replace one source provenance record.")
    parser.add_argument("--validate", action="store_true", help="Validate the ledger against verified sources in 03_文献矩阵.md.")
    parser.add_argument("--source-id")
    parser.add_argument("--title", default="")
    parser.add_argument("--database", default="")
    parser.add_argument("--route-url", default="")
    parser.add_argument("--method", default="")
    parser.add_argument("--local-file")
    parser.add_argument("--retrieved-at")
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "source_provenance_ledger.md"

    matrix_text = read(run_dir / "03_文献矩阵.md")
    records = parse_records(read(out))
    if args.add:
        if not args.source_id:
            parser.error("--source-id is required with --add")
        records[args.source_id] = record_from_args(args, run_dir)

    output, ready, issues = build_output(run_dir, records, matrix_text)
    if args.add or args.validate or not out.exists():
        out.write_text(output, encoding="utf-8")

    print(f"provenance_ready={'yes' if ready else 'no'}")
    print(f"missing_or_invalid={len(issues)}")
    print(f"out={out}")
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
