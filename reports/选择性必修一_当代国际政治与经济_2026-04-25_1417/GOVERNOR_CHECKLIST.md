# Governor Checklist

## Evidence Gate

- PASS: 当前主观题证据口径已收紧为纯细则：只承认 `source_type=rubric`。
- PASS: `marking-report`、`lecture-scoring`、普通 `reference-answer` 均不进入纯细则版。
- PASS: 44 条主观题覆盖保留为 `included`。
- PASS: 2 条非纯细则来源已标为 `blocked`，且从纯细则版主框架删除。

## Blocked Items

| 套卷 | 题号 | 原来源类型 | 处理 |
|---|---|---|---|
| 2024朝阳期中 | 20(3) | marking-report | blocked，需找到同题 rubric 细则才能恢复 |
| 2025东城期末 | 20 | lecture-scoring | blocked，需找到同题 rubric 细则才能恢复 |

## Coverage Gate

- PASS: `COVERAGE_MATRIX.csv` 已按纯细则口径更新：main/lecture-scoring 中 44 `included`，2 `blocked`。
- PASS: `MAIN_EVIDENCE_PURE_RUBRIC_AUDIT.csv` 与 `MAIN_EVIDENCE_PURE_RUBRIC_AUDIT.md` 已生成。
- PASS: 选择题错肢库不属于主观题纯细则筛查对象，保持原覆盖。

## Current Decision

READY_PURE_RUBRIC_ONLY