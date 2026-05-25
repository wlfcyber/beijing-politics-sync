# ORDER_012_XUANBIYI_GPTPRO_CAPTURE_BLOCKER_0009

生成时间：2026-05-24 00:09 +08:00

适用线程：选必一《当代国际政治与经济》严格最终重建线

## 状态判定

维持 `DELIVERED_WITH_GOVERNANCE_GAPS`；`11_strict_final_rebuild_2026-05-23` 子线仍为 `RUNNING`，不得写 `STRICT_FINAL_ACCEPTED`。

## 本轮发现的新证据

- 23:43 生成 `06_claudecode_independent_opus47/CLAUDECODE_INDEPENDENT_THICK_DRAFT.md`。
- 23:45 生成 `06_claudecode_independent_opus47/CLAUDECODE_INDEPENDENT_RISK_LOG.md`。
- 23:48 生成 `07_gpt_pro_fusion/GPT_PRO_FUSION_PROMPT.md`，长度约 172K，说明已准备 GPT Pro 融合包。
- 23:52 与 23:53 生成 `GPT_PRO_FUSION_CAPTURE*.md`，但捕获文件长度只有 191 字节，Last Assistant Output 只有残片，不能作为真实 GPT Pro 复核记录。
- 严格重建目录仍未出现新的 `.docx`、`.pdf`、渲染 PNG、最终 Governor、最终 Confucius。

## 硬补丁命令

1. 不得把 `GPT_PRO_FUSION_CAPTURE.md` 或 `GPT_PRO_FUSION_CAPTURE_CONTINUE.md` 记为 GPT Pro 通过。它们只能标记为 `BLOCKED_ADVISOR_CAPTURE_INCOMPLETE`。
2. 重新执行 GPT Pro web 融合复核，必须保存完整原始回答、会话链接、截图或可审计日志。若网页仍只返回残片，写 `GPT_PRO_WEB_RETRY_BLOCKED.md`，不要继续升级。
3. 用 GPT Pro 完整复核时，输入必须覆盖三件事：
   - ClaudeCode 独立厚稿与风险日志；
   - `BATCH_015`、13 项 `NEEDS_EVIDENCE`、2024 东城一模 Q16、题号/年份错配；
   - 是否允许把 30 个独立单题条目并入学生宝典，以及哪些条目必须降级/排除。
4. GPT Pro 完整复核完成后，必须再跑 Claude Opus delta 复核，不能用旧父级外审覆盖新补丁。
5. 在真实 GPT/Claude delta 都完成前，不得生成 `GOVERNOR_STRICT_FINAL_ACCEPTANCE`，不得生成最终 Word/PDF。
6. 若完成外审并进入成品化，必须先产出新的学生版 Markdown，再生成 Word/PDF，再保存渲染 QA 与页数/空白页检查。

## 下一次心跳要检查

- 是否出现完整 GPT Pro 原始回答，而不是 191 字节残片。
- 是否出现 Claude Opus delta 复核。
- 是否出现 `BATCH_015` 与 `NEEDS_EVIDENCE` 的逐题闭合表。
- 是否出现新的 Word/PDF 与渲染 QA。
