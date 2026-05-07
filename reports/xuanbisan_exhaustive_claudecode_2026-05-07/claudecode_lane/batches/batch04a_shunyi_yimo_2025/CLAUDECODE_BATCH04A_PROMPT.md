# ClaudeCode Batch04a: 2025顺义一模单套闭合

你是真实 ClaudeCode CLI 的 B 线厚内容矿工。本批只处理 `S-2025顺义一模`，用于修复 Batch04 整批停在 `_candidates.csv` 的问题。

写入目录：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch04a_shunyi_yimo_2025`

## 必读

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch04_fengtai_shunyi_tongzhou\_candidates.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_audit\audit_batch_dir.py`

## 本批 scope

只处理 `S-2025顺义一模` 的全部候选行。`_candidates.csv` 中该套 raw `92` 行，unique question_id `23` 个。每个 unique question_id 必须落入：

- `入正文`
- `同类索引`
- `blocked`
- `excluded`

## 必交文件

1. `PROGRESS.md`
2. `QUESTION_DECISIONS.csv`
3. `MAIN_THINKING_LEDGER.csv`
4. `CHOICE_TRAP_LEDGER.csv`
5. `FRAMEWORK_NODE_MATRIX.csv`
6. `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
7. `BLOCKED_OR_BOUNDARY.md`
8. `suite_reports\S-2025顺义一模.md`
9. `entries\batch04a_entries.jsonl`
10. `BATCH04A_ACCEPTANCE.md`

## 输出硬规则

- 不准只写 `PROGRESS.md` 自称完成。
- 不准空 `suite_reports/` 或空 `entries/`。
- 所有 CSV 必须用结构化 CSV 写入器。
- `needs_codex_recheck` 只允许 `yes/no`。
- JSONL 每行必须含：
  `question_id,type,framework_node,material_signal,trigger_logic,answer_sentence,evidence_level,needs_codex_recheck,source_batch`。
- 学生候选内容不得出现“固定分析流程”。
- 不写 `PASS`，不写终稿，不生成 Word/PDF。

现在开始。可以先写启动段落，但不得写“完成/闭合/验收”直到全部文件真实存在并通过自检。
