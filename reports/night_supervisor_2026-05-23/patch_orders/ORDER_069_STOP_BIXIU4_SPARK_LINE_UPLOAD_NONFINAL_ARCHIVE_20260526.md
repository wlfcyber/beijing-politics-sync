# ORDER_069 - Stop Bixiu4 Spark Line And Upload Nonfinal Archive

Timestamp: 2026-05-26 02:10 +08

Status: `USER_STOPPED_SPARK_LINE_UPLOAD_ARCHIVE`

## User Instruction

The user ordered the migrated Bixiu4 sub-thread stopped because it was not running under the required `5.5 xhigh` model/effort.

## Model Evidence

The active Bixiu4 migrated recovery session:

`C:\Users\Administrator\.codex\sessions\2026\05\24\rollout-2026-05-24T22-56-45-019e5a7d-0e79-7643-a03d-2e7614d2acec.jsonl`

contains recent token-count records with:

- `limit_id`: `codex_bengalfox`
- `limit_name`: `GPT-5.3-Codex-Spark`
- `model_context_window`: `258400`

This is not the user's required `5.5 xhigh`.

## Stop Rule

Stop the Bixiu4 Spark recovery line immediately.

- Do not continue Batch22+ or any new semantic repair in this line.
- Do not mark Bixiu4 as `STRICT_FINAL_ACCEPTED`.
- Do not treat Spark-produced content as a qualified final answer.
- Preserve the outputs as a non-final archive/restart base only.

## Upload Rule

The user ordered GitHub upload from this non-5.5xhigh point. Upload is permitted only as a non-final archive with clear caveats.

Required upload scope:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/`
- the relevant night-supervisor stop/upload orders and snapshots
- model-mismatch evidence summary

Do not upload raw `.codex/sessions/*.jsonl` files. They are outside the repo, too large, and may contain process-private context. Instead, upload a summary of the token-count evidence.

Before push:

1. Generate an upload scope report.
2. Run a sensitive-pattern scan over the selected scope.
3. Push only if the report records `NO_SECRET_PATTERN_MATCHES`.
4. Commit message must say this is a non-final Bixiu4 Spark archive, not strict final.
