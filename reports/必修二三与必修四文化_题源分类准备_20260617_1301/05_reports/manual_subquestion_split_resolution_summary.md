# Manual Subquestion Split Resolution Summary

- purpose: Conservative draft split for rows marked `manual_subquestion_split_needed`; this does not by itself close final coverage.
- input_rows: 45
- output_subquestion_rows: 58
- unresolved_parent_rows: 20
- output_matrix: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/04_module_classification/subquestion_split_matrix.csv`
- unresolved_file: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/05_reports/manual_subquestion_split_unresolved.csv`

## Parent Resolution Counts

- unresolved_by_subquestion_draft: 21
- fully_resolved_by_subquestion_draft: 20
- partially_resolved_by_subquestion_draft: 4

## Subquestion Resolution Counts

- resolved_target_subquestion: 27
- resolved_boundary_subquestion: 24
- unresolved_needs_manual_review: 7

## Subquestion Module Counts

- B2_ECONOMICS: 22
- XB3_EXCLUDED: 15
- UNKNOWN_OR_MIXED: 7
- XB1_EXCLUDED: 6
- B3_POLITICS_RULE_OF_LAW: 4
- B4_PHILOSOPHY_EXCLUDED: 2
- XB2_EXCLUDED: 1
- B4_CULTURE: 1

## Governor Note

- Rows with `resolved_target_subquestion` can be considered draft-ready for future B2/B3/B4_CULTURE intake only after parent matrix integration.
- Rows with `resolved_boundary_subquestion` should remain visible as excluded subparts, so future handbooks do not silently lose them.
- Classification uses the subquestion prompt up to the first score marker when available; the longer `part_text` is retained only as evidence context.
- Any unresolved row must be checked against the original paper or a longer OCR extract before changing the parent matrix.
