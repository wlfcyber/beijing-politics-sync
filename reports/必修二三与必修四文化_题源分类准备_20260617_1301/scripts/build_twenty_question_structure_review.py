#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "auxiliary_clue_repaired_classification_matrix.csv"
REPAIR = RUN_DIR / "05_reports" / "question_gap_repair_candidates.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
GAP_BEFORE = RUN_DIR / "05_reports" / "question_gap_after_auxiliary_clue_review.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "twenty_question_structure_accepted_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv"
OUT_REVIEW = RUN_DIR / "05_reports" / "twenty_question_structure_review.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "twenty_question_structure_acceptance_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "twenty_question_structure_accepted_blocked_queue.csv"
OUT_GAP_AFTER = RUN_DIR / "05_reports" / "question_gap_after_twenty_question_structure_review.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "twenty_question_structure_acceptance_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 900) -> str:
    return re.sub(r"\s+", " ", text).strip()[:limit]


def question_base(question: str) -> str:
    match = re.match(r"(\d+)", question or "")
    return match.group(1) if match else question


def split_missing(text: str) -> list[str]:
    return [item for item in re.split(r"[;\s]+", text or "") if item]


def top_level_q21_hits(text: str) -> list[str]:
    patterns = [
        re.compile(r"(?m)^\s*21\s*[\.．、]\s*.{0,120}"),
        re.compile(r"(?m)^\s*21\s*[（(]\s*\d+\s*分\s*[)）]?.{0,120}"),
        re.compile(r"(?m)^\s*第\s*21\s*题\s*.{0,120}"),
        re.compile(r"(?m)^\s*二十一\s*[\.．、]\s*.{0,120}"),
    ]
    hits: list[str] = []
    for pattern in patterns:
        for match in pattern.finditer(text):
            hits.append(compact(match.group(0), 160))
    return hits


def main() -> int:
    matrix_rows = load_csv(IN_MATRIX)
    matrix_fields = list(matrix_rows[0].keys())
    target_candidates = [
        row
        for row in load_csv(REPAIR)
        if row["recommended_action"] == "accept_20_question_structure_after_source_spotcheck"
    ]
    candidate_rows = load_csv(QUESTION_CANDIDATES)
    by_suite: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in candidate_rows:
        by_suite[row["suite_id"]].append(row)

    review_fields = [
        "suite_id",
        "missing_question",
        "review_result",
        "paper_or_ocr_q20_seen",
        "candidate_q21_rows",
        "top_level_q21_text_hits",
        "evidence_source_types",
        "evidence_text_paths",
        "q20_evidence_text",
        "decision_note",
    ]
    audit_fields = [
        "suite_id",
        "missing_question",
        "accepted_as_actual_20_question_structure",
        "evidence_basis",
        "q20_evidence_text",
    ]

    review_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    accepted: set[tuple[str, str]] = set()

    for repair in target_candidates:
        suite_id = repair["suite_id"]
        missing_question = repair["missing_question"]
        suite_candidates = by_suite[suite_id]
        q21_rows = [
            row
            for row in suite_candidates
            if question_base(row["question"]) == missing_question
        ]
        q20_rows = [
            row
            for row in suite_candidates
            if question_base(row["question"]) == "20"
        ]
        paper_or_ocr_q20 = [
            row
            for row in q20_rows
            if row["source_type"] in {"paper", "ocr-cache"}
        ]
        chosen_q20 = (paper_or_ocr_q20 or q20_rows or [{}])[0]
        text_paths = sorted(
            {
                row["run_text_path"]
                for row in suite_candidates
                if row.get("run_text_path")
                and Path(row["run_text_path"]).exists()
                and row["source_type"] in {"paper", "ocr-cache", "reference-answer", "rubric"}
            }
        )
        q21_hits: list[str] = []
        for path in text_paths:
            text = Path(path).read_text(encoding="utf-8", errors="ignore")
            q21_hits.extend([f"{path}: {hit}" for hit in top_level_q21_hits(text)])

        can_accept = (
            missing_question == "21"
            and bool(paper_or_ocr_q20)
            and not q21_rows
            and not q21_hits
        )
        review_result = (
            "accepted_actual_20_question_structure"
            if can_accept
            else "keep_gap_open_needs_manual_source_check"
        )
        decision_note = (
            "Paper/OCR evidence reaches Q20 and no candidate or line-start source-text hit supports top-level Q21."
            if can_accept
            else "Insufficient evidence to accept actual 20-question structure."
        )
        review_rows.append(
            {
                "suite_id": suite_id,
                "missing_question": missing_question,
                "review_result": review_result,
                "paper_or_ocr_q20_seen": "yes" if paper_or_ocr_q20 else "no",
                "candidate_q21_rows": str(len(q21_rows)),
                "top_level_q21_text_hits": " | ".join(q21_hits),
                "evidence_source_types": ";".join(
                    sorted({row["source_type"] for row in suite_candidates if row["question"] in {"19", "20"}})
                ),
                "evidence_text_paths": ";".join(text_paths),
                "q20_evidence_text": compact(chosen_q20.get("snippet", ""), 1000),
                "decision_note": decision_note,
            }
        )
        if can_accept:
            accepted.add((suite_id, missing_question))
            audit_rows.append(
                {
                    "suite_id": suite_id,
                    "missing_question": missing_question,
                    "accepted_as_actual_20_question_structure": "yes",
                    "evidence_basis": "paper_or_ocr_q20_seen;no_candidate_q21;no_line_start_q21_text_hit",
                    "q20_evidence_text": compact(chosen_q20.get("snippet", ""), 1000),
                }
            )

    gap_after_rows = []
    prior_remaining = 0
    remaining = 0
    for row in load_csv(GAP_BEFORE):
        before = split_missing(row.get("missing_after_auxiliary_clue_review", ""))
        prior_remaining += len(before)
        resolved = [q for q in before if (row["suite_id"], q) in accepted]
        after = [q for q in before if (row["suite_id"], q) not in accepted]
        remaining += len(after)
        gap_after_rows.append(
            {
                "suite_id": row["suite_id"],
                "missing_after_twenty_question_structure_review": ";".join(after),
                "resolved_by_auxiliary_clue_review": row.get("resolved_by_auxiliary_clue_review", ""),
                "resolved_by_twenty_question_structure_review": ";".join(resolved),
            }
        )

    write_csv(OUT_MATRIX, matrix_rows, matrix_fields)
    write_csv(OUT_COVERAGE, matrix_rows, matrix_fields)
    write_csv(OUT_REVIEW, review_rows, review_fields)
    write_csv(OUT_AUDIT, audit_rows, audit_fields)
    write_csv(OUT_BLOCKED, [row for row in matrix_rows if row["status"] == "blocked"], matrix_fields)
    write_csv(
        OUT_GAP_AFTER,
        gap_after_rows,
        [
            "suite_id",
            "missing_after_twenty_question_structure_review",
            "resolved_by_auxiliary_clue_review",
            "resolved_by_twenty_question_structure_review",
        ],
    )

    status_counts = Counter(row["status"] for row in matrix_rows)
    target_counts = Counter(
        row["book_module"] for row in matrix_rows if row["status"] == "included"
    )
    duplicate_keys = len(matrix_rows) - len(
        {(row["suite_id"], row["question"]) for row in matrix_rows}
    )
    blocked_count = sum(1 for row in matrix_rows if row["status"] == "blocked")

    report = f"""# Twenty-Question Structure Acceptance Report

Generated from `{IN_MATRIX.name}`.

## Scope

- Reviewed likely actual 20-question structures: {len(target_candidates)}
- Accepted as actual 20-question papers: {len(accepted)}
- Kept open: {len(target_candidates) - len(accepted)}
- Matrix rows added: 0

## Matrix Counts

- Rows: {len(matrix_rows)}
- Status counts: {dict(status_counts)}
- Included target counts: {dict(target_counts)}
- Blocked rows: {blocked_count}
- Duplicate `(suite_id, question)` keys: {duplicate_keys}

## Gap Counts

- Missing-question entries before this review: {prior_remaining}
- Resolved by this review: {len(accepted)}
- Remaining missing-question entries: {remaining}

## Acceptance Rule

A `21` gap was accepted as an actual 20-question structure only when paper/OCR candidates reached Q20, no question-candidate row had top-level Q21, and source text search found no line-start top-level Q21 marker.

## Deliverables

- `{OUT_REVIEW.relative_to(RUN_DIR)}`
- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_GAP_AFTER.relative_to(RUN_DIR)}`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
