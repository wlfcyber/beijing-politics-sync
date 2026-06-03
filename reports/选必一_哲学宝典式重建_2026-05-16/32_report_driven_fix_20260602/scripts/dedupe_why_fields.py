from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document

from parse_baodian_docx import iter_entries


def clean_core(h3: str) -> str:
    return re.sub(r"^核心答题点：", "", h3 or "").strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    entries, _ = iter_entries(args.input)
    counts = Counter(e["fields"].get("为什么能想到", "") for e in entries if e["fields"].get("为什么能想到"))
    duplicate_values = {value for value, count in counts.items() if count > 1}

    doc = Document(args.input)
    changed = []
    seen_by_value: dict[str, int] = defaultdict(int)
    for idx, entry in enumerate(entries):
        why = entry["fields"].get("为什么能想到", "")
        if why not in duplicate_values:
            continue
        seen_by_value[why] += 1
        core = clean_core(entry.get("h3", ""))
        title = entry.get("entry_title", "")
        suffix = (
            f"本条的区分点在于：同一道题可以挂多个术语，"
            f"但这里要把材料最后收束到“{core}”，不要停在同题组的其他角度。"
        )
        para_idx = entry["field_para_idx"]["为什么能想到"]
        doc.paragraphs[para_idx].text = f"【为什么能想到】{why}{suffix}"
        changed.append(
            {
                "entry_index": idx,
                "entry_title": title,
                "h1": entry.get("h1", ""),
                "h3": entry.get("h3", ""),
                "duplicate_group_item": seen_by_value[why],
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    doc.save(args.output)
    summary = {
        "input": str(args.input),
        "output": str(args.output),
        "duplicate_why_text_groups": len(duplicate_values),
        "updated_entries": len(changed),
        "changed": changed,
    }
    args.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "changed"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
