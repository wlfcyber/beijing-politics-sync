#!/usr/bin/env python3
"""Audit whether the topic engine produced a usable topic-selection matrix."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_COLUMN_ALIASES: dict[str, tuple[str, ...]] = {
    "编号": ("编号",),
    "候选题目": ("候选题目", "题目"),
    "研究对象": ("研究对象", "对象"),
    "方法": ("方法", "研究方法"),
    "文献可得": ("文献可得", "文献可得性", "文献可得度"),
    "材料可得": ("材料可得", "材料可得性", "材料可得度"),
    "对象清晰": ("对象清晰", "对象清晰度"),
    "方法可行": ("方法可行", "方法可行性"),
    "原创风险": ("原创风险", "创新风险"),
    "贡献限度": ("贡献限度", "贡献谦抑", "贡献适度", "贡献边界"),
    "完成风险": ("完成风险", "完成度风险"),
    "总分": ("总分", "合计"),
    "结论": ("结论", "选择", "处理"),
}

SCORE_COLUMNS = (
    "文献可得",
    "材料可得",
    "对象清晰",
    "方法可行",
    "原创风险",
    "贡献限度",
    "完成风险",
    "总分",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def parse_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    tables: list[tuple[list[str], list[list[str]]]] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines) - 1:
        line = lines[index].strip()
        next_line = lines[index + 1].strip()
        if line.startswith("|") and next_line.startswith("|"):
            header = split_markdown_row(line)
            separator = split_markdown_row(next_line)
            if is_separator_row(separator) and len(header) == len(separator):
                rows: list[list[str]] = []
                index += 2
                while index < len(lines) and lines[index].strip().startswith("|"):
                    cells = split_markdown_row(lines[index])
                    if len(cells) == len(header) and not is_separator_row(cells):
                        rows.append(cells)
                    index += 1
                tables.append((header, rows))
                continue
        index += 1
    return tables


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text).strip()


def find_column(header: list[str], logical_name: str) -> int | None:
    aliases = REQUIRED_COLUMN_ALIASES[logical_name]
    normalized_header = [normalize(cell) for cell in header]
    for alias in aliases:
        normalized_alias = normalize(alias)
        for index, cell in enumerate(normalized_header):
            if normalized_alias == cell or normalized_alias in cell:
                return index
    return None


def choose_topic_table(tables: list[tuple[list[str], list[list[str]]]]) -> tuple[list[str], list[list[str]]] | None:
    for header, rows in tables:
        if find_column(header, "编号") is not None and find_column(header, "候选题目") is not None:
            return header, rows
    return None


def is_candidate_row(row: list[str], id_index: int) -> bool:
    return bool(re.fullmatch(r"T\d{1,3}", normalize(row[id_index]), flags=re.IGNORECASE))


def has_number(value: str) -> bool:
    return bool(re.search(r"-?\d+(?:\.\d+)?", value))


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    topic_path = run_dir / "01_选题评分表.md"
    text = read(topic_path)
    issues: list[str] = []

    if not text:
        issues.append("missing topic matrix: 01_选题评分表.md")
        print("status=INCOMPLETE")
        print("candidate_count=0")
        print("main_selection_count=0")
        print("backup_count=0")
        print("numeric_score_ready=no")
        for issue in issues:
            print(f"- {issue}")
        return 1

    table = choose_topic_table(parse_tables(text))
    if table is None:
        issues.append("missing markdown topic table with 编号 and 候选题目 columns")
        print("status=INCOMPLETE")
        print("candidate_count=0")
        print("main_selection_count=0")
        print("backup_count=0")
        print("numeric_score_ready=no")
        for issue in issues:
            print(f"- {issue}")
        return 1

    header, rows = table
    column_indexes: dict[str, int] = {}
    for required in REQUIRED_COLUMN_ALIASES:
        index = find_column(header, required)
        if index is None:
            issues.append(f"missing required column: {required}")
        else:
            column_indexes[required] = index

    id_index = column_indexes.get("编号", 0)
    candidate_rows = [row for row in rows if len(row) > id_index and is_candidate_row(row, id_index)]
    candidate_count = len(candidate_rows)
    if candidate_count < 20 or candidate_count > 30:
        issues.append(f"candidate_count must be between 20 and 30: {candidate_count}")

    conclusion_index = column_indexes.get("结论")
    main_selection_count = 0
    backup_count = 0
    if conclusion_index is None:
        issues.append("cannot count main/backup selections without 结论 column")
    else:
        for row in candidate_rows:
            conclusion = normalize(row[conclusion_index])
            if "主选" in conclusion:
                main_selection_count += 1
            if "备选" in conclusion:
                backup_count += 1
        if main_selection_count != 1:
            issues.append(f"main_selection_count must be exactly 1: {main_selection_count}")
        if backup_count != 3:
            issues.append(f"backup_count must be exactly 3: {backup_count}")

    numeric_score_ready = True
    for logical_name in SCORE_COLUMNS:
        index = column_indexes.get(logical_name)
        if index is None:
            numeric_score_ready = False
            continue
        for row in candidate_rows:
            source_id = row[id_index] if id_index < len(row) else "unknown"
            value = row[index] if index < len(row) else ""
            if not has_number(value):
                numeric_score_ready = False
                issues.append(f"missing numeric score: {source_id} / {logical_name}")

    status = "PASS" if not issues else "INCOMPLETE"
    print(f"status={status}")
    print(f"candidate_count={candidate_count}")
    print(f"main_selection_count={main_selection_count}")
    print(f"backup_count={backup_count}")
    print(f"numeric_score_ready={'yes' if numeric_score_ready else 'no'}")
    print("columns=" + ", ".join(header))
    for issue in issues:
        print(f"- {issue}")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
