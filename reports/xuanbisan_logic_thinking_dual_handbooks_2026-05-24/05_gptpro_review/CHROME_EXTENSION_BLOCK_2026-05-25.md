# GPT Pro Submission Block: Chrome Extension Profile Mismatch

Status: `gptpro_real_submission_blocked_by_chrome_profile_extension_mismatch`

## Check Result

Attempted to connect to the Codex Chrome Extension for GPT Pro web submission. The browser connection returned:

`Browser is not available: extension`

Environment checks:

- Google Chrome is installed and running.
- Native messaging host manifest is present and correct.
- Selected Chrome profile reported by the plugin is `Profile`.
- The Codex Chrome Extension is not installed/enabled in selected `Profile`.
- The extension is installed and enabled in `Profile 1`.

## In-App Browser Retry

The Codex in-app browser route was also retried after V63 packaging. It opened `https://chatgpt.com/` but landed on `https://chatgpt.com/auth/login` with login buttons visible, so no authenticated GPT Pro submission was possible from that surface.

## Consequence

No GPT Pro V63 result has been captured. This is still a P0 external-review blocker. Per Chrome plugin rules, Codex should not repair or rewrite the browser profile setup directly.

## Required User-Side Action

Enable/install the Codex Chrome Extension in the selected Chrome profile, or make the profile with the extension (`Profile 1`) the active profile used by the Codex Chrome plugin. Alternatively, log in to ChatGPT Pro in the Codex in-app browser. After that, rerun GPT Pro V63 submission.
