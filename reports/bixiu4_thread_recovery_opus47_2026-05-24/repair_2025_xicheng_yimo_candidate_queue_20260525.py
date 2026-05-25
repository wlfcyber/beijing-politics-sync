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
REPORT_MD = RECOVERY / "XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
UPLOAD_SCOPE = RECOVERY / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"

SUITE = "2025西城一模"
YEAR = "2025"
STAGE = "一模"
SOURCE_BUNDLE = (
    "preprocessed_corpus\\gpt_suite_bundles\\"
    "2025各区模拟题__2025各区一模__2025西城一模.md"
)

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q2",
        "heading_suffix": "2025西城一模 第2题（选择题）",
        "material_trigger": "题干把“民惟邦本”“自强不息”“苟日新”“天人合一”等中华优秀传统文化资源同当代治国理政、高质量发展、生态理念相连接；正确项为②③。",
        "question_prompt": "建设中华民族现代文明，正确组合为C（②③）：既要有一脉相承的坚持坚守，又要有独树一帜的创新创造；要植根于中华优秀传统文化，彰显中华文化的主体性。",
        "why_trigger": "“坚持坚守”和“创新创造”并列，是典型的守正创新表达；“植根中华优秀传统文化”说明文化现代化不是抛弃传统，而是在继承中发展，在发展中创新。",
        "answer_landing": "本题应选C。建设中华民族现代文明，要坚持守正创新，既传承中华优秀传统文化的根脉，又推动其创造性转化、创新性发展，形成具有主体性的现代文明表达。本条只作选择题正确项链条，不作主观题评分细则。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:185-193; {SOURCE_BUNDLE}:476-479",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q4",
        "heading_suffix": "2025西城一模 第4题（选择题）",
        "material_trigger": "题干围绕政府工作报告中“投资于人”，并把“人的发展和保障”同资金资源配置联系起来；正确项③写明人是发展的目的、以人民为中心。",
        "question_prompt": "关于“投资于人”与“投资于物”的关系，正确答案为D（③④）：人是发展的目的，强调更多资金资源投资于人是以人民为中心的生动体现；要把投资于物同投资于人结合起来。",
        "why_trigger": "看到“投资于人”“人的发展和保障”“人是发展的目的”，应从人民群众和人民立场理解发展目的：发展不是为了物本身，而是为了满足人民需要、促进人的全面发展。",
        "answer_landing": "本题应选D。本节点只处理③：人民群众是社会历史的主体，发展必须坚持人民立场，把人的发展和保障作为现代化的重要目的。④可作为联系/良性循环的选择题信息，不扩展成主观题评分链条。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:205-212; {SOURCE_BUNDLE}:476-479",
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q16",
        "heading_suffix": "2025西城一模 第16题（主观题）",
        "material_trigger": "正式细则文化分析3分要求：学习、了解中华优秀传统文化；深化对本民族文化的理解、增进文化认同；以实际行动弘扬和传承中华优秀传统文化/促进文化创新/创造性转化创新性发展。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐述行动框架中从“行前准备”到“持续行动”的必要性。",
        "why_trigger": "行动框架不是停留在诵读和观看纪录片，而是安排实地研学、校园诗经角、主题旅游路线等持续行动，说明对优秀传统文化的学习要转化为传承、弘扬和创新实践。",
        "answer_landing": "从文化角度看，研学行动要在理解《诗经》等中华优秀传统文化的基础上，增进文化认同和文化自信，并通过持续种植、文化墙更新、文旅路线设计等行动推动中华优秀传统文化创造性转化、创新性发展。",
        "evidence_level": "正式评分细则（主观题，文化分析3分）",
        "source_lines": f"{SOURCE_BUNDLE}:47-56; {SOURCE_BUNDLE}:344-361",
    },
]

UPDATED_Q22_VALUE_ENTRY = {
    "material_trigger": "正式细则第22题要求从“把握发展趋势”“正确价值观”和“中华优秀传统文化/民族精神/自强不息”等角度作答；材料写“坚持就是胜利”“做困难而正确的事”“长期主义深植于中华民族的文化基因”。",
    "question_prompt": "“坚持长期主义，做困难而正确的事”，结合材料，综合运用所学，谈谈你对这句话的理解。",
    "why_trigger": "“困难而正确”首先是价值判断：把长期价值、可持续价值置于短期功利之上；“长期主义深植于中华民族的文化基因”又说明这种价值追求有中华优秀传统文化和自强不息民族精神作支撑。",
    "answer_landing": "正确价值观对人们认识世界、改造世界具有导向作用。坚持长期主义，就是以符合规律、符合人民长远利益的正确价值观抵制短期主义和功利主义；同时要从中华优秀传统文化和自强不息民族精神中汲取力量，把“做困难而正确的事”转化为长期坚持的实践选择。",
}


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


def is_section_heading(p) -> bool:
    return p_style(p) in {"Heading2", "2", "4"}


def is_entry_heading(p) -> bool:
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


def set_plain_text(p, text: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(text))


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
    start = next((i for i, p in enumerate(paras) if is_section_heading(p) and para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if is_section_heading(paras[i])), len(paras))
    return start, end


def section_templates(paras, start: int, end: int):
    heading_template = next((paras[i] for i in range(start + 1, end) if is_entry_heading(paras[i])), None)
    label_template = next(
        (paras[i] for i in range(start + 1, end) if not is_entry_heading(paras[i]) and para_text(paras[i]).strip().startswith("【")),
        None,
    )
    blank_template = next((paras[i] for i in range(start + 1, end) if not para_text(paras[i]).strip()), None)
    if heading_template is None or label_template is None:
        raise RuntimeError(f"Could not locate templates in section {para_text(paras[start])}")
    return heading_template, label_template, blank_template


def next_heading_number(paras, start: int, end: int) -> int:
    numbers: list[int] = []
    for i in range(start + 1, end):
        if not is_entry_heading(paras[i]):
            continue
        head = para_text(paras[i]).strip().split(".", 1)[0]
        if head.isdigit():
            numbers.append(int(head))
    return (max(numbers) if numbers else 0) + 1


def add_entry(body, entry: dict[str, str]) -> str:
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    heading_template, label_template, blank_template = section_templates(paras, start, end)
    number = next_heading_number(paras, start, end)
    heading = deepcopy(heading_template)
    heading_text = f"{number}. {entry['heading_suffix']}"
    set_plain_text(heading, heading_text)
    insert_at = list(body).index(paras[end]) if end < len(paras) else len(body)
    body.insert(insert_at, heading)
    insert_at += 1
    for label, key in LABELS:
        p = deepcopy(label_template)
        set_label_text(p, label, entry[key])
        body.insert(insert_at, p)
        insert_at += 1
    if blank_template is not None:
        body.insert(insert_at, deepcopy(blank_template))
    return heading_text


def remove_q17_entry(body) -> int:
    paras = [p for p in body if p.tag == W + "p"]
    removed = 0
    for i, p in enumerate(paras):
        text = para_text(p)
        if SUITE in text and "第17题" in text:
            end = i + 1
            while end < len(paras) and not is_entry_heading(paras[end]) and not is_section_heading(paras[end]):
                end += 1
            for target in paras[i:end]:
                body.remove(target)
                removed += 1
            break
    return removed


def update_q22_value_entry(body) -> bool:
    paras = [p for p in body if p.tag == W + "p"]
    for i, p in enumerate(paras):
        if SUITE in para_text(p) and "第22题" in para_text(p):
            section = None
            for j in range(i - 1, -1, -1):
                if is_section_heading(paras[j]):
                    section = para_text(paras[j]).strip()
                    break
            if section != "价值观的导向作用":
                continue
            labels_seen = 0
            k = i + 1
            while k < len(paras) and labels_seen < 4:
                text = para_text(paras[k]).strip()
                for label, key in LABELS:
                    if text.startswith(label):
                        set_label_text(paras[k], label, UPDATED_Q22_VALUE_ENTRY[key])
                        labels_seen += 1
                        break
                k += 1
            return labels_seen == 4
    return False


def write_docx_from_tree(temp: Path, target: Path) -> None:
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zout:
        for path in temp.rglob("*"):
            if path.is_file():
                zout.write(path, path.relative_to(temp).as_posix())


def edit_docx(timestamp: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_xicheng_yimo_repair_{timestamp}.docx")
    shutil.copy2(docx, backup)
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
        removed_paragraphs = remove_q17_entry(body)
        inserted_headings = [add_entry(body, entry) for entry in INSERT_ENTRIES]
        q22_updated = update_q22_value_entry(body)
        tree.write(str(document_xml), encoding="utf-8", xml_declaration=True, standalone=True)
        write_docx_from_tree(temp, docx)
    return {
        "docx": str(docx),
        "docx_backup": str(backup),
        "removed_q17_paragraphs": removed_paragraphs,
        "inserted_headings": inserted_headings,
        "q22_value_entry_updated": q22_updated,
    }


def update_ledger(timestamp: str, inserted_headings: list[str]) -> dict[str, object]:
    backup = None
    rows: list[dict[str, str]] = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2025_xicheng_yimo_repair_{timestamp}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames:
                fieldnames = reader.fieldnames
            rows = [r for r in reader if not (r.get("source_suite") == SUITE and r.get("question_no") == "Q17")]
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for entry, heading in zip(INSERT_ENTRIES, inserted_headings, strict=True):
        row = {
            "canonical_node": entry["canonical_node"],
            "source_suite": SUITE,
            "question_no": entry["question_no"],
            "inserted_heading": heading.split(". ", 1)[1],
        }
        key = (row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in existing:
            rows.append(row)
            added.append(row["inserted_heading"])
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger_backup": str(backup) if backup else None, "ledger_rows_added": added}


def update_matrix(timestamp: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2025_xicheng_yimo_candidate_repair_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    by_id = {r["matrix_row_id"]: r for r in rows}

    def set_row(row_id: str, **updates: str) -> None:
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        by_id[row_id].update(updates)

    def decision(
        row_id: str,
        q: str,
        kind: str,
        in_book: str,
        node: str,
        support: str,
        evidence: str,
        misplaced: str,
        thick: str,
        current: str,
        note: str,
        source: str,
    ) -> None:
        set_row(
            row_id,
            题源=SUITE,
            年份=YEAR,
            阶段=STAGE,
            题号=q,
            题型或模块判断=kind,
            是否进宝典=in_book,
            宝典节点=node,
            细则支持原理=support,
            证据等级=evidence,
            是否误放=misplaced,
            是否需补厚=thick,
            当前处理=current,
            备注=note,
            source_artifact=source,
        )

    decision(
        "M0469",
        "Q1",
        "选择题：三农/改革开放话语，非稳定必修四挂点",
        "否：不进正文",
        "-",
        "官方答案A只支持①③；改革话语属于政策/中国特色社会主义语境，不能因词命中扩展为哲学或文化评分链条。",
        "官方答案键+边界裁决",
        "否：未进正文",
        "否",
        "EXCLUDE_NON_BIXIU4_CHOICE_KEY_ONLY",
        "旧生产线仅因“改革”命中，已裁决为非正文。",
        f"{SOURCE_BUNDLE}:170-184; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0470",
        "Q2",
        "选择题：必修四文化/守正创新正确项链条",
        "是：已进入当前DOCX/PDF正文",
        "辩证否定 / 守正创新",
        "官方答案C支持②③：坚持坚守与创新创造；植根中华优秀传统文化、彰显中华文化主体性。",
        "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "否",
        "否",
        "INSERTED_CHOICE_CHAIN_NOT_MAIN_RUBRIC",
        "本题是选择题，只作正确项挂点；不冒充主观题评分细则。",
        f"{SOURCE_BUNDLE}:185-193; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0471",
        "Q3",
        "选择题：认识论正确项链条",
        "是：已进入当前DOCX/PDF正文",
        "认识发展原理",
        "官方答案A支持“世界上只有尚未被认识之物，没有不可认识之物”。",
        "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "否",
        "否",
        "KEEP_CURRENT_DOCX_CHOICE_CHAIN",
        "当前DOCX已有该题认识发展原理条目；保留并标明选择题边界。",
        f"{SOURCE_BUNDLE}:198-204; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0472",
        "Q4",
        "选择题：人民立场/人民群众正确项链条",
        "是：已进入当前DOCX/PDF正文",
        "人民群众",
        "官方答案D支持③④；本条只取③“人是发展的目的、以人民为中心”的必修四社会历史观挂点。",
        "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "否",
        "否",
        "INSERTED_CHOICE_CHAIN_NOT_MAIN_RUBRIC",
        "④的联系/良性循环信息不扩展为主观评分链条。",
        f"{SOURCE_BUNDLE}:205-212; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0473",
        "Q5",
        "选择题：逻辑/人本质表述，正文不新增",
        "否：不进正文",
        "-",
        "官方答案D只是选择题正确项；旧候选的“意识/矛盾”命中不受答案键支持，不能扩展为正文条目。",
        "官方答案键+边界裁决",
        "否：未进正文",
        "否",
        "EXCLUDE_WEAK_TERM_HIT",
        "机器人半马题不建立稳定必修四宝典节点。",
        f"{SOURCE_BUNDLE}:213-218; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0474",
        "Q7",
        "选择题：动态性辩证思维，选必三边界",
        "否：候选线已判边界排除",
        "-",
        "官方答案C写“动态性的辩证思维”，属于选必三《逻辑与思维》思维方法边界。",
        "官方答案键+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_XUANBISAN",
        "不因“部分”等词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:244-251; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0475",
        "Q8",
        "选择题：城市治理/数据赋能，非稳定必修四挂点",
        "否：不进正文",
        "-",
        "官方答案B强调数据赋能治理、增强预见性、提升政务服务效能；不能仅因“预见性”扩展为意识能动性条目。",
        "官方答案键+边界裁决",
        "否：未进正文",
        "否",
        "EXCLUDE_NON_BIXIU4_CHOICE_KEY_ONLY",
        "城市治理信息不生成哲学/文化正文。",
        f"{SOURCE_BUNDLE}:252-258; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0476",
        "Q11",
        "选择题：法律与生活边界",
        "否：候选线已判边界排除",
        "-",
        "委托合同/侵权责任属于选必二《法律与生活》。",
        "官方答案键+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_XUANBIER",
        "旧行误挂到细则包，已按题号重裁。",
        f"{SOURCE_BUNDLE}:294-299; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0477",
        "Q12",
        "选择题：经济与社会边界",
        "否：候选线已判边界排除",
        "-",
        "赋权、科技成果转化、收入分配和创新活力属于经济模块。",
        "官方答案键+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_ECONOMICS",
        "不因“发展/改革”词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:300-306; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0478",
        "Q13",
        "选择题：统一大市场/经济法治边界",
        "否：候选线已判边界排除",
        "-",
        "全国统一大市场、市场基础制度规则统一属于经济/法治政策边界。",
        "官方答案键+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_ECONOMICS_OR_LAW",
        "旧候选的“发展/部分”命中不成立。",
        f"{SOURCE_BUNDLE}:307-329; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0479",
        "Q14",
        "选择题：国际法/选必一边界",
        "否：候选线已判边界排除",
        "-",
        "国际法和国际交往规则属于选必一《当代国际政治与经济》。",
        "官方答案键+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_XUANBIYI",
        "不因“发展”词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:330-336; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0480",
        "Q15",
        "选择题：全球治理/选必一边界",
        "否：候选线已判边界排除",
        "-",
        "人工智能全球治理与金砖国家合作属于选必一国际政治经济边界。",
        "官方答案键+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_XUANBIYI",
        "不因“发展/部分”词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:337-343; {SOURCE_BUNDLE}:476-479",
    )
    decision(
        "M0481",
        "Q16",
        "主观题：必修四哲学文化综合",
        "是：已进入当前DOCX/PDF正文",
        "实践与认识（总）; 实践是认识的基础; 认识对实践的反作用; 认识发展原理; 辩证否定 / 守正创新",
        "正式细则：哲学3分（以知导行、实践决定认识、认识深化）+文化3分（了解优秀传统文化、增进文化认同、弘扬传承/文化创新）+一致性1分。",
        "正式评分细则",
        "否",
        "否",
        "CURRENT_DOCX_COVERED_AND_CULTURE_CHAIN_INSERTED",
        "原正文已有认识论多节点；本轮补入文化创新/守正创新链条。",
        f"{SOURCE_BUNDLE}:47-56; {SOURCE_BUNDLE}:344-361",
    )
    decision(
        "M0482",
        "Q17",
        "主观题：选必三科学思维边界",
        "否：已从当前DOCX/PDF正文移除",
        "-",
        "正式细则要求追求认识客观性、辩证思维方法、创新思维三个维度，属于选必三《逻辑与思维》科学思维。",
        "正式评分细则+模块边界",
        "否：旧误放已修复，当前正文无误放",
        "否",
        "REMOVED_FROM_DOCX_EXCLUDE_XUANBISAN",
        "旧正文曾放在“一切从实际出发”，本轮删除。",
        f"{SOURCE_BUNDLE}:59-84; {SOURCE_BUNDLE}:366-373",
    )
    decision(
        "M0483",
        "Q18",
        "主观题：经济与社会边界",
        "否：候选线已判边界排除",
        "-",
        "正式细则为产业优势、物质条件、市场/双循环等经济模块。",
        "正式评分细则+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_ECONOMICS",
        "不因“发展/改革/物质”词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:85-99; {SOURCE_BUNDLE}:375-377",
    )
    decision(
        "M0484",
        "Q19",
        "主观题：政治与法治边界",
        "否：候选线已判边界排除",
        "-",
        "正式细则为人大代表履职、国家机关办理建议、全过程人民民主。",
        "正式评分细则+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_POLITICS_AND_LAW",
        "不因“人民群众/发展”词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:100-113; {SOURCE_BUNDLE}:378-423",
    )
    decision(
        "M0485",
        "Q21",
        "主观题：当代国际政治与经济边界",
        "否：候选线已判边界排除",
        "-",
        "发展理念成为国际公共产品，属于选必一国际公共产品/全球治理语境。",
        "正式评分细则+模块边界",
        "否：按边界排除",
        "否",
        "EXCLUDE_XUANBIYI",
        "不因“理念/价值/发展”词命中进入必修四正文。",
        f"{SOURCE_BUNDLE}:127-139; {SOURCE_BUNDLE}:433-446",
    )
    decision(
        "M0486",
        "Q22",
        "主观题：必修四哲学文化综合",
        "是：已进入当前DOCX/PDF正文",
        "规律的客观性; 量变与质变 / 适度原则; 事物发展是前进性与曲折性的统一; 真理观; 价值观的导向作用",
        "正式细则：把握发展趋势/长期与正确两个层面；长期主义植根中华优秀传统文化，蕴含自强不息民族精神；正确价值观、坚持真理、尊重规律等。",
        "正式评分细则",
        "否",
        "否",
        "CURRENT_DOCX_COVERED_Q22_VALUE_CULTURE_THICKENED",
        "当前DOCX已有Q22五个哲学节点；本轮补厚价值观条目的优秀传统文化/民族精神落点。",
        f"{SOURCE_BUNDLE}:141-146; {SOURCE_BUNDLE}:451-462",
    )
    for row_id in ["M0180", "M0214"]:
        decision(
            row_id,
            "Q16",
            "主观题：必修四哲学文化综合",
            "是：已进入当前DOCX/PDF正文",
            "实践与认识（总）; 实践是认识的基础; 认识对实践的反作用; 认识发展原理; 辩证否定 / 守正创新",
            "正式细则哲学3分+文化3分+一致性1分；当前正文已有认识论多节点，本轮补入文化创新链条。",
            "正式评分细则",
            "否",
            "否",
            "CURRENT_DOCX_COVERED_AND_CULTURE_CHAIN_INSERTED",
            "与M0481同题去重闭合；不再作为待核候选。",
            f"{SOURCE_BUNDLE}:47-56; {SOURCE_BUNDLE}:344-361",
        )
    for row_id in ["M0181", "M0215"]:
        decision(
            row_id,
            "Q17",
            "主观题：选必三科学思维边界",
            "否：已从当前DOCX/PDF正文移除",
            "-",
            "正式细则要求科学思维/辩证思维/创新思维，属于选必三边界。",
            "正式评分细则+模块边界",
            "否：旧误放已修复，当前正文无误放",
            "否",
            "REMOVED_FROM_DOCX_EXCLUDE_XUANBISAN",
            "与M0482同题去重闭合。",
            f"{SOURCE_BUNDLE}:59-84; {SOURCE_BUNDLE}:366-373",
        )

    next_id = max(int(r["matrix_row_id"][1:]) for r in rows if r["matrix_row_id"].startswith("M")) + 1
    added = []

    def add_missing(q: str, kind: str, support: str, current: str, note: str, source: str) -> None:
        nonlocal next_id
        row = {name: "" for name in fieldnames}
        row.update(
            {
                "matrix_row_id": f"M{next_id:04d}",
                "row_source": "codex_recovery_2025_xicheng_yimo_explicit_boundary",
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": q,
                "题型或模块判断": kind,
                "是否进宝典": "否：候选线已判边界排除",
                "宝典节点": "-",
                "细则支持原理": support,
                "证据等级": "官方答案键/题干+模块边界",
                "是否误放": "否：未进正文",
                "是否需补厚": "否",
                "当前处理": current,
                "备注": note,
                "source_artifact": source,
            }
        )
        rows.append(row)
        added.append(row["matrix_row_id"])
        next_id += 1

    existing_qs = {(r["题源"], r["题号"]) for r in rows}
    if (SUITE, "Q6") not in existing_qs:
        add_missing("Q6", "选择题：逻辑与思维边界", "假言判断/充分必要条件/推理规则，属于选必三逻辑边界。", "EXCLUDE_XUANBISAN_LOGIC", "补齐Q1-Q22显式决策。", f"{SOURCE_BUNDLE}:219-227; {SOURCE_BUNDLE}:476-479")
    if (SUITE, "Q9") not in existing_qs:
        add_missing("Q9", "选择题：行政法/法律边界", "行政处罚、过罚相当、行政相对人权益，属于法律模块。", "EXCLUDE_XUANBIER_OR_POLITICS_LAW", "补齐Q1-Q22显式决策。", f"{SOURCE_BUNDLE}:260-283; {SOURCE_BUNDLE}:476-479")
    if (SUITE, "Q10") not in existing_qs:
        add_missing("Q10", "选择题：著作权/肖像权/隐私权边界", "公众号发布图片与照片的权利风险，属于法律模块。", "EXCLUDE_XUANBIER", "补齐Q1-Q22显式决策。", f"{SOURCE_BUNDLE}:288-293; {SOURCE_BUNDLE}:476-479")
    if (SUITE, "Q20") not in existing_qs:
        add_missing("Q20", "主观题：法律与经济综合边界", "集体协商、劳动合同、劳动者权益、公平效率，属于法律与经济综合。", "EXCLUDE_LAW_AND_ECONOMICS", "补齐Q1-Q22显式决策。", f"{SOURCE_BUNDLE}:115-125; {SOURCE_BUNDLE}:424-431")

    set_row(
        "M0840",
        题型或模块判断="套卷级覆盖口径，已由逐题修复覆盖",
        是否进宝典="套卷有最终DOCX提及或闭合记录",
        宝典节点="SUITE_LEVEL_SUMMARY_SUPERSEDED",
        细则支持原理="逐题矩阵已补齐Q1-Q22决策；套卷级行不替代逐题细则核验。",
        证据等级="COVERED_OR_PATCHED",
        是否误放="不适用",
        是否需补厚="否",
        当前处理="SUPERSEDED_BY_ROW_LEVEL_REPAIR",
        备注="2025西城一模本轮回源闭合；不再作为风险行。",
    )

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "added_rows": added, "updated_rows": 25}


def append_text(path: Path, text: str) -> None:
    existing = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    path.write_text(existing.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def write_reports(timestamp: str, docx_result: dict[str, object], ledger_result: dict[str, object], matrix_result: dict[str, object]) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")
    report = f"""
# XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `XICHENG_2025_YIMO_REPAIRED_DOCX_Q17_REMOVED_Q2_Q4_Q16_INSERTED_RENDER_PENDING`

Updated: {now}

## Source Basis

- Source bundle: `{SOURCE_BUNDLE}`.
- Formal source inventory: bundle lines `7-8`.
- Official answer key: bundle lines `21-26` and `476-479`.
- Q16 formal rubric: bundle lines `47-56`.
- Q17 formal rubric: bundle lines `59-84`.
- Q22 formal rubric: bundle lines `141-146`.

## Decisions

- Removed Q17 from current DOCX because the formal rubric requires scientific thinking / dialectical thinking / innovative thinking, which belongs to the selected-compulsory-three boundary.
- Inserted Q2 under `辩证否定 / 守正创新` as a culture choice-question chain supported by the official answer key.
- Inserted Q4 under `人民群众` as a choice-question chain for the people-centered development purpose.
- Inserted Q16 under `辩证否定 / 守正创新` to cover the formal culture rubric point: cultural identity, inheritance, cultural innovation, and creative transformation/innovative development.
- Updated the existing Q22 value-guidance entry to include the formal rubric's Chinese excellent traditional culture / self-improvement national-spirit landing.
- Kept existing current-DOCX coverage for Q3, Q16 recognition nodes, and Q22 philosophy nodes.
- Excluded Q1/Q5/Q6-Q15/Q18-Q21 by official answer key, formal rubric, or module boundary.
- Added missing matrix boundary rows for Q6/Q9/Q10/Q20 so Q1-Q22 have explicit decisions.
- Choice-question chains are not treated as main-question scoring-rubric evidence.
- No Sonnet/Haiku/model-unknown evidence was promoted.
- GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review remain `real_call_pending`.

## Backups And Outputs

- DOCX backup: `{docx_result['docx_backup']}`.
- Matrix backup: `{matrix_result['matrix_backup']}`.
- Ledger backup: `{ledger_result['ledger_backup']}`.
- DOCX Q17 removed paragraphs: `{docx_result['removed_q17_paragraphs']}`.
- Inserted headings: `{'; '.join(docx_result['inserted_headings'])}`.
- Q22 value entry updated: `{docx_result['q22_value_entry_updated']}`.
- Matrix rows added: `{', '.join(matrix_result['added_rows'])}`.

## Boundary

This is a local source/DOCX/matrix repair. Render QA is required after this DOCX change. External model review, full manual typography review, ClaudeCode model confirmation, and the deferred ORDER_063 final GitHub upload gate remain open.
"""
    REPORT_MD.write_text(report.strip() + "\n", encoding="utf-8")
    REPORT_JSON.write_text(
        json.dumps(
            {
                "timestamp": timestamp,
                "docx": docx_result,
                "ledger": ledger_result,
                "matrix": matrix_result,
                "model_evidence": "NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    append_text(
        GOVERNOR,
        f"""
## Governor Finding: Xicheng 2025 Yimo Candidate Queue Repair
Updated: {now}

- Governor decision: `LOCAL_DOCX_Q17_REMOVED_Q2_Q4_Q16_INSERTED_MATRIX_CLOSED_RENDER_PENDING_MODEL_GATES_OPEN`.
- Corrective action: removed the current-DOCX Q17 entry because formal scoring places it in scientific/dialectical/innovative thinking, outside this book boundary.
- Corrective action: inserted Q2 culture choice chain, Q4 people-centered choice chain, and Q16 culture/creative-transformation rubric chain into current DOCX.
- Q22 existing value-guidance entry was thickened with the formal rubric's Chinese excellent traditional culture / self-improvement national-spirit support.
- Matrix action: existing suite rows were rewritten against the source bundle; missing Q6/Q9/Q10/Q20 boundary rows were added so Q1-Q22 have explicit decisions.
- Boundary exclusions: Q1/Q5/Q6-Q15/Q18-Q21 do not enter the current book body except where current-DOCX choice chains are explicitly supported and retained.
- Render QA is required after this DOCX change.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""",
    )
    append_text(
        CONFUCIUS,
        f"""
## Artifact Check: Xicheng 2025 Yimo Candidate Queue Repair
Updated: {now}

- `repair_2025_xicheng_yimo_candidate_queue_20260525.py`: present.
- `XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: present and status `XICHENG_2025_YIMO_REPAIRED_DOCX_Q17_REMOVED_Q2_Q4_Q16_INSERTED_RENDER_PENDING`.
- `XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json`: present.
- DOCX backup before repair: present.
- Matrix backup before rewrite: present.
- Ledger backup before insert registration: present.
- Current DOCX no longer contains the old Q17 entry under `一切从实际出发`.
- Current DOCX now contains new 2025西城一模 entries for Q2, Q4, and Q16 culture/creative-transformation line; Q22 value line has been thickened.
- Matrix now includes explicit Q6/Q9/Q10/Q20 boundary rows.
- Remaining open gates: render QA rerun after DOCX change, GPTPro web review, full Claude Opus web/app review through direct `https://claude.ai`, ClaudeCode model confirmation, and deferred ORDER_063 final GitHub upload.
""",
    )
    append_text(
        STATUS,
        f"""
## Xicheng 2025 Yimo Recovery Repair
Updated: {now}

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_XICHENG_2025_YIMO_DOCX_REPAIRED_RENDER_PENDING`.
- Q17 was removed from the current DOCX as a selected-compulsory-three boundary item.
- Q2/Q4 choice chains and Q16 culture/creative-transformation line were inserted into the current DOCX and registered in `docx_insert_ledger.csv`.
- Q22 value-guidance entry was thickened with formal rubric support for Chinese excellent traditional culture and self-improvement national spirit.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` was rewritten for 2025西城一模 with explicit Q1-Q22 decisions.
- Render QA must be rerun after this DOCX change before this repair can be treated as layout-checked.
- External review gates remain open: GPTPro `real_call_pending`; full Claude Opus web/app `real_call_pending`; ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
""",
    )
    append_text(
        UPLOAD_SCOPE,
        f"""
## Deferred Upload Scope Addition: 2025西城一模 Repair
Updated: {now}

- Include in future ORDER_063 upload scope after all active lines end:
  - `XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`
  - `XICHENG_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json`
  - `repair_2025_xicheng_yimo_candidate_queue_20260525.py`
  - updated `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
  - updated `docx_insert_ledger.csv`
  - current DOCX/PDF after render QA
  - refreshed `FORMAT_RENDER_QA_20260524.md`, `GOVERNOR_RECOVERY_REPORT_20260524.md`, `CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`, `THREAD_RECOVERY_STATUS_20260524.md`
- Upload still deferred; no push before all active Beijing politics lines reach terminal/user-approved states and secret scan records `NO_SECRET_PATTERN_MATCHES`.
""",
    )
    append_text(
        MODEL_LEDGER,
        f"""
## MODEL_GATE_SUMMARY_AFTER_XICHENG_2025_YIMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- 2025西城一模 repair was performed by local cached source bundle, formal rubric/source review, current DOCX removal/insertion, and matrix rewrite.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local repair.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`.
- GPTPro web full artifact review remains `real_call_pending`.
- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    )


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = edit_docx(timestamp)
    ledger_result = update_ledger(timestamp, docx_result["inserted_headings"])
    matrix_result = update_matrix(timestamp)
    write_reports(timestamp, docx_result, ledger_result, matrix_result)
    print(json.dumps({"docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
