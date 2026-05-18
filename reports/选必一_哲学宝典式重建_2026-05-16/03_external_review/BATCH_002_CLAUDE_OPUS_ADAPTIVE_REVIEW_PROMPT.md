# Batch 002 Claude Opus 4.7 Adaptive Review Prompt

你是 Claude Opus 4.7 Adaptive Thinking，任务是对“选必一《当代国际政治与经济》哲学宝典式重建”Batch 002 进行外部审核和完善建议。

请严格按附件顺序阅读：

1. `BATCH_002_SOURCE_PACKET`：五道题的题目、评分细则、边界说明和证据路径。
2. `BATCH_002_AFTER_GPT_PRO_PATCH`：Codex 在 GPT Pro 审核后已经本地裁决并修订的当前稿。
3. `BATCH_002_GPT_PRO_ADVANCED_REVIEW`：GPT Pro 原始审核意见。
4. `BATCH_002_GPT_PRO_DECISION_LOG`：Codex 对 GPT 意见的源包裁决记录。

## 审核目标

请不要重写全文。你只做“源包约束下的审核与补丁建议”：

- 找出当前稿仍然存在的概念错误、跨题混并、细则位置不准、材料触发不贴题、答案句不像卷面作答、选必一边界越界、同点替代表述累加等问题。
- 特别复查 GPT 已修订处是否仍有二次风险，尤其是 2024东城一模Q20 的经济相关知识边界、2024朝阳期中Q20(3) 的世界角度边界、2025东城一模Q20 的“此次出访”边界、2025海淀二模Q21 的联合国评分结构。
- 所有建议必须回到源包，不得凭常识新增评分点。

## 输出格式

第一部分输出 TSV 表，表头固定为：

`issue_id	severity	question_id	entry_term	diagnosis	source_basis	required_patch`

severity 只能使用：

- `must_fix_source`
- `must_fix_boundary`
- `merge_or_index_issue`
- `wording_improvement`
- `no_action`

第二部分输出 `PATCH_BLOCKS`。每个需要修改的问题给一个块：

```text
PATCH_BLOCK B002-Cxx
target: <当前稿中的标题或字段>
replace/add/delete:
<可直接执行的中文修改建议>
source_basis: <源包依据>
```

如果你认为某处无需修改，也要在 TSV 中写 `no_action`，但不要给 PATCH_BLOCK。

## 硬约束

- 不得把 `依托国内超大规模市场优势` 写入 2024朝阳期中Q20(3) 主链。
- 不得把 2025西城二模Q19(2) 强行并入“五方向经济全球化”完整公式。
- 2025东城一模Q20 必须聚焦 2024年11月13日开始的此次出访，不能把背景材料当作主要触发。
- 2025东城一模Q20 中“维护发展中国家的利益”为2分主表述，“完善全球治理/推进国际关系民主化”为1分替代表述，不能累加成满分新术语。
- 海淀二模Q21 的联合国结构要保留：中国需要联合国、联合国需要中国两大部分及其内部评分点。
- 学生可背诵稿不得出现流程词、证据路径、模型名或元评价。
