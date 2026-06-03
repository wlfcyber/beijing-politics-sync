# Framework v1 Patch Suggestions

## Summary
- PASS direct hits: 16
- PARTIAL transfer/reference rows: 49
- FAIL gap rows: 0

## Method Note
Pressure-test entry matching used only question text, ask atoms, material text, and material atoms. Rubric/answer text was not used to choose a framework node.

## Required Patch Logic

1. Do not upgrade PARTIAL rows to PASS without new dual-model source-checked observations.
2. Keep reference_only rows outside core even if templates seem usable.
3. For transfer rows, inspect actual rubric atoms and decide whether they support a new codebook observation.
4. For FAIL rows, run source-level open observation; do not invent IP/AI/ecology/family/minor nodes from current pending observations.

## Patch Type Counts
- 材料触发不清: 45
- 证据不足: 4

## Candidate Expansion Clusters To Source-Check
- 制度作用、基本原则、公共利益、生态/绿色原则类。
- 知识产权、创新保护、不正当竞争、AI 数字治理类。
- 家庭、赡养、继承、未成年人保护类。
- 原因/说明类：当前 7 节点没有独立奖励机制。
- 维权/起诉状/措施类：只有 CODE_COWORK_007 一道 direct 支撑，不能过扩。
