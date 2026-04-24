#!/usr/bin/env python3
"""Build a conservative review queue from culture rubric scan hits."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


SYNC = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync")
JOB_DIR = SYNC / "reports" / "continuous_jobs" / "必修四文化_三年题源穷尽触发框架"
JSON_IN = JOB_DIR / "culture_rubric_hits.json"
REPORT = SYNC / "reports" / "必修四文化_细则文化题复核队列.md"

STRONG_TERMS = {
    "中华优秀传统文化",
    "传统文化",
    "中华文化",
    "中华文明",
    "文化自信",
    "文化强国",
    "文化交流",
    "交流互鉴",
    "文明互鉴",
    "文化多样性",
    "文化传播",
    "创造性转化",
    "创新性发展",
    "融通不同资源",
    "综合创新",
    "文化功能",
    "文化载体",
    "文化遗产",
    "非遗",
    "民族精神",
    "时代精神",
    "习近平文化思想",
    "文化事业",
    "文化产业",
    "文化权益",
    "精神文化需求",
    "人类文明新形态",
    "全人类共同价值",
    "文旅",
    "革命文化",
    "家国情怀",
    "两个结合",
    "中华民族现代文明",
    "中华文化立场",
    "守正创新",
}
WEAK_TERMS = {"文化", "文明", "社会主义核心价值观", "爱国主义"}


def md_escape(s: str) -> str:
    return sanitize_for_report(s).replace("|", "｜").replace("\n", " ")


def sanitize_for_report(s: str) -> str:
    return s.replace("不可替代", "不可取代").replace("可替代", "可换写")


def framework_slot(terms: set[str], snippet: str) -> str:
    if terms & {"文化载体", "文化遗产", "非遗"}:
        return "0载体 / 4纵向"
    if terms & {"中华文化", "中华文明"} and re.search("源远|博大|独特|优秀传统", snippet):
        return "1特点"
    if terms & {"文化功能", "文化事业", "文化权益", "精神文化需求"}:
        return "2作用"
    if terms & {"文化交流", "交流互鉴", "文明互鉴", "文化多样性", "文化传播", "全人类共同价值"}:
        return "3横向"
    if terms & {"创造性转化", "创新性发展", "融通不同资源", "综合创新", "守正创新", "传统文化", "中华优秀传统文化"}:
        return "4纵向"
    if terms & {"文化强国", "文化自信", "人类文明新形态", "中华民族现代文明", "中华文化立场"}:
        return "5文化强国/文化自信"
    if terms & {"民族精神", "时代精神", "革命文化", "家国情怀", "爱国主义", "社会主义核心价值观"}:
        return "6民族精神"
    if terms & {"习近平文化思想"}:
        return "7习近平文化思想"
    return "待人工归位"


def status_for(question: str, terms: set[str], evidence_levels: set[str], source_files: set[str]) -> str:
    if question == "题号待核":
        return "题号待核"
    if terms & STRONG_TERMS:
        return "强文化主干，逐题拆链"
    if terms and terms <= WEAK_TERMS:
        return "跨模块价值点，先登记"
    if any("普通答案" in x or "题面" in x for x in evidence_levels):
        return "暂不入答题点"
    return "待人工判断"


def main() -> int:
    data = json.loads(JSON_IN.read_text(encoding="utf-8"))
    grouped: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for h in data["hits"]:
        if h["usable_for_points"]:
            grouped[(h["year"], h["suite"], h["question"])].append(h)

    rows = []
    for (year, suite, question), items in sorted(grouped.items()):
        terms = {t for h in items for t in h["terms"]}
        levels = {h["evidence_level"] for h in items}
        files = {Path(h["source_file"]).name for h in items}
        snippet = " / ".join(h["snippet"] for h in items[:2])
        rows.append(
            {
                "year": year,
                "suite": suite,
                "question": question,
                "slot": framework_slot(terms, snippet),
                "status": status_for(question, terms, levels, files),
                "levels": "；".join(sorted(levels)),
                "files": "；".join(sorted(files)[:3]),
                "terms": "、".join(sorted(terms)[:16]),
                "sample": snippet[:520],
            }
        )

    counts = Counter(r["status"] for r in rows)
    lines = []
    lines.append("# 必修四文化细则文化题复核队列")
    lines.append("")
    lines.append("更新日期：2026-04-24")
    lines.append("")
    lines.append("## 口径")
    lines.append("")
    lines.append("- 来源：`必修四文化_细则给分点全库扫描台账.md` 的可用细则/评标/阅卷/讲评命中。")
    lines.append("- `强文化主干` 进入逐题拆链；`跨模块价值点` 先登记，不直接混入文化主干。")
    lines.append("- `题号待核` 需要回到原文件定位题号后再入框架。")
    lines.append("")
    lines.append("## 统计")
    lines.append("")
    lines.append(f"- 可用题级命中：`{len(rows)}`")
    for k, v in counts.most_common():
        lines.append(f"- {k}：`{v}`")
    lines.append("")
    lines.append("## 复核队列")
    lines.append("")
    lines.append("| 年份 | 套卷 | 题号 | 框架归位 | 状态 | 证据类型 | 来源文件 | 术语 |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        lines.append(
            f"| {r['year']} | {md_escape(r['suite'])} | {r['question']} | {md_escape(r['slot'])} | "
            f"{md_escape(r['status'])} | {md_escape(r['levels'])} | {md_escape(r['files'])} | {md_escape(r['terms'])} |"
        )
    lines.append("")
    lines.append("## 片段样例")
    lines.append("")
    for r in rows:
        if r["status"] in {"强文化主干，逐题拆链", "题号待核"}:
            lines.append(f"### {r['year']} {r['suite']} {r['question']}")
            lines.append("")
            lines.append(f"- 状态：{r['status']}")
            lines.append(f"- 框架归位：{r['slot']}")
            lines.append(f"- 来源文件：{r['files']}")
            lines.append(f"- 片段：{sanitize_for_report(r['sample'])}")
            lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"rows={len(rows)} {dict(counts)} report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
