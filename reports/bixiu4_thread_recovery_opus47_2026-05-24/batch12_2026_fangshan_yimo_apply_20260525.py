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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH12_2026_FANGSHAN_YIMO_CODEX_20260525.md"
SOURCE_TRANSCRIPTION = RECOVERY / "BATCH12_2026_FANGSHAN_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
SUITE = "2026房山一模"

SOURCE_BUNDLE = "01_source_inventory/suite_source_bundles/2026房山一模.md"
PAPER_RENDER = "preprocessed_corpus/renders/e37482eff39f3618"
RUBRIC_DOCX = "2026各区模拟题/2026各区一模/2026房山一模/26 房山一模评标 全.docx"
DETAIL_RULE_DOCX = "2026各区模拟题/2026各区一模/2026房山一模/细则/2026房山一模细则.docx"

Q16_2_PROMPT = "结合材料一和材料二，运用哲学知识，谈谈你对“因地制宜，本质就是实事求是”的理解。（7分）"
Q18_1_PROMPT = "结合材料一，运用辩证思维方法，分析北京是如何通过科学治理实现“常态蓝天”的。（6分）"
Q20_PROMPT = "结合材料，综合运用所学，谈谈你对“坚持依法治国和依规治党有机统一”的认识。"

Q16_SOURCE_LINES = (
    f"{RUBRIC_DOCX}:paras13-21; {DETAIL_RULE_DOCX}:paras13-21; "
    f"{PAPER_RENDER}/page_007.png"
)
Q18_SOURCE_LINES = (
    f"{RUBRIC_DOCX}:paras42-49; {DETAIL_RULE_DOCX}:paras42-49; "
    f"{PAPER_RENDER}/page_009.png"
)
Q20_SOURCE_LINES = (
    f"{RUBRIC_DOCX}:paras69-81; {DETAIL_RULE_DOCX}:paras69-81; "
    f"{PAPER_RENDER}/page_011.png"
)


ENTRIES = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q16(2)",
        "heading_suffix": "2026房山一模 第16题第（2）问（主观题）",
        "material_trigger": "材料二直接提出“因地制宜，本质就是实事求是”；评标细则把“一切从实际出发/开展调查研究”“从客观存在的事物出发，经过调查研究，找出事物本身的规律性”列为采分链条。",
        "question_prompt": Q16_2_PROMPT,
        "why_trigger": "看到“因地制宜”和“实事求是”连用，且细则要求结合调查研究、客观存在和规律性，就应落到一切从实际出发，而不是把经验模板机械套用到不同地区。",
        "answer_landing": "作答应写：物质决定意识，要求坚持一切从实际出发、实事求是。各地发展清洁能源产业必须立足本地资源禀赋、产业基础和发展阶段，通过调查研究把握实际情况，再制定符合本地条件的路径。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE_LINES,
    },
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q16(2)",
        "heading_suffix": "2026房山一模 第16题第（2）问（主观题）",
        "material_trigger": "评标细则列出“尊重客观规律、发挥主观能动性”，并把“尊重规律/主观能动性深入论述”作为高档论述要求。",
        "question_prompt": Q16_2_PROMPT,
        "why_trigger": "因地制宜不是被动接受条件，也不是主观造势，而是在尊重能源资源、产业基础和地区条件等客观规律的基础上主动谋划发展。",
        "answer_landing": "卷面可写：发展清洁能源产业既要尊重物质运动和产业发展的客观规律，又要发挥主观能动性，通过科学规划、调查研究和政策组织，把本地优势转化为现实发展成效。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE_LINES,
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q16(2)",
        "heading_suffix": "2026房山一模 第16题第（2）问（主观题）",
        "material_trigger": "评标细则列“联系的观点”，并在细则中写到“在大局中找准定位”，要求把地方发展放入产业发展和国家大局中理解。",
        "question_prompt": Q16_2_PROMPT,
        "why_trigger": "看到地方资源、产业布局、国家能源转型和区域定位被放在一起，就不能孤立看某地条件，而要用联系的观点分析各要素之间的关系。",
        "answer_landing": "卷面可写：坚持联系的观点，把地方实际与国家战略、区域协同、产业链需求联系起来，在大局中找准定位，实现因地制宜的发展。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE_LINES,
    },
    {
        "canonical_node": "矛盾的普遍性和特殊性",
        "question_no": "Q16(2)",
        "heading_suffix": "2026房山一模 第16题第（2）问（主观题）",
        "material_trigger": "评标细则写明“矛盾普遍性和特殊性的统一”，并进一步写“矛盾普遍性与特殊性具体的历史统一”“在普遍性的指导下具体问题具体分析”。",
        "question_prompt": Q16_2_PROMPT,
        "why_trigger": "清洁能源发展有一般规律，但各地资源、产业和区位条件不同。看到“因地制宜”，就要把普遍规律和具体地区特殊性统一起来。",
        "answer_landing": "卷面可写：矛盾的普遍性和特殊性相互联结。发展清洁能源要在普遍规律指导下分析本地特殊条件，做到共性要求与个性路径具体的历史的统一。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE_LINES,
    },
    {
        "canonical_node": "整体与部分",
        "question_no": "Q16(2)",
        "heading_suffix": "2026房山一模 第16题第（2）问（主观题）",
        "material_trigger": "评标细则高档要求写“融入大局中找定位/系统/整体，逻辑清晰、知识运用准确”，并在细则提示中写“在大局中找准定位”。",
        "question_prompt": Q16_2_PROMPT,
        "why_trigger": "地方发展是国家能源转型和区域产业体系中的部分。看到“在大局中找定位”，应想到部分服从和服务整体，同时在整体布局中发挥局部优势。",
        "answer_landing": "卷面可写：要立足整体、统筹全局，把地方产业作为国家能源转型和区域协同中的部分来定位；同时发挥地方资源禀赋和产业基础，使局部发展服务整体目标。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q16_SOURCE_LINES,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q18(1)",
        "heading_suffix": "2026房山一模 第18题第（1）问（主观题）",
        "material_trigger": "评标细则把治理路径一写为“整体性/分析与综合/联系/系统优化”，答案示例写“坚持系统治理，统筹四大结构调整，实现整体推进”。",
        "question_prompt": Q18_1_PROMPT,
        "why_trigger": "看到北京治理蓝天不是单点治理，而是统筹产业、能源、交通、用地等结构调整，就应想到系统优化和整体推进。",
        "answer_landing": "卷面可写：北京坚持系统治理，把污染治理中的多领域、多主体、多环节作为系统来把握，统筹四大结构调整，推动各要素协同优化，实现整体治理效果。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q18_SOURCE_LINES,
    },
    {
        "canonical_node": "量变与质变 / 适度原则",
        "question_no": "Q18(1)",
        "heading_suffix": "2026房山一模 第18题第（1）问（主观题）",
        "material_trigger": "评标细则把治理路径三写为“动态性/质量互变/发展”，答案示例写“坚持久久为功，以日积月累推动空气质量稳步提升，实现从量变到质变”。",
        "question_prompt": Q18_1_PROMPT,
        "why_trigger": "看到“久久为功”“日积月累”“稳步提升”，应想到量变积累到一定程度引起质变，常态蓝天来自持续治理的长期积累。",
        "answer_landing": "卷面可写：北京坚持久久为功，通过持续减排、结构调整和精细治理积累量变，推动空气质量发生质的改善，形成常态蓝天。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q18_SOURCE_LINES,
    },
    {
        "canonical_node": "矛盾的特殊性 / 具体问题具体分析",
        "question_no": "Q18(1)",
        "heading_suffix": "2026房山一模 第18题第（1）问（主观题）",
        "material_trigger": "评标细则把治理路径二写为“矛盾分析法/具体问题具体分析/两点论与重点论统一/分析与综合”，答案示例写“分区分类、一企一策，做到具体问题具体分析”。",
        "question_prompt": Q18_1_PROMPT,
        "why_trigger": "看到“精准施策”“分区分类”“一企一策”，应想到矛盾具有特殊性，治理不能一刀切，必须具体问题具体分析。",
        "answer_landing": "卷面可写：北京抓住不同区域、行业、企业污染成因的差异，分区分类、一企一策，做到具体问题具体分析，提高治理的针对性和实效性。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q18_SOURCE_LINES,
    },
    {
        "canonical_node": "两点论与重点论",
        "question_no": "Q18(1)",
        "heading_suffix": "2026房山一模 第18题第（1）问（主观题）",
        "material_trigger": "评标细则明确写“矛盾分析法/具体问题具体分析/两点论与重点论统一/分析与综合”，答案示例写“聚焦重点领域，分区分类、一企一策”。",
        "question_prompt": Q18_1_PROMPT,
        "why_trigger": "北京蓝天治理既统筹多方面问题，又聚焦重点领域和重点环节。看到“聚焦重点领域”，应想到坚持两点论与重点论统一。",
        "answer_landing": "卷面可写：治理常态蓝天既要全面分析污染治理的多方面矛盾，又要抓主要矛盾和重点领域，通过精准施策带动整体治理提升。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q18_SOURCE_LINES,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q20",
        "heading_suffix": "2026房山一模 第20题（主观题）",
        "material_trigger": "评标细则6-8分层级列出“系统优化等”，设问要求认识依法治国和依规治党有机统一。",
        "question_prompt": Q20_PROMPT,
        "why_trigger": "依法治国和依规治党不是两条割裂线，而是在中国特色社会主义法治体系和党的建设体系中相互支撑、协同推进。",
        "answer_landing": "卷面可写：坚持系统观念，把依法治国和依规治党放在推进中国式现代化和国家治理现代化的整体中统筹，使国家法律规范体系和党内法规制度体系协同发力。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q20_SOURCE_LINES,
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q20",
        "heading_suffix": "2026房山一模 第20题（主观题）",
        "material_trigger": "评标细则6-8分层级列出“认识与实践”，要求从原因、关系、意义和行动层面综合说明有机统一。",
        "question_prompt": Q20_PROMPT,
        "why_trigger": "依法治国和依规治党的统一来自新时代治国理政实践，也要回到实践中检验和完善制度建设。",
        "answer_landing": "卷面可写：实践是认识的基础，新时代全面依法治国和全面从严治党的实践推动我们深化对二者关系的认识；正确认识又指导制度建设和治理实践不断完善。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q20_SOURCE_LINES,
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q20",
        "heading_suffix": "2026房山一模 第20题（主观题）",
        "material_trigger": "评标细则列“中国共产党的地位、矛盾等”，并在4-5分层级要求写明二者“联系/对立统一于中国式现代化建设进程中”。",
        "question_prompt": Q20_PROMPT,
        "why_trigger": "“依法治国”和“依规治党”分属国家法律规范和党内法规制度，但二者在中国式现代化治理进程中相互联系、相互支撑。",
        "answer_landing": "卷面可写：矛盾双方既有区别又有联系。依法治国和依规治党各有侧重，又统一于坚持党的领导、人民当家作主和依法治国有机统一的实践中，必须协同推进。",
        "evidence_level": "评分细则原文明示",
        "source_lines": Q20_SOURCE_LINES,
    },
]

SECTION_NEXT = {
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
    "尊重客观规律与发挥主观能动性相结合": "规律的客观性",
    "联系的普遍性 / 联系的观点（总）": "联系的客观性",
    "整体与部分": "系统观念 / 系统优化",
    "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
    "量变与质变 / 适度原则": "事物发展是前进性与曲折性的统一",
    "矛盾的特殊性 / 具体问题具体分析": "矛盾的普遍性和特殊性",
    "矛盾的普遍性和特殊性": "主要矛盾和次要矛盾",
    "两点论与重点论": "内因与外因",
    "实践与认识（总）": "实践是认识的基础",
    "矛盾就是对立统一": "矛盾的普遍性",
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_fangshan_yimo_batch12_{timestamp}.docx")
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
        "source_lane": "Codex Batch12 recovery production",
        "source_repair_basis": entry["source_lines"],
        "source_lines": entry["source_lines"],
        "batch": "batch12_2026_fangshan_yimo",
    }


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch12_fangshan_yimo_{timestamp}{LEDGER.suffix}")
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
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch12_fangshan_yimo_{timestamp}{ACCEPTED.suffix}")
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
    needs: str,
    action: str,
    note: str,
    artifact: str,
) -> dict[str, str]:
    return {
        KEYS["id"]: row_id,
        "row_source": "batch12_2026_fangshan_yimo_missing_choice_inventory",
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
        KEYS["needs"]: needs,
        KEYS["action"]: action,
        KEYS["note"]: note,
        KEYS["artifact"]: artifact,
    }


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch12_2026_fangshan_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}
    h = dict(zip([(e["question_no"], e["canonical_node"]) for e in ENTRIES], headings))
    q16_note = (
        "Q16(2)已登记现有/新增正文："
        f"{h[('Q16(2)', '一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一')]}；"
        f"{h[('Q16(2)', '尊重客观规律与发挥主观能动性相结合')]}；"
        f"{h[('Q16(2)', '联系的普遍性 / 联系的观点（总）')]}；"
        f"{h[('Q16(2)', '矛盾的普遍性和特殊性')]}；"
        f"{h[('Q16(2)', '整体与部分')]}。"
    )
    q18_note = (
        "Q18(1)已登记现有/新增正文："
        f"{h[('Q18(1)', '系统观念 / 系统优化')]}；"
        f"{h[('Q18(1)', '量变与质变 / 适度原则')]}；"
        f"{h[('Q18(1)', '矛盾的特殊性 / 具体问题具体分析')]}；"
        f"{h[('Q18(1)', '两点论与重点论')]}。"
    )
    q20_note = (
        "Q20已登记现有/新增正文："
        f"{h[('Q20', '系统观念 / 系统优化')]}；"
        f"{h[('Q20', '实践与认识（总）')]}；"
        f"{h[('Q20', '矛盾就是对立统一')]}。"
    )
    q16_principle = "房山一模评标/细则paras13-21明示：矛盾普遍性和特殊性的统一、一切从实际出发、尊重客观规律、发挥主观能动性、联系；高档要求融入大局中找定位/系统/整体。"
    q18_principle = "房山一模评标/细则paras42-49明示：整体性/系统优化、质量互变/发展、具体问题具体分析、两点论与重点论统一、立足实践。"
    q20_principle = "房山一模评标/细则paras69-81明示：矛盾、联系/对立统一、认识与实践、系统优化等。"
    decisions = {
        "M0070": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="矛盾的普遍性和特殊性", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0071": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0072": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="尊重客观规律与发挥主观能动性相结合", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0073": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="整体与部分", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="INSERTED_BATCH12_2026_FANGSHAN_Q16_OVERALL_PART", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0132": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="矛盾的普遍性和特殊性", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0133": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0134": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="尊重客观规律与发挥主观能动性相结合", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0135": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="整体与部分", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="INSERTED_BATCH12_2026_FANGSHAN_Q16_OVERALL_PART", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0169": dict(in_body="是：已由当前DOCX覆盖并补齐整体与部分条目", node="矛盾普遍性与特殊性统一/一切从实际出发/尊重规律-主观能动性/联系观/整体与部分", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0222": dict(in_body="是：已由当前DOCX覆盖并补齐整体与部分条目", node="矛盾普遍特殊统一/一切从实际/规律主观能动/联系立足整体", principle=q16_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH12", note=q16_note, artifact=Q16_SOURCE_LINES),
        "M0566": dict(in_body="否：法律与生活/法治知识边界题", node="不进入当前哲学宝典正文", principle="Q17(1)民事法律关系，Q17(2)法治知识；价值观字样是法治题可选表达，不构成必修四哲学正文落点。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH12", note="不把法治题中的价值表达转入价值观节点。", artifact=f"{RUBRIC_DOCX}:paras23-41; {PAPER_RENDER}/page_008.png"),
        "M0567": dict(in_body="是：已由当前DOCX覆盖并补齐两点论与重点论条目", node="系统观念/量变质变/具体问题具体分析/两点论与重点论", principle=q18_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH12", note=q18_note, artifact=Q18_SOURCE_LINES),
        "M0568": dict(in_body="否：选必一当代国际政治与经济边界题", node="不进入当前哲学宝典正文", principle="Q19设问要求运用《当代国际政治与经济》知识，说明海南自由贸易港封关如何助力国际循环。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH12", note="不把选必一题转入必修四哲学正文。", artifact=f"{RUBRIC_DOCX}:paras61-68; {PAPER_RENDER}/page_010.png"),
        "M0569": dict(in_body="是：已由当前DOCX覆盖并补齐矛盾对立统一条目", node="系统观念 / 实践与认识 / 矛盾就是对立统一", principle=q20_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH12", note=q20_note, artifact=Q20_SOURCE_LINES),
        "M0570": dict(in_body="否：抽取残留/混合题号", node="不进入当前哲学宝典正文", principle="该行没有独立题号，内容为Q16-Q20抽取残留；本批已逐题处理Q16-Q20。", evidence="逐题回源清理", misplaced="否", needs="否", action="EXTRACTION_RESIDUE_CLOSED_BATCH12", note="用Q16-Q20逐题行替代残留行。", artifact=f"{SOURCE_BUNDLE}; {RUBRIC_DOCX}:paras13-81"),
        "M0798": dict(in_body="套卷级旧行已拆分为逐题行", node="SUITE_LEVEL_SUMMARY", principle="当前有效状态见Q16-Q20回源行和新增Q1-Q15选择题答案键blocker行。", evidence="Batch12逐题拆分", misplaced="否", needs="否", action="SUPERSEDED_BY_BATCH12_PER_QUESTION_ROWS", note="套卷级记录不替代逐题记录。", artifact=f"{SOURCE_BUNDLE}; {PAPER_RENDER}/page_001.png-page_011.png"),
        "M0847": dict(in_body="套卷级旧行已拆分为逐题行", node="SUITE_LEVEL_SUMMARY", principle="当前有效状态见Q16-Q20回源行和新增Q1-Q15选择题答案键blocker行。", evidence="Batch12逐题拆分", misplaced="否", needs="否", action="SUPERSEDED_BY_BATCH12_PER_QUESTION_ROWS", note="Q1-Q15仍需答案键，已拆成M0880起逐题挂起。", artifact=f"{SOURCE_BUNDLE}; {PAPER_RENDER}/page_001.png-page_011.png"),
    }
    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)

    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    no_key_evidence = "PDF渲染目测题干；未找到可靠选择题答案键，不能裁决正确项及是否入正文"
    choice_rows = [
        ("Q1", "文化/精神谱系选择题", "伟大建党精神和精神谱系相关选择题；缺少官方答案键，不能确认正确项是否进入必修四宝典。", "page_001.png"),
        ("Q2", "文化/价值选择题", "价值观/文化表达相关选择题；缺少官方答案键，不能确认正确项是否进入必修四宝典。", "page_002.png"),
        ("Q3", "文化传承选择题", "汉服、唐妆、非遗、国风等文化传承相关选择题；缺少官方答案键，不能确认正确项是否进入必修四宝典。", "page_002.png"),
        ("Q4", "马克思主义理论/哲学候选选择题", "马克思主义理论研究和区域实践相关选择题；缺少官方答案键，不能确认真理条件、系统优化、社会意识等选项是否为正确项。", "page_002.png"),
        ("Q5", "逻辑推理/一国两制选择题", "十五运会、一国两制和逻辑推理相关选择题；缺少官方答案键，不能确认是否仅为选必三边界题。", "page_003.png"),
        ("Q6", "逻辑与科学思维选择题", "光的波粒二象性和科学实验相关选择题；缺少官方答案键，不能确认是否仅为逻辑与思维边界题。", "page_003.png"),
        ("Q7", "逻辑/创新思维候选选择题", "春晚机器人武术表演相关选择题；缺少官方答案键，不能确认实践、创新思维或意识能动性等选项是否为正确项。", "page_003.png"),
        ("Q8", "政治与法治/党员干部选择题", "党员干部、红色传统和公共服务相关选择题；缺少官方答案键，暂不作正文依据。", "page_004.png"),
        ("Q9", "政治与法治/人大执法检查选择题", "文明行为促进条例执法检查相关选择题；缺少官方答案键，暂不作正文依据。", "page_004.png"),
        ("Q10", "法律与生活/人格权选择题", "公共直播、隐私权/肖像权相关选择题；缺少官方答案键，暂不作正文依据。", "page_004.png"),
        ("Q11", "法律与生活/债务清偿选择题", "债务清偿/破产修复相关选择题；缺少官方答案键，暂不作正文依据。", "page_005.png"),
        ("Q12", "政治与法治/社会救助立法选择题", "社会救助立法相关选择题；缺少官方答案键，暂不作正文依据。", "page_005.png"),
        ("Q13", "经济与社会/国企新质生产力选择题", "中央企业和新质生产力相关选择题；缺少官方答案键，暂不作正文依据。", "page_005.png"),
        ("Q14", "经济与社会/创新创业选择题", "独角兽企业、创新创业和经营机制相关选择题；缺少官方答案键，暂不作正文依据。", "page_006.png"),
        ("Q15", "当代国际政治与经济/全球治理选择题", "全球治理倡议相关选择题；缺少官方答案键，暂不作正文依据。", "page_006.png"),
    ]
    existing_choice_keys = {
        (r[KEYS["source"]], r[KEYS["question"]], r.get("row_source", ""))
        for r in rows
    }
    additions = []
    for idx, (q, type_, principle, page) in enumerate(choice_rows, start=1):
        additions.append(
            row_values(
                f"M{max_id + idx:04d}",
                q,
                type_,
                "待定：缺少可靠选择题答案键，不能裁决是否进宝典",
                "ANSWER_KEY_REQUIRED_BEFORE_PLACEMENT",
                principle,
                no_key_evidence,
                "是：缺少可靠选择题答案键，不能逐项裁决",
                "NEED_ANSWER_KEY_BATCH12",
                "房山一模原始目录仅发现试卷PDF和主观题评标/细则docx；未发现Q1-Q15官方答案键。",
                f"{PAPER_RENDER}/{page}",
            )
        )
    for row in additions:
        key = (row[KEYS["source"]], row[KEYS["question"]], row["row_source"])
        if key not in existing_choice_keys:
            rows.append(row)
            existing_choice_keys.add(key)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_source_transcription(timestamp: str) -> None:
    text = f"""# Batch12 Source Transcription - 2026房山一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026房山一模
status: SOURCE_PACKET_PARTIAL_WITH_CHOICE_ANSWER_KEY_BLOCKER

## Source Files Checked

- paper PDF: `2026各区模拟题/2026各区一模/2026房山一模/2026北京房山高三一模政治.pdf`
- rendered paper pages: `{PAPER_RENDER}/page_001.png` to `page_011.png`
- rubric/marking file: `{RUBRIC_DOCX}`
- detail rule file: `{DETAIL_RULE_DOCX}`

## Choice Questions Q1-Q15

The PDF has no text layer in the preprocessed cache and the available rubric/docx files only cover the subjective questions. No reliable official answer key for Q1-Q15 was found in the current source directory. Therefore Q1-Q15 were added to `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` as per-question rows with `NEED_ANSWER_KEY_BATCH12`; none of these choice questions were inserted into the DOCX body.

Page map:

- Q1: `{PAPER_RENDER}/page_001.png`
- Q2-Q4: `{PAPER_RENDER}/page_002.png`
- Q5-Q7: `{PAPER_RENDER}/page_003.png`
- Q8-Q10: `{PAPER_RENDER}/page_004.png`
- Q11-Q13: `{PAPER_RENDER}/page_005.png`
- Q14-Q15: `{PAPER_RENDER}/page_006.png`

## Q16(2)

Prompt: {Q16_2_PROMPT}

Rubric paragraphs 13-21 support:

- 矛盾普遍性和特殊性的统一
- 一切从实际出发 / 开展调查研究 / 从客观存在的事物出发
- 尊重客观规律
- 发挥主观能动性
- 联系的观点 / 在大局中找准定位
- 高档要求：融入大局中找定位 / 系统 / 整体

Disposition: retain/register existing entries for 实事求是、规律与主观能动性、联系观、矛盾普遍性与特殊性; add/register 整体与部分.

## Q17

Rubric paragraphs 23-41 show Q17(1) is 民事法律关系 and Q17(2) is 法治知识. The value-related wording appears inside a law/rule-of-law answer path and is not a standalone 必修四价值观 placement.

Disposition: module-boundary excluded.

## Q18(1)

Prompt: {Q18_1_PROMPT}

Rubric paragraphs 42-49 support:

- 整体性 / 分析与综合 / 联系 / 系统优化
- 矛盾分析法 / 具体问题具体分析 / 两点论与重点论统一 / 分析与综合
- 动态性 / 质量互变 / 发展
- 立足实践 / 注重实践

Disposition: retain/register existing 系统观念、量变质变、具体问题具体分析 entries; add/register 两点论与重点论.

## Q19

Prompt/rubric paragraphs 61-68 require 《当代国际政治与经济》 and discuss 海南自由贸易港封关助力国际循环.

Disposition: module-boundary excluded.

## Q20

Prompt: {Q20_PROMPT}

Rubric paragraphs 69-81 support:

- 矛盾等
- 联系 / 对立统一于中国式现代化建设进程中
- 认识与实践
- 系统优化等

Disposition: retain/register existing 系统观念 and 实践与认识 entries; add/register 矛盾就是对立统一.
"""
    SOURCE_TRANSCRIPTION.write_text(text, encoding="utf-8")


def write_report(timestamp: str, headings: list[str]) -> None:
    inserted = "\n".join(f"- {heading}" for heading in headings)
    text = f"""# Coverage Fusion Batch12 - 2026房山一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026房山一模
status: CODEX_BATCH12_SOURCE_COVERAGE_PARTIAL_WITH_CHOICE_ANSWER_KEY_BLOCKER

## Applied To DOCX / Ledger / Accepted

{inserted}

## Matrix Disposition

- Existing Q16(2) rows were re-grounded in 房山一模评标/细则paras13-21 and registered in `docx_insert_ledger.csv` plus `student_patch_entries.accepted.jsonl`.
- Q16(2) `整体与部分` was newly inserted because the rubric explicitly says “融入大局中找定位/系统/整体”.
- Q17 was excluded as legal/rule-of-law boundary.
- Q18(1) existing 系统观念、量变质变、具体问题具体分析 entries were registered; `两点论与重点论` was newly inserted because the rubric explicitly lists it.
- Q19 was excluded as 《当代国际政治与经济》 boundary.
- Q20 existing 系统观念 and 实践与认识 entries were registered; `矛盾就是对立统一` was newly inserted because the rubric explicitly lists “矛盾” and “联系/对立统一”.
- Q1-Q15 were added as individual rows with `NEED_ANSWER_KEY_BATCH12` because no reliable official answer key was found for the choice questions.

## Boundary

No Sonnet/Haiku/model-unknown output was used. The suite is not closed: Q1-Q15 remain blocked until an official answer key or equivalent reliable scoring source is found.
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
    print(f"Batch12 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
