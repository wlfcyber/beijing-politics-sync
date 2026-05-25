from __future__ import annotations

import csv
import json
import re
import shutil
import tempfile
import zipfile
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
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"

THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH21_2025_DONGCHENG_FINAL_CODEX_20260525.md"

SUITE = "2025东城期末"
VALUE_NODE = "价值判断与价值选择"

REFRESHED = {
    "material_trigger": "材料明确给出“中国式现代化，民生为大是价值取向，更是实践要求”。图2指向人民立场；材料二列出居民收入、医保覆盖率、高等教育入学率、体育场地等民生发展事实，也列出人大基层立法联系点听民声、最高检办民生“小案件”、政府推进文化惠民工程等治理实践。",
    "question_prompt": "中国式现代化，民生为大是价值取向，更是实践要求。结合材料，综合运用所学，谈谈你对这句话的理解。",
    "why_trigger": "题干把“民生为大”明确界定为价值取向，说明现代化建设首先要回答“为了谁、依什么标准评价政策和行动”。看到人民立场、发展为民生、治理重民生，就应落到正确价值判断和价值选择必须自觉站在最广大人民立场上，把人民群众的根本利益作为最高价值标准。",
    "answer_landing": "正确的价值判断和价值选择要符合社会发展规律，并自觉站在最广大人民的立场上。中国式现代化坚持民生为大，就是在发展、立法、司法、公共服务和文化惠民等选择中，以是否保障和发展人民利益、是否回应人民对美好生活的需要、是否让发展成果更多更公平惠及人民为评价尺度。材料中的收入增长、医保覆盖、教育发展、基层立法听民声、民生“小案件”和文化惠民，说明这种价值取向不是口号，而是转化为持续改善民生的实践要求。",
}


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS)).strip()


def style_val(p: etree._Element) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


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


def replace_label_para(p: etree._Element, label: str, body_text: str) -> None:
    clear_runs(p)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + body_text))


def update_docx(timestamp: str) -> tuple[Path, str]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch21_q21_value_refresh_{timestamp}.docx")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        parts = {item.filename: zin.read(item.filename) for item in infos}
    root = etree.fromstring(parts["word/document.xml"])
    paras = root.xpath("//w:body/w:p", namespaces=NS)

    current_node = ""
    start_idx = None
    for idx, p in enumerate(paras):
        text = para_text(p)
        if style_val(p) == "4":
            current_node = text
        if current_node == VALUE_NODE and style_val(p) == "5" and SUITE in text and "第21题" in text:
            start_idx = idx
            break
    if start_idx is None:
        raise RuntimeError("Q21 value-judgment entry not found")

    body_paras = paras[start_idx + 1 : start_idx + 5]
    if len(body_paras) != 4:
        raise RuntimeError("Q21 value-judgment entry body is incomplete")
    replace_label_para(body_paras[0], "【材料触发点】", REFRESHED["material_trigger"])
    replace_label_para(body_paras[1], "【设问】", REFRESHED["question_prompt"])
    replace_label_para(body_paras[2], "【为什么能想到】", REFRESHED["why_trigger"])
    replace_label_para(body_paras[3], "【答案落点】", REFRESHED["answer_landing"])

    parts["word/document.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for info in infos:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.comment = info.comment
            zi.extra = info.extra
            zi.internal_attr = info.internal_attr
            zi.external_attr = info.external_attr
            zi.create_system = info.create_system
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, parts[info.filename])
    shutil.move(str(tmp_path), docx)
    return backup, para_text(paras[start_idx])


def extract_q21_value_block() -> str:
    docx = current_docx()
    with zipfile.ZipFile(docx) as zf:
        xml = zf.read("word/document.xml")
    root = etree.fromstring(xml)
    paras = root.xpath("//w:body/w:p", namespaces=NS)
    current_node = ""
    for idx, p in enumerate(paras):
        text = para_text(p)
        if style_val(p) == "4":
            current_node = text
        if current_node == VALUE_NODE and style_val(p) == "5" and SUITE in text and "第21题" in text:
            block = [text]
            j = idx + 1
            while j < len(paras) and style_val(paras[j]) not in {"3", "4", "5"}:
                t = para_text(paras[j])
                if t:
                    block.append(t)
                j += 1
            return "\n".join(block)
    raise RuntimeError("refreshed Q21 value block not found")


def update_accepted(timestamp: str, heading: str, block: str) -> int:
    backup = ACCEPTED.with_name(f"student_patch_entries.accepted_backup_before_batch21_q21_value_refresh_{timestamp}.jsonl")
    shutil.copy2(ACCEPTED, backup)
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    updated = 0
    for record in records:
        if (
            record.get("source_suite") == SUITE
            and record.get("question_no") == "Q21"
            and record.get("canonical_node") == VALUE_NODE
            and record.get("registered_heading") == heading
        ):
            record["student_facing_text"] = block
            record["source_lane"] = "Codex Batch21 Dongcheng final existing-entry refresh"
            record["boundary_note"] = (
                "Q21 is a综合题; this refreshed value-judgment entry uses formal rubric support for人民立场/价值取向, "
                "not a claim that the whole answer is only this node."
            )
            updated += 1
    if updated != 1:
        raise RuntimeError(f"Expected to update 1 accepted record, updated {updated}")
    ACCEPTED.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")
    return updated


def update_matrix(timestamp: str) -> int:
    backup = MATRIX.with_name(f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch21_q21_value_refresh_{timestamp}.csv")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    updates = 0
    for row in rows:
        if row.get("row_source") != "codex_batch21_2025_dongcheng_final" or row.get("题源") != SUITE:
            continue
        q = row.get("题号")
        node = row.get("宝典节点")
        if q == "Q4" and node == "矛盾就是对立统一":
            row["题型或模块判断"] = "选择题哲学：既有正文补登记"
            row["当前处理"] = "REGISTERED_EXISTING_DOCX_BATCH21_DONGCHENG_Q4"
            updates += 1
        elif q == "Q16" and node == "主观能动性 / 意识的能动作用":
            row["题型或模块判断"] = "主观题哲学与文化：既有正文补登记"
            row["当前处理"] = "REGISTERED_EXISTING_DOCX_BATCH21_DONGCHENG_Q16"
            updates += 1
        elif q == "Q21" and node == "价值判断与价值选择":
            row["题型或模块判断"] = "综合主观题：既有正文补厚"
            row["当前处理"] = "REFRESHED_EXISTING_DOCX_BATCH21_DONGCHENG_Q21_VALUE"
            row["备注"] = row["备注"] + " Batch21 refreshed the thin answer landing with a concrete people-interest evaluation chain."
            updates += 1
        elif q == "Q21" and node == "人民群众":
            row["题型或模块判断"] = "综合主观题：本批新增正文"
            row["当前处理"] = "INSERTED_DOCX_BATCH21_DONGCHENG_Q21_PEOPLE"
            updates += 1
    if updates != 4:
        raise RuntimeError(f"Expected 4 matrix body-row updates, got {updates}")
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    return updates


def append_reports(backup: Path, accepted_updated: int, matrix_updates: int) -> None:
    append = f"""

## Batch21 Q21 Value-Judgment Refresh - 2026-05-25

- refreshed existing `2025东城期末 第21题` entry under `价值判断与价值选择`.
- DOCX backup: `{backup}`.
- accepted records updated: `{accepted_updated}`.
- matrix body rows normalized: `{matrix_updates}`.
- reason: the pre-existing Q21 value entry was source-supported but answer landing was too thin; it now gives a concrete chain from人民立场 to policy/legislation/judicial/public-service evaluation by人民利益.
"""
    BATCH_REPORT.write_text(BATCH_REPORT.read_text(encoding="utf-8") + append, encoding="utf-8")

    status_append = f"""

## Batch21 Refinement: 2025东城期末 Q21价值判断补厚 - 2026-05-25

- status: `RECOVERED_EXECUTION_IN_PROGRESS`
- action: refreshed existing Q21 `价值判断与价值选择` body entry; synchronized accepted record and matrix row actions.
- matrix correction: Q4/Q16 are marked as registered existing DOCX entries, Q21 value as refreshed existing, and Q21 people as newly inserted.
- render/model state remains pending until the next gates run.
"""
    THREAD_STATUS.write_text(THREAD_STATUS.read_text(encoding="utf-8") + status_append, encoding="utf-8")

    governor_append = f"""

### Governor Batch21 Refinement

- Q21 `价值判断与价值选择` was strengthened from a thin generic landing into a concrete people-interest value-evaluation chain.
- Matrix action labels now distinguish existing registration, refreshed existing content, and the one newly inserted Q21 people entry.
"""
    GOVERNOR.write_text(GOVERNOR.read_text(encoding="utf-8") + governor_append, encoding="utf-8")

    confucius_append = f"""

### Confucius Batch21 Refinement

- The learner-facing Q21 value-judgment entry now directly teaches: stand with the people, evaluate modernization policies by人民利益, and convert the value orientation into livelihood-improvement practice.
"""
    CONFUCIUS.write_text(CONFUCIUS.read_text(encoding="utf-8") + confucius_append, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, heading = update_docx(timestamp)
    block = extract_q21_value_block()
    accepted_updated = update_accepted(timestamp, heading, block)
    matrix_updates = update_matrix(timestamp)
    append_reports(backup, accepted_updated, matrix_updates)
    print(
        json.dumps(
            {
                "backup": str(backup),
                "heading": heading,
                "accepted_updated": accepted_updated,
                "matrix_updates": matrix_updates,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
