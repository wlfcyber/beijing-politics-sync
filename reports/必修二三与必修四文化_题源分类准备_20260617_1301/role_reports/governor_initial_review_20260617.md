# Governor Initial Review 2026-06-17

## Findings

- Source-forward inventory exists and no longer relies on document thickness or model summary.
- Duplicate source copies are visible through sha256 and `duplicate-or-drift` status.
- The three target modules have preliminary included rows:
  - B2_ECONOMICS: 162 included rows.
  - B3_POLITICS_RULE_OF_LAW: 141 included rows.
  - B4_CULTURE: 106 included rows.
- Boundary rows are explicit, including B4 philosophy, XB1, XB2, XB3, B1, and 2026 石景山期末 hard-rule exclusion.
- Suite-level OCR blockers are cleared after Apple Vision OCR absorption.
- Two no-stable-suite helper compilations are marked `REFERENCE_HELPER_ONLY` and cannot be used as coverage evidence.
- File-name module hints were removed after detecting legal/logic/international questions being pulled into B2/B4 by path names.
- Classification now uses paper text first and explicit boundary terms before normal scoring.

## Rejection For Final Closure

- 190 rows are `UNKNOWN_OR_MIXED`.
- 45 rows require subquestion-level split.
- 21 suites need question-gap review before any full-coverage claim.
- This run can seed future宝典 work, but it cannot yet certify complete question coverage.

## Decision

blocked for final coverage; pass for preparation handoff.
