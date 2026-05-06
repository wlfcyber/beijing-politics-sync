# 给 GPT-5.5 Pro：Phase04 Batch03 A-only 队列完成后的 Commander Review

你是本项目的 GPT-5.5 Pro 总指挥 / 内容审稿人。请只基于我下面提供的状态判断下一步，继续保持严格门禁。

本项目：北京高考政治 选必三《逻辑与思维》从 0 重跑，目标最终做成类似此前“哲学宝典”的终极教研文档，但当前仍在 evidence-control 阶段。

总规则：

1. Codex A、ClaudeCode B、GPT-5.5 Pro、Claude/Opus 四线工作流。
2. Codex 不只是总控，也要自己跑；ClaudeCode 是独立生产/复核线。
3. 旧成果只可定位，不继承旧结论。
4. 思维部分要模仿哲学宝典：材料信号 → 思维/方法 → 答题动作 → 来源例题。
5. 推理部分要按题型分类：三段论、假言推理、选言/联言、归纳/类比、概念/判断等，每类下面穷尽所有题。
6. 所有 PDF、Word、PPT、图片、扫描、表格、漫画/图示都必须调用工具处理，不得因工具缺失放弃。
7. 当前禁止：学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。

## GPT 上次裁决

你在 Batch02 后裁决为：`GO_TO_BATCH03_AONLY_QUEUE`。

要求：

- 必须处理剩余 `L1_A_ONLY_PENDING_B_TARGET=112`。
- Batch02 只算 targeted visual/scope repair。
- 继续禁止学生稿、Claude/Opus 成文化、Word/PDF、final PASS。
- `2024西城一模 Q11` 必须保持 `B=①③`，若出现 `B=①④` 视为污染。
- `2025海淀二模 Q12/Q13` 答案源定位必须保留。

## Batch03 执行方式

先前误开过两个 Sonnet 进程，用户纠正后已全部停止，未采用其输出。

正式 Batch03 ClaudeCode Lane B 改用：

- `--model opus --effort max`
- debug 确认：`model=claude-opus-4-7`
- debug 确认：`effectiveWindow=980000`
- 独立日志目录：`logs/opus47_max/`
- 独立输出目录：
  - `claudecode_lane/opus47_batch03_subjective/`
  - `claudecode_lane/opus47_batch03_choice/`

Codex A 同步完成主观题与选择题预检，Lane B 独立复核后再归并。

## Batch03 队列与结果

Batch03 A-only 队列：

- 总数：112 行
- 主观题：56 行
- 选择题：56 行

Lane B 主观题结果：

- 56 / 56 已处理
- `B_TARGET_CONFIRMED`: 23
- `B_TARGET_SCOPE_OUT`: 33
- `can_enter_student_draft=no`: 56
- CSV 结构验收通过，无错列

Lane B 选择题结果：

- 56 / 56 已处理
- raw CSV 有 4 行因中文逗号导致字段错位；Codex 保留 raw，并生成机械归一化副本和 audit。
- normalized 后：
  - `B_TARGET_CONFIRMED`: 34
  - `B_TARGET_SCOPE_OUT`: 22
  - `can_enter_fusion=yes`: 34
  - `can_enter_student_draft=no`: 56
  - CSV 结构验收通过
- raw report 里有手工计数 31/25 与 row-level CSV 34/22 不一致，Codex 将 row-level normalized CSV 作为 merge source，并将此作为后续审计点。

归一化文件：

- `claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv`
- `claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalization_audit.csv`

## Batch03 合并结果

merge source：

- 主观题：`claudecode_lane/opus47_batch03_subjective/phase04_batch03_A_subjective_results.csv`
- 选择题：`claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv`

输出：

- `05_coverage/phase04_control_base_status_after_batch03.csv`
- `06_conflicts/phase04_batch03_codexA_laneB_reconciliation.csv`
- `06_conflicts/phase04_batch03_codexA_laneB_reconciliation.md`

Raw after Batch03 控制表：

- 364 行
- `L4_LOCKED_FOR_FUSION`: 4
- `L3_A_PLUS_B_TARGET_CONFIRMED`: 70
- `L0_BLOCKED`: 290
- 学生稿权限仍全部阻塞

## Queue-meta cleanup

Opus 主观题线指出：

1. `2026东城期末 Q16` 被队列错误拆成 `16(1)` 和 `16(2)`，但原卷与细则都是一个 7 分单题，且是哲学与文化，非选必三逻辑与思维。
2. `2025西城二模 Q16(2)` 在 Batch03 队列里缺失，但全局控制表中已经由 Batch01 锁定为 `L4_LOCKED_FOR_FUSION`，不需要重复补行。

Codex 已生成 downstream-cleaned 控制表：

- `05_coverage/phase04_control_base_status_after_batch03_cleaned.csv`
- `06_conflicts/phase04_batch03_queue_meta_cleanup_decisions.csv`
- `06_conflicts/phase04_batch03_queue_meta_cleanup_decisions.md`

Cleaned downstream table：

- 362 行
- `L4_LOCKED_FOR_FUSION`: 4
- `L3_A_PLUS_B_TARGET_CONFIRMED`: 70
- `L0_BLOCKED`: 288
- 无重复 canonical id
- `Q-2026东城期末-16` 只保留一个边界关闭行
- `Q-2025西城二模-16(2)` 保持 `L4_LOCKED_FOR_FUSION`

## 当前可用于 evidence fusion 的 74 行

合计 74 行：`L4=4` + `L3=70`。

按题型：

- 主观题 27
- 选择题 47

按模块：

- 推理 38
- 思维 23
- 交叉 13

按套卷分布：

- 2026朝阳期中 7
- 2024朝阳期中 6
- 2026顺义一模 6
- 2024西城一模 5
- 2025东城期末 5
- 2025丰台期末 5
- 2026丰台一模 5
- 2026通州期末 5
- 2024朝阳一模 4
- 2024朝阳二模 4
- 2025海淀期末 4
- 2025顺义一模 4
- 2024海淀二模 3
- 2025海淀二模 3
- 2025西城二模 3
- 2026东城期末 3
- 2026东城一模 2

关键 hard samples / guards：

- `2024西城一模 Q11`：保持 `B=①③`，不得回到 `B=①④`。
- `2025海淀二模 Q12/Q13`：从补充答案源确认并保留 locator。
- `2025西城二模 Q16(2)`：充分条件假言推理，后件真不能确定前件真，已 L4。
- `2025西城二模 Q16(3)`：创新思维，已 L4。
- `2026丰台一模 Q18(2)`：必要条件假言推理 + 三段论大项不当扩大，已 L4。
- `2025海淀二模 Q20`：辩证思维角度池，已 L4。
- `2026东城期末 Q17(2)`：形式逻辑综合，含矛盾律、充分条件假言、必要条件假言、三段论。

## 需要你裁决

请给出明确 verdict，建议只能在下面几类中选：

1. `GO_TO_PHASE05_EVIDENCE_FUSION_ARCHIVE`
   - 允许 Codex 把 74 行做成“证据融合底稿/同类题归档/思维与推理框架骨架”。
   - 仍然禁止学生稿、Claude/Opus 成文化、Word/PDF、final PASS。

2. `REPAIR_BATCH03_BEFORE_FUSION`
   - 说明必须先修哪些问题，例如选择题 34/22 与 report 31/25 不一致、某些 scope_out 误判、某些答案源不足、Q16 cleanup 不认可等。

3. `GO_TO_STUDENT_DRAFT_PREP`
   - 只有你确认 evidence pool 足够稳定，且可以进入学生稿准备；若选择此项，请仍说明是否允许 Claude/Opus 成文化，是否仍需先做 content outline 审查。

请特别检查：

- Batch03 是否真正完成了 GPT 要求的 112 个 A-only/L1 行？
- 选择题 normalized CSV 是否可作为 merge source？
- `2026东城期末 Q16` cleanup 是否合理？
- `2025西城二模 Q16(2)` 是否应视为已保留而不是新缺口？
- 现在是否可以进入 Phase05 evidence fusion archive？

请最后输出：

- verdict
- must-fix list
- allowed next actions
- still forbidden actions
- 你建议下一批让 Codex / ClaudeCode / Claude-Opus 分别做什么
