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
SOURCE_TRANSCRIPTION = RECOVERY / "BATCH16_2026_FENGTAI_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH16_2026_FENGTAI_YIMO_CODEX_20260525.md"

SUITE = "2026丰台一模"
YEAR = "2026"
STAGE = "一模"

PAPER_SOURCE = "C:/Users/Administrator/Desktop/2026各区模拟题/2026各区一模/2026丰台一模/试卷/丰台一模.pdf"
RUBRIC_SOURCE = "C:/Users/Administrator/Desktop/2026各区模拟题/2026各区一模/2026丰台一模/细则/2026丰台一模细则.pptx"
ANSWER_SOURCE = "reports/overnight_2026-04-25/objective_answer_source_closure.md:9"
ANSWER_PDF = "reports/overnight_2026-04-25/downloaded_evidence/2026_fengtai_yimo_with_answers.pdf"
ANSWER_PAGE = "reports/overnight_2026-04-25/downloaded_evidence_pages/2026_fengtai_yimo_with_answers_page_09.png"
RUBRIC_CACHE = "beijing_politics_research/data/preprocessed_corpus/gpt_sources/26649804f1de31f5_2026丰台一模细则.md"
SUITE_BUNDLE = "reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026丰台一模.md"
ANSWER_KEY = "1B 2A 3D 4A 5A 6D 7B 8C 9D 10C 11D 12B 13A 14A 15C"

Q4_PROMPT = (
    "许多中国传统风格建筑的屋顶被设计成经典的凹曲屋面。现代研究证实，这一屋顶设计形式与重力作用下雨水最快排出的"
    "“最速降线”高度吻合。凹曲屋面的设计说明什么？官方答案A（①②）。"
)
Q5_PROMPT = (
    "量子通信通过量子密钥分发，利用量子态的不可克隆性和不确定性等特性，使任何试图窃听密钥的行为都会被通信双方察觉，"
    "从而保证密钥分发安全，实现“一话一密”。官方答案A（①②）。"
)
Q6_PROMPT = (
    "颐和园“借景”有苏州街近借两岸古树、昆明湖远借玉泉山玉峰塔、十七孔桥应时借冬至斜晖轨迹等例子。"
    "官方答案D（③④）。"
)

SOURCE_LINES_CHOICE = f"{ANSWER_SOURCE}; {ANSWER_PDF}; {ANSWER_PAGE}; {PAPER_SOURCE}"
SOURCE_LINES_Q16 = f"{RUBRIC_CACHE}; {SUITE_BUNDLE}; {ANSWER_PDF}:pages 5,9"
SOURCE_LINES_Q21 = f"{ANSWER_PDF}:pages 8,10; {RUBRIC_CACHE}; {SUITE_BUNDLE}"

NEW_ENTRIES = [
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q4",
        "heading_suffix": "2026丰台一模 第4题（选择题）",
        "material_trigger": "官方答案A包含①：凹曲屋面是古人在建筑营造实践中积淀而成的智慧结晶；题干还用现代“最速降线”研究反向说明古代实践经验的合理性。",
        "question_prompt": Q4_PROMPT,
        "why_trigger": "学生看到“建筑营造实践中积淀而成的智慧结晶”，应先想到认识来源于实践、实践推动认识形成和发展。凹曲屋面不是先有抽象数学命题再套用，而是在长期建筑实践、排水经验和审美营造中形成稳定认识，现代研究只是进一步解释其合理性。",
        "answer_landing": "本题应选A。本节点只处理①：古人在建筑营造实践中形成凹曲屋面的设计智慧，说明实践是认识的来源和发展动力。②“综合思维”属选择性必修三思维方法，不作为本哲学节点新增；③“全新重构”和④“迁移最速降线理论”均与题意不符。",
        "evidence_level": "客观答案表+题面正确项；非主观评分细则",
        "source_lines": SOURCE_LINES_CHOICE,
    },
    {
        "canonical_node": "根据固有联系建立新的具体联系",
        "question_no": "Q5",
        "heading_suffix": "2026丰台一模 第5题（选择题）",
        "material_trigger": "官方答案A包含①：量子通信利用量子态的不可克隆性和不确定性等独特性质，在通信安全场景中建立起新的具体联系，实现“一话一密”。",
        "question_prompt": Q5_PROMPT,
        "why_trigger": "量子通信不是凭主观意志任意连接，而是依据量子态本身的客观特性，把密钥分发、窃听可察觉、通信安全连接成新的技术关系。看到“利用量子态独特性质”“实现加密”，应想到根据事物固有联系建立新的具体联系。",
        "answer_landing": "本题应选A。本节点只处理①：人们尊重量子态的客观特性，建立量子密钥分发这一新的具体联系，使安全通信成为可能。③错在把技术进步说成超越客观条件；④错在把意识说成具有直接现实性。",
        "evidence_level": "客观答案表+题面正确项；非主观评分细则",
        "source_lines": SOURCE_LINES_CHOICE,
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q5",
        "heading_suffix": "2026丰台一模 第5题（选择题）",
        "material_trigger": "官方答案A包含②：量子通信深化了人们对量子技术的认识，有助于推动通信实践继续发展。",
        "question_prompt": Q5_PROMPT,
        "why_trigger": "材料把量子通信核心技术解释为量子密钥分发，说明对量子态不可克隆性、不确定性的认识已经转化为通信安全方案。看到“深化认识，有助于推动实践发展”，应落到认识对实践具有反作用，正确认识推动实践发展。",
        "answer_landing": "本题应选A。本节点只处理②：对量子技术规律性认识的深化，能够指导量子通信实践，提升密钥分发安全性并推动通信技术发展。注意这不是意识直接改造世界，必须通过实践和技术方案转化为现实。",
        "evidence_level": "客观答案表+题面正确项；非主观评分细则",
        "source_lines": SOURCE_LINES_CHOICE,
    },
    {
        "canonical_node": "联系的多样性",
        "question_no": "Q6",
        "heading_suffix": "2026丰台一模 第6题（选择题）",
        "material_trigger": "官方答案D包含③：颐和园“借景”可因“远、近、时”而变，巧妙利用不同景物之间多样的时空条件。",
        "question_prompt": Q6_PROMPT,
        "why_trigger": "近借、远借、应时而借不是同一种单线联系，而是在空间距离、时间光影、自然景观与人文意境等不同条件中把握多样联系。学生看到“远近时”并列，就应想到联系具有多样性，要具体分析不同条件下的联系形式。",
        "answer_landing": "本题应选D。本节点只处理③：借景之妙在于把握联系的多样性，因距离、时间、光影和景物条件不同而采用不同借景方式。①错在“立足局部景观”，系统优化应立足整体；②把造园手法拔高为中华民族整体风貌和精神特征，表述过宽。",
        "evidence_level": "客观答案表+题面正确项；非主观评分细则",
        "source_lines": SOURCE_LINES_CHOICE,
    },
]

REGISTER_EXISTING = [
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则酌情点+答案版参考答案+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "矛盾的普遍性",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "矛盾的主要方面和次要方面",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "两点论与重点论",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q16",
        "heading_suffix": "2026丰台一模 第16题（主观题）",
        "evidence_level": "正式阅卷细则+原卷题干+既有最终DOCX正文",
        "source_lines": SOURCE_LINES_Q16,
    },
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q21",
        "heading_suffix": "2026丰台一模 第21题（主观题）",
        "evidence_level": "答案版参考答案+PPT宽泛哲学角度+既有最终DOCX正文；非逐点细则",
        "source_lines": SOURCE_LINES_Q21,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q21",
        "heading_suffix": "2026丰台一模 第21题（主观题）",
        "evidence_level": "答案版参考答案+PPT宽泛哲学角度+既有最终DOCX正文；非逐点细则",
        "source_lines": SOURCE_LINES_Q21,
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q21",
        "heading_suffix": "2026丰台一模 第21题（主观题）",
        "evidence_level": "答案版参考答案+PPT宽泛哲学角度+既有最终DOCX正文；非逐点细则",
        "source_lines": SOURCE_LINES_Q21,
    },
]

SECTION_NEXT = {
    "尊重客观规律与发挥主观能动性相结合": "规律的客观性",
    "联系的普遍性 / 联系的观点（总）": "联系的客观性",
    "联系的客观性": "根据固有联系建立新的具体联系",
    "根据固有联系建立新的具体联系": "联系的多样性",
    "联系的多样性": "整体与部分",
    "整体与部分": "系统观念 / 系统优化",
    "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
    "辩证否定 / 守正创新": "矛盾就是对立统一",
    "矛盾就是对立统一": "矛盾的普遍性",
    "矛盾的普遍性": "矛盾的特殊性 / 具体问题具体分析",
    "矛盾的主要方面和次要方面": "两点论与重点论",
    "两点论与重点论": "内因与外因",
    "实践是认识的基础": "认识对实践的反作用",
    "认识对实践的反作用": "认识发展原理",
    "价值观的导向作用": "价值判断与价值选择",
    "价值判断与价值选择": "实现人生价值",
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
    for p in template:
        body.insert(end, p)
        end += 1
    return heading


def find_existing_block(root, item: dict[str, str]) -> tuple[str, str]:
    body = root.find("w:body", namespaces=NS)
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, item["canonical_node"])
    for idx in range(start + 1, end):
        heading = para_text(paras[idx]).strip()
        if heading.endswith(item["heading_suffix"]):
            lines = [heading]
            for p in paras[idx + 1 : min(idx + 5, end)]:
                t = para_text(p).strip()
                if t:
                    lines.append(t)
            return heading, "\n".join(lines)
    raise RuntimeError(f"existing heading not found: {item['canonical_node']} / {item['heading_suffix']}")


def replace_text_nodes(root) -> int:
    replacements = {
        "肤代影像": "篡改历史影像",
        "人类文明世界注入新的智慧": "人类文明进步注入强劲动能",
        "为人类文明注入新的智慧": "为人类文明进步注入强劲动能",
        "如何应对智慧引导": "如何以哲学智慧指引方向",
        "朝着善、安全、公平方向": "朝着有益、安全、公平方向",
        "被掉在”智能鸿沟“问题之外": "被排斥在智能服务之外",
        "被掉在”智能鸿沟“之外": "被排斥在智能服务之外",
    }
    changed = 0
    for node in root.xpath(".//w:t", namespaces=NS):
        if node.text is None:
            continue
        new = node.text
        for old, repl in replacements.items():
            new = new.replace(old, repl)
        if new != node.text:
            node.text = new
            changed += 1
    return changed


def update_docx(timestamp: str) -> tuple[list[str], dict[tuple[str, str], tuple[str, str]], int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_fengtai_yimo_batch16_{timestamp}.docx")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        data = {info.filename: zin.read(info.filename) for info in infos}
    root = etree.fromstring(data["word/document.xml"])
    replacements = replace_text_nodes(root)
    new_headings = [insert_entry(root, entry) for entry in NEW_ENTRIES]
    registered_blocks = {
        (item["question_no"], item["canonical_node"]): find_existing_block(root, item)
        for item in REGISTER_EXISTING
    }
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
    return new_headings, registered_blocks, replacements


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
        "source_lane": "Codex Batch16 recovery production",
        "source_repair_basis": entry["source_lines"],
        "source_lines": entry["source_lines"],
        "batch": "batch16_2026_fengtai_yimo",
    }


def registered_record(item: dict[str, str], heading: str, block_text: str) -> dict[str, str]:
    return {
        "source_suite": SUITE,
        "question_no": item["question_no"],
        "framework_node": item["canonical_node"],
        "canonical_node": item["canonical_node"],
        "student_facing_text": block_text,
        "evidence_level": item["evidence_level"],
        "boundary_note": item["evidence_level"],
        "source_lane": "Codex Batch16 existing-DOCX registration",
        "source_repair_basis": item["source_lines"],
        "source_lines": item["source_lines"],
        "batch": "batch16_2026_fengtai_yimo",
        "registered_heading": heading,
    }


def update_ledger(timestamp: str, new_headings: list[str], registered_blocks: dict[tuple[str, str], tuple[str, str]]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch16_fengtai_yimo_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    desired: dict[tuple[str, str, str], dict[str, str]] = {}
    for entry, heading in zip(NEW_ENTRIES, new_headings):
        key = (entry["canonical_node"], SUITE, entry["question_no"])
        desired[key] = {
            "canonical_node": entry["canonical_node"],
            "source_suite": SUITE,
            "question_no": entry["question_no"],
            "inserted_heading": heading,
        }
    for item in REGISTER_EXISTING:
        heading, _ = registered_blocks[(item["question_no"], item["canonical_node"])]
        key = (item["canonical_node"], SUITE, item["question_no"])
        desired[key] = {
            "canonical_node": item["canonical_node"],
            "source_suite": SUITE,
            "question_no": item["question_no"],
            "inserted_heading": heading,
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


def update_accepted(timestamp: str, new_headings: list[str], registered_blocks: dict[tuple[str, str], tuple[str, str]]) -> None:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch16_fengtai_yimo_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup)
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    desired: dict[tuple[str, str, str], dict[str, str]] = {}
    for entry, heading in zip(NEW_ENTRIES, new_headings):
        desired[(SUITE, entry["question_no"], entry["canonical_node"])] = accepted_record(entry, heading)
    for item in REGISTER_EXISTING:
        heading, block_text = registered_blocks[(item["question_no"], item["canonical_node"])]
        desired[(SUITE, item["question_no"], item["canonical_node"])] = registered_record(item, heading, block_text)
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


def next_matrix_id(rows: list[dict[str, str]]) -> int:
    nums = []
    for row in rows:
        m = re.match(r"^M(\d+)$", row.get("matrix_row_id", ""))
        if m:
            nums.append(int(m.group(1)))
    return max(nums) + 1


def add_row_if_missing(rows: list[dict[str, str]], fieldnames: list[str], row: dict[str, str], next_id: int) -> int:
    key = (row["题源"], row["题号"], row["宝典节点"], row["row_source"])
    for existing in rows:
        if (existing.get("题源"), existing.get("题号"), existing.get("宝典节点"), existing.get("row_source")) == key:
            existing.update(row)
            return next_id
    complete = {name: "" for name in fieldnames}
    complete.update(row)
    complete["matrix_row_id"] = f"M{next_id:04d}"
    rows.append(complete)
    return next_id + 1


def update_matrix(timestamp: str, new_headings: list[str], registered_blocks: dict[tuple[str, str], tuple[str, str]]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch16_2026_fengtai_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}
    h = {(entry["question_no"], entry["canonical_node"]): heading for entry, heading in zip(NEW_ENTRIES, new_headings)}

    boundary_decisions = {
        "M0541": ("Q1", "中国特色社会主义/时政选择题", "否：不进入当前哲学宝典正文", "中国特色社会主义/党的领导/个人奋斗边界", "官方答案B（①④）：党的全面领导与个人奋斗融入民族复兴；可作价值教育背景，但非当前哲学节点稳定落点。"),
        "M0542": ("Q2", "政治与法治选择题", "否：模块边界排除", "政治与法治/司法民主边界", "官方答案A（①②）：人民陪审员制度提升司法民主化、兼顾法理情理，属于政治与法治。"),
        "M0543": ("Q3", "政治与法治选择题", "否：模块边界排除", "政治与法治/协同立法边界", "官方答案D（②④）：京津冀协同立法提升区域环境治理效能，落实协同发展战略。"),
        "M0546": ("Q17", "政治与法治主观题", "否：模块边界排除", "政治与法治/生态环境法典边界", "Q17要求运用《政治与法治》阐释生态环境法典，不能因细则中出现“系统整合”而转入哲学。"),
        "M0547": ("Q19", "当代国际政治与经济主观题", "否：模块边界排除", "当代国际政治与经济/可持续发展边界", "Q19明确限定《当代国际政治与经济》，参考答案为人类命运共同体、多边主义、全球治理观等。"),
        "M0548": ("Q20", "法律与生活主观题", "否：模块边界排除", "法律与生活/侵权责任边界", "Q20明确限定《法律与生活》，参考答案为安全保障义务、侵权责任、司法公正等。"),
    }
    for row_id, (qno, qtype, in_body, node, principle) in boundary_decisions.items():
        if row_id in by_id:
            patch_row(
                by_id[row_id],
                type=qtype,
                in_body=in_body,
                node=node,
                principle=principle,
                evidence="答案版PDF题干+答案键/参考答案+模块边界",
                misplaced="否",
                needs="否",
                action="SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH16_FENGTAI_YIMO",
                note="Batch16回源核对后关闭早期PPT关键词误抓；不进入当前哲学宝典正文。",
                artifact=f"{ANSWER_PDF}; {ANSWER_PAGE}; {SOURCE_TRANSCRIPTION.name}",
            )

    if "M0544" in by_id:
        patch_row(
            by_id["M0544"],
            type="哲学与文化选择题",
            in_body="是：Batch16新增进入当前DOCX/PDF正文并登记ledger/accepted",
            node="实践是认识的基础",
            principle="Q4官方答案A（①②）：①明确凹曲屋面是古人在建筑营造实践中积淀而成的智慧结晶；②为选必三综合思维，不作为本哲学节点新增。",
            evidence="客观答案表+题面正确项；非主观评分细则",
            misplaced="否",
            needs="否",
            action="INSERTED_AND_REGISTERED_BATCH16_FENGTAI_Q4",
            note=f"新增正文：{h[('Q4', '实践是认识的基础')]}。",
            artifact=f"{SOURCE_LINES_CHOICE}; {SOURCE_TRANSCRIPTION.name}",
        )
    if "M0545" in by_id:
        patch_row(
            by_id["M0545"],
            type="哲学与文化选择题",
            in_body="是：Batch16新增进入当前DOCX/PDF正文并登记ledger/accepted",
            node="根据固有联系建立新的具体联系 / 认识对实践的反作用",
            principle="Q5官方答案A（①②）：①利用量子态独特性质建立新的具体联系；②深化对量子技术的认识，有助于推动实践发展。",
            evidence="客观答案表+题面正确项；非主观评分细则",
            misplaced="否",
            needs="否",
            action="INSERTED_AND_REGISTERED_BATCH16_FENGTAI_Q5",
            note=f"新增正文：{h[('Q5', '根据固有联系建立新的具体联系')]}；{h[('Q5', '认识对实践的反作用')]}。",
            artifact=f"{SOURCE_LINES_CHOICE}; {SOURCE_TRANSCRIPTION.name}",
        )

    q16_registered = "；".join(heading for heading, _ in registered_blocks.values() if "第16题" in heading)
    for row_id in ["M0049", "M0050", "M0051", "M0052", "M0128", "M0129", "M0130", "M0131"]:
        if row_id in by_id:
            patch_row(
                by_id[row_id],
                type="哲学与文化主观题",
                in_body="是：Batch16回源确认，既有最终DOCX已覆盖并补登记ledger/accepted",
                evidence="正式阅卷细则+原卷题干+答案版参考答案+最终DOCX正文",
                misplaced="否",
                needs="否",
                action="REGISTERED_EXISTING_DOCX_BATCH16_FENGTAI_Q16",
                note=f"早期question_prompt_not_verified已解除；Q16登记标题：{q16_registered}",
                artifact=f"{SOURCE_LINES_Q16}; {SOURCE_TRANSCRIPTION.name}",
            )
    for row_id in ["M0161", "M0220", "M0549"]:
        if row_id in by_id:
            patch_row(
                by_id[row_id],
                type="哲学与文化主观题/重复候选汇总",
                in_body="已闭合：拆分到既有DOCX节点并补登记ledger/accepted",
                node="矛盾就是对立统一 / 矛盾的普遍性 / 矛盾主次方面 / 两点论与重点论 / 联系观点 / 系统观念 / 辩证否定 / 价值判断与价值选择",
                principle="PPT正式细则明确哲学三角度：矛盾观点、联系整体部分、价值观导向；另有主观能动性与尊重规律、辩证否定观酌情给分。答案版PDF亦含对立统一、人民主体、辩证否定、价值观等参考点。",
                evidence="正式阅卷细则+原卷题干+答案版参考答案+最终DOCX正文",
                misplaced="否",
                needs="否",
                action="SOURCE_REVIEW_CLOSED_REGISTERED_EXISTING_BATCH16_FENGTAI_Q16",
                note="早期Qunknown/PPT整段抓取转为Q16已闭合记录；不再作为开放遗漏。",
                artifact=f"{SOURCE_LINES_Q16}; {SOURCE_TRANSCRIPTION.name}",
            )

    next_id = next_matrix_id(rows)
    q6_heading = h[("Q6", "联系的多样性")]
    additions = [
        ("Q6", "哲学与文化选择题", "是：Batch16新增进入当前DOCX/PDF正文并登记ledger/accepted", "联系的多样性", "Q6官方答案D（③④）：③明确“借景”因远、近、时而变，巧妙利用景物之间多样的时空条件；④属文化审美，不作哲学节点新增。", "客观答案表+题面正确项；非主观评分细则", "INSERTED_AND_REGISTERED_BATCH16_FENGTAI_Q6", f"新增正文：{q6_heading}。", SOURCE_LINES_CHOICE),
        ("Q7", "逻辑与思维选择题", "否：模块边界排除", "逻辑与思维/科学思维方法边界", "官方答案B（①④）：四诊法对应发散聚合、超前思维等，属于选择性必修三逻辑与思维。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q8", "逻辑与思维选择题", "否：模块边界排除", "逻辑与思维/假言推理边界", "官方答案C（②③）：围绕充分条件假言推理有效式与相关判断。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q9", "逻辑与思维选择题", "否：模块边界排除", "逻辑与思维/概念与判断边界", "官方答案D：判断灯谜、概念外延与联言判断等逻辑知识。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q10", "法律与生活选择题", "否：模块边界排除", "法律与生活/相邻关系侵权边界", "官方答案C（②④）：相邻关系、侵权责任、调解和诉讼。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q11", "法律与生活选择题", "否：模块边界排除", "法律与生活/劳动与要约边界", "官方答案D（③④）：录用通知书要约与用人单位诚信。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q12", "经济与社会选择题", "否：模块边界排除", "经济与社会/智能经济传导路径边界", "官方答案B（①③）：关键核心技术、场景培育和实体经济融合。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q13", "经济与社会选择题", "否：模块边界排除", "经济与社会/平台价格监管边界", "官方答案A（①③）：规范平台价格行为、市场竞争秩序与消费者权益。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q14", "当代国际政治与经济选择题", "否：模块边界排除", "当代国际政治与经济/中非关系边界", "官方答案A（①②）：中非情谊与政治经济合作。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q15", "当代国际政治与经济选择题", "否：模块边界排除", "当代国际政治与经济/APEC边界", "官方答案C（②③）：亚太区域经济一体化、多样性基础上的多层次合作。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", SOURCE_LINES_CHOICE),
        ("Q18", "经济与社会+逻辑与思维主观题", "否：模块边界排除", "经济与社会/逻辑与思维边界", "Q18(1)限定《经济与社会》；Q18(2)为必要条件假言推理和三段论推理，属选择性必修三。", "答案版参考答案+题干+模块边界", "SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH16", "不进入必修四哲学正文。", f"{ANSWER_PDF}:pages 6,9"),
        ("Q21", "综合主观题：已有哲学正文覆盖", "是：既有最终DOCX已覆盖并补登记ledger/accepted", "尊重客观规律与发挥主观能动性相结合 / 系统观念 / 矛盾就是对立统一", "Q21答案版参考答案强调立足实际、把握发展规律、系统思维、发展观点；PPT仅给宽泛哲学角度和等级描述，故作为既有正文登记，不冒充逐点评分细则。", "答案版参考答案+PPT宽泛哲学角度+最终DOCX正文；非逐点细则", "REGISTERED_EXISTING_DOCX_BATCH16_FENGTAI_Q21", "补登既有Q21正文到ledger/accepted；不新增正文。", SOURCE_LINES_Q21),
    ]
    for qno, qtype, in_body, node, principle, evidence, action, note, artifact in additions:
        next_id = add_row_if_missing(
            rows,
            fieldnames,
            {
                "row_source": "codex_batch16_2026_fengtai_yimo",
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": qno,
                "题型或模块判断": qtype,
                "是否进宝典": in_body,
                "宝典节点": node,
                "细则支持原理": principle,
                "证据等级": evidence,
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": action,
                "备注": note,
                "source_artifact": f"{artifact}; {SOURCE_TRANSCRIPTION.name}",
            },
            next_id,
        )
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_source_transcription(timestamp: str, replacements: int) -> None:
    text = f"""# Batch16 2026丰台一模 source transcription

Updated: {timestamp} +08

## Source files

- Local scan paper: `{PAPER_SOURCE}`
- Local rubric PPT: `{RUBRIC_SOURCE}`
- Cache rubric markdown: `{RUBRIC_CACHE}`
- Suite source bundle: `{SUITE_BUNDLE}`
- Public answer-version PDF: `{ANSWER_PDF}`
- Objective answer key ledger: `{ANSWER_SOURCE}`
- Saved answer page image: `{ANSWER_PAGE}`

## Objective answer key

`{ANSWER_KEY}`

## Choice-question decisions

- Q1: official answer B. Boundary: 中国特色社会主义/时政/个人奋斗，不新增哲学正文。
- Q2: official answer A. Boundary: 政治与法治/人民陪审员制度，不新增哲学正文。
- Q3: official answer D. Boundary: 政治与法治/协同立法，不新增哲学正文。
- Q4: official answer A. Entered `实践是认识的基础` for correct item ①; item ② is 选必三综合思维 and is not admitted as a philosophy node.
- Q5: official answer A. Entered `根据固有联系建立新的具体联系` for item ① and `认识对实践的反作用` for item ②. Wrong options ③/④ remain traps only.
- Q6: official answer D. Entered `联系的多样性` for item ③; item ④ is cultural/aesthetic support, not a separate philosophy-node insertion.
- Q7-Q9: 逻辑与思维 boundary.
- Q10-Q11: 法律与生活 boundary.
- Q12-Q13: 经济与社会 boundary.
- Q14-Q15: 当代国际政治与经济 boundary.

## Q16 rubric transcription

Rubric PPT states Q16 is `哲学与文化`, with formal philosophy scoring points:

1. 矛盾观点：坚持矛盾观点，用全面、辩证眼光看问题。AI 为人类文明进步注入强劲动能，同时带来风险与隐忧；要坚持一分为二，既看积极作用，又正视挑战。
2. 两点论与重点论：AI 积极作用是主流，风险与隐忧是支流；抓主流、促发展，同时不能忽视支流，需规范引导。
3. 联系观点/整体部分：人工智能发展与社会生活、文化传承、民生福祉紧密相连；推动健康发展需要统筹科技、伦理与社会公平，实现整体最优。
4. 价值观导向：以哲学智慧指引方向，遵循社会发展规律，站在最广大人民立场上作出正确价值判断和价值选择，确保 AI 朝着有益、安全、公平方向健康发展。
5. PPT另写：发挥主观能动性和尊重客观规律相结合、坚持辩证否定观，言之成理酌情给分。

Answer-version PDF reference answer also lists: 对立统一、人民主体地位、辩证否定观、立足实践与正确价值观。

## Q16 document registration

Batch16 did not duplicate Q16 text. It registered existing final-DOCX entries under:

- 联系的普遍性 / 联系的观点（总）
- 系统观念 / 系统优化
- 辩证否定 / 守正创新
- 矛盾就是对立统一
- 矛盾的普遍性
- 矛盾的主要方面和次要方面
- 两点论与重点论
- 价值判断与价值选择

Inline source-consistency repairs applied to existing Q16 text nodes: `{replacements}`.

## Q17-Q21 decisions

- Q17: 政治与法治，生态环境法典。Boundary.
- Q18: 经济与社会 + 逻辑与思维。Boundary.
- Q19: 当代国际政治与经济。Boundary.
- Q20: 法律与生活。Boundary.
- Q21: 综合题，existing final-DOCX entries registered under `尊重客观规律与发挥主观能动性相结合`, `系统观念 / 系统优化`, and `矛盾就是对立统一`. Evidence is answer-version reference answer plus broad PPT angle; not treated as point-by-point scoring rubric.
"""
    SOURCE_TRANSCRIPTION.write_text(text, encoding="utf-8")


def write_report(timestamp: str, new_headings: list[str], registered_blocks: dict[tuple[str, str], tuple[str, str]], replacements: int) -> None:
    q16_nodes = [node for (qno, node), _ in registered_blocks.items() if qno == "Q16"]
    q21_nodes = [node for (qno, node), _ in registered_blocks.items() if qno == "Q21"]
    text = f"""# Coverage Fusion Batch16: 2026丰台一模

Updated: {timestamp} +08

## Actions

- Verified answer key: `{ANSWER_KEY}` from `{ANSWER_SOURCE}` and `{ANSWER_PAGE}`.
- Inserted 4 new choice-question DOCX entries:
{chr(10).join(f"  - {heading}" for heading in new_headings)}
- Registered existing Q16 DOCX coverage into ledger/accepted nodes:
{chr(10).join(f"  - {node}" for node in q16_nodes)}
- Registered existing Q21 DOCX coverage into ledger/accepted nodes:
{chr(10).join(f"  - {node}" for node in q21_nodes)}
- Corrected `{replacements}` inline Q16 text nodes to align with source wording.
- Closed Q1-Q3, Q7-Q15, Q17-Q20 as source-supported module boundaries.
- Added missing matrix rows for Q6-Q15, Q18, and Q21 where the previous matrix lacked question-level rows.

## Evidence boundary

- Q4-Q6 are choice-question correct-option chains. Evidence level is official answer key plus stem/correct option, not main-question scoring rubric.
- Q16 has formal PPT scoring support and answer-version reference answer support.
- Q21 remains answer-version reference answer plus broad PPT angle; it is not upgraded to point-by-point formal scoring-rule evidence.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_headings, registered_blocks, replacements = update_docx(timestamp)
    update_ledger(timestamp, new_headings, registered_blocks)
    update_accepted(timestamp, new_headings, registered_blocks)
    write_source_transcription(timestamp, replacements)
    update_matrix(timestamp, new_headings, registered_blocks)
    write_report(timestamp, new_headings, registered_blocks, replacements)
    print("timestamp", timestamp)
    print("new_headings")
    for heading in new_headings:
        print(heading)
    print("registered", len(registered_blocks))
    print("text_node_replacements", replacements)


if __name__ == "__main__":
    main()
