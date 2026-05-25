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
REPORT_MD = RECOVERY / "SHUNYI_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "SHUNYI_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026顺义一模"
YEAR = "2026"
STAGE = "一模"

DESKTOP = Path.home() / "Desktop"
SOURCE_DIR = DESKTOP / "2026各区模拟题" / "2026各区一模" / "2026顺义一模"
PAPER_PDF = SOURCE_DIR / "2026顺义一模.pdf"
RUBRIC_PPT = SOURCE_DIR / "2026年顺义一模  细则.pptx"
SOURCE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / "2026顺义一模.md"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q2",
        "heading_suffix": "2026顺义一模 第2题（选择题）",
        "material_trigger": "题干写多台北京题材新戏大戏上演，其中杂技剧场《屋顶上的北平》用现代舞台语言演绎古都风云；官方答案键第2题为C，对应正确项明确写出“在内容与形式的统一中体现意识的能动性”。",
        "question_prompt": "从北京题材剧目和现代舞台表达看，为什么第2题应抓住意识能动作用？本题正确答案为C。",
        "why_trigger": "看到“用现代舞台语言演绎古都风云”“内容与形式的统一”“体现意识的能动性”，应想到意识不是被动摹写对象，而是能动地选择、加工和创造性表达历史文化材料。",
        "answer_landing": "本题应选C。杂技剧场《屋顶上的北平》把古都历史内容转化为现代舞台表达，说明意识活动具有目的性、自觉选择性和能动创造性，能够在内容与形式的统一中再现、加工并表达客观材料。A混淆个性与共性的包含关系，B把文化呈现说成重构历史，D外延关系判断不当，均不进入正文链条。",
        "evidence_level": "选择题官方答案键+题干正确项链条；选择题证据边界已明示，非主观题评分细则",
    },
    {
        "canonical_node": "认识发展原理",
        "question_no": "Q5",
        "heading_suffix": "2026顺义一模 第5题（选择题）",
        "material_trigger": "题干写顺义区某中学校园博物馆、馆藏资源、体验活动以及师生在展品前“触摸历史温度、聆听无声之教”；官方答案键第5题为D，对应正确项明确写出“师生在感觉、知觉、表象的基础上认识事物的本质和规律”。",
        "question_prompt": "从校园博物馆体验活动看，为什么第5题应落到从感性认识到理性认识的认识发展链条？本题正确答案为D。",
        "why_trigger": "看到“静默的展品”“触摸历史温度”“感受中华优秀传统文化魅力”以及正确项中的“感觉、知觉、表象”和“认识事物的本质和规律”，应想到认识由感性材料积累上升到把握本质和规律。",
        "answer_landing": "本题应选D。校园博物馆的展品和体验活动为师生提供感性材料，师生通过感觉、知觉、表象形成对历史文化的直接感受，并在此基础上进一步把握中华优秀传统文化的本质、价值和规律性认识。A把比喻式表达误判为本质属性判断，B把活动组织误判为发散思维，C关系判断分析不当，均不进入正文链条。",
        "evidence_level": "选择题官方答案键+题干正确项链条；选择题证据边界已明示，非主观题评分细则",
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_shunyi_yimo_repair_{ts}.docx")
    shutil.copy2(docx, backup)
    inserted: list[dict[str, str]] = []
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
                inserted.append({"question_no": entry["question_no"], "heading": heading, "node": entry["canonical_node"]})
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, inserted: list[dict[str, str]]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_shunyi_yimo_repair_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for item in inserted:
        clean = item["heading"].split(". ", 1)[1]
        key = (SUITE, item["question_no"], clean)
        if key in existing:
            continue
        row = {field: "" for field in fieldnames}
        row.update(
            {
                "canonical_node": item["node"],
                "source_suite": SUITE,
                "question_no": item["question_no"],
                "inserted_heading": clean,
            }
        )
        rows.append(row)
        added.append(row)
    if rows:
        with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
    return {"ledger": str(LEDGER), "ledger_backup": str(backup) if backup else None, "added_rows": added}


def update_row(row: dict[str, str], **values: str) -> None:
    row.update(values)


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_shunyi_yimo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    source = f"{RUBRIC_PPT}; {SOURCE_BUNDLE}; {PAPER_PDF}"
    touched: list[str] = []
    q21_support = (
        "顺义一模第21题正式评分PPT第10-11页写明哲学角度：客观性2分可用主观能动性和客观规律相结合、社会存在和社会意识、实践和认识等；"
        "辩证性2分可用主次矛盾和矛盾主次方面辩证关系、两点论和重点论、矛盾对立统一、整体部分/系统优化、前进性曲折性、量变质变、内外因；"
        "价值性2分可用人民群众是历史创造者、群众观点路线、价值判断价值选择遵循社会发展规律并站在最广大人民立场。当前DOCX已在相应节点多处覆盖第21题。"
    )
    q16_support = (
        "顺义一模第16题正式评分PPT第2页写明可选知识：量质变、适度原则、矛盾转化；联系观、系统优化；文化功能、价值观导向等，并按防范治理逻辑赋分。当前DOCX已有第16题对应条目。"
    )

    exclude = {
        "M0657": ("Q1", "政治/中国特色社会主义选择题", "不进入当前哲学宝典", "第1题官方答案B，围绕中国共产党领导推动中国社会发展进步的根本保证；不把Q21评分PPT中的哲学词误嫁接到Q1。"),
        "M0659": ("Q3", "选择性必修三逻辑与思维选择题", "不进入当前哲学宝典", "第3题官方答案C，核心为整体性与独立性、动态性与静态性以及分析与综合；作为逻辑与思维/辩证思维考查，不作当前必修四哲学正文新增。"),
        "M0661": ("Q17", "政治与法治主观题", "不进入当前哲学宝典", "第17题评分PPT按党的领导、民主集中制、制度优势、全过程人民民主、法治政府、协同共治等赋分，属于政治与法治。"),
        "M0662": ("Q20", "当代国际政治与经济主观题", "不进入当前哲学宝典", "第20题评分PPT明确要求运用《当代国际政治与经济》知识，围绕南南合作、共同利益、经济全球化、和平与发展等赋分。"),
    }

    for row in rows:
        if row.get("题源") != SUITE:
            continue
        row_id = row.get("matrix_row_id", "")
        if row_id == "M0658":
            update_row(
                row,
                题型或模块判断="必修四哲学选择题",
                是否进宝典="是：本批新增进入当前DOCX/PDF正文",
                宝典节点=INSERT_ENTRIES[0]["canonical_node"],
                细则支持原理=INSERT_ENTRIES[0]["material_trigger"],
                证据等级=INSERT_ENTRIES[0]["evidence_level"],
                是否误放="否",
                是否需补厚="否：已补入对应节点；选择题证据边界已明示",
                当前处理="DOCX_INSERTED_SHUNYI_2026_YIMO_RENDER_PENDING",
                备注="第2题只把正确项C的意识能动性链条入正文；不把选择题答案键冒充主观题评分细则。",
                source_artifact=source,
            )
        elif row_id == "M0660":
            update_row(
                row,
                题型或模块判断="必修四认识论选择题",
                是否进宝典="是：本批新增进入当前DOCX/PDF正文",
                宝典节点=INSERT_ENTRIES[1]["canonical_node"],
                细则支持原理=INSERT_ENTRIES[1]["material_trigger"],
                证据等级=INSERT_ENTRIES[1]["evidence_level"],
                是否误放="否",
                是否需补厚="否：已补入对应节点；选择题证据边界已明示",
                当前处理="DOCX_INSERTED_SHUNYI_2026_YIMO_RENDER_PENDING",
                备注="第5题只把正确项D的感性认识到理性认识链条入正文；不把选择题答案键冒充主观题评分细则。",
                source_artifact=source,
            )
        elif row_id in {"M0078", "M0079", "M0080", "M0171", "M0233", "M0663"}:
            node = row.get("宝典节点", "")
            if row_id == "M0079":
                node = "矛盾的主要方面和次要方面 / 两点论与重点论 / 主要矛盾和次要矛盾（评分PPT综合角度）"
            elif row_id in {"M0171", "M0233", "M0663"}:
                node = "尊重客观规律与发挥主观能动性相结合；两点论与重点论；人民群众/价值判断价值选择"
            update_row(
                row,
                题型或模块判断="必修四哲学主观题现有正文覆盖",
                是否进宝典="是：已进入当前DOCX/PDF正文，本批不重复插入",
                宝典节点=node,
                细则支持原理=q21_support,
                证据等级="正式评分PPT-哲学角度+等级赋分（非逐点细则）",
                是否误放="否",
                是否需补厚="否：当前正文已覆盖，本批改正证据等级并关闭重复候选",
                当前处理="SOURCE_REVIEW_CLOSED_CURRENT_DOCX_COVERAGE_SHUNYI_2026_YIMO",
                备注="第21题已有当前DOCX多节点覆盖；本批只修正普通参考答案冒充细则的问题，并记录正式评分PPT边界。",
                source_artifact=source,
            )
        elif row_id == "M0664":
            update_row(
                row,
                题号="Qunknown",
                题型或模块判断="套卷抽取误并行风险记录",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="顺义一模：Q2/Q5选择题链条本批补入；Q16/Q21已有当前DOCX正文覆盖并有正式评分PPT支持；Q1/Q3/Q17/Q20等风险行按模块边界关闭。该套卷级长摘录不替代逐题行。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_SHUNYI_2026_YIMO_REPAIR_RENDER_PENDING",
                备注="套卷级误并行长摘录已由逐题行承接；不得再作为独立入正文证据。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id in {"M0805", "M0856"}:
            update_row(
                row,
                题型或模块判断="套卷级覆盖口径，不替代逐题细则核验",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="顺义一模本批完成Q2/Q5新增、Q16/Q21现有正文覆盖核验、非本模块行边界排除；套卷级记录只作为闭合摘要。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_SHUNYI_2026_YIMO_REPAIR_RENDER_PENDING",
                备注="套卷级记录不替代逐题矩阵；本批渲染后再标记RENDER_PASS。",
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
                证据等级="正式答案键/评分PPT-模块边界",
                是否误放="否",
                是否需补厚="否",
                当前处理="MODULE_BOUNDARY_EXCLUDED_SHUNYI_2026_YIMO_SOURCE_REVIEW",
                备注="不把政治、法治、国政经、逻辑与思维或其他非当前哲学正文内容偷换为本宝典正文。",
                source_artifact=source,
            )
        elif row_id == "M0078":
            pass
        if row_id:
            touched.append(row_id)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_row_ids": sorted(set(touched))}


def write_report(ts: str, docx_info: dict[str, object], ledger_info: dict[str, object], matrix_info: dict[str, object]) -> None:
    data = {
        "timestamp": ts,
        "suite": SUITE,
        "docx": docx_info,
        "ledger": ledger_info,
        "matrix": matrix_info,
        "sources": {
            "rubric_ppt": str(RUBRIC_PPT),
            "paper_pdf": str(PAPER_PDF),
            "source_bundle": str(SOURCE_BUNDLE),
        },
        "render_status": "RENDER_PENDING",
        "model_gate_status": {
            "claude_web_app_full_artifact_review": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web_full_artifact_review": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    inserted = "\n".join(f"- `{item['heading']}`" for item in docx_info["inserted_headings"])
    md = f"""# SHUNYI_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`

- Suite: `{SUITE}`.
- Timestamp: `{ts}`.
- Formal scoring source: `{RUBRIC_PPT}`.
- Paper source: `{PAPER_PDF}`.
- Source bundle: `{SOURCE_BUNDLE}`.

## DOCX Inserts

{inserted}

## Matrix Closure

- Q2 inserted under `主观能动性 / 意识的能动作用` as a choice-question correct-option chain.
- Q5 inserted under `认识发展原理` as a choice-question correct-option chain.
- Q21 is closed against existing current-DOCX coverage and the formal scoring PPT's philosophy-angle/level-scoring support.
- Q1, Q3, Q17, and Q20 risk rows are module-boundary exclusions.
- The Qunknown long suite-extraction row and suite-level rows are closed as summaries only; they do not replace row-level evidence.
- Choice-question evidence is explicitly bounded as answer-key plus stem/correct-option chain, not main-question scoring-rubric evidence.
- Matrix backup: `{matrix_info['matrix_backup']}`.
- Ledger backup: `{ledger_info['ledger_backup']}`.
- DOCX backup: `{docx_info['docx_backup']}`.

## Open Gates

- DOCX/PDF render QA is pending for this batch.
- Claude web/app full artifact review through direct `https://claude.ai` remains `real_call_pending`.
- ClaudeCode Opus 4.7 max-effort/adaptive-thinking confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until a real capture proves it.
- GPTPro web full artifact review remains `real_call_pending`.
- ORDER_063 final GitHub upload remains deferred until all active Beijing politics lines reach terminal or user-approved blocker state and upload-scope plus secret scan are complete.
"""
    REPORT_MD.write_text(md, encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_info = edit_docx(ts)
    ledger_info = update_ledger(ts, docx_info["inserted_headings"])
    matrix_info = update_matrix(ts)
    write_report(ts, docx_info, ledger_info, matrix_info)
    print(json.dumps({"docx": docx_info, "ledger": ledger_info, "matrix": matrix_info}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
