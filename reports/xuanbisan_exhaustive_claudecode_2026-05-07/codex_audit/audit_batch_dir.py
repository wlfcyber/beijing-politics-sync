# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
AUDIT_DIR = RUN_DIR / "codex_audit"
TERMINAL_DECISIONS = {"入正文", "同类索引", "blocked", "excluded"}
REQUIRED_JSONL_FIELDS = {
    "question_id",
    "type",
    "framework_node",
    "material_signal",
    "trigger_logic",
    "answer_sentence",
    "evidence_level",
    "needs_codex_recheck",
    "source_batch",
}
VALID_EVIDENCE_LEVELS = {"A-formal", "A-support", "B-choice-signal", "C-boundary", "missing"}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(RUN_DIR))
    except ValueError:
        return str(path)


def csv_width_report(path: Path) -> dict:
    if not path.exists():
        return {"exists": False}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return {"exists": True, "header_width": 0, "data_rows": 0, "bad_width_rows": []}
    width = len(rows[0])
    bad = [
        {"line": idx, "field_count": len(row), "head": row[: min(len(row), 10)]}
        for idx, row in enumerate(rows[1:], start=2)
        if len(row) != width
    ]
    return {
        "exists": True,
        "header_width": width,
        "data_rows": len(rows) - 1,
        "bad_width_rows": bad,
    }


def read_dict_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def audit_jsonl(path: Path) -> dict:
    if not path.exists():
        return {"exists": False}
    bad_json = 0
    missing_required = 0
    invalid_evidence_level = 0
    counts: Counter[str] = Counter()
    rows = 0
    samples = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            rows += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                bad_json += 1
                if len(samples) < 5:
                    samples.append({"line": line_no, "error": str(exc), "text": line[:160]})
                continue
            counts[str(obj.get("type", ""))] += 1
            missing = sorted(k for k in REQUIRED_JSONL_FIELDS if not str(obj.get(k, "")).strip())
            if missing:
                missing_required += len(missing)
                if len(samples) < 5:
                    samples.append({"line": line_no, "missing": missing, "question_id": obj.get("question_id", "")})
            evidence_level = str(obj.get("evidence_level", "")).strip()
            if evidence_level and evidence_level not in VALID_EVIDENCE_LEVELS:
                invalid_evidence_level += 1
                if len(samples) < 5:
                    samples.append(
                        {
                            "line": line_no,
                            "invalid_evidence_level": evidence_level[:120],
                            "question_id": obj.get("question_id", ""),
                        }
                    )
    return {
        "exists": True,
        "rows": rows,
        "bad_json": bad_json,
        "missing_required_fields": missing_required,
        "invalid_evidence_level": invalid_evidence_level,
        "type_counts": dict(counts),
        "samples": samples,
    }


def find_entries(batch_dir: Path) -> list[Path]:
    entries_dir = batch_dir / "entries"
    if not entries_dir.exists():
        return []
    return sorted(entries_dir.glob("*.jsonl"))


def contains_forbidden_phrase(paths: list[Path]) -> list[str]:
    hits = []
    for path in paths:
        if not path.exists() or path.is_dir():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "固定分析流程" in text:
            hits.append(rel(path))
    return hits


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python audit_batch_dir.py <batch_dir>", file=sys.stderr)
        return 2
    batch_dir = Path(sys.argv[1]).resolve()
    name = batch_dir.name

    required = [
        "PROGRESS.md",
        "QUESTION_DECISIONS.csv",
        "MAIN_THINKING_LEDGER.csv",
        "CHOICE_TRAP_LEDGER.csv",
        "FRAMEWORK_NODE_MATRIX.csv",
        "FRAMEWORK_NODE_MATRIX_SUMMARY.csv",
        "BLOCKED_OR_BOUNDARY.md",
    ]
    missing = [item for item in required if not (batch_dir / item).exists()]
    acceptance_files = sorted(p for p in batch_dir.glob("*ACCEPTANCE*.md") if not p.name.startswith("SUPERVISOR_PATCH"))
    suite_reports = sorted((batch_dir / "suite_reports").glob("*.md")) if (batch_dir / "suite_reports").exists() else []
    entry_files = find_entries(batch_dir)

    qd = batch_dir / "QUESTION_DECISIONS.csv"
    qd_width = csv_width_report(qd)
    qd_rows = read_dict_rows(qd) if not qd_width.get("bad_width_rows") else []
    decision_counts = Counter(r.get("claudecode_decision", "") for r in qd_rows)
    invalid_decisions = [
        r.get("question_id", "")
        for r in qd_rows
        if r.get("claudecode_decision", "") not in TERMINAL_DECISIONS
    ]
    invalid_recheck = [
        r.get("question_id", "")
        for r in qd_rows
        if r.get("needs_codex_recheck", "") not in {"yes", "no"}
    ]

    jsonl_reports = {rel(path): audit_jsonl(path) for path in entry_files}
    # Forbidden student-facing phrasing matters in material that can flow into
    # the student artifact. Boundary and acceptance files are audit/control
    # documents and may legitimately quote the forbidden list as a check.
    student_flow_paths = [
        batch_dir / "MAIN_THINKING_LEDGER.csv",
        batch_dir / "CHOICE_TRAP_LEDGER.csv",
        batch_dir / "FRAMEWORK_NODE_MATRIX.csv",
    ] + entry_files + suite_reports
    forbidden_hits = contains_forbidden_phrase(student_flow_paths)

    hard_failures = []
    if missing:
        hard_failures.append("missing_required_files")
    if not acceptance_files:
        hard_failures.append("missing_acceptance_file")
    if not suite_reports:
        hard_failures.append("missing_suite_reports")
    if not entry_files:
        hard_failures.append("missing_entries_jsonl")
    if qd_width.get("bad_width_rows"):
        hard_failures.append("invalid_csv_width")
    if invalid_decisions:
        hard_failures.append("invalid_terminal_decisions")
    if invalid_recheck:
        hard_failures.append("invalid_needs_codex_recheck")
    for report in jsonl_reports.values():
        if report.get("bad_json") or report.get("missing_required_fields"):
            hard_failures.append("invalid_jsonl_schema")
            break
    for report in jsonl_reports.values():
        if report.get("invalid_evidence_level"):
            hard_failures.append("invalid_jsonl_evidence_level")
            break
    if forbidden_hits:
        hard_failures.append("forbidden_student_phrase")

    verdict = "BATCH_QA_FAIL" if hard_failures else "BATCH_QA_STRUCTURALLY_OK_NOT_FINAL"
    summary = {
        "batch_dir": str(batch_dir),
        "verdict": verdict,
        "hard_failures": sorted(set(hard_failures)),
        "missing_required_files": missing,
        "acceptance_files": [rel(p) for p in acceptance_files],
        "suite_report_count": len(suite_reports),
        "entry_jsonl_files": list(jsonl_reports),
        "question_decisions_csv": qd_width,
        "decision_counts": dict(decision_counts),
        "invalid_decision_qids": invalid_decisions[:50],
        "invalid_needs_codex_recheck_qids": invalid_recheck[:50],
        "jsonl_reports": jsonl_reports,
        "forbidden_phrase_hits": forbidden_hits,
    }

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    (AUDIT_DIR / f"{name}_qa_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        f"# Batch QA - {name}",
        "",
        f"Verdict: `{verdict}`",
        "",
        "## Hard failures",
        "",
    ]
    if hard_failures:
        for item in sorted(set(hard_failures)):
            lines.append(f"- `{item}`")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Required files",
            "",
            f"- missing: {', '.join(missing) if missing else 'none'}",
            f"- suite_reports: {len(suite_reports)}",
            f"- entries jsonl: {len(entry_files)}",
            f"- acceptance files: {len(acceptance_files)}",
            "",
            "## QUESTION_DECISIONS.csv",
            "",
            f"- data rows: {qd_width.get('data_rows', 0)}",
            f"- bad width rows: {len(qd_width.get('bad_width_rows', []))}",
            f"- decision counts: {dict(decision_counts)}",
            f"- invalid needs_codex_recheck rows: {len(invalid_recheck)}",
            "",
            "## JSONL",
            "",
        ]
    )
    if jsonl_reports:
        for path, report in jsonl_reports.items():
            lines.append(f"- `{path}`: rows={report.get('rows', 0)}, bad_json={report.get('bad_json', 0)}, missing_required={report.get('missing_required_fields', 0)}, invalid_evidence_level={report.get('invalid_evidence_level', 0)}, types={report.get('type_counts', {})}")
    else:
        lines.append("- none")
    lines.extend(["", "## Forbidden Phrase Hits", ""])
    if forbidden_hits:
        for hit in forbidden_hits:
            lines.append(f"- `{hit}`")
    else:
        lines.append("- none")
    lines.extend(["", "## Note", "", "- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF."])
    (AUDIT_DIR / f"{name}_qa.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if hard_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
