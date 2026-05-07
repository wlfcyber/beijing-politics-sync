# ClaudeCode Batch01: 海淀/西城套卷穷尽闭合

你是真实 ClaudeCode CLI 的 B 线厚内容矿工。不要写终稿，不要写 PASS，不要生成 Word/PDF。本批只处理海淀/西城相关套卷，目标是把每一行候选题给出 `入正文 / 同类索引 / blocked / excluded` 结论，并给可融合题写厚内容。

## 最高规则

读取并遵守：

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`

用户最新要求是“穷尽所有考题”。这不是 33/29 小包，也不是 77 行直接终稿。每个候选题都要有去向。

## 写入目录

只写入：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng`

不要覆盖 `claudecode_lane` 根目录的大任务文件。

## 必读控制文件

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\CODEX_EXHAUSTIVE_DECISION_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\CODEX_EXHAUSTIVE_CANONICAL_DECISION_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\CODEX_SIGNAL_CLOSURE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase12_362_control_base_rescan_matrix.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\09_student_draft\phase12_expanded_body_FROM_362_control_matrix.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase05_thinking_signal_archive.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase05_reasoning_typology_archive.csv`

## 本批套卷边界

只处理这些 suite：

- `S-2025海淀二模`
- `S-2025海淀期末`
- `S-2024海淀二模`
- `S-2025西城二模`
- `S-2024西城一模`

必须覆盖这些 suite 在控制矩阵中的全部候选题，不只覆盖已入正文题。

优先厚写这些题：

- `Q-2025海淀二模-20`
- `Q-2025海淀二模-12`
- `Q-2025海淀二模-13`
- `Q-2025海淀期末-17-1`
- `Q-2025海淀期末-18`
- `Q-2024海淀二模-17-1`
- `Q-2024海淀二模-17-2`
- `Q-2025西城二模-16-2`
- `Q-2025西城二模-16-3`
- `Q-2025西城二模-6`
- `Q-2024西城一模-19-2`
- `Q-2024西城一模-19-3`
- `Q-2024西城一模-19-5`

## 输出文件

在本 batch 目录写：

1. `PROGRESS.md`：按 suite 写推进，不要泛泛写完成。
2. `QUESTION_DECISIONS.csv`：字段至少含 `question_id,suite_id,original_qno,question_type,codex_current_decision,claudecode_decision,decision_reason,needs_codex_recheck`。
3. `MAIN_THINKING_LEDGER.csv`：主观题厚内容，字段含 `question_id,来源,完整设问,材料动作,总帽子,小方法,触发逻辑,答案句,证据等级,框架落点,题型标签`。
4. `CHOICE_TRAP_LEDGER.csv`：选择题厚内容，字段含 `question_id,题干信号,完整选项或选项单位,答案源,正确项理由,诱人错项,陷阱类型,是否可入学生稿`。
5. `FRAMEWORK_NODE_MATRIX.csv`：本批每个框架节点挂载哪些题，哪些只是索引或 blocked。
6. `BLOCKED_OR_BOUNDARY.md`：本批所有 blocked/excluded 的理由。
7. `suite_reports\<suite_id>.md`：每套卷一个 report。
8. `entries\batch01_entries.jsonl`：每条可融合厚内容一行 JSON。

## 内容风格

可融合条目必须像哲学宝典那样厚：讲清材料怎么触发方法、为什么能想到、答案句如何写成卷面语言。学生正文候选里不要出现“固定分析流程”这个栏目或措辞。不要把后台状态词、路径、phase 字段、A/B/PASS 写进学生内容。

现在开始，先写 `PROGRESS.md` 启动记录，再逐套卷推进。
