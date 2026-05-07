# Supervisor Patch 02 - Batch02a 只有中间文件，不可验收

时间：2026-05-07 13:34

当前目录证据：

- 已写：`_chaoyang_yimo_full_codex.csv`
- 已建：`entries/`
- 缺失：`PROGRESS.md`
- 缺失：`QUESTION_DECISIONS.csv`
- 缺失：`MAIN_THINKING_LEDGER.csv`
- 缺失：`CHOICE_TRAP_LEDGER.csv`
- 缺失：`FRAMEWORK_NODE_MATRIX.csv`
- 缺失：`FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
- 缺失：`BLOCKED_OR_BOUNDARY.md`
- 缺失：`suite_reports/*.md`
- 缺失：`entries/batch02a_entries.jsonl`
- 缺失：`BATCH02A_ACCEPTANCE.md`

纠偏要求：

1. `_chaoyang_yimo_full_codex.csv` 是中间抽取物，且不是可验收的正式交付件。
2. 立刻把 `S-2024朝阳一模` 单套卷转成正式文件：逐题四类结论、厚内容 ledger、选择题 trap、framework matrix、blocked/boundary、suite report、schema 合格 JSONL。
3. 所有 `入正文` 和 `同类索引` 项必须给出材料动作、触发逻辑和可迁移答案句；证据不足的选择题必须 `blocked`。
4. 不得覆盖 Batch02 大目录文件；只写 Batch02a 子目录。

Codex 监管结论：Batch02a 当前状态为 `INTERMEDIATE_ONLY_STALL`，不能并入融合。
