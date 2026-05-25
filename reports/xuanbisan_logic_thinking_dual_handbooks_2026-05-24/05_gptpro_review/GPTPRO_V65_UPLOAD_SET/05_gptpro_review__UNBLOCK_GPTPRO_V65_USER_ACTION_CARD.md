# Unblock GPT Pro V65 User Action Card

Status: `USER_ACTION_REQUIRED`

Current packet:

- `10_packets/GPTPRO_REVIEW_PACKET_V65.md`

Required output after submission:

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`

## Current Blocker

The local review package is ready, but GPT Pro submission is not possible from the current automated path:

- Chrome extension route, V76: the extension-backed channel can see a ChatGPT tab, but the tab is still `https://chatgpt.com/auth/login` with title `开始使用 | ChatGPT`, not an authenticated GPT Pro workspace. Evidence: `05_gptpro_review/GPTPRO_V65_CHROME_EXTENSION_RECHECK_V76.md`.
- Earlier profile note: the Codex Chrome Extension was available in `Profile 1`, while the active selected Chrome profile did not expose the extension bridge.
- In-app browser route: reaches ChatGPT login, not an authenticated GPT Pro workspace.
- Chrome CDP recheck on 2026-05-25: the reachable Chrome page is a Google account login page, not an authenticated GPT Pro workspace. Evidence: `05_gptpro_review/GPTPRO_V65_CDP_RECHECK_2026-05-25.md`.
- Governor recheck: `07_governor_confucius/EXTERNAL_REVIEW_GATE_AUDIT_V71.md`.

No password, email, or account details should be put into project files or chat.

## User Steps

1. Open the Chrome profile that has the Codex Chrome Extension enabled, or enable the extension in the currently selected Chrome profile.
2. In that same profile, use the current ChatGPT login tab or open ChatGPT and confirm the account is logged in.
3. Open/select the GPT Pro workspace or model mode required for this project.
4. Upload `05_gptpro_review/GPTPRO_V65_UPLOAD_SET.zip`, or upload the individual files listed in `05_gptpro_review/GPTPRO_V65_UPLOAD_MANIFEST.md`.
5. Save the GPT Pro result as `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`.
6. Resume this thread after the result file exists.

Prepared upload paths:

- Folder: `05_gptpro_review/GPTPRO_V65_UPLOAD_SET/`
- Zip: `05_gptpro_review/GPTPRO_V65_UPLOAD_SET.zip`
- One-screen handoff: `05_gptpro_review/GPTPRO_V65_USER_HANDOFF_V77.md`
- Prompt/manifest: `05_gptpro_review/GPTPRO_V65_UPLOAD_MANIFEST.md`
- Clean copy-paste prompt: `05_gptpro_review/GPTPRO_V65_COPY_PASTE_PROMPT_CLEAN.md`
- Result drop instructions: `05_gptpro_review/GPTPRO_V65_RESULT_DROP_INSTRUCTIONS.md`
- Closure runbook: `07_governor_confucius/EXTERNAL_REVIEW_CLOSURE_RUNBOOK_V74.md`
- Claude gate test: `06_claude_review/test_claude_v63_gate.ps1`

## Next Automated Step After User Action

After `GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md` exists, Codex should:

1. Run `05_gptpro_review/run_gptpro_v65_intake_check.ps1`.
2. Stop unless `05_gptpro_review/GPTPRO_V65_INTAKE_READY_CHECK.md` reports `READY_FOR_GPTPRO_TRIAGE`.
3. Read and classify GPT Pro findings into `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`.
4. Apply only source-verified patches.
5. Run Claude V63 using `10_packets/CLAUDE_REVIEW_PACKET_V63.md`; the runner will refuse to invoke Claude unless the GPT Pro result, ready intake, and filled GPT triage all exist.
6. Save the result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md`.
7. Continue with final Governor, Confucius, and Word/PDF delivery QA only after those external gates are closed.
