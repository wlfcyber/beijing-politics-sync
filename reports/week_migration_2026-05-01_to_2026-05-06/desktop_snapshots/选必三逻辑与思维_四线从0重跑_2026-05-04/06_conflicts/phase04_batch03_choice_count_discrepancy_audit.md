# Phase04 Batch03 Choice Count Discrepancy Audit

Status: `ROW_LEVEL_NORMALIZED_CSV_CONTROLS_MERGE`.

- raw report summary count: `31 confirmed / 25 scope_out`.
- normalized row-level CSV count: `34 confirmed / 22 scope_out`.
- raw CSV: `claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results.csv`
- normalized CSV: `claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv`
- merge source: normalized row-level CSV.

Reason: the report's top-level summary and closing note were stale hand counts. The report's own per-suite table and compact 56-row table agree with the normalized row-level CSV at `34 / 22`. Row-level `target_id` records override the stale summary.

## Three-Row Delta Review

| question_id | raw_report_status | normalized_row_status | cause_of_difference | source_locator | answer_locator | final_merge_status |
|---|---|---|---|---|---|---|
| Q-2024朝阳二模-6 | stale_summary_effectively_not_in_confirmed_31 | B_TARGET_CONFIRMED / 交叉 / answer=C | marginal_not_counted_in_stale_summary | 023_细则::Q6=C | answer_confirmed_C_from_023_rubric | kept_as_L3_or_cross_marginal_evidence_only; no student draft |
| Q-2025丰台期末-7 | stale_summary_effectively_not_in_confirmed_31 | B_TARGET_CONFIRMED / 交叉 / answer=C | marginal_not_counted_in_stale_summary | 040试卷::Q7=C | answer_confirmed_C_from_040_paper | kept_as_L3_or_cross_marginal_evidence_only; no student draft |
| Q-2026通州期末-9 | stale_summary_effectively_not_in_confirmed_31 | B_TARGET_CONFIRMED / 交叉 / answer=D | marginal_not_counted_in_stale_summary | 006试卷::Q9=D | answer_confirmed_D_from_006_paper | kept_as_L3_or_cross_marginal_evidence_only; no student draft |

## Guard

- These rows are not student-facing examples.
- If Phase05 cannot preserve locator, answer source, and marginal/cross risk note for any of the three rows, that row must be downgraded before archive backcheck passes.
