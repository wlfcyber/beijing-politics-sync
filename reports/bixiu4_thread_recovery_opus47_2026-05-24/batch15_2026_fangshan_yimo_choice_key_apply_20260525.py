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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH15_2026_FANGSHAN_YIMO_CHOICE_KEY_CODEX_20260525.md"
SOURCE_TRANSCRIPTION = RECOVERY / "BATCH15_2026_FANGSHAN_YIMO_CHOICE_KEY_SOURCE_TRANSCRIPTION_20260525.md"

SUITE = "2026房山一模"
YEAR = "2026"
STAGE = "一模"

PAPER_RENDER = "preprocessed_corpus/renders/e37482eff39f3618"
ANSWER_SOURCE = "reports/overnight_2026-04-25/objective_answer_source_closure.md:10"
ANSWER_PDF = "reports/overnight_2026-04-25/downloaded_evidence/2026_fangshan_yimo_with_answers.pdf"
ANSWER_PAGE = "reports/overnight_2026-04-25/downloaded_evidence_pages/2026_fangshan_yimo_with_answers_page_09.png"
OLD_FRAMEWORK = (
    "skills/feige-politics-garden-bixiu4/assets/current-artifacts/"
    "必修四哲学材料-知识触发总框架_持续更新版_v2.md:1813-1835"
)

Q2_SOURCE = f"{PAPER_RENDER}/page_002.png; {ANSWER_SOURCE}; {ANSWER_PAGE}; {OLD_FRAMEWORK}"
Q4_SOURCE = f"{PAPER_RENDER}/page_002.png; {ANSWER_SOURCE}; {ANSWER_PAGE}; {OLD_FRAMEWORK}"
Q6_DOWNGRADE_SOURCE = f"{PAPER_RENDER}/page_003.png; {ANSWER_SOURCE}; {ANSWER_PAGE}; {OLD_FRAMEWORK}"
ANSWER_KEY = "1C 2D 3B 4A 5C 6D 7B 8A 9D 10B 11D 12C 13B 14C 15A"

Q2_PROMPT = (
    "南朝《世说新语·品藻》中的“我与我周旋久，宁作我”与今天的“爱老己”对读。"
    "官方答案D（②④）：既强调对自我价值的认可与关照，也强调人的价值只能在社会中实现，"
    "需要正确处理个人与社会的关系。"
)
Q4_PROMPT = (
    "改革开放以来我国大规模城镇化和反贫困实践得到世界承认，同时原创区域经济研究不足。"
    "官方答案A（①③）：立足当代中国具体实践推动原创理论建构，并坚持系统优化方法，统筹理论创新、"
    "实践总结与学术交流。"
)

ENTRIES = [
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q2",
        "heading_suffix": "2026房山一模 第2题（选择题）",
        "material_trigger": "官方答案D包含②④；题干把“爱老己”放在生活水平提升、个人价值确认和个人社会关系中理解。",
        "question_prompt": Q2_PROMPT,
        "why_trigger": "“爱老己”不是躺平式自我封闭，而是在社会生活中评价自我、关照自我并处理个人与社会关系，本质上要求作出正确的价值判断和价值选择。",
        "answer_landing": "本题应选D。作答落点是价值判断与价值选择要符合社会发展规律并站在正确立场上；个人关照不能脱离社会关系，个人价值要在社会中实现。",
        "evidence_level": "客观题答案表+题面正确项；非主观评分细则",
        "source_lines": Q2_SOURCE,
    },
    {
        "canonical_node": "实现人生价值",
        "question_no": "Q2",
        "heading_suffix": "2026房山一模 第2题（选择题）",
        "material_trigger": "官方答案D中的④明确“人的价值只能在社会中实现”，“爱老己”需要正确处理个人与社会的关系。",
        "question_prompt": Q2_PROMPT,
        "why_trigger": "看到“人的价值只能在社会中实现”和“个人与社会关系”，应落到人生价值在个人与社会统一中创造和实现，而不是把自我价值理解为孤立的自我感受。",
        "answer_landing": "本题应选D。作答可写：人既是价值创造者也是价值享受者，人生价值要在个人与社会统一中实现；关照自我应与承担社会责任、参与社会生活统一起来。",
        "evidence_level": "客观题答案表+正确项④；非主观评分细则",
        "source_lines": Q2_SOURCE,
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q4",
        "heading_suffix": "2026房山一模 第4题（选择题）",
        "material_trigger": "官方答案A包含①；正确项要求立足当代中国具体实践，推动原创性理论建构与自主知识体系创新。",
        "question_prompt": Q4_PROMPT,
        "why_trigger": "理论创新不是从西方既有理论中套出来，也不是抽象思辨自转，而是从中国城镇化、反贫困、区域发展等具体实践中提出问题、总结经验、建构理论。",
        "answer_landing": "本题应选A。作答落点是实践是认识的来源和发展动力；中国实践为原创理论建构提供现实基础，理论创新必须立足中国具体实践。",
        "evidence_level": "客观题答案表+正确项①；非主观评分细则",
        "source_lines": Q4_SOURCE,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q4",
        "heading_suffix": "2026房山一模 第4题（选择题）",
        "material_trigger": "官方答案A包含③；正确项明确“坚持系统优化方法，统筹理论创新、实践总结与学术交流的协同关系”。",
        "question_prompt": Q4_PROMPT,
        "why_trigger": "构建中国哲学社会科学自主知识体系不能只抓单一环节，而要把理论创新、实践总结、学术交流放入同一系统中协同推进。",
        "answer_landing": "本题应选A。作答可写：坚持系统优化方法，统筹理论、实践和交流等要素，促进各部分协同发力，推动自主知识体系创新。",
        "evidence_level": "客观题答案表+正确项③；非主观评分细则",
        "source_lines": Q4_SOURCE,
    },
]

SECTION_NEXT = {
    "实践是认识的基础": "认识对实践的反作用",
    "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
    "价值判断与价值选择": "实现人生价值",
    "实现人生价值": "__END__",
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
    if next_heading == "__END__":
        return start, len(paras)
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
    ref = paras[end] if end < len(paras) else body[-1]
    insert_at = body.index(ref) if end < len(paras) else len(body) - 1
    for p in template:
        body.insert(insert_at, p)
        insert_at += 1
    return heading


def update_docx(timestamp: str) -> list[str]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_fangshan_yimo_choice_batch15_{timestamp}.docx")
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
        "source_lane": "Codex Batch15 recovery production",
        "source_repair_basis": entry["source_lines"],
        "source_lines": entry["source_lines"],
        "batch": "batch15_2026_fangshan_yimo_choice_key",
    }


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch15_fangshan_choice_{timestamp}{LEDGER.suffix}")
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
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch15_fangshan_choice_{timestamp}{ACCEPTED.suffix}")
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


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch15_2026_fangshan_choice_key_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}
    h = dict(zip([(e["question_no"], e["canonical_node"]) for e in ENTRIES], headings))
    q2_note = (
        "答案键补证后转正："
        f"{h[('Q2', '价值判断与价值选择')]}；"
        f"{h[('Q2', '实现人生价值')]}。"
    )
    q4_note = (
        "答案键补证后转正："
        f"{h[('Q4', '实践是认识的基础')]}；"
        f"{h[('Q4', '系统观念 / 系统优化')]}。"
    )
    decisions = {
        "M0880": dict(
            type="文化/精神谱系选择题",
            in_body="否：纯文化精神谱系题，不进入当前哲学宝典正文",
            node="不进入当前哲学宝典正文；可作为未来文化触发表素材",
            principle="Q1官方答案C：伟大建党精神为源头的精神谱系是中国人民百年奋斗的精神密码并提供滋养；属于文化/精神谱系判断，不构成当前哲学正文落点。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="答案键已补证，撤销NEED_ANSWER_KEY；不把文化精神谱系强塞进哲学节点。",
            artifact=f"{PAPER_RENDER}/page_001.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0881": dict(
            type="文化/价值选择题",
            in_body="是：本批新增进入当前DOCX/PDF正文并登记ledger/accepted",
            node="价值判断与价值选择 / 实现人生价值",
            principle="Q2官方答案D（②④）：②强调对自我价值的认可与关照，④明确人的价值只能在社会中实现，“爱老己”需要正确处理个人与社会的关系。",
            evidence="客观答案表+题面正确项；非主观评分细则",
            misplaced="否",
            needs="否",
            action="INSERTED_AND_REGISTERED_BATCH15_FANGSHAN_Q2",
            note=q2_note,
            artifact=Q2_SOURCE,
        ),
        "M0882": dict(
            type="文化传承选择题",
            in_body="否：纯文化传承题，不进入当前哲学宝典正文",
            node="不进入当前哲学宝典正文；可作为未来文化触发表素材",
            principle="Q3官方答案B（①③）：年轻人积极共创成为传承古韵国风的重要主体，中华文明具有连续性和生命力；属于文化传承与文明延续，不作当前哲学节点新增。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="答案键已补证，撤销NEED_ANSWER_KEY；纯文化项按既有规则不并入哲学主表。",
            artifact=f"{PAPER_RENDER}/page_002.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0883": dict(
            type="马克思主义理论/哲学选择题",
            in_body="是：本批新增进入当前DOCX/PDF正文并登记ledger/accepted",
            node="实践是认识的基础 / 系统观念 / 系统优化",
            principle="Q4官方答案A（①③）：①要求立足当代中国具体实践推动原创性理论建构与自主知识体系创新；③要求坚持系统优化方法，统筹理论创新、实践总结与学术交流的协同关系。",
            evidence="客观答案表+题面正确项；非主观评分细则",
            misplaced="否",
            needs="否",
            action="INSERTED_AND_REGISTERED_BATCH15_FANGSHAN_Q4",
            note=q4_note,
            artifact=Q4_SOURCE,
        ),
        "M0884": dict(
            type="逻辑推理/一国两制选择题",
            in_body="否：选必三逻辑与思维边界题",
            node="不进入当前哲学宝典正文",
            principle="Q5官方答案C：围绕十五运会与“一国两制”制度优势作逻辑真假判断，核心落点为逻辑推理/选必三边界。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="不把制度优势材料转入哲学正文。",
            artifact=f"{PAPER_RENDER}/page_003.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0885": dict(
            type="逻辑与科学思维选择题",
            in_body="否：选必三超前思维边界题；旧回填候选已降级",
            node="不进入当前哲学宝典正文",
            principle="Q6官方答案D：正确项为“运用超前思维，基于现有的实验成果预测未来发展趋势”。旧v2框架曾把该题列为必修四候选，但逐题核对后，正确项核心为选必三超前思维；材料中的实验认识论只作近邻素材，不作为正文落点。",
            evidence="客观答案表+正确项D+旧框架复核降级",
            misplaced="否",
            needs="否",
            action="OLD_BACKFILL_DOWNGRADED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="撤销NEED_ANSWER_KEY；不继承旧“Q6已回填”结论作为当前合格正文证据。",
            artifact=Q6_DOWNGRADE_SOURCE,
        ),
        "M0886": dict(
            type="逻辑/创新思维选择题",
            in_body="否：选必三逻辑与创新思维边界题",
            node="不进入当前哲学宝典正文",
            principle="Q7官方答案B（①④）：节目创意、思维能动性、矛盾律与科技创新表述主要落在逻辑与思维/创新思维；实践字样不足以支撑当前哲学正文新增。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="不把选必三思维术语近邻强行迁入必修四正文。",
            artifact=f"{PAPER_RENDER}/page_003.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0887": dict(
            type="政治与法治/党员干部选择题",
            in_body="否：政治与法治边界题",
            node="不进入当前哲学宝典正文",
            principle="Q8官方答案A：强调党员干部践行根本宗旨、把为民造福作为最大政绩，属于政治与法治/党的宗旨与干部作风。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="红色传统材料不自动转为价值观正文条目。",
            artifact=f"{PAPER_RENDER}/page_004.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0888": dict(
            type="政治与法治/人大执法检查选择题",
            in_body="否：政治与法治边界题",
            node="不进入当前哲学宝典正文",
            principle="Q9官方答案D（③④）：人大常委会执法检查发挥制度优势并依法行使监督权，属于政治与法治。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="不把制度优势或全域检查转写为系统观念。",
            artifact=f"{PAPER_RENDER}/page_004.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0889": dict(
            type="法律与生活/人格权选择题",
            in_body="否：法律与生活边界题",
            node="不进入当前哲学宝典正文",
            principle="Q10官方答案B（①③）：依法保护人格权、要求删除画面停止传播并赔礼道歉，属于法律与生活。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="不把科技向善等错误项或近邻价值词转入正文。",
            artifact=f"{PAPER_RENDER}/page_004.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0890": dict(
            type="法律与生活/债务清偿选择题",
            in_body="否：法律与生活边界题",
            node="不进入当前哲学宝典正文",
            principle="Q11官方答案D：法院创新司法实践、平衡债权人和债务人利益关系，属于法律与生活/司法制度。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="利益平衡不等同于哲学矛盾正文落点。",
            artifact=f"{PAPER_RENDER}/page_005.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0891": dict(
            type="政治与法治/社会救助立法选择题",
            in_body="否：政治与法治/社会保障边界题",
            node="不进入当前哲学宝典正文",
            principle="Q12官方答案C（②③）：社会救助法立法、社会领域法治建设、共享发展成果和维护公平，属于政治法治/社会保障。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="共享发展与公平是模块边界内材料，不新增价值观正文。",
            artifact=f"{PAPER_RENDER}/page_005.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0892": dict(
            type="经济与社会/国企新质生产力选择题",
            in_body="否：经济与社会边界题",
            node="不进入当前哲学宝典正文",
            principle="Q13官方答案B：立足实体经济，推动科技创新和产业创新深度融合，属于经济与社会/新质生产力。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="不把科技创新经济题转成哲学实践条目。",
            artifact=f"{PAPER_RENDER}/page_005.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0893": dict(
            type="经济与社会/创新创业选择题",
            in_body="否：经济与社会边界题",
            node="不进入当前哲学宝典正文",
            principle="Q14官方答案C：提供个体创业政策供给，激发微观主体创新活力，发展数字经济，属于经济与社会/创新创业。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="OPC创新创业不进入当前哲学正文。",
            artifact=f"{PAPER_RENDER}/page_006.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
        "M0894": dict(
            type="当代国际政治与经济/全球治理选择题",
            in_body="否：当代国际政治与经济边界题",
            node="不进入当前哲学宝典正文",
            principle="Q15官方答案A：全球治理倡议有利于推进国际关系民主化、提升发展中国家发言权，属于当代国际政治与经济。",
            evidence="客观答案表+题面正确项+模块边界",
            misplaced="否",
            needs="否",
            action="ANSWER_KEY_CLOSED_MODULE_BOUNDARY_EXCLUDED_BATCH15",
            note="不把全球治理倡议转入哲学正文。",
            artifact=f"{PAPER_RENDER}/page_006.png; {ANSWER_SOURCE}; {ANSWER_PAGE}",
        ),
    }
    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_source_transcription(timestamp: str) -> None:
    text = f"""# Batch15 Source Transcription - 2026房山一模 Choice Key

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026房山一模
status: SOURCE_PACKET_COMPLETE_FOR_BATCH15_CHOICE_KEY

## Source Files Checked

- paper render pages: `{PAPER_RENDER}/page_001.png` to `{PAPER_RENDER}/page_006.png`
- objective answer closure: `{ANSWER_SOURCE}`
- saved answer PDF: `{ANSWER_PDF}`
- rendered answer page: `{ANSWER_PAGE}`
- prior v2 framework candidate line: `{OLD_FRAMEWORK}`

## Objective Answer Key

`{ANSWER_KEY}`

The answer table is visible on `{ANSWER_PAGE}` and is also recorded in `{ANSWER_SOURCE}`. It is used only for objective-choice placement and module-boundary decisions. It is not used as a replacement for subjective marking rules.

## Placement Decisions

- Q2 answer D enters the current philosophy DOCX under `价值判断与价值选择` and `实现人生价值`.
- Q4 answer A enters the current philosophy DOCX under `实践是认识的基础` and `系统观念 / 系统优化`.
- Q6 answer D is downgraded from the old v2 candidate status because the official correct option is `超前思维`, a Logic and Thinking boundary. The material may be a near-neighbor for认识论, but the answer landing is not a current philosophy-body point.
- Q1, Q3, Q5, Q7-Q15 are closed by answer key and module boundary; none are inserted into the current philosophy body.

## Evidence Boundary

Choice-question evidence level is recorded as `客观题答案表+题面正确项；非主观评分细则` for inserted rows. It is deliberately not labeled as subjective scoring-rubric evidence.
"""
    SOURCE_TRANSCRIPTION.write_text(text, encoding="utf-8")


def write_report(timestamp: str, headings: list[str]) -> None:
    inserted = "\n".join(f"- {heading}" for heading in headings)
    text = f"""# Coverage Fusion Batch15 - 2026房山一模 Choice Key

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026房山一模
status: CODEX_BATCH15_CHOICE_KEY_COVERAGE_APPLIED

## Applied To DOCX / Ledger / Accepted

{inserted}

## Matrix Disposition

- M0880-M0894 are no longer `NEED_ANSWER_KEY_BATCH12`.
- Q2 and Q4 are inserted and registered in current DOCX, `docx_insert_ledger.csv`, and `student_patch_entries.accepted.jsonl`.
- Q6 is explicitly downgraded from old v2 “已回填” candidate status because the official correct option D is `超前思维`, not a current 必修四哲学 answer landing.
- Q1, Q3, Q5, Q7-Q15 are closed as module boundaries and do not require more thickness in the current philosophy body.

## Evidence Boundary

No Sonnet/Haiku/model-unknown output was used. The answer PDF and closure ledger are used only as objective-choice evidence. Subjective principles remain governed by local marking rules and rubric files.
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
    print("timestamp", timestamp)
    print("headings")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
