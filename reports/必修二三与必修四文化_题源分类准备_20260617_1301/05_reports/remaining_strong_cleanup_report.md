# Remaining Strong Cleanup Report

Generated from `culture_component_extracted_classification_matrix.csv`.

## Scope

- Original blocked rows resolved or excluded: 13
- Target component rows added: 9
- Remaining blocked rows: 40

## Matrix Counts

- Rows: 1294
- Status counts: {'reference-only': 6, 'included': 522, 'module-boundary-excluded': 726, 'blocked': 40}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 171, 'B2_ECONOMICS': 213, 'B4_CULTURE': 138}
- Row granularity counts: {'suite': 3, 'question': 1202, 'subquestion': 60, 'culture_component': 20, 'target_component': 9}
- Duplicate `(suite_id, question)` keys: 0

## Rule Boundary

This pass only handles rows whose module direction is explicit in the source prompt, options, or answer context. Multi-module rows that still require answer keys, small-question splitting, or uncertain module weights remain blocked.

## Deliverables

- `05_reports/remaining_strong_cleanup_audit.csv`
- `05_reports/remaining_target_component_audit.csv`
- `04_module_classification/remaining_strong_cleanup_classification_matrix.csv`
- `00_control/REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv`
- `05_reports/remaining_strong_cleanup_blocked_queue.csv`
