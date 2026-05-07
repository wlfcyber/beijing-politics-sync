# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
LANE = RUN_DIR / "claudecode_lane" / "p2_recheck"
MANIFEST = RUN_DIR / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"
FIELDS = [
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
ALLOWED = {
    "confirmed",
    "confirmed_with_patch",
    "downgrade_to_index",
    "source_insufficient",
    "wrong_framework",
    "block_from_student_body",
}
FORBIDDEN = ["固定分析流程", "FINAL_PASS", "终稿已通过", "最终版"]


def load_expected(source_ids: set[str]) -> list[dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.DictReader(f) if r.get("priority") == "P2" and r.get("source_id") in source_ids]


def row_key(row: dict[str, str]) -> tuple[str, str]:
    return row.get("question_id", ""), row.get("framework_node", "")


def read_decisions(path: Path) -> tuple[list[str], list[dict[str, str]], list[dict[str, object]]]:
    if not path.exists():
        return [], [], []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        raw = list(csv.reader(f))
    if not raw:
        return [], [], []
    header = raw[0]
    bad = [
        {"line": i, "field_count": len(row), "expected": len(header), "head": row[:8]}
        for i, row in enumerate(raw[1:], start=2)
        if len(row) != len(header)
    ]
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f)) if not bad else []
    return header, rows, bad


def read_patches(path: Path) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
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
                issues.append({"kind": "bad_json", "line": line_no, "error": str(exc), "text": text[:120]})
                continue
            rows.append(obj)
            missing = [field for field in PATCH_FIELDS if not str(obj.get(field, "")).strip()]
            if missing:
                issues.append({"kind": "patch_missing_fields", "line": line_no, "question_id": obj.get("question_id", ""), "fields": missing})
            if obj.get("decision") not in ALLOWED:
                issues.append({"kind": "patch_invalid_decision", "line": line_no, "question_id": obj.get("question_id", ""), "decision": obj.get("decision")})
    return issues, rows


def main() -> int:
    if len(sys.argv) < 4:
        raise SystemExit("usage: audit_p2_source_group.py PREFIX EXPECTED SOURCE_ID [SOURCE_ID...]")
    prefix = sys.argv[1].upper()
    expected_count = int(sys.argv[2])
    source_ids = set(sys.argv[3:])
    expected = load_expected(source_ids)
    exp_keys = Counter(row_key(row) for row in expected)
    exp_evidence = {row_key(row): row.get("evidence_level", "") for row in expected}
    required = [
        f"{prefix}_RECHECK_DECISIONS.csv",
        f"{prefix}_RECHECK_PATCHES.jsonl",
        f"{prefix}_SOURCE_EVIDENCE.md",
        f"{prefix}_RECHECK_ACCEPTANCE.md",
        f"{prefix}_PROGRESS.md",
    ]
    missing_files = [name for name in required if not (LANE / name).exists()]
    header, decisions, bad_width = read_decisions(LANE / f"{prefix}_RECHECK_DECISIONS.csv")
    patch_issues, patches = read_patches(LANE / f"{prefix}_RECHECK_PATCHES.jsonl")
    issues: list[dict[str, object]] = []
    if len(expected) != expected_count:
        issues.append({"kind": "expected_manifest_count_mismatch", "manifest": len(expected), "expected": expected_count})
    if missing_files:
        issues.append({"kind": "missing_required_files", "files": missing_files})
    if header and header != FIELDS:
        issues.append({"kind": "decision_header_mismatch", "header": header})
    if bad_width:
        issues.append({"kind": "decision_bad_width", "rows": bad_width[:20]})
    if decisions and len(decisions) != expected_count:
        issues.append({"kind": "decision_row_count_mismatch", "count": len(decisions), "expected": expected_count})
    if patches and len(patches) != expected_count:
        issues.append({"kind": "patch_row_count_mismatch", "count": len(patches), "expected": expected_count})
    decision_keys = Counter(row_key(row) for row in decisions)
    patch_keys = Counter(row_key(row) for row in patches)
    if decisions and decision_keys != exp_keys:
        issues.append({"kind": "decision_key_mismatch", "missing": sorted(map(str, (exp_keys - decision_keys).elements())), "extra": sorted(map(str, (decision_keys - exp_keys).elements()))})
    if patches and patch_keys != exp_keys:
        issues.append({"kind": "patch_key_mismatch", "missing": sorted(map(str, (exp_keys - patch_keys).elements())), "extra": sorted(map(str, (patch_keys - exp_keys).elements()))})
    for i, row in enumerate(decisions, start=2):
        rk = row_key(row)
        missing = [field for field in FIELDS if not str(row.get(field, "")).strip()]
        if missing:
            issues.append({"kind": "decision_missing_fields", "line": i, "question_id": row.get("question_id", ""), "fields": missing})
        if row.get("priority") != "P2":
            issues.append({"kind": "priority_not_p2", "line": i, "question_id": row.get("question_id", ""), "priority": row.get("priority")})
        if row.get("decision") not in ALLOWED:
            issues.append({"kind": "decision_invalid", "line": i, "question_id": row.get("question_id", ""), "decision": row.get("decision")})
        if row.get("can_enter_fusion") not in {"yes", "no"}:
            issues.append({"kind": "bad_can_enter_fusion", "line": i, "question_id": row.get("question_id", ""), "value": row.get("can_enter_fusion")})
        if rk in exp_evidence and row.get("evidence_level") != exp_evidence[rk]:
            issues.append({"kind": "evidence_mismatch", "line": i, "question_id": row.get("question_id", ""), "got": row.get("evidence_level"), "expected": exp_evidence[rk]})
    issues.extend(patch_issues)
    combined = "\n".join((LANE / name).read_text(encoding="utf-8", errors="replace") for name in required if (LANE / name).exists())
    hits = {token: combined.count(token) for token in FORBIDDEN}
    if any(hits.values()):
        issues.append({"kind": "forbidden_text_present", "hits": hits})
    summary = {
        "verdict": f"{prefix}_QA_OK_NOT_FINAL" if not issues else f"{prefix}_QA_FAIL",
        "prefix": prefix,
        "expected_rows": expected_count,
        "missing_files": missing_files,
        "decision_rows": len(decisions),
        "patch_rows": len(patches),
        "decision_counts": dict(Counter(row.get("decision", "") for row in decisions)),
        "evidence_counts": dict(Counter(row.get("evidence_level", "") for row in decisions)),
        "can_enter_fusion_counts": dict(Counter(row.get("can_enter_fusion", "") for row in decisions)),
        "issue_count": len(issues),
        "issues": issues[:120],
    }
    (LANE / f"{prefix}_QA.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (LANE / f"{prefix}_QA.md").write_text(
        "\n".join(
            [
                f"# {prefix} QA",
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
                *([f"- `{issue['kind']}`: `{issue}`" for issue in issues[:80]] if issues else ["- none"]),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
