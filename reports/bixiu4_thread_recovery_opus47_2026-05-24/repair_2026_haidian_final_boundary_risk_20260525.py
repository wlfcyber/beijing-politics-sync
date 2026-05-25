from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = RECOVERY / "HAIDIAN_2026_FINAL_BOUNDARY_RISK_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "HAIDIAN_2026_FINAL_BOUNDARY_RISK_REPAIR_20260525.json"

SUITE = "2026海淀期末"

BOUNDARY_ROWS = {
    "M1364": "Q5文化选择题：文博会、数字技术与文化传播，属于文化模块；不进入当前哲学正文。",
    "M1365": "Q6法律选择题：商业秘密保护和侵权责任，属于法律与生活。",
    "M1366": "Q7法律选择题：交通事故责任与民事侵权问题，属于法律与生活。",
    "M1367": "Q8法律选择题：婚姻登记条例、行政服务和个人信息，属于法律与生活。",
    "M1368": "Q9法律选择题：企业用工、劳动合同和劳动争议，属于法律与生活。",
    "M1369": "Q10法律/市场规则选择题：诚信表述处在消费者权益和市场规则法治语境中，不转写为哲学价值观正文条。",
    "M1370": "Q11逻辑与思维选择题：形式逻辑判断和谓项周延，属于选必三边界。",
    "M1371": "Q12逻辑与思维选择题：三段论推理规则，属于选必三边界。",
    "M1372": "Q13逻辑与思维选择题：探究方案与推理方法，属于选必三边界。",
    "M1373": "Q14逻辑与思维选择题：研究结论不具必然性，属于逻辑思维/科学思维判断。",
    "M1374": "Q15逻辑与思维/公共服务选择题：综合思维、问题导向和公共服务精准对接，归入选必三边界。",
}


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_haidian_final_boundary_risk_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    touched = []
    for row in rows:
        row_id = row.get("matrix_row_id", "")
        if row.get("题源") != SUITE or row_id not in BOUNDARY_ROWS:
            continue
        row["证据等级"] = "正式教师版答案键+题面-模块边界（非评分细则）"
        row["细则支持原理"] = BOUNDARY_ROWS[row_id] + " 本行只证明模块边界排除，不作为主观题评分细则或正文原理支撑。"
        row["是否误放"] = "否"
        row["是否需补厚"] = "否"
        row["备注"] = "已回源核定为模块边界排除；普通答案键不冒充评分细则，也不支撑新增正文。"
        touched.append(row_id)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_row_ids": touched}


def write_report(ts: str, info: dict[str, object]) -> None:
    data = {
        "timestamp": ts,
        "suite": SUITE,
        "status": "MATRIX_BOUNDARY_RISK_REPAIRED_NO_DOCX_CHANGE",
        "matrix": info,
        "render_status": "NO_DOCX_CHANGE_RENDER_NOT_REQUIRED",
        "boundary": "Rows M1364-M1374 remain excluded from the current philosophy body; evidence level now explicitly distinguishes formal teacher answer-key boundary proof from scoring-rubric support.",
        "model_gate_status": {
            "claude_web_app_full_artifact_review": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web_full_artifact_review": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    md = f"""# HAIDIAN_2026_FINAL_BOUNDARY_RISK_REPAIR_20260525

Status: `MATRIX_BOUNDARY_RISK_REPAIRED_NO_DOCX_CHANGE`

- Suite: `{SUITE}`.
- Timestamp: `{ts}`.
- Updated rows: `{', '.join(info['updated_row_ids'])}`.
- Matrix backup: `{info['matrix_backup']}`.
- DOCX/PDF: no content change; render not required for this matrix-only boundary repair.

## Boundary Decision

- Rows M1364-M1374 remain excluded from the current philosophy body.
- Evidence level was normalized to `正式教师版答案键+题面-模块边界（非评分细则）`.
- This does not upgrade ordinary answer keys into scoring rubrics; it only records that the teacher answer key and question stem are sufficient to prove module-boundary exclusion.

## Open Gates

- GPTPro web full artifact review remains `real_call_pending`.
- Claude web/app full artifact review through direct `https://claude.ai` remains `real_call_pending`.
- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 final GitHub upload remains deferred.
"""
    REPORT_MD.write_text(md, encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    info = update_matrix(ts)
    write_report(ts, info)
    print(json.dumps(info, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
