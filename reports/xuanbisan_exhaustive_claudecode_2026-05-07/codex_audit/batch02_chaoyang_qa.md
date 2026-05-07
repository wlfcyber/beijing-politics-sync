# Batch QA - batch02_chaoyang

Verdict: `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL`

## Hard failures

- none

## Required files

- missing: none
- suite_reports: 4
- entries jsonl: 1
- acceptance files: 1

## QUESTION_DECISIONS.csv

- data rows: 90
- bad width rows: 0
- decision counts: {'excluded': 66, '同类索引': 2, '入正文': 20, 'blocked': 2}
- invalid needs_codex_recheck rows: 0

## JSONL

- `claudecode_lane\batches\batch02_chaoyang\entries\batch02_entries.jsonl`: rows=32, bad_json=0, missing_required=0, types={'main_thinking': 20, 'choice_trap': 12}

## Forbidden Phrase Hits

- none

## Note

- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF.