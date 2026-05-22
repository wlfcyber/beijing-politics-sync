# Governor Gate Check v12.2

Status: `markdown_baodian_complete_pending_docx_pdf_render`

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
| Markdown baodian output | pass | `final_baodian_20260523/00_READ_ME_FIRST.md`; `final_baodian_20260523/01_法律主观题框架章.md`; `final_baodian_20260523/02_42题按框架解析宝典.md`; `final_baodian_20260523/05_GOVERNOR_FINAL_CHECK.md` |
| 42/42 question-card coverage | pass | `final_baodian_20260523/02_42题按框架解析宝典.md`; `traceability/TRACEABILITY_MATRIX_v12_2_BAODIAN_INDEX.csv` |
| reference/open rows separated | pass | `final_baodian_20260523/03_开放容器与不晋升题附录.md` |
| DOCX/PDF rendered delivery | fail / not produced | no `.docx` or `.pdf` final delivery exists in this milestone |

## Governor Verdict

Current allowed label:

`markdown_baodian_complete_pending_docx_pdf_render`

Forbidden labels:

- DOCX/PDF final delivery
- TASK_COMPLETE

## Required Before Final Document Delivery

1. Decide whether next-backfill candidates are frozen or moved into a new evidence pass.
2. Optional: render the Markdown baodian into DOCX/PDF and visually verify layout.
3. Only then claim DOCX/PDF delivery or broader TASK_COMPLETE.
