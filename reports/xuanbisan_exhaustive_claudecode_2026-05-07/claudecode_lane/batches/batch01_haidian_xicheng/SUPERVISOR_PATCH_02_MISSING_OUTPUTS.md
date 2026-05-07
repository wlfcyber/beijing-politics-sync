# Supervisor Patch 02 — Batch01 不得只交判定表

Codex supervisor check time: 2026-05-07 12:56

## 当前状态

Batch01 已写：

- `QUESTION_DECISIONS.csv`：101 rows
- `MAIN_THINKING_LEDGER.csv`：20 rows

Batch01 仍缺：

- `CHOICE_TRAP_LEDGER.csv`
- `FRAMEWORK_NODE_MATRIX.csv`
- `BLOCKED_OR_BOUNDARY.md`
- `entries\batch01_entries.jsonl`

## 硬纠偏

本批任务不是只判题。海淀/西城批次必须交出可供 Codex 融合的厚内容和审计闭环。

立刻补齐以下文件：

1. `CHOICE_TRAP_LEDGER.csv`
   - 覆盖 `QUESTION_DECISIONS.csv` 中 `question_type=选择题` 且 `claudecode_decision=入正文/同类索引` 的行。
   - 字段至少含：`question_id,题干信号,完整选项或选项单位,答案源,正确项理由,诱人错项,陷阱类型,是否可入学生稿,needs_codex_recheck`。
   - 如果完整四选项还没回源，不得写成成品；写 `blocked_full_options_recheck` 并在 `needs_codex_recheck=yes` 标明。

2. `FRAMEWORK_NODE_MATRIX.csv`
   - 按用户框架节点统计本批挂载。
   - 字段至少含：`framework_node,入正文题,同类索引题,blocked题,excluded题,补充说明`。

3. `BLOCKED_OR_BOUNDARY.md`
   - 汇总本批 101 行中所有 `blocked/excluded` 的理由。
   - 必须单列：其他模块、纯形式逻辑、缺完整选项、缺正式细则、图像/OCR、同类索引不独立入正文。

4. `entries\batch01_entries.jsonl`
   - 每条 `MAIN_THINKING_LEDGER.csv` 可融合行至少一条 JSON。
   - 每条 `CHOICE_TRAP_LEDGER.csv` 可融合行至少一条 JSON。
   - JSON 字段至少含：`question_id,type,framework_node,material_signal,trigger_logic,answer_sentence,evidence_level,needs_codex_recheck`。

## 不准做的事

- 不准写 PASS / final / 终稿 / 宝典成品。
- 不准把缺完整选项的选择题写成可直接学生稿。
- 不准把纯形式逻辑题混入思维方法主链。
- 不准覆盖根 `claudecode_lane` 的文件；只写本 Batch01 目录。
