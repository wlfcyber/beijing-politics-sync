你是 ClaudeCode，作为独立审计线复核 Codex 刚补的 `2025海淀二模 Q10/Q11` 选择题证据边界。

工作目录：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

请只检查以下文件，不要泛化扩展：

1. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\haidian_2025_second_mock_choice_source_addendum_20260524.md`
2. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\haidian_2025_second_mock_evidence_closeout_20260524.md`
3. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\06_governor_confucius\CURRENT_ACCEPTANCE_STATUS_20260524.md`
4. `reports\choice_question_processing_ledger.md`
5. `reports\governor_board.md`
6. `artifacts\北京高考政治错肢库_持续更新版.md`
7. `reports\bixiu4_philosophy_strict_v8_2026-05-23\new_9_suite_integration\必修四哲学材料-知识触发框架_v8_65套新增卷子并入版.md`

审计问题：

- Codex 是否准确区分了“当前 raw folder 未找到教师版 PDF”和“旧台账/总督记录曾经闭合过答案源”？
- `Q10/Q11` 是否只被保留为选择题链条，而没有被升级成主观题评分细则？
- 新增附录是否有虚构来源、过度宣称、或把旧记录当作本轮重新读 PDF？
- `CURRENT_ACCEPTANCE_STATUS_20260524.md` 是否仍明确写着 GPTPro web pending，而不是最终全模型 PASS？
- 外审包是否已经包含新增附录？

输出格式：

| severity | location | finding | fix |
|---|---|---|---|

severity 只能用 `PASS / NEED_EVIDENCE / REWRITE / DELETE`。

如果结论是可接受，请明确写：
`SCOPED_PASS: Haidian Q10/Q11 choice-source boundary is acceptable; no final all-model PASS because GPTPro web remains pending.`
