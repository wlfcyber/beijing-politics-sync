# Supervisor Patch 01 - P0 progress-only stall

Issued by Codex supervisor at 2026-05-07 15:44 Asia/Shanghai.

## Observed State

- Real ClaudeCode CLI process is still running.
- Last Claude-authored business file is `PROGRESS.md`.
- Required deliverables are still missing:
  - `P0_RECHECK_DECISIONS.csv`
  - `P0_RECHECK_PATCHES.jsonl`
  - `P0_SOURCE_EVIDENCE.md`
  - `P0_RECHECK_ACCEPTANCE.md`
- Local QA currently fails only because these required files are absent.

## Correction

Do not keep reading without writing. Finish the P0 recheck as auditable rows.

Write the required files in this order:

1. `P0_RECHECK_DECISIONS.csv` with exactly 19 rows.
2. `P0_RECHECK_PATCHES.jsonl` with exactly 19 JSON lines.
3. `P0_SOURCE_EVIDENCE.md`, grouped by source.
4. `P0_RECHECK_ACCEPTANCE.md`, explicitly saying Word/PDF=no and final authorization=no.

If a source cannot support the current framework node, use `source_insufficient`,
`wrong_framework`, `downgrade_to_index`, or `block_from_student_body`. Do not force
a confirmed result.

## Boundary

- Do not generate Word or PDF.
- Do not write final/student delivery.
- Do not start a four-lane final run.
