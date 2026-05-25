from __future__ import annotations

import csv
import json
import shutil
import tempfile
import zipfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"
NS = {"w": W_NS}

RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
REPORT_MD = RECOVERY / "FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026房山二模"
YEAR = "2026"
STAGE = "二模"
ROW_SOURCE = "codex_recovery_20260525_fangshan_2026_ermo_repair"

DESKTOP = Path.home() / "Desktop"
ANSWER_DOCX = next(p for p in DESKTOP.rglob("*.docx") if SUITE in str(p))
PAPER_PDF = next(p for p in DESKTOP.rglob("*.pdf") if SUITE in str(p))
SOURCE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / f"{SUITE}.md"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q18(2)",
        "heading_suffix": "2026房山二模 第18题第（2）问（主观题）",
        "material_trigger": "正式细则写明：OPC的出现是对传统一人公司这一旧矛盾统一体的否定，实现“单人成军”全新创业范式，是联系的环节、发展的环节；OPC的发展要求创业者坚持扬弃，肯定并保留数字员工的强大功能，同时针对法律风险加以改造。",
        "question_prompt": "第18题第（2）问要求从OPC的出现和发展理解其新创业范式及风险应对，评分细则按“联系、发展、扬弃”和“否定分析/肯定分析”赋分。",
        "why_trigger": "看到“旧矛盾统一体的否定”“联系的环节”“发展的环节”“坚持扬弃”“保留强大功能又针对法律风险改造”，应定位辩证否定观：新事物不是简单抛弃旧事物，而是在否定中保留合理因素、克服消极因素，实现发展。",
        "answer_landing": "OPC的出现否定了传统单人公司依赖个人单打独斗的旧形态，形成“单人成军”的新创业范式；这种否定是联系和发展的环节。OPC继续发展时，既要肯定数字员工带来的效率和能力提升，又要对商业诋毁、秘密泄露、侵权等风险进行规范改造，把风险治理包含进新事物发展过程，这就是坚持扬弃。",
        "evidence_level": "正式评分细则-逐点赋分",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "heading_suffix": "2026房山二模 第21题（主观题）",
        "material_trigger": "第21题正式细则围绕“新征程是新的长征”，列出“坚持人民至上/人民群众是历史的主体”，并要求围绕以中国式现代化全面推进中华民族伟大复兴展开综合论述。",
        "question_prompt": "第21题要求综合运用所学，谈谈对“新征程是新的长征”的理解。",
        "why_trigger": "看到“以中国式现代化全面推进中华民族伟大复兴”“走好新的长征路”“坚持人民至上”，应想到人民群众是社会历史的主体：新的长征路不是少数人完成的工程，而是依靠人民、为了人民推进民族复兴的历史实践。",
        "answer_landing": "可从人民群众角度作答：新征程是新的长征，意味着推进中国式现代化和民族复兴必须坚持人民至上，尊重人民主体地位，依靠人民群众的实践创造，把人民对美好生活的向往作为奋斗目标。这样才能把新的长征路走稳、走实。",
        "evidence_level": "正式评分细则-综合论述角度+等级赋分（非逐点细则）",
    },
    {
        "canonical_node": "矛盾的普遍性",
        "question_no": "Q21",
        "heading_suffix": "2026房山二模 第21题（主观题）",
        "material_trigger": "第21题正式细则在“走好新的长征路”的角度中列出“矛盾普遍性，承认分析解决矛盾/伟大斗争（四个伟大）”，并将其纳入综合论述可用角度。",
        "question_prompt": "第21题要求综合运用所学，谈谈对“新征程是新的长征”的理解。",
        "why_trigger": "看到“新的长征”与“伟大斗争”，应想到矛盾具有普遍性：推进现代化强国建设会不断遇到风险、挑战和复杂矛盾，必须承认矛盾、分析矛盾、解决矛盾，而不是回避矛盾。",
        "answer_landing": "可从矛盾普遍性角度作答：新的长征路上必然会遇到发展不平衡、改革攻坚、科技创新、生态文明、国际环境等矛盾和挑战。要坚持问题导向，承认并分析矛盾，通过伟大斗争和系统实践解决矛盾，推动中国式现代化不断前进。",
        "evidence_level": "正式评分细则-综合论述角度+等级赋分（非逐点细则）",
    },
]


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def p_style(p) -> str:
    node = p.find("./w:pPr/w:pStyle", namespaces=NS)
    return node.get(W + "val") if node is not None else ""


def is_section(p) -> bool:
    return p_style(p) in {"Heading2", "2", "4"}


def is_entry(p) -> bool:
    return p_style(p) in {"Heading3", "3", "5"}


def make_run(text: str, label: bool = False):
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set(XML + "space", "preserve")
    t.text = text
    return r


def set_plain(p, text: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(text))


def set_label(p, label: str, rest: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(label, True))
    p.append(make_run(" " + rest))
    ppr = p.find("./w:pPr", namespaces=NS)
    if ppr is None:
        ppr = etree.Element(W + "pPr")
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def find_section(paras, heading: str) -> tuple[int, int]:
    start = next((i for i, p in enumerate(paras) if is_section(p) and para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if is_section(paras[i])), len(paras))
    return start, end


def templates(paras, start: int, end: int):
    heading_template = next((paras[i] for i in range(start + 1, end) if is_entry(paras[i])), None)
    label_template = next((paras[i] for i in range(start + 1, end) if para_text(paras[i]).strip().startswith("【")), None)
    blank_template = next((paras[i] for i in range(start + 1, end) if not para_text(paras[i]).strip()), None)
    if heading_template is None or label_template is None:
        raise RuntimeError(f"templates not found in {para_text(paras[start])}")
    return heading_template, label_template, blank_template


def next_num(paras, start: int, end: int) -> int:
    nums = []
    for i in range(start + 1, end):
        if is_entry(paras[i]):
            head = para_text(paras[i]).strip().split(".", 1)[0]
            if head.isdigit():
                nums.append(int(head))
    return (max(nums) if nums else 0) + 1


def add_entry(body, entry: dict[str, str]) -> str | None:
    if any(entry["heading_suffix"] in para_text(p) for p in body if p.tag == W + "p"):
        return None
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    heading_template, label_template, blank_template = templates(paras, start, end)
    heading_text = f"{next_num(paras, start, end)}. {entry['heading_suffix']}"
    insert_at = list(body).index(paras[end]) if end < len(paras) else len(body)
    h = deepcopy(heading_template)
    set_plain(h, heading_text)
    body.insert(insert_at, h)
    insert_at += 1
    for label, key in LABELS:
        p = deepcopy(label_template)
        set_label(p, label, entry[key])
        body.insert(insert_at, p)
        insert_at += 1
    if blank_template is not None:
        body.insert(insert_at, deepcopy(blank_template))
    return heading_text


def edit_docx(ts: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_fangshan_ermo_repair_{ts}.docx")
    shutil.copy2(docx, backup)
    inserted: list[str] = []
    skipped: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        xml_path = temp / "word" / "document.xml"
        tree = etree.parse(str(xml_path))
        body = tree.getroot().find("w:body", namespaces=NS)
        if body is None:
            raise RuntimeError("missing body")
        for entry in INSERT_ENTRIES:
            heading = add_entry(body, entry)
            if heading is None:
                skipped.append(entry["heading_suffix"])
            else:
                inserted.append(heading)
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, inserted_headings: list[str]) -> dict[str, object]:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_fangshan_ermo_repair_{ts}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for entry, heading in zip(INSERT_ENTRIES, inserted_headings, strict=False):
        clean = heading.split(". ", 1)[1]
        key = (SUITE, entry["question_no"], clean)
        if key in existing:
            continue
        row = {field: "" for field in fieldnames}
        row.update({"canonical_node": entry["canonical_node"], "source_suite": SUITE, "question_no": entry["question_no"], "inserted_heading": clean})
        rows.append(row)
        added.append(row)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger": str(LEDGER), "ledger_backup": str(backup), "added_rows": added}


def in_body_update(q: str, node: str, support: str, evidence: str, source: str) -> dict[str, str]:
    return {
        "题型或模块判断": "必修四哲学主观题",
        "是否进宝典": "是：本批新增进入当前DOCX/PDF正文",
        "宝典节点": node,
        "细则支持原理": support,
        "证据等级": evidence,
        "是否误放": "否",
        "是否需补厚": "否：已补入对应节点；证据边界已明示",
        "当前处理": "DOCX_INSERTED_FANGSHAN_2026_ERMO_RENDER_PENDING",
        "备注": "本批回源核对正式答案/评分细则；综合论述角度不冒充逐点细则。",
        "source_artifact": source,
        "题号": q,
    }


def excluded_update(q: str, qtype: str, support: str, source: str) -> dict[str, str]:
    return {
        "题号": q,
        "题型或模块判断": qtype,
        "是否进宝典": "否：模块边界排除",
        "宝典节点": "不进入当前哲学宝典",
        "细则支持原理": support,
        "证据等级": "正式评分细则-模块边界",
        "是否误放": "否",
        "是否需补厚": "否",
        "当前处理": "MODULE_BOUNDARY_EXCLUDED_FANGSHAN_2026_ERMO_SOURCE_REVIEW",
        "备注": "不把法律、经济、国际政治经济或文化线内容偷换为当前哲学正文。",
        "source_artifact": source,
    }


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_fangshan_ermo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    source = f"{ANSWER_DOCX}; {SOURCE_BUNDLE}; {PAPER_PDF}"
    updates = {
        "M0111": in_body_update("Q18(2)", "辩证否定 / 守正创新", INSERT_ENTRIES[0]["material_trigger"], INSERT_ENTRIES[0]["evidence_level"], source),
        "M0157": {
            "题型或模块判断": "Q16重复候选汇总",
            "是否进宝典": "是：已由当前DOCX覆盖",
            "宝典节点": "尊重规律与能动性/系统观念/量变质变",
            "细则支持原理": "Q16正式评分细则列正确发挥主观能动性、系统观念、矛盾、中华文明特征等角度；当前DOCX已有Q16三处哲学正文条目覆盖。",
            "证据等级": "正式评分细则+当前DOCX正文覆盖",
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_EXISTING_BODY_FANGSHAN_2026_ERMO",
            "备注": "关闭早期生产线候选，不重复插入Q16。",
            "source_artifact": source,
        },
        "M0158": {
            "题型或模块判断": "Q18(2)重复候选",
            "是否进宝典": "是：已由本批新增DOCX覆盖",
            "宝典节点": "辩证否定 / 守正创新",
            "细则支持原理": INSERT_ENTRIES[0]["material_trigger"],
            "证据等级": INSERT_ENTRIES[0]["evidence_level"],
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_M0111_FANGSHAN_2026_ERMO",
            "备注": "与M0111同源；不重复插入。",
            "source_artifact": source,
        },
        "M0237": {
            "题型或模块判断": "Q16重复候选汇总",
            "是否进宝典": "是：已由当前DOCX覆盖",
            "宝典节点": "尊重规律与能动性/系统观念/量变质变",
            "细则支持原理": "Q16正式评分细则列正确发挥主观能动性、系统观念、矛盾、中华文明特征等角度；当前DOCX已有Q16三处哲学正文条目覆盖。",
            "证据等级": "正式评分细则+当前DOCX正文覆盖",
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_EXISTING_BODY_FANGSHAN_2026_ERMO",
            "备注": "关闭早期生产线候选，不重复插入Q16。",
            "source_artifact": source,
        },
        "M0238": {
            "题型或模块判断": "Q18(2)重复候选",
            "是否进宝典": "是：已由本批新增DOCX覆盖",
            "宝典节点": "辩证否定 / 守正创新",
            "细则支持原理": INSERT_ENTRIES[0]["material_trigger"],
            "证据等级": INSERT_ENTRIES[0]["evidence_level"],
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_M0111_FANGSHAN_2026_ERMO",
            "备注": "与M0111同源；不重复插入。",
            "source_artifact": source,
        },
        "M0691": {
            "题型或模块判断": "Q16重复候选汇总",
            "是否进宝典": "是：已由当前DOCX覆盖",
            "宝典节点": "尊重规律与能动性/系统观念/量变质变",
            "细则支持原理": "Q16正式评分细则列正确发挥主观能动性、系统观念、矛盾、中华文明特征等角度；当前DOCX已有Q16三处哲学正文条目覆盖。",
            "证据等级": "正式评分细则+当前DOCX正文覆盖",
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_EXISTING_BODY_FANGSHAN_2026_ERMO",
            "备注": "关闭早期生产线候选，不重复插入Q16。",
            "source_artifact": source,
        },
        "M0692": excluded_update("Q17", "法律/政治法治主观题", "Q17正式细则按涉外法律法规、涉外司法、多元纠纷解决和涉外法治建设评分。", source),
        "M0693": {
            "题号": "Q18(2)",
            "题型或模块判断": "Q18混合题中的哲学分问",
            "是否进宝典": "是：已由本批新增DOCX覆盖",
            "宝典节点": "辩证否定 / 守正创新",
            "细则支持原理": INSERT_ENTRIES[0]["material_trigger"],
            "证据等级": INSERT_ENTRIES[0]["evidence_level"],
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_M0111_FANGSHAN_2026_ERMO",
            "备注": "Q18(1)为法律边界分问；Q18(2)为必修四哲学分问，已新增正文。",
            "source_artifact": source,
        },
        "M0694": excluded_update("Q19", "经济与社会主观题", "Q19正式细则按社会主义市场经济体制、宏观调控、供给需求、扩大内需评分。", source),
        "M0695": excluded_update("Q20", "当代国际政治与经济主观题", "Q20正式细则按经济全球化、世界多极化、全球治理观、数据要素流动评分。", source),
        "M0696": in_body_update("Q21", "人民群众", INSERT_ENTRIES[1]["material_trigger"], INSERT_ENTRIES[1]["evidence_level"], source),
        "M0697": in_body_update("Q21", "矛盾的普遍性", INSERT_ENTRIES[2]["material_trigger"], INSERT_ENTRIES[2]["evidence_level"], source),
        "M0846": {
            "题型或模块判断": "套卷级闭合记录",
            "是否进宝典": "套卷逐题风险已回源闭合",
            "宝典节点": "SUITE_LEVEL_SUMMARY",
            "细则支持原理": "2026房山二模：Q16已有正文覆盖，Q18(2)和Q21哲学角度本批补入，Q17/Q19/Q20边界排除，Q18(1)法律边界不入哲学正文。",
            "证据等级": "逐题回源闭合汇总",
            "是否误放": "不适用",
            "是否需补厚": "否：本批已逐题闭合风险行；外部模型门仍按总账记录。",
            "当前处理": "SUITE_LEVEL_CLOSED_BY_FANGSHAN_2026_ERMO_REPAIR_RENDER_PENDING",
            "备注": "套卷级记录不替代逐题行；本批已补足逐题记录。",
            "source_artifact": f"{REPORT_MD}; {REPORT_JSON}",
        },
    }
    touched = []
    for row in rows:
        row_id = row.get("matrix_row_id", "")
        if row.get("题源") == SUITE and row_id in updates:
            row.update(updates[row_id])
            touched.append(row_id)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_row_ids": touched}


def write_report(ts: str, docx_result: dict[str, object], ledger_result: dict[str, object], matrix_result: dict[str, object]) -> None:
    manifest = {
        "timestamp": ts,
        "suite": SUITE,
        "docx": docx_result,
        "ledger": ledger_result,
        "matrix": matrix_result,
        "sources": {"answer_docx": str(ANSWER_DOCX), "paper_pdf": str(PAPER_PDF), "source_bundle": str(SOURCE_BUNDLE)},
        "render_status": "RENDER_PENDING",
        "model_gate_status": {
            "claude_web_app": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525",
        "",
        "Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`",
        "",
        f"- Suite: `{SUITE}`.",
        f"- Timestamp: `{ts}`.",
        f"- Answer/rubric source: `{ANSWER_DOCX}`.",
        f"- Paper source: `{PAPER_PDF}`.",
        f"- Source bundle: `{SOURCE_BUNDLE}`.",
        "",
        "## DOCX Inserts",
        "",
    ]
    for heading in docx_result["inserted_headings"]:
        lines.append(f"- `{heading}`")
    lines.extend(
        [
            "",
            "## Matrix Closure",
            "",
            "- Q16 duplicate candidates closed against current-DOCX coverage and formal scoring support.",
            "- Q18(2) inserted as a formal scoring-rule chain for dialectical negation/sublation.",
            "- Q21 inserted under `人民群众` and `矛盾的普遍性` using formal comprehensive-question angle evidence and level descriptors.",
            "- Q17/Q19/Q20 and Q18(1) remain module-boundary exclusions.",
            f"- Matrix backup: `{matrix_result['matrix_backup']}`.",
            f"- Ledger backup: `{ledger_result['ledger_backup']}`.",
            f"- DOCX backup: `{docx_result['docx_backup']}`.",
            "",
            "## Open Gates",
            "",
            "- DOCX/PDF render QA is pending for this batch.",
            "- Claude web/app external review remains `real_call_pending`.",
            "- ClaudeCode Opus 4.7 max-effort confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until a real capture proves it.",
            "- GPTPro web review remains `real_call_pending`.",
        ]
    )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = edit_docx(ts)
    ledger_result = update_ledger(ts, docx_result["inserted_headings"])
    matrix_result = update_matrix(ts)
    write_report(ts, docx_result, ledger_result, matrix_result)
    print(json.dumps({"docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
