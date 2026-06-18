#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "prompt_resolved_classification_matrix.csv"
REPAIR = RUN_DIR / "05_reports" / "question_gap_repair_candidates.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "gap_high_confidence_repaired_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "GAP_HIGH_CONFIDENCE_REPAIRED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "gap_high_confidence_repair_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "gap_high_confidence_repaired_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "gap_high_confidence_repair_report.md"
OUT_GAP_AFTER = RUN_DIR / "05_reports" / "question_gap_after_high_confidence_repair.csv"
TRIAGE = RUN_DIR / "05_reports" / "question_gap_triage.csv"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 900) -> str:
    return re.sub(r"\s+", " ", text).strip()[:limit]


def parse_suite(suite_id: str) -> tuple[str, str, str]:
    parts = suite_id.split("_")
    year = parts[0] if len(parts) > 0 else ""
    district = parts[1] if len(parts) > 1 else ""
    stage = parts[2] if len(parts) > 2 else ""
    return year, district, stage


def resolve_high_confidence(prompt: str) -> dict[str, str]:
    xb2_terms = ["法律与生活", "民事法律关系", "诉讼", "侵权", "调解", "欠条", "货款"]
    b3_terms = ["政治与法治", "人大代表", "人民代表大会", "依法行政", "交通勤务", "政府部门"]
    b2_terms = ["经济与社会", "新质生产力", "高质量发展", "市场", "消费", "产业"]
    b4_terms = ["文化自信", "中华优秀传统文化", "文化遗产", "博物馆", "文旅"]
    for rule_id, module, status, next_action, terms in [
        ("GAP_XB2_LAW_HIGH_CONFIDENCE", "XB2_EXCLUDED", "module-boundary-excluded", "exclude_from_three_target_lines", xb2_terms),
        ("GAP_B3_POLITICS_HIGH_CONFIDENCE", "B3_POLITICS_RULE_OF_LAW", "included", "future_baodian_intake", b3_terms),
        ("GAP_B2_ECONOMICS_HIGH_CONFIDENCE", "B2_ECONOMICS", "included", "future_baodian_intake", b2_terms),
        ("GAP_B4_CULTURE_HIGH_CONFIDENCE", "B4_CULTURE", "included", "future_baodian_intake", b4_terms),
    ]:
        hits = [term for term in terms if term in prompt]
        if hits:
            return {
                "rule_id": rule_id,
                "book_module": module,
                "status": status,
                "next_action": next_action,
                "matched_terms": ",".join(hits[:8]),
            }
    return {
        "rule_id": "GAP_HIGH_CONFIDENCE_UNRESOLVED",
        "book_module": "UNKNOWN_OR_MIXED",
        "status": "blocked",
        "next_action": "manual_review_needed",
        "matched_terms": "",
    }


def question_type(question: str) -> str:
    return "objective" if question.isdigit() and int(question) <= 15 else "subjective"


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    existing = {(row["suite_id"], row["question"]) for row in rows}
    added_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []

    for repair in load_csv(REPAIR):
        if repair["recommended_action"] != "repair_primary_question_split_high_confidence":
            continue
        key = (repair["suite_id"], repair["missing_question"])
        if key in existing:
            continue
        year, district, stage = parse_suite(repair["suite_id"])
        prompt = compact(repair["raw_marker_snippet"], 1200)
        resolved = resolve_high_confidence(prompt)
        row = {field: "" for field in fields}
        row.update(
            {
                "suite_id": repair["suite_id"],
                "year": year,
                "district": district,
                "stage": stage,
                "question": repair["missing_question"],
                "parent_question": "",
                "row_granularity": "question",
                "book_module": resolved["book_module"],
                "question_type": question_type(repair["missing_question"]),
                "evidence_source": repair["raw_marker_text_path"],
                "source_types": "ocr-cache;gap-repair",
                "status": resolved["status"],
                "artifact_location": "05_reports/gap_high_confidence_repair_audit.csv",
                "decision_reason": json.dumps(
                    {
                        "rule_id": resolved["rule_id"],
                        "matched_terms": resolved["matched_terms"],
                        "source": "question_gap_repair_candidates.csv",
                        "repair_confidence": repair["raw_marker_confidence"],
                    },
                    ensure_ascii=False,
                ),
                "next_action": resolved["next_action"],
                "integration_status": "gap_high_confidence_repair",
            }
        )
        added_rows.append(row)
        audit_rows.append(
            {
                "suite_id": repair["suite_id"],
                "question": repair["missing_question"],
                "raw_marker_confidence": repair["raw_marker_confidence"],
                "new_book_module": resolved["book_module"],
                "new_status": resolved["status"],
                "rule_id": resolved["rule_id"],
                "matched_terms": resolved["matched_terms"],
                "raw_marker_text_path": repair["raw_marker_text_path"],
                "prompt": prompt,
            }
        )

    out_rows = rows + added_rows
    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(
        OUT_AUDIT,
        audit_rows,
        [
            "suite_id",
            "question",
            "raw_marker_confidence",
            "new_book_module",
            "new_status",
            "rule_id",
            "matched_terms",
            "raw_marker_text_path",
            "prompt",
        ],
    )
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    added_keys = {(row["suite_id"], row["question"]) for row in added_rows}
    gap_after = []
    for row in load_csv(TRIAGE):
        missing = [q for q in row["missing_if_expected_1_to_21"].split() if (row["suite_id"], q) not in added_keys]
        gap_after.append(
            {
                "suite_id": row["suite_id"],
                "missing_after_high_confidence_repair": " ".join(missing),
                "resolved_by_high_confidence_repair": " ".join(
                    q for q in row["missing_if_expected_1_to_21"].split() if (row["suite_id"], q) in added_keys
                ),
                "prior_triage_status": row["triage_status"],
            }
        )
    write_csv(
        OUT_GAP_AFTER,
        gap_after,
        [
            "suite_id",
            "missing_after_high_confidence_repair",
            "resolved_by_high_confidence_repair",
            "prior_triage_status",
        ],
    )

    status_counts = Counter(row["status"] for row in out_rows)
    target_counts = Counter(
        row["book_module"] for row in out_rows if row["status"] == "included" and row["book_module"] in TARGET_MODULES
    )
    action_counts = Counter(row["rule_id"] for row in audit_rows)
    remaining_missing = sum(
        len(row["missing_after_high_confidence_repair"].split()) for row in gap_after if row["missing_after_high_confidence_repair"]
    )

    lines = [
        "# Gap High-Confidence Repair Report",
        "",
        f"- input_rows: {len(rows)}",
        f"- added_high_confidence_rows: {len(added_rows)}",
        f"- output_rows: {len(out_rows)}",
        f"- output_matrix: `{OUT_MATRIX}`",
        f"- output_coverage: `{OUT_COVERAGE}`",
        f"- audit: `{OUT_AUDIT}`",
        f"- remaining_missing_question_entries_from_prior_gap: {remaining_missing}",
        "",
        "## Status Counts",
        "",
    ]
    for key, value in status_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Target Included Counts", ""])
    for key in ["B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"]:
        lines.append(f"- {key}: {target_counts.get(key, 0)}")
    lines.extend(["", "## Added Rules", ""])
    for key, value in action_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- This matrix repairs only high-confidence missing question starts from the gap packet.",
            "- It does not close the remaining blocked rows or low-confidence gap candidates.",
            "- Keep `PROMPT_RESOLVED_COVERAGE_MATRIX.csv` as audit history; use this matrix only after accepting the high-confidence repair audit.",
        ]
    )
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUT_MATRIX)
    print(OUT_COVERAGE)
    print(OUT_AUDIT)
    print("added", len(added_rows), "rows", len(out_rows), "remaining_gap_entries", remaining_missing)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
