# ORDER_014_XUANBIYI_WEB_STUCK_SINGLE_CHAR_0109

生成时间：2026-05-24 01:09 +08:00

适用线程：选必一《当代国际政治与经济》严格最终重建线

## 状态判定

维持 `DELIVERED_WITH_GOVERNANCE_GAPS`；严格重建子线仍为 `RUNNING`，不得写 `STRICT_FINAL_ACCEPTED`。

## 本轮新增证据

- 00:53 更新 `07_gpt_pro_fusion/GPT_PRO_FUSION_CAPTURE_CONTINUE.md`，长度仍为 191 字节。
- 文件内容显示 Last Assistant Output 只有单字“我”。
- 00:54 生成 `GPT_PRO_FUSION_COMPACT_PROMPT.md`，这是给 GPT Pro 的压缩提示包，不是 GPT Pro 审查结果。
- `GPT_PRO_WEB_RETRY_STATUS.md` 仍不存在。
- `coverage_blockers_after_independent_thick_draft.csv` 仍不存在。

## 硬补丁命令

1. 立即停止把当前 ChatGPT 网页会话当作有效外审。该会话当前状态必须记为 `BLOCKED_ADVISOR_CAPTURE_INCOMPLETE_SINGLE_CHAR_OUTPUT`。
2. 在 `07_gpt_pro_fusion/` 下写 `GPT_PRO_WEB_RETRY_STATUS.md`，明确：
   - 最近完整捕获失败时间；
   - 失败形态：只输出“我”；
   - 是否需要新建 ChatGPT 会话或等待用户醒后人工确认网页状态；
   - 当前不能计入 GPT Pro gate。
3. 若继续尝试 GPT Pro，不要继续覆盖 `GPT_PRO_FUSION_CAPTURE_CONTINUE.md`；另存为 `GPT_PRO_FUSION_CAPTURE_FULL_YYYYMMDD_HHMM.md`，否则总管无法区分残片重试和完整输出。
4. 在没有完整 GPT Pro 输出前，仍可做本地证据整理，但必须先建立 `coverage_blockers_after_independent_thick_draft.csv`，至少列：
   - `BATCH_015`
   - 13 项 `NEEDS_EVIDENCE`
   - 2024 东城一模 Q16
   - 题号/年份错配项
   - 每项当前源证据等级与能否入主表
5. 不得用 `GPT_PRO_FUSION_COMPACT_PROMPT.md` 冒充外审记录；它只能算“待发送提示包”。

## 下一轮心跳只认这些证据

- `GPT_PRO_WEB_RETRY_STATUS.md`。
- `GPT_PRO_FUSION_CAPTURE_FULL_*.md` 且包含完整 GPT Pro 原始回复。
- `coverage_blockers_after_independent_thick_draft.csv`。
- 后续 Claude Opus delta、Governor/Confucius、Word/PDF QA。
