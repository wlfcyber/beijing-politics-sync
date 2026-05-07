# ClaudeCode Batch02 Output Repair: 朝阳批次正式产物修复

你是真实 ClaudeCode CLI 的 B 线修复工。当前 Batch02 朝阳大批已经出现两个硬失败：

1. `PROGRESS.md` 自称闭合，但正式产物缺失。
2. `QUESTION_DECISIONS.csv` 手写逗号导致 CSV 转义失效，`needs_codex_recheck` 列被理由文本污染。

本修复批只写入下列目录，不得覆盖原 Batch02 大目录：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_output_repair`

## 必读

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_chaoyang\PROGRESS.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_chaoyang\QUESTION_DECISIONS.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_chaoyang\SUPERVISOR_PATCH_02_MISSING_OUTPUTS.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_chaoyang\SUPERVISOR_PATCH_03_INVALID_CSV.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\codex_lane\QUESTION_COVERAGE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\QUESTION_COVERAGE_MATRIX.csv`

## 修复范围

只处理四套朝阳套卷：

- `S-2024朝阳一模`
- `S-2024朝阳二模`
- `S-2024朝阳期中`
- `S-2026朝阳期中`

覆盖这四套控制矩阵中的全部候选题。每题必须落入四类之一：

- `入正文`
- `同类索引`
- `blocked`
- `excluded`

## 必交文件

在本修复目录写出：

1. `PROGRESS.md`
2. `QUESTION_DECISIONS.csv`
3. `MAIN_THINKING_LEDGER.csv`
4. `CHOICE_TRAP_LEDGER.csv`
5. `FRAMEWORK_NODE_MATRIX.csv`
6. `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
7. `BLOCKED_OR_BOUNDARY.md`
8. `suite_reports\S-2024朝阳一模.md`
9. `suite_reports\S-2024朝阳二模.md`
10. `suite_reports\S-2024朝阳期中.md`
11. `suite_reports\S-2026朝阳期中.md`
12. `entries\batch02_entries.jsonl`
13. `BATCH02_REPAIR_ACCEPTANCE.md`
14. `REPAIR_QA_NOTES.md`

## 输出硬规则

- 使用结构化 CSV 写入器生成所有 CSV，不要手写逗号拼接。
- `QUESTION_DECISIONS.csv` 的 `needs_codex_recheck` 只允许 `yes/no`。
- `entries/batch02_entries.jsonl` 每行必须是合法 JSON，且每行含字段：
  `question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。
- 所有学生候选厚内容不得出现“固定分析流程”。
- 不写 `PASS`，不写终稿，不生成 Word/PDF。
- 如果证据不足，写 `blocked`，不要硬塞入正文。
- 纯形式逻辑/推理题可入推理索引或 choice trap，但不得混入思维方法主链。
- 使用 max effort 和 adaptive-thinking 工作方式：先审计失败，再逐套补齐，再自检 schema/行数。

现在开始。先写 `PROGRESS.md`，再重写合格 CSV 和缺失产物。
