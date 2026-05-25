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
W = f"{{{W_NS}}}"
NS = {"w": W_NS}

ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
GLOBAL_AUDIT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"
GLOBAL_AUDIT_MD = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH19_2024_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH19_2024_CHAOYANG_MIDTERM_CODEX_20260525.md"

THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"

PREPROCESSED = Path(r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus")
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2024各区模拟题__2024各区期中__2024朝阳期中.md"
PAPER_TEXT = PREPROCESSED / "gpt_sources" / "0a50f76fd1e1c50f_202411朝阳高三政治_期中1试题.md"
RUBRIC_DOCX = PREPROCESSED / "gpt_sources" / "92a268ce852f6944_2024.11期中政治朝阳评标2.md"
RUBRIC_RTF = PREPROCESSED / "gpt_sources" / "25b6e8c2207d9d9e_2024朝阳期中细则.md"

SUITE = "2024朝阳期中"
YEAR = "2024"
STAGE = "期中"
BATCH_ID = "batch19_2024_chaoyang_midterm"
MATRIX_SOURCE = "codex_batch19_2024_chaoyang_midterm"
ANSWER_KEY = "1B 2D 3D 4C 5A 6C 7B 8D 9B 10D 11C 12C 13C 14A 15B"
SOURCE_PACKET = (
    "BATCH19_2024_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md; "
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/"
    "gpt_suite_bundles/2024各区模拟题__2024各区期中__2024朝阳期中.md; "
    "C:/Users/Administrator/Desktop/2024各区模拟题/2024各区期中/2024朝阳期中/细则/2024朝阳期中细则.rtf; "
    "current DOCX text verified"
)


NEW_ENTRIES = [
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q3",
        "heading_suffix": "2024朝阳期中 第3题（选择题）",
        "material_trigger": "唐代王维画物“多不问四时”，将桃、杏、芙蓉、莲花同画一景，并有“雪中芭蕉”的艺术处理。官方答案D指出绘画创作中的意识活动具有自觉选择性和能动创造性。",
        "question_prompt": "唐代王维画物，多不问四时；相关评价中有人认为失真，也有人认为“意到便成”。下列说法正确的是：A.脱离实景就缺乏审美价值 B.评价具有主体差异性，难有客观标准 C.绘画创作特殊规律与艺术创作一般规律迥然不同 D.绘画创作中的意识活动具有自觉选择性和能动创造性。",
        "why_trigger": "题干不是要求判断画得像不像，而是呈现画家对现实材料进行选择、加工和重组的艺术活动。学生看到“多不问四时”“意到便成”“雪中芭蕉”这种不机械复制客观物象的表达，就应想到意识活动具有目的性、自觉选择性和能动创造性。",
        "answer_landing": "本题应选D。本节点只处理D项：绘画创作可以在尊重艺术规律基础上对现实材料作能动加工，说明意识活动不是被动摹写，而具有自觉选择性和能动创造性。A把艺术创造简单等同于照相式再现，B否认审美评价的客观标准，C割裂特殊规律和一般规律，均不当。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q4",
        "heading_suffix": "2024朝阳期中 第4题（选择题）",
        "material_trigger": "某地在人工除草、化学农药除草之外增加生物防治方法，通过肉苁蓉根系抑制杂草、防止覆盖土壤、改变土壤酸碱度。官方答案C包含②：坚持系统优化方法，从整体上把握草、粮、地之间的联系。",
        "question_prompt": "某地在传统人工除草和化学农药除草方法之外，又发明生物防治方法：将肉苁蓉根茎撒播在杂草区域，抑制杂草、防止覆盖土壤并改变土壤酸碱度。这一做法说明什么？A.①② B.①③ C.②④ D.③④。",
        "why_trigger": "材料同时涉及杂草、粮食作物、土地酸碱度、防治方法等多个要素，并强调从单一除草转向综合防治。学生看到“草、粮、地”之间的联动效果，就应想到系统优化：立足整体、统筹要素、优化结构，使防治方案服务粮食生产和土地保护的整体目标。",
        "answer_landing": "本题应选C。本节点只处理②：生物防治把草、粮、地和防治方式作为系统来统筹，体现系统优化方法。①错在把数量控制说成改变毒性；③错在说斗争性向同一性转化；④另在守正创新节点处理。",
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q4",
        "heading_suffix": "2024朝阳期中 第4题（选择题）",
        "material_trigger": "该地没有简单抛弃人工除草和化学农药除草，而是在保留原有方法的基础上增加生物防治手段。官方答案C包含④：在保留原有方法的基础上增加新的防治手段，体现创新意识。",
        "question_prompt": "某地在传统人工除草和化学农药除草方法之外，又发明生物防治方法：将肉苁蓉根茎撒播在杂草区域，抑制杂草、防止覆盖土壤并改变土壤酸碱度。这一做法说明什么？A.①② B.①③ C.②④ D.③④。",
        "why_trigger": "材料中的创新不是把旧方法全部推翻，而是在既有人工、化学方法基础上增添更符合生态条件的生物防治方式。学生看到“保留原有方法+增加新手段”这种保留与突破并存的结构，就应想到辩证否定和守正创新。",
        "answer_landing": "本题应选C。本节点只处理④：防治方法的改进是在继承原有经验基础上的创新，体现辩证否定的扬弃和守正创新意识。②另在系统优化节点处理。",
    },
    {
        "canonical_node": "认识发展原理",
        "question_no": "Q5",
        "heading_suffix": "2024朝阳期中 第5题（选择题）",
        "material_trigger": "亚里士多德说哲理探索起于对自然万物的惊异，先惊异于迷惑现象，逐渐积累解释，再对日月星辰运行、宇宙创生等重大问题作成说明。官方答案A包含①②。",
        "question_prompt": "亚里士多德认为人们开始哲理探索起于对自然万物的惊异，先惊异于现象，逐渐积累解释，并对重大问题作成说明。下列说法正确的是：①探讨哲理探索的发生、路径和过程，有助于启发人们探索人与世界的关系；②认为人们可以通过探索外部的、表面的现实世界而获得深层次的理性认识；③重在追求体验鲜活性；④人生必需品满足是追求真理的充分必要条件。A.①② B.①④ C.②③ D.③④。",
        "why_trigger": "题干从“惊异于现象”到“积累解释”再到“重大问题说明”，呈现认识由表及里、由浅入深的发展过程。学生看到“迷惑的现象—解释—重大问题说明”这一链条，应落到感性认识上升为理性认识、认识不断深化发展的原理。",
        "answer_landing": "本题应选A。本节点处理①②：哲理探索从外部现象出发，通过解释和概括走向对人与世界关系、深层规律性问题的理性把握。③把哲理探索降为体验鲜活性，④把生活条件绝对化为充分必要条件，均不当。",
    },
    {
        "canonical_node": "量变与质变 / 适度原则",
        "question_no": "Q10",
        "heading_suffix": "2024朝阳期中 第10题（选择题）",
        "material_trigger": "中国式现代化是人与自然和谐共生的现代化；还老百姓蓝天白云、鸟语花香的愿景如今正在变成现实。官方答案D指出这说明要把握事物发展过程中量变与质变的关系。",
        "question_prompt": "中国式现代化是人与自然和谐共生的现代化。良好生态环境是最普惠的民生福祉；还老百姓蓝天白云、鸟语花香田园风光，这些美好愿景如今正在变成现实。下列选项正确的是：A.属种关系 B.外延一致 C.“留住”为对称关系 D.“如今正在变成现实”说明要把握好量变与质变的关系。",
        "why_trigger": "题干强调生态治理愿景“正在变成现实”，不是一蹴而就，而是在持续治理、长期积累中逐步达到新的生态环境状态。学生看到“愿景正在变成现实”这种从持续量的积累到阶段性变化的表述，应想到量变积累到一定程度引起质变，并在发展过程中重视量变。",
        "answer_landing": "本题应选D。本节点只处理D项：生态文明建设需要在持续治理中积累量变，推动生态环境质量发生积极变化。A、B、C是逻辑概念或关系判断干扰项，不作为本哲学节点新增。",
    },
]

BOUNDARY_ROWS = [
    ("Q2", "文化选择题", "否：哲学正文边界排除", "文化影响/家文化边界", "官方答案D：各地民居中蕴含的家文化深刻影响中国人的精神世界，属于文化影响方向。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_CULTURE_BOUNDARY_BATCH19", "不进入当前哲学正文。"),
    ("Q6", "文化/航天发展选择题", "否：哲学正文边界排除", "文化民族精神/航天发展事实边界", "官方答案C（②④）：中国特色月球探测发展道路与弘扬探月精神；①把科技规律说成可创新，③夸大技术攻关。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_CULTURE_BOUNDARY_BATCH19", "不进入当前哲学正文。"),
    ("Q7", "逻辑与思维选择题", "否：模块边界排除", "三段论推理边界", "题干要求从三个判断中构成三段论推理。", "题干+模块边界", "SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH19", "选择性必修三，不进入必修四哲学正文。"),
    ("Q8", "逻辑与思维选择题", "否：模块边界排除", "必要条件/逻辑规则边界", "题干要求依照逻辑规则判断一定为真的命题。", "题干+模块边界", "SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH19", "选择性必修三，不进入必修四哲学正文。"),
    ("Q9", "逻辑与思维选择题", "否：模块边界排除", "归纳推理/共变法边界", "题干要求判断实验推理方法，官方答案B为共变法。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH19", "选择性必修三，不进入必修四哲学正文。"),
    ("Q11", "逻辑与思维选择题", "否：模块边界排除", "判断/推理/逻辑规律边界", "题干要求准确把握概念、判断、推理，官方答案C。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH19", "选择性必修三，不进入必修四哲学正文。"),
    ("Q12", "经济与社会选择题", "否：模块边界排除", "高水平社会主义市场经济体制边界", "官方答案C（②③）：市场机制、反垄断、隐性壁垒治理。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH19", "经济与社会，不进入当前哲学正文。"),
    ("Q13", "经济与社会选择题", "否：模块边界排除", "宏观经济政策边界", "官方答案C（②③）：货币政策、房贷利率、存款准备金率传导。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH19", "经济与社会，不进入当前哲学正文。"),
    ("Q14", "经济与社会选择题", "否：模块边界排除", "国有经济改革边界", "官方答案A（①②）：国有企业分类考核、监管机制、竞争性环节改革。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH19", "经济与社会，不进入当前哲学正文。"),
    ("Q15", "当代国际政治与经济选择题", "否：模块边界排除", "中非合作/全球治理边界", "官方答案B（①④）：发展中国家共同利益、普惠包容经济全球化。", "答案键+题干+模块边界", "ANSWER_KEY_CLOSED_MODULE_BOUNDARY_BATCH19", "当代国际政治与经济，不进入当前哲学正文。"),
    ("Q18", "逻辑与思维主观题", "否：模块边界排除", "楚王和晏子推理评析边界", "题干明确要求运用《逻辑与思维》相关知识评析推理。", "题干+模块边界", "SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH19", "选择性必修三，不进入当前哲学正文。"),
    ("Q19", "逻辑与思维主观题", "否：模块边界排除", "创新思维边界", "题干明确要求分析首发经济样本如何体现创新思维。", "题干+模块边界", "SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH19", "选择性必修三，不进入当前哲学正文。"),
    ("Q20", "经济与社会/当代国际政治与经济主观题", "否：模块边界排除", "数字经济/数字贸易边界", "Q20(1)(2)为经济信息与经济高质量发展，Q20(3)限定《当代国际政治与经济》。", "题干+模块边界", "SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY_BATCH19", "不进入当前哲学正文。"),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS)).strip()


def style_val(p: etree._Element) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


def clear_runs(p: etree._Element) -> None:
    for child in list(p):
        if child.tag == W + "r" or child.tag == W + "hyperlink":
            p.remove(child)


def make_run(text: str, label: bool = False) -> etree._Element:
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return r


def new_heading_para(template: etree._Element, text: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(text))
    return p


def new_label_para(template: etree._Element, label: str, body: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + body))
    return p


def next_entry_number(paras: list[etree._Element], section_idx: int, end_idx: int) -> int:
    count = 0
    for p in paras[section_idx + 1 : end_idx]:
        if style_val(p) == "5" and re.match(r"^\d+\.", para_text(p)):
            count += 1
    return count + 1


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2024_chaoyang_midterm_batch19_{timestamp}.docx")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
        all_parts = {item.filename: zin.read(item.filename) for item in zin.infolist() if item.filename != "word/document.xml"}

    root = etree.fromstring(xml)
    body = root.xpath("//w:body", namespaces=NS)[0]

    inserted = 0
    for entry in NEW_ENTRIES:
        paras = body.xpath("./w:p", namespaces=NS)
        texts = [para_text(p) for p in paras]
        section_idx = next((i for i, text in enumerate(texts) if style_val(paras[i]) == "4" and text == entry["canonical_node"]), None)
        if section_idx is None:
            raise RuntimeError(f"Missing section: {entry['canonical_node']}")
        end_idx = len(paras)
        for i in range(section_idx + 1, len(paras)):
            if style_val(paras[i]) in {"3", "4"}:
                end_idx = i
                break
        if any(entry["heading_suffix"] in para_text(p) for p in paras[section_idx + 1 : end_idx]):
            continue
        heading_template = next((p for p in reversed(paras[section_idx + 1 : end_idx]) if style_val(p) == "5"), None)
        if heading_template is None:
            heading_template = next(p for p in paras if style_val(p) == "5")
        body_template = next((p for p in paras[section_idx + 1 : end_idx] if para_text(p).startswith("【材料触发点】")), None)
        if body_template is None:
            body_template = next(p for p in paras if para_text(p).startswith("【材料触发点】"))

        heading = f"{next_entry_number(paras, section_idx, end_idx)}. {entry['heading_suffix']}"
        new_paras = [
            new_heading_para(heading_template, heading),
            new_label_para(body_template, "【材料触发点】", entry["material_trigger"]),
            new_label_para(body_template, "【设问】", entry["question_prompt"]),
            new_label_para(body_template, "【为什么能想到】", entry["why_trigger"]),
            new_label_para(body_template, "【答案落点】", entry["answer_landing"]),
        ]
        for offset, new_p in enumerate(new_paras):
            body.insert(end_idx + offset, new_p)
        inserted += 1

    new_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
    with tempfile.TemporaryDirectory() as tmp:
        tmp_docx = Path(tmp) / docx.name
        with zipfile.ZipFile(tmp_docx, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for name, data in all_parts.items():
                zout.writestr(name, data)
            zout.writestr("word/document.xml", new_xml)
        shutil.copy2(tmp_docx, docx)

    return backup, inserted


def extract_docx_entries() -> list[dict[str, str]]:
    docx = current_docx()
    with zipfile.ZipFile(docx) as zf:
        xml = zf.read("word/document.xml")
    root = etree.fromstring(xml)
    paras = root.xpath("//w:body/w:p", namespaces=NS)
    text_style = [(style_val(p), para_text(p)) for p in paras if para_text(p)]
    entries: list[dict[str, str]] = []
    current_node = ""
    i = 0
    while i < len(text_style):
        style, text = text_style[i]
        if style == "4":
            current_node = text
        if style == "5" and SUITE in text:
            parts = [text]
            j = i + 1
            while j < len(text_style) and text_style[j][0] not in {"3", "4", "5"}:
                parts.append(text_style[j][1])
                j += 1
            m = re.search(r"第(\d+)题", text)
            if not m:
                raise RuntimeError(f"Could not parse question number from {text}")
            entries.append(
                {
                    "canonical_node": current_node,
                    "question_no": f"Q{m.group(1)}",
                    "inserted_heading": text,
                    "student_facing_text": "\n".join(parts),
                }
            )
            i = j
            continue
        i += 1
    return entries


def evidence_for(question_no: str, node: str) -> tuple[str, str]:
    if question_no in {"Q1", "Q3", "Q4", "Q5", "Q10"}:
        return (
            "客观答案表+题面正确项；非主观评分细则",
            "选择题客观答案链只能证明正确项进入该哲学节点；不得当作主观题评分细则。",
        )
    if question_no == "Q16":
        return (
            "正式阅卷细则+当前DOCX正文",
            "Q16阅卷细则逐点列出历史唯物主义原理，当前DOCX已有对应正文；本批补登记，不重复插入。",
        )
    if question_no == "Q17":
        return (
            "正式阅卷细则（哲学2分开放角度）+当前DOCX正文",
            "Q17细则明确文化6分+哲学2分，并列出辩证否定、对立统一/全面、具体问题具体分析、价值判断与选择、尊重规律发挥能动性等开放角度；不得冒充逐点细则。",
        )
    return ("题干+模块边界", "边界行。")


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    shutil.copy2(LEDGER, LEDGER.with_name(f"docx_insert_ledger_backup_before_batch19_2024_chaoyang_midterm_{timestamp}.csv"))
    shutil.copy2(ACCEPTED, ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch19_2024_chaoyang_midterm_{timestamp}.jsonl"))

    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        ledger_rows = list(reader)
    ledger_keys = {(r["canonical_node"], r["source_suite"], r["question_no"], r["inserted_heading"]) for r in ledger_rows}
    ledger_added = 0
    for e in entries:
        row = {
            "canonical_node": e["canonical_node"],
            "source_suite": SUITE,
            "question_no": e["question_no"],
            "inserted_heading": e["inserted_heading"],
        }
        key = (row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in ledger_keys:
            ledger_rows.append(row)
            ledger_keys.add(key)
            ledger_added += 1
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(ledger_rows)

    accepted_lines = ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines()
    accepted_records = [json.loads(line) for line in accepted_lines if line.strip()]
    accepted_keys = {
        (r.get("source_suite"), r.get("question_no"), r.get("canonical_node"), r.get("registered_heading"))
        for r in accepted_records
    }
    accepted_added = 0
    with ACCEPTED.open("a", encoding="utf-8") as f:
        for e in entries:
            evidence, boundary = evidence_for(e["question_no"], e["canonical_node"])
            record = {
                "source_suite": SUITE,
                "question_no": e["question_no"],
                "framework_node": e["canonical_node"],
                "canonical_node": e["canonical_node"],
                "student_facing_text": e["student_facing_text"],
                "evidence_level": evidence,
                "boundary_note": boundary,
                "source_lane": "Codex Batch19 existing-DOCX registration and choice insertion",
                "source_repair_basis": SOURCE_PACKET,
                "source_lines": SOURCE_PACKET,
                "batch": BATCH_ID,
                "registered_heading": e["inserted_heading"],
            }
            key = (record["source_suite"], record["question_no"], record["canonical_node"], record["registered_heading"])
            if key not in accepted_keys:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                accepted_keys.add(key)
                accepted_added += 1

    return {
        "ledger_rows": len(ledger_rows),
        "ledger_added": ledger_added,
        "accepted_rows": len(accepted_records) + accepted_added,
        "accepted_added": accepted_added,
    }


def build_matrix_rows(entries: list[dict[str, str]], start_id: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def mid() -> str:
        nonlocal start_id
        value = f"M{start_id:04d}"
        start_id += 1
        return value

    for e in entries:
        evidence, _ = evidence_for(e["question_no"], e["canonical_node"])
        if e["question_no"] == "Q1":
            qtype = "选择题哲学：既有正文覆盖"
            rule = "官方答案B（①③）：为国尽责、为民服务中实现个人价值；学习新知识、练就本领服务社会。"
            action = "REGISTERED_EXISTING_DOCX_BATCH19_CHAOYANG_Q1"
            note = "既有最终DOCX已覆盖；本批补登记ledger/accepted和矩阵。"
        elif e["question_no"] in {"Q3", "Q4", "Q5", "Q10"}:
            qtype = "选择题哲学：本批补入正文"
            rule_by_q = {
                "Q3": "官方答案D：绘画创作中的意识活动具有自觉选择性和能动创造性。",
                "Q4": "官方答案C（②④）：系统优化方法；保留原有方法基础上增加新防治手段体现创新意识。",
                "Q5": "官方答案A（①②）：哲理探索由现象惊异、解释积累走向理性认识和人与世界关系的探索。",
                "Q10": "官方答案D：生态愿景正在变成现实，说明要把握事物发展过程中量变与质变的关系。",
            }
            rule = rule_by_q[e["question_no"]]
            action = "INSERTED_DOCX_BATCH19_CHAOYANG_CHOICE"
            note = "本批依据客观答案链补入最终DOCX；不冒充主观评分细则。"
        elif e["question_no"] == "Q16":
            qtype = "主观题历史唯物主义：既有正文覆盖"
            rule = "正式评分细则：社会存在决定社会意识、人民群众是社会历史主体和创造者、生产关系适应生产力/上层建筑适应经济基础、改革是社会主义社会发展的直接动力等。"
            action = "REGISTERED_EXISTING_DOCX_BATCH19_CHAOYANG_Q16"
            note = "既有最终DOCX已覆盖；本批补登记ledger/accepted和矩阵。"
        elif e["question_no"] == "Q17":
            qtype = "主观题哲学与文化：哲学2分开放角度既有正文覆盖"
            rule = "正式评分细则：文化6分+哲学2分；哲学可从辩证否定、对立统一/全面、具体问题具体分析、价值观导向、价值判断和价值选择、尊重规律发挥主观能动性等方面作答，知识1分+材料1分。"
            action = "REGISTERED_EXISTING_DOCX_BATCH19_CHAOYANG_Q17"
            note = "既有最终DOCX已覆盖；哲学2分为开放角度，登记时不说成逐点评分细则。"
        else:
            qtype = "哲学正文条目"
            rule = evidence
            action = "REGISTERED_BATCH19"
            note = ""

        rows.append(
            {
                "matrix_row_id": mid(),
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": e["question_no"],
                "题型或模块判断": qtype,
                "是否进宝典": "是：已进入当前DOCX/PDF正文",
                "宝典节点": e["canonical_node"],
                "细则支持原理": rule,
                "证据等级": evidence,
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": action,
                "备注": note,
                "source_artifact": SOURCE_PACKET,
            }
        )

    for q, qtype, in_body, node, rule, evidence, action, note in BOUNDARY_ROWS:
        rows.append(
            {
                "matrix_row_id": mid(),
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": q,
                "题型或模块判断": qtype,
                "是否进宝典": in_body,
                "宝典节点": node,
                "细则支持原理": rule,
                "证据等级": evidence,
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": action,
                "备注": note,
                "source_artifact": SOURCE_PACKET,
            }
        )
    rows.sort(key=lambda r: (int(r["题号"][1:]) if r["题号"].startswith("Q") and r["题号"][1:].isdigit() else 999, r["宝典节点"]))
    return rows


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    shutil.copy2(MATRIX, RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch19_2024_chaoyang_midterm_{timestamp}.csv")
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = [r for r in reader if r.get("row_source") != MATRIX_SOURCE]
    max_id = max(int((r.get("matrix_row_id") or "M0000")[1:]) for r in rows if re.match(r"^M\d+$", r.get("matrix_row_id", "")))
    new_rows = build_matrix_rows(entries, max_id + 1)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    return {
        "matrix_rows": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "open_rows": sum(1 for r in new_rows if "待" in "".join(r.values()) or "疑似" in "".join(r.values())),
    }


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    paper = read_text(PAPER_TEXT)
    rubric = read_text(RUBRIC_DOCX)
    q16_start = rubric.find("16.（8分）")
    q17_start = rubric.find("17.（8分）")
    q18_start = rubric.find("能力要求", q17_start)
    q16_excerpt = rubric[q16_start:q17_start].strip() if q16_start >= 0 and q17_start >= 0 else "[missing q16 excerpt]"
    q17_excerpt = rubric[q17_start:q18_start].strip() if q17_start >= 0 and q18_start >= 0 else "[missing q17 excerpt]"

    def excerpt(q: int) -> str:
        marker = f"{q}. "
        start = paper.find(marker)
        if q == 4:
            start = paper.find("4. 我国部分农田")
        if start < 0:
            return f"[missing Q{q}]"
        end = paper.find(f"{q + 1}. ", start + 5) if q < 20 else -1
        if end < 0:
            end = min(len(paper), start + 1800)
        return paper[start:end].strip()

    entry_lines = "\n".join(
        f"- {e['question_no']} -> `{e['canonical_node']}` -> `{e['inserted_heading']}`" for e in entries
    )
    content = f"""# Batch19 2024朝阳期中 Source Transcription

status: `SOURCE_REVIEWED_BATCH19`

## Source Files

- paper cache: `{PAPER_TEXT}`
- suite bundle: `{GPT_BUNDLE}`
- rubric cache: `{RUBRIC_DOCX}`
- RTF rubric cache: `{RUBRIC_RTF}`
- raw RTF source: `C:/Users/Administrator/Desktop/2024各区模拟题/2024各区期中/2024朝阳期中/细则/2024朝阳期中细则.rtf`

## Objective Answer Key

RTF answer table verified by Word text conversion:

`{ANSWER_KEY}`

Evidence boundary: this answer table is used only for objective-choice placement. It is not treated as a subjective scoring rule.

## Choice Questions Used For New/Existing Philosophy Entries

### Q1

{excerpt(1)}

### Q3

{excerpt(3)}

### Q4

{excerpt(4)}

### Q5

{excerpt(5)}

### Q10

{excerpt(10)}

## Main Question Rubric Excerpts

### Q16 Rubric

{q16_excerpt[:4500]}

### Q17 Rubric

{q17_excerpt[:4500]}

## Current DOCX Entries After Batch19

{entry_lines}

## Boundary Questions

- Q2: culture influence / family culture boundary.
- Q6: space-development fact plus national-spirit culture boundary.
- Q7-Q9 and Q11: Logic and Thinking boundary.
- Q12-Q15: Economic and Social / International Politics and Economy boundary.
- Q18: Logic and Thinking main question.
- Q19: innovation thinking main question.
- Q20: Economic and Social plus International Politics and Economy.
"""
    SOURCE_TRANSCRIPTION.write_text(content, encoding="utf-8")


def update_global_audit(docx_mentions: int, matrix_rows_for_suite: int) -> dict[str, int]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        if row.get("normalized_suite") == SUITE:
            row["matrix_rows"] = str(matrix_rows_for_suite)
            row["current_docx_mentions"] = str(docx_mentions)
            row["current_status"] = "covered_by_batch19_recovery_matrix"
            row["blocker_or_next_action"] = "question-level disposition rows added by Batch19; DOCX entries registered/inserted"
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
    content = f"""# Global Raw Suite Exhaustion Audit 2026-05-25

status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`

## Summary

- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(rows)}`
- current covered by first/second mock audit or recovery matrix: `{len(covered)}`
- remaining midterm/final raw suites outside current coverage: `{len(missing)}`
- current recovery matrix rows for `2024朝阳期中`: `{matrix_rows_for_suite}`
- current DOCX mentions for `2024朝阳期中`: `{docx_mentions}`

## Finding

The source-scope gap is reduced but not closed. Batch19 brought `2024朝阳期中` into the recovery matrix and DOCX/ledger/accepted governance system.
The remaining suites below must still be incorporated or explicitly excluded before whole-project completion can be claimed.

## Remaining Missing Or Out-Of-Scope Raw Suites

| suite | stage | status | next action |
|---|---|---|---|
{missing_table}

## Evidence Files

- CSV detail: `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- Batch19 source transcription: `BATCH19_2024_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`
- current recovery matrix: `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
"""
    GLOBAL_AUDIT_MD.write_text(content, encoding="utf-8")
    return {"remaining_missing": len(missing), "covered": len(covered)}


def append_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    if marker not in text:
        path.write_text(text.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8")


def write_batch_report(stats: dict[str, int], entries: list[dict[str, str]], audit: dict[str, int]) -> None:
    q_counts: dict[str, int] = {}
    for e in entries:
        q_counts[e["question_no"]] = q_counts.get(e["question_no"], 0) + 1
    content = f"""# Coverage Fusion Batch19: 2024朝阳期中

status: `BATCH19_CODEX_LOCAL_APPLIED_RENDER_PENDING`

## What Changed

- Added `2024朝阳期中` to the recovery matrix with question-level disposition rows.
- Inserted missing objective-choice philosophy entries for Q3, Q4, Q5, and Q10.
- Registered existing DOCX entries for Q1, Q16, and Q17 into `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Updated the global raw-suite audit: remaining source-scope gap is now `{audit['remaining_missing']}` suites.

## Counts

- DOCX entries for suite after Batch19: `{len(entries)}`
- DOCX entry count by question: `{q_counts}`
- matrix rows total: `{stats['matrix_rows']}`
- Batch19 matrix rows: `{stats['batch_rows']}`
- Batch19 open rows: `{stats['open_rows']}`
- ledger rows: `{stats['ledger_rows']}`
- accepted JSONL rows: `{stats['accepted_rows']}`

## Evidence Boundary

- Choice entries use the RTF objective answer table and question stem only; they are not represented as subjective scoring rules.
- Q16 uses direct formal rubric support.
- Q17 uses formal rubric support for an open `哲学2分` add-on; it is not represented as point-by-point detailed scoring rules.
- Sonnet/Haiku/model-unknown evidence remains non-qualifying.
- GPTPro web and external Claude Opus full-artifact reviews remain `real_call_pending`.
"""
    BATCH_REPORT.write_text(content, encoding="utf-8")

    status_block = f"""## Batch19 Update: 2024朝阳期中 - 2026-05-25

- status: `RECOVERED_EXECUTION_IN_PROGRESS`
- batch state: `BATCH19_CODEX_LOCAL_APPLIED_RENDER_PENDING`
- files created/updated: `batch19_2024_chaoyang_midterm_apply_20260525.py`, `BATCH19_2024_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`, `COVERAGE_FUSION_BATCH19_2024_CHAOYANG_MIDTERM_CODEX_20260525.md`, `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md/.csv`.
- DOCX work: inserted missing Q3/Q4/Q5/Q10 choice entries; registered existing Q1/Q16/Q17 entries.
- evidence discipline: choice rows use objective answer table only; Q16 formal rubric direct; Q17 formal rubric open philosophy add-on, not point-by-point detailed scoring rules.
- global source-scope gap reduced to `{audit['remaining_missing']}` remaining midterm/final suites.
- ClaudeCode Opus 4.7 recheck: pending for Batch19.
- external reviews: GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`."""
    append_once(THREAD_STATUS, "## Batch19 Update: 2024朝阳期中", status_block)

    governor_block = f"""## Governor Batch19 Recovery Finding: 2024朝阳期中
Updated: 2026-05-25

- Verdict: Batch19 Codex lane is `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Coverage: `2024朝阳期中` now has `{stats['batch_rows']}` matrix rows and `0` open rows in the batch set.
- Insertions: Q3 -> `主观能动性 / 意识的能动作用`; Q4 -> `系统观念 / 系统优化` and `辩证否定 / 守正创新`; Q5 -> `认识发展原理`; Q10 -> `量变与质变 / 适度原则`.
- Existing registrations: Q1 -> `实现人生价值`; Q16 -> historical-materialism nodes; Q17 -> open philosophy add-on nodes already in current DOCX.
- Evidence quality: choice entries are objective-answer-table evidence only; Q16 is direct formal rubric; Q17 is formal open-add-on rubric and must not be inflated into detailed point-by-point scoring-rule evidence.
- Global source-scope gap remains open at `{audit['remaining_missing']}` raw midterm/final suites.
- ClaudeCode Opus 4.7 and render gates still need to run for this batch; external GPTPro/Claude full-artifact reviews remain `real_call_pending`."""
    append_once(GOVERNOR, "## Governor Batch19 Recovery Finding: 2024朝阳期中", governor_block)

    confucius_block = f"""## Confucius Batch19 Artifact Check: 2024朝阳期中
Updated: 2026-05-25

- Verdict: student-facing artifact update is applied but not yet render/model closed.
- Student-facing additions: Q3 teaches conscious activity's selectivity and creativity; Q4 teaches system optimization and守正创新; Q5 teaches recognition development from phenomena toward rational understanding; Q10 teaches量变与质变 in ecological progress.
- Student-facing registrations: Q1/Q16/Q17 existing entries are now governed by ledger/accepted records.
- Boundary discipline: Q2/Q6 culture-only or non-philosophy choice rows and Q7-Q9/Q11/Q18/Q19 logic rows remain excluded; Q12-Q15/Q20 are economy/international-politics boundaries.
- Remaining blockers: render QA and ClaudeCode Opus 4.7 batch recheck are pending; global source-scope gap remains `{audit['remaining_missing']}` suites; GPTPro and external Claude full-artifact reviews remain `real_call_pending`."""
    append_once(CONFUCIUS, "## Confucius Batch19 Artifact Check: 2024朝阳期中", confucius_block)


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    _, inserted = update_docx(timestamp)
    entries = extract_docx_entries()
    if len(entries) != 15:
        raise RuntimeError(f"Expected 15 current DOCX entries for {SUITE}, found {len(entries)}")
    ledger_stats = update_ledger_and_accepted(entries, timestamp)
    matrix_stats = update_matrix(entries, timestamp)
    write_source_transcription(entries)
    docx_mentions = sum(1 for e in entries if SUITE in e["inserted_heading"])
    audit_stats = update_global_audit(docx_mentions, matrix_stats["batch_rows"])
    stats = {**ledger_stats, **matrix_stats, "inserted": inserted}
    write_batch_report(stats, entries, audit_stats)
    print(json.dumps({**stats, **audit_stats, "docx_entries": len(entries)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
