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
REPORT = RECOVERY / "CHAOYANG_2025_Q16_FORMAL_IMAGE_EVIDENCE_REPAIR_20260525.md"

TARGET_MATRIX_IDS = {"M0177", "M0209", "M0424"}

SUPPORT_TEXT = (
    "2025朝阳一模细则第16题渲染页page_001显示“答案变通说明”："
    "①作为文化载体1分；②重视文化资源/传递正确价值观2分；"
    "③借助现代科技推动文化创新、传统文化与现代传播方式结合2分；"
    "④立足时代之基、面向人民需求，衔接传统文化内涵与时代审美愿望2分；"
    "⑤把握社会客观条件、个人与社会统一，弘扬劳动精神/工匠精神/创新精神，"
    "实现人生价值，以局部推动整体1分。"
)

SOURCE_ARTIFACT = (
    "01_source_inventory/suite_source_bundles/2025朝阳一模.md:688-704;855-856;"
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/gpt_sources/"
    "f5f683a900508fd2_2025朝阳一模细则.md;"
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/renders/"
    "f5f683a900508fd2/page_001.png"
)

EVIDENCE_LEVEL = "正式评分细则原图证据+题干/答案区闭环"
CURRENT_STATUS = "COVERED_AND_REGISTERED_BATCH14_FORMAL_IMAGE_RUBRIC_CONFIRMED"


def backup(path: Path, label: str) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target = path.with_name(f"{path.stem}_backup_before_{label}_{stamp}{path.suffix}")
    shutil.copy2(path, target)
    return target


def repair_matrix() -> tuple[Path, list[str]]:
    backup_path = backup(MATRIX, "chaoyang_q16_formal_image_evidence")
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    changed: list[str] = []
    for row in rows:
        if row.get("matrix_row_id") not in TARGET_MATRIX_IDS:
            continue
        row["细则支持原理"] = SUPPORT_TEXT
        row["证据等级"] = EVIDENCE_LEVEL
        row["是否误放"] = "否"
        row["是否需补厚"] = "否：本行已由朝阳细则渲染页逐点支撑；全书外审仍 real_call_pending。"
        row["当前处理"] = CURRENT_STATUS
        note = row.get("备注", "")
        append = "2026-05-25复核：2025朝阳一模细则PDF无文本层，但缓存渲染page_001可视读取得第16题答案变通说明和分值点；已剔除教师版参考答案作为合格细则证据的表述。"
        row["备注"] = f"{note}；{append}" if note else append
        row["source_artifact"] = SOURCE_ARTIFACT
        changed.append(row["matrix_row_id"])

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return backup_path, changed


def repair_accepted_jsonl() -> tuple[Path, list[int]]:
    backup_path = backup(ACCEPTED, "chaoyang_q16_formal_image_evidence")
    lines = ACCEPTED.read_text(encoding="utf-8").splitlines()
    changed_lines: list[int] = []
    out_lines: list[str] = []
    for idx, line in enumerate(lines, start=1):
        if not line.strip():
            out_lines.append(line)
            continue
        record = json.loads(line)
        if record.get("source_suite") == "2025朝阳一模" and record.get("question_no") == "Q16":
            record["evidence_level"] = EVIDENCE_LEVEL
            record["boundary_note"] = "formal-image-rubric; page_001 visual evidence; external model review still real_call_pending"
            record["source_repair_basis"] = SUPPORT_TEXT + " source: " + SOURCE_ARTIFACT
            for key in ["material_trigger", "why_trigger", "answer_landing", "student_facing_text"]:
                value = record.get(key)
                if isinstance(value, str):
                    value = value.replace("参考答案列", "细则第16题答案变通说明列")
                    value = value.replace("参考答案", "细则第16题答案变通说明")
                    record[key] = value
            changed_lines.append(idx)
        out_lines.append(json.dumps(record, ensure_ascii=False))
    ACCEPTED.write_text("\n".join(out_lines) + "\n", encoding="utf-8", newline="\n")
    return backup_path, changed_lines


def write_report(matrix_backup: Path, accepted_backup: Path, changed_matrix: list[str], changed_lines: list[int]) -> None:
    lines = [
        "# CHAOYANG_2025_Q16_FORMAL_IMAGE_EVIDENCE_REPAIR_20260525",
        "",
        "Status: `FORMAL_IMAGE_RUBRIC_CONFIRMED_FOR_TARGET_ROWS`",
        "",
        "## Scope",
        "",
        "- Matrix rows repaired: `" + ", ".join(changed_matrix) + "`.",
        "- Accepted JSONL lines repaired: `" + ", ".join(str(x) for x in changed_lines) + "`.",
        "- Matrix backup: `" + str(matrix_backup) + "`.",
        "- Accepted JSONL backup: `" + str(accepted_backup) + "`.",
        "",
        "## Source Finding",
        "",
        "- `2025朝阳一模细则.pdf` has no text layer in the source bundle, but the cached rendered image exists at `C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/renders/f5f683a900508fd2/page_001.png`.",
        "- Visual reading of page_001 shows Q16 `答案变通说明` with explicit point allocation: cultural carrier 1 point; cultural resources/correct value guidance 2 points; modern technology and cultural innovation 2 points; era basis and people's needs 2 points; personal-social unity, labor/craft/innovation spirit, life value, local-to-whole 1 point.",
        "- Therefore the three matrix rows are upgraded from mixed teacher-reference evidence to formal image-rubric evidence.",
        "",
        "## Boundary",
        "",
        "- This repair does not close GPTPro or Claude Opus external review; those gates remain `real_call_pending`.",
        "- This repair does not change the global acceptance state.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    matrix_backup, changed_matrix = repair_matrix()
    accepted_backup, changed_lines = repair_accepted_jsonl()
    write_report(matrix_backup, accepted_backup, changed_matrix, changed_lines)
    print(f"MATRIX_CHANGED={','.join(changed_matrix)}")
    print(f"ACCEPTED_JSONL_LINES_CHANGED={','.join(str(x) for x in changed_lines)}")
    print(f"REPORT={REPORT}")


if __name__ == "__main__":
    main()
