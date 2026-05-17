# ClaudeCode Batch 007 Production Prompt

你是飞哥政治庄园选必一生产线的 ClaudeCode 生产稿 B 线，不是评论员。请直接基于下面三个文件产出一份独立初稿，保存为 Markdown 正文格式输出到 stdout：

1. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\01_source_packets\BATCH_007_SOURCE_PACKET.md`
2. `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
3. `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

可参考但不得照抄 Codex A 线初稿：

4. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\02_codex_batches\BATCH_007_CODEX_DRAFT.md`

## 硬性要求

- 只处理 Batch 007 的五题：
  1. 2024海淀期中Q21(2)
  2. 2024丰台一模Q20
  3. 2024丰台二模Q19
  4. 2024石景山一模Q19(2)
  5. 2024西城二模Q19
- 每个条目必须严格包含六项：
  - `术语`
  - `完整设问`
  - `细则位置`
  - `来源`
  - `材料触发`
  - `答案句`
- `术语` 必须来自评分细则、评标、阅卷提示或正式参考答案链条，不得自造概括。
- `答案句` 必须是考生可直接写在卷面上的句子：术语 + 本题材料事实 + 因果/作用/结果。
- 2024丰台一模Q20 是等级化细则：答案提示四个方面任选其三为6-7分，不得伪造成每点固定2分。
- 2024丰台二模Q19 暂未定位到完整独立题面；只使用细则明示的应对气候变化、南南合作、区域合作三层，不外推项目事实；不得泛写经济全球化、国际关系民主化。
- 2024石景山一模Q19(2) 只有教师版参考答案，证据层级低于正式细则；不得称为正式评分细则。
- 2024西城二模Q19 要写处理国际关系的新思路：既要批判集团政治、实力至上等旧逻辑，也要写人类命运共同体、全球协作、国际秩序公正合理。
- 2024海淀期中Q21(2) 必须分清“变”与“不变”：多极化、全球化、和平与发展、人类命运共同体放在“变”；独立自主、宗旨、基本目标、和平共处五项原则放在“不变”。
- 同一核心采分功能应先合并再表述积累，不要把“时代主题”“和平与发展”“顺应和平与发展时代主题”拆成多个重复条。
- 最终正文不得出现工作流、模型、审核、prompt、文件路径等后台语言。

## 输出格式

只输出 Markdown 正文，不要解释你如何工作。按六大桶组织：

1. 时代背景
2. 理论
3. 经济全球化
4. 政治多极化
5. 中国
6. 联合国

每个条目用：

```markdown
**术语：……**

- 完整设问：……
- 细则位置：……
- 来源：……
- 材料触发：……
- 答案句：……
```

如果你认为 Codex A 线遗漏或错分，请在你的正文中直接给出更好的条目，不要写“我认为”“建议”“问题”等评论语。
