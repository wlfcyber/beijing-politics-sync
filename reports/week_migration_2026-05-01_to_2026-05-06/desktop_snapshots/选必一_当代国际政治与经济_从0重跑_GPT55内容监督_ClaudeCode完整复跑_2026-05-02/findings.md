# Findings

Record source discoveries here, especially after PDF/image/browser/OCR/visual reads.

## Source Findings
# Findings

## 2026-05-02 Setup Findings

- Latest orchestrator skill requires GPT-5.5 Pro content review at fixed trigger objects: `outline`, `section_batch`, `final_markdown`, and `word_pdf`.
- Latest control-file rules require `content_correction_log.md` to include local evidence check result and verified-closed status; raw GPT review alone does not close G11.
- Primary source roots exist for 2024, 2025, and 2026 mock-paper collections.
- Previous run folder contains a student final Markdown and delivery/audit files; it is preserved as reference only and cannot be used as evidence.
- Initial source inventory found 177 files from primary roots: 98 P0 candidate scoring files, 2 P1 candidate reference-answer files, 7 P2 candidate teaching/lecture files, 61 P3 candidate paper files, and 9 unknown.
- Suite grouping produced 55 suite-like groups. Two groups need manual classification because file-level metadata did not identify district/stage cleanly.
- ClaudeCode lane has created `progress.md`, `source_inventory.csv`, `coverage_matrix.csv`, `missing_blockers.md`, and `conflicts_for_codex.md`, and is actively processing must-check items.
- 2026通州期末 Q20 current-run evidence: paper PDF gives the full prompt and material; scoring PPTX slide 14 gives answer layer and slide 15 gives six-point scoring rubric. Paper prompt lacks the extra comma before `彰显担当` that appears in PPTX prompt text, so Codex uses the paper prompt for `完整设问` and PPTX for scoring positions.
