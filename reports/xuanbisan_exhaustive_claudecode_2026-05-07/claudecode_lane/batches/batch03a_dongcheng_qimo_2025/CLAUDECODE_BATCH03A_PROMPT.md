# ClaudeCode Batch03a: 2025东城期末单套闭合

你是真实 ClaudeCode CLI 的 B 线厚内容矿工。本批只处理 `S-2025东城期末`，用于修复 Batch03 东城整批“自称完成但无正式输出”的问题。

## 失败背景

`batch03_dongcheng/PROGRESS.md` 已写了东城整批闭合，但目录只有 `_dongcheng_candidates.csv` 和 `PROGRESS.md`，缺所有正式产物。你必须只写本目录，不覆盖原 Batch03。

写入目录：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch03a_dongcheng_qimo_2025`

## 必读

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch03_dongcheng\_dongcheng_candidates.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch03_dongcheng\PROGRESS.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_audit\audit_batch_dir.py`

## 本批 scope

只处理 `S-2025东城期末` 的全部候选行。`_dongcheng_candidates.csv` 中该套共 54 行，unique question_id 应闭合到 24 个左右；每个候选必须落入：

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
8. `suite_reports\S-2025东城期末.md`
9. `entries\batch03a_entries.jsonl`
10. `BATCH03A_ACCEPTANCE.md`

## 已由 Batch03 进度锁定、但必须文件化验证的重点

- `Q-2025东城期末-18-2`：创新思维主观题，细则支持两层：思路新/方法新/结果新 + 聚合发散/联想/超前。
- `Q-2025东城期末-5`：辩证思维选择题，整体性/动态性/矛盾分析法，答案 C（②④）。
- `Q-2025东城期末-13`：三段论中项不周延，答案 B（①③）。
- `Q-2025东城期末-14`：性质判断/关系判断/谓项周延，答案 D。
- `Q-2025东城期末-15`：充分条件假言推理，答案 B。

## 输出硬规则

- 所有 CSV 必须用结构化 CSV 写入器，不能手写逗号。
- `needs_codex_recheck` 只允许 `yes/no`。
- JSONL 每行必须含：
  `question_id,type,framework_node,material_signal,trigger_logic,answer_sentence,evidence_level,needs_codex_recheck,source_batch`。
- 不准只写 `PROGRESS.md` 自称完成。
- 不准空 `suite_reports/` 或空 `entries/`。
- 学生候选内容不得出现“固定分析流程”。
- 不写 `PASS`，不写终稿，不生成 Word/PDF。

现在开始。可以先写启动段落，但不得写“完成”直到全部文件真实存在并自检通过。
