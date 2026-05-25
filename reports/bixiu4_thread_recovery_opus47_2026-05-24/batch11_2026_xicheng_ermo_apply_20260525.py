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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH11_2026_XICHENG_ERMO_CODEX_20260525.md"
SUITE = "2026西城二模"


QUESTION_3 = (
    "规划一座城市，本质上是在规划人与空间、人与时间、人与人的关系，当我们真正将城市视为生命体，"
    "或许就能让人们在城市的一呼一吸中找到想要的诗和远方。对此，下列理解正确的是："
    "①城市是静止的物理空间，是人类实践活动的产物；②强调对城市精神价值的回归，体现了意识活动的直接现实性；"
    "③现代城市规划更注重“对人的规划”，说明矛盾是有条件的、可变的；"
    "④世界并不缺乏联系，缺乏的是发现联系的创新意识和价值理性。A.①② B.①③ C.②④ D.③④。官方答案：D。"
)
QUESTION_4 = (
    "北京创新推出外卖骑手随手拍机制：外卖骑手若发现后厨脏乱、无证经营、操作违规等问题，可通过平台一键上报至监管部门快速处置，"
    "并给予基金奖励，形成“核查—奖励—提升”的工作闭环。让骑手从城市服务者变为治理参与者，这一机制："
    "A.坚持系统优化方法，统筹多方主体、整合分散力量实现整体最优；B.创新社会治理规律，依靠多元主体协同解决食品安全问题；"
    "C.推动角色转变，根据人的实践需要建立治理联动的具体联系；D.调整上层建筑以适应经济基础的发展，消除食品安全领域固有矛盾。官方答案：A。"
)
QUESTION_16 = "结合材料，运用《哲学与文化》知识，分析中式生活方式为什么能跨越文化差异、引发全球青年广泛共鸣。"
QUESTION_20 = "结合材料，综合运用所学，谈谈你对“要牢固树立和践行正确政绩观”的理解。"

RUBRIC_RENDER = (
    "99_logs/weak_gate_sources/renders/xicheng_rubric/page_001.png;"
    "99_logs/weak_gate_sources/renders/xicheng_rubric/page_002.png;"
    "99_logs/weak_gate_sources/renders/xicheng_rubric/page_003.png;"
    "BATCH11_2026_XICHENG_ERMO_RUBRIC_TRANSCRIPTION_20260525.md"
)

ENTRIES = [
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q3",
        "heading_suffix": "2026西城二模 第3题（选择题）",
        "material_trigger": "题干把城市规划界定为规划人与空间、人与时间、人与人的关系；官方答案D锁定③④，其中④明确“世界并不缺乏联系”。",
        "question_prompt": QUESTION_3,
        "why_trigger": "看到城市不只是静止空间，而是人与空间、时间、他人之间的关系网络，应想到联系的观点。正确项④把“联系”直接写出，说明城市治理要发现并处理多重联系。",
        "answer_landing": "本题应选D。本节点处理④：城市规划要看到人与空间、时间、他人的普遍联系，用联系的观点理解城市生命体，而不是把城市拆成孤立的物理空间。",
        "evidence_level": "选择题官方答案键+题干正确项链条（正确项④）",
        "source_lines": "01_source_inventory/suite_source_bundles/2026西城二模.md:44-49;166-170",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q4",
        "heading_suffix": "2026西城二模 第4题（选择题）",
        "material_trigger": "题干写外卖骑手、平台、监管部门和基金奖励共同构成“核查—奖励—提升”的工作闭环；官方答案A直接写“系统优化方法”和“整体最优”。",
        "question_prompt": QUESTION_4,
        "why_trigger": "看到多方主体被放入一个闭环机制，并以整体治理效果为目标，就应想到系统优化。正确项A明确要求统筹多方主体、整合分散力量，实现整体最优。",
        "answer_landing": "本题应选A。随手拍机制不是单一主体单点执法，而是把骑手发现、平台上报、监管处置、奖励激励组织成系统，体现用系统优化方法提升食品安全治理整体效果。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2026西城二模.md:50-54;166-170",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q16",
        "heading_suffix": "2026西城二模 第16题（主观题）",
        "material_trigger": "材料写全球青年体验喝热水、练八段锦、节气起居与和睦共居，在烟火气中感受中华文明崇尚和谐、顺应自然、身心兼顾的独特智慧；评标渲染页明确列“价值观的导向作用”。",
        "question_prompt": QUESTION_16,
        "why_trigger": "这些生活方式能引发共鸣，不只是因为形式新鲜，而是因为其中蕴含健康、和谐、顺应自然、身心兼顾等价值取向；价值观影响人们对中式生活方式的认识、评价和行为选择。",
        "answer_landing": "中式生活方式承载的健康、和谐、顺应自然等价值追求契合当代青年对美好生活的期待。卷面可写：价值观具有导向作用，共通的价值追求引导海外青年理解、认同并模仿中式生活方式。",
        "evidence_level": "评标PDF渲染证据-哲学观点明示",
        "source_lines": RUBRIC_RENDER,
    },
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q20",
        "heading_suffix": "2026西城二模 第20题（主观题）",
        "material_trigger": "材料引用“要坚持从实际出发、按规律办事、科学决策、苦干实干”，并把正确政绩观落实到创造经得起实践、人民、历史检验的实绩。",
        "question_prompt": QUESTION_20,
        "why_trigger": "看到“从实际出发、按规律办事、科学决策”这一组直接表述，应落到实事求是。正确政绩观不是为短期显绩造概念，而是从人民需要、客观条件和长期发展规律出发办实事。",
        "answer_landing": "树立正确政绩观，要坚持实事求是，从实际出发、按规律办事、科学决策，把工作建立在真实民情、客观条件和长期规律上，创造经得起实践检验的实绩。",
        "evidence_level": "教师版参考答案宽角度+材料明示（非逐点细则）",
        "source_lines": "01_source_inventory/suite_source_bundles/2026西城二模.md:159-164;180-183",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q20",
        "heading_suffix": "2026西城二模 第20题（主观题）",
        "material_trigger": "材料反复强调“最广大人民群众的最大利益”“为民初心”“为民造福”，并要求政绩经得起人民检验。",
        "question_prompt": QUESTION_20,
        "why_trigger": "正确政绩观首先要回答“为谁干事”。材料把政绩方向交给人民利益和人民检验，说明人民群众是社会历史的主体，党员干部干事创业必须坚持群众观点。",
        "answer_landing": "树立正确政绩观，要坚持人民主体地位，把为民造福作为出发点和落脚点，让工作成效由人民需要和人民评价来检验，而不是追求个人声望或表面工程。",
        "evidence_level": "教师版参考答案宽角度+材料明示（非逐点细则）",
        "source_lines": "01_source_inventory/suite_source_bundles/2026西城二模.md:159-164;180-183",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q20",
        "heading_suffix": "2026西城二模 第20题（主观题）",
        "material_trigger": "材料强调既做眼前实事，也做为后人作铺垫、打基础、利长远的好事；谷文昌“久久为功”，一代代优秀共产党人推动党和国家事业行稳致远。",
        "question_prompt": QUESTION_20,
        "why_trigger": "看到“利长远”“打基础”“久久为功”“行稳致远”，不能只看短期成效，而要用发展的观点看政绩。正确政绩观要求把当前工作放到长期发展进程中衡量。",
        "answer_landing": "树立正确政绩观，要用发展的观点处理当前和长远的关系，既办群众当下看得见的实事，也做打基础、利长远的好事，以持续奋斗推动事业长远发展。",
        "evidence_level": "教师版参考答案宽角度+材料明示（非逐点细则）",
        "source_lines": "01_source_inventory/suite_source_bundles/2026西城二模.md:159-164;180-183",
    },
]

SECTION_NEXT = {
    "联系的普遍性 / 联系的观点（总）": "联系的客观性",
    "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
    "价值观的导向作用": "价值判断与价值选择",
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
    "人民群众": "五、价值观 / 人生观",
    "发展的观点 / 发展的普遍性": "量变与质变 / 适度原则",
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


def para_text(p):
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
    end = next((i for i in range(start + 1, len(paras)) if para_text(paras[i]).strip() == next_heading), None)
    if end is None:
        raise RuntimeError(f"next heading not found after {heading}: {next_heading}")
    return start, end


def insert_entry(root, entry: dict[str, str]) -> str:
    body = root.find("w:body", namespaces=NS)
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    existing = next((para_text(paras[i]).strip() for i in range(start + 1, end) if para_text(paras[i]).strip().endswith(entry["heading_suffix"])), None)
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
    ref = paras[end]
    for p in template:
        body.insert(body.index(ref), p)
    return heading


def update_docx(timestamp: str) -> list[str]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_xicheng_ermo_batch11_{timestamp}.docx")
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
        "source_lane": "Codex Batch11 recovery production",
        "source_repair_basis": entry["source_lines"],
        "source_lines": entry["source_lines"],
        "batch": "batch11_2026_xicheng_ermo",
    }


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch11_xicheng_ermo_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    desired = {(e["canonical_node"], SUITE, e["question_no"]): {"canonical_node": e["canonical_node"], "source_suite": SUITE, "question_no": e["question_no"], "inserted_heading": h} for e, h in zip(ENTRIES, headings)}
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
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch11_xicheng_ermo_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup)
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    desired = {(SUITE, e["question_no"], e["canonical_node"]): accepted_record(e, h) for e, h in zip(ENTRIES, headings)}
    # Also repair prior Q16 evidence text so it points to the rendered rubric, not only the teacher answer.
    for record in records:
        key = (record.get("source_suite"), record.get("question_no"), record.get("canonical_node"))
        if key in {
            (SUITE, "Q16", "矛盾的普遍性和特殊性"),
            (SUITE, "Q16", "实践是认识的基础"),
        }:
            record["evidence_level"] = "评标PDF渲染证据-哲学观点明示"
            record["source_repair_basis"] = RUBRIC_RENDER
            record["source_lines"] = RUBRIC_RENDER
            record["boundary_note"] = "西城二模评标PDF渲染页明示该哲学观点；教师版答案只作辅助文本指针。"
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


def row_values(row_id: str, q: str, type_: str, in_body: str, node: str, principle: str, evidence: str, action: str, note: str, artifact: str) -> dict[str, str]:
    return {
        KEYS["id"]: row_id,
        "row_source": "batch11_2026_xicheng_ermo_recovery",
        KEYS["source"]: SUITE,
        KEYS["year"]: "2026",
        KEYS["stage"]: "二模",
        KEYS["question"]: q,
        KEYS["type"]: type_,
        KEYS["in_body"]: in_body,
        KEYS["node"]: node,
        KEYS["principle"]: principle,
        KEYS["evidence"]: evidence,
        KEYS["misplaced"]: "否",
        KEYS["needs"]: "否",
        KEYS["action"]: action,
        KEYS["note"]: note,
        KEYS["artifact"]: artifact,
    }


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch11_2026_xicheng_ermo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}
    common = "01_source_inventory/suite_source_bundles/2026西城二模.md"
    q3, q4, q16_value, q20_reality, q20_people, q20_development = headings
    q20_note = f"新增Q20条目：{q20_reality}；{q20_people}；{q20_development}。证据为教师版参考答案宽角度+材料明示，非逐点细则。"
    decisions = {
        "M0027": dict(in_body="是：已由当前DOCX覆盖", node="矛盾的普遍性和特殊性", principle="Q16评标PDF渲染页明示哲学观点：矛盾普遍性寓于特殊性，特殊性包含普遍性。", evidence="评标PDF渲染证据-哲学观点明示+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH11", note="旧强细则来源说明已修正为评标PDF渲染证据。", artifact=RUBRIC_RENDER),
        "M0028": dict(in_body="是：已由当前DOCX覆盖", node="实践是认识的基础", principle="Q16评标PDF渲染页明示实践决定认识（来源/动力/标准）。", evidence="评标PDF渲染证据-哲学观点明示+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH11", note="旧强细则来源说明已修正为评标PDF渲染证据。", artifact=RUBRIC_RENDER),
        "M0041": dict(in_body="否：重复旧弱证据行，已被评标PDF渲染证据替代", node="矛盾的普遍性和特殊性", principle="旧行称评标PDF 0字节；现已用渲染页和转录文件补证。", evidence="旧弱证据行关闭", misplaced="否", needs="否", action="SUPERSEDED_BY_RENDERED_RUBRIC_BATCH11", note="以M0027/M0117当前证据为准。", artifact=RUBRIC_RENDER),
        "M0042": dict(in_body="否：重复旧弱证据行，已被评标PDF渲染证据替代", node="实践是认识的基础", principle="旧行称需回源核验；现已用渲染页和转录文件补证。", evidence="旧弱证据行关闭", misplaced="否", needs="否", action="SUPERSEDED_BY_RENDERED_RUBRIC_BATCH11", note="以M0028/M0118当前证据为准。", artifact=RUBRIC_RENDER),
        "M0112": dict(in_body="旧撤回结论已被评标PDF渲染证据推翻；不作为当前状态", node="价值观的导向作用", principle="评标PDF渲染页明确列出价值观的导向作用，故旧“细则不支持价值观”结论失效。", evidence="旧撤回结论作废", misplaced="否", needs="否", action="SUPERSEDED_BY_BATCH11_VALUE_RUBRIC_RECHECK", note="当前有效状态见M0119和Batch11新增DOCX条目。", artifact=RUBRIC_RENDER),
        "M0117": dict(in_body="是：已由当前DOCX覆盖", node="矛盾的普遍性和特殊性", principle="Q16评标PDF渲染页明示矛盾普遍性寓于特殊性，特殊性包含普遍性。", evidence="评标PDF渲染证据-哲学观点明示+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH11", note="保留现有正文。", artifact=RUBRIC_RENDER),
        "M0118": dict(in_body="是：已由当前DOCX覆盖", node="实践是认识的基础", principle="Q16评标PDF渲染页明示实践决定认识（来源/动力/标准）。", evidence="评标PDF渲染证据-哲学观点明示+现有DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_BY_EXISTING_DOCX_BATCH11", note="保留现有正文。", artifact=RUBRIC_RENDER),
        "M0119": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="价值观的导向作用", principle="Q16评标PDF渲染页明示价值观的导向作用。", evidence="评标PDF渲染证据-哲学观点明示", misplaced="否", needs="否", action="INSERTED_BATCH11_2026_XICHENG_Q16_VALUE_GUIDANCE", note=f"新增条目：{q16_value}。", artifact=RUBRIC_RENDER),
        "M0150": dict(in_body="是：已由当前DOCX覆盖并补齐价值观条目", node="矛盾普遍性与特殊性/实践/价值观", principle="Q16评标PDF渲染页支持矛盾普遍性与特殊性、实践决定认识、价值观导向作用。", evidence="评标PDF渲染证据-哲学观点明示+现有/新增DOCX正文覆盖", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH11", note="弱候选挂起关闭。", artifact=RUBRIC_RENDER),
        "M0245": dict(in_body="是：已由当前DOCX覆盖并补齐价值观条目", node="矛盾的普遍性和特殊性/实践是认识的基础/价值观的导向作用", principle="Q16三条哲学观点经评标PDF渲染补证后闭合。", evidence="评标PDF渲染证据-哲学观点明示", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH11", note="当前DOCX含矛盾、实践、价值观三条。", artifact=RUBRIC_RENDER),
        "M0756": dict(in_body="否：经济/制度优势边界题", node="不进入当前哲学宝典正文", principle="Q1官方答案D，正确项③④为制度优势和科技创新/农业现代化；①生产力表述为错误项，不能入正文。", evidence="官方答案键+错误项剔除+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="不采错误项①。", artifact=f"{common}:29-38;166-170"),
        "M0757": dict(in_body="否：文化线边界题", node="不进入当前哲学宝典正文", principle="Q2官方答案A，文化主体性、文化自信和生态领域话语权属于文化/综合国力表达；不进入当前哲学主线。", evidence="官方答案键+文化线边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="文化线另审。", artifact=f"{common}:39-43;166-170"),
        "M0758": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="联系的普遍性 / 联系的观点（总）", principle="Q3官方答案D，正确项④明确世界并不缺乏联系，缺乏发现联系的创新意识和价值理性。", evidence="选择题官方答案键+题干正确项链条", misplaced="否", needs="否", action="INSERTED_BATCH11_2026_XICHENG_Q3_CONNECTION", note=f"新增条目：{q3}；正确项③不单独展开为新节点。", artifact=f"{common}:44-49;166-170"),
        "M0759": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="系统观念 / 系统优化", principle="Q4官方答案A，正确项明确系统优化方法、统筹多方主体、整合分散力量实现整体最优。", evidence="选择题官方答案键+题干正确项链条", misplaced="否", needs="否", action="INSERTED_BATCH11_2026_XICHENG_Q4_SYSTEM_OPTIMIZATION", note=f"新增条目：{q4}。", artifact=f"{common}:50-54;166-170"),
        "M0760": dict(in_body="否：选必三逻辑与思维边界题", node="不进入当前哲学宝典正文", principle="Q5官方答案B，考查必要条件/复合判断推理，属于逻辑与思维。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="逻辑推理题排除。", artifact=f"{common}:55-61;166-170"),
        "M0761": dict(in_body="否：选必三创新思维边界题", node="不进入当前哲学宝典正文", principle="Q6官方答案A，联想、跨界融合和创新思维跨越性/独特性属于逻辑与思维；③为错误项。", evidence="官方答案键+模块边界+错误项剔除", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="不把错误项③的扬弃表述转入哲学正文。", artifact=f"{common}:62-67;166-170"),
        "M0762": dict(in_body="否：政治与法治/人大代表边界题", node="不进入当前哲学宝典正文", principle="Q7官方答案D，数字人大推动民生实事解决，属于政治与法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="政治模块排除。", artifact=f"{common}:68-72;166-170"),
        "M0763": dict(in_body="否：政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q8官方答案B，五年规划编制涉及党的领导、问计于民和法定程序，属于政治与法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="政治模块排除。", artifact=f"{common}:73-84;166-170"),
        "M0764": dict(in_body="否：法律与生活/基层治理边界题", node="不进入当前哲学宝典正文", principle="Q9官方答案D，考查物业纠纷、权利救济与居委会调解，属于法律与生活/基层治理。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="法律模块排除。", artifact=f"{common}:85-92;166-170"),
        "M0765": dict(in_body="否：法律与生活边界题", node="不进入当前哲学宝典正文", principle="Q11官方答案C，考查夫妻财产、抵押、公司经营收益与有限责任，属于法律与生活。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="法律模块排除。", artifact=f"{common}:98-103;166-170"),
        "M0766": dict(in_body="否：选必一全球经济治理边界题", node="不进入当前哲学宝典正文", principle="Q15官方答案B，二十国集团完善全球经济治理属于当代国际政治与经济。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="选必一模块排除。", artifact=f"{common}:123-128;166-170"),
        "M0767": dict(in_body="是：已由当前DOCX覆盖并补齐价值观条目", node="矛盾普遍性与特殊性/实践/价值观", principle="Q16评标PDF渲染页明示三条哲学观点：矛盾普遍性与特殊性、实践决定认识、价值观导向作用。", evidence="评标PDF渲染证据-哲学观点明示", misplaced="否", needs="否", action="COVERED_AND_INSERTED_BATCH11", note="Q16候选闭合。", artifact=RUBRIC_RENDER),
        "M0768": dict(in_body="否：经济与社会边界题", node="不进入当前哲学宝典正文", principle="Q17正式答案为国家规划引领、政策支持、技术进步、供需互动和市场扩张，属于经济与社会。", evidence="教师版参考答案-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="经济模块排除。", artifact=f"{common}:134-141;173-174"),
        "M0769": dict(in_body="否：法律/法治/逻辑与思维边界题", node="不进入当前哲学宝典正文", principle="Q18(1)-(3)为法律与法治；Q18(4)为逻辑与思维的科学思维/辩证思维/创新意识，不进入当前必修四哲学主线。", evidence="教师版参考答案-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="第(4)问属于《逻辑与思维》，不作为必修四哲学正文。", artifact=f"{common}:142-152;175-179"),
        "M0770": dict(in_body="否：选必一当代国际政治经济边界题", node="不进入当前哲学宝典正文", principle="Q19为全球数据治理、数字经济、国际组织与国际合作，属于当代国际政治与经济。", evidence="教师版参考答案-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH11", note="选必一模块排除。", artifact=f"{common}:153-158;180-182"),
        "M0771": dict(in_body="是：本批新增进入当前DOCX/PDF正文", node="一切从实际出发 / 实事求是；人民群众；发展的观点 / 发展的普遍性", principle="Q20教师版参考答案列群众观点、实事求是、发展观等角度；材料直接写从实际出发、按规律办事、为民造福、利长远、久久为功。", evidence="教师版参考答案宽角度+材料明示（非逐点细则）", misplaced="否", needs="否", action="INSERTED_BATCH11_2026_XICHENG_Q20_POLITICAL_ACHIEVEMENT_VIEW", note=q20_note, artifact=f"{common}:159-164;180-183"),
        "M0772": dict(in_body="否：抽取残留/题号不明", node="不进入当前哲学宝典正文", principle="该行无独立题号；经Q1-Q20回源，缺行已补为Q10/Q12/Q13/Q14，残留关闭。", evidence="抽取残留清理+逐题源包核对", misplaced="否", needs="否", action="EXTRACTION_RESIDUE_CLOSED_BATCH11", note="不保留Qunknown挂起。", artifact=f"{common}:1-206"),
        "M0812": dict(in_body="套卷逐题已由Batch11闭合", node="SUITE_LEVEL_SUMMARY", principle="逐题回源已闭合：Q3/Q4/Q16价值观/Q20新增，Q16原两条重引评标PNG证据，其余模块边界排除或补行。", evidence="Batch11逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH11", note="套卷级记录不替代逐题记录。", artifact=f"{common}:1-206"),
        "M0858": dict(in_body="套卷逐题已由Batch11闭合", node="SUITE_LEVEL_SUMMARY", principle="逐题回源已闭合：Q3/Q4/Q16价值观/Q20新增，Q16原两条重引评标PNG证据，其余模块边界排除或补行。", evidence="Batch11逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH11", note="原套卷级挂起项关闭。", artifact=f"{common}:1-206"),
    }
    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)
    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    additions = [
        row_values(f"M{max_id + 1:04d}", "Q10", "法律与生活/劳动纠纷边界题", "否：法律与生活边界题", "不进入当前哲学宝典正文", "Q10官方答案C，诉调对接解决劳动关系纠纷，属于法律与生活/劳动纠纷解决。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH11", "原矩阵缺独立Q10行，本批补充边界闭合。", f"{common}:93-97;166-170"),
        row_values(f"M{max_id + 2:04d}", "Q12", "经济与社会边界题", "否：经济与社会边界题", "不进入当前哲学宝典正文", "Q12官方答案B，流动性陷阱、消费券、转移支付和社会保障属于经济与社会/宏观调控。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH11", "原矩阵缺独立Q12行，本批补充边界闭合。", f"{common}:104-109;166-170"),
        row_values(f"M{max_id + 3:04d}", "Q13", "经济与社会/对外开放边界题", "否：经济与对外开放边界题", "不进入当前哲学宝典正文", "Q13官方答案C，为跨国公司制定在华投资方案，属于经济与社会/开放型经济。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH11", "原矩阵缺独立Q13行，本批补充边界闭合。", f"{common}:110-115;166-170"),
        row_values(f"M{max_id + 4:04d}", "Q14", "经济与社会/消费市场边界题", "否：经济与消费市场边界题", "不进入当前哲学宝典正文", "Q14官方答案C，老年智能产品交易规模、需求匹配和消费升级属于经济与社会。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH11", "原矩阵缺独立Q14行，本批补充边界闭合。", f"{common}:116-122;166-170"),
    ]
    existing = {(r[KEYS["source"]], r[KEYS["question"]], r[KEYS["action"]]) for r in rows}
    for row in additions:
        key = (row[KEYS["source"]], row[KEYS["question"]], row[KEYS["action"]])
        if key not in existing:
            rows.append(row)
            existing.add(key)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(timestamp: str, headings: list[str]) -> None:
    text = f"""# Coverage Fusion Batch11 - 2026西城二模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2026西城二模
status: CODEX_BATCH11_SOURCE_COVERAGE_APPLIED

## Source Basis

- source bundle: `01_source_inventory/suite_source_bundles/2026西城二模.md`
- Q16 rendered rubric transcription: `BATCH11_2026_XICHENG_ERMO_RUBRIC_TRANSCRIPTION_20260525.md`
- Q16 rubric image evidence: `99_logs/weak_gate_sources/renders/xicheng_rubric/page_001.png` to `page_003.png`
- paper/answer lines checked: Q1-Q15 `29-128`, answer key `166-170`; Q16-Q20 `131-164`, teacher answer/reference `171-205`

## Inserted Into DOCX

- {headings[0]} -> 联系的普遍性 / 联系的观点（总）
- {headings[1]} -> 系统观念 / 系统优化
- {headings[2]} -> 价值观的导向作用
- {headings[3]} -> 一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一
- {headings[4]} -> 人民群众
- {headings[5]} -> 发展的观点 / 发展的普遍性

## Question Disposition

- Q1: excluded; correct options are system/economics, and the production-force philosophy-like option is wrong.
- Q2: excluded; culture-line boundary.
- Q3: inserted under 联系的普遍性 using correct item ④.
- Q4: inserted under 系统观念 using correct item A.
- Q5: excluded; logic and thinking boundary.
- Q6: excluded; innovation-thinking boundary; wrong option ③ not used.
- Q7-Q15: excluded by politics/law/economics/international module boundaries.
- Q16: existing contradiction/practice entries retained with rendered-rubric evidence; value-guidance companion entry added; culture angles are not merged into the philosophy mainline.
- Q17-Q19: excluded by economics/law/logic/international module boundaries.
- Q20: inserted under 实事求是, 人民群众, and 发展观 with explicit weaker evidence label: teacher-version broad angle plus material wording, not point-by-point rubric.
- Qunknown: closed as extraction residue.
- Missing independent rows added and excluded for Q10/Q12/Q13/Q14.

## Boundary

No Sonnet/Haiku/model-unknown output was used for Codex placement decisions. Q20 entries are intentionally labeled as broad teacher-answer support rather than formal detailed scoring rules.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp, headings)
    update_matrix(timestamp, headings)
    write_report(timestamp, headings)
    print(f"Batch11 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
