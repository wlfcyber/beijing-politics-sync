# Governor Gate Check v12.2

Status: `framework_baseline_gate_pass_not_final_document`

Date: 2026-05-22

## Gate Table

| gate | result | evidence |
|---|---|---|
| source pack exists | pass | `codex_source_checks/*`, `coverage_check_v12_2_council.csv` |
| 42/42 core mapping checked | pass | `codex_source_checks/coverage_delta_after_source_check_20260522.md` |
| local source adjudication complete | pass | `codex_source_checks/pending_source_check_20260522.md` |
| Claude Opus 4.7 Round 03 real call | pass | `model_outputs/claude_round03_source_check_review_key_capture.md` |
| GPT Round 03 real call | pass with model-label caution | `model_outputs/gpt_round03_source_check_review.md` |
| Codex Round 03 adjudication | pass for framework baseline | `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` |
| student-facing framework written | pass for framework baseline | `final_framework_candidate/FRAMEWORK_BASELINE_v12_2_SOURCE_CHECKED.md` |
| final baodian / DOCX/PDF | fail | final teaching document not produced in this step |

## Governor Verdict

Current allowed label:

`complete_source_checked_framework_baseline_gpt_claude_reviewed`

Forbidden labels:

- final baodian
- DOCX/PDF final delivery
- TASK_COMPLETE

## Required Before Final Document Delivery

1. Decide whether next-backfill candidates are frozen or moved into a new evidence pass.
2. Convert this framework baseline into the requested baodian/classroom document.
3. Run final document governor review.
4. Only then claim final baodian, DOCX/PDF delivery, or TASK_COMPLETE.
