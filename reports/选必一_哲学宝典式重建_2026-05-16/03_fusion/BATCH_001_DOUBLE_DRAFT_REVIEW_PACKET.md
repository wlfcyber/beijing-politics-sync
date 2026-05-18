# Batch 001 Double-Draft Review Packet

## Correct Workflow

This packet follows the corrected sequence:

1. Codex production lane A creates an initial draft.
2. ClaudeCode production lane B creates an independent initial draft from the same source packet.
3. GPT and Claude review both drafts against the original source evidence.
4. Codex adjudicates every review issue against the source before any final merge.

The aborted earlier Claude review attempt is not counted because it reviewed only the Codex draft and used the wrong sequence.

## Files To Review

Source evidence:

- `reports/选必一_哲学宝典式重建_2026-05-16/01_source_packets/BATCH_001_SOURCE_PACKET.md`

Draft A:

- `reports/选必一_哲学宝典式重建_2026-05-16/02_codex_batches/BATCH_001_CODEX_DRAFT.md`

Draft B:

- `reports/选必一_哲学宝典式重建_2026-05-16/02_claudecode_batches/BATCH_001_CLAUDECODE_DRAFT.md`

Rules:

- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

## Batch 001 Questions

1. 2026 通州期末 Q20
2. 2026 朝阳期中 Q17
3. 2025 海淀期中 Q16(2)
4. 2025 海淀期中 Q21(2)
5. 2024 东城一模 Q16

## Review Questions

1. Which draft is more source-faithful for each question?
2. Which draft has better student-facing answer language?
3. Did either draft invent a term not supported by the source?
4. Did either draft misread scoring hierarchy, especially:
   - 2026 通州期末 Q20 six rubric points,
   - 2026 朝阳期中 Q17 three total/detail layers,
   - 2025 海淀期中 Q16(2) selected 2-point 选必一 chain,
   - 2025 海淀期中 Q21(2) 变/不变 hierarchy,
   - 2024 东城一模 Q16 cross-module boundary.
5. Which entries should be merged, deleted, downgraded to boundary notes, or kept as expression variants?

## Required Output Format

Use this table:

| issue_id | severity | question_id | draft | entry_term | diagnosis | source_basis | recommended_action |
|---|---|---|---|---|---|---|---|

Severity values:

- `must_fix_source`
- `must_fix_rubric`
- `must_fix_module_boundary`
- `should_fix_teaching`
- `keep_best_of_both`
- `note`

## Review Boundaries

- Do not directly rewrite the final document.
- Do not add new terms without a source basis.
- Do not count ordinary reference answers as rubrics.
- Reviewer opinions are advisory. Codex must adjudicate them against source evidence before fusion.
