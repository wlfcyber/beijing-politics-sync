# 进度记录

## 2026-05-03

- 已确认本轮不继承旧选必二结论。
- 已把用户新要求写入小本本：框架必须同时满足“主干高频”和“全面可归位”。
- 已创建框架运行目录：`framework_bootstrap_2026-05-03`。
- 正在建立批次协议、模型提示词和当前预处理快照分析。
- 用户纠正：GPT-5.5 Pro 和 Claude Opus 4.7 Adaptive 必须真实调用，不能用 Codex 子智能体替代。已暂停任何子智能体替代方案，转为修订 skill 与本运行目录控制规则。
- 用户进一步要求：框架自我进化流程不能只是后置审稿，应让 GPT-5.5 Pro 和 Claude Opus 4.7 Adaptive 一起研究框架制定和更新。已新增 `SELF_EVOLUTION_PROTOCOL.md`，并把流程改为 Evidence Pack -> GPT 独立方案 -> Claude 独立方案 -> 双向交叉质询 -> Codex 本地证据裁决 -> 版本升级。
- 用户提供法律命题人权威图片，要求学习和参考；并新增框架升级点：揣摩题目的命题路径，根据命制逻辑从前到后或从总到分反推框架。已保存图片、提炼命题参考，并把 `proposition_path` 写入小本本、skill、MASTER、SELF_EVOLUTION、BATCH_PROTOCOL 和 GPT/Claude Council prompts。
- 用户提醒 GPT、Claude 和 ClaudeCode 正在跑另一个项目，本轮必须新开独立对话，不能影响其他项目。已写入小本本、MASTER_REQUIREMENTS、ROLE_LEDGER；后续真实调用均加“禁止继承其他项目上下文”提示。
- Batch01 前三道主观题试验已完成案例卡、归位矩阵、framework delta 和 gap list。三题中 B01-Q1、B01-Q3 为 formal_or_scoring_source，B01-Q2 为 reference_answer，只能入开放观察容器。
- GPT-5.5 通过 `codex exec -m gpt-5.5` 的 OpenAI CLI 非交互会话完成独立方案和 cross-critique；该调用不会出现在 ChatGPT 网页版历史。Claude Opus 通过 `claude -p --model opus` CLI 非交互会话完成；该调用不会出现在 Claude 网页版 Adaptive Thinking 对话历史。用户明确要求 `GPT-5.5 Pro` 和 `Claude Opus 4.7 Adaptive Thinking` 模式后，本批二者均降级为 `cli_provisional_advice`，正式 gate 状态为 `web_visible_pro_adaptive_call_pending`。
- 已生成网页端正式 gate prompts：`04_advisor_prompts/WEB_GPT55_PRO_BATCH01_PROMPT.md` 和 `04_advisor_prompts/WEB_CLAUDE_OPUS47_ADAPTIVE_BATCH01_PROMPT.md`。后续需用用户可见的新对话分别跑 GPT-5.5 Pro 与 Claude Opus 4.7 Adaptive Thinking，再归档原文输出。
- Codex 已完成本地融合裁决，生成 `06_fusion/batch01_trial3_convergence_and_local_decision.md` 与 `02_framework_candidates/FRAMEWORK_V1_CANDIDATE_TRIAL3.md`。状态为候选试运行，不能定稿。
- 已完成用户可见网页端/桌面端正式 gate：GPT-5.5 Pro 独立报告、Claude Opus 4.7 Adaptive 独立报告、GPT 对 Claude 交叉批判、Claude 对 GPT 交叉批判均已归档到 `05_advisor_reports/*_web/`。
- 已纠正并记录一次剪贴板/复制目标错误：`Web Claude Cross-Critique Prompt` 是应发送给 Claude 的 prompt，不能作为 Codex 输出或模型报告；正式归档文件头已复核无误。
- 已生成正式审阅融合稿：`06_fusion/batch01_trial3_web_official_convergence_for_review.md`。融合结论为 `V0.1 证据分层候选版`，不是 V1 定稿；学生端暂定为 `零步看问法 + 四步答题 + 价值一规 + 五域索引`。
- 用户指出三题展示和框架层级问题后，已复核并纠正：B01-Q2 `2024海淀一模第19题` 本地有正式细则层次表，不能继续按 reference-only 处理；三题均为 formal/scoring 支撑，但仍只是 Trial3，不定 V1。
- 已在候选框架中补明：一核二线三问没有删除，而是分层；五域只是临时覆盖索引，依据和重划风险必须显性标注。
