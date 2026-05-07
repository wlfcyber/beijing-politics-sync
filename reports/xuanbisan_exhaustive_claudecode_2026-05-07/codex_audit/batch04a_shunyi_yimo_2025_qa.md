# Batch QA - batch04a_shunyi_yimo_2025

Verdict: `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL`

## Hard failures

- none

## Required files

- missing: none
- suite_reports: 1
- entries jsonl: 1
- acceptance files: 1

## QUESTION_DECISIONS.csv

- data rows: 23
- bad width rows: 0
- decision counts: {'excluded': 18, '同类索引': 1, '入正文': 4}
- invalid needs_codex_recheck rows: 0

## JSONL

- `claudecode_lane\batches\batch04a_shunyi_yimo_2025\entries\batch04a_entries.jsonl`: rows=5, bad_json=0, missing_required=0, types={'选择题-边界陷阱': 1, '选择题-推理形式辨析': 1, '选择题-概念与判断综合': 1, '选择题-三段论谬误辨析': 1, '主观题-复合判断演绎推理': 1}

## Forbidden Phrase Hits

- none

## Note

- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF.