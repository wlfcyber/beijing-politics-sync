# Batch QA - batch02_chaoyang_controlled_input

Verdict: `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL`

## Hard failures

- none

## Required files

- missing: none
- suite_reports: 4
- entries jsonl: 1
- acceptance files: 1

## QUESTION_DECISIONS.csv

- data rows: 93
- bad width rows: 0
- decision counts: {'excluded': 69, '同类索引': 2, '入正文': 20, 'blocked': 2}
- invalid needs_codex_recheck rows: 0

## JSONL

- `fusion\batch02_chaoyang_controlled_input\entries\batch02_entries.jsonl`: rows=32, bad_json=0, missing_required=0, invalid_evidence_level=0, types={'main_thinking': 20, 'choice_trap': 12}

## Forbidden Phrase Hits

- none

## Note

- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF.