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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH09_2025_FENGTAI_YIMO_CODEX_20260525.md"
SUITE = "2025丰台一模"

QUESTION_15 = (
    "在近现代人类社会发展的历史进程中，处理国与国关系，共同维护世界和平与安宁，促进全人类发展与进步，始终是各国不懈探索的重大命题。"
    "20世纪50年代，中国领导人首次完整提出和平共处五项原则这个“历史答案”；进入新时代，中国又给出了构建人类命运共同体这个“时代答案”。"
    "上述两个“答案”：①体现中国外交理念和政策连续性与创新性的有机统一；②展现中国对如何处理国际关系的积极探索与担当作为；"
    "③旨在提升发展中国家在全球治理中的发言权和话语权；④表明中国是维护世界和平与发展的主导力量和积极因素。"
    "A.①② B.①③ C.②③ D.②④。官方答案：A。"
)

QUESTION_18_1 = "结合材料，分析我国在推动新一代人工智能发展的过程中是如何运用科学思维的。"

ENTRIES = [
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q15",
        "heading_suffix": "2025丰台一模 第15题（选择题）",
        "material_trigger": "题干把20世纪50年代和平共处五项原则称为“历史答案”，把新时代构建人类命运共同体称为“时代答案”；正确项①明确“连续性与创新性的有机统一”。",
        "question_prompt": QUESTION_15,
        "why_trigger": "看到“历史答案”和“时代答案”并列，又看到正确项直接写“连续性与创新性的有机统一”，应落到守正创新和辩证否定。新时代中国外交不是抛弃既有理念，而是在继承和平共处等基本精神的基础上，根据新的时代条件提出新的中国方案。",
        "answer_landing": "本题应选A。本节点处理①：和平共处五项原则与构建人类命运共同体既一脉相承，又面向新时代国际关系的新问题作出创新发展；这体现对既有外交理念的继承、发展和创新，是连续性与创新性的有机统一。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2025丰台一模.md:350-361;468-504",
    },
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q18(1)",
        "heading_suffix": "2025丰台一模 第18题第（1）问（主观题）",
        "material_trigger": "人工智能规划材料写明我国按2020、2025、2030三步战略目标推进人工智能发展；18(1)评分标准明确“我国从实际出发”单独给1分。",
        "question_prompt": QUESTION_18_1,
        "why_trigger": "看到国家根据人工智能技术基础、应用水平、教育变革需要和未来发展趋势作出分段规划，并且细则直接给出“从实际出发”评分点，应落到一切从实际出发。这里的关键不是空喊科技强国，而是把战略部署建立在人工智能发展阶段和国家现实需要之上。",
        "answer_landing": "答案落点：我国推动新一代人工智能发展，坚持从实际出发，根据人工智能技术发展水平、产业应用状况和教育变革需要作出阶段性战略安排；这样才能使主观规划符合客观实际，在实践中检验并完善政策部署。",
        "evidence_level": "正式细则局部评分点（科学思维设问中的从实际出发）",
        "source_lines": "01_source_inventory/suite_source_bundles/2025丰台一模.md:67-73;390-396;531-535",
    },
]

SECTION_NEXT = {
    "辩证否定 / 守正创新": "矛盾就是对立统一",
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
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


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def set_plain_text(p: etree._Element, text: str) -> None:
    texts = p.xpath(".//w:t", namespaces=NS)
    if not texts:
        r = etree.SubElement(p, W + "r")
        t = etree.SubElement(r, W + "t")
        t.text = text
        return
    texts[0].text = text
    for node in texts[1:]:
        node.text = ""


def make_run(text: str, *, label: bool = False) -> etree._Element:
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


def set_label_text(p: etree._Element, label: str, rest: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + rest))
    ppr = p.find("./w:pPr", namespaces=NS)
    if ppr is None:
        ppr = etree.Element(W + "pPr", nsmap=p.nsmap)
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def find_section(paras: list[etree._Element], heading: str) -> tuple[int, int]:
    next_heading = SECTION_NEXT[heading]
    start = next((i for i, p in enumerate(paras) if para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section heading not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if para_text(paras[i]).strip() == next_heading), None)
    if end is None:
        raise RuntimeError(f"next heading not found after {heading}: {next_heading}")
    return start, end


def insert_entry(root: etree._Element, entry: dict[str, str]) -> str:
    body = root.find("w:body", namespaces=NS)
    if body is None:
        raise RuntimeError("word/document.xml has no body")
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    existing = next((para_text(paras[i]).strip() for i in range(start + 1, end) if para_text(paras[i]).strip().endswith(entry["heading_suffix"])), None)
    if existing:
        return existing

    numbered = []
    for idx in range(start + 1, end):
        text = para_text(paras[idx]).strip()
        m = re.match(r"^(\d+)\.\s", text)
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_fengtai_yimo_batch09_{timestamp}.docx")
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
                payload = data[info.filename]
                zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                zi.compress_type = info.compress_type
                zi.external_attr = info.external_attr
                zout.writestr(zi, payload)
        shutil.move(tmp_path, docx)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    return headings


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch09_fengtai_yimo_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    desired = {
        (entry["canonical_node"], SUITE, entry["question_no"]): {
            "canonical_node": entry["canonical_node"],
            "source_suite": SUITE,
            "question_no": entry["question_no"],
            "inserted_heading": heading,
        }
        for entry, heading in zip(ENTRIES, headings)
    }
    cleaned: list[dict[str, str]] = []
    seen = set()
    for row in rows:
        key = (row["canonical_node"], row["source_suite"], row["question_no"])
        if key in desired:
            if key not in seen:
                cleaned.append(desired[key])
                seen.add(key)
            continue
        cleaned.append(row)
    rows = cleaned
    for key, row in desired.items():
        if key not in seen:
            rows.append(row)
            seen.add(key)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def accepted_record(entry: dict[str, str], heading: str) -> dict[str, str]:
    return {
        "source_suite": SUITE,
        "question_no": entry["question_no"],
        "canonical_node": entry["canonical_node"],
        "student_facing_text": (
            f"{heading}\n"
            f"【材料触发点】 {entry['material_trigger']}\n"
            f"【设问】 {entry['question_prompt']}\n"
            f"【为什么能想到】 {entry['why_trigger']}\n"
            f"【答案落点】 {entry['answer_landing']}"
        ),
        "evidence_level": entry["evidence_level"],
        "source_lines": entry["source_lines"],
        "batch": "batch09_2025_fengtai_yimo",
    }


def update_accepted(timestamp: str, headings: list[str]) -> None:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch09_fengtai_yimo_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup)
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    desired = {
        (SUITE, entry["question_no"], entry["canonical_node"]): accepted_record(entry, heading)
        for entry, heading in zip(ENTRIES, headings)
    }
    cleaned: list[dict[str, str]] = []
    seen = set()
    for record in records:
        key = (record.get("source_suite"), record.get("question_no"), record.get("canonical_node"))
        if key in desired:
            if key not in seen:
                cleaned.append(desired[key])
                seen.add(key)
            continue
        cleaned.append(record)
    records = cleaned
    for key, record in desired.items():
        if key not in seen:
            records.append(record)
            seen.add(key)
    ACCEPTED.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n", encoding="utf-8")


def patch_row(row: dict[str, str], **values: str) -> None:
    for key, value in values.items():
        row[KEYS[key]] = value


def row_values(row_id: str, q: str, type_: str, in_body: str, node: str, principle: str, evidence: str, misplaced: str, needs: str, action: str, note: str, artifact: str) -> dict[str, str]:
    return {
        KEYS["id"]: row_id,
        "row_source": "batch09_2025_fengtai_yimo_recovery",
        KEYS["source"]: SUITE,
        KEYS["year"]: "2025",
        KEYS["stage"]: "一模",
        KEYS["question"]: q,
        KEYS["type"]: type_,
        KEYS["in_body"]: in_body,
        KEYS["node"]: node,
        KEYS["principle"]: principle,
        KEYS["evidence"]: evidence,
        KEYS["misplaced"]: misplaced,
        KEYS["needs"]: needs,
        KEYS["action"]: action,
        KEYS["note"]: note,
        KEYS["artifact"]: artifact,
    }


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch09_2025_fengtai_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    by_id = {r[KEYS["id"]]: r for r in rows}
    common = "01_source_inventory/suite_source_bundles/2025丰台一模.md"
    q15_heading, q18_1_heading = headings
    decisions = {
        "M0104": dict(in_body="否：文化线边界，不进当前哲学主线", node="不进入当前哲学宝典正文", principle="Q16正式细则有传承中华优秀传统文化/传统美德角度，属于文化线；当前哲学主线不补。", evidence="正式细则-文化线边界", misplaced="否", needs="否", action="EXCLUDE_OR_ROUTE_TO_CULTURE_LINE_BATCH09", note="文化线另审，不混入哲学主框架。", artifact=f"{common}:15-31;364-369;511-524"),
        "M0105": dict(in_body="是：已由当前DOCX覆盖", node="价值判断与价值选择", principle="Q16评分标准说明明确可从坚持正确价值观、做出正确价值判断和价值选择角度作答。", evidence="正式细则-哲学可用知识明示+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="现有DOCX已有Q16价值判断与价值选择条目。", artifact=f"{common}:21-31;364-369;511-524"),
        "M0106": dict(in_body="否：文化线边界，不进当前哲学主线", node="不进入当前哲学宝典正文", principle="Q16民族精神/时代精神/家国情怀属于文化线，不进入当前哲学主框架。", evidence="正式细则-文化线边界", misplaced="否", needs="否", action="EXCLUDE_OR_ROUTE_TO_CULTURE_LINE_BATCH09", note="文化线另审。", artifact=f"{common}:15-31;364-369;511-524"),
        "M0107": dict(in_body="是：已由当前DOCX覆盖", node="联系的普遍性 / 联系的观点（总）", principle="Q18(3)评分标准明确可从联系观等角度阐述人与人工智能的关系；当前DOCX已有联系观Q18(3)条目。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="不把广义角度提示升格为逐点细则。", artifact=f"{common}:88-97;417-420;546-559"),
        "M0108": dict(in_body="是：已由当前DOCX覆盖", node="发展的观点 / 发展的普遍性", principle="Q18(3)评分标准明确可从发展观等角度阐述人与人工智能的关系；当前DOCX已有发展观Q18(3)条目。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="不把广义角度提示升格为逐点细则。", artifact=f"{common}:88-97;417-420;546-559"),
        "M0109": dict(in_body="是：已由当前DOCX覆盖", node="矛盾就是对立统一", principle="Q18(3)评分标准明确可从矛盾观等角度阐述人与人工智能的关系；当前DOCX已有矛盾对立统一Q18(3)条目。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="不把广义角度提示升格为逐点细则。", artifact=f"{common}:88-97;417-420;546-559"),
        "M0110": dict(in_body="是：已由当前DOCX覆盖", node="价值观的导向作用；价值判断与价值选择", principle="Q18(3)评分标准明确可从价值观等角度阐述人与人工智能的关系；当前DOCX已有价值观相关Q18(3)条目。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="不把广义角度提示升格为逐点细则。", artifact=f"{common}:88-97;417-420;546-559"),
        "M0174": dict(in_body="是：价值判断节点已覆盖；文化线不入当前哲学主线", node="价值判断与价值选择；文化线另审", principle="Q16正式细则支持价值判断与价值选择；民族精神、传统美德为文化线。", evidence="正式细则-哲学可用知识明示+文化线边界", misplaced="否", needs="否", action="COVERED_AND_CULTURE_BOUNDARY_BATCH09", note="关闭Q16混合挂起。", artifact=f"{common}:15-31;364-369;511-524"),
        "M0175": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一", principle="Q18(1)正式细则在科学思维设问中明确“我国从实际出发”单独给1分。", evidence="正式细则局部评分点（科学思维设问中的从实际出发）", misplaced="否", needs="否", action="INSERTED_BATCH09_2025_FENGTAI_Q18_1_REALITY", note=f"新增条目：{q18_1_heading}；科学思维主线不整体纳入，只采明确哲学方法论落点。", artifact=f"{common}:67-73;390-396;531-535"),
        "M0176": dict(question="Q18(3)", in_body="是：已由当前DOCX覆盖", node="联系观/发展观/矛盾观/价值观", principle="原行题号误写为Q18(2)，实际对应Q18(3)人与人工智能关系；评分标准明确可从联系观、发展观、矛盾观、价值观等角度阐述。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="QUESTION_NUMBER_CORRECTED_AND_COVERED_BATCH09", note="题号从Q18(2)更正为Q18(3)；Q18(2)经济逻辑不入哲学宝典。", artifact=f"{common}:88-97;417-420;546-559"),
        "M0204": dict(in_body="是：价值判断节点已覆盖；文化线不入当前哲学主线", node="价值判断与价值选择；文化线另审", principle="Q16母版核定：价值判断节点有正式细则支持，民族精神/传统美德为文化线边界。", evidence="正式细则-哲学可用知识明示+文化线边界", misplaced="否", needs="否", action="COVERED_AND_CULTURE_BOUNDARY_BATCH09", note="关闭母版核定挂起。", artifact=f"{common}:15-31;364-369;511-524"),
        "M0205": dict(question="Q18(3)", in_body="是：已由当前DOCX覆盖", node="联系观/发展观/矛盾观/价值观", principle="原行题号误写为Q18(2)，实际对应Q18(3)人与人工智能关系；证据为正式评分标准角度提示。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="QUESTION_NUMBER_CORRECTED_AND_COVERED_BATCH09", note="不把参考答案冒充逐点细则。", artifact=f"{common}:88-97;417-420;546-559"),
        "M0354": dict(in_body="否：革命文化/中特边界题", node="不进入当前哲学宝典正文", principle="Q1官方答案A，考查遵义会议主题实践、红色基因、跟党走与长征精神，属于革命文化/中特边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="文化/中特线另审。", artifact=f"{common}:176-186;468-504"),
        "M0355": dict(in_body="是：已由当前DOCX覆盖", node="矛盾就是对立统一", principle="Q2官方答案B，正确项①明确笔画间对立统一成就书法艺术生命力；当前DOCX已有Q2矛盾条目。", evidence="选择题官方答案键+题干正确项链条+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="正确项③偏文化表达，不另拆。", artifact=f"{common}:187-197;468-504"),
        "M0356": dict(in_body="否：文化线边界题", node="不进入当前哲学宝典正文", principle="Q3官方答案C，考查中国建筑承载中华优秀传统文化精神基因，属于文化线。", evidence="官方答案键+文化模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="文化线另审。", artifact=f"{common}:202-213;468-504"),
        "M0357": dict(in_body="是：已由当前DOCX覆盖", node="规律的客观性", principle="Q4官方答案A，正确项②明确尊重自然规律，实现生态环境与基础设施和谐统一；当前DOCX已有Q4规律客观性条目。", evidence="选择题官方答案键+题干正确项链条+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH09", note="正确项①为信息交合法/选必三，不另入哲学主框架。", artifact=f"{common}:214-226;468-504"),
        "M0358": dict(in_body="否：基层治理/政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q5官方答案D，社区共享小屋、邻里议事亭、基层党组织作用，属于基层治理/政治与法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="政治模块排除。", artifact=f"{common}:227-238;468-504"),
        "M0359": dict(in_body="否：经济/数据治理边界题", node="不进入当前哲学宝典正文", principle="Q6官方答案A，公共数据资源登记平台和政府职能，属于经济治理/政府职能边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="经济/政治边界排除。", artifact=f"{common}:239-250;468-504"),
        "M0360": dict(in_body="否：经济与社会边界题", node="不进入当前哲学宝典正文", principle="Q7官方答案D，耐心资本、国资央企、科创企业与新质生产力，属于经济与社会。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="经济模块排除。", artifact=f"{common}:251-262;468-504"),
        "M0361": dict(in_body="否：经济与社会/财政边界题", node="不进入当前哲学宝典正文", principle="Q8官方答案D，零基预算改革、财政支出结构和资金效率，属于经济与社会。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="财政模块排除。", artifact=f"{common}:263-273;468-504"),
        "M0362": dict(in_body="否：政治与法治/国家安全边界题", node="不进入当前哲学宝典正文", principle="Q9官方答案B，网络空间治理、政府依法治理和总体国家安全观，属于政治与法治/国家安全。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="政治法治模块排除。", artifact=f"{common}:274-284;468-504"),
        "M0363": dict(in_body="否：法律与生活边界题", node="不进入当前哲学宝典正文", principle="Q10官方答案B，检察公益诉讼保护新就业形态劳动者权益，属于法律与生活/法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="法律模块排除。", artifact=f"{common}:285-295;468-504"),
        "M0364": dict(in_body="否：法律与生活边界题", node="不进入当前哲学宝典正文", principle="Q11官方答案C，养老卡合同退款、诚信原则与违约责任，属于法律与生活。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="法律模块排除。", artifact=f"{common}:296-308;468-504"),
        "M0365": dict(in_body="否：选必三逻辑与思维边界题", node="不进入当前哲学宝典正文", principle="Q14官方答案C，判断/概念周延关系，属于逻辑与思维。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="Q12/Q13缺失独立行已另补。", artifact=f"{common}:342-349;468-504"),
        "M0366": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="辩证否定 / 守正创新", principle="Q15官方答案A，正确项①明确中国外交理念和政策连续性与创新性的有机统一。", evidence="选择题官方答案键+题干正确项链条", misplaced="否", needs="否", action="INSERTED_BATCH09_2025_FENGTAI_Q15_CONTINUITY_INNOVATION", note=f"新增条目：{q15_heading}", artifact=f"{common}:350-361;468-504"),
        "M0367": dict(in_body="是：价值判断节点已覆盖；文化线不入当前哲学主线", node="价值判断与价值选择；文化线另审", principle="Q16正式细则支持价值判断与选择；传统文化、民族精神、家国情怀为文化线边界。", evidence="正式细则-哲学可用知识明示+文化线边界", misplaced="否", needs="否", action="COVERED_AND_CULTURE_BOUNDARY_BATCH09", note="不新增重复Q16正文。", artifact=f"{common}:15-31;364-369;511-524"),
        "M0368": dict(in_body="否：政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q17正式细则为全过程人民民主、人大制度、政协制度和协商民主，属于政治与法治。", evidence="正式细则-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="政治法治模块排除。", artifact=f"{common}:32-66;374-389;525-530"),
        "M0369": dict(in_body="是：Q18(1)本批新增；Q18(3)已由当前DOCX覆盖；Q18(2)经济边界", node="一切从实际出发；联系观/发展观/矛盾观/价值观", principle="Q18(1)细则明示从实际出发；Q18(3)评分标准明示联系观、发展观、矛盾观、价值观；Q18(2)为经济逻辑。", evidence="正式细则局部评分点+正式评分标准角度提示+现有DOCX正文覆盖", misplaced="否", needs="否", action="Q18_SPLIT_INSERTED_AND_COVERED_BATCH09", note=f"新增Q18(1)：{q18_1_heading}；Q18(3)旧条目保留但证据不升格。", artifact=f"{common}:67-97;390-420;531-559"),
        "M0370": dict(in_body="否：法律与生活边界题", node="不进入当前哲学宝典正文", principle="Q19正式细则为知识产权侵权、市场竞争秩序、司法典型案例和法治信仰，属于法律与生活/法治。", evidence="正式细则-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="法律模块排除。", artifact=f"{common}:98-108;421-429;560-563"),
        "M0371": dict(in_body="否：经济与社会/当代国际政治经济边界题", node="不进入当前哲学宝典正文", principle="Q20正式细则为便利贸易投资、科技创新、高水平对外开放和开放型经济，属于经济与社会/当代国际政治经济。", evidence="正式细则-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="经济/选必一边界排除。", artifact=f"{common}:109-127;430-450;564-567"),
        "M0372": dict(in_body="否：综合时评题，当前哲学宝典不补", node="不进入当前哲学宝典正文", principle="Q21评分标准为党的领导、习近平新时代中国特色社会主义思想、人民至上、新发展理念、制度优势等宽泛综合角度，未给出具体必修四哲学原理落点。", evidence="正式评分标准-综合角度边界（非哲学逐点细则）", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH09", note="不把“变化者”题引和综合角度提示强行转成哲学条目。", artifact=f"{common}:128-155;451-463;568-584"),
        "M0373": dict(in_body="否：抽取残留/模块边界", node="不进入当前哲学宝典正文", principle="该行由Q20/Q21或跨模块材料抽取残留形成，没有独立哲学题号。", evidence="抽取残留清理+源包核对", misplaced="否", needs="否", action="EXTRACTION_RESIDUE_CLOSED_BATCH09", note="关闭Qunknown残留。", artifact=f"{common}:430-584"),
        "M0786": dict(in_body="套卷逐题已由Batch09闭合", node="SUITE_LEVEL_SUMMARY", principle="逐题回源已闭合：Q15/Q18(1)新增，Q2/Q4/Q16/Q18(3)现有覆盖，其余模块边界排除。", evidence="Batch09逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH09", note="套卷级记录不替代逐题记录。", artifact=f"{common}:1-584"),
        "M0833": dict(in_body="套卷逐题已由Batch09闭合", node="SUITE_LEVEL_SUMMARY", principle="逐题回源已闭合：Q15/Q18(1)新增，Q2/Q4/Q16/Q18(3)现有覆盖，其余模块边界排除。", evidence="Batch09逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH09", note="套卷级挂起项关闭。", artifact=f"{common}:1-584"),
    }

    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)

    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    additions = [
        row_values(f"M{max_id + 1:04d}", "Q12", "选必三逻辑与思维边界题", "否：选必三逻辑与思维边界题", "不进入当前哲学宝典正文", "Q12官方答案B，考查联言判断/联言推理与条件推理，属于逻辑与思维。", "官方答案键+模块边界", "否", "否", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH09", "原矩阵缺独立Q12行，本批补充边界闭合。", f"{common}:309-326;468-504"),
        row_values(f"M{max_id + 2:04d}", "Q13", "选必三逻辑与思维边界题", "否：选必三逻辑与思维边界题", "不进入当前哲学宝典正文", "Q13题干为“犯了与示例相同逻辑错误”，官方答案C，属于逻辑与思维；源包选项图文抽取不完整，但不影响当前必修四边界排除。", "官方答案键+题干模块边界", "否", "否", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH09", "原矩阵缺独立Q13行，本批补充边界闭合；选项图像如处理逻辑宝典需另取源页。", f"{common}:327-340;468-504"),
    ]
    existing_keys = {(r[KEYS["source"]], r[KEYS["question"]], r[KEYS["action"]]) for r in rows}
    for row in additions:
        key = (row[KEYS["source"]], row[KEYS["question"]], row[KEYS["action"]])
        if key not in existing_keys:
            rows.append(row)
            existing_keys.add(key)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(timestamp: str, headings: list[str]) -> None:
    text = f"""# Coverage Fusion Batch09 - 2025丰台一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2025丰台一模
status: CODEX_BATCH09_SOURCE_COVERAGE_APPLIED

## Source Basis

- source bundle: `01_source_inventory/suite_source_bundles/2025丰台一模.md`
- formal scoring/rubric lines checked: Q16 `15-31`, Q17 `32-66`, Q18(1) `67-73`, Q18(3) `88-97`, Q19 `98-108`, Q20 `109-127`, Q21 `128-155`
- paper/answer lines checked: Q1-Q15 `176-361`, answer key `468-504`

## Inserted Into DOCX

- {headings[0]} -> 辩证否定 / 守正创新
- {headings[1]} -> 一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一

## Question Disposition

- Q1: excluded, revolution culture/中特 boundary.
- Q2: already covered by current DOCX under 矛盾就是对立统一.
- Q3: excluded, culture-line boundary.
- Q4: already covered by current DOCX under 规律的客观性.
- Q5-Q11: excluded by political, economic, legal, or governance module boundary.
- Q12-Q13: missing rows added and excluded as logic/thinking boundary.
- Q14: excluded as logic/thinking boundary.
- Q15: inserted under 辩证否定 / 守正创新 because correct option ① explicitly says 连续性与创新性的有机统一.
- Q16: value-judgment philosophy node retained; traditional culture/moral/national spirit angles routed to culture line, not current philosophy mainline.
- Q17: excluded by formal Political and Rule of Law rubric.
- Q18(1): inserted only for the explicit formal scoring point “我国从实际出发”; scientific-thinking mainline remains boundary material.
- Q18(2): excluded as economics.
- Q18(3): existing DOCX coverage retained for 联系观、发展观、矛盾观、价值观; evidence is formal scoring-angle/level support, not point-by-point detailed rubric.
- Q19: excluded by formal legal rubric.
- Q20: excluded by formal economic/international-political-economy rubric.
- Q21: excluded as broad综合时评; no specific philosophy point is promoted from broad angle prompts.
- Qunknown: closed as extraction residue.

## Controls

- Sonnet evidence not used.
- GPTPro web / external Claude Opus full-artifact review remains `real_call_pending`.
- ClaudeCode Batch09 Opus 4.7 recheck still must be called after this Codex production patch.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp, headings)
    update_matrix(timestamp, headings)
    write_report(timestamp, headings)
    print(f"Batch09 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
