你是 ClaudeCode Opus 4.7。请作为独立审计员，复核 GPT Pro 指出的学生版后台词 P0 已清理后，当前选必一宝典是否仍有必须修的内容硬伤。

重要边界：

1. 这不是 Claude 桌面应用端复审。Claude 桌面应用当前白屏，应用端 PASS 仍未闭合。
2. 你是 ClaudeCode CLI 真实模型复核，只能作为 provisional reviewer / ClaudeCode evidence，不能替代 Claude 应用端 Opus Adaptive gate。
3. 不要重写全文。只做审计和必要补丁建议。

请读取并审计这些文件：

1. 终稿：
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md

2. 候选稿：
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\选必一_当代国际政治与经济_主观题术语宝典_学生版_v7_rescue_candidate.md

3. 本轮 GPT Pro 失败与修复证据：
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\GPTPRO_V7_POST_PATCH_COMPACT_REVIEW_CAPTURE_20260525.md
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\P0_GPTPRO_BACKEND_WORD_CLEANUP_REPORT_20260525.md
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\GPTPRO_V7_POST_CLEANUP_PASS_WITH_SCOPE_CAPTURE_20260525.md
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\P0_POST_GPTPRO_CLEANUP_LOCAL_QA_20260525.md

4. 覆盖与阻断报告：
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\P0_FINAL_COVERAGE_RECONCILIATION_20260525.md
   C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\FINAL_ACCEPTANCE_AND_BLOCKER_REPORT_20260525.md

必须检查：

- 学生版正文是否仍残留这些后台/管线词：细则、评标、评分、参考答案、rubric、PASS、FAIL、Claude、GPT、Codex、来源：、挂载审计。
- 141 个核心答题点、373 主桶题例、380 个 `###` 题号标题的口径是否自洽。
- 是否还有一个 `###` 标题合并两个不同题号。
- 经济全球化是否仍把不能互相替代的术语粗并。
- 政治多极化/中国/联合国/理论四类是否还有明显错归。
- 独立自主和平外交政策、和平共处五项原则、新型国际关系、开放型世界经济等高风险点是否仍错层。

输出格式：

- verdict：PASS / PASS_WITH_PATCH / FAIL_MUST_PATCH / FAIL_REBUILD 四选一。
- local_content_status：评价终稿本地内容是否还有 P0。
- gpt_patch_status：评价 GPT Pro 本轮 FAIL 点是否已经修复；必须区分 PASS_WITH_SCOPE 与整稿 full-pass。
- claude_app_gate_status：必须诚实说明应用端 gate 当前是否仍 pending。
- must_fix_items：若有，给文件、标题/题号、原因、具体修法。
- allowed_claim：现在最多能对用户怎么说，不得夸大。
- next_actions：最多 5 条。

严格要求：

- 输出中文。
- 不要泛泛建议。
- 如果只是外部 gate 未闭合，不能要求重建全文。
- 如果发现内容硬伤，必须给出具体标题/题号，不能只说“建议加强”。
