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
REPORT = RECOVERY / "THICKNESS_FLAG_REPAIR_TONGZHOU_SHUNYI_20260525.md"

FIXES = {
    "M0023": {
        "accepted_line": 23,
        "misplaced": "否",
        "need_thick": "否：本行已按通州评标细则逐行重引源证；全书厚度外审仍 real_call_pending。",
        "status": "KEEP_IN_BODY_LOCAL_THICKNESS_PASS_EXTERNAL_OPEN",
        "support": "通州一模评标Q18：评分细则写“坚持对立统一（1分），隆福寺在保护古都肌理的同时融入现代科技，实现二者共生共荣（1分）”；本节点只收哲学给分点。",
        "note": "通州Q18评标细则明确对立统一及材料分析各1分，正文已有材料触发、为什么、卷面落地三层。",
        "source_artifact": "04_fusion_audit\\student_patch_entries.accepted.jsonl:23; 01_source_inventory\\suite_source_bundles\\2026通州一模.md:169-178",
    },
    "M0024": {
        "accepted_line": 24,
        "misplaced": "否",
        "need_thick": "否：本行已按通州评标细则逐行重引源证；全书厚度外审仍 real_call_pending。",
        "status": "KEEP_IN_BODY_LOCAL_THICKNESS_PASS_EXTERNAL_OPEN",
        "support": "通州一模评标Q18：评分细则写“辩证否定观（1分），既保留历史记忆，又注入时代元素，实现传统与现代融合（1分）”；“双创”只作文化表达边界，不单独立哲学节点。",
        "note": "通州Q18评标细则明确辩证否定观及材料分析各1分，正文已有材料触发、为什么、卷面落地三层。",
        "source_artifact": "04_fusion_audit\\student_patch_entries.accepted.jsonl:24; 01_source_inventory\\suite_source_bundles\\2026通州一模.md:169-178",
    },
    "M0030": {
        "accepted_line": 30,
        "misplaced": "否",
        "need_thick": "否：本行已按顺义阅卷版逐行重引源证；全书厚度外审仍 real_call_pending。",
        "status": "KEEP_IN_BODY_LOCAL_THICKNESS_PASS_EXTERNAL_OPEN",
        "support": "顺义二模评标Q16阅卷版：角度3写“价值引领，义利兼顾”，并明确“价值观对人们认识世界和改造世界的活动具有重要导向作用”，要求拒绝低俗化、流量化倾向，聚焦时代正能量。",
        "note": "顺义Q16阅卷版明确价值观导向、反低俗化/流量化、社会效益优先，正文已有材料触发、为什么、卷面落地三层。",
        "source_artifact": "04_fusion_audit\\student_patch_entries.accepted.jsonl:30; 01_source_inventory\\suite_source_bundles\\2026顺义二模.md:55-62",
    },
}


def backup(path: Path, timestamp: str) -> Path:
    out = path.with_name(f"{path.stem}_backup_before_thickness_flag_repair_{timestamp}{path.suffix}")
    shutil.copy2(path, out)
    return out


def repair_matrix(timestamp: str) -> tuple[Path, list[str]]:
    backup_path = backup(MATRIX, timestamp)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    support_key = headers[9]
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
        row[support_key] = fix["support"]
        row[misplaced_key] = fix["misplaced"]
        row[need_key] = fix["need_thick"]
        row[status_key] = fix["status"]
        row[note_key] = fix["note"]
        row[source_key] = fix["source_artifact"]
        repaired.append(row_id)

    if set(repaired) != set(FIXES):
        raise RuntimeError(f"Matrix repair incomplete: {repaired}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    return backup_path, repaired


def repair_accepted(timestamp: str) -> tuple[Path, list[int]]:
    backup_path = backup(ACCEPTED, timestamp)
    lines = ACCEPTED.read_text(encoding="utf-8").splitlines()
    line_to_fix = {fix["accepted_line"]: fix for fix in FIXES.values()}
    repaired: list[int] = []
    out_lines: list[str] = []
    for idx, line in enumerate(lines, start=1):
        if not line.strip():
            out_lines.append(line)
            continue
        obj = json.loads(line)
        fix = line_to_fix.get(idx)
        if fix:
            obj["source_repair_basis"] = fix["support"]
            obj["thickness_recheck_status"] = "local_row_thickness_pass_external_review_open"
            repaired.append(idx)
        out_lines.append(json.dumps(obj, ensure_ascii=False))

    if set(repaired) != {fix["accepted_line"] for fix in FIXES.values()}:
        raise RuntimeError(f"Accepted JSONL repair incomplete: {repaired}")

    ACCEPTED.write_text("\n".join(out_lines) + "\n", encoding="utf-8", newline="\n")
    return backup_path, repaired


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    matrix_backup, matrix_rows = repair_matrix(timestamp)
    accepted_backup, accepted_lines = repair_accepted(timestamp)
    REPORT.write_text(
        "\n".join(
            [
                "# THICKNESS_FLAG_REPAIR_TONGZHOU_SHUNYI_20260525",
                "",
                "Status: `LOCAL_ROW_THICKNESS_FLAGS_CLEARED_EXTERNAL_REVIEW_OPEN`",
                "",
                f"- Timestamp: `{timestamp}`.",
                f"- Matrix backup: `{matrix_backup}`.",
                f"- Accepted JSONL backup: `{accepted_backup}`.",
                f"- Matrix rows repaired: `{', '.join(matrix_rows)}`.",
                f"- Accepted JSONL lines repaired: `{', '.join(str(i) for i in accepted_lines)}`.",
                "- Tongzhou Q18 source: `01_source_inventory/suite_source_bundles/2026通州一模.md:169-178`.",
                "- Shunyi Q16 source: `01_source_inventory/suite_source_bundles/2026顺义二模.md:55-62`.",
                "- Action: converted stale row-level `need thickening` flags into local row-level pass with explicit source support.",
                "- Boundary: this does not close the full-book thickness gate; GPTPro and Claude Opus web/app review remain `real_call_pending`.",
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
