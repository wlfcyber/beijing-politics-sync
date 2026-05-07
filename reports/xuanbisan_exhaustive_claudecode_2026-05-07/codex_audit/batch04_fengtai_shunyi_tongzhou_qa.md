# Batch QA - batch04_fengtai_shunyi_tongzhou

Verdict: `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL`

## Hard failures

- none

## Required files

- missing: none
- suite_reports: 5
- entries jsonl: 1
- acceptance files: 1

## QUESTION_DECISIONS.csv

- data rows: 98
- bad width rows: 0
- decision counts: {'excluded': 66, '入正文': 26, '同类索引': 5, 'blocked': 1}
- invalid needs_codex_recheck rows: 0

## JSONL

- `claudecode_lane\batches\batch04_fengtai_shunyi_tongzhou\entries\batch04_entries.jsonl`: rows=36, bad_json=0, missing_required=0, invalid_evidence_level=0, types={'main_thinking': 17, 'choice_trap': 19}

## Forbidden Phrase Hits

- none

## Note

- `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` only means the batch is structurally usable as fusion input; it never authorizes final Word/PDF.