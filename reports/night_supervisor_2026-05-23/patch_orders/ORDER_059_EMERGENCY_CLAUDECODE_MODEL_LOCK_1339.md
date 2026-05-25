# ORDER_059_EMERGENCY_CLAUDECODE_MODEL_LOCK_1339

时间：2026-05-24 13:39 +08  
触发：用户明确要求检查当前线程中是否有 ClaudeCode 使用 Sonnet，并紧急叫停；只有 `Opus 4.7 / max effort` 才算合格。

## 总判定

立即生效：三条线所有 ClaudeCode 产物必须满足 `--model opus --effort max` 或等价的 `Opus 4.7 / max effort` 可核验证据。凡是 `sonnet`、`haiku`、默认模型、未知模型、或无模型证据的 ClaudeCode 输出，均不得计入最终验收。

本轮进程表检查未发现正在运行的 `claude --model sonnet` ClaudeCode CLI 进程；仅发现 Claude 桌面客户端进程，命令行不含 Sonnet/Opus CLI 参数。因此本轮没有可安全精准击杀的 Sonnet CLI 进程。

## 已定位的模型风险

### 1. 选必一：旧 Sonnet 问题属实，但最新审计称已改 Opus/max

风险来源：

- `选必一_哲学宝典式重建_2026-05-16/07_claudecode_full_rerun/CLAUDECODE_RUN_AUDIT.md`
- `选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/02_gptpro_web/primary_fusion_remediation_packet_20260524/07_CLAUDECODE_RUN_AUDIT.md`

审计内容显示：旧问题属实，`run_claudecode_single_batch.ps1`、`run_claudecode_batch_head.ps1`、`run_claudecode_fusion_index_review.ps1` 曾写死 `--model sonnet`。该审计同时声称本轮已改为：

```powershell
claude -p --model opus --effort max --tools '' --output-format text
```

处理命令：

1. 选必一禁止使用任何旧 Sonnet 批次作为合格证据。
2. 只有能追溯到 `CLAUDECODE_RUN_AUDIT.md` 中 Opus/max 重跑范围的批次，才可作为 ClaudeCode 生产线候选证据。
3. 若发现正文或融合仍引用旧 Sonnet 批次，必须立刻标记 `BLOCKED_MODEL_DOWNGRADE`，从同一 prompt、同一源范围用 `--model opus --effort max` 重跑。
4. 选必一最终验收仍不能用 ClaudeCode Opus fallback 替代用户可见 Claude Opus/Adaptive 外部审查。

### 2. 选必一：Haiku 调试日志也不合格

发现位置：

- `08_2026_second_mock_backfill/02_claudecode_independent/claudecode_debug.log`
- `08_2026_second_mock_backfill/06_claudecode_after_gpt_review/claudecode_gpt_review_debug.log`

日志显示模型为 `claude-haiku-4-5-20251001`。这不是 Sonnet，但同样不满足用户现在指定的 `Opus 4.7 / max effort` 合格线。

处理命令：

1. 这两条 Haiku 运行不得计入合格 ClaudeCode 证据。
2. 若其中内容被并入候选正文、覆盖矩阵、Governor 或 GPT/Claude 提交包，必须标注来源降级，并由 Opus/max 重跑覆盖。

### 3. 必修四：未见 Sonnet 命令，但模型证据不足时不得合格

本轮在当前必修四活动目录中未检出 `sonnet` 或 `haiku`。但新增 ClaudeCode 二模复核文件若没有完整模型启动证据，不得仅凭文件名 `ClaudeCode` 计入硬验收。

处理命令：

1. 必修四后续所有 ClaudeCode 补丁、复核、审计必须附模型锁定证明。
2. 证明至少包括：ClaudeCode 版本、完整命令、`--model opus --effort max`、stdout/stderr 或 debug/stream 证据、产物路径。
3. 没有模型证据的 ClaudeCode 复核只能作为线索，不能作为合格生产/外审门槛。

### 4. 选必二：未见 Sonnet 命令，但继续要求模型证据闭环

本轮在选必二当前目录未检出 `sonnet` 或 `haiku`，现有主要外部 Claude 记录多为用户可见 `Opus 4.7 Adaptive`。但后续 v13.11/v14 任何新增 ClaudeCode 或 Claude 审查必须重新给出模型证据，不能引用旧记录自动过门。

处理命令：

1. 选必二 v13.11/v14 若要升级验收，必须补真实 GPT Pro + Claude Opus/Adaptive delta review。
2. 任何 ClaudeCode 本地 fallback 必须用 `--model opus --effort max`，且不得替代真实 Claude Opus/Adaptive web/app 门槛。

## 全线模型锁定规则

从本补丁令起，三线所有 ClaudeCode 相关产物必须在同目录或控制台账中留下：

- `model_gate: CLAUDECODE_OPUS47_MAX_EFFORT`
- `command: claude -p --model opus --effort max ...`
- `claude_version`
- `started_at` / `finished_at`
- `stdout_path` / `stderr_path` / `debug_or_stream_path`
- `exit_code`
- `evidence_scope`
- `does_not_replace_real_claude_opus_web_or_app_gate`

禁止写法：

- `--model sonnet`
- `--model haiku`
- 未显式指定模型
- 仅写“ClaudeCode 已审查”但无命令与模型证据
- 用 ClaudeCode Opus fallback 冒充用户可见 Claude Opus/Adaptive 最终门槛

## 下一轮总管检查

下一轮必须优先检查：

1. 是否出现新的 `sonnet` / `haiku` / 默认模型 ClaudeCode 记录。
2. 是否有线程把旧 Sonnet/Haiku 产物并入正文或验收台账。
3. 是否出现 `CLAUDECODE_OPUS47_MAX_EFFORT` 模型锁定证明。
4. 若有非 Opus/max 运行，立刻发出 `STOP_AND_RERUN_OPUS47_MAX_EFFORT`，并把对应候选降级为 `DELIVERED_WITH_GOVERNANCE_GAPS` 或 `BLOCKED_MODEL_DOWNGRADE`。
