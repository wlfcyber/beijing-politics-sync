# Supervisor Patch 02 - Batch02 缺正式产物，不可验收

时间：2026-05-07 13:34

当前目录证据：

- 已写：`QUESTION_DECISIONS.csv`
- 缺失：`MAIN_THINKING_LEDGER.csv`
- 缺失：`CHOICE_TRAP_LEDGER.csv`
- 缺失：`FRAMEWORK_NODE_MATRIX.csv`
- 缺失：`FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
- 缺失：`BLOCKED_OR_BOUNDARY.md`
- 缺失：`suite_reports/*.md`
- 缺失：`entries/batch02_entries.jsonl`
- 缺失：`BATCH02_ACCEPTANCE.md`

纠偏要求：

1. `PROGRESS.md` 中已经写了“闭合”和“最终交付清单”，但正式文件尚未全部落盘；这种状态不能算完成。
2. 立刻按 `PROGRESS.md` 自己承诺的清单补齐全部文件。
3. `entries/batch02_entries.jsonl` 必须为合法 JSONL，每行必须含字段：
   `question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。
4. `QUESTION_DECISIONS.csv` 中每一题仍必须只有四类终端结论：`入正文 / 同类索引 / blocked / excluded`。
5. 不许写 `PASS`、不许写终稿、不许生成 Word/PDF；本批目标只是朝阳厚内容矿和套卷闭合材料。

Codex 监管结论：在上述缺失文件补齐并通过 schema/行数检查之前，Batch02 状态为 `MISSING_OUTPUTS_AFTER_SELF_CLAIMED_CLOSURE`。
