# External Gate Root Cause And Recovery Log (2026-05-25 08:45)

## Current Root Cause

The local handbook chain did not disappear. The failure is in the external real-call gates.

Observed current state:

- The Markdown final still exists and hashes to `9DC2615B0615AF1F64E34505747221CC95B1C342E343955F42DD765337BD0490`.
- Local scan still reports 141 core points, 380 question headings, and 0 mixed-question heading candidates.
- Chrome remote debugging on port `9224` is usable, but the controllable ChatGPT page is logged out and says uploads require login.
- A no-credential recovery attempt opened the ChatGPT login flow and reached the Google sign-in identifier page. It now requires user-side account authorization; no account was selected and no credential was entered.
- Claude Desktop is no longer a blank white screen after the relay/cache/config repair, but the app-side Claude Opus gate is still at the authorization/login step.
- ClaudeCode CLI is installed and authenticated enough to run `claude --version`; earlier Opus 4.7 CLI evidence for the current final remains saved, but this still cannot substitute for the user-visible Claude Desktop app gate.

## Why It Looked Fine Earlier

Earlier evidence files were real local artifacts: GPT Pro captures, ClaudeCode Opus 4.7 captures, coverage scans, and the final Markdown were saved. Later, browser/app state drifted:

1. The controllable ChatGPT page moved to a logged-out temporary-chat state, so upload and Pro review cannot proceed from that tab.
2. The previous Chrome-extension path had already shown unstable behavior: pages could be opened or listed, but click/input/upload did not reliably submit content.
3. Claude Desktop lost usable authenticated app state and fell back first to blank-screen/bootstrap errors, then to the login page after recovery.

Therefore, "four GPT pages exist" or "Claude window exists" is not evidence of review completion. Only saved raw model replies count.

## Recovery Decision

- Do not rewrite the final just because external gates are blocked.
- Lock the current final hash as the local baseline.
- Continue safe local evidence checks and ClaudeCode production/review work.
- Treat GPT Pro full-file review and Claude Desktop Opus Adaptive review as `real_call_pending` until fresh raw replies are captured.
- Do not claim strict final acceptance until both external app/web gates are closed or the user explicitly waives that exact requirement.

## Next Concrete Actions

1. Run a fresh ClaudeCode Opus 4.7 production/check pass against the current final baseline and save raw evidence.
2. Keep the ChatGPT/Claude app login pages available for user-side authorization, but do not enter or select credentials.
3. After authorization, submit the locked final to GPT Pro for full-file review and Claude Desktop Opus Adaptive for app-side final review.
4. If either reviewer returns content issues, verify each issue against local sources before patching the student artifact.
