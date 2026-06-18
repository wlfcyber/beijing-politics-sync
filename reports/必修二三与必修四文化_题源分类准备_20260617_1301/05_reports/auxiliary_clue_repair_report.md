# Auxiliary Clue Source Review Repair Report

Generated from `raw_marker_review_repaired_classification_matrix.csv`.

## Scope

- Reviewed auxiliary-only clues: 6
- Added matrix rows: 6
- Unaccepted auxiliary clues: 1 (`2026_丰台_期末` Q6, primary source not found)

## Matrix Counts

- Rows: 1249
- Status counts: {'reference-only': 6, 'included': 458, 'module-boundary-excluded': 666, 'blocked': 119}
- Included module counts: {'B3_POLITICS_RULE_OF_LAW': 155, 'B2_ECONOMICS': 193, 'B4_CULTURE': 110}
- Duplicate `(suite_id, question)` keys: 0
- Remaining question-gap entries: 33

## Decisions

- `2024_顺义_二模` Q6: accepted as top-level hidden-number question; classified `XB3_EXCLUDED`.
- `2024_顺义_二模` Q20: accepted as top-level hidden-number question; classified `B1_EXCLUDED`.
- `2026_丰台_一模` Q7: accepted as top-level OCR hyphen-marker question; classified `XB3_EXCLUDED`.
- `2026_丰台_期末` Q6: not accepted; rubric clue only, no reliable primary-source span located.
- `2026_丰台_期末` Q9: accepted as top-level hidden-number question; classified `B3_POLITICS_RULE_OF_LAW`.
- `2026_房山_一模` Q17: accepted and split into Q17(1) `XB2_EXCLUDED` plus Q17(2) `B3_POLITICS_RULE_OF_LAW`.

## Deliverables

- `05_reports/auxiliary_clue_source_review.csv`
- `05_reports/auxiliary_clue_repair_audit.csv`
- `04_module_classification/auxiliary_clue_repaired_classification_matrix.csv`
- `00_control/AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv`
- `05_reports/auxiliary_clue_repaired_blocked_queue.csv`
- `05_reports/question_gap_after_auxiliary_clue_review.csv`
