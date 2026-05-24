你是 ClaudeCode Opus 4.7。请作为独立审计员，不要重写全文，只审计当前选必一宝典是否已经达到用户目标。

用户目标：生成一份类似必修四哲学宝典含金量的《选择性必修一 当代国际政治与经济》主观题术语/答题点宝典。必须覆盖 2024-2026 模拟题中纳入范围的主观题；不能把两道题合并成一个题例；不能把不同模块、不能互相替代的术语粗合并；Codex 与 ClaudeCode 都要是真实生产/审计链路；GPT Pro 和 Claude Opus 外部审核不能用本地模拟冒充。

请读取并审计这些文件：
1. 终稿：C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md
2. 本轮覆盖复核与断点说明：C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\P0_FINAL_COVERAGE_RECONCILIATION_20260525.md
3. 凌晨最终验收与阻断说明：C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\FINAL_ACCEPTANCE_AND_BLOCKER_REPORT_20260525.md
4. 同目录下的 ClaudeCode / GPT / P0 审核捕获文件，如有必要请自行读取。

你必须输出：
- verdict：PASS / PASS_WITH_PATCH / FAIL_MUST_PATCH / FAIL_REBUILD 四选一。
- local_content_status：只评价终稿本身是否仍有 P0 内容硬伤，包括漏题、混题、出现次数错误、分类错位、经济全球化粗合并、政治多极化/中国/联合国错归类、外交政策/和平共处五项原则错层。
- external_gate_status：评价 GPT Pro、Claude 应用端/ClaudeCode、逐 5 题循环、哲学宝典对标是否真的闭合。不能把没有原文证据的 gate 说成通过。
- must_fix_items：若有，列具体文件、标题/题号/模块、原因、修法。
- allowed_claim：现在对用户最多能诚实宣称到什么程度。
- next_actions：最多 5 条，按优先级排序。

严格要求：
- 不要泛泛建议。
- 如果终稿本地内容已无明显 P0，但外部 gate 未闭合，请明确区分“本地内容候选可读/可继续”与“最终目标未通过”。
- 检查是否还有单个 ### 题例标题中混入两个不同题号；若只靠报告，必须说明是基于报告还是你重新扫描了文件。
- 输出中文。
