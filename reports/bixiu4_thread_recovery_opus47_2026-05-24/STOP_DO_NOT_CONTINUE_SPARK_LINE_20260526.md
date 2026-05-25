# Stop Order - Bixiu4 Spark Line

Timestamp: 2026-05-26 02:10 +08

Second stop check: 2026-05-26 02:21 +08

Status: `STOPPED_BY_USER_MODEL_MISMATCH`

User instruction: stop this migrated Bixiu4 recovery line because the active Codex token ledger shows `GPT-5.3-Codex-Spark`, while the required model/effort is `5.5 xhigh`.

Evidence:

- Session: `C:\Users\Administrator\.codex\sessions\2026\05\24\rollout-2026-05-24T22-56-45-019e5a7d-0e79-7643-a03d-2e7614d2acec.jsonl`
- Recent token-count records show:
  - `limit_id`: `codex_bengalfox`
  - `limit_name`: `GPT-5.3-Codex-Spark`
  - `model_context_window`: `258400`

Boundary:

- Do not continue production work in this line.
- Do not write `STRICT_FINAL_ACCEPTED`.
- Do not represent the artifacts from this line as a qualified 5.5 xhigh result.
- Current artifacts may be uploaded only as non-final process/archive evidence and as a restart base for a future true `5.5 xhigh` rerun.

Process stop record:

- Initial likely process group stopped at 2026-05-26 02:10 +08:
  - `codex.exe` PID `23236`
  - `node_repl.exe` PID `37092`
- The session was later observed writing again, so a rehydrated process group was stopped at 2026-05-26 02:21 +08:
  - `codex.exe` PID `11888`
  - `node_repl.exe` PID `9448`
- This file is the authoritative instruction if the desktop app rehydrates the thread again: the Spark line must not continue production.

Goal-state stop record:

- The target thread still advanced after process kills and wrote a Batch22 attempt locally.
- The Codex goals database was backed up, then the target thread goal was changed from `active` to `paused` at 2026-05-26 02:28 +08.
- Backup: `C:\Users\Administrator\.codex\backups\goals_1_before_pause_bixiu4_spark_20260526_022835.sqlite`
- Target thread id: `019e5a7d-0e79-7643-a03d-2e7614d2acec`
- Post-stop Batch22 local overrun is not qualified final evidence and is not part of the original nonfinal archive commit unless separately archived with explicit caveat.
