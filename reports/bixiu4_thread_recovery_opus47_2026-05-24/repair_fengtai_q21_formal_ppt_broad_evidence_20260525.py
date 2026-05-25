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
REPORT = RECOVERY / "FENGTAI_Q21_FORMAL_PPT_BROAD_EVIDENCE_REPAIR_20260525.md"

SUPPORT = (
    "2026丰台一模Q21源包PPT第61-63页为正式评分材料：Q21（9分）可从党的领导、"
    "唯物辩证法、中国式现代化等角度作答；等级描述要求紧扣问题、综合运用所学、"
    "逻辑严密；典型示例写明“立足实际”“把握经济社会规律”“坚持系统思维、辩证思维”；"
    "第63页进一步列“系统思维（发展观）、辩证思维（矛盾观）、遵循规律”等角度。"
    "本行只登记正式PPT宽角度支持，不冒充逐点评分细则。"
)
EVIDENCE = "正式PPT评分宽角度+等级描述+当前DOCX正文；非逐点细则"
SOURCE = (
    "reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/"
    "01_source_inventory/suite_source_bundles/2026丰台一模.md:737-755;"
    "BATCH16_2026_FENGTAI_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
)


def backup(path: Path, label: str) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target = path.with_name(f"{path.stem}_backup_before_{label}_{stamp}{path.suffix}")
    shutil.copy2(path, target)
    return target


def repair_matrix() -> Path:
    backup_path = backup(MATRIX, "fengtai_q21_formal_ppt_broad")
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    changed = 0
    for row in rows:
        if row.get("matrix_row_id") != "M0913":
            continue
        row["细则支持原理"] = SUPPORT
        row["证据等级"] = EVIDENCE
        row["是否误放"] = "否：正式PPT只支撑宽角度"
        row["是否需补厚"] = "否：本行已限定为正式PPT宽角度登记；全书外审仍 real_call_pending。"
        row["当前处理"] = "REGISTERED_EXISTING_DOCX_BATCH16_FENGTAI_Q21_FORMAL_PPT_BROAD_CONFIRMED"
        row["备注"] = "2026-05-25复核：源包PPT第61-63页提供正式评分宽角度和等级描述；删除“答案版参考答案”作为主要证据的表述。"
        row["source_artifact"] = SOURCE
        changed += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    if changed != 1:
        raise RuntimeError(f"Expected to change 1 matrix row, changed {changed}")
    return backup_path


def repair_accepted() -> tuple[Path, list[int]]:
    backup_path = backup(ACCEPTED, "fengtai_q21_formal_ppt_broad")
    out = []
    changed_lines = []
    for idx, line in enumerate(ACCEPTED.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            out.append(line)
            continue
        record = json.loads(line)
        if record.get("source_suite") == "2026丰台一模" and record.get("question_no") == "Q21":
            record["evidence_level"] = EVIDENCE
            record["boundary_note"] = "formal-PPT-broad-angle; not point-by-point rubric; external review still real_call_pending"
            record["source_repair_basis"] = SUPPORT + " source: " + SOURCE
            changed_lines.append(idx)
        out.append(json.dumps(record, ensure_ascii=False))
    ACCEPTED.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    return backup_path, changed_lines


def write_report(matrix_backup: Path, accepted_backup: Path, changed_lines: list[int]) -> None:
    lines = [
        "# FENGTAI_Q21_FORMAL_PPT_BROAD_EVIDENCE_REPAIR_20260525",
        "",
        "Status: `FORMAL_PPT_BROAD_EVIDENCE_CONFIRMED`",
        "",
        "## Changes",
        "",
        "- Matrix row repaired: `M0913`.",
        "- Accepted JSONL lines repaired: `" + ", ".join(str(x) for x in changed_lines) + "`.",
        "- Matrix backup: `" + str(matrix_backup) + "`.",
        "- Accepted backup: `" + str(accepted_backup) + "`.",
        "",
        "## Evidence",
        "",
        "- Source bundle lines `737-755` show Q21 formal PPT scoring material: broad answer angles, level description, typical example, and explicit angle list including system thinking, dialectical thinking, development view, contradiction view, and following laws.",
        "- The row remains labeled as broad formal PPT evidence, not point-by-point rubric evidence.",
        "",
        "## Boundary",
        "",
        "- This repair removes ordinary answer-version reference wording from the evidence grade.",
        "- It does not close GPTPro or Claude Opus external review.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    matrix_backup = repair_matrix()
    accepted_backup, changed_lines = repair_accepted()
    write_report(matrix_backup, accepted_backup, changed_lines)
    print("MATRIX_CHANGED=M0913")
    print("ACCEPTED_JSONL_LINES_CHANGED=" + ",".join(str(x) for x in changed_lines))
    print(f"REPORT={REPORT}")


if __name__ == "__main__":
    main()
