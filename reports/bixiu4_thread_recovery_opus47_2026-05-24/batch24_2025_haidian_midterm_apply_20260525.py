from __future__ import annotations

import csv
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
GLOBAL_AUDIT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"
GLOBAL_AUDIT_MD = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH24_2025_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH24_2025_HAIDIAN_MIDTERM_CODEX_20260525.md"

PREPROCESSED = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区期末__2025海淀期中.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "7bbd92bd3b93e531_2025海淀期中细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "b452d8b4e21b94be_2024北京海淀高三_上_期中政治_教师版.md"

SUITE = "2025海淀期中"
YEAR = "2025"
STAGE = "期中"
BATCH_ID = "batch24_2025_haidian_midterm"
MATRIX_SOURCE = "codex_batch24_2025_haidian_midterm"
SOURCE_PACKET = f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; current DOCX text verified: no existing {SUITE} headings before Batch24"

BOUNDARY_ROWS = [
    ("Q1", "经济与社会选择题", "国有企业/民营企业/商业航天产业链", "答案C；考查多种所有制经济、企业创新主体与产业链协同，不是必修四哲学联系观。", "细则答案+教师版题面"),
    ("Q2", "经济与社会选择题", "市场需求/差异化产品/消费者性价比", "答案A；考查消费者需求和企业差异化供给，属经济与社会。", "细则答案+教师版题面"),
    ("Q3", "经济与社会选择题", "二次元经济/消费新空间", "答案C；虽出现创新、因地制宜等词，但题干主线为消费市场和地区经济增长，非必修四哲学方法论。", "细则答案+教师版题面"),
    ("Q4", "经济与社会选择题", "市场准入制度/非公有制经济", "答案D；考查放宽服务业准入限制与行业活力，属经济与社会。", "细则答案+教师版题面"),
    ("Q5", "经济与社会选择题", "医保个人账户/社会保障", "答案B；考查医保服务便利和社会保障基金共济使用。", "细则答案+教师版题面"),
    ("Q6", "经济与社会选择题", "养老助餐/民营企业/公共服务供给", "答案A；考查科技赋能养老服务和民营企业市场机遇。", "细则答案+教师版题面"),
    ("Q7", "政治与法治选择题", "党建引领/党员先锋模范作用/社会治理", "答案B；考查基层党组织和党员先锋模范作用，不把“新力量”泛化为人民群众历史观。", "细则答案+教师版题面"),
    ("Q8", "政治与法治选择题", "全国人大常委会执法检查/人大监督", "答案D；考查人大监督和法律贯彻落实。", "细则答案+教师版题面"),
    ("Q9", "政治与法治/民族政策选择题", "对口支援西藏/民族团结/生存权发展权", "答案D；考查民族团结、民族地区发展与人权保障，非哲学历史观正文。", "细则答案+教师版题面"),
    ("Q10", "政治与法治/法律规范选择题", "网络暴力治理/多方主体/特殊群体权益", "答案A；考查网络暴力信息治理法规和公平正义，属法治治理边界。", "细则答案+教师版题面"),
    ("Q11", "政治与法治选择题", "基层治理法治化/协商民主", "答案B；考查司法局法律指引、纠纷处理和基层治理法治化。", "细则答案+教师版题面"),
    ("Q12", "政治与法治选择题", "总体国家安全观/国家安全利益", "答案B；考查国家安全观，不进入必修四哲学正文。", "细则答案+教师版题面"),
    ("Q13", "当代国际政治与经济选择题", "入境游/公共外交/经济动能", "答案A；考查开放政策、公共外交和经济动能。", "细则答案+教师版题面"),
    ("Q14", "当代国际政治与经济选择题", "中国特色大国外交/人类命运共同体/一个中国原则", "答案C；考查国际政治时事解读。", "细则答案+教师版题面"),
    ("Q15", "当代国际政治与经济选择题", "APEC能源合作/国际能源合作", "答案D；考查国际组织和中国能源合作，不进入哲学正文。", "细则答案+教师版题面"),
    ("Q16(1)", "经济与社会主观题", "咖啡市场前景/生产技术/产品质量/消费方式/市场需求", "题干明确限定《经济与社会》；细则要求从生产技术、产品质量、消费方式、市场需求等角度回答。", "细则+题面模块限定"),
    ("Q16(2)", "经济与社会/当代国际经济主观题", "企业出海/经营战略/海外市场/经济全球化/全球治理", "细则要求客观看待出海机遇挑战、制定经营战略、调查海外市场、提升自主创新能力、利用国际国内两种资源两个市场和参与全球经济治理；不作为哲学原理。", "细则+题面模块限定"),
    ("Q17", "经济与社会主观题", "瞪羚企业/财政补贴/税收优惠/融资支持/人才引进", "题干明确运用《经济与社会》知识；细则按经营成本、创新活力、融资成本、人才研发能力给分。", "细则+题面模块限定"),
    ("Q18", "政治与法治主观题", "基层民主/党的领导/基层群众自治/协商共治", "题干要求分析“五民工作法”对发展基层民主的启示；细则按党的领导、基层群众自治、多方参与治理给分。", "细则+题面模块限定"),
    ("Q19", "政治与法治主观题", "党纪处分条例/全面从严治党/党内法规/依法治国", "细则虽写“实事求是、与时俱进”，但处于中国共产党始终走在时代前列和党纪法规修订的政治法治语境，不作为必修四哲学正文。", "细则+题面模块限定"),
    ("Q20", "经济与社会主观题", "粮食产销区省际横向利益补偿/共同富裕/粮食安全/区域协调发展", "题干明确运用《经济与社会》知识；细则按农民收入、粮食安全、区域协调、乡村振兴和高质量发展给分。", "细则+题面模块限定"),
    ("Q21(1)", "法律与生活/法治知识主观题", "婚姻法/民法典/良法之治/权利义务相对应", "题干明确要求运用法治知识；细则中的“符合国情和实际、符合社会发展的需求”是良法评价标准，不作为一切从实际出发或发展观哲学正文。", "细则+题面模块限定"),
    ("Q21(2)", "当代国际政治与经济主观题", "新中国外交的变与不变/外交思想/独立自主和平外交政策", "题干明确限定《当代国际政治与经济》；细则按时代背景、综合国力、外交指导思想和外交基本原则给分。", "细则+题面模块限定"),
]


def current_docx_mentions() -> int:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    import zipfile
    from lxml import etree

    with zipfile.ZipFile(docs[0], "r") as zf:
        root = etree.fromstring(zf.read("word/document.xml"))
    return "".join(t.text or "" for t in root.xpath("//w:t", namespaces={"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"})).count(SUITE)


def update_matrix(timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch24_2025_haidian_midterm_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    rows = [r for r in rows if not (r.get("题源") == SUITE and r.get("row_source") == MATRIX_SOURCE)]
    max_id = 0
    for row in rows:
        match = re.match(r"M(\d+)", row.get("matrix_row_id", ""))
        if match:
            max_id = max(max_id, int(match.group(1)))
    new_rows = []
    next_id = max_id + 1
    for q, qtype, node, support, evidence in BOUNDARY_ROWS:
        new_rows.append(
            {
                "matrix_row_id": f"M{next_id:04d}",
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": q,
                "题型或模块判断": qtype,
                "是否进宝典": "否：模块边界排除",
                "宝典节点": node,
                "细则支持原理": support,
                "证据等级": evidence,
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH24_HAIDIAN_MIDTERM",
                "备注": "本题或本小问不含可进必修四哲学宝典正文的细则支持原理；不把普通政治/经济/法律/国际政治语言偷换为哲学原理。",
                "source_artifact": SOURCE_PACKET,
            }
        )
        next_id += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    return {
        "matrix_rows_total": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "body_rows": 0,
        "boundary_rows": len(new_rows),
        "matrix_backup": str(backup),
    }


def update_global_audit(docx_mentions: int, batch_rows: int) -> dict[str, int]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    updated = False
    for row in rows:
        if row.get("normalized_suite") == SUITE or row.get("raw_suite") == SUITE:
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = str(batch_rows)
            row["current_docx_mentions"] = str(docx_mentions)
            row["current_status"] = "covered_by_batch24_boundary_matrix_no_body"
            row["blocker_or_next_action"] = "Batch24 added question-level boundary rows; no rubric-supported philosophy-body placement found; render not required because DOCX body unchanged; ClaudeCode Opus 4.7 recheck pending."
            updated = True
    if not updated:
        raise RuntimeError(f"global audit row for {SUITE} not found")
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    missing = [r for r in rows if r.get("current_status") == "missing_from_current_47_suite_audit_scope"]
    covered = [r for r in rows if r.get("current_status") != "missing_from_current_47_suite_audit_scope"]
    missing_table = "\n".join(
        f"| {r['normalized_suite']} | {r['stage_dir']} | {r['current_status']} | {r['blocker_or_next_action']} |"
        for r in missing
    )
    GLOBAL_AUDIT_MD.write_text(
        f"""# Global Raw Suite Exhaustion Audit 2026-05-25

status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`

## Summary

- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(rows)}`
- current covered by first/second mock audit or recovery matrix: `{len(covered)}`
- remaining midterm/final raw suites outside current coverage: `{len(missing)}`
- current recovery matrix rows for `{SUITE}`: `{batch_rows}`
- current DOCX mentions for `{SUITE}`: `{docx_mentions}`

## Batch24 Finding

`{SUITE}` is now covered by question-level recovery matrix rows. No question or subquestion has a rubric-supported 必修四哲学正文 placement. All 23 rows are explicit module-boundary exclusions.

## Remaining Gap Suites

| normalized_suite | stage_dir | status | next action |
|---|---|---|---|
{missing_table}

## Guardrail

- This audit does not establish whole-project final acceptance.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- The model-effort/adaptive proof gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
""",
        encoding="utf-8",
    )
    return {"covered": len(covered), "missing": len(missing)}


def write_reports(docx_mentions: int, matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    boundary_lines = "\n".join(f"- {q}: {qtype} -> {node}" for q, qtype, node, _support, _evidence in BOUNDARY_ROWS)
    source_paths = "\n".join(
        [
            f"- suite bundle: `{GPT_BUNDLE}`",
            f"- rubric/answer source: `{RUBRIC_SOURCE}`",
            f"- teacher-version paper: `{TEACHER_SOURCE}`",
            "- raw rubric: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025海淀期中\\细则\\2025海淀期中细则.docx`",
            "- raw teacher paper: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025海淀期中\\试卷\\2024北京海淀高三（上）期中政治（教师版）.pdf`",
        ]
    )
    SOURCE_TRANSCRIPTION.write_text(
        f"""# Batch24 Source Transcription - 2025海淀期中

Status: `SOURCE_REVIEWED_BATCH24`

## Source Files

{source_paths}

## Source Facts

- Answer key: `1C 2A 3C 4D 5B 6A 7B 8D 9D 10A 11B 12B 13A 14C 15D`.
- The scoring source is a DOCX answer/rubric file with direct text extraction.
- Current DOCX had `{docx_mentions}` existing `{SUITE}` mentions before Batch24 registration, so no inherited philosophy-body entry existed to register.
- Q16(1), Q16(2), Q17, and Q20 are 《经济与社会》 or economic/global-economy questions.
- Q18 and Q19 are 《政治与法治》 questions.
- Q21(1) is a legal/fazhi question; wording about “符合国情和实际、符合社会发展的需求” is a good-law evaluation standard, not a philosophy scoring point.
- Q21(2) is 《当代国际政治与经济》.
- Choice questions Q1-Q15 are economics, politics/law, national-security, international-politics, or public-governance rows; none has a rubric-supported 必修四 philosophy body placement.

## Boundary Rows

{boundary_lines}

## Guardrail

- No DOCX body insertion was made.
- No ordinary reference answer is treated as a philosophy scoring rubric.
- Political, economic, legal, and international-politics concepts are not converted into philosophy nodes merely because words like “实际”, “发展”, “创新”, or “公平正义” appear.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
""",
        encoding="utf-8",
    )
    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch24 - 2025海淀期中

Status: `LOCAL_APPLIED_NO_BODY_RENDER_NOT_NEEDED_MODEL_PENDING`

## Execution Summary

- Current thread remains the recovered execution owner; old failed thread context is not used as execution evidence.
- No DOCX body insertion was made because no question/subquestion had a scoring-source-backed 必修四 philosophy placement.
- Current DOCX mentions for `{SUITE}`: `{docx_mentions}`.
- Matrix rows added for `{SUITE}`: `{matrix_result['batch_rows']}` total, `0` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Ledger rows added: `0`; accepted JSONL records added: `0`.
- Global raw-suite remaining gap after Batch24: `{global_result['missing']}`.

## Placement Verdict

- All Q1-Q15 choice questions are objective/module-boundary rows.
- Q16(1), Q16(2), Q17, Q20 are economic rows.
- Q18 and Q19 are political/legal-governance rows.
- Q21(1) is legal/fazhi; its “实际/发展” wording is not imported as philosophy.
- Q21(2) is contemporary international politics/economics.

## Render / Format Gate

- `NO_DOCX_CHANGE_RENDER_NOT_NEEDED`: current DOCX/PDF body was not modified in this batch.
- Latest full render evidence remains Batch23: `254/254` pages/images, labels `2375/2375`, visible Batch23 suite headings `21/21`.

## Remaining Gates

- ClaudeCode Opus 4.7 recheck is pending for Batch24.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until independently confirmed.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""",
        encoding="utf-8",
    )
    format_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch24 Render/Format QA: 2025海淀期中"
    if marker in format_text:
        format_text = format_text[: format_text.index(marker)]
    format_text += f"""

## Batch24 Render/Format QA: 2025海淀期中
Updated: 2026-05-25

- Render status: `NO_DOCX_CHANGE_RENDER_NOT_NEEDED`.
- Reason: Batch24 found no rubric-supported philosophy-body placement, so DOCX/PDF content was not modified.
- Latest full render evidence remains Batch23: `word_render_qa_20260525_batch23_word/render_manifest.json`.
- No new font/style surface was introduced by Batch24.
"""
    FORMAT_QA.write_text(format_text, encoding="utf-8")
    append_block = f"""

## Batch24 Local Application: 2025海淀期中
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_NO_BODY_RENDER_NOT_NEEDED_MODEL_PENDING`.
- DOCX body insertions: `0`.
- Current DOCX mentions for `{SUITE}`: `{docx_mentions}`.
- Matrix rows added: `{matrix_result['batch_rows']}` (`0` body / `{matrix_result['boundary_rows']}` boundary).
- Global remaining raw midterm/final gap: `{global_result['missing']}`.
- Model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; GPTPro/Claude external full-artifact review remain `real_call_pending`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch24 Local Application: 2025海淀期中"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8")
    model_text = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH24_HAIDIAN_MIDTERM_RECHECK"
    if marker in model_text:
        model_text = model_text[: model_text.index(marker)]
    model_text += """

## CLAUDECODE_BATCH24_HAIDIAN_MIDTERM_RECHECK

status: `real_call_pending`

- No ClaudeCode Opus 4.7 max/adaptive recheck has been completed for Batch24 yet.
- No Sonnet/Haiku/model-unknown result is accepted as qualified evidence.
- Until runtime evidence proves the required lane, the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    MODEL_LEDGER.write_text(model_text, encoding="utf-8")


def main() -> int:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_mentions = current_docx_mentions()
    matrix_result = update_matrix(timestamp)
    global_result = update_global_audit(docx_mentions, int(matrix_result["batch_rows"]))
    write_reports(docx_mentions, matrix_result, global_result)
    print(json.dumps({"docx_mentions": docx_mentions, "matrix": matrix_result, "global": global_result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
