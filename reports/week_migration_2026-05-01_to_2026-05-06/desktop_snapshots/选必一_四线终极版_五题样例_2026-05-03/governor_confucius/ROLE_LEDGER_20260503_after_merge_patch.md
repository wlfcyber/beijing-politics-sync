# Garden Role Ledger After Merge Patch

time: 2026-05-03 18:10 CST

## Scope

This ledger covers the post-review wording/workflow patch after the user pointed out that same-core terms were over-merged or under-merged in the six-bucket index.

Changed student artifact:

- `delivery/选必一_五题样例_学生版.md`

## Role Status

| Role | Status | Evidence |
|---|---|---|
| Codex local controller | RUN | Applied the same-core merge rule, repaired the economic-globalization core wording, updated skill rules, and synchronized `delivery/` plus `fusion/`. |
| Codex production lane A | RUN | Edited the student Markdown and workflow rules directly; no new source claim was introduced. |
| ClaudeCode production lane B | NOT_RERUN_FOR_THIS_PATCH | Existing five-question ClaudeCode lane remains in `claudecode_lane/`. This patch changed student-facing grouping/wording only and did not add new source evidence or new题目. |
| Claude Opus 4.7 Adaptive | NOT_RERUN_FOR_THIS_PATCH | Existing real Claude review remains saved in `opus_writer/web_external/claude_opus47_adaptive_web_review.md`. The latest delta is a user-directed merge-rule correction, not a new prose rewrite requiring Opus. |
| ChatGPT web Pro / GPT-5.5 Pro lane | NOT_RERUN_FOR_THIS_PATCH | Existing real ChatGPT web review remains saved in `gpt55_review/web_external/gpt55_pro_web_review.md`. The latest delta implements user feedback and local evidence boundaries. |
| Governor | RUN | See `governor_confucius/Governor_patch_gate_20260503_after_merge_patch.md`. |
| Confucius | RUN | See `governor_confucius/Confucius_artifact_only_20260503_after_merge_patch.md`. |

## Rule Patch

The Garden workflow now explicitly requires visible role traces even for Codex solo or narrow continuation work:

- `feige-politics-garden/SKILL.md`
- `feige-politics-garden-book-orchestrator/SKILL.md`

The 选必一 workflow also now requires same-core merging while preserving the highest-information scoring wording:

- `feige-politics-garden-xuanbiyi/SKILL.md`
- `feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## Closure Note

The latest student-facing artifact change invalidated the old Confucius report for `delivery/final_loop/选必一_五题闭环终版.md`. A fresh artifact-only Confucius pass was therefore run against `delivery/选必一_五题样例_学生版.md`.
