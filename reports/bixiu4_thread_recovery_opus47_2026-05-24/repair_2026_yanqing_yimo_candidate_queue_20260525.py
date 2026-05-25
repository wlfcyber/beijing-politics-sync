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
REPORT_MD = RECOVERY / "YANQING_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "YANQING_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
UPLOAD_SCOPE = RECOVERY / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"

SUITE = "2026延庆一模"
YEAR = "2026"
STAGE = "一模"
SOURCE_BUNDLE = "preprocessed_corpus\\gpt_suite_bundles\\2026各区模拟题__2026各区一模__2026延庆一模.md"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

ENTRIES = [
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q2",
        "heading_suffix": "2026延庆一模 第2题（选择题）",
        "material_trigger": "题干列举机械臂、智能客服等人工智能应用；正确项③写明“人工智能的应用是意识能动作用的体现，推动劳动向智能化、高效化转型”。",
        "question_prompt": "在人工智能广泛应用于生产生活领域的当下，许多传统劳动任务部分或全部由智能机器替代执行。正确答案为D（③④）。",
        "why_trigger": "人工智能不是自然自发出现的力量，而是人把目的、算法、工具系统对象化之后形成的技术应用。看到“推动劳动向智能化、高效化转型”，应想到意识活动具有目的性、能动创造性，并能通过实践改造客观世界。",
        "answer_landing": "本题应选D。本节点只处理③：人工智能应用体现人发挥意识能动作用，把人的目的、知识和技术方案转化为智能化生产生活实践，推动劳动方式升级。④作为劳动分工信息保留为选择题边界，不扩展为主观题评分链条。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:178-185; {SOURCE_BUNDLE}:440-442",
    },
    {
        "canonical_node": "矛盾的特殊性 / 具体问题具体分析",
        "question_no": "Q3",
        "heading_suffix": "2026延庆一模 第3题（选择题）",
        "material_trigger": "题干写各地立足自身资源优势，探索各具特色的乡村发展模式；正确项①明确“具体问题具体分析是解决问题的关键，要因地制宜”。",
        "question_prompt": "乡村振兴中各地立足资源优势，同时国家统筹基础设施和统一销售平台。正确答案为A（①③）。",
        "why_trigger": "看到“各地立足自身资源优势”“各具特色”“因地制宜”，应从矛盾特殊性和具体问题具体分析切入，而不是套用单一乡村发展模板。",
        "answer_landing": "本题应选A。本节点只处理①：乡村振兴必须分析不同地区资源禀赋、产业条件和发展阶段的特殊性，坚持具体问题具体分析，因地制宜选择发展路径。③的整体统筹信息另作矩阵记录，不扩展为主观题评分链条。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:186-194; {SOURCE_BUNDLE}:440-442",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q4",
        "heading_suffix": "2026延庆一模 第4题（选择题）",
        "material_trigger": "老墙承载集体记忆与社区文化，但居民围绕安全、美观、记忆保护产生不同判断；正确项①支持价值判断具有主体差异性。",
        "question_prompt": "老旧小区改造中是否拆除30年老墙产生争议，社区决定保留主体并微改造。正确答案为A（①②）。",
        "why_trigger": "不同居民从安全、美观、历史记忆、社区文化等不同需要出发作出判断，说明价值判断会受主体需要、立场和认识条件影响。",
        "answer_landing": "本题应选A。本节点只处理①：不同居民围绕老墙作出不同价值判断，体现价值判断具有主体差异性；社区通过协商兼顾安全与记忆，是在多元价值诉求中作出更符合公共利益的价值选择。②的肯定/否定关系作为选择题信息保留，不冒充主观题评分细则。",
        "evidence_level": "官方答案键+题干正确项链条（选择题，非主观题评分细则）",
        "source_lines": f"{SOURCE_BUNDLE}:199-207; {SOURCE_BUNDLE}:440-442",
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


def add_entry(body, entry: dict[str, str]) -> str:
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
    heading_text = f"{(max(nums) if nums else 0) + 1}. {entry['heading_suffix']}"
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_yanqing_yimo_choice_insert_{ts}.docx")
    shutil.copy2(docx, backup)
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        xml_path = temp / "word" / "document.xml"
        tree = etree.parse(str(xml_path))
        body = tree.getroot().find("w:body", namespaces=NS)
        if body is None:
            raise RuntimeError("missing body")
        inserted = [add_entry(body, e) for e in ENTRIES]
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted}


def update_ledger(ts: str, headings: list[str]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_yanqing_yimo_choice_insert_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for entry, heading in zip(ENTRIES, headings, strict=True):
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


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_yanqing_yimo_candidate_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    by_id = {r["matrix_row_id"]: r for r in rows}

    def upd(row_id: str, q: str, kind: str, in_book: str, node: str, support: str, evidence: str, current: str, note: str, source: str, mis: str = "否", thick: str = "否") -> None:
        by_id[row_id].update({
            "题源": SUITE, "年份": YEAR, "阶段": STAGE, "题号": q, "题型或模块判断": kind,
            "是否进宝典": in_book, "宝典节点": node, "细则支持原理": support, "证据等级": evidence,
            "是否误放": mis, "是否需补厚": thick, "当前处理": current, "备注": note, "source_artifact": source,
        })

    upd("M0550", "Q2", "选择题：意识能动作用正确项链条", "是：已进入当前DOCX/PDF正文", "主观能动性 / 意识的能动作用", "官方答案D支持③：AI应用体现意识能动作用，推动劳动智能化高效化。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", "INSERTED_CHOICE_CHAIN_NOT_MAIN_RUBRIC", "只作选择题挂点，④劳动分工信息不扩展。", f"{SOURCE_BUNDLE}:178-185; {SOURCE_BUNDLE}:440-442")
    upd("M0551", "Q3", "选择题：具体问题具体分析/整体部分正确项链条", "是：已进入当前DOCX/PDF正文", "矛盾的特殊性 / 具体问题具体分析", "官方答案A支持①③；正文补①，③作为矩阵支持记录。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", "INSERTED_CHOICE_CHAIN_NOT_MAIN_RUBRIC", "选择题边界已明示。", f"{SOURCE_BUNDLE}:186-194; {SOURCE_BUNDLE}:440-442")
    upd("M0552", "Q4", "选择题：价值判断主体差异正确项链条", "是：已进入当前DOCX/PDF正文", "价值判断与价值选择", "官方答案A支持①②；正文补①，②作为选择题信息记录。", "官方答案键+题干正确项链条（选择题，非主观题评分细则）", "INSERTED_CHOICE_CHAIN_NOT_MAIN_RUBRIC", "选择题边界已明示。", f"{SOURCE_BUNDLE}:199-207; {SOURCE_BUNDLE}:440-442")
    upd("M0553", "Q5", "选择题：选必三科学思维边界", "否：候选线已判边界排除", "-", "官方答案C指向科学思维追求认识客观性，属于选必三。", "官方答案键+模块边界", "EXCLUDE_XUANBISAN", "不因认识词命中进入必修四正文。", f"{SOURCE_BUNDLE}:208-215; {SOURCE_BUNDLE}:440-442")
    upd("M0554", "Q7", "选择题：逻辑思维边界", "否：候选线已判边界排除", "-", "AIGC概念、反对关系、推理规则属于选必三逻辑。", "官方答案键+模块边界", "EXCLUDE_XUANBISAN_LOGIC", "不因发展词命中进入必修四正文。", f"{SOURCE_BUNDLE}:226-232; {SOURCE_BUNDLE}:440-442")
    upd("M0555", "Q10", "选择题：政治与法治/民族区域自治边界", "否：候选线已判边界排除", "-", "西藏自治区、党的领导、民族区域自治属于政治与法治。", "官方答案键+模块边界", "EXCLUDE_POLITICS_AND_LAW", "不因意识词命中进入必修四正文。", f"{SOURCE_BUNDLE}:251-258; {SOURCE_BUNDLE}:440-442")
    upd("M0556", "Q12", "选择题：经济与社会边界", "否：候选线已判边界排除", "-", "投资于人、财政公共资源、人力资本属于经济模块。", "官方答案键+模块边界", "EXCLUDE_ECONOMICS", "不因发展词命中进入必修四正文。", f"{SOURCE_BUNDLE}:266-277; {SOURCE_BUNDLE}:440-442")
    upd("M0557", "Q13", "选择题：经济高质量发展边界", "否：候选线已判边界排除", "-", "现代产业体系、区域绿色转型、比较优势属于经济模块。", "官方答案键+模块边界", "EXCLUDE_ECONOMICS", "不因系统/发展词命中进入必修四正文。", f"{SOURCE_BUNDLE}:278-285; {SOURCE_BUNDLE}:440-442")
    upd("M0558", "Q14", "选择题：对外开放/经济路径边界", "否：候选线已判边界排除", "-", "制度型开放、外资服务保障、营商环境属于经济/国际经济边界。", "官方答案键+模块边界", "EXCLUDE_ECONOMICS_OR_XUANBIYI", "不因发展词命中进入必修四正文。", f"{SOURCE_BUNDLE}:286-291; {SOURCE_BUNDLE}:440-442")
    upd("M0559", "Q15", "选择题：APEC/国际政治经济边界", "否：候选线已判边界排除", "-", "APEC成员多样性、区域经济一体化属于选必一。", "官方答案键+模块边界", "EXCLUDE_XUANBIYI", "不因部分词命中进入必修四正文。", f"{SOURCE_BUNDLE}:292-299; {SOURCE_BUNDLE}:440-442")
    upd("M0560", "Q16", "主观题：必修四哲学文化综合", "是：已进入当前DOCX/PDF正文", "辩证否定 / 守正创新; 矛盾就是对立统一; 矛盾的特殊性 / 具体问题具体分析; 社会存在与社会意识; 人民群众", "正式细则列矛盾观、群众观点、矛盾特殊性、辩证否定、文化传承创新等；当前DOCX已有对应节点。", "正式评分细则", "CURRENT_DOCX_COVERED", "无需新增正文。", f"{SOURCE_BUNDLE}:58-80; {SOURCE_BUNDLE}:302-320")
    upd("M0561", "Q17", "主观题：政治与法治边界", "否：候选线已判边界排除", "-", "正式细则为政府治理、依法行政、职能科学、智能高效。", "正式评分细则+模块边界", "EXCLUDE_POLITICS_AND_LAW", "不因系统词命中进入必修四正文。", f"{SOURCE_BUNDLE}:81-87; {SOURCE_BUNDLE}:321-332")
    upd("M0562", "Q18", "主观题：法律与生活/逻辑与思维边界", "否：候选线已判边界排除", "-", "Q18(1)为肖像权、名誉权、消费者权益、不正当竞争；Q18(2)为逻辑与思维。", "正式评分细则+模块边界", "EXCLUDE_XUANBIER_AND_XUANBISAN", "不进入必修四正文。", f"{SOURCE_BUNDLE}:88-107; {SOURCE_BUNDLE}:333-366")
    upd("M0563", "Q19", "主观题：经济与社会/当代国际政治经济边界", "否：候选线已判边界排除", "-", "Q19(1)经济高质量发展，Q19(2)国家利益/国际合作/全球治理。", "正式评分细则+模块边界", "EXCLUDE_ECONOMICS_AND_XUANBIYI", "不因实践/改革/系统词命中进入必修四正文。", f"{SOURCE_BUNDLE}:109-130; {SOURCE_BUNDLE}:367-422")
    upd("M0564", "Q20", "主观题：必修四哲学综合", "是：已进入当前DOCX/PDF正文", "尊重客观规律与发挥主观能动性相结合; 规律的客观性; 发展的观点 / 发展的普遍性; 量变与质变 / 适度原则; 矛盾就是对立统一; 矛盾的主要方面和次要方面; 两点论与重点论", "正式细则明确可用发展观、规律、矛盾观、发挥主观能动性等必修四角度；当前DOCX已有多节点覆盖。", "正式评分细则", "CURRENT_DOCX_COVERED", "无需新增正文。", f"{SOURCE_BUNDLE}:132-145; {SOURCE_BUNDLE}:423-434")
    upd("M0565", "Q20", "主观题：必修四哲学综合去重行", "是：已进入当前DOCX/PDF正文", "Q20多节点正文覆盖", "由正式细则Q20与当前DOCX上下文闭合；旧Qunknown行改为Q20去重记录。", "正式评分细则", "CURRENT_DOCX_COVERED_DUPLICATE_ROW_NORMALIZED", "旧Qunknown已归并。", f"{SOURCE_BUNDLE}:132-145; {SOURCE_BUNDLE}:423-434")
    upd("M0168", "Q16", "主观题：必修四哲学文化综合", "是：已进入当前DOCX/PDF正文", "Q16多节点正文覆盖", "正式细则存在，并非参考答案无细则；当前DOCX覆盖矛盾观、群众观点、辩证否定、社会意识等。", "正式评分细则", "CURRENT_DOCX_COVERED", "纠正旧备注。", f"{SOURCE_BUNDLE}:58-80; {SOURCE_BUNDLE}:302-320")
    upd("M0221", "Q待定", "旧待定占位行，已由逐题修复覆盖", "否：占位行不进正文", "-", "逐题矩阵已补齐显式决策。", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "占位行不再作为风险。", SOURCE_BUNDLE)
    upd("M0860", "SUITE_LEVEL", "套卷级覆盖口径，已由逐题修复覆盖", "套卷有最终DOCX提及或闭合记录", "SUITE_LEVEL_SUMMARY_SUPERSEDED", "逐题矩阵已补齐Q1-Q20决策；套卷级行不替代逐题细则核验。", "COVERED_OR_PATCHED", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "不再作为风险行。", SOURCE_BUNDLE)

    existing = {(r["题源"], r["题号"]) for r in rows}
    next_id = max(int(r["matrix_row_id"][1:]) for r in rows if r["matrix_row_id"].startswith("M")) + 1
    added = []

    def add(q: str, kind: str, support: str, current: str, source: str) -> None:
        nonlocal next_id
        row = {name: "" for name in fieldnames}
        row.update({
            "matrix_row_id": f"M{next_id:04d}", "row_source": "codex_recovery_2026_yanqing_yimo_explicit_boundary",
            "题源": SUITE, "年份": YEAR, "阶段": STAGE, "题号": q, "题型或模块判断": kind,
            "是否进宝典": "否：候选线已判边界排除", "宝典节点": "-", "细则支持原理": support,
            "证据等级": "官方答案键/题干+模块边界", "是否误放": "否：未进正文", "是否需补厚": "否",
            "当前处理": current, "备注": "补齐Q1-Q20显式决策。", "source_artifact": source,
        })
        rows.append(row); added.append(row["matrix_row_id"]); next_id += 1

    missing = [
        ("Q1", "选择题：中国特色社会主义/党史边界", "抗战胜利、中国共产党中流砥柱、民族复兴属于必修一/政治史。", "EXCLUDE_NON_BIXIU4", f"{SOURCE_BUNDLE}:169-177; {SOURCE_BUNDLE}:440-442"),
        ("Q6", "选择题：逻辑推理边界", "海南封关条件推理属于选必三逻辑。", "EXCLUDE_XUANBISAN_LOGIC", f"{SOURCE_BUNDLE}:216-225; {SOURCE_BUNDLE}:440-442"),
        ("Q8", "选择题：法律与生活边界", "共用暖气管、共有财产/相邻权属于法律模块。", "EXCLUDE_XUANBIER", f"{SOURCE_BUNDLE}:233-243; {SOURCE_BUNDLE}:440-442"),
        ("Q9", "选择题：民法/未成年人保护边界", "限制民事行为能力、合同无效、家庭保护属于法律模块。", "EXCLUDE_XUANBIER", f"{SOURCE_BUNDLE}:244-250; {SOURCE_BUNDLE}:440-442"),
        ("Q11", "选择题：法治中国边界", "全民普法、依法治国、法治信仰属于政治与法治。", "EXCLUDE_POLITICS_AND_LAW", f"{SOURCE_BUNDLE}:259-265; {SOURCE_BUNDLE}:440-442"),
    ]
    for item in missing:
        if (SUITE, item[0]) not in existing:
            add(*item)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "added_rows": added, "updated_rows": 19}


def append(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    path.write_text(old.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def write_reports(ts: str, docx_result: dict[str, object], ledger_result: dict[str, object], matrix_result: dict[str, object]) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")
    report = f"""
# YANQING_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `YANQING_2026_YIMO_REPAIRED_DOCX_Q2_Q3_Q4_INSERTED_RENDER_PENDING`

Updated: {now}

## Decisions

- Inserted Q2 under `主观能动性 / 意识的能动作用` as a choice-question chain.
- Inserted Q3 under `矛盾的特殊性 / 具体问题具体分析` as a choice-question chain.
- Inserted Q4 under `价值判断与价值选择` as a choice-question chain.
- Kept existing current-DOCX coverage for Q16 and Q20 formal-rubric main-question nodes.
- Excluded Q1/Q5-Q15/Q17-Q19 by official answer key, formal rubric, or module boundary.
- Added missing boundary rows for Q1/Q6/Q8/Q9/Q11 so Q1-Q20 have explicit decisions.
- Choice-question chains are not treated as main-question scoring-rubric evidence.
- No Sonnet/Haiku/model-unknown evidence was promoted.
- GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review remain `real_call_pending`.

## Backups And Outputs

- DOCX backup: `{docx_result['docx_backup']}`.
- Matrix backup: `{matrix_result['matrix_backup']}`.
- Ledger backup: `{ledger_result['ledger_backup']}`.
- Inserted headings: `{'; '.join(docx_result['inserted_headings'])}`.
- Matrix rows added: `{', '.join(matrix_result['added_rows'])}`.

## Boundary

This is a local source/DOCX/matrix repair. Render QA is required after this DOCX change. External model review, full manual typography review, ClaudeCode model confirmation, and the deferred ORDER_063 final GitHub upload gate remain open.
"""
    REPORT_MD.write_text(report.strip() + "\n", encoding="utf-8")
    REPORT_JSON.write_text(json.dumps({"timestamp": ts, "docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for path, section in [
        (GOVERNOR, "Governor Finding"),
        (CONFUCIUS, "Artifact Check"),
        (STATUS, "Yanqing 2026 Yimo Recovery Repair"),
    ]:
        append(path, f"""
## {section}: Yanqing 2026 Yimo Candidate Queue Repair
Updated: {now}

- Status: `YANQING_2026_YIMO_DOCX_REPAIRED_RENDER_PENDING_MODEL_GATES_OPEN`.
- Q2/Q3/Q4 choice chains were inserted into current DOCX and registered in `docx_insert_ledger.csv`.
- Q16 and Q20 existing current-DOCX formal-rubric coverage was retained.
- Matrix was rewritten for 2026延庆一模 with explicit Q1-Q20 decisions and missing Q1/Q6/Q8/Q9/Q11 boundary rows.
- Render QA is required after this DOCX change.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""")
    append(UPLOAD_SCOPE, f"""
## Deferred Upload Scope Addition: 2026延庆一模 Repair
Updated: {now}

- Include `YANQING_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`, `YANQING_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json`, `repair_2026_yanqing_yimo_candidate_queue_20260525.py`, updated matrix/ledger, current DOCX/PDF after render QA, and refreshed Governor/Confucius/status/render QA files in future ORDER_063 upload scope.
- Upload still deferred; no push before all active Beijing politics lines reach terminal/user-approved states and secret scan records `NO_SECRET_PATTERN_MATCHES`.
""")
    append(MODEL_LEDGER, f"""
## MODEL_GATE_SUMMARY_AFTER_YANQING_2026_YIMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- 2026延庆一模 repair was performed by local cached source bundle, formal rubric/source review, current DOCX insertion, and matrix rewrite.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local repair.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`.
- GPTPro web full artifact review remains `real_call_pending`.
- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = edit_docx(ts)
    ledger_result = update_ledger(ts, docx_result["inserted_headings"])
    matrix_result = update_matrix(ts)
    write_reports(ts, docx_result, ledger_result, matrix_result)
    print(json.dumps({"docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
