# External Review Closure Runbook V74

Status: `NOT_COMPLETE_EXTERNAL_REVIEW_GATE_OPEN`

This runbook is the executable closure path for the original objective. It does not waive the real GPT Pro / Claude requirement and does not promote the current review drafts to final.

## Current Evidence

- GPT Pro packet: `10_packets/GPTPRO_REVIEW_PACKET_V65.md`.
- Claude packet: `10_packets/CLAUDE_REVIEW_PACKET_V63.md`.
- GPT Pro result: `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md` is missing.
- GPT Pro intake output: `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md` currently reports `BLOCKED_MISSING_GPTPRO_RESULT`.
- Claude result: `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md` is missing.
- Open blocker: `B2026ERMO-016:GPTPRO_V65/CLAUDE_V63:open_external_review`.
- Latest browser state recheck: `05_gptpro_review/GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md` reports that Chrome extension communication works, but this continuation did not reach a controllable GPT Pro submission page and no result was captured.

## Closure Sequence

1. User-visible GPT Pro V65 submission.
   - Use `05_gptpro_review/GPTPRO_V65_UPLOAD_SET.zip` or the files in `05_gptpro_review/GPTPRO_V65_UPLOAD_MANIFEST.md`.
   - Preserve the full response in `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`.
   - Do not put account credentials or personal identifiers into project files.

2. GPT Pro intake gate.
   - Run from the project root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\05_gptpro_review\run_gptpro_v65_intake_check.ps1
```

   - Required output: `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md`.
   - Stop unless the status is `READY_FOR_GPTPRO_TRIAGE`.
   - V78 shortcut after saving the GPT Pro result:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\07_governor_confucius\resume_after_gptpro_v65.ps1
```

   - V78 output: `07_governor_confucius/POST_GPTPRO_RESUME_CHECK_V78.md`.
   - This shortcut still stops before Claude until `GPTPRO_V65_TRIAGE_FILLED.md` exists and passes the V83 triage quality gate.

3. GPT Pro triage and source verification.
   - Fill `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`.
   - Run `05_gptpro_review/validate_gptpro_v65_triage_v83.ps1`.
   - Stop unless `05_gptpro_review/GPTPRO_V65_TRIAGE_READY_CHECK_V83.md` reports `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`.
   - Use `04_fusion/POST_EXTERNAL_REVIEW_SOURCE_PATCH_PROTOCOL_V70.md`.
   - Patch only source-verified P0/P1 items; unsupported or unverifiable items remain blockers.

4. Claude V63 external review.
   - `06_claude_review/run_claude_external_review_v63.ps1` now enforces:
     - GPT Pro result exists and is non-empty;
     - `GPTPRO_V65_INTAKE_READY_CHECK.md` reports `READY_FOR_GPTPRO_TRIAGE`;
     - `GPTPRO_V65_TRIAGE_FILLED.md` exists and is non-empty;
     - `GPTPRO_V65_TRIAGE_READY_CHECK_V83.md` reports `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`.
   - Run from `06_claude_review/` or with the full path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_claude_external_review_v63.ps1
```

   - Required output: `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md`.

5. Claude triage and second source verification.
   - Fill `06_claude_review/CLAUDE_V63_TRIAGE_FILLED.md`.
   - Run `06_claude_review/validate_claude_v63_triage_v84.ps1`.
   - Stop unless `06_claude_review/CLAUDE_V63_TRIAGE_READY_CHECK_V84.md` reports `READY_FOR_FINAL_LOCAL_GATES_AFTER_CLAUDE_TRIAGE`.
   - Reconcile GPT Pro and Claude findings by local source evidence, not model preference.
   - Patch only source-verified P0/P1 items.

6. Final local gates.
   - Re-run student-facing contamination scan.
   - Run final Governor.
   - Run final Confucius artifact-only learning check.
   - Generate final Markdown, Word, and PDF only after those gates pass.
   - Render/QA Word and PDF before any final claim.

## V74 Guard Test

The runner guard is covered by:

- `06_claude_review/test_claude_v63_gate.ps1`

The test verifies:

- missing GPT Pro result writes gate return code `2`;
- GPT Pro result without ready intake is blocked and does not invoke Claude;
- ready intake without filled GPT triage is blocked and does not invoke Claude;
- ready intake plus weak/non-V83-ready GPT triage is blocked and does not invoke Claude;
- ready intake plus V83-ready GPT triage allows the Claude runner to proceed.

## V78 Resume Guard Test

- `07_governor_confucius/test_post_gptpro_resume_v78.ps1`

The test verifies:

- missing GPT Pro result keeps the resume gate blocked;
- `READY_FOR_GPTPRO_TRIAGE` without filled GPT triage stops before Claude;
- explicit `-RunClaude` invokes Claude only after GPT result, ready intake, filled GPT triage, and V83 triage readiness exist.

## V83/V84 Triage Quality Tests

- `05_gptpro_review/test_gptpro_v65_triage_quality_v83.ps1`
- `06_claude_review/test_claude_v63_triage_quality_v84.ps1`

These tests prevent non-empty but weak triage files from unlocking the next lane or the final local gates.

## Governor Decision

Decision: `HOLD`

The current dual handbook drafts remain review drafts. The original objective is not complete until this closure sequence has real captured outputs and the final gates pass.
