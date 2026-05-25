# CLAUDE_WEB_OPUS47_DIRECT_REVIEW_PACKET_AFTER_SHIJINGSHAN_20260525

Status: `SCOPED_EXTERNAL_REVIEW_PACKET_AFTER_SHIJINGSHAN_LOCAL_REPAIR`

Updated: 2026-05-25 14:28 +08

## Scope

This is a scoped Claude web/app external review through direct `https://claude.ai` auto-login. It is not a full DOCX/PDF final review.

Review the governance state for the Beijing Gaokao politics 必修四 recovery thread after the latest Yanqing and Shijingshan local repairs:

- Whether the thread should remain recovered execution in progress with open external gates.
- Whether Sonnet/Haiku/model-unknown output must remain excluded from qualified ClaudeCode evidence.
- Whether the 2026-05-24 22:01 and 22:09 Sonnet calls must remain invalidated.
- Whether the corrected Claude web/app route is direct `https://claude.ai` auto-login, not repeated Google login.
- Whether ordinary answer/reference text is kept separate from formal scoring/marking evidence.
- Whether the latest local matrix state supports "current body has no flagged row-level evidence risk" while still leaving web/model gates open.

## Current Evidence Summary

- `THREAD_RECOVERY_STATUS_20260524.md`: status is `RECOVERED_EXECUTION_IN_PROGRESS_LOCAL_BODY_EVIDENCE_CLEARED_AFTER_SHIJINGSHAN_REPAIR_MODEL_GATES_OPEN`.
- `SONNET_INVALIDATION_LEDGER.md`: invalidates Sonnet calls at 2026-05-24 22:01 and 22:09.
- `MODEL_EVIDENCE_LEDGER.md`: allows only model-confirmed Claude Opus 4.7 max-effort/adaptive-thinking evidence; otherwise records `BLOCKED_MODEL_CONFIRMATION_REQUIRED` or `real_call_pending`.
- `CLAUDE_WEB_LOGIN_CORRECTION_20260525.md`: user correction says to open `https://claude.ai` directly and rely on existing session auto-login; do not loop through Google login.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/csv`: refreshed after Shijingshan repair, matrix rows `1471`, in-book/body rows `442`, total risk rows `288`, in-book/body risk rows `0`.
- `SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: 2025石景山一模 rows changed `28`; risk rows for this suite now `0`.
- `FORMAT_RENDER_QA_20260524.md`: latest valid render snapshot remains Yanqing/global-style render, `278/278` pages, DOCX/PDF label counts `2771/2771`, blank-like body pages `0`.
- `ORDER_063_FINAL_GITHUB_UPLOAD_ACK_20260525.md`: GitHub upload is deferred; no push is allowed until all active Beijing politics lines end, then upload scope and secret-pattern scan must be done first.

## Latest Repair Detail

2025石景山一模 was repaired locally:

- Q16 retained as formal-rubric coverage for 联系观/发展观/矛盾观 and Chinese excellent traditional culture value.
- The old standalone objective-law/subjective-initiative placement was corrected because the formal Q16 scoring rules do not support it as an independent node for this suite.
- Q3/Q4 retained only as choice-question chains supported by the official answer key; they are not main-question scoring evidence.
- Q17 politics/IR, Q18 economics, Q19 logic/scientific thinking, and Q20 law are excluded by module boundary.
- Q21 keeps only Bixiu4-relevant reform/social-development-law points already present in current DOCX.
- DOCX/PDF text was not changed in this Shijingshan repair; no new render was required.

## Open Gates

- GPTPro web external review remains `real_call_pending`.
- Full Claude Opus web/app external review of the complete DOCX/PDF deliverable remains `real_call_pending` unless separately performed and captured.
- ClaudeCode model evidence gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` where runtime artifacts show auxiliary Haiku alongside Opus.
- Full manual every-page typography review is not claimed.
- ORDER_063 final GitHub upload remains deferred; no push now.

## Requested External Review Output

Please return a concise Chinese review with:

1. `model_ui_scope`: whether this is a scoped Claude web/app review only, not a full artifact final review.
2. `governance_verdict`: whether current status should remain in-progress/open-gate.
3. `sonnet_verdict`: whether 22:01 and 22:09 Sonnet outputs must stay invalidated.
4. `direct_login_verdict`: whether the corrected route is direct `https://claude.ai` auto-login retry, not Google-login failure.
5. `matrix_verdict`: whether latest local audit supports current body row-level risk `0` while broader non-body candidate risk and external gates remain open.
6. `blockers`: list remaining blockers.
7. `evidence_boundary`: state that ordinary reference answers cannot substitute for formal rubric/marking evidence.

Do not claim final acceptance. Do not count Sonnet, Haiku, or unknown-model output as qualified evidence.
