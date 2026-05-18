# Batch 001 Claude Review Packet

请作为 Claude 教学文本审核者，只审核下面 5 道题的 Codex 初稿。不要替 Codex 重写全文，只输出问题清单。

## 审核重点

1. 是否像学生能直接使用的“宝典”语言。
2. `材料触发` 是否真正解释了“为什么这道题触发该术语”。
3. `答案句` 是否像考生答题纸语言，不含后台制作说明。
4. 同一题的总说/分说层次是否完整，尤其 2026 朝阳期中 Q17。
5. 跨模块题 2024 东城一模 Q16 是否讲清边界，避免把哲学/文化术语塞入选必一。

## 必须使用的输出格式

| issue_id | severity | question_id | entry_term | problem | suggested_fix | must_check_source |
|---|---|---|---|---|---|---|

severity 只允许：must_fix / should_fix / note。

## 材料包

- 源证据：`../01_source_packets/BATCH_001_SOURCE_PACKET.md`
- Codex 初稿：`../02_codex_batches/BATCH_001_CODEX_DRAFT.md`

## 禁止事项

- 不要新增没有细则来源的术语。
- 不要把普通参考答案当评分细则。
- 不要把旧版内容当可信依据。
- 不要仅给泛泛评价，必须定位到题号和术语。
