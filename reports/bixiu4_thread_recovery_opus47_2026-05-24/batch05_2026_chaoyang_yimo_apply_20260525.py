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
BLOCKED = RUN / "04_fusion_audit" / "student_patch_entries.blocked.jsonl"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
SUITE = "2026朝阳一模"

QUESTION_1 = (
    "实干，是中国共产党人的鲜明特质，是成就事业的必由之路，是破解难题的根本途径。"
    "从延安时期“自己动手、丰衣足食”到新中国成立后“自力更生、艰苦奋斗”，"
    "从改革开放“大胆地试、勇敢地改”到新时代脱贫攻坚战“不获全胜、决不收兵”，"
    "一切伟大的成就都是党和人民一道拼出来、干出来的。下列说法正确的是（    ）"
    "①“自己动手、丰衣足食”坚持了从边区的实际出发，有利于抗日战争取得胜利；"
    "②“自力更生、艰苦奋斗”反映了对外贸易环境条件的变化，构建了新发展格局；"
    "③“大胆地试、勇敢地改”印证了决心和勇气是想问题、作决策、办事情的出发点；"
    "④“不获全胜、决不收兵”要求“务实”的作为，脚踏实地、埋头苦干、久久为功。"
)

QUESTION_2 = (
    "中国艺术以“古意”为崇高审美理想。在一定程度上，古意就是本初、朴素之意。"
    "传统艺术中与“古”相关的很多概念，与这种古意有关。如古澹，强调以淡然本真之怀面世，"
    "克制人追求主观目的的冲动；古朴，形容一种朴实自然的格调；浑古，强调超越知识分别的"
    "无时间境界；高古，一种与永恒同在的非时空境界，等等。对此，下列说法正确的是（    ）"
)

QUESTION_3 = (
    "非遗变脸与机械武术同台演绎，自制旋转木马讲解力学原理，机器人乐队、科普实验轮番亮相……"
    "某地以春节科普活动为契机，实现“科普+文化”“科普+非遗”相融合，让观众在感受年味的同时，"
    "轻松读懂传统文化背后的科学密码。这体现出（    ）①春节成为全民科学素养提升的主阵地和文化传播的新平台；"
    "②科普让科学精神融入日常生活，让文化自信浸润中华大地；③只有抓住主要矛盾，才能实现民族文化与外来文化的交融；"
    "④坚持辩证否定，可以使传统文化在科技赋能下焕发新的光彩。"
)

ENTRIES = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q1",
        "heading_suffix": "2026朝阳一模 第1题（选择题）",
        "material_trigger": "题干把延安时期“自己动手、丰衣足食”同当时边区条件联系起来，选项①明确说要“从边区的实际出发”。",
        "question_prompt": QUESTION_1,
        "why_trigger": "能想到一切从实际出发，是因为“自己动手、丰衣足食”不是抽象口号，而是在边区物资条件、抗战任务和群众生产生活条件下形成的具体做法。学生看到“从边区的实际出发”时，应当抓住主观方案必须符合客观实际这一哲学信号。",
        "answer_landing": "本题应选B。本节点处理①：延安时期开展“自己动手、丰衣足食”，是从边区的具体条件和抗战实际出发，把主观奋斗目标同客观现实条件统一起来；这说明想问题、作决策、办事情要坚持一切从实际出发、实事求是。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026朝阳一模 source bundle lines 25-36 and 365-400: Q1=B, ①④正确。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q1",
        "heading_suffix": "2026朝阳一模 第1题（选择题）",
        "material_trigger": "题干反复写“实干”“拼出来、干出来”，选项④又要求“务实”的作为，脚踏实地、埋头苦干、久久为功。",
        "question_prompt": QUESTION_1,
        "why_trigger": "能想到实践观，是因为材料把事业成就和难题破解落到真实行动上，而不是落到空谈、愿望或单纯决心上。学生看到“实干”“拼出来、干出来”“脚踏实地”这一组动词时，应当抓住实践是改造客观世界的活动，是成就事业的根本路径。",
        "answer_landing": "本题应选B。本节点处理④：脱贫攻坚“不获全胜、决不收兵”要求把认识和目标落实为务实行动，通过脚踏实地、埋头苦干、久久为功的实践推动事业发展；这说明实践不是口号，而是破解难题、创造伟大成就的现实活动。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026朝阳一模 source bundle lines 25-36 and 365-400: Q1=B, ①④正确。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q2",
        "heading_suffix": "2026朝阳一模 第2题（选择题）",
        "material_trigger": "题干解释“古澹”强调以淡然本真之怀面世，克制人追求主观目的的冲动；选项A把这种审美取向概括为价值观的导向作用。",
        "question_prompt": QUESTION_2,
        "why_trigger": "能想到价值观导向作用，是因为“古澹”并非只描述艺术形式，而是在引导人如何看待功利、欲望和本真生活。学生看到审美理想影响人的判断、选择和行为取向时，应当抓住价值观对认识世界和改造世界具有导向作用。",
        "answer_landing": "本题应选A。古澹所强调的看淡功利、克制冲动，是一种审美价值取向对人的认识和行为的引导；它说明价值观会影响人们怎样评价事物、怎样选择生活态度和艺术追求。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026朝阳一模 source bundle lines 37-44 and 365-400: Q2=A。",
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q3",
        "heading_suffix": "2026朝阳一模 第3题（选择题）",
        "material_trigger": "题干写非遗变脸、传统文化与机械武术、旋转木马、机器人乐队、科普实验相结合，选项④明确说坚持辩证否定能使传统文化在科技赋能下焕发新的光彩。",
        "question_prompt": QUESTION_3,
        "why_trigger": "能想到辩证否定，是因为材料不是把非遗和传统文化原样保存，也不是用科技替代传统文化，而是在保留文化根脉的基础上加入科普和技术表达。学生看到“科普+文化”“科普+非遗”“科技赋能传统文化”时，应当抓住继承与创新相统一、守正与创新相结合。",
        "answer_landing": "本题应选D。本节点处理④：非遗和传统文化在科技赋能下获得新的展示方式，说明辩证否定不是简单抛弃旧事物，而是在保留传统文化合理内核的基础上进行创造性转化、创新性发展，使传统文化焕发新光彩。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026朝阳一模 source bundle lines 45-55 and 365-400: Q3=D, ②④正确；②为文化线，当前哲学正文只处理④。",
    },
]

SECTION_NEXT = {
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
    "实践与认识（总）": "实践是认识的基础",
    "价值观的导向作用": "价值判断与价值选择",
    "辩证否定 / 守正创新": "矛盾就是对立统一",
}

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]


def current_docx() -> Path:
    docs = [
        p for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
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
    p.append(make_run(" " + rest, label=False))
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
    end = next(
        (i for i in range(start + 1, len(paras)) if para_text(paras[i]).strip() == next_heading),
        None,
    )
    if end is None:
        raise RuntimeError(f"next heading not found after {heading}: {next_heading}")
    return start, end


def insert_entry(root: etree._Element, entry: dict[str, str]) -> str:
    body = root.find("w:body", namespaces=NS)
    if body is None:
        raise RuntimeError("word/document.xml has no body")
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_chaoyang_yimo_batch05_{timestamp}.docx")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        data = {info.filename: zin.read(info.filename) for info in infos}
    root = etree.fromstring(data["word/document.xml"])
    headings = [insert_entry(root, entry) for entry in ENTRIES]
    data["word/document.xml"] = etree.tostring(root, encoding="UTF-8", xml_declaration=True, standalone=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
        for info in infos:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.comment = info.comment
            zi.extra = info.extra
            zi.internal_attr = info.internal_attr
            zi.external_attr = info.external_attr
            zi.create_system = info.create_system
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, data[info.filename])
    shutil.move(str(tmp_path), docx)
    print(f"DOCX_BACKUP={backup}")
    return headings


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"docx_insert_ledger_backup_before_batch05_chaoyang_yimo_{timestamp}.csv")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if not fieldnames:
        raise RuntimeError("ledger has no header")
    existing = {
        (r["canonical_node"], r["source_suite"], r["question_no"], r["inserted_heading"])
        for r in rows
    }
    for entry, heading in zip(ENTRIES, headings):
        row = {
            "canonical_node": entry["canonical_node"],
            "source_suite": SUITE,
            "question_no": entry["question_no"],
            "inserted_heading": heading,
        }
        key = (row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in existing:
            rows.append(row)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"LEDGER_BACKUP={backup}")


def update_accepted(timestamp: str) -> None:
    backup = ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch05_chaoyang_yimo_{timestamp}.jsonl")
    shutil.copy2(ACCEPTED, backup)
    items = []
    if ACCEPTED.exists():
        for line in ACCEPTED.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                items.append(json.loads(line))
    existing = {
        (i.get("source_suite"), i.get("question_no"), i.get("canonical_node"), i.get("material_trigger"))
        for i in items
    }
    for entry in ENTRIES:
        item = {
            "source_suite": SUITE,
            "question_no": entry["question_no"],
            "framework_node": entry["canonical_node"],
            "canonical_node": entry["canonical_node"],
            "material_trigger": entry["material_trigger"],
            "question_prompt": entry["question_prompt"],
            "why_trigger": entry["why_trigger"],
            "answer_landing": entry["answer_landing"],
            "evidence_level": entry["evidence_level"],
            "boundary_note": entry["source_lines"],
            "source_lane": "Codex Batch05 2026朝阳一模",
            "source_repair_basis": entry["source_lines"],
        }
        key = (item["source_suite"], item["question_no"], item["canonical_node"], item["material_trigger"])
        if key not in existing:
            items.append(item)
    ACCEPTED.write_text("\n".join(json.dumps(i, ensure_ascii=False) for i in items) + "\n", encoding="utf-8")
    print(f"ACCEPTED_BACKUP={backup}")


def update_blocked_metadata(timestamp: str) -> None:
    if not BLOCKED.exists():
        return
    backup = BLOCKED.with_name(f"student_patch_entries.blocked_backup_before_batch05_chaoyang_yimo_{timestamp}.jsonl")
    shutil.copy2(BLOCKED, backup)
    items = []
    for line in BLOCKED.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        if item.get("source_suite") == SUITE and item.get("question_no") == "Q16":
            node = item.get("canonical_node")
            if node == "尊重客观规律与发挥主观能动性相结合":
                item["evidence_level"] = "正式阅卷细则必答角度"
                item["boundary_note"] = "正式阅卷细则第16题必答角度①，3分。"
            elif node == "中华优秀传统文化的特点-文化自信":
                item["evidence_level"] = "正式阅卷细则必答角度"
                item["boundary_note"] = "正式阅卷细则第16题必答角度②，2分；文化线，不进入当前哲学主线。"
            elif node == "系统观念 / 系统优化":
                item["evidence_level"] = "正式阅卷细则选答角度"
                item["boundary_note"] = "正式阅卷细则列入哲学类选答角度：联系观/系统优化，累计不超过3分。"
            elif node == "矛盾的普遍性和特殊性":
                item["evidence_level"] = "教师版参考答案+正式阅卷细则宽角度"
                item["boundary_note"] = "教师版参考答案写矛盾普遍性与特殊性；正式阅卷细则只宽列对立统一选答角度，不标为逐点强细则。"
            elif node == "实践是认识的基础":
                item["evidence_level"] = "正式阅卷细则选答角度"
                item["boundary_note"] = "正式阅卷细则列入哲学类选答角度：认识论/实践与认识，累计不超过3分。"
        items.append(item)
    BLOCKED.write_text("\n".join(json.dumps(i, ensure_ascii=False) for i in items) + "\n", encoding="utf-8")
    print(f"BLOCKED_BACKUP={backup}")


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch05_2026_chaoyang_yimo_{timestamp}.csv"
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if not fieldnames:
        raise RuntimeError("matrix has no header")

    fields = {
        "id": "matrix_row_id",
        "in": "是否进宝典",
        "node": "宝典节点",
        "rule": "细则支持原理",
        "ev": "证据等级",
        "mis": "是否误放",
        "need": "是否需补厚",
        "action": "当前处理",
        "note": "备注",
    }
    inserted = {}
    for entry, heading in zip(ENTRIES, headings):
        inserted.setdefault(entry["question_no"], []).append((entry["canonical_node"], heading, entry["source_lines"]))

    def set_row(row: dict[str, str], status: str, node: str, rule: str, ev: str, mis: str, need: str, action: str, note: str) -> None:
        row[fields["in"]] = status
        row[fields["node"]] = node
        row[fields["rule"]] = rule
        row[fields["ev"]] = ev
        row[fields["mis"]] = mis
        row[fields["need"]] = need
        row[fields["action"]] = action
        old = row.get(fields["note"], "")
        row[fields["note"]] = f"{old}；{note}" if old else note

    updates = {
        "M0053": ("母版已覆盖：本轮不重复新增", "尊重客观规律与发挥主观能动性相结合", "正式阅卷细则第16题必答角度①，3分。", "正式阅卷细则必答角度", "否", "否", "Batch05核验：现有正文保留。"),
        "M0054": ("否：文化线边界，不进哲学主线", "中华优秀传统文化的特点-文化自信", "正式阅卷细则第16题必答角度②，2分；文化核心考点。", "正式阅卷细则必答角度", "否：按边界排除", "否", "Batch05核验：文化线边界保留。"),
        "M0055": ("母版已覆盖：本轮不重复新增", "系统观念 / 系统优化", "正式阅卷细则列哲学类选答角度：联系观/系统优化；答对且结合材料得2-3分，累计不超过3分。", "正式阅卷细则选答角度", "否", "否", "Batch05核验：现有正文保留。"),
        "M0056": ("母版已覆盖：本轮不重复新增", "矛盾的普遍性和特殊性", "教师版参考答案支持矛盾普遍性与特殊性；正式阅卷细则只宽列对立统一选答角度。", "教师版参考答案+正式阅卷细则宽角度", "否", "否", "Batch05证据降格：不再写逐点强细则。"),
        "M0057": ("母版已覆盖：本轮不重复新增", "实践是认识的基础", "正式阅卷细则列哲学类选答角度：认识论/实践与认识；答对且结合材料得2-3分，累计不超过3分。", "正式阅卷细则选答角度", "否", "否", "Batch05核验：现有正文保留。"),
        "M0162": ("是：已在最终DOCX覆盖（无需新增）", "尊重规律-主观能动性/联系-系统优化/对立统一或矛盾普特/实践与认识；文化自信走文化线", "回源确认题号为Q16中国农历智慧题；正式阅卷细则 lines 586-595 支持必答与选答角度。", "正式阅卷细则必答/选答角度", "否", "否", "Batch05闭合：不是Q17，按Q16现有正文覆盖。"),
        "M0223": ("是：已在最终DOCX覆盖（无需新增）", "规律主观能动/联系系统优化/矛盾普特/实践认识；文化自信走文化线", "Q16正式阅卷细则与教师版答案示例支持；当前DOCX已有对应正文。", "正式阅卷细则必答/选答角度", "否", "否", "Batch05闭合：现有正文覆盖。"),
        "M0224": ("否：题号漂移/无Q17(3)哲学小问", "(无)", "源包Q17只有(1)逻辑与思维、(2)政治与法治；不存在可进入当前哲学宝典的Q17(3)。", "抽取漂移", "否：候选未进正文", "否", "Batch05闭合：HOLD改为排除。"),
        "M0574": ("否：文化交流题，当前哲学正文不补", "文化线边界", "Q4官方答案B，①④均为中非文明交流互鉴/人类命运共同体文化与国际交流语境。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0575": ("否：选必三逻辑题，当前哲学正文不补", "逻辑与思维", "Q5官方答案D，考查假言判断、划分、非传递关系等逻辑知识。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0576": ("否：选必三思维方法题，不按必修四联系观入正文", "逻辑与思维", "Q6官方答案D，表述为发散和聚合思维；“建立联系”是思维方法语境，不作为必修四联系观落点。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0577": ("否：政治与法治题，当前哲学正文不补", "政治与法治", "Q8官方答案A，人大代表/政协委员履职与全过程人民民主。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0578": ("否：政治与法治题，当前哲学正文不补", "政治与法治", "Q9官方答案C，党的主张经法定程序成为国家意志，体现三统一。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0579": ("否：法律与生活题，当前哲学正文不补", "法律与生活", "Q10官方答案C，财产权与知识产权法律判断。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0580": ("否：法律与生活/社会治理语境，当前哲学正文不补", "法律与生活", "Q11官方答案B，道交纠纷一体化与多元解纷；不落必修四矛盾观。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0581": ("否：经济与社会题，当前哲学正文不补", "经济与社会", "Q12官方答案A，智能经济实施路径；“系统性重塑”为经济情境，不作系统观正文落点。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0582": ("否：经济与社会题，当前哲学正文不补", "经济与社会", "Q13官方答案B，制造业行业数据与产业转型。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0583": ("否：经济/国际开放题，当前哲学正文不补", "经济与社会/当代国际政治与经济", "Q14官方答案C，制度型开放与高水平开放。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0584": ("否：当代国际政治与经济题，当前哲学正文不补", "当代国际政治与经济", "Q15官方答案C，四大全球倡议与人类命运共同体；不因“人民至上/发展”词面命中进入哲学正文。", "选择题官方答案键+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0585": ("是：已在最终DOCX覆盖（无需新增）", "尊重客观规律与发挥主观能动性相结合；联系的普遍性；系统观念；矛盾的普遍性和特殊性；实践是认识的基础；认识对实践的反作用", "Q16正式阅卷细则 lines 586-595 支持规律必答角度与哲学选答角度；教师版答案 lines 403-428 及 720-722 支持现有正文表达。", "正式阅卷细则必答/选答角度+教师版答案示例", "否", "否", "Batch05闭合：现有6条正文覆盖；文化必答角度走文化线，不补哲学主线。"),
        "M0586": ("否：Q17为逻辑与思维/政治与法治，当前哲学正文不补", "逻辑与思维；政治与法治", "Q17(1)正式阅卷细则为不完全归纳推理、迁移/想象；Q17(2)为政治与法治建议题。", "正式阅卷细则+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0587": ("否：法律与生活题，当前哲学正文不补", "法律与生活", "Q18正式阅卷细则 lines 637-647，人民法院依法保护知识产权。", "正式阅卷细则+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0588": ("否：经济与社会题，当前哲学正文不补", "经济与社会", "Q19正式阅卷细则 lines 648-665，京津冀新能源汽车产业协同。", "正式阅卷细则+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0589": ("否：当代国际政治与经济题，当前哲学正文不补", "当代国际政治与经济", "Q20正式阅卷细则 lines 666-682，中国为全球发展注入稳定性与正能量。", "正式阅卷细则+模块边界", "否：候选未进正文", "否", "Batch05边界排除。"),
        "M0590": ("是：已在最终DOCX覆盖（无需新增）", "社会存在与社会意识；社会发展的两大基本规律和基本矛盾；人民群众", "Q21正式阅卷细则 lines 683-696 明确综合运用，可用社会存在决定社会意识、上层建筑适应经济基础、以人民为中心等角度；当前DOCX已有三条对应正文。", "正式阅卷细则综合哲学角度", "否", "否", "Batch05闭合：现有正文覆盖。"),
        "M0591": ("否：抽取残片/题号未知，Q1-Q21已逐题处理", "(无)", "该行是源包整段抽取残片；Batch05已逐题裁决Q1-Q21。", "抽取残片", "否：候选未进正文", "否", "Batch05残片闭合。"),
        "M0843": ("套卷有最终DOCX提及且Batch05已逐题闭合", "SUITE_LEVEL_SUMMARY", "Batch05逐题回源闭合，不再仅依赖套卷级记录。", "COVERED_OR_PATCHED_WITH_ROW_REVIEW", "不适用", "否", "Batch05套卷级闭合。"),
    }

    for row in rows:
        mid = row.get(fields["id"])
        if mid in {"M0571", "M0572", "M0573"}:
            q = {"M0571": "Q1", "M0572": "Q2", "M0573": "Q3"}[mid]
            data = inserted[q]
            set_row(
                row,
                f"是：Batch05补入最终DOCX",
                "；".join(node for node, _, _ in data),
                "；".join(src for _, _, src in data),
                "选择题官方答案键+题干正确项链条",
                "否",
                "否",
                "Batch05补入：" + "；".join(heading for _, heading, _ in data),
                "2026朝阳一模逐题回源裁决。",
            )
        elif mid in updates:
            status, node, rule, ev, mis, need, action = updates[mid]
            set_row(row, status, node, rule, ev, mis, need, action, "2026朝阳一模Batch05闭合。")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"MATRIX_BACKUP={backup}")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp)
    update_blocked_metadata(timestamp)
    update_matrix(timestamp, headings)
    print("INSERTED_HEADINGS")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
