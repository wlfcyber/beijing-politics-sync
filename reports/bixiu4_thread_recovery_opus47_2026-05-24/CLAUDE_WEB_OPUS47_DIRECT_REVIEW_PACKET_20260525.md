# CLAUDE_WEB_OPUS47_DIRECT_REVIEW_PACKET_20260525

Status: `SCOPED_EXTERNAL_REVIEW_PACKET`

Updated: 2026-05-25 13:12 +08

## Scope

This packet is for a scoped Claude web/app external review through direct `https://claude.ai` auto-login. It is not a full DOCX/PDF final review.

Review the recovery governance state for the Beijing Gaokao politics 必修四 thread recovery:

- Whether the thread is correctly treated as recovered execution in progress, not final closure.
- Whether Sonnet/Haiku/model-unknown outputs are excluded from qualified ClaudeCode evidence.
- Whether the 2026-05-24 22:01 and 22:09 Sonnet calls are invalidated.
- Whether the corrected Claude web/app retry path is direct `https://claude.ai` auto-login, not repeated Google login.
- Whether the row-level matrix risk queue remains open after the latest repair.
- Whether ordinary answer/reference text is kept separate from formal scoring/marking evidence.

## Current Evidence Summary

- `THREAD_RECOVERY_STATUS_20260524.md`: status is recovered execution in progress with open gates.
- `SONNET_INVALIDATION_LEDGER.md`: invalidates Sonnet calls at 2026-05-24 22:01 and 22:09.
- `MODEL_EVIDENCE_LEDGER.md`: allows only model-confirmed Claude Opus 4.7 max-effort/adaptive-thinking evidence; otherwise records `BLOCKED_MODEL_CONFIRMATION_REQUIRED` or `real_call_pending`.
- `CLAUDE_WEB_LOGIN_CORRECTION_20260525.md`: user correction says to open `https://claude.ai` directly and rely on existing session auto-login; do not loop through Google login.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/csv`: refreshed after repair, total risk rows `415`, in-book/body risk rows `67`.
- `SHUNYI_Q16_MODEL_SUMMARY_SUPPORT_REPAIR_20260525.md`: repaired `M0032`, `2026顺义二模 Q16`, node `实践是认识的基础`, replacing model-summary support text with the formal marking/阅卷版 source text.

## Latest Repair Detail

Repaired matrix row:

- Row: `M0032`
- Suite: `2026顺义二模`
- Question: `Q16`
- Node: `实践是认识的基础`
- Old support: `external Claude triage + suite source bundle repair`
- New support: 顺义二模评标 doc 第16题阅卷版：评标说明列“实践观点”；阅卷版明确“一切从实际出发，实事求是/实践是认识的基础/社会存在决定社会意识”，并写“群众的实践活动是新大众文艺创作的源泉”。
- Audit result: `MODEL_SUMMARY_USED_AS_SUPPORT_TEXT` count went from `1` to `0`; `M0032` is absent from the refreshed risk CSV.

## Open Gates

- Row-level placement/source/thickness risk queue remains active: `415` risk rows, `67` in-book/body risk rows.
- GPTPro web external review remains `real_call_pending`.
- Full Claude Opus web/app external review of the complete DOCX/PDF deliverable remains `real_call_pending` unless separately performed and captured.
- ClaudeCode model evidence gate remains blocked where runtime artifacts cannot prove model identity plus effort/adaptive-thinking provenance.

## Requested External Review Output

Please return a concise Chinese review with:

1. `model_ui_scope`: whether this is a scoped Claude web/app review only, not a full artifact final review.
2. `governance_verdict`: whether current status should remain in-progress/open-gate.
3. `sonnet_verdict`: whether 22:01 and 22:09 Sonnet outputs must stay invalidated.
4. `direct_login_verdict`: whether the corrected blocker should be direct `https://claude.ai` auto-login retry, not Google-login failure.
5. `matrix_verdict`: whether the Shunyi repair clears the model-summary support defect but leaves the broader risk queue open.
6. `blockers`: list remaining blockers.
7. `evidence_boundary`: state that ordinary reference answers cannot substitute for formal rubric/marking evidence.

Do not claim final acceptance. Do not count Sonnet, Haiku, or unknown-model output as qualified evidence.
