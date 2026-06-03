# Framework Synthesis Plan - v1

## Synthesis Decision

Use GPT's “设问功能分流” and Claude's “设问识别→码本路由→句式模板” as the shared trunk. The synthesized v1 has three layers:

1. **设问入口**：学生先看题目要求，不按教材目录启动。
2. **七个 codebook 节点**：只有 `CODE_COWORK_001` to `CODE_COWORK_007` can generate scoring claims.
3. **缺口隔离**：未被 codebook 直接支撑的题进入 pressure-test gap log, not new nodes.

## Evidence Boundary

- Directly supported questions: 16/65.
- Not directly supported: 49/65.
- Uncovered evidence levels: formal 45, reference_only 4.
- Current uncovered ask distribution:
- 综合: 13
- 论证: 10
- 说明: 9
- 意义: 6
- 原因: 5
- 评析: 3
- 建议: 2
- 开放: 1

## Node Policy

- Keep seven nodes in `framework_v1` because the codebook has seven rows and each row has its own evidence map.
- Treat `CODE_COWORK_004` and `CODE_COWORK_006` as sibling nodes under one four-step family, but do not merge their evidence in the CSV.
- Do not create independent IP/AI/ecology/family/minor/green-principle nodes from pending observations.
- Do not let `reference_only` rows support core nodes.

## Pressure-Test Categories

- `DIRECT_HIT`: question_id appears in the node's supporting_question_ids.
- `TRANSFER_TEST`: ask/material shape matches a node, but question_id is not direct codebook support; this can test transfer but cannot prove core support.
- `GAP_PENDING`: no node can generate a close answer without inventing an unsupported code.
- `REFERENCE_ONLY`: evidence_level is reference_only; use for illustration only.

## Next Artifacts

1. `framework_v1.md`
2. `framework_v1_evidence_map.csv`
3. `10_framework_validation/framework_v1_question_by_question_test.csv`
4. `framework_v1_failure_cases.md`
5. `framework_v1_patch_suggestions.md`
6. `framework_v1_pass_report.md`
