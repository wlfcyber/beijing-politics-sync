# Supervisor Patch 03 — entries 卡住，必须修补

Codex supervisor check time: 2026-05-07 13:05

## 当前状态

Batch01 已补齐：

- `QUESTION_DECISIONS.csv`
- `MAIN_THINKING_LEDGER.csv`
- `CHOICE_TRAP_LEDGER.csv`
- `FRAMEWORK_NODE_MATRIX.csv`
- `BLOCKED_OR_BOUNDARY.md`
- `suite_reports/*.md` 共 5 份

但仍缺：

- `entries\batch01_entries.jsonl`

## 纠偏

`entries\batch01_entries.jsonl` 是 Codex 后续融合的机器可读入口。没有它，Batch01 不能算闭合。

立刻生成 entries：

- 来源一：`MAIN_THINKING_LEDGER.csv` 每一行生成一个 `type=main_thinking` entry。
- 来源二：`CHOICE_TRAP_LEDGER.csv` 每一行生成一个 `type=choice_trap` entry。
- 每行必须是合法 JSON。
- 字段至少含：
  - `question_id`
  - `type`
  - `framework_node`
  - `material_signal`
  - `trigger_logic`
  - `answer_sentence`
  - `evidence_level`
  - `needs_codex_recheck`
  - `source_batch`

## 兜底

如果本 ClaudeCode 进程不能及时生成，Codex 将启动独立 repair 小批读取上述 CSV 生成 entries，并把原进程输出视为不完整。
