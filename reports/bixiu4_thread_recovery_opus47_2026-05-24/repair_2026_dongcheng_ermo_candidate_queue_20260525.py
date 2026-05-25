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
REPORT_MD = RECOVERY / "DONGCHENG_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "DONGCHENG_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026东城二模"
YEAR = "2026"
STAGE = "二模"
ROW_SOURCE = "codex_recovery_20260525_dongcheng_2026_ermo_repair"
TEACHER_DOCX = "2026各区模拟题\\2026各区二模\\2026东城二模\\试卷\\2026北京东城高三二模政治（教师版）.docx"
RUBRIC_16 = "2026各区模拟题\\2026各区二模\\2026东城二模\\细则\\16.pdf"
RUBRIC_21 = "2026各区模拟题\\2026各区二模\\2026东城二模\\细则\\二模21题细则模版.pdf"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

ENTRIES = [
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q2",
        "heading_suffix": "2026东城二模 第2题（选择题）",
        "material_trigger": "商代甲骨文中的“值”与征伐巡视相关，西周大盂鼎铭文在“值”下增“心”而成“德”，施政理念从“以力服人”转向“以心服人”；教师版答案键为C，正确项②写明“德”对“值”的否定增添了新的规定性，正确项③写明中华文明源远流长、生生不息。",
        "question_prompt": "“值”到“德”的字形和理念演进折射出中华文明传承发展；教师版答案键为C（②③）。",
        "why_trigger": "看到“在值下增心而成德”“从以力服人转向以心服人”“后经传承发展，德的内涵不断丰富”，应抓住旧因素被扬弃、新规定性被生成的过程，而不是把文化传承理解成简单复古或彻底抛弃。",
        "answer_landing": "本题应选C。本节点只处理②的哲学链：辩证否定不是全盘否定，而是在保留和改造既有文化符号的基础上增添新的规定性，使“德”从“值”的威慑意味中扬弃出来，发展成更丰富的道德政治理念；③的中华文明连续性作为文化线索保留，不扩展为主观题评分链。",
        "evidence_level": "教师版答案键+题干正确项链（选择题，非主观题评分细则）",
        "source_artifact": TEACHER_DOCX,
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q4",
        "heading_suffix": "2026东城二模 第4题（选择题）",
        "material_trigger": "科研团队用传统“灯诱法”捕捉害虫样本、用先进技术完善数据，从“肉眼辨虫”升级为“智能识虫”；教师版答案键为D，正确项写明在把握灯诱法和先进技术的对立统一中实现识虫效果飞跃。",
        "question_prompt": "人工智能辅助识别田间害虫，传统灯诱法与先进技术结合破解害虫防治难题；教师版答案键为D。",
        "why_trigger": "传统方法和先进技术不是非此即彼：灯诱法提供样本和经验基础，先进技术提供数据完善和智能识别能力。二者存在差异和张力，也能在害虫识别这一实践目标中相互补充、协同转化。",
        "answer_landing": "本题应选D。把握矛盾就是对立统一，才能理解传统灯诱法和先进技术既有区别又能统一于害虫防治实践之中；正是在这种对立统一关系中，科研团队把传统样本捕捉和智能识别结合起来，推动识虫效果实现飞跃。",
        "evidence_level": "教师版答案键+题干正确项链（选择题，非主观题评分细则）",
        "source_artifact": TEACHER_DOCX,
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q21",
        "heading_suffix": "2026东城二模 第21题（主观题）",
        "material_trigger": "材料要求理解科技金融、绿色金融、普惠金融、养老金融、数字金融“五篇大文章”；21题细则明确可从“辩证思维整体性/系统优化/综合思维/联系观——中国特色金融体系——金融强国/中国式现代化”作答。",
        "question_prompt": "结合材料，综合运用所学，谈谈你对做好这“五篇大文章”的理解。",
        "why_trigger": "“五篇大文章”不是彼此孤立的政策清单，而是服务中国式现代化和金融强国建设的金融体系安排。看到“金融体系”“协同发展”“科技、数字、绿色、普惠、养老金融协同发力”等表述，应从联系观和系统优化切入。",
        "answer_landing": "做好“五篇大文章”要坚持系统观念，把科技、数字、绿色、普惠、养老金融放到中国特色现代金融体系中统筹优化，使不同金融资源围绕创新、绿色转型、民生保障和实体经济协同发力；只有优化系统结构、促进各要素联动，才能提高金融服务中国式现代化的整体效能。",
        "evidence_level": "正式评分细则-联系观/系统优化主观题支撑",
        "source_artifact": RUBRIC_21,
    },
]


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


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def find_section(paras, heading: str) -> tuple[int, int]:
    start = next((i for i, p in enumerate(paras) if is_section(p) and para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if is_section(paras[i])), len(paras))
    return start, end


def add_entry(body, entry: dict[str, str]) -> str | None:
    full_heading_suffix = entry["heading_suffix"]
    if any(full_heading_suffix in para_text(p) for p in body if p.tag == W + "p"):
        return None
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    h_template = next(p for p in paras[start + 1 : end] if is_entry(p))
    l_template = next(p for p in paras[start + 1 : end] if para_text(p).strip().startswith("【"))
    blank = next((p for p in paras[start + 1 : end] if not para_text(p).strip()), None)
    nums = []
    for p in paras[start + 1 : end]:
        if is_entry(p):
            head = para_text(p).strip().split(".", 1)[0]
            if head.isdigit():
                nums.append(int(head))
    heading_text = f"{(max(nums) if nums else 0) + 1}. {full_heading_suffix}"
    insert_at = list(body).index(paras[end]) if end < len(paras) else len(body)
    h = deepcopy(h_template)
    set_plain(h, heading_text)
    body.insert(insert_at, h)
    insert_at += 1
    for label, key in LABELS:
        p = deepcopy(l_template)
        set_label(p, label, entry[key])
        body.insert(insert_at, p)
        insert_at += 1
    if blank is not None:
        body.insert(insert_at, deepcopy(blank))
    return heading_text


def edit_docx(ts: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_dongcheng_ermo_insert_{ts}.docx")
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
        for entry in ENTRIES:
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
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, headings: list[str]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_dongcheng_ermo_insert_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for entry, heading in zip(ENTRIES, headings, strict=False):
        clean = heading.split(". ", 1)[1]
        key = (SUITE, entry["question_no"], clean)
        if key in existing:
            continue
        rows.append({"canonical_node": entry["canonical_node"], "source_suite": SUITE, "question_no": entry["question_no"], "inserted_heading": clean})
        added.append(clean)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger_backup": str(backup) if backup else None, "ledger_rows_added": added}


def next_matrix_id(rows: list[dict[str, str]]) -> int:
    nums = []
    for row in rows:
        rid = row.get("matrix_row_id", "")
        if rid.startswith("M") and rid[1:].isdigit():
            nums.append(int(rid[1:]))
    return max(nums, default=0) + 1


def new_row(fieldnames: list[str], mid: int, question: str, qtype: str, in_book: str, node: str, support: str,
            evidence: str, misplaced: str, need_thick: str, current: str, note: str, artifact: str) -> dict[str, str]:
    row = {name: "" for name in fieldnames}
    row.update({
        "matrix_row_id": f"M{mid:04d}",
        "row_source": ROW_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": question,
        "题型或模块判断": qtype,
        "是否进宝典": in_book,
        "宝典节点": node,
        "细则支持原理": support,
        "证据等级": evidence,
        "是否误放": misplaced,
        "是否需补厚": need_thick,
        "当前处理": current,
        "备注": note,
        "source_artifact": artifact,
    })
    return row


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_dongcheng_ermo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    by_id = {r.get("matrix_row_id", ""): r for r in rows}
    updated: list[str] = []
    added: list[str] = []

    yes_body = "是：已进入当前DOCX/PDF正文"
    no_body = "否：不进入当前哲学宝典正文"
    choice_evidence = "教师版答案键+题干正确项链（选择题，非主观题评分细则）"

    row_updates = {
        "M0146": ("候选已核：由Q16既有正文矩阵承接", "SUPERSEDED_BY_EXISTING_Q16_BODY_ROWS", RUBRIC_16, "Q16候选已由M0001-M0006及当前DOCX正文承接。"),
        "M0234": ("候选已核：由Q16既有正文矩阵承接", "SUPERSEDED_BY_EXISTING_Q16_BODY_ROWS", RUBRIC_16, "Q16候选已由M0001-M0006及当前DOCX正文承接。"),
        "M0665": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q1答案A，属于中国特色社会主义/党领导与民族复兴道路选择；不进入当前哲学宝典正文。"),
        "M0666": (yes_body, "KEEP_IN_BODY_INSERTED_20260525", TEACHER_DOCX, "Q2答案C，本轮新增辩证否定/守正创新选择题链，只处理正确项②；正确项③为文化线索。"),
        "M0667": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q3答案B，主要为消费市场与辩证思维表述；不作为必修四主观评分链或正文新增依据。"),
        "M0668": (yes_body, "KEEP_IN_BODY_INSERTED_20260525", TEACHER_DOCX, "Q4答案D，本轮新增矛盾对立统一选择题链。"),
        "M0669": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q5答案A，科学思维追求客观性属选必三科学思维边界；不进入当前哲学宝典正文。"),
        "M0670": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q6答案B，数字经济/算力/新质生产力，属于经济与社会边界。"),
        "M0671": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q8答案C，政务服务法治化与改革成果固化，属于政治与法治边界。"),
        "M0672": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q14答案B，世界数据组织与数字贸易，属于国际经济治理边界。"),
        "M0673": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX, "Q15答案A，外空治理与国际法，属于当代国际政治与经济边界。"),
        "M0674": ("候选已核：由Q16既有正文矩阵承接", "SUPERSEDED_BY_EXISTING_Q16_BODY_ROWS", RUBRIC_16, "Q16问题显性候选已由M0001-M0006及当前DOCX正文承接。"),
        "M0675": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "2026各区模拟题\\2026各区二模\\2026东城二模\\细则\\17题评标.pdf", "Q17评标为政治与法治基层协商、民主与法治建议题，边界排除。"),
        "M0676": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "2026各区模拟题\\2026各区二模\\2026东城二模\\细则\\东城二模 19题阅卷细则.pdf", "Q19阅卷细则为法律与生活/营商环境，边界排除。"),
        "M0677": (no_body, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "2026各区模拟题\\2026各区二模\\2026东城二模\\细则\\20题（1+2）.pdf", "Q20为经济与社会及当代国际政治经济综合题，边界排除。"),
        "M0678": (yes_body, "KEEP_IN_BODY_INSERTED_20260525", RUBRIC_21, "Q21正式细则明确联系观/系统优化角度，本轮新增系统观念正文条目。"),
        "M0679": ("候选已核：逐题矩阵承接", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", TEACHER_DOCX, "抽取残留行，不是独立题号；逐题覆盖已承接。"),
        "M0844": ("套卷级行已被逐题矩阵承接", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", RUBRIC_16, "套卷级覆盖口径已由2026-05-25逐题矩阵修复承接。"),
    }

    for rid, (in_book, current, artifact, support) in row_updates.items():
        row = by_id.get(rid)
        if not row:
            continue
        row["是否进宝典"] = in_book
        row["当前处理"] = current
        row["是否误放"] = "否"
        row["是否需补厚"] = "否"
        row["细则支持原理"] = support
        row["source_artifact"] = artifact
        if rid == "M0666":
            row["题型或模块判断"] = "选择题正确项链"
            row["宝典节点"] = "辩证否定 / 守正创新"
            row["证据等级"] = choice_evidence
        elif rid == "M0668":
            row["题型或模块判断"] = "选择题正确项链"
            row["宝典节点"] = "矛盾就是对立统一"
            row["证据等级"] = choice_evidence
        elif rid == "M0678":
            row["题型或模块判断"] = "必修四哲学主观题正文条目"
            row["宝典节点"] = "系统观念 / 系统优化"
            row["证据等级"] = "强细则"
        elif in_book.startswith("否："):
            row["宝典节点"] = "不进入当前哲学宝典正文"
            row["证据等级"] = "模块边界/题干答案键边界"
        else:
            row["宝典节点"] = "SUPERSEDED_BY_ROW_LEVEL_MATRIX"
            row["证据等级"] = "强细则" if "Q16" in support else "套卷级/候选承接"
        row["备注"] = "2026-05-25回源闭合。"
        updated.append(rid)

    mid = next_matrix_id(rows)
    missing = [
        ("Q7", "经济与社会选择题边界", no_body, "不进入当前哲学宝典正文", "Q7答案C，长期护理保险属于社会保障制度与再分配，经济与社会边界。", "模块边界/教师版答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX),
        ("Q9", "政治/社会治理选择题边界", no_body, "不进入当前哲学宝典正文", "Q9答案B，城市治理聚焦人民幸福感，属于政治治理/公共服务边界；不新增哲学正文。", "模块边界/教师版答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX),
        ("Q10", "法律与生活选择题边界", no_body, "不进入当前哲学宝典正文", "Q10答案D，买卖合同和违约责任，法律与生活边界。", "模块边界/教师版答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX),
        ("Q11", "法律/司法选择题边界", no_body, "不进入当前哲学宝典正文", "Q11答案D，人民法院司法为民、公平正义，政治法治/法律边界。", "模块边界/教师版答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX),
        ("Q12", "逻辑与思维选择题边界", no_body, "不进入当前哲学宝典正文", "Q12答案D，判断与推理，选必三逻辑与思维边界。", "模块边界/教师版答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX),
        ("Q13", "逻辑与思维选择题边界", no_body, "不进入当前哲学宝典正文", "Q13答案C，形式逻辑必然判断，选必三逻辑与思维边界。", "模块边界/教师版答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", TEACHER_DOCX),
        ("Q18", "逻辑与思维主观题边界", no_body, "不进入当前哲学宝典正文", "Q18阅卷细则要求类比推理和超前思维价值，属于选必三逻辑与思维边界。", "强细则-模块边界", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "2026各区模拟题\\2026各区二模\\2026东城二模\\细则\\18题阅卷细则(5.9).pdf"),
    ]
    existing_keys = {(r.get("题源"), r.get("题号"), r.get("宝典节点"), r.get("当前处理")) for r in rows}
    for q, qtype, in_book, node, support, evidence, current, artifact in missing:
        key = (SUITE, q, node, current)
        if key in existing_keys:
            continue
        row = new_row(fieldnames, mid, q, qtype, in_book, node, support, evidence, "否", "否", current, "逐题覆盖补齐。", artifact)
        rows.append(row)
        added.append(row["matrix_row_id"])
        mid += 1

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "updated_rows": updated, "added_rows": added}


def write_report(ts: str, docx_info: dict[str, object], ledger_info: dict[str, object], matrix_info: dict[str, object]) -> dict[str, object]:
    summary = {
        "status": "DONGCHENG_2026_ERMO_REPAIRED_DOCX_Q2_Q4_Q21_INSERTED_RENDER_PENDING",
        "timestamp": ts,
        **docx_info,
        **ledger_info,
        **matrix_info,
        "model_gates": {
            "gptpro_web": "real_call_pending",
            "claude_opus_web_app": "real_call_pending_direct_claude_ai",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
        },
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# DONGCHENG_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525",
        "",
        "Status: `DONGCHENG_2026_ERMO_REPAIRED_DOCX_Q2_Q4_Q21_INSERTED_RENDER_PENDING_MODEL_GATES_OPEN`",
        "",
        f"- Timestamp: `{ts}`.",
        "- Corrective action: inserted Q2 choice chain under `辩证否定 / 守正创新`.",
        "- Corrective action: inserted Q4 choice chain under `矛盾就是对立统一`.",
        "- Corrective action: inserted Q21 formal-rubric chain under `系统观念 / 系统优化`.",
        "- Choice evidence boundary: Q2/Q4 use the teacher-version answer key and are not treated as main-question scoring rules.",
        "- Main-question evidence boundary: Q21 uses the formal scoring PDF; the row uses only the contact/system-optimization angle, not selected-compulsory-three thinking labels.",
        f"- DOCX backup: `{Path(str(docx_info['docx_backup'])).name}`.",
        f"- Matrix backup: `{Path(str(matrix_info['matrix_backup'])).name}`.",
        f"- Ledger backup: `{Path(str(ledger_info['ledger_backup'])).name if ledger_info.get('ledger_backup') else 'NONE'}`.",
        f"- Matrix rows updated: `{len(matrix_info['updated_rows'])}`.",
        f"- Matrix rows added: `{len(matrix_info['added_rows'])}`.",
        "",
        "## Inserted Headings",
        "",
    ]
    for heading in docx_info["inserted_headings"]:
        lines.append(f"- `{heading}`")
    lines.extend([
        "",
        "## Open Gates",
        "",
        "- Render QA is required because the DOCX changed.",
        "- GPTPro web full artifact review remains `real_call_pending`.",
        "- Claude Opus web/app full artifact review remains `real_call_pending`; corrected route is direct `https://claude.ai` auto-login.",
        "- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
    ])
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_info = edit_docx(ts)
    ledger_info = update_ledger(ts, docx_info["inserted_headings"])
    matrix_info = update_matrix(ts)
    summary = write_report(ts, docx_info, ledger_info, matrix_info)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
