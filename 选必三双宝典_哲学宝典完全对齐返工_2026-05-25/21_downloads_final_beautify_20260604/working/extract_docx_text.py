from __future__ import annotations

import csv
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}


def qn(tag: str) -> str:
    prefix, name = tag.split(":")
    return f"{{{NS[prefix]}}}{name}"


def paragraph_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        if node.tag == qn("w:t"):
            parts.append(node.text or "")
        elif node.tag == qn("w:tab"):
            parts.append("\t")
        elif node.tag in {qn("w:br"), qn("w:cr")}:
            parts.append("\n")
    return "".join(parts)


def paragraph_style(p: ET.Element) -> str:
    p_style = p.find("./w:pPr/w:pStyle", NS)
    if p_style is None:
        return ""
    return p_style.attrib.get(qn("w:val"), "")


def extract_paragraphs(docx_path: Path) -> list[dict]:
    with zipfile.ZipFile(docx_path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    paragraphs: list[dict] = []
    for i, p in enumerate(root.iter(qn("w:p")), start=1):
        text = paragraph_text(p).strip()
        style = paragraph_style(p)
        if text:
            paragraphs.append({"p_index": i, "style": style, "text": text})
    return paragraphs


def heading_level(style: str, text: str) -> int | None:
    m = re.search(r"Heading(\d+)|标题\s*(\d+)", style or "", re.I)
    if m:
        return int(next(g for g in m.groups() if g))
    if re.match(r"^第[一二三四五六七八九十]+[部分章]", text):
        return 1
    if re.match(r"^[一二三四五六七八九十]+、", text):
        return 2
    if re.match(r"^（[一二三四五六七八九十]+）", text):
        return 3
    if re.match(r"^\d+[.、]\s*", text):
        return 4
    return None


def build_context(paragraphs: list[dict]) -> list[dict]:
    stack: dict[int, str] = {}
    rows: list[dict] = []
    for p in paragraphs:
        level = heading_level(p["style"], p["text"])
        if level is not None:
            stack[level] = p["text"]
            for old in list(stack):
                if old > level:
                    del stack[old]
        row = dict(p)
        row["heading_level"] = level or ""
        row["h1"] = stack.get(1, "")
        row["h2"] = stack.get(2, "")
        row["h3"] = stack.get(3, "")
        row["h4"] = stack.get(4, "")
        rows.append(row)
    return rows


FIELD_NAMES = ["材料触发点", "设问", "为什么能想到", "答案落点", "同题说明"]
FIELD_RE = re.compile(r"^【(" + "|".join(FIELD_NAMES) + r")】\s*(.*)")
ANY_FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)")
ENTRY_TITLE_RE = re.compile(r"^(?:\d+[.、]\s+|补充[:：])")


def parse_entries(rows: list[dict]) -> list[dict]:
    entries: list[dict] = []
    current: dict | None = None
    current_field: str | None = None

    def start_entry(row: dict) -> dict:
        return {
            "entry_no": len(entries) + 1,
            "title": row["text"],
            "start_p": row["p_index"],
            "end_p": row["p_index"],
            "h1": row.get("h1", ""),
            "h2": row.get("h2", ""),
            "h3": row.get("h3", ""),
            "h4": row.get("h4", ""),
            "fields": {name: "" for name in FIELD_NAMES},
            "other_notes": [],
            "raw": [row["text"]],
        }

    for row in rows:
        text = row["text"]
        if ENTRY_TITLE_RE.match(text):
            if current:
                entries.append(current)
            current = start_entry(row)
            current_field = None
            continue

        field_m = FIELD_RE.match(text)
        if field_m:
            if current is None:
                current = start_entry({**row, "text": ""})
                current["raw"] = []
            current_field = field_m.group(1)
            current["fields"][current_field] = field_m.group(2).strip()
            current["raw"].append(text)
            current["end_p"] = row["p_index"]
            continue

        other_m = ANY_FIELD_RE.match(text)
        if other_m and current is not None:
            current["other_notes"].append({"label": other_m.group(1), "text": other_m.group(2).strip(), "p_index": row["p_index"]})
            current["raw"].append(text)
            current["end_p"] = row["p_index"]
            current_field = None
            continue

        if current is not None:
            if current_field and text:
                current["fields"][current_field] = (current["fields"][current_field] + "\n" + text).strip()
            current["raw"].append(text)
            current["end_p"] = row["p_index"]

    if current:
        entries.append(current)
    return entries


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: extract_docx_text.py input.docx out_dir")
    docx_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    paragraphs = extract_paragraphs(docx_path)
    rows = build_context(paragraphs)
    entries = parse_entries(rows)

    (out_dir / "doc_text.txt").write_text("\n".join(r["text"] for r in rows), encoding="utf-8")
    with (out_dir / "doc_paragraphs.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["p_index", "style", "heading_level", "h1", "h2", "h3", "h4", "text"], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    with (out_dir / "entries.json").open("w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    with (out_dir / "entries.tsv").open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["entry_no", "title", "start_p", "end_p", "h1", "h2", "h3", "h4", "other_note_labels"] + FIELD_NAMES
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for e in entries:
            row = {k: e.get(k, "") for k in ["entry_no", "title", "start_p", "end_p", "h1", "h2", "h3", "h4"]}
            row["other_note_labels"] = "|".join(note["label"] for note in e.get("other_notes", []))
            row.update(e["fields"])
            writer.writerow(row)

    summary = {
        "docx": str(docx_path),
        "paragraph_count": len(rows),
        "entry_count": len(entries),
        "same_question_note_count": sum(1 for e in entries if e["fields"].get("同题说明")),
        "missing_fields": {
            name: sum(1 for e in entries if not e["fields"].get(name, "").strip())
            for name in FIELD_NAMES[:-1]
        },
    }
    (out_dir / "extract_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
