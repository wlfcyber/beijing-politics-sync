# Supervisor Review of ClaudeCode Phase 2

## Status

- ClaudeCode produced `claudecode_lane/phase2_source_inventory_report.md`.
- CLI ended with `error_max_budget_usd` after writing the report.
- Treat the report as usable Phase 2 evidence where it names checked files, but do not treat it as complete extraction for all 173 sources.

## Accepted

- SOURCE_LEDGER coverage finding: no missing source roots/suites found in 2024/2025/2026 directories.
- High-priority queue:
  - 2026通州期末 Q20
  - 2026朝阳期中 Q17
  - 2025海淀期中 Q16(2)
  - 2025海淀期中 Q21(2)
  - 2025海淀期末 Q22
  - 2024东城一模 Q16
  - 2024东城一模 Q20
- Exclusions:
  - 2026石景山期末 remains excluded.
  - 2026海淀期末 remains excluded unless new evidence appears.
- Technical warning: embedded DOCX images and image/PPT/PDF visual layers must not be skipped.

## Corrected Or Refined By Codex

- ClaudeCode said `USER_FRAMEWORK.md` and `USER_QUESTIONS.md` were unread; Codex had already written them, and Phase 3 workers must read them.
- 2026石景山期末 PDF text extraction did return answer-reference text with 选必一-like terms, but hard rule still excludes it because it is not usable scoring evidence.
- 2026海淀期末 PDF text extraction returned text but no priority 选必一 hits; keep excluded per user confirmation.
- 2025海淀期中 embedded images were visually read by Codex:
  - `image2.png` and `image3.png` confirm Q16(2) scoring supplement.
  - `image8.png` confirms Q21(2) table-form scoring rules.

## Files Created Or Updated After Review

- `codex_lane/scripts/extract_priority_sources.py`
- `codex_lane/priority_source_extract_report.md`
- `codex_lane/extracted_text/`
- `codex_lane/extracted_media/SRC_cda046c2d36d/`
- `audit/haidian_midterm_docx_media_contact_sheet.png`
- `audit/visual_read_2025海淀期中_media.md`
- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`
