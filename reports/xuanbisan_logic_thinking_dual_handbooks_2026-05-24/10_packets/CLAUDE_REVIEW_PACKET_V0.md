# Claude External Review Packet V0

Status: `prepared_not_submitted`

This packet is for a separate Claude reviewer lane. It must not be confused with ClaudeCode B-line production.

## Review Target

Run directory:

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`

Read these first:

- `TASK_BRIEF.md`
- `DEVELOPMENT_PLAN.md`
- `PROGRESS.md`
- `04_fusion/A_B_DIFF_SNAPSHOT.md`
- `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md`
- `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md`
- `03_claudecode_lane/blocked_or_boundary.md`
- `03_claudecode_lane/fusion_candidates.csv`
- `03_claudecode_lane/blockers.csv`

Then spot-check evidence:

- `02_codex_lane/HARD_SAMPLE_SOURCE_PACKETS.md`
- `02_codex_lane/FAMILY_SOURCE_PACKETS_Q0006_Q0012.md`
- `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0013_Q0017.md`
- `01_source_inventory/QUESTION_COVERAGE_MATRIX.csv`

## Required Review

You are a separate external reviewer. Your job is to catch overclaim, source drift, wrong module routing, and weak teaching usability.

Check:

1. Do the two review drafts obey the user instruction: 思维部分对齐必修四宝典制作质量，讲触发；推理部分同一推理形式汇总？
2. Are any `A-formal` rows actually not formal enough?
3. Are any B-line high-confidence rows missing from Codex A source-lock priority?
4. Are any blocker rows incorrectly allowed into review drafts?
5. What is the fastest path from current review drafts to a safe next version?

## Output Format

Write `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V0.md` with:

- Verdict.
- Findings table: severity, file, issue, required fix.
- Coverage pressure list.
- Fusion recommendations.
- Forbidden final claims.

Do not write PASS.
