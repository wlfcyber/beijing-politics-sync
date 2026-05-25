from __future__ import annotations

import csv
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"

TARGET_IDS = {"M0034", "M0035", "M0036"}

FIELD_ID = "matrix_row_id"
FIELD_SOURCE_RULE = "\u7ec6\u5219\u652f\u6301\u539f\u7406"
FIELD_EVIDENCE = "\u8bc1\u636e\u7b49\u7ea7"
FIELD_MISPLACED = "\u662f\u5426\u8bef\u653e"
FIELD_THICKEN = "\u662f\u5426\u9700\u8865\u539a"
FIELD_STATUS = "\u5f53\u524d\u5904\u7406"
FIELD_NOTE = "\u5907\u6ce8"

VALUE_SOURCE_RULE = (
    "\u7b54\u6848\u8bc4\u5206\u53c2\u8003\u7b2c17(3)\u660e\u786e"
    "\u53ef\u4ece\u8054\u7cfb\u3001\u77db\u76fe\u3001\u5b9e\u8df5"
    "\u4e0e\u8ba4\u8bc6\u5173\u7cfb\u7b49\u89d2\u5ea6\u56de\u7b54"
    "\uff1b\u4ec5\u4e3a\u4efb\u9009\u8def\u5f84\uff0c"
    "\u4e0d\u4f5c\u7d2f\u52a0\u91c7\u5206\u3002"
)
VALUE_EVIDENCE = "\u6b63\u5f0f\u8bc4\u5206\u53c2\u8003\u89d2\u5ea6"
VALUE_NO = "\u5426"
VALUE_STATUS = (
    "Batch04 ClaudeCode correction applied: evidence_level synced to "
    "optional scoring-reference angle; not cumulative strong rubric."
)
VALUE_NOTE = (
    "Batch04 ClaudeCode correction: structured evidence_level synced "
    "from strong rubric to optional scoring-reference angle."
)


def main() -> None:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = RECOVERY / (
        "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_"
        f"batch04_claudecode_mirror_correction_{stamp}.csv"
    )
    shutil.copy2(MATRIX, backup)

    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    if not fieldnames:
        raise SystemExit("matrix has no header")

    seen = set()
    for row in rows:
        if row.get(FIELD_ID) not in TARGET_IDS:
            continue
        seen.add(row[FIELD_ID])
        row[FIELD_SOURCE_RULE] = VALUE_SOURCE_RULE
        row[FIELD_EVIDENCE] = VALUE_EVIDENCE
        row[FIELD_MISPLACED] = VALUE_NO
        row[FIELD_THICKEN] = VALUE_NO
        row[FIELD_STATUS] = VALUE_STATUS
        note = row.get(FIELD_NOTE, "")
        if VALUE_NOTE not in note:
            row[FIELD_NOTE] = f"{note} {VALUE_NOTE}".strip()

    missing = TARGET_IDS - seen
    if missing:
        raise SystemExit(f"missing target rows: {sorted(missing)}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"backup={backup}")
    print(f"updated={','.join(sorted(seen))}")


if __name__ == "__main__":
    main()
