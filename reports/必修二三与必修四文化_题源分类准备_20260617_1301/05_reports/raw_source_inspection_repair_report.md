# Raw Source Inspection Repair Report

Generated from `twenty_question_structure_accepted_classification_matrix.csv`.

## Scope

- Reviewed remaining missing-question entries: 22
- Added matrix rows: 16
- Accepted absent-structure gap entries: 6
- Remaining missing-question entries: 0

## Matrix Counts

- Rows: 1265
- Status counts: {'reference-only': 6, 'included': 464, 'module-boundary-excluded': 674, 'blocked': 121}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 159, 'B2_ECONOMICS': 195, 'B4_CULTURE': 110}
- Included rows: 464
- Module-boundary-excluded rows: 674
- Blocked rows: 121
- Reference-only rows: 6
- Duplicate `(suite_id, question)` keys: 0

## Decisions

- `2024_西城_一模`: Q5 added as `B3_POLITICS_RULE_OF_LAW`; Q20/Q21 accepted absent because the paper ends at Q19.
- `2024_西城_二模`: Q15 added as `XB3_EXCLUDED`; Q20/Q21 accepted absent because the paper ends at Q19.
- `2024_顺义_二模`: Q9 added as `B3_POLITICS_RULE_OF_LAW`; Q14 added as `XB1_EXCLUDED`; Q21 accepted absent after the already accepted Q20 span.
- `2026_丰台_一模`: Q5 added as `B4_PHILOSOPHY_EXCLUDED`; Q9 added as `XB3_EXCLUDED`.
- `2026_丰台_二模`: Q15 added as `XB1_EXCLUDED`.
- `2026_丰台_期末`: Q2 and Q6 added as `UNKNOWN_OR_MIXED` blocked rows; Q7 added as `B3_POLITICS_RULE_OF_LAW`; Q12 added as `B2_ECONOMICS`.
- `2026_房山_一模`: Q5 added as `XB3_EXCLUDED`; Q8 added as `B3_POLITICS_RULE_OF_LAW`; Q21 accepted absent because the paper ends at Q20.
- `2026_西城_一模`: Q12 added as `B2_ECONOMICS`; Q14 added as `XB3_EXCLUDED`.
- `2026_西城_期末`: Q9 added as `XB3_EXCLUDED`.

## Note

This closes the visible question-number gap ledger but does not close the run: two newly found questions remain blocked as mixed objective items, and the whole matrix still has 121 blocked rows.

## Deliverables

- `05_reports/raw_source_inspection_review.csv`
- `05_reports/raw_source_inspection_repair_audit.csv`
- `04_module_classification/raw_source_inspection_repaired_classification_matrix.csv`
- `00_control/RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv`
- `05_reports/raw_source_inspection_repaired_blocked_queue.csv`
- `05_reports/question_gap_after_raw_source_inspection.csv`
