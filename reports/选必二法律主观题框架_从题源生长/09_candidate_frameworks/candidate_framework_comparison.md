# Candidate Framework Comparison - Cowork Refined 20260519

## Input Gate

- Input packet: `candidate_framework_input_cowork_refined_20260519.zip`
- Current corpus: 65 core subjective law questions, formal 61, reference_only 4, missing 0.
- Codebook: 7 rows, all formal-supported.
- Direct codebook support: 16/65 questions.
- Uncovered by direct codebook support: 49/65 questions, including formal 45 and reference_only 4.

## Model Proposals

| Source | Proposed Shapes | Recommendation | Key Warning |
| --- | --- | --- | --- |
| GPT-5.5 Pro | 设问功能分流；材料信号驱动；评分采点矩阵 | 候选框架一：设问功能分流框架 | 7 条 codebook 直接支持 16/65；其余 49 题不能宣称满分闭环。 |
| Claude Opus 4.7 Adaptive | 七锚直码型；设问识别→码本路由→句式模板；码-题-证据诊断型 | 框架 B：设问识别→码本路由→句式模板 | Layer 1 只能识别，不发分；分数判断必须来自 codebook。 |

## Shared Agreements

1. 两个模型都确认当前证据不能直接推出 65 题满分闭环；7 条 codebook 只能直接支撑 16 题。
2. 两个模型都把候选框架入口放在“设问/任务形态”而不是教材目录或法学理论。
3. 两个模型都要求 pending/source-check 观察只能做开放容器或风险提醒，不能升级为核心节点。
4. 两个模型都认为 `CODE_COWORK_004` 与 `CODE_COWORK_006` 是同一四步机制在侵权/行为与合同/责任场景中的两个支路。
5. 两个模型都把 4 道 reference_only 题放在非核心位置：只能参考，不能支撑核心节点。

## Differences And Codex Adjudication

| Issue | GPT Position | Claude Position | Codex Decision |
| --- | --- | --- | --- |
| 入口形态 | 设问功能分流最适合考场启动 | 设问识别层最适合全题压测 | 采用“设问入口 + codebook 节点 + 缺口隔离”的 v1。 |
| `CODE_004` 与 `CODE_006` | 分成侵权/行为四步和合同/责任四步 | 建议承认同源，可合并为四步定性法 | 保留两个 sibling 节点，避免合同/侵权证据混写；在说明中标注同源。 |
| 未覆盖 49 题 | 标记为可迁移待验证或 pending | 用识别层送入压测，记录“入口命中但码本失效” | 压测时设 `DIRECT_HIT / TRANSFER_TEST / GAP_PENDING / REFERENCE_ONLY` 四类。 |
| 候选三/诊断图 | 作为评分反推工具 | 作为后续扩 codebook 的诊断地图 | 不进入学生主框架，但用于 `framework_v1_failure_cases.md` 和 patch suggestions。 |

## Decision

Promote a conservative `framework_v1`: **设问入口分流 + 七个 codebook 节点 + 缺口隔离记录**.

This is not a final framework. It is the smallest framework that both real model proposals support without inventing unsupported nodes. The next required gate is all-65-question pressure testing.
