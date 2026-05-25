from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = RECOVERY / "TONGZHOU_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "TONGZHOU_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026通州一模"
DESKTOP = Path.home() / "Desktop"
SOURCE_DIR = DESKTOP / "2026各区模拟题" / "2026各区一模" / "2026通州一模"
PAPER_PDF = SOURCE_DIR / "2026北京通州高三一模政治.pdf"
RUBRIC_PDF = SOURCE_DIR / "26 通州一模评标.pdf"
SOURCE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / "2026通州一模.md"
PAPER_RENDER_DIR = RECOVERY / "tongzhou_yimo_source_pages_20260525"
RUBRIC_RENDER_DIR = RECOVERY / "tongzhou_yimo_rubric_pages_20260525"


def update_row(row: dict[str, str], **values: str) -> None:
    row.update(values)


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_tongzhou_yimo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    source = f"{RUBRIC_PDF}; {SOURCE_BUNDLE}; {PAPER_PDF}; {PAPER_RENDER_DIR / 'page_01.png'}; {PAPER_RENDER_DIR / 'page_05.png'}; {PAPER_RENDER_DIR / 'page_08.png'}; {RUBRIC_RENDER_DIR / 'page_01.png'}"
    q18_support = (
        "通州一模评标第9-10页已明确第18题：坚持对立统一及材料分析各1分，辩证否定观及材料分析各1分；"
        "当前DOCX已在矛盾就是对立统一、辩证否定/守正创新两处覆盖第18题。"
    )
    choice_missing = "源卷图像可见选择题题面，但本套当前可用评标文件未给出第一部分官方答案键；选择题不能凭题面词或模型推断入正文。"
    exclude = {
        "M0633": ("Q1", "党史/中国特色社会主义选择题", "中国共产党领导/民族复兴/党史", "源卷第1页第1题围绕《中国共产党简史》、党的领导和民族复兴；" + choice_missing),
        "M0634": ("Q2", "文化生活选择题", "文化自信/中式生活方式/文化传播", "源卷第1页第2题围绕“成为中国人”、中式生活体验和文化吸引力；" + choice_missing),
        "M0635": ("Q3", "法治/政治与哲学交叉选择题暂不入正文", "耕地保护立法/社会意识/上层建筑/科学立法", "源卷第1页第3题虽出现社会意识、上层建筑和辩证否定等选项词，但缺官方答案键，不能确认正确项链条；本批不写入正文，等待后续官方选择题答案键补证。"),
        "M0636": ("Q17", "经济与社会/选择性必修三逻辑与思维主观题", "人工智能/经济高质量发展/辩证思维", "评标第4-8页第17题第(1)问为经济高质量发展，第(2)问明确要求运用《逻辑与思维》辩证思维；不进入当前必修四哲学正文。"),
    }

    touched: list[str] = []
    for row in rows:
        if row.get("题源") != SUITE:
            continue
        row_id = row.get("matrix_row_id", "")
        if row_id in {"M0167", "M0231"}:
            update_row(
                row,
                题型或模块判断="源文件已回补；Q18现有正文覆盖",
                是否进宝典="是：Q18已进入当前DOCX/PDF正文；本行关闭旧OCR失败/候选记录",
                宝典节点="矛盾就是对立统一；辩证否定 / 守正创新",
                细则支持原理=q18_support,
                证据等级="正式评标细则-当前DOCX覆盖",
                是否误放="否",
                是否需补厚="否",
                当前处理="SOURCE_REVIEW_CLOSED_CURRENT_DOCX_COVERAGE_TONGZHOU_2026_YIMO_Q18",
                备注="旧OCR失败状态已由源卷/评标渲染和当前正文覆盖修复；不再保留为待核候选。",
                source_artifact=source,
            )
        elif row_id == "M0637":
            update_row(
                row,
                题号="Qunknown",
                题型或模块判断="套卷抽取误并行风险记录",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="2026通州一模：Q18已由正式评标细则和当前DOCX两处正文覆盖；Q1-Q3因缺第一部分官方答案键不入正文；Q17按经济与逻辑思维边界排除；Q16政治与法治、Q20法律、Q21哲学综合已有各自边界不由本行承接。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_TONGZHOU_2026_YIMO_REPAIR",
                备注="套卷级长摘录不替代逐题行；本批已用源卷图像页和评标文本逐题承接。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id == "M0857":
            update_row(
                row,
                题型或模块判断="套卷级覆盖口径，不替代逐题细则核验",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="2026通州一模本批完成Q18现有正文覆盖核验、Q1-Q3选择题答案键缺失边界记录、Q17模块边界排除；套卷级记录只作为闭合摘要。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_TONGZHOU_2026_YIMO_REPAIR",
                备注="套卷级记录不替代逐题矩阵；无DOCX内容变更，渲染不需要重跑。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id in exclude:
            q, qtype, node, support = exclude[row_id]
            update_row(
                row,
                题号=q,
                题型或模块判断=qtype,
                是否进宝典="否：模块边界排除/选择题答案键缺失",
                宝典节点=node,
                细则支持原理=support,
                证据等级="源卷图像+正式评标文本-边界核定（非正文证据）",
                是否误放="否",
                是否需补厚="否",
                当前处理="SOURCE_REVIEW_CLOSED_TONGZHOU_2026_YIMO_NO_BODY_INSERT",
                备注="不把选择题题面词、经济、政治、文化或选必三逻辑与思维内容偷换为当前哲学正文；缺答案键的选择题等待后续补证。",
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
            "paper_page_01": str(PAPER_RENDER_DIR / "page_01.png"),
            "paper_page_05": str(PAPER_RENDER_DIR / "page_05.png"),
            "paper_page_08": str(PAPER_RENDER_DIR / "page_08.png"),
            "rubric_page_01": str(RUBRIC_RENDER_DIR / "page_01.png"),
        },
        "render_status": "NO_DOCX_CHANGE_RENDER_NOT_REQUIRED",
        "model_gate_status": {
            "claude_web_app_full_artifact_review": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web_full_artifact_review": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    md = f"""# TONGZHOU_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `MATRIX_REPAIRED_NO_DOCX_CHANGE`

- Suite: `{SUITE}`.
- Timestamp: `{ts}`.
- Formal scoring source: `{RUBRIC_PDF}`.
- Paper source: `{PAPER_PDF}`.
- Source page renders used: `{PAPER_RENDER_DIR / 'page_01.png'}`, `{PAPER_RENDER_DIR / 'page_05.png'}`, `{PAPER_RENDER_DIR / 'page_08.png'}`.
- Matrix backup: `{matrix_info['matrix_backup']}`.

## Matrix Closure

- Q18 closed against current-DOCX two-node coverage and formal scoring-rubric support.
- Q1-Q3 are not imported because the available scoring file has no first-part official answer key; Q3 remains a source-boundary row rather than a model-inferred philosophy chain.
- Q17 is excluded as economics plus `逻辑与思维`辩证思维 boundary.
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
