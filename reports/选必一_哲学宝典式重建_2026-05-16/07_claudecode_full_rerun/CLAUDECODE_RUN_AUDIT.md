# ClaudeCode Opus 4.7 全量重跑审计

## 结论

本次已按用户要求把 ClaudeCode 厚稿生产线从 Sonnet 切换为 Opus/max 重跑。旧问题属实：`run_claudecode_single_batch.ps1`、`run_claudecode_batch_head.ps1`、`run_claudecode_fusion_index_review.ps1` 之前写死了 `--model sonnet`。本轮已全部改为：

```powershell
claude -p --model opus --effort max --tools '' --output-format text
```

最小模型探针输出为 `OPUS_MODEL_CHECK_OK — Opus 4.7 responding.`；批次日志均写入 `MODEL opus; EFFORT max; NOTE Claude Opus 4.7 alias verified via minimal CLI check`。

## CLI 证据

- ClaudeCode 命令：`C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\Anthropic.ClaudeCode_Microsoft.Winget.Source_8wekyb3d8bbwe\claude.exe`
- 版本：`2.1.119 (Claude Code)`
- 本轮执行模式：`--model opus --effort max`
- 本轮不使用桌面 Claude App，也不使用旧 `sonnet` 参数。

## 重跑范围

- 主批次：`CLAUDECODE_BATCH_001.md` 至 `CLAUDECODE_BATCH_013.md`
- Opus 补头批次：`CLAUDECODE_BATCH_003_HEAD.md`、`004_HEAD.md`、`005_HEAD.md`、`007_HEAD.md`、`008_HEAD.md`、`009_HEAD.md`
- 运行队列记录：
  - `CLAUDECODE_OPUS47_QUEUE_PIDS.csv`
  - `CLAUDECODE_OPUS47_HEAD_QUEUE_PIDS.csv`
  - `CLAUDECODE_OPUS47_HEAD_QUEUE_PIDS_2.csv`
- 批次输出目录：`parts`
- 批次日志目录：`batch_logs`

## 运行结果

- 13 个主批次全部退出 `0`。
- 6 个现存补头批次全部退出 `0`。
- 所有主批次和补头批次的 stderr 均为 `0` bytes。
- 结构扫描显示 001、002、004、005、006、007、009、010、011、012、013 主批次均以 `# BATCH xxx 独立厚稿` 开头，并含六桶标题。
- 003、008 主输出存在开头截断，因此用 Opus/max 补头文件补足开头段；这是长 Markdown 输出截头问题，不是模型降级问题。

## 索引重建

- 已用 Opus 产物重建 `CLAUDECODE_COMBINED_CORE_INDEX.csv`。
- ClaudeCode Opus 索引抽取节点：247 个。
- 已同步重建 `CODEX_CURRENT_CORE_INDEX.csv`。
- 当前 Codex 终稿节点：94 个。
- 已用 Opus/max 重跑 `CLAUDECODE_INDEX_FUSION_RECOMMENDATIONS.md`，用于后续把 ClaudeCode 厚稿与 Codex 终稿再交给 GPT Pro 融合。

## 后续裁决

本轮只完成“ClaudeCode 独立厚稿生产线改用 Opus 4.7 alias 并重跑”。它还没有自动替换终稿，也没有完成新的 GPT Pro 主融合。下一步应把新的 ClaudeCode Opus 厚稿索引和融合建议交给 GPT Pro，由 GPT Pro 按用户 V2 权威链做主融合，再由 Codex 做证据回查、格式落盘和 Governor 校验。
