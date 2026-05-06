# ClaudeCode Thread Routing - 2026-05-05

## Current Rule

There are now two separate ClaudeCode surfaces. They must not write the same files.

## Lane T1 - Codex-Supervised Terminal ClaudeCode

- Surface: Terminal visible window opened by Codex.
- Process pattern: `claude --model opus --effort max --permission-mode bypassPermissions`
- Current task: Phase11C bad Word content failure audit.
- Current status: completed and received; seven files landed under `claudecode_lane/phase11C_bad_word_content_audit_visible/`; digest at `08_review/phase11C_visible_claudecode_output_digest.md`.
- Work directory: `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- Prompt file: `08_review/claudecode_phase11C_visible_bad_word_rewrite_prompt.md`
- Write scope:
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/`
- Must not edit:
  - `09_student_draft/`
  - `09_delivery/`
  - any Word/PDF/final artifact
  - files owned by VSCode ClaudeCode lane

## Lane V1 - User-Opened VSCode ClaudeCode

- Surface: VSCode opened by the user.
- Status: user reported it is separate from the Terminal lane.
- Current observed status 2026-05-05 14:45 CST: visible VSCode ClaudeCode session is working on a different 选必二《法律与生活》 C-line/framework task; no files exist yet under `claudecode_lane/vscode_lane_phase11C/`.
- Current receiving rule: do not count VSCode ClaudeCode as a 选必三 lane until it writes the current-lane output path or the user names a different 选必三 output path.
- Default write scope until explicitly changed:
  - `claudecode_lane/vscode_lane_phase11C/`
- Recommended task: independent critique or sample rewrite only, not the same output files as T1.
- Must not edit:
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/`
  - `codex_lane/phase11C_bad_word_content_audit/`
  - `09_student_draft/`
  - any Word/PDF/final artifact

## Conflict Rule

If both lanes propose changes to the same content, neither lane merges. Codex records the conflict under `06_conflicts/` and makes the local source-evidence decision.

## Current Final Gate

No Word/PDF/final/终稿/宝典成品 until Phase11C content gate passes:

- real prompts;
- concrete material triggers;
- clear trigger logic;
- direct student answer sentences;
- no template prompts;
- no production-instruction answer landings;
- no same-question multi-node copy-paste.
