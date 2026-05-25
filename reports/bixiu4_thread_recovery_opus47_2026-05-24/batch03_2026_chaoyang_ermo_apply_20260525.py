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


RUN_DIR = "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DOCX_BASENAME = "哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"
NS = {"w": W_NS}


ENTRIES = [
    {
        "canonical_node": "价值观的导向作用",
        "source_suite": "2026朝阳二模",
        "question_no": "Q1",
        "heading_suffix": "2026朝阳二模 第1题（选择题）",
        "material_trigger": "材料把“中国路”写成连接山川大地、印证中国式现代化独特路径的现实载体，正确项①又点明“通达之路”联结革命老区，坚持以人民为中心的价值追求。",
        "question_prompt": "关于“中国路”，下列说法正确的是：①“通达之路”联结革命老区，坚持以人民为中心的价值追求；②“创新之路”攻克技术难关，以硬实力夯实高质量发展根基；③“共赢之路”主导全球发展，积极推动构建人类命运共同体；④“奋进之路”传承长征精神，为中国式现代化提供根本遵循。",
        "why_trigger": "能想到价值观，是因为正确项①不是只说道路建设的物理连通，而是把“联结革命老区”同“以人民为中心的价值追求”连在一起。学生看到道路建设服务老区、服务人民、服务中国式现代化时，应当想到价值观对认识和实践具有导向作用。",
        "answer_landing": "正确项是 A（①②）。本节点只处理①：通达之路联结革命老区，体现道路建设和现代化实践受以人民为中心的正确价值观引导；这种价值追求规定了建设为了谁、服务谁、依靠谁，使“中国路”不只是交通工程，也是服务人民美好生活和共同发展的实践路径。",
        "evidence_level": "选择题官方答案键+题干",
    },
    {
        "canonical_node": "实践是认识的基础",
        "source_suite": "2026朝阳二模",
        "question_no": "Q3",
        "heading_suffix": "2026朝阳二模 第3题（选择题）",
        "material_trigger": "材料说“词元”日均调用量两年间增长超千倍，并随着人工智能技术普及逐步走进大众视野，成为人们理解数字时代的重要认知工具。正确项③明确“实践是认识发展的动力，规模化应用促进人们深化对词元价值的认识”。",
        "question_prompt": "词元（Token）是大模型处理信息的最小单元。我国词元日均调用量两年间增长超千倍，这一专业概念也随技术普及逐步走进大众视野，成为人们理解数字时代的重要认知工具。这体现了什么？",
        "why_trigger": "“日均调用量增长”“技术普及”“走进大众视野”不是抽象概念自我展开，而是人工智能规模化应用推动人们认识词元、理解词元、重新把握数字时代。学生看到实践规模扩大带来认识深化，就应想到实践是认识发展的动力。",
        "answer_landing": "正确项是 D（③④）。本节点只处理③：人工智能应用规模扩大，使词元从专业概念进入大众认知，说明实践不断提出新问题、积累新经验、提供新对象，从而推动人们深化对词元价值和数字时代运行方式的认识。",
        "evidence_level": "选择题官方答案键+题干",
    },
    {
        "canonical_node": "社会存在与社会意识",
        "source_suite": "2026朝阳二模",
        "question_no": "Q3",
        "heading_suffix": "2026朝阳二模 第3题（选择题）",
        "material_trigger": "材料把人工智能技术发展、词元调用量增长和“词元”概念普及连在一起，正确项④明确“社会存在决定社会意识，人工智能技术发展催生并普及了‘词元’概念”。",
        "question_prompt": "词元（Token）是大模型处理信息的最小单元。我国词元日均调用量两年间增长超千倍，这一专业概念也随技术普及逐步走进大众视野，成为人们理解数字时代的重要认知工具。这体现了什么？",
        "why_trigger": "能想到社会存在决定社会意识，是因为“词元”这个观念不是凭空流行，而是由人工智能大模型应用、数据处理方式、技术普及等现实社会存在推动出来的。技术和社会生活变化催生新的概念、新的表达和新的理解框架。",
        "answer_landing": "正确项是 D（③④）。本节点只处理④：人工智能技术发展和大规模应用构成新的社会存在，推动“词元”这一专业概念走进大众视野，说明社会意识随着社会存在的变化而产生和发展。",
        "evidence_level": "选择题官方答案键+题干",
    },
    {
        "canonical_node": "联系的多样性",
        "source_suite": "2026朝阳二模",
        "question_no": "Q4",
        "heading_suffix": "2026朝阳二模 第4题（选择题）",
        "material_trigger": "材料写老旧小区引入智慧物业系统，整合门禁、电梯监测、消防预警、垃圾分类监控等模块，既降低运营成本，也提升居民安全感和幸福感。正确项③明确“适应居民生活需求，把握了联系的多样性，提升了社区治理的效能”。",
        "question_prompt": "近年来，北京多个老旧小区引入“智慧物业”管理系统。该系统整合智能门禁、电梯监测、消防预警、垃圾分类监控等多个模块，既降低运营成本，也提升居民的安全感和幸福感。这一做法说明什么？",
        "why_trigger": "智慧物业不是只抓一个孤立设备，而是把安全、通行、消防、垃圾分类、居民需求、运营成本等多种联系一并纳入治理。学生看到多模块、多需求、多效果之间相互作用时，应想到联系具有多样性，必须具体分析不同联系在治理中的作用。",
        "answer_landing": "正确项是 A（①③）。本节点只处理③：老旧小区治理要看到居民安全、生活便利、运营成本和公共服务之间的多样联系，运用智慧物业把这些联系转化为治理效能，才能更精准地满足居民生活需求。",
        "evidence_level": "选择题官方答案键+题干",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "source_suite": "2026朝阳二模",
        "question_no": "Q4",
        "heading_suffix": "2026朝阳二模 第4题（选择题）",
        "material_trigger": "材料中的智慧物业管理系统把智能门禁、电梯监测、消防预警、垃圾分类监控等多个模块整合起来，正确项①明确“立足小区整体，通过数据联动整合治理资源，实现小区精细化管理”。",
        "question_prompt": "近年来，北京多个老旧小区引入“智慧物业”管理系统。该系统整合智能门禁、电梯监测、消防预警、垃圾分类监控等多个模块，既降低运营成本，也提升居民的安全感和幸福感。这一做法说明什么？",
        "why_trigger": "能想到系统观念，是因为材料反复强调“系统”“整合”“多个模块”“数据联动”，治理对象不是一个单点问题，而是小区整体运行。只有把门禁、电梯、消防、垃圾分类和居民需求放进同一个系统中优化组合，才能说明治理效能为什么提升。",
        "answer_landing": "正确项是 A（①③）。本节点只处理①：智慧物业立足小区整体，把不同治理模块和数据资源联动起来，优化小区治理系统的结构和功能，使各部分协同服务社区精细化管理。",
        "evidence_level": "选择题官方答案键+题干",
    },
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def set_plain_text(p: etree._Element, text: str) -> None:
    texts = p.xpath(".//w:t", namespaces=NS)
    if not texts:
        if text == "":
            return
        raise RuntimeError("paragraph has no text nodes")
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


def find_section(paras: list[etree._Element], heading: str, next_heading: str) -> tuple[int, int]:
    start = None
    for idx, p in enumerate(paras):
        if para_text(p).strip() == heading:
            start = idx
            break
    if start is None:
        raise RuntimeError(f"section heading not found: {heading}")
    end = None
    for idx in range(start + 1, len(paras)):
        if para_text(paras[idx]).strip() == next_heading:
            end = idx
            break
    if end is None:
        raise RuntimeError(f"next heading not found after {heading}: {next_heading}")
    return start, end


def insert_entry(root: etree._Element, entry: dict[str, str], next_map: dict[str, str]) -> str:
    body = root.find("w:body", namespaces=NS)
    if body is None:
        raise RuntimeError("word/document.xml has no body")
    paras = [p for p in body if p.tag == W + "p"]
    node = entry["canonical_node"]
    start, end = find_section(paras, node, next_map[node])

    numbered: list[tuple[int, etree._Element, int]] = []
    for idx in range(start + 1, end):
        text = para_text(paras[idx]).strip()
        m = re.match(r"^(\d+)\.\s", text)
        if m:
            numbered.append((idx, paras[idx], int(m.group(1))))
    if not numbered:
        raise RuntimeError(f"no numbered item in section {node}")

    last_idx, _, last_no = numbered[-1]
    block_end = end
    for idx in range(last_idx + 1, end):
        if re.match(r"^\d+\.\s", para_text(paras[idx]).strip()):
            block_end = idx
            break
    template_block = [deepcopy(p) for p in paras[last_idx:block_end]]
    if len(template_block) < 5:
        raise RuntimeError(f"template block too short for {node}: {len(template_block)}")

    new_no = last_no + 1
    heading = f"{new_no}. {entry['heading_suffix']}"
    set_plain_text(template_block[0], heading)
    labels = [
        ("【材料触发点】", entry["material_trigger"]),
        ("【设问】", entry["question_prompt"]),
        ("【为什么能想到】", entry["why_trigger"]),
        ("【答案落点】", entry["answer_landing"]),
    ]
    for p, (label, rest) in zip(template_block[1:5], labels):
        set_label_text(p, label, rest)
    if len(template_block) > 5:
        set_plain_text(template_block[5], "")

    ref = paras[end]
    for p in template_block:
        body.insert(body.index(ref), p)
    return heading


def update_docx(docx_path: Path, timestamp: str) -> list[str]:
    backup = docx_path.with_name(
        f"{docx_path.stem}_backup_before_2026_chaoyang_ermo_choice_insert_{timestamp}.docx"
    )
    shutil.copy2(docx_path, backup)

    next_map = {
        "联系的多样性": "整体与部分",
        "系统观念 / 系统优化": "发展的观点 / 发展的普遍性",
        "实践是认识的基础": "认识对实践的反作用",
        "社会存在与社会意识": "社会发展的两大基本规律和基本矛盾",
        "价值观的导向作用": "价值判断与价值选择",
    }

    with zipfile.ZipFile(docx_path, "r") as zin:
        infos = zin.infolist()
        entries = {info.filename: zin.read(info.filename) for info in infos}
    root = etree.fromstring(entries["word/document.xml"])

    headings = []
    for entry in ENTRIES:
        headings.append(insert_entry(root, entry, next_map))

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
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
            zout.writestr(zi, entries[info.filename])
    shutil.move(str(tmp_path), docx_path)
    print(f"DOCX_BACKUP {backup}")
    return headings


def append_ledger(ledger_path: Path, headings: list[str], timestamp: str) -> None:
    backup = ledger_path.with_name(f"docx_insert_ledger_backup_before_batch03_chaoyang_ermo_{timestamp}.csv")
    shutil.copy2(ledger_path, backup)
    existing = set()
    with ledger_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        for row in rows:
            existing.add((row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"]))

    new_rows = []
    for entry, heading in zip(ENTRIES, headings):
        row = {
            "canonical_node": entry["canonical_node"],
            "source_suite": entry["source_suite"],
            "question_no": entry["question_no"],
            "inserted_heading": heading,
        }
        key = (row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in existing:
            new_rows.append(row)

    rows.extend(new_rows)
    with ledger_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"LEDGER_BACKUP {backup}")
    print(f"LEDGER_APPENDED {len(new_rows)}")


def append_jsonl(jsonl_path: Path, timestamp: str) -> None:
    backup = jsonl_path.with_name(f"{jsonl_path.stem}_backup_before_batch03_chaoyang_ermo_{timestamp}{jsonl_path.suffix}")
    shutil.copy2(jsonl_path, backup)
    with jsonl_path.open("a", encoding="utf-8", newline="\n") as f:
        for entry in ENTRIES:
            payload = {
                "source_suite": entry["source_suite"],
                "question_no": entry["question_no"],
                "framework_node": entry["canonical_node"],
                "canonical_node": entry["canonical_node"],
                "material_trigger": entry["material_trigger"],
                "question_prompt": entry["question_prompt"],
                "why_trigger": entry["why_trigger"],
                "answer_landing": entry["answer_landing"],
                "evidence_level": entry["evidence_level"],
                "boundary_note": "选择题正确选项链；不是主观题逐点评分细则。",
                "source_lane": "Codex Batch03 2026朝阳二模",
                "source_repair_basis": "2026朝阳二模 source bundle lines 182-205, 271-300, 484-524; choice answer key and rubric/stem cross-check.",
            }
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    print(f"JSONL_BACKUP {backup}")
    print(f"JSONL_APPENDED {len(ENTRIES)}")


def update_matrix(matrix_path: Path, timestamp: str) -> None:
    backup = matrix_path.with_name(
        f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch03_2026_chaoyang_ermo_{timestamp}.csv"
    )
    shutil.copy2(matrix_path, backup)
    col_in = "是否进宝典"
    col_node = "宝典节点"
    col_principle = "细则支持原理"
    col_evidence = "证据等级"
    col_misplaced = "是否误放"
    col_need = "是否需补厚"
    col_current = "当前处理"
    col_note = "备注"

    decisions = {
        "M0151": ("是：已在最终DOCX覆盖（无需新增）", "Q16：矛盾/联系/辩证否定或发展/具体问题具体分析/价值观", "source bundle lines 123-148 and 505-524 give Q16 detailed scoring dimensions.", "强细则", "否", "否", "Batch03回源闭合：保留现有Q16多节点条目。"),
        "M0152": ("是：已在最终DOCX覆盖（无需新增）", "Q21：系统观念/量变质变", "source bundle lines 424-440 give Q21 system thinking, strategic persistence, quantity-quality and required leadership points.", "强细则", "否", "否", "Batch03回源闭合：保留现有Q21系统与量变条目。"),
        "M0698": ("是：Batch03补入最终DOCX", "价值观的导向作用", "source bundle lines 182-188 plus answer key line 484: Q1=A, correct option ① names people-centered value pursuit.", "选择题官方答案键+题干", "否", "否", "Batch03新增选择题正确选项链。"),
        "M0699": ("否：文化线/非遗选择题，不入当前哲学宝典", "-", "source bundle lines 189-193 plus answer key line 484: Q2=B; culture-line protection/use of intangible heritage.", "选择题官方答案键+模块边界", "否：候选未入正文", "否：当前哲学宝典不补；文化线另审", "Batch03边界排除。"),
        "M0700": ("是：Batch03补入最终DOCX", "实践是认识的基础/社会存在与社会意识", "source bundle lines 194-199 plus answer key line 484: Q3=D, correct options ③实践推动认识发展 and ④社会存在决定社会意识.", "选择题官方答案键+题干", "否", "否", "Batch03新增两个选择题正确选项链。"),
        "M0701": ("是：Batch03补入最终DOCX", "联系的多样性/系统观念", "source bundle lines 200-205 plus answer key line 484: Q4=A, correct options ①立足整体/数据联动 and ③联系多样性.", "选择题官方答案键+题干", "否", "否", "Batch03新增两个选择题正确选项链。"),
        "M0702": ("否：正确项为形象思维/翻译鉴赏，辩证否定为误触发", "-", "source bundle lines 206-211 plus answer key line 484: Q5=C; correct options are ② and ④, not ③辩证否定.", "选择题官方答案键+误触发排除", "否：候选未入正文", "否", "Batch03排除误触发。"),
        "M0703": ("否：选必三逻辑推理，不入必修四哲学宝典", "-", "source bundle lines 212-216 plus answer key line 484: Q6=D; conditional/inference judgment.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0704": ("否：选必三创新思维；次要矛盾为错项", "-", "source bundle lines 217-221 plus answer key line 484: Q7=D; correct option is innovation thinking, not C次要矛盾.", "选择题官方答案键+模块边界", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0705": ("否：政治与法治/人大代表情境，不入当前哲学宝典", "-", "source bundle lines 222-227 plus answer key line 484: Q8=B.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0706": ("否：文化与法治交叉选择题，不入当前哲学节点", "-", "source bundle lines 228-233 plus answer key line 484: Q9=A; culture practice plus legal promotion, not current philosophy node.", "选择题官方答案键+模块边界", "否：候选未入正文", "否：文化线另审", "Batch03边界排除。"),
        "M0707": ("否：法律/婚姻家庭选择题，不入当前哲学宝典", "-", "source bundle line 234 and answer key line 484: Q10=C.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0708": ("否：法律与生活/劳动合同，不入当前哲学宝典", "-", "source bundle line 235 and answer key line 484: Q11=D.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0709": ("否：经济与社会/城市经济，不入当前哲学宝典", "-", "source bundle line 240 and answer key line 484: Q12=B.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0710": ("否：经济与社会/新业态，不入当前哲学宝典", "-", "source bundle line 247 and answer key line 484: Q13=C.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0711": ("否：规划指标/经济治理选择题，不入当前哲学宝典", "-", "source bundle line 254 and answer key line 484: Q14=B.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0712": ("否：当代国际政治与经济/国际组织，不入当前哲学宝典", "-", "source bundle line 263 and answer key line 484: Q15=C.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0713": ("是：已在最终DOCX覆盖（无需新增）", "Q16：矛盾/联系/辩证否定或发展/具体问题具体分析/价值观", "source bundle lines 123-148 and 505-524 give Q16 detailed scoring dimensions.", "强细则", "否", "否", "Batch03回源闭合：Q16已覆盖。"),
        "M0714": ("否：Q19为选必三逻辑+经济与社会，不入当前哲学宝典", "-", "source bundle lines 285-291 and 377-396: Q19(1)逻辑与思维，Q19(2)经济与社会.", "模块边界明确", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0715": ("否：Q20主链为当代国际政治与经济；哲学思维只是可酌情表达", "-", "source bundle lines 292-297 and 401-414; line 409 mentions optional 对立统一 only as supplemental thinking, not current philosophy scoring mainline.", "模块边界明确/哲学可酌情非主链", "否：候选未入正文", "否", "Batch03边界排除。"),
        "M0716": ("是：已在最终DOCX覆盖（无需新增）", "Q21：系统观念/量变质变", "source bundle lines 424-440 give Q21 system thinking, strategic persistence, quantity-quality and required leadership points.", "强细则", "否", "否", "Batch03回源闭合：Q21已覆盖。"),
        "M0717": ("否：抽取残片/题号未知，不入当前哲学宝典", "-", "Qunknown is extraction residue; Q1-Q21 have been independently reviewed in Batch03.", "抽取错误", "否：候选未入正文", "否", "Batch03排除残片。"),
    }

    with matrix_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = reader.fieldnames
    if fields is None:
        raise RuntimeError("matrix header missing")
    touched = []
    for row in rows:
        mid = row.get("matrix_row_id")
        if mid in decisions:
            row[col_in], row[col_node], row[col_principle], row[col_evidence], row[col_misplaced], row[col_need], row[col_current] = decisions[mid]
            row[col_note] = (row.get(col_note, "") + "；" if row.get(col_note) else "") + "Batch03 2026朝阳二模逐题回源裁决。"
            touched.append(mid)
    missing = sorted(set(decisions) - set(touched))
    if missing:
        raise RuntimeError(f"matrix ids not found: {missing}")
    with matrix_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"MATRIX_BACKUP {backup}")
    print(f"MATRIX_TOUCHED {len(touched)}")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    root = repo_root()
    run = root / "reports" / RUN_DIR
    delivery = run / "05_delivery"
    docx = delivery / DOCX_BASENAME
    ledger = delivery / "docx_insert_ledger.csv"
    jsonl = run / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
    matrix = root / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24" / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
    for path in [docx, ledger, jsonl, matrix]:
        if not path.exists():
            raise FileNotFoundError(path)
    headings = update_docx(docx, ts)
    append_ledger(ledger, headings, ts)
    append_jsonl(jsonl, ts)
    update_matrix(matrix, ts)
    print("INSERTED_HEADINGS")
    for h in headings:
        print(h)


if __name__ == "__main__":
    main()
