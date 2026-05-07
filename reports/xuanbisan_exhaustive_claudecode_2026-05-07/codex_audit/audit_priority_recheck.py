# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
MANIFEST = RUN_DIR / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"

DECISION_FIELDS = [
    "priority",
    "question_id",
    "parent_question_id",
    "source_batch",
    "type",
    "framework_node",
    "evidence_level",
    "decision",
    "decision_reason",
    "source_evidence",
    "patch_needed",
    "can_enter_fusion",
]

PATCH_FIELDS = [
    "question_id",
    "parent_question_id",
    "framework_node",
    "decision",
    "patched_material_signal",
    "patched_trigger_logic",
    "patched_answer_sentence",
    "source_evidence",
    "notes",
]

ALLOWED_DECISIONS = {
    "confirmed",
    "confirmed_with_patch",
    "downgrade_to_index",
    "source_insufficient",
    "wrong_framework",
    "block_from_student_body",
}
ALLOWED_ENTER_FUSION = {"yes", "no"}
FORBIDDEN_TEXT = [
    "固定分析流程",
    "FINAL_PASS",
    "终稿已通过",
    "最终版",
]


def read_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]], list[dict[str, object]]]:
    if not path.exists():
        return [], [], []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        raw_rows = list(csv.reader(f))
    if not raw_rows:
        return [], [], []
    header = raw_rows[0]
    bad_width = [
        {"line": idx, "field_count": len(row), "expected": len(header), "head": row[:8]}
        for idx, row in enumerate(raw_rows[1:], start=2)
        if len(row) != len(header)
    ]
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f)) if not bad_width else []
    return header, rows, bad_width


def manifest_rows(priority: str) -> list[dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r.get("priority") == priority]


def row_key(row: dict[str, str]) -> tuple[str, str]:
    return (row.get("question_id", ""), row.get("framework_node", ""))


def audit_jsonl(path: Path) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    issues: list[dict[str, object]] = []
    rows: list[dict[str, str]] = []
    if not path.exists():
        return issues, rows
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line_no, line in enumerate(f, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                obj = json.loads(text)
            except json.JSONDecodeError as exc:
                issues.append({"kind": "bad_json", "line": line_no, "error": str(exc), "text": text[:160]})
                continue
            rows.append(obj)
            missing = [field for field in PATCH_FIELDS if not str(obj.get(field, "")).strip()]
            if missing:
                issues.append(
                    {
                        "kind": "patch_missing_fields",
                        "line": line_no,
                        "question_id": obj.get("question_id", ""),
                        "fields": missing,
                    }
                )
            decision = str(obj.get("decision", ""))
            if decision and decision not in ALLOWED_DECISIONS:
                issues.append(
                    {
                        "kind": "patch_invalid_decision",
                        "line": line_no,
                        "question_id": obj.get("question_id", ""),
                        "decision": decision,
                    }
                )
            joined = " ".join(str(obj.get(field, "")) for field in PATCH_FIELDS)
            if any(token in joined for token in FORBIDDEN_TEXT):
                issues.append({"kind": "patch_forbidden_text", "line": line_no, "question_id": obj.get("question_id", "")})
    return issues, rows


def text_or_empty(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def main() -> int:
    priority = (sys.argv[1] if len(sys.argv) > 1 else "P1").upper()
    lower = priority.lower()
    lane_dir = RUN_DIR / "claudecode_lane" / f"{lower}_recheck"
    out_json = lane_dir / f"{priority}_RECHECK_QA.json"
    out_md = lane_dir / f"{priority}_RECHECK_QA.md"

    required_files = [
        "PROGRESS.md",
        f"{priority}_RECHECK_DECISIONS.csv",
        f"{priority}_RECHECK_PATCHES.jsonl",
        f"{priority}_SOURCE_EVIDENCE.md",
        f"{priority}_RECHECK_ACCEPTANCE.md",
    ]

    expected_rows = manifest_rows(priority)
    expected_keys = Counter(row_key(row) for row in expected_rows)
    expected_evidence = {row_key(row): row.get("evidence_level", "") for row in expected_rows}
    expected_count = len(expected_rows)

    missing_files = [name for name in required_files if not (lane_dir / name).exists()]
    decision_header, decisions, bad_width = read_csv_rows(lane_dir / f"{priority}_RECHECK_DECISIONS.csv")
    patch_issues, patch_rows = audit_jsonl(lane_dir / f"{priority}_RECHECK_PATCHES.jsonl")

    issues: list[dict[str, object]] = []
    if missing_files:
        issues.append({"kind": "missing_required_files", "files": missing_files})
    if decision_header and decision_header != DECISION_FIELDS:
        issues.append({"kind": "decision_header_mismatch", "header": decision_header})
    if bad_width:
        issues.append({"kind": "decision_bad_width", "rows": bad_width[:20]})
    if decisions and len(decisions) != expected_count:
        issues.append({"kind": "decision_row_count_mismatch", "count": len(decisions), "expected": expected_count})
    if patch_rows and len(patch_rows) != expected_count:
        issues.append({"kind": "patch_row_count_mismatch", "count": len(patch_rows), "expected": expected_count})

    decision_keys = Counter(row_key(row) for row in decisions)
    patch_keys = Counter(row_key(row) for row in patch_rows)
    if decisions and decision_keys != expected_keys:
        issues.append(
            {
                "kind": "decision_row_key_mismatch",
                "missing": sorted([str(k) for k, n in (expected_keys - decision_keys).items() for _ in range(n)]),
                "extra": sorted([str(k) for k, n in (decision_keys - expected_keys).items() for _ in range(n)]),
            }
        )
    if patch_rows and patch_keys != expected_keys:
        issues.append(
            {
                "kind": "patch_row_key_mismatch",
                "missing": sorted([str(k) for k, n in (expected_keys - patch_keys).items() for _ in range(n)]),
                "extra": sorted([str(k) for k, n in (patch_keys - expected_keys).items() for _ in range(n)]),
            }
        )

    for idx, row in enumerate(decisions, start=2):
        key = row_key(row)
        qid = row.get("question_id", "")
        missing = [field for field in DECISION_FIELDS if not str(row.get(field, "")).strip()]
        if missing:
            issues.append({"kind": "decision_missing_fields", "line": idx, "question_id": qid, "fields": missing})
        if row.get("priority") != priority:
            issues.append({"kind": "decision_priority_mismatch", "line": idx, "question_id": qid, "priority": row.get("priority")})
        if row.get("decision") not in ALLOWED_DECISIONS:
            issues.append({"kind": "decision_invalid_value", "line": idx, "question_id": qid, "decision": row.get("decision")})
        if row.get("can_enter_fusion") not in ALLOWED_ENTER_FUSION:
            issues.append({"kind": "decision_invalid_can_enter_fusion", "line": idx, "question_id": qid, "value": row.get("can_enter_fusion")})
        if key in expected_evidence and row.get("evidence_level") != expected_evidence[key]:
            issues.append(
                {
                    "kind": "decision_evidence_level_mismatch",
                    "line": idx,
                    "question_id": qid,
                    "got": row.get("evidence_level"),
                    "expected": expected_evidence[key],
                }
            )
        joined = " ".join(str(row.get(field, "")) for field in DECISION_FIELDS)
        if any(token in joined for token in FORBIDDEN_TEXT):
            issues.append({"kind": "decision_forbidden_text", "line": idx, "question_id": qid})

    issues.extend(patch_issues)

    evidence_text = text_or_empty(lane_dir / f"{priority}_SOURCE_EVIDENCE.md")
    acceptance_text = text_or_empty(lane_dir / f"{priority}_RECHECK_ACCEPTANCE.md")
    combined_text = "\n".join(
        text_or_empty(lane_dir / name)
        for name in [
            f"{priority}_RECHECK_DECISIONS.csv",
            f"{priority}_RECHECK_PATCHES.jsonl",
            f"{priority}_SOURCE_EVIDENCE.md",
            f"{priority}_RECHECK_ACCEPTANCE.md",
            "PROGRESS.md",
        ]
    )
    if evidence_text and len(evidence_text.strip()) < 300:
        issues.append({"kind": "source_evidence_too_short", "length": len(evidence_text.strip())})
    if acceptance_text:
        lower_acceptance = acceptance_text.lower()
        if str(expected_count) not in acceptance_text:
            issues.append({"kind": "acceptance_missing_expected_count", "expected": expected_count})
        if "not_final" not in lower_acceptance and "not final" not in lower_acceptance and "非终稿" not in acceptance_text:
            issues.append({"kind": "acceptance_missing_not_final"})
        has_word_no = "word" in lower_acceptance and "no" in lower_acceptance
        has_pdf_no = "pdf" in lower_acceptance and "no" in lower_acceptance
        if not (has_word_no and has_pdf_no):
            issues.append({"kind": "acceptance_missing_word_pdf_no"})
    if any(token in combined_text for token in FORBIDDEN_TEXT):
        issues.append({"kind": "forbidden_text_present"})

    if priority == "P1":
        if any(row.get("decision") == "source_insufficient" for row in decisions):
            issues.append({"kind": "p1_unexpected_source_insufficient"})
        if any(row.get("can_enter_fusion") != "yes" for row in decisions):
            issues.append({"kind": "p1_unexpected_blocked_from_fusion"})

    decision_counts = Counter(r.get("decision", "") for r in decisions)
    evidence_counts = Counter(r.get("evidence_level", "") for r in decisions)
    enter_counts = Counter(r.get("can_enter_fusion", "") for r in decisions)
    summary = {
        "verdict": f"{priority}_RECHECK_QA_OK_NOT_FINAL" if not issues else f"{priority}_RECHECK_QA_FAIL",
        "priority": priority,
        "expected_rows": expected_count,
        "missing_files": missing_files,
        "decision_rows": len(decisions),
        "patch_rows": len(patch_rows),
        "decision_counts": dict(decision_counts),
        "evidence_counts": dict(evidence_counts),
        "can_enter_fusion_counts": dict(enter_counts),
        "issue_count": len(issues),
        "issues": issues[:200],
    }
    out_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# {priority} Recheck QA",
        "",
        f"Verdict: `{summary['verdict']}`",
        "",
        f"- decision rows: `{summary['decision_rows']}` / `{expected_count}`",
        f"- patch rows: `{summary['patch_rows']}` / `{expected_count}`",
        f"- decision counts: `{summary['decision_counts']}`",
        f"- evidence counts: `{summary['evidence_counts']}`",
        f"- can_enter_fusion counts: `{summary['can_enter_fusion_counts']}`",
        f"- missing files: `{summary['missing_files']}`",
        f"- issue count: `{summary['issue_count']}`",
        "",
        "## Issues",
        "",
    ]
    if issues:
        for issue in issues[:80]:
            lines.append(f"- `{issue['kind']}`: `{issue}`")
    else:
        lines.append("- none")
    lines.extend(["", "## Boundary", "", "- This QA does not authorize final Word/PDF."])
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
