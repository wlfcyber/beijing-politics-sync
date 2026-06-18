# Classification Readiness Report

- generated_at: 2026-06-17T17:00:00
- source_inventory_rows: 370
- canonical_source_rows: 195
- extracted_or_checked_rows: 195
- question_candidate_rows: 3186
- classified_suite_question_rows: 1203
- current_handoff_matrix: `00_control/FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv`
- current_handoff_rows: 1337
- current_handoff_blocked_rows: 0
- suites_with_classified_rows: 63

- suite_overview_rows: 63
- suites_without_classified_rows: 0

## Cache And Extraction

- cache_hit_no: 28
- cache_hit_yes: 167

- cache-hit: 167
- empty-or-unsupported: 3
- raw-extracted: 23
- skipped-excluded: 2

## Classification Status Counts

- blocked: 190
- included: 409
- module-boundary-excluded: 598
- reference-only: 6

## Module Counts

- B1_EXCLUDED: 3
- B2_ECONOMICS: 164
- B3_POLITICS_RULE_OF_LAW: 143
- B4_CULTURE: 106
- B4_PHILOSOPHY_EXCLUDED: 107
- EXCLUDED_BY_HARD_RULE: 1
- REFERENCE_HELPER_ONLY: 2
- UNKNOWN_OR_MIXED: 190
- XB1_EXCLUDED: 127
- XB2_EXCLUDED: 205
- XB3_EXCLUDED: 155

## Question Type Counts

- objective: 859
- subjective: 341
- unknown: 3

## Included Target Counts

- B2_ECONOMICS: 162
- B3_POLITICS_RULE_OF_LAW: 141
- B4_CULTURE: 106

## Boundary And Blocker Notes

- Rows marked `module-boundary-excluded` should not enter the three future宝典 lines.
- Rows marked `blocked` require manual review before any future coverage claim.
- This is a source-forward preparation matrix, not a student-facing artifact.

## Subquestion Split Draft

- input_parent_rows: 45
- draft_subquestion_rows: 58
- resolved_target_subquestions: 27
- resolved_boundary_subquestions: 24
- unresolved_subquestions_after_split: 7
- duplicate_subquestion_keys: 0
- parent_disposition: 20 fully resolved by draft; 4 partially resolved by draft; 21 unresolved by draft.
- output: `04_module_classification/subquestion_split_matrix.csv`
- note: This draft is not yet integrated into the parent matrix and cannot be used as final coverage closure by itself.

## Subquestion-Integrated Handoff Matrix

- output_rows: 1236
- replaced_blocked_parent_rows: 25
- integrated_subquestion_rows: 58
- status_counts: included 436; module-boundary-excluded 622; blocked 172; reference-only 6
- target_included_counts: B2_ECONOMICS 184; B3_POLITICS_RULE_OF_LAW 145; B4_CULTURE 107
- duplicate_question_or_subquestion_keys: 0
- output: `00_control/SUBQUESTION_INTEGRATED_COVERAGE_MATRIX.csv`
- blocked_queue: `05_reports/subquestion_integrated_blocked_queue.csv`
- note: Use this as the safer handoff matrix for future B2/B3/B4_CULTURE宝典 preparation, while preserving the parent-only matrix as audit history.

## Prompt-Resolved Handoff Matrix

- output_rows: 1236
- prompt_resolved_rows: 53
- status_counts: included 453; module-boundary-excluded 658; blocked 119; reference-only 6
- target_included_counts: B2_ECONOMICS 192; B3_POLITICS_RULE_OF_LAW 152; B4_CULTURE 109
- duplicate_question_or_subquestion_keys: 0
- high_risk_boundary_terms_in_target_prompt_resolved_rows: 0
- output: `00_control/PROMPT_RESOLVED_COVERAGE_MATRIX.csv`
- blocked_queue: `05_reports/prompt_resolved_blocked_queue.csv`
- audit: `05_reports/prompt_resolution_audit.csv`
- note: This remains audit history for the strong-prompt resolution stage. It was superseded by later gap repair matrices and is not final closure.

## Question Gap Triage

- input_gap_rows: 21
- likely_actual_20_question_paper: 11
- paper_or_ocr_missing_but_auxiliary_present: 6
- source_or_ocr_missing_no_candidate: 4
- output: `05_reports/question_gap_triage.csv`
- note: The gap list is now prioritized. The 10 non-20-question rows are the urgent repair/inspection set for final closure.

## Question Gap Repair Candidates

- missing_question_rows: 45
- repair_primary_question_split_high_confidence: 2
- raw_marker_candidate_visual_check: 8
- raw_paper_repair_with_auxiliary_clue: 6
- raw_source_manual_inspection_needed: 18
- accept_20_question_structure_after_source_spotcheck: 11
- output: `05_reports/question_gap_repair_candidates.csv`
- note: This packet is deliberately conservative. Raw OCR/text digits can be option numbers or table numbers; only high-confidence rows should drive splitter repair before visual/original-paper inspection.

## Gap High-Confidence Repaired Handoff Matrix

- output_rows: 1238
- added_high_confidence_rows: 2
- status_counts: included 454; module-boundary-excluded 659; blocked 119; reference-only 6
- target_included_counts: B2_ECONOMICS 192; B3_POLITICS_RULE_OF_LAW 153; B4_CULTURE 109
- remaining_missing_question_entries_from_prior_gap: 43
- output: `00_control/GAP_HIGH_CONFIDENCE_REPAIRED_COVERAGE_MATRIX.csv`
- audit: `05_reports/gap_high_confidence_repair_audit.csv`
- note: This remains audit history for the high-confidence gap repair stage. It is not final closure.

## Raw Marker Review Repaired Handoff Matrix

- reviewed_raw_marker_rows: 8
- true_top_level_questions: 5
- false_markers: 3
- output_rows: 1243
- status_counts: included 456; module-boundary-excluded 662; blocked 119; reference-only 6
- target_included_counts: B2_ECONOMICS 193; B3_POLITICS_RULE_OF_LAW 153; B4_CULTURE 110
- remaining_missing_question_entries_from_prior_gap: 38
- output: `00_control/RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv`
- review: `05_reports/raw_marker_visual_review.csv`
- audit: `05_reports/raw_marker_review_repair_audit.csv`
- note: This remains audit history for the raw-marker review stage. It is not final closure.

## Auxiliary Clue Repaired Handoff Matrix

- reviewed_auxiliary_clue_rows: 6
- accepted_parent_question_gaps: 5
- added_matrix_rows: 6
- unaccepted_rubric_only_clues: 1
- output_rows: 1249
- status_counts: included 458; module-boundary-excluded 666; blocked 119; reference-only 6
- target_included_counts: B2_ECONOMICS 193; B3_POLITICS_RULE_OF_LAW 155; B4_CULTURE 110
- remaining_missing_question_entries_from_prior_gap: 33
- output: `00_control/AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv`
- review: `05_reports/auxiliary_clue_source_review.csv`
- audit: `05_reports/auxiliary_clue_repair_audit.csv`
- note: This remains audit history for the auxiliary-clue review stage. It is not final closure.

## Twenty-Question Structure Accepted Handoff Matrix

- reviewed_likely_actual_20_question_structures: 11
- accepted_actual_20_question_structures: 11
- kept_open: 0
- matrix_rows_added: 0
- output_rows: 1249
- status_counts: included 458; module-boundary-excluded 666; blocked 119; reference-only 6
- target_included_counts: B2_ECONOMICS 193; B3_POLITICS_RULE_OF_LAW 155; B4_CULTURE 110
- remaining_missing_question_entries_from_prior_gap: 22
- output: `00_control/TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv`
- review: `05_reports/twenty_question_structure_review.csv`
- audit: `05_reports/twenty_question_structure_acceptance_audit.csv`
- note: This remains audit history after accepting the 11 proved 20-question structures. It is not final closure.

## Raw Source Inspection Repaired Handoff Matrix

- reviewed_remaining_gap_entries: 22
- added_matrix_rows: 16
- accepted_absent_structure_gap_entries: 6
- output_rows: 1265
- status_counts: included 464; module-boundary-excluded 674; blocked 121; reference-only 6
- target_included_counts: B2_ECONOMICS 195; B3_POLITICS_RULE_OF_LAW 159; B4_CULTURE 110
- remaining_missing_question_entries: 0
- duplicate_question_or_subquestion_keys: 0
- output: `00_control/RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv`
- review: `05_reports/raw_source_inspection_review.csv`
- audit: `05_reports/raw_source_inspection_repair_audit.csv`
- blocked_queue: `05_reports/raw_source_inspection_repaired_blocked_queue.csv`
- note: This remains audit history for the raw-source inspection stage. It closes the visible question-number gap ledger but has been superseded by the strong-blocker-resolved matrix.

## Strong Blocker Resolved Handoff Matrix

- input_blocked_rows: 121
- strong_source_rows_resolved: 64
- rows_kept_blocked: 57
- output_rows: 1265
- status_counts: included 486; module-boundary-excluded 716; blocked 57; reference-only 6
- target_included_counts: B2_ECONOMICS 206; B3_POLITICS_RULE_OF_LAW 167; B4_CULTURE 113
- duplicate_question_or_subquestion_keys: 0
- remaining_missing_question_entries: 0
- high_risk_boundary_terms_in_newly_resolved_target_rows: 0
- output: `00_control/STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv`
- review: `05_reports/strong_blocker_resolution_review.csv`
- audit: `05_reports/strong_blocker_resolution_audit.csv`
- blocked_queue: `05_reports/strong_blocker_resolved_blocked_queue.csv`
- note: This remains audit history for the strong-blocker stage. It has been superseded by the culture-component-extracted matrix after applying the user rule on philosophy/culture mixed questions.

## Culture Component Extracted Handoff Matrix

- user_rule: 哲学文化混合题需要抽离题面和细则中的文化部分；民族精神属于文化。
- culture_component_rows_added: 20
- original_rows_resolved_or_remainder_closed: 5
- output_rows: 1285
- status_counts: included 508; module-boundary-excluded 718; blocked 53; reference-only 6
- target_included_counts: B2_ECONOMICS 206; B3_POLITICS_RULE_OF_LAW 167; B4_CULTURE 135
- row_granularity_counts: suite 3; question 1202; subquestion 60; culture_component 20
- duplicate_question_or_component_keys: 0
- remaining_missing_question_entries: 0
- output: `00_control/CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv`
- review: `05_reports/culture_component_extraction_review.csv`
- audit: `05_reports/culture_component_extraction_audit.csv`
- row_resolution_audit: `05_reports/culture_component_row_resolution_audit.csv`
- blocked_queue: `05_reports/culture_component_extracted_blocked_queue.csv`
- note: This remains audit history for the culture-component extraction stage. It has been superseded by the remaining-strong-cleanup matrix, and final coverage closure remains rejected.

## Remaining Strong Cleanup Handoff Matrix

- original_blocked_rows_resolved_or_remainder_closed: 13
- target_component_rows_added: 9
- output_rows: 1294
- status_counts: included 522; module-boundary-excluded 726; blocked 40; reference-only 6
- target_included_counts: B2_ECONOMICS 213; B3_POLITICS_RULE_OF_LAW 171; B4_CULTURE 138
- row_granularity_counts: suite 3; question 1202; subquestion 60; culture_component 20; target_component 9
- duplicate_question_or_component_keys: 0
- remaining_missing_question_entries: 0
- audit_blank_evidence_rows_after_fallback_repair: 0
- output: `00_control/REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv`
- row_audit: `05_reports/remaining_strong_cleanup_audit.csv`
- component_audit: `05_reports/remaining_target_component_audit.csv`
- blocked_queue: `05_reports/remaining_strong_cleanup_blocked_queue.csv`
- note: This remains audit history for the remaining-strong-cleanup stage. It has been superseded by the source-explicit-cleanup matrix, and final coverage closure remains rejected.

## Source Explicit Cleanup Handoff Matrix

- original_blocked_rows_resolved_or_remainder_closed: 17
- target_component_rows_added: 6
- output_rows: 1300
- status_counts: included 536; module-boundary-excluded 735; blocked 23; reference-only 6
- target_included_counts: B2_ECONOMICS 217; B3_POLITICS_RULE_OF_LAW 181; B4_CULTURE 138
- row_granularity_counts: suite 3; question 1202; subquestion 60; culture_component 20; target_component 15
- duplicate_question_or_component_keys: 0
- remaining_missing_question_entries: 0
- audit_blank_evidence_rows: 0
- output: `00_control/SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv`
- row_audit: `05_reports/source_explicit_cleanup_audit.csv`
- component_audit: `05_reports/source_explicit_target_component_audit.csv`
- blocked_queue: `05_reports/source_explicit_cleanup_blocked_queue.csv`
- note: This remains audit history for the source-explicit-cleanup stage. It has been superseded by the suite-identity-culture-repaired matrix after splitting the 2025 海淀期中/期末 source collision.

## Suite Identity Culture Repaired Handoff Matrix

- contaminated_2025_haidian_final_rows_removed: 22
- rebuilt_2025_haidian_midterm_rows: 24
- rebuilt_2025_haidian_final_rows: 28
- target_component_rows_added_this_pass: 6
- output_rows: 1330
- status_counts: included 554; module-boundary-excluded 750; blocked 20; reference-only 6
- target_included_counts: B2_ECONOMICS 223; B3_POLITICS_RULE_OF_LAW 190; B4_CULTURE 141
- row_granularity_counts: suite 3; question 1222; subquestion 64; culture_component 20; target_component 21
- duplicate_question_or_component_keys: 0
- matrix_control_equality: pass
- audit_blank_evidence_rows: 0
- q22_culture_component: `2025_海淀_期末` `22#B4_CULTURE_COMPONENT` records `中华优秀传统文化,中华民族精神,愚公精神`; `民族精神` is treated as B4_CULTURE.
- output: `00_control/SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv`
- audit: `05_reports/suite_identity_culture_repair_audit.csv`
- blocked_queue: `05_reports/suite_identity_culture_repaired_blocked_queue.csv`
- note: This remains audit history for the suite-identity-culture-repaired stage. It has been superseded by the culture-hint-final-cleanup matrix after applying the renewed rule that culture points must be extracted from both question text and scoring/rubric text.

## Culture Hint Final Cleanup Handoff Matrix

- original_blocked_rows_resolved_or_remainder_closed: 17
- redundant_component_rows_removed: 1
- component_rows_added_this_pass: 7
- output_rows: 1336
- status_counts: included 562; module-boundary-excluded 765; blocked 3; reference-only 6
- target_included_counts: B2_ECONOMICS 225; B3_POLITICS_RULE_OF_LAW 193; B4_CULTURE 144
- row_granularity_counts: suite 3; question 1222; subquestion 64; culture_component 23; target_component 24
- duplicate_question_or_component_keys: 0
- matrix_control_equality: pass
- audit_blank_evidence_rows: 0
- direct_included_high_risk_boundary_pollution: 0
- culture_rule: question text and scoring/rubric text were both checked for cultural scoring points; `民族精神`, `中华民族精神`, `革命精神谱系`, `爱国主义精神`, and `中华优秀传统文化` are treated as B4_CULTURE when supported by source/rubric evidence.
- output: `00_control/CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv`
- canonical_output: `00_control/COVERAGE_MATRIX.csv`
- classification_matrix: `04_module_classification/culture_hint_final_cleanup_classification_matrix.csv`
- canonical_classification_matrix: `04_module_classification/module_classification_matrix.csv`
- audit: `05_reports/culture_hint_final_cleanup_audit.csv`
- component_audit: `05_reports/culture_hint_final_component_audit.csv`
- blocked_queue: `05_reports/culture_hint_final_blocked_queue.csv`
- note: This remains audit history for the culture-hint-final-cleanup stage. It has been superseded by the final-answer-key closure matrix after reliable answer keys closed `2026_丰台_一模 Q1`, `2026_丰台_期末 Q2`, and `2026_丰台_期末 Q6`.

## Final Answer Key Closure Handoff Matrix

- answer_key_blocker_rows_resolved: 3
- target_component_rows_added_this_pass: 1
- output_rows: 1337
- status_counts: included 563; module-boundary-excluded 768; reference-only 6; blocked 0
- target_included_counts: B2_ECONOMICS 225; B3_POLITICS_RULE_OF_LAW 194; B4_CULTURE 144
- row_granularity_counts: suite 3; question 1222; subquestion 64; culture_component 23; target_component 25
- duplicate_question_or_component_keys: 0
- matrix_control_equality: pass
- audit_blank_evidence_rows: 0
- remaining_missing_question_entries: 0
- closed_rows: `2026_丰台_一模 Q1` answer B; `2026_丰台_期末 Q2` answer C; `2026_丰台_期末 Q6` answer A
- output: `00_control/FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv`
- canonical_output: `00_control/COVERAGE_MATRIX.csv`
- classification_matrix: `04_module_classification/final_answer_key_closure_classification_matrix.csv`
- canonical_classification_matrix: `04_module_classification/module_classification_matrix.csv`
- row_audit: `05_reports/final_answer_key_closure_audit.csv`
- component_audit: `05_reports/final_answer_key_component_audit.csv`
- blocked_queue: `05_reports/final_answer_key_blocked_queue.csv`
- note: This is the latest handoff matrix for future B2/B3/B4_CULTURE 宝典 preparation. It keeps reference-only/helper rows separate and leaves no live blocker under the declared source-forward preparation scope.

## Fable5 Source Cache Handoff

- primary_file_for_fable5: `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`
- read_me: `06_fable5_source_cache/FABLE5_READ_ME_FIRST.md`
- manifest: `06_fable5_source_cache/fable5_source_cache_manifest.csv`
- suite_index: `06_fable5_source_cache/fable5_suite_source_index.csv`
- source_inventory_rows: 370
- canonical_cache_rows: 195
- canonical_cache_unique_sha256: 194
- cache_status_after_repair: cache-hit 167; raw-extracted 26; skipped-excluded 2; empty-or-unsupported 0
- fable5_handoff_status: ai_readable_text_ready 193; excluded_by_hard_rule 2; needs_repair 0
- repaired_empty_or_unsupported_sources: 3
- jsonl_lines: 195
- jsonl_parse_errors: 0
- embedded_source_text_chars: 1,060,103
- subjective_included_rows_using_reference_answer_as_source: 0
- reference_answer_guardrail: reference-answer packets are marked `do_not_use_as_rubric`
- missing_matrix_evidence_paths: 0
- note: Fable5 should start from this source cache instead of re-OCRing PDFs/PPTX/DOCX. OCR text is source-derived and page-marked, but not a human-certified character-perfect校勘 layer.

## Top Suites By Row Count

- 2025_海淀_期末: 28
- 2025_东城_期末: 26
- 2024_丰台_二模: 24
- 2024_石景山_一模: 24
- 2026_朝阳_一模: 24
- 2025_海淀_期中: 24
- 2024_东城_一模: 23
- 2024_顺义_二模: 23
- 2025_东城_二模: 23
- 2025_丰台_期末: 23
- 2025_延庆_一模: 23
- 2025_朝阳_一模: 23
- 2025_顺义_一模: 23
- 2026_东城_二模: 23
- 2026_丰台_期末: 23
- 2026_延庆_一模: 23
- 2026_房山_一模: 23
- 2026_石景山_二模: 23
- 2024_东城_二模: 22
- 2024_朝阳_期中: 22

## Suites Without Classified Rows
