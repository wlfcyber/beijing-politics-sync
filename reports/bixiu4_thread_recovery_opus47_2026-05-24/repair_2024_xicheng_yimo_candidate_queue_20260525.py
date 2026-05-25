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
REPORT_MD = RECOVERY / "XICHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "XICHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2024西城一模"
YEAR = "2024"
STAGE = "一模"
ROW_SOURCE = "codex_recovery_20260525_xicheng_2024_yimo_repair"
BUNDLE = "data\\preprocessed_corpus\\gpt_suite_bundles\\2024各区模拟题__2024各区一模__2024西城一模.md"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q2",
        "heading_suffix": "2024西城一模 第2题（选择题）",
        "material_trigger": "科技小院把农业专业学生的理论学习、农业专家和田间地头连接起来，学生在真实生产中研究解决农业农村实际问题；官方答案键为A，正确项②写明“走进乡土中国深处，才能深刻理解怎样实事求是、联系群众”。",
        "question_prompt": "科技小院中学生在生产实践中解决农业农村实际问题；正确组合为A（①②）。",
        "why_trigger": "看到“完成知识、理论学习”以后还要进入田间地头解决实际问题，并且正确项直接写出“实事求是”，应想到一切从实际出发、主观与客观具体的历史的统一：认识农业农村不能停在书本和抽象理论上，要回到乡土实际和生产实践中检验、理解和运用。",
        "answer_landing": "本题应选A。本节点只处理②：走进乡土中国深处，才能在真实生产生活条件中理解怎样实事求是、联系群众，说明想问题、办事情要从客观实际出发，使理论认识同具体实践相结合。①的产业发展和农民致富作为经济线索保留，不扩展成主观题评分链。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
    },
    {
        "canonical_node": "矛盾的普遍性",
        "question_no": "Q9",
        "heading_suffix": "2024西城一模 第9题（选择题）",
        "material_trigger": "青藏高原高寒、干旱等极端环境却生长更多千年古树；研究推测树木经过逆境长期适应，采用慢速生长策略，减少资源消耗，维持生命韧性；官方答案键为D。",
        "question_prompt": "青藏高原千年古树在逆境中维持生命韧性，以下分析正确的是D：无处不在的矛盾，能引发对生命意义、生命潜能的反思。",
        "why_trigger": "材料强调逆境与适应、慢速生长与生命韧性、资源消耗与持久生存之间的对立统一；正确项D直接落在“无处不在的矛盾”。原正文把本题放在“主观能动性”下，容易被误读为支持错误项B“树木具备主观能动性”，因此本次移到“矛盾的普遍性”。",
        "answer_landing": "本题应选D。世界上的一切事物都包含矛盾，矛盾具有普遍性；逆境与生命韧性、资源消耗与长期生存之间的矛盾关系，引发人们对生命意义和生命潜能的反思。A把理性认识都说成真理性认识，B把主观能动性错误用于树木，C把矛盾转化结果绝对化，均不作为正文链条。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
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


def is_section(p) -> bool:
    return p_style(p) in {"Heading2", "2", "4"}


def is_entry(p) -> bool:
    return p_style(p) in {"Heading3", "3", "5"}


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


def set_plain(p, text: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(text))


def set_label(p, label: str, rest: str) -> None:
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
    start = next((i for i, p in enumerate(paras) if is_section(p) and para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if is_section(paras[i])), len(paras))
    return start, end


def templates(paras, start: int, end: int):
    heading_template = next((paras[i] for i in range(start + 1, end) if is_entry(paras[i])), None)
    label_template = next((paras[i] for i in range(start + 1, end) if para_text(paras[i]).strip().startswith("【")), None)
    blank_template = next((paras[i] for i in range(start + 1, end) if not para_text(paras[i]).strip()), None)
    if heading_template is None or label_template is None:
        raise RuntimeError(f"templates not found in {para_text(paras[start])}")
    return heading_template, label_template, blank_template


def next_num(paras, start: int, end: int) -> int:
    nums = []
    for i in range(start + 1, end):
        if is_entry(paras[i]):
            head = para_text(paras[i]).strip().split(".", 1)[0]
            if head.isdigit():
                nums.append(int(head))
    return (max(nums) if nums else 0) + 1


def remove_existing_q9(body) -> int:
    paras = [p for p in body if p.tag == W + "p"]
    target = f"{SUITE} 第9题"
    for i, p in enumerate(paras):
        if target in para_text(p):
            end = i + 1
            while end < len(paras) and not is_entry(paras[end]) and not is_section(paras[end]):
                end += 1
            for victim in paras[i:end]:
                body.remove(victim)
            return end - i
    return 0


def add_entry(body, entry: dict[str, str]) -> str | None:
    if any(entry["heading_suffix"] in para_text(p) for p in body if p.tag == W + "p"):
        return None
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    heading_template, label_template, blank_template = templates(paras, start, end)
    heading_text = f"{next_num(paras, start, end)}. {entry['heading_suffix']}"
    insert_at = list(body).index(paras[end]) if end < len(paras) else len(body)
    h = deepcopy(heading_template)
    set_plain(h, heading_text)
    body.insert(insert_at, h)
    insert_at += 1
    for label, key in LABELS:
        p = deepcopy(label_template)
        set_label(p, label, entry[key])
        body.insert(insert_at, p)
        insert_at += 1
    if blank_template is not None:
        body.insert(insert_at, deepcopy(blank_template))
    return heading_text


def edit_docx(ts: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2024_xicheng_yimo_repair_{ts}.docx")
    shutil.copy2(docx, backup)
    inserted: list[str] = []
    skipped: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        xml_path = temp / "word" / "document.xml"
        tree = etree.parse(str(xml_path))
        body = tree.getroot().find("w:body", namespaces=NS)
        if body is None:
            raise RuntimeError("missing body")
        removed = remove_existing_q9(body)
        for entry in INSERT_ENTRIES:
            heading = add_entry(body, entry)
            if heading is None:
                skipped.append(entry["heading_suffix"])
            else:
                inserted.append(heading)
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "removed_q9_paragraphs": removed, "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, inserted_headings: list[str]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2024_xicheng_yimo_repair_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for entry, heading in zip(INSERT_ENTRIES, inserted_headings, strict=False):
        clean = heading.split(". ", 1)[1]
        key = (SUITE, entry["question_no"], clean)
        if key not in existing:
            rows.append(
                {
                    "canonical_node": entry["canonical_node"],
                    "source_suite": SUITE,
                    "question_no": entry["question_no"],
                    "inserted_heading": clean,
                }
            )
            added.append(clean)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger_backup": str(backup) if backup else None, "ledger_rows_added": added}


def source(lines: str) -> str:
    return f"{BUNDLE}:{lines}"


def set_decision(row: dict[str, str], h: dict[str, str], *, question: str, qtype: str, in_book: str, node: str, support: str, evidence: str, current: str, note: str, artifact: str) -> None:
    row[h["question"]] = question
    row[h["qtype"]] = qtype
    row[h["in_book"]] = in_book
    row[h["node"]] = node
    row[h["support"]] = support
    row[h["evidence"]] = evidence
    row[h["misplaced"]] = "否"
    row[h["need"]] = "否"
    row[h["current"]] = current
    row[h["note"]] = note
    row[h["artifact"]] = artifact


def append_row(rows: list[dict[str, str]], fieldnames: list[str], h: dict[str, str], next_id: int, *, question: str, qtype: str, in_book: str, node: str, support: str, evidence: str, current: str, note: str, artifact: str) -> int:
    row = {name: "" for name in fieldnames}
    row[fieldnames[0]] = f"M{next_id:04d}"
    row[fieldnames[1]] = ROW_SOURCE
    row[fieldnames[2]] = SUITE
    row[fieldnames[3]] = YEAR
    row[fieldnames[4]] = STAGE
    set_decision(row, h, question=question, qtype=qtype, in_book=in_book, node=node, support=support, evidence=evidence, current=current, note=note, artifact=artifact)
    rows.append(row)
    return next_id + 1


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2024_xicheng_yimo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    h = {
        "id": fieldnames[0],
        "source": fieldnames[2],
        "question": fieldnames[5],
        "qtype": fieldnames[6],
        "in_book": fieldnames[7],
        "node": fieldnames[8],
        "support": fieldnames[9],
        "evidence": fieldnames[10],
        "misplaced": fieldnames[11],
        "need": fieldnames[12],
        "current": fieldnames[13],
        "note": fieldnames[14],
        "artifact": fieldnames[15],
    }
    by_id = {r.get(h["id"], ""): r for r in rows}
    updated: list[str] = []

    def upd(rid: str, **kwargs) -> None:
        set_decision(by_id[rid], h, **kwargs)
        updated.append(rid)

    choice_ev = "官方答案键+题干正确项链条（选择题，非主观题评分细则）"
    boundary_ev = "官方答案键/题干模块边界"
    formal_ev = "正式评分细则"

    upd("M0145", question="Q7", qtype="法律与生活边界题", in_book="否：选必二法律与生活边界", node="NO_DOCX_ACTION", support="Q7围绕生鲜灯、诚信经营、消费者维权和自主选择权；官方答案键A，属于法律与生活消费者权益链条。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="旧待核行关闭；不是Q17哲学题，不进入必修四正文。", artifact=source("201-230"))
    upd("M0196", question="Q17", qtype="哲学主观题旧候选", in_book="是：已进入当前DOCX/PDF正文", node="Q17多节点已由当前DOCX覆盖", support="正式细则列出生态价值观、实践与认识、客观规律与主观能动性、联系与发展、对立统一、否定之否定等角度。", evidence=formal_ev, current="SUPERSEDED_BY_Q17_ROW_REVIEW", note="旧候选行保留为历史线索，具体正文覆盖以Q17行和当前DOCX为准。", artifact=source("82-110"))
    upd("M0202", question="Q17", qtype="哲学主观题旧候选", in_book="是：已进入当前DOCX/PDF正文", node="Q17多节点已由当前DOCX覆盖", support="当前DOCX已有Q17在规律与能动性、系统观念、发展、矛盾、实践、价值观等节点的正文条目。", evidence=formal_ev, current="SUPERSEDED_BY_Q17_ROW_REVIEW", note="旧候选行关闭，避免重复插入。", artifact=source("82-110"))
    upd("M0321", question="Q1", qtype="选择题边界排除", in_book="否：正确项不落必修四正文", node="NO_DOCX_ACTION", support="官方答案键C，对应②③；①虽有马克思主义基本原理/时代实践字样但不是正确项，不得作为选择题正文链条。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="错误项或非正确项不得入宝典。", artifact=source("201-220"))
    upd("M0322", question="Q2", qtype="选择题正确项链条", in_book="是：已进入当前DOCX/PDF正文", node="一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一", support="官方答案键A，正确项②写明走进乡土中国深处才能深刻理解怎样实事求是、联系群众。", evidence=choice_ev, current="DOCX_INSERTED_CHOICE_CHAIN_RENDER_PENDING", note="只处理②的实事求是链条；①经济线索不扩展为主观题评分链。", artifact=source("201-230"))
    upd("M0323", question="Q4", qtype="选择题边界排除", in_book="否：文化/基层治理弱链条，不进当前正文", node="NO_DOCX_ACTION", support="官方答案键B，侧重融洽邻里关系、弘扬文明风尚、助力农村基层群众自治；不是稳定的必修四哲学/文化原理落点。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="不把普通文明风尚表述强行提升为文化主链。", artifact=source("201-240"))
    upd("M0324", question="Q6", qtype="法律与生活边界题", in_book="否：选必二法律与生活边界", node="NO_DOCX_ACTION", support="Q6围绕债权、担保物权、质权和优先受偿；官方答案键C，非必修四正文。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="关闭旧认识术语命中。", artifact=source("201-250"))
    upd("M0325", question="Q9", qtype="选择题正确项链条", in_book="是：已进入当前DOCX/PDF正文", node="矛盾的普遍性", support="官方答案键D；正确项写明无处不在的矛盾，能引发对生命意义、生命潜能的反思。", evidence=choice_ev, current="DOCX_Q9_MOVED_TO_CORRECT_NODE_RENDER_PENDING", note="从主观能动性节点移出，防止误读为支持错误项B。", artifact=source("201-270"))
    upd("M0326", question="Q10", qtype="选择题边界关闭", in_book="否：当前框架无独立价值概念节点，暂不强塞正文", node="NO_DOCX_ACTION", support="官方答案键A；正确项①③涉及价值概念和文化价值生成，不等同于价值观导向、价值判断或人生价值节点。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="保留为价值概念素材，不在本次正文补入。", artifact=source("201-280"))
    upd("M0327", question="Q11", qtype="逻辑与思维边界题", in_book="否：选必三逻辑与思维边界", node="NO_DOCX_ACTION", support="Q11考查推理形式与结论可靠性；官方答案键B，非必修四哲学/文化正文。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="关闭旧部分术语命中。", artifact=source("201-300"))
    upd("M0328", question="Q12", qtype="选择题正确项链条", in_book="是：已进入当前DOCX/PDF正文", node="辩证否定 / 守正创新", support="官方答案键C；正确项说明肯定与否定互为条件且只存在于联系中，当前DOCX已有本题正文条目。", evidence=choice_ev, current="CURRENT_DOCX_COVERAGE_VERIFIED", note="保留现有正文位置；不新增。", artifact=source("201-310"))
    upd("M0329", question="Q15", qtype="当代国际政治与经济边界题", in_book="否：选必一/国际政治经济边界", node="NO_DOCX_ACTION", support="Q15围绕一带一路、共商共建共享、国际合作；官方答案键C，非必修四正文。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="关闭旧发展/实践/部分术语命中。", artifact=source("201-330"))
    upd("M0330", question="Q17", qtype="哲学主观题", in_book="是：已进入当前DOCX/PDF正文", node="生态价值观/实践与认识/规律与主观能动性/联系与发展/对立统一/辩证否定", support="正式细则Q17列出生态价值观、实践与认识、客观规律与主观能动性、联系与发展、对立统一、否定之否定等角度；附中版要求三个知识点、每点理论+材料，价值观为怎么做角度必出。", evidence=formal_ev, current="CURRENT_DOCX_COVERAGE_VERIFIED", note="当前DOCX已有11处2024西城一模条目，其中Q17多节点覆盖。", artifact=source("82-110"))
    upd("M0331", question="Q18", qtype="法律与生活主观题", in_book="否：选必二法律与生活主线，文化价值仅作法律题意义点", node="NO_DOCX_ACTION", support="Q18主问为法治知识、赡养义务、回避制度和诉讼代理人；文化/传统美德仅是法律题意义点，不单独进入必修四正文。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="普通文化意义点不冒充必修四文化主链。", artifact=source("82-130"))
    upd("M0332", question="Q19", qtype="逻辑与思维/经济边界综合题", in_book="否：选必三逻辑与思维及经济边界", node="NO_DOCX_ACTION", support="Q19(5)明确要求运用《逻辑与思维》知识研判未来产业方向；其他小问为经济/国际经济内容，非必修四正文。", evidence=boundary_ev, current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="虽有实践、矛盾等词，但题目模块和评分任务不是必修四主链。", artifact=source("82-160"))
    upd("M0333", question="Qunknown", qtype="抽取残片", in_book="否：抽取残片关闭", node="NO_DOCX_ACTION", support="该行来自答案文件整段抽取残留；本次已逐题裁决Q1-Q19。", evidence="套卷逐题裁决完成", current="SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", note="不作为独立题目。", artifact=source("13-201"))
    for rid in ["M0784", "M0825"]:
        if rid in by_id:
            upd(rid, question="SUITE_LEVEL", qtype="套卷闭合记录", in_book="套卷有最终DOCX提及或闭合记录", node="SUITE_LEVEL_SUMMARY", support="当前DOCX已有2024西城一模正文提及，且本次补入Q2、移动Q9、逐题关闭旧候选。", evidence="COVERED_OR_PATCHED_WITH_ROW_REVIEW", current="SUITE_LEVEL_CLOSED", note="不得把套卷级闭合记录当作行级证据；行级证据见Q2/Q9/Q12/Q17及边界行。", artifact=source("201-380"))

    next_id = max(int(r[fieldnames[0]][1:]) for r in rows if r.get(fieldnames[0], "").startswith("M") and r.get(fieldnames[0], "")[1:].isdigit()) + 1
    additions = [
        ("Q3", "选择题边界排除", "否：政治品格/干部价值表达，不进当前正文", "NO_DOCX_ACTION", "官方答案键D，材料指向党员干部价值追求和奋斗姿态；不是可稳定落到必修四价值观方法论的评分链。", boundary_ev, "SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", "不把政治格言直接改写成价值观主链。", "201-235"),
        ("Q5", "法律与生活边界题", "否：司法/法治边界", "NO_DOCX_ACTION", "Q5围绕司法机关定分止争、司法担当和社会和谐；官方答案键B，非必修四正文。", boundary_ev, "SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", "补足缺失逐题行。", "201-245"),
        ("Q8", "法律与生活边界题", "否：民事纠纷解决边界", "NO_DOCX_ACTION", "Q8围绕人民调解、诉讼和相邻关系纠纷解决；官方答案键D，非必修四正文。", boundary_ev, "SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", "补足缺失逐题行。", "201-260"),
        ("Q13", "逻辑与思维边界题", "否：选必三逻辑与思维边界", "NO_DOCX_ACTION", "Q13考查联想思维特征；官方答案键B，属于逻辑与思维，不进必修四正文。", boundary_ev, "SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", "补足缺失逐题行。", "201-320"),
        ("Q14", "当代国际政治与经济边界题", "否：选必一国际政治经济边界", "NO_DOCX_ACTION", "Q14围绕中国-东盟开放包容伙伴关系和人类命运共同体；官方答案键A，非必修四正文。", boundary_ev, "SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", "补足缺失逐题行。", "201-330"),
        ("Q16", "政治与法治主观题", "否：政治与法治边界", "NO_DOCX_ACTION", "Q16设问明确运用《政治与法治》知识说明市人大如何推进条例修订；非必修四正文。", boundary_ev, "SOURCE_REVIEWED_CLOSED_NO_DOCX_ACTION", "补足缺失逐题行。", "82-100"),
    ]
    added = []
    existing_questions = {(r.get(fieldnames[2]), r.get(fieldnames[5]), r.get(fieldnames[13])) for r in rows}
    for question, qtype, in_book, node, support, evidence, current, note, lines in additions:
        marker = (SUITE, question, current)
        if marker in existing_questions:
            continue
        next_id = append_row(rows, fieldnames, h, next_id, question=question, qtype=qtype, in_book=in_book, node=node, support=support, evidence=evidence, current=current, note=note, artifact=source(lines))
        added.append(f"M{next_id - 1:04d}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "updated_rows": updated, "added_rows": added}


def write_report(ts: str, docx_result: dict[str, object], ledger_result: dict[str, object], matrix_result: dict[str, object]) -> None:
    report = {
        "status": "XICHENG_2024_YIMO_REPAIRED_DOCX_Q2_INSERTED_Q9_MOVED_RENDER_PENDING",
        "timestamp": ts,
        **docx_result,
        **ledger_result,
        **matrix_result,
        "model_gates": {
            "gptpro_web": "real_call_pending",
            "claude_opus_web_app_full_artifact_review": "real_call_pending_direct_claude_ai",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
        },
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# XICHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525",
        "",
        "Status: `XICHENG_2024_YIMO_REPAIRED_DOCX_Q2_INSERTED_Q9_MOVED_RENDER_PENDING_MODEL_GATES_OPEN`",
        "",
        f"- Timestamp: `{ts}`.",
        "- Corrective action: inserted Q2 under `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一` as a choice-question chain.",
        "- Corrective action: moved Q9 from the old `主观能动性 / 意识的能动作用` placement to `矛盾的普遍性`, because the official answer key supports D and rejects the tree-subjectivity option.",
        "- Existing current-DOCX coverage for Q12 and Q17 was verified and reflected in the matrix.",
        "- Remaining questions were closed as answer-key/module-boundary/no-DOCX-action rows; Q10 is retained as a value-concept material but not forced into a non-matching current framework node.",
        f"- DOCX backup: `{Path(str(docx_result['docx_backup'])).name}`.",
        f"- Matrix backup: `{Path(str(matrix_result['matrix_backup'])).name}`.",
        f"- Ledger backup: `{Path(str(ledger_result['ledger_backup'])).name if ledger_result.get('ledger_backup') else 'none'}`.",
        f"- Removed old Q9 paragraphs: `{docx_result['removed_q9_paragraphs']}`.",
        f"- Matrix rows updated: `{len(matrix_result['updated_rows'])}`.",
        f"- Matrix rows added: `{len(matrix_result['added_rows'])}`.",
        "",
        "## Inserted Or Reinserted Headings",
        "",
    ]
    for heading in docx_result["inserted_headings"]:
        lines.append(f"- `{heading}`")
    lines.extend(
        [
            "",
            "## Open Gates",
            "",
            "- Render QA is required because the DOCX changed.",
            "- GPTPro web full artifact review remains `real_call_pending`.",
            "- Claude Opus web/app full artifact review remains `real_call_pending`; corrected route is direct `https://claude.ai` auto-login.",
            "- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
        ]
    )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = edit_docx(ts)
    ledger_result = update_ledger(ts, docx_result["inserted_headings"])
    matrix_result = update_matrix(ts)
    write_report(ts, docx_result, ledger_result, matrix_result)
    print(json.dumps({"status": "XICHENG_2024_YIMO_REPAIRED_DOCX_Q2_INSERTED_Q9_MOVED_RENDER_PENDING", **docx_result, **ledger_result, **matrix_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
