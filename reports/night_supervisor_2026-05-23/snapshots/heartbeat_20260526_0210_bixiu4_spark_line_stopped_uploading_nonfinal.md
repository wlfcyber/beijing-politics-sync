# Heartbeat Snapshot - 2026-05-26 02:10 +08

Status: `BIXIU4_SPARK_LINE_STOPPED_UPLOAD_NONFINAL`

## User Override

The user ordered the migrated Bixiu4 sub-thread stopped because it was not running under the required `5.5 xhigh` model/effort.

## Model Finding

The active migrated Bixiu4 recovery session:

`C:\Users\Administrator\.codex\sessions\2026\05\24\rollout-2026-05-24T22-56-45-019e5a7d-0e79-7643-a03d-2e7614d2acec.jsonl`

contains recent token-count records showing:

- `limit_id`: `codex_bengalfox`
- `limit_name`: `GPT-5.3-Codex-Spark`
- `model_context_window`: `258400`

Therefore it does not satisfy the requested `5.5 xhigh` condition.

## Stop Action

- Wrote `reports/bixiu4_thread_recovery_opus47_2026-05-24/STOP_DO_NOT_CONTINUE_SPARK_LINE_20260526.md`.
- Wrote `patch_orders/ORDER_069_STOP_BIXIU4_SPARK_LINE_UPLOAD_NONFINAL_ARCHIVE_20260526.md`.
- Stopped the likely migrated-thread process group:
  - `codex.exe` PID `23236`
  - `node_repl.exe` PID `37092`
- The target session was observed writing again after the first stop. A rehydrated process group was then stopped at 2026-05-26 02:21 +08:
  - `codex.exe` PID `11888`
  - `node_repl.exe` PID `9448`

Boundary: this is best-effort process stopping from the supervisor thread. If Codex Desktop rehydrates the target thread into another app-server, the stop marker remains authoritative and the line must not continue production.

## Upload Direction

The user ordered GitHub upload from this non-5.5xhigh point. Upload is now allowed only as a non-final archive:

- do not call it `STRICT_FINAL_ACCEPTED`;
- do not call it a qualified 5.5 xhigh result;
- upload selected artifacts, logs, matrices, final current DOCX/PDF, and governance files;
- exclude raw `.codex/sessions/*.jsonl`, rendered page PNG bulk, pycache, backups, and obvious bulky intermediate render folders.

## Current Bixiu4 Boundary At Stop

Latest visible local status before stop:

- P0 cleared earlier.
- Batch20 completed; Batch21 artifacts and refreshed queue appeared.
- Latest queue summary at `2026-05-26 02:05 +08`:
  - queued thin candidates: `442`
  - P1: `210`
  - P2: `207`
  - P3: `25`
- Latest render QA visible:
  - PDF pages: `309`
  - rendered PNG count: `309`
  - DOCX/PDF label counts: `2891/2891`
  - blank-like body pages: `0`
- Open gates:
  - current-version GPTPro full-artifact review pending;
  - current-version Claude Opus full-artifact review pending;
  - model gate blocked because the thread shows Spark, not 5.5 xhigh;
  - not strict final.
