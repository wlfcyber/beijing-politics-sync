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
REPORT_MD = RECOVERY / "SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2026顺义二模"
DESKTOP = Path.home() / "Desktop"
SOURCE_DIR = DESKTOP / "2026各区模拟题" / "2026各区二模" / "2026顺义二模"
PAPER_PDF = SOURCE_DIR / "26顺义二模(1).pdf"
RUBRIC_DOC = SOURCE_DIR / "26顺义二模评标.doc"
SOURCE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / "2026顺义二模.md"
SOURCE_RENDER_DIR = RECOVERY / "shunyi_ermo_source_pages_20260525"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

INSERT_ENTRIES = [
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q21",
        "heading_suffix": "2026顺义二模 第21题（主观题）",
        "material_trigger": "题干要求“综合运用哲学”阐述“先见”与“远虑”的传统理政智慧为什么能支撑中国式现代化稳步前行、护航民族复兴；评标doc第21题阅卷参考维度明确列出哲学角度：坚持尊重客观规律与发挥主观能动性相统一，依托认识与实践的辩证发展，并秉持联系、发展、全面的辩证观点。",
        "question_prompt": "为什么“先见”与“远虑”能从传统理政智慧转化为支撑中国式现代化和民族复兴的重要实践指引？",
        "why_trigger": "看到“先见”“远虑”“前瞻性视野”“长远规划”“五年规划与远景目标接续衔接”“谋定后动、久久为功”，应想到这不是主观愿望堆砌，而是在认识客观趋势和社会发展规律基础上发挥能动性，把前瞻判断转化为制度化、持续性的实践安排。",
        "answer_landing": "本题可写：传统理政智慧之所以能服务中国式现代化，是因为它要求人们尊重社会发展规律、准确把握时代大势，同时发挥主观能动性进行战略研判和长远谋划；在实践中形成认识，又用认识指导新的实践，使五年规划、远景目标和风险防范能够接续推进。运用联系、发展、全面的观点统筹改革、发展、安全和民生，才能把“先见”“远虑”转化为稳步前行、久久为功的现实治理效能。",
        "evidence_level": "正式评标doc-哲学综合角度+等级赋分（非逐点细则）",
    }
]


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
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
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_shunyi_ermo_repair_{ts}.docx")
    shutil.copy2(docx, backup)
    inserted: list[dict[str, str]] = []
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
                inserted.append({"question_no": entry["question_no"], "heading": heading, "node": entry["canonical_node"]})
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, inserted: list[dict[str, str]]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2026_shunyi_ermo_repair_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for item in inserted:
        clean = item["heading"].split(". ", 1)[1]
        key = (SUITE, item["question_no"], clean)
        if key in existing:
            continue
        row = {field: "" for field in fieldnames}
        row.update(
            {
                "canonical_node": item["node"],
                "source_suite": SUITE,
                "question_no": item["question_no"],
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


def update_row(row: dict[str, str], **values: str) -> None:
    row.update(values)


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_shunyi_ermo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    source = f"{RUBRIC_DOC}; {SOURCE_BUNDLE}; {PAPER_PDF}; {SOURCE_RENDER_DIR / 'page_05.png'}; {SOURCE_RENDER_DIR / 'page_12.png'}"
    q16_support = (
        "顺义二模评标doc第16题阅卷版已明确实践观点、人民主体、价值观、矛盾观、中华优秀传统文化等角度，"
        "当前DOCX已分别在实践是认识的基础、人民群众、价值观的导向作用、两点论与重点论、辩证否定/守正创新五个节点覆盖。"
    )
    q21_support = INSERT_ENTRIES[0]["material_trigger"]

    exclude = {
        "M0773": ("Q11", "法律与生活选择题", "租赁合同/承租人权利", "源卷第5页第11题为商铺转租与民法典租赁合同效力问题，官方答案D；属于法律与生活。"),
        "M0774": ("Q17", "政治与法治主观题", "枫桥经验/基层治理/全过程人民民主", "评标doc第17题围绕党的领导、人民当家作主、基层群众自治、治理体系和治理能力现代化，属于政治与法治。"),
        "M0775": ("Q18", "逻辑与思维/法律主观题", "矛盾律/科学思维客观性/民事权利保护", "评标doc第18题第(1)问为逻辑与思维中的矛盾律和科学思维客观性，第(2)问为法律与生活权利保护；不进入当前必修四哲学正文。"),
        "M0776": ("Q20", "当代国际政治与经济主观题", "中国发展与世界/经济全球化/新型国际关系", "源卷第11页和评标doc第20题明确要求运用《当代国际政治与经济》知识，属于国政经边界。"),
    }

    touched: list[str] = []
    for row in rows:
        if row.get("题源") != SUITE:
            continue
        row_id = row.get("matrix_row_id", "")
        if row_id in {"M0043", "M0044", "M0045", "M0159"}:
            node = row.get("宝典节点", "")
            if row_id == "M0045":
                node = "两点论与重点论"
            elif row_id == "M0159":
                node = "实践是认识的基础；人民群众；价值观的导向作用；两点论与重点论；辩证否定 / 守正创新"
            update_row(
                row,
                题型或模块判断="必修四哲学主观题现有正文覆盖",
                是否进宝典="是：已进入当前DOCX/PDF正文，本批关闭弱证据重复候选",
                宝典节点=node,
                细则支持原理=q16_support,
                证据等级="正式评标doc/阅卷版-已由强证据行覆盖",
                是否误放="否",
                是否需补厚="否：已由M0029-M0033及M0120-M0124强证据行覆盖",
                当前处理="SOURCE_REVIEW_CLOSED_CURRENT_DOCX_COVERAGE_SHUNYI_2026_ERMO_Q16",
                备注="弱参考答案候选已由顺义二模评标doc阅卷版修复；本行不再作为独立待补正文。",
                source_artifact=source,
            )
        elif row_id == "M0777":
            update_row(
                row,
                题型或模块判断="必修四哲学主观题",
                是否进宝典="是：本批新增进入当前DOCX/PDF正文",
                宝典节点=INSERT_ENTRIES[0]["canonical_node"],
                细则支持原理=q21_support,
                证据等级=INSERT_ENTRIES[0]["evidence_level"],
                是否误放="否",
                是否需补厚="否：已补入核心节点；联系/发展/认识实践作为该条答案落点内部链条，不拆成无逐点细则的多条",
                当前处理="DOCX_INSERTED_SHUNYI_2026_ERMO_RENDER_PENDING",
                备注="源卷第12页设问明确“综合运用哲学”；评标doc给出哲学综合角度，故本批补入核心节点。",
                source_artifact=source,
            )
        elif row_id == "M0778":
            update_row(
                row,
                题号="Qunknown",
                题型或模块判断="套卷抽取误并行风险记录",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="顺义二模：Q16已由评标doc强证据覆盖并进入当前DOCX五个节点；Q21本批新增进入尊重客观规律与发挥主观能动性相结合节点；Q11/Q17/Q18/Q20按法律、政治、逻辑、国政经边界排除。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_SHUNYI_2026_ERMO_REPAIR_RENDER_PENDING",
                备注="套卷级长摘录不替代逐题行；本批已用源卷图像页和评标doc逐题承接。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id == "M0855":
            update_row(
                row,
                题型或模块判断="套卷级覆盖口径，不替代逐题细则核验",
                是否进宝典="套卷逐题风险已回源闭合",
                宝典节点="SUITE_LEVEL_SUMMARY",
                细则支持原理="顺义二模本批完成Q16弱证据重复候选关闭、Q21新增、Q11/Q17/Q18/Q20边界排除；套卷级记录只作为闭合摘要。",
                证据等级="逐题回源闭合汇总",
                是否误放="不适用",
                是否需补厚="否",
                当前处理="SUITE_LEVEL_CLOSED_BY_SHUNYI_2026_ERMO_REPAIR_RENDER_PENDING",
                备注="套卷级记录不替代逐题矩阵；本批渲染后再标记RENDER_PASS。",
                source_artifact=f"{REPORT_MD}; {REPORT_JSON}",
            )
        elif row_id in exclude:
            q, qtype, node, support = exclude[row_id]
            update_row(
                row,
                题号=q,
                题型或模块判断=qtype,
                是否进宝典="否：模块边界排除",
                宝典节点=node,
                细则支持原理=support,
                证据等级="正式评标doc/源卷图像-模块边界",
                是否误放="否",
                是否需补厚="否",
                当前处理="MODULE_BOUNDARY_EXCLUDED_SHUNYI_2026_ERMO_SOURCE_REVIEW",
                备注="不把法律、政治与法治、逻辑与思维、国政经内容偷换为当前哲学正文。",
                source_artifact=source,
            )
        if row_id:
            touched.append(row_id)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix": str(MATRIX), "matrix_backup": str(backup), "updated_row_ids": sorted(set(touched))}


def write_report(ts: str, docx_info: dict[str, object], ledger_info: dict[str, object], matrix_info: dict[str, object]) -> None:
    data = {
        "timestamp": ts,
        "suite": SUITE,
        "docx": docx_info,
        "ledger": ledger_info,
        "matrix": matrix_info,
        "sources": {
            "rubric_doc": str(RUBRIC_DOC),
            "paper_pdf": str(PAPER_PDF),
            "source_bundle": str(SOURCE_BUNDLE),
            "source_page_05": str(SOURCE_RENDER_DIR / "page_05.png"),
            "source_page_12": str(SOURCE_RENDER_DIR / "page_12.png"),
        },
        "render_status": "RENDER_PENDING",
        "model_gate_status": {
            "claude_web_app_full_artifact_review": "real_call_pending",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
            "gptpro_web_full_artifact_review": "real_call_pending",
        },
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    inserted = "\n".join(f"- `{item['heading']}`" for item in docx_info["inserted_headings"])
    md = f"""# SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`

- Suite: `{SUITE}`.
- Timestamp: `{ts}`.
- Formal scoring/marking source: `{RUBRIC_DOC}`.
- Paper source: `{PAPER_PDF}`.
- Source bundle: `{SOURCE_BUNDLE}`.
- Source page renders used: `{SOURCE_RENDER_DIR / 'page_05.png'}`, `{SOURCE_RENDER_DIR / 'page_12.png'}`.

## DOCX Inserts

{inserted}

## Matrix Closure

- Q21 inserted under `尊重客观规律与发挥主观能动性相结合` from the source-paper philosophy prompt and formal marking-document philosophy angle.
- Q16 weak-reference duplicate rows were closed against existing current-DOCX coverage and the formal marking-document/阅卷版.
- Q11, Q17, Q18, and Q20 are module-boundary exclusions.
- Qunknown and suite-level rows are closed as summaries only; they do not replace row-level evidence.
- Q21 broad terms such as 认识与实践、联系、发展 are retained inside the answer landing, not split into standalone rows without point-by-point scoring support.
- Matrix backup: `{matrix_info['matrix_backup']}`.
- Ledger backup: `{ledger_info['ledger_backup']}`.
- DOCX backup: `{docx_info['docx_backup']}`.

## Open Gates

- DOCX/PDF render QA is pending for this batch.
- Claude web/app full artifact review through direct `https://claude.ai` remains `real_call_pending`.
- ClaudeCode Opus 4.7 max-effort/adaptive-thinking confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web full artifact review remains `real_call_pending`.
- ORDER_063 final GitHub upload remains deferred.
"""
    REPORT_MD.write_text(md, encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_info = edit_docx(ts)
    ledger_info = update_ledger(ts, docx_info["inserted_headings"])
    matrix_info = update_matrix(ts)
    write_report(ts, docx_info, ledger_info, matrix_info)
    print(json.dumps({"docx": docx_info, "ledger": ledger_info, "matrix": matrix_info}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
