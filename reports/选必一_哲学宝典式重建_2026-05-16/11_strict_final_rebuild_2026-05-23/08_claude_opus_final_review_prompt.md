# Claude Opus final adaptive review and improvement

You are the final Claude Opus review/improvement lane for the Xuanbiyi strict final rebuild.
Use high effort. The command launching you uses `claude -p --model opus --effort max`.

## Context

GPT Pro was genuinely submitted through the logged-in ChatGPT Pro web UI multiple ways:
- full prompt text
- compact prompt text
- uploaded files plus short prompt
- 5-entry batch prompt
The UI repeatedly returned only the single character `?` or stalled for long periods, while a short `OK` ping worked. Treat GPT Pro as attempted but no effective output. Do not claim GPT Pro produced content.

Your job now is to review Codex independent thick draft and ClaudeCode independent thick draft, then produce the final strict fusion patch that Codex can merge and verify.

## Inputs

Read:
- `reports/???_???????_2026-05-16/11_strict_final_rebuild_2026-05-23/05_codex_drafts/CODEX_INDEPENDENT_THICK_DRAFT.md`
- `reports/???_???????_2026-05-16/11_strict_final_rebuild_2026-05-23/06_claudecode_independent_opus47/CLAUDECODE_INDEPENDENT_THICK_DRAFT.md`
- `reports/???_???????_2026-05-16/11_strict_final_rebuild_2026-05-23/06_claudecode_independent_opus47/CLAUDECODE_INDEPENDENT_RISK_LOG.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

Output directory:
`C:/Users/Administrator/Desktop/02_代码项目与工具/mac-thread-restore/beijing-politics-sync-visible/reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/08_claude_opus_final_review`

## Hard rules

1. Only subjective questions and only Xuanbiyi scoring points.
2. Main entries require scoring rubric / marking rule / rubric PPT / lecture scoring material / user-confirmed rubric. Ordinary answer keys must be downgraded.
3. Every case must be single-question independent. Do not merge two source questions into one heading or one example.
4. Preserve scoring-source terms. Do not invent broad umbrella terms after `??????`.
5. Bucket boundaries:
   - new-type international relations / international relations democratization / true multilateralism / fair and reasonable international order -> political multipolarity.
   - independent foreign policy of peace / Five Principles of Peaceful Coexistence / independent basic stance -> China.
   - economic globalization internal grouping must be expression-sensitive.
6. Where Codex and ClaudeCode conflict, decide from source evidence and write the conflict note.
7. If evidence is insufficient, write `NEEDS_EVIDENCE`; do not force inclusion.

## Required outputs

Write exactly these files:

1. `CLAUDE_OPUS_FINAL_FUSION_PATCH.md`
   - The final accepted entries only, organized by the six buckets.
   - Use the student-handbook field labels: `??????`, `??????` if needed, `???????`, `????`, `????????`, `??????`, `??????`, `????`.
   - Each source question must stay as its own example. No heading may contain `?` or combine two source questions.

2. `CLAUDE_OPUS_FINAL_REJECT_DOWNGRADE.md`
   - Rejected, downgraded, and NEEDS_EVIDENCE list.

3. `CLAUDE_OPUS_FINAL_REVIEW_SUMMARY.md`
   - Counts by bucket, conflict decisions, and merge instructions.

Print stdout with counts: accepted entries, rejected/downgraded, needs evidence, and whether any merged heading remains.
