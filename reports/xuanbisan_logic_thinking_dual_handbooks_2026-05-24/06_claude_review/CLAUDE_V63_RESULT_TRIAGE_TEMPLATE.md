# Claude V63 Result Triage Template

Status: `TEMPLATE_WAITING_FOR_CLAUDE_RESULT`

Use this after `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md` exists. Do not use it to simulate Claude.

## Required Inputs

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`
- `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`
- `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md`

## Reconciliation Rules

1. Claude V63 must explicitly reconcile GPT Pro V65 findings.
2. If Claude contradicts GPT Pro, Codex resolves by local source evidence, not by model preference.
3. If both reviewers agree but local evidence is weak, keep the issue open.
4. If both reviewers miss a Governor/Confucius issue, Codex still must block final acceptance.

## Triage Table

| id | severity | Claude finding | Relation to GPT Pro V65 | Affected artifact | Local evidence to inspect | Codex source verdict | Patch target | Status |
|---|---|---|---|---|---|---|---|---|
| CLV63-001 | P0/P1/P2 |  | agrees/conflicts/new |  |  | pending/source_verified/rejected/unverifiable |  | pending |

## Required Output After Triage

Write the filled triage as:

- `06_claude_review/CLAUDE_V63_TRIAGE_FILLED.md`

Then update:

- `04_fusion/POST_EXTERNAL_REVIEW_SOURCE_PATCH_PROTOCOL_V70.md`
- `04_fusion/PROMOTION_HOLD.md`
- `04_fusion/PROMOTION_QUALITY_CHECK.md`
- `07_governor_confucius/GOVERNOR_CHECKLIST.md`

## V84 Triage Quality Gate

After filling `06_claude_review/CLAUDE_V63_TRIAGE_FILLED.md`, run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\06_claude_review\validate_claude_v63_triage_v84.ps1
```

The check must report `READY_FOR_FINAL_LOCAL_GATES_AFTER_CLAUDE_TRIAGE` before final Governor, Confucius, Word, or PDF gates may begin. A non-empty but weak Claude triage file is not enough.
