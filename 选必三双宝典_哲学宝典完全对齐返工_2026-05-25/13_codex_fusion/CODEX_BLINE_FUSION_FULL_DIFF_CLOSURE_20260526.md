# Codex/B 线融合全量差异闭环 2026-05-26

verdict: `BLINE_DIFF_ACCOUNTED_STILL_NOT_FINAL`

本文件对 `claudecode_lane/entries/` 三类 B 线厚内容做全量差异闭环，目的不是机械把 B 线 85 条全部搬进正文，而是确认每条都有明确裁决：进入正文、已由现正文覆盖、拒绝进入正文、或保留审计索引。

## 输入范围

- `claudecode_lane/entries/thinking_main.jsonl`：31 条。
- `claudecode_lane/entries/reasoning_main.jsonl`：31 条。
- `claudecode_lane/entries/reasoning_choice.jsonl`：23 条。
- 合计：85 条。

比对对象：

- `05_candidate_md/选必三_逻辑与思维_思维宝典_哲学完全对齐候选稿.md`
- `05_candidate_md/选必三_逻辑与思维_推理宝典_哲学完全对齐候选稿.md`

比对方法：

- 以 `source_suite + question_id`、`question_id`、`source_lock run_question_id` 和此前 `fusion_candidates.md` 的 F1-F7 裁决为索引。
- 自动命中只作为定位证据；最终裁决仍以 source-lock、coverage、已写入的 Batch1/Batch2/Batch3 报告和当前正文为准。

## 全量结果

| 类别 | B 线条数 | 当前状态 |
| --- | ---: | --- |
| thinking_main | 31 | 31 条均已在思维正文中有对应题源/复挂或已由 Batch1/Batch3 融合加厚。 |
| reasoning_main | 31 | 29 条已在推理正文中有对应题源；2 条不进入学生正文，见下表。 |
| reasoning_choice | 23 | 23 条均已在推理正文中有对应选择题、题干选项、答案和错因结构。 |
| 合计 | 85 | 83 条正文覆盖，2 条非正文裁决；无“未裁决消失”条目。 |

## 两条非正文裁决

| B 线 entry | 当前裁决 | 理由 |
| --- | --- | --- |
| `RM-2024-XICHENG-1MO-Q19-5` | reject for current body | B 线写成“逻辑规律/同一律(枚举概括+同一对象替换)”主观题；但本 run coverage `Q0066` 锁定为未来产业方向研判、超前思维等思维链条，且当前思维正文已有该题对应内容。不得把它强行改写为推理册同一律主观题。 |
| `RM-2025-HAIDIAN-2MO-CROSS` | keep as audit index | 该条只是把 `2025海淀二模 Q20` 作为推理册“同题不构成单一推理形式”的交叉索引；当前思维册已按分析综合、整体性、动态性质量互变、辩证否定四节点充分挂载。为避免学生误把综合辩证思维题当单一推理形式，不进入推理学生正文。 |

## 已完成的 B 线融合批次

- Batch1：思维硬样本分节点融合，覆盖 `2026顺义一模 Q19(2)`、`2025海淀二模 Q20`、`2026朝阳期中 Q21(2)`、`2024海淀二模 Q17(1)`。
- Batch2：推理硬样本局部融合，清理 `答案表` 后台口径，加厚 `2024朝阳一模 Q6` 选择题错因。
- Reconciliation Matrix：裁决 F1-F7，拒绝 `2024西城一模 Q19(2)` B 线“新质生产力”替换和 `2025海淀期末 Q18` “社区闲置厂房”替换。
- Batch3：属种真包含、晏子类比、传统/未来产业辩证否定、月季野生近缘种联想复挂。

## 学生版污染回查

当前两本候选 Markdown 中未命中以下 B 线污染关键词：

- `AI 助教`
- `电动汽车续航`
- `人体免疫系统`
- `企业风险控制`
- `社区闲置厂房`
- `新质生产力是以科技创新`

当前两本候选 Markdown 中未命中以下后台/审计词：

- `候选稿门禁`
- `答案表`
- `待回源`
- `以原卷为准`
- `题干触发点`
- `先写`
- `要写`
- `本题需要`
- `设问要求`
- `采分点`
- `question_id`
- `A-formal`
- `B-choice-signal`

## 结论

B 线厚内容差异已经完成一轮全量裁决闭环：没有“B 线条目消失但未说明”的情况。这个结论只解除“B 线融合剩余差异未全量裁决”的控制阻断，不等于最终版通过。

最终仍被以下事项阻断：

- GPT Pro 真实审查：`real_call_pending`。
- Claude 真实审查：`real_call_pending`。
- fresh-context 零基础盲测尚未运行。
- Governor / Confucius 尚未以最新 Word/PDF 作最终 artifact-only 验收。
