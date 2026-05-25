# Post External Review Source Patch Protocol V70

Status: `STAGED_WAITING_FOR_GPTPRO_AND_CLAUDE`

This protocol governs all patches after GPT Pro V65 and Claude V63. It prevents external-review suggestions from directly changing the student artifacts without local source verification.

V74 closure references:

- `07_governor_confucius/EXTERNAL_REVIEW_CLOSURE_RUNBOOK_V74.md`
- `06_claude_review/test_claude_v63_gate.ps1`

## Inputs

Required before patching:

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`
- `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md` with status `READY_FOR_GPTPRO_TRIAGE`
- `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`
- `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md`

Current review bases:

- `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md`
- `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md`

## Patch Order

1. GPT Pro V65 triage.
2. Codex local source verification for each accepted GPT Pro finding.
3. Patch only source-verified P0/P1 items.
4. Run Claude V63 only after GPT Pro intake is `READY_FOR_GPTPRO_TRIAGE`, GPT triage is filled, and GPT Pro patches are applied or logged as blocked.
5. Claude V63 triage.
6. Codex local source verification for each accepted Claude finding.
7. Patch only source-verified P0/P1 items.
8. Re-run student-facing contamination scan.
9. Run final Governor and Confucius.
10. Generate Word/PDF only after final gates pass.

## Evidence Rule

External reviewers may identify issues, but they are not evidence authorities. A patch is allowed only if at least one local evidence source supports it:

- original paper / rendered page / OCR text;
- formal marking rule, evaluation report, or scoring source;
- reliable objective answer key for choice questions;
- existing source-lock note;
- ledger row with source pointer.

## Patch Ledger Template

| patch_id | source_review | review_finding_id | affected_question_or_section | local_source_checked | source_verdict | patch_file | patch_summary | post_patch_scan |
|---|---|---|---|---|---|---|---|---|
| PATCH-V70-001 | GPT Pro V65 / Claude V63 |  |  |  | verified/rejected/unverifiable |  |  | pending |

## Forbidden Shortcuts

- Do not patch because GPT Pro or Claude says so without source verification.
- Do not promote `A-support` or choice-signal rows to formal scoring rows unless the source hierarchy supports it.
- Do not remove boundary warnings merely to make prose smoother.
- Do not generate final Word/PDF before final Governor and Confucius.
- Do not mark final/pass/complete while `B2026ERMO-016` remains open.
