# v13.11 logic-first framework rebuild

Status: `candidate_pending_real_gpt_claude_review`

本目录回应用户对 v13.10 的核心批评：框架逻辑不清，学生无法习得。

v13.11 不覆盖 v13.10。它先把学生前台改成一条能学会的推理链：

`生活冲突 -> 争点 -> 法律翻译 -> 法律结果 -> 价值收束`

旧 A/B 双轴保留，但降级：

- A 轴只作为法律关系工具箱。
- B 轴只作为答案形状工具箱。
- 学生第一入口不再是 A1-A10 或 B1-B7，而是“这题争什么”。

边界：

- 本轮是 Codex 本地逻辑重构和题卡重排。
- 还没有新的真实 GPT/Claude advisor gate。
- 因此本目录不能替代 v13.10 终版交付，只能作为 v13.11 候选，等待真实 GPT/Claude 和零基础学生试读复核。
