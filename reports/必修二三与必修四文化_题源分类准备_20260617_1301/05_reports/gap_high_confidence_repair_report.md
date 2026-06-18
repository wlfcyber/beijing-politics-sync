# Gap High-Confidence Repair Report

- input_rows: 1236
- added_high_confidence_rows: 2
- output_rows: 1238
- output_matrix: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/04_module_classification/gap_high_confidence_repaired_classification_matrix.csv`
- output_coverage: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/00_control/GAP_HIGH_CONFIDENCE_REPAIRED_COVERAGE_MATRIX.csv`
- audit: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/05_reports/gap_high_confidence_repair_audit.csv`
- remaining_missing_question_entries_from_prior_gap: 43

## Status Counts

- module-boundary-excluded: 659
- included: 454
- blocked: 119
- reference-only: 6

## Target Included Counts

- B2_ECONOMICS: 192
- B3_POLITICS_RULE_OF_LAW: 153
- B4_CULTURE: 109

## Added Rules

- GAP_B3_POLITICS_HIGH_CONFIDENCE: 1
- GAP_XB2_LAW_HIGH_CONFIDENCE: 1

## Governor Note

- This matrix repairs only high-confidence missing question starts from the gap packet.
- It does not close the remaining blocked rows or low-confidence gap candidates.
- Keep `PROMPT_RESOLVED_COVERAGE_MATRIX.csv` as audit history; use this matrix only after accepting the high-confidence repair audit.
