from __future__ import annotations

import csv
import json
import re
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

ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH13_2026_MENTOUGOU_YIMO_CODEX_20260525.md"
SOURCE_TRANSCRIPTION = RECOVERY / "BATCH13_2026_MENTOUGOU_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
SUITE = "2026门头沟一模"

SOURCE_BUNDLE = "01_source_inventory/suite_source_bundles/2026门头沟一模.md"
PAPER_PDF = "2026各区一模/2026门头沟一模/试卷/门头沟区高三政治一模试卷.pdf"
RULE_DOCX = "2026各区一模/2026门头沟一模/细则/2026门头沟一模细则.docx"
ANSWER_RULE_DOCX = "2026各区一模/2026门头沟一模/门头沟高三政治一模参考答案及评标细则新.docx"

Q4_PROMPT = "2025年，北京市启动“两园一河”项目，将工业遗存改造为消费地标、将水上运动与生态景观串联，国潮时尚街区精彩亮相、工业遗存与高品质餐饮结合。这种“以文塑旅、以旅彰文”的融合发展模式体现什么。官方答案：B（①④）。"
Q5_PROMPT = "北京鲜批市场公交专线将站点创造性地设在市场二层交易区，被称为“能上楼的专线”。该专线的成功运行蕴含的道理。官方答案：C（②③）。"
Q7_PROMPT = "自北京市启动中学生学农教育实践活动以来，同学走进田间、操作间，在劳动中掌握生活技能、懂得劳动价值。下列说法正确。官方答案：B（①④）。"
Q16_PROMPT = "结合材料，运用《哲学与文化》知识，谈谈对永定河古渠“不是沉睡的文物，而是奔流不息的活态遗产”的理解。"
Q21_PROMPT = "结合材料，综合运用所学，谈谈中国为何能为世界提供宝贵的确定性。"

Q4_SOURCE = f"{SOURCE_BUNDLE}:195-203;87-88;1012-1013"
Q5_SOURCE = f"{SOURCE_BUNDLE}:204-213;87-88;1012-1013"
Q7_SOURCE = f"{SOURCE_BUNDLE}:230-238;87-88;1012-1013"
Q16_SOURCE = f"{SOURCE_BUNDLE}:19-30;371-379;944-955"
Q21_SOURCE = f"{SOURCE_BUNDLE}:79-86;477-520;1004-1011"

ENTRIES = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q4",
        "heading_suffix": "2026门头沟一模 第4题（选择题）",
        "material_trigger": "题干写“两园一河”把园博园、首钢园和永定河的工业遗存、生态景观、国潮街区、高品质餐饮等资源结合起来；官方答案B包含④“坚持从实际出发的态度”。",
        "question_prompt": Q4_PROMPT,
        "why_trigger": "正确项④直接落到从实际出发：文旅融合不是抽象套模式，而是立足“两园一河”的真实资源、生态条件、工业遗存和消费场景来设计发展路径。",
        "answer_landing": "本题应选B。本节点只处理④：发展文旅融合要坚持一切从实际出发，立足本地工业遗存、河流生态、消费需求和文化资源，把主观规划同客观条件统一起来。",
        "evidence_level": "选择题官方答案键+正确选项④",
        "source_lines": Q4_SOURCE,
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q5",
        "heading_suffix": "2026门头沟一模 第5题（选择题）",
        "material_trigger": "题干写公交专线把站点创造性地设在市场二层交易区，既解决采购出行最后一公里，又形成“能上楼”的服务创新；官方答案C包含②“对传统公交模式进行扬弃”。",
        "question_prompt": Q5_PROMPT,
        "why_trigger": "正确项②直接写“扬弃”。这不是简单否定传统公交，而是在保留公交公共服务功能的同时，改造站点设置和服务场景，更好满足群众需求。",
        "answer_landing": "本题应选C。本节点只处理②：公交服务创新体现辩证否定，既保留传统公交服务民生的基本功能，又突破固定站点和单一运行场景，实现守正创新。",
        "evidence_level": "选择题官方答案键+正确选项②",
        "source_lines": Q5_SOURCE,
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q7",
        "heading_suffix": "2026门头沟一模 第7题（选择题）",
        "material_trigger": "题干写学生走进田间学习整地做畦、菜苗移栽，在操作间炒菜、制作豆腐，从背诵诗句到切身感受劳动艰辛；官方答案B包含①“走出课堂参与田间生产劳作感悟劳动价值，体现了坚持实践第一观点”。",
        "question_prompt": Q7_PROMPT,
        "why_trigger": "看到“走出课堂”“参与田间生产劳作”“切身感受劳动价值”，应想到实践是认识的来源和基础。学生不是只从书本背诵劳动，而是在劳动实践中形成对劳动价值的真实认识。",
        "answer_landing": "本题应选B。本节点只处理①：实践是认识的基础，学生通过田间生产和生活劳动获得对农业知识、劳动艰辛和劳动价值的直接认识，体现坚持实践第一观点。",
        "evidence_level": "选择题官方答案键+正确选项①",
        "source_lines": Q7_SOURCE,
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q16",
        "heading_suffix": "2026门头沟一模 第16题（主观题）",
        "material_trigger": "材料写门头沟以“灌溉遗产+”模式串联京西古道、潭柘寺，打造水脉与文脉交融的首都文化新地标；细则哲学角度明确列“联系的观点”。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "古渠从单一灌溉设施转化为活态遗产，关键在于把灌溉、防洪、生态补水、校园体验、京西古道、潭柘寺和文化地标联系起来整体理解。",
        "answer_landing": "卷面可写：坚持联系的观点，把古渠的水利功能、生态功能、教育体验和文化旅游资源联系起来，推动水脉与文脉交融，使古渠成为奔流不息的活态遗产。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "根据固有联系建立新的具体联系",
        "question_no": "Q16",
        "heading_suffix": "2026门头沟一模 第16题（主观题）",
        "material_trigger": "材料写创新“灌溉遗产+”模式，把永定河古渠同京西古道、潭柘寺、校园体验、生态补水和首都文化地标联系起来。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "这些联系不是主观拼贴，而是建立在古渠既有水利、生态、文化和空间关系基础上的新连接，体现根据事物固有联系建立新的具体联系。",
        "answer_landing": "卷面可写：人们可以根据事物固有联系改变事物状态、建立新的具体联系。门头沟依托古渠既有水利和文化联系，拓展生态补水、研学体验和文旅融合功能，使遗产活起来。",
        "evidence_level": "评分细则原文明示+材料直接支撑",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q16",
        "heading_suffix": "2026门头沟一模 第16题（主观题）",
        "material_trigger": "细则哲学角度明确列“发展的观点”；示例写永定河古渠如今仍在灌溉农田、生态补水，作为活态遗产服务社会、推动发展。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "“不是沉睡的文物，而是奔流不息的活态遗产”本身就是从静态保存转向动态发展的表述，要用发展的观点看古渠当代价值。",
        "answer_landing": "卷面可写：事物是变化发展的，要用发展的观点看问题。古渠不是停留在过去的文物，而是在灌溉、生态补水、研学体验和文旅融合中不断生成新的现实价值。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q16",
        "heading_suffix": "2026门头沟一模 第16题（主观题）",
        "material_trigger": "细则哲学角度明确列“辩证否定观”；示例写辩证否定是联系和发展的环节，实质是扬弃，古渠保留核心灌溉、防洪功能，又增加生态补水等功能。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "古渠活化不是否定传统，也不是原样封存，而是在保留核心功能和历史文脉的基础上增加新功能、新场景，体现扬弃。",
        "answer_landing": "卷面可写：坚持辩证否定观，做到扬弃。门头沟保留古渠灌溉、防洪等核心功能，同时拓展生态补水、研学体验和文旅融合，实现优秀传统文化创造性转化、创新性发展。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q16",
        "heading_suffix": "2026门头沟一模 第16题（主观题）",
        "material_trigger": "细则哲学角度明确列“矛盾双方对立统一”；示例写用一分为二观点看问题，创造条件、化不利为有利，使古渠没有成为沉睡文物，而是活态遗产。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "古渠既可能因年代久远而沉睡，也能通过保护利用转化为活态遗产。看到“不利条件—创造条件—有利转化”，应想到矛盾双方对立统一。",
        "answer_landing": "卷面可写：矛盾双方在一定条件下相互转化。通过保护、申遗和创新利用，门头沟把古渠可能沉睡、闲置的一面转化为服务生态、文化和社会发展的有利一面。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q21",
        "heading_suffix": "2026门头沟一模 第21题（主观题）",
        "material_trigger": "细则允许结合材料一用哲学或思维阐释，并列出“尊重客观规律与发挥主观能动性相结合”；材料一写中国长期制定和实施五年规划，一棒接着一棒跑。",
        "question_prompt": Q21_PROMPT,
        "why_trigger": "中国能提供确定性，不是凭主观愿望，而是在把握经济社会发展规律、世界经济周期和自身发展阶段基础上，主动制定并接续实施规划。",
        "answer_landing": "卷面可写：坚持尊重客观规律与发挥主观能动性相结合。中国立足发展规律和国情，主动制定、实施和接续推进五年规划，以科学规划增强长期发展的稳定性和可预期性。",
        "evidence_level": "综合题细则明示哲学或思维角度（非逐点详细细则）",
        "source_lines": Q21_SOURCE,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q21",
        "heading_suffix": "2026门头沟一模 第21题（主观题）",
        "material_trigger": "细则允许结合材料一用哲学或思维阐释，并列出“系统思维”；材料写中国规划作为国家治理模式长期接续，经济、市场、科技产业和对外开放多方面共同构成确定性来源。",
        "question_prompt": Q21_PROMPT,
        "why_trigger": "中国确定性来自制度、规划、市场、科技产业和开放联动，不是单一因素。看到多方面共同支撑、长期接续推进，应想到系统思维和系统优化。",
        "answer_landing": "卷面可写：坚持系统观念，把制度优势、长期规划、超大市场、创新驱动和开放合作作为相互联系的系统来统筹推进，从而为世界提供稳定预期和发展机遇。",
        "evidence_level": "综合题细则明示哲学或思维角度（非逐点详细细则）",
        "source_lines": Q21_SOURCE,
    },
]

SECTION_NEXT = {
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
    "辩证否定 / 守正创新": "矛盾就是对立统一",
    "实践是认识的基础": "认识对实践的反作用",
    "联系的普遍性 / 联系的观点（总）": "联系的客观性",
    "根据固有联系建立新的具体联系": "联系的多样性",
    "发展的观点 / 发展的普遍性": "量变与质变 / 适度原则",
    "矛盾就是对立统一": "矛盾的普遍性",
    "尊重客观规律与发挥主观能动性相结合": "规律的客观性",
    "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
}
LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]
KEYS = {
    "id": "matrix_row_id",
    "source": "题源",
    "year": "年份",
    "stage": "阶段",
    "question": "题号",
    "type": "题型或模块判断",
    "in_body": "是否进宝典",
    "node": "宝典节点",
    "principle": "细则支持原理",
    "evidence": "证据等级",
    "misplaced": "是否误放",
    "needs": "是否需补厚",
    "action": "当前处理",
    "note": "备注",
    "artifact": "source_artifact",
}


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def set_plain_text(p, text: str) -> None:
    texts = p.xpath(".//w:t", namespaces=NS)
    if not texts:
        r = etree.SubElement(p, W + "r")
        t = etree.SubElement(r, W + "t")
        t.text = text
        return
    texts[0].text = text
    for node in texts[1:]:
        node.text = ""


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


def set_label_text(p, label: str, rest: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(label, True))
    p.append(make_run(" " + rest))
    ppr = p.find("./w:pPr", namespaces=NS)
    if ppr is None:
        ppr = etree.Element(W + "pPr", nsmap=p.nsmap)
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def find_section(paras, heading: str) -> tuple[int, int]:
    next_heading = SECTION_NEXT[heading]
    start = next((i for i, p in enumerate(paras) if para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section heading not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if para_text(paras[i]).strip() == next_heading), None)
    if end is None:
        raise RuntimeError(f"next heading not found after {heading}: {next_heading}")
    return start, end


def insert_entry(root, entry: dict[str, str]) -> str:
    body = root.find("w:body", namespaces=NS)
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    existing = next(
        (
            para_text(paras[i]).strip()
            for i in range(start + 1, end)
            if para_text(paras[i]).strip().endswith(entry["heading_suffix"])
        ),
        None,
    )
    if existing:
        return existing
    numbered = []
    for idx in range(start + 1, end):
        m = re.match(r"^(\d+)\.\s", para_text(paras[idx]).strip())
        if m:
            numbered.append((idx, int(m.group(1))))
    if not numbered:
        raise RuntimeError(f"no numbered item under {entry['canonical_node']}")
    last_idx, last_no = numbered[-1]
    block_end = end
    for idx in range(last_idx + 1, end):
        if re.match(r"^\d+\.\s", para_text(paras[idx]).strip()):
            block_end = idx
            break
    template = [deepcopy(p) for p in paras[last_idx:block_end]]
    if len(template) < 5:
        raise RuntimeError(f"template too short under {entry['canonical_node']}: {len(template)}")
    heading = f"{last_no + 1}. {entry['heading_suffix']}"
    set_plain_text(template[0], heading)
    for p, (label, key) in zip(template[1:5], LABELS):
        set_label_text(p, label, entry[key])
    if len(template) > 5:
        set_plain_text(template[5], "")
    ref = paras[end]
    for p in template:
        body.insert(body.index(ref), p)
    return heading


def update_docx(timestamp: str) -> list[str]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_mentougou_yimo_batch13_{timestamp}.docx")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        data = {info.filename: zin.read(info.filename) for info in infos}
    root = etree.fromstring(data["word/document.xml"])
    headings = [insert_entry(root, entry) for entry in ENTRIES]
    data["word/document.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    try:
        with zipfile.ZipFile(tmp_path, "w") as zout:
            for info in infos:
                zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                zi.compress_type = info.compress_type
                zi.external_attr = info.external_attr
                zout.writestr(zi, data[info.filename])
        shutil.move(tmp_path, docx)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    return headings


def accepted_record(entry: dict[str, str], heading: str) -> dict[str, str]:
    student = (
        f"{heading}\n"
        f"【材料触发点】 {entry['material_trigger']}\n"
        f"【设问】 {entry['question_prompt']}\n"
        f"【为什么能想到】 {entry['why_trigger']}\n"
        f"【答案落点】 {entry['answer_landing']}"
    )
    return {
        "source_suite": SUITE,
        "question_no": entry["question_no"],
        "framework_node": entry["canonical_node"],
        "canonical_node": entry["canonical_node"],
        "material_trigger": entry["material_trigger"],
        "question_prompt": entry["question_prompt"],
        "why_trigger": entry["why_trigger"],
        "answer_landing": entry["answer_landing"],
        "student_facing_text": student,
        "evidence_level": entry["evidence_level"],
        "boundary_note": entry["evidence_level"],
        "source_lane": "Codex Batch13 recovery production",
        "source_repair_basis": entry["source_lines"],
        "source_lines": entry["source_lines"],
        "batch": "batch13_2026_mentougou_yimo",
    }


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch13_mentougou_yimo_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    desired = {
        (e["canonical_node"], SUITE, e["question_no"]): {
            "canonical_node": e["canonical_node"],
            "source_suite": SUITE,
            "question_no": e["question_no"],
            "inserted_heading": h,
        }
        for e, h in zip(ENTRIES, headings)
    }
    out, seen = [], set()
    for row in rows:
        key = (row["canonical_node"], row["source_suite"], row["question_no"])
        if key in desired:
            if key not in seen:
                out.append(desired[key])
                seen.add(key)
            continue
        out.append(row)
    for key, row in desired.items():
        if key not in seen:
            out.append(row)
            seen.add(key)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)


def update_accepted(timestamp: str, headings: list[str]) -> None:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch13_mentougou_yimo_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup)
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    desired = {(SUITE, e["question_no"], e["canonical_node"]): accepted_record(e, h) for e, h in zip(ENTRIES, headings)}
    out, seen = [], set()
    for record in records:
        key = (record.get("source_suite"), record.get("question_no"), record.get("canonical_node"))
        if key in desired:
            if key not in seen:
                out.append(desired[key])
                seen.add(key)
            continue
        out.append(record)
    for key, record in desired.items():
        if key not in seen:
            out.append(record)
            seen.add(key)
    ACCEPTED.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n", encoding="utf-8")


def patch_row(row: dict[str, str], **values: str) -> None:
    for key, value in values.items():
        row[KEYS[key]] = value


def row_values(
    row_id: str,
    q: str,
    type_: str,
    in_body: str,
    node: str,
    principle: str,
    evidence: str,
    action: str,
    note: str,
    artifact: str,
) -> dict[str, str]:
    return {
        KEYS["id"]: row_id,
        "row_source": "batch13_2026_mentougou_yimo_missing_boundary_inventory",
        KEYS["source"]: SUITE,
        KEYS["year"]: "2026",
        KEYS["stage"]: "一模",
        KEYS["question"]: q,
        KEYS["type"]: type_,
        KEYS["in_body"]: in_body,
        KEYS["node"]: node,
        KEYS["principle"]: principle,
        KEYS["evidence"]: evidence,
        KEYS["misplaced"]: "否",
        KEYS["needs"]: "否",
        KEYS["action"]: action,
        KEYS["note"]: note,
        KEYS["artifact"]: artifact,
    }


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch13_2026_mentougou_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}
    h = dict(zip([(e["question_no"], e["canonical_node"]) for e in ENTRIES], headings))
    q16_note = (
        "Q16已登记现有正文："
        f"{h[('Q16', '联系的普遍性 / 联系的观点（总）')]}；"
        f"{h[('Q16', '根据固有联系建立新的具体联系')]}；"
        f"{h[('Q16', '发展的观点 / 发展的普遍性')]}；"
        f"{h[('Q16', '辩证否定 / 守正创新')]}；"
        f"{h[('Q16', '矛盾就是对立统一')]}。"
    )
    q21_note = (
        "Q21已登记现有正文："
        f"{h[('Q21', '尊重客观规律与发挥主观能动性相结合')]}；"
        f"{h[('Q21', '系统观念 / 系统优化')]}。"
        "证据为综合题角度细则，非逐点详细细则。"
    )
    q16_principle = "门头沟一模细则明确哲学角度：发展的观点、矛盾双方对立统一、辩证否定观、联系的观点；答出一点2分，两点及以上3分，结合材料1分。"
    decisions = {
        "M0074": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="发展的观点 / 发展的普遍性", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0075": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="矛盾就是对立统一", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0076": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="辩证否定 / 守正创新", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0077": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="联系的普遍性 / 联系的观点（总）", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0170": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="发展观/矛盾对立统一/辩证否定-扬弃/联系/根据固有联系建立新联系", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0232": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="发展观/矛盾对立统一/辩证否定-扬弃/联系-根据固有联系建立新联系", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0638": dict(in_body="否：党史/政治与文化精神边界题", node="不进入当前哲学宝典正文", principle="Q1官方答案B（①③）：①是统一战线/建国力量，③是赶考精神财富；本批不把红色精神文化线转入哲学正文。", evidence="官方答案键+正确选项链条+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项②④。", artifact=f"{SOURCE_BUNDLE}:133-160;87-88"),
        "M0639": dict(in_body="否：党史/政治史边界题", node="不进入当前哲学宝典正文", principle="Q2官方答案D（③④）：中国梦接力奋斗、党是主心骨；属于政治史/中国特色社会主义边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项①②。", artifact=f"{SOURCE_BUNDLE}:161-187;87-88"),
        "M0640": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一", principle="Q4官方答案B（①④），其中④明确坚持从实际出发；①为文化经济交融，不另入哲学节点。", evidence="选择题官方答案键+正确选项④", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=f"登记条目：{h[('Q4', '一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一')]}。", artifact=Q4_SOURCE),
        "M0641": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="辩证否定 / 守正创新", principle="Q5官方答案C（②③），其中②明确对传统公交模式进行扬弃；③为反向思考，按逻辑与思维边界不入本节点。", evidence="选择题官方答案键+正确选项②", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=f"登记条目：{h[('Q5', '辩证否定 / 守正创新')]}。", artifact=Q5_SOURCE),
        "M0642": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="实践是认识的基础", principle="Q7官方答案B（①④），其中①明确走出课堂参与田间生产劳作感悟劳动价值，体现坚持实践第一观点；④为辩证思维整体性特征，按逻辑与思维边界不入本节点。", evidence="选择题官方答案键+正确选项①", misplaced="否", needs="否", action="INSERTED_BATCH13_2026_MENTOUGOU_Q7_PRACTICE_FIRST", note=f"新增条目：{h[('Q7', '实践是认识的基础')]}。", artifact=Q7_SOURCE),
        "M0643": dict(in_body="否：政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q8官方答案C（乙、丁），讨论生态环境法典、民族团结进步促进法、国家发展规划法，属于法治/政治制度边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误发言甲/丙。", artifact=f"{SOURCE_BUNDLE}:239-252;87-88"),
        "M0644": dict(in_body="否：政治与法治/民族政策边界题", node="不进入当前哲学宝典正文", principle="Q9官方答案D（③④），民族区域自治制度促进共享发展成果、铸牢中华民族共同体意识，属于政治与法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项①②。", artifact=f"{SOURCE_BUNDLE}:253-263;87-88"),
        "M0645": dict(in_body="否：法律与生活/反不正当竞争边界题", node="不进入当前哲学宝典正文", principle="Q11官方答案C（②③），人工智能模型保护、诚信守法、市场秩序，属于法律与生活/经济法治边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项①④。", artifact=f"{SOURCE_BUNDLE}:286-296;87-88"),
        "M0646": dict(in_body="否：经济与社会/社会保障边界题", node="不进入当前哲学宝典正文", principle="Q12官方答案A（①③），普惠服务、社会保障、民生政策属于经济与社会/社会保障边界；④文化产业项非正确项。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项②④。", artifact=f"{SOURCE_BUNDLE}:297-318;87-88"),
        "M0647": dict(in_body="否：经济与社会/创新发展边界题", node="不进入当前哲学宝典正文", principle="Q13官方答案B（①④），创新指数、要素配置、创新驱动和产业附加值属于经济与社会边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项②③。", artifact=f"{SOURCE_BUNDLE}:323-332;87-88"),
        "M0648": dict(in_body="否：当代国际政治与经济边界题", node="不进入当前哲学宝典正文", principle="Q14官方答案A（①②），全球治理倡议与人类命运共同体属于当代国际政治与经济。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项③④。", artifact=f"{SOURCE_BUNDLE}:333-342;87-88"),
        "M0649": dict(in_body="否：当代国际政治与经济/国际贸易边界题", node="不进入当前哲学宝典正文", principle="Q15官方答案D（②④），进博会、跨境电商、最不发达国家专区属于开放贸易和世界经济边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不使用错误项①③。", artifact=f"{SOURCE_BUNDLE}:343-360;87-88"),
        "M0650": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="发展观/矛盾对立统一/辩证否定/联系/根据固有联系建立新联系", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q16_note, artifact=Q16_SOURCE),
        "M0651": dict(in_body="否：政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q17设问明确运用《政治与法治》知识，细则为党的领导、全过程人民民主、依法治国和多元主体协同治理。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不把城市发展规律字样转入哲学正文。", artifact=f"{SOURCE_BUNDLE}:31-41;386-399"),
        "M0652": dict(in_body="否：法律与生活/逻辑与思维边界题", node="不进入当前哲学宝典正文", principle="Q18(1)明确《法律与生活》；Q18(2)明确《逻辑与思维》科学思维方法，虽含联系发展全面/矛盾分析法等近邻术语，但不作为必修四哲学正文新增。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="与房山Q18不同，本题设问直接限定《逻辑与思维》，不混入必修四正文。", artifact=f"{SOURCE_BUNDLE}:42-60;404-423"),
        "M0653": dict(in_body="否：经济与社会边界题", node="不进入当前哲学宝典正文", principle="Q19设问明确运用《经济与社会》知识，细则为供给创造需求、科技创新、新发展理念、供给侧改革、需求牵引供给、市场与政府协同。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不因出现新发展理念/改革而进入哲学正文。", artifact=f"{SOURCE_BUNDLE}:61-66;426-455"),
        "M0654": dict(in_body="否：当代国际政治与经济边界题", node="不进入当前哲学宝典正文", principle="Q20设问明确运用《当代国际政治与经济》知识，细则为对外开放、经济全球化、高水平对外开放和海南封关意义。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH13", note="不把经济发展字样转入发展观节点。", artifact=f"{SOURCE_BUNDLE}:67-78;460-475"),
        "M0655": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="尊重客观规律与发挥主观能动性相结合/系统观念 / 系统优化", principle="Q21综合题细则允许材料一使用哲学或思维：尊重客观规律与发挥主观能动性相结合、辩证思维、系统思维等；本批只登记已有两条明确节点。", evidence="综合题细则明示哲学或思维角度（非逐点详细细则）", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH13", note=q21_note, artifact=Q21_SOURCE),
        "M0656": dict(in_body="否：抽取残留/题号不明", node="不进入当前哲学宝典正文", principle="该行无独立题号；本批已按Q1-Q21逐题处理，并补齐Q3/Q6/Q10缺行。", evidence="抽取残留清理+逐题源包核对", misplaced="否", needs="否", action="EXTRACTION_RESIDUE_CLOSED_BATCH13", note="不保留Qunknown挂起。", artifact=f"{SOURCE_BUNDLE}:1-1038"),
        "M0804": dict(in_body="套卷逐题已由Batch13闭合", node="SUITE_LEVEL_SUMMARY", principle="Q1-Q21已逐题回源；Q7新增，Q3/Q6/Q10补边界行，其余入正文/排除均有答案键或细则依据。", evidence="Batch13逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH13", note="套卷级记录不替代逐题记录。", artifact=f"{SOURCE_BUNDLE}:1-1038"),
        "M0852": dict(in_body="套卷逐题已由Batch13闭合", node="SUITE_LEVEL_SUMMARY", principle="Q1-Q21已逐题回源；Q7新增，Q3/Q6/Q10补边界行，其余入正文/排除均有答案键或细则依据。", evidence="Batch13逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH13", note="原套卷级挂起项关闭。", artifact=f"{SOURCE_BUNDLE}:1-1038"),
    }
    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)
    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    additions = [
        row_values(f"M{max_id + 1:04d}", "Q3", "教育/立德树人边界题", "否：教育/政治文化边界题", "不进入当前哲学宝典正文", "Q3官方答案D，健康第一教育理念落地旨在坚守立德树人初心、筑牢接班人的身心根基；不进入当前哲学正文。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH13", "原矩阵缺独立Q3行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:188-194;87-88"),
        row_values(f"M{max_id + 2:04d}", "Q6", "逻辑与思维/推理边界题", "否：逻辑与思维边界题", "不进入当前哲学宝典正文", "Q6官方答案A，考查类比推理和概念/推理关系，属于逻辑与思维。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH13", "原矩阵缺独立Q6行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:214-225;87-88"),
        row_values(f"M{max_id + 3:04d}", "Q10", "法律与生活/亲属关系边界题", "否：法律与生活边界题", "不进入当前哲学宝典正文", "Q10官方答案C，考查扶养关系案例识别，属于法律与生活。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH13", "原矩阵缺独立Q10行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:276-285;87-88"),
    ]
    existing = {(r[KEYS["source"]], r[KEYS["question"]], r[KEYS["action"]]) for r in rows}
    for row in additions:
        key = (row[KEYS["source"]], row[KEYS["question"]], row[KEYS["action"]])
        if key not in existing:
            rows.append(row)
            existing.add(key)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_source_transcription(timestamp: str) -> None:
    text = f"""# Batch13 Source Transcription - 2026门头沟一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026门头沟一模
status: SOURCE_PACKET_COMPLETE_FOR_BATCH13

## Source Files Checked

- paper PDF: `{PAPER_PDF}`
- detail rule file: `{RULE_DOCX}`
- answer/rule file: `{ANSWER_RULE_DOCX}`
- source bundle: `{SOURCE_BUNDLE}`

## Answer Key

Q1-Q15 official answer key from the rule files:

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| answer | B | D | D | B | C | A | B | C | D | C | C | A | B | A | D |

## Student-Facing Insert/Register Decisions

- Q4 -> existing `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, supported only by correct item ④.
- Q5 -> existing `辩证否定 / 守正创新`, supported only by correct item ②.
- Q7 -> newly inserted `实践是认识的基础`, supported only by correct item ①.
- Q16 -> existing entries registered under 联系观、根据固有联系建立新的具体联系、发展观、辩证否定、矛盾对立统一. The formal detail rule explicitly lists the four philosophy angles: 发展的观点、矛盾双方对立统一、辩证否定观、联系的观点.
- Q21 -> existing entries registered under 尊重客观规律与发挥主观能动性相结合 and 系统观念 / 系统优化. Evidence is comprehensive-question angle support, not point-by-point detailed scoring rules.

## Exclusions

- Q1: party history / red-spirit culture boundary.
- Q2: party history / politics boundary.
- Q3: education /立德树人 boundary; missing row added.
- Q6: logic and thinking boundary; missing row added.
- Q8-Q15 except Q7/Q5/Q4: law, politics, economics, or international-politics/economics boundaries according to official answer key.
- Q17: Political and Law.
- Q18: Q18(1) Legal Life; Q18(2) Logic and Thinking. Not inserted into 必修四 because the prompt explicitly limits Q18(2) to 《逻辑与思维》.
- Q19: Economy and Society.
- Q20: Contemporary International Politics and Economy.
- Qunknown: extraction residue.
"""
    SOURCE_TRANSCRIPTION.write_text(text, encoding="utf-8")


def write_report(timestamp: str, headings: list[str]) -> None:
    inserted = "\n".join(f"- {heading}" for heading in headings)
    text = f"""# Coverage Fusion Batch13 - 2026门头沟一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026门头沟一模
status: CODEX_BATCH13_SOURCE_COVERAGE_APPLIED

## Applied To DOCX / Ledger / Accepted

{inserted}

## Matrix Disposition

- Existing Q4, Q5, Q16 x5, and Q21 x2 DOCX rows were registered in `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Q7 was newly inserted under `实践是认识的基础`.
- Missing boundary rows were added for Q3, Q6, and Q10.
- Q1, Q2, Q8-Q15, Q17-Q20, and Qunknown were closed as source-supported module-boundary or extraction-residue decisions.
- Q18 was excluded because Q18(1) is 《法律与生活》 and Q18(2) is explicitly 《逻辑与思维》; broad near-neighbor terms were not used to force a 必修四 placement.
- Suite-level rows were closed after per-question rows were updated.

## Boundary

No Sonnet/Haiku/model-unknown output was used. Q21 is labeled as comprehensive angle support, not a point-by-point detailed scoring rule.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp, headings)
    update_matrix(timestamp, headings)
    write_source_transcription(timestamp)
    write_report(timestamp, headings)
    print(f"Batch13 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
