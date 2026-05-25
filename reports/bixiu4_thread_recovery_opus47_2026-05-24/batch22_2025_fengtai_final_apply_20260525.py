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
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH22_2025_FENGTAI_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH22_2025_FENGTAI_FINAL_CODEX_20260525.md"

PREPROCESSED = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区期末__2025丰台期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "360d57a4b250de81_2025丰台期末细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "89765092a6f26242_2025北京丰台高三_上_期末政治_教师版.md"

SUITE = "2025丰台期末"
YEAR = "2025"
STAGE = "期末"
BATCH_ID = "batch22_2025_fengtai_final"
MATRIX_SOURCE = "codex_batch22_2025_fengtai_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    "current DOCX text verified before Batch22 insertion"
)

Q4_PROMPT = (
    "“人民医护工作者”路生梅、“人民教育家”黄大年、“人民卫士”巴依卡等榜样人物的事迹说明什么？"
    "教师版答案A，正确项①③。"
)
Q16_PROMPT = (
    "胸中有“数”的工作方法，是毛泽东从中国革命和建设实践中总结得出的宝贵经验。"
    "“数”从哪里来，“数”当如何定，“数”为何所用……阐述“胸中有‘数’”带来的哲学思考。"
)

NEW_ENTRIES = [
    {
        "canonical_node": "实现人生价值",
        "question_no": "Q4",
        "heading_suffix": "2025丰台期末 第4题（选择题）",
        "material_trigger": "教师版答案A包含①③：路生梅、黄大年、巴依卡等榜样人物在为国尽责、为民服务的实践中展现人生风采，并以修身立德、服务他人和社会实现人生价值。",
        "question_prompt": Q4_PROMPT,
        "why_trigger": "题干并不是单纯表彰个人荣誉，而是把榜样人物的岗位实践、为民服务和对社会的责任贡献放在一起。看到“为国尽责、为民服务”“为他人和社会作贡献”，应落到人的真正价值在于对社会的责任和贡献，以及在劳动和奉献中实现人生价值。",
        "answer_landing": "本题应选A。本节点只处理正确项①③：人生价值不是靠追求社会对自我的肯定实现，而是在服务国家、服务人民、贡献社会的实践中实现。②把精彩人生限于卓越人物过窄，④把真正价值落在社会肯定上错误。本条证据只来自客观题答案键和正确项解析，不冒充主观评分细则。",
        "evidence_level": "教师版客观答案/解析+题面正确项；非主观评分细则",
        "boundary_note": "客观选择题证据只证明正确项可挂实现人生价值节点，不升级为主观题细则。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q16",
        "heading_suffix": "2025丰台期末 第16题（主观题）",
        "material_trigger": "细则第255行把“数从哪里来”对应到实践、实际、规律、发挥主观能动性；材料强调“不懂得注意决定事物质量的数量界限，一切都是胸中无数，结果就不能不犯错误”。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "数量界限和质量变化的关系不是主观偏好，而是事物发展中的客观规定。学生看到“规律”“数量界限”“不注意就犯错误”，应想到规律具有客观性，必须尊重客观规律。",
        "answer_landing": "做到胸中有“数”，首先要承认事物发展有客观规律和客观数量界限。调查统计、百分比分析和“度”的把握，是为了使决策符合客观规律，避免凭主观愿望任意定数、任意用数。",
        "evidence_level": "正式PPT评分细则+教师版题面/解析",
        "boundary_note": "Q16正式细则明列“规律”；该条仅登记规律客观性落点。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q16",
        "heading_suffix": "2025丰台期末 第16题（主观题）",
        "material_trigger": "细则第256-257行把“数当如何定”“数为何所用”指向系统优化、整体部分；示例答案要求坚持系统观念，立足整体把握相互关联的诸多要素。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "“看大数、看长远”“做计划、定方案”不是孤立看一个数字，而是把多个要素、局部数据和长远目标放进整体结构中统筹。看到“系统优化、整体部分”，应落到系统观念。",
        "answer_landing": "胸中有“数”要求坚持系统观念，用综合思维处理部分数据和整体目标的关系，在工作方案和国家治理中优化要素组合，把局部之“数”服务于整体最优。",
        "evidence_level": "正式PPT评分细则+当前DOCX整体/联系条目可互证",
        "boundary_note": "当前DOCX已有整体与部分条目；Batch22补齐正式细则中单列的系统优化节点。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q16",
        "heading_suffix": "2025丰台期末 第16题（主观题）",
        "material_trigger": "细则第208、257、260行均把发展列为可作答角度：数当如何定涉及发展等，数为何所用涉及发展等，第16题可从联系观、发展观、矛盾观等角度作答。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "材料要求在工作生活中做计划、定方案，在国家治理中看大数、看长远。“看长远”说明“数”的判断不是静止截面，而要放到事物发展过程和未来趋势中理解。",
        "answer_landing": "作答可用发展的观点说明：胸中有“数”要把对象看成变化发展的过程，既分析当下数量状态，也判断发展趋势和长远影响，使计划方案适应事物发展的方向和阶段性要求。",
        "evidence_level": "正式PPT评分细则明列发展观",
        "boundary_note": "细则只给发展观宽角度，故本条不细化到前进性曲折性等更窄节点。",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q16",
        "heading_suffix": "2025丰台期末 第16题（主观题）",
        "material_trigger": "细则第209、257行把“数为何所用”指向做计划、定方案，以及认识对实践的反作用、意识的能动作用；题干也写“在工作生活中，要做计划、定方案；在国家治理中，要看大数、看长远”。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "“数”不是为了停留在统计表里，而是为了指导计划、方案和治理实践。看到“数为何所用”“做计划、定方案”，应落到正确认识对实践具有指导作用。",
        "answer_landing": "对客观情况形成正确的数量认识后，还要把这种认识用于制定计划、优化方案和改进治理。正确认识能够反作用于实践，减少决策和指导中的盲目性与随意性。",
        "evidence_level": "正式PPT评分细则+教师版题面",
        "boundary_note": "本条只登记认识反作用，不把所有治理意义泛化为价值观或政治治理节点。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q16",
        "heading_suffix": "2025丰台期末 第16题（主观题）",
        "material_trigger": "细则第257行把“数为何所用”明确列为可涉及正确的价值观；材料把“数”用于计划方案和国家治理，要求避免盲目性与随意性。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "掌握“数”之后服务什么目标，决定了数据和方案如何被使用。看到细则中的“正确的价值观”和材料中的国家治理、长远发展，应想到价值观对认识和实践活动具有导向作用。",
        "answer_landing": "胸中有“数”不能只是技术性掌握数据，还要在正确价值观导向下使用数据。只有把“数”用于科学决策、公共治理和人民利益，才能使数据分析转化为正确行动，避免片面追求指标或凭偏好用数。",
        "evidence_level": "正式PPT评分细则明列正确价值观",
        "boundary_note": "细则给的是正确价值观宽角度，故登记为价值观导向作用，不扩展为价值判断与价值选择。",
    },
]

BOUNDARY_ROWS = [
    ("Q1", "文化选择题", "否：哲学正文边界排除", "中华文化/中华文明突出特性", "教师版答案B；题干落在中华文明多元一体、开放包容等文化知识，不作为哲学正文新增。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "文化线不进入当前哲学宝典正文。"),
    ("Q2", "政治与法治选择题", "否：模块边界排除", "人大代表履职/全过程人民民主", "教师版答案D；题干围绕人大代表家站点和代表履职。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "政治与法治边界。"),
    ("Q3", "经济与社会/民生服务选择题", "否：模块边界排除", "养老服务体系/社会保障与公共服务", "教师版答案B；题干聚焦养老服务供给体系，不形成必修四哲学正文落点。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "经济与社会/民生服务边界。"),
    ("Q5", "经济与社会/数字发展选择题", "否：模块边界排除", "互联网赋能发展", "教师版答案A；题干围绕网络直播、远程教育和数字资源整合，主线为数字发展与共同富裕，不进入哲学正文。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "经济与社会边界。"),
    ("Q6", "文化选择题", "否：哲学正文边界排除", "中华优秀传统文化/文化自信", "教师版答案A；题干为非遗彩灯与北京文化融合，属于文化线。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "文化线不进入当前哲学宝典正文。"),
    ("Q8", "逻辑与思维选择题", "否：模块边界排除", "形象思维/发散思维", "教师版答案D；题干明确考查形象思维和发散思维。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必三边界。"),
    ("Q9", "逻辑与思维选择题", "否：模块边界排除", "充分条件假言推理", "教师版答案D；题干考查假言推理。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必三边界。"),
    ("Q10", "逻辑与思维选择题", "否：模块边界排除", "归纳推理/类比推理", "教师版答案B；题干考查归纳推理与类比推理。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必三边界。"),
    ("Q11", "法律与生活选择题", "否：模块边界排除", "肖像权/人格权保护", "教师版答案D；题干为民事人格权与网络法治。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必二边界。"),
    ("Q12", "法律与生活选择题", "否：模块边界排除", "旅游合同/安全保障义务", "教师版答案B；题干为合同与侵权责任。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必二边界。"),
    ("Q13", "经济与社会选择题", "否：模块边界排除", "财政政策/货币政策传导", "教师版答案C；题干为宏观经济政策传导。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "经济与社会边界。"),
    ("Q14", "经济与社会选择题", "否：模块边界排除", "首发经济/产业消费", "教师版答案C；题干为首发经济影响。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "经济与社会边界。"),
    ("Q15", "经济与社会/开放经济选择题", "否：模块边界排除", "外贸高质量发展/新发展理念", "教师版答案A；题干为外贸结构和绿色发展，不进入哲学正文。", "教师版客观答案/解析+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "经济与社会边界。"),
    ("Q18(1)", "逻辑与思维主观题", "否：模块边界排除", "必要条件假言判断/联言判断", "题干要求写判断类型和保真条件，正式细则第108-117行也按逻辑判断给分。", "题面+正式PPT细则", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必三边界。"),
    ("Q18(2)", "经济与社会主观题", "否：模块边界排除", "数字经济/市场和政府关系", "题干明确限定《经济与社会》，细则第134-140行按有效市场和有为政府给分。", "题面+正式PPT细则", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "经济与社会边界。"),
    ("Q18(3)", "政治与法治主观题", "否：模块边界排除", "法治护航市场经济", "题干明确限定《政治与法治》，教师版答案按科学立法、严格执法、公正司法、法治社会作答。", "题面+教师版参考答案", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "政治与法治边界。"),
    ("Q19", "法律与生活主观题", "否：模块边界排除", "劳动合同/劳动者义务", "题干明确限定《法律与生活》相关知识阐释法院裁判理由。", "题面+教师版参考答案", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必二边界。"),
    ("Q20", "当代国际政治与经济主观题", "否：模块边界排除", "中非合作/全球治理/人类命运共同体", "题干明确限定《当代国际政治与经济》，细则第216-224行按时代主题、共同利益、全球治理观、新型国际关系等给分。", "题面+正式PPT细则", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "选必一边界。"),
    ("Q21", "综合主观题", "否：模块边界排除", "制度优势/中国特色社会主义制度", "教师版答案要求从具体制度、理论和实践层面阐述制度优势；主线为制度体系、人大制度、市场经济体制等，不登记为必修四哲学正文。", "题面+教师版参考答案/评分标准", "MODULE_BOUNDARY_EXCLUDED_BATCH22_FENGTAI_FINAL", "综合政治/经济制度边界。"),
]


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
        if child.tag in {W + "r", W + "hyperlink"}:
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


def new_label_para(template: etree._Element, label: str, body_text: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + body_text))
    return p


def next_entry_number(paras: list[etree._Element], section_idx: int, end_idx: int) -> int:
    count = 0
    for p in paras[section_idx + 1 : end_idx]:
        if style_val(p) == "5" and re.match(r"^\d+\.", para_text(p)):
            count += 1
    return count + 1


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch22_2025_fengtai_final_{timestamp}.docx")
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
        section_idx = next(
            (i for i, text in enumerate(texts) if style_val(paras[i]) == "4" and text == entry["canonical_node"]),
            None,
        )
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
    entries.sort(key=lambda e: (q_sort(e["question_no"]), e["canonical_node"], e["inserted_heading"]))
    return entries


def evidence_for(question_no: str, node: str) -> tuple[str, str]:
    if question_no == "Q4":
        return ("教师版客观答案/解析+题面正确项；非主观评分细则", "Q4 is objective-choice evidence only; do not upgrade to subjective rubric.")
    if question_no == "Q7":
        return ("教师版客观答案/解析+题面正确项；非主观评分细则", "Q7 is objective-choice evidence only; current DOCX placement is retained and registered.")
    if question_no == "Q16":
        return ("正式PPT评分细则+教师版题面/解析+当前DOCX正文", "Q16 formal rubric supports multiple philosophy nodes; each entry remains tied to rubric-listed principles.")
    if question_no == "Q17":
        return ("正式PPT评分细则+教师版题面/解析+当前DOCX正文", "Q17 only registers the people/history philosophy point;全过程人民民主等政治点 are not imported into philosophy nodes.")
    return ("题面+模块边界", "Boundary row.")


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    shutil.copy2(LEDGER, LEDGER.with_name(f"docx_insert_ledger_backup_before_batch22_2025_fengtai_final_{timestamp}.csv"))
    shutil.copy2(
        ACCEPTED,
        ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch22_2025_fengtai_final_{timestamp}.jsonl"),
    )

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

    accepted_records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
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
                "source_lane": "Codex Batch22 Fengtai final insertion and registration",
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


def next_matrix_id(rows: list[dict[str, str]]) -> int:
    max_id = 0
    for row in rows:
        value = row.get("matrix_row_id", "")
        if re.match(r"^M\d+$", value):
            max_id = max(max_id, int(value[1:]))
    return max_id + 1


def q_sort(question_no: str) -> tuple[int, str]:
    m = re.search(r"Q(\d+)", question_no)
    return (int(m.group(1)) if m else 999, question_no)


def body_rule_for(e: dict[str, str]) -> str:
    q = e["question_no"]
    node = e["canonical_node"]
    if q == "Q4":
        return "教师版答案A，正确项①③明确为“在为国尽责、为民服务的实践中实现个人价值、展现人生风采”和修身立德、服务他人社会。"
    if q == "Q7":
        return "教师版答案C，正确项为“从实际出发，从当下做起，生活才能少些迷茫”；漫画解析围绕把握当下现实处境。"
    if q == "Q17":
        return "正式PPT评分细则第55、71行：人民性是马克思主义的本质属性/人民群众是历史的创造者；可替换群众观点。"
    if q == "Q16":
        if node == "规律的客观性":
            return "正式PPT细则第255行列“规律”，材料强调数量界限和不按规律会犯错。"
        if node == "系统观念 / 系统优化":
            return "正式PPT细则第256-257行明列系统优化、整体部分；示例答案要求坚持系统观念。"
        if node == "发展的观点 / 发展的普遍性":
            return "正式PPT细则第208、257、260行明列发展/发展观；题干“看长远”支持发展过程视角。"
        if node == "认识对实践的反作用":
            return "正式PPT细则第209、257行明列认识对实践的反作用；题干写做计划、定方案和国家治理。"
        if node == "价值观的导向作用":
            return "正式PPT细则第257行明列正确的价值观；数据使用方向由正确价值观导向。"
        return "正式PPT细则第205-263行支持实践、实际出发、联系观、量变质变、矛盾观等，当前DOCX已有正文条目。"
    return "当前DOCX登记条目。"


def build_matrix_rows(entries: list[dict[str, str]], start_id: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def mid() -> str:
        nonlocal start_id
        value = f"M{start_id:04d}"
        start_id += 1
        return value

    new_nodes = {(entry["question_no"], entry["canonical_node"]) for entry in NEW_ENTRIES}
    for e in entries:
        evidence, boundary = evidence_for(e["question_no"], e["canonical_node"])
        action = "INSERTED_DOCX_BATCH22_FENGTAI_FINAL" if (e["question_no"], e["canonical_node"]) in new_nodes else "REGISTERED_EXISTING_DOCX_BATCH22_FENGTAI_FINAL"
        rows.append(
            {
                "matrix_row_id": mid(),
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": e["question_no"],
                "题型或模块判断": "哲学正文条目",
                "是否进宝典": "是：已进入当前DOCX/PDF正文",
                "宝典节点": e["canonical_node"],
                "细则支持原理": body_rule_for(e),
                "证据等级": evidence,
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": action,
                "备注": boundary,
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
    return rows


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    shutil.copy2(MATRIX, RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch22_2025_fengtai_final_{timestamp}.csv")
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = [r for r in reader if r.get("row_source") != MATRIX_SOURCE]
    new_rows = build_matrix_rows(entries, next_matrix_id(rows))
    new_rows.sort(key=lambda r: (q_sort(r["题号"]), r["宝典节点"]))
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    return {
        "matrix_rows": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "body_rows": sum(1 for r in new_rows if r["是否进宝典"].startswith("是")),
        "boundary_rows": sum(1 for r in new_rows if not r["是否进宝典"].startswith("是")),
    }


def update_global_audit(docx_mentions: int, matrix_rows_for_suite: int) -> dict[str, int]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    updated = False
    for row in rows:
        if row.get("normalized_suite") == SUITE or row.get("raw_suite") == SUITE:
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = str(matrix_rows_for_suite)
            row["current_docx_mentions"] = str(docx_mentions)
            row["current_status"] = "covered_by_batch22_recovery_matrix"
            row["blocker_or_next_action"] = "Batch22 added question-level disposition rows, registered inherited DOCX entries, inserted six missing DOCX entries; render/model gates pending."
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
- current recovery matrix rows for `{SUITE}`: `{matrix_rows_for_suite}`
- current DOCX mentions for `{SUITE}`: `{docx_mentions}`

## Batch22 Finding

`{SUITE}` is now covered by question-level recovery matrix rows. Q4, Q7, Q16, and Q17 have governed DOCX entries; remaining questions/subparts are explicit module-boundary exclusions.

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
    return {"remaining_gap": len(missing), "covered_rows": len(covered)}


def write_reports(
    docx_backup: Path,
    inserted: int,
    entries: list[dict[str, str]],
    ledger_result: dict[str, int],
    matrix_result: dict[str, int],
    global_result: dict[str, int],
) -> None:
    entry_lines = "\n".join(f"- {e['question_no']} -> `{e['canonical_node']}` -> `{e['inserted_heading']}`" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(
        f"""# Batch22 Source Transcription - 2025丰台期末

Status: `SOURCE_REVIEWED_BATCH22`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- formal rubric cache: `{RUBRIC_SOURCE}`
- teacher-version paper cache: `{TEACHER_SOURCE}`
- raw rubric: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025丰台期末\\细则\\2025丰台期末细则.pptx`
- raw teacher paper: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025丰台期末\\试卷\\2025北京丰台高三（上）期末政治（教师版）.pdf`

## Source Facts

- Teacher-version answer key: `1B 2D 3B 4A 5A 6A 7C 8D 9D 10B 11D 12B 13C 14C 15A`.
- Q4 answer A supports only an objective-choice `实现人生价值` placement.
- Q7 answer C was already in current DOCX under `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`; Batch22 registers it rather than duplicating it.
- Q16 formal PPT rubric lines 205-210 and 254-263 support practice, actual conditions,规律,主观能动性,质量互变,系统优化,整体部分,矛盾,发展,认识对实践的反作用,意识能动作用,正确价值观.
- Q17 formal PPT rubric lines 53-73 support only the 必修四 historical-materialism point `人民群众是历史的创造者 / 群众观点`; `全过程人民民主` remains政治与法治边界.
- Q18-Q21 are module-boundary rows except Q17's people-history point; ordinary reference answers are not treated as detailed philosophy rubrics.

## Current DOCX Entries After Batch22

{entry_lines}

## Guardrail

- Objective-choice evidence is not upgraded to subjective scoring-rule evidence.
- Formal PPT scoring rules are used for Q16/Q17 principle landings.
- No Sonnet/Haiku/model-unknown evidence is counted as qualified ClaudeCode evidence.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
""",
        encoding="utf-8",
    )

    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch22 - 2025丰台期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Scope

- Suite: `{SUITE}`
- Matrix row source: `{MATRIX_SOURCE}`
- DOCX backup before edit: `{docx_backup}`
- Newly inserted DOCX entries: `{inserted}`
- Total governed DOCX entries for this suite after Batch22: `{len(entries)}`

## Counts

- Full matrix total rows: `{matrix_result['matrix_rows']}`
- Batch22 rows: `{matrix_result['batch_rows']}`
- Batch22 body rows: `{matrix_result['body_rows']}`
- Batch22 boundary rows: `{matrix_result['boundary_rows']}`
- Ledger total rows: `{ledger_result['ledger_rows']}`
- Ledger rows added: `{ledger_result['ledger_added']}`
- Accepted JSONL total rows: `{ledger_result['accepted_rows']}`
- Accepted JSONL rows added: `{ledger_result['accepted_added']}`
- Remaining raw midterm/final source gap after Batch22: `{global_result['remaining_gap']}`

## Disposition

- Q4 inserted under `实现人生价值` using teacher-version objective answer A and correct-option chain only.
- Q7 retained and registered under current DOCX placement; no duplicate inserted.
- Q16 inherited eight current DOCX entries and inserted five missing formal-rubric-supported entries: `规律的客观性`, `系统观念 / 系统优化`, `发展的观点 / 发展的普遍性`, `认识对实践的反作用`, `价值观的导向作用`.
- Q17 retained and registered under `人民群众`; its political democracy points are not imported into philosophy nodes.
- Q1-Q3, Q5-Q6, Q8-Q15, Q18-Q21 are closed as module-boundary rows.

## Pending Gates

- Render/format QA is pending for Batch22.
- ClaudeCode Opus 4.7 production-lane recheck is pending.
- Model-effort/adaptive proof gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
""",
        encoding="utf-8",
    )

    append_block = f"""

## Batch22 Recovery Update: 2025丰台期末
Updated: 2026-05-25

- Verdict: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Coverage: `2025丰台期末` matrix rows `{matrix_result['batch_rows']}`, body rows `{matrix_result['body_rows']}`, boundary rows `{matrix_result['boundary_rows']}`.
- DOCX: `{inserted}` new entries inserted; inherited Q7/Q16/Q17 entries registered into ledger and accepted JSONL.
- Evidence quality: Q4/Q7 are objective-answer-key chains only; Q16/Q17 body entries are supported by formal PPT scoring rules. Ordinary reference answers are not treated as detailed rubrics.
- Global source-scope gap is reduced to `{global_result['remaining_gap']}` suites.
- Render QA and ClaudeCode Opus 4.7 recheck remain pending; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; GPTPro/Claude external reviews remain `real_call_pending`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch22 Recovery Update: 2025丰台期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8")


def main() -> int:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    entries = extract_docx_entries()
    if len(entries) < 16:
        raise RuntimeError(f"Expected at least 16 {SUITE} entries after Batch22, found {len(entries)}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), matrix_result["batch_rows"])
    write_reports(backup, inserted, entries, ledger_result, matrix_result, global_result)
    print(
        json.dumps(
            {
                "inserted": inserted,
                "docx_entries": len(entries),
                "ledger": ledger_result,
                "matrix": matrix_result,
                "global": global_result,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
