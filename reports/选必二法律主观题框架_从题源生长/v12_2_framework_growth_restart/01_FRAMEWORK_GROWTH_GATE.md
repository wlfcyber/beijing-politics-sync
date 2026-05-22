# Framework growth gate

## Hard reset

本阶段不沿用 v10 的 `EXHAUSTIVE_FRAMEWORK_PASS`，不沿用 v11/v12/v12.1 的阶段性清洗结论作为最终框架证明。v12.1 只提供题源底座，不提供最终框架合法性。

## Batch rule

### Batch 01

优先城区正文题链：海淀、西城、东城、朝阳，共 25 道。用途是让双模型先从北京高权重区的真实题源中抽出主干入口、材料触发和得分动作。

### Batch 02

其余正文题链，共 17 道。用途是检验 Batch 01 生成的主干是否能覆盖普通区县、低频题型和非典型材料。

### Batch 03

5 道 `OPEN_OR_REFERENCE` 和 6 道下一版回填候选。用途是暴露开放容器、边界风险和框架缺口；不得直接把这些题硬塞进核心。

## Model rule

- Round 01: GPT 和 Claude 独立读同一批题源包，分别产出框架生长建议。
- Round 02: GPT 必须批判 Claude 的原文输出；Claude 必须批判 GPT 的原文输出。
- Codex adjudication: 只接受同时满足“题源证据支持 + 改善高频主干/覆盖/迁移/风险控制之一”的框架变化。

## Promotion rule

任何新框架版本要晋级，必须同时具备：

- Batch evidence pack
- GPT Round 01 原始输出
- Claude Round 01 原始输出
- GPT 对 Claude 的交叉批判
- Claude 对 GPT 的交叉批判
- Codex evidence adjudication
- 覆盖矩阵 delta

否则只能写 `candidate_pending_real_call` 或 `blocked_advisor`。

