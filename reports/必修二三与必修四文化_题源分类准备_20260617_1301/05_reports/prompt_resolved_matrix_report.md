# Prompt-Resolved Matrix Report

- purpose: Conservative prompt-level resolution of remaining blocked rows after subquestion integration.
- input_rows: 1236
- prompt_resolved_rows: 53
- output_rows: 1236
- blocked_rows_after_prompt_resolution: 119
- output_matrix: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/04_module_classification/prompt_resolved_classification_matrix.csv`
- output_coverage: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/00_control/PROMPT_RESOLVED_COVERAGE_MATRIX.csv`
- audit_file: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/05_reports/prompt_resolution_audit.csv`
- blocked_queue: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/05_reports/prompt_resolved_blocked_queue.csv`

## Rule Counts

- B1_SOCIALISM_PROMPT: 12
- XB1_INTERNATIONAL_PROMPT: 9
- B4_PHILOSOPHY_PROMPT: 9
- B2_EXPLICIT_ECONOMICS_PROMPT: 8
- B3_EXPLICIT_POLITICS_PROMPT: 7
- XB3_LOGIC_PROMPT: 6
- B4_CULTURE_PROMPT: 2

## Status Counts

- module-boundary-excluded: 658
- included: 453
- blocked: 119
- reference-only: 6

## Target Included Counts

- B2_ECONOMICS: 192
- B3_POLITICS_RULE_OF_LAW: 152
- B4_CULTURE: 109

## Module Counts

- XB2_EXCLUDED: 206
- B2_ECONOMICS: 194
- XB3_EXCLUDED: 176
- B3_POLITICS_RULE_OF_LAW: 154
- XB1_EXCLUDED: 142
- UNKNOWN_OR_MIXED: 119
- B4_PHILOSOPHY_EXCLUDED: 118
- B4_CULTURE: 109
- B1_EXCLUDED: 15
- REFERENCE_HELPER_ONLY: 2
- EXCLUDED_BY_HARD_RULE: 1

## Governor Note

- This pass only resolves rows with strong prompt evidence. Weak single-keyword rows remain blocked.
- Final closure still requires reviewing the remaining blocked queue and the question-gap review.
