# Batch 013 Tail Claude Opus Adaptive Review Prompt

你是 Claude Opus 4.7 Adaptive Thinking 审核员。请审核 GPT Pro 后的补丁稿 `BATCH_013_AFTER_GPT_PRO_PATCH`。

请重点检查：

1. `2026朝阳期末Q20` 是否可正式入链。
2. 五条正式术语是否保留了同题阅卷细则原词。
3. 角度4拆分成 `理论：国家利益` 和 `中国：维护人民利益/中国式现代化` 后，是否充分标注二者同属细则角度4，是否会造成赋分角度膨胀。
4. 总说句是否已经作为 `formal_rubric_fallback_credit` 兜底加分表达处理，而不是正式逐点术语。
5. `2026丰台期末Q20` 是否应继续 blocked_prompt_only。

请输出：

- 通过/小修/阻断裁决。
- 必须修改项。
- 建议修改项。
- 是否允许 Codex 进入终稿融合和 Governor。

