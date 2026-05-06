你是 ClaudeCode Lane B，继续参与飞哥政治庄园-选必三《逻辑与思维》四线从0重跑。你不是唯一工作者；Codex Lane A 已冻结 Phase04 控制底座。请不要覆盖 Codex Lane A 的输出，不要写学生稿，不要让 Opus 成文化，不要生成 Word/PDF，不要宣称 PASS。

## 当前阶段

Run folder:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

GPT-5.5 Pro Phase03 裁决为：

`GO_BUT_WITH_BLOCKERS`

下一阶段名称必须是：

`Phase04 targeted evidence fusion with open coverage blockers`

允许进入 evidence fusion / same-type archive / targeted verification；继续禁止学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。

## 必读控制文件

1. `08_review/gpt_phase_advice/phase_03_gpt55_digest.md`
2. `05_coverage/phase04_control_base_status.csv`
3. `05_coverage/phase04_in_scope_cross_119_index.md`
4. `06_conflicts/phase03_post_patch_gap_queue.csv`
5. `06_conflicts/phase03_P0_evidence_notes_codex.md`
6. `05_coverage/phase03_codex_local_patch_addendum.csv`
7. `claudecode_lane/phase03_laneB_patch_addendum.csv`
8. `05_coverage/phase04_answer_key_pairing_matrix.csv`
9. `05_coverage/phase04_rubric_pairing_matrix.csv`
10. `05_coverage/phase04_visual_confirmation_matrix.csv`

## 你的任务：Phase04 Targeted Verification Batch 01

本批次只做 P0/最高风险补缺，不做全书学生稿。

### A. 写 targeted verification plan

写：

`claudecode_lane/phase04_laneB_targeted_verification_plan.md`

必须把 GPT 要求的 Lane B targeted 范围列成批次：

- A-only in-scope/cross keys 76 个。
- B-only candidate keys 7 个。
- A blocked rows 42 个。
- visual blockers union。
- 14 unread sources。
- 4 pending suites。
- 所有推理主观题。
- 所有形式逻辑综合题。
- 所有选择题答案配对风险题。
- 所有 PPTX 内嵌图片、图形批注、学生答卷图片相关题。

但本次执行优先 Batch 01：P0 gap queue + Codex local patch addendum + 两个 Lane B focused patch rows 的状态复核。

### B. 独立复核 Batch 01

请回源复核下列对象，不要只复述 Codex 结论：

1. `2024西城一模 Q11`
   - 目标：确认题干/选项/答案/逻辑归属；若 Word/PDF 文本抽取缺选项，必须标记视觉/Word渲染 blocker，不可猜。
2. `2025海淀二模 Q12`
3. `2025海淀二模 Q13`
   - 目标：确认是否推理选择题、完整选项、答案来源、是否仍需视觉核读。
4. `2025海淀期末 Q2`
   - 目标：确认是否思维部分、哲学边界或应排除；若图/选项缺失则 blocked。
5. `2025西城二模 Q16(2)`
   - 目标：独立确认充分条件假言推理，后件真不能确定前件真。
6. `2025西城二模 Q16(3)`
   - 目标：独立确认创新思维，而不是推理；按子问拆分解决 A/B 冲突。
7. `2025西城二模 Q7`
   - 目标：确认是否推理选择题、完整选项、答案来源；视觉/选项不全则 blocked。
8. `2026丰台一模 suite-level PENDING`
   - 目标：不要只确认 Q18(2)，还要说明本套题是否仍有其他选必三题未解析风险。
9. `2026朝阳期中 Q11/Q13/Q14/Q15`
   - 目标：独立确认原卷题干、完整选项、答案表配对 A/D/B/D 是否可靠；给出推理/思维/交叉分类与陷阱。
10. `2025海淀二模 Q20` 和 `2026丰台一模 Q18(2)`
    - 目标：确认它们维持 `LOCKED_FOR_FUSION`，但明确仍然 `NO_STUDENT_DRAFT_YET`。

## 必写输出

1. `claudecode_lane/phase04_laneB_targeted_verification_plan.md`

2. `claudecode_lane/phase04_laneB_targeted_verification_results.csv`

字段：

`target_id,suite,qno,source_locator,question_type,section_scope,laneB_result,evidence_level,visual_status,answer_status,rubric_status,reasoning_or_thinking_node,logical_form,rule_slogan,trap_or_boundary,can_enter_fusion,can_enter_student_draft,blocker_reason,notes`

`laneB_result` 只能是：

- `B_TARGET_CONFIRMED`
- `B_TARGET_DISAGREES`
- `B_TARGET_BLOCKED`
- `B_TARGET_NEEDS_VISUAL`
- `B_TARGET_SCOPE_OUT`

3. `claudecode_lane/phase04_Aonly_76_review_batch01.csv`

只写本批次涉及到的 A-only 行，字段同上；未处理的 A-only 76 不要假装完成，写入 plan 的 remaining 队列。

4. `claudecode_lane/phase04_Bonly_7_review_batch01.csv`

本批次若涉及 B-only 行则写入；否则写表头并说明 no Batch01 row。

5. `claudecode_lane/phase04_unread_sources_patch.md`

本批次至少列出 14 unread sources 的 source_id/name/read-risk，并说明 Batch02 该如何补读。

6. `claudecode_lane/phase04_pending_suites_patch.md`

列出 4 pending suites、风险、是否可能影响 119 个 in-scope/cross 控制候选。

7. `04_suite_reports/claudecode_suite_reports/phase04_laneB_targeted_verification_batch01_report.md`

8. 在 `claudecode_lane/progress.md` 顶部追加 Batch01 记录。

## 硬规则

- 只要缺完整四个选项，选择题就不能进入学生稿。
- 只要无可靠答案来源，选择题就不能进入学生稿。
- 只要主观题无设问/评分落点，主观题就不能进入学生稿。
- 视觉未确认的题不能 locked。
- A-only 题不能因为 Codex 已写就自动 locked。
- 你可以把题确认到 evidence fusion，但必须写 `can_enter_student_draft=no`。
- 不要生成学生版正文。
- 不要写“最终完成”。
