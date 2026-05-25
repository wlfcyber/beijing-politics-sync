# Supervisor Patch: 2026 二模 B 线复跑

Status: `real_slice_rerun_captured_findings_open`

## Why This Patch Exists

Codex A 线已经在 `Q0113-Q0140` 中本地锁定 2026 二模八套卷的选必三相关题和边界。ClaudeCode B 线原始 thick mine 结束于更早阶段，`suite_reports/` 尚无 2026 二模套卷报告，因此双线闭合尚未成立。

## Execution Note

整套一次性复跑未产出必需文件，改为 suite-slice 真实复跑。最终 8 个套卷切片及顺义正文路径补充复核均返回 `0`，原始日志保存在 `03_claudecode_lane/logs/`。B 线证据已捕获，但发现项仍打开，不能据此宣布终稿、通过、发布或交付。

## Scope

只复跑本机可见 2026 二模八套：

- 2026丰台二模
- 2026东城二模
- 2026朝阳二模
- 2026海淀二模
- 2026房山二模
- 2026西城二模
- 2026石景山二模
- 2026顺义二模

重点核对 `Q0113-Q0140` 及相关边界题，不重跑 2024/2025 全量，不生成 final/Word/PDF，不宣布通过。

## Must Read

1. `00_飞哥选必三逻辑与思维硬性要求记事本.md`
2. `01_source_inventory/2026_ERMO_SUITE_CLOSURE_REPORT.md`
3. `01_source_inventory/QUESTION_COVERAGE_MATRIX.csv`
4. `02_codex_lane/GAP020_2026_FENGTAI_DONGCHENG_ERMO_Q8_Q9_Q21_Q12_Q18_SOURCE_LOCK.md`
5. `02_codex_lane/GAP021_2026_CHAOYANG_ERMO_Q5_Q6_Q7_Q19_1_SOURCE_LOCK.md`
6. `02_codex_lane/GAP022_2026_HAIDIAN_ERMO_Q3_Q4_Q5_Q6_Q7_Q18_1_Q20_1_SOURCE_LOCK.md`
7. `02_codex_lane/GAP023_2026_FANGSHAN_ERMO_Q18_2_SOURCE_LOCK.md`
8. `02_codex_lane/GAP024_2026_XICHENG_ERMO_Q5_Q6_Q18_4_SOURCE_LOCK.md`
9. `02_codex_lane/GAP025_2026_SHIJINGSHAN_ERMO_Q6_Q7_Q17_2_SOURCE_LOCK.md`
10. `02_codex_lane/GAP026_2026_SHUNYI_ERMO_Q5_Q6_Q7_Q18_1_Q21_SOURCE_LOCK.md`
11. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
12. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`

## Required Outputs

Write or update:

- `03_claudecode_lane/suite_reports/2026二模_B线复跑.md`
- `03_claudecode_lane/entries/2026_ermo_b_line_entries.jsonl`
- `03_claudecode_lane/2026_ERMO_B_LINE_RERUN_RESULT.md`
- `03_claudecode_lane/fusion_candidates_2026_ermo.csv`
- `03_claudecode_lane/blockers_2026_ermo.csv`
- `03_claudecode_lane/PROGRESS.md`
- `03_claudecode_lane/DECISION_LOG.md`

## Review Questions

For every `Q0113-Q0140`:

1. Does the A-line source-lock evidence actually support the row?
2. Is the evidence level correct: `A-formal`, `A-support`, or `B-choice-signal`?
3. Is the row in the correct book part: thinking, reasoning, or dual?
4. Does any source show a missing option, missing table, OCR/render issue, or wrong boundary?
5. Should this row enter the final framework body, remain only in same-type index, or remain blocked?

## Hard Holds

- Do not write `PASS`, `final`, `终稿`, `完成`, or `宝典成品`.
- Do not treat Q0140 as a pure elective-3 prompt; preserve the综合题 boundary.
- Do not promote Q0137/Q0138 beyond B-choice-signal unless source evidence clearly supports it.
- Do not demote A-formal rows merely because they also have boundary/comprehensive features; explain if a dual registration is needed.
