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
REPORT_MD = RECOVERY / "DONGCHENG_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "DONGCHENG_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
UPLOAD_SCOPE = RECOVERY / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"

SUITE = "2026东城一模"
YEAR = "2026"
STAGE = "一模"
SOURCE_BUNDLE = (
    "preprocessed_corpus\\gpt_suite_bundles\\"
    "2026各区模拟题__2026各区一模__2026东城一模.md"
)

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

ENTRIES = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q1",
        "heading_suffix": "2026东城一模 第1题（选择题）",
        "material_trigger": "题干要求评价我国经济在复杂严峻环境下交出的“六字”成绩单；正确项③明确写出“只有一切从实际出发，实事求是，才能持续向新向优”。",
        "question_prompt": "2025年，面对复杂严峻的国内外环境，我国经济交出“六字”亮眼成绩单。正确组合为B（①③）。本条只处理③：一切从实际出发、实事求是与持续向新向优的关系。",
        "why_trigger": "看到“复杂严峻环境”“持续向新向优”，不能把成绩理解成主观愿望直接生成，而要从客观实际出发，把经济治理建立在真实国情、形势变化和规律把握之上。",
        "answer_landing": "本题应选B。本节点只处理③：推动经济持续向新向优，必须坚持一切从实际出发、实事求是，把主观决策同客观国情、发展阶段和现实问题具体地历史地统一起来。选择题边界已明示；非主观题评分细则。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:334-341; {SOURCE_BUNDLE}:594-600",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q2",
        "heading_suffix": "2026东城一模 第2题（选择题）",
        "material_trigger": "隆福寺街区中老字号、文创、新式饮品、非遗沉浸体验和机器人科技共同出现；正确项③明确写出“文化与经济的对立统一推动街区业态迭代与功能升级”。",
        "question_prompt": "北京隆福寺街区成为兼具烟火气与时尚感的城市地标。正确组合为A（①③）。本条只处理③：文化与经济的对立统一。",
        "why_trigger": "材料把传统商业、文化体验、科技活力和消费场景放在同一街区中，说明文化与经济不是割裂的两个方面，而是在相互作用、相互促进中推动街区功能升级。",
        "answer_landing": "本题应选A。本节点只处理③：文化与经济既有区别又相互联结、相互作用，隆福寺街区正是在传统文化资源与消费业态的对立统一中实现迭代升级。选择题边界已明示；非主观题评分细则。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:342-348; {SOURCE_BUNDLE}:594-600",
    },
    {
        "canonical_node": "认识发展原理",
        "question_no": "Q5",
        "heading_suffix": "2026东城一模 第5题（选择题）",
        "material_trigger": "专家团队收集、分析海量影像数据，把握中国人群脑结构动态变化，区分疾病对应指标偏离特征，并形成脑结构正常参考值；正确项B指向“获得规律性认识”。",
        "question_prompt": "国内专家团队成功构建中国人群全生命周期的脑结构正常参考值。正确答案为B：通过分析综合海量数据获得中国人群脑结构的规律性认识。",
        "why_trigger": "从海量影像数据到动态变化、指标偏离特征、正常参考值，是从感性材料到理性把握的认识深化过程；学生应抓住“分析综合”和“规律性认识”。",
        "answer_landing": "本题应选B。通过收集、分析和综合大量数据，人们能够把握对象内部稳定联系和变化规律，使认识由零散材料上升为规律性认识，并服务临床诊断。选择题边界已明示；非主观题评分细则。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:369-375; {SOURCE_BUNDLE}:594-600",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q8",
        "heading_suffix": "2026东城一模 第8题（选择题）",
        "material_trigger": "《北京市养老服务条例》把基本养老、市场化养老、社会互助共济养老放在同一养老服务体系中统筹；正确项①写出“推进各类养老资源统筹，系统性提升养老服务供给水平”。",
        "question_prompt": "《北京市养老服务条例》规定本市养老服务包括基本养老服务、市场化养老服务和社会互助共济养老服务。正确组合为A（①③）。本条只处理①的系统性养老服务供给。",
        "why_trigger": "看到“体系”“包括多类服务”“资源统筹”，应从系统观念理解：养老服务不是单一供给，而是多主体、多类型、多环节协同优化。",
        "answer_landing": "本题应选A。本节点只处理①：提升养老服务供给水平，要统筹基本养老、市场化养老和社会互助共济养老等资源，立足养老服务体系整体，优化结构和协同关系。选择题边界已明示；非主观题评分细则。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:398-408; {SOURCE_BUNDLE}:594-600",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q16",
        "heading_suffix": "2026东城一模 第16题（主观题）",
        "material_trigger": "题目把“大众情绪”与“时代情感”对照，细则明确要求把时代情感转化为社会主义核心价值观、中华民族精神等关键概念，并强调优秀文艺要弘扬和践行民族精神和核心价值观。",
        "question_prompt": "有人认为：能够满足大众情绪需求的文艺，就是优秀文艺。结合材料，运用《哲学与文化》知识，评析这一观点。",
        "why_trigger": "“唯有以情铸魂，方能涵养根脉”“家国之情”“烈士豪情”“劳动者之歌”都不是一般情绪满足，而是价值导向、民族精神和核心价值观的承载。学生应从价值观对文艺创作和社会发展的导向作用切入。",
        "answer_landing": "优秀文艺不能只满足瞬时情绪，还要以正确价值观引领人、塑造人，弘扬中华民族精神和社会主义核心价值观，把大众情绪提升为深沉的时代情感。题目观点把“满足情绪”当作唯一标准，忽视了优秀文艺的价值导向作用，因而是片面的。",
        "evidence_level": "正式PPT评分细则+核心考点（主观题细则）",
        "source_lines": f"{SOURCE_BUNDLE}:673-731",
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


def is_heading2(p) -> bool:
    return p_style(p) in {"Heading2", "2", "4"}


def is_heading3(p) -> bool:
    return p_style(p) in {"Heading3", "3", "5"}


def set_plain_text(p, text: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    r = etree.SubElement(p, W + "r")
    t = etree.SubElement(r, W + "t")
    t.text = text


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
        ppr = etree.Element(W + "pPr")
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def find_section(paras, heading: str) -> tuple[int, int]:
    start = next((i for i, p in enumerate(paras) if is_heading2(p) and para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if is_heading2(paras[i])), len(paras))
    return start, end


def section_templates(paras, start: int, end: int):
    heading_template = next((paras[i] for i in range(start + 1, end) if is_heading3(paras[i])), None)
    label_template = next(
        (paras[i] for i in range(start + 1, end) if not is_heading3(paras[i]) and para_text(paras[i]).strip().startswith("【")),
        None,
    )
    blank_template = next((paras[i] for i in range(start + 1, end) if not para_text(paras[i]).strip()), None)
    if heading_template is None or label_template is None:
        raise RuntimeError("Could not locate section templates")
    return heading_template, label_template, blank_template


def next_heading_number(paras, start: int, end: int) -> int:
    numbers = []
    for i in range(start + 1, end):
        if not is_heading3(paras[i]):
            continue
        text = para_text(paras[i]).strip()
        head = text.split(".", 1)[0]
        if head.isdigit():
            numbers.append(int(head))
    return (max(numbers) if numbers else 0) + 1


def insert_entries_into_docx(docx: Path, timestamp: str) -> dict[str, object]:
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_dongcheng_yimo_choice_culture_insert_{timestamp}.docx")
    shutil.copy2(docx, backup)

    inserted: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        document_xml = temp / "word" / "document.xml"
        tree = etree.parse(str(document_xml))
        root = tree.getroot()
        body = root.find("w:body", namespaces=NS)
        if body is None:
            raise RuntimeError("Missing word body")

        for entry in ENTRIES:
            paras = [p for p in body if p.tag == W + "p"]
            start, end = find_section(paras, entry["canonical_node"])
            if any(entry["heading_suffix"] in para_text(paras[i]) for i in range(start + 1, end)):
                continue
            heading_template, label_template, blank_template = section_templates(paras, start, end)
            number = next_heading_number(paras, start, end)
            heading_text = f"{number}. {entry['heading_suffix']}"
            new_nodes = []
            heading = deepcopy(heading_template)
            set_plain_text(heading, heading_text)
            new_nodes.append(heading)
            for label, key in LABELS:
                para = deepcopy(label_template)
                set_label_text(para, label, entry[key])
                new_nodes.append(para)
            if blank_template is not None:
                blank = deepcopy(blank_template)
                set_plain_text(blank, "")
                new_nodes.append(blank)
            insert_at = body.index(paras[end]) if end < len(paras) else len(body)
            for offset, node in enumerate(new_nodes):
                body.insert(insert_at + offset, node)
            inserted.append(heading_text)

        tree.write(str(document_xml), encoding="utf-8", xml_declaration=True, standalone=True)
        tmp_docx = temp / "updated.docx"
        with zipfile.ZipFile(tmp_docx, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path == tmp_docx or path.is_dir():
                    continue
                zout.write(path, path.relative_to(temp).as_posix())
        shutil.copy2(tmp_docx, docx)

    return {"docx_backup": str(backup), "inserted_headings": inserted}


def update_ledger(timestamp: str) -> dict[str, object]:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_dongcheng_yimo_choice_culture_insert_{timestamp}.csv")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    existing = {(r["canonical_node"], r["source_suite"], r["question_no"]) for r in rows}
    added = []
    for entry in ENTRIES:
        key = (entry["canonical_node"], SUITE, entry["question_no"])
        if key in existing:
            continue
        rows.append(
            {
                "canonical_node": entry["canonical_node"],
                "source_suite": SUITE,
                "question_no": entry["question_no"],
                "inserted_heading": entry["heading_suffix"],
            }
        )
        added.append(entry["heading_suffix"])
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger_backup": str(backup), "ledger_rows_added": added}


def source(*ranges: str) -> str:
    return "; ".join(f"{SOURCE_BUNDLE}:{r}" for r in ranges)


def set_fields(row: dict[str, str], **fields: str) -> None:
    for key, value in fields.items():
        row[key] = value


def update_matrix(timestamp: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_dongcheng_yimo_candidate_repair_{timestamp}.csv")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {row["matrix_row_id"]: row for row in rows}

    updates = {
        "M0524": ("Q1", "选择题 / 必修四正确项链条", "是：已补入当前DOCX", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一", "官方答案键B支持正确项③“一切从实际出发、实事求是”；选择题边界已明示，非主观题评分细则。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", source("334-341", "594-600"), "DOCX_INSERTED_Q1_CHOICE_CHAIN"),
        "M0525": ("Q2", "选择题 / 必修四正确项链条", "是：已补入当前DOCX", "矛盾就是对立统一", "官方答案键A支持正确项③“文化与经济的对立统一推动街区业态迭代与功能升级”；选择题边界已明示，非主观题评分细则。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", source("342-348", "594-600"), "DOCX_INSERTED_Q2_CHOICE_CHAIN"),
        "M0526": ("Q3", "选择题 / 模块边界排除", "否：模块边界排除", "不入宝典", "官方答案键C；题干指向青年科技创新、国际交流与教育育人成效，不构成必修四哲学/文化稳定原理链。", "官方答案键+题干模块边界", source("349-360", "594-600"), "EXCLUDED_EDUCATION_INTERNATIONAL_BOUNDARY"),
        "M0527": ("Q4", "选择题 / 弱文化效果项不单独进正文", "否：不单独进宝典", "不入宝典", "官方答案键A仅支持“唤醒中式美学与文化根脉共鸣”的文化效果判断；不得用未选项D或题面科技元素冒充守正创新/辩证否定细则。", "官方答案键+题干边界（选择题，非主观题评分细则）", source("361-368", "594-600"), "EXCLUDED_WEAK_CULTURE_EFFECT_CHOICE_BOUNDARY"),
        "M0528": ("Q5", "选择题 / 必修四正确项链条", "是：已补入当前DOCX", "认识发展原理", "官方答案键B支持“通过分析综合海量数据获得规律性认识”；选择题边界已明示，非主观题评分细则。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", source("369-375", "594-600"), "DOCX_INSERTED_Q5_CHOICE_CHAIN"),
        "M0529": ("Q6", "选择题 / 逻辑模块边界排除", "否：模块边界排除", "不入宝典", "官方答案键D；考查换质位推理，属于《逻辑与思维》边界；不得把错误项A/B作为必修四正文证据。", "官方答案键+题干模块边界", source("376-383", "594-600"), "EXCLUDED_XUANBISAN_LOGIC_BOUNDARY"),
        "M0530": ("Q8", "选择题 / 必修四正确项链条", "是：已补入当前DOCX", "系统观念 / 系统优化", "官方答案键A支持正确项①“推进各类养老资源统筹，系统性提升养老服务供给水平”；选择题边界已明示，非主观题评分细则。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", source("398-408", "594-600"), "DOCX_INSERTED_Q8_CHOICE_CHAIN"),
        "M0531": ("Q9", "选择题 / 政治法治边界排除", "否：模块边界排除", "不入宝典", "官方答案键D；题干与正确项指向健康学校建设、依法履行管理职责和现代化国家健康基石，不构成必修四稳定原理链。", "官方答案键+题干模块边界", source("409-416", "594-600"), "EXCLUDED_POLITICS_HEALTH_BOUNDARY"),
        "M0532": ("Q13", "选择题 / 经济模块边界排除", "否：模块边界排除", "不入宝典", "官方答案键C；货币政策传导路径属于经济与社会边界。", "官方答案键+题干模块边界", source("446-452", "594-600"), "EXCLUDED_ECONOMICS_BOUNDARY"),
        "M0533": ("Q14", "选择题 / 选必一边界排除", "否：模块边界排除", "不入宝典", "官方答案键B；中非关系、国际分工、对非政策理念属于当代国际政治与经济边界。", "官方答案键+题干模块边界", source("453-464", "594-600"), "EXCLUDED_XUANBIYI_BOUNDARY"),
        "M0534": ("Q15", "选择题 / 选必一边界排除", "否：模块边界排除", "不入宝典", "官方答案键A；外交微评与全球治理、人类命运共同体属于当代国际政治与经济边界。", "官方答案键+题干模块边界", source("465-486", "594-600"), "EXCLUDED_XUANBIYI_BOUNDARY"),
        "M0160": ("Q16", "主观题 / 哲学与文化综合", "是：已补入当前DOCX", "价值观的导向作用", "正式PPT细则列中华民族精神、社会主义核心价值观、发展中国特色社会主义文化等文化点；本轮补入价值导向条目，现有DOCX还覆盖矛盾主次方面、人民群众、社会意识、价值判断等哲学点。", "正式PPT评分细则+当前DOCX正文", source("673-731"), "DOCX_INSERTED_Q16_CULTURE_VALUE_CHAIN"),
        "M0219": ("Q16", "主观题 / 哲学与文化综合", "是：当前DOCX已覆盖", "矛盾的主要方面和次要方面 / 两点论与重点论", "正式PPT细则明确哲学核心考点含“矛盾的主次方面（情绪需求是次要方面，思想性、艺术性是主要方面）”；当前DOCX已有主次方面和两点论重点论条目。", "正式PPT评分细则+当前DOCX正文", source("694-713", "727-731"), "CURRENT_DOCX_VERIFIED_Q16_MAIN_SECONDARY_ASPECTS"),
        "M0535": ("Q16", "主观题 / 哲学与文化综合", "是：当前DOCX已覆盖", "人民群众 / 社会存在与社会意识 / 价值判断与价值选择", "正式PPT细则列人民是文化发展的主体、人民群众是社会历史主体、社会意识反作用、价值判断与价值选择等；当前DOCX已有对应多节点条目。", "正式PPT评分细则+当前DOCX正文", source("694-731"), "CURRENT_DOCX_VERIFIED_Q16_MULTI_NODE"),
        "M0536": ("Q17", "主观题 / 政治与法治边界排除", "否：模块边界排除", "不入宝典", "正式细则为全过程人民民主、人大、政协、政府、公民权利等政治与法治知识，不作必修四正文链。", "正式评分细则模块边界", source("89-136", "616-621", "738-796"), "EXCLUDED_POLITICS_LAW_BOUNDARY"),
        "M0537": ("Q18", "主观题 / 法律与生活边界排除", "否：模块边界排除", "不入宝典", "正式细则为诉讼调解、惩罚性赔偿、恶意诉讼、公正司法、知识产权等法律与生活知识；“矛盾/和谐价值观”等仅为法律语境，不生成必修四正文链。", "正式评分细则模块边界", source("138-176", "622-625", "800-908"), "EXCLUDED_LAW_BOUNDARY"),
        "M0538": ("Q19(4)", "主观题 / 必修四系统观念", "是：当前DOCX已覆盖", "系统观念 / 系统优化", "正式PPT细则明确系统观念知识1分，要求立足整体、综合思维、结构优化、整体功能等；当前DOCX已有Q19(4)系统观念条目。创新思维部分属于选必三边界，不在必修四正文扩展。", "正式PPT评分细则+当前DOCX正文", source("1059-1091"), "CURRENT_DOCX_VERIFIED_Q19_4_SYSTEM_ONLY"),
        "M0539": ("Q20", "主观题 / 综合所学含必修四", "是：当前DOCX已覆盖", "实践是认识的基础 / 认识发展原理 / 发展观 / 人民群众", "正式PPT细则明确实践与认识关系、发展观、人民角度等；当前DOCX已有实践、认识发展、发展观、人民群众等多节点条目。", "正式PPT评分细则+当前DOCX正文", source("1098-1148"), "CURRENT_DOCX_VERIFIED_Q20_MULTI_NODE"),
        "M0540": ("Qunknown", "套卷索引残留", "否：已由逐题行替代", "套卷索引残留", "原行为抽取残留/整包候选，不替代Q1-Q20逐题裁决；本轮已补齐缺失题号和Q19分问。", "套卷索引边界", source("1-18", "594-654"), "SUPERSEDED_BY_PER_QUESTION_ADJUDICATION"),
        "M0845": ("SUITE_LEVEL", "套卷级摘要", "否：套卷级摘要，不替代逐题入正文", "套卷级摘要", "套卷级覆盖摘要仅说明当前DOCX提及或闭合记录；本轮已逐题裁决。", "套卷级边界", source("1-18"), "SUITE_LEVEL_SUPERSEDED_BY_PER_QUESTION_REVIEW"),
    }

    for row_id, (question, qtype, in_book, node, support, evidence, artifact, action) in updates.items():
        row = by_id.get(row_id)
        if not row:
            continue
        set_fields(
            row,
            题源=SUITE,
            年份=YEAR,
            阶段=STAGE,
            题号=question,
            题型或模块判断=qtype,
            是否进宝典=in_book,
            宝典节点=node,
            细则支持原理=support,
            证据等级=evidence,
            是否误放="否",
            是否需补厚="否",
            当前处理=action,
            备注="2026东城一模逐题回源修复：正式细则、PPT细则、官方答案键分层；选择题不冒充主观题评分细则。",
            source_artifact=artifact,
        )

    present = {(r["题源"], r["题号"]) for r in rows}
    max_id = max(int(r["matrix_row_id"][1:]) for r in rows if r["matrix_row_id"].startswith("M") and r["matrix_row_id"][1:].isdigit())
    additions = [
        ("Q7", "选择题 / 逻辑模块边界排除", "否：模块边界排除", "不入宝典", "官方答案键D；逃逸粒子条件推理属于《逻辑与思维》边界。", "官方答案键+题干模块边界", source("384-397", "594-600"), "EXCLUDED_XUANBISAN_LOGIC_BOUNDARY"),
        ("Q10", "选择题 / 法律边界排除", "否：模块边界排除", "不入宝典", "官方答案键C；宅基地、夫妻债务、处分权、收益分配属于法律与生活/经济边界。", "官方答案键+题干模块边界", source("417-422", "594-600"), "EXCLUDED_LAW_ECON_BOUNDARY"),
        ("Q11", "选择题 / 法律边界排除", "否：模块边界排除", "不入宝典", "官方答案键C；AIGC数字人、肖像权、声音权益、直播电商标识属于法律与生活边界。", "官方答案键+题干模块边界", source("423-438", "594-600"), "EXCLUDED_LAW_PERSONALITY_RIGHTS_BOUNDARY"),
        ("Q12", "选择题 / 经济产业边界排除", "否：模块边界排除", "不入宝典", "官方答案键B；脑机接口产业链结构和核心技术攻关属于经济/产业分析边界。", "官方答案键+题干模块边界", source("439-445", "594-600"), "EXCLUDED_ECONOMICS_INDUSTRY_BOUNDARY"),
        ("Q19(1)", "主观题 / 必修四认识论支撑", "是：当前DOCX已覆盖", "实践是认识的基础", "正式PPT细则给出调查研究法，并把“实践是认识的基础/获取感性材料”列为替代知识；当前DOCX已有Q19(1)实践是认识基础条目。", "正式PPT评分细则+当前DOCX正文", source("919-924"), "CURRENT_DOCX_VERIFIED_Q19_1_PRACTICE"),
        ("Q19(2)", "主观题 / 经济边界排除", "否：模块边界排除", "不入宝典", "正式PPT细则为中关村产业园独特优势和推动北京高质量发展的经济分析，并提示“用哲学/思维”为无关知识堆砌。", "正式PPT评分细则模块边界", source("949-981"), "EXCLUDED_ECONOMICS_BOUNDARY"),
        ("Q19(3)", "主观题 / 选必一边界排除", "否：模块边界排除", "不入宝典", "正式PPT细则为高水平对外开放与产业链韧性的关系，属于《当代国际政治与经济》边界。", "正式PPT评分细则模块边界", source("998-1040"), "EXCLUDED_XUANBIYI_BOUNDARY"),
    ]
    added_rows = []
    for question, qtype, in_book, node, support, evidence, artifact, action in additions:
        if (SUITE, question) in present:
            continue
        max_id += 1
        row = {field: "" for field in fieldnames}
        set_fields(
            row,
            matrix_row_id=f"M{max_id:04d}",
            row_source="manual_full_question_adjudication_20260525",
            题源=SUITE,
            年份=YEAR,
            阶段=STAGE,
            题号=question,
            题型或模块判断=qtype,
            是否进宝典=in_book,
            宝典节点=node,
            细则支持原理=support,
            证据等级=evidence,
            是否误放="否",
            是否需补厚="否",
            当前处理=action,
            备注="补齐原矩阵缺失题号/分问，确保2026东城一模Q1-Q20均有逐题裁决。",
            source_artifact=artifact,
        )
        rows.append(row)
        added_rows.append(row["matrix_row_id"])

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "updated_existing_rows": len(updates), "added_rows": added_rows}


def append_once(path: Path, marker: str, text: str) -> None:
    old = path.read_text(encoding="utf-8")
    if marker in old:
        old = old[: old.index(marker)].rstrip() + "\n"
    path.write_text(old.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8", newline="\n")


def write_reports(timestamp: str, result: dict[str, object]) -> None:
    hm = f"{timestamp[9:11]}:{timestamp[11:13]}"
    report = f"""# DONGCHENG_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `DONGCHENG_2026_YIMO_REPAIRED_DOCX_CHOICE_CULTURE_INSERTED_RENDER_PENDING`

Updated: 2026-05-25 {hm} +08

## Source Basis

- Source bundle: `{SOURCE_BUNDLE}`.
- Formal source inventory: bundle lines `7-18`.
- Teacher-version question/answer key: bundle lines `329-654`.
- Q16 formal PPT rubric: bundle lines `673-731`.
- Q19(1) formal PPT rubric: bundle lines `919-924`.
- Q19(4) formal PPT rubric: bundle lines `1059-1091`.
- Q20 formal PPT rubric: bundle lines `1098-1148`.

## Decisions

- Inserted choice chains: Q1 under `一切从实际出发 / 实事求是`, Q2 under `矛盾就是对立统一`, Q5 under `认识发展原理`, Q8 under `系统观念 / 系统优化`.
- Inserted Q16 culture/value chain under `价值观的导向作用`, using formal PPT rubric support for national spirit/core values/文化点.
- Kept existing current-DOCX coverage for Q16 philosophy nodes, Q19(1), Q19(4), and Q20.
- Excluded Q3/Q4/Q6/Q7/Q9-Q15/Q17/Q18/Q19(2)/Q19(3) by official key, formal rubric, or module boundary.
- Added missing matrix rows for Q7, Q10, Q11, Q12, Q19(1), Q19(2), Q19(3), so Q1-Q20 have explicit decisions.
- Choice-question chains are not treated as main-question scoring-rubric evidence.
- No Sonnet/Haiku/model-unknown evidence was promoted.
- GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review remain `real_call_pending`.

## Backups And Outputs

- DOCX backup: `{result['docx']['docx_backup']}`.
- Matrix backup: `{result['matrix']['matrix_backup']}`.
- Ledger backup: `{result['ledger']['ledger_backup']}`.
- Matrix rows added: `{', '.join(result['matrix']['added_rows']) or '0'}`.
- Inserted headings: `{'; '.join(result['docx']['inserted_headings']) or 'already_present'}`.

## Boundary

This is a local source/DOCX/matrix repair. It does not close render QA, external model review, full manual typography review, ClaudeCode model confirmation, or the deferred ORDER_063 final GitHub upload gate.
"""
    REPORT_MD.write_text(report, encoding="utf-8", newline="\n")
    REPORT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    gov = f"""## Governor Finding: Dongcheng 2026 Yimo Candidate Queue Repair
Updated: 2026-05-25 {hm} +08

- Governor decision: `LOCAL_DOCX_CHOICE_CULTURE_INSERTED_MATRIX_CLOSED_RENDER_PENDING_MODEL_GATES_OPEN`.
- Corrective action: inserted Q1/Q2/Q5/Q8 choice-question chains and Q16 culture/value chain into current DOCX; all choice chains are explicitly non-main-question scoring evidence.
- Matrix action: existing 21 suite rows were rewritten against source bundle/formal PPT rubrics; missing Q7/Q10/Q11/Q12/Q19(1)/Q19(2)/Q19(3) rows were added for explicit Q1-Q20 coverage.
- Current-DOCX coverage retained for Q16 philosophy nodes, Q19(1), Q19(4), and Q20 under formal PPT scoring support.
- Boundary exclusions: Q3/Q4/Q6/Q7/Q9-Q15/Q17/Q18/Q19(2)/Q19(3) do not enter the 必修四正文.
- Render QA is required after this DOCX change.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
"""
    append_once(GOVERNOR, "\n## Governor Finding: Dongcheng 2026 Yimo Candidate Queue Repair", gov)

    conf = f"""## Artifact Check: Dongcheng 2026 Yimo Candidate Queue Repair
Updated: 2026-05-25 {hm} +08

- `{Path(__file__).name}`: present.
- `{REPORT_MD.name}`: present and status `DONGCHENG_2026_YIMO_REPAIRED_DOCX_CHOICE_CULTURE_INSERTED_RENDER_PENDING`.
- `{REPORT_JSON.name}`: present.
- DOCX backup before insertion: present.
- Matrix backup before rewrite: present.
- Ledger backup before insert registration: present.
- Current DOCX now contains new 2026东城一模 entries for Q1, Q2, Q5, Q8, and Q16 value/culture line.
- Matrix now includes explicit Q7/Q10/Q11/Q12/Q19(1)/Q19(2)/Q19(3) rows.
- Remaining open gates: render QA rerun after DOCX change, GPTPro web review, full Claude Opus web/app review through direct `https://claude.ai`, ClaudeCode model confirmation, and deferred ORDER_063 final GitHub upload.
"""
    append_once(CONFUCIUS, "\n## Artifact Check: Dongcheng 2026 Yimo Candidate Queue Repair", conf)

    status = f"""## Dongcheng 2026 Yimo Recovery Repair
Updated: 2026-05-25 {hm} +08

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_DONGCHENG_2026_YIMO_DOCX_REPAIRED_RENDER_PENDING`.
- Q1/Q2/Q5/Q8 choice chains and Q16 value/culture line were inserted into the current DOCX and registered in `docx_insert_ledger.csv`.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` was rewritten for 2026东城一模 with explicit Q1-Q20 decisions.
- Render QA must be rerun after this DOCX change before this repair can be treated as layout-checked.
- External review gates remain open: GPTPro `real_call_pending`; full Claude Opus web/app `real_call_pending`; ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
"""
    append_once(STATUS, "\n## Dongcheng 2026 Yimo Recovery Repair", status)

    upload = f"""## Deferred Upload Scope Addition: 2026东城一模 Repair
Updated: 2026-05-25 {hm} +08

- Include in future ORDER_063 upload scope after all active lines end:
  - `{REPORT_MD.name}`
  - `{REPORT_JSON.name}`
  - `{Path(__file__).name}`
  - updated `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
  - updated `docx_insert_ledger.csv`
  - current DOCX/PDF after render QA
  - refreshed `FORMAT_RENDER_QA_20260524.md`, `GOVERNOR_RECOVERY_REPORT_20260524.md`, `CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`, `THREAD_RECOVERY_STATUS_20260524.md`
- Upload still deferred; no push before all active Beijing politics lines reach terminal/user-approved states and secret scan records `NO_SECRET_PATTERN_MATCHES`.
"""
    append_once(UPLOAD_SCOPE, "\n## Deferred Upload Scope Addition: 2026东城一模 Repair", upload)

    model = f"""## MODEL_GATE_SUMMARY_AFTER_DONGCHENG_2026_YIMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- 2026东城一模 repair was performed by local cached source bundle, formal PPT/rubric source review, current DOCX insertion, matrix rewrite, and pending render QA.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local repair.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`.
- GPTPro web full artifact review remains `real_call_pending`.
- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
"""
    append_once(MODEL_LEDGER, "\n## MODEL_GATE_SUMMARY_AFTER_DONGCHENG_2026_YIMO_LOCAL_REPAIR_20260525", model)


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx = current_docx()
    result = {
        "timestamp": timestamp,
        "docx": insert_entries_into_docx(docx, timestamp),
        "ledger": update_ledger(timestamp),
        "matrix": update_matrix(timestamp),
        "current_docx": str(docx),
    }
    write_reports(timestamp, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
