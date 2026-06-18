# Suite Identity + Culture Component Repair Report

Generated from `source_explicit_cleanup_classification_matrix.csv`.

## Scope

- Removed contaminated `2025_海淀_期末` rows: 22
- Rebuilt `2025_海淀_期中` rows: 24
- Rebuilt `2025_海淀_期末` rows: 28
- Explicit target components added: 6
- Remaining blocked rows: 20

## Matrix Counts

- Rows: 1330
- Status counts: {'reference-only': 6, 'included': 554, 'module-boundary-excluded': 750, 'blocked': 20}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 190, 'B2_ECONOMICS': 223, 'B4_CULTURE': 141}
- Row granularity counts: {'suite': 3, 'question': 1222, 'subquestion': 64, 'culture_component': 20, 'target_component': 21}
- Duplicate `(suite_id, question)` keys: 0

## User Rule Applied

- Mixed philosophy/culture or integrated questions must not be swallowed as one undifferentiated row.
- Cultural content is extracted when the question or rubric explicitly gives cultural knowledge/material hooks.
- `民族精神` is treated as `B4_CULTURE`.

## Deliverables

- `05_reports/suite_identity_culture_repair_audit.csv`
- `04_module_classification/suite_identity_culture_repaired_classification_matrix.csv`
- `00_control/SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv`
- `05_reports/suite_identity_culture_repaired_blocked_queue.csv`
