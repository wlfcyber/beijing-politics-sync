#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
MATRIX = RUN_DIR / "04_module_classification" / "module_classification_matrix.csv"
CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
OUT_DIR = RUN_DIR / "05_reports"


def load_best_snippets() -> dict[tuple[str, str], dict[str, str]]:
    rows_by_key: dict[tuple[str, str], list[dict[str, str]]] = {}
    with CANDIDATES.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            rows_by_key.setdefault((row["suite_id"], row["question"]), []).append(row)

    best: dict[tuple[str, str], dict[str, str]] = {}
    for key, rows in rows_by_key.items():
        paper_rows = [row for row in rows if row["source_type"] == "paper"]
        selected = paper_rows[0] if paper_rows else rows[0]
        best[key] = selected
    return best


def parse_reason(value: str) -> dict[str, object]:
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        return {}


def main() -> int:
    snippets = load_best_snippets()
    with MATRIX.open("r", encoding="utf-8", newline="") as f:
        matrix_rows = list(csv.DictReader(f))

    blocked_rows = [row for row in matrix_rows if row["status"] == "blocked"]
    out_fields = [
        "suite_id",
        "year",
        "district",
        "stage",
        "question",
        "question_type",
        "target",
        "target_score",
        "boundary",
        "boundary_score",
        "override",
        "book_module",
        "status",
        "next_action",
        "evidence_source",
        "candidate_source_type",
        "candidate_file_path",
        "snippet",
        "decision_reason",
    ]
    queue_path = OUT_DIR / "blocked_manual_review_queue.csv"
    split_path = OUT_DIR / "manual_subquestion_split_queue.csv"

    queue_rows = []
    split_rows = []
    for row in blocked_rows:
        reason = parse_reason(row["decision_reason"])
        candidate = snippets.get((row["suite_id"], row["question"]), {})
        out = {
            "suite_id": row["suite_id"],
            "year": row["year"],
            "district": row["district"],
            "stage": row["stage"],
            "question": row["question"],
            "question_type": row["question_type"],
            "target": str(reason.get("target", "")),
            "target_score": str(reason.get("target_score", "")),
            "boundary": str(reason.get("boundary", "")),
            "boundary_score": str(reason.get("boundary_score", "")),
            "override": str(reason.get("override", "")),
            "book_module": row["book_module"],
            "status": row["status"],
            "next_action": row["next_action"],
            "evidence_source": row["evidence_source"],
            "candidate_source_type": candidate.get("source_type", ""),
            "candidate_file_path": candidate.get("file_path", ""),
            "snippet": candidate.get("snippet", ""),
            "decision_reason": row["decision_reason"],
        }
        queue_rows.append(out)
        if out["override"] == "manual_subquestion_split_needed":
            split_rows.append(out)

    with queue_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(queue_rows)
    with split_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(split_rows)

    status_counts = Counter(row["status"] for row in matrix_rows)
    module_counts = Counter(row["book_module"] for row in matrix_rows)
    next_counts = Counter(row["next_action"] for row in blocked_rows)
    override_counts = Counter(row["override"] for row in queue_rows)

    summary = [
        "# Blocked Review Summary",
        "",
        f"- blocked_rows: {len(blocked_rows)}",
        f"- manual_subquestion_split_rows: {len(split_rows)}",
        f"- review_queue: `{queue_path}`",
        f"- split_queue: `{split_path}`",
        "",
        "## Status Counts",
        "",
    ]
    for key, value in status_counts.most_common():
        summary.append(f"- {key}: {value}")
    summary.extend(["", "## Module Counts", ""])
    for key, value in module_counts.most_common():
        summary.append(f"- {key}: {value}")
    summary.extend(["", "## Blocked Next Actions", ""])
    for key, value in next_counts.most_common():
        summary.append(f"- {key}: {value}")
    summary.extend(["", "## Blocked Overrides", ""])
    for key, value in override_counts.most_common():
        label = key or "none"
        summary.append(f"- {label}: {value}")

    summary_path = OUT_DIR / "blocked_review_summary.md"
    summary_path.write_text("\n".join(summary) + "\n", encoding="utf-8")

    print(queue_path)
    print(split_path)
    print(summary_path)
    print(f"blocked_rows={len(blocked_rows)} split_rows={len(split_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
