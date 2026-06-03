#!/usr/bin/env python3
"""Aggregate core source-lock cards: extract prompt + rubric snippets per category, output a compact summary the framework writer can consume."""
import csv, re
from pathlib import Path

INDEX = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/04_core_questions.csv")
CARDS_DIR = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/source_lock_cards")
OUT = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/05_framework_aggregation.md")

def read_card(path):
    text = path.read_text(encoding="utf-8")
    def section(name):
        # Find heading, then the first fenced ``` block after it
        m = re.search(rf"## {re.escape(name)}\s*\n(?:.*?\n)*?```\n(.*?)\n```", text, re.S)
        return m.group(1).strip() if m else ""
    prompt = section("真实设问（来自原卷抽取，未润色）")
    material = section("真实材料核心（题干材料，未润色）")
    rubric = section("对应答案/细则/评标/讲评（原文摘录）")
    return prompt, material, rubric

def main():
    with INDEX.open() as f:
        rows = list(csv.DictReader(f))
    by_cat = {}
    for r in rows:
        cards_file = r["card_file"].replace("source_lock_cards/", "")
        card_path = CARDS_DIR / cards_file
        if not card_path.exists():
            continue
        prompt, material, rubric = read_card(card_path)
        for cat in (r["category"] or "未分类").split(", "):
            by_cat.setdefault(cat, []).append({
                "qid": r["question_id"],
                "subq": r["subq"] or "0",
                "evidence_level": r["evidence_level"],
                "prompt": prompt,
                "material_short": material[:400],
                "rubric": rubric,
            })
    lines = ["# 05 Framework Aggregation (from core cards)",
             "",
             "本文件是 STEP 6 框架与 STEP 7 题链的写作中间产物，把 23 道核心题按法律类别归位后，列出每题的设问/材料抓手/细则。",
             ""]
    for cat in sorted(by_cat):
        lines.append(f"## {cat}（{len(by_cat[cat])} 题）")
        lines.append("")
        for item in by_cat[cat]:
            lines.append(f"### `{item['qid']}` 子问{item['subq']} ({item['evidence_level']})")
            lines.append("")
            lines.append("- 设问：")
            for L in item["prompt"].split("\n")[:6]:
                lines.append(f"  > {L.strip()}")
            lines.append("- 材料抓手：")
            for L in item["material_short"].split("\n")[:6]:
                lines.append(f"  > {L.strip()}")
            lines.append("- 细则原文（已截断）：")
            for L in item["rubric"][:1500].split("\n")[:18]:
                if L.strip():
                    lines.append(f"  - {L.strip()}")
            lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}, categories={len(by_cat)}")

if __name__ == "__main__":
    main()
