# ORDER_018_XUANBIYI_CANDIDATE_MERGED_GAPS_0309

生成时间：2026-05-24 03:09 +08:00

适用线程：选必一《当代国际政治与经济》严格最终重建线

## 状态判定

从“无推进”改判为：`DELIVERED_WITH_GOVERNANCE_GAPS`。

理由：Claude Opus 已产出终审融合补丁，且 37 条新增已合入学生版 Markdown/Word 候选；但 GPT Pro gate 仍无有效内容输出，覆盖阻塞表缺失，DOCX 渲染 QA 被跳过，Confucius 未闭合，因此不得写 `STRICT_FINAL_ACCEPTED`。

## 本轮新增证据

- `08_claude_opus_final_review/CLAUDE_OPUS_FINAL_FUSION_PATCH.md`：51 条 accepted，6 桶。
- `08_claude_opus_final_review/CLAUDE_OPUS_FINAL_REJECT_DOWNGRADE.md`：17 DOWNGRADED、13 NEEDS_EVIDENCE、49 EXCLUDE_OTHER_MODULE、3 个反合并残留 NEEDS_EVIDENCE。
- `08_claude_opus_final_review/CLAUDE_OPUS_FINAL_REVIEW_SUMMARY.md`：记录 10 个 Codex×ClaudeCode 冲突裁决。
- `09_integration_report.md`：51 条补丁中 14 条原文已含，37 条新增插入。
- `MODEL_EVIDENCE_LEDGER.md`：明确 GPT Pro 多次捕获仅为单字符或 ping `OK`，不计入内容源。
- `FINAL_STRICT_GOVERNOR_AUDIT.md`：状态为 `DELIVERED_WITH_GPT_PRO_WEB_FAILURE_DISCLOSED`，并记录 DOCX render QA skipped。

## 硬补丁命令

1. 不得把当前选必一称为严格最终；只能称为“Claude Opus 候选合入版/披露 GPT Pro web 失败的候选交付”。
2. 必须补写 `07_gpt_pro_fusion/GPT_PRO_WEB_RETRY_STATUS.md`，把多次“我”、`OK` ping、batch 捕获失败逐项列入，并明确 `BLOCKED_ADVISOR_WEB_RESPONDS_BUT_CONTENT_REVIEW_EMPTY`。
3. 必须补写 `coverage_blockers_after_independent_thick_draft.csv`，至少覆盖：
   - 13 个 `NEEDS_EVIDENCE`；
   - 顺义二模 Q20；
   - 2026 东城期中 Q20；
   - 2026 石景山二模 Q19；
   - 2024 东城一模 Q16 是否为哲学/非选必一边界；
   - 顺义一模 Q19/Q20 题号核对；
   - 2026 朝阳期中 Q17 是否漏入队列。
4. 必须做 Word/PDF 视觉 QA：当前 Governor 记录 `DOCX render QA skipped`，这不能过终验。优先从 docx 导出 PDF 并 rasterize；失败则保留 caveat。
5. 必须新增 Confucius artifact-only 检查，只读合入后的学生版 Markdown/Word，判断 37 条新增是否能让高三学生按“材料信号 -> 术语 -> 答案句”迁移。
6. 若不能完成 GPT Pro web 内容审查，最终状态只能写 `DELIVERED_WITH_GOVERNANCE_GAPS` 或 `BLOCKED_ADVISOR`，不能写 `STRICT_FINAL_ACCEPTED`。

## 下一轮心跳只认这些证据

- `GPT_PRO_WEB_RETRY_STATUS.md`。
- `coverage_blockers_after_independent_thick_draft.csv`。
- Word/PDF render QA。
- Confucius artifact-only 检查。
- 若 GPT Pro 恢复，则完整原始回复和截图/链接。
