# 必修四政治庄园新线程迁移交接包

时间：2026-05-24 22:58 +08

旧线程：`019dc06d-2f76-7d41-8b0a-19f3abd07076`

新线程任务：接管必修四政治庄园，不再依赖旧线程作为生产主线。

新线程：`019e5a7d-0e79-7643-a03d-2e7614d2acec`（worker: Feynman）

## 迁移原因

旧线程存在三类故障：

1. 线程进入 Plan Mode，22:23 明确说“目前还没开始改宝典，因为你这轮处在 Plan Mode，我不能直接写文件”，随后 `task_complete`。
2. 新 goal 在 `goals_1.sqlite` 中仍为 `active`，但 `tokens_used = 0`，说明目标挂着但没有进入有效执行。
3. 旧线程在 22:01、22:09 使用了 `claude.exe -p --model sonnet`。按用户硬要求，Sonnet/Haiku/模型不明证据不能计入合格 ClaudeCode 证据，必须换成 Opus 4.7 max effort / adaptive thinking。

另有风险：旧线程历史 `tokens_used = 410241187`，并且 memory_stage1 曾报 `Codex ran out of room in the model's context window`。继续在旧线程内推进，容易再次失控。

## 接管目标

用户新目标原文：

> 需要你确保：每一道题是否都涵盖在这个宝典里，2024-2026三年七十多套卷子，你要确保真的穷尽了。
> 第二，是否真的放对位置了。细则里到底有没有那个原理方法论，还是你自己凭空判断的，你需要一个题一个题去回溯，判断是真的切合细则，你自己的判断没有意义，细则有才算有。这件事要让codex和claudecode一起双生产线进行。
> 第三，是否格式渲染到位，字体这些新加的和先前的是否一致，我现在打开明显不一致。
> 第四，无论是新的还是旧的，是否够厚实，够扎实。逻辑论证是否扎实，这点让gptpro和claudeopus4.7adaptivethinking来审核，为了防止他们过载，生成完最终版后你可以分批发给他们审核，他们同意才算过。

## 可接管产物

主运行目录：

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24`

当前桌面候选产物：

- `C:\Users\Administrator\Desktop\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `C:\Users\Administrator\Desktop\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`
- `C:\Users\Administrator\Desktop\feige_bixiu4_philosophy_external_review_packet_2026-05-24.zip`
- `C:\Users\Administrator\Desktop\CURRENT_ACCEPTANCE_STATUS_20260524.md`

关键目录：

- `03_claudecode_lane/`
- `04_fusion_audit/`
- `05_delivery/`
- `06_governor_confucius/`
- `07_render_check/`
- `08_external_review/`

## 已知当前状态

候选包已经完成一轮 DOCX/PDF 重建和外审包生成，不能直接作废；但不能签严格最终。

已知验证数字：

- accepted inserted rows: 36
- delivery ledger rows: 36
- final PDF pages: 236
- coverage matrix status: 35 rows `COVERED_OR_PATCHED`
- final ZIP exists

边界：

- GPTPro web 外审未形成严格闭环。
- ClaudeCode 中至少两次 Sonnet 调用必须剔除，不得作为合格证据。
- 旧线程已在 Plan Mode 停止执行。

## 必须作废的证据

旧线程日志显示以下 ClaudeCode 调用使用了 Sonnet：

- 2026-05-24 22:01: `PROMPT_VERIFY_GPTPRO_WEB_FIXES_20260524.md | claude.exe -p --model sonnet`
- 2026-05-24 22:09: `PROMPT_VERIFY_BATCH03_CLEANUP_20260524.md | claude.exe -p --model sonnet`

因此以下输出只能作为参考，不得计入合格 ClaudeCode 硬证据，除非用 Opus 4.7 max effort 重新跑并生成新记录：

- `03_claudecode_lane/claudecode_verify_gptpro_web_fixes_20260524.md`
- `03_claudecode_lane/claudecode_verify_batch03_cleanup_20260524.md`

## 新线程第一批文件

新线程必须在本目录下创建或更新：

- `THREAD_RECOVERY_STATUS_20260524.md`
- `MODEL_EVIDENCE_LEDGER.md`
- `SONNET_INVALIDATION_LEDGER.md`
- `OPUS47_CLAUDECODE_RECHECK_PROMPT.md`
- `OPUS47_CLAUDECODE_RECHECK_RESULT.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `FORMAT_RENDER_QA_20260524.md`
- `GOVERNOR_RECOVERY_REPORT_20260524.md`
- `CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`

## 执行硬规则

1. 不得继续使用旧线程作为生产主线。
2. 不得使用 Sonnet、Haiku 或模型不明输出作为合格 ClaudeCode 证据。
3. ClaudeCode 合格证据必须是 Opus 4.7 max effort / adaptive thinking，并在 `MODEL_EVIDENCE_LEDGER.md` 写明模型、时间、命令、输入、输出。
4. 若无法确认 Opus 4.7 max effort，写 `BLOCKED_MODEL_CONFIRMATION_REQUIRED`，不得伪造 PASS。
5. 当前状态只能是 `RECOVERED_EXECUTION_IN_PROGRESS` 或 `DELIVERED_WITH_GOVERNANCE_GAPS`，不得写 `STRICT_FINAL_ACCEPTED`。
6. 每题是否覆盖、是否放对位置，必须回到题源/细则/评标/评分文件。普通参考答案不能冒充细则。
7. 选择题链与主观题评分链必须分开。
8. DOCX/PDF 必须做渲染 QA，格式不一致要列出页码或位置。
9. GPTPro web 和 Claude Opus 外审如果未真实完成，必须保留 `real_call_pending`。

## 新线程第一句话

新线程启动后应先写：

`THREAD_RECOVERY_STATUS = RECOVERED_EXECUTION_IN_PROGRESS`

并说明已经接管旧线程 `019dc06d-2f76-7d41-8b0a-19f3abd07076`，旧线程不再作为生产主线。
