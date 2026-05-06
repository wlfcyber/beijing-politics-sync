#!/usr/bin/env python3
"""Create a non-promotional source-repair priority queue from Phase10.5 inventory."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "09_student_draft" / "phase10_5_pre_gpt_expansion_gap_inventory.csv"
OUT_CSV = ROOT / "09_student_draft" / "phase10_5_source_repair_priority_queue.csv"
OUT_MD = ROOT / "09_student_draft" / "phase10_5_source_repair_priority_queue.md"
OUT_VERIFY = ROOT / "08_review" / "phase10_5_source_repair_priority_verification.md"

PROTECTED_HOLD_IDS = {
    # GPT and Governor hard-lock rows: may appear as index-only or absent, but no answer
    # expansion before explicit source repair and later authorization.
    "Q-2024西城一模-11",
    "Q-2025海淀二模-12",
    "Q-2025海淀二模-13",
    "Q-2026顺义一模-3",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def ref_count(row: dict[str, str]) -> int:
    refs = row.get("referenced_by_phase10_body_ids", "")
    if not refs:
        return 0
    return len([r for r in refs.split("；") if r.strip()])


def priority(row: dict[str, str]) -> tuple[str, str]:
    qid = row["question_id"]
    body_status = row["phase10_body_status"]
    action = row["recommended_next_action"]
    qtype = row["question_type"]
    module = row["module"]
    refs = ref_count(row)

    if qid in PROTECTED_HOLD_IDS:
        return (
            "P0_PROTECTED_HOLD_DO_NOT_EXPAND",
            "hard-lock row; keep absent or index-only until explicit source repair plus later GPT/Governor authorization",
        )
    if body_status == "same_type_index_only" and refs >= 3:
        return (
            "P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER",
            "already supports several Phase10 same-type links; repair source before any body expansion",
        )
    if body_status == "same_type_index_only":
        return (
            "P2_REPAIR_INDEX_CLUSTER",
            "already visible as same-type index; repair before deciding whether it deserves body treatment",
        )
    if action == "source_repair_required_before_body_expansion" and module in {"思维", "交叉"}:
        return (
            "P3_REPAIR_THINKING_OR_CROSS_SOURCE",
            "thought/cross row absent from body; source-answer locator must be repaired first",
        )
    if qtype == "主观题":
        return (
            "P4_RECHECK_SUBJECTIVE_REASONING_FORM",
            "subjective row may carry teachable structure, but reasoning form must be rechecked before body use",
        )
    return (
        "P5_RECHECK_CHOICE_REASONING_FORM",
        "choice row needs reasoning-form or answer-location recheck before any expansion",
    )


def main() -> None:
    rows = [r for r in read_csv(INVENTORY) if r["phase10_body_status"] != "in_phase10_body"]
    out_rows: list[dict[str, str]] = []
    for row in rows:
        p, reason = priority(row)
        out_rows.append(
            {
                "priority": p,
                "question_id": row["question_id"],
                "visible_title": row["visible_title"],
                "module": row["module"],
                "question_type": row["question_type"],
                "phase10_body_status": row["phase10_body_status"],
                "phase07_input_permission": row["phase07_input_permission"],
                "ref_count": str(ref_count(row)),
                "referenced_by_phase10_body_ids": row["referenced_by_phase10_body_ids"],
                "repair_reason": reason,
                "source_locator": row["source_locator"],
                "answer_locator": row["answer_locator"],
                "hold_reason": row["hold_reason"],
                "risk_note": row["risk_note"],
            }
        )

    order = {
        "P0_PROTECTED_HOLD_DO_NOT_EXPAND": 0,
        "P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER": 1,
        "P2_REPAIR_INDEX_CLUSTER": 2,
        "P3_REPAIR_THINKING_OR_CROSS_SOURCE": 3,
        "P4_RECHECK_SUBJECTIVE_REASONING_FORM": 4,
        "P5_RECHECK_CHOICE_REASONING_FORM": 5,
    }
    out_rows.sort(
        key=lambda r: (
            order[r["priority"]],
            -int(r["ref_count"]),
            r["module"],
            r["visible_title"],
        )
    )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    counts = Counter(r["priority"] for r in out_rows)
    lines = [
        "# Phase10.5 Source Repair Priority Queue",
        "",
        "Status: `LOCAL_PREPARATION_ONLY_NO_PHASE_PROMOTION`",
        "",
        "This queue does not authorize expansion. It orders the 45 non-body rows so later GPT/Governor-authorized repair can start from the highest-risk/highest-value rows.",
        "",
        "## Counts",
        "",
    ]
    for key in sorted(counts, key=order.get):
        lines.append(f"- `{key}`: {counts[key]}")

    lines.extend(["", "## Queue", ""])
    current = None
    for row in out_rows:
        if row["priority"] != current:
            current = row["priority"]
            lines.extend(["", f"### {current}", ""])
        refs = row["referenced_by_phase10_body_ids"] or "none"
        lines.append(
            f"- `{row['question_id']}` {row['visible_title']} | {row['module']} | {row['question_type']} | "
            f"refs={row['ref_count']} ({refs}) | {row['repair_reason']}"
        )

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    protected_missing = sorted(PROTECTED_HOLD_IDS - {r["question_id"] for r in out_rows})
    verify = [
        "# Phase10.5 Source Repair Priority Verification",
        "",
        "Verdict: `PASS_LOCAL_PRIORITY_QUEUE_NO_PHASE_PROMOTION`",
        "",
        f"- non-body rows read: {len(rows)}",
        f"- queue rows written: {len(out_rows)}",
        f"- protected hard-lock rows present: {not protected_missing}",
        f"- protected missing ids: {'；'.join(protected_missing) if protected_missing else 'none'}",
        "- GPT Phase10 gate remains blocked until real web retry succeeds.",
        "- Word/PDF/final PASS remain blocked.",
    ]
    OUT_VERIFY.write_text("\n".join(verify) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
