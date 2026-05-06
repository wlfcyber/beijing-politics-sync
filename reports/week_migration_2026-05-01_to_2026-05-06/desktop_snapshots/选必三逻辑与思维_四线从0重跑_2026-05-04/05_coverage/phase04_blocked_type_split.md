# Phase04 Blocked Type Split

Status: `BATCH02_CONTROL_SPLIT_READY`.

## Counts

- PENDING_SCOPE: 139
- A_ONLY_PENDING_B: 114
- OUT_OF_SCOPE_OR_BOUNDARY: 50
- OPTIONS_MISSING: 31
- ANSWER_SOURCE_MISSING: 14
- LOCKED_FOR_FUSION: 4
- VISUAL_BLOCKED: 3
- CONFIRMED_NOT_LOCKED: 3

## Notes

- This split is heuristic and conservative; Lane B must recheck P0 visual/answer/scope rows.
- It exists to prevent `L0_BLOCKED=236` from hiding out-of-scope, duplicate, support, and true blocker rows in one bucket.
