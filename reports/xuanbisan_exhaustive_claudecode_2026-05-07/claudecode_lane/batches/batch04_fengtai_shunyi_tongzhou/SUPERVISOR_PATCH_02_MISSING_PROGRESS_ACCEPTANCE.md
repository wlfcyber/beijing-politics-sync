# Supervisor Patch 02: missing control closure files

Status: `CORE_OUTPUTS_READY_BUT_PROGRESS_ACCEPTANCE_MISSING`

Codex audit at 2026-05-07 14:55 found Batch04 still fails structural QA only because the control closure files are incomplete.

Already present and structurally usable:

- `QUESTION_DECISIONS.csv`: 98 rows, CSV width OK, decisions only `入正文 / 同类索引 / blocked / excluded`.
- `MAIN_THINKING_LEDGER.csv`
- `CHOICE_TRAP_LEDGER.csv`
- `FRAMEWORK_NODE_MATRIX.csv`
- `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
- `entries\batch04_entries.jsonl`: 36 rows, JSON valid, required fields present.
- `suite_reports\*.md`: all 5 suite reports present.
- `BLOCKED_OR_BOUNDARY.md`: present according to the audit script.

Hard missing:

- `PROGRESS.md`
- `BATCH04_ACCEPTANCE.md`

Required correction:

1. Do not rewrite or shrink the existing thick-content ledgers, entries, decision table, framework matrix, or suite reports unless a real content error is found.
2. Write `PROGRESS.md` with a truthful file-evidence based status: candidate count, decision distribution, entry count, suite report count, blocker count, and the statement that this is fusion input only, not final/Word/PDF.
3. Write `BATCH04_ACCEPTANCE.md` with a self-check matching `codex_audit\audit_batch_dir.py`: required files, decision rows, JSONL rows, suite reports, forbidden student-facing phrases, unresolved blockers, and no final artifact authorization.
4. After writing those files, rerun or record the exact QA command:
   `python codex_audit\audit_batch_dir.py claudecode_lane\batches\batch04_fengtai_shunyi_tongzhou`

This patch does not authorize a final manuscript, Word, or PDF.
