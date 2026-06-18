# 2026 朝阳期中/期末身份与 OCR 文化补丁报告

## Scope

- removed contaminated `2026_朝阳_期末` live rows: 22
- rebuilt/split `2026_朝阳_期中` matrix rows from contaminated suite: 22
- rebuilt actual `2026_朝阳_期末` rows: 28
- added actual 2026 朝阳期末 parent/subquestion rows: 22
- added actual 2026 朝阳期末 target/culture components: 6
- full OCR paper text: `02_text_cache/ocr_cache/2026_朝阳_期末_试卷/试卷.ocr.txt`
- full OCR rubric text: `02_text_cache/ocr_cache/2026_朝阳_期末_细则/细则.ocr.txt`

## Source Identity Repairs

{
  "source_inventory.csv:2025_海淀_期末->2025_海淀_期中": 4,
  "source_inventory.csv:2026_朝阳_期末->2026_朝阳_期中": 6,
  "SOURCE_LEDGER.csv:2025_海淀_期末->2025_海淀_期中": 4,
  "SOURCE_LEDGER.csv:2026_朝阳_期末->2026_朝阳_期中": 6,
  "question_candidates.csv:2025_海淀_期末->2025_海淀_期中": 37,
  "question_candidates.csv:2026_朝阳_期末->2026_朝阳_期中": 37,
  "cache_manifest.csv:2025_海淀_期末->2025_海淀_期中": 2,
  "cache_manifest.csv:2026_朝阳_期末->2026_朝阳_期中": 2,
  "cache_manifest:chaoyang_final_paper_ocr_repaired": 1,
  "cache_manifest:chaoyang_final_rubric_ocr_repaired": 1,
  "question_candidates:chaoyang_final_paper_rows_added": 22,
  "question_candidates:chaoyang_final_rubric_rows_added": 7,
  "question_candidates:rows_before": 3186,
  "question_candidates:rows_after": 3215
}

## Matrix Counts

- rows: 1393
- status counts: {'reference-only': 6, 'included': 586, 'module-boundary-excluded': 801}
- included module counts: {'B3_POLITICS_RULE_OF_LAW': 202, 'B2_ECONOMICS': 231, 'B4_CULTURE': 153}
- row granularity counts: {'suite': 3, 'question': 1265, 'subquestion': 64, 'culture_component': 30, 'target_component': 31}
- blocked rows: 0
- duplicate `(suite_id, question)` keys: 0

## User Rule Applied

- 题目中的中华优秀传统文化滋养、中华法律文化精华、文化根基被抽为 B4_CULTURE 组件。
- 第16题细则中的中华优秀传统文化、文化自信、民族文化认同感、创造性转化和创新性发展被抽为 B4_CULTURE 组件。
- 第21题综合题不整题归入 B2/B3；只抽社会主义市场经济、市场/产业/人才优势为 B2 组件，抽党的全面领导、以人民为中心为 B3 组件。
- 父题余项继续按哲学、必修一、选必一、选必二、选必三边界关闭。

## Deliverables

- `05_reports/chaoyang_2026_identity_ocr_culture_patch_audit.csv`
- `04_module_classification/chaoyang_2026_identity_ocr_culture_patched_classification_matrix.csv`
- `00_control/CHAOYANG_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`
- `05_reports/chaoyang_2026_identity_ocr_culture_patch_blocked_queue.csv`
