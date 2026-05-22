# Framework v1 Pass Report

## Counts

- Total: 65
- PASS: 16
- PARTIAL: 49
- FAIL: 0
- Evidence levels: formal 61, reference_only 4, missing 0

## Method

Entry matching used only the question layer:题干、设问、材料、材料原子、设问原子. It did not use answer_text or rubric_text to decide the framework entry.

## Interpretation

`framework_v1` is conservative and intentionally not final. It closes only direct codebook-supported rows. It can start transfer rows, but those rows are not full-score closures until their rubric atoms support a new or expanded codebook observation.

## Gate Decision

- Final framework allowed now: NO.
- Final baodian allowed now: NO.
- Next allowed step: source-check PARTIAL/FAIL clusters and decide whether to launch another codebook-expansion model round or revise v1 into v2 after evidence-backed patches.

## Status Breakdown

- Direct PASS rows: 16
- Non-core PARTIAL rows: 49
- Hard FAIL rows: 0

## Entry Type Counts

- DIRECT_HIT: 16
- TRANSFER_TEST: 45
- REFERENCE_ONLY: 4
