#!/usr/bin/env python3
"""Create downstream-cleaned Phase04 control table after Batch03 queue-meta fixes."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "05_coverage" / "phase04_control_base_status_after_batch03.csv"
OUT = ROOT / "05_coverage" / "phase04_control_base_status_after_batch03_cleaned.csv"
DECISIONS_CSV = ROOT / "06_conflicts" / "phase04_batch03_queue_meta_cleanup_decisions.csv"
DECISIONS_MD = ROOT / "06_conflicts" / "phase04_batch03_queue_meta_cleanup_decisions.md"


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([{k: row.get(k, "") for k in fieldnames} for row in rows])


def main() -> None:
    fieldnames, rows = read_rows(IN)
    out_rows: list[dict[str, str]] = []
    decisions: list[dict[str, str]] = []

    skip_ids = {"Q-2026东城期末-16-1", "Q-2026东城期末-16-2"}
    q16_source_rows = {
        row["canonical_question_id"]: row
        for row in rows
        if row.get("canonical_question_id") in {"Q-2026东城期末-16-1", "Q-2026东城期末-16-2"}
    }

    for row in rows:
        qid = row.get("canonical_question_id", "")
        if qid == "Q-2026东城期末-16":
            cleaned = dict(row)
            duplicate = q16_source_rows.get("Q-2026东城期末-16-1") or q16_source_rows.get("Q-2026东城期末-16-2") or {}
            cleaned["B_status"] = "B_TARGET_SCOPE_OUT"
            cleaned["fusion_status"] = "blocked_scope_out_after_batch03_cleanup"
            cleaned["phase04_level"] = "L0_BLOCKED"
            cleaned["verification_level"] = "C-boundary"
            cleaned["answer_pairing_status"] = duplicate.get("answer_pairing_status", cleaned.get("answer_pairing_status", ""))
            cleaned["rubric_pairing_status"] = duplicate.get("rubric_pairing_status", cleaned.get("rubric_pairing_status", ""))
            cleaned["visual_status"] = duplicate.get("visual_status", cleaned.get("visual_status", ""))
            cleaned["student稿_permission"] = "NO_STUDENT_DRAFT"
            cleaned["blocker_reason"] = "queue_split_error_cleaned: Q16原卷与细则均为单题；哲学与文化，非选必三逻辑与思维"
            cleaned["gap_priority"] = "P0_BOUNDARY_CLOSED"
            cleaned["gap_action"] = "existing Q16 retained and enriched with Opus split-error evidence; Q16(1)/Q16(2) removed"
            cleaned["excerpt"] = (
                cleaned.get("excerpt", "")[:700]
                + " || Cleaned duplicate evidence: "
                + duplicate.get("excerpt", "")[:450]
            )[:1200]
            out_rows.append(cleaned)
            decisions.append(
                {
                    "decision_id": "B03-CLEAN-01A",
                    "target_id": "Q-2026东城期末-16",
                    "action": "retain_existing_Q16_and_enrich_boundary_decision",
                    "status": "done_in_cleaned_table",
                    "evidence": "Opus Lane B blockers/conflicts: paper 044 and rubric 044 both show Q16 is one 7-point philosophy/culture item.",
                    "downstream_effect": "single canonical Q16 retained; duplicate split rows removed; no student draft permission",
                }
            )
            continue

        if qid in skip_ids:
            decisions.append(
                {
                    "decision_id": "B03-CLEAN-01B" if qid.endswith("-1") else "B03-CLEAN-01C",
                    "target_id": qid,
                    "action": "collapse_duplicate_into_Q-2026东城期末-16",
                    "status": "removed_from_cleaned_table_only",
                    "evidence": "Opus Lane B found original paper/rubric contain one Q16, not Q16(1)/Q16(2). Both duplicate rows are scope_out.",
                    "downstream_effect": "prevents duplicate counting; raw after_batch03 table preserved unchanged",
                }
            )
            continue

        out_rows.append(row)

    tracked = {row.get("canonical_question_id"): row for row in rows}
    if tracked.get("Q-2025西城二模-16-2", {}).get("phase04_level") == "L4_LOCKED_FOR_FUSION":
        decisions.append(
            {
                "decision_id": "B03-CLEAN-02",
                "target_id": "Q-2025西城二模-16-2",
                "action": "no_new_row_needed",
                "status": "already_preserved_from_batch01",
                "evidence": "Control table after Batch03 retains Q-2025西城二模-16-2 as L4_LOCKED_FOR_FUSION, B_TARGET_CONFIRMED, A-formal.",
                "downstream_effect": "Opus Batch03 queue-omission warning resolved as batch03-local only; do not duplicate the row",
            }
        )

    write_rows(OUT, fieldnames, out_rows)

    with DECISIONS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(decisions[0]))
        writer.writeheader()
        writer.writerows(decisions)

    raw_counts = Counter(row.get("phase04_level", "") for row in rows)
    clean_counts = Counter(row.get("phase04_level", "") for row in out_rows)
    lines = [
        "# Phase04 Batch03 Queue-Meta Cleanup Decisions",
        "",
        "Status: `QUEUE_META_CLEANED_FOR_DOWNSTREAM_NO_STUDENT_DRAFT`.",
        "",
        f"- raw_control: `{IN.relative_to(ROOT)}` ({len(rows)} rows)",
        f"- cleaned_control: `{OUT.relative_to(ROOT)}` ({len(out_rows)} rows)",
        f"- decisions_csv: `{DECISIONS_CSV.relative_to(ROOT)}`",
        "",
        "## Decisions",
        "",
    ]
    for d in decisions:
        lines.append(f"- `{d['decision_id']}` `{d['target_id']}`: {d['action']} -> {d['status']}. {d['downstream_effect']}")
    lines.extend(["", "## Phase04 Level Counts", ""])
    lines.append("Raw after Batch03:")
    lines.extend(f"- {k}: {v}" for k, v in raw_counts.items())
    lines.append("")
    lines.append("Cleaned downstream table:")
    lines.extend(f"- {k}: {v}" for k, v in clean_counts.items())
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "- This is a queue-meta cleanup only.",
            "- No content judgment was promoted to student稿.",
            "- The raw Batch03 control table is preserved; downstream fusion should use the cleaned table.",
        ]
    )
    DECISIONS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {OUT}")
    print(f"wrote {DECISIONS_CSV}")
    print(f"wrote {DECISIONS_MD}")
    print(f"raw_rows={len(rows)} cleaned_rows={len(out_rows)}")


if __name__ == "__main__":
    main()
