# GPT Pro V65 Result Drop Instructions

Status: `WAITING_FOR_REAL_GPTPRO_RESULT`

After the real GPT Pro review is complete, save the full response in this exact file:

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`

Then run the local intake gate from the project root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\05_gptpro_review\run_gptpro_v65_intake_check.ps1
```

The command writes:

- `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md`

If the check reports `BLOCKED_MISSING_GPTPRO_RESULT`, `BLOCKED_EMPTY_GPTPRO_RESULT`, or any other blocked status, do not fill triage and do not start Claude V63.

Minimum acceptable content:

- GPT Pro verdict.
- P0 findings section.
- P1 findings section.
- Thinking handbook structure judgment.
- Reasoning handbook structure judgment.
- Must-fix-before-Claude list.
- Forbidden-claims section.
- Any source-verification requests.

Do not summarize the result into project notes only. The original GPT Pro response or a complete copied response must be preserved so Codex can triage it.

After the result file exists, the next required local files are:

- `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md` with status `READY_FOR_GPTPRO_TRIAGE`
- `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`
- `04_fusion/POST_EXTERNAL_REVIEW_SOURCE_PATCH_PROTOCOL_V70.md` patch ledger entries, if any source-verified patches are needed
- `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md`, after Claude V63 is allowed to run
