# Claude Direct Login Correction 20260525

Status: `CLAUDE_DIRECT_LOGIN_PATH_REQUIRED`

Updated: 2026-05-25 12:45 +08

## Correction

The previous Xuanbiyi external-review recovery wording must be corrected for future Claude attempts:

- Open `https://claude.ai` directly.
- Use the current machine's existing Claude session and expected automatic login.
- Do not repeatedly choose `Continue with Google`.
- Do not classify the blocker as `Google/OpenAI login chain`, `Google account chooser`, or generic Claude web/app login failure unless direct `https://claude.ai` auto-login has first been tried and evidenced.

## Superseded Local Wording

These older records are superseded only for the retry path, not deleted as historical evidence:

- `FINAL_ACCEPTANCE_STATUS_20260525.md`: the phrase that the Chrome/web channel got stuck in a `Google/OpenAI` login chain must not be reused as the next Claude retry instruction.
- `CLAUDE_APP_BLANK_SCREEN_RECOVERY_LOG_20260525.md`: the Google account chooser step is not the correct next retry path if direct `https://claude.ai` auto-login has not been tried.
- `../03_claude_opus/CLAUDE_WEB_BLOCKED_LOGIN_20260524.md`: the next action is no longer "wait for user confirms login"; the next action is direct `https://claude.ai` auto-login attempt with evidence capture.

## Gate Boundary

- ClaudeCode Opus 4.7 CLI outputs remain provisional production/review evidence only.
- Claude web/app Opus Adaptive final review remains `real_call_pending` for the current final SHA until a fresh direct-path Claude review is captured.
- Do not count Sonnet, Haiku-only, model-unknown, or app/login-recovery notes as a completed Claude Opus Adaptive gate.

## Next Allowed Retry

1. Open direct `https://claude.ai`.
2. If the chat surface opens automatically, verify/select Opus 4.7 Adaptive and run the review.
3. If it redirects to login, record the exact direct-path failure and keep the gate pending.
