# ORDER_017_XUANBIYI_GPT_PING_NOT_REVIEW_0239

生成时间：2026-05-24 02:39 +08:00

适用线程：选必一《当代国际政治与经济》严格最终重建线

## 状态判定

维持 `DELIVERED_WITH_GOVERNANCE_GAPS`；严格重建子线仍为 `RUNNING`，不得写 `STRICT_FINAL_ACCEPTED`。

## 本轮新增证据

- 02:16 `GPT_PRO_FILE_UPLOAD_CAPTURE.md` 仍只有 191 字节，Last Assistant Output 为“我”。
- 02:21 `GPT_PRO_PING_CAPTURE.md` 只返回 `OK`。这只能证明网页能响应 ping，不能计入 GPT Pro 内容审查。
- 02:22 生成 11 个 `GPT_PRO_BATCH_*_PROMPT.md`，都是待审提示包，不是模型输出。
- 02:37 `GPT_PRO_BATCH_01_CAPTURE.md` 仍只有 191 字节，Last Assistant Output 为“我”。
- 02:37 生成 `08_claude_opus_final_review_prompt.md`，但 `08_claude_opus_final_review_stdout.txt` 与 `stderr.txt` 均为 0 字节，输出目录无可验收文件。
- `GPT_PRO_WEB_RETRY_STATUS.md` 与 `coverage_blockers_after_independent_thick_draft.csv` 仍不存在。

## 硬补丁命令

1. 必须把 GPT Pro web gate 写成 `BLOCKED_ADVISOR_WEB_RESPONDS_BUT_CONTENT_REVIEW_EMPTY`。`OK` ping 不能当审查。
2. 立即写 `07_gpt_pro_fusion/GPT_PRO_WEB_RETRY_STATUS.md`，列明：
   - 文件上传捕获仍为“我”；
   - ping 仅返回 `OK`；
   - batch 01 捕获仍为“我”；
   - 当前没有有效 GPT Pro 内容审查。
3. 不得用 `GPT_PRO_BATCH_*_PROMPT.md` 冒充 GPT Pro 输出；它们只算待发送提示包。
4. Claude Opus 线当前只有 prompt 和空 stdout/stderr，必须标为 `CLAUDE_OPUS_NO_OUTPUT_YET`。没有 `CLAUDE_OPUS_FINAL_FUSION_PATCH.md` 等输出文件前，不得计入 Claude gate。
5. 先补 `coverage_blockers_after_independent_thick_draft.csv`，否则本地覆盖线也没有闭合依据。
6. 禁止生成最终 Word/PDF、最终 Governor 或 Confucius，直到 GPT/Claude/覆盖阻塞表三项至少有明确成功或 blocked 记录。

## 下一轮心跳只认这些证据

- `GPT_PRO_WEB_RETRY_STATUS.md`。
- `coverage_blockers_after_independent_thick_draft.csv`。
- `08_claude_opus_final_review/CLAUDE_OPUS_FINAL_FUSION_PATCH.md`、`CLAUDE_OPUS_FINAL_REJECT_DOWNGRADE.md`、`CLAUDE_OPUS_FINAL_REVIEW_SUMMARY.md` 或明确 Claude blocked 记录。
- 后续 Governor/Confucius、Word/PDF QA。
