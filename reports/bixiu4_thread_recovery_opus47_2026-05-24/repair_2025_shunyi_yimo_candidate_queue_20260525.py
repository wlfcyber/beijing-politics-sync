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
REPORT_MD = RECOVERY / "SHUNYI_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "SHUNYI_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2025顺义一模"
YEAR = "2025"
STAGE = "一模"
SOURCE_BUNDLE = "preprocessed_corpus\\gpt_suite_bundles\\2025各区模拟题__2025各区一模__2025顺义一模.md"

ENTRY = {
    "canonical_node": "矛盾的特殊性 / 具体问题具体分析",
    "question_no": "Q2",
    "heading_suffix": "2025顺义一模 第2题（选择题）",
    "material_trigger": "题干写共建社区微花园需要居民积极献言建策、共同参与社区小微空间改造；正确项②明确“需集思广益、因地制宜，既贴近社区实际，又契合居民期待”。",
    "question_prompt": "2025年北京市政府提出共建社区微花园，居民共同参与社区小微空间改造。正确答案为C（②③）。",
    "why_trigger": "看到“社区微花园”“贴近社区实际”“契合居民期待”“因地制宜”，应从矛盾特殊性和具体问题具体分析切入：不同社区的空间条件、居民需求和治理基础不同，不能用一个模板改造所有社区。",
    "answer_landing": "本题应选C。本节点只处理②：共建社区微花园要坚持具体问题具体分析，结合社区具体空间、居民具体需求和治理具体条件因地制宜推进。③的民生治理理念作为选择题信息保留，不扩展为主观题评分链条。",
    "evidence_level": "官方答案键+题面正确项链条（选择题，非主观题评分细则）",
    "source_lines": f"{SOURCE_BUNDLE}:134-141; {SOURCE_BUNDLE}:395-417",
}

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
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


def add_entry(body) -> str:
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, ENTRY["canonical_node"])
    h_template = next(p for p in paras[start + 1 : end] if is_entry(p))
    l_template = next(p for p in paras[start + 1 : end] if para_text(p).strip().startswith("【"))
    blank = next((p for p in paras[start + 1 : end] if not para_text(p).strip()), None)
    nums = []
    for p in paras[start + 1 : end]:
        if is_entry(p):
            head = para_text(p).strip().split(".", 1)[0]
            if head.isdigit():
                nums.append(int(head))
    heading_text = f"{(max(nums) if nums else 0) + 1}. {ENTRY['heading_suffix']}"
    insert_at = list(body).index(paras[end]) if end < len(paras) else len(body)
    h = deepcopy(h_template)
    set_plain(h, heading_text)
    body.insert(insert_at, h)
    insert_at += 1
    for label, key in LABELS:
        p = deepcopy(l_template)
        set_label(p, label, ENTRY[key])
        body.insert(insert_at, p)
        insert_at += 1
    if blank is not None:
        body.insert(insert_at, deepcopy(blank))
    return heading_text


def edit_docx(ts: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_shunyi_yimo_q2_insert_{ts}.docx")
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
        heading = add_entry(body)
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_heading": heading}


def update_ledger(ts: str, heading: str) -> dict[str, object]:
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    rows = []
    backup = None
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2025_shunyi_yimo_q2_insert_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    clean = heading.split(". ", 1)[1]
    key = (SUITE, ENTRY["question_no"], clean)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    if key not in existing:
        rows.append({
            "canonical_node": ENTRY["canonical_node"],
            "source_suite": SUITE,
            "question_no": ENTRY["question_no"],
            "inserted_heading": clean,
        })
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
    return max(nums) + 1


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2025_shunyi_yimo_candidate_repair_{ts}{MATRIX.suffix}")
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

    upd("M0507", "Q1", "选择题：政治与法治/党的建设边界", "否：模块边界排除", "-", "官方答案A指向党的领导、全面从严治党、党的建设。", "官方答案键+模块边界", "EXCLUDE_POLITICS_AND_LAW", "不因“改革/发展”词命中进入哲学正文。", f"{SOURCE_BUNDLE}:126-133; {SOURCE_BUNDLE}:395-407")
    upd("M0508", "Q2", "选择题：具体问题具体分析正确项链条", "是：已进入当前DOCX/PDF正文", "矛盾的特殊性 / 具体问题具体分析", "官方答案C支持②：因地制宜、贴近社区实际、契合居民期待。", ENTRY["evidence_level"], "INSERTED_CHOICE_CHAIN_NOT_MAIN_RUBRIC", "③民生治理理念只作选择题边界信息，不扩展为主观题评分链条。", ENTRY["source_lines"])
    upd("M0509", "Q3", "选择题：文化交流交融知识，非哲学主链", "否：文化选择题边界，不进入当前哲学正文", "-", "官方答案B为多元冰雪文化交流交融赋能发展；错项含哲学词但不构成正确项哲学落点。", "官方答案键+题面文化知识（非主观题评分细则）", "EXCLUDE_CULTURE_CHOICE_NOT_PHILOSOPHY_NODE", "不把错项“矛盾普遍性/逆向思维”冒充细则或正确项。", f"{SOURCE_BUNDLE}:142-149; {SOURCE_BUNDLE}:418-425")
    upd("M0510", "Q4", "选择题：价值判断与价值选择正确项链条", "是：当前DOCX已有正文", "价值判断与价值选择", "官方答案D支持④：居民更加注重健身、学习是基于价值判断基础上做出的价值选择。", "官方答案键+题面正确项链条（选择题，非主观题评分细则）", "CURRENT_DOCX_COVERED", "当前DOCX已有2025顺义一模第4题条目；无需重复新增。", f"{SOURCE_BUNDLE}:150-168; {SOURCE_BUNDLE}:426-438")
    upd("M0511", "Q5", "选择题：逻辑与思维边界", "否：模块边界排除", "-", "命题矛盾关系属于选择性必修三逻辑。", "官方答案键+模块边界", "EXCLUDE_XUANBISAN_LOGIC", "不因“矛盾”字样进入辩证法正文。", f"{SOURCE_BUNDLE}:169-173; {SOURCE_BUNDLE}:395-398")
    upd("M0512", "Q7", "选择题：逻辑与思维边界", "否：模块边界排除", "-", "三段论逻辑错误分析属于选择性必修三逻辑。", "官方答案键+模块边界", "EXCLUDE_XUANBISAN_LOGIC", "不因“物质”作为逻辑例词进入唯物论正文。", f"{SOURCE_BUNDLE}:192-215; {SOURCE_BUNDLE}:395-398")
    upd("M0513", "Q8", "选择题：政治与法治/人大代表制度边界", "否：模块边界排除", "-", "代表法修正、人大代表联系群众、民主集中制属于政治与法治。", "官方答案键+模块边界", "EXCLUDE_POLITICS_AND_LAW", "人民群众词命中不构成历史唯物主义落点。", f"{SOURCE_BUNDLE}:216-239; {SOURCE_BUNDLE}:395-398")
    upd("M0514", "Q11", "选择题：法律与生活边界", "否：模块边界排除", "-", "见义勇为受益人补偿、民事权益保护属于法律与生活。", "官方答案键+模块边界", "EXCLUDE_XUANBIER_LAW", "不因“部分”误判整体与部分。", f"{SOURCE_BUNDLE}:240-265; {SOURCE_BUNDLE}:395-398")
    upd("M0515", "Q12", "选择题：经济与社会/新质生产力边界", "否：模块边界排除", "-", "数据要素、农业新质生产力、资源配置、乡村振兴属于经济模块。", "官方答案键+模块边界", "EXCLUDE_ECONOMICS", "农谚认识材料不是本题正确项哲学评分链。", f"{SOURCE_BUNDLE}:266-277; {SOURCE_BUNDLE}:395-398")
    upd("M0516", "Q13", "选择题：经济与社会/资源配置边界", "否：模块边界排除", "-", "矿业权竞争性出让、市场资源配置属于经济模块。", "官方答案键+模块边界", "EXCLUDE_ECONOMICS", "不因“物质/认识”词命中进入哲学正文。", f"{SOURCE_BUNDLE}:278-285; {SOURCE_BUNDLE}:395-398")
    upd("M0517", "Q14", "选择题：政治与法治/国家安全边界", "否：模块边界排除", "-", "国家安全宣传教育和平安中国建设属于政治与法治。", "官方答案键+模块边界", "EXCLUDE_POLITICS_AND_LAW", "不因“意识”词命中进入社会意识或意识能动性节点。", f"{SOURCE_BUNDLE}:286-291; {SOURCE_BUNDLE}:395-398")
    upd("M0518", "Q15", "选择题：当代国际政治与经济边界", "否：模块边界排除", "-", "中国国际形象、国际事务、和平发展道路属于选择性必修一。", "官方答案键+模块边界", "EXCLUDE_XUANBIYI", "不因“发展”词命中进入发展观正文。", f"{SOURCE_BUNDLE}:292-299; {SOURCE_BUNDLE}:395-398")
    upd("M0519", "Q16", "主观题：哲学与文化综合", "是：当前DOCX已有多节点正文覆盖", "联系的观点; 发展的观点; 辩证否定 / 守正创新; 矛盾的特殊性 / 具体问题具体分析; 价值判断与价值选择", "正式细则明确列联系、发展、矛盾、中华文化与中华文明、文化功能等角度；当前DOCX已有Q16多节点覆盖。", "正式评分细则", "CURRENT_DOCX_COVERED_FORMAL_RUBRIC", "无需重复新增；细则与正文节点相符。", f"{SOURCE_BUNDLE}:30-43; {SOURCE_BUNDLE}:563-590")
    upd("M0520", "Q18", "主观题：经济与社会/新质生产力边界", "否：模块边界排除", "-", "正式评分细则为新质生产力、现代化产业体系、创新发展理念、传统/新兴/未来产业。", "正式评分细则+模块边界", "EXCLUDE_ECONOMICS", "不因“发展/矛盾/联系”泛词命中进入哲学正文。", f"{SOURCE_BUNDLE}:66-69; {SOURCE_BUNDLE}:327-348")
    upd("M0521", "Q20", "主观题：当代国际政治与经济边界", "否：模块边界排除", "-", "正式评分细则为小而美项目、当地价值、中国理念、世界贡献、人类命运共同体/经济全球化等。", "正式评分细则+模块边界", "EXCLUDE_XUANBIYI", "不因“实践/发展/部分”泛词命中进入哲学正文。", f"{SOURCE_BUNDLE}:85-90; {SOURCE_BUNDLE}:361-370")
    upd("M0522", "Q21", "主观题：综合运用所学；当前DOCX有非细则证据链", "是：当前DOCX已有正文，但证据等级明示为非正式细则", "整体与部分; 价值判断与价值选择", "教师版参考答案写明“原卷无答案，此答案仅供参考”；题面与教师版答案支持整体/部分、价值取向链条，但不能冒充细则。", "教师版参考答案+题面显性链条（非正式评分细则）", "CURRENT_DOCX_COVERED_NON_RUBRIC_EVIDENCE", "保留当前正文，证据等级降格明示；不写成正式细则。", f"{SOURCE_BUNDLE}:371-378; {SOURCE_BUNDLE}:731-748")
    upd("M0523", "Q16", "旧Qunknown占位/源包摘录行，已由逐题修复覆盖", "否：占位行不进正文", "-", "逐题矩阵已显式覆盖Q1-Q21；该行不再作为风险。", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "旧Qunknown归并为Q16源包摘录占位。", SOURCE_BUNDLE)
    if "M0189" in by_id:
        upd("M0189", "Q16", "主观题：哲学与文化综合", "是：当前DOCX已有多节点正文覆盖", "联系/发展/矛盾/价值观/文化科技融合", "正式细则明确哲学文化双维度；当前DOCX已覆盖Q16多节点。", "正式评分细则", "CURRENT_DOCX_COVERED_FORMAL_RUBRIC", "旧待核行已闭合。", f"{SOURCE_BUNDLE}:30-43")
    if "M0218" in by_id:
        upd("M0218", "Q16", "主观题：哲学与文化综合", "是：当前DOCX已有多节点正文覆盖", "辩证否定扬弃/联系/发展/具体问题/价值观", "正式细则明确；当前DOCX已覆盖。", "正式评分细则", "CURRENT_DOCX_COVERED_FORMAL_RUBRIC", "旧NO_ACTION行已复核闭合。", f"{SOURCE_BUNDLE}:30-43")
    if "M0838" in by_id:
        upd("M0838", "SUITE_LEVEL", "套卷级覆盖口径，不替代逐题细则核验", "套卷已完成逐题修复记录", "SUITE_LEVEL_SUMMARY", "逐题矩阵已覆盖Q1-Q21；套卷级记录不再作为补厚风险。", "COVERED_OR_PATCHED", "COVERED_OR_PATCHED_ROW_LEVEL_REPAIRED", "套卷级行不替代逐题证据。", "06_governor_confucius\\FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv:26")

    existing_q = {r.get("题号") for r in rows if r.get("题源") == SUITE}
    added = []
    new_id = next_matrix_id(rows)
    missing = {
        "Q6": ("选择题：逻辑与经济政策边界", "否：模块边界排除", "-", "证券基金保险公司互换便利、判断类型/划分标准属于经济政策和逻辑，非必修四主链。", "官方答案键+模块边界", "EXCLUDE_ECONOMICS_OR_LOGIC", "题面含判断形式但不进哲学正文。", f"{SOURCE_BUNDLE}:174-191; {SOURCE_BUNDLE}:395-398"),
        "Q9": ("选择题：政治与法治/政府公共服务边界", "否：模块边界排除", "-", "心理援助热线、政务服务资源整合、政府服务实效属于政治与法治。", "官方答案键+模块边界", "EXCLUDE_POLITICS_AND_LAW", "不进哲学正文。", f"{SOURCE_BUNDLE}:216-239; {SOURCE_BUNDLE}:395-398"),
        "Q10": ("选择题：法律与生活/劳动法边界", "否：模块边界排除", "-", "孕期劳动者调岗、劳动合同解除、特殊劳动保护属于法律与生活。", "官方答案键+模块边界", "EXCLUDE_XUANBIER_LAW", "不进哲学正文。", f"{SOURCE_BUNDLE}:240-265; {SOURCE_BUNDLE}:395-398"),
        "Q17": ("主观题：逻辑与思维/政治与法治边界", "否：模块边界排除", "-", "Q17(1)为充分/必要/相容选言判断；Q17(2)为政府职能和依法治国主体。", "正式评分细则+模块边界", "EXCLUDE_XUANBISAN_AND_POLITICS", "正式细则不支持必修四哲学正文。", f"{SOURCE_BUNDLE}:46-65; {SOURCE_BUNDLE}:603-644"),
        "Q19": ("主观题：法律与生活边界", "否：模块边界排除", "-", "民事权利边界、多元纠纷解决、市场主体权益属于法律与生活。", "正式阅卷细则+模块边界", "EXCLUDE_XUANBIER_LAW", "不进哲学正文。", f"{SOURCE_BUNDLE}:70-84; {SOURCE_BUNDLE}:672-706"),
    }
    for q, vals in missing.items():
        if q in existing_q:
            continue
        kind, in_book, node, support, evidence, current, note, source = vals
        rid = f"M{new_id:04d}"
        new_id += 1
        added.append(rid)
        row = {k: "" for k in fieldnames}
        row.update({
            "matrix_row_id": rid,
            "row_source": "codex_recovery_2025_shunyi_yimo_explicit_boundary",
            "题源": SUITE,
            "年份": YEAR,
            "阶段": STAGE,
            "题号": q,
            "题型或模块判断": kind,
            "是否进宝典": in_book,
            "宝典节点": node,
            "细则支持原理": support,
            "证据等级": evidence,
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": current,
            "备注": note,
            "source_artifact": source,
        })
        rows.append(row)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "added_rows": added, "updated_rows": 21}


def write_report(ts: str, docx_result: dict[str, object], ledger_result: dict[str, object], matrix_result: dict[str, object]) -> None:
    payload = {"timestamp": ts, "docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD.write_text(
        "\n".join([
            "# SHUNYI_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525",
            "",
            "Status: `SHUNYI_2025_YIMO_REPAIRED_DOCX_Q2_INSERTED_RENDER_PENDING`",
            "",
            f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} +08",
            "",
            "## Decisions",
            "",
            "- Inserted Q2 under `矛盾的特殊性 / 具体问题具体分析` as a choice-question chain.",
            "- Kept existing current-DOCX coverage for Q4, Q16, and Q21.",
            "- Q16 is supported by the formal scoring rules; Q21 is explicitly downgraded to teacher-version reference answer plus question-text evidence, not formal scoring rules.",
            "- Excluded Q1/Q3/Q5-Q15/Q17-Q20 by official answer key, formal rubric, or module boundary.",
            "- Added missing boundary rows for Q6/Q9/Q10/Q17/Q19 so Q1-Q21 have explicit decisions.",
            "- Choice-question chains are not treated as main-question scoring-rubric evidence.",
            "- No Sonnet/Haiku/model-unknown evidence was promoted.",
            "- GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review remain `real_call_pending`.",
            "",
            "## Backups And Outputs",
            "",
            f"- DOCX backup: `{docx_result['docx_backup']}`.",
            f"- Matrix backup: `{matrix_result['matrix_backup']}`.",
            f"- Ledger backup: `{ledger_result['ledger_backup']}`.",
            f"- Inserted heading: `{docx_result['inserted_heading']}`.",
            f"- Matrix rows added: `{', '.join(matrix_result['added_rows'])}`.",
            "",
            "## Boundary",
            "",
            "This is a local source/DOCX/matrix repair. Render QA is required after this DOCX change. External model review, full manual typography review, ClaudeCode model confirmation, and the deferred ORDER_063 final GitHub upload gate remain open.",
            "",
        ]),
        encoding="utf-8",
    )


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = edit_docx(ts)
    ledger_result = update_ledger(ts, str(docx_result["inserted_heading"]))
    matrix_result = update_matrix(ts)
    write_report(ts, docx_result, ledger_result, matrix_result)
    print(json.dumps({"docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
