# ClaudeCode Batch02: 朝阳套卷穷尽闭合

你是真实 ClaudeCode CLI 的 B 线厚内容矿工。不要写终稿，不要写 PASS，不生成 Word/PDF。本批只处理朝阳套卷。

## 继承纠偏

必须吸取 Batch01 的问题：

- 不准只交 `QUESTION_DECISIONS.csv`。
- 不准漏 `entries/*.jsonl`。
- JSONL 必须是 schema 合格字段，不准只写中文散列字段。
- 每条 JSON 必须含：`question_id,type,framework_node,material_signal,trigger_logic,answer_sentence,evidence_level,needs_codex_recheck,source_batch`。
- 选择题若缺完整选项或答案源，不得写入正文；必须写 `blocked` 并说明。
- 本批不覆盖根 lane 和 Batch01 文件，只写本目录。

## 写入目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_chaoyang`

## 必读文件

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase05_thinking_signal_archive.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase05_reasoning_typology_archive.csv`

## 本批 suite

- `S-2024朝阳一模`
- `S-2024朝阳二模`
- `S-2024朝阳期中`
- `S-2026朝阳期中`

覆盖这四套在控制矩阵中的全部候选行，不只写入正文题。

## 输出文件

必须写：

1. `PROGRESS.md`
2. `QUESTION_DECISIONS.csv`
3. `MAIN_THINKING_LEDGER.csv`
4. `CHOICE_TRAP_LEDGER.csv`
5. `FRAMEWORK_NODE_MATRIX.csv`
6. `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
7. `BLOCKED_OR_BOUNDARY.md`
8. `suite_reports\<suite_id>.md`
9. `entries\batch02_entries.jsonl`
10. `BATCH02_ACCEPTANCE.md`

## 口径

- 结论只允许四类：`入正文 / 同类索引 / blocked / excluded`。
- 纯形式逻辑、推理规则题不进思维主链，但可进入推理索引或 choice trap。
- 主观题只在有 A-formal/A-support 明确依据时入正文。
- 选择题必须有完整选项和可靠答案源才可入 choice trap。
- 学生候选内容不得出现“固定分析流程”。

现在开始。先写 `PROGRESS.md`，再逐套卷推进。
