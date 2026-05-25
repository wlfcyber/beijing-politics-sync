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
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH06_2026_HAIDIAN_ERMO_CODEX_20260525.md"
SUITE = "2026海淀二模"

QUESTION_2 = (
    "某博物馆推出“24小时不打烊”开放模式。深夜展厅里观众与文物静默对话，"
    "数字化古画场景成为打卡热点……该博物馆也带动所在区域客流增长、辐射周边商圈。"
    "这表明：①文化对经济发展起支配作用；②文化作为社会意识能够转化为现实生产力；"
    "③不同资源相互融通可以催生新的发展动能；④激活经济价值，文化事业才能满足大众需求。"
    "A．①③ B．①④ C．②③ D．②④。官方答案：C。"
)

QUESTION_3 = (
    "“吾家洗砚池头树，个个花开淡墨痕，不要人夸颜色好，只留清气满乾坤。”"
    "自然界本无墨色梅花，在传统审美习惯中，花卉也多以艳丽为美，但中国传统画家却以水墨绘梅，"
    "舍艳色而取傲雪之姿，借以表达高洁的人格之美。墨梅这一独特的美学符号："
    "A．是在思维具体中描摹了梅花的整体表象；B．由梅的特性隐喻人格之美，运用了类比推理方法；"
    "C．表明人们能够创造出自然界并不存在的艺术形象；D．在艺术创作实践中深化了对梅花自然属性的真理性认识。"
    "官方答案：C。"
)

QUESTION_4 = (
    "深圳湾公园是全球候鸟迁飞通道上的重要“补给站”和“中转站”。为防止干扰鸟类昼夜节律，"
    "该公园将园内部分道路灯光调暗，在主要出入口保留基础照明设施。对此，有市民认为"
    "“公园亮灯是城市文明的体现，调暗灯光为生态让路也是城市文明的体现”。下列说法正确的是："
    "A．候鸟迁飞与公园照明之间的联系具有“人化”的特点；"
    "B．在候鸟迁飞期间，生态保护成为当前社会主要矛盾的主要方面；"
    "C．材料中市民的说法是对同一事物作出相反的论断，违反了矛盾律的要求；"
    "D．公园的做法遵循折中主义，实现“便民”与“护鸟”平衡。官方答案：A。"
)

ENTRIES = [
    {
        "canonical_node": "社会存在与社会意识",
        "question_no": "Q2",
        "heading_suffix": "2026海淀二模 第2题（选择题）",
        "material_trigger": "博物馆夜间开放、数字化古画场景带动客流和周边商圈；正确项②明确说“文化作为社会意识能够转化为现实生产力”。",
        "question_prompt": QUESTION_2,
        "why_trigger": "能想到社会存在与社会意识，是因为题目不是单纯考文化活动热闹，而是把文化形态、观众体验、区域客流和商圈发展连在一起。文化属于社会意识，能够反作用于社会存在；当文化资源以新的方式进入生活场景，就会影响经济活动和社会生活。",
        "answer_landing": "本题应选C。本节点处理②：文化作为社会意识不是被动影子，在一定条件下能够转化为现实生产力，带动客流、消费和区域发展。③“不同资源相互融通”可辅助理解联系，但本次不另拆成独立哲学采分点，避免把经济文化融合泛化成多节点堆砌。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2026海淀二模.md:1007-1010;1133-1137;1157-1160",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q3",
        "heading_suffix": "2026海淀二模 第3题（选择题）",
        "material_trigger": "题干写自然界本无墨色梅花，画家以水墨绘梅并借以表达高洁人格；正确项C说人们能够创造出自然界并不存在的艺术形象。",
        "question_prompt": QUESTION_3,
        "why_trigger": "能想到意识的能动作用，是因为墨梅不是对自然梅花的机械复制，而是在审美选择、人格寄托和艺术加工中形成的新形象。意识活动具有目的性、自觉选择性和能动创造性，能在反映客观对象的基础上创造观念形象。",
        "answer_landing": "本题应选C。卷面抓住“自然界本无墨色梅花”与“艺术形象”这组信号：人能够在尊重客观对象的基础上发挥意识的能动创造作用，把自然梅花加工成承载人格之美的艺术符号。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2026海淀二模.md:1011-1015;1133-1137;1157-1160",
    },
    {
        "canonical_node": "联系的客观性",
        "question_no": "Q4",
        "heading_suffix": "2026海淀二模 第4题（选择题）",
        "material_trigger": "深圳湾公园依据候鸟迁飞和照明干扰之间的关系调暗道路灯光；正确项A说“候鸟迁飞与公园照明之间的联系具有‘人化’的特点”。",
        "question_prompt": QUESTION_4,
        "why_trigger": "能想到联系的客观性，是因为“人化”的联系并不等于主观任意制造联系。园区照明是人为设施，但它对候鸟昼夜节律的影响是客观发生的；人只能在尊重生态规律和客观条件的基础上调整设施安排。",
        "answer_landing": "本题应选A。卷面可写：人为事物的联系具有“人化”特点，但形成之后仍具有客观性，必须以客观规律和客观条件为依据。调暗照明体现的是尊重候鸟迁飞规律、按客观联系优化城市管理，而不是主观折中。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "01_source_inventory/suite_source_bundles/2026海淀二模.md:1016-1020;1133-1137;1157-1160",
    },
]

SECTION_NEXT = {
    "主观能动性 / 意识的能动作用": "尊重客观规律与发挥主观能动性相结合",
    "联系的客观性": "根据固有联系建立新的具体联系",
    "社会存在与社会意识": "社会发展的两大基本规律和基本矛盾",
}

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]


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
    existing = next((para_text(p).strip() for p in paras if para_text(p).strip().endswith(entry["heading_suffix"])), None)
    if existing:
        return existing

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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_haidian_ermo_batch06_{timestamp}.docx")
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
    backup = LEDGER.with_name(f"docx_insert_ledger_backup_before_batch06_haidian_ermo_{timestamp}.csv")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if not fieldnames:
        raise RuntimeError("ledger has no header")
    existing = {(r["canonical_node"], r["source_suite"], r["question_no"], r["inserted_heading"]) for r in rows}
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


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    items = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.strip():
            items.append(json.loads(line))
    return items


def write_jsonl(path: Path, items: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(i, ensure_ascii=False) for i in items) + "\n", encoding="utf-8")


def update_accepted(timestamp: str) -> None:
    backup = ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch06_haidian_ermo_{timestamp}.jsonl")
    shutil.copy2(ACCEPTED, backup)
    items = load_jsonl(ACCEPTED)

    for item in items:
        if item.get("source_suite") == SUITE and item.get("question_no") == "Q16":
            if item.get("canonical_node") in {"联系的普遍性 / 联系的观点（总）", "实践与认识（总）"}:
                item["evidence_level"] = "答案和评分参考角度（非逐点细则）"
                item["boundary_note"] = (
                    "可读源只明确列“联系、实践与认识”等角度；保留总节点，不拆成矛盾、实践基础、认识反作用等独立采分点。"
                )
                item["source_repair_basis"] = (
                    "01_source_inventory/suite_source_bundles/2026海淀二模.md:1092-1094;1140-1141;1162-1163; "
                    "2026海淀二模_Q16_readable_evidence.md"
                )

    existing = {(i.get("source_suite"), i.get("question_no"), i.get("canonical_node"), i.get("material_trigger")) for i in items}
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
            "source_lane": "Codex Batch06 2026海淀二模",
            "source_repair_basis": entry["source_lines"],
        }
        key = (item["source_suite"], item["question_no"], item["canonical_node"], item["material_trigger"])
        if key not in existing:
            items.append(item)
    write_jsonl(ACCEPTED, items)
    print(f"ACCEPTED_BACKUP={backup}")


def update_blocked(timestamp: str) -> None:
    if not BLOCKED.exists():
        return
    backup = BLOCKED.with_name(f"student_patch_entries.blocked_backup_before_batch06_haidian_ermo_{timestamp}.jsonl")
    shutil.copy2(BLOCKED, backup)
    items = load_jsonl(BLOCKED)
    for item in items:
        if item.get("source_suite") != SUITE:
            continue
        q = item.get("question_no")
        node = item.get("canonical_node") or item.get("framework_node")
        if q == "Q16":
            if node in {"联系的普遍性 / 联系的观点（总）", "实践是认识的基础"}:
                item["evidence_level"] = "答案和评分参考角度（已融合处理）"
                item["boundary_note"] = "Batch06裁决：Q16只保留“联系”和“实践与认识”总节点；不再把弱候选拆成单独正文条目。"
                item["block_reason"] = "superseded_by_broad_q16_nodes"
            else:
                item["evidence_level"] = "证据不足：不单独成条"
                item["boundary_note"] = "Batch06裁决：可读评分参考没有给出该具体原理的独立落点，不进当前正文。"
                item["block_reason"] = "retracted_weak_split"
        elif q == "Q21":
            item["evidence_level"] = "宽泛答案和评分参考角度（非逐点细则）"
            item["boundary_note"] = "Batch06裁决：Q21仅列“中国共产党的领导、中国式现代化、全面依法治国、国家安全、矛盾的观点、辩证思维”等宽角度；不凭普通角度提示进哲学正文。"
            item["block_reason"] = "HOLD_NO_INSERT_BROAD_ANGLE_ONLY"
    write_jsonl(BLOCKED, items)
    print(f"BLOCKED_BACKUP={backup}")


def set_row(row: dict[str, str], *, status: str, node: str, rule: str, ev: str, mis: str, need: str, action: str, note: str) -> None:
    row["是否进宝典"] = status
    row["宝典节点"] = node
    row["细则支持原理"] = rule
    row["证据等级"] = ev
    row["是否误放"] = mis
    row["是否需补厚"] = need
    row["当前处理"] = action
    old = row.get("备注", "")
    marker = f"Batch06裁决：{note}"
    row["备注"] = old if marker in old else (f"{old}；{marker}" if old else marker)


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch06_2026_haidian_ermo_{timestamp}.csv"
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if not fieldnames:
        raise RuntimeError("matrix has no header")

    heading_by_q = {entry["question_no"]: heading for entry, heading in zip(ENTRIES, headings)}
    source_by_q = {entry["question_no"]: entry["source_lines"] for entry in ENTRIES}
    node_by_q = {entry["question_no"]: entry["canonical_node"] for entry in ENTRIES}

    updates: dict[str, dict[str, str]] = {
        "M0025": dict(status="是：已进入当前DOCX/PDF正文", node="联系的普遍性 / 联系的观点（总）", rule="答案和评分参考只列“联系、实践与认识”等角度；当前只保留联系总节点。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="Batch06保留总节点并降格证据表述", note="Q16不再写成讲评逐点细则。"),
        "M0026": dict(status="是：已进入当前DOCX/PDF正文", node="实践与认识（总）", rule="答案和评分参考只列“联系、实践与认识”等角度；当前只保留实践与认识总节点。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="Batch06保留总节点并降格证据表述", note="Q16不单拆实践基础/认识反作用。"),
        "M0038": dict(status="已融合：不另立弱证据正文", node="联系的普遍性 / 联系的观点（总）", rule="由M0025宽角度覆盖；不另立弱候选。", ev="答案和评分参考角度（已融合）", mis="否", need="否", action="MERGED_INTO_M0025", note="blocked旧行作融合闭合。"),
        "M0039": dict(status="已融合：不另立弱证据正文", node="实践与认识（总）", rule="由M0026宽角度覆盖；不单拆实践是认识的基础。", ev="答案和评分参考角度（已融合）", mis="否", need="否", action="MERGED_INTO_M0026", note="blocked旧行作融合闭合。"),
        "M0040": dict(status="否：宽泛角度提示不进正文", node="矛盾的观点/辩证思维", rule="Q21答案和评分参考仅列多个可选宽角度，没有提供矛盾观点逐点细则；辩证思维还涉及选必三边界。", ev="宽泛答案和评分参考角度（非逐点细则）", mis="否：未进入正文", need="否", action="HOLD_NO_INSERT_BROAD_ANGLE_ONLY", note="保留未来候选，不作为当前宝典落点。"),
        "M0113": dict(status="已融合：由M0025覆盖", node="联系的普遍性 / 联系的观点（总）", rule="可读源支持联系宽角度，保留总节点。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="MERGED_INTO_M0025", note="不再按讲评页强逐点表述扩张。"),
        "M0114": dict(status="已融合：由M0026覆盖", node="实践与认识（总）", rule="可读源支持实践与认识宽角度，不单拆实践基础。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="MERGED_INTO_M0026", note="不单立实践是认识的基础。"),
        "M0115": dict(status="否：不进当前正文", node="认识对实践的反作用", rule="可读源没有给出认识反作用独立落点。", ev="证据不足：不单独成条", mis="否：未进入正文", need="否", action="RETRACT_WEAK_SPLIT", note="弱修复拆点撤回。"),
        "M0116": dict(status="否：不进当前正文", node="矛盾就是对立统一", rule="可读源没有给出矛盾对立统一独立落点。", ev="证据不足：不单独成条", mis="否：未进入正文", need="否", action="RETRACT_WEAK_SPLIT", note="弱修复拆点撤回。"),
        "M0148": dict(status="已闭合：由M0025/M0026覆盖", node="联系/实践与认识", rule="Q16宽角度已进入两个总节点。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="FUSION_CLOSED_BROAD_Q16", note="ClaudeCode B弱候选融合裁决完成。"),
        "M0149": dict(status="否：宽泛角度提示不进正文", node="矛盾的观点/辩证思维", rule="Q21缺逐点细则，且辩证思维为选必三边界风险。", ev="宽泛答案和评分参考角度（非逐点细则）", mis="否：未进入正文", need="否", action="HOLD_NO_INSERT_BROAD_ANGLE_ONLY", note="ClaudeCode B弱候选闭合为不插入。"),
        "M0241": dict(status="部分保留：只保留Q16两个总节点", node="联系的普遍性 / 联系的观点（总）；实践与认识（总）", rule="可读源只支持“联系、实践与认识”等宽角度。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="PARTIAL_KEEP_ONLY_BROAD_Q16_TWO_NODES", note="旧四条强细则口径撤回为两个总节点。"),
        "M0242": dict(status="否：Q21继续HOLD不进正文", node="(待定)", rule="Q21只给宽泛综合角度，不能作为当前哲学正文细则证据。", ev="宽泛答案和评分参考角度（非逐点细则）", mis="否：未进入正文", need="否", action="HOLD_NO_INSERT_BROAD_ANGLE_ONLY", note="未来若取得正式细则再处理。"),
        "M0718": dict(status="否：正确项为政治系统表述，不进当前哲学正文", node="中国特色社会主义/道路自信边界", rule="官方答案Q1=D，③④正确；①②为错误项，不能用“人民群众/发展”词面命中进宝典。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_WRONG_OPTION_OR_MODULE_BOUNDARY", note="词面候选关闭。"),
        "M0719": dict(status="是：Batch06补入最终DOCX", node=node_by_q["Q2"], rule="官方答案Q2=C；②支持社会意识反作用于社会存在，③不另拆哲学节点。", ev="选择题官方答案键+题干正确项链条", mis="否", need="否", action=f"Batch06补入：{heading_by_q['Q2']}", note=source_by_q["Q2"]),
        "M0720": dict(status="是：Batch06补入最终DOCX", node=node_by_q["Q3"], rule="官方答案Q3=C；人能创造自然界不存在的艺术形象，支持意识能动创造作用。", ev="选择题官方答案键+题干正确项链条", mis="否", need="否", action=f"Batch06补入：{heading_by_q['Q3']}", note=source_by_q["Q3"]),
        "M0721": dict(status="是：Batch06补入最终DOCX", node=node_by_q["Q4"], rule="官方答案Q4=A；人化联系仍以客观生态规律和客观条件为基础。", ev="选择题官方答案键+题干正确项链条", mis="否", need="否", action=f"Batch06补入：{heading_by_q['Q4']}", note=source_by_q["Q4"]),
        "M0722": dict(status="否：选必三逻辑与思维边界", node="逻辑与思维", rule="官方答案Q6=A，考查类比推理/迁移应用等思维方法，不按必修四哲学进正文。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q6候选关闭。"),
        "M0723": dict(status="否：选必三逻辑与思维边界", node="逻辑与思维", rule="官方答案Q7=A，考查归纳/不完全归纳等逻辑知识，不按必修四哲学进正文。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q7候选关闭。"),
        "M0724": dict(status="否：政治与法治/法律边界", node="政治与法治/法律与生活", rule="官方答案Q8=B，属于法治政府/权力行使等政治法律语境。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q8候选关闭。"),
        "M0725": dict(status="否：法律与生活边界", node="法律与生活", rule="官方答案Q11=D，考查诉讼程序/法律关系，不进当前哲学正文。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q11候选关闭。"),
        "M0726": dict(status="否：经济与社会边界", node="经济与社会", rule="官方答案Q12=D，属于宏观经济/产业或市场语境，不因词面“发展”进入哲学正文。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q12候选关闭。"),
        "M0727": dict(status="否：经济与社会边界", node="经济与社会", rule="官方答案Q13=B，属于社会保险/经济民生语境，不进当前哲学正文。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q13候选关闭。"),
        "M0728": dict(status="否：当代国际政治与经济边界", node="当代国际政治与经济", rule="官方答案Q15=A，属于国际政治经济语境，不进当前哲学正文。", ev="选择题官方答案键+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q15候选关闭。"),
        "M0729": dict(status="是：已由现有两个总节点覆盖", node="联系的普遍性 / 联系的观点（总）；实践与认识（总）", rule="Q16答案和评分参考列“联系、实践与认识”等角度。", ev="答案和评分参考角度（非逐点细则）", mis="否", need="否", action="COVERED_BY_M0025_M0026", note="不新增矛盾/实践基础/认识反作用拆点。"),
        "M0730": dict(status="否：政治与法治边界", node="政治与法治", rule="Q17答案围绕全过程人民民主、政协协商和基层治理，不进必修四哲学正文。", ev="答案和评分参考+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q17候选关闭。"),
        "M0731": dict(status="否：选必三逻辑与思维/法律边界", node="逻辑与思维；法律与生活", rule="Q18(1)分析与综合、联想思维、科学思维；Q18(2)知识产权法律，不进必修四哲学正文。", ev="答案和评分参考+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q18候选关闭。"),
        "M0732": dict(status="否：经济与社会边界", node="经济与社会", rule="Q19答案要求现代化首都都市圈经济意义，不进当前哲学正文。", ev="答案和评分参考+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q19候选关闭。"),
        "M0733": dict(status="否：逻辑与思维/当代国际政治经济边界", node="逻辑与思维；当代国际政治与经济", rule="Q20(1)三段论，Q20(2)全球发展倡议与国际政治经济，不进必修四哲学正文。", ev="答案和评分参考+模块边界", mis="否：未进入正文", need="否", action="EXCLUDE_MODULE_BOUNDARY", note="Q20候选关闭。"),
        "M0734": dict(status="否：宽泛综合角度暂不进正文", node="矛盾的观点/辩证思维", rule="Q21仅列多个可选宽角度，没有提供矛盾观点逐点细则；辩证思维涉及选必三边界。", ev="宽泛答案和评分参考角度（非逐点细则）", mis="否：未进入正文", need="否", action="HOLD_NO_INSERT_BROAD_ANGLE_ONLY", note="Q21不插入。"),
        "M0735": dict(status="否：抽取残片/题号未知，Q1-Q21已逐题闭合", node="(无)", rule="该行是源包整段抽取残片；Batch06已裁决2026海淀二模Q1-Q21。", ev="抽取残片", mis="否：未进入正文", need="否", action="EXCLUDE_EXTRACTION_RESIDUE", note="Qunknown残片关闭。"),
        "M0810": dict(status="套卷已逐题回源闭合", node="SUITE_LEVEL_SUMMARY", rule="Batch06完成Q1-Q21逐题裁决；DOCX现含Q2/Q3/Q4/Q16共5个海淀二模正文条目。", ev="COVERED_OR_PATCHED_WITH_ROW_REVIEW", mis="不适用", need="否", action="BATCH06_SUITE_CLOSED_WITH_ROW_REVIEW", note="不再仅依赖套卷级记录。"),
        "M0850": dict(status="套卷已逐题回源闭合", node="SUITE_LEVEL_SUMMARY", rule="Batch06完成Q1-Q21逐题裁决；新增Q2/Q3/Q4，保留Q16两总节点，Q21 HOLD。", ev="COVERED_OR_PATCHED_WITH_ROW_REVIEW", mis="不适用", need="否", action="BATCH06_SUITE_CLOSED_WITH_ROW_REVIEW", note="full_source_vs_docx套卷镜像行同步关闭。"),
    }

    for row in rows:
        mid = row.get("matrix_row_id", "")
        if mid in updates:
            set_row(row, **updates[mid])

    existing_qs = {(r.get("题源"), r.get("题号")) for r in rows}
    max_id = max(int(r["matrix_row_id"][1:]) for r in rows if r.get("matrix_row_id", "").startswith("M") and r["matrix_row_id"][1:].isdigit())
    missing_boundaries = [
        ("Q5", "逻辑与思维", "官方答案Q5=D，考查概念、判断或逻辑规则，属选必三逻辑与思维边界。"),
        ("Q9", "政治与法治", "官方答案Q9=C，属于基层治理/民主政治语境，不进当前哲学正文。"),
        ("Q10", "法律与生活", "官方答案Q10=A，属于合同或民事法律关系，不进当前哲学正文。"),
        ("Q14", "经济与社会", "官方答案Q14=B，属于外贸/经济发展语境，不进当前哲学正文。"),
    ]
    for q, node, rule in missing_boundaries:
        if (SUITE, q) in existing_qs:
            continue
        max_id += 1
        rows.append(
            {
                "matrix_row_id": f"M{max_id:04d}",
                "row_source": "batch06_codex_added_boundary",
                "题源": SUITE,
                "年份": "2026",
                "阶段": "二模",
                "题号": q,
                "题型或模块判断": "逐题覆盖补充边界行",
                "是否进宝典": "否：模块边界排除",
                "宝典节点": node,
                "细则支持原理": rule,
                "证据等级": "选择题官方答案键+模块边界",
                "是否误放": "否：未进入正文",
                "是否需补厚": "否",
                "当前处理": "EXCLUDE_MODULE_BOUNDARY_ADDED_BY_BATCH06",
                "备注": "Batch06补齐逐题覆盖缺口；此前矩阵没有该题独立边界行。",
                "source_artifact": "01_source_inventory/suite_source_bundles/2026海淀二模.md:1021-1025;1045-1057;1076-1082;1133-1137;1157-1160",
            }
        )

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"MATRIX_BACKUP={backup}")


def write_batch_report(headings: list[str]) -> None:
    report = f"""# Batch06 Coverage Fusion: 2026海淀二模

Status: `RECOVERED_EXECUTION_IN_PROGRESS`

## Source Basis

- Source bundle: `01_source_inventory/suite_source_bundles/2026海淀二模.md`.
- Q1-Q15 official keys: source bundle lines 1133-1137 and 1157-1160.
- Q16 prompt: source bundle lines 1092-1094.
- Q16 answer/scoring-reference angle: source bundle lines 1140-1141 and 1162-1163, plus `2026海淀二模_Q16_readable_evidence.md`.
- Q21 answer/scoring-reference angle: source bundle lines 1154-1155 and 1195-1196.

## Inserted Into DOCX

{chr(10).join(f'- `{h}`' for h in headings)}

## Question-Level Decisions

| Question | Decision |
|---|---|
| Q1 | Excluded. Official key D; correct options are political/system claims. Wrong-option philosophy term hits are invalid. |
| Q2 | Inserted under `社会存在与社会意识`; option ② is supported by official key C. Option ③ is not split into a separate philosophy node. |
| Q3 | Inserted under `主观能动性 / 意识的能动作用`; official key C supports conscious creative construction of artistic images. |
| Q4 | Inserted under `联系的客观性`; official key A supports objective basis of humanized connections. |
| Q5 | Added boundary row; logic/thinking module. |
| Q6 | Excluded; logic/thinking module. |
| Q7 | Excluded; logic/thinking module. |
| Q8 | Excluded; politics/law boundary. |
| Q9 | Added boundary row; politics/law boundary. |
| Q10 | Added boundary row; law boundary. |
| Q11 | Excluded; law boundary. |
| Q12 | Excluded; economics boundary. |
| Q13 | Excluded; economics boundary. |
| Q14 | Added boundary row; economics boundary. |
| Q15 | Excluded; international politics/economics boundary. |
| Q16 | Retained only two broad nodes already in DOCX: `联系的普遍性 / 联系的观点（总）` and `实践与认识（总）`; evidence wording downgraded to answer/scoring-reference angle, not per-point rubric. |
| Q17 | Excluded; politics/law boundary. |
| Q18 | Excluded; logic/thinking and law boundary. |
| Q19 | Excluded; economics boundary. |
| Q20 | Excluded; logic plus international politics/economics boundary. |
| Q21 | HOLD/no insert. The source lists broad angles including `矛盾的观点、辩证思维`; this is not enough to create a concrete philosophy entry. |

## Evidence Rule

No Sonnet/Haiku/model-unknown evidence is used as qualified ClaudeCode evidence. Q16 remains a broad answer/scoring-reference angle, and Q21 remains held because ordinary angle prompts cannot substitute for a detailed scoring rule.
"""
    BATCH_REPORT.write_text(report, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headings = update_docx(timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp)
    update_blocked(timestamp)
    update_matrix(timestamp, headings)
    write_batch_report(headings)
    print("INSERTED_HEADINGS")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
