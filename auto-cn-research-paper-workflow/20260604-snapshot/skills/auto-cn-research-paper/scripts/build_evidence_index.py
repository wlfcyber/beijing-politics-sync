#!/usr/bin/env python3
"""Build a page-level evidence index from extracted full-text files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_TERMS = [
    "数字形式主义",
    "形式主义",
    "正确政绩观",
    "基层治理",
    "乡村治理",
    "基层减负",
    "数字负担",
    "痕迹",
    "考核",
    "平台",
    "算法",
    "堕距",
    "理念",
    "制度",
    "技术",
    "治理路径",
    "技术治理",
    "问责机制",
    "自由裁量权",
    "乡镇干部",
    "乡镇干部行动",
    "程序性行动",
    "避责",
    "数字循环",
    "数字隔离",
    "数字行政",
    "公共价值空间",
    "数字素养",
    "结果运用虚置化",
    "短效数据增长",
    "选择性行动",
    "重复性开发",
    "替代性服务",
    "碎片化协作",
    "悬浮化",
    "智能码",
    "数字平台",
    "数据悬浮",
    "规则悬浮",
    "知识悬浮",
    "运行悬浮",
    "治理情境",
    "一网统管",
    "结构嵌合",
    "关系重塑",
    "数字悬浮",
    "政民互动",
    "技术嵌入",
    "注意力竞争",
    "数字创造",
    "主动型生产",
    "低价值生产",
    "Cultural Lag",
    "cultural lag",
    "bureaucratic",
    "Bureaucratic",
    "rules",
    "discipline",
    "decision-making",
    "Decision-Making",
    "administrative",
    "Administrative",
]


PAGE_RE = re.compile(r"(?:===== PAGE\s+(\d+)\s+=====|---\s*page\s+(\d+)\s*---)", re.IGNORECASE)


def split_pages(text: str) -> list[tuple[int, str]]:
    matches = list(PAGE_RE.finditer(text))
    if not matches:
        return [(1, text)]
    pages: list[tuple[int, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        page_no = match.group(1) or match.group(2)
        pages.append((int(page_no), text[start:end]))
    return pages


def snippet(page_text: str, term: str, width: int = 42) -> str:
    compact = re.sub(r"\s+", "", page_text)
    pos = compact.lower().find(term.lower())
    if pos < 0:
        return ""
    start = max(pos - width, 0)
    end = min(pos + len(term) + width, len(compact))
    return compact[start:end]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text-dir", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--pattern", default="*.txt")
    parser.add_argument("--terms", help="Comma-separated terms. Defaults to core workflow terms.")
    parser.add_argument("--max-pages-per-term", type=int, default=5)
    args = parser.parse_args()

    text_dir = Path(args.text_dir).expanduser().resolve()
    terms = [t.strip() for t in (args.terms.split(",") if args.terms else DEFAULT_TERMS) if t.strip()]

    lines = [
        "# Evidence Index",
        "",
        "This index is generated from extracted full text. It supports page/location checks; it is not a substitute for final manual citation polishing.",
        "",
        "| Source text | Pages | Characters | Top evidence locations |",
        "| --- | --- | --- | --- |",
    ]

    detail_lines: list[str] = ["", "## Term Locations", ""]
    source_count = 0
    for path in sorted(text_dir.glob(args.pattern), key=lambda p: p.name):
        text = path.read_text(encoding="utf-8", errors="ignore")
        pages = split_pages(text)
        source_count += 1
        locations: list[str] = []
        detail_lines.append(f"### {path.name}")
        detail_lines.append("")
        detail_lines.append("| Term | Pages | Example context |")
        detail_lines.append("| --- | --- | --- |")
        for term in terms:
            hits: list[tuple[int, str]] = []
            for page_no, page_text in pages:
                if term.lower() in page_text.lower():
                    hits.append((page_no, snippet(page_text, term)))
            if not hits:
                continue
            page_list = [str(page) for page, _ in hits[: args.max_pages_per_term]]
            context = hits[0][1].replace("|", "/")
            detail_lines.append(f"| {term} | {', '.join(page_list)} | {context} |")
            if len(locations) < 5:
                locations.append(f"{term}: p.{page_list[0]}")
        detail_lines.append("")
        lines.append(
            f"| `{path}` | {len(pages)} | {len(text)} | {'; '.join(locations)} |"
        )

    lines.append("")
    lines.append(f"- source_count: {source_count}")
    output = "\n".join(lines + detail_lines)
    Path(args.out).expanduser().resolve().write_text(output, encoding="utf-8")
    print(f"source_count={source_count}")
    print(f"out={Path(args.out).expanduser().resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
