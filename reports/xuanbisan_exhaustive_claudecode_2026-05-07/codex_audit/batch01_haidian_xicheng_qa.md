# Batch QA - batch01_haidian_xicheng

Verdict: `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL`

## Hard failures

- none

## Required files

- missing: none
- suite_reports: 5
- entries jsonl: 1
- acceptance files: 1

## QUESTION_DECISIONS.csv

- data rows: 101
- bad width rows: 0
- decision counts: {'excluded': 78, '入正文': 21, 'blocked': 1, '同类索引': 1}
- invalid needs_codex_recheck rows: 0

## JSONL

- `claudecode_lane\batches\batch01_haidian_xicheng\entries\batch01_entries.jsonl`: rows=31, bad_json=0, missing_required=0, invalid_evidence_level=0, types={'main_thinking': 20, 'choice_trap': 11}

## Forbidden Phrase Hits

- none

## Note

- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF.