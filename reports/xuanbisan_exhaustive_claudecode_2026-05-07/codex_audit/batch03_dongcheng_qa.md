# Batch QA - batch03_dongcheng

Verdict: `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL`

## Hard failures

- none

## Required files

- missing: none
- suite_reports: 3
- entries jsonl: 1
- acceptance files: 1

## QUESTION_DECISIONS.csv

- data rows: 72
- bad width rows: 0
- decision counts: {'excluded': 57, '入正文': 12, '同类索引': 3}
- invalid needs_codex_recheck rows: 0

## JSONL

- `claudecode_lane\batches\batch03_dongcheng\entries\batch03_entries.jsonl`: rows=20, bad_json=0, missing_required=0, invalid_evidence_level=0, types={'main_thinking': 11, 'choice_trap': 9}

## Forbidden Phrase Hits

- none

## Note

- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF.