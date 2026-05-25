# Thickness Repair Priority Queue 20260525

Updated: 2026-05-26 02:05 +08

Status: `THICKNESS_REPAIR_PRIORITY_QUEUE_CREATED_REPAIR_NOT_DONE`

- Source audit: `THICKNESS_DENSITY_AUDIT_20260525.csv`.
- Total density-audit entries: `721`.
- Thin candidates queued: `442`.
- Queue CSV: `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.csv`.
- JSON summary: `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.json`.

## Priority Counts

- `P1`: `210`
- `P2`: `207`
- `P3`: `25`

## Group Counts

- `legacy`: `232`
- `inserted`: `210`

## Question Kind Counts

- `subjective`: `314`
- `choice`: `128`

## Flag Counts

- `SHORT_WITHOUT_POINT_MARKERS`: `373`
- `ANSWER_LT_120_CHARS`: `277`
- `WHY_LT_90_CHARS`: `75`

## Repair Rule

- P0: subjective triple-thin rows: short answer, short reasoning, and no point markers.
- P1: inserted rows with any density flag, because new additions must match legacy thickness.
- P2: remaining subjective rows with density flags.
- P3: choice-chain rows with density flags; keep them as objective-key chains.

## Boundary

- This queue is a worklist, not a completed thickness repair.
- It does not close the GPTPro/Claude thickness gate.
- It should be used to drive the next semantic rewrite pass before any external acceptance retry.
