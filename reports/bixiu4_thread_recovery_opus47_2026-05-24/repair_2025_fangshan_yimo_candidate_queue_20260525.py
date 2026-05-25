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
ROOT = RECOVERY.parents[1]
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
REPORT_MD = RECOVERY / "FANGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "FANGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
UPLOAD_SCOPE = RECOVERY / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md"

SUITE = "2025房山一模"
YEAR = "2025"
STAGE = "一模"
SOURCE_BUNDLE = (
    "preprocessed_corpus\\gpt_suite_bundles\\"
    "2025各区模拟题__2025各区一模__2025房山一模.md"
)

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

ENTRIES = [
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q2",
        "heading_suffix": "2025房山一模 第2题（选择题）",
        "material_trigger": "题干把“打造能出汗的体育课”放在增强体质、健全人格，并促进德育、智育、美育、劳育发展的整体目标中；正确项D为“坚持统筹兼顾，促进中小学生的全面发展”。",
        "question_prompt": "北京市《关于进一步加强新时代中小学体育工作的若干措施》指出，通过“打造能出汗的体育课”帮助学生在体育锻炼中增强体质、健全人格，发挥体育在促进学生德育、智育、美育、劳育发展中的基础性作用。该措施（A. 推动良法之治……；B. 推进全过程人民民主；C. 立足部分，实现最优目标；D. 坚持统筹兼顾，促进中小学生的全面发展）。",
        "why_trigger": "看到“体育锻炼+体质+人格+德智美劳全面发展”，不能把体育课孤立看成单一部分，也不能像错项C那样“立足部分”。正确链条是把学生成长看成一个有机整体，统筹各方面要素，促进整体优化。",
        "answer_landing": "答案选D。体育课不是只解决体能问题，而是服务学生全面发展这一整体目标；应坚持系统观念和统筹兼顾，把体育、德育、智育、美育、劳育放在同一育人系统中协同推进。选择题边界已明示；非主观题评分细则。",
        "evidence_level": "正式答案键+教师详解（选择题链，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:198-204; {SOURCE_BUNDLE}:417-424",
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q5",
        "heading_suffix": "2025房山一模 第5题（选择题）",
        "material_trigger": "青春版《牡丹亭》保留昆曲传统内核，又通过舞台、服装、人物等形式创新，20多年演出500多场，吸引国内外年轻观众，成为中华文化走出去的名片。",
        "question_prompt": "青春版《牡丹亭》，舞台、服装、人物都非常美，古老的昆曲绽放新的华彩，是中华文化走出去一张有魅力的名片。可见（A. 青春版《牡丹亭》守正创新，体现了内容美与形式美的统一；B. 文化创作立足中华传统文化；C. 发展文化产业要以经济效益为中心；D. 中华文化与世界各国文化兼容并蓄）。",
        "why_trigger": "“古老昆曲绽放新的华彩”是守住传统内核又更新表达形式；“舞台、服装、人物都非常美”说明形式创新服务内容表达。看到这种“保留传统内核+创新现代表达+走向世界”的结构，应想到辩证否定、守正创新，以及中华优秀传统文化创造性转化和创新性发展。",
        "answer_landing": "答案选A。青春版《牡丹亭》既守住昆曲艺术的传统内核和文化价值，又通过舞台、服装、人物塑造等现代表达增强吸引力，实现内容美与形式美统一，推动中华优秀传统文化创造性转化、创新性发展。选择题边界已明示；非主观题评分细则。",
        "evidence_level": "正式答案键+教师详解（选择题链，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:222-228; {SOURCE_BUNDLE}:447-454",
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
    label_template = next((paras[i] for i in range(start + 1, end) if not is_heading3(paras[i]) and para_text(paras[i]).strip().startswith("【")), None)
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_fangshan_yimo_q2_q5_choice_insert_{timestamp}.docx")
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2025_fangshan_yimo_q2_q5_choice_insert_{timestamp}.csv")
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
        heading = entry["heading_suffix"]
        rows.append(
            {
                "canonical_node": entry["canonical_node"],
                "source_suite": SUITE,
                "question_no": entry["question_no"],
                "inserted_heading": heading,
            }
        )
        added.append(heading)
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
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2025_fangshan_yimo_candidate_repair_{timestamp}.csv")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    if not fieldnames:
        raise RuntimeError("Matrix has no header")

    by_id = {row["matrix_row_id"]: row for row in rows}
    updates = {
        "M0098": ("Q16(1)", "是：当前DOCX已覆盖", "价值观的导向作用", "正式细则哲学3分第①点：树立正确价值观/价值判断与价值选择。", "强细则", source("29-45"), "CURRENT_DOCX_VERIFIED_Q16_1"),
        "M0099": ("Q16(1)", "是：当前DOCX已覆盖", "矛盾就是对立统一", "正式细则哲学3分第②点：一分为二全面看问题2分，或矛盾/辩证看问题1分。", "强细则", source("29-45"), "CURRENT_DOCX_VERIFIED_Q16_1"),
        "M0186": ("Q16(1)", "是：当前DOCX已覆盖", "价值观的导向作用；矛盾就是对立统一；中华优秀传统文化创造性转化和创新性发展", "正式细则：文化4分含优秀文化传承、创造性转化创新性发展、文化自信、文化功能；哲学3分含价值观和一分为二。Q16(2)(3)为逻辑/创新思维边界，不进本体。", "强细则", source("29-69"), "CURRENT_DOCX_VERIFIED_Q16_1_BOUNDARY_SPLIT"),
        "M0208": ("Q16(1)", "是：当前DOCX已覆盖", "价值观的导向作用；矛盾就是对立统一", "正式细则哲学3分支持价值观与一分为二/矛盾观；当前DOCX已有Q16(1)正文块。", "强细则", source("29-45"), "CURRENT_DOCX_VERIFIED_Q16_1"),
        "M0394": ("Q1", "否：模块边界排除", "不入宝典", "正式答案键B；题干与答案详解指向科技创新、生产力发展和第二个百年目标，不构成必修四哲学/文化稳定链。", "正式答案键边界", source("21-27", "191-197", "408-416"), "EXCLUDED_MODULE_BOUNDARY_AFTER_SOURCE_REVIEW"),
        "M0395": ("Q2", "是：已补入当前DOCX", "系统观念 / 系统优化", "正式答案键D+教师详解支持“统筹兼顾、全面发展”；选择题边界已明示，非主观题评分细则。", "正式答案键+教师详解（选择题链，非主观题评分细则）", source("198-204", "417-424"), "DOCX_INSERTED_Q2_CHOICE_CHAIN"),
        "M0396": ("Q3", "是：当前DOCX已覆盖", "矛盾的特殊性 / 具体问题具体分析", "正式答案键为B；当前DOCX已放入“具体问题具体分析”选择题链。教师版详解处出现D项冲突，裁决以正式答案键为强来源。选择题边界已明示，非主观题评分细则。", "正式答案键+冲突披露（选择题链，非主观题评分细则）", source("21-27", "205-210", "425-433"), "CURRENT_DOCX_VERIFIED_Q3_FORMAL_KEY_OVERRIDES_TEACHER_CONFLICT"),
        "M0397": ("Q4", "是：当前DOCX已覆盖", "矛盾的普遍性和特殊性", "正式答案键C+教师详解支持北京经验共性与曼谷特点个性具体历史统一；当前DOCX已有Q4选择题链。选择题边界已明示，非主观题评分细则。", "正式答案键+教师详解（选择题链，非主观题评分细则）", source("211-221", "434-446"), "CURRENT_DOCX_VERIFIED_Q4_CHOICE_CHAIN"),
        "M0398": ("Q5", "是：已补入当前DOCX", "辩证否定 / 守正创新", "正式答案键A+教师详解支持青春版《牡丹亭》保留昆曲传统内核并创新舞台服装等形式，体现守正创新和内容美与形式美统一。选择题边界已明示，非主观题评分细则。", "正式答案键+教师详解（选择题链，非主观题评分细则）", source("222-228", "447-454"), "DOCX_INSERTED_Q5_CHOICE_CHAIN"),
        "M0399": ("Q6", "否：模块边界排除", "不入宝典", "正式答案键B；题干考查《逻辑与思维》复合判断/推理，不属于必修四宝典正文。", "正式答案键边界", source("229-236", "455-465"), "EXCLUDED_XUANBISAN_LOGIC_BOUNDARY"),
        "M0400": ("Q7", "否：模块边界排除", "不入宝典", "正式答案键B；教师详解明确“反向法”打破传统表演界限，属于《逻辑与思维》创新思维方法，不作为必修四正文链。", "正式答案键+教师详解边界", source("237-242", "466-474"), "EXCLUDED_XUANBISAN_INNOVATIVE_THINKING_BOUNDARY"),
        "M0401": ("Q8", "否：模块边界排除", "不入宝典", "正式答案键C；自治与法治、基层治理法治化，属于政治与法治/法律生活边界。", "正式答案键边界", source("243-250", "475-486"), "EXCLUDED_POLITICS_LAW_BOUNDARY"),
        "M0402": ("Q9", "否：模块边界排除", "不入宝典", "正式答案键A；党坚持以人民为中心、人民监督与自我革命，属于政治与法治边界；材料中的“化解矛盾”是治理语义，不构成必修四矛盾观落点。", "正式答案键边界", source("251-262", "487-495"), "EXCLUDED_POLITICS_BOUNDARY"),
        "M0403": ("Q12", "否：模块边界排除", "不入宝典", "正式答案键C；民营经济和市场准入/营商环境，属于经济与社会边界。", "正式答案键边界", source("281-288", "513-526"), "EXCLUDED_ECONOMICS_BOUNDARY"),
        "M0404": ("Q13", "否：模块边界排除", "不入宝典", "正式答案键D；扩大国内需求、消费和专项债，属于经济与社会边界。", "正式答案键边界", source("289-299", "527-530"), "EXCLUDED_ECONOMICS_BOUNDARY"),
        "M0405": ("Q14", "否：模块边界排除", "不入宝典", "正式答案键D；开放中国与人类命运共同体，属于选择性必修一国际政治经济边界。", "正式答案键边界", source("300-306"), "EXCLUDED_XUANBIYI_BOUNDARY"),
        "M0406": ("Q15", "否：模块边界排除", "不入宝典", "正式答案键A；外贸结构、改革开放和贸易全球化，属于经济/选必一边界。", "正式答案键边界", source("307-315"), "EXCLUDED_ECONOMICS_XUANBIYI_BOUNDARY"),
        "M0407": ("Q16(1)", "是：当前DOCX已覆盖", "价值观的导向作用；矛盾就是对立统一；中华优秀传统文化创造性转化和创新性发展", "正式细则支持Q16(1)文化4分+哲学3分；Q16(2)三段论、Q16(3)创新思维为模块边界，不进入必修四正文。", "强细则", source("29-69", "318-360"), "CURRENT_DOCX_VERIFIED_Q16_1_BOUNDARY_SPLIT"),
        "M0408": ("Q17", "否：模块边界排除", "不入宝典", "正式细则为党的领导、政府、协商民主、公民/社会等政治与法治角度；不作必修四正文链。", "正式细则边界", source("71-88"), "EXCLUDED_POLITICS_LAW_BOUNDARY"),
        "M0409": ("Q18", "否：模块边界排除", "不入宝典", "正式细则Q18(1)为经济高质量发展，Q18(2)为国际竞争、开放型世界经济、人类命运共同体等选必一/经济边界；不作必修四正文链。", "正式细则边界", source("90-114"), "EXCLUDED_ECONOMICS_XUANBIYI_BOUNDARY"),
        "M0410": ("Q19", "否：模块边界排除", "不入宝典", "正式细则为不正当竞争、惩罚性赔偿、公正司法、知识产权、劳动者义务等法律生活/法治边界；“社会主义核心价值观”只作法律道德意义，不足以生成必修四正文链。", "正式细则边界", source("116-139"), "EXCLUDED_LAW_BOUNDARY"),
        "M0411": ("Q20", "是：当前DOCX已覆盖", "主观能动性；发展观；价值判断与价值选择；实现人生价值；中华民族精神", "正式细则列必答“全面深化改革或中华民族精神-奋斗精神”，并列可用知识点：发挥主观能动性、发展观（质量互变/前进性曲折性）、实现人生价值、价值判断与价值选择等；当前DOCX已有Q20多节点覆盖。", "强细则", source("150-160"), "CURRENT_DOCX_VERIFIED_Q20_FORMAL_RUBRIC"),
        "M0412": ("Qunknown", "否：已由逐题行替代", "套卷索引残留", "原行为套卷源包/索引残留，不替代Q1-Q20逐题裁决；本轮已补齐Q10/Q11边界行并重写所有现存题号。", "套卷索引边界", source("1-18", "21-160"), "SUPERSEDED_BY_PER_QUESTION_ADJUDICATION"),
        "M0788": ("SUITE_LEVEL", "否：套卷级摘要，不替代逐题入正文", "套卷级摘要", "套卷级覆盖摘要仅说明当前DOCX提及或闭合记录；本轮逐题裁决已单独落入矩阵。", "套卷级边界", source("1-18"), "SUITE_LEVEL_SUPERSEDED_BY_PER_QUESTION_REVIEW"),
        "M0831": ("SUITE_LEVEL", "否：套卷级摘要，不替代逐题入正文", "套卷级摘要", "套卷级记录不能替代逐题回源；本轮已逐题裁决并新增Q10/Q11模块边界行。", "套卷级边界", source("1-18"), "SUITE_LEVEL_SUPERSEDED_BY_PER_QUESTION_REVIEW"),
    }

    for row_id, (question, in_book, node, support, evidence, artifact, action) in updates.items():
        row = by_id.get(row_id)
        if not row:
            continue
        set_fields(
            row,
            题源=SUITE,
            年份=YEAR,
            阶段=STAGE,
            题号=question,
            题型或模块判断="逐题回源裁决",
            是否进宝典=in_book,
            宝典节点=node,
            细则支持原理=support,
            证据等级=evidence,
            是否误放="否",
            是否需补厚="否",
            当前处理=action,
            备注="2025房山一模逐题回源修复：正式细则/正式答案键与教师详解分层，不把普通答案冒充主观评分细则。",
            source_artifact=artifact,
        )

    present_questions = {(r["题源"], r["题号"]) for r in rows}
    max_id = max(int(r["matrix_row_id"][1:]) for r in rows if r["matrix_row_id"].startswith("M") and r["matrix_row_id"][1:].isdigit())
    additions = [
        ("Q10", "正式答案键A；AI生成图片著作权、信息网络传播权，属于法律生活/知识产权边界。", source("263-270", "496-502"), "EXCLUDED_LAW_IP_BOUNDARY"),
        ("Q11", "正式答案键C；不动产相邻权、权利行使界限、公序良俗，属于法律生活边界。", source("271-280", "503-512"), "EXCLUDED_LAW_NEIGHBOR_BOUNDARY"),
    ]
    added_rows = []
    for question, support, artifact, action in additions:
        if (SUITE, question) in present_questions:
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
            题型或模块判断="选择题-模块边界排除",
            是否进宝典="否：模块边界排除",
            宝典节点="不入宝典",
            细则支持原理=support,
            证据等级="正式答案键边界",
            是否误放="否",
            是否需补厚="否",
            当前处理=action,
            备注="补齐原矩阵缺失题号，确保2025房山一模Q1-Q20逐题均有裁决。",
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
    report = f"""# FANGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `FANGSHAN_2025_YIMO_REPAIRED_DOCX_Q2_Q5_INSERTED_MODEL_GATES_OPEN`

Updated: 2026-05-25 {timestamp[9:11]}:{timestamp[11:13]} +08

## Source Basis

- Source bundle: `{SOURCE_BUNDLE}`.
- Formal answer key: source-bundle lines `21-27`.
- Q2 prompt and teacher detail: source-bundle lines `198-204`, `417-424`.
- Q5 prompt and teacher detail: source-bundle lines `222-228`, `447-454`.
- Q16 formal rubric: source-bundle lines `29-45`; Q16(2)(3) are logic/innovative-thinking boundaries.
- Q20 formal rubric: source-bundle lines `150-160`.

## Decisions

- Inserted into current DOCX:
  - `2025房山一模 第2题（选择题）` under `系统观念 / 系统优化`.
  - `2025房山一模 第5题（选择题）` under `辩证否定 / 守正创新`.
- Q2/Q5 are recorded as correct-option chains only: `选择题边界已明示；非主观题评分细则`.
- Q3 remains current-DOCX covered under the formal answer key. The teacher-version detailed explanation conflicts with the formal key, so the formal key controls.
- Q4 remains current-DOCX covered as a choice chain.
- Q16(1) and Q20 remain current-DOCX covered under formal rubric support.
- Q1, Q6-Q15, Q17-Q19 are excluded by module boundary; Q10/Q11 were added to the matrix because the prior matrix lacked explicit rows for them.
- No Sonnet/Haiku/model-unknown evidence was promoted.
- GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review remain `real_call_pending`.

## Backups And Outputs

- DOCX backup: `{result['docx']['docx_backup']}`.
- Matrix backup: `{result['matrix']['matrix_backup']}`.
- Ledger backup: `{result['ledger']['ledger_backup']}`.
- Matrix rows added: `{', '.join(result['matrix']['added_rows']) or '0'}`.
- Inserted headings: `{'; '.join(result['docx']['inserted_headings']) or 'already_present'}`.

## Boundary

This is a local source/DOCX/matrix repair. It does not close external model review, full manual typography review, ClaudeCode model confirmation, or the deferred ORDER_063 final GitHub upload gate.
"""
    REPORT_MD.write_text(report, encoding="utf-8", newline="\n")
    REPORT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    gov = f"""## Governor Finding: Fangshan 2025 Yimo Candidate Queue Repair
Updated: 2026-05-25 {timestamp[9:11]}:{timestamp[11:13]} +08

- Governor decision: `LOCAL_DOCX_Q2_Q5_INSERTED_AND_MATRIX_CLOSED_MODEL_GATES_OPEN`.
- Finding: `2025房山一模` still had unresolved candidate wording and lacked current-DOCX coverage for Q2/Q5 choice chains.
- Corrective action: inserted Q2 under `系统观念 / 系统优化` and Q5 under `辩证否定 / 守正创新`, both explicitly labeled as choice-question chains and not main-question scoring rubrics.
- Matrix action: existing 25 suite rows were rewritten against the source bundle; missing Q10/Q11 module-boundary rows were added so Q1-Q20 have explicit decisions.
- Evidence: `{REPORT_MD.name}`, current DOCX backup, matrix backup, and `docx_insert_ledger.csv`.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
"""
    append_once(GOVERNOR, "\n## Governor Finding: Fangshan 2025 Yimo Candidate Queue Repair", gov)

    conf = f"""## Artifact Check: Fangshan 2025 Yimo Candidate Queue Repair
Updated: 2026-05-25 {timestamp[9:11]}:{timestamp[11:13]} +08

- `{Path(__file__).name}`: present.
- `{REPORT_MD.name}`: present and status `FANGSHAN_2025_YIMO_REPAIRED_DOCX_Q2_Q5_INSERTED_MODEL_GATES_OPEN`.
- `{REPORT_JSON.name}`: present.
- DOCX backup before insertion: present.
- Matrix backup before rewrite: present.
- Ledger backup before insert registration: present.
- Current DOCX now contains `2025房山一模 第2题（选择题）` and `2025房山一模 第5题（选择题）`.
- Matrix now includes explicit Q10/Q11 boundary rows for this suite.
- Remaining open gates: render QA rerun after DOCX change, GPTPro web review, full Claude Opus web/app review through direct `https://claude.ai`, ClaudeCode model confirmation, and deferred ORDER_063 final GitHub upload.
"""
    append_once(CONFUCIUS, "\n## Artifact Check: Fangshan 2025 Yimo Candidate Queue Repair", conf)

    status = f"""## Fangshan 2025 Yimo Recovery Repair
Updated: 2026-05-25 {timestamp[9:11]}:{timestamp[11:13]} +08

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_FANGSHAN_2025_YIMO_DOCX_REPAIRED_RENDER_PENDING`.
- Q2/Q5 were inserted into the current DOCX and registered in `docx_insert_ledger.csv`.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` was rewritten for 2025房山一模 with explicit Q1-Q20 decisions.
- Render QA must be rerun after this DOCX change before this repair can be treated as layout-checked.
- External review gates remain open: GPTPro `real_call_pending`; full Claude Opus web/app `real_call_pending`; ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
"""
    append_once(STATUS, "\n## Fangshan 2025 Yimo Recovery Repair", status)

    upload = f"""## Deferred Upload Scope Addition: 2025房山一模 Repair
Updated: 2026-05-25 {timestamp[9:11]}:{timestamp[11:13]} +08

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
    append_once(UPLOAD_SCOPE, "\n## Deferred Upload Scope Addition: 2025房山一模 Repair", upload)


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
