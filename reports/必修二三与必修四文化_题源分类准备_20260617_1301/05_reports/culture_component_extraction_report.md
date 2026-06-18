# Culture Component Extraction Report

Generated from `strong_blocker_resolved_classification_matrix.csv`.

## Scope

- User rule applied: 哲学文化混合题需要抽离题面和细则中的文化部分；民族精神属于文化。
- Culture component rows added: 20
- Original rows resolved or remainder-closed: 5
- Remaining blocked rows: 53

## Matrix Counts

- Rows: 1285
- Status counts: {'reference-only': 6, 'included': 508, 'module-boundary-excluded': 718, 'blocked': 53}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 167, 'B2_ECONOMICS': 206, 'B4_CULTURE': 135}
- Row granularity counts: {'suite': 3, 'question': 1202, 'subquestion': 60, 'culture_component': 20}
- Culture component rows: 20
- Duplicate `(suite_id, question)` keys: 0

## Rule Boundary

This pass does not treat every cultural word in a material as a B4_CULTURE answer point. It only adds a component when the question, answer, rubric, or manually verified source signal shows a culture judgment or scoring angle. Cross-book legal, logic, or international rows remain excluded unless a culture component is explicitly extracted and recorded.

## Deliverables

- `05_reports/culture_component_extraction_review.csv`
- `05_reports/culture_component_extraction_audit.csv`
- `05_reports/culture_component_row_resolution_audit.csv`
- `04_module_classification/culture_component_extracted_classification_matrix.csv`
- `00_control/CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv`
- `05_reports/culture_component_extracted_blocked_queue.csv`
