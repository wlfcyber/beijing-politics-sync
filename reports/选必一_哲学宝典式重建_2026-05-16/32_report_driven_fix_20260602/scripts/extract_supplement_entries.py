from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TARGETS = [
    "2024丰台一模Q20",
    "2024丰台一模Q21",
    "2024石景山一模Q19",
    "2025朝阳一模Q20",
    "2025朝阳二模Q21",
    "2025海淀一模Q21",
    "2025石景山一模Q17",
    "2025门头沟一模Q19",
    "2026东城二模Q20",
    "2026丰台二模Q20",
    "2026丰台期末Q21",
    "2026房山二模Q20",
    "2026朝阳二模Q20",
    "2026海淀期中Q22",
    "2026西城一模Q20",
    "2026通州一模Q19",
]


def compact(text: str) -> str:
    return re.sub(r"[\s()（）第问：:，,。；;、\"“”'‘’_\-—]+", "", text)


def target_hit(title: str) -> str | None:
    ctitle = compact(title)
    for target in TARGETS:
        if compact(target) in ctitle:
            return target
        # Allow subquestion variants such as Q19(2), Q20(3)
        base = compact(re.sub(r"Q(\d+)$", r"Q\1", target))
        if base in ctitle:
            return target
    return None


def parse_blocks(md_path: Path):
    lines = md_path.read_text(encoding="utf-8").splitlines()
    h1 = ""
    h2 = ""
    entries = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ") and not line.startswith("## "):
            h1 = line[2:].strip()
            i += 1
            continue
        if line.startswith("## 核心答题点："):
            h2 = line[3:].strip()
            h2 = re.sub(r"（出现\d+次）", "", h2)
            i += 1
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            hit = target_hit(title)
            start = i
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("## ") and not lines[i].startswith("# "):
                block.append(lines[i])
                i += 1
            if hit:
                entries.append({
                    "target": hit,
                    "h1": h1,
                    "core": h2,
                    "title": title,
                    "start_line": start + 1,
                    "block": "\n".join(block).strip(),
                    "fields": extract_fields(block),
                })
            continue
        i += 1
    return entries


def extract_fields(lines: list[str]) -> dict[str, str]:
    text = "\n".join(lines)
    labels = ["什么时候写", "设问", "得分层次", "为什么能想到", "卷面句", "同题组"]
    fields: dict[str, str] = {}
    for idx, label in enumerate(labels):
        start = text.find(f"【{label}】")
        if start < 0:
            continue
        start += len(f"【{label}】")
        end = len(text)
        for next_label in labels[idx + 1:]:
            nxt = text.find(f"【{next_label}】", start)
            if nxt >= 0:
                end = min(end, nxt)
        fields[label] = text[start:end].strip()
    return fields


def clean_why(text: str) -> str:
    parts = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"^[-•]\s*", "", line)
        line = re.sub(r"^(材料信号|设问意图|答题动作)：", "", line)
        parts.append(line)
    return "".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("md", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    entries = parse_blocks(args.md)
    for entry in entries:
        f = entry["fields"]
        entry["current_fields"] = {
            "材料触发点": f.get("什么时候写", ""),
            "设问": f.get("设问", ""),
            "为什么能想到": clean_why(f.get("为什么能想到", "")),
            "答案落点": f.get("卷面句", ""),
            "同题组": f.get("同题组", ""),
            "得分层次": f.get("得分层次", ""),
        }
    args.json.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {}
    for e in entries:
        counts[e["target"]] = counts.get(e["target"], 0) + 1
    print(json.dumps({"entries": len(entries), "counts": counts}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
