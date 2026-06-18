# Twenty-Question Structure Acceptance Report

Generated from `auxiliary_clue_repaired_classification_matrix.csv`.

## Scope

- Reviewed likely actual 20-question structures: 11
- Accepted as actual 20-question papers: 11
- Kept open: 0
- Matrix rows added: 0

## Matrix Counts

- Rows: 1249
- Status counts: {'reference-only': 6, 'included': 458, 'module-boundary-excluded': 666, 'blocked': 119}
- Included target counts: {'B3_POLITICS_RULE_OF_LAW': 155, 'B2_ECONOMICS': 193, 'B4_CULTURE': 110}
- Blocked rows: 119
- Duplicate `(suite_id, question)` keys: 0

## Gap Counts

- Missing-question entries before this review: 33
- Resolved by this review: 11
- Remaining missing-question entries: 22

## Acceptance Rule

A `21` gap was accepted as an actual 20-question structure only when paper/OCR candidates reached Q20, no question-candidate row had top-level Q21, and source text search found no line-start top-level Q21 marker.

## Deliverables

- `05_reports/twenty_question_structure_review.csv`
- `05_reports/twenty_question_structure_acceptance_audit.csv`
- `05_reports/question_gap_after_twenty_question_structure_review.csv`
- `04_module_classification/twenty_question_structure_accepted_classification_matrix.csv`
- `00_control/TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv`
- `05_reports/twenty_question_structure_accepted_blocked_queue.csv`
