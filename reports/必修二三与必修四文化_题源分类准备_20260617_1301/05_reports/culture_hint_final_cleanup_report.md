# Culture Hint Final Cleanup Report

- input_matrix: `04_module_classification/suite_identity_culture_repaired_classification_matrix.csv`
- output_matrix: `04_module_classification/culture_hint_final_cleanup_classification_matrix.csv`
- output_coverage: `00_control/CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv`
- original blocked rows resolved or remainder-closed: 17
- redundant component rows removed: 1
- component rows added: 7
- output rows: 1336
- status counts: module-boundary-excluded 765; included 562; reference-only 6; blocked 3
- target included counts: B2_ECONOMICS 225; B3_POLITICS_RULE_OF_LAW 193; B4_CULTURE 144
- row granularity counts: question 1222; subquestion 64; target_component 24; culture_component 23; suite 3
- duplicate matrix keys: 0
- audit blank evidence rows: 0

## Still Blocked

The remaining blocked rows require a reliable answer key or manual choice split before closure:

- 2026_丰台_一模 1: manual_review_needed
- 2026_丰台_期末 2: manual_choice_module_split_or_answer_key_needed
- 2026_丰台_期末 6: manual_choice_module_split_or_answer_key_needed

## User Rule Applied

- Philosophy/culture mixed questions were rechecked against both question text and scoring/rubric text.
- Explicit culture points, including `民族精神` and `中华优秀传统文化`, were extracted as B4_CULTURE components instead of being swallowed by philosophy remainders.
