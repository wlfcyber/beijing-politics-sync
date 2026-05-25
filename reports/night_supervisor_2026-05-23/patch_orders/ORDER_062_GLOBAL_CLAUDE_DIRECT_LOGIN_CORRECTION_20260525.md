# ORDER_062_GLOBAL_CLAUDE_DIRECT_LOGIN_CORRECTION_20260525

Issued: 2026-05-25 12:45 +08

Status: `ACTIVE_CORRECTION`

## User Correction

Any current or resumed Beijing politics thread that needs a Claude web/app external review must use this corrected login path:

1. Open `https://claude.ai` directly.
2. Rely on the current machine's existing Claude session and expected automatic login.
3. Do not repeatedly choose the Google login button.
4. Do not record the blocker as "Google login failed", "Google/OpenAI login chain", "Claude app account chooser", or a generic web-entry failure unless the direct `https://claude.ai` auto-login path has first been tried and documented with evidence.
5. After direct auto-login succeeds, select or verify Claude Opus 4.7 Adaptive / max-effort review before counting the external Claude gate.

## Affected Lines

- Bixiu4 migrated recovery thread `019e5a7d-0e79-7643-a03d-2e7614d2acec`: already corrected in `bixiu4_thread_recovery_opus47_2026-05-24/CLAUDE_WEB_LOGIN_CORRECTION_20260525.md`; direct retry still not completed.
- Xuanbiyi v7/final external-review line: old records mention `Google/OpenAI` or Google account chooser. Those records are superseded for future retries by `CLAUDE_DIRECT_LOGIN_CORRECTION_20260525.md`.
- Xuanbier line: no current false Google-login blocker found in the latest scan; if it resumes a Claude review, it must still follow this order.
- Any future nightly supervisor or worker thread: this order overrides older "click Google / wait for account chooser" retry instructions.

## Acceptance Boundary

- Sonnet, Haiku-only, or model-unknown outputs remain invalid for the required Claude evidence gate.
- ClaudeCode CLI Opus evidence remains useful production/review evidence, but it is not a substitute for a user-visible Claude web/app Opus 4.7 Adaptive gate when that gate is required.
- Do not write `STRICT_FINAL_ACCEPTED` only because this login correction was issued. The corrected direct-login retry must actually run and the model/mode/provenance must be captured.

## Required Next Actions

1. Every active worker must add a note to its local model/evidence ledger: `Claude direct login correction active; direct https://claude.ai required before declaring web/app blocker`.
2. Before the next Claude external review attempt, open direct `https://claude.ai`; do not press Google login unless direct auto-login failed and the failure is evidenced.
3. If direct `https://claude.ai` opens an already logged-in chat surface, proceed with the Opus 4.7 Adaptive review and capture model/mode evidence.
4. If direct `https://claude.ai` still redirects to a login screen, record that exact direct-path failure and keep the gate as `real_call_pending`.
