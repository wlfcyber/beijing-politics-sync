# 2026 海淀期中/期末身份与 OCR 文化补丁报告

## Scope

- removed contaminated `2026_海淀_期末` live rows: 21
- rebuilt `2026_海淀_期中` rows: 21
- rebuilt `2026_海淀_期末` rows: 28
- added 2026 海淀期末 culture/target components: 7
- full OCR text for 2026 海淀期末 paper: `02_text_cache/ocr_cache/2026_海淀_期末_试卷/试卷.ocr.txt`
- canonical text overwritten from partial cache: 0

## Source Identity Repairs

- `source_inventory.csv` midterm/final rows changed: 0/4
- `SOURCE_LEDGER.csv` midterm/final rows changed: 0/4
- `question_candidates.csv` midterm/final rows changed: 0/15
- `cache_manifest.csv` midterm/final rows changed: 0/2

## Matrix Counts

- rows: 1365
- status counts: {'reference-only': 6, 'included': 572, 'module-boundary-excluded': 787}
- included module counts: {'B3_POLITICS_RULE_OF_LAW': 197, 'B2_ECONOMICS': 226, 'B4_CULTURE': 149}
- row granularity counts: {'suite': 3, 'question': 1243, 'subquestion': 64, 'culture_component': 27, 'target_component': 28}
- blocked rows: 0
- duplicate `(suite_id, question)` keys: 0

## User Rule Applied

- 海淀期末第 17 题题面与细则中的红色文化、民族精神、发展中国特色社会主义文化抽为 B4_CULTURE 组件。
- 海淀期末第 18、19 题细则中的社会主义核心价值观/诚信价值点抽为 B4_CULTURE 组件。
- 父题的法律、哲学、选必三等余项保留边界排除，不用组件行冒充整题归属。

## Deliverables

- `05_reports/haidian_2026_identity_ocr_culture_patch_audit.csv`
- `04_module_classification/haidian_2026_identity_ocr_culture_patched_classification_matrix.csv`
- `00_control/HAIDIAN_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`
- `05_reports/haidian_2026_identity_ocr_culture_patch_blocked_queue.csv`
