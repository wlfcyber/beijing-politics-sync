from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "P1_BATCH22_MATRIX_CANDIDATE_INSPECTION_20260526.md"


def suite_from_heading(heading: str) -> str:
    parts = heading.split()
    return parts[1] if len(parts) > 1 else ""


def question_from_heading(heading: str) -> str:
    match = re.search(r"第(\d+)题", heading)
    return f"Q{match.group(1)}" if match else ""


def is_formal_body_support(level: str, support: str) -> bool:
    bad = ["客观", "模块边界", "答案键", "题面正确项；非主观", "非必修四评分细则"]
    if any(token in level for token in bad):
        return False
    strong = [
        "正式",
        "评分",
        "细则",
        "阅卷",
        "评标",
        "评卷",
        "PPT",
        "原图",
        "报告",
        "标准",
    ]
    joined = level + " " + support
    return any(token in joined for token in strong)


def main() -> int:
    queue_rows: list[dict[str, str]] = []
    with (ROOT / "THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.csv").open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row["priority"] == "P1" and row["question_kind"] == "subjective":
                queue_rows.append(row)
            if len(queue_rows) >= 80:
                break

    with (ROOT / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        source_col = fieldnames[2]
        q_col = fieldnames[5]
        node_col = fieldnames[8]
        support_col = fieldnames[9]
        level_col = fieldnames[10]
        matrix_rows = list(reader)

    lines = [
        "# P1 Batch22 Matrix Candidate Inspection 20260526",
        "",
        "Purpose: inspect the first 80 current P1 subjective queue rows after Batch21 against same-suite and same-question matrix support.",
        "",
    ]
    for idx, row in enumerate(queue_rows, 1):
        suite = suite_from_heading(row["heading"])
        qno = question_from_heading(row["heading"])
        same_suite = [m for m in matrix_rows if m[source_col] == suite]
        same_question = [m for m in same_suite if m[q_col] == qno]
        formal_same_question = [
            m for m in same_question if is_formal_body_support(m[level_col], m[support_col])
        ]
        lines.extend(
            [
                f"## {idx}. {row['queue_id']} {row['heading']}",
                "",
                f"- suite: `{suite}`",
                f"- question: `{qno}`",
                f"- answer chars: `{row['answer_chars']}`; why chars: `{row['why_chars']}`; point markers: `{row['answer_point_markers']}`",
                f"- old answer excerpt: {row['answer_excerpt']}",
                f"- same-suite matrix rows: `{len(same_suite)}`",
                f"- same-question matrix rows: `{len(same_question)}`",
                f"- formal same-question support rows: `{len(formal_same_question)}`",
                "",
                "| matrix row | node | evidence level | support excerpt |",
                "|---|---|---|---|",
            ]
        )
        hits = formal_same_question or same_question[:12]
        for hit in hits[:16]:
            support = hit[support_col].replace("\n", " ")[:220]
            lines.append(
                f"| {hit['matrix_row_id']} | {hit[node_col]} | {hit[level_col]} | {support} |"
            )
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(str(OUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
