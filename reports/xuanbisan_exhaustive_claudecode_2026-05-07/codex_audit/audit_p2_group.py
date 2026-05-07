# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
MANIFEST = RUN_DIR / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"
LANE = RUN_DIR / "claudecode_lane" / "p2_recheck"

GROUPS = {
    "P2A": {
        "sources": {
            "017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf",
            "003_Desktop_2026模拟题_2026各区期末和期中_2026朝阳期中_试卷_试卷.pdf",
            "012_Desktop_2025模拟题_2025各区期末_2025东城期末_试卷_试卷.pdf",
            "046_Desktop_2026模拟题_2026各区一模_2026东城一模_试卷_试卷.pdf",
            "044_Desktop_2026模拟题_2026各区期末和期中_2026东城期末_试卷_试卷.pdf",
        },
        "expected": 17,
    },
    "P2B": {
        "sources": {
            "040_Desktop_2025模拟题_2025各区期末_2025丰台期末_试卷_试卷.pdf",
            "042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf",
            "001_Desktop_2026模拟题_2026各区一模_2026顺义一模_试卷_试卷.pdf",
            "006_Desktop_2026模拟题_2026各区期末和期中_2026通州期末_试卷_试卷.pdf",
            "035_GaokaoPolitics_2025各区模拟题_2025各区一模_2025顺义一模_2025北京顺义高三一模政治_教师版_.pdf",
        },
        "expected": 22,
    },
}

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
FORBIDDEN = ["固定分析流程", "FINAL_PASS", "终稿已通过", "最终版"]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]], list[dict[str, object]]]:
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


def expected_rows(group: str) -> list[dict[str, str]]:
    sources = GROUPS[group]["sources"]
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [row for row in rows if row.get("priority") == "P2" and row.get("source_id") in sources]


def key(row: dict[str, str]) -> tuple[str, str]:
    return row.get("question_id", ""), row.get("framework_node", "")


def load_jsonl(path: Path) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
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
            if obj.get("decision") not in ALLOWED_DECISIONS:
                issues.append({"kind": "patch_invalid_decision", "line": line_no, "question_id": obj.get("question_id", ""), "decision": obj.get("decision")})
    return issues, rows


def main() -> int:
    group = (sys.argv[1] if len(sys.argv) > 1 else "P2A").upper()
    if group not in GROUPS:
        raise SystemExit(f"unknown group: {group}")
    exp = expected_rows(group)
    exp_keys = Counter(key(row) for row in exp)
    exp_evidence = {key(row): row.get("evidence_level", "") for row in exp}
    required = [
        f"{group}_RECHECK_DECISIONS.csv",
        f"{group}_RECHECK_PATCHES.jsonl",
        f"{group}_SOURCE_EVIDENCE.md",
        f"{group}_RECHECK_ACCEPTANCE.md",
        f"{group}_PROGRESS.md",
    ]
    missing_files = [name for name in required if not (LANE / name).exists()]
    header, decisions, bad_width = read_csv(LANE / f"{group}_RECHECK_DECISIONS.csv")
    patch_issues, patches = load_jsonl(LANE / f"{group}_RECHECK_PATCHES.jsonl")
    issues: list[dict[str, object]] = []
    if missing_files:
        issues.append({"kind": "missing_required_files", "files": missing_files})
    if header and header != DECISION_FIELDS:
        issues.append({"kind": "decision_header_mismatch", "header": header})
    if bad_width:
        issues.append({"kind": "decision_bad_width", "rows": bad_width[:20]})
    if decisions and len(decisions) != GROUPS[group]["expected"]:
        issues.append({"kind": "decision_row_count_mismatch", "count": len(decisions), "expected": GROUPS[group]["expected"]})
    if patches and len(patches) != GROUPS[group]["expected"]:
        issues.append({"kind": "patch_row_count_mismatch", "count": len(patches), "expected": GROUPS[group]["expected"]})
    decision_keys = Counter(key(row) for row in decisions)
    patch_keys = Counter(key(row) for row in patches)
    if decisions and decision_keys != exp_keys:
        issues.append({"kind": "decision_key_mismatch", "missing": sorted(map(str, (exp_keys - decision_keys).elements())), "extra": sorted(map(str, (decision_keys - exp_keys).elements()))})
    if patches and patch_keys != exp_keys:
        issues.append({"kind": "patch_key_mismatch", "missing": sorted(map(str, (exp_keys - patch_keys).elements())), "extra": sorted(map(str, (patch_keys - exp_keys).elements()))})
    for i, row in enumerate(decisions, start=2):
        row_key = key(row)
        missing = [field for field in DECISION_FIELDS if not str(row.get(field, "")).strip()]
        if missing:
            issues.append({"kind": "decision_missing_fields", "line": i, "question_id": row.get("question_id", ""), "fields": missing})
        if row.get("priority") != "P2":
            issues.append({"kind": "decision_priority_not_p2", "line": i, "question_id": row.get("question_id", ""), "priority": row.get("priority")})
        if row.get("decision") not in ALLOWED_DECISIONS:
            issues.append({"kind": "decision_invalid", "line": i, "question_id": row.get("question_id", ""), "decision": row.get("decision")})
        if row.get("can_enter_fusion") not in {"yes", "no"}:
            issues.append({"kind": "decision_bad_can_enter", "line": i, "question_id": row.get("question_id", ""), "value": row.get("can_enter_fusion")})
        if row_key in exp_evidence and row.get("evidence_level") != exp_evidence[row_key]:
            issues.append({"kind": "decision_evidence_mismatch", "line": i, "question_id": row.get("question_id", ""), "got": row.get("evidence_level"), "expected": exp_evidence[row_key]})
    issues.extend(patch_issues)

    combined = "\n".join(
        (LANE / name).read_text(encoding="utf-8", errors="replace")
        for name in required
        if (LANE / name).exists()
    )
    hits = {token: combined.count(token) for token in FORBIDDEN}
    if any(hits.values()):
        issues.append({"kind": "forbidden_text_present", "hits": hits})
    if group == "P2A":
        by_qid = {row.get("question_id", ""): row for row in decisions}
        for qid in ["Q-2026东城一模-5", "Q-2026东城一模-7"]:
            row = by_qid.get(qid)
            if row and (row.get("decision") == "source_insufficient" or row.get("can_enter_fusion") != "yes"):
                issues.append({"kind": "dongcheng_yimo_answer_visible_but_blocked", "question_id": qid, "decision": row.get("decision"), "can_enter_fusion": row.get("can_enter_fusion")})

    summary = {
        "verdict": f"{group}_QA_OK_NOT_FINAL" if not issues else f"{group}_QA_FAIL",
        "group": group,
        "expected_rows": GROUPS[group]["expected"],
        "missing_files": missing_files,
        "decision_rows": len(decisions),
        "patch_rows": len(patches),
        "decision_counts": dict(Counter(row.get("decision", "") for row in decisions)),
        "evidence_counts": dict(Counter(row.get("evidence_level", "") for row in decisions)),
        "can_enter_fusion_counts": dict(Counter(row.get("can_enter_fusion", "") for row in decisions)),
        "issue_count": len(issues),
        "issues": issues[:120],
    }
    (LANE / f"{group}_QA.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        f"# {group} QA",
        "",
        f"Verdict: `{summary['verdict']}`",
        "",
        f"- decision rows: `{summary['decision_rows']}` / `{GROUPS[group]['expected']}`",
        f"- patch rows: `{summary['patch_rows']}` / `{GROUPS[group]['expected']}`",
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
        lines.extend(f"- `{issue['kind']}`: `{issue}`" for issue in issues[:80])
    else:
        lines.append("- none")
    (LANE / f"{group}_QA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
