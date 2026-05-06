# Codex Phase 02 Hard Samples Report

Date: 2026-05-04

Scope: five hard samples only. No student-facing text produced.

## Outputs

- `02_extraction/extract_phase02_hard_samples.py`
- `05_coverage/phase02_hard_sample_trial_matrix.csv`
- `02_extraction/hard_samples/raw_text/`
- `02_extraction/hard_samples/renders/`
- `02_extraction/hard_samples/visual_fallback_queue.md`
- `03_entries/phase02_hard_sample_entries_internal.md`
- `05_coverage/reasoning_question_attachment_matrix.csv`
- `06_conflicts/phase01_AB_diff.md`

## Results

- HS01 2026 顺义一模 Q19(2): locked pending ClaudeCode cross-check.
- HS02 2025 海淀二模 Q20: rubric locked, paper requires independent visual cross-check.
- HS03 2026 朝阳期中 Q21(2): locked pending ClaudeCode cross-check.
- HS04 2026 通州期末 Q11: full choice stem/options/key locked pending ClaudeCode cross-check.
- HS05 2026 东城期末 Q17(2): formal-logic typology entry locked pending ClaudeCode cross-check.

## Tool Notes

- Missing local tools: `pdftotext`, `pdftoppm`, `soffice`, `tesseract`, `ocrmypdf`, ImageMagick.
- Working fallback tools: PyMuPDF, `python-docx`, `python-pptx`, PIL, `textutil`, `qlmanage`, `sips`.
- Decision: missing external conversion tools are blockers only for particular files after fallback attempts fail; they are not a reason to skip PDF, Word, PPT, image, table, or scanned material.

## Gate Status

- PASS not allowed.
- Student manuscript not allowed.
- Next required lane: ClaudeCode Phase 02 independent hard-sample cross-check.
