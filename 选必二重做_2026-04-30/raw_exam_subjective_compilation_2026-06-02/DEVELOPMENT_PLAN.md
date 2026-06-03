# DEVELOPMENT_PLAN

## Minimal-Step Plan

1. Control repair: create run controls, ledgers, and output paths for this clean rerun.
2. Inventory: recursively scan Desktop for 2024-2026 candidate exam, answer, rubric, marking, lecture, and OCR files; exclude old compiled artifacts.
3. Text extraction: convert readable DOCX/PDF/TXT/PPTX files to plain text, marking scan/OCR gaps explicitly.
4. Suite grouping: group question papers with corresponding answer/rubric/marking files by year, district/exam, and paper type.
5. Serial extraction: process one suite at a time; identify legal subjective subquestions and copy material/prompt/rubric text verbatim.
6. Incremental draft: after each suite, append/update source packet, coverage row, progress row, and the working Markdown.
7. Second pass: rescan inventory and extracted text for legal keywords and unmatched rubrics to find missed legal subjective questions.
8. Final assembly: regenerate coverage table, ordered entries, total count, pending-confirmation list, governor note, and acceptance note.

## Evidence Rules

- Old compilation outputs are forbidden as evidence and must not be opened for content.
- Reference answers are allowed only when no independent scoring rubric is available, and must be marked.
- If a file cannot be read or OCR is needed, status must be blocked_conversion until OCR succeeds.
- If module attribution is uncertain, include the item as 【待确认】 rather than dropping it.

## Current Step

STEP-01-control-repair, then STEP-02-inventory.
