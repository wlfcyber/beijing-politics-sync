# External Model Safe Interaction SOP

Created: 2026-05-05

This file is now a hard workflow rule for the current four-line 选必三 run.

## Why This Exists

The GPT-5.5 Pro web lane was interrupted multiple times by operator error. Any stopped GPT thinking attempt is invalid and must not be counted as review, approval, or closure.

## Hard Rules

1. Codex must not click GPT's send/stop button by coordinate.
2. Codex must not use the same visible button area for both submit and stop.
3. Codex must not interact with the ChatGPT page while the page shows thinking, generating, stopping, or a similar in-progress state.
4. Codex must not submit a second message into an unfinished GPT response.
5. Codex must not treat a stopped, paused, quota-blocked, or partial GPT response as valid review.
6. Codex must not let GPT availability block safe local source work, but final promotion remains blocked until a real usable GPT review is captured or the user explicitly waives that exact gate.

## New GPT Lane Procedure

Codex only prepares the package locally:

- `08_review/gpt_phase_advice/phase_11D_seed_plus_batch02_prompt_for_gpt55.md`
- screenshots/evidence notes if needed
- exact expected GPT output schema

Submission options are now ordered as follows:

1. Preferred: the user manually submits the prepared prompt to GPT-5.5 Pro, then Codex captures and digests the completed reply.
2. Allowed only if the user explicitly re-authorizes Codex to operate the page: Codex uses accessibility elements only, not coordinates, and stops immediately if the send/stop state is ambiguous.
3. If no safe accessibility send path is available, Codex logs `real_gpt_pending_manual_submit` and continues local work that does not require GPT promotion.

## Capture Procedure

After GPT completes:

1. Copy the complete GPT answer once.
2. Save raw reply to `08_review/gpt_phase_advice/phase_11D_seed_plus_batch02_gpt55_raw.md`.
3. Write digest to `08_review/gpt_phase_advice/phase_11D_seed_plus_batch02_gpt55_digest.md`.
4. Convert every GPT issue into a local evidence task before patching.
5. Do not proceed to Opus, Governor, Word, or final delivery if unresolved `must_fix_content` remains.

## Current Status

- GPT Phase11D attempts before this SOP are invalid if stopped.
- Current prompt is prepared locally but not safely completed by GPT.
- Gate state: `real_gpt_pending_manual_submit_or_safe_reauth`.
