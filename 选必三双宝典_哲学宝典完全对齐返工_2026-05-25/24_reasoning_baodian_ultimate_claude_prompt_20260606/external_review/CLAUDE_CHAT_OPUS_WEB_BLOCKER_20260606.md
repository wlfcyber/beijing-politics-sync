# Claude Chat Opus Web Lane Blocker

Status: `RESOLVED_BY_PASTED_ATTACHMENT_WORKAROUND`

Resolution: the file-upload blocker below was bypassed by using Claude web's pasted attachment flow plus a short typed instruction. Claude Chat Opus 4.8 Max returned `ACCEPT`; see `external_review/CLAUDE_CHAT_OPUS_FINAL_REVIEW_RESULT_20260606.md`.

## What Was Attempted

- Opened Claude web in Chrome under the logged-in Max account.
- Confirmed model selector showed `Opus 4.8 Max`.
- Prepared `CLAUDE_CHAT_OPUS_FINAL_REVIEW_PROMPT_20260606.md` and attempted to attach it with the final Markdown, QA report, QA JSON, PDF QA JSON, defect ledger, final acceptance report, and GPT Pro seventh result.
- Claude file chooser opened and reported multi-file support, but `setFiles` failed with `Not allowed`.
- Fallback paste of the full text packet was accepted by the page only as a collapsed `PASTED` block; Claude treated the submitted prompt as empty and returned an invalid response.
- Programmatic text input works for about 1000 characters, but larger single fills are truncated or ignored, making a full 115k-character review packet impractical through plain typing.

## Historical User-Side Repair Path

Enable local file upload for the Codex Chrome extension:

`chrome://extensions` -> Codex extension -> Details -> enable `Allow access to file URLs`.

This repair path is no longer required for this run because the pasted-attachment workaround produced a valid Claude Chat Opus verdict.

## Boundary

This was not a content rejection from Claude. The application/web lane is now closed by `CLAUDE_CHAT_OPUS_FINAL_REVIEW_RESULT_20260606.md`; after post-review local source recovery, the remaining content boundary is only the one neutralized `needs_manual_source` entry in the defect ledger.
