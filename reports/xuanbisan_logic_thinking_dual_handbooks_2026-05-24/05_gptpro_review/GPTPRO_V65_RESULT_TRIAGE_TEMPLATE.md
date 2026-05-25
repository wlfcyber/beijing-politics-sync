# GPT Pro V65 Result Triage Template

Status: `TEMPLATE_WAITING_FOR_GPTPRO_RESULT`

Use this after `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md` exists. Do not use it to simulate GPT Pro.

## Required Input

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`
- `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md`

Before filling triage, run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\05_gptpro_review\run_gptpro_v65_intake_check.ps1
```

The check must report `READY_FOR_GPTPRO_TRIAGE`. If it reports `BLOCKED_MISSING_GPTPRO_RESULT`, `BLOCKED_EMPTY_GPTPRO_RESULT`, or another blocked status, stop here.

## Triage Rules

1. Separate GPT Pro comments into P0, P1, P2, and advisory notes.
2. Do not accept any new conceptual claim, deletion, relocation, or wording change until Codex verifies it against local source evidence.
3. If GPT Pro flags a source/evidence issue, map it to one of:
   - source file or render page;
   - `QUESTION_COVERAGE_MATRIX.csv`;
   - `MAIN_THINKING_LEDGER.csv`;
   - `REASONING_FORM_LEDGER.csv`;
   - `CHOICE_TRAP_LEDGER.csv`;
   - source-lock note under `02_codex_lane/`.
4. If GPT Pro flags only style/readability, patch student-facing drafts only after confirming the patch does not alter source meaning.
5. Any finding that cannot be verified locally remains a blocker, not a patch.

## Triage Table

| id | severity | GPT Pro finding | Affected artifact | Local evidence to inspect | Codex source verdict | Patch target | Status |
|---|---|---|---|---|---|---|---|
| GPTV65-001 | P0/P1/P2 |  |  |  | pending/source_verified/rejected/unverifiable |  | pending |

## Required Output After Triage

Write the filled triage as:

- `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`

Then update:

- `04_fusion/PROMOTION_HOLD.md`
- `04_fusion/PROMOTION_QUALITY_CHECK.md`
- `03_claudecode_lane/blockers_2026_ermo.csv`
- `07_governor_confucius/GOVERNOR_CHECKLIST.md`

Only after GPT Pro triage and source-verified patches may Claude V63 run.

## V83 Triage Quality Gate

After filling `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`, run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\05_gptpro_review\validate_gptpro_v65_triage_v83.ps1
```

The check must report `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE` before `resume_after_gptpro_v65.ps1 -RunClaude` is allowed. A non-empty but weak triage file is not enough.
