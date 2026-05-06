# Four-Line Closure Gate

Created: 2026-05-05 15:04 CST

This gate records the user's renewed instruction: the current 选必三《逻辑与思维》run must close through all four real lanes before Word/final delivery.

## Required Lanes

1. Codex production/control lane
   - Codex must source-check, rebuild, fuse, patch, govern, and create the final artifacts.
   - Codex may not act only as dispatcher.

2. ClaudeCode visible production/review lane
   - Terminal T1 visible ClaudeCode must provide independent worker outputs in its own lane folder.
   - Current T1 active task: `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/`.
   - VSCode ClaudeCode remains a separate lane and must not be mixed unless the user explicitly assigns it to this project.

3. GPT-5.5 Pro content-review lane
   - Must be a real ChatGPT web Pro call in the visible conversation `高考政治四线工作流`.
   - Required for Phase11D seed review and later final content review.
   - If stopped, quota-blocked, unavailable, or not captured, status is `real_call_pending`; do not promote.

4. Claude Opus 4.7 Adaptive Thinking teaching-text lane
   - Must be a real Claude/Opus 4.7 Adaptive Thinking call in the visible Claude app/web lane, not Codex roleplay.
   - Runs after evidence/source lock and before final Markdown/Word delivery.
   - Opus may improve student-facing wording and structure, but any new claim returns to Codex source verification.

## Hard Blocking Rules

- No `.docx`, `.pdf`, `final`, `终稿`, `最终稿`, `宝典成品`, or final `PASS` until all four lanes are present and reconciled.
- GPT and Claude Opus are not source authorities. Their corrections must be accepted, rejected, or blocked by Codex with local source evidence.
- ClaudeCode output is worker evidence, not merge authority.
- The failed Word/Markdown from `选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04` remains a failure sample only.
- Any interrupted GPT/Claude/ClaudeCode call must be explicitly retried or marked `real_call_pending`; no silent closure.

## Current Status

- Codex: Phase11D local source-rebuild has produced a 29-entry source-verified review packet and passed the mechanical four-element gate.
- ClaudeCode T1: Phase11D visible seed audit and next-batch queue completed under `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/`; output has been digested as worker evidence, not merge authority.
- GPT-5.5 Pro: Phase11D seed review was submitted but the web response was interrupted/stopped; a later continuation attempt was also stopped by operator error. Full retry/continuation is required before promotion.
- Claude Opus 4.7 Adaptive Thinking: combined18 and combined29 passes completed in the visible Claude desktop app. The combined29 raw summary and 11-point concern list were captured/digested; the full artifact copy action mis-captured the original prompt and was quarantined. Codex source reconciliation resolved or constrained the 11 Opus concerns in `08_review/opus_writer/phase_11D_combined29_opus47_reconciliation.md`.
- Phase11E candidate Word: Codex generated a 29-entry candidate Markdown/DOCX, opened it in Microsoft Word, updated fields, saved, exported a 23-page PDF, rendered page PNGs, spot-checked images/options/watermark/TOC, and wrote `governor_confucius/phase11E_candidate_governor_precheck.md`. This is still a candidate, not final.

Gate verdict: `FOUR_LINE_CLOSURE_REQUIRED_NO_FINAL_UNTIL_ALL_REAL_LANES_CLOSED`.

## External Model Safety Patch

Created: 2026-05-05 15:25 CST

- New hard procedure: `00_control/EXTERNAL_MODEL_SAFE_INTERACTION_SOP_2026-05-05.md`.
- GPT web submission attempts that are stopped by Codex operator error are invalid.
- Codex must not click GPT send/stop by coordinate again.
- Current GPT Phase11D prompt may only be submitted by user manual action, or by a later explicitly re-authorized accessibility-only path where the send/stop state is unambiguous.
- Until a complete GPT raw reply is captured, GPT lane status remains `real_gpt_pending_manual_submit_or_safe_reauth`.
