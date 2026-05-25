from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "P1_BATCH20_MATRIX_CANDIDATE_INSPECTION_20260526.md"


def suite_from_heading(heading: str) -> str:
    parts = heading.split()
    return parts[1] if len(parts) > 1 else ""


def main() -> int:
    apply_json = ROOT / "P1_THICKNESS_REPAIR_BATCH20_APPLY_20260526.json"
    applied_rows = json.loads(apply_json.read_text(encoding="utf-8"))["applied"]

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
        "# P1 Batch20 Matrix Candidate Inspection 20260526",
        "",
        "Purpose: rebuild the matrix inspection artifact for the 16 rows actually applied in P1 Batch20.",
        "",
        "- Source: `P1_THICKNESS_REPAIR_BATCH20_APPLY_20260526.json`.",
        "- Boundary: this file documents same-suite matrix context and the formal evidence notes used in the apply artifact.",
        "- Excluded during Batch20: T0257 and T0055 were not applied because inspected support did not meet the same-question philosophy scoring boundary for the candidate answer.",
        "",
    ]
    for idx, row in enumerate(applied_rows, 1):
        suite = suite_from_heading(row["heading"])
        hits = [m for m in matrix_rows if m[source_col] == suite]
        lines.extend(
            [
                f"## {idx}. {row['queue_id']} {row['heading']}",
                "",
                f"- suite: `{suite}`",
                f"- old answer excerpt: {row['old_answer_excerpt']}",
                f"- evidence note used: {row['evidence_note']}",
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
