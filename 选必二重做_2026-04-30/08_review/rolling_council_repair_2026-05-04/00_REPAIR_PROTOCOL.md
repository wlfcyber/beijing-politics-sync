# 选必二四线闭合补跑协议

时间：2026-05-04

## 结论先写清

昨晚内容产物已完成，但四线流程未闭合。原因不是题库没有做完，而是外部模型审议没有按小本本要求形成“边跑试卷、边更新框架”的滚动闭环。

本补跑只做流程闭合修复，不把未完成的外部 gate 写成 PASS。

## 硬门槛

1. 真实 GPT-5.5 Pro：必须在用户可见 ChatGPT 网页/桌面端新对话中执行。若界面不能逐字确认 GPT-5.5 Pro，只能记为 `gpt55_exact_mode_confirm_pending`。
2. 真实 Claude Opus 4.7 Adaptive Thinking：必须在用户可见 Claude 网页/桌面端新对话中执行。
3. 每个批次都必须有：GPT 独立框架意见、Claude 独立框架意见、GPT 对 Claude 的交叉批判、Claude 对 GPT 的交叉批判、Codex 本地证据裁决、coverage/gap delta。
4. reference answer 不推动主干；所有模型建议必须回到本地题面与细则/讲评/评卷口径核验。
5. 最终 Governor 与 Confucius 必须重跑；未完成 exact GPT gate 时不得 PASS。

## 批次

本轮基于当前 112 道入框法律题，按五域拆成 5 个滚动审议批次：

1. 合同消费者劳动：38 道，主观 14，选择 24。
2. 物权相邻继承家庭：20 道，主观 4，选择 16。
3. 人格权侵权：17 道，主观 7，选择 10。
4. 知识产权不正当竞争：15 道，主观 6，选择 9。
5. 纠纷解决生态公益与新业态：22 道，主观 12，选择 10。

## 闭合状态记录

- batch_status：pending
- gpt55_exact_mode：pending
- claude_opus47_adaptive：pending
- final_governor_refresh：pending
- final_confucius_refresh：pending
