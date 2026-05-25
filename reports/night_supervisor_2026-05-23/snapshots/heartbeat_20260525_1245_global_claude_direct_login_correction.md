# Heartbeat Snapshot - 2026-05-25 12:45 +08

Status: `GLOBAL_CLAUDE_DIRECT_LOGIN_CORRECTION_ISSUED`

## Trigger

User corrected the supervisor: more than one thread may be using the wrong Claude login recovery path. The correct path is direct `https://claude.ai` auto-login, not repeated Google login/account chooser flow.

## Actions Taken

- Issued `patch_orders/ORDER_062_GLOBAL_CLAUDE_DIRECT_LOGIN_CORRECTION_20260525.md`.
- Confirmed Bixiu4 migrated recovery thread already wrote `CLAUDE_WEB_LOGIN_CORRECTION_20260525.md`, updated its model ledger and Governor report, and kept the gate as `real_call_pending`.
- Identified Xuanbiyi v7/final external-review records with stale wording around `Google/OpenAI` or Google account chooser.
- Added Xuanbiyi local correction file `CLAUDE_DIRECT_LOGIN_CORRECTION_20260525.md`.

## Current Gate Boundary

- Bixiu4: correction issued; direct `claude.ai` retry not yet run; no strict final.
- Xuanbiyi: correction issued; old Google/account-chooser blocker wording is superseded for future retries; Claude Desktop/web Opus Adaptive gate remains pending for current SHA.
- Xuanbier: no active stale Google-login blocker found in latest scan, but the global order applies if it resumes Claude web/app review.

## Hard Rule For Next Wake

Any worker that needs Claude web/app external review must first try direct `https://claude.ai` auto-login and capture the result. It may not keep using "Google login failed" or "account chooser" as the blocker without direct-path evidence.
