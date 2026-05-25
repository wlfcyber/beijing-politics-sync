# Claude V63 Runbook

Status: `STAGED_WAITING_FOR_GPTPRO_V65`

Claude V63 must not run until the real GPT Pro V65 result exists, the GPT Pro intake gate is ready, and GPT Pro triage has passed the V83 quality gate.

Required input:

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`
- `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md` with status `READY_FOR_GPTPRO_TRIAGE`
- `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`
- `05_gptpro_review/GPTPRO_V65_TRIAGE_READY_CHECK_V83.md` with status `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`

Runner:

- `06_claude_review/run_claude_external_review_v63.ps1`

Suggested Windows launch:

- `powershell -NoProfile -ExecutionPolicy Bypass -File .\run_claude_external_review_v63.ps1`

Expected output:

- `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md`

Safety behavior:

- If the GPT Pro result file is missing or empty, the runner writes `claude_external_review_v63_blocked.txt`, sets return code `2`, and refuses to run.
- If the GPT Pro intake check is missing or not `READY_FOR_GPTPRO_TRIAGE`, the runner writes `claude_external_review_v63_blocked.txt`, sets return code `2`, and refuses to run.
- If `GPTPRO_V65_TRIAGE_FILLED.md` is missing or empty, the runner writes `claude_external_review_v63_blocked.txt`, sets return code `2`, and refuses to run.
- If `GPTPRO_V65_TRIAGE_READY_CHECK_V83.md` is missing or not `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`, the runner writes `claude_external_review_v63_blocked.txt`, sets return code `2`, and refuses to run.
- If Claude returns normally but only writes stdout, the runner copies stdout into the expected result file so the external review is captured.

Guard test:

- Current test before GPT Pro result exists correctly refused to run.
- V74/V83 guard test: `06_claude_review/test_claude_v63_gate.ps1` verifies missing GPT result, missing/blocked intake, missing triage, and non-V83-ready triage are all blocked before Claude is invoked.
- V74 closure runbook: `07_governor_confucius/EXTERNAL_REVIEW_CLOSURE_RUNBOOK_V74.md`.
- V84 Claude triage quality test: `06_claude_review/test_claude_v63_triage_quality_v84.ps1`.
- `claude_external_review_v63_blocked.txt` was written.
- `claude_external_review_v63_return_code.txt` contains `2`.
- `CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md` was not created.

After Claude V63:

1. Codex must classify GPT Pro and Claude findings.
2. Every accepted finding must be patched only after source verification.
3. `06_claude_review/CLAUDE_V63_TRIAGE_FILLED.md` must pass `validate_claude_v63_triage_v84.ps1`.
4. Final Governor/Confucius and Word/PDF QA may run only after those patches and V84 are complete.
