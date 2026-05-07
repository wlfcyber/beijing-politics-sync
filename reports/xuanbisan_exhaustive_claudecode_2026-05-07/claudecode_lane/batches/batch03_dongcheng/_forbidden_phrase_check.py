# -*- coding: utf-8 -*-
"""Check entries.jsonl student-facing fields for forbidden phrases."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).parent

# Forbidden phrases per hard rules notebook §11 学生版与审计版分离
FORBIDDEN = [
    "评标",
    "参考答案",
    "答案写",
    "可从",
    "答案/补充",
    "答案核",
    "A-formal",
    "B-choice-signal",
    "phase05",
    "source_pool",
    "/Users/",
    "OCR",
    "debug",
    "filled",
    "correct_option_chain",
    "固定分析流程",
    "v7漏了",
]

# C:\ check needs to be done specifically
def has_windows_path(text):
    return "C:\\" in text or "c:\\" in text

# Note: 学生面向字段 in entries.jsonl
STUDENT_FIELDS = [
    "设问",
    "材料触发点",
    "为什么能想到",
    "答案落点",
    "题干信号",
    "完整选项或选项单位",
    "正确项理由",
    "诱人错项",
    "material_signal",
    "answer_sentence",
]
# Note: trigger_logic is a research/teaching field for choice_trap and may legitimately reference
# 答案源 / 细则 / 评分 since those are part of the 学生 transferable reasoning explanation,
# not as final 学生稿正文. We exclude trigger_logic from this hard check.


def main():
    hits = []
    p = BASE / "entries" / "batch03_entries.jsonl"
    with p.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            qid = obj.get("question_id", "?")
            for fld in STUDENT_FIELDS:
                text = str(obj.get(fld, ""))
                for phrase in FORBIDDEN:
                    if phrase in text:
                        hits.append((qid, fld, phrase, text[:120]))
                if has_windows_path(text):
                    hits.append((qid, fld, "C:\\\\", text[:120]))

    print(f"Forbidden phrase hits in student-facing fields:")
    for h in hits:
        print(f"  {h[0]} | field={h[1]} | hit={h[2]}")
        print(f"    text: {h[3]}")
    print(f"Total hits: {len(hits)}")
    return len(hits)


if __name__ == "__main__":
    sys.exit(main())
