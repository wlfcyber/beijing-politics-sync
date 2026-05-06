# GPT Phase Gate Review 2026-05-02

## Sent Phase Package

Codex sent a sanitized phase package to GPT-5.5 Pro through the ChatGPT web Pro route after updating the whole-book orchestrator skill with a phase-boundary GPT commander gate.

## Raw GPT Commander Advice

### 1. stop/go 判断

**GO，条件通过。**

这套机制可以进入实战，但必须补上“阶段闸门”和“建议失效规则”。GPT 阶段指挥包只能推动下一阶段任务设计，不能替代 Governor 验收，不能替代本地证据复核，也不能成为项目停摆点。

### 2. 最大风险

最大风险是形成新的“GPT 假闭环”：Codex 写了阶段报告，GPT 给了看似完整的下一阶段建议，Codex 保存了建议日志，于是团队误以为该阶段已经被高质量审过。

真正危险点有三个：

1. **脱敏阶段报告过粗**，GPT 看不到覆盖缺口、证据等级混淆、非文本材料遗漏。
2. **Codex 消化建议流于形式**，只写“已采纳”，没有转成本地任务、证据复核、返修结果。
3. **GPT fallback 被滥用**，网页端卡住后 Codex 继续跑是对的，但不能借 fallback 跳过阶段质询和自检。

### 3. 还应该补的硬规则

阶段报告必须有最低字段：

```text
阶段名
本阶段目标
已完成动作
未完成动作
源材料覆盖摘要
非文本材料处理摘要
P0/P1/P2/P3 证据等级统计
遗漏题/遗漏套卷/遗漏文件类型
双线差异
冲突清单摘要
blocker
本阶段 Governor 闸门状态
请求 GPT 判断的问题
下一阶段候选任务
```

GPT 建议不能直接进入任务队列；每条建议都要标采纳、部分采纳、拒绝或延后，并写理由、对应本地任务、需要复核的本地证据、执行状态、是否影响学生文档。

阶段推进权归 Governor。GPT 可以建议进入下一阶段，但真正放行必须看 Governor。

GPT fallback 后必须补一次迟到审查。GPT 恢复后，必须对 fallback 阶段做迟到审查；迟到审查发现重大漏洞时，要触发返工。

阶段报告不能只报好消息；必须写本阶段最不确定的三件事、最可能遗漏的材料类型、最可能误判的证据等级、最可能误导学生的表达。

脱敏不能牺牲可审查性；不能发路径、文件名、试题原文、评分细则原文，但必须保留 source_id、年份、区级/考试类型、文件类型、题型、证据等级、处理状态、是否含图片/漫画/表格、是否有 blocker。

每阶段必须有“禁止进入学生版”清单，隔离未裁决冲突、仅由 P1 支撑却被写成评分规则的内容、OCR 低可信内容、图片/漫画未复核内容、GPT/Claude 未经本地证据确认的建议、旧线结论。

GPT 指挥包要有失效条件：本地证据范围变化、用户框架变化、发现 P0/P1 证据等级误标、发现大规模遗漏题、发现非文本材料未处理、从续跑改为从0开始、ClaudeCode 独立线结论大面积冲突。

### 4. Codex 下一步应该做什么

```text
1. 把 phase report 模板升级为强制字段版。
2. 把 gpt_phase_advice、MODEL_ADVICE_LOG、codex_response_to_advice 三者建立一一对应关系。
3. 在 Governor 里新增“GPT 阶段机制闸门”：
   a. phase report 是否完整
   b. GPT 原始建议是否保存
   c. Codex 是否逐条消化
   d. fallback 是否记录
   e. 迟到审查是否安排
4. 做一次 30 分钟小范围演练：
   选一个小模块，跑完整的“阶段报告 -> GPT 建议 -> Codex 消化 -> 本地任务 -> fallback 模拟 -> 验收”链条。
5. 检查演练是否出现：
   a. 报告太空
   b. GPT 建议无法落地
   c. Codex 只写采纳但没执行
   d. fallback 后无人复审
   e. 学生版混入审计话术
6. 演练通过后，再把这套机制固化进“整本书三线总控”的默认启动流程。
```

最终判断：**可以开跑，但先补阶段闸门、建议消化格式、fallback 迟到审查三项硬规则。**

## Codex Digestion

- Accepted: required phase report fields, including negative-risk fields.
- Accepted: one-to-one chain among phase report, raw GPT advice, Codex digestion, and local tasks.
- Accepted: Governor G10 GPT phase mechanism gate.
- Accepted: fallback late review before final promotion.
- Accepted: GPT advice expiration conditions.
- Deferred: 30-minute drill will be run when the next concrete book/module task starts or when the user explicitly asks for a drill.
