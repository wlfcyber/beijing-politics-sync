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
REPORT_MD = RECOVERY / "SHIJINGSHAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "SHIJINGSHAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026石景山一模"
YEAR = "2026"
STAGE = "一模"
ROW_SOURCE = "codex_recovery_20260525_shijingshan_2026_yimo_repair"

DESKTOP = Path.home() / "Desktop"
SOURCE_DIR = DESKTOP / "2026各区模拟题" / "2026各区一模" / "2026石景山一模"
PAPER_PDF = SOURCE_DIR / "2026北京石景山高三一模政治（教师版）.pdf"
RUBRIC_DOC = SOURCE_DIR / "2026石景山区高三一模评分细则.doc"
SOURCE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / "2026石景山一模.md"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q2",
        "heading_suffix": "2026石景山一模 第2题（选择题）",
        "material_trigger": "材料写长白山从“一季养四季”到“四季皆旺季”、衡阳把“沉睡”的工业厂房蝶变为新的文旅消费场景；官方答案键第2题为D，对应正确项②④，其中④明确“坚持发展观点，以新视角、新方法开发资源价值，把握发展主动权”。",
        "question_prompt": "从资源再利用和消费场景更新看，为什么本题应抓住发展观点？本题正确组合为D（②④）。",
        "why_trigger": "看到“破圈”“沉睡厂房蝶变”“全新视角”“新的消费场景”“打开发展新思路”，应想到发展不是停在原有用途上，而是在创造条件、更新方式中把资源潜能转化为新价值；正确项②可作为矛盾双方转化的选择题链条，正文主落点放在发展观点。",
        "answer_landing": "本题应选D。长白山和工业遗址的材料说明，人们能够用发展的观点看待既有资源，通过新视角、新方法创造条件，使原有季节资源、工业厂房转化为新的文旅消费场景和发展优势。①把系统优化误写为“部分功能之和大于整体功能”，③把客观见之于主观说反，均不进入正文链条。",
        "evidence_level": "选择题官方答案键+题干正确项链条；选择题边界已明示（非主观题评分细则）",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q3",
        "heading_suffix": "2026石景山一模 第3题（选择题）",
        "material_trigger": "材料写AI写作能提升效率、形成风格，但也会出现机械表述、信息来源模糊、缺乏原创性和创造力等问题；官方答案键第3题为A，对应正确项①③，其中①强调AI不能替代人的意识和特有感知，③强调写作应发挥主观能动性、展现独立思考。",
        "question_prompt": "AI写作的优势与局限怎样说明人的意识能动性？本题正确组合为A（①③）。",
        "why_trigger": "看到“AI能模仿创作范式但缺乏原创性和创造力”“写作要跳出路径依赖、独立思考”，应想到意识能动性：人能够有目的、有选择地认识和表达，不能把算法生成等同于人的意识活动和价值判断。",
        "answer_landing": "本题应选A。AI可以进行思维模拟和信息处理，但不能替代人的意识、感知、价值判断和创造性表达；写作仍需要人发挥主观能动性，跳出路径依赖，形成独立思考。②把利弊说成不可调和，④把AI写作说成具有实践的直接现实性，均不进入正文链条。",
        "evidence_level": "选择题官方答案键+题干正确项链条；选择题边界已明示（非主观题评分细则）",
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_shijingshan_yimo_repair_{ts}.docx")
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
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_shijingshan_yimo_repair_{ts}{LEDGER.suffix}")
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
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_shijingshan_yimo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    source = f"{RUBRIC_DOC}; {SOURCE_BUNDLE}; {PAPER_PDF}"
    touched: list[str] = []
    q17_support = (
        "石景山一模第17题正式评分细则写明：第（1）问可从规律、联系、发展、矛盾、文化传承与创新等角度回答；"
        "示例明确列出阴阳对立统一、具体问题具体分析、系统优化方法、人民至上价值观和中医药文化传承。"
    )
    q21_support = (
        "石景山一模第21题正式评分细则写明可从党的领导、制度优势、新发展理念、系统优化、科学立法、辩证思维等角度回答；"
        "当前DOCX已有系统观念和发展观点两处正文覆盖。"
    )

    exclude = {
        "M0599": ("Q1", "政治/中国特色社会主义选择题", "不进入当前哲学宝典", "第1题正确项围绕中国共产党推进中国式现代化和青年担当，属于政治与中国特色社会主义模块。"),
        "M0602": ("Q4", "文化生活选择题", "不进入当前哲学宝典", "第4题正确项围绕西安唐诗文化品牌、文化发展成果和城市文明，属于文化线，不作为哲学主线新增。"),
        "M0603": ("Q5", "逻辑与思维选择题", "不进入当前哲学宝典", "第5题考查概念外延、定义项和换质位推理，属于选择性必修三逻辑与思维。"),
        "M0604": ("Q7", "逻辑与思维选择题", "不进入当前哲学宝典", "第7题正确项为不完全归纳推理，属于选择性必修三逻辑与思维；错误项D的辩证思维不作正文证据。"),
        "M0605": ("Q8", "政治与法治选择题", "不进入当前哲学宝典", "第8题围绕人大代表职责和民生建议办理，属于政治与法治。"),
        "M0606": ("Q9", "政治与法治选择题", "不进入当前哲学宝典", "第9题围绕政协、检察公益保护衔接和社会治理，属于政治与法治。"),
        "M0607": ("Q10", "经济与社会选择题", "不进入当前哲学宝典", "第10题围绕国有经济、非公有制经济、科技创新与产业融合，属于经济与社会。"),
        "M0608": ("Q11", "经济与社会选择题", "不进入当前哲学宝典", "第11题围绕低空经济政策、法规和产业链，属于经济与产业治理，不作为哲学正文。"),
        "M0609": ("Q14", "法律与生活选择题", "不进入当前哲学宝典", "第14题围绕消费者充值合同、广告误导和民事行为能力，属于法律与生活。"),
        "M0610": ("Q15", "经济与开放发展选择题", "不进入当前哲学宝典", "第15题围绕海南封关、零关税、制度型开放和双循环，属于经济/开放发展。"),
        "M0611": ("Q16", "经济与社会主观题", "不进入当前哲学宝典", "第16题正式评分细则按市场资源配置、技术创新、应用场景、政府监管和基础设施规划评分，属于经济与社会。"),
        "M0613": ("Q18", "法律与生活主观题", "不进入当前哲学宝典", "第18题正式评分细则按行政诉讼、民事侵权、举证责任和过错推定评分，属于法律与生活。"),
        "M0614": ("Q19", "政治与法治主观题", "不进入当前哲学宝典", "第19题正式评分细则按以人民为中心、政府依法履职、法治社会和共建共治共享评分，属于政治与法治。"),
        "M0615": ("Q20", "当代国际政治与经济主观题", "不进入当前哲学宝典", "第20题正式评分细则按共商共建共享、人类命运共同体、经济全球化、和平发展合作共赢和共同利益评分。"),
    }

    for row in rows:
        if row.get("题源") != SUITE:
            continue
        row_id = row.get("matrix_row_id", "")
        if row_id == "M0600":
            update_row(
                row,
                题型或模块判断="必修四哲学选择题",
                是否进宝典="是：本批新增进入当前DOCX/PDF正文",
                宝典节点="发展的观点 / 发展的普遍性",
                细则支持原理=INSERT_ENTRIES[0]["material_trigger"],
                证据等级=INSERT_ENTRIES[0]["evidence_level"],
                是否误放="否",
                是否需补厚="否：已补入对应节点；选择题证据边界已明示",
                当前处理="DOCX_INSERTED_SHIJINGSHAN_2026_YIMO_RENDER_PENDING",
                备注="第2题只把正确项②④的哲学链条入正文；选择题答案键不冒充主观题评分细则。",
                source_artifact=source,
            )
        elif row_id == "M0601":
            update_row(
                row,
                题型或模块判断="必修四哲学选择题",
                是否进宝典="是：本批新增进入当前DOCX/PDF正文",
                宝典节点="主观能动性 / 意识的能动作用",
                细则支持原理=INSERT_ENTRIES[1]["material_trigger"],
                证据等级=INSERT_ENTRIES[1]["evidence_level"],
                是否误放="否",
                是否需补厚="否：已补入对应节点；选择题证据边界已明示",
                当前处理="DOCX_INSERTED_SHIJINGSHAN_2026_YIMO_RENDER_PENDING",
                备注="第3题只把正确项①③的意识能动性链条入正文；选择题答案键不冒充主观题评分细则。",
                source_artifact=source,
            )
        elif row_id in {"M0066", "M0067", "M0068", "M0069", "M0164", "M0227", "M0612"}:
            node = row.get("宝典节点", "") or "矛盾/系统/发展等已覆盖节点"
            update_row(
                row,
                题型或模块判断="必修四哲学主观题现有正文覆盖",
                是否进宝典="是：已进入当前DOCX/PDF正文",
                宝典节点=node,
                细则支持原理=q17_support,
                证据等级="正式评分细则-综合角度+示例（非逐点细则）",
                是否误放="否",
                是否需补厚="否",
                当前处理="SOURCE_REVIEW_CLOSED_CURRENT_DOCX_COVERAGE_SHIJINGSHAN_2026_YIMO",
                备注="现有DOCX多处第17题第（1）问条目覆盖；本批不重复插入。",
                source_artifact=source,
            )
        elif row_id == "M0616":
            update_row(
                row,
                题型或模块判断="必修四哲学主观题现有正文覆盖",
                是否进宝典="是：已进入当前DOCX/PDF正文",
                宝典节点="系统观念 / 系统优化；发展的观点 / 发展的普遍性",
                细则支持原理=q21_support,
                证据等级="正式评分细则-综合角度+等级赋分（非逐点细则）",
                是否误放="否",
                是否需补厚="否",
                当前处理="SOURCE_REVIEW_CLOSED_CURRENT_DOCX_COVERAGE_SHIJINGSHAN_2026_YIMO",
                备注="现有DOCX已含第21题系统观念和发展观点两处正文条目；不重复插入。",
                source_artifact=source,
            )
        elif row_id in {"M0617", "M0801", "M0854"}:
            update_row(
                row,
                题型或模块判断="套卷级闭合记录",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="2026石景山一模：Q2/Q3哲学选择链条本批补入；Q17(1)和Q21已有当前DOCX正文覆盖；其余政治、法律、经济、逻辑、国际题边界排除。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_SHIJINGSHAN_2026_YIMO_REPAIR_RENDER_PENDING",
                备注="套卷级记录不替代逐题行；本批已补足逐题记录。",
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
                证据等级="正式答案键/评分细则-模块边界",
                是否误放="否",
                是否需补厚="否",
                当前处理="MODULE_BOUNDARY_EXCLUDED_SHIJINGSHAN_2026_YIMO_SOURCE_REVIEW",
                备注="不把政治、法律、经济、逻辑、国际政治经济或文化线内容偷换为当前哲学正文。",
                source_artifact=source,
            )
        touched.append(row_id)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_row_ids": touched}


def write_report(ts: str, docx_info: dict[str, object], ledger_info: dict[str, object], matrix_info: dict[str, object]) -> None:
    data = {
        "timestamp": ts,
        "suite": SUITE,
        "docx": docx_info,
        "ledger": ledger_info,
        "matrix": matrix_info,
        "sources": {
            "rubric_doc": str(RUBRIC_DOC),
            "paper_pdf": str(PAPER_PDF),
            "source_bundle": str(SOURCE_BUNDLE),
        },
        "render_status": "RENDER_PENDING",
        "model_gate_status": {
            "claude_web_app": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    inserted = "\n".join(f"- `{item['heading']}`" for item in docx_info["inserted_headings"])
    md = f"""# SHIJINGSHAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`

- Suite: `2026石景山一模`.
- Timestamp: `{ts}`.
- Formal scoring source: `{RUBRIC_DOC}`.
- Paper source: `{PAPER_PDF}`.
- Source bundle: `{SOURCE_BUNDLE}`.

## DOCX Inserts

{inserted}

## Matrix Closure

- Q2 inserted under `发展的观点 / 发展的普遍性` as a choice-question correct-option chain.
- Q3 inserted under `主观能动性 / 意识的能动作用` as a choice-question correct-option chain.
- Q17(1) and Q21 are closed against existing current-DOCX coverage and formal scoring-document support.
- Q1, Q4-Q5, Q7-Q11, Q14-Q16, and Q18-Q20 are module-boundary exclusions.
- Choice-question evidence is explicitly bounded as answer-key plus stem/correct-option chain, not main-question scoring-rubric evidence.
- Matrix backup: `{matrix_info['matrix_backup']}`.
- Ledger backup: `{ledger_info['ledger_backup']}`.
- DOCX backup: `{docx_info['docx_backup']}`.

## Open Gates

- DOCX/PDF render QA is pending for this batch.
- Claude web/app external review remains `real_call_pending`.
- ClaudeCode Opus 4.7 max-effort confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until a real capture proves it.
- GPTPro web review remains `real_call_pending`.
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
