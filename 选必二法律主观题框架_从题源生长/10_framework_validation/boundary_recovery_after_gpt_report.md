# Boundary Recovery After GPT Review Report

- generated_at: 2026-05-19T14:30:00+08:00
- official GPT review: `10_framework_validation/gpt55pro_boundary_recovery_review.md`
- old local delta superseded: `10_framework_validation/framework_v2_boundary_recovery_delta.csv`
- new controlling delta: `10_framework_validation/framework_v2_boundary_recovery_delta_after_gpt.csv`

## Decision

The user's challenge is correct: the earlier 35/37 framing under-counted the legal-question universe because it reported only strict v1 PASS/core closure. After source recovery and GPT review, the count must be reported in layers, not as one number.

## Current Count Policy

- `37`: original v1 strict PASS count.
- `48`: strict closed law core after adding 8 recovered existing formal units, 2 split formal units, and patched CC0229.
- `53`: core + open/reference/formal-boundary units after patched CC0229.
- `CC0229` rubric atoms are patched, and the CC0229 handbook section has been regenerated from patched atoms.
- Pending/tracked units such as CC0094_LAW_PENDING, CC0259_LAW, and CC0118_LAW are not closure counts.

## Required Corrections Before Releasing Revised v2/Handbook

1. Remove `CC0250_2026_丰台_一模_19` from open-container/final body.
2. Change `CC0094_2025_东城_期末_19_3` from open-container to split/deduplicate pending.
3. `CC0229_2026_东城_一模_18` rubric atoms have been patched from F0153/F0146; regenerate the affected final handbook/framework sections before release.
4. Accept only split subquestions for `CC0305_18_3`, `CC0373_18`, and `CC0380_18_2`; do not count parent rows as whole legal questions.
5. Keep all reference_only units as weak/open examples, never core support.

## Status

Existing `framework_v2` and `选必二法律主观题满分宝典` are still provisional until the remaining split/reextract patch queue is completed; CC0229 itself is no longer a blocker.
