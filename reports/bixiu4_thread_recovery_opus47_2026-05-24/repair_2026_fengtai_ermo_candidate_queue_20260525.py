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
REPORT_MD = RECOVERY / "FENGTAI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "FENGTAI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026丰台二模"
YEAR = "2026"
STAGE = "二模"
ROW_SOURCE = "codex_recovery_20260525_fengtai_2026_ermo_repair"

DESKTOP = Path.home() / "Desktop"
ANSWER_DOCX = next(p for p in DESKTOP.rglob("*.docx") if SUITE in str(p) and "答案" in p.name)
PAPER_PDF = next(p for p in DESKTOP.rglob("*.pdf") if SUITE in str(p) and "政治" in p.name)
RUBRIC_PPT = next(p for p in DESKTOP.rglob("*.pptx") if SUITE in str(p) and "阅卷细则" in p.name)

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "整体与部分",
        "question_no": "Q4",
        "heading_suffix": "2026丰台二模 第4题（选择题）",
        "material_trigger": "材料写龙骨水车由摇柄、木链、刮板、水槽等部分组成，并通过链传动把河水引入农田、提取海水析盐；官方答案键第4题为C，对应正确项②③，其中③明确“依托各部件有序联动形成提水功能，使整体功能大于各部分功能之和”。",
        "question_prompt": "龙骨水车作为链传动刮板式提水工具，如何理解“部件有序联动”形成整体功能？本题正确组合为C（②③）。",
        "why_trigger": "看到“各部件有序联动”“形成提水功能”“整体功能大于各部分功能之和”，应定位整体与部分关系：整体由部分构成，部分以合理结构形成合力时，整体功能可以大于部分功能之和；不能把价值大小说成只取决于自身属性，也不能把特殊性寓于普遍性倒置。",
        "answer_landing": "本题应选C。龙骨水车不是零散部件的简单相加，而是通过摇柄、木链、刮板、水槽等部分按一定结构发生联系，形成提水、灌溉、析盐等整体功能；正确项③服务于“整体与部分/系统优化”链条，正确项②作为实践智慧补充，错误项①和④不进入正文链条。",
        "evidence_level": "官方答案键+试卷题干正确项链条（选择题，非主观题评分细则）",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q5",
        "heading_suffix": "2026丰台二模 第5题（选择题）",
        "material_trigger": "材料列举“爱竹咏怀、画竹喻节、以竹明志”，说明诗人、画家、士人借竹寄托风骨、品格和追求；官方答案键第5题为D，对应正确项②④，其中④明确竹的美好寓意“是人脑对竹子进行加工与改造的主观映象”。",
        "question_prompt": "竹的美好寓意如何由客观竹子转化为文化象征和主观映象？本题正确组合为D（②④）。",
        "why_trigger": "看到“咏竹言志、描竹写意、栽竹自勉”，应想到意识不是对客观对象的机械复写，而是人在社会文化实践中对竹子的特点进行能动加工、改造和表达；同时，文化象征不能脱离竹的客观特点凭空产生。",
        "answer_landing": "本题应选D。竹的美好寓意既以竹自身形态、气节等客观特点为基础，又经过创作者审美、价值追求和文化传统的加工，成为人脑对竹子能动反映的主观映象。①把来源误归为创作者素养，③把审美象征误说成揭示本质属性，均不作为正文链条。",
        "evidence_level": "官方答案键+试卷题干正确项链条（选择题，非主观题评分细则）",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q6",
        "heading_suffix": "2026丰台二模 第6题（选择题）",
        "material_trigger": "材料写“燕子归来”在经典诗词中被赋予早春生机、春日和暖、时光流转等丰富内涵；官方答案键第6题为D，正确项为“是人们对春日生机的反映，体现了思维的能动性”。",
        "question_prompt": "文学作品中的“燕子归来”意象体现了意识对客观春日景象的什么作用？本题正确答案为D。",
        "why_trigger": "看到同一自然现象在诗词中形成不同意象，应想到意识具有能动性：人能够在客观事物基础上进行概括、选择、加工和表达；但不能脱离客观现实，也不能把文学意象等同于直接揭示本质必然联系。",
        "answer_landing": "本题应选D。燕子归来的文学意象来源于现实春日景象，又经过人的审美加工，反映春日生机和时光流转，说明思维能够能动地反映客观世界。A夸大为直接揭示本质必然联系，B误写主客观相互转化，C误写脱离客观现实，均应排除。",
        "evidence_level": "官方答案键+试卷题干正确项链条（选择题，非主观题评分细则）",
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q7",
        "heading_suffix": "2026丰台二模 第7题（选择题）",
        "material_trigger": "材料写可控核聚变研究在EAST与环流三号两大实验装置上实现上亿摄氏度运行，科研团队在二十余年研制迭代中突破核心技术、攻克物理难题；官方答案键第7题为D，对应正确项③④，其中④为“在科研实践中解决实际难题，会不断深化人们对规律的认识”。",
        "question_prompt": "可控核聚变实验装置的研制与迭代如何体现实践与认识的关系？本题正确组合为D（③④）。",
        "why_trigger": "看到“实验装置”“科研实践”“攻克难题”“为后续科研奠定基础”，应定位实践是认识发展的动力和检验、深化认识的基础：科学认识规律不是凭空获得，而是在解决实际难题的实践中不断推进。",
        "answer_landing": "本题应选D。可控核聚变研究通过实验装置和技术攻关不断解决现实难题，使人们对核聚变规律的认识持续深化，并为后续科研提供实践基础。③作为能源安全方向保留，④进入实践与认识链条；①把科技创新说成社会发展的根本动力且彻底否定既有成果，②把发展片面归结为量变，均不进入正文链条。",
        "evidence_level": "官方答案键+试卷题干正确项链条（选择题，非主观题评分细则）",
    },
    {
        "canonical_node": "主要矛盾和次要矛盾",
        "question_no": "Q22",
        "heading_suffix": "2026丰台二模 第22题（主观题）",
        "material_trigger": "题干引用“建设社会主义现代化强国，关键在科技自立自强”，材料分“强国之基、领航定向、实践路径”说明科技事业成就、规划纲要和关键核心技术攻关；阅卷PPT第60-64页列出本题可从唯物辩证法等角度作答，并在哲学角度中明示“主要矛盾、系统观念、联系、创新、生产力”。",
        "question_prompt": "综合运用所学，谈谈对“建设社会主义现代化强国，关键在科技自立自强”的理解。",
        "why_trigger": "看到设问中的“关键”以及材料中“聚焦关键领域与产业链薄弱环节攻坚关键核心技术”，应想到抓主要矛盾、抓重点：在强国建设这个复杂系统中，科技自立自强是牵动现代化建设全局的重要环节。注意，本题为综合论述题，PPT给的是哲学角度提示和等级描述，不是逐点固定采分细则。",
        "answer_landing": "可从主要矛盾角度作答：建设社会主义现代化强国任务复杂，要抓住科技自立自强这个关键，把关键核心技术、国家创新体系、教育科技人才统筹等重点环节抓实，才能带动新质生产力发展和现代化强国建设。其他政治、经济、国际与逻辑角度不混入本节点。",
        "evidence_level": "正式阅卷PPT-哲学角度提示+等级赋分（非逐点细则）",
    },
]

EXCLUDE_ROWS = [
    ("Q8", "逻辑与思维选择题", "脑机接口定义、换位推理、三段论和概念外延，属于选择性必修三《逻辑与思维》。"),
    ("Q9", "逻辑与思维选择题", "花茶真假话推理题，属于逻辑推理训练，不进入必修四哲学正文。"),
    ("Q10", "法律与生活选择题", "在线旅游服务合同和退款条款，属于法律与生活合同/消费者权益。"),
    ("Q11", "法律与生活选择题", "著作权、专利权、质押、土地征收补偿，属于法律与生活财产权。"),
    ("Q12", "经济与社会选择题", "新场景培育、要素市场化配置、市场主体活力，属于经济与社会。"),
    ("Q13", "经济与社会选择题", "长期护理保险、社会保障和筹资机制，属于经济与社会。"),
    ("Q14", "当代国际政治与经济选择题", "世界数据组织、国际组织和数据治理，属于当代国际政治与经济。"),
    ("Q15", "经济与社会/开放经济选择题", "货物贸易含新、含绿、含智和出口竞争优势，属于经济与开放发展。"),
    ("Q17", "政治与法治主观题", "超大城市治理、党的领导、人民当家作主、依法治国、法治政府，阅卷PPT第14-25页均按政治与法治评分。"),
]


def current_docx() -> Path:
    docs = [
        p
        for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_fengtai_ermo_repair_{ts}.docx")
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
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, inserted_headings: list[str]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_fengtai_ermo_repair_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    heading_by_q = {entry["question_no"]: heading for entry, heading in zip(INSERT_ENTRIES, inserted_headings, strict=False)}
    for entry in INSERT_ENTRIES:
        heading = heading_by_q.get(entry["question_no"])
        if not heading:
            continue
        clean = heading.split(". ", 1)[1]
        key = (SUITE, entry["question_no"], clean)
        if key in existing:
            continue
        row = {field: "" for field in fieldnames}
        row.update(
            {
                "canonical_node": entry["canonical_node"],
                "source_suite": SUITE,
                "question_no": entry["question_no"],
                "inserted_heading": clean,
            }
        )
        rows.append(row)
        added.append(row)
    if rows:
        with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
    return {"ledger": str(LEDGER), "ledger_backup": str(backup) if backup else None, "added_rows": added}


def new_row_id(existing_rows: list[dict[str, str]]) -> str:
    ids = []
    for row in existing_rows:
        value = row.get("matrix_row_id", "")
        if value.startswith("M") and value[1:].isdigit():
            ids.append(int(value[1:]))
    return f"M{(max(ids) if ids else 0) + 1:04d}"


def replace_or_append(rows: list[dict[str, str]], fieldnames: list[str], row: dict[str, str]) -> None:
    target = row["matrix_row_id"]
    for idx, existing in enumerate(rows):
        if existing.get("matrix_row_id") == target:
            rows[idx] = {field: row.get(field, "") for field in fieldnames}
            return
    rows.append({field: row.get(field, "") for field in fieldnames})


def in_body_row(row_id: str, q: str, node: str, support: str, evidence: str, source: str) -> dict[str, str]:
    return {
        "matrix_row_id": row_id,
        "row_source": ROW_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": q,
        "题型或模块判断": "必修四哲学选择/主观题",
        "是否进宝典": "是：本批新增进入当前DOCX/PDF正文",
        "宝典节点": node,
        "细则支持原理": support,
        "证据等级": evidence,
        "是否误放": "否",
        "是否需补厚": "否：已补入对应节点；选择题证据边界已明示",
        "当前处理": "DOCX_INSERTED_FENGTAI_2026_ERMO_RENDER_PENDING",
        "备注": "本批回源核对试卷、答案键和主观题阅卷PPT；未把选择题答案键冒充主观评分细则。",
        "source_artifact": source,
    }


def excluded_row(row_id: str, q: str, qtype: str, node: str, support: str, source: str) -> dict[str, str]:
    return {
        "matrix_row_id": row_id,
        "row_source": ROW_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": q,
        "题型或模块判断": qtype,
        "是否进宝典": "否：模块边界排除",
        "宝典节点": node,
        "细则支持原理": support,
        "证据等级": "试卷题干+答案键/阅卷PPT边界",
        "是否误放": "否",
        "是否需补厚": "否",
        "当前处理": "MODULE_BOUNDARY_EXCLUDED_FENGTAI_2026_ERMO_SOURCE_REVIEW",
        "备注": "本题或本点不作为当前哲学宝典正文；不把法律、逻辑、经济、政治或国际政治经济题偷换为哲学原理。",
        "source_artifact": source,
    }


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_fengtai_ermo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    paper_source = f"{PAPER_PDF}; {ANSWER_DOCX}"
    ppt_source = f"{RUBRIC_PPT}; {PAPER_PDF}; {ANSWER_DOCX}"

    updates: dict[str, dict[str, str]] = {
        "M0153": {
            "题型或模块判断": "Q16重复候选汇总",
            "是否进宝典": "是：已由当前DOCX覆盖",
            "宝典节点": "矛盾特殊性/规律与能动性/系统优化/发展观/价值观",
            "细则支持原理": "丰台二模Q16正式阅卷PPT第2-4页已列哲学角度，当前DOCX已有5处Q16正文条目（M0013-M0017）覆盖。",
            "证据等级": "正式阅卷PPT+当前DOCX正文覆盖",
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_EXISTING_BODY_FENGTAI_2026_ERMO",
            "备注": "关闭早期生产线候选，不作为新增正文证据重复计算。",
            "source_artifact": ppt_source,
        },
        "M0236": {
            "题型或模块判断": "Q16重复候选汇总",
            "是否进宝典": "是：已由当前DOCX覆盖",
            "宝典节点": "矛盾特殊性/规律与能动性/系统优化/发展观/价值观",
            "细则支持原理": "丰台二模Q16正式阅卷PPT第2-4页已列哲学角度，当前DOCX已有5处Q16正文条目（M0013-M0017）覆盖。",
            "证据等级": "正式阅卷PPT+当前DOCX正文覆盖",
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_EXISTING_BODY_FENGTAI_2026_ERMO",
            "备注": "关闭早期生产线候选，不作为新增正文证据重复计算。",
            "source_artifact": ppt_source,
        },
        "M0680": excluded_row("M0680", "Q1", "政治/中国特色社会主义选择题", "不进入当前哲学宝典", "五年规划、党的领导和制度优势，属中国特色社会主义/政治模块。", paper_source),
        "M0681": excluded_row("M0681", "Q2", "政治与法治选择题", "不进入当前哲学宝典", "儿童友好城市、基层治理和公民参与，属政治与法治。", paper_source),
        "M0682": excluded_row("M0682", "Q3", "政治与法治/法律选择题", "不进入当前哲学宝典", "最高检“检护民生”法律监督和民生权益保障，属政治与法治/法律模块。", paper_source),
        "M0683": in_body_row(
            "M0683",
            "Q4",
            "整体与部分",
            INSERT_ENTRIES[0]["material_trigger"],
            INSERT_ENTRIES[0]["evidence_level"],
            paper_source,
        ),
        "M0684": in_body_row(
            "M0684",
            "Q5",
            "主观能动性 / 意识的能动作用",
            INSERT_ENTRIES[1]["material_trigger"],
            INSERT_ENTRIES[1]["evidence_level"],
            paper_source,
        ),
        "M0685": {
            "题型或模块判断": "Q16重复候选汇总",
            "是否进宝典": "是：已由当前DOCX覆盖",
            "宝典节点": "矛盾特殊性/规律与能动性/系统优化/发展观/价值观",
            "细则支持原理": "丰台二模Q16正式阅卷PPT第2-4页已列哲学角度，当前DOCX已有5处Q16正文条目（M0013-M0017）覆盖。",
            "证据等级": "正式阅卷PPT+当前DOCX正文覆盖",
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": "SOURCE_REVIEW_CLOSED_DUPLICATE_OF_EXISTING_BODY_FENGTAI_2026_ERMO",
            "备注": "关闭早期生产线候选，不作为新增正文证据重复计算。",
            "source_artifact": ppt_source,
        },
        "M0686": excluded_row("M0686", "Q18", "法律与生活主观题", "不进入当前哲学宝典", "阅卷PPT第28-36页按法治与德治、民法典、生态环境法典和侵权责任评分；社会主义核心价值观仅为法律题价值导向，不转入哲学正文。", ppt_source),
        "M0687": excluded_row("M0687", "Q19", "经济与社会主观题", "不进入当前哲学宝典", "阅卷PPT第37-45页按市场配置、消费、产业升级、乡村振兴、绿色发展理念等经济知识评分。", ppt_source),
        "M0688": excluded_row("M0688", "Q20", "当代国际政治与经济主观题", "不进入当前哲学宝典", "自由贸易试验区/自由贸易港建设和高水平对外开放，属当代国际政治与经济。", paper_source),
        "M0689": excluded_row("M0689", "Q21", "逻辑与思维主观题", "不进入当前哲学宝典", "阅卷PPT第46-55页明确按创新思维、联想思维、发散思维与聚合思维评分；不把选必三创新思维偷换为必修四哲学创新。", ppt_source),
        "M0690": in_body_row(
            "M0690",
            "Q22",
            "主要矛盾和次要矛盾",
            INSERT_ENTRIES[4]["material_trigger"],
            INSERT_ENTRIES[4]["evidence_level"],
            ppt_source,
        ),
        "M0848": {
            "题型或模块判断": "套卷级闭合记录",
            "是否进宝典": "套卷逐题风险已回源闭合",
            "宝典节点": "SUITE_LEVEL_SUMMARY",
            "细则支持原理": "2026丰台二模逐题回源：Q4-Q7、Q22补入或登记正文链条；Q16已有5处正文覆盖；其余政治/法律/经济/逻辑/国际政治经济题边界排除。",
            "证据等级": "逐题回源闭合汇总",
            "是否误放": "不适用",
            "是否需补厚": "否：本批已逐题闭合风险行；外部模型门仍按总账记录。",
            "当前处理": "SUITE_LEVEL_CLOSED_BY_FENGTAI_2026_ERMO_REPAIR_RENDER_PENDING",
            "备注": "套卷级记录不替代逐题行；本批已补足逐题记录。",
            "source_artifact": f"{REPORT_MD}; {REPORT_JSON}",
        },
    }

    for row in rows:
        row_id = row.get("matrix_row_id", "")
        if row_id in updates:
            row.update(updates[row_id])

    for entry in INSERT_ENTRIES[2:4]:
        rows.append(
            in_body_row(
                new_row_id(rows),
                entry["question_no"],
                entry["canonical_node"],
                entry["material_trigger"],
                entry["evidence_level"],
                paper_source,
            )
        )

    for q, qtype, support in EXCLUDE_ROWS:
        rows.append(
            excluded_row(
                new_row_id(rows),
                q,
                qtype,
                "不进入当前哲学宝典",
                support,
                ppt_source if q in {"Q17"} else paper_source,
            )
        )

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    touched = sorted(set(updates) | {r["matrix_row_id"] for r in rows if r.get("row_source") == ROW_SOURCE})
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_or_added_row_ids": touched}


def write_report(ts: str, docx_result: dict[str, object], ledger_result: dict[str, object], matrix_result: dict[str, object]) -> None:
    manifest = {
        "timestamp": ts,
        "suite": SUITE,
        "docx": docx_result,
        "ledger": ledger_result,
        "matrix": matrix_result,
        "sources": {
            "paper_pdf": str(PAPER_PDF),
            "answer_docx": str(ANSWER_DOCX),
            "rubric_ppt": str(RUBRIC_PPT),
        },
        "render_status": "RENDER_PENDING",
        "model_gate_status": {
            "claude_web_app": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# FENGTAI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525",
        "",
        "Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`",
        "",
        f"- Suite: `{SUITE}`.",
        f"- Timestamp: `{ts}`.",
        f"- Paper source: `{PAPER_PDF}`.",
        f"- Answer source: `{ANSWER_DOCX}`.",
        f"- Rubric source: `{RUBRIC_PPT}`.",
        "",
        "## DOCX Inserts",
        "",
    ]
    for heading in docx_result["inserted_headings"]:
        lines.append(f"- `{heading}`")
    if docx_result["skipped_existing"]:
        lines.append("")
        lines.append("Skipped existing headings:")
        for heading in docx_result["skipped_existing"]:
            lines.append(f"- `{heading}`")
    lines.extend(
        [
            "",
            "## Matrix Closure",
            "",
            "- Q1-Q3: module-boundary excluded.",
            "- Q4-Q7: inserted as choice-question chains; evidence is answer key plus paper stem, not main-question scoring rules.",
            "- Q16: duplicate candidate rows closed against existing five DOCX entries and formal marking PPT.",
            "- Q17-Q21: module-boundary excluded according to paper/PPT module limits.",
            "- Q22: inserted under `主要矛盾和次要矛盾` with formal marking PPT angle and level-description evidence; not treated as point-by-point scoring rules.",
            f"- Matrix backup: `{matrix_result['matrix_backup']}`.",
            f"- Ledger backup: `{ledger_result['ledger_backup']}`.",
            f"- DOCX backup: `{docx_result['docx_backup']}`.",
            "",
            "## Open Gates",
            "",
            "- DOCX/PDF render QA is pending for this batch.",
            "- Claude web/app external review remains `real_call_pending`.",
            "- ClaudeCode Opus 4.7 max-effort confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until a real capture proves it.",
            "- GPTPro web review remains `real_call_pending`.",
        ]
    )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_result = edit_docx(ts)
    ledger_result = update_ledger(ts, docx_result["inserted_headings"])
    matrix_result = update_matrix(ts)
    write_report(ts, docx_result, ledger_result, matrix_result)
    print(json.dumps({"docx": docx_result, "ledger": ledger_result, "matrix": matrix_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
