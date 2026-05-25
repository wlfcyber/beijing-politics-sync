# heartbeat_20260524_1339_model_lock

巡检时间：2026-05-24 13:39 +08  
触发：用户要求紧急检查 ClaudeCode 是否使用 Sonnet，并叫停降级模型。  
补丁令：`patch_orders/ORDER_059_EMERGENCY_CLAUDECODE_MODEL_LOCK_1339.md`

## 结论

当前没有发现正在运行的 `claude --model sonnet` ClaudeCode CLI 进程；进程表只看到 Claude 桌面客户端，不含 Sonnet/Opus CLI 参数。因此没有执行进程击杀。

文件证据层面，选必一旧 ClaudeCode 生产线曾经使用 Sonnet，且审计文件明确承认这一点；最新审计称已改为 `--model opus --effort max` 重跑。另有两条选必一 Haiku 调试日志，虽不是 Sonnet，也不满足用户指定的 Opus 4.7 max-effort 合格线。

## 各线状态

| 线程 | Sonnet/非 Opus 风险 | 本轮处置 |
| --- | --- | --- |
| 选必一 | 旧 `07_claudecode_full_rerun` 审计承认三个脚本曾写死 `--model sonnet`；`08_2026_second_mock_backfill` 两条 debug log 使用 `claude-haiku-4-5-20251001` | 写入紧急模型锁定令。旧 Sonnet/Haiku 产物不得计入合格证据；只有可追溯到 `--model opus --effort max` 重跑的产物可进入候选。 |
| 必修四 | 当前活动目录未检出 `sonnet`/`haiku`，但新增 ClaudeCode 复核需补完整模型证明 | 要求后续所有 ClaudeCode 产物写明 `CLAUDECODE_OPUS47_MAX_EFFORT`、完整命令、版本、日志、退出码。 |
| 选必二 | 当前目录未检出 `sonnet`/`haiku`；主要 Claude 记录为 Opus 4.7 Adaptive web/app 记录，但 v13.11/v14 增量不能套旧记录 | 要求新增 delta review 继续使用真实 GPT Pro + Claude Opus/Adaptive；本地 ClaudeCode fallback 必须 `--model opus --effort max` 且不能替代真实外部门槛。 |

## 硬门槛

从本轮起，任何 ClaudeCode 输出只要无法证明 `Opus 4.7 / max effort`，就不能作为合格生产证据，也不能支撑 `STRICT_FINAL_ACCEPTED`。

继续监督，不结束 automation。
