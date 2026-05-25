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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH07_2024_FENGTAI_YIMO_CODEX_20260525.md"
SUITE = "2024丰台一模"

QUESTION_8 = (
    "30多年前，《福州市20年经济社会发展战略设想》系统谋划了福州3年、8年、20年经济社会发展的目标、步骤、布局、重点等，"
    "明确了“建设现代化国际城市”的宏伟目标，为福州擘画了美好蓝图。从“后排就座”到奋勇争先，从“纸褚福州城”到宜居幸福城……"
    "该战略工程的实施，让福州大地迎来沧桑巨变。该战略：①坚持准确识变、主动求变，以量的渐进性突破质的连续性；"
    "②放眼长远规划，以福州美好蓝图作为实现巨变的根本动力；③立足福州实际，深刻认识并准确把握了福州的特点和优势；"
    "④坚持统筹全局、系统谋划，为福州高质量发展做好顶层设计。A.①② B.①④ C.②③ D.③④。官方答案：D。"
)

ENTRIES = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q8",
        "heading_suffix": "2024丰台一模 第8题（选择题）",
        "material_trigger": "《福州市20年经济社会发展战略设想》从福州实际出发，系统谋划目标、步骤、布局、重点；正确项③明确“立足福州实际，深刻认识并准确把握了福州的特点和优势”。",
        "question_prompt": QUESTION_8,
        "why_trigger": "看到“立足福州实际”“特点和优势”，应先落到一切从实际出发、实事求是和主观与客观具体的历史的统一。题目不是让学生背规划口号，而是要求判断蓝图能否成为现实，关键在于规划是否尊重当地客观实际。",
        "answer_landing": "本题应选D。本节点处理③：战略设想能够推动福州变化，不是因为蓝图本身是根本动力，而是因为规划以福州实际为依据，正确把握本地特点和优势，把主观规划建立在客观条件之上。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2024丰台一模.md:221-235;422-458",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q8",
        "heading_suffix": "2024丰台一模 第8题（选择题）",
        "material_trigger": "题干写明战略设想系统谋划福州3年、8年、20年发展的目标、步骤、布局、重点；正确项④明确“坚持统筹全局、系统谋划，为福州高质量发展做好顶层设计”。",
        "question_prompt": QUESTION_8,
        "why_trigger": "看到“3年、8年、20年”“目标、步骤、布局、重点”“统筹全局、系统谋划”，应落到系统观念和系统优化。材料强调的不是单点政策，而是把阶段目标、空间布局、发展重点放进整体方案中优化组合。",
        "answer_landing": "本题应选D。本节点处理④：系统观念要求立足整体、统筹全局，用综合思维认识和处理问题。福州战略设想通过顶层设计把时间阶段、发展目标和重点布局组织成整体方案，为高质量发展提供系统性安排。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2024丰台一模.md:221-235;422-458",
    },
]

SECTION_NEXT = {
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2024_fengtai_yimo_batch07_{timestamp}.docx")
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch07_fengtai_yimo_{timestamp}{LEDGER.suffix}")
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
    for entry, heading in zip(ENTRIES, headings):
        key = (entry["canonical_node"], SUITE, entry["question_no"])
        if key not in seen:
            rows.append(desired[key])
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
        "batch": "batch07_2024_fengtai_yimo",
    }


def update_accepted(timestamp: str, headings: list[str]) -> None:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch07_fengtai_yimo_{timestamp}{ACCEPTED.suffix}")
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
    for entry, heading in zip(ENTRIES, headings):
        key = (SUITE, entry["question_no"], entry["canonical_node"])
        if key not in seen:
            records.append(accepted_record(entry, heading))
            seen.add(key)
    ACCEPTED.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n", encoding="utf-8")


def patch_row(row: dict[str, str], **values: str) -> None:
    for key, value in values.items():
        row[KEYS[key]] = value


def row_values(row_id: str, q: str, type_: str, in_body: str, node: str, principle: str, evidence: str, misplaced: str, needs: str, action: str, note: str, artifact: str) -> dict[str, str]:
    return {
        KEYS["id"]: row_id,
        "row_source": "batch07_2024_fengtai_yimo_recovery",
        KEYS["source"]: SUITE,
        KEYS["year"]: "2024",
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
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch07_2024_fengtai_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    by_id = {r[KEYS["id"]]: r for r in rows}
    common_artifact = "01_source_inventory/suite_source_bundles/2024丰台一模.md"
    decisions = {
        "M0139": dict(
            in_body="否：政治与法治边界题",
            node="不进入必修四哲学宝典",
            principle="16题细则明确调用《政治与法治》；评分点为党的领导、群众路线、治理机制，不属于当前哲学正文。",
            evidence="正式细则-模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_CONFIRMED_BATCH07",
            note="Q16保留为政治模块排除，不新增哲学正文。",
            artifact=f"{common_artifact}:14-28;292-314",
        ),
        "M0140": dict(
            in_body="是：已由当前DOCX覆盖",
            node="系统观念 / 系统优化；发展的观点 / 发展的普遍性；社会发展规律相关节点",
            principle="18(1)细则只给联系、发展、矛盾、唯物史观等作答角度并按等级赋分，当前DOCX已有3处第18题第（1）问条目。",
            evidence="正式细则-角度提示+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="不把角度提示冒充逐点细则；仅标为已覆盖且证据为等级评分角度。",
            artifact=f"{common_artifact}:38-49;337-346;476-494",
        ),
        "M0141": dict(
            in_body="是：已由当前DOCX覆盖",
            node="矛盾的普遍性和特殊性；价值判断与价值选择",
            principle="21题参考答案提示可从唯物辩证法、构建人类命运共同体等角度作答，等级赋分；当前DOCX已有2处第21题条目。",
            evidence="正式答案/评分参考-角度提示+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="非逐点细则，证据等级不升格为强细则。",
            artifact=f"{common_artifact}:515-536",
        ),
        "M0191": dict(
            in_body="是：已由当前DOCX覆盖",
            node="联系/发展/矛盾/唯物史观相关节点",
            principle="18(1)仅为等级赋分角度提示，已由现有正文3处覆盖。",
            evidence="正式细则-角度提示+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="关闭证据等级不足挂起项，但保留证据降级说明。",
            artifact=f"{common_artifact}:38-49;476-494",
        ),
        "M0192": dict(
            in_body="是：已由当前DOCX覆盖",
            node="唯物辩证法相关节点；价值判断与价值选择",
            principle="21题为等级赋分角度提示，已由现有正文2处覆盖。",
            evidence="正式答案/评分参考-角度提示+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="关闭参考答案证据挂起项，不升格为逐点细则。",
            artifact=f"{common_artifact}:515-536",
        ),
        "M0198": dict(
            in_body="是：已由当前DOCX覆盖",
            node="联系/发展/矛盾/唯物史观；唯物辩证法相关节点",
            principle="母版覆盖核定：18(1)与21均已有现有正文；证据均为角度提示/等级赋分。",
            evidence="现有DOCX正文覆盖+正式细则/答案角度提示",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="不新增重复主观题条目。",
            artifact=f"{common_artifact}:38-49;515-536",
        ),
        "M0251": dict(
            in_body="否：文化/中特边界题",
            node="不进入必修四哲学宝典",
            principle="Q1官方答案B，题干围绕革命文物和长征历史文化价值，属于文化/中特表达，不作为哲学原理落点。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="原候选文本存在抽取漂移，已按源卷Q1重新裁决。",
            artifact=f"{common_artifact}:160-174;422-458",
        ),
        "M0252": dict(
            in_body="否：文化边界题",
            node="不进入必修四哲学宝典",
            principle="Q2官方答案D，题干为龙凤传统纹样文化表达与创意转化，当前必修四哲学宝典不补文化线。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="文化专题另线处理。",
            artifact=f"{common_artifact}:175-184;422-458",
        ),
        "M0253": dict(
            in_body="否：政治与法治边界题",
            node="不进入必修四哲学宝典",
            principle="Q3官方答案D，题干为基层/地方政府服务与政务协同，非哲学正文落点。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="按政治模块排除。",
            artifact=f"{common_artifact}:185-189;422-458",
        ),
        "M0254": dict(
            in_body="否：政治与法治边界题",
            node="不进入必修四哲学宝典",
            principle="Q4官方答案C，题干为海洋环境保护法修订、科学立法与生态文明建设，不作为哲学正文。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="法律/政治边界排除。",
            artifact=f"{common_artifact}:190-199;422-458",
        ),
        "M0255": dict(
            in_body="否：法律与生活边界题",
            node="不进入必修四哲学宝典",
            principle="Q6官方答案B，题干为自动扶梯侵权责任和监护责任，属于法律与生活。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="M0255原为Q6；Q5另补独立边界行。",
            artifact=f"{common_artifact}:207-214;422-458",
        ),
        "M0256": dict(
            in_body="是：本批新增进入当前DOCX/PDF正文",
            node="一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一；系统观念 / 系统优化",
            principle="Q8正确项③落到立足福州实际、把握特点优势；正确项④落到统筹全局、系统谋划和顶层设计。",
            evidence="选择题官方答案键+题干正确项链条",
            misplaced="否",
            needs="否",
            action="INSERTED_BATCH07_2024_FENGTAI_Q8_TWO_NODES",
            note="新增条目：" + "；".join(headings),
            artifact=f"{common_artifact}:221-235;422-458",
        ),
        "M0257": dict(
            in_body="是：已由当前DOCX覆盖",
            node="真理观/获得真理性认识受主客观条件制约",
            principle="Q9官方答案C，当前DOCX已有“2024丰台一模 第9题（选择题）”条目。",
            evidence="官方答案键+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="漫画图像未在本批新增；保留为后续版式/图像完整性检查提示。",
            artifact=f"{common_artifact}:236-240;422-458",
        ),
        "M0258": dict(
            in_body="否：选必三逻辑与思维边界题",
            node="不进入必修四哲学宝典",
            principle="Q10官方答案A，考查抽象思维与形象思维互补，属于逻辑与思维。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="不纳入哲学宝典正文。",
            artifact=f"{common_artifact}:241-247;422-458",
        ),
        "M0259": dict(
            in_body="否：选必三逻辑与思维边界题",
            node="不进入必修四哲学宝典",
            principle="Q11官方答案D，考查推理/条件关系判断，属于逻辑与思维。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="不纳入必修四哲学正文。",
            artifact=f"{common_artifact}:248-255;422-458",
        ),
        "M0260": dict(
            in_body="否：经济与社会边界题",
            node="不进入必修四哲学宝典",
            principle="Q12官方答案A，考查民营经济政策与经营发展。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="经济模块排除。",
            artifact=f"{common_artifact}:256-262;422-458",
        ),
        "M0261": dict(
            in_body="否：经济与社会/社会保障边界题",
            node="不进入必修四哲学宝典",
            principle="Q13官方答案B，考查京津冀一卡通、公共服务和民生服务。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="公共服务/经济社会边界排除。",
            artifact=f"{common_artifact}:263-275;422-458",
        ),
        "M0262": dict(
            in_body="否：经济与国际贸易边界题",
            node="不进入必修四哲学宝典",
            principle="Q14官方答案B，考查中间品贸易传导路径。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="国际贸易/经济模块排除。",
            artifact=f"{common_artifact}:276-282;422-458",
        ),
        "M0263": dict(
            in_body="否：当代国际政治与经济边界题",
            node="不进入必修四哲学宝典",
            principle="Q15官方答案A，题干为元首外交和中国外交气度。",
            evidence="官方答案键+模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="选必一/国际政治经济边界排除。",
            artifact=f"{common_artifact}:283-291;422-458",
        ),
        "M0264": dict(
            in_body="否：政治与法治边界题",
            node="不进入必修四哲学宝典",
            principle="Q16细则明确调用《政治与法治》，评分点为党的领导、群众路线、治理机制。",
            evidence="正式细则-模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="与M0139闭合一致。",
            artifact=f"{common_artifact}:14-28;292-314",
        ),
        "M0265": dict(
            in_body="否：法律与生活边界题",
            node="不进入必修四哲学宝典",
            principle="Q17细则明确调用《法律与生活》，考查好意同乘、侵权责任和赔偿减轻。",
            evidence="正式细则-模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="法律模块排除。",
            artifact=f"{common_artifact}:29-37;315-334;470-475",
        ),
        "M0266": dict(
            in_body="是：已由当前DOCX覆盖",
            node="联系/发展/矛盾/唯物史观相关节点",
            principle="Q18(1)细则为角度提示和等级赋分；Q18(2)为经济与社会。当前DOCX已覆盖Q18(1)三处。",
            evidence="正式细则-角度提示+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="不重复新增；Q18(2)按经济模块排除。",
            artifact=f"{common_artifact}:38-70;337-346;476-503",
        ),
        "M0267": dict(
            in_body="否：选必三逻辑与思维边界题",
            node="不进入必修四哲学宝典",
            principle="Q19细则为头脑风暴法、问卷调查法、访谈法等研究方法，属于逻辑与思维/科学思维。",
            evidence="正式细则-模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="不进入当前必修四哲学宝典。",
            artifact=f"{common_artifact}:71-98;504-510",
        ),
        "M0268": dict(
            in_body="否：当代国际政治与经济边界题",
            node="不进入必修四哲学宝典",
            principle="Q20答案围绕全球供应链、基础设施、供应链金融和经济全球化。",
            evidence="正式答案-模块边界",
            misplaced="否",
            needs="否",
            action="MODULE_BOUNDARY_EXCLUDED_BATCH07",
            note="选必一/经济全球化边界排除。",
            artifact=f"{common_artifact}:99-105;511-514",
        ),
        "M0269": dict(
            in_body="是：已由当前DOCX覆盖",
            node="矛盾的普遍性和特殊性；价值判断与价值选择",
            principle="Q21可从唯物辩证法、构建人类命运共同体等角度作答，等级赋分；当前DOCX已有两处Q21条目。",
            evidence="正式答案/评分参考-角度提示+现有DOCX正文覆盖",
            misplaced="否",
            needs="否",
            action="COVERED_BY_EXISTING_DOCX_BATCH07",
            note="不新增重复条目；证据不升格为逐点细则。",
            artifact=f"{common_artifact}:515-536",
        ),
        "M0270": dict(
            in_body="否：抽取残留/经济模块边界",
            node="不进入必修四哲学宝典",
            principle="该行由Q18(2)经济逻辑材料/答案抽取残留形成，Q18(2)明确调用《经济与社会》。",
            evidence="正式细则-模块边界+抽取残留清理",
            misplaced="否",
            needs="否",
            action="EXTRACTION_RESIDUE_CLOSED_BATCH07",
            note="关闭Qunknown残留，不作为哲学题。",
            artifact=f"{common_artifact}:50-70;495-503",
        ),
        "M0780": dict(
            in_body="套卷逐题已由Batch07闭合",
            node="SUITE_LEVEL_SUMMARY",
            principle="逐题回源已闭合：Q8新增两节点，Q9/Q18/Q21现有覆盖，其余模块边界排除。",
            evidence="Batch07逐题矩阵闭合",
            misplaced="否",
            needs="否",
            action="SUITE_CLOSED_BY_BATCH07",
            note="套卷级记录不再替代逐题记录。",
            artifact=f"{common_artifact}:1-536",
        ),
        "M0819": dict(
            in_body="套卷逐题已由Batch07闭合",
            node="SUITE_LEVEL_SUMMARY",
            principle="逐题回源已闭合：Q8新增两节点，Q9/Q18/Q21现有覆盖，其余模块边界排除。",
            evidence="Batch07逐题矩阵闭合",
            misplaced="否",
            needs="否",
            action="SUITE_CLOSED_BY_BATCH07",
            note="套卷级挂起项关闭；以M0251-M0270及新增Q5/Q7边界行为准。",
            artifact=f"{common_artifact}:1-536",
        ),
    }

    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)

    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    additions = [
        row_values(
            f"M{max_id + 1:04d}",
            "Q5",
            "法律与生活边界题",
            "否：法律与生活边界题",
            "不进入必修四哲学宝典",
            "Q5官方答案D，人民法院立案窗口工作规范考查诉权保障和司法为民。",
            "官方答案键+模块边界",
            "否",
            "否",
            "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH07",
            "原矩阵缺独立Q5行，本批补充边界闭合。",
            f"{common_artifact}:200-206;422-458",
        ),
        row_values(
            f"M{max_id + 2:04d}",
            "Q7",
            "选必三逻辑与思维边界题",
            "否：选必三逻辑与思维边界题",
            "不进入必修四哲学宝典",
            "Q7官方答案C，考查概念周延/文段逻辑分析。",
            "官方答案键+模块边界",
            "否",
            "否",
            "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH07",
            "原矩阵缺独立Q7行，本批补充边界闭合。",
            f"{common_artifact}:215-220;422-458",
        ),
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
    text = f"""# Coverage Fusion Batch07 - 2024丰台一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2024丰台一模
status: CODEX_BATCH07_SOURCE_COVERAGE_APPLIED

## Source Basis

- source bundle: `01_source_inventory/suite_source_bundles/2024丰台一模.md`
- formal scoring/rubric lines checked: Q16 `14-28`, Q17 `29-37`, Q18(1) `38-49`, Q21 `515-536`
- paper/answer lines checked: Q5 `200-206`, Q7 `215-220`, Q8 `221-235`, Q9 `236-240`, Q10-Q15 `241-291`, answers `422-458`

## Inserted Into DOCX

- {headings[0]} -> 一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一
- {headings[1]} -> 系统观念 / 系统优化

Both entries are supported by the official answer key plus correct-option chain for Q8. This is not marked as formal rubric-level evidence.

## Question Disposition

- Q1: excluded, culture/中特 boundary.
- Q2: excluded, culture boundary.
- Q3: excluded, political/governance boundary.
- Q4: excluded, political/legal boundary.
- Q5: missing matrix row added; excluded, legal boundary.
- Q6: excluded, legal boundary.
- Q7: missing matrix row added; excluded, logic/thinking boundary.
- Q8: inserted into two philosophy nodes.
- Q9: already covered by existing DOCX Q9 entry; no duplicate insertion.
- Q10-Q11: excluded, logic/thinking boundary.
- Q12-Q14: excluded, economics/international trade boundary.
- Q15: excluded, international politics/economy boundary.
- Q16: excluded by formal Political and Rule of Law rubric.
- Q17: excluded by formal Law and Life rubric.
- Q18(1): already covered by existing DOCX; evidence remains formal angle prompt plus level grading, not point-by-point rubric.
- Q18(2): excluded, Economic and Social Life boundary.
- Q19: excluded, logic/scientific thinking boundary.
- Q20: excluded, international political economy boundary.
- Q21: already covered by existing DOCX; evidence remains answer/rating angle prompt, not point-by-point rubric.
- Qunknown: closed as extraction residue from Q18(2) economics.

## Controls

- Sonnet evidence not used.
- GPTPro web / external Claude Opus full-artifact review remains `real_call_pending`.
- ClaudeCode Batch07 Opus 4.7 recheck still must be called after this Codex production patch.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp, headings)
    update_matrix(timestamp, headings)
    write_report(timestamp, headings)
    print(f"Batch07 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
