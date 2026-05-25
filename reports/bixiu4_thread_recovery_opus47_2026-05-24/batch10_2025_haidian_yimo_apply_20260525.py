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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH10_2025_HAIDIAN_YIMO_CODEX_20260525.md"
SUITE = "2025海淀一模"

QUESTION_2 = (
    "华夏先民观天象以授农时，察物候而定节气，在农耕文明中凝练出独特的时序标尺——春生、夏长、秋收、冬藏。"
    "四时轮转，体现生命变化的节奏；寒来暑往，二十四节气循环往复，提示人们顺时而为、与时偕行。"
    "据此，下列说法正确的是：①春生、夏长、秋收、冬藏的时序标尺构建出自在事物间的联系；"
    "②授农时、定节气实现了从思维具体到思维抽象的升华；③顺时而为的农耕文明蕴藏着中华优秀传统文化的核心思想理念；"
    "④与时偕行的实践智慧折射出主动作为与敬畏自然相统一。A.①② B.①④ C.②③ D.③④。官方答案：D。"
)

QUESTION_5 = (
    "生态产品价值实现机制是指在严格保护生态环境的前提下，由政府和市场通过合理的路径和方式，"
    "将生态产品价值转化为经济价值和社会价值的制度形式。据此，下列理解正确的是："
    "①这是运用定义的方法明确“生态产品价值实现机制”的外延；②除非严格保护生态环境，否则不能构建生态产品价值实现机制；"
    "③如果生态产品价值未能成功转化，要么缺少政府作用，要么缺少市场作用；"
    "④完善该机制需要运用矛盾运动的观点，以动态的方式思考生态产品价值。A.①② B.①③ C.②④ D.③④。官方答案：C。"
)

ENTRIES = [
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q2",
        "heading_suffix": "2025海淀一模 第2题（选择题）",
        "material_trigger": "题干以观天象授农时、察物候定节气、顺时而为和与时偕行为情境；官方答案D锁定③④，其中④明确“主动作为与敬畏自然相统一”。",
        "question_prompt": QUESTION_2,
        "why_trigger": "看到“顺时而为”不能理解为消极顺从自然，而要和正确项④的“主动作为与敬畏自然相统一”连读，应落到尊重客观规律和发挥主观能动性相结合。③属于文化线，本节点不展开。",
        "answer_landing": "本题应选D。本节点只处理④：农耕实践建立在对季节物候规律的把握上，同时人主动安排生产生活，体现按客观规律办事与发挥主观能动性的统一。",
        "evidence_level": "选择题官方答案键+题干正确项链条（正确项④）",
        "source_lines": "01_source_inventory/suite_source_bundles/2025海淀一模.md:241-251;537-538",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q5",
        "heading_suffix": "2025海淀一模 第5题（选择题）",
        "material_trigger": "题干写明生态产品价值实现机制是在严格保护生态环境前提下，由政府和市场推动价值转化；官方答案C锁定②④，其中④直接写“矛盾运动的观点”和“动态的方式”。",
        "question_prompt": QUESTION_5,
        "why_trigger": "看到生态保护与价值转化、政府与市场共同作用，再看到正确项④明确出现“矛盾运动”和“动态方式”，应落到矛盾双方对立统一及矛盾运动。②为条件关系判断，保留边界，不作为本节点正文主证。",
        "answer_landing": "本题应选C。本节点处理④：完善生态产品价值实现机制，要在严格保护生态环境和实现经济社会价值之间动态把握条件、路径与限度，体现用矛盾运动的观点分析和推进制度完善。",
        "evidence_level": "选择题官方答案键+题干正确项链条（正确项④）",
        "source_lines": "01_source_inventory/suite_source_bundles/2025海淀一模.md:278-287;537-541",
    },
]

SECTION_NEXT = {
    "尊重客观规律与发挥主观能动性相结合": "规律的客观性",
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_haidian_yimo_batch10_{timestamp}.docx")
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch10_haidian_yimo_{timestamp}{LEDGER.suffix}")
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
        "batch": "batch10_2025_haidian_yimo",
    }


def update_accepted(timestamp: str, headings: list[str]) -> None:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch10_haidian_yimo_{timestamp}{ACCEPTED.suffix}")
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
        "row_source": "batch10_2025_haidian_yimo_recovery",
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
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch10_2025_haidian_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    by_id = {r[KEYS["id"]]: r for r in rows}
    common = "01_source_inventory/suite_source_bundles/2025海淀一模.md"
    q2_heading, q5_heading = headings
    decisions = {
        "M0021": dict(in_body="是：已由当前DOCX覆盖", node="系统观念 / 系统优化", principle="Q22正式评分标准要求阐释系统观念及其重要性，并结合所选领域说明系统观念的表现；源包展开了普遍联系、全面系统、发展变化、全局局部、当前长远等系统观念链条。", evidence="正式评分标准-系统观念评分点+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH10", note="重引源证关闭，不新增重复条目。", artifact=f"{common}:101-122;203-210;601-616"),
        "M0022": dict(in_body="是：已由当前DOCX覆盖", node="主要矛盾和次要矛盾", principle="Q22系统观念材料明确要求把握全局和局部、主要矛盾和次要矛盾、特殊和一般的关系；当前DOCX已有Q22主次矛盾条目。", evidence="正式评分标准-系统观念展开文本+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH10", note="重引源证关闭，不新增重复条目。", artifact=f"{common}:117-122;601-616"),
        "M0178": dict(in_body="是：已由当前DOCX覆盖", node="矛盾分析法/实践与认识关系/价值观", principle="Q16正式评分标准仅给出可从矛盾分析法、实践与认识的关系、价值观等角度作答，属于角度提示；当前DOCX已有相关节点覆盖，但不升格为逐点细则。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH10", note="证据等级已明确，不再作为遗漏挂起。", artifact=f"{common}:17-20;176-178;554-568"),
        "M0179": dict(question="Q22", in_body="是：已由当前DOCX覆盖", node="系统观念-联系/整体性关联性/主次矛盾/特殊一般", principle="原行题号误写为Q21(8分)，实为Q22系统观念。正式评分标准要求阐释系统观念并结合领域说明表现。", evidence="正式评分标准-系统观念评分点+现有DOCX正文覆盖", misplaced="否", needs="否", action="QUESTION_NUMBER_CORRECTED_AND_COVERED_BATCH10", note="题号由Q21(8分)更正为Q22；真实Q21另补边界行。", artifact=f"{common}:101-122;203-210;601-616"),
        "M0210": dict(in_body="是：已由当前DOCX覆盖", node="矛盾分析法/实践与认识/价值观", principle="Q16正式评分标准为角度提示：可从矛盾分析法、实践与认识的关系、价值观等角度作答；当前DOCX已有对应Q16覆盖。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH10", note="母版核定挂起关闭，但证据不升格。", artifact=f"{common}:17-20;176-178;554-568"),
        "M0211": dict(question="Q22", in_body="是：已由当前DOCX覆盖", node="系统观念/系统优化/主次矛盾", principle="原行题号误写为Q21，实为Q22系统观念。源包正式评分点支持系统观念，展开文本支持主次矛盾。", evidence="正式评分标准-系统观念评分点+现有DOCX正文覆盖", misplaced="否", needs="否", action="QUESTION_NUMBER_CORRECTED_AND_COVERED_BATCH10", note="真实Q21为逻辑与选必一边界，另补独立行。", artifact=f"{common}:101-122;203-210;601-616"),
        "M0431": dict(in_body="否：理论宣讲/政治文化边界题", node="不进入当前哲学宝典正文", principle="Q1官方答案B，正确项为聚焦时代问题、宣讲形式创新激发情感共鸣，属于理论宣讲/政治文化表达，不形成必修四哲学落点。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="不把“大道理大流量”泛化为哲学条目。", artifact=f"{common}:229-239;537"),
        "M0432": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="尊重客观规律与发挥主观能动性相结合", principle="Q2官方答案D，正确项④明确“主动作为与敬畏自然相统一”。", evidence="选择题官方答案键+题干正确项链条（正确项④）", misplaced="否", needs="否", action="INSERTED_BATCH10_2025_HAIDIAN_Q2_RULE_SUBJECTIVITY", note=f"新增条目：{q2_heading}；正确项③为文化线，不在本节点展开。", artifact=f"{common}:241-251;537-538"),
        "M0433": dict(in_body="否：文化交流边界题", node="不进入当前哲学宝典正文", principle="Q3官方答案D，正确项为跨文明对话中的尊重差异、交流借鉴和互补共生，属于文化交流线。", evidence="官方答案键+文化模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="文化线另审。", artifact=f"{common}:252-262;539"),
        "M0434": dict(in_body="否：体育教育/青年责任边界题", node="不进入当前哲学宝典正文", principle="Q4官方答案A，正确项①②指向学生责任和学校全面育人；含“成长成才规律”的③为错误选项，不能作为哲学正文证据。", evidence="官方答案键+错误项剔除", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="不得把错误选项③转成规律条目。", artifact=f"{common}:263-277;540"),
        "M0435": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="矛盾就是对立统一", principle="Q5官方答案C，正确项④明确“运用矛盾运动的观点，以动态的方式思考生态产品价值”。", evidence="选择题官方答案键+题干正确项链条（正确项④）", misplaced="否", needs="否", action="INSERTED_BATCH10_2025_HAIDIAN_Q5_CONTRADICTION_MOVEMENT", note=f"新增条目：{q5_heading}；②为条件关系判断，不作为本哲学节点正文主证。", artifact=f"{common}:278-287;537-541"),
        "M0436": dict(in_body="否：选必三逻辑与思维边界题", node="不进入当前哲学宝典正文", principle="Q6官方答案B，正确项①④为联想思维迁移和想象性；含辩证否定意味的②为错误选项，不能入哲学正文。", evidence="官方答案键+错误项剔除+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="不采错误选项②。", artifact=f"{common}:288-298;542"),
        "M0437": dict(in_body="否：法律/检察公益诉讼边界题", node="不进入当前哲学宝典正文", principle="Q7官方答案D，正确项为公益诉讼检察和普法宣传，属于法律与政治法治边界。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="法律线排除。", artifact=f"{common}:299-310;543"),
        "M0438": dict(in_body="否：养老服务/政治治理边界题", node="不进入当前哲学宝典正文", principle="Q8官方答案A，正确项为基层党组织作用和志愿服务，属于养老服务治理/政治与法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="政治治理线排除。", artifact=f"{common}:311-321;544"),
        "M0439": dict(in_body="否：政协/区域协作边界题", node="不进入当前哲学宝典正文", principle="Q9官方答案D，考查政协优势、双向沟通和铸牢中华民族共同体意识，属于政治与法治/政协。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="政治模块排除。", artifact=f"{common}:326-332;545"),
        "M0440": dict(in_body="否：经济与社会边界题", node="不进入当前哲学宝典正文", principle="Q12官方答案C，民营企业参股核电项目涉及股权结构、市场准入和营商环境，属于经济与社会。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="经济模块排除。", artifact=f"{common}:354-364;548"),
        "M0441": dict(in_body="否：选必一国际经济政治边界题", node="不进入当前哲学宝典正文", principle="Q14官方答案D，国际金融体系、全球治理和南南合作/南北对话，属于当代国际政治与经济。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="选必一另审。", artifact=f"{common}:377-387;550"),
        "M0442": dict(in_body="否：国际关系/公共外交边界题", node="不进入当前哲学宝典正文", principle="Q15官方答案B，正确项为人民友谊促进国际关系和多样化人民交往，属于国际关系/公共外交。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="选必一/文化交流边界排除。", artifact=f"{common}:388-403;551"),
        "M0443": dict(in_body="是：已由当前DOCX覆盖", node="矛盾分析法/实践与认识/价值观", principle="Q16正式评分标准仅给出矛盾分析法、实践与认识的关系、价值观等角度，当前DOCX已覆盖对应Q16条目；证据等级按角度提示处理。", evidence="正式评分标准-角度提示+现有DOCX正文覆盖（非逐点细则）", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH10", note="不新增重复Q16。", artifact=f"{common}:406-415;554-568"),
        "M0444": dict(in_body="否：政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q17正式评分标准为人民主体地位、社会治理法治化和法治宣传教育，属于政治与法治。", evidence="正式评分标准-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="政治法治模块排除。", artifact=f"{common}:24-31;569-576"),
        "M0445": dict(in_body="否：法律与生活边界题", node="不进入当前哲学宝典正文", principle="Q18正式评分标准为格式合同、诚信原则和合同解除，属于法律与生活。", evidence="正式评分标准-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="法律模块排除。", artifact=f"{common}:38-41;577-580"),
        "M0446": dict(in_body="否：政治与法治/基层治理边界题", node="不进入当前哲学宝典正文", principle="Q19正式评分标准为党的领导、法治政府和多方参与社会治理，属于政治与法治/基层治理。", evidence="正式评分标准-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="政治法治模块排除。", artifact=f"{common}:44-56;581-585"),
        "M0447": dict(in_body="否：经济与社会/政协边界题", node="不进入当前哲学宝典正文", principle="Q20正式评分标准甲为企业经营，乙为政协委员履职；源包明确乙为必修三模块且无其他模块替换，不得混搭模块。", evidence="正式评分标准-模块边界+禁止混搭提示", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH10", note="不得用普通参考答案或其他模块提示混入哲学正文。", artifact=f"{common}:58-81;586-594"),
        "M0448": dict(question="Q22", in_body="是：已由当前DOCX覆盖", node="系统观念 / 系统优化；主要矛盾和次要矛盾", principle="原行题号记为Q21但内容对应Q22系统观念。正式评分点支持系统观念，展开文本支持主要矛盾和次要矛盾。", evidence="正式评分标准-系统观念评分点+现有DOCX正文覆盖", misplaced="否", needs="否", action="QUESTION_NUMBER_CORRECTED_AND_COVERED_BATCH10", note="真实Q21另补边界行。", artifact=f"{common}:101-122;203-210;601-616"),
        "M0449": dict(in_body="否：抽取残留/题号不明", node="不进入当前哲学宝典正文", principle="该行无可核定独立题号；经Q1-Q22回源，真实缺行已补为Q10、Q11、Q13、Q21，残留关闭。", evidence="抽取残留清理+逐题源包核对", misplaced="否", needs="否", action="EXTRACTION_RESIDUE_CLOSED_BATCH10", note="不保留Qunknown挂起。", artifact=f"{common}:1-616"),
        "M0790": dict(in_body="套卷逐题已由Batch10闭合", node="SUITE_LEVEL_SUMMARY", principle="逐题回源已闭合：Q2/Q5新增，Q16/Q22现有覆盖并重引源证，其余模块边界排除或另补边界行。", evidence="Batch10逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH10", note="套卷级记录不替代逐题记录。", artifact=f"{common}:1-616"),
        "M0835": dict(in_body="套卷逐题已由Batch10闭合", node="SUITE_LEVEL_SUMMARY", principle="逐题回源已闭合：Q2/Q5新增，Q16/Q22现有覆盖并重引源证，其余模块边界排除或另补边界行。", evidence="Batch10逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH10", note="原套卷级挂起项关闭。", artifact=f"{common}:1-616"),
    }

    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)

    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    additions = [
        row_values(f"M{max_id + 1:04d}", "Q10", "法律与生活边界题", "否：法律与生活边界题", "不进入当前哲学宝典正文", "Q10官方答案C，考查未成年人侵权、举证责任和法院裁判原则，属于法律与生活。", "官方答案键+模块边界", "否", "否", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH10", "原矩阵缺独立Q10行，本批补充边界闭合。", f"{common}:333-343;546"),
        row_values(f"M{max_id + 2:04d}", "Q11", "法律/创业经营边界题", "否：法律与创业经营边界题", "不进入当前哲学宝典正文", "Q11官方答案A，考查合伙企业、有限责任公司和创业法律形式，属于法律与生活/经营主体边界。", "官方答案键+模块边界", "否", "否", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH10", "原矩阵缺独立Q11行，本批补充边界闭合。", f"{common}:344-353;547"),
        row_values(f"M{max_id + 3:04d}", "Q13", "经济/智慧监管边界题", "否：经济与监管边界题", "不进入当前哲学宝典正文", "Q13官方答案B，产品数字护照为监管部门提供可追溯数据、提高智慧监管水平，属于经济治理/监管能力。", "官方答案键+模块边界", "否", "否", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH10", "原矩阵缺独立Q13行，本批补充边界闭合。", f"{common}:365-376;549"),
        row_values(f"M{max_id + 4:04d}", "Q21", "选必三逻辑与思维/选必一国际贸易边界题", "否：逻辑与思维/选必一边界题", "不进入当前哲学宝典正文", "Q21(1)评分标准为演绎推理基本规则；Q21(2)为开放战略、贸易便利化、绿色贸易和国际合作，属于选必三逻辑与选必一国际经济。", "正式评分标准-模块边界", "否", "否", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH10", "原矩阵把Q21误挂到Q22系统观念，本批补真实Q21边界行。", f"{common}:84-98;595-600"),
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
    text = f"""# Coverage Fusion Batch10 - 2025海淀一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2025海淀一模
status: CODEX_BATCH10_SOURCE_COVERAGE_APPLIED

## Source Basis

- source bundle: `01_source_inventory/suite_source_bundles/2025海淀一模.md`
- formal scoring/rubric lines checked: Q16 `17-20;554-568`, Q17 `24-31;569-576`, Q18 `38-41;577-580`, Q19 `44-56;581-585`, Q20 `58-81;586-594`, Q21 `84-98;595-600`, Q22 `101-162;203-210;601-616`
- paper/answer lines checked: Q1-Q15 `229-403`, answer key `537-551`

## Inserted Into DOCX

- {headings[0]} -> 尊重客观规律与发挥主观能动性相结合
- {headings[1]} -> 矛盾就是对立统一

## Question Disposition

- Q1: excluded; theory publicity / political-culture boundary.
- Q2: inserted; official answer D, correct item ④ supports rule + subjectivity.
- Q3: excluded; culture exchange boundary.
- Q4: excluded; official answer A uses ①②, option ③ with rule language is wrong.
- Q5: inserted; official answer C, correct item ④ supports contradiction movement.
- Q6: excluded; official answer B is logic/thinking, option ② is wrong.
- Q7: excluded; law/procuratorate public-interest litigation.
- Q8: excluded; elderly-care governance / politics boundary.
- Q9: excluded; CPPCC / regional coordination politics boundary.
- Q10: missing row added and excluded; law boundary.
- Q11: missing row added and excluded; legal/business form boundary.
- Q12: excluded; economics / market access boundary.
- Q13: missing row added and excluded; economic regulation / data governance boundary.
- Q14: excluded; international economic governance boundary.
- Q15: excluded; international relations / public diplomacy boundary.
- Q16: covered by existing DOCX; formal rubric is angle-level support only, not point-by-point scoring rule.
- Q17: excluded; politics and rule-of-law boundary.
- Q18: excluded; law / contract boundary.
- Q19: excluded; politics and governance boundary.
- Q20: excluded; economics + CPPCC, with source warning not to mix modules.
- Q21: missing row added and excluded; logic + international trade boundary.
- Q22: covered by existing DOCX; formal system-view scoring points recited.
- Qunknown: closed as extraction residue.

## Matrix/Artifact Updates

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` updated for all existing 2025海淀一模 rows plus four missing boundary rows.
- `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl` now include Q2 and Q5.
- Sonnet/Haiku/model-unknown evidence was not used for this Codex production decision.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp, headings)
    update_matrix(timestamp, headings)
    write_report(timestamp, headings)
    print(f"Batch10 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
