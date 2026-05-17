# ClaudeCode 全量重跑任务：选必一主观题术语宝典

你现在在一个 Windows 本地仓库中工作。请只写入：

`reports/选必一_哲学宝典式重建_2026-05-16/07_claudecode_full_rerun/`

不要修改现有终稿、脚本、规则文件或批次源文件。

## 任务目标

为选择性必修一《当代国际政治与经济》主观题术语宝典做一次 ClaudeCode 独立全量重跑，然后与当前 Codex 版进行对照，给出融合建议。你的输出不是简单评论，而是可供后续融合的厚稿和差异表。

## 必读文件

先读以下规则：

1. `skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
2. `skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

再读全部批次源稿：

`reports/选必一_哲学宝典式重建_2026-05-16/03_fusion/BATCH_*_FINAL_AFTER_GPT_AND_CLAUDE.md`

最后再读当前 Codex 版用于对照：

1. `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_学生版.md`
2. `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md`
3. `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_宝典终稿_GOVERNOR_FINAL_AUDIT.md`

## 独立性要求

第一阶段必须从 13 个批次源稿独立建立六桶体系，不要先照抄当前 Codex 版。当前 Codex 版只能在你完成独立判断之后，用于对照、查漏和融合建议。

## 用户最新纠偏必须钉死

1. `合作共赢的新型国际关系 / 相互尊重、公平正义、合作共赢的新型国际关系` 必须归入 `政治多极化`，不能放入 `理论`。
2. 经济全球化桶的同类项合并必须看细则表述是否接近、学生卷面是否可替代、细则是否明示为同一点可选表述，不能只看抽象本质是否相同。
3. 不能把 `开放型世界经济`、`开放型经济`、`创新型、开放型世界经济`、`全球经济治理和规则制定`、`多边贸易体系`、`普惠包容的经济全球化`、`贸易自由化` 只因都属于开放合作就塞进一个节点。
4. 术语必须来自评分细则、评标、阅卷总结或用户确认材料。普通参考答案不能冒充评分细则。
5. 2026 石景山期末全模块排除，除非用户另给新细则。

## 输出文件

请生成以下文件：

1. `CLAUDECODE_FULL_RERUN.md`
   - 按六桶组织：时代背景、理论、经济全球化、政治多极化、中国、联合国，必要时附兜底句。
   - 每个核心节点写 `## 核心答题点：...（出现N次）`。
   - 每个节点必须有 `表述积累`、`本节点真题`。
   - 每条题例必须包含：`细则术语`、`材料触发点`、`设问`、`为什么能想到`、`答案落点`、`细则位置`、`来源`。
   - 不要写后台制作话，如 Codex、GPT、Claude、prompt、审核、文件路径、采分点、要落到、v7、证据层级等。

2. `CLAUDECODE_CORE_INDEX.csv`
   - 列：bucket, core_point, count, representative_variants, source_questions, merge_reason, risk_note。

3. `CLAUDECODE_DIFF_TO_CURRENT.md`
   - 与当前 Codex 版比较，列出：
     - ClaudeCode 新增或拆出的核心点。
     - ClaudeCode 认为 Codex 版应合并的核心点。
     - ClaudeCode 认为 Codex 版归桶错误或边界可疑的核心点。
     - 经济全球化桶内所有开放、贸易、治理、产业链节点的可替代表述复查。
     - `新型国际关系` 与 `合作共赢` 相关节点的归桶复查。

4. `CLAUDECODE_FUSION_RECOMMENDATIONS.md`
   - 给后续 GPT Pro 主融合使用。
   - 对每个有分歧的核心点给出建议：保留 Codex、采用 ClaudeCode、合并、拆分、证据不足暂不入表。
   - 每条建议必须说明依据：细则表述、材料触发、学生卷面可替代性。

5. `CLAUDECODE_RUN_AUDIT.md`
   - 写清读取了哪些源文件、输出题例总数、核心节点总数、六桶分布、未处理或证据不足项、是否发现后台词污染。

## 输出质量

这次不是写“建议报告”就结束。请尽量生成可融合进学生宝典的完整厚稿。宁可核心节点更多，也不要把不可替代的细则术语压扁。合并必须谨慎，拆分要有理由。
