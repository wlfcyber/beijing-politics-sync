#!/usr/bin/env python3
"""Generate Phase05 gate files required by GPT Batch03 verdict."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "05_coverage/phase04_control_base_status_after_batch03_cleaned.csv"
RAW_CHOICE = ROOT / "claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results.csv"
NORM_CHOICE = ROOT / "claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv"
FREEZE = ROOT / "05_coverage/phase04_batch03_cleaned_status_freeze.md"
COUNT_AUDIT = ROOT / "06_conflicts/phase04_batch03_choice_count_discrepancy_audit.md"
Q11_LOCK = ROOT / "06_conflicts/phase04_2024_xicheng_yimo_Q11_pairing_lock.md"
Q12Q13_LOCK = ROOT / "06_conflicts/phase04_2025_haidian_ermo_Q12_Q13_answer_locator_lock.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def get_answer_from_status(status: str) -> str:
    parts = status.split("_")
    for part in parts:
        if part in {"A", "B", "C", "D"}:
            return part
    return ""


def main() -> None:
    clean_rows = read_csv(CLEAN)
    ids = [r["canonical_question_id"] for r in clean_rows]
    dupes = sorted(k for k, v in Counter(ids).items() if v > 1)
    level_counts = Counter(r["phase04_level"] for r in clean_rows)
    student_bad = [r["canonical_question_id"] for r in clean_rows if not r["student稿_permission"].startswith("NO_STUDENT_DRAFT")]
    l1_rows = [r for r in clean_rows if r["phase04_level"].startswith("L1")]

    FREEZE.write_text(
        "\n".join(
            [
                "# Phase04 Batch03 Cleaned Status Freeze",
                "",
                "Status: `FROZEN_FOR_PHASE05_EVIDENCE_ARCHIVE`.",
                "",
                f"- source: `{CLEAN.relative_to(ROOT)}`",
                f"- total rows: {len(clean_rows)}",
                f"- L4_LOCKED_FOR_FUSION: {level_counts.get('L4_LOCKED_FOR_FUSION', 0)}",
                f"- L3_A_PLUS_B_TARGET_CONFIRMED: {level_counts.get('L3_A_PLUS_B_TARGET_CONFIRMED', 0)}",
                f"- L0_BLOCKED: {level_counts.get('L0_BLOCKED', 0)}",
                f"- L1 rows: {len(l1_rows)}",
                f"- duplicate canonical id: {len(dupes)}",
                f"- student-facing permission violations: {len(student_bad)}",
                "",
                "## Gate",
                "",
                "- Phase05 may use this table as the downstream control base.",
                "- This does not authorize student稿, Claude/Opus 成文化, Word/PDF, or final PASS.",
                "- L3 and L4 must remain separate in every Phase05 output.",
                "",
                "## Duplicate IDs",
                "",
                *(f"- `{d}`" for d in dupes),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    norm_rows = read_csv(NORM_CHOICE)
    report_implied = {
        "Q-2024朝阳二模-6": "marginal_not_counted_in_stale_summary",
        "Q-2025丰台期末-7": "marginal_not_counted_in_stale_summary",
        "Q-2026通州期末-9": "marginal_not_counted_in_stale_summary",
    }
    norm_by_id = {r["target_id"]: r for r in norm_rows}
    lines = [
        "# Phase04 Batch03 Choice Count Discrepancy Audit",
        "",
        "Status: `ROW_LEVEL_NORMALIZED_CSV_CONTROLS_MERGE`.",
        "",
        "- raw report summary count: `31 confirmed / 25 scope_out`.",
        "- normalized row-level CSV count: `34 confirmed / 22 scope_out`.",
        f"- raw CSV: `{RAW_CHOICE.relative_to(ROOT)}`",
        f"- normalized CSV: `{NORM_CHOICE.relative_to(ROOT)}`",
        "- merge source: normalized row-level CSV.",
        "",
        "Reason: the report's top-level summary and closing note were stale hand counts. The report's own per-suite table and compact 56-row table agree with the normalized row-level CSV at `34 / 22`. Row-level `target_id` records override the stale summary.",
        "",
        "## Three-Row Delta Review",
        "",
        "| question_id | raw_report_status | normalized_row_status | cause_of_difference | source_locator | answer_locator | final_merge_status |",
        "|---|---|---|---|---|---|---|",
    ]
    for qid, cause in report_implied.items():
        row = norm_by_id[qid]
        answer = get_answer_from_status(row.get("answer_status", ""))
        source = row.get("source_evidence", "")
        lines.append(
            "| "
            + " | ".join(
                [
                    qid,
                    "stale_summary_effectively_not_in_confirmed_31",
                    f"{row['laneB_result']} / {row['section_scope']} / answer={answer}",
                    cause,
                    source,
                    row.get("answer_status", ""),
                    "kept_as_L3_or_cross_marginal_evidence_only; no student draft",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Guard",
            "",
            "- These rows are not student-facing examples.",
            "- If Phase05 cannot preserve locator, answer source, and marginal/cross risk note for any of the three rows, that row must be downgraded before archive backcheck passes.",
        ]
    )
    COUNT_AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    q11 = next(r for r in clean_rows if r["canonical_question_id"] == "Q-2024西城一模-11")
    Q11_LOCK.write_text(
        "\n".join(
            [
                "# 2024西城一模 Q11 Pairing Lock",
                "",
                "Status: `PAIRING_LOCK_ACTIVE`.",
                "",
                "- question_id: `Q-2024西城一模-11`",
                "- correct answer: `B`",
                "- correct pairing: `B=①③`",
                "- A=①②",
                "- B=①③",
                "- C=②④",
                "- D=③④",
                "- Codex A prior wrong pairing: `B=①④`",
                "- wrong pairing must not propagate.",
                "",
                f"- visual/options status: `{q11['visual_status']}`",
                f"- answer source: `{q11['answer_pairing_status']}`",
                f"- risk note: `{q11['blocker_reason']}`",
                "",
                "Any Phase05 or later file containing `B=①④` for this row fails the gate and must be repaired before continuing.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    rows = [r for r in clean_rows if r["canonical_question_id"] in {"Q-2025海淀二模-12", "Q-2025海淀二模-13"}]
    q_lines = [
        "# 2025海淀二模 Q12/Q13 Answer Locator Lock",
        "",
        "Status: `ANSWER_LOCATOR_LOCK_ACTIVE`.",
        "",
        "| question_id | full_options_locator | answer_key_locator | answer | LaneB_confirmation | fusion_status |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        answer = get_answer_from_status(row.get("answer_pairing_status", ""))
        q_lines.append(
            "| "
            + " | ".join(
                [
                    row["canonical_question_id"],
                    row["stable_locator"],
                    row["answer_pairing_status"],
                    answer,
                    row["B_status"],
                    row["fusion_status"],
                ]
            )
            + " |"
        )
    q_lines.extend(
        [
            "",
            "If either row loses a verifiable answer locator in Phase05, downgrade it from L3 before archive backcheck passes.",
        ]
    )
    Q12Q13_LOCK.write_text("\n".join(q_lines) + "\n", encoding="utf-8")

    print(f"wrote {FREEZE}")
    print(f"wrote {COUNT_AUDIT}")
    print(f"wrote {Q11_LOCK}")
    print(f"wrote {Q12Q13_LOCK}")


if __name__ == "__main__":
    main()
