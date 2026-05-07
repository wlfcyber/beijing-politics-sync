# Supervisor Patch 02 - Batch03 缺 entries 与 acceptance

时间：2026-05-07 14:17

当前 QA 证据：

- 已写：`QUESTION_DECISIONS.csv`（72 行数据，列宽合格）
- 已写：`MAIN_THINKING_LEDGER.csv`
- 已写：`CHOICE_TRAP_LEDGER.csv`
- 已写：`FRAMEWORK_NODE_MATRIX.csv`
- 已写：`FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
- 已写：`BLOCKED_OR_BOUNDARY.md`
- 已写：`suite_reports/S-2025东城期末.md`
- 已写：`suite_reports/S-2026东城一模.md`
- 已写：`suite_reports/S-2026东城期末.md`

仍缺：

- `entries/batch03_entries.jsonl`
- `BATCH03_ACCEPTANCE.md`

纠偏要求：

1. 立刻从 `MAIN_THINKING_LEDGER.csv` 和 `CHOICE_TRAP_LEDGER.csv` 生成 `entries/batch03_entries.jsonl`。
2. 每行 JSON 必须含字段：
   `question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。
3. 立刻写 `BATCH03_ACCEPTANCE.md`，只写“可作为融合输入/仍需 Codex 裁决”，不得写 `PASS`。
4. 写完后本目录必须通过 `codex_audit/audit_batch_dir.py`。

Codex 监管结论：Batch03 当前状态为 `CORE_OUTPUTS_READY_BUT_ENTRIES_ACCEPTANCE_MISSING`。
