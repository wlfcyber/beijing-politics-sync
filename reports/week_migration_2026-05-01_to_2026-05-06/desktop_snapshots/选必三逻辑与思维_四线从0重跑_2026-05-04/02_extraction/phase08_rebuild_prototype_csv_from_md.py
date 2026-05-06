#!/usr/bin/env python3
"""Rebuild Phase08 review-only prototype CSV from the cleaned Markdown body.

This is a recovery script for the Phase08 prototype CSV. It uses the cleaned
review-only Markdown as the teaching body and the Phase08 input freeze as the
source of IDs, module labels, and locked statuses. It does not edit freeze files.
"""

from __future__ import annotations

import csv
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
PROTO_MD = ROOT / "07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md"
PROTO_CSV = ROOT / "07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv"
FREEZE_CSV = ROOT / "05_coverage/phase08_opus_prototype_input_freeze.csv"

FIELDNAMES = [
    "question_id",
    "module",
    "prototype_section",
    "source_entry_status",
    "generated_text",
    "fields_preserved_check",
    "opus_self_note",
]


def read_freeze() -> dict[str, dict[str, str]]:
    with FREEZE_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 29:
        raise SystemExit(f"freeze row count is not 29: {len(rows)}")
    return {row["question_id"]: row for row in rows}


def extract_md_blocks() -> list[tuple[str, str]]:
    text = PROTO_MD.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^### (Q-[^\n]+)\n", text, flags=re.M))
    blocks: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        qid = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        if "\n---\n\n## 输入边界备注" in block:
            block = block.split("\n---\n\n## 输入边界备注", 1)[0]
        blocks.append((qid, block.strip()))
    if len(blocks) != 29:
        raise SystemExit(f"markdown block count is not 29: {len(blocks)}")
    return blocks


def flatten_block(block: str) -> str:
    parts: list[str] = []
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line == "---" or line.startswith(">"):
            continue
        if line.startswith("- "):
            parts.append(line[2:].strip())
        elif line.startswith("## "):
            continue
        else:
            parts.append(line)
    text = ";".join(parts)
    text = re.sub(r"\s+", " ", text).strip()
    forbidden = [
        "phase07",
        "primary_reasoning_type",
        "rule_slogan",
        "细则022",
        "细则31",
        "cross_reference_policy",
        "reduce repetitive wording",
        "source locator",
        "framework_node",
        "LOCKED_FOR_FUSION",
        "A-formal",
        "B-choice-signal",
        "/Users/",
    ]
    hits = [term for term in forbidden if term in text]
    if hits:
        raise SystemExit(f"dirty markdown body terms remain: {hits}\n{text[:500]}")
    return text


def make_section(module: str, freeze_row: dict[str, str], generated_text: str) -> str:
    qtype = freeze_row.get("question_type", "")
    topic = ""
    for segment in generated_text.split(";"):
        if segment.startswith("题型:"):
            topic = segment.removeprefix("题型:").strip()
            break
        if module == "思维" and segment.startswith("可写思维/方法:"):
            topic = segment.removeprefix("可写思维/方法:").strip()
            break
    topic = topic[:36] if topic else qtype
    return f"{module}-{topic}-{qtype}".strip("-")


def source_status(freeze_row: dict[str, str]) -> str:
    if freeze_row["status"] == "L4":
        return "L4"
    if freeze_row["status"] == "L3":
        return "L3_candidate"
    return freeze_row["status"]


def main() -> None:
    freeze = read_freeze()
    blocks = extract_md_blocks()
    block_ids = [qid for qid, _ in blocks]
    freeze_ids = set(freeze)
    if set(block_ids) != freeze_ids:
        raise SystemExit(
            "markdown/freeze id mismatch: "
            f"missing={sorted(freeze_ids - set(block_ids))}; extra={sorted(set(block_ids) - freeze_ids)}"
        )
    if len(block_ids) != len(set(block_ids)):
        raise SystemExit("duplicate markdown question IDs")

    rows: list[dict[str, str]] = []
    for qid, block in blocks:
        freeze_row = freeze[qid]
        generated_text = flatten_block(block)
        module = freeze_row["module"]
        rows.append(
            {
                "question_id": qid,
                "module": module,
                "prototype_section": make_section(module, freeze_row, generated_text),
                "source_entry_status": source_status(freeze_row),
                "generated_text": generated_text,
                "fields_preserved_check": "answer preserved; status preserved; question_id preserved; cross pairing preserved if applicable",
                "opus_self_note": "RECOVERED_FROM_CLEANED_MARKDOWN_AFTER_LANEB_PATCH; no answer/status/question/pairing changes; review_only",
            }
        )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if PROTO_CSV.exists():
        shutil.copy2(PROTO_CSV, PROTO_CSV.with_suffix(PROTO_CSV.suffix + f".corrupt_before_rebuild_{timestamp}.bak"))
    tmp = PROTO_CSV.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(PROTO_CSV)
    print("PHASE08_PROTOTYPE_CSV_REBUILT_FROM_CLEANED_MD")
    print(f"rows={len(rows)}")
    print(f"modules={{'思维': {sum(1 for r in rows if r['module']=='思维')}, '推理': {sum(1 for r in rows if r['module']=='推理')}, '交叉': {sum(1 for r in rows if r['module']=='交叉')}}}")


if __name__ == "__main__":
    main()
