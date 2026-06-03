#!/usr/bin/env python3
import csv
import json
import re
import sys
from pathlib import Path

from docx import Document


ENTRY_RE = re.compile(r"^(\d+)[.．]\s*(\d{4}.+)$")
FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")
SOURCE_RE = re.compile(r"(\d{4}[^Q\n，。；;：:（）()【】]*?Q\d+(?:\(\d+\))?)")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: extract_claude_docx_entries.py INPUT.docx OUTDIR", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = Document(input_path)
    paragraphs = []
    text_lines = []
    for idx, para in enumerate(doc.paragraphs, 1):
        text = clean(para.text)
        paragraphs.append(
            {
                "para_no": idx,
                "style": para.style.name if para.style else "",
                "text": text,
            }
        )
        if text:
            text_lines.append(text)

    (out_dir / "claude_docx_text.txt").write_text("\n".join(text_lines), encoding="utf-8")
    with (out_dir / "claude_docx_paragraphs.jsonl").open("w", encoding="utf-8") as f:
        for row in paragraphs:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    entries = []
    bucket = ""
    second_level = ""
    core_point = ""
    current = None

    def flush():
        nonlocal current
        if not current:
            return
        raw_lines = current.pop("_raw_lines")
        fields = current.pop("_fields")
        current["when_to_write"] = fields.get("什么时候写", "")
        current["prompt"] = fields.get("设问", "")
        current["score_layers"] = fields.get("得分层次", "")
        current["why_signal"] = fields.get("为什么能想到", "")
        current["surface_sentence"] = fields.get("卷面句", "")
        current["same_group"] = fields.get("同题组", "")
        current["other_fields_json"] = json.dumps(
            {k: v for k, v in fields.items() if k not in {"什么时候写", "设问", "得分层次", "为什么能想到", "卷面句", "同题组"}},
            ensure_ascii=False,
        )
        current["raw_block"] = "\n".join(raw_lines)
        current["mentioned_sources"] = "；".join(sorted(set(SOURCE_RE.findall(current["raw_block"]))))
        entries.append(current)
        current = None

    for row in paragraphs:
        text = row["text"]
        if not text:
            continue
        style = row["style"]
        if style == "Heading 1":
            flush()
            bucket = text
            second_level = ""
            core_point = ""
            continue
        if style == "Heading 2":
            flush()
            second_level = text
            core_point = ""
            continue
        if style == "Heading 3":
            flush()
            core_point = text.replace("核心答题点：", "").strip()
            continue

        m = ENTRY_RE.match(text)
        if m and bucket and bucket not in {"二级结构说明"}:
            flush()
            current = {
                "global_entry_no": len(entries) + 1,
                "local_entry_no": m.group(1),
                "source_label": m.group(2).strip(),
                "bucket": bucket,
                "second_level": second_level,
                "core_point": core_point,
                "start_para": row["para_no"],
                "_fields": {},
                "_raw_lines": [text],
            }
            continue

        if current:
            current["_raw_lines"].append(text)
            fm = FIELD_RE.match(text)
            if fm:
                field_name, field_text = fm.group(1), fm.group(2)
                current["_fields"][field_name] = field_text
            else:
                # Append continuation text to the last known field. This keeps
                # multiline 同题组 lists attached to the entry without guessing
                # semantic roles.
                if current["_fields"]:
                    last_key = next(reversed(current["_fields"]))
                    current["_fields"][last_key] = clean(current["_fields"][last_key] + "\n" + text)

    flush()

    fieldnames = [
        "global_entry_no",
        "local_entry_no",
        "source_label",
        "bucket",
        "second_level",
        "core_point",
        "start_para",
        "mentioned_sources",
        "when_to_write",
        "prompt",
        "score_layers",
        "why_signal",
        "surface_sentence",
        "same_group",
        "other_fields_json",
        "raw_block",
    ]
    with (out_dir / "ENTRY_INDEX.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow({k: entry.get(k, "") for k in fieldnames})

    with (out_dir / "ENTRY_INDEX.jsonl").open("w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    summary = {
        "input": str(input_path),
        "paragraphs": len(paragraphs),
        "nonempty_paragraphs": len(text_lines),
        "entries": len(entries),
        "buckets": sorted(set(e["bucket"] for e in entries)),
        "entries_by_bucket": {},
    }
    for entry in entries:
        summary["entries_by_bucket"][entry["bucket"]] = summary["entries_by_bucket"].get(entry["bucket"], 0) + 1
    (out_dir / "extract_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
