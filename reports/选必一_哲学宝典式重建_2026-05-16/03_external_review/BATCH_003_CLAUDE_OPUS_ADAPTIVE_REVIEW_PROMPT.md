# Batch 003 Claude Opus 4.7 Adaptive Review Request

你是第二轮外部审核。请基于粘贴包中的源包、GPT后修订稿、GPT原始审核和Codex裁决日志，审核 Batch 003 是否仍存在：

1. 评分细则术语误放、漏放、过度泛化；
2. 材料触发和答案句是否有源包不支持的事实；
3. 2026朝阳一模Q20必答链条与发展潜力可选链条是否清楚；
4. 2026西城一模Q20(2)标准规则、产业链供应链、综合层是否混层；
5. 2025东城二模Q20是否保住背景/精神/行动三层和“同球共济”；
6. 2025朝阳二模Q21是否按中国/区域/世界三主体角度，且同一关键词不重复；
7. 2026东城期末Q20是否保住四大倡议4分、系统推动2分、实践层面1分。

输出格式：
- 先给 issue 表：issue_id, severity, question_id, term, diagnosis, source_basis, required_patch。
- 再给 PATCH_BLOCK，必须可执行，写明 target 和 replace/add/delete。
- 只能依据粘贴包，不要引入源包外事实。你不是最终裁决者，所有建议会由 Codex 回源裁决。
