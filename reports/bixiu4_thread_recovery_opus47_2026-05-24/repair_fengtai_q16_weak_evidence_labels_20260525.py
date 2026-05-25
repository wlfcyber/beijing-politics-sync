from __future__ import annotations

import csv
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT = RECOVERY / "FENGTAI_Q16_WEAK_EVIDENCE_LABEL_REPAIR_20260525.md"

SOURCE = (
    "01_source_inventory\\suite_source_bundles\\2026丰台一模.md:432-436; "
    "C:\\Users\\Administrator\\Desktop\\beijing_politics_research\\data\\preprocessed_corpus\\gpt_sources\\26649804f1de31f5_2026丰台一模细则.md:98-101"
)

FIXES = {
    "M0049": (
        "正式阅卷细则",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（1）点明确“坚持矛盾的观点，用全面、辩证的眼光看问题”，并要求看到AI积极作用和风险挑战。",
    ),
    "M0128": (
        "正式阅卷细则",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（1）点明确“坚持矛盾的观点，用全面、辩证的眼光看问题”，并要求看到AI积极作用和风险挑战。",
    ),
    "M0050": (
        "正式阅卷细则（进阶阐述）",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（1）点后写“或者进一步阐述：坚持两点论与重点论的统一。AI的积极作用是主流，风险与隐忧是支流”。",
    ),
    "M0129": (
        "正式阅卷细则（进阶阐述）",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（1）点后写“或者进一步阐述：坚持两点论与重点论的统一。AI的积极作用是主流，风险与隐忧是支流”。",
    ),
    "M0051": (
        "正式阅卷细则",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（2）点明确“坚持联系的观点，立足整体，统筹部分”，要求统筹科技、伦理与社会公平。",
    ),
    "M0130": (
        "正式阅卷细则",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（2）点明确“坚持联系的观点，立足整体，统筹部分”，要求统筹科技、伦理与社会公平。",
    ),
    "M0052": (
        "正式阅卷细则",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（3）点明确“坚持正确的价值观，发挥科学价值观的导向作用”，并要求朝着有益、安全、公平方向健康发展。",
    ),
    "M0131": (
        "正式阅卷细则",
        "丰台一模主观题阅卷说明Q16哲学评分细则：第（3）点明确“坚持正确的价值观，发挥科学价值观的导向作用”，并要求朝着有益、安全、公平方向健康发展。",
    ),
}


def backup(path: Path, timestamp: str) -> Path:
    out = path.with_name(f"{path.stem}_backup_before_fengtai_q16_weak_label_repair_{timestamp}{path.suffix}")
    shutil.copy2(path, out)
    return out


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup(MATRIX, timestamp)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    support_key = headers[9]
    evidence_key = headers[10]
    misplaced_key = headers[11]
    need_key = headers[12]
    status_key = headers[13]
    note_key = headers[14]
    source_key = headers[15]
    repaired: list[str] = []

    for row in rows:
        row_id = row.get("matrix_row_id", "")
        fix = FIXES.get(row_id)
        if not fix:
            continue
        evidence, support = fix
        row[support_key] = support
        row[evidence_key] = evidence
        row[misplaced_key] = "否"
        row[need_key] = "否：Q16对应节点已有正式阅卷细则支撑；全书厚度外审仍 real_call_pending。"
        row[status_key] = "KEEP_IN_BODY_FORMAL_RUBRIC_CONFIRMED_EXTERNAL_OPEN"
        row[note_key] = "移除证据等级中的参考答案措辞；本行只按正式阅卷细则计入正文支撑。"
        row[source_key] = SOURCE
        repaired.append(row_id)

    if set(repaired) != set(FIXES):
        raise RuntimeError(f"Repair incomplete: {repaired}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    REPORT.write_text(
        "\n".join(
            [
                "# FENGTAI_Q16_WEAK_EVIDENCE_LABEL_REPAIR_20260525",
                "",
                "Status: `FORMAL_RUBRIC_LABEL_REPAIRED_EXTERNAL_REVIEW_OPEN`",
                "",
                f"- Timestamp: `{timestamp}`.",
                f"- Matrix backup: `{backup_path}`.",
                f"- Matrix rows repaired: `{', '.join(repaired)}`.",
                "- Source used: `2026丰台一模` 主观题阅卷说明 / 评分细则, lines `432-436` in the suite bundle and lines `98-101` in the GPT source cache.",
                "- Corrected issue: evidence labels previously mixed formal marking text with answer-version/reference-answer wording, causing weak-evidence risk.",
                "- Boundary: Q21 remains weak/reference evidence because its available source is still answer-version plus broad PPT angle, not a point-by-point scoring rule.",
            ]
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"MATRIX_BACKUP={backup_path}")
    print(f"MATRIX_ROWS_REPAIRED={','.join(repaired)}")
    print(f"REPORT={REPORT}")


if __name__ == "__main__":
    main()
