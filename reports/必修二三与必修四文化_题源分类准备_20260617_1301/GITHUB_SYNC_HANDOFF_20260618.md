# GitHub Sync Handoff - 2026-06-18

## Scope

This handoff uploads the current thread's work for:

- `reports/必修二三与必修四文化_题源分类准备_20260617_1301`
- the matching master-governor index files needed to rediscover this run from the sync repo

This is a source-preparation and classification run for:

- B2_ECONOMICS: 必修二《经济与社会》
- B3_POLITICS_RULE_OF_LAW: 必修三《政治与法治》
- B4_CULTURE: 必修四《哲学与文化》文化部分

It is not a final student handbook.

## Live Handoff Entry Points

- `00_control/00_飞哥必修二三与文化分类准备硬性要求记事本.md`
- `00_control/COVERAGE_MATRIX.csv`
- `04_module_classification/module_classification_matrix.csv`
- `00_control/CHAOYANG_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`
- `00_control/FINAL_ACCEPTANCE_REPORT.md`
- `06_fable5_source_cache/FABLE5_READ_ME_FIRST.md`
- `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`

## Final Verified State Before Sync

- Current matrix rows: 1393.
- Live blocked rows: 0.
- Live ocr-needed rows: 0.
- Duplicate question/subquestion/component keys: 0.
- Target included counts: B2 231, B3 202, B4_CULTURE 153.
- Row granularity: suite 3, question 1265, subquestion 64, culture_component 30, target_component 31.
- Source sha equality: source_inventory 194, cache_manifest 194, Fable5 manifest 194.
- Fable5 JSONL: 194 lines, 0 parse errors, 1,091,691 embedded source-text characters.
- Fable5 statuses: ai_readable_text_ready 193, excluded_by_hard_rule 1, needs_repair 0.
- Reference-answer guardrail: reference-answer packet marked do_not_use_as_rubric; included subjective rows using reference-answer as scoring source: 0.

## Rules Captured In This Thread

- Philosophy/culture mixed questions must be checked through both question text and scoring rules.
- Cultural scoring points must be extracted as B4_CULTURE components instead of being swallowed by philosophy remainders.
- `民族精神`, `中华民族精神`, revolutionary spirit, patriotism, and excellent traditional Chinese culture are cultural points when supported by source evidence.
- Source identity collisions between midterm/final folders must be repaired in source inventory, ledger, cache manifest, question candidates, coverage matrix, and Fable5 cache together.
- Fable5 handoff is not complete unless every source_inventory unique sha is present in cache_manifest and the Fable5 manifest.

## Boundary

OCR text is an AI-readable transcription layer. For exact quotation or page-level visual proof, return to the original PDF/rendered page.

