# 选必一终稿验收状态与故障原因记录（2026-05-25）

## 1. 为什么下午还能跑，后来又断了

本地终稿没有丢，也不是正文倒退。断点出在外部审核通道：

- Claude Windows 应用端从可用状态退化为白屏/登录态异常。日志和现场恢复显示，问题集中在本地应用缓存、Web 状态、代理/网络路径与登录态握手；白屏已恢复到登录/账号选择页，但仍需要用户侧完成账号选择，不能由 Codex 代点。
- Chrome/网页通道曾卡在 Google/OpenAI 登录链路，无法作为稳定的 GPT Pro 上传通道。
- ChatGPT Desktop 仍可用，并确认是 Pro 模式，因此最终 GPT Pro 审核链路改走 ChatGPT Desktop。

结论：下午“还好好的”是因为外部应用会话当时还在；后来本机应用状态和登录态断裂，导致 Claude 应用审核不能继续。正文文件本身一直可恢复、可校验。

## 2. 当前终稿

- 终稿源文件：`reports/选必一_哲学宝典式重建_2026-05-16/12_external_acceptance_bixiu4_benchmark_2026-05-24/04_v7_rescue_fusion/选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md`
- 桌面短文件名副本：`C:\Users\Administrator\Desktop\xuanbiyi_final_20260525.md`
- SHA256：`E7043252D04AA265F2D48E7520DEC85DCAFD5018F0A527B327BF735DB9CFE5FF`

本地硬指标复扫：

- 核心答题点：141
- 核心题例期望数：372
- 核心题例实际数：372
- 全文 `###`：380
- 频次不匹配：0
- `2025西城二模Q20(2)` 残留：0
- `2024东城一模Q16` 主链内出现：0
- `2024东城一模Q16` 边界独立题例：1
- TODO/待补/待核/FIXME：0
- 内部调试标记：0
- 混题标题：0
- `和平与发展仍是时代主题（出现18次）` 编号：1-18 连续
- `推动构建人类命运共同体（出现10次）` 编号：1-10 连续

## 3. GPT Pro 审核链

已真实走 ChatGPT Desktop / GPT Pro：

- `GPTPRO_DESKTOP_FULLFILE_REVIEW_CAPTURE_20260525_1012.md`：GPT Pro 第一轮全文审查为 `FAIL_MUST_PATCH`，指出 Q16 边界、经济全球化拆分、WTO/开放型世界经济解释缺失、零关税题号等硬伤。
- `GPTPRO_POST_PATCH_FUSION_REVIEW_CAPTURE_20260525_1008.md`：补丁后 GPT Pro 判定 `PASS_WITH_MINOR_PATCH`，只剩附录 Q16 独立结构和两处编号连续性问题。
- `GPTPRO_FINAL_PATCH_CONFIRM_UIA_TEXT_20260525.md`：三处小修完成后，GPT Pro 最终确认 `VERDICT: STRICT_FINAL_ACCEPTED`。

GPT Pro 最终可宣称口径：

> 当前终稿已完成 Codex + ClaudeCode 两线融合；上一轮 GPT Pro 要求的三处小修已闭合，核心点计数一致、Q16 边界独立、两处编号连续、无残留 Q20(2)、无混题标题、无待办和调试标记；经 GPT Pro 最终补丁确认，判定为 `STRICT_FINAL_ACCEPTED`。

## 4. Claude 应用端状态

Claude 应用端已经从白屏恢复到登录/账号选择步骤，但账号选择涉及用户身份，Codex 不能代点。

因此当前严谨状态是：

- ClaudeCode Opus 4.7 生产/审计证据：已有。
- Claude Windows 应用端 Opus Adaptive 最终审核：仍为 `real_call_pending`，不能宣称已通过。

## 5. 当前可对用户说的话

可以说：

- 终稿正文和结构硬指标已修干净。
- GPT Pro 最终补丁确认已通过。
- Claude 应用白屏问题已恢复到账号授权步骤。

不能说：

- 不能说 Claude 应用端 Opus Adaptive 已完成最终审核。
- 不能说所有外部通道都完全恢复。
