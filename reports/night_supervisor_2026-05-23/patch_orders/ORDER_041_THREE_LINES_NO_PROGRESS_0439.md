# ORDER_041_THREE_LINES_NO_PROGRESS_0439

触发时间：2026-05-24 04:39 +08

## 总管判定

04:09 至 04:39 巡检窗口内，三条线均无新增有效产物。不得写 `STRICT_FINAL_ACCEPTED`。

三线当前统一状态：`DELIVERED_WITH_GOVERNANCE_GAPS`。

## 共同硬命令

1. 不得把候选稿、可读稿、局部 PASS、父级旧外审、Codex 本地模拟意见写成严格终局。
2. 每条线必须先补控制文件，再补正文或交付物。控制文件至少要说明：本轮新增证据、仍缺什么、哪些旧结论被降级、下一步具体文件名。
3. 真实 GPT Pro / Claude Opus 若不可用，必须写 blocked/pending 文件，保存失败原因、会话证据或原始输出；不得用子 agent 代替。
4. Word/PDF QA 必须是产物级 QA；Markdown 检查不能代替 DOCX/PDF 渲染或导出验证。

## 选必一补丁命令

工作目录：
`reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23`

必须立刻产出或更新：

1. `07_gpt_pro_fusion/GPT_PRO_WEB_RETRY_STATUS.md`：记录 GPT Pro web 复核是否真实完成；若仍失败，写明失败方式，不得只写“待确认”。
2. `coverage_blockers_after_independent_thick_draft.csv`：逐条列出仍未闭合的 BATCH_015、12 个 `NEEDS_EVIDENCE`、2024 东城一模 Q16、顺义/延庆/丰台/海淀题号年份错配。
3. `CONFUCIUS_ARTIFACT_CHECK.md`：只读学生版/导航版成品，判断聪明高三学生能否直接迁移答题。
4. `WORD_PDF_RENDER_QA.md` 或 `RENDER_QA.md`：以最新 DOCX/PDF 为对象，不得沿用旧版截图。

若以上四项任一缺失，选必一继续保持 `DELIVERED_WITH_GOVERNANCE_GAPS`。

## 必修四补丁命令

工作目录：

- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23`
- `reports/bixiu4_philosophy_full_coverage_double_lane_2026-05-23`

必须立刻产出或更新：

1. `00_39_BLOCKER_STATUS.md`：说明 Chrome/GPT Pro web review、旧主观题 68 条质量失败、旧选择题 174 条缺口、最终 Governor/Confucius/Word-PDF QA 的当前真实状态。
2. `old_gap_closure_matrix_0039.csv`：逐条闭合旧缺题，不得只用总数报告代替。
3. 明确夜间 v8 仍只是可用候选，不得覆盖 4.29 v6 认可底稿，也不得把废弃重编版当最终底稿。

若 `00_39_BLOCKER_STATUS.md` 和 `old_gap_closure_matrix_0039.csv` 仍不存在，必修四继续保持 `DELIVERED_WITH_GOVERNANCE_GAPS`。

## 选必二补丁命令

根目录：
`reports/选必二法律主观题框架_从题源生长/v12_2_framework_growth_restart`

必须立刻产出或更新：

1. `V13_11_BLOCKER_STATUS.md`：说明 v13.11 是否启动；若未启动，列明卡点。
2. `v13_11_strict_acceptance_patch/`：只处理 v13.8-v13.10 学生化增量，不重写 v13.10 成品。
3. `v13_11_delta_review/`：保存真实 GPT Pro web 与 Claude Opus web 对 v13.10 delta 的原始复核记录；若失败，保存 blocked 证据。
4. `v13_11_final_baodian_integrated/`：只有 delta review、DOCX 直渲染/导出 QA、42 题 traceability reconciliation、开放容器裁决、rubric-level 学生全对检查全部闭合后才允许建立。

若 v13.11 目录和 `V13_11_BLOCKER_STATUS.md` 仍不存在，选必二继续保持 `DELIVERED_WITH_GOVERNANCE_GAPS`。

## 下一心跳判定标准

下一轮只看新证据，不听口头完成声明。若仍没有上述控制文件和 QA 文件，继续写 no-progress 补丁令并维持降级状态。
