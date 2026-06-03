#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document


RUN_DIR = Path(__file__).resolve().parent
DOCX = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细则再锁_核心答题点红色强化_学生版_带水印_20260603.docx")
OUT_JSON = RUN_DIR / "round38_samegroup_inventory.json"
OUT_CSV = RUN_DIR / "round38_samegroup_inventory.csv"
OUT_UNIQUE = RUN_DIR / "round38_unique_questions.csv"

QUESTION_RE = re.compile(r"(20\d{2})\s*([^\n\dQ]{1,16}?(?:思政二模|一模|二模|期中|期末|模拟|高考))\s*Q(\d+)(?:\((\d+)\))?")
ITEM_RE = re.compile(r"^\s*\d+\.\s*20\d{2}")
FIELD_RE = re.compile(r"^【(材料触发点|设问|为什么能想到|答案落点|同题组)】")


def iter_text_paragraphs(doc: Document) -> list[dict]:
    return [{"text": p.text.strip(), "style": p.style.name if p.style is not None else ""} for p in doc.paragraphs]


def normalize_key(text: str) -> str | None:
    m = QUESTION_RE.search(text)
    if not m:
        return None
    year, exam, q, sub = m.groups()
    return f"{year}{exam}Q{q}" + (f"({sub})" if sub else "")


def nearest_question(paragraphs: list[dict], idx: int) -> tuple[str, str, int]:
    for j in range(idx - 1, max(-1, idx - 25), -1):
        key = normalize_key(paragraphs[j]["text"])
        if key:
            return key, paragraphs[j]["text"], j
    raise RuntimeError(f"Cannot locate question heading before paragraph {idx}")


def nearest_core(paragraphs: list[dict], idx: int) -> str:
    for j in range(idx - 1, -1, -1):
        text = paragraphs[j]["text"]
        if text.startswith("核心答题点：") or text.startswith("【核心答题点】"):
            return text
    return ""


def extract_samegroup_lines(paragraphs: list[dict], idx: int) -> list[str]:
    lines: list[str] = []
    for para in paragraphs[idx + 1 :]:
        text = para["text"]
        style = para["style"]
        if style.startswith("Heading"):
            break
        if not text:
            continue
        if ITEM_RE.match(text) or text.startswith("核心答题点：") or text.startswith("【核心答题点】"):
            break
        if FIELD_RE.match(text) and not text.startswith("【同题组】"):
            break
        lines.append(text)
    return lines


def main() -> None:
    doc = Document(DOCX)
    paragraphs = iter_text_paragraphs(doc)
    records = []
    for i, text in enumerate(paragraphs):
        if "【同题组】" not in text["text"]:
            continue
        key, title, title_idx = nearest_question(paragraphs, i)
        lines = extract_samegroup_lines(paragraphs, i)
        records.append(
            {
                "key": key,
                "question_title": title,
                "question_paragraph_index": title_idx,
                "samegroup_paragraph_index": i,
                "core_heading": nearest_core(paragraphs, i),
                "samegroup_marker": text["text"],
                "samegroup_lines": lines,
                "samegroup_text": "\n".join([text["text"]] + lines),
            }
        )

    by_key: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_key[record["key"]].append(record)

    unique_rows = []
    for key, recs in sorted(by_key.items()):
        unique_rows.append(
            {
                "key": key,
                "count": len(recs),
                "sample_title": recs[0]["question_title"],
                "sample_core_heading": recs[0]["core_heading"],
                "sample_samegroup_text": recs[0]["samegroup_text"],
            }
        )

    OUT_JSON.write_text(json.dumps({"records": records, "unique": unique_rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "key",
                "question_title",
                "question_paragraph_index",
                "samegroup_paragraph_index",
                "core_heading",
                "samegroup_marker",
                "samegroup_text",
            ],
        )
        writer.writeheader()
        for record in records:
            writer.writerow({field: record.get(field, "") for field in writer.fieldnames})
    with OUT_UNIQUE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["key", "count", "sample_title", "sample_core_heading", "sample_samegroup_text"])
        writer.writeheader()
        writer.writerows(unique_rows)

    print(
        json.dumps(
            {
                "docx": str(DOCX),
                "samegroup_records": len(records),
                "unique_questions": len(unique_rows),
                "top_counts": Counter(r["key"] for r in records).most_common(15),
                "outputs": [str(OUT_JSON), str(OUT_CSV), str(OUT_UNIQUE)],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
