# HANDOFF_QUEUE

## H001 - Cache-first requirement

- status: open
- message: Before raw conversion, inspect reusable project caches under `/Users/wanglifei/Desktop/北京高考政治` and relevant preprocessed corpus folders if present. Raw files are fallback when cache is missing or insufficient.

## H002 - Future ClaudeCode packet

- status: ready
- message: If the user wants an independent ClaudeCode rerun, pass `SOURCE_LEDGER.csv`, `COVERAGE_MATRIX.csv`, `module_classification_matrix.csv`, `question_gap_review.csv`, the run hard-rule notebook, and the script directory. The worker must not call the matrix full coverage until `UNKNOWN_OR_MIXED` rows and gap warnings are reviewed.

## H003 - Manual module review

- status: open
- message: Review 190 `UNKNOWN_OR_MIXED` rows in `05_reports/blocked_manual_review_queue.csv` and decide whether each belongs to B2, B3, B4_CULTURE, another module, or remains blocked.

## H004 - Question gap review

- status: open
- message: Review `05_reports/question_gap_review.csv`; confirm whether each missing question number is an OCR split issue, an actual shorter paper, or a source problem.

## H005 - Manual subquestion split

- status: draft_done_pending_integration
- message: `04_module_classification/subquestion_split_matrix.csv` now gives a conservative draft for the 45 split rows: 58 subquestion rows, 27 target subquestions, 24 boundary subquestions, 7 unresolved subquestions, 0 duplicate subquestion keys. Parent matrix is not yet updated.

## H006 - Subquestion draft integration

- status: done_with_blockers_remaining
- message: Formal integrated matrix created at `00_control/SUBQUESTION_INTEGRATED_COVERAGE_MATRIX.csv` and `04_module_classification/subquestion_integrated_classification_matrix.csv`; remaining blockers are visible in `05_reports/subquestion_integrated_blocked_queue.csv`.

## H007 - Remaining integrated blockers

- status: superseded_by_prompt_resolved_queue
- message: `05_reports/subquestion_integrated_blocked_queue.csv` remains audit history. The live queue is now `05_reports/prompt_resolved_blocked_queue.csv` with 119 blocked rows.

## H008 - Remaining prompt-resolved blockers

- status: open
- message: Continue from `05_reports/prompt_resolved_blocked_queue.csv`, which has 119 blocked rows after subquestion integration and strong prompt resolution. Do not use the older 190-row or 172-row blocker counts as the live handoff count except for audit history.

## H009 - Question gap triage

- status: open
- message: Continue from `05_reports/question_gap_triage.csv`: 11 rows likely actual 20-question paper structures, 6 rows need OCR/raw-paper repair with auxiliary clues, and 4 rows need raw-source inspection because no candidate captured the missing question numbers.

## H010 - Question gap repair candidates

- status: superseded_by_H012
- message: `05_reports/question_gap_repair_candidates.csv` remains audit history. The 2 high-confidence rows and 8 raw-marker candidates have been processed into H011/H012. Continue from H012 plus the remaining auxiliary-only and raw-source inspection rows.

## H011 - High-confidence gap repaired matrix

- status: superseded_by_H012
- message: `00_control/GAP_HIGH_CONFIDENCE_REPAIRED_COVERAGE_MATRIX.csv` remains audit history. It has been superseded by `RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv` after closing the 8 raw-marker candidates.

## H012 - Raw marker review repaired matrix

- status: superseded_by_H013
- message: `00_control/RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv` remains audit history. It has been superseded by `AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv` after closing the 6 auxiliary-clue source checks.

## H013 - Auxiliary clue repaired matrix

- status: superseded_by_H014
- message: `00_control/AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv` remains audit history. It has been superseded by `TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv` after accepting the 11 likely actual 20-question structures.

## H014 - Twenty-question structure accepted matrix

- status: superseded_by_H015
- message: `00_control/TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv` remains audit history. It has been superseded by `RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv` after closing the remaining 22 question-gap entries.

## H015 - Raw source inspection repaired matrix

- status: superseded_by_H017
- message: `00_control/RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv` remains audit history. It closed the visible question-number gap ledger, but has been superseded by the strong-blocker-resolved matrix after 64 blocked rows were resolved.

## H016 - Boundary reason suspect outside gap ledger

- status: open
- message: During raw-source spot-check, `2026_西城_一模` Q21 was observed in original DOCX as a philosophy/exploration-modernization subjective item, while the inherited matrix classifies it as `XB2_EXCLUDED`. Status remains boundary-excluded, so it does not pollute B2/B3/B4_CULTURE included counts, but the boundary reason should be corrected in a later boundary-reason cleanup pass.

## H017 - Strong blocker resolved matrix

- status: superseded_by_H018
- message: `00_control/STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv` remains audit history. It reduced blocked rows from 121 to 57, then was superseded by culture-component extraction after user clarified that philosophy/culture mixed questions need cultural scoring-point extraction.

## H018 - Culture component extracted matrix

- status: superseded_by_H019
- message: `00_control/CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv` remains audit history. It added 20 B4_CULTURE culture-component rows, then was superseded by remaining-strong-cleanup after 13 more original blocked rows were resolved/excluded and 9 target-component rows were added.

## H019 - Remaining strong cleanup matrix

- status: superseded_by_H020
- message: `00_control/REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv` remains audit history. It reduced live blocked rows to 40, then was superseded by source-explicit-cleanup after 17 more original blocked rows were resolved/excluded and 6 target-component rows were added.

## H020 - Source explicit cleanup matrix

- status: superseded_by_H021
- message: `00_control/SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv` remains audit history. It has been superseded by suite-identity + culture repair after the 2025 海淀期中/期末 collision was split and 2025 海淀期末 Q22 culture components were added.

## H021 - Suite identity culture repaired matrix

- status: superseded_by_H022
- message: `00_control/SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv` remains audit history. It was superseded by `CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv` after the user reiterated that philosophy/culture questions require extracting culture from both question text and scoring rubrics.

## H022 - Culture hint final cleanup matrix

- status: superseded_by_H023
- message: Latest handoff matrix is now `00_control/CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv`, also copied to canonical `00_control/COVERAGE_MATRIX.csv` and `04_module_classification/module_classification_matrix.csv`. It has 1336 rows, 23 culture-component rows and 24 target-component rows, raises B2/B3/B4_CULTURE included to 225/193/144, keeps question-number gap at 0, and leaves 3 blocked rows in `05_reports/culture_hint_final_blocked_queue.csv`: 2026 丰台一模 Q1, 2026 丰台期末 Q2, 2026 丰台期末 Q6. These remaining blockers need reliable answer keys or manual choice-option split; do not force-close them from culture background alone.

## H023 - Final answer-key closure matrix

- status: current_final_handoff
- message: Latest handoff matrix is now `00_control/FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv`, also copied to canonical `00_control/COVERAGE_MATRIX.csv` and `04_module_classification/module_classification_matrix.csv`. It has 1337 rows, 23 culture-component rows and 25 target-component rows, raises B2/B3/B4_CULTURE included to 225/194/144, keeps question-number gap at 0, and leaves 0 live blocked rows. It closes 2026 丰台一模 Q1 with answer B, 2026 丰台期末 Q2 with answer C, and 2026 丰台期末 Q6 with answer A; future B2/B3/B4_CULTURE 宝典 work should start from this matrix.

## H024 - Fable5 source cache handoff

- status: current_model_cache_handoff
- message: Give Fable5 `06_fable5_source_cache/FABLE5_READ_ME_FIRST.md` first, then `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`. The source cache has 195 canonical source packets, 193 AI-readable text-ready packets and 2 hard-rule-excluded Shijingshan final packets. `empty-or-unsupported` is now 0 after repairing Xicheng 2026 second-mock rubric OCR, Tongzhou 2026 first-mock paper OCR, and Shunyi 2026 second-mock paper OCR. Reference-answer packets are marked `do_not_use_as_rubric`; no final included subjective row uses reference-answer as scoring evidence.
