# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
P0_DIR = RUN_DIR / "claudecode_lane" / "p0_recheck"
MANIFEST = RUN_DIR / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"
OUT_JSON = P0_DIR / "P0_RECHECK_QA.json"
OUT_MD = P0_DIR / "P0_RECHECK_QA.md"

REQUIRED_FILES = [
    "PROGRESS.md",
    "P0_RECHECK_DECISIONS.csv",
    "P0_RECHECK_PATCHES.jsonl",
    "P0_SOURCE_EVIDENCE.md",
    "P0_RECHECK_ACCEPTANCE.md",
]

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
    "\u56fa\u5b9a\u5206\u6790\u6d41\u7a0b",
    "FINAL_PASS",
    "\u7ec8\u7a3f\u5df2\u901a\u8fc7",
    "\u6700\u7ec8\u7248",
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


def manifest_p0_rows() -> list[dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r.get("priority") == "P0"]


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
                issues.append({"kind": "patch_missing_fields", "line": line_no, "question_id": obj.get("question_id", ""), "fields": missing})
            decision = str(obj.get("decision", ""))
            if decision and decision not in ALLOWED_DECISIONS:
                issues.append({"kind": "patch_invalid_decision", "line": line_no, "question_id": obj.get("question_id", ""), "decision": decision})
            for field in ["patched_material_signal", "patched_trigger_logic", "patched_answer_sentence"]:
                value = str(obj.get(field, ""))
                if any(token in value for token in FORBIDDEN_TEXT):
                    issues.append({"kind": "patch_forbidden_text", "line": line_no, "question_id": obj.get("question_id", ""), "field": field})
    return issues, rows


def main() -> int:
    P0_DIR.mkdir(parents=True, exist_ok=True)
    expected_rows = manifest_p0_rows()
    expected_keys = Counter(row_key(row) for row in expected_rows)
    expected_qids = [row.get("question_id", "") for row in expected_rows]

    missing_files = [name for name in REQUIRED_FILES if not (P0_DIR / name).exists()]
    decision_header, decisions, bad_width = read_csv_rows(P0_DIR / "P0_RECHECK_DECISIONS.csv")
    patch_issues, patch_rows = audit_jsonl(P0_DIR / "P0_RECHECK_PATCHES.jsonl")

    issues: list[dict[str, object]] = []
    if missing_files:
        issues.append({"kind": "missing_required_files", "files": missing_files})
    if decision_header and decision_header != DECISION_FIELDS:
        issues.append({"kind": "decision_header_mismatch", "header": decision_header})
    if bad_width:
        issues.append({"kind": "decision_bad_width", "rows": bad_width[:20]})
    if decisions and len(decisions) != 19:
        issues.append({"kind": "decision_row_count_not_19", "count": len(decisions)})
    if patch_rows and len(patch_rows) != 19:
        issues.append({"kind": "patch_row_count_not_19", "count": len(patch_rows)})

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
        qid = row.get("question_id", "")
        missing = [field for field in DECISION_FIELDS if not str(row.get(field, "")).strip()]
        if missing:
            issues.append({"kind": "decision_missing_fields", "line": idx, "question_id": qid, "fields": missing})
        if row.get("priority") != "P0":
            issues.append({"kind": "decision_priority_not_p0", "line": idx, "question_id": qid, "priority": row.get("priority")})
        if row.get("decision") not in ALLOWED_DECISIONS:
            issues.append({"kind": "decision_invalid_value", "line": idx, "question_id": qid, "decision": row.get("decision")})
        if row.get("can_enter_fusion") not in ALLOWED_ENTER_FUSION:
            issues.append({"kind": "decision_invalid_can_enter_fusion", "line": idx, "question_id": qid, "value": row.get("can_enter_fusion")})
        joined = " ".join(str(row.get(field, "")) for field in ["framework_node", "decision_reason", "source_evidence"])
        if any(token in joined for token in FORBIDDEN_TEXT):
            issues.append({"kind": "decision_forbidden_text", "line": idx, "question_id": qid})

    issues.extend(patch_issues)

    evidence_text = (P0_DIR / "P0_SOURCE_EVIDENCE.md").read_text(encoding="utf-8", errors="replace") if (P0_DIR / "P0_SOURCE_EVIDENCE.md").exists() else ""
    acceptance_text = (P0_DIR / "P0_RECHECK_ACCEPTANCE.md").read_text(encoding="utf-8", errors="replace") if (P0_DIR / "P0_RECHECK_ACCEPTANCE.md").exists() else ""
    if evidence_text and len(evidence_text.strip()) < 400:
        issues.append({"kind": "source_evidence_too_short", "length": len(evidence_text.strip())})
    if acceptance_text:
        lower = acceptance_text.lower()
        if "19" not in acceptance_text:
            issues.append({"kind": "acceptance_missing_19_count"})
        has_word_no = ("word" in lower and "no" in lower) or "\u662f\u5426\u751f\u6210 Word\uff1a**no**".lower() in lower
        has_pdf_no = ("pdf" in lower and "no" in lower) or "\u662f\u5426\u751f\u6210 PDF\uff1a**no**".lower() in lower
        if not (has_word_no and has_pdf_no):
            issues.append({"kind": "acceptance_missing_word_pdf_no"})
        if "\u7ec8\u7a3f" not in acceptance_text and "final" not in lower:
            issues.append({"kind": "acceptance_missing_final_boundary"})

    if any(row.get("question_id") == "Q-2026\u987a\u4e49\u4e00\u6a21-19-1" and row.get("decision") == "source_insufficient" for row in decisions):
        issues.append({"kind": "shunyi_19_1_still_source_insufficient"})
    if any(row.get("question_id") == "Q-2026\u987a\u4e49\u4e00\u6a21-19-1" and row.get("decision") == "source_insufficient" for row in patch_rows):
        issues.append({"kind": "shunyi_19_1_patch_still_source_insufficient"})
    current_decision_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in [P0_DIR / "P0_RECHECK_DECISIONS.csv", P0_DIR / "P0_RECHECK_PATCHES.jsonl"]
        if path.exists()
    )
    if "\u7ec6\u5219.pptx\u7a7a" in current_decision_text:
        issues.append({"kind": "corrected_sources_still_marked_empty"})

    decision_counts = Counter(r.get("decision", "") for r in decisions)
    enter_counts = Counter(r.get("can_enter_fusion", "") for r in decisions)
    summary = {
        "verdict": "P0_RECHECK_QA_OK_NOT_FINAL" if not issues else "P0_RECHECK_QA_FAIL",
        "expected_rows": 19,
        "expected_qids": expected_qids,
        "missing_files": missing_files,
        "decision_rows": len(decisions),
        "patch_rows": len(patch_rows),
        "decision_counts": dict(decision_counts),
        "can_enter_fusion_counts": dict(enter_counts),
        "issue_count": len(issues),
        "issues": issues[:200],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# P0 Recheck QA",
        "",
        f"Verdict: `{summary['verdict']}`",
        "",
        f"- decision rows: `{summary['decision_rows']}` / `19`",
        f"- patch rows: `{summary['patch_rows']}` / `19`",
        f"- decision counts: `{summary['decision_counts']}`",
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
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
