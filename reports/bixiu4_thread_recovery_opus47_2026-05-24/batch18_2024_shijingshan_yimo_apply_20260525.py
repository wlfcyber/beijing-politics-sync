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
W = f"{{{W_NS}}}"
NS = {"w": W_NS}

ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH18_2024_SHIJINGSHAN_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH18_2024_SHIJINGSHAN_YIMO_CODEX_20260525.md"

SUITE = "2024石景山一模"
YEAR = "2024"
STAGE = "一模"
ANSWER_KEY = "1C 2B 3D 4A 5C 6A 7B 8B 9C 10A 11D 12D 13B 14C 15C"
SOURCE_BUNDLE = (
    "reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/"
    "01_source_inventory/suite_source_bundles/2024石景山一模.md"
)
GPT_BUNDLE = (
    "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/"
    "gpt_suite_bundles/2024各区模拟题__2024各区一模__2024石景山一模.md"
)
PAPER_DOCX_TEXT = (
    "reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2024/texts/"
    "2024各区一模__2024石景山一模__试卷__2024北京石景山高三一模政治（教师版带答案）.docx.txt"
)

NEW_HEADING = "31. 2024石景山一模 第2题（选择题）"
NEW_NODE = "实践是认识的基础"
NEW_PARAGRAPHS = [
    (
        "【材料触发点】",
        "我国自主研制的北斗卫星导航系统在农业领域应用到农机自动驾驶、精准收割、昼夜连续作业、整理土地和变量施肥。官方答案B包含①：农业生产实践具有历史性，其形式和水平不断发展。",
    ),
    (
        "【设问】",
        "我国自主研制的北斗卫星导航系统已在农业领域得到广泛应用：将卫星导航定位与电子控制等技术相结合，可以实现农机自动驾驶、精准收割；可以昼夜连续工作，加快作业速度；可以整理土地和变量施肥，改善农作物生长环境……和以往的农业生产方式相比，北斗系统在农业生产中的应用表明什么？A.①② B.①③ C.②④ D.③④。",
    ),
    (
        "【为什么能想到】",
        "题干把“以往的农业生产方式”和“北斗系统在农业生产中的应用”进行对比，关键不只是技术先进，而是农业生产实践的工具、形式和水平随着历史条件、科技水平发展而发展。学生看到“农机自动驾驶、精准收割、变量施肥”这种生产实践形态升级，就应想到实践具有社会历史性，实践活动总是在一定历史条件下进行并随历史条件变化而发展。",
    ),
    (
        "【答案落点】",
        "本题应选B。本节点只处理①：北斗系统进入农业生产，使农机作业方式、作业速度和生产管理方式明显不同于以往，说明实践是认识的基础，同时实践本身具有社会历史性。③“科技创新推动农业生产力的发展和农业现代化进程”是经济与社会/生产力发展方向，可作背景但不作为本哲学节点新增；②把生产工具更新直接推成生产关系变革，④说改变客观规律，均不当。",
    ),
]
STUDENT_TEXT = NEW_HEADING + "\n" + "\n".join(label + " " + body for label, body in NEW_PARAGRAPHS)
EVIDENCE_LEVEL = "客观答案表+题面正确项；非主观评分细则"
SOURCE_LINES = f"{SOURCE_BUNDLE}; {GPT_BUNDLE}; {PAPER_DOCX_TEXT}"


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def clear_runs(p: etree._Element) -> None:
    for child in list(p):
        if child.tag == W + "r" or child.tag == W + "hyperlink":
            p.remove(child)


def make_run(text: str, label: bool = False) -> etree._Element:
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return r


def new_heading_para(template: etree._Element, text: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(text))
    return p


def new_label_para(template: etree._Element, label: str, body: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + body))
    return p


def new_blank_para(template: etree._Element) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    return p


def update_docx(timestamp: str) -> Path:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2024_shijingshan_yimo_batch18_{timestamp}.docx")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
        all_parts = {item.filename: zin.read(item.filename) for item in zin.infolist() if item.filename != "word/document.xml"}

    root = etree.fromstring(xml)
    body = root.xpath("//w:body", namespaces=NS)[0]
    paras = body.xpath("./w:p", namespaces=NS)
    texts = [para_text(p) for p in paras]

    if NEW_HEADING in texts:
        return backup

    insert_idx = next(i for i, t in enumerate(texts) if t == "认识对实践的反作用")
    heading_template = paras[insert_idx - 6]  # current "30. 2026丰台一模 第4题（选择题）"
    label_template = paras[insert_idx - 5]
    blank_template = paras[insert_idx - 1]

    new_paras = [new_heading_para(heading_template, NEW_HEADING)]
    new_paras.extend(new_label_para(label_template, label, body_text) for label, body_text in NEW_PARAGRAPHS)
    new_paras.append(new_blank_para(blank_template))

    for offset, p in enumerate(new_paras):
        body.insert(insert_idx + offset, p)

    new_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    try:
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for name, data in all_parts.items():
                zout.writestr(name, data)
            zout.writestr("word/document.xml", new_xml)
        shutil.move(tmp_path, docx)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    return backup


def update_ledger() -> None:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    key = (NEW_NODE, SUITE, "Q2")
    if not any((r.get("canonical_node"), r.get("source_suite"), r.get("question_no")) == key for r in rows):
        rows.append(
            {
                "canonical_node": NEW_NODE,
                "source_suite": SUITE,
                "question_no": "Q2",
                "inserted_heading": NEW_HEADING,
            }
        )
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def update_accepted() -> None:
    rows = []
    if ACCEPTED.exists():
        for line in ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    record = {
        "source_suite": SUITE,
        "question_no": "Q2",
        "framework_node": NEW_NODE,
        "canonical_node": NEW_NODE,
        "student_facing_text": STUDENT_TEXT,
        "evidence_level": EVIDENCE_LEVEL,
        "boundary_note": "选择题客观答案链，仅证明正确项①进入实践社会历史性/实践基础节点；不得当作主观题评分细则。",
        "source_lane": "Codex Batch18 insertion",
        "source_repair_basis": SOURCE_LINES,
        "source_lines": SOURCE_LINES,
        "batch": "batch18_2024_shijingshan_yimo",
        "registered_heading": NEW_HEADING,
    }
    replaced = False
    for idx, old in enumerate(rows):
        if (
            old.get("source_suite") == SUITE
            and old.get("question_no") == "Q2"
            and old.get("canonical_node") == NEW_NODE
        ):
            rows[idx] = record
            replaced = True
            break
    if not replaced:
        rows.append(record)
    ACCEPTED.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")


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


def patch_row(row: dict[str, str], **kwargs: str) -> None:
    for key, value in kwargs.items():
        row[KEYS[key]] = value


def update_matrix(timestamp: str) -> tuple[int, int, int, Path]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch18_2024_shijingshan_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}

    def close_boundary(row_id: str, qno: str, node: str, principle: str, action: str = "BATCH18_CLOSED_MODULE_BOUNDARY_SOURCE_REVIEW") -> None:
        if row_id in by_id:
            patch_row(
                by_id[row_id],
                type="module_boundary_or_false_positive_source_reviewed",
                in_body="否：模块边界排除或旧术语误报",
                node=node,
                principle=principle,
                evidence="题面+教师版答案键/参考答案；无必修四主链细则",
                misplaced="否",
                needs="否",
                action=action,
                note=f"{qno} 已经按教师版题面与答案回源闭合，不进入当前哲学宝典正文。",
                artifact=f"{SOURCE_LINES}; {SOURCE_TRANSCRIPTION.name}",
            )

    close_boundary("M0304", "Q1", "中国特色社会主义/党的领导/人民军队边界", "Q1答案C（②④），主链为党对军队绝对领导与思想政治工作，不是必修四哲学可复用落点。")
    close_boundary("M0307", "Q4", "文化传承发展/文化自信边界", "Q4答案A（①②），主链为全球文明倡议、文明多样性与中华文化传播，不新增哲学节点。")
    close_boundary("M0309", "Q6", "选择性必修三《逻辑与思维》边界", "Q6答案A，题面考联想思维/类比推理/超前思维/发散思维，显性属于逻辑与思维。")
    close_boundary("M0310", "Q7", "选择性必修三《逻辑与思维》边界", "Q7为概念外延关系图判断，显性属于逻辑与思维；材料中社会主要矛盾字样只是选项内容。")
    close_boundary("M0143", "Q7", "选择性必修三《逻辑与思维》边界", "Q7为概念外延关系图判断，显性属于逻辑与思维；旧行保留为误触发排除。")
    close_boundary("M0311", "Q11", "法律与生活/消费者权益边界", "Q11答案D，主链为商品宣传、欺诈、惩罚性赔偿与举证责任。")
    close_boundary("M0312", "Q12", "经济与社会/冰雪经济边界", "Q12答案D，主链为消费场景、资源优势转化和产业多业态发展。")
    close_boundary("M0313", "Q14", "当代国际政治与经济/数字贸易边界", "Q14答案C，主链为数字贸易、全球数字治理与数字鸿沟。")
    close_boundary("M0314", "Q15", "当代国际政治与经济/一带一路边界", "Q15答案C，主链为和平发展道路与人类命运共同体。")
    close_boundary("M0316", "Q17", "法律与生活边界", "Q17要求运用法律知识说明合同成立和民法基本原则意义。")
    close_boundary("M0317", "Q18", "政治与法治/法律与生活边界", "Q18(1)限政治与法治基层治理，Q18(2)限法治知识/人民调解与物业合同。")
    close_boundary("M0318", "Q19", "经济与社会/当代国际政治与经济/逻辑与思维边界", "Q19(1)限经济与社会，Q19(2)限当代国际政治与经济，Q19(3)明确《逻辑与思维》辩证思维方法。")
    close_boundary("M0319", "Q20", "综合运用/宽参考答案边界", "Q20参考答案仅写可从党的领导、制度优势、经济社会发展、国家治理、文化自信等角度回答，非哲学逐点细则；不新增正文。")
    close_boundary("M0320", "Qunknown", "整卷/PPT抽取残留", "Qunknown来自整卷或PPT相邻文本术语误报，不是独立题号。")

    for row_id in ["M0144", "M0195", "M0201", "M0315"]:
        if row_id in by_id:
            patch_row(
                by_id[row_id],
                type="main_question_existing_docx_reference_answer_supported",
                in_body="是：既有最终DOCX已覆盖；不重复新增",
                node="发展的观点 / 认识对实践的反作用",
                principle="Q16教师版参考答案写明可从文化继承与发展、文化自信、认识的作用、联系、发展等角度回答；该来源是教师版参考答案宽角度，不是逐点评分细则。当前DOCX已有发展观点与认识作用两处覆盖。",
                evidence="教师版参考答案+当前DOCX；非正式细则",
                misplaced="否",
                needs="否：无正式逐点细则，暂不把联系/文化自信宽角度扩写成新增正文",
                action="BATCH18_CLOSED_EXISTING_DOCX_REFERENCE_SUPPORT",
                note="Q16保留既有正文，不冒充细则，不重复插入。",
                artifact=f"{SOURCE_LINES}; {SOURCE_TRANSCRIPTION.name}",
            )

    if "M0305" in by_id:
        patch_row(
            by_id["M0305"],
            type="choice_philosophy_inserted",
            in_body="是：Batch18新增进入当前DOCX/PDF正文并登记ledger/accepted",
            node=NEW_NODE,
            principle="Q2教师版答案B（①③）：①明确“农业生产实践具有历史性，其形式和水平不断发展”；本条只取①进入实践社会历史性/实践基础节点，③作为经济与社会背景不单独入哲学节点。",
            evidence=EVIDENCE_LEVEL,
            misplaced="否",
            needs="否",
            action="INSERTED_AND_REGISTERED_BATCH18_SHIJINGSHAN_Q2",
            note=f"新增正文：{NEW_HEADING}",
            artifact=f"{SOURCE_LINES}; {SOURCE_TRANSCRIPTION.name}",
        )

    if "M0306" in by_id:
        patch_row(
            by_id["M0306"],
            type="choice_philosophy_existing_docx_covered",
            in_body="是：既有最终DOCX已覆盖",
            node="社会存在与社会意识",
            principle="Q3教师版答案D（③④）：城市精神植根北京深厚历史并反映市民价值追求，体现社会存在决定社会意识；当前DOCX已有该题正文覆盖。",
            evidence="客观答案表+题面正确项+当前DOCX；非主观评分细则",
            misplaced="否",
            needs="否",
            action="BATCH18_CLOSED_EXISTING_DOCX_COVERED_Q3",
            note="当前DOCX已有 2024石景山一模 第3题 1处。",
            artifact=f"{SOURCE_LINES}; {SOURCE_TRANSCRIPTION.name}",
        )

    if "M0308" in by_id:
        patch_row(
            by_id["M0308"],
            type="choice_philosophy_existing_docx_covered",
            in_body="是：既有最终DOCX已覆盖",
            node="根据固有联系建立新的具体联系 / 把握本质和规律",
            principle="Q5教师版答案C（②④）：人能够把握自然天气现象背后的本质和规律，并从事物固有联系中构建防灾减灾预案；当前DOCX已有该题正文覆盖。",
            evidence="客观答案表+题面正确项+当前DOCX；非主观评分细则",
            misplaced="否",
            needs="否",
            action="BATCH18_CLOSED_EXISTING_DOCX_COVERED_Q5",
            note="当前DOCX已有 2024石景山一模 第5题 1处。",
            artifact=f"{SOURCE_LINES}; {SOURCE_TRANSCRIPTION.name}",
        )

    for row_id in ["M0783", "M0822"]:
        if row_id in by_id:
            patch_row(
                by_id[row_id],
                type="套卷级覆盖口径，不替代逐题细则核验",
                in_body="套卷已完成Batch18逐题回源；有新增Q2正文和既有Q3/Q5/Q16覆盖",
                node="SUITE_LEVEL_SUMMARY",
                evidence="BATCH18_SUITE_SOURCE_REVIEW_CLOSED",
                misplaced="不适用",
                needs="否",
                action="BATCH18_SUITE_SOURCE_REVIEW_CLOSED",
                note="Batch18逐题回源：Q2新增；Q3/Q5/Q16既有覆盖；Q1/Q4/Q6/Q7/Q11-Q15/Q17-Q20/Qunknown为模块边界或抽取误报。",
                artifact=f"{SOURCE_LINES}; {SOURCE_TRANSCRIPTION.name}",
            )

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    suite_rows = [r for r in rows if r.get(KEYS["source"]) == SUITE]
    markers = ["待核", "HOLD", "TO_BE_PLACED", "weak_hit", "base_has_local_match", "possible_omission", "疑似", "候选"]
    openish = [
        r
        for r in suite_rows
        if any(marker in (r.get(KEYS["action"], "") + r.get(KEYS["in_body"], "") + r.get(KEYS["misplaced"], "")) for marker in markers)
    ]
    return len(rows), len(suite_rows), len(openish), backup


def write_source_transcription(timestamp: str) -> None:
    text = f"""# Batch18 Source Transcription - 2024石景山一模

Updated: {timestamp} +08

status: `source_review_closed_with_one_docx_insert`

## Source Packet

- suite inventory bundle: `{SOURCE_BUNDLE}`
- GPT suite bundle: `{GPT_BUNDLE}`
- extracted teacher-version DOCX text: `{PAPER_DOCX_TEXT}`
- current DOCX/PDF: `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

## Objective Answer Key

`{ANSWER_KEY}`

Evidence boundary: this is a teacher-version objective answer key. It is sufficient for choice-question correct-option placement only; it is not a subjective scoring rule.

## Included Or Registered Items

### Q2 - newly inserted

```text
2. 我国自主研制的北斗卫星导航系统已在农业领域得到广泛应用：将卫星导航定位与电子控制等技术相结合，可以实现农机自动驾驶，精准收割；可以昼夜连续工作，加快作业速度；可以整理土地和变量施肥，改善农作物生长环境……和以往的农业生产方式相比，北斗系统在农业生产中的应用表明
①农业生产实践具有历史性，其形式和水平不断发展
②农业生产工具的更新，促进了农村生产关系的变革
③科技创新推动农业生产力的发展和农业现代化的进程
④人们能够利用科技改变农作物生长的客观环境和规律
A.①② B.①③ C.②④ D.③④
```

Decision: official answer `B` contains item ①. Q2 enters `实践是认识的基础` as a choice-question chain for实践社会历史性. Item ③ is treated as economy/productive-force background, not a separate philosophy node.

### Q3 - existing DOCX coverage

Official answer `D` contains ③④: city spirit has regional/era character and is rooted in Beijing historical social existence. Current DOCX already has one `2024石景山一模 第3题` entry under社会存在与社会意识.

### Q5 - existing DOCX coverage

Official answer `C` contains ②④: grasping natural-weather essence/laws and constructing disaster-prevention plans from inherent links. Current DOCX already has one `2024石景山一模 第5题` entry.

### Q16 - existing DOCX coverage, reference-answer level only

```text
16. （6分）可从文化的继承与发展，文化自信，认识的作用，联系，发展等角度回答。
```

Decision: current DOCX already has two `2024石景山一模 第16题` entries, under development and cognition/recognition作用. Because the source is a teacher-version reference answer with broad angles, not a detailed scoring rule, Batch18 does not inflate every broad angle into new entries.

## Exclusions

- Q1: 中国特色社会主义/党的领导/人民军队边界。
- Q4: 文化传承、文明多样性与文化自信边界；不新增哲学节点。
- Q6-Q7: 选择性必修三《逻辑与思维》边界。
- Q11: 法律与生活/消费者权益边界。
- Q12: 经济与社会/冰雪经济边界。
- Q14-Q15: 当代国际政治与经济边界。
- Q17: 法律与生活边界。
- Q18: 政治与法治/法律与生活边界。
- Q19: (1)经济与社会，(2)当代国际政治与经济，(3)明确《逻辑与思维》辩证思维方法；不进入必修四正文。
- Q20: 综合运用题，参考答案只有党的领导、制度优势、经济社会发展、国家治理、文化自信等宽角度；不作为哲学逐点细则。
- Qunknown: 整卷/PPT相邻文本抽取残留。
"""
    SOURCE_TRANSCRIPTION.write_text(text, encoding="utf-8")


def write_batch_report(timestamp: str, matrix_rows: int, suite_rows: int, openish: int, matrix_backup: Path, docx_backup: Path) -> None:
    text = f"""# Coverage Fusion Batch18 - 2024石景山一模

Updated: {timestamp} +08

status: `BATCH18_CLOSED_SOURCE_REVIEW_WITH_Q2_DOCX_INSERT`

## Scope

Resolved stale candidate rows for `2024石景山一模` in `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.

## Actions

- Inserted one new DOCX entry: `{NEW_HEADING}` under `{NEW_NODE}`.
- Registered the new Q2 entry in `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Confirmed existing DOCX coverage:
  - Q3: `社会存在与社会意识`
  - Q5: `根据固有联系建立新的具体联系 / 把握本质和规律`
  - Q16: `发展的观点 / 认识对实践的反作用`
- Closed Q1/Q4/Q6/Q7/Q11-Q15/Q17-Q20/Qunknown as module boundaries or extraction residue.

## Matrix Outcome

- matrix rows: `{matrix_rows}`
- suite rows after update: `{suite_rows}`
- open-ish rows remaining for this suite: `{openish}`
- matrix backup: `{matrix_backup}`
- DOCX backup: `{docx_backup}`

## Evidence Boundary

Q2/Q3/Q5 are choice-question chains supported by the teacher-version objective answer key plus question stem/correct option. Q16 is only teacher-version reference-answer broad support. No ordinary reference answer is labeled as a detailed scoring rule.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_backup = update_docx(timestamp)
    update_ledger()
    update_accepted()
    write_source_transcription(timestamp)
    matrix_rows, suite_rows, openish, matrix_backup = update_matrix(timestamp)
    write_batch_report(timestamp, matrix_rows, suite_rows, openish, matrix_backup, docx_backup)
    print(json.dumps({
        "timestamp": timestamp,
        "inserted_heading": NEW_HEADING,
        "matrix_rows": matrix_rows,
        "suite_rows": suite_rows,
        "openish_suite_rows": openish,
        "docx_backup": str(docx_backup),
        "matrix_backup": str(matrix_backup),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
