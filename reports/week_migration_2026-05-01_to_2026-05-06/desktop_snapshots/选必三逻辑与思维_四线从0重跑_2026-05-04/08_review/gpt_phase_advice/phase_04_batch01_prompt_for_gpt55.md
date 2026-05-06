你是 GPT-5.5 Pro，继续担任飞哥政治庄园四线工作流里的“总指挥/内容压力测试官”。请审阅 Phase04 Batch01 targeted verification 结果，裁决下一步 Batch02 怎么跑。

## 背景

任务：从0重跑北京高考政治 选必三《逻辑与思维》。思维部分要完全模仿哲学宝典；推理部分必须按题型挂载所有题。

当前 run folder：

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

你上次裁决为：

`GO_BUT_WITH_BLOCKERS`

阶段名：

`Phase04 targeted evidence fusion with open coverage blockers`

继续禁止：学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。

## Phase04 Batch01 已完成

### Codex A

已生成：

- `05_coverage/phase04_control_base_status.csv`
- `05_coverage/phase04_control_base_status_after_laneB_batch01.csv`
- `06_conflicts/phase04_batch01_codexA_laneB_reconciliation.md`
- `05_coverage/phase04_answer_key_pairing_matrix.csv`
- `05_coverage/phase04_rubric_pairing_matrix.csv`
- `05_coverage/phase04_visual_confirmation_matrix.csv`
- `05_coverage/phase04_reasoning_attachment_matrix.csv`
- `05_coverage/phase04_thinking_signal_chain_matrix.csv`
- `05_coverage/phase04_same_type_archive.md`
- `05_coverage/phase04_Governor_interim_gate.md`

### ClaudeCode Lane B Batch01

交付：

- `claudecode_lane/phase04_laneB_targeted_verification_plan.md`
- `claudecode_lane/phase04_laneB_targeted_verification_results.csv`
- `claudecode_lane/phase04_Aonly_76_review_batch01.csv`
- `claudecode_lane/phase04_Bonly_7_review_batch01.csv`
- `claudecode_lane/phase04_unread_sources_patch.md`
- `claudecode_lane/phase04_pending_suites_patch.md`
- `04_suite_reports/claudecode_suite_reports/phase04_laneB_targeted_verification_batch01_report.md`

## 当前合并状态

`phase04_control_base_status_after_laneB_batch01.csv` counts:

- `L0_BLOCKED`: 236
- `L1_A_ONLY_PENDING_B_TARGET`: 114
- `L2_PENDING_SCOPE_DECISION`: 1
- `L3_A_PLUS_B_TARGET_CONFIRMED`: 3
- `L4_LOCKED_FOR_FUSION`: 4

in-scope/cross control rows are now 120 because Batch01 found `2026朝阳期中 Q12` should be added from `待判` into 推理.

## Important Confirmed Rows

`L4_LOCKED_FOR_FUSION` but still `NO_STUDENT_DRAFT_YET`:

- `2025海淀二模 Q20`: 辩证思维角度池，非三点全必答。
- `2026丰台一模 Q18(2)`: 必要条件假言推理 + 三段论大项不当扩大。
- `2025西城二模 Q16(2)`: 充分条件假言推理，肯定后件不能确定前件。
- `2025西城二模 Q16(3)`: 创新思维，改变创造条件、建立新联系。

`L3_A_PLUS_B_TARGET_CONFIRMED`:

- `2026朝阳期中 Q11`: 三段论补大前提，答案 A，证据等级 B-choice-signal。
- `2026朝阳期中 Q12`: 逻辑规则/选言判断等，答案 B，Batch01 report 发现并纠正 Codex 待判遗漏。
- `2026朝阳期中 Q13`: 感性具体 -> 思维抽象 + 联想思维，答案 D，证据等级 B-choice-signal。

`L2_PENDING_SCOPE_DECISION`:

- `2025海淀期末 Q2`: 答案 C，②场景迁移/联想思维，③辩证思维整体性；但①是哲学扬弃诱惑项，需裁 scope。

## 当前冲突/阻塞

1. `2024西城一模 Q11`
   - Lane B: marked `B_TARGET_BLOCKED` because it saw options as image-embedded and unavailable.
   - Codex A after Lane B prompt: recovered all four options from Word XML text boxes and answer B from 025/026.
   - Current status: keep pending B recheck, not locked.

2. `2025海淀二模 Q12/Q13`
   - Lane B: marked scan-blocked.
   - Codex A after Lane B prompt: visually read `008 ... page_04.png` and recovered full options for Q12/Q13.
   - Answer source still not found in 009/010/011.
   - Current status: full options recovered, answer missing; blocked until answer source/B recheck.

3. `2026丰台一模 suite`
   - Q18(2) locked, but suite-level still visual-blocked because 042 scan text is blank/thin.
   - Need visual reading of 042 full suite to ensure no choice questions or other selected-compulsory-three rows were missed.

4. `2026朝阳期中 Q14/Q15`
   - Lane B confirmed answers B/D, but CSV marked `can_enter_fusion=no`.
   - Need decide whether to treat them as L3 after additional formal pairing or keep pending.

## Please裁决

请严格回答：

1. Batch01 是否合格？是否允许进入 Batch02？
2. Batch02 的 P0 顺序应该是什么？请在以下候选中排序：
   - 2024西城一模 Q11 B线复核 Codex XML textbox recovery；
   - 2025海淀二模 Q12/Q13 视觉选项 + answer source 补找；
   - 2026丰台一模 042 renders 全套视觉题号/选必三选择题清点；
   - 2026朝阳期中 Q12 正式补入控制表并让 B 线写 results CSV row；
   - 2026朝阳期中 Q14/Q15 是否可从 B-choice-signal 升为 L3；
   - 2025海淀期末 Q2 scope decision；
   - 其余 A-only 114/116 行如何分批。
3. 对 `2024西城一模 Q11`，如果 Codex A 能从 Word XML 直接提取四个文本框选项，这是否可以替代视觉截图？还是仍必须让 B 做独立复核后才能进入 fusion？
4. 对 `2025海淀二模 Q12/Q13`，有完整选项但无答案源，是否应保持 blocked？是否允许用题目逻辑推答案？
5. 对 `2025海淀期末 Q2`，scope 如何裁？思维部分、边界交叉，还是不入？
6. 是否允许在 Batch02 后开始“推理题型归档正文骨架”（仍非学生稿），还是必须先把所有 A-only 114 行核完？
7. 给出短 verdict：
   - `GO_TO_BATCH02_VISUAL_AND_SCOPE_REPAIR`
   - `STAY_IN_BATCH01_FIX_MERGE`
   - `STOP_AND_REBUILD_CONTROL_BASE`

请继续记住：最终目标是哲学宝典级质量，绝不快速糊一份。
