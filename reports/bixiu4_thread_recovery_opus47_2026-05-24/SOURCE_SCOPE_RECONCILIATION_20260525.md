# Source Scope Reconciliation 2026-05-25

status: `SOURCE_SCOPE_RECONCILED_NO_UNAUDITED_EXAM_SUITE_FOUND`

## Purpose

This file checks whether the recovery audit's `64` raw-suite count is a real source-scope count or an accidental undercount against the user's `2024-2026` district-paper objective.

## Result

- raw exam-suite directories under `2024/2025/2026各区模拟题`: `64`.
- other non-suite material directories found under those roots: `1`.
- global audit rows in `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`: `64`.
- GPT suite bundles currently present in the reusable cache: `56`.

The current desktop source tree does not contain seventy-plus independent exam-suite directories. It contains `64` exam suites plus `1` other-material folder. The user's earlier `七十多套` expectation is therefore not proven by the current local filesystem snapshot.

## Exam Suite Counts By Stage

- `first_mock`: `27`
- `second_mock`: `20`
- `midterm_or_final`: `17`

## Reconciliation Status Counts

- `present_in_global_audit`: `64`

## Name Normalization

- `2024顺义思政二模` is normalized as `2024顺义二模`; this explains the raw/global name difference.

## Missing Exam Suites

| raw suite | normalized suite | stage | status | note |
|---|---|---|---|---|
| none | none | none | none | all exam-suite directories reconcile to the global audit |

## Other Materials Not Counted As Suites

| folder | stage | source files | note |
|---|---|---:|---|
| 202404各区一模试题分类（按模块） | 其他材料 | 7 | module-classification material, not an independent district paper suite |

## Boundary

- This reconciles the filesystem source scope only; it does not prove row-level correctness, content thickness, or final external acceptance.
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv` remains the suite-level coverage ledger.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` remains the question/placement ledger.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
