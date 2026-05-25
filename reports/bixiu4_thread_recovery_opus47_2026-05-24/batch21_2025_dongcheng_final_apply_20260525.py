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

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH21_2025_DONGCHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH21_2025_DONGCHENG_FINAL_CODEX_20260525.md"

PREPROCESSED = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区期末__2025东城期末.md"
LECTURE_SOURCE = PREPROCESSED / "gpt_sources" / "5b78436dd863858b_2025_1东城讲评_修改.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "26b1173765262a2f_2025东城期末细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "8eda36bd87dba194_2025北京东城高三_上_期末政治_教师版.md"

SUITE = "2025东城期末"
YEAR = "2025"
STAGE = "期末"
BATCH_ID = "batch21_2025_dongcheng_final"
MATRIX_SOURCE = "codex_batch21_2025_dongcheng_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {LECTURE_SOURCE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    "current DOCX text verified after Batch21 insertion"
)

NEW_ENTRIES = [
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q4",
        "heading_suffix": "2025东城期末 第4题（选择题）",
        "material_trigger": "殷墟甲骨文距今三千多年，汉字结构依然未变。题干从“点”“横”“竖”到横、撇、捺、提、折、钩，说明不同笔画既有区别又统一于汉字结构之中；教师版正确项①明确写出“在笔画的对立统一中彰显中华汉字之美”。",
        "question_prompt": "殷墟甲骨文距今三千多年，汉字结构依然未变。材料说明汉字之美如何生成？正确项包含①在笔画的对立统一中彰显中华汉字之美、②汉字笔画蕴含着人们的精神向往和美好追求，答案为A。",
        "why_trigger": "看到“点、横、竖”等笔画各有姿态，又共同构成一个有气韵、有布局的汉字整体，就要落到矛盾双方既对立又统一。这里的“对立”不是冲突破坏，而是差异、主次、长短、布局留白等不同规定性；“统一”是这些差异在一个汉字结构中相互依存、共同呈现美。",
        "answer_landing": "本题可用“矛盾就是对立统一”说明①：汉字笔画之美正是在不同笔画的差异、制约和协调统一中生成的。②属于文化与精神追求表达，可保留在答案理解中；③把个性寓于共性之中不合题意，④把主笔说成唯一核心而忽视整体结构，均不选。本条证据只来自客观题正确项和解析，不冒充主观题评分细则。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q16",
        "heading_suffix": "2025东城期末 第16题（主观题）",
        "material_trigger": "设问要求运用《哲学与文化》知识理解“器以述史、物以载道”。讲评细则第三层明确要求“正确发挥主观能动性，提高对器物价值的认识，做好搜集、保护、研究工作”，教师版解析也写到“意识具有能动作用，能指导人们认识世界和改造世界”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，谈谈你对“器以述史、物以载道”的理解。",
        "why_trigger": "材料不是单纯让学生复述何尊的文化价值，还要求回答“我们该怎么做”。一旦材料从“器物承载历史和文化”推进到“提高认识、保护研究、传播利用”，就进入意识能动作用：正确认识器物价值，可以指导人们做好文物搜集、保护、研究和传播。",
        "answer_landing": "作答时先承认器物作为中华文化载体和中华文明特征的材料意义，再落到本节点：意识具有能动作用，正确意识能指导人们认识世界和改造世界。对何尊等器物价值的正确认识，能够引导我们加强保护、研究和阐释，用文物讲好中华文明故事，推动中华优秀传统文化创造性转化、创新性发展。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q21",
        "heading_suffix": "2025东城期末 第21题（主观题）",
        "material_trigger": "材料明确给出“中国式现代化，民生为大是价值取向，更是实践要求”。评分细则把“价值取向”层面写为人民性、群众观、价值观、价值判断标准、党的宗旨、初心等；材料二列出居民收入、医保、教育、体育场地、基层立法联系点、民生“小案件”和文化惠民等事实。",
        "question_prompt": "中国式现代化，民生为大是价值取向，更是实践要求。结合材料，综合运用所学，谈谈你对这句话的理解。",
        "why_trigger": "题干把“民生为大”界定为价值取向，说明现代化建设要先回答“为了谁、以什么标准评价政策和行动”。看到“人民立场”“民生无小事”“发展向前、民生向暖”和治理重民生，就应落到正确价值判断和价值选择必须符合人民群众的根本利益。",
        "answer_landing": "正确的价值判断和价值选择要自觉站在最广大人民的立场上，把人民群众的利益作为最高价值标准。中国式现代化坚持民生为大，就是在发展、立法、司法、公共服务和文化惠民等决策中，以是否保障和发展人民利益、是否让发展成果更多更公平惠及人民为评价尺度，并把这种价值取向转化为持续改善民生的制度安排和实践行动。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "heading_suffix": "2025东城期末 第21题（主观题）",
        "material_trigger": "材料一强调“民生无小事枝叶总关情”，图示与细则均指向人民立场、群众观；材料二写到发展为民生、治理重民生，居民意见通过基层立法联系点进入国家立法，检察机关办好民生“小案件”，政府推进文化惠民工程。",
        "question_prompt": "中国式现代化，民生为大是价值取向，更是实践要求。结合材料，综合运用所学，谈谈你对这句话的理解。",
        "why_trigger": "题目把民生、人民立场、基层民意、为民司法和公共文化服务放在同一链条中，说明中国式现代化不是抽象指标增长，而是依靠人民、为了人民、由人民评价的现代化。这里可落到人民群众是社会历史主体以及群众观点、群众路线。",
        "answer_landing": "人民群众是社会历史的主体，是历史的创造者。中国式现代化必须坚持人民主体地位，把人民对美好生活的需要作为奋斗目标；在发展中增进民生福祉，在治理中听民声、汇民智、解民忧，使立法、司法、公共服务和文化建设回应群众真实需要。这样才能把“民生为大”的价值立场转化为可感可及的现代化成果。",
    },
]

BOUNDARY_ROWS = [
    ("Q1", "中国特色社会主义选择题", "否：模块边界排除", "改革开放意义/中国特色社会主义边界", "教师版解析：改革开放是坚持和发展中国特色社会主义的必由之路；不作为必修四哲学正文条目。", "教师版客观答案/解析+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "不进入必修四哲学宝典。"),
    ("Q2", "中国特色社会主义选择题", "否：模块边界排除", "长征精神/党的建设与中国特色社会主义边界", "题面围绕新时代长征路、思想指导和长征精神；未形成当前必修四哲学正文落点。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "不进入必修四哲学宝典。"),
    ("Q3", "文化选择题", "否：哲学正文边界排除", "文化功能/文化认同边界", "澳门回归与“一国两制”材料主要落在文化、制度与国家认同表达；不扩展为哲学节点。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "文化角度不进入当前哲学正文。"),
    ("Q5", "逻辑与思维选择题", "否：模块边界排除", "辩证思维/整体动态/矛盾分析法边界", "题干评论社区空间“小修小补”，正确项落在选必三辩证思维表达；不把“整体和动态”“矛盾分析法”偷换为必修四正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "不进入必修四哲学宝典。"),
    ("Q6", "政治与法治选择题", "否：模块边界排除", "人民代表大会制度/科学民主立法边界", "题干围绕全国人大及其常委会行使立法权、公开征求意见和科学民主立法。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "政治与法治边界。"),
    ("Q7", "经济与社会选择题", "否：模块边界排除", "宏观政策传导/经济高质量发展边界", "题干为促进经济增长一揽子政策及传导路径判断，属于经济模块。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "经济与社会边界。"),
    ("Q8", "当代国际政治与经济选择题", "否：模块边界排除", "国际关系/国际经济边界", "题干落在国际政治经济材料，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必一边界。"),
    ("Q9", "当代国际政治与经济选择题", "否：模块边界排除", "国际贸易/全球治理边界", "题干落在国际政治经济材料，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必一边界。"),
    ("Q10", "当代国际政治与经济选择题", "否：模块边界排除", "国际组织/国际经济边界", "题干落在国际政治经济材料，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必一边界。"),
    ("Q11", "法律与生活选择题", "否：模块边界排除", "民事权利义务/法律生活边界", "题干落在法律与生活，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必二边界。"),
    ("Q12", "法律与生活选择题", "否：模块边界排除", "民事法律关系边界", "题干落在法律与生活，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必二边界。"),
    ("Q13", "逻辑与思维选择题", "否：模块边界排除", "判断/推理/逻辑规则边界", "题干落在逻辑与思维，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必三边界。"),
    ("Q14", "逻辑与思维选择题", "否：模块边界排除", "科学思维/推理边界", "题干落在逻辑与思维，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必三边界。"),
    ("Q15", "逻辑与思维选择题", "否：模块边界排除", "逻辑与思维边界", "题干落在逻辑与思维，不进入必修四哲学正文。", "教师版客观答案/题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必三边界。"),
    ("Q17", "法律与生活/政治与法治主观题", "否：模块边界排除", "生态司法/法治作用边界", "讲评细则按法院审判、公正司法、生态修复、公开道歉和法治教育给分，属于法治知识。", "正式讲评/评分细则+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "不进入必修四哲学宝典。"),
    ("Q18(1)", "经济与社会主观题", "否：模块边界排除", "数字经济/公共文化服务经济边界", "题目第一问不属于必修四哲学正文。", "题面+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "经济与社会边界。"),
    ("Q18(2)", "逻辑与思维主观题", "否：模块边界排除", "创新思维建设公共文化空间边界", "题干明确要求分析北京城市图书馆如何运用创新思维建设新型公共文化空间。", "题面明确限定《逻辑与思维》", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必三边界。"),
    ("Q19(1)", "法律与生活主观题", "否：模块边界排除", "农村土地确权登记/法治现实意义边界", "题干要求运用法治知识阐释农村土地确权登记的现实意义。", "题面+讲评/评分细则", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "法治边界。"),
    ("Q19(2)", "法律与生活主观题", "否：模块边界排除", "民法典侵权责任/权利义务边界", "题干围绕民法典侵权责任编解释条款分析。", "题面+讲评/评分细则", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "法律与生活边界。"),
    ("Q19(3)", "政治与法治主观题", "否：模块边界排除", "民生领域立法/司法/治理边界", "题目落在法治与政治治理链条；不作为必修四哲学正文条目。", "题面+讲评/评分细则", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "政治与法治边界。"),
    ("Q20", "当代国际政治与经济主观题", "否：模块边界排除", "新能源汽车贸易争端/国际政治经济边界", "题干明确要求运用《当代国际政治与经济》知识写短文。", "题面明确限定《当代国际政治与经济》", "MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL", "选必一边界。"),
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
    backup = docx.with_name(f"{docx.stem}_backup_before_batch21_2025_dongcheng_final_{timestamp}.docx")
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
        body_template = next(
            (p for p in paras[section_idx + 1 : end_idx] if para_text(p).startswith("【材料触发点】")),
            None,
        )
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
    if question_no == "Q4":
        return (
            "教师版客观答案/解析+题面正确项；非主观评分细则",
            "选择题客观答案只能证明正确项进入该哲学节点；不冒充主观题评分细则。",
        )
    if question_no == "Q16":
        return (
            "正式讲评/评分细则+教师版解析+当前DOCX正文",
            "Q16第三层明确给出主观能动性/意识能动作用落点；文化载体等文化点不扩展为哲学正文新节点。",
        )
    if question_no == "Q21":
        return (
            "正式讲评/评分细则+题面材料+当前DOCX正文",
            "Q21是综合题；本批只登记价值判断与价值选择、人民群众两个有细则支撑的哲学角度，不把综合题全答案压成单一哲学节点。",
        )
    return ("题面+模块边界", "边界行。")


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    shutil.copy2(LEDGER, LEDGER.with_name(f"docx_insert_ledger_backup_before_batch21_2025_dongcheng_final_{timestamp}.csv"))
    shutil.copy2(
        ACCEPTED,
        ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch21_2025_dongcheng_final_{timestamp}.jsonl"),
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
                "source_lane": "Codex Batch21 Dongcheng final insertion and registration",
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


def build_matrix_rows(entries: list[dict[str, str]], start_id: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def mid() -> str:
        nonlocal start_id
        value = f"M{start_id:04d}"
        start_id += 1
        return value

    for e in entries:
        evidence, boundary = evidence_for(e["question_no"], e["canonical_node"])
        if e["question_no"] == "Q4":
            qtype = "选择题哲学：本批补入正文"
            rule = "教师版答案A，正确项①为“在笔画的对立统一中彰显中华汉字之美”；本证据只用于客观题节点定位。"
            action = "INSERTED_DOCX_BATCH21_DONGCHENG_Q4"
            note = boundary
        elif e["question_no"] == "Q16":
            qtype = "主观题哲学与文化：本批补入正文"
            rule = "讲评细则第三层：正确发挥主观能动性，提高对器物价值的认识，做好搜集、保护、研究工作；教师版解析含意识能动作用。"
            action = "INSERTED_DOCX_BATCH21_DONGCHENG_Q16"
            note = boundary
        elif e["question_no"] == "Q21" and e["canonical_node"] == "价值判断与价值选择":
            qtype = "综合主观题：本批补入正文"
            rule = "评分细则价值取向层：人民性、群众观、价值观、价值判断标准、党的宗旨、初心等；题面给出“民生为大是价值取向”。"
            action = "INSERTED_DOCX_BATCH21_DONGCHENG_Q21_VALUE"
            note = boundary
        elif e["question_no"] == "Q21" and e["canonical_node"] == "人民群众":
            qtype = "综合主观题：本批补入正文"
            rule = "评分细则价值取向层列出人民性/群众观，材料链条为人民立场、发展为民生、治理重民生。"
            action = "INSERTED_DOCX_BATCH21_DONGCHENG_Q21_PEOPLE"
            note = boundary
        else:
            qtype = "哲学正文条目"
            rule = evidence
            action = "INSERTED_DOCX_BATCH21_DONGCHENG"
            note = boundary

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
    return rows


def q_sort(question_no: str) -> tuple[int, str]:
    m = re.search(r"Q(\d+)", question_no)
    return (int(m.group(1)) if m else 999, question_no)


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    shutil.copy2(MATRIX, RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch21_2025_dongcheng_final_{timestamp}.csv")
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
            row["current_status"] = "covered_by_batch21_recovery_matrix"
            row["blocker_or_next_action"] = "Batch21 added question-level disposition rows and four DOCX entries; render/model gates pending."
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

## Batch21 Finding

`{SUITE}` is now covered by question-level recovery matrix rows. Q4, Q16, and Q21 have student-facing DOCX entries; the remaining questions are explicit module-boundary exclusions.

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
        f"""# Batch21 Source Transcription - 2025东城期末

Status: `SOURCE_REVIEWED_BATCH21`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- lecture/report cache: `{LECTURE_SOURCE}`
- formal rubric cache: `{RUBRIC_SOURCE}`
- teacher-version paper cache: `{TEACHER_SOURCE}`
- raw suite directory: `C:/Users/Administrator/Desktop/2025各区模拟题/2025各区期末/2025东城期末`

## Source Findings

- Q4: teacher-version objective answer supports item 1, `在笔画的对立统一中彰显中华汉字之美`; this is objective-answer evidence only.
- Q16: prompt is `结合材料，运用《哲学与文化》知识，谈谈你对“器以述史、物以载道”的理解。`
- Q16 formal lecture/rubric support: third layer requires correct use of subjective initiative / consciousness's active role to improve understanding of artifact value and do collection, protection, and research work.
- Q21: prompt is `中国式现代化，民生为大是价值取向，更是实践要求。结合材料，综合运用所学，谈谈你对这句话的理解。`
- Q21 rubric support: value orientation includes人民性、群众观、价值观、价值判断标准等；practice requirement includes development for livelihood and governance focused on livelihood.
- Q17, Q18, Q19, and Q20 are not promoted into this philosophy body because their prompts/rubrics are law, logic-thinking, political-law, economic, or international-political-economy boundaries.

## Current DOCX Entries After Batch21

{entry_lines}

## Evidence Discipline

- Ordinary reference answers are not treated as subjective scoring rubrics.
- Q4 uses objective answer evidence only.
- Q16 and Q21 use lecture/rubric evidence.
- Q21 is a综合题; the two philosophy entries are angle-level supported landings, not a claim that the whole answer is only philosophy.
""",
        encoding="utf-8",
    )

    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch21 - 2025东城期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Codex Lane Decision

- DOCX entries inserted: `{inserted}`.
- DOCX backup: `{docx_backup}`.
- Current suite entries in DOCX: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`; accepted records added: `{ledger_result['accepted_added']}`.
- Matrix rows added: `{matrix_result['batch_rows']}` (`{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows).
- Global raw-suite gap after Batch21: `{global_result['remaining_gap']}`.

## Question Coverage

- Q4 enters `矛盾就是对立统一` from teacher-version objective answer evidence.
- Q16 enters `主观能动性 / 意识的能动作用` from formal lecture/rubric third-layer evidence.
- Q21 enters `价值判断与价值选择` and `人民群众` from formal rubric value-orientation evidence.
- Q1-Q3, Q5-Q15, Q17-Q20 are closed by explicit module-boundary rows.

## Remaining Gates

- Render QA pending.
- ClaudeCode Opus 4.7 production-lane recheck pending.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
""",
        encoding="utf-8",
    )

    status_append = f"""

## Batch21 Update: 2025东城期末 - 2026-05-25

- status: `RECOVERED_EXECUTION_IN_PROGRESS`
- batch state: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`
- files created/updated: `batch21_2025_dongcheng_final_apply_20260525.py`, `BATCH21_2025_DONGCHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md`, `COVERAGE_FUSION_BATCH21_2025_DONGCHENG_FINAL_CODEX_20260525.md`, `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md/.csv`, `docx_insert_ledger.csv`, `student_patch_entries.accepted.jsonl`, current DOCX.
- student-facing entries inserted: `{inserted}`; current `{SUITE}` DOCX entries: `{len(entries)}`.
- matrix rows added: `{matrix_result['batch_rows']}`; all Q1-Q21 dispositions are recorded.
- global source-scope gap reduced to `{global_result['remaining_gap']}` remaining midterm/final suites.
- render state: pending.
- ClaudeCode evidence: pending.
- model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- external reviews: GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
"""
    THREAD_STATUS.write_text(THREAD_STATUS.read_text(encoding="utf-8") + status_append, encoding="utf-8")

    governor_append = f"""

## Governor Batch21 Recovery Finding: 2025东城期末
Updated: 2026-05-25

- Verdict: Batch21 Codex lane is `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Coverage: `{SUITE}` has `{matrix_result['batch_rows']}` matrix rows and `{len(entries)}` DOCX entries.
- Evidence quality: Q4 is objective-answer evidence only; Q16/Q21 use lecture/rubric evidence. Ordinary teacher answers are not promoted into scoring rules.
- Boundary discipline: Q17-Q20 and non-Bixiu4 objective questions are excluded by module-boundary rows.
- Global source-scope gap remains open at `{global_result['remaining_gap']}` raw midterm/final suites.
- Render QA and ClaudeCode Opus 4.7 gates still need to run for this batch; external GPTPro/Claude full-artifact reviews remain `real_call_pending`.
"""
    GOVERNOR.write_text(GOVERNOR.read_text(encoding="utf-8") + governor_append, encoding="utf-8")

    confucius_append = f"""

## Confucius Batch21 Artifact Check: 2025东城期末
Updated: 2026-05-25

- Verdict: student-facing artifact update is applied but not yet render/model closed.
- Student-facing additions: Q4 under `矛盾就是对立统一`, Q16 under `主观能动性 / 意识的能动作用`, Q21 under `价值判断与价值选择`, and Q21 under `人民群众`.
- Teaching boundary: Q4 is marked as objective-answer evidence; Q16/Q21 use lecture/rubric support. The Q21综合题 is not reduced to a single philosophy answer.
- Boundary discipline: non-Bixiu4 questions are closed by explicit matrix boundary rows.
- Remaining blockers: render QA and ClaudeCode Opus 4.7 batch recheck are pending; global source-scope gap remains `{global_result['remaining_gap']}` suites; GPTPro and external Claude full-artifact reviews remain `real_call_pending`.
"""
    CONFUCIUS.write_text(CONFUCIUS.read_text(encoding="utf-8") + confucius_append, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_backup, inserted = update_docx(timestamp)
    entries = extract_docx_entries()
    if len(entries) != 4:
        raise RuntimeError(f"Expected 4 {SUITE} DOCX entries after insertion, found {len(entries)}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(docx_mentions=len(entries), matrix_rows_for_suite=matrix_result["batch_rows"])
    write_reports(docx_backup, inserted, entries, ledger_result, matrix_result, global_result)
    print(
        json.dumps(
            {
                "docx_backup": str(docx_backup),
                "inserted": inserted,
                "entries": len(entries),
                "ledger": ledger_result,
                "matrix": matrix_result,
                "global": global_result,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
