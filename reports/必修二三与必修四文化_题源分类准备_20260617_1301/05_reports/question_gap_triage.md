# Question Gap Triage

- input_gap_rows: 21
- output: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/05_reports/question_gap_triage.csv`

## Triage Counts

- likely_actual_20_question_paper: 11
- paper_or_ocr_missing_but_auxiliary_present: 6
- source_or_ocr_missing_no_candidate: 4

## Rows

- 2024_东城_一模: missing=4; status=paper_or_ocr_missing_but_auxiliary_present; note=auxiliary_sources_have_missing_questions=4
- 2024_朝阳_二模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2024_朝阳_期中: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2024_海淀_一模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2024_海淀_期中: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2024_石景山_一模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2024_西城_一模: missing=5 20 21; status=source_or_ocr_missing_no_candidate; note=missing_questions_absent_from_primary_and_auxiliary_candidates
- 2024_西城_二模: missing=1 4 15 20 21; status=paper_or_ocr_missing_but_auxiliary_present; note=auxiliary_sources_have_missing_questions=1
- 2024_顺义_二模: missing=6 9 14 20 21; status=paper_or_ocr_missing_but_auxiliary_present; note=auxiliary_sources_have_missing_questions=6,20
- 2025_房山_一模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2025_西城_二模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2026_东城_一模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2026_丰台_一模: missing=5 7 9 14; status=paper_or_ocr_missing_but_auxiliary_present; note=auxiliary_sources_have_missing_questions=5,7
- 2026_丰台_二模: missing=15; status=source_or_ocr_missing_no_candidate; note=missing_questions_absent_from_primary_and_auxiliary_candidates
- 2026_丰台_期末: missing=2 6 7 9 10 12; status=paper_or_ocr_missing_but_auxiliary_present; note=auxiliary_sources_have_missing_questions=2,6,9,10
- 2026_延庆_一模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2026_房山_一模: missing=1 5 8 17 21; status=paper_or_ocr_missing_but_auxiliary_present; note=auxiliary_sources_have_missing_questions=17
- 2026_石景山_二模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2026_西城_一模: missing=12 14; status=source_or_ocr_missing_no_candidate; note=missing_questions_absent_from_primary_and_auxiliary_candidates
- 2026_西城_二模: missing=21; status=likely_actual_20_question_paper; note=primary_sources_have_1_to_20_no_21
- 2026_西城_期末: missing=9 15; status=source_or_ocr_missing_no_candidate; note=missing_questions_absent_from_primary_and_auxiliary_candidates

## Governor Note

- `likely_actual_20_question_paper` can be accepted only as a paper-structure finding for the source matrix, not as proof that the final handbook is complete.
- `paper_or_ocr_missing_but_auxiliary_present` should be routed to OCR/raw-paper repair before final closure.
- `source_or_ocr_missing_no_candidate` requires raw source inspection if final coverage is needed.
