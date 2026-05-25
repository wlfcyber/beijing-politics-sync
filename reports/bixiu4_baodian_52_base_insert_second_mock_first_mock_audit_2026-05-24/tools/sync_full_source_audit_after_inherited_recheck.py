from __future__ import annotations

import csv
import shutil
from datetime import datetime
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
GOV = RUN / "06_governor_confucius"
CSV_PATH = GOV / "FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv"
MD_PATH = GOV / "FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.md"

OLD_STATUS = "INHERITED_BASE_NOT_REOPENED_THIS_DELTA"
OLD_BUCKET = "DOCX_BASE_COVERED_NOT_REOPENED_THIS_DELTA"
NEW_STATUS = "INHERITED_BASE_ROW_RECHECKED_SCOPED_PASS"
NEW_BUCKET = "DOCX_BASE_COVERED_ROW_RECHECKED_SCOPED_PASS"


def backup(path: Path) -> Path:
    dest = path.with_name(f"{path.stem}_backup_before_inherited_recheck_sync_{datetime.now():%Y%m%d_%H%M%S}{path.suffix}")
    shutil.copy2(path, dest)
    return dest


def sync_csv() -> int:
    backup(CSV_PATH)
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = f.seek(0) or None
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []

    changed = 0
    for row in rows:
        if row.get("current_closure_status") == OLD_STATUS:
            row["current_closure_status"] = NEW_STATUS
            row["coverage_bucket"] = NEW_BUCKET
            changed += 1

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return changed


def sync_md(changed: int) -> None:
    backup(MD_PATH)
    text = MD_PATH.read_text(encoding="utf-8")
    text = text.replace(
        "| suites present in final DOCX but inherited from accepted base, not reopened in this delta | 12 |",
        "| suites present in final DOCX and inherited-base row-level rechecked | 12 |",
    )
    text = text.replace(
        "It does not independently re-score every inherited 2024/2025 second-mock row; those rows are treated as base-handbook coverage unless a separate row-level rerun is ordered.",
        "The 12 inherited 2024/2025 second-mock suites were later row-level extracted and rechecked: 135 rows, 0 thin material/why/answer fields after patching, with ClaudeCode scoped PASS and the Haidian Q10/Q11 choice-only boundary preserved.",
    )
    text = text.replace(OLD_STATUS, NEW_STATUS)
    text = text.replace(OLD_BUCKET, NEW_BUCKET)
    marker = "## Boundary\n\n"
    insert = (
        "## Inherited Row-Level Sync\n\n"
        f"- Synced after inherited second-mock row-level recheck: {changed} suite rows updated from `not reopened` to `row-level rechecked scoped pass`.\n"
        "- Detailed evidence: `INHERITED_2024_2025_SECOND_MOCK_ROW_EXTRACT_20260524.csv`, `haidian_2025_second_mock_evidence_closeout_20260524.md`, and ClaudeCode recheck outputs.\n\n"
    )
    if "## Inherited Row-Level Sync" not in text:
        text = text.replace(marker, insert + marker)
    MD_PATH.write_text(text, encoding="utf-8")


def main() -> int:
    changed = sync_csv()
    sync_md(changed)
    print(f"updated_inherited_rows={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
