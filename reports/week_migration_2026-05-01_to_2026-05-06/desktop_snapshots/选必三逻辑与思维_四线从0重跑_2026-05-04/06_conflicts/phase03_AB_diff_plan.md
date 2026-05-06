# Phase 03 A/B Diff Plan

Status: scaffold prepared while ClaudeCode Lane B is running. Do not execute final diff until Lane B files exist.

## Required Lane A Inputs

- `05_coverage/phase03_question_coverage_matrix.csv`
- `05_coverage/phase03_thinking_signal_chain_matrix.csv`
- `05_coverage/phase03_reasoning_question_attachment_matrix.csv`
- `05_coverage/phase03_blocked_questions.csv`
- `02_extraction/blank_pdf_visual_inventory_codexA.md`

## Required Lane B Inputs

- `claudecode_lane/phase03_laneB_question_coverage_matrix.csv`
- `claudecode_lane/phase03_laneB_thinking_signal_candidates.csv`
- `claudecode_lane/phase03_laneB_reasoning_attachment.csv`
- `claudecode_lane/phase03_laneB_visual_blockers.md`
- `claudecode_lane/phase03_laneB_missing_and_conflicts.md`
- `04_suite_reports/claudecode_suite_reports/phase03_laneB_full_scan_report.md`

## Diff Checks

1. Suite coverage: every Lane A suite must exist in Lane B, and vice versa.
2. Blank-text PDFs: `2025海淀二模` and `2026丰台一模` must be either independently visually inventoried by Lane B or remain hard blockers.
3. Hard samples: HS01-HS05 must preserve the Phase 02 fusion decisions; HS02 must not be upgraded into student content without independent visual confirmation.
4. 思维部分: every candidate must carry material signal, possible method, answer action, source locator, evidence level, and student稿 eligibility.
5. 推理部分: every candidate must carry typology, logical form, rule slogan, valid/invalid pattern or trap, and same-type grouping readiness.
6. Choice questions: option completeness blockers must remain until all four options and answer key are recovered.
7. Boundary rows: non-选必三 or non-current-section content must stay visible as boundary/blocked rows, not disappear.

## Promotion Rule

Only rows with source locator, paired paper/answer/rubric evidence where required, no visual blocker, and no A/B conflict may be promoted to fusion. Everything else stays in blocked/missing/conflict.
