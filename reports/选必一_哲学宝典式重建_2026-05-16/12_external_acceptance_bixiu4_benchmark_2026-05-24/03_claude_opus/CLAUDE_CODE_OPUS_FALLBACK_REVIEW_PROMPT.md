# Claude Code Opus Fallback Review Prompt

你是 Claude Opus 审稿人。请以最高强度审稿模式，审核选择性必修一《当代国际政治与经济》主观题术语宝典学生版 v2。

## 必读文件

1. 学生版 v2：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\选必一_当代国际政治与经济_主观题术语宝典_学生精简版_GPT一审后_v2.md`

2. GPT Pro 一审原始反馈：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\02_gptpro_web\GPTPRO_REVIEW_CAPTURE_20260524.md`

3. GPT 一审后 v1/v2 修订说明：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\GPT一审修订说明.md`
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\GPT一审后学生版v2修订说明.md`

4. 必修四哲学宝典标杆摘要与样本：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\01_review_materials\03_bixiu4_benchmark_status.md`
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\01_review_materials\02_bixiu4_philosophy_benchmark_student.md`

## 审核目标

请判断学生版 v2 是否已经达到“类似必修四哲学宝典的含金量”，重点看：

- 是否是真正学生可学、可背、可迁移的宝典，而不是教师追溯稿。
- 是否还残留评分、评标、细则、来源、模型过程、审计、补丁、后台制作语言。
- 是否仍存在把两道题合并成一个案例的问题。
- 351 个题例是否被作为独立案例保留。
- 经济全球化是否避免把不能互相替代表述的术语塞进同一类。
- 政治多极化、中国外交、联合国、经济全球化、理论桶之间边界是否清楚。
- “合作共赢的新型国际关系”是否主要放在政治多极化/国际秩序链条，而不是理论桶。
- “独立自主和平外交与和平共处五项原则”是否主要放在中国外交链条，而不是理论桶。
- 与必修四哲学宝典相比，材料触发、为什么能想到、卷面句、易错边界的教学转化是否同等有用。

## 输出格式

请只输出中文审核报告：

1. 最终结论：PASS / FAIL / CONDITIONAL_PASS 三选一。
2. 是否可认定为与必修四哲学宝典同等含金量：是/否/接近但未到。
3. P0 必修清单：若有，逐条写明具体问题、位置、修改建议。
4. P1 优化清单：不阻断交付但建议改的地方。
5. 对 GPT Pro 一审 P0 的关闭判断：逐条说明已关闭/未关闭。
6. 最终交付建议：是否建议进入 GPT Pro 复审和网页 Claude Opus 复审。

不要改文件。不要泛泛而谈，必须引用学生版 v2 中的具体栏目或具体问题类型。

