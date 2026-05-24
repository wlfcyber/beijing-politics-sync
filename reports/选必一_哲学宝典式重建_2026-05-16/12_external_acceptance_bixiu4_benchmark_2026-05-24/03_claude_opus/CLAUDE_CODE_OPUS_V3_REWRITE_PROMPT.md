# Claude Code Opus v3 Rewrite Prompt

你是 ClaudeCode Opus 生产线，不是审稿人。请直接基于学生版 v2 生成学生版 v3，并写出修订报告。

## 必须读取

1. 学生版 v2：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\选必一_当代国际政治与经济_主观题术语宝典_学生精简版_GPT一审后_v2.md`

2. Claude Opus fallback 审稿报告：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\03_claude_opus\CLAUDE_CODE_OPUS_FALLBACK_REVIEW_CAPTURE_20260524.md`

3. GPT Pro 一审原始反馈：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\02_gptpro_web\GPTPRO_REVIEW_CAPTURE_20260524.md`

4. 必修四哲学宝典样本：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\01_review_materials\02_bixiu4_philosophy_benchmark_student.md`

## 输出文件

请创建：

1. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\选必一_当代国际政治与经济_主观题术语宝典_学生精简版_ClaudeCode重写_v3.md`

2. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\CLAUDECODE_V3_REWRITE_REPORT.md`

## 硬规则

- 保留 351 个独立 `###` 题例，不得把两道不同题合并。
- 同一来源题有多个答题点时，不能删掉任何一个答题点；可以新增“同题组索引/同题组提示”，帮助学生知道这是同一道题的不同答题点。
- v3 学生正文不要出现教师/后台/追溯口吻：`细则`、`评标`、`参考答案`、`来源等级`、`教师`、`追溯`、`评分`、`阅卷`、`讲评`、`source_path`、`审计`、`补丁`、`题目要求`、`本题`、`采分`、`给分`、`计分`、`得分`、`答案提示`、`答案术语`、`答题层`、`本节点`。
- 删除或吸收正文里的二代后台字段：`【表述积累】`、`【题例数量】`、`【小类】`、`【核心表述】`。可把有用信息并入 `【什么时候写】` 或 `【易错提醒】`。
- 正文标题去掉“（出现N次）”。频次可以放入报告，不放学生正文。
- `【使用提醒】` 只保留真正学生易错边界；凡是解释“等”的元注释删除。
- `为什么能想到` 必须改成学生审题语言，不能保留机械模板：
  - 禁止：`看到材料里出现...且题目追问...就把材料事实接到...`
  - 禁止：`这道题设问与材料共同指向...材料关系正对应...`
  - 推荐：`这道题不是只问某个事实，而是在问某类关系/原因/意义；材料中的具体信号说明需要从某知识链切入，所以卷面先写某术语，再接材料事实。`
- “合作共赢的新型国际关系”主归政治多极化/国际秩序，不放理论桶。
- “独立自主和平外交、和平共处五项原则”主归中国外交链，不放理论桶。
- 经济全球化不要把不能互相替代的术语合并为一类。

## 重写策略

1. 保持六大桶顺序。
2. 每个核心点只保留学生需要的结构：
   - `## 核心答题点：...`
   - 必要时：`【怎么认】...`
   - `### n. 来源题目`
   - `【什么时候写】...`
   - `【设问】...`
   - `【为什么能想到】...`
   - `【卷面句】...`
   - 必要时：`【易错提醒】...`
   - 必要时：`【同题组】同一来源题还对应...，本条只学...`
3. 所有同题组提示必须只用于同一来源题的多个答题点，不能合并不同题。
4. 输出报告中说明：
   - 351 题例是否保留。
   - 删除了哪些二代后台字段。
   - 改写了多少条机械模板。
   - 建立了多少条同题组提示。
   - 哪些 GPT/Claude P0 已关闭，哪些仍需人工复核。

请直接写文件，不要只输出建议。

