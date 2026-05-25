# ORDER_061_BIXIU4_THREAD_FAULT_RECOVERY_2255

时间：2026-05-24 22:55 +08

目标线程：`019dc06d-2f76-7d41-8b0a-19f3abd07076`（必修四 政治庄园）

## 故障判定

该线程当前不是正常后台推进状态，而是线程层故障状态。

## 证据

1. 该线程在 2026-05-24 22:21 进入 Plan Mode，随后只做读取检查。
2. 该线程在 2026-05-24 22:23 明确回复：“目前还没开始改宝典，因为你这轮处在 Plan Mode，我不能直接写文件。”
3. 该线程随后 `task_complete`，没有继续推进目标执行。
4. `goals_1.sqlite` 中该线程新 goal 仍为 `active`，但 `tokens_used = 0`，说明新目标创建后没有进入有效执行统计。
5. 同一线程在 2026-05-24 22:01、22:09 两次调用 `claude.exe -p --model sonnet`，违反用户硬要求：ClaudeCode 必须换成 Opus 4.7 max effort 才能计入合格证据。
6. `state_5.sqlite` 中该线程历史 `tokens_used = 410241187`，且 memory_stage1 job 曾报错：`Codex ran out of room in the model's context window. Start a new thread or clear earlier history before retrying.` 该线程上下文已经极重，不适合作为继续生产主线。

## 恢复命令

不要继续在该线程内只做 Plan Mode 方案。恢复路径必须二选一：

### 路径 A：保留原线程，但必须人工切回 Default/执行模式

在必修四线程 UI 中切回 Default/执行模式后，立即发送：

```text
继续当前 active goal，但先执行故障恢复：
1. 停止使用任何 sonnet/haiku/model unknown 的 ClaudeCode 证据。
2. 所有 ClaudeCode 命令必须使用 Opus 4.7 max effort / adaptive thinking，并在 MODEL_EVIDENCE_LEDGER.md 写明模型、时间、命令、输出文件。
3. 不要继续 Plan Mode；直接执行文件核查、逐题矩阵、格式渲染 QA、厚度审核和外审包重建。
4. 当前状态只能写 DELIVERED_WITH_GOVERNANCE_GAPS；不得写 STRICT_FINAL_ACCEPTED，直到 GPTPro web + Claude Opus 4.7 + 逐题证据矩阵 + Governor/Confucius + Word/PDF QA 全部闭合。
```

### 路径 B：停止依赖旧线程，新开执行线程接管

建议采用路径 B。旧线程上下文过大，且已进入 Plan Mode 误停；新执行线程从以下文件接管：

- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/`
- `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`
- `06_governor_confucius/CURRENT_ACCEPTANCE_STATUS_20260524.md`
- `08_external_review/feige_bixiu4_philosophy_external_review_packet_2026-05-24.zip`

新线程第一任务：

1. 读取上列文件。
2. 建 `MODEL_EVIDENCE_LEDGER.md`，剔除 Sonnet 复核，不计入合格证据。
3. 用 Opus 4.7 max effort 重新跑 ClaudeCode 复核。
4. 建逐题覆盖与位置矩阵：每题题源、题号、细则支持原理、宝典落点、证据强度、是否需改。
5. 对最终 DOCX/PDF 做格式一致性和渲染页 QA。
6. 将结论写成 `THREAD_RECOVERY_STATUS_20260524.md`，状态只能是 `RECOVERED_EXECUTION_IN_PROGRESS` 或 `DELIVERED_WITH_GOVERNANCE_GAPS`。

## 监督结论

该线程的“目标+计划”卡住不是内容工作自然慢，而是：

- UI/线程进入 Plan Mode；
- 新 goal active 但没有有效执行；
- 还违规使用 Sonnet；
- 上下文过载风险极高。

必须重启执行链，且 ClaudeCode 证据必须重跑为 Opus 4.7 max effort。
