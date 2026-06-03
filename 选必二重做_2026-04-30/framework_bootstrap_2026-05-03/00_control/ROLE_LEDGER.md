# 角色账本

## 四类 AI 资源

| 资源 | 本轮定位 | 权限边界 | 输出位置 |
|---|---|---|---|
| Codex | 本地总控、证据裁决、生产线 A、最终融合 | 可以读写本运行目录和新线预处理成果；不得继承旧选必二结论 | `00_control/`、`01_evidence_cards/`、`02_framework_candidates/`、`06_fusion/` |
| ClaudeCode | 独立生产线 B，复跑题源、查漏、挑战 Codex 归位 | 只能从新线小本本、原始题源和本轮控制文件出发；不得读旧选必二框架 | `05_advisor_reports/claudecode/`、后续 `claudecode_lane/` |
| GPT-5.5 Pro | 战略审框架、主干/全面双标准压力测试 | 只能基于脱敏摘要和框架候选给建议；不是证据权威 | 正式网页端：`05_advisor_reports/gpt55_web/`；CLI provisional：`05_advisor_reports/gpt55/` |
| Claude Opus 4.7 Adaptive | 框架表达、教学迁移、学生语言、反向可学性 | 只能基于证据锁定包与框架候选给建议；不是证据权威 | 正式网页/桌面端：`05_advisor_reports/claude_opus_web/`；CLI provisional：`05_advisor_reports/claude_opus/` |

## 真实调用硬规则

- GPT-5.5 Pro 必须真实调用 GPT-5.5 Pro；不能由 Codex 子智能体、Codex 本地模拟、普通 advisor 角色或“GPT 风格”文本替代。
- Claude Opus 4.7 Adaptive 必须真实调用 Claude Opus 4.7 Adaptive；不能由 ClaudeCode 默认模型、Codex 子智能体、Codex 本地模拟或“Claude 风格”文本替代。
- 若真实调用暂时不可用，本轮可以继续做本地证据和题目归位准备，但所有 GPT/Claude 相关 gate 记为 `real_call_pending`，不得 PASS。
- 真实调用输出必须保存原文，再由 Codex 写消化和本地证据裁决。
- 若 GPT-5.5 Pro、Claude Opus 4.7 Adaptive 或 ClaudeCode 正在跑其他项目，本轮必须新开独立对话/会话/工作目录；不得复用或打断其他项目线程。无法确认独立性时，记为 `advisor_session_isolation_uncertain` 并重开。
- 用户要求的正式 GPT/Claude gate 必须是用户可见的 `GPT-5.5 Pro` 与 `Claude Opus 4.7 Adaptive Thinking` 模式会话。CLI 非交互调用只算 `cli_provisional_advice`，除非用户明确豁免网页端/桌面端可见要求。
- Batch01 Trial3 已完成正式网页端/桌面端 gate：GPT-5.5 Pro 独立报告 + cross-critique、Claude Opus 4.7 Adaptive 独立报告 + cross-critique 均已归档；一次 Claude 空 prompt 失败和一次剪贴板误抓 prompt 已排除。

## 六类智能体/角色

| 角色 | 职责 | 当前实现 |
|---|---|---|
| 决策者 | 决定下一批题、下一处瓶颈、是否升级框架版本 | Codex 本地，必要时请 GPT-5.5 Pro 给 commander packet |
| 劳动者 | 题目案例卡、细则拆点、初步归位 | Codex A + ClaudeCode B |
| 补丁者 | 查漏、查硬塞、查同一材料多点、查框架重叠 | Codex 子智能体/本地 pass |
| 监管者/Governor | 否决弱证据、旧线污染、参考答案升级、假闭环 | Codex 本地，写入 `07_governor_confucius/` |
| 自动化检测者 | 检查矩阵、频次、缺口、输出是否一致 | Codex 脚本 + 本地 pass |
| 框架辩论/融合者 | 组织 GPT 和 Claude 的观点交叉审议，形成 Codex 裁决 | GPT-5.5 Pro + Claude Opus + Codex fusion |

## 运行规则

- 每个角色必须留下文件证据。
- GPT/Claude 的建议进入日志，不直接进入学生文档。
- ClaudeCode 和 Codex 都必须做生产，不互相复制。
- 若模型分歧，回到题面、细则、证据等级和用户要求裁决。
- Codex 子智能体不能替代 GPT-5.5 Pro 或 Claude Opus 4.7 Adaptive。

## Framework Council 角色分工

| Council 环节 | GPT-5.5 Pro | Claude Opus 4.7 Adaptive | Codex |
|---|---|---|---|
| Evidence Pack | 提出希望看到的证据字段 | 提出希望看到的学生迁移字段 | 生成脱敏证据包 |
| Independent Blueprint | 主干高频、全面覆盖、节点升降级 | 可学性、可背性、迁移语言、误用风险 | 不抢先定稿，只记录 |
| Cross-Critique | 质疑 Claude 是否弱化覆盖和证据边界 | 质疑 GPT 是否过抽象和不利学生使用 | 组织双向交叉审议 |
| Convergence | 给出最终高频/覆盖建议 | 给出最终教学/迁移建议 | 汇总一致与冲突 |
| Local Decision | 无裁决权 | 无裁决权 | 回本地题源和细则裁决 |
