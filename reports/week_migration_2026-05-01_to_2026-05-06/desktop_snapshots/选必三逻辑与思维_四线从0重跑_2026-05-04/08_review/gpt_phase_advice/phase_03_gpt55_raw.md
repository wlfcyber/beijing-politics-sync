# GPT-5.5 Pro Phase 03 Blocker Commander Reply

Capture note: ChatGPT web's visible "copy reply" control did not place the latest reply on the clipboard in this Safari session. The reply below was captured from the visible ChatGPT Pro page and Safari accessibility text. Supporting capture files are:

- `phase_03_gpt55_full_page_copy.md`
- `safari_ax_dump_phase03.tsv`

## Verdict

`GO_BUT_WITH_BLOCKERS`

GPT-5.5 Pro裁决：可以从 Phase03 进入 Phase04 的“补缺式证据融合 / 同类题归档”，但 Phase03 不能宣布 `full every-question coverage` 已完成。

下一阶段名称必须改为：

`Phase04 targeted evidence fusion with open coverage blockers`

## Allowed

1. 用 Codex A canonical 358 行作为 `every-question control base`。
2. 用 canonical in-scope/cross 119 行作为内容融合主控制表。
3. 对 A-only、B-only、高风险视觉题、推理题、主观题做 targeted independent verification。
4. 开始同类题归档，但只能归档到 evidence pool，不得进入学生稿。
5. 对思维部分和推理部分建立 `locked / pending / blocked` 三态体系。

## Still Forbidden

1. 学生稿。
2. Claude / Opus 成文化。
3. Word / PDF。
4. 最终 PASS。
5. 声称已穷尽北京全部可获得材料。
6. 声称 Lane B 已完成 every-question coverage。

## Why Not Full Go

不能用 `GO_TO_PHASE04_TARGETED_FUSION`，因为 B 线还有 14 unread sources、4 pending suites，A-only 76 个 in-scope/cross keys 尚未被独立复核，A 线刚完成去重拆分，choice-answer pairing、视觉/OCR 全页题号恢复仍未收口。

也不必退回 `STAY_IN_PHASE03_FULL_COVERAGE`，因为 A 线 canonical base 已经把 528 噪声矩阵压成 358 个原卷题目行，支撑材料已拆出，两个 P1 视觉点也已补锁。继续要求 B 短期复制 528 行矩阵会浪费时间，且不会自动提高成品质量。

## Phase04 Control Logic

Phase03 does not PASS.

Phase04 targeted fusion may start.

Student-facing production remains blocked.

Phase04 第一原则：

1. A canonical base controls completeness.
2. B targeted verification controls independence.
3. Governor controls whether unresolved A-only evidence can ever move forward.

## Lane B Targeted Verification Scope

Lane B 不需要复刻 528 行，但必须独立复核以下集合：

1. A-only in-scope/cross keys：76 个，全部复核。
2. B-only candidate keys：7 个，全部回源裁决。
3. A blocked rows：42 个，全部确认 blocked 原因。
4. A visual blockers 与 B visual blockers 的并集，全部视觉确认或继续 blocked。
5. 14 unread sources，至少做 source/suite 级补读，确认是否含 in-scope/cross 题。
6. 4 pending suites，必须给出 pending 原因、题量风险、是否影响 119 个主控制候选。
7. 所有推理主观题，全部复核。
8. 所有形式逻辑综合题，全部复核。
9. 所有选择题答案配对不稳的题，全部复核。
10. 所有 PPTX 内嵌图片、图形批注、学生答卷图片相关题，全部复核。

抽样哨兵：

1. A/B common keys 抽查不少于 15%。
2. A 判 out_of_scope 的 canonical rows 抽查不少于 10%。
3. 如发现系统性漏判，立即扩大到对应 suite 全量复核。

## A-only Handling

1. A-only + 高风险：必须 B targeted verify。
2. A-only + 主观题：必须 B targeted verify。
3. A-only + 推理题：必须 B targeted verify。
4. A-only + 选择题但答案/选项完整：可进 pending fusion，不可进 locked。
5. A-only + 无答案或无选项：blocked。
6. A-only + 视觉未核：blocked 或 pending_visual。

任何 A-only 题想进入未来学生稿，至少需要：

1. A raw source locator。
2. B targeted verification。
3. answer/rubric pairing。
4. scope classification。
5. Governor gate note。

## Next 5 Tasks

P0 任务 1：冻结 A canonical control base，并给每一行赋状态。

Required outputs:

- `phase04_control_base_status.csv`
- `phase04_canonical_358_index.md`
- `phase04_in_scope_cross_119_index.md`
- `phase04_support_reference_index.md`
- `phase04_removed_duplicates_log.md`

P0 任务 2：执行 Lane B targeted independent verification。

Required outputs:

- `phase04_laneB_targeted_verification_plan.md`
- `phase04_laneB_targeted_verification_results.csv`
- `phase04_Aonly_76_review.csv`
- `phase04_Bonly_7_review.csv`
- `phase04_unread_sources_patch.md`
- `phase04_pending_suites_patch.md`

P0 任务 3：完成 answer/rubric/visual 三重配对。

Required outputs:

- `phase04_answer_key_pairing_matrix.csv`
- `phase04_rubric_pairing_matrix.csv`
- `phase04_visual_confirmation_matrix.csv`
- `phase04_blocked_questions_final_for_phase04.csv`

P1 任务 4：推理部分先建 attachment matrix，再做同类题归档。

Required outputs:

- `phase04_reasoning_attachment_matrix.csv`
- `phase04_reasoning_typology_tree_observed.md`
- `phase04_reasoning_same_type_archive.md`
- `phase04_reasoning_logical_form_check.md`
- `phase04_reasoning_trap_action_matrix.md`

P1 任务 5：思维部分建立 signal-chain archive。

Required outputs:

- `phase04_thinking_signal_chain_matrix.csv`
- `phase04_thinking_method_archive.md`
- `phase04_thinking_answer_action_matrix.md`
- `phase04_thinking_optional_angle_pool.md`

## Student Draft Gates

思维部分不许进学生稿的硬门槛：

- 没有 stable locator。
- 题干、设问、材料不完整。
- 主观题没有答案依据、细则依据或讲评依据。
- 需要视觉确认但尚未 `visual_confirmed`。
- 只写知识点名称，没有材料信号。
- 只写材料复述，没有可写思维/方法。
- 只有答案结论，没有答题动作。
- 没有说明为什么从材料能想到该思维方法。
- 可选角度题被写成全部必答。
- 替代给分角度被写成唯一标准答案。
- 同一题多问没有拆成子题。
- 旧稿结论参与了内容判断。
- A/B 冲突未解决。
- `blocker_reason` 尚未清空。

推理部分不许进学生稿的硬门槛：

- 没有 stable locator。
- 题干或设问不完整。
- 选择题没有完整选项。
- 选择题没有可靠答案。
- 主观题没有评分点、讲评依据或可定位答案依据。
- 只标“推理部分”但没有具体题型。
- 只标“形式逻辑综合”但没有拆出具体规则。
- 没有 `logical_form`。
- 没有 `rule_slogan`。
- 没有 `valid_or_invalid_pattern`。
- 没有 `trap`。
- 没有 `answer_action`。
- 没有 `same_type_question_ids`。
- 一题多法没有 primary / secondary 挂载。
- A/B 对题型或答案存在冲突且未裁决。
- 视觉题未确认。
- 推理题没有进入 `reasoning_attachment_matrix`。
- `reasoning_attachment_matrix` 与同类题归档不一致。

## Two Visual Patch Rows

2026 丰台一模 Q18(2)：可以进入 `fusion evidence pool`，建议状态为 `LOCKED_FOR_FUSION / NO_STUDENT_DRAFT_YET`。

2025 海淀二模 Q20：可以进入 `fusion evidence pool`，建议状态为 `LOCKED_FOR_FUSION / OPTIONAL_ANGLE_POOL_CONFIRMED / NO_STUDENT_DRAFT_YET`。

## Final Warning

最大风险是把 Phase04 的“证据融合”误操作成“内容成文化”。必须坚持：

1. 先锁证据。
2. 再归同类。
3. 再写动作。
4. 最后才成文化。

## Required End-of-Phase04 Packet

- `phase04_control_base_status.csv`
- `phase04_laneB_targeted_verification_results.csv`
- `phase04_answer_key_pairing_matrix.csv`
- `phase04_rubric_pairing_matrix.csv`
- `phase04_visual_confirmation_matrix.csv`
- `phase04_thinking_signal_chain_matrix.csv`
- `phase04_reasoning_attachment_matrix.csv`
- `phase04_same_type_archive.md`
- `phase04_blocked_questions_final.csv`
- `phase04_Governor_interim_gate.md`
- `phase04_GPT_review_packet.md`

缺任何核心矩阵，禁止进入学生稿准备阶段。
