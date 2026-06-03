#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import argparse
import re
from pathlib import Path


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
DEFAULT_AUDIT = RUN / "03_structured" / "DRAFT_ENTRY_AUDIT.csv"
OUT = RUN / "05_qa"


def compact(s: str) -> str:
    s = s or ""
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[，。；：、（）()《》“”\"'？?！!·,.；:：\[\]【】\-_—/]", "", s)
    return s


def best_chunk_hit(needle: str, haystack: str):
    n = compact(needle)
    h = compact(haystack)
    if not n:
        return "EMPTY"
    if n in h:
        return "EXACT"
    # OCR and teacher-version punctuation can differ; use long chunks to avoid false positives.
    chunks = []
    for size in (28, 22, 16, 12):
        for i in range(0, max(0, len(n) - size + 1), max(1, size // 2)):
            chunks.append(n[i:i + size])
    hits = [c for c in chunks if len(c) >= 12 and c in h]
    if len(hits) >= 2 or (hits and len(n) < 28):
        return "PARTIAL"
    return "NO_MATCH"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--prefix", default="DRAFT")
    return parser.parse_args()


def main():
    args = parse_args()
    prefix = args.prefix.upper()
    OUT.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(args.audit.open(encoding="utf-8-sig")))
    out_rows = []
    for row in rows:
        card_text = ""
        if row.get("card_path") and Path(row["card_path"]).exists():
            card_text = Path(row["card_path"]).read_text(encoding="utf-8")
        prompt_status = best_chunk_hit(row.get("设问", ""), card_text)
        score = row.get("得分层次", "")
        score_status = best_chunk_hit(score, card_text) if score else "EMPTY"
        surface_status = best_chunk_hit(row.get("卷面句", ""), card_text)
        flags = []
        if row["evidence_status"] != "RAW_CARD_READY":
            flags.append("NO_CONFIRMED_CARD")
        if prompt_status == "NO_MATCH":
            flags.append("PROMPT_NOT_IN_CARD")
        if score and score_status == "NO_MATCH":
            flags.append("SCORE_TEXT_NOT_IN_CARD")
        out = dict(row)
        out.update({
            "prompt_check": prompt_status,
            "score_check": score_status,
            "surface_check": surface_status,
            "qa_flags": ";".join(flags),
        })
        out_rows.append(out)

    fieldnames = list(out_rows[0].keys())
    with (OUT / f"{prefix}_VS_SOURCE_QA.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)
    flagged = [r for r in out_rows if r["qa_flags"]]
    with (OUT / f"{prefix}_VS_SOURCE_FLAGS.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(flagged)
    print("rows", len(out_rows))
    print("flagged", len(flagged))
    from collections import Counter
    print("prompt", Counter(r["prompt_check"] for r in out_rows))
    print("score", Counter(r["score_check"] for r in out_rows))


if __name__ == "__main__":
    main()
