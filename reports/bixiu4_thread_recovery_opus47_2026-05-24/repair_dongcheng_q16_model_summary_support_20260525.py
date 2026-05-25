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
REPORT = RECOVERY / "DONGCHENG_Q16_MODEL_SUMMARY_SUPPORT_REPAIR_20260525.md"

SUPPORT_BY_ROW = {
    "M0002": "东城第16题主观题细则16.pdf第4页知识表列“实践决定认识、物质决定意识（规律）”；本条只使用物质决定意识/一切从实际出发，不再展开主观能动性。",
    "M0003": "东城第16题主观题细则16.pdf第4页知识表列“联系（系统）”；本条对应系统观念/系统优化，要求把课程目标、真实场景、探究任务和数字资源作为整体协同理解。",
    "M0005": "东城第16题主观题细则16.pdf第4页知识表列“矛盾特殊性”；本条对应具体问题具体分析，要求从北京真实城市资源、学生成长实际和育人任务出发。",
    "M0006": "东城第16题主观题细则16.pdf第4页知识表列“价值观”；同页要求材料落到“京彩课堂的价值”，示例总述写“价值深远/国家、民族、时代新人”。",
}

SUPPORT_BY_ACCEPTED_INDEX = {
    1: SUPPORT_BY_ROW["M0002"],
    2: SUPPORT_BY_ROW["M0003"],
    4: SUPPORT_BY_ROW["M0005"],
    5: SUPPORT_BY_ROW["M0006"],
}


def backup(path: Path, timestamp: str) -> Path:
    out = path.with_name(f"{path.stem}_backup_before_dongcheng_q16_support_repair_{timestamp}{path.suffix}")
    shutil.copy2(path, out)
    return out


def repair_matrix(timestamp: str) -> tuple[Path, list[str]]:
    backup_path = backup(MATRIX, timestamp)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    row_id_key = "matrix_row_id"
    support_key = headers[9]
    repaired = []
    for row in rows:
        row_id = row.get(row_id_key, "")
        if row_id not in SUPPORT_BY_ROW:
            continue
        row[support_key] = SUPPORT_BY_ROW[row_id]
        repaired.append(row_id)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    return backup_path, repaired


def repair_accepted(timestamp: str) -> tuple[Path, list[int]]:
    backup_path = backup(ACCEPTED, timestamp)
    lines = ACCEPTED.read_text(encoding="utf-8").splitlines()
    repaired: list[int] = []
    out_lines = []
    for idx, line in enumerate(lines):
        if not line.strip():
            out_lines.append(line)
            continue
        obj = json.loads(line)
        if idx in SUPPORT_BY_ACCEPTED_INDEX:
            obj["source_repair_basis"] = SUPPORT_BY_ACCEPTED_INDEX[idx]
            repaired.append(idx + 1)
        out_lines.append(json.dumps(obj, ensure_ascii=False))
    ACCEPTED.write_text("\n".join(out_lines) + "\n", encoding="utf-8", newline="\n")
    return backup_path, repaired


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    matrix_backup, matrix_rows = repair_matrix(timestamp)
    accepted_backup, accepted_lines = repair_accepted(timestamp)
    REPORT.write_text(
        "\n".join(
            [
                "# DONGCHENG_Q16_MODEL_SUMMARY_SUPPORT_REPAIR_20260525",
                "",
                "Status: `MODEL_SUMMARY_SUPPORT_REPLACED_WITH_FORMAL_RUBRIC_TEXT`",
                "",
                f"- Timestamp: `{timestamp}`.",
                f"- Matrix backup: `{matrix_backup}`.",
                f"- Accepted JSONL backup: `{accepted_backup}`.",
                f"- Matrix rows repaired: `{', '.join(matrix_rows)}`.",
                f"- Accepted JSONL lines repaired: `{', '.join(str(i) for i in accepted_lines)}`.",
                "- Formal source used: `01_source_inventory/suite_source_bundles/2026东城二模.md`, file section `16.pdf`, page 4 knowledge table.",
                "- Replaced support text that previously read as model-summary provenance with explicit rubric phrases: `物质决定意识（规律）`, `联系（系统）`, `矛盾特殊性`, and `价值观`.",
                "",
                "Boundary: this repair changes evidence wording/provenance only. It does not change DOCX body text, placement, or external-review gates.",
            ]
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"MATRIX_BACKUP={matrix_backup}")
    print(f"ACCEPTED_BACKUP={accepted_backup}")
    print(f"MATRIX_ROWS_REPAIRED={','.join(matrix_rows)}")
    print(f"ACCEPTED_LINES_REPAIRED={','.join(str(i) for i in accepted_lines)}")
    print(f"REPORT={REPORT}")


if __name__ == "__main__":
    main()
