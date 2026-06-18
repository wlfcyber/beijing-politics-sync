#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
MAIN_MATRIX = RUN_DIR / "04_module_classification" / "module_classification_matrix.csv"
SUB_MATRIX = RUN_DIR / "04_module_classification" / "subquestion_split_matrix.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "subquestion_integrated_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "SUBQUESTION_INTEGRATED_COVERAGE_MATRIX.csv"
OUT_QUEUE = RUN_DIR / "05_reports" / "subquestion_integrated_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "subquestion_integrated_matrix_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


OUT_FIELDS = [
    "suite_id",
    "year",
    "district",
    "stage",
    "question",
    "parent_question",
    "row_granularity",
    "book_module",
    "question_type",
    "evidence_source",
    "source_types",
    "status",
    "artifact_location",
    "decision_reason",
    "next_action",
    "integration_status",
]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main_to_out(row: dict[str, str], integration_status: str = "main_matrix_original") -> dict[str, str]:
    return {
        "suite_id": row["suite_id"],
        "year": row["year"],
        "district": row["district"],
        "stage": row["stage"],
        "question": row["question"],
        "parent_question": "",
        "row_granularity": "suite" if row["question"] == "SUITE_BLOCKER" else "question",
        "book_module": row["book_module"],
        "question_type": row["question_type"],
        "evidence_source": row["evidence_source"],
        "source_types": row["source_types"],
        "status": row["status"],
        "artifact_location": row["artifact_location"],
        "decision_reason": row["decision_reason"],
        "next_action": row["next_action"],
        "integration_status": integration_status,
    }


def sub_to_out(row: dict[str, str]) -> dict[str, str]:
    question_type = "subjective" if row["parent_question"].isdigit() and int(row["parent_question"]) >= 16 else "objective"
    if row["status"] == "included" and row["book_module"] in TARGET_MODULES:
        integration_status = "subquestion_integrated_target"
    elif row["status"] == "module-boundary-excluded":
        integration_status = "subquestion_integrated_boundary"
    else:
        integration_status = "subquestion_integrated_blocked"
    return {
        "suite_id": row["suite_id"],
        "year": row["year"],
        "district": row["district"],
        "stage": row["stage"],
        "question": row["subquestion"],
        "parent_question": row["parent_question"],
        "row_granularity": "subquestion",
        "book_module": row["book_module"],
        "question_type": question_type,
        "evidence_source": row["source_path"],
        "source_types": row["source_type"],
        "status": row["status"],
        "artifact_location": "04_module_classification/subquestion_split_matrix.csv",
        "decision_reason": row["decision_reason"],
        "next_action": row["next_action"],
        "integration_status": integration_status,
    }


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    main_rows = load_csv(MAIN_MATRIX)
    sub_rows = load_csv(SUB_MATRIX)
    replaced_parent_keys = {(row["suite_id"], row["parent_question"]) for row in sub_rows}

    out_rows: list[dict[str, str]] = []
    replaced_parent_rows: list[dict[str, str]] = []
    for row in main_rows:
        key = (row["suite_id"], row["question"])
        if key in replaced_parent_keys and row["status"] == "blocked":
            replaced_parent_rows.append(row)
            continue
        out_rows.append(main_to_out(row))

    out_rows.extend(sub_to_out(row) for row in sub_rows)
    out_rows.sort(
        key=lambda row: (
            row["year"],
            row["district"],
            row["stage"],
            row["suite_id"],
            row["parent_question"] or row["question"],
            row["question"],
        )
    )

    blocked_rows = [row for row in out_rows if row["status"] == "blocked"]
    write_csv(OUT_MATRIX, out_rows, OUT_FIELDS)
    write_csv(OUT_COVERAGE, out_rows, OUT_FIELDS)
    write_csv(OUT_QUEUE, blocked_rows, OUT_FIELDS)

    status_counts = Counter(row["status"] for row in out_rows)
    module_counts = Counter(row["book_module"] for row in out_rows)
    integration_counts = Counter(row["integration_status"] for row in out_rows)
    target_counts = Counter(
        row["book_module"]
        for row in out_rows
        if row["status"] == "included" and row["book_module"] in TARGET_MODULES
    )
    blocked_granularity = Counter(row["row_granularity"] for row in blocked_rows)

    lines = [
        "# Subquestion Integrated Matrix Report",
        "",
        "- purpose: Formal handoff matrix that preserves the original question matrix while replacing source-confirmed split parents with subquestion rows.",
        f"- main_matrix_rows: {len(main_rows)}",
        f"- replaced_blocked_parent_rows: {len(replaced_parent_rows)}",
        f"- integrated_subquestion_rows: {len(sub_rows)}",
        f"- output_rows: {len(out_rows)}",
        f"- blocked_rows_after_integration: {len(blocked_rows)}",
        f"- output_matrix: `{OUT_MATRIX}`",
        f"- output_coverage: `{OUT_COVERAGE}`",
        f"- blocked_queue: `{OUT_QUEUE}`",
        "",
        "## Status Counts",
        "",
    ]
    for key, value in status_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Target Included Counts", ""])
    for key, value in target_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Module Counts", ""])
    for key, value in module_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Integration Counts", ""])
    for key, value in integration_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Blocked Granularity", ""])
    for key, value in blocked_granularity.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- This matrix is safer for future B2/B3/B4_CULTURE intake than the parent-only matrix because it no longer treats resolved multi-module parent questions as single unknown rows.",
            "- It is still not final coverage: blocked rows remain, question-gap review remains, and source confirmation is still required for unresolved rows.",
        ]
    )
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(OUT_MATRIX)
    print(OUT_COVERAGE)
    print(OUT_QUEUE)
    print(OUT_REPORT)
    print(f"output_rows={len(out_rows)} blocked_rows={len(blocked_rows)} replaced_parents={len(replaced_parent_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
