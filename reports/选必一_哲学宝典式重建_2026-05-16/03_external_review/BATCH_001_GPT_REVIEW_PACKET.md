# Batch 001 GPT Review Packet

请作为 GPT-5.5 Pro 内容总审，只审核下面 5 道题的 Codex 初稿。目标是发现概念错误、细则错读、模块边界错误、同类项错误和证据不足。

## 审核重点

1. `术语` 是否都来自评分细则、评标、阅卷细则或用户确认细则。
2. 是否存在把参考答案、材料事实或教材框架冒充术语。
3. 六大要素归类是否合理。
4. 同一采分核心是否被重复拆分。
5. 2026 通州期末 Q20 是否完整保留用户确认的六点细则。
6. 2026 朝阳期中 Q17 是否保留总说/分说结构，且没有把必修二内容硬塞进选必一主链。
7. 2025 海淀期中 Q16(2) 是否只把“贸易摩擦-国际组织权利-全球经济治理规则制定”作为选必一硬链。
8. 2024 东城一模 Q16 是否只作为跨模块补入，不污染主链。

## 必须使用的输出格式

| issue_id | severity | question_id | source_location | codex_entry | diagnosis | proposed_action |
|---|---|---|---|---|---|---|

severity 只允许：must_fix_source / must_fix_rubric / must_fix_module_boundary / should_fix_teaching / note。

## 材料包

- 源证据：`../01_source_packets/BATCH_001_SOURCE_PACKET.md`
- Codex 初稿：`../02_codex_batches/BATCH_001_CODEX_DRAFT.md`

## 裁决规则

你的意见是审核建议，不直接改正文。每条意见必须能回到源文件或源包定位。没有源定位的建议只能作为 note。
