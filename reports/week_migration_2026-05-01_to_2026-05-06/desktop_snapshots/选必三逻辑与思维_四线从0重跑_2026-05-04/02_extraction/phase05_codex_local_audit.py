#!/usr/bin/env python3
"""Codex A local hard audit for Phase05 evidence archives."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "codex_lane/phase05_local_audit"
AUDIT_CSV = OUT_DIR / "phase05_codexA_local_audit.csv"
AUDIT_MD = OUT_DIR / "phase05_codexA_local_audit.md"


def read_csv(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def add(rows: list[dict[str, str]], check_id: str, scope: str, result: bool, details: str, severity: str = "P1") -> None:
    rows.append(
        {
            "check_id": check_id,
            "scope": scope,
            "result": "PASS" if result else "FAIL",
            "severity": "INFO" if result else severity,
            "details": details,
        }
    )


def main() -> None:
    pool = read_csv("05_coverage/phase05_evidence_pool_74.csv")
    thinking = read_csv("05_coverage/phase05_thinking_signal_archive.csv")
    reasoning = read_csv("05_coverage/phase05_reasoning_typology_archive.csv")
    cross = read_csv("05_coverage/phase05_cross_question_split_matrix.csv")
    control = read_csv("05_coverage/phase04_control_base_status_after_batch03_cleaned.csv")
    rows: list[dict[str, str]] = []

    add(rows, "A01", "evidence_pool", len(pool) == 74, f"data_rows={len(pool)}")
    add(rows, "A02", "thinking_archive", len(thinking) == 36, f"data_rows={len(thinking)}")
    add(rows, "A03", "reasoning_archive", len(reasoning) == 51, f"data_rows={len(reasoning)}")
    add(rows, "A04", "cross_archive", len(cross) == 13, f"data_rows={len(cross)}")

    control_counts = Counter(r["phase04_level"] for r in control)
    expected_control = len(control) == 362 and control_counts["L4_LOCKED_FOR_FUSION"] == 4 and control_counts["L3_A_PLUS_B_TARGET_CONFIRMED"] == 70 and control_counts["L0_BLOCKED"] == 288
    add(rows, "A05", "control_freeze", expected_control, f"rows={len(control)} counts={dict(control_counts)}")

    ids = [r["question_id"] for r in pool]
    add(rows, "A06", "evidence_pool", len(ids) == len(set(ids)), f"duplicates={len(ids) - len(set(ids))}")

    required = ["question_id", "suite_id", "source_locator", "answer_locator", "status", "student_permission"]
    missing_required = [
        r["question_id"]
        for r in pool
        if any(not (r.get(col) or "").strip() for col in required)
    ]
    add(rows, "A07", "evidence_pool", not missing_required, f"missing_required={missing_required[:20]}", "P0")

    student_bad = [r["question_id"] for r in pool if not r["student_permission"].startswith("NO_STUDENT_DRAFT")]
    add(rows, "A08", "student_permission", not student_bad, f"violations={student_bad}", "P0")

    l4_expected = {"Q-2025海淀二模-20", "Q-2025西城二模-16-2", "Q-2025西城二模-16-3", "Q-2026丰台一模-18-2"}
    l4_actual = {r["question_id"] for r in pool if r["status"] == "L4_LOCKED_FOR_FUSION"}
    add(rows, "A09", "L4_lock", l4_actual == l4_expected, f"actual={sorted(l4_actual)} expected={sorted(l4_expected)}", "P0")

    q11_text = "\n".join(
        str(r)
        for table in [pool, thinking, reasoning, cross]
        for r in table
        if r.get("question_id") == "Q-2024西城一模-11"
    )
    add(rows, "A10", "Q11_lock", "B=①④" not in q11_text and "B=①③" in q11_text, "Q11 wrong-pairing string absent and B=①③ retained", "P0")

    q12 = next((r for r in pool if r["question_id"] == "Q-2025海淀二模-12"), None)
    q13 = next((r for r in pool if r["question_id"] == "Q-2025海淀二模-13"), None)
    q12_ok = bool(q12 and "page9" in q12["source_locator"] and "render_008_page_04" in q12["source_locator"] and "D" in q12["answer_locator"])
    q13_ok = bool(q13 and "page9" in q13["source_locator"] and "render_008_page_04" in q13["source_locator"] and "C" in q13["answer_locator"])
    add(rows, "A11", "Q12_Q13_locator", q12_ok and q13_ok, f"Q12={q12}; Q13={q13}", "P0")

    cross_ids = {r["question_id"] for r in cross}
    thinking_ids = {r["question_id"] for r in thinking}
    reasoning_ids = {r["question_id"] for r in reasoning}
    cross_missing = sorted(q for q in cross_ids if q not in thinking_ids or q not in reasoning_ids)
    add(rows, "A12", "cross_double_mount", not cross_missing, f"missing_double_mount={cross_missing}", "P0")

    l0_summary = (ROOT / "05_coverage/phase05_L0_blocker_reason_summary.md").read_text(encoding="utf-8")
    add(rows, "A13", "L0_retention", "- L0 rows: 288" in l0_summary, "L0 summary reports 288 rows", "P0")

    phase05_text = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in [
        "05_coverage/phase05_evidence_pool_74.md",
        "05_coverage/phase05_thinking_signal_archive.md",
        "05_coverage/phase05_reasoning_typology_archive.md",
        "05_coverage/phase05_reasoning_same_type_index.md",
        "06_conflicts/phase05_archive_backcheck_report.md",
    ])
    forbidden_authorize = ["授权学生稿", "允许学生稿", "可以进入学生稿", "final PASS authorized", "DOCX PASS", "Word/PDF PASS"]
    add(rows, "A14", "no_final_authorization", not any(x in phase05_text for x in forbidden_authorize), "no positive final/student/Word authorization phrase found", "P0")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_CSV.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["check_id", "scope", "result", "severity", "details"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    fail_rows = [r for r in rows if r["result"] != "PASS"]
    lines = [
        "# Phase05 Codex A Local Audit",
        "",
        f"Verdict: `{'PASS_LOCAL_HARD_AUDIT' if not fail_rows else 'FAIL_REPAIR_REQUIRED'}`",
        "",
        f"- checks: {len(rows)}",
        f"- failures: {len(fail_rows)}",
        "",
        "This is an internal Phase05 evidence archive audit only. It does not authorize student稿, Claude/Opus 成文化, Word/PDF, or final PASS.",
        "",
        "## Checks",
        "",
    ]
    for row in rows:
        lines.append(f"- {row['result']}: {row['check_id']} {row['scope']} - {row['details']}")
    AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(AUDIT_MD)


if __name__ == "__main__":
    main()
