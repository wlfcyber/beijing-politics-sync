# Strong Blocker Resolution Report

Generated from `raw_source_inspection_repaired_classification_matrix.csv`.

## Scope

- Input blocked rows: 121
- Strong-source rows resolved: 64
- Rows kept blocked: 57

## Matrix Counts

- Rows: 1265
- Status counts: {'reference-only': 6, 'included': 486, 'module-boundary-excluded': 716, 'blocked': 57}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 167, 'B2_ECONOMICS': 206, 'B4_CULTURE': 113}
- Resolved module counts: {'XB1_EXCLUDED': 9, 'B2_ECONOMICS': 11, 'XB3_EXCLUDED': 17, 'B3_POLITICS_RULE_OF_LAW': 8, 'B4_PHILOSOPHY_EXCLUDED': 8, 'XB2_EXCLUDED': 8, 'B4_CULTURE': 3}
- Duplicate `(suite_id, question)` keys: 0

## Rule Boundary

This pass only resolves rows with direct paper/OCR source signals. It does not resolve manual-subquestion-split rows, answer-key-dependent mixed choice rows, or weak keyword rows.

## Deliverables

- `05_reports/strong_blocker_resolution_review.csv`
- `05_reports/strong_blocker_resolution_audit.csv`
- `04_module_classification/strong_blocker_resolved_classification_matrix.csv`
- `00_control/STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv`
- `05_reports/strong_blocker_resolved_blocked_queue.csv`
