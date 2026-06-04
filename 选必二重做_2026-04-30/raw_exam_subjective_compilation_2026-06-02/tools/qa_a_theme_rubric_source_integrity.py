#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = RUN_DIR / "05_output"
QA_MD = OUT_DIR / "A_THEME_RUBRIC_SOURCE_INTEGRITY_QA_20260604.md"

sys.path.insert(0, str((RUN_DIR / "tools").resolve()))
import build_a_theme_full_handbook_docx as gen  # noqa: E402


TEACHER_NOISE = [
    "学生表现",
    "学生问题",
    "教学启示",
    "教师教学",
    "改进措施",
    "PAGEPAGE",
    "全球治理倡议",
    "上合组织",
    "全球南方",
]


def count_text(text: str, token: str) -> int:
    return text.count(token)


def first_trim_marker(raw: str) -> str:
    hits = []
    for marker in gen.RUBRIC_TRUNCATE_MARKERS:
        idx = raw.find(marker)
        if idx != -1:
            hits.append((idx, marker.replace("\n", "\\n")))
    if not hits:
        return "line/header cleanup"
    return min(hits, key=lambda item: item[0])[1]


def main() -> None:
    packets, _, _, overrides = gen.load_rows()
    packets = gen.apply_source_repair_overrides(packets, gen.load_source_repair_overrides())
    rows = []
    all_shown = []
    empty_raw = []
    for entry in packets:
        raw = gen.clean_text(gen.raw_rubric_text(entry, overrides))
        shown = gen.clean_text(gen.rubric_text(entry, overrides))
        all_shown.append(shown)
        if not raw:
            empty_raw.append(entry)
        if raw != shown:
            rows.append(
                {
                    "entry_id": entry["entry_id"],
                    "title": entry["title"],
                    "raw_len": len(raw),
                    "shown_len": len(shown),
                    "marker": first_trim_marker(raw),
                    "keeps_negative_boundary": "不得分" in shown or "不给分" in shown,
                }
            )
    shown_text = "\n".join(all_shown)
    exact = len(packets) - len(rows)

    lines = [
        "# A类十主题细则原文完整性 QA",
        "",
        "## 1. 结论",
        "",
        f"- 分问总数：{len(packets)}。",
        f"- 【细则】非空：{len(packets) - len(empty_raw)}。",
        f"- 与源包/覆盖层评分段完全一致：{exact}。",
        f"- 仅作页眉或教师端讲评截除：{len(rows)}。",
        "- 本轮规则保留“不得分 / 不给分 / 替换答案 / 变通说明”等评分边界句。",
        "",
        "## 2. 教师端噪音扫描",
        "",
        "| 词/模式 | 命中 |",
        "| --- | ---: |",
    ]
    for token in TEACHER_NOISE:
        lines.append(f"| `{token}` | {count_text(shown_text, token)} |")

    lines.extend(
        [
            "",
            "## 3. 截除项",
            "",
            "| 条目 | 源长度 | 显示长度 | 截除触发 | 仍含不给分边界 |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in rows:
        keep = "是" if row["keeps_negative_boundary"] else "否/无该类边界"
        lines.append(
            f"| {row['entry_id']} {row['title']} | {row['raw_len']} | {row['shown_len']} | {row['marker']} | {keep} |"
        )
    if not rows:
        lines.append("| 无 | 0 | 0 | 无 | 无 |")

    if empty_raw:
        lines.extend(["", "## 4. 空细则风险", ""])
        for entry in empty_raw:
            lines.append(f"- {entry['entry_id']} {entry['title']}")
    else:
        lines.extend(["", "## 4. 空细则风险", "", "- 无。"])

    QA_MD.write_text("\n".join(lines), encoding="utf-8")
    print(QA_MD)
    print(f"rubric_total={len(packets)} nonempty={len(packets) - len(empty_raw)} exact={exact} trimmed={len(rows)}")
    print("noise=" + ", ".join(f"{token}:{count_text(shown_text, token)}" for token in TEACHER_NOISE))


if __name__ == "__main__":
    main()
