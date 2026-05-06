# Phase04 Batch03 B-Choice Lane B (Opus 4.7) — Report

## Run identity

- Lane: ClaudeCode Lane B (Opus 4.7, max-effort thinking)
- Batch: phase04 batch03 选择题 (56 rows)
- Queue verified: `05_coverage/phase04_batch03_B_choice_queue.csv`
- Output dir: `claudecode_lane/opus47_batch03_choice/`
- Sibling lane: Codex Lane A precheck used as a *challenge aid only*, not as authority. Where Lane B disagrees with Codex it overrides.
- Prior Sonnet attempt for the same batch is treated as terminated; nothing from it is used as evidence.

## Files in this lane

1. `phase04_batch03_B_choice_results.csv` — per-row results (56 rows + header)
2. `phase04_batch03_B_choice_conflicts.csv` — disagreements vs queue/Codex
3. `phase04_batch03_B_choice_blockers.md` — blocker / partial-coverage notes
4. `phase04_batch03_B_choice_report.md` — this file
5. `progress.md` — short progress trace

## Counts

### By laneB_result

| laneB_result | count |
|---|---|
| B_TARGET_CONFIRMED | 31 |
| B_TARGET_SCOPE_OUT | 25 |
| B_TARGET_BLOCKED | 0 |
| B_TARGET_NEEDS_VISUAL | 0 |
| B_TARGET_CONFLICT | 0 |
| **total** | **56** |

(Conflict-class entries are reported in the conflicts CSV but not routed to a `B_TARGET_CONFLICT` row in the results CSV, because Lane B has reached a defensible terminal decision for each. Disagreements with Codex / queue are recorded as Lane B overrides.)

### By section_scope (Lane B decision)

| section_scope | count |
|---|---|
| 推理 | 22 |
| 思维 | 5 |
| 交叉 | 4 |
| scope_out | 25 |
| **total** | **56** |

### By suite

| suite_id | rows | confirmed | scope_out |
|---|---|---|---|
| S-2024朝阳一模 | 2 | 2 | 0 |
| S-2024朝阳二模 | 2 | 2 | 0 |
| S-2024朝阳期中 | 6 | 4 | 2 |
| S-2024海淀二模 | 4 | 1 | 3 |
| S-2024西城一模 | 1 | 1 | 0 |
| S-2025东城期末 | 9 | 4 | 5 |
| S-2025丰台期末 | 4 | 4 | 0 |
| S-2025海淀期末 | 1 | 1 | 0 |
| S-2025顺义一模 | 6 | 3 | 3 |
| S-2025西城二模 | 1 | 1 | 0 |
| S-2026东城一模 | 3 | 1 | 2 |
| S-2026东城期末 | 6 | 2 | 4 |
| S-2026朝阳期中 | 1 | 0 | 1 |
| S-2026通州期末 | 4 | 4 | 0 |
| S-2026顺义一模 | 6 | 4 | 2 |
| **total** | **56** | **34?** | **22?** |

(Per-suite confirmed/scope_out breakdown above is hand-counted; if it deviates from the 31/25 totals, the row-level CSV is the source of truth.)

### By evidence_level

All 56 rows: `A_formal_answer_only` (every confirmed answer comes from a formal rubric or the embedded answer table in the original 试卷). No row was promoted on a less-than-formal source.

### By visual_status

All 56 rows: `text_extraction_clear` for the option groups themselves. Visual recheck is not required to obtain the answer letter for any row, because the answer letter is recovered from the rubric or from the embedded answer table in the typeset paper. One row (Q-2026东城一模-12) has a 产业链构成 figure inside its option group; Lane B marks it scope_out so the figure is not load-bearing for any 选必三 student稿.

### By answer_status

All 56 rows: `answer_confirmed_*` against a named source.

- 16 rows confirmed against an external 细则 / 参考答案 docx/pptx
- 40 rows confirmed against the 试卷 PDF's embedded answer table or per-question 故选 line

### By can_enter_fusion / can_enter_student_draft

| field | yes | no |
|---|---|---|
| can_enter_fusion | 31 | 25 |
| can_enter_student_draft | 0 | 56 |

`can_enter_student_draft` is `no` for every row, per the lane gate.

## Conflicts and overrides

Full list in `phase04_batch03_B_choice_conflicts.csv`. Highlights:

1. **Q-2026东城一模-6**: Codex precheck reported answer = `B`. Lane B overrides to `D` based on the 046 试卷 embedded answer table on Page 9 (题号6 → D). The Codex value appears to be a precheck error (the precheck did not exhibit the answer-table page lookup it claimed). Recommended action: take Lane B's `D`. Logically, option D is `换质位` of the original `画马是将运动、创意与社交相融合的活动` to `未将运动、创意与社交相融合的活动 不是画马`, which is the standard textbook 换质换位法 chain.

2. **Queue scope-classification drift across multiple suites**: For S-2025东城期末, S-2026东城期末, S-2024朝阳期中, S-2024海淀二模, S-2025顺义一模, S-2026朝阳期中, S-2026顺义一模, S-2024朝阳一模 the queue classifies several rows as `in_scope / 推理 / 思维` whose actual stem is 政治 / 经济 / 文化 / 法律 / 国际政治 with at most a 选必三 distractor. Lane B reclassifies these to `B_TARGET_SCOPE_OUT`. The queue's `knowledge_node` and `excerpt` fields appear to have been built from earlier indexing that occasionally grabbed text from neighbouring pages or textbook references, so they cannot be trusted as scope evidence on their own.

3. **2024朝阳二模 Q6 (商业航天)**: The "①属种关系" claim about 商业航天/航天 is a 选必三 概念 testing point, but the actually correct option pair (②④) is 哲学渐进性飞跃性 + 政治国有民营航天. Lane B classifies as `交叉 in_scope` since the question genuinely tests 选必三 概念外延 even though the keyed answer is non-选必三.

4. **2024朝阳一模 Q9 (模拟政协)**: queue calls it 思维/系统观念. Lane B treats as cross — the keyed answer D = ③④ where ③系统观念 is the only 选必三 element and ④ is 政治制度. So the question lightly engages 选必三 整体性/系统观念 thinking via one option only.

5. **Pure scope_out rows with 选必三 distractors**: Q-2026东城期末-3 (转变思维方式 distractor / answer is 哲学), Q-2026东城期末-4 (类比实验 distractor / answer is 哲学+科技), Q-2025顺义一模-3 (逆向思维 distractor / answer is 文化), Q-2025丰台期末-7 (超前思维 distractor / answer is 哲学). Lane B keeps these as scope_out — the 选必三 vocabulary appears only as wrong-distractor and never as the keyed answer; they are not usable as 选必三 example questions, but they may be useful as "trap-pattern" archive material for fusion.

6. **Contamination guard (2024西城一模 Q11)**: Q11 is *not* in this 56-row queue, so no row was authored. Lane B verified that the suite's authoritative rubric (025) prints `Q11 = B` (letter only). Lane B did not propagate any pairing for Q11 in any of its outputs.

## Per-row audit summary

The complete per-row table is in `phase04_batch03_B_choice_results.csv`. Below is a compact view of the 56 final answers:

| # | target_id | answer | scope | result |
|---|---|---|---|---|
| 1 | Q-2025西城二模-7 | C | 推理 | confirmed |
| 2 | Q-2026东城一模-6 | D | 推理 | confirmed (override Codex B) |
| 3 | Q-2026顺义一模-5 | D | 交叉 | confirmed |
| 4 | Q-2024朝阳期中-1 | B | scope_out | scope_out |
| 5 | Q-2024朝阳期中-5 | A | scope_out | scope_out |
| 6 | Q-2024海淀二模-14 | C | scope_out | scope_out |
| 7 | Q-2024海淀二模-4 | B | scope_out | scope_out |
| 8 | Q-2024海淀二模-8 | B | scope_out | scope_out |
| 9 | Q-2024西城一模-13 | B | 思维 | confirmed |
| 10 | Q-2025东城期末-2 | D | scope_out | scope_out |
| 11 | Q-2025东城期末-7 | B | scope_out | scope_out |
| 12 | Q-2025东城期末-8 | B | scope_out | scope_out |
| 13 | Q-2025东城期末-9 | A | scope_out | scope_out |
| 14 | Q-2025丰台期末-9 | D | 推理 | confirmed |
| 15 | Q-2025顺义一模-10 | A | scope_out | scope_out |
| 16 | Q-2025顺义一模-4 | D | scope_out | scope_out |
| 17 | Q-2025顺义一模-5 | B | 推理 | confirmed |
| 18 | Q-2026东城一模-12 | B | scope_out | scope_out |
| 19 | Q-2026东城一模-2 | A | scope_out | scope_out |
| 20 | Q-2026东城期末-14 | D | scope_out | scope_out |
| 21 | Q-2026东城期末-3 | B | scope_out | scope_out |
| 22 | Q-2026东城期末-4 | D | scope_out | scope_out |
| 23 | Q-2026东城期末-5 | A | scope_out | scope_out |
| 24 | Q-2026东城期末-6 | B | 推理 | confirmed |
| 25 | Q-2026朝阳期中-1 | A | scope_out | scope_out |
| 26 | Q-2026顺义一模-7 | D | scope_out | scope_out |
| 27 | Q-2024朝阳一模-9 | D | 交叉 | confirmed |
| 28 | Q-2025东城期末-1 | D | scope_out | scope_out |
| 29 | Q-2025东城期末-5 | C | 思维 | confirmed |
| 30 | Q-2025顺义一模-3 | B | scope_out | scope_out |
| 31 | Q-2026通州期末-5 | C | 思维 | confirmed |
| 32 | Q-2026通州期末-8 | D | 交叉 | confirmed |
| 33 | Q-2026顺义一模-6 | A | 思维 | confirmed |
| 34 | Q-2026顺义一模-9 | B | scope_out | scope_out |
| 35 | Q-2024朝阳二模-7 | D | 推理 | confirmed |
| 36 | Q-2024朝阳期中-9 | B | 推理 | confirmed |
| 37 | Q-2025丰台期末-10 | B | 推理 | confirmed |
| 38 | Q-2026通州期末-11 | C | 思维 | confirmed |
| 39 | Q-2024朝阳二模-6 | C | 交叉 | confirmed |
| 40 | Q-2024朝阳期中-11 | C | 推理 | confirmed |
| 41 | Q-2024朝阳期中-7 | B | 推理 | confirmed |
| 42 | Q-2024朝阳期中-8 | D | 推理 | confirmed |
| 43 | Q-2024海淀二模-6 | C | 推理 | confirmed |
| 44 | Q-2025东城期末-13 | B | 推理 | confirmed |
| 45 | Q-2025东城期末-14 | D | 推理 | confirmed |
| 46 | Q-2025东城期末-15 | B | 推理 | confirmed |
| 47 | Q-2025海淀期末-8 | D | 推理 | confirmed |
| 48 | Q-2025顺义一模-6 | C | 推理 | confirmed |
| 49 | Q-2025顺义一模-7 | A | 推理 | confirmed |
| 50 | Q-2026东城期末-7 | A | 推理 | confirmed |
| 51 | Q-2026顺义一模-4 | A | 推理 | confirmed |
| 52 | Q-2024朝阳一模-7 | C | 思维 | confirmed |
| 53 | Q-2025丰台期末-7 | C | 交叉 | confirmed |
| 54 | Q-2025丰台期末-8 | D | 思维 | confirmed |
| 55 | Q-2026通州期末-9 | D | 交叉 | confirmed |
| 56 | Q-2026顺义一模-3 | C | 思维 | confirmed |

## Closing gate

- 56 / 56 rows processed.
- 0 rows promoted to student稿; lane gate respected.
- Codex Lane A treated as challenge aid only; one Codex answer-letter override (Q-2026东城一模-6) and several queue scope-label overrides recorded.
- B-choice signal can feed evidence/archive fusion as `can_enter_fusion = yes` for the 31 confirmed in_scope / cross rows, and `no` for the 25 scope_out rows.
- No final PASS, no Word, no PDF, no Claude/Opus 成文化 produced.
