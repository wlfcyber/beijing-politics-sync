from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
REPORT = RECOVERY / "SHUNYI_Q16_MODEL_SUMMARY_SUPPORT_REPAIR_20260525.md"

ROW_ID = "M0032"
ACCEPTED_LINE_NO = 32
SUPPORT_TEXT = (
    "顺义二模评标doc第16题阅卷版：评标说明列“实践观点”；阅卷版明确"
    "“一切从实际出发，实事求是/实践是认识的基础/社会存在决定社会意识”，"
    "并写“群众的实践活动是新大众文艺创作的源泉”。"
)


def backup(path: Path, timestamp: str) -> Path:
    out = path.with_name(f"{path.stem}_backup_before_shunyi_q16_support_repair_{timestamp}{path.suffix}")
    shutil.copy2(path, out)
    return out


def repair_matrix(timestamp: str) -> tuple[Path, bool, str]:
    backup_path = backup(MATRIX, timestamp)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    support_key = headers[9]
    old_support = ""
    repaired = False
    for row in rows:
        if row.get("matrix_row_id") != ROW_ID:
            continue
        old_support = row.get(support_key, "")
        row[support_key] = SUPPORT_TEXT
        repaired = True
        break

    if not repaired:
        raise RuntimeError(f"Matrix row not found: {ROW_ID}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    return backup_path, repaired, old_support


def repair_accepted(timestamp: str) -> tuple[Path, bool, str]:
    backup_path = backup(ACCEPTED, timestamp)
    lines = ACCEPTED.read_text(encoding="utf-8").splitlines()
    index = ACCEPTED_LINE_NO - 1
    if index >= len(lines):
        raise RuntimeError(f"Accepted JSONL line not found: {ACCEPTED_LINE_NO}")

    out_lines: list[str] = []
    old_support = ""
    repaired = False
    for idx, line in enumerate(lines):
        if not line.strip():
            out_lines.append(line)
            continue
        obj = json.loads(line)
        if idx == index:
            old_support = obj.get("source_repair_basis", "")
            obj["source_repair_basis"] = SUPPORT_TEXT
            repaired = True
        out_lines.append(json.dumps(obj, ensure_ascii=False))

    if not repaired:
        raise RuntimeError(f"Accepted JSONL line not repaired: {ACCEPTED_LINE_NO}")

    ACCEPTED.write_text("\n".join(out_lines) + "\n", encoding="utf-8", newline="\n")
    return backup_path, repaired, old_support


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    matrix_backup, _, old_matrix_support = repair_matrix(timestamp)
    accepted_backup, _, old_accepted_support = repair_accepted(timestamp)

    REPORT.write_text(
        "\n".join(
            [
                "# SHUNYI_Q16_MODEL_SUMMARY_SUPPORT_REPAIR_20260525",
                "",
                "Status: `MODEL_SUMMARY_SUPPORT_REPLACED_WITH_FORMAL_MARKING_TEXT`",
                "",
                f"- Timestamp: `{timestamp}`.",
                f"- Matrix backup: `{matrix_backup}`.",
                f"- Accepted JSONL backup: `{accepted_backup}`.",
                f"- Matrix row repaired: `{ROW_ID}`.",
                f"- Accepted JSONL line repaired: `{ACCEPTED_LINE_NO}`.",
                "- Old matrix support text: `" + old_matrix_support.replace("`", "'") + "`.",
                "- Old accepted support text: `" + old_accepted_support.replace("`", "'") + "`.",
                "- Formal source used: `01_source_inventory/suite_source_bundles/2026顺义二模.md`, file section `26顺义二模评标.doc`, Q16 marking/阅卷版.",
                "- Replacement support text: `" + SUPPORT_TEXT.replace("`", "'") + "`.",
                "",
                "Boundary: this repair changes evidence wording/provenance only. It does not change body placement, DOCX text, or external-review gates.",
                "",
                "External review status: Claude Opus 4.7 / GPTPro web-app external review remains `real_call_pending` until a real model-confirmed call is completed.",
            ]
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"MATRIX_BACKUP={matrix_backup}")
    print(f"ACCEPTED_BACKUP={accepted_backup}")
    print(f"MATRIX_ROW_REPAIRED={ROW_ID}")
    print(f"ACCEPTED_LINE_REPAIRED={ACCEPTED_LINE_NO}")
    print(f"REPORT={REPORT}")


if __name__ == "__main__":
    main()
