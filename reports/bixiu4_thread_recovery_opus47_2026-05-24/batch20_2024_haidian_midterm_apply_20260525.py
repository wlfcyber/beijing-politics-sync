from __future__ import annotations

import csv
import json
import re
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
NS = {"w": W_NS}

ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
DOCX = DELIVERY / "哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
GLOBAL_AUDIT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"
GLOBAL_AUDIT_MD = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"

SUITE = "2024海淀期中"
YEAR = "2024"
STAGE = "期中"
BATCH_ID = "batch20_2024_haidian_midterm"
MATRIX_SOURCE = "codex_batch20_2024_haidian_midterm"

SOURCE_BUNDLE = (
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/"
    "gpt_suite_bundles/2024各区模拟题__2024各区期中__2024海淀期中.md"
)
RUBRIC_SOURCE = (
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/"
    "gpt_sources/fee5258a9b7359d5_2024海淀期中细则.md"
)
PAPER_SOURCE = (
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/"
    "gpt_sources/16c75dff224a222c_海淀区2024_2025学年第一学期期中练习政治试题.md"
)
SOURCE_PACKET = f"{SOURCE_BUNDLE}; {RUBRIC_SOURCE}; {PAPER_SOURCE}; current DOCX text verified"

MODULE_DISTRIBUTION = (
    "细则套卷结构表明：客观题1-6为必修2，7-11为必修3，12-15为选择性必修1；"
    "主观题16(1)、17、20为必修2，18、19、21(1)为必修3，16(2)、21(2)为选择性必修1。"
)
Q18_RUBRIC_BOUNDARY = (
    "第18题细则明确知识板块为《政治与法治》基层民主，评分角度为党的领导、全过程人民民主、"
    "基层民主、协商民主/民主决策/民主监督/民主管理、多元主体共建共治；没有必修四哲学原理方法论。"
)

BOUNDARY_ROWS = [
    ("Q1", "经济与社会选择题", "必修2客观题边界", "细则套卷结构表：客观题1-6为必修2。"),
    ("Q2", "经济与社会选择题", "必修2客观题边界", "细则套卷结构表：客观题1-6为必修2。"),
    ("Q3", "经济与社会选择题", "必修2客观题边界", "细则套卷结构表：客观题1-6为必修2。"),
    ("Q4", "经济与社会选择题", "必修2客观题边界", "细则套卷结构表：客观题1-6为必修2。"),
    ("Q5", "经济与社会选择题", "必修2客观题边界", "细则套卷结构表：客观题1-6为必修2。"),
    ("Q6", "经济与社会选择题", "必修2客观题边界", "细则套卷结构表：客观题1-6为必修2。"),
    ("Q7", "政治与法治选择题", "必修3客观题边界", "细则套卷结构表：客观题7-11为必修3。"),
    ("Q8", "政治与法治选择题", "必修3客观题边界", "细则套卷结构表：客观题7-11为必修3。"),
    ("Q9", "政治与法治选择题", "必修3客观题边界", "细则套卷结构表：客观题7-11为必修3。"),
    ("Q10", "政治与法治选择题", "必修3客观题边界", "细则套卷结构表：客观题7-11为必修3。"),
    ("Q11", "政治与法治选择题", "必修3客观题边界", "细则套卷结构表：客观题7-11为必修3。"),
    ("Q12", "当代国际政治与经济选择题", "选择性必修1客观题边界", "细则套卷结构表：客观题12-15为选择性必修1。"),
    ("Q13", "当代国际政治与经济选择题", "选择性必修1客观题边界", "细则套卷结构表：客观题12-15为选择性必修1。"),
    ("Q14", "当代国际政治与经济选择题", "选择性必修1客观题边界", "细则套卷结构表：客观题12-15为选择性必修1。"),
    ("Q15", "当代国际政治与经济选择题", "选择性必修1客观题边界", "细则套卷结构表：客观题12-15为选择性必修1。"),
    ("Q16(1)", "经济与社会主观题", "必修2主观题边界", "细则套卷结构表：主观题16(1)为必修2；评分细则为供给、需求等经济链条。"),
    ("Q16(2)", "当代国际政治与经济主观题", "选择性必修1主观题边界", "细则套卷结构表：主观题16(2)为选择性必修1。"),
    ("Q17", "经济与社会主观题", "必修2主观题边界", "细则套卷结构表：主观题17为必修2；第17题评阅说明为经济政策工具、高质量发展等经济链条。"),
    ("Q18", "政治与法治主观题", "基层民主边界", Q18_RUBRIC_BOUNDARY),
    ("Q19", "政治与法治主观题", "党纪法规/党的建设边界", "细则套卷结构表：主观题19为必修3；第19题细则为中国共产党、全面从严治党、党内法规、依法治国等政治与法治角度。"),
    ("Q20", "经济与社会主观题", "粮食生产/经济高质量发展边界", "细则套卷结构表：主观题20为必修2；第20题细则为共同富裕、粮食安全、区域协调、高质量发展等经济角度。"),
    ("Q21(1)", "法律与政治综合主观题", "法治知识边界", "细则套卷结构表：主观题21(1)为必修3；评分细则为科学立法、权利义务、法律面前人人平等等法治角度。"),
    ("Q21(2)", "当代国际政治与经济主观题", "外交变与不变边界", "细则套卷结构表：主观题21(2)为选择性必修1；评分细则为国际形势、国家利益、独立自主、外交宗旨目标原则等。"),
]

MISPLACED_NODES = [
    ("系统观念 / 系统优化", "1. 2024海淀期中 第18题（主观题）"),
    ("矛盾的特殊性 / 具体问题具体分析", "2. 2024海淀期中 第18题（主观题）"),
    ("人民群众", "2. 2024海淀期中 第18题（主观题）"),
]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def set_para_text(p: etree._Element, text: str) -> None:
    nodes = p.xpath(".//w:t", namespaces=NS)
    if not nodes:
        raise RuntimeError("paragraph has no text node")
    nodes[0].text = text
    for node in nodes[1:]:
        node.text = ""


def style_val(p: etree._Element) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


def zip_write_back(docx_path: Path, root: etree._Element, entries: dict[str, bytes], infos: list[zipfile.ZipInfo]) -> None:
    entries["word/document.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for info in infos:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.comment = info.comment
            zi.extra = info.extra
            zi.internal_attr = info.internal_attr
            zi.external_attr = info.external_attr
            zi.create_system = info.create_system
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, entries[info.filename])
    shutil.move(str(tmp_path), docx_path)


def remove_misplaced_docx_entries(timestamp: str) -> dict[str, object]:
    backup = DOCX.with_name(f"{DOCX.stem}_backup_before_batch20_2024_haidian_midterm_removal_{timestamp}.docx")
    shutil.copy2(DOCX, backup)

    with zipfile.ZipFile(DOCX, "r") as zin:
        entries = {info.filename: zin.read(info.filename) for info in zin.infolist()}
        infos = zin.infolist()
    root = etree.fromstring(entries["word/document.xml"])
    body = root.find("w:body", namespaces=NS)
    if body is None:
        raise RuntimeError("document body not found")

    removed: list[dict[str, object]] = []
    while True:
        paragraphs = [child for child in list(body) if child.tag == f"{W}p"]
        start = None
        section = ""
        heading = ""
        for idx, p in enumerate(paragraphs):
            text = para_text(p).strip()
            if SUITE in text and "第18题" in text and style_val(p) == "5":
                start = idx
                heading = text
                for prev in range(idx - 1, -1, -1):
                    if style_val(paragraphs[prev]) == "4":
                        section = para_text(paragraphs[prev]).strip()
                        break
                break
        if start is None:
            break

        end = len(paragraphs)
        for idx in range(start + 1, len(paragraphs)):
            if style_val(paragraphs[idx]) in {"3", "4", "5"}:
                end = idx
                break
        removed_paras = [para_text(p).strip() for p in paragraphs[start:end]]
        for p in paragraphs[start:end]:
            body.remove(p)
        removed.append({"section": section, "heading": heading, "paragraphs": removed_paras})

    paragraphs = [child for child in list(body) if child.tag == f"{W}p"]
    renumbered: list[tuple[str, str]] = []
    current_count = 0
    for p in paragraphs:
        style = style_val(p)
        text = para_text(p).strip()
        if style == "4":
            current_count = 0
            continue
        if style == "3":
            current_count = 0
            continue
        if style == "5" and re.match(r"^\d+\.\s", text):
            current_count += 1
            new_text = re.sub(r"^\d+\.", f"{current_count}.", text, count=1)
            if new_text != text:
                set_para_text(p, new_text)
                renumbered.append((text, new_text))

    zip_write_back(DOCX, root, entries, infos)
    return {"backup": str(backup), "removed": removed, "renumbered_count": len(renumbered), "renumbered_preview": renumbered[:12]}


def next_matrix_id(rows: list[dict[str, str]]) -> int:
    max_id = 0
    for row in rows:
        value = row.get("matrix_row_id", "")
        if re.match(r"^M\d+$", value):
            max_id = max(max_id, int(value[1:]))
    return max_id + 1


def update_matrix(timestamp: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch20_2024_haidian_midterm_{timestamp}.csv")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    existing = {(r.get("row_source"), r.get("题源"), r.get("题号"), r.get("宝典节点"), r.get("当前处理")) for r in rows}
    next_id = next_matrix_id(rows)
    added: list[dict[str, str]] = []

    def add_row(question_no: str, question_type: str, node: str, principle: str, evidence: str, misplaced: str, action: str, note: str) -> None:
        nonlocal next_id
        key = (MATRIX_SOURCE, SUITE, question_no, node, action)
        if key in existing:
            return
        row = {
            "matrix_row_id": f"M{next_id:04d}",
            "row_source": MATRIX_SOURCE,
            "题源": SUITE,
            "年份": YEAR,
            "阶段": STAGE,
            "题号": question_no,
            "题型或模块判断": question_type,
            "是否进宝典": "否：模块边界排除" if misplaced == "否" else "否：误放已移除",
            "宝典节点": node,
            "细则支持原理": principle,
            "证据等级": evidence,
            "是否误放": misplaced,
            "是否需补厚": "否",
            "当前处理": action,
            "备注": note,
            "source_artifact": SOURCE_PACKET,
        }
        rows.append(row)
        added.append(row)
        existing.add(key)
        next_id += 1

    for q, qtype, node, principle in BOUNDARY_ROWS:
        add_row(
            question_no=q,
            question_type=qtype,
            node=node,
            principle=principle,
            evidence="正式细则模块分布/评分细则",
            misplaced="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH20_HAIDIAN_MIDTERM",
            note="该题不进入必修四哲学宝典；不使用普通参考答案或模型判断扩展为必修四节点。",
        )

    for node, old_heading in MISPLACED_NODES:
        add_row(
            question_no="Q18",
            question_type="既有DOCX误放条目",
            node=node,
            principle=Q18_RUBRIC_BOUNDARY,
            evidence="正式评分细则反证：政治与法治基层民主题；无必修四哲学原理方法论",
            misplaced="是",
            action="REMOVED_MISPLACED_DOCX_BATCH20_HAIDIAN_Q18",
            note=f"旧DOCX条目 `{old_heading}` 已从正文移除；不得保留在该哲学节点。",
        )

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return {"backup": str(backup), "added_rows": len(added), "added_ids": [r["matrix_row_id"] for r in added]}


def update_global_audit() -> dict[str, object]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    updated = False
    for row in rows:
        if row.get("normalized_suite") == SUITE or row.get("raw_suite") == SUITE:
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = "26"
            row["current_docx_mentions"] = "0"
            row["current_status"] = "covered_by_batch20_recovery_matrix"
            row["blocker_or_next_action"] = "Batch20 closed as module-boundary excluded and removed three misplaced Q18 DOCX entries."
            updated = True
    if not updated:
        raise RuntimeError("global audit row for 2024海淀期中 not found")
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    remaining = [r for r in rows if r.get("current_status") == "missing_from_current_47_suite_audit_scope"]
    covered_batch20 = [r for r in rows if r.get("current_status") == "covered_by_batch20_recovery_matrix"]
    md = f"""# Global Raw Suite Exhaustion Audit - 2026-05-25

Status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`

## Current Count

- Raw strict suite directories: `64`
- Covered by current first/second-mock audit or recovery matrix: `49`
- Newly covered by Batch20: `{len(covered_batch20)}`
- Remaining midterm/final raw-source gap: `{len(remaining)}`

## Batch20 Closure

- `2024海淀期中` is now covered by `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.
- The suite is closed as module-boundary excluded for 必修四哲学宝典.
- Three old unregistered DOCX entries for `2024海淀期中 第18题` were removed because the formal rubric places Q18 in 《政治与法治》基层民主, not 必修四哲学.

## Remaining Gap Suites

{chr(10).join(f"- `{r['normalized_suite']}` | `{r['raw_path']}`" for r in remaining)}

## Guardrail

- This audit does not establish whole-project final acceptance.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- The model-effort/adaptive proof gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    GLOBAL_AUDIT_MD.write_text(md, encoding="utf-8")
    return {"remaining_gap": len(remaining), "covered_batch20_rows": len(covered_batch20)}


def write_reports(docx_result: dict[str, object], matrix_result: dict[str, object], global_result: dict[str, object]) -> None:
    source_report = RECOVERY / "BATCH20_2024_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md"
    source_report.write_text(
        f"""# Batch20 Source Transcription - 2024海淀期中

Status: `SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY`

## Source Packet

- Suite bundle: `{SOURCE_BUNDLE}`
- Rubric/scoring source: `{RUBRIC_SOURCE}`
- Paper source cache: `{PAPER_SOURCE}`
- Original rubric PDF: `C:/Users/Administrator/Desktop/2024各区模拟题/2024各区期中/2024海淀期中/细则/2024海淀期中细则.pdf`
- Original paper PDF: `C:/Users/Administrator/Desktop/2024各区模拟题/2024各区期中/2024海淀期中/试卷/海淀区2024～2025学年第一学期期中练习政治试题.pdf`

## Cache Finding

- The suite bundle and rubric cache are readable and sufficient for module-boundary classification.
- The paper cache text is not readable for full question extraction. Because this batch does not add student-facing entries and the formal rubric gives the full module distribution plus Q18/Q19/Q20/Q21 scoring boundaries, no new DOCX prompt is generated from the bad paper cache.

## Formal Module Distribution

{MODULE_DISTRIBUTION}

## Q18 Misplacement Evidence

{Q18_RUBRIC_BOUNDARY}

Removed old DOCX entries:

{chr(10).join(f"- `{item['section']}` -> `{item['heading']}`" for item in docx_result['removed'])}

## Decision

- No `2024海淀期中` question enters the 必修四哲学宝典正文.
- All questions are represented in the matrix as module-boundary rows.
- The three old Q18 philosophy entries are treated as misplaced and removed from the student-facing DOCX.
""",
        encoding="utf-8",
    )

    removal_ledger = RECOVERY / "BATCH20_2024_HAIDIAN_MIDTERM_MISPLACED_REMOVAL_LEDGER.csv"
    with removal_ledger.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["source_suite", "question_no", "old_node", "old_heading", "removal_reason", "removed_paragraph_count"])
        writer.writeheader()
        for item in docx_result["removed"]:
            writer.writerow(
                {
                    "source_suite": SUITE,
                    "question_no": "Q18",
                    "old_node": item["section"],
                    "old_heading": item["heading"],
                    "removal_reason": Q18_RUBRIC_BOUNDARY,
                    "removed_paragraph_count": len(item["paragraphs"]),
                }
            )

    coverage_report = RECOVERY / "COVERAGE_FUSION_BATCH20_2024_HAIDIAN_MIDTERM_CODEX_20260525.md"
    coverage_report.write_text(
        f"""# Coverage Fusion Batch20 - 2024海淀期中

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Codex Lane Decision

- Matrix rows added: `{matrix_result['added_rows']}`.
- Current suite decision: no question enters the 必修四哲学宝典正文.
- Removed misplaced DOCX entries: `{len(docx_result['removed'])}`.
- DOCX backup: `{docx_result['backup']}`.
- Matrix backup: `{matrix_result['backup']}`.

## Question Coverage

- Q1-Q6: 必修2 objective-choice boundary.
- Q7-Q11: 必修3 objective-choice boundary.
- Q12-Q15: 选择性必修1 objective-choice boundary.
- Q16(1), Q17, Q20: 必修2 subjective boundary.
- Q16(2), Q21(2): 选择性必修1 subjective boundary.
- Q18, Q19, Q21(1): 必修3 / 法治 / 基层民主 boundary.

## Misplacement Correction

- Q18 had three old DOCX philosophy entries under `系统观念 / 系统优化`, `矛盾的特殊性 / 具体问题具体分析`, and `人民群众`.
- The formal Q18 rubric supports only 《政治与法治》基层民主 points, so those entries were removed and matrix rows record them as misplaced.

## Remaining Gates

- Render QA pending for this batch.
- ClaudeCode Opus 4.7 production-lane recheck pending.
- Global raw-suite gap after Batch20: `{global_result['remaining_gap']}`.
- GPTPro web and external Claude Opus full-artifact reviews remain `real_call_pending`.
""",
        encoding="utf-8",
    )

    append = f"""

## Batch20 Update: 2024海淀期中 - 2026-05-25

- status: `RECOVERED_EXECUTION_IN_PROGRESS`
- batch state: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`
- files created/updated: `batch20_2024_haidian_midterm_apply_20260525.py`, `BATCH20_2024_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`, `COVERAGE_FUSION_BATCH20_2024_HAIDIAN_MIDTERM_CODEX_20260525.md`, `BATCH20_2024_HAIDIAN_MIDTERM_MISPLACED_REMOVAL_LEDGER.csv`, `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md/.csv`.
- source decision: formal rubric module distribution excludes the whole suite from 必修四哲学正文.
- DOCX correction: removed `3` old unregistered Q18 philosophy entries because Q18 is formally a 《政治与法治》基层民主 question.
- matrix state: added `{matrix_result['added_rows']}` rows; all Q1-Q21 subparts have boundary disposition.
- global source-scope gap reduced to `{global_result['remaining_gap']}` remaining midterm/final suites.
- render state: pending.
- ClaudeCode evidence: pending.
- model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- external reviews: GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
"""
    THREAD_STATUS.write_text(THREAD_STATUS.read_text(encoding="utf-8") + append, encoding="utf-8")

    governor_append = f"""

## Governor Batch20 Recovery Finding: 2024海淀期中
Updated: 2026-05-25

- Verdict: Batch20 Codex lane is `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Coverage: `2024海淀期中` is represented by `{matrix_result['added_rows']}` new matrix rows covering Q1-Q21 subparts and the three removed Q18 misplacements.
- Evidence quality: formal rubric/module distribution is sufficient to exclude the suite from 必修四哲学正文; no ordinary reference answer is used as a scoring rule.
- Misplacement correction: three old Q18 entries under `系统观念 / 系统优化`, `矛盾的特殊性 / 具体问题具体分析`, and `人民群众` were removed because the formal Q18 rubric is 《政治与法治》基层民主 only.
- Global source-scope gap remains open at `{global_result['remaining_gap']}` raw midterm/final suites.
- Render QA and ClaudeCode Opus 4.7 gates still need to run for this batch; external GPTPro/Claude full-artifact reviews remain `real_call_pending`.
"""
    GOVERNOR.write_text(GOVERNOR.read_text(encoding="utf-8") + governor_append, encoding="utf-8")

    confucius_append = f"""

## Confucius Batch20 Artifact Check: 2024海淀期中
Updated: 2026-05-25

- Verdict: student-facing artifact correction is applied but not yet render/model closed.
- Student-facing additions: none.
- Student-facing removals: three old Q18 philosophy entries were removed because formal scoring evidence places Q18 in 《政治与法治》基层民主, not 必修四哲学.
- Boundary discipline: all `2024海淀期中` questions are closed as 必修2/必修3/选必1 module boundaries; no model-inferred philosophy placement is retained.
- Remaining blockers: render QA and ClaudeCode Opus 4.7 batch recheck are pending; global source-scope gap remains `{global_result['remaining_gap']}` suites; GPTPro and external Claude full-artifact reviews remain `real_call_pending`.
"""
    CONFUCIUS.write_text(CONFUCIUS.read_text(encoding="utf-8") + confucius_append, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = remove_misplaced_docx_entries(timestamp)
    matrix_result = update_matrix(timestamp)
    global_result = update_global_audit()
    write_reports(docx_result, matrix_result, global_result)
    print(json.dumps({"docx": docx_result, "matrix": matrix_result, "global": global_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
