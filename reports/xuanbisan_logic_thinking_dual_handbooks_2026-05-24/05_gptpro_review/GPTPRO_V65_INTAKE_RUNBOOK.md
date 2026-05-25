# GPT Pro V65 Intake Runbook

Status: `WAITING_FOR_REAL_GPTPRO_RESULT`

Purpose: verify that the saved GPT Pro V65 response is complete enough for triage. This runbook does not simulate GPT Pro and does not replace real review.

## Required Input

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`

## Command

From the project root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\05_gptpro_review\run_gptpro_v65_intake_check.ps1
```

Expected output file:

- `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md`

## Exit Codes

- `0`: result appears complete enough to enter GPT Pro triage.
- `2`: result is missing, empty, too short, or missing required sections/signals.
- `2`: result is a placeholder/template/TODO handoff file rather than the real GPT Pro response.

## Required Sections In The GPT Pro Result

- Verdict.
- P0 findings.
- P1 findings.
- Thinking handbook structure judgment.
- Reasoning handbook structure judgment.
- Must-fix-before-Claude list.
- Forbidden-claims section.
- Source-verification requests.

## Next Gate

Only after the intake check returns `0` may Codex fill:

- `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`

## V82 Placeholder Guard

The intake script now blocks long placeholder or template files before ordinary section checks. If `GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md` contains handoff text such as `TODO`, `placeholder`, `template`, or `paste the real GPT Pro response`, the status becomes `BLOCKED_PLACEHOLDER_GPTPRO_RESULT`.

Claude V63 remains blocked until GPT Pro triage and any source-verified P0/P1 patches are complete.
