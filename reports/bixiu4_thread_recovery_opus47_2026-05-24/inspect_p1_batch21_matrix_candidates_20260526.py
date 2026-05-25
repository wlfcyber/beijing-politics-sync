from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "P1_BATCH21_MATRIX_CANDIDATE_INSPECTION_20260526.md"


def suite_from_heading(heading: str) -> str:
    parts = heading.split()
    return parts[1] if len(parts) > 1 else ""


def main() -> int:
    queue_rows: list[dict[str, str]] = []
    with (ROOT / "THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.csv").open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row["priority"] == "P1" and row["question_kind"] == "subjective":
                queue_rows.append(row)
            if len(queue_rows) >= 40:
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
        "# P1 Batch21 Matrix Candidate Inspection 20260526",
        "",
        "Purpose: inspect the first 40 remaining P1 subjective queue rows after Batch20 against the coverage/placement matrix.",
        "",
    ]
    for idx, row in enumerate(queue_rows, 1):
        suite = suite_from_heading(row["heading"])
        hits = [m for m in matrix_rows if m[source_col] == suite]
        lines.extend(
            [
                f"## {idx}. {row['queue_id']} {row['heading']}",
                "",
                f"- suite: `{suite}`",
                f"- answer chars: `{row['answer_chars']}`; why chars: `{row['why_chars']}`; point markers: `{row['answer_point_markers']}`",
                f"- old answer excerpt: {row['answer_excerpt']}",
                f"- matrix rows for suite: `{len(hits)}`",
                "",
                "| matrix row | question | node | evidence level | support excerpt |",
                "|---|---|---|---|---|",
            ]
        )
        for hit in hits[:18]:
            support = hit[support_col].replace("\n", " ")[:180]
            lines.append(
                f"| {hit['matrix_row_id']} | {hit[q_col]} | {hit[node_col]} | {hit[level_col]} | {support} |"
            )
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(str(OUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
