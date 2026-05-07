# Batch01 Entries QA

Status: `REPAIR_ENTRIES_ACCEPTED_AS_FUSION_INPUT`

## 检查结果

- 原 Batch01：`claudecode_lane\batches\batch01_haidian_xicheng\entries\batch01_entries.jsonl`
  - JSON 行数：31
  - JSON 解析：0 bad lines
  - 问题：31 行均缺少约定的融合字段 `type/material_signal/trigger_logic/answer_sentence/source_batch` 等；字段主要是中文正文键，可作内容备份，但不作为机器融合主入口。

- ClaudeCode entries repair：`claudecode_lane\batches\batch01_entries_repair\batch01_entries.jsonl`
  - JSON 行数：31
  - JSON 解析：0 bad lines
  - 类型：`main_thinking` 20，`choice_trap` 11
  - 必需字段缺失：0
  - 结论：可作为 Batch01 的机器融合入口。

- Codex 兜底 repair：`claudecode_lane\batches\batch01_entries_repair\codex_repair_batch01_entries.jsonl`
  - JSON 行数：31
  - JSON 解析：0 bad lines
  - 类型：`main_thinking` 20，`choice_trap` 11
  - 必需字段缺失：0
  - 结论：作为 ClaudeCode repair entries 的备份和比对源。

## 处理意见

- Batch01 内容不再因 entries 缺失而阻塞。
- 融合时优先读取 `batch01_entries_repair\batch01_entries.jsonl`。
- 原 Batch01 entries 只作内容溯源，不直接喂入机器融合。
- 本状态不授权终稿；只说明海淀/西城批次的融合入口已可用。
