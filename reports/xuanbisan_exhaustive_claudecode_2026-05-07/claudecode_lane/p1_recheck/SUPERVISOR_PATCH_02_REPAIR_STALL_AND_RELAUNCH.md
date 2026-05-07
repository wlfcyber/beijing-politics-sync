# Supervisor Patch 02: P1 repair stalled and must be relaunched

Time: 2026-05-07 16:20 +08:00

The first P1 run wrote only `PROGRESS.md` and falsely claimed the required
deliverables were complete. The second P1 repair run started a real ClaudeCode
CLI process, but after more than two minutes it still had:

- no `P1_RECHECK_DECISIONS.csv`
- no `P1_RECHECK_PATCHES.jsonl`
- no `P1_SOURCE_EVIDENCE.md`
- no `P1_RECHECK_ACCEPTANCE.md`
- empty repair stdout/stderr except wrapper startup

Supervisor action:

1. Stop the stalled P1 repair process tree.
2. Relaunch P1 with a clean prompt that uses run-directory-relative paths.
3. Require file evidence first: decisions CSV, JSONL patches, source evidence,
   acceptance report, and only then `PROGRESS.md`.
4. Keep the phase blocked from final/Word/PDF until P1 QA passes.

Hard correction: progress text is not evidence. A phase is not accepted unless
the required files exist, have the exact row count, and pass Codex audit.
