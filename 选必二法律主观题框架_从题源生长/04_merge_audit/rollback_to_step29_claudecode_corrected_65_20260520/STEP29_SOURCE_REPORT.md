# Suite Exhaustive Corpus — ClaudeCode Corrected 2026-05-19

Generated at: 2026-05-19T16:02:13.322879+08:00

This corpus supersedes `suite_exhaustive_20260519` for downstream reasoner packets.

## Corrections Applied

- Added `RECOVER_2026_朝阳_期末_18_1` from ClaudeCode missed-core audit; evidence level formal; source recovered from rendered pages F0213/F0392 and F0212/F0393.
- Removed from core and moved to boundary audit:
  - `CC0051_2024_海淀_期中_21_1`
  - `RECOVER_2024_顺义_二模_17`
- Split `CC0311_2026_海淀_二模_18` into core-only `CC0311_2026_海淀_二模_18_2`; logic subquestion removed from core.
- Corrected seven mislabeled 2026 term rows from `期中` to `期末`.
- Split true 2026 朝阳期中 / 朝阳期末 and true 2026 海淀期中 / 海淀期末 in the suite matrix.
- Preserved OCR/source blockers as audit risks; OCR-recovered entries are tagged in notes/uncertainty fields.

## Counts

- Core questions: 65
- Evidence levels: {'formal': 61, 'reference_only': 4}
- Material atoms: 541
- Ask atoms: 65
- Rubric atoms: 362
- Removed from core: 2
- Boundary/blocked cases: 9

## Current Downstream Gate

This corrected corpus may be used to rebuild reasoner packets. GPT-5.5 Pro / Claude Opus outputs created from older 53/56/66-row packets remain superseded.

Remaining blocker before final framework: OCR/source blockers in ClaudeCode audit should remain visible, especially 2026 丰台期末 mixed case and 2026 西城期末 formal rubric OCR.
