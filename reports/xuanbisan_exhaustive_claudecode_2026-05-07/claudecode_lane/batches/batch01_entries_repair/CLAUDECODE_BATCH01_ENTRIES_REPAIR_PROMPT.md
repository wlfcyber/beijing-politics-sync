# ClaudeCode Batch01 Entries Repair

你是真实 ClaudeCode CLI 的修补小批。你不是重新跑整本，不生成终稿，不覆盖 Batch01 已有文件。

## 任务

读取：

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng\QUESTION_DECISIONS.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng\MAIN_THINKING_LEDGER.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng\CHOICE_TRAP_LEDGER.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng\FRAMEWORK_NODE_MATRIX.csv`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_haidian_xicheng\BLOCKED_OR_BOUNDARY.md`

写入：

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_entries_repair\batch01_entries.jsonl`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_entries_repair\REPAIR_REPORT.md`

## JSONL 要求

从 `MAIN_THINKING_LEDGER.csv` 每行生成一个 JSON：

- `question_id`
- `type`: `main_thinking`
- `framework_node`
- `material_signal`
- `trigger_logic`
- `answer_sentence`
- `evidence_level`
- `needs_codex_recheck`
- `source_batch`: `batch01_haidian_xicheng`

从 `CHOICE_TRAP_LEDGER.csv` 每行生成一个 JSON：

- `question_id`
- `type`: `choice_trap`
- `framework_node`
- `material_signal`
- `trigger_logic`
- `answer_sentence`
- `evidence_level`
- `needs_codex_recheck`
- `source_batch`: `batch01_haidian_xicheng`

如果字段名与上述不完全一致，按中文含义映射。缺字段不要编造，留空并在 `REPAIR_REPORT.md` 里列出。

不要写 PASS / final / 终稿。
