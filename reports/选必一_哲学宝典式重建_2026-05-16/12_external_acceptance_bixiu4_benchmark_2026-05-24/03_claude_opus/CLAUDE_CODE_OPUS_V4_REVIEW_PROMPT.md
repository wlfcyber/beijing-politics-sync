# Claude Code Opus v4 Review Prompt

你是 Claude Opus 审稿人。请复审学生版 v4 是否已关闭 GPT Pro 一审与 Claude fallback 审稿中的 P0。

## 必读文件

1. 学生版 v4：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\选必一_当代国际政治与经济_主观题术语宝典_学生精简版_v4.md`

2. v4 本地重写报告：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\V4_LOCAL_REWRITE_REPORT.md`

3. 上一轮 Claude fallback FAIL 报告：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\03_claude_opus\CLAUDE_CODE_OPUS_FALLBACK_REVIEW_CAPTURE_20260524.md`

4. GPT Pro 一审报告：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\02_gptpro_web\GPTPRO_REVIEW_CAPTURE_20260524.md`

## 核心判定

请重点判断：

- 351 个独立题例是否仍在。
- 不同题是否没有被合并。
- 同题组提示是否解决了“同一道题多点散落”问题，还是制造了新的重复负担。
- `为什么能想到` 是否已经从机械模板转成可接受的学生审题语言。
- 学生版是否还残留后台字段或二代后台词。
- 经济全球化、政治多极化、中国外交、联合国、理论桶边界是否有重大错误。
- 是否已经可以进入 GPT Pro 复审和网页 Claude Opus/Adaptive 复审。

## 输出格式

1. 最终结论：PASS / FAIL / CONDITIONAL_PASS。
2. 是否可送 GPT Pro 与网页 Claude Opus 复审：是/否。
3. 若 FAIL，列出 P0 必修清单，不超过 10 条，必须具体到位置或可检索句式。
4. 若 CONDITIONAL_PASS，列出必须在最终版前补的 P1/P2。
5. 对上一轮 FAIL 的六个 P0-A 至 P0-F 逐条给关闭判断。

不要修改文件，只输出审核报告。

