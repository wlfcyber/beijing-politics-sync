#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
GAP_REVIEW = RUN_DIR / "05_reports" / "question_gap_review.csv"
CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
MATRIX = RUN_DIR / "04_module_classification" / "prompt_resolved_classification_matrix.csv"
OUT_CSV = RUN_DIR / "05_reports" / "question_gap_triage.csv"
OUT_MD = RUN_DIR / "05_reports" / "question_gap_triage.md"

PRIMARY_SOURCE_TYPES = {"paper", "ocr-cache", "reference-answer"}
AUX_SOURCE_TYPES = {"rubric", "marking-report", "lecture"}


def qsort(values: set[str]) -> list[str]:
    return sorted(values, key=lambda value: int(value) if value.isdigit() else 999)


def load_candidates() -> dict[str, dict[str, set[str]]]:
    by_suite: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    with CANDIDATES.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if not row["question"].isdigit():
                continue
            by_suite[row["suite_id"]][row["source_type"]].add(row["question"])
    return by_suite


def load_matrix_questions() -> dict[str, set[str]]:
    by_suite: dict[str, set[str]] = defaultdict(set)
    with MATRIX.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            question = row.get("parent_question") or row["question"]
            if question.isdigit():
                by_suite[row["suite_id"]].add(question)
    return by_suite


def classify_gap(missing: list[str], primary_qs: set[str], aux_qs: set[str]) -> tuple[str, str]:
    if missing == ["21"] and not {"21"} & primary_qs and all(str(i) in primary_qs for i in range(1, 21)):
        return "likely_actual_20_question_paper", "primary_sources_have_1_to_20_no_21"
    aux_hits = [q for q in missing if q in aux_qs]
    primary_hits = [q for q in missing if q in primary_qs]
    if primary_hits:
        return "matrix_or_filter_omission", f"primary_sources_have_missing_questions={','.join(primary_hits)}"
    if aux_hits:
        return "paper_or_ocr_missing_but_auxiliary_present", f"auxiliary_sources_have_missing_questions={','.join(aux_hits)}"
    return "source_or_ocr_missing_no_candidate", "missing_questions_absent_from_primary_and_auxiliary_candidates"


def main() -> int:
    candidates = load_candidates()
    matrix_qs = load_matrix_questions()
    rows = []
    with GAP_REVIEW.open("r", encoding="utf-8", newline="") as f:
        for gap in csv.DictReader(f):
            suite = gap["suite_id"]
            missing = gap["missing_if_expected_1_to_21"].split()
            source_map = candidates.get(suite, {})
            primary_qs = set()
            aux_qs = set()
            for source_type, qs in source_map.items():
                if source_type in PRIMARY_SOURCE_TYPES:
                    primary_qs |= qs
                elif source_type in AUX_SOURCE_TYPES:
                    aux_qs |= qs
            status, note = classify_gap(missing, primary_qs, aux_qs)
            rows.append(
                {
                    "suite_id": suite,
                    "detected_question_count": gap["detected_question_count"],
                    "missing_if_expected_1_to_21": gap["missing_if_expected_1_to_21"],
                    "triage_status": status,
                    "triage_note": note,
                    "primary_detected_questions": " ".join(qsort(primary_qs)),
                    "auxiliary_detected_questions": " ".join(qsort(aux_qs)),
                    "matrix_detected_questions": " ".join(qsort(matrix_qs.get(suite, set()))),
                }
            )

    fields = [
        "suite_id",
        "detected_question_count",
        "missing_if_expected_1_to_21",
        "triage_status",
        "triage_note",
        "primary_detected_questions",
        "auxiliary_detected_questions",
        "matrix_detected_questions",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    from collections import Counter

    counts = Counter(row["triage_status"] for row in rows)
    lines = [
        "# Question Gap Triage",
        "",
        f"- input_gap_rows: {len(rows)}",
        f"- output: `{OUT_CSV}`",
        "",
        "## Triage Counts",
        "",
    ]
    for key, value in counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Rows", ""])
    for row in rows:
        lines.append(
            f"- {row['suite_id']}: missing={row['missing_if_expected_1_to_21']}; "
            f"status={row['triage_status']}; note={row['triage_note']}"
        )
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- `likely_actual_20_question_paper` can be accepted only as a paper-structure finding for the source matrix, not as proof that the final handbook is complete.",
            "- `paper_or_ocr_missing_but_auxiliary_present` should be routed to OCR/raw-paper repair before final closure.",
            "- `source_or_ocr_missing_no_candidate` requires raw source inspection if final coverage is needed.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUT_CSV)
    print(OUT_MD)
    print("counts", dict(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
