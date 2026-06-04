# Claude App Blank-Screen Recovery Log (2026-05-25)

## Symptom

The user asked why the external review lane stopped working after it had been usable earlier. Claude Desktop was running and had a visible top-level window titled `Claude`, but the content area rendered as a blank white page. This made it unsafe to paste the final handbook or count the app lane as reviewed.

## Evidence

- Process existed: `Claude_1.8555.2.0_x64__pzs8sxrjxfjjc\app\Claude.exe`
- Account state in `main.log`: `claude.ai account active and logged in`
- App auth cache refreshed successfully at 2026-05-25 03:47:42
- Current frontend error in `claude.ai-web.log`: `Uncaught (in promise) ReferenceError: Cannot access '$n' before initialization`
- Historical model config errors were also present for `model_configs/claude-opus-4-7[1m]` returning 404, but this was not proven to be the immediate blank-screen cause.

## Recovery Attempts

1. Restarted Claude Desktop normally.
   - Result: still blank.
2. Moved regenerable frontend caches to backup, preserving account/app config state.
   - Backup: `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\cache_backup_20260525_034947`
   - Moved: `Cache`, `Code Cache`, `GPUCache`, `DawnGraphiteCache`, `DawnWebGPUCache`
   - Result: still blank.
3. Moved frontend local UI state to backup, preserving app auth config.
   - Backup: `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\webstate_backup_20260525_035050`
   - Moved: `Local Storage`, `Session Storage`, `WebStorage`
   - Result: still blank.
4. Relaunched via Start Apps ID `Claude_pzs8sxrjxfjjc!Claude`.
   - Result: still blank.
5. Relaunched with GPU disabled flags.
   - Result: the app did not provide a usable review input/capture surface.

## Current Gate Status

Claude application-side Opus Adaptive review remains `real_call_pending`. It must not be counted as passed.

To keep local work moving without faking the gate, a separate ClaudeCode CLI Opus 4.7 provisional review was run and saved as:

- `CLAUDECODE_OPUS47_POST_GPT_CLEANUP_REREVIEW_CAPTURE_20260525.md`
- `CLAUDECODE_OPUS47_POST_GPT_CLEANUP_REREVIEW_CAPTURE_20260525.json`

That CLI review is useful evidence for content sanity, but it is not a replacement for the Claude Desktop app gate requested by the user.

## Later Recovery Update (2026-05-25 04:10-04:40)

Further investigation showed the blank screen was not caused by a missing process. The app shell was running, but the webview could not complete account/bootstrap loading:

- `main.log` repeatedly showed a brief `claude.ai account active and logged in` state followed by `User logged out during IPC wait`.
- `claude.ai-web.log` showed `["account_profile"] data is undefined`, `TypeError: Failed to fetch`, and the same `$n` frontend initialization error.
- Direct proxy checks showed `claude.ai` returning Cloudflare challenge responses through the current proxy path, while `api.anthropic.com` was reachable.
- The MSIX app did not have a loopback exemption, so a non-loopback local relay was created from `192.168.1.133:18002` to `127.0.0.1:18001`, and the Windows user proxy was pointed at that relay.
- A Windows Firewall prompt for the Python relay was blocking the relay until it was explicitly allowed.
- A prior config restore had accidentally produced a BOM-prefixed JSON once; Claude logged this as config corruption and reset to defaults. The saved app auth config backup was restored again using UTF-8 without BOM.
- An older browser network-state backup containing prior account/bootstrap state was restored from `deep_webstate_backup_20260525_040701`.

After the relay, config, browser state, and firewall prompt were fixed, Claude Desktop no longer rendered as a pure blank screen. It reached the normal `Claude for Windows` start page and then the sign-in page. This means the white-screen incident is recovered to an authorization step, but the app review lane is still not passed.

Current state:

- `blank_screen`: recovered
- `app_network_path`: recovered via `192.168.1.133:18002 -> 127.0.0.1:18001`
- `firewall_prompt`: allowed for the Python relay
- `app_auth`: pending user-side account selection / credential step
- `opus_adaptive_app_review_gate`: still `real_call_pending`

Do not count any Claude app review until the app is fully signed in and a fresh Opus 4.7 Adaptive review result is captured.

## Latest Recovery Update (2026-05-25 10:15-10:25)

Claude Desktop was brought to the foreground and verified visually:

- The pure blank/white screen state is recovered.
- The app reached `Claude for Windows`.
- Clicking `Get started` reached the Claude sign-in screen.
- Clicking `Continue with Google` opened the Google account chooser in Chrome.

At this point the workflow must stop on the Claude app lane because selecting a Google/Claude account is a user-identity action. Codex must not choose the account or enter credentials.

Current state:

- `blank_screen`: recovered
- `auth_step`: reached Google account chooser
- `user_action_needed`: select the intended account / finish sign-in
- `opus_adaptive_app_review_gate`: still `real_call_pending`

This is enough to explain the afternoon-to-now regression: the app was not missing; its local app state and auth bootstrap failed, then recovery reached an account-selection gate. It is not enough to count Claude app Opus review as complete.

## User Direct-Login Correction (2026-05-25 12:45 +08)

This recovery log is superseded for the next retry path. Future Claude web/app review attempts must not keep walking through `Continue with Google` or stop at the Google account chooser as the default blocker.

Correct next retry:

1. Open `https://claude.ai` directly.
2. Rely on the current machine's existing Claude session and expected automatic login.
3. If the chat surface opens, verify/select Opus 4.7 Adaptive and run the review.
4. If direct `https://claude.ai` redirects to login or fails, record that exact direct-path failure and keep `opus_adaptive_app_review_gate` as `real_call_pending`.

The prior Google chooser observation remains historical recovery evidence, but it is not the accepted next action.
