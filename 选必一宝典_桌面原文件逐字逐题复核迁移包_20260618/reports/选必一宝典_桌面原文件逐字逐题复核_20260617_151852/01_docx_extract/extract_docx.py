from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


SOURCE = Path("/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx")
OUT_DIR = Path("/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/01_docx_extract")
EXPECTED_SHA256 = "876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e"

FIELD_NAMES = ["术语", "完整设问", "细则位置", "来源", "材料触发", "答案句"]
DOC_FIELD_LABELS = ["材料触发点", "设问", "为什么能想到", "答案落点", "同题组"]
QUESTION_RE = re.compile(r"(20\d{2}[^，。\n]{0,12}(?:一模|二模|期中|期末|适应性|模拟)?[^，。\n]{0,12}(?:第?\d+题|Q\d+)|Q\d+|第\d+题)")
NUMBERED_QUESTION_RE = re.compile(r"^\d+[.．]\s*(.+?(?:20\d{2}|Q\d+|第\d+题).*)$")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_blocks(doc: Document):
    for child in doc.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield "paragraph", Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield "table", Table(child, doc)


def paragraph_record(idx: int, para: Paragraph) -> dict:
    text = para.text.strip()
    style = para.style.name if para.style is not None else ""
    return {
        "block_id": idx,
        "type": "paragraph",
        "style": style,
        "text": text,
        "rows": None,
    }


def table_record(idx: int, table: Table) -> dict:
    rows = []
    flat_parts = []
    for r_i, row in enumerate(table.rows, start=1):
        cells = []
        for c_i, cell in enumerate(row.cells, start=1):
            cell_text = "\n".join(p.text.strip() for p in cell.paragraphs if p.text.strip())
            cells.append(cell_text)
            if cell_text:
                flat_parts.append(f"R{r_i}C{c_i}: {cell_text}")
        rows.append(cells)
    return {
        "block_id": idx,
        "type": "table",
        "style": "",
        "text": "\n".join(flat_parts).strip(),
        "rows": rows,
    }


def classify_field(text: str) -> list[str]:
    hits = []
    for name in FIELD_NAMES:
        if f"{name}：" in text or f"{name}:" in text:
            hits.append(name)
    return hits


def extract_question_ref(text: str) -> str:
    match = QUESTION_RE.search(text)
    return match.group(1) if match else ""


def build_entry_candidates(records: list[dict]) -> list[dict]:
    entries = []
    current = None
    current_heading = ""
    doc_order = 0

    for rec in records:
        text = rec["text"]
        if not text:
            continue

        style = rec.get("style") or ""
        if style.lower().startswith("heading") or text in {"时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"}:
            current_heading = text

        if "术语：" in text or "术语:" in text:
            if current:
                entries.append(current)
            doc_order += 1
            current = {
                "entry_id": f"E{doc_order:04d}",
                "start_block_id": rec["block_id"],
                "end_block_id": rec["block_id"],
                "section_heading": current_heading,
                "question_ref": extract_question_ref(text),
                "fields_present": set(classify_field(text)),
                "text": [text],
            }
            continue

        if current:
            current["end_block_id"] = rec["block_id"]
            current["fields_present"].update(classify_field(text))
            if not current["question_ref"]:
                current["question_ref"] = extract_question_ref(text)
            current["text"].append(text)

    if current:
        entries.append(current)

    normalized = []
    for entry in entries:
        missing = [name for name in FIELD_NAMES if name not in entry["fields_present"]]
        joined = "\n".join(entry["text"])
        normalized.append(
            {
                "entry_id": entry["entry_id"],
                "start_block_id": entry["start_block_id"],
                "end_block_id": entry["end_block_id"],
                "section_heading": entry["section_heading"],
                "question_ref": entry["question_ref"],
                "fields_present": sorted(entry["fields_present"]),
                "missing_fields": missing,
                "char_count": len(joined),
                "text_preview": joined[:300],
            }
        )
    return normalized


def doc_field_hits(text: str) -> list[str]:
    hits = []
    for label in DOC_FIELD_LABELS:
        if f"【{label}】" in text or f"[{label}]" in text:
            hits.append(label)
    return hits


def build_question_candidates(records: list[dict]) -> list[dict]:
    entries = []
    current = None
    h1 = h2 = h3 = ""
    doc_order = 0

    def close_current():
        nonlocal current
        if current:
            joined = "\n".join(current["text"])
            fields_present = sorted(current["fields_present"])
            current["fields_present"] = fields_present
            current["missing_doc_fields"] = [label for label in DOC_FIELD_LABELS if label not in fields_present]
            current["char_count"] = len(joined)
            current["text_preview"] = joined[:500]
            entries.append(current)
            current = None

    for rec in records:
        text = rec["text"]
        if not text:
            continue
        style = rec.get("style") or ""

        if style == "Heading 1":
            close_current()
            h1 = text
            h2 = h3 = ""
            continue
        if style == "Heading 2":
            close_current()
            h2 = text
            h3 = ""
            continue
        if style == "Heading 3":
            close_current()
            h3 = text
            continue

        q_match = NUMBERED_QUESTION_RE.match(text)
        if q_match:
            close_current()
            doc_order += 1
            question_title = q_match.group(1).strip()
            core_point = h3.removeprefix("核心答题点：").strip() if h3.startswith("核心答题点：") else h3
            current = {
                "entry_id": f"Q{doc_order:04d}",
                "doc_order": doc_order,
                "start_block_id": rec["block_id"],
                "end_block_id": rec["block_id"],
                "bucket": h1,
                "sub_bucket": h2,
                "core_point": core_point,
                "question_title": question_title,
                "question_ref": extract_question_ref(question_title) or question_title,
                "fields_present": set(doc_field_hits(text)),
                "text": [text],
            }
            continue

        if current:
            current["end_block_id"] = rec["block_id"]
            current["fields_present"].update(doc_field_hits(text))
            current["text"].append(text)

    close_current()
    return entries


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    actual_sha = sha256(SOURCE)
    if actual_sha != EXPECTED_SHA256:
        print(f"SHA256 mismatch: {actual_sha} != {EXPECTED_SHA256}", file=sys.stderr)
        return 2

    doc = Document(str(SOURCE))
    records = []
    for idx, (kind, block) in enumerate(iter_blocks(doc), start=1):
        if kind == "paragraph":
            records.append(paragraph_record(idx, block))
        else:
            records.append(table_record(idx, block))

    with (OUT_DIR / "blocks.jsonl").open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    with (OUT_DIR / "paragraph_table_inventory.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["block_id", "type", "style", "text"])
        writer.writeheader()
        for rec in records:
            writer.writerow({k: rec[k] for k in ["block_id", "type", "style", "text"]})

    with (OUT_DIR / "full_text.md").open("w", encoding="utf-8") as f:
        f.write(f"# Extracted Text\n\nsource: {SOURCE}\nsha256: {actual_sha}\n\n")
        for rec in records:
            if rec["text"]:
                f.write(f"\n\n<!-- block:{rec['block_id']} type:{rec['type']} style:{rec['style']} -->\n")
                f.write(rec["text"])

    entries = build_entry_candidates(records)
    with (OUT_DIR / "entry_candidates.jsonl").open("w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    with (OUT_DIR / "entry_candidates.csv").open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "entry_id",
            "start_block_id",
            "end_block_id",
            "section_heading",
            "question_ref",
            "fields_present",
            "missing_fields",
            "char_count",
            "text_preview",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            row = dict(entry)
            row["fields_present"] = ";".join(row["fields_present"])
            row["missing_fields"] = ";".join(row["missing_fields"])
            writer.writerow(row)

    question_entries = build_question_candidates(records)
    with (OUT_DIR / "question_entry_candidates.jsonl").open("w", encoding="utf-8") as f:
        for entry in question_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    with (OUT_DIR / "question_entry_candidates.csv").open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "entry_id",
            "doc_order",
            "start_block_id",
            "end_block_id",
            "bucket",
            "sub_bucket",
            "core_point",
            "question_title",
            "question_ref",
            "fields_present",
            "missing_doc_fields",
            "char_count",
            "text_preview",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in question_entries:
            row = {k: entry[k] for k in fieldnames}
            row["fields_present"] = ";".join(row["fields_present"])
            row["missing_doc_fields"] = ";".join(row["missing_doc_fields"])
            writer.writerow(row)

    with zipfile.ZipFile(SOURCE) as zf:
        names = set(zf.namelist())
    structure = {
        "source": str(SOURCE),
        "sha256": actual_sha,
        "block_count": len(records),
        "entry_candidate_count": len(entries),
        "question_entry_candidate_count": len(question_entries),
        "has_comments_xml": "word/comments.xml" in names,
        "has_footnotes_xml": "word/footnotes.xml" in names,
        "has_endnotes_xml": "word/endnotes.xml" in names,
        "has_numbering_xml": "word/numbering.xml" in names,
        "has_styles_xml": "word/styles.xml" in names,
    }
    (OUT_DIR / "extract_summary.json").write_text(json.dumps(structure, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(structure, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
