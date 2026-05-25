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

SUITE = "2026石景山二模"

ENTRIES = [
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q1",
        "heading_suffix": "2026石景山二模 第1题（选择题）",
        "material_trigger": "材料写“十五五”规划部署6方面109项重大工程，正确项②明确推进中国式现代化是一个系统工程，需要统筹兼顾、系统谋划、整体推动。",
        "question_prompt": "十四届全国人大四次会议批准了关于国民经济和社会发展第十五个五年规划纲要。由此带来的启示是：①党的主张可以通过法定程序转化为国家意志和全体人民的共同行动；②推进中国式现代化是一个系统工程，需要统筹兼顾、系统谋划、整体推动；③应把握事物发展过程的渐进性与飞跃性，不失时机跨越历史条件实现现代化；④国家规划能直接谋划推动改革创新，实现马克思主义中国化时代化新的飞跃。",
        "why_trigger": "能想到系统观念，是因为正确项②直接把中国式现代化说成“系统工程”，并用“统筹兼顾、系统谋划、整体推动”描述方法。学生看到多任务、多工程、多领域协同推进时，应想到要从整体上把握结构和功能，避免把现代化建设拆成孤立事项。",
        "answer_landing": "正确项是A（①②）。本节点只处理②：推进中国式现代化要坚持系统观念，把经济社会发展各领域、各工程、各环节放到整体中统筹谋划，使局部任务服务强国建设和民族复兴的整体目标。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026石景山二模 source bundle lines 17-19, 116-121, 225-227.",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q2",
        "heading_suffix": "2026石景山二模 第2题（选择题）",
        "material_trigger": "材料写立体剪纸既保留传统剪纸技法，又融入数字投影技术呈现抗战英雄人物和重要抗战场景。正确项④明确“艺术性与思想性的对立属性寓于剪纸作品的统一属性中”。",
        "question_prompt": "抗战胜利80周年之际，一些非遗传承人以“剪忆抗战”为主题创作系列立体剪纸作品，既保留传统剪纸的阴阳镂空、千剪不断的连纹技法，又融入数字投影技术呈现动态抗战英雄人物、重要抗战场景。作品通过“破纸重生”工艺生动展现抗战历史，引导人们铭记历史，珍爱和平。据此，下列理解正确的是：①立体抗战剪纸是对传统剪纸中合理因素的辩证否定；②剪纸作品承载并传递着以爱国主义为核心的民族精神；③剪纸作品是根据抗战纪念需要建立起的人为事物的联系；④艺术性与思想性的对立属性寓于剪纸作品的统一属性中。",
        "why_trigger": "能想到矛盾对立统一，是因为正确项④直接出现“对立属性”和“统一属性”。艺术性和思想性不是彼此隔绝的两件事：剪纸的艺术形式承载抗战记忆，思想内容又通过艺术形式表达出来，二者在同一作品中相互依存。",
        "answer_landing": "正确项是D（②④）。本节点只处理④：抗战剪纸把艺术表达和思想教育统一起来，说明矛盾双方既有区别又相互依存，艺术性与思想性在同一作品中实现对立统一。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026石景山二模 source bundle lines 17-19, 122-127, 225-227.",
    },
    {
        "canonical_node": "整体与部分",
        "question_no": "Q3",
        "heading_suffix": "2026石景山二模 第3题（选择题）",
        "material_trigger": "题干说明“致广大而尽精微”包含大与小的辩证法，正确项①强调立足推进中国式现代化的大局谋划地区工作，正确项③强调以“绣花功夫”把改革发展各项工作做扎实、做到位。",
        "question_prompt": "“致广大而尽精微”语出《中庸》，意思是：既要致力于达到广博深厚的境界，又要尽心于精细微妙之处。这句话包含大与小的辩证法，又是为政、修身的方法论。以下做法符合其理念的是：①立足推进中国式现代化的大局谋划地区工作，因地制宜、精准发力；②重视“微”，群众利益无小事，从细节着手，做到“眉毛胡子一把抓”；③注重“精”，以“绣花功夫”把改革发展各项工作做扎实、做到位；④做到“尽”，防止过犹不及，做到得中而处，把握好事物发展的度。",
        "why_trigger": "能想到整体与部分，是因为正确项①要求立足“大局”，正确项③要求把具体工作做扎实，二者把全局目标和具体环节联系起来。学生看到“大局谋划”和“精微落实”同时出现，应想到既要着眼整体，又要重视局部和细节对整体目标的支撑作用。",
        "answer_landing": "正确项是B（①③）。本节点处理整体与部分：地区工作既要服务中国式现代化这个整体大局，又要把每一项具体改革发展任务做扎实，以局部落实支撑整体推进。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026石景山二模 source bundle lines 17-19, 128-133, 225-227.",
    },
    {
        "canonical_node": "矛盾的特殊性 / 具体问题具体分析",
        "question_no": "Q3",
        "heading_suffix": "2026石景山二模 第3题（选择题）",
        "material_trigger": "正确项①说“因地制宜、精准发力”，把地区工作放到本地实际条件中处理，而不是套用一个抽象方案。",
        "question_prompt": "“致广大而尽精微”语出《中庸》，意思是：既要致力于达到广博深厚的境界，又要尽心于精细微妙之处。这句话包含大与小的辩证法，又是为政、修身的方法论。以下做法符合其理念的是：①立足推进中国式现代化的大局谋划地区工作，因地制宜、精准发力；②重视“微”，群众利益无小事，从细节着手，做到“眉毛胡子一把抓”；③注重“精”，以“绣花功夫”把改革发展各项工作做扎实、做到位；④做到“尽”，防止过犹不及，做到得中而处，把握好事物发展的度。",
        "why_trigger": "能想到具体问题具体分析，是因为正确项①直接写“因地制宜、精准发力”。不同地区的发展基础、资源禀赋、任务重点不同，不能用同一模板推进，而要分析本地矛盾的特殊性。",
        "answer_landing": "正确项是B（①③）。本节点只处理①中的“因地制宜”：谋划地区工作要具体分析本地区实际和发展任务，把中国式现代化的大局要求转化为适合本地条件的精准举措。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026石景山二模 source bundle lines 17-19, 128-133, 225-227.",
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q9",
        "heading_suffix": "2026石景山二模 第9题（选择题）",
        "material_trigger": "材料要求树立和践行正确政绩观，正确项③说政绩不是喊出来的，要扎根实际、躬身力行；正确项④说政绩要经得起实践、人民、历史的检验。",
        "question_prompt": "在“十五五”开局之年，党中央决定在全党开展树立和践行正确政绩观学习教育，引导广大党员干部落实“立党为公、为民造福、科学决策、真抓实干”总要求，创造经得起实践、人民、历史检验的实绩。对此，理解正确的是：①政绩为谁而树——坚定理想信仰，为实现共产主义共同理想而奋斗；②树什么样的政绩——做群众看得见的“显绩”而不是利长远的“潜绩”；③靠什么树政绩——政绩从来不是喊出来的，要扎根实际、躬身力行；④如何检验政绩——政绩要能经得起实践、人民、历史的检验。",
        "why_trigger": "能想到实践，是因为正确项③反对空喊，强调扎根实际、躬身力行；正确项④明确把实践作为检验政绩的重要尺度。学生看到“不是喊出来的”“经得起实践检验”，应想到实践是认识的来源、动力和检验标准，正确政绩观必须落到真实行动和实际成效上。",
        "answer_landing": "正确项是D（③④）。本节点处理实践标准：政绩不能停留在口号和主观愿望中，而要在实际工作中形成、在人民生活改善和社会发展实践中接受检验。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026石景山二模 source bundle lines 17-19, 158-163, 225-227.",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q9",
        "heading_suffix": "2026石景山二模 第9题（选择题）",
        "material_trigger": "材料把政绩观同“立党为公、为民造福”相连，正确项④明确政绩要经得起“人民”的检验。",
        "question_prompt": "在“十五五”开局之年，党中央决定在全党开展树立和践行正确政绩观学习教育，引导广大党员干部落实“立党为公、为民造福、科学决策、真抓实干”总要求，创造经得起实践、人民、历史检验的实绩。对此，理解正确的是：①政绩为谁而树——坚定理想信仰，为实现共产主义共同理想而奋斗；②树什么样的政绩——做群众看得见的“显绩”而不是利长远的“潜绩”；③靠什么树政绩——政绩从来不是喊出来的，要扎根实际、躬身力行；④如何检验政绩——政绩要能经得起实践、人民、历史的检验。",
        "why_trigger": "能想到人民群众，是因为题干和正确项都把政绩评价交给人民和历史，而不是只看个人声望或短期显绩。人民群众是社会历史的主体，政绩最终要看是否真正服务人民、是否经得起人民检验。",
        "answer_landing": "正确项是D（③④）。本节点处理人民群众标准：树立正确政绩观必须坚持人民主体地位，把为民造福作为出发点和落脚点，让工作成效经得起人民检验。",
        "evidence_level": "选择题官方答案键+题干正确项链条",
        "source_lines": "2026石景山二模 source bundle lines 17-19, 158-163, 225-227.",
    },
]


SECTION_NEXT = {
    "整体与部分": "系统观念 / 系统优化",
    "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
    "矛盾就是对立统一": "矛盾的普遍性",
    "矛盾的特殊性 / 具体问题具体分析": "矛盾的普遍性和特殊性",
    "实践是认识的基础": "认识对实践的反作用",
    "人民群众": "价值观的导向作用",
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
        if text == "":
            return
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

    numbered = []
    for idx in range(start + 1, end):
        text = para_text(paras[idx]).strip()
        m = re.match(r"^(\d+)\.\s", text)
        if m:
            numbered.append((idx, int(m.group(1))))
    if not numbered:
        raise RuntimeError(f"no numbered items under {entry['canonical_node']}")

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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_shijingshan_ermo_batch04_{timestamp}.docx")
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
    backup = LEDGER.with_name(f"docx_insert_ledger_backup_before_batch04_shijingshan_ermo_{timestamp}.csv")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fieldnames = f.seek(0) or csv.DictReader(f).fieldnames
    if fieldnames is None:
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


def update_accepted(timestamp: str) -> None:
    backup = ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch04_shijingshan_ermo_{timestamp}.jsonl")
    shutil.copy2(ACCEPTED, backup)
    items = []
    for line in ACCEPTED.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        if item.get("source_suite") == SUITE and item.get("question_no") == "Q17(3)":
            item["evidence_level"] = "正式评分参考角度"
            item["boundary_note"] = "答案评分参考允许联系、矛盾、实践与认识等角度任选展开；本条为可选路径，不代表三项累计得分，不标为逐点评分强细则。"
            item["source_repair_basis"] = "2026石景山二模 source bundle lines 49-71: 第17(3)可从联系、矛盾、实践与认识关系等角度回答。"
        items.append(item)

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
            "boundary_note": f"选择题只按官方答案键和正确项链条进入；{entry['source_lines']}",
            "source_lane": "Codex Batch04 2026石景山二模",
            "source_repair_basis": entry["source_lines"],
        }
        key = (item["source_suite"], item["question_no"], item["canonical_node"], item["material_trigger"])
        if key not in existing:
            items.append(item)

    ACCEPTED.write_text("\n".join(json.dumps(i, ensure_ascii=False) for i in items) + "\n", encoding="utf-8")
    print(f"ACCEPTED_BACKUP={backup}")


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch04_2026_shijingshan_ermo_{timestamp}.csv"
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise RuntimeError("matrix has no header")
        rows = list(reader)

    k_id = "matrix_row_id"
    k_in = "是否进宝典"
    k_node = "宝典节点"
    k_rule = "细则支持原理"
    k_ev = "证据等级"
    k_mis = "是否误放"
    k_need = "是否需补厚"
    k_action = "当前处理"
    k_note = "备注"

    insert_by_q = {}
    for entry, heading in zip(ENTRIES, headings):
        insert_by_q.setdefault(entry["question_no"], []).append((entry["canonical_node"], heading, entry["source_lines"]))

    updates = {
        "M0155": ("是：已在最终DOCX覆盖（无需新增）", "联系的普遍性 / 联系的观点（总）；矛盾就是对立统一；实践与认识（总）", "答案评分参考第17(3)明确可从联系、矛盾、实践与认识关系等角度回答；仅为任选路径，不作累加采分。", "正式评分参考角度", "否", "否", "Batch04回源闭合：既有三条任选路径已覆盖，证据标签降格。"),
        "M0244": ("是：已在最终DOCX覆盖（无需新增）", "联系的普遍性 / 联系的观点（总）；矛盾就是对立统一；实践与认识（总）", "答案评分参考第17(3)明确可从联系、矛盾、实践与认识关系等角度回答；仅为任选路径，不作累加采分。", "正式评分参考角度", "否", "否", "Batch04回源闭合：既有三条任选路径已覆盖，证据标签降格。"),
        "M0156": ("否：综合题宽泛可选角度不足以入当前哲学正文", "系统观念 / 系统优化（仅宽泛可选角度）", "第20题为综合运用所学，答案评分参考仅列制度优势、高质量发展、文化强国建设、系统观等宽泛角度；无具体哲学材料链，暂不入正文。", "宽泛角度提示", "否", "否", "Batch04边界排除：不把宽泛参考角度冒充具体评分细则。"),
        "M0739": ("否：文化与科技融合题，当前哲学主线不补", "文化线边界", "Q4官方答案C对应②③，主要为文化科技融合、文化遗产数字化共享；不落当前哲学方法论节点。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0740": ("否：选必三思维/文化传播边界", "选必三辩证思维与创新思维；文化线", "Q5官方答案C对应②③；③为辩证思维和创新思维，属于选必三思维线，不入当前哲学宝典。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0741": ("否：选必三形象思维边界", "选必三逻辑与思维", "Q6官方答案D，考查联想、想象等思维形态，属于选必三逻辑与思维。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0742": ("否：选必三逻辑规则边界", "选必三逻辑与思维", "Q7官方答案B，考查同一律/食品标签概念误导，属于逻辑规则。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0743": ("否：政治与法治基层治理边界", "政治与法治", "Q8官方答案D，对应基层群众自治与社区治理效能，非当前哲学正文节点。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0745": ("否：法律与生活边界", "法律与生活", "Q11官方答案B，劳动关系与劳动仲裁/工伤认定法律问题。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0746": ("否：法律与生活边界", "法律与生活", "Q12官方答案A，著作权侵权法律问题。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0747": ("否：经济与社会边界", "经济与社会", "Q13官方答案A，长期护理保险与社会保障体系。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0748": ("否：经济与社会边界", "经济与社会", "Q14官方答案A，首发经济、市场供给与消费潜力。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0749": ("否：当代国际政治与经济边界", "当代国际政治与经济", "Q15官方答案D，国际供应链促进博览会与开放合作。", "选择题官方答案键+模块边界", "否", "否", "Batch04边界排除。"),
        "M0750": ("否：经济与社会边界", "经济与社会", "Q16设问明确运用《经济与社会》阐释农业政策稳中求进。", "答案评分参考+模块边界", "否", "否", "Batch04边界排除。"),
        "M0751": ("部分覆盖：Q17(3)已入最终DOCX；Q17(1)(2)不入当前哲学正文", "Q17(3)：联系/矛盾/实践与认识；Q17(1)：政治与法治；Q17(2)：选必三辩证思维", "第17(3)答案评分参考明确可从联系、矛盾、实践与认识关系等角度回答；第17(1)为政治与法治，第17(2)为逻辑与思维。", "正式评分参考角度+模块边界", "否", "否", "Batch04回源闭合：只保留Q17(3)任选哲学路径。"),
        "M0752": ("否：当代国际政治与经济边界", "当代国际政治与经济", "Q18设问明确运用《当代国际政治与经济》，答案围绕国家利益、经济全球化、中国东盟合作。", "答案评分参考+模块边界", "否", "否", "Batch04边界排除。"),
        "M0753": ("否：法律与生活边界", "法律与生活", "Q19设问明确运用《法律与生活》，围绕民法典、治安管理处罚法、未成年人校园欺凌。", "答案评分参考+模块边界", "否", "否", "Batch04边界排除。"),
        "M0754": ("否：综合题宽泛可选角度不足以入当前哲学正文", "系统观念 / 系统优化（仅宽泛可选角度）", "第20题为综合运用所学，答案评分参考仅列系统观等宽泛角度，无具体哲学材料链，暂不入正文。", "宽泛角度提示", "否", "否", "Batch04边界排除：不把宽泛参考角度冒充具体评分细则。"),
        "M0755": ("否：抽取残片/题号未知，不入当前哲学宝典", "无", "Qunknown为抽取残片；Q1-Q20已逐题处理。", "抽取残片", "否", "否", "Batch04残片闭合。"),
    }

    inserted_rows = {
        "M0736": ("Q1", "是：Batch04补入最终DOCX"),
        "M0737": ("Q2", "是：Batch04补入最终DOCX（仅哲学正确项④；民族精神②属文化线）"),
        "M0738": ("Q3", "是：Batch04补入最终DOCX"),
        "M0744": ("Q9", "是：Batch04补入最终DOCX"),
    }
    for row in rows:
        row_id = row.get(k_id)
        if row_id in inserted_rows:
            q, status = inserted_rows[row_id]
            data = insert_by_q[q]
            row[k_in] = status
            row[k_node] = "；".join(node for node, _, _ in data)
            row[k_rule] = "；".join(src for _, _, src in data)
            row[k_ev] = "选择题官方答案键+题干正确项链条"
            row[k_mis] = "否"
            row[k_need] = "否"
            row[k_action] = f"Batch04补入：{'；'.join(h for _, h, _ in data)}"
            row[k_note] = (row.get(k_note, "") + "；" if row.get(k_note) else "") + "2026石景山二模逐题回源裁决。"
        elif row_id in updates:
            row[k_in], row[k_node], row[k_rule], row[k_ev], row[k_mis], row[k_need], row[k_action] = updates[row_id]
            row[k_note] = (row.get(k_note, "") + "；" if row.get(k_note) else "") + "2026石景山二模Batch04闭合。"

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
    update_matrix(timestamp, headings)
    print("INSERTED_HEADINGS")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
