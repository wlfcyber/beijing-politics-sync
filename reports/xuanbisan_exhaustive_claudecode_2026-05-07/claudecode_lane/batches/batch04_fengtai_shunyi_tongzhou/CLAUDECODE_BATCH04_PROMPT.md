# ClaudeCode Batch04: 丰台/顺义/通州套卷穷尽闭合

你是真实 ClaudeCode CLI 的 B 线厚内容矿工。不要写终稿，不要写 PASS，不生成 Word/PDF。本批只处理丰台、顺义、通州套卷。

## 已验证教训，必须执行

- 不准只写 `PROGRESS.md` 自称完成。
- 不准只写中间候选表。
- 所有 CSV 必须用结构化 CSV 写入器生成，不能手写逗号拼接。
- `needs_codex_recheck` 只允许 `yes/no`。
- 必须写真实 `suite_reports/*.md` 和真实 `entries/*.jsonl`，不准空目录。
- JSONL 每行必须含：
  `question_id,type,framework_node,material_signal,trigger_logic,answer_sentence,evidence_level,needs_codex_recheck,source_batch`。
- 写完后必须能通过 `codex_audit/audit_batch_dir.py`；不要只写“已通过”。
- 学生候选内容不得出现“固定分析流程”，不得把审计话术/source path/phase/debug/OCR 写入学生候选正文。

## 写入目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch04_fengtai_shunyi_tongzhou`

只写本目录，不覆盖前面批次、fusion 或根 lane。

## 必读文件

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_audit\audit_batch_dir.py`

## 本批 suite

- `S-2025丰台期末`
- `S-2026丰台一模`
- `S-2025顺义一模`
- `S-2026顺义一模`
- `S-2026通州期末`

覆盖这五套在控制矩阵中的全部候选行，不只写入正文题。

## 必交文件

1. `PROGRESS.md`
2. `QUESTION_DECISIONS.csv`
3. `MAIN_THINKING_LEDGER.csv`
4. `CHOICE_TRAP_LEDGER.csv`
5. `FRAMEWORK_NODE_MATRIX.csv`
6. `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
7. `BLOCKED_OR_BOUNDARY.md`
8. `suite_reports\S-2025丰台期末.md`
9. `suite_reports\S-2026丰台一模.md`
10. `suite_reports\S-2025顺义一模.md`
11. `suite_reports\S-2026顺义一模.md`
12. `suite_reports\S-2026通州期末.md`
13. `entries\batch04_entries.jsonl`
14. `BATCH04_ACCEPTANCE.md`

## 口径

- 结论只允许四类：`入正文 / 同类索引 / blocked / excluded`。
- `blocked` 不是删除；必须说明题面、选项、答案、细则、视觉核读或模块边界缺口。
- `同类索引` 不是正文题量；必须说明为什么不单独入正文。
- 主观题只在有 A-formal/A-support 明确依据时入正文。
- 选择题必须有完整选项和可靠答案源才可入 choice trap。
- 纯形式逻辑、推理规则题不进思维主链，但可进入推理索引或 choice trap。
- 所有可融合题都要写厚内容：材料动作 -> 总帽子/推理类型 -> 小方法/逻辑形式 -> 触发逻辑 -> 卷面答案句。

现在开始。可以先写启动段落，但不得写“完成/闭合/验收”直到全部文件真实存在并自检通过。
