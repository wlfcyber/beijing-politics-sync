# ClaudeCode Batch 006 Production Prompt

你是飞哥政治庄园选必一生产线的 ClaudeCode 生产稿 B 线，不是评论员。请直接基于下面三个文件产出一份独立初稿，保存为 Markdown 正文格式输出到 stdout：

1. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\01_source_packets\BATCH_006_SOURCE_PACKET.md`
2. `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
3. `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

可参考但不得照抄 Codex A 线初稿：

4. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\02_codex_batches\BATCH_006_CODEX_DRAFT.md`

## 硬性要求

- 只处理 Batch 006 的五题：
  1. 2024海淀一模Q18(1)
  2. 2024海淀二模Q18(1)
  3. 2024朝阳一模Q21
  4. 2025延庆一模Q20(2)
  5. 2025房山一模Q18(2) / 母表旧号Q20(2)
- 每个条目必须严格包含六项：
  - `术语`
  - `完整设问`
  - `细则位置`
  - `来源`
  - `材料触发`
  - `答案句`
- `术语` 必须来自评分细则、评标、阅卷提示或正式参考答案链条，不得自造概括。
- `答案句` 必须是考生可直接写在卷面上的句子：术语 + 本题材料事实 + 因果/作用/结果。
- 不能把普通教师版参考答案提升为细则术语。2025房山题以正式细则两条链为准，教师版答案只作支持。
- 2024海淀二模只有“可从时代主题、世界多极化、人类命运共同体、国际组织等角度作答”的宽泛正式角度；不得伪造成每点固定分值。
- 2024朝阳一模中经济增速稳健、高质量发展阶段偏必修二经济分析，不进入选必一主链；措施部分必须覆盖政治多极化和经济全球化两个维度。
- 2024海淀一模中“推进高水平对外开放/发展更高水平开放型经济”单独看偏必修二边界项，不作为独立选必一术语；可依附于贸易投资便利化、全球资源要素流动、两个市场两种资源。
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
