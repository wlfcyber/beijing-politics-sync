# Source Explicit Cleanup Report

Generated from `remaining_strong_cleanup_classification_matrix.csv`.

## Scope

- Original blocked rows resolved or excluded: 17
- Target component rows added: 6
- Remaining blocked rows: 23

## Matrix Counts

- Rows: 1300
- Status counts: {'reference-only': 6, 'included': 536, 'module-boundary-excluded': 735, 'blocked': 23}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 181, 'B2_ECONOMICS': 217, 'B4_CULTURE': 138}
- Row granularity counts: {'suite': 3, 'question': 1202, 'subquestion': 60, 'culture_component': 20, 'target_component': 15}
- Duplicate `(suite_id, question)` keys: 0

## Rule Boundary

This pass only handles rows whose source prompt, answer/rubric pair, or question structure explicitly names the target module or boundary module. Known suite-id collision and answer-key-dependent objective rows remain blocked.

## Deliverables

- `05_reports/source_explicit_cleanup_audit.csv`
- `05_reports/source_explicit_target_component_audit.csv`
- `04_module_classification/source_explicit_cleanup_classification_matrix.csv`
- `00_control/SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv`
- `05_reports/source_explicit_cleanup_blocked_queue.csv`
