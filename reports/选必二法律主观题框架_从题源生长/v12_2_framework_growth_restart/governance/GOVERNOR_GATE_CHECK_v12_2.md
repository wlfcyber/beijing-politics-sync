# Governor Gate Check v12.2

Status: `not_final_pass`

Date: 2026-05-22

## Gate Table

| gate | result | evidence |
|---|---|---|
| source pack exists | pass | `codex_source_checks/*`, `coverage_check_v12_2_council.csv` |
| 42/42 core mapping checked | pass | `codex_source_checks/coverage_delta_after_source_check_20260522.md` |
| local source adjudication complete | pass | `codex_source_checks/pending_source_check_20260522.md` |
| Claude Opus 4.7 Round 03 real call | pass | `model_outputs/claude_round03_source_check_review_key_capture.md` |
| GPT Round 03 real call | fail | `model_outputs/gpt_round03_browser_attempt_blocked_20260522.md` |
| Codex Round 03 adjudication | pass for candidate only | `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` |
| student-facing framework written | pass for candidate only | `final_framework_candidate/FRAMEWORK_BASELINE_v12_2_SOURCE_CHECKED.md` |
| final PASS / baodian / DOCX/PDF | fail | blocked by GPT and governance closure |

## Governor Verdict

Current allowed label:

`complete_source_checked_candidate_framework`

Forbidden labels:

- final PASS
- final baodian
- DOCX/PDF final delivery
- TASK_COMPLETE

## Required Before Promotion

1. Capture GPT Round 03 source-check review or get an explicit user waiver for that exact gate.
2. Re-run Codex final adjudication after GPT Round 03.
3. Confirm traceability matrix and source aliases.
4. Decide whether next-backfill candidates are frozen or moved into a new evidence pass.
5. Only then run final governor review.

