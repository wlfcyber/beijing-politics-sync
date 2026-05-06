# Conflict Register

## 2026-05-03 2025海淀期中 Evidence Level

- conflict_id: `C-2025HDQZ-evidence-level`
- source: `2025_海淀_期中`
- Codex finding: `细则.docx` contains 8 embedded images and 7 tables. `image2.png` is Q16(2) scoring detail; `image8.png` is Q21(2) scoring table. Codex marks `SRC_cda046c2d36d` as `P0_verified_rubric`.
- ClaudeCode restart finding: `claudecode_evidence_level_recheck.csv` currently marks `2025海淀期中_细则` as `P1_reference_answer` and says user-confirmed image/table formal scoring material was not found.
- local evidence locator:
  - `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image2.png`
  - `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image8.png`
  - `08_review/phase_reports/hard_sample_review_2025_haidian_midterm_q16_q21.md`
- current decision: Codex evidence wins provisionally because the embedded scoring images were directly extracted from the current-run DOCX. ClaudeCode output must be corrected or treated as stale on this item.
- status: `codex_resolved_pending_claudecode_ack`
