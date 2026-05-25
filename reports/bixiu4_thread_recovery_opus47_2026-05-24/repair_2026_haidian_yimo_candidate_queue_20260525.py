from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = RECOVERY / "HAIDIAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "HAIDIAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026海淀一模"
DESKTOP = Path.home() / "Desktop"
SOURCE_DIR = DESKTOP / "2026各区模拟题" / "2026各区一模" / "2026海淀一模"
PAPER_PDF = SOURCE_DIR / "2026海淀一模 试卷扫描版_去水印.pdf"
RUBRIC_PDF = SOURCE_DIR / "26海淀一模政治评分标准.pdf"
SOURCE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / "2026海淀一模.md"
SOURCE_RENDER_DIR = RECOVERY / "haidian_yimo_source_pages_20260525"


def update_row(row: dict[str, str], **values: str) -> None:
    row.update(values)


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_haidian_yimo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    source = f"{RUBRIC_PDF}; {SOURCE_BUNDLE}; {PAPER_PDF}; {SOURCE_RENDER_DIR / 'page_04.png'}; {SOURCE_RENDER_DIR / 'page_05.png'}"
    q16_support = (
        "26海淀一模政治评分标准第1页第16题写明可从发展的观点、社会存在与社会意识、价值观、文化的功能等角度作答；"
        "源卷第5页第16题要求运用《哲学与文化》认识人工智能时代人文学科价值。当前DOCX已在物质决定意识、意识能动作用、发展观点、社会存在与社会意识、价值观导向、价值判断与价值选择六处覆盖。"
    )
    exclude = {
        "M0592": ("Q15", "当代国际政治与经济选择题", "国际组织/国际协定/全球治理", "源卷第4页第15题围绕《海洋生物多样性协定》、联合国框架、国际合作和全球安全，官方答案C；属于当代国际政治与经济。"),
        "M0594": ("Q17", "选择性必修三逻辑与思维主观题", "调查问卷逻辑错误/科学思维/辩证思维", "评分标准第2-3页第17题限定逻辑错误、科学思维、逻辑思维规则、辩证思维和调研方法，属于选必三逻辑与思维边界。"),
        "M0595": ("Q18", "经济与社会/法律与生活主观题", "服务性消费/隐私权/消费者权益", "评分标准第3-4页第18题第(1)(2)问为经济消费结构和服务业，第(3)问为隐私权、消费者权益和诚信法治语境，不进入当前哲学正文。"),
        "M0596": ("Q19", "政治与法治主观题", "备案审查/公平竞争审查/法治政府", "评分标准第5页第19题围绕全国人大常委会备案审查、规范性文件和公平竞争审查条例，属于政治与法治。"),
        "M0597": ("Q20", "当代国际政治与经济主观题", "制度型开放/全球治理/国际标准", "评分标准第6页第20题围绕高水平对外开放、国际标准、全球治理和新发展格局，属于国政经边界。"),
    }

    touched: list[str] = []
    for row in rows:
        if row.get("题源") != SUITE:
            continue
        row_id = row.get("matrix_row_id", "")
        if row_id in {"M0163", "M0593"}:
            update_row(
                row,
                题型或模块判断="必修四哲学主观题现有正文覆盖",
                是否进宝典="是：已进入当前DOCX/PDF正文，本批关闭弱证据重复候选",
                宝典节点="物质决定意识；主观能动性 / 意识的能动作用；发展的观点；社会存在与社会意识；价值观的导向作用；价值判断与价值选择",
                细则支持原理=q16_support,
                证据等级="正式评分标准-综合角度+当前DOCX覆盖（非逐点细则）",
                是否误放="否",
                是否需补厚="否：当前正文已覆盖，本批改正证据等级并关闭重复候选",
                当前处理="SOURCE_REVIEW_CLOSED_CURRENT_DOCX_COVERAGE_HAIDIAN_2026_YIMO_Q16",
                备注="普通参考答案弱候选已由正式评分标准和当前DOCX六处覆盖承接；本行不再作为独立待补正文。",
                source_artifact=source,
            )
        elif row_id == "M0598":
            update_row(
                row,
                题号="Qunknown",
                题型或模块判断="套卷抽取误并行风险记录",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="2026海淀一模：Q16已由正式评分标准和当前DOCX六处正文覆盖；Q15/Q17/Q18/Q19/Q20分别按国政经、逻辑、经济/法律、政治法治、国政经边界排除。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_HAIDIAN_2026_YIMO_REPAIR",
                备注="套卷级长摘录不替代逐题行；本批已用源卷图像页和评分标准逐题承接。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id == "M0851":
            update_row(
                row,
                题型或模块判断="套卷级覆盖口径，不替代逐题细则核验",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="2026海淀一模本批完成Q16现有正文覆盖核验，Q15/Q17/Q18/Q19/Q20边界排除；套卷级记录只作为闭合摘要。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_HAIDIAN_2026_YIMO_REPAIR",
                备注="套卷级记录不替代逐题矩阵；无DOCX内容变更，渲染不需要重跑。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id in exclude:
            q, qtype, node, support = exclude[row_id]
            update_row(
                row,
                题号=q,
                题型或模块判断=qtype,
                是否进宝典="否：模块边界排除",
                宝典节点=node,
                细则支持原理=support,
                证据等级="正式评分标准/源卷图像-模块边界",
                是否误放="否",
                是否需补厚="否",
                当前处理="MODULE_BOUNDARY_EXCLUDED_HAIDIAN_2026_YIMO_SOURCE_REVIEW",
                备注="不把国政经、逻辑与思维、经济、法律或政治法治内容偷换为当前哲学正文。",
                source_artifact=source,
            )
        if row_id:
            touched.append(row_id)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_row_ids": sorted(set(touched))}


def write_report(ts: str, matrix_info: dict[str, object]) -> None:
    data = {
        "timestamp": ts,
        "suite": SUITE,
        "status": "MATRIX_REPAIRED_NO_DOCX_CHANGE",
        "matrix": matrix_info,
        "sources": {
            "rubric_pdf": str(RUBRIC_PDF),
            "paper_pdf": str(PAPER_PDF),
            "source_bundle": str(SOURCE_BUNDLE),
            "source_page_04": str(SOURCE_RENDER_DIR / "page_04.png"),
            "source_page_05": str(SOURCE_RENDER_DIR / "page_05.png"),
        },
        "render_status": "NO_DOCX_CHANGE_RENDER_NOT_REQUIRED",
        "model_gate_status": {
            "claude_web_app_full_artifact_review": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web_full_artifact_review": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    md = f"""# HAIDIAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `MATRIX_REPAIRED_NO_DOCX_CHANGE`

- Suite: `{SUITE}`.
- Timestamp: `{ts}`.
- Formal scoring source: `{RUBRIC_PDF}`.
- Paper source: `{PAPER_PDF}`.
- Source page renders used: `{SOURCE_RENDER_DIR / 'page_04.png'}`, `{SOURCE_RENDER_DIR / 'page_05.png'}`.
- Matrix backup: `{matrix_info['matrix_backup']}`.

## Matrix Closure

- Q16 closed against current-DOCX six-node coverage and formal scoring-standard support.
- Q15, Q17, Q18, Q19, and Q20 are module-boundary exclusions.
- Qunknown and suite-level rows are closed as summaries only; they do not replace row-level evidence.
- No DOCX content changed in this repair, so render was not rerun.

## Open Gates

- GPTPro web full artifact review remains `real_call_pending`.
- Claude web/app full artifact review through direct `https://claude.ai` remains `real_call_pending`.
- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 final GitHub upload remains deferred.
"""
    REPORT_MD.write_text(md, encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    matrix_info = update_matrix(ts)
    write_report(ts, matrix_info)
    print(json.dumps(matrix_info, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
