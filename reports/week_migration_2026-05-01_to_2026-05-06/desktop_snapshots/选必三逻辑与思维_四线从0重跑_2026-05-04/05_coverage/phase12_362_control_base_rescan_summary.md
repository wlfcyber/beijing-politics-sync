# Phase12 362 Control Base Rescan Summary

Status: `REVIEW_ONLY_362_RESCAN_DONE_NO_WORD_NO_FINAL`

本文件记录 362-row control base 回扫的最终分类。它不授权 Word/PDF/final，也不把当前扩展稿命名为终稿。

## Counts

- total control-base rows: 362
- already_in_74: 74
- new_body_candidate: 3
- answer_missing: 134
- visual_missing: 32
- out_of_scope: 104
- duplicate: 0
- blocked: 15

## Body Impact

- 74-row review-only body remains fully represented.
- new source-confirmed rows added from 362 rescan: 3
- expanded review-only body rows after 362 rescan: 77
- 主观题: 27
- 选择题: 50
- 当前目标 90-120 未强行凑数：本轮只把证据闭合的新增题进 review-only；答案缺口或视觉缺口继续 blocked。

## New Body Candidates

- `Q-2024朝阳一模-6` | 2024 朝阳一模第6题 | answer=B | paper:030 lines 71-75; commentary:032 lines 106-111 gives B and option diagnoses
- `Q-2025西城二模-6` | 2025 西城二模第6题 | answer=C | paper:037 lines 61-64; answer key:037 line 306 / 038 line 5 gives 6.C
- `Q-2026通州期末-10` | 2026 通州期末第10题 | answer=B | paper text:006 lines 138-143; render page_04 shows four statements; answer table:006 lines 307-329 gives Q10=B

## New But Blocked

- `Q-2024朝阳期中-10` | answer_missing | 题干显然涉及概念外延/关系判断，但本轮只找到试卷题面，未找到可靠选择题答案表；不得逻辑猜答案。

## Action Counts

- blocked_keep_out: 181
- excluded_keep_out: 104
- covered_by_74_review_body: 74
- body_after_362_repair: 3

## Output Files

- `05_coverage/phase12_362_control_base_rescan_matrix.csv`
- `05_coverage/phase12_362_new_candidate_repair_queue.csv`
- `09_student_draft/phase12_362_new_entries_REVIEW_ONLY.md`
- `09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md`
- `09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv`
- `09_student_draft/phase12_expanded_body_FROM_362_gap_backcheck.csv`

## Remaining Gate

- 双索引尚未生成。
- Codex/ClaudeCode/GPT/Governor/Confucius 验收尚未完成。
- Word/PDF/final 仍禁止。
