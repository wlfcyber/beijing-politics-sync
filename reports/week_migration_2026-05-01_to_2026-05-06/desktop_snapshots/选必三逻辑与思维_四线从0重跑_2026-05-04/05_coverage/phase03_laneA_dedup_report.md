# Phase 03 Lane A Dedup/Split Report

Status: `CLEANUP_DONE_NOT_STUDENT_FACING`.

## Counts

- Input rows: 528
- Canonical paper/question rows: 358
- Support/reference rows split out: 46
- Duplicate/removed rows logged: 170
- Unknown rows treated as paper candidates: 0
- Duplicate suite/question keys in input: 118
- Canonical in-scope or cross candidates: 119
- Canonical locked rows: 2
- Canonical rows with any blocker/status: 358

## Output Files

- Canonical matrix: `05_coverage/phase03_laneA_dedup_question_matrix.csv`
- Support evidence matrix: `05_coverage/phase03_laneA_support_evidence_matrix.csv`
- Removed/reference log: `05_coverage/phase03_laneA_duplicate_or_reference_rows.csv`

## Gate Meaning

- This pass separates original paper/question rows from answer/rubric/reference rows.
- It does not resolve missing answers, choice options, or module boundary disputes.
- It does not unlock HS02 or 2026丰台一模 Q18(2); those still need the focused Lane B patch.
- Student稿、Claude Opus 成文化、Word/PDF、最终 PASS remain blocked.
