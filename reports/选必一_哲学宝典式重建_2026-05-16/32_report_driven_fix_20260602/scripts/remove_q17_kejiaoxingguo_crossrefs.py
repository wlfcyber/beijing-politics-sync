from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from docx import Document


ENTRY_PAT = re.compile(r"^\d+\.\s+")
BAD_TERM = "科教兴国战略与人才强国战略（人才与国际竞争力）"


def clean_line(text: str) -> str:
    text = text.replace(BAD_TERM, "")
    text = re.sub(r"；{2,}", "；", text)
    text = text.replace("：；", "：")
    text = text.replace("；；", "；")
    text = text.replace("；)", ")")
    text = text.replace("；）", "）")
    text = re.sub(r"；\s*$", "", text)
    text = re.sub(r"：\s*$", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    doc = Document(args.input)
    in_q17 = False
    changed = []
    for idx, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if ENTRY_PAT.match(text):
            in_q17 = "2026朝阳期中Q17" in text
        if not in_q17 or BAD_TERM not in text:
            continue
        new_text = clean_line(para.text)
        para.text = new_text
        changed.append({"paragraph": idx, "old": text, "new": new_text})

    doc.save(args.output)
    summary = {
        "input": str(args.input),
        "output": str(args.output),
        "bad_term": BAD_TERM,
        "changed_count": len(changed),
        "changed": changed,
    }
    args.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "changed"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
