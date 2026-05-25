from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import matrix_evidence_risk_audit_20260525 as risk


ROOT = Path(__file__).resolve().parent
MATRIX = ROOT / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
OUT_CSV = ROOT / "BODY_ROW_PROOF_PACK_20260525.csv"
OUT_MD = ROOT / "BODY_ROW_PROOF_PACK_20260525.md"
OUT_JSON = ROOT / "BODY_ROW_PROOF_PACK_20260525.json"

YES = chr(0x662F)
PENDING = "".join(chr(c) for c in [0x5F85, 0x8865])
CHOICE = "".join(chr(c) for c in [0x9009, 0x62E9])
OBJECTIVE = "".join(chr(c) for c in [0x5BA2, 0x89C2])
ANSWER_KEY = "".join(chr(c) for c in [0x7B54, 0x6848, 0x952E])
REF_ANSWER = "".join(chr(c) for c in [0x53C2, 0x8003, 0x7B54, 0x6848])
TEACHER_VERSION = "".join(chr(c) for c in [0x6559, 0x5E08, 0x7248])
MODEL_SUMMARY = "".join(chr(c) for c in [0x6A21, 0x578B, 0x6458, 0x8981])
WEAK = chr(0x5F31)
NON_MAIN_RUBRIC = "".join(chr(c) for c in [0x975E, 0x4E3B, 0x89C2, 0x9898, 0x8BC4, 0x5206, 0x7EC6, 0x5219])
CHOICE_BOUNDARY = "".join(chr(c) for c in [0x9009, 0x62E9, 0x9898, 0x8FB9, 0x754C])
BROAD_TERMS = [
    "".join(chr(c) for c in [0x5BBD, 0x89D2, 0x5EA6]),
    "".join(chr(c) for c in [0x7EFC, 0x5408, 0x89D2, 0x5EA6]),
    "".join(chr(c) for c in [0x5F00, 0x653E, 0x89D2, 0x5EA6]),
    "".join(chr(c) for c in [0x7B49, 0x7EA7]),
    "".join(chr(c) for c in [0x672F, 0x8BED, 0x652F, 0x6301]),
    "".join(chr(c) for c in [0x975E, 0x9010, 0x70B9]),
]


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def read_matrix() -> list[dict[str, str]]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        out = []
        for row in reader:
            raw = dict(zip(header, row))
            out.append(
                {
                    "row_id": raw.get("matrix_row_id", ""),
                    "row_source": raw.get("row_source", ""),
                    "suite": raw.get(header[2], ""),
                    "year": raw.get(header[3], ""),
                    "stage": raw.get(header[4], ""),
                    "question": raw.get(header[5], ""),
                    "question_type": raw.get(header[6], ""),
                    "in_book": raw.get(header[7], ""),
                    "node": raw.get(header[8], ""),
                    "support_text": raw.get(header[9], ""),
                    "evidence_level": raw.get(header[10], ""),
                    "misplaced": raw.get(header[11], ""),
                    "need_thick": raw.get(header[12], ""),
                    "current_status": raw.get(header[13], ""),
                    "note": raw.get(header[14], ""),
                    "source_artifact": raw.get(header[15], ""),
                }
            )
        return out


def in_body(row: dict[str, str]) -> bool:
    return row["in_book"].startswith(YES)


def contains_any(text: str, terms: list[str]) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in terms)


def formal_signal(text: str) -> bool:
    return contains_any(text, risk.FORMAL_TERMS)


def objective_key_signal(text: str) -> bool:
    return any(term in text for term in [CHOICE, OBJECTIVE, ANSWER_KEY])


def choice_boundary_disclosed(text: str) -> bool:
    return NON_MAIN_RUBRIC in text or CHOICE_BOUNDARY in text


def weak_signal(text: str) -> bool:
    return any(term in text for term in [WEAK, REF_ANSWER, TEACHER_VERSION, MODEL_SUMMARY, "Claude", "GPT", "model"])


def ordinary_reference_signal(text: str) -> bool:
    return any(term in text for term in [REF_ANSWER, TEACHER_VERSION])


def broad_angle_signal(text: str) -> bool:
    return contains_any(text, BROAD_TERMS) or "formal_rubric_optional_angle" in text


def classify(row: dict[str, str], combined: str) -> str:
    formal = formal_signal(combined)
    objective = objective_key_signal(combined)
    boundary = choice_boundary_disclosed(combined)
    weak = weak_signal(combined)
    broad = broad_angle_signal(combined)
    if objective and boundary:
        return "objective_choice_chain_bounded"
    if formal and broad:
        return "formal_broad_angle_or_level_support"
    if formal and weak:
        return "weak_signal_with_formal_support"
    if formal:
        return "formal_scoring_or_marking_support"
    if objective:
        return "objective_key_signal_boundary_needed"
    if weak:
        return "weak_reference_only_boundary_needed"
    return "needs_manual_evidence_classification"


def proof_gap_flags(row: dict[str, str], combined: str, source_exists: bool) -> list[str]:
    flags: list[str] = []
    formal = formal_signal(combined)
    objective = objective_key_signal(combined)
    boundary = choice_boundary_disclosed(combined)
    weak = weak_signal(combined)
    if not source_exists:
        flags.append("MISSING_SOURCE_POINTER")
    if weak and not formal and not (objective and boundary):
        flags.append("WEAK_ONLY_BODY_SUPPORT")
    if objective and not formal and not boundary:
        flags.append("OBJECTIVE_KEY_WITHOUT_BOUNDARY")
    if not formal and not (objective and boundary):
        flags.append("NO_FORMAL_OR_OBJECTIVE_BOUNDARY_SIGNAL")
    if row["misplaced"].startswith(YES):
        flags.append("MATRIX_MARKED_MISPLACED")
    if row["need_thick"].startswith(YES) or PENDING in row["need_thick"]:
        flags.append("MATRIX_MARKED_NEEDS_THICKENING")
    if any(token in row["current_status"].upper() for token in ["NEED", "PENDING", "BLOCK", "TODO"]):
        flags.append("CURRENT_STATUS_OPEN")
    return flags


def main() -> None:
    rows = read_matrix()
    body = [row for row in rows if in_body(row)]
    proof_rows: list[dict[str, str]] = []
    for row in body:
        combined = " | ".join(
            [
                row["question_type"],
                row["support_text"],
                row["evidence_level"],
                row["misplaced"],
                row["need_thick"],
                row["current_status"],
                row["note"],
            ]
        )
        source_exists = risk.source_pointer_exists(row["source_artifact"])
        flags = proof_gap_flags(row, combined, source_exists)
        evidence_class = classify(row, combined)
        proof_rows.append(
            {
                "matrix_row_id": row["row_id"],
                "suite": row["suite"],
                "year": row["year"],
                "stage": row["stage"],
                "question": row["question"],
                "question_type": row["question_type"],
                "in_book_value": row["in_book"],
                "baodian_node": row["node"],
                "evidence_level": row["evidence_level"],
                "evidence_class": evidence_class,
                "formal_signal": str(formal_signal(combined)).lower(),
                "objective_key_signal": str(objective_key_signal(combined)).lower(),
                "choice_boundary_disclosed": str(choice_boundary_disclosed(combined)).lower(),
                "weak_signal": str(weak_signal(combined)).lower(),
                "ordinary_reference_signal": str(ordinary_reference_signal(combined)).lower(),
                "broad_angle_or_level_signal": str(broad_angle_signal(combined)).lower(),
                "source_pointer_exists": str(source_exists).lower(),
                "source_artifact": row["source_artifact"],
                "current_status": row["current_status"],
                "misplaced_value": row["misplaced"],
                "need_thickness_value": row["need_thick"],
                "proof_status": "PASS_MACHINE_PROOF_PACK_ROW" if not flags else "REVIEW_REQUIRED",
                "proof_gap_flags": "|".join(flags),
                "support_excerpt": row["support_text"][:500],
                "note_excerpt": row["note"][:300],
            }
        )

    fields = [
        "matrix_row_id",
        "suite",
        "year",
        "stage",
        "question",
        "question_type",
        "in_book_value",
        "baodian_node",
        "evidence_level",
        "evidence_class",
        "formal_signal",
        "objective_key_signal",
        "choice_boundary_disclosed",
        "weak_signal",
        "ordinary_reference_signal",
        "broad_angle_or_level_signal",
        "source_pointer_exists",
        "source_artifact",
        "current_status",
        "misplaced_value",
        "need_thickness_value",
        "proof_status",
        "proof_gap_flags",
        "support_excerpt",
        "note_excerpt",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(proof_rows)

    counts = {
        "total_matrix_rows": len(rows),
        "body_rows": len(body),
        "proof_rows": len(proof_rows),
        "review_required_rows": sum(1 for row in proof_rows if row["proof_status"] != "PASS_MACHINE_PROOF_PACK_ROW"),
        "missing_source_pointer_rows": sum(1 for row in proof_rows if row["source_pointer_exists"] != "true"),
        "weak_signal_rows": sum(1 for row in proof_rows if row["weak_signal"] == "true"),
        "weak_only_body_support_rows": sum(1 for row in proof_rows if "WEAK_ONLY_BODY_SUPPORT" in row["proof_gap_flags"]),
        "ordinary_reference_signal_rows": sum(1 for row in proof_rows if row["ordinary_reference_signal"] == "true"),
        "objective_key_signal_rows": sum(1 for row in proof_rows if row["objective_key_signal"] == "true"),
        "objective_key_without_boundary_rows": sum(1 for row in proof_rows if "OBJECTIVE_KEY_WITHOUT_BOUNDARY" in row["proof_gap_flags"]),
        "broad_angle_or_level_rows": sum(1 for row in proof_rows if row["broad_angle_or_level_signal"] == "true"),
        "matrix_marked_misplaced_rows": sum(1 for row in proof_rows if "MATRIX_MARKED_MISPLACED" in row["proof_gap_flags"]),
        "matrix_marked_needs_thickening_rows": sum(1 for row in proof_rows if "MATRIX_MARKED_NEEDS_THICKENING" in row["proof_gap_flags"]),
    }
    class_counts = Counter(row["evidence_class"] for row in proof_rows)
    evidence_counts = Counter(row["evidence_level"] for row in proof_rows)
    status_counts = Counter(row["proof_status"] for row in proof_rows)
    source_kind_counts = Counter(row["row_source"] for row in body)

    summary = {
        "updated": now(),
        **counts,
        "proof_status_counts": dict(status_counts),
        "evidence_class_counts": dict(class_counts),
        "top_evidence_levels": dict(evidence_counts.most_common(30)),
        "row_source_counts": dict(source_kind_counts.most_common()),
        "output_csv": OUT_CSV.name,
        "boundary": [
            "This is a machine-built proof pack from the current coverage matrix and source_artifact pointers.",
            "It is not a substitute for manual source-page adjudication where the matrix support text itself is wrong.",
            "It does not close the separate thickness or every-page visual review gates.",
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Body Row Proof Pack 20260525",
        "",
        f"Updated: {summary['updated']}",
        "",
        "Status: `BODY_ROW_PROOF_PACK_CREATED_MACHINE_PASS_ZERO_ROW_GAPS`"
        if counts["review_required_rows"] == 0
        else "Status: `BODY_ROW_PROOF_PACK_CREATED_WITH_REVIEW_ROWS`",
        "",
        f"- Matrix rows audited: `{counts['total_matrix_rows']}`.",
        f"- In-book/body rows using matrix `是...` status: `{counts['body_rows']}`.",
        f"- Proof rows written: `{counts['proof_rows']}`.",
        f"- Rows requiring machine review: `{counts['review_required_rows']}`.",
        f"- Missing source pointer rows: `{counts['missing_source_pointer_rows']}`.",
        f"- Weak-signal rows: `{counts['weak_signal_rows']}`.",
        f"- Weak-only body support rows: `{counts['weak_only_body_support_rows']}`.",
        f"- Ordinary reference/teacher-version signal rows: `{counts['ordinary_reference_signal_rows']}`.",
        f"- Objective/choice-key signal rows: `{counts['objective_key_signal_rows']}`.",
        f"- Objective-key rows without explicit boundary: `{counts['objective_key_without_boundary_rows']}`.",
        f"- Broad-angle or level-support rows: `{counts['broad_angle_or_level_rows']}`.",
        f"- Matrix-marked misplaced rows: `{counts['matrix_marked_misplaced_rows']}`.",
        f"- Matrix-marked needs-thickening rows: `{counts['matrix_marked_needs_thickening_rows']}`.",
        f"- Output CSV: `{OUT_CSV.name}`.",
        f"- JSON summary: `{OUT_JSON.name}`.",
        "",
        "## Evidence Class Counts",
        "",
    ]
    for key, count in class_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Proof Status Counts", ""])
    for key, count in status_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Top Evidence Levels", ""])
    for key, count in evidence_counts.most_common(25):
        lines.append(f"- `{key or 'EMPTY'}`: `{count}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This proof pack is generated from the current matrix and source pointers, so it proves the current ledger state is internally auditable row-by-row.",
            "- It does not prove that every source paragraph was manually reread in this turn.",
            "- It does not close the separate `THICKNESS_DENSITY_AUDIT_20260525` queue, the 290-page visual log, or the ClaudeCode model-confirmation gate.",
            "- Choice-question rows are classified as bounded only when the matrix explicitly marks them as objective/correct-option chains or not main-question scoring-rubric evidence.",
            "- Ordinary reference answer or teacher-version signals are not accepted alone; any such body row must also have formal support or objective-choice boundary support. The weak-only count above must remain zero.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
