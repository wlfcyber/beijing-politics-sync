# 批次处理协议

## 批次单位

优先按“若干套试卷”跑；若同一批题型高度集中，也可按题型簇跑。

建议批次：

- Batch 01：当前预处理主观题中证据为 `formal_or_scoring_source` 的前 8-10 道。
- Batch 02：剩余主观题 formal 证据。
- Batch 03：`unknown`、`reference_answer`、题号/设问异常项，只做边界与缺口，不升格。
- Batch 04：已锁答案选择题。
- Batch 05：未锁答案选择题，回原始答案表复核后再处理。
- Batch 06：`MISSING_OR_UNCERTAIN.md` 中的套卷/OCR/自动抽题缺口。

## 每题案例卡字段

- `suite_id`
- `year`
- `district`
- `stage`
- `question_no`
- `question_type`
- `evidence_type`
- `prompt`
- `material_signal`
- `legal_relation`
- `dispute_focus`
- `legal_rule_or_elements`
- `result_or_solution`
- `responsibility_effect_procedure`
- `value_closure`
- `proposition_goal`
- `carrier_choice`
- `question_path`
- `rubric_rewarded_action`
- `legal_vs_value_balance`
- `framework_domain`
- `framework_core_action`
- `framework_gap`
- `proposition_path_status`
- `confidence`
- `notes`

## 每批输出

- `batch_XX_cards.csv`
- `batch_XX_report.md`
- `batch_XX_framework_delta.md`
- `batch_XX_gap_list.md`

## 批次后模型审议触发条件

任一条件满足，即触发 GPT-5.5 Pro + Claude Opus 审议：

- 新增或拆分框架节点。
- 有 2 道及以上题无法自然归位。
- 高频统计显示某个节点超过 20% 命中。
- Codex A 与 ClaudeCode B 对同一题归位冲突。
- 学生版表达可能变得太抽象、不可背、不可迁移。

审议必须是真实调用 GPT-5.5 Pro 和 Claude Opus 4.7 Adaptive。Codex 子智能体或本地模拟只能做预检查，不能替代审议结果。

## Framework Council 自我进化流程

每次触发审议，不是简单“审稿”，而是一次框架制定/更新会议：

1. `Round 0 Evidence Pack`：Codex 只提供脱敏证据包，不提供想让模型迎合的答案。
2. `Round 1 Independent Blueprints`：
   - GPT-5.5 Pro 独立提出框架修订方案，重点看主干高频、全面覆盖、缺口和风险。
   - Claude Opus 4.7 Adaptive 独立提出框架修订方案，重点看可学性、可背性、迁移路径和学生误用风险。
3. `Round 2 Cross-Critique`：
   - Claude Opus 必须回应 GPT 的方案：哪些保留、哪些会误导学生、哪些太抽象。
   - GPT-5.5 Pro 必须回应 Claude 的方案：哪些过度教学化、哪些缺证据容器、哪些会漏题。
4. `Round 3 Convergence Brief`：Codex 汇总一致点、冲突点和待核验证据点。
5. `Round 4 Local Evidence Decision`：Codex 逐条裁决为：`accepted`、`partially_accepted`、`rejected_no_evidence`、`deferred_more_batches`、`candidate_pending_real_call`。
6. `Round 5 Version Update`：只有 accepted / partially_accepted 且完成本地证据核验的项目进入新版本。

模型一致不等于正确；模型分歧不等于阻塞。最终看本地题源和细则。

## 版本升级条件

一个框架修改必须至少满足以下一项，才允许进入新版本：

- 提升高频主干清晰度。
- 让原本无法自然归位的题能够自然归位。
- 减少硬塞和重叠节点。
- 更准确区分“主干高频层”和“开放容器层”。
- 提升学生迁移能力。
- 修正证据边界错误。

不满足上述条件的建议，即使来自 GPT 和 Claude 一致意见，也只记录，不升级。
