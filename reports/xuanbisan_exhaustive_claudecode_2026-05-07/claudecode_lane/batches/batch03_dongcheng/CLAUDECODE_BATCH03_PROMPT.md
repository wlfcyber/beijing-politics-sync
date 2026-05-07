# ClaudeCode Batch03: 东城套卷穷尽闭合

你是真实 ClaudeCode CLI 的 B 线厚内容矿工。不要写终稿，不要写 PASS，不生成 Word/PDF。本批只处理东城套卷。

## 已发生的监督教训，必须吸取

- 不准只写 `PROGRESS.md` 后自称完成。
- 不准只交 `QUESTION_DECISIONS.csv`。
- 不准手写逗号拼接 CSV；所有 CSV 必须用结构化 CSV 写入器生成，确保含逗号/引号/换行的字段正确转义。
- `QUESTION_DECISIONS.csv` 中 `needs_codex_recheck` 只允许 `yes/no`。
- 不准漏 `entries/*.jsonl`。
- JSONL 必须 schema 合格；每行必须含：
  `question_id,type,framework_node,material_signal,trigger_logic,answer_sentence,evidence_level,needs_codex_recheck,source_batch`。
- 不准只建空目录；`suite_reports/` 和 `entries/` 必须有真实文件。
- 学生候选内容不得出现“固定分析流程”。
- 审计话术、source path、phase/source_pool/debug/OCR 等不得进入学生候选正文。
- 选择题若缺完整选项或可靠答案源，不得写入正文；必须写 `blocked` 并说明缺口。
- 写完后必须自检：文件存在、CSV 列宽、四类结论、JSONL schema、entries 行数。

## 写入目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch03_dongcheng`

只写本目录，不覆盖 Batch01、Batch02、fusion 或根 lane。

## 必读文件

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_audit\audit_batch_dir.py`

## 本批 suite

- `S-2025东城期末`
- `S-2026东城一模`
- `S-2026东城期末`

覆盖这三套在控制矩阵中的全部候选行，不只写入正文题。

## 必交文件

1. `PROGRESS.md`
2. `QUESTION_DECISIONS.csv`
3. `MAIN_THINKING_LEDGER.csv`
4. `CHOICE_TRAP_LEDGER.csv`
5. `FRAMEWORK_NODE_MATRIX.csv`
6. `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
7. `BLOCKED_OR_BOUNDARY.md`
8. `suite_reports\S-2025东城期末.md`
9. `suite_reports\S-2026东城一模.md`
10. `suite_reports\S-2026东城期末.md`
11. `entries\batch03_entries.jsonl`
12. `BATCH03_ACCEPTANCE.md`

## 口径

- 结论只允许四类：`入正文 / 同类索引 / blocked / excluded`。
- `blocked` 不是删除；必须说明题面、选项、答案、细则、视觉核读或模块边界缺口。
- `同类索引` 不是正文题量；必须说明为什么不单独入正文。
- 主观题只在有 A-formal/A-support 明确依据时入正文。
- 选择题必须有完整选项和可靠答案源才可入 choice trap。
- 纯形式逻辑、推理规则题不进思维主链，但可进入推理索引或 choice trap。
- 所有可融合题都要写厚内容：材料动作 -> 总帽子/推理类型 -> 小方法/逻辑形式 -> 触发逻辑 -> 卷面答案句。

现在开始。先写 `PROGRESS.md`，再逐套卷推进；最后必须用 `codex_audit\audit_batch_dir.py` 的同等规则自检，不要只写完成声明。
