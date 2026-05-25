from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
ROOT = RECOVERY.parents[1]
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DESKTOP = Path.home() / "Desktop"
RESEARCH = DESKTOP / "beijing_politics_research"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
OUT_CSV = RECOVERY / "MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv"
OUT_MD = RECOVERY / "MATRIX_EVIDENCE_RISK_AUDIT_20260525.md"

YES = chr(0x662F)
NO = chr(0x5426)
STRONG = "".join(chr(c) for c in [0x5F3A, 0x7EC6, 0x5219])
RUBRIC = "".join(chr(c) for c in [0x7EC6, 0x5219])
REF_ANSWER = "".join(chr(c) for c in [0x53C2, 0x8003, 0x7B54, 0x6848])
TEACHER_KEY = "".join(chr(c) for c in [0x6559, 0x5E08, 0x7248, 0x7B54, 0x6848, 0x952E])
ANSWER_KEY = "".join(chr(c) for c in [0x7B54, 0x6848, 0x952E])
SCORING = "".join(chr(c) for c in [0x8BC4, 0x5206])
MARKING_REVIEW = "".join(chr(c) for c in [0x9605, 0x5377])
EVAL_STANDARD = "".join(chr(c) for c in [0x8BC4, 0x6807])
FORMAL = "".join(chr(c) for c in [0x6B63, 0x5F0F])
CHOICE = "".join(chr(c) for c in [0x9009, 0x62E9])
OBJECTIVE = "".join(chr(c) for c in [0x5BA2, 0x89C2])
WEAK = chr(0x5F31)
PENDING = "".join(chr(c) for c in [0x5F85, 0x8865])
CHOICE_BOUNDARY_DISCLOSED = "".join(chr(c) for c in [0x9009, 0x62E9, 0x9898, 0x8FB9, 0x754C, 0x5DF2, 0x660E, 0x793A])
NOT_MAIN_SCORING_RUBRIC = "".join(
    chr(c)
    for c in [
        0x975E,
        0x4E3B,
        0x89C2,
        0x9898,
        0x8BC4,
        0x5206,
        0x7EC6,
        0x5219,
    ]
)
MEDIUM_EVIDENCE_TERMS = [
    "".join(chr(c) for c in [0x4E2D, 0x7B49, 0x8BC1, 0x636E]),
    "".join(chr(c) for c in [0x4E2D, 0x7B49, 0x652F, 0x6301]),
    "".join(chr(c) for c in [0x4E2D, 0x7B49, 0x5F3A, 0x5EA6]),
]

FORMAL_TERMS = [
    STRONG,
    RUBRIC,
    SCORING,
    MARKING_REVIEW,
    EVAL_STANDARD,
    FORMAL,
    "rubric",
    "marking",
    "formal",
]


def clean_source_path(raw: str) -> str:
    item = raw.strip().strip("`").strip()
    if not item:
        return ""
    if "|" in item:
        item = item.split("|", 1)[0].strip()
    # Drop common line/page/paragraph suffixes from relative artifact pointers.
    item = re.sub(r":\s*(pages?|paras?|lines?)\s*[\w,\-\s]+$", "", item, flags=re.IGNORECASE)
    if ":" in item and not (len(item) > 2 and item[1] == ":"):
        head, tail = item.rsplit(":", 1)
        if tail.isdigit() or all(ch.isdigit() or ch == "-" for ch in tail):
            item = head
    return item.replace("/", "\\")


def source_pointer_candidates(item: str) -> list[Path]:
    candidate = Path(item)
    if candidate.is_absolute():
        return [candidate]
    candidates = []
    for root in [RECOVERY, RUN, ROOT, DESKTOP, RESEARCH, RESEARCH / "data"]:
        candidates.append(root / item)
    return candidates


def source_pointer_exists(raw: str) -> bool:
    parts = [part for part in raw.split(";") if part.strip()]
    if not parts:
        parts = [raw]
    for part in parts:
        item = clean_source_path(part)
        if not item:
            continue
        for candidate in source_pointer_candidates(item):
            if candidate.exists():
                return True
    return False


def row_risks(row: dict[str, str]) -> list[str]:
    in_book = row["in_book"]
    evidence = row["evidence_level"]
    support = row["support_text"]
    misplaced = row["misplaced"]
    need_thick = row["need_thick"]
    current = row["current_status"]
    source = row["source_artifact"]

    risks: list[str] = []
    is_in_body = in_book.startswith(YES)
    combined = " ".join([evidence, support, row["question_type"], row["note"]])
    combined_lower = combined.lower()
    formal_signal = any(term.lower() in combined_lower for term in FORMAL_TERMS)
    objective_key_signal = any(token in combined for token in [ANSWER_KEY, CHOICE, OBJECTIVE])
    choice_boundary_disclosed = CHOICE_BOUNDARY_DISCLOSED in combined or NOT_MAIN_SCORING_RUBRIC in combined
    if is_in_body and not formal_signal:
        if objective_key_signal:
            if not choice_boundary_disclosed:
                risks.append("OBJECTIVE_KEY_ONLY_IN_BODY_BOUNDARY")
        else:
            risks.append("IN_BODY_LACKS_FORMAL_RUBRIC_SIGNAL")
    if is_in_body and (WEAK in evidence or REF_ANSWER in evidence or any(token in evidence for token in MEDIUM_EVIDENCE_TERMS)):
        risks.append("IN_BODY_WEAK_OR_REFERENCE_EVIDENCE")
    if any(token in support for token in ["external Claude", "GPTPro", "source bundle repair", "Claude triage"]):
        risks.append("MODEL_SUMMARY_USED_AS_SUPPORT_TEXT")
    if any(token in support for token in [REF_ANSWER, TEACHER_KEY]) and not formal_signal:
        risks.append("ANSWER_KEY_OR_REFERENCE_SUPPORT_NEEDS_BOUNDARY_CHECK")
    if any(token in evidence for token in ["term_hit_needs_review", "(寰呭畾)", "(待定)", "needs_review"]):
        risks.append("EVIDENCE_LEVEL_STILL_REVIEW_NEEDED")
    if misplaced.startswith(YES):
        risks.append("ROW_MARKED_MISPLACED")
    if need_thick.startswith(YES) or PENDING in need_thick:
        risks.append("ROW_MARKED_NEEDS_THICKENING")
    if any(token in current.upper() for token in ["NEED", "PENDING", "BLOCK", "TODO"]):
        risks.append("CURRENT_STATUS_OPEN")
    if not source_pointer_exists(source):
        risks.append("SOURCE_ARTIFACT_POINTER_NOT_RESOLVED")
    if is_in_body and not support.strip():
        risks.append("IN_BODY_EMPTY_SUPPORT_TEXT")
    return risks


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        raw_rows = [dict(zip(header, row)) for row in reader]

    rows = []
    for row in raw_rows:
        rows.append(
            {
                "row_id": row.get("matrix_row_id", ""),
                "row_source": row.get("row_source", ""),
                "suite": row.get(header[2], ""),
                "year": row.get(header[3], ""),
                "stage": row.get(header[4], ""),
                "question": row.get(header[5], ""),
                "question_type": row.get(header[6], ""),
                "in_book": row.get(header[7], ""),
                "node": row.get(header[8], ""),
                "support_text": row.get(header[9], ""),
                "evidence_level": row.get(header[10], ""),
                "misplaced": row.get(header[11], ""),
                "need_thick": row.get(header[12], ""),
                "current_status": row.get(header[13], ""),
                "note": row.get(header[14], ""),
                "source_artifact": row.get(header[15], ""),
            }
        )

    risk_rows = []
    for row in rows:
        risks = row_risks(row)
        if not risks:
            continue
        risk_rank = 0
        if row["in_book"].startswith(YES):
            risk_rank += 20
        if "IN_BODY_LACKS_FORMAL_RUBRIC_SIGNAL" in risks:
            risk_rank += 30
        if "OBJECTIVE_KEY_ONLY_IN_BODY_BOUNDARY" in risks:
            risk_rank += 10
        if "MODEL_SUMMARY_USED_AS_SUPPORT_TEXT" in risks:
            risk_rank += 25
        if "EVIDENCE_LEVEL_STILL_REVIEW_NEEDED" in risks:
            risk_rank += 20
        if "ROW_MARKED_MISPLACED" in risks or "ROW_MARKED_NEEDS_THICKENING" in risks:
            risk_rank += 20
        if "SOURCE_ARTIFACT_POINTER_NOT_RESOLVED" in risks:
            risk_rank += 10
        risk_rows.append({**row, "risk_rank": str(risk_rank), "risks": "|".join(risks)})

    risk_rows.sort(key=lambda r: (-int(r["risk_rank"]), r["suite"], r["question"], r["row_id"]))

    out_fields = [
        "risk_rank",
        "row_id",
        "suite",
        "year",
        "stage",
        "question",
        "in_book",
        "node",
        "evidence_level",
        "current_status",
        "risks",
        "support_text",
        "source_artifact",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for row in risk_rows:
            writer.writerow({field: row.get(field, "") for field in out_fields})

    total = len(rows)
    in_body = sum(1 for row in rows if row["in_book"].startswith(YES))
    risk_in_body = sum(1 for row in risk_rows if row["in_book"].startswith(YES))
    evidence_counts = Counter(row["evidence_level"] for row in rows)
    risk_counts = Counter()
    for row in risk_rows:
        risk_counts.update(row["risks"].split("|"))
    suite_risk_counts = Counter(row["suite"] for row in risk_rows)
    top = risk_rows[:25]
    status = "RISK_QUEUE_CLOSED" if not risk_rows else "RISK_QUEUE_CREATED_NOT_CLOSED"

    lines = [
        "# MATRIX_EVIDENCE_RISK_AUDIT_20260525",
        "",
        f"Status: `{status}`",
        "",
        f"- Matrix rows audited: `{total}`.",
        f"- Rows marked in-book/body: `{in_body}`.",
        f"- Risk rows generated: `{len(risk_rows)}`.",
        f"- In-book/body risk rows: `{risk_in_body}`.",
        f"- Output CSV: `MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv`.",
        "",
        "## Evidence Level Distribution",
        "",
    ]
    for key, count in evidence_counts.most_common():
        lines.append(f"- `{key or 'EMPTY'}`: `{count}`")
    lines.extend(["", "## Risk Type Distribution", ""])
    for key, count in risk_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Highest-Risk Suites", ""])
    for key, count in suite_risk_counts.most_common(20):
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Top Risk Rows", ""])
    lines.append("| rank | row | suite | question | evidence | risks |")
    lines.append("|---:|---|---|---|---|---|")
    for row in top:
        lines.append(
            "| {rank} | {row_id} | {suite} | {question} | {evidence} | {risks} |".format(
                rank=row["risk_rank"],
                row_id=row["row_id"],
                suite=row["suite"].replace("|", "/"),
                question=row["question"].replace("|", "/"),
                evidence=row["evidence_level"].replace("|", "/"),
                risks=row["risks"].replace("|", "<br>"),
            )
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This audit is a triage queue, not a row-level closure.",
            "- `SOURCE_ARTIFACT_POINTER_NOT_RESOLVED` can include descriptive source packets; those rows require human source-path normalization before being treated as unsupported.",
            "- Model summary text, teacher answer keys, and reference answers remain non-rubric support unless the row also points to formal scoring rules, marking reports, or user-confirmed scoring files.",
            "- Choice-question official answer-key rows are not counted as formal-rubric risks only when the matrix explicitly says they are correct-option chains, not main-question scoring-rubric evidence.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"MATRIX_ROWS={total}")
    print(f"IN_BODY_ROWS={in_body}")
    print(f"RISK_ROWS={len(risk_rows)}")
    print(f"IN_BODY_RISK_ROWS={risk_in_body}")
    print(f"OUT_CSV={OUT_CSV}")
    print(f"OUT_MD={OUT_MD}")


if __name__ == "__main__":
    main()
