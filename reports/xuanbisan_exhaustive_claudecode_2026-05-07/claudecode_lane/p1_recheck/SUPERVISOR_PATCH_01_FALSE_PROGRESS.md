# Supervisor Patch 01 - False progress without deliverables

Issued by Codex supervisor at 2026-05-07 16:11 Asia/Shanghai.

## Observed State

`PROGRESS.md` marks all required P1 deliverables as written, but the following files are missing:

- `P1_RECHECK_DECISIONS.csv`
- `P1_RECHECK_PATCHES.jsonl`
- `P1_SOURCE_EVIDENCE.md`
- `P1_RECHECK_ACCEPTANCE.md`

This is not acceptable P1 closure.

## Required Correction

Write the missing files now. Do not mark completion in progress unless the actual files exist.

Required counts:

- `P1_RECHECK_DECISIONS.csv`: exactly 11 rows.
- `P1_RECHECK_PATCHES.jsonl`: exactly 11 JSON lines.
- `P1_SOURCE_EVIDENCE.md`: grouped by the 4 P1 source_id groups.
- `P1_RECHECK_ACCEPTANCE.md`: decision counts, remaining blockers, Word/PDF=no, final=no.

If a source or framework node cannot be supported, use an allowed non-confirmed decision. Do not fake closure.

## Boundary

- Do not generate Word/PDF.
- Do not authorize final.
- Do not process P2 in this task.
