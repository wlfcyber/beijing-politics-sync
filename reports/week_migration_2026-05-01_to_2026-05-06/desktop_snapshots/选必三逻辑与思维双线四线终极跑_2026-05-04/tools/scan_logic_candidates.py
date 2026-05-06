#!/usr/bin/env python3
"""Scan local readable caches for 选必三《逻辑与思维》思维/推理候选题.

This is an inventory helper only. Hits are not promoted as evidence until a
later pass re-opens the paired paper, answer key, and rubric/marking source.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


THINKING_TERMS = {
    "科学思维": ["科学思维", "客观性", "预见性", "可检验性"],
    "辩证思维": ["辩证思维", "分析与综合", "整体性", "动态性", "质量互变", "适度原则", "辩证否定"],
    "创新思维": ["创新思维", "超前思维", "联想思维", "发散思维", "聚合思维", "逆向思维", "迁移", "想象"],
    "思维抽象与思维具体": ["思维抽象", "思维具体", "感性具体", "认识发展历程"],
    "逻辑与思维提示": ["运用《逻辑与思维》", "逻辑与思维", "系统观念"],
}

REASONING_TERMS = {
    "三段论": ["三段论", "中项", "大项", "小项", "周延", "四概念"],
    "假言推理": ["假言推理", "充分条件假言", "必要条件假言", "充要条件", "肯定前件", "否定后件", "肯前", "否后"],
    "选言推理": ["选言推理", "相容选言", "不相容选言", "或者", "要么"],
    "联言推理": ["联言推理", "联言判断"],
    "归纳推理": ["归纳推理", "不完全归纳", "完全归纳", "求同法", "求异法", "共变法", "剩余法"],
    "类比推理": ["类比推理", "类比"],
    "换质换位": ["换质", "换位"],
    "逻辑三律/概念": ["同一律", "矛盾律", "排中律", "偷换概念", "偷换论题", "概念的外延", "定义", "划分"],
}

NOISE_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^[-=]{4,}$"),
]


def read_text(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return path.read_text(encoding=enc, errors="replace")
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def source_group(path: Path) -> str:
    p = str(path)
    if "full_source_text_cache_20260503" in p:
        return "cross_book_text_cache_20260503_xuanbiyi"
    if "preprocess_v2_2026-05-03/text_cache" in p:
        return "cross_book_text_cache_20260503_xuanbier"
    if "02_extraction/pdf_text" in p:
        return "user_uploaded_framework_pdf_extract"
    if "选必三_逻辑与思维" in p or "codex_连续任务_选必三" in p:
        return "old_xuanbisan_index_only"
    return "local_text"


def source_status(path: Path) -> str:
    name = path.name
    p = str(path)
    if "old_xuanbisan_index_only" == source_group(path):
        return "index_only_not_evidence"
    if re.search(r"细则|评分|评标|阅卷|报告|总结", name) or re.search(r"细则|评分|评标|阅卷|报告|总结", p):
        return "rubric_like_candidate"
    if re.search(r"讲评|pptx|ppt", name, re.I):
        return "lecture_support_candidate"
    if re.search(r"试卷|原卷|教师版", name):
        return "paper_candidate"
    if re.search(r"答案|解析|answer", name, re.I):
        return "answer_candidate"
    return "unclassified_text_candidate"


def source_id_for(path: Path) -> str:
    digest = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:12]
    return f"SRC_SCAN_{digest}"


def collect_files(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for root in paths:
        if not root.exists():
            continue
        if root.is_file() and root.suffix.lower() in {".txt", ".md"}:
            out.append(root)
        elif root.is_dir():
            for suffix in ("*.txt", "*.md"):
                out.extend(root.rglob(suffix))
    return sorted(set(out), key=lambda p: str(p))


def context(lines: list[str], idx: int, radius: int) -> str:
    start = max(0, idx - radius)
    end = min(len(lines), idx + radius + 1)
    snippet = " / ".join(normalize_space(x) for x in lines[start:end] if normalize_space(x))
    return snippet[:900]


def title_hint(lines: list[str]) -> str:
    hints = []
    for line in lines[:80]:
        s = normalize_space(line)
        if not s:
            continue
        if any(rx.search(s) for rx in NOISE_PATTERNS):
            continue
        hints.append(s)
        if len(hints) >= 5:
            break
    return " | ".join(hints)[:500]


def scan_file(path: Path, radius: int) -> list[dict[str, str]]:
    text = read_text(path)
    lines = text.splitlines()
    rows: list[dict[str, str]] = []
    all_terms = []
    for topic, terms in THINKING_TERMS.items():
        for term in terms:
            all_terms.append(("thinking", topic, term))
    for topic, terms in REASONING_TERMS.items():
        for term in terms:
            all_terms.append(("reasoning", topic, term))

    seen = set()
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        for category, topic, term in all_terms:
            if term not in line:
                continue
            key = (i, category, topic, term)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "source_id": source_id_for(path),
                    "source_group": source_group(path),
                    "source_status": source_status(path),
                    "category": category,
                    "topic": topic,
                    "matched_term": term,
                    "line_no": str(i + 1),
                    "file": str(path),
                    "file_name": path.name,
                    "title_hint": title_hint(lines),
                    "hit_line": normalize_space(line)[:500],
                    "context": context(lines, i, radius),
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fields = [
        "source_id",
        "source_group",
        "source_status",
        "category",
        "topic",
        "matched_term",
        "line_no",
        "file_name",
        "title_hint",
        "hit_line",
        "context",
        "file",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_report(path: Path, rows: list[dict[str, str]], category: str) -> None:
    subset = [r for r in rows if r["category"] == category]
    by_topic: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in subset:
        by_topic[row["topic"]].append(row)

    label = "思维部分候选" if category == "thinking" else "推理部分候选"
    lines = [
        f"# {label}扫描报告",
        "",
        "本报告只是候选题定位账。进入正文前，必须回到原试卷、答案表、细则/评标/讲评材料核验。",
        "",
        f"- 候选命中数：{len(subset)}",
        "",
    ]
    for topic in sorted(by_topic):
        items = by_topic[topic]
        lines.append(f"## {topic}（{len(items)} hits）")
        lines.append("")
        for row in items[:40]:
            lines.append(
                f"- `{row['source_status']}` `{row['matched_term']}` "
                f"{row['file_name']}:{row['line_no']}｜{row['hit_line']}"
            )
            lines.append(f"  - context: {row['context']}")
            lines.append(f"  - source_id: `{row['source_id']}` group: `{row['source_group']}`")
        if len(items) > 40:
            lines.append(f"- ... 另有 {len(items) - 40} 条，见 CSV/JSONL。")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--radius", type=int, default=2)
    parser.add_argument("--extra-root", action="append", default=[])
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    default_roots = [
        run_dir / "02_extraction" / "pdf_text",
        Path("/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/02_extraction/full_source_text_cache_20260503"),
        Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/preprocess_v2_2026-05-03/text_cache"),
        Path("/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_框架+三年题链_穷尽版.md"),
        Path("/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_逐题材料-思维路径积累_穷尽版.md"),
        Path("/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_零基础满分课稿.md"),
    ]
    roots = default_roots + [Path(x) for x in args.extra_root]
    files = collect_files(roots)

    rows: list[dict[str, str]] = []
    for file in files:
        rows.extend(scan_file(file, args.radius))

    rows.sort(key=lambda r: (r["category"], r["topic"], r["source_status"], r["file_name"], int(r["line_no"])))

    out_dir = run_dir / "01_source_inventory"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(out_dir / "logic_candidate_hits.csv", rows)
    write_jsonl(out_dir / "logic_candidate_hits.jsonl", rows)
    write_report(out_dir / "thinking_candidate_hits.md", rows, "thinking")
    write_report(out_dir / "reasoning_candidate_hits.md", rows, "reasoning")

    summary = {
        "files_scanned": len(files),
        "hits": len(rows),
        "thinking_hits": sum(1 for r in rows if r["category"] == "thinking"),
        "reasoning_hits": sum(1 for r in rows if r["category"] == "reasoning"),
        "outputs": [
            str(out_dir / "logic_candidate_hits.csv"),
            str(out_dir / "logic_candidate_hits.jsonl"),
            str(out_dir / "thinking_candidate_hits.md"),
            str(out_dir / "reasoning_candidate_hits.md"),
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
