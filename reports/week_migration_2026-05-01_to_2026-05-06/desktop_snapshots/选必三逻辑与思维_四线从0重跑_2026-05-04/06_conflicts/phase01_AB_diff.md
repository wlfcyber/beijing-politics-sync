# Phase 01 A/B Diff - Source Inventory And Gate Review

Status: initial diff after Codex lane A source work, ClaudeCode lane B Phase 01, and GPT-5.5 Pro conditional-go advice.

## Agreement

- Both lanes treat old 选必三 drafts and old outputs as locator-only, not evidence.
- Both lanes found current usable source roots under Desktop 2024/2025/2026 mock-paper folders and the user-uploaded framework PDFs.
- Both lanes agree that no current 2026 二模 source set is available in the scanned roots as of this run.
- Both lanes identify the five hard samples as the right Phase 02 trial set: 2026 顺义一模 Q19(2), 2025 海淀二模 Q20, 2026 朝阳期中 Q21(2), 2026 通州期末 Q11, 2026 东城期末 Q17(2).
- Both lanes agree the reasoning part must be attached as a typology bank, not left as a short abstract summary.

## Differences

- Codex lane A has already extracted the five hard samples into raw text and page renders; ClaudeCode lane B Phase 01 only inventoried and proposed candidates.
- ClaudeCode lane B saw several PPTX/DOC conversion blockers. Codex lane A confirmed the local fallback route: `python-pptx`, `python-docx`, and PyMuPDF extraction/rendering work even though `pdftotext`, `pdftoppm`, `soffice`, and OCR tools are missing.
- Codex lane A found HS02 paper needs visual handling because the PDF text layer contains only 168 chars. ClaudeCode must independently verify that rendered page before HS02 becomes fully locked.
- The top-level `SOURCE_LEDGER.csv` still contains old-artifact locator rows and must be replaced or split before final evidence PASS. This is acceptable only as a temporary inventory artifact, not as final evidence registry.

## GPT-5.5 Pro Gate Result

- Verdict: CONDITIONAL GO.
- Allowed now: source inventory, coverage/diff, reasoning attachment matrix, and limited sample extraction.
- Blocked now: student manuscript, Opus final wording, Word/PDF delivery, final PASS.

## Required Next Closure

- ClaudeCode Phase 02 must independently process the five hard samples and return anchors, classifications, and disagreements.
- Codex must merge A/B differences into `06_conflicts/resolved_conflicts.md` or `06_conflicts/unresolved_conflicts.md`.
- Coverage matrix must stop being header-only and include every locked, suspect, or blocked question.
