# Conflicts / Notes For Codex

RUN ID: xuanbiyi_zero_gpt55_claudecode_2026-05-02

This file records scoring-term disagreements, module-boundary calls, and evidence-level differences between ClaudeCode lane and expected Codex lane outputs.

## Module Boundary Notes

(Updated as encountered)

## Term Disagreements

(Updated as encountered)

## Evidence Level Differences

(Updated as encountered)

### 2025海淀期中

- ClaudeCode restart matrix currently marks `2025海淀期中_细则` as `P1_reference_answer` and says image/table formal scoring material was not found.
- Codex has extracted the embedded DOCX media and located:
  - `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image2.png`
  - `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image8.png`
- Codex decision: treat `SRC_cda046c2d36d` as `P0_verified_rubric` for Q16(2)/Q21(2) unless later source inspection disproves the images.
- ClaudeCode should recheck DOCX embedded media, not just text extraction.
