# Fable5 Source Cache Handoff

- generated_at: 2026-06-17T18:06:14+08:00
- run_dir: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301`
- primary_file_for_fable5: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`
- manifest: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/06_fable5_source_cache/fable5_source_cache_manifest.csv`
- suite_index: `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/06_fable5_source_cache/fable5_suite_source_index.csv`

## What This Solves

- Fable5 can start from one JSONL source cache instead of opening PDFs, DOCX, DOC, or PPTX one by one.
- Each packet keeps the original source path, sha256, suite id, source type, extraction status, and source-derived text.
- Reference answers are explicitly marked `do_not_use_as_rubric`; they may support objective answer-key checks only.
- Rubrics/marking reports are marked separately as usable scoring sources.

## Source Cache Status

- source_inventory_rows: 370
- source_inventory_unique_sha256: 194
- canonical_cache_rows: 194
- canonical_cache_unique_sha256: 194
- cache_handoff_status: {'ai_readable_text_ready': 193, 'excluded_by_hard_rule': 1}
- source_type_counts: {'paper': 71, 'module-classification': 7, 'rubric': 110, 'reference-answer': 1, 'marking-report': 5}
- repaired_empty_or_unsupported_sources: 3
- needs_repair_after_handoff: 0

## Coverage Matrix Status

- final_matrix_rows: 1393
- final_matrix_status_counts: {'reference-only': 6, 'included': 586, 'module-boundary-excluded': 801}
- target_included_counts: B2_ECONOMICS 231; B3_POLITICS_RULE_OF_LAW 202; B4_CULTURE 153
- final_matrix_question_type_counts: {'unknown': 3, 'objective': 950, 'subjective': 440}
- question_candidate_rows: 3215
- subjective_included_rows_using_reference_answer_as_source: 0
- missing_matrix_evidence_paths: 0

## Remaining Boundaries

- `excluded_by_hard_rule` sources are kept visible but are not required input for the B2/B3/B4_CULTURE main handoff.
- Source-derived OCR is an AI-readable transcription layer; exact visual formatting remains in the original files and rendered evidence where needed.
- Do not treat this cache as a student-facing artifact. It is a model handoff/cache artifact.

## Repair Audit

- `2026_通州_一模` paper: raw-extracted -> raw-extracted, chars 9401, `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/02_text_cache/texts/dced3f3054457ebc.txt`
- `2026_西城_二模` rubric: raw-extracted -> raw-extracted, chars 6228, `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/02_text_cache/texts/f414cf7940ad8202.txt`
- `2026_顺义_二模` paper: raw-extracted -> raw-extracted, chars 9103, `/Users/wanglifei/Desktop/北京高考政治/reports/必修二三与必修四文化_题源分类准备_20260617_1301/02_text_cache/texts/fb15943f37f694ac.txt`
