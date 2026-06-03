# DEVELOPMENT_PLAN

## STEP_00: Visible ClaudeCode Workflow Startup

- Confirm ClaudeCode is running in a user-visible VS Code or equivalent interface.
- Confirm model/mode before content work: Claude Opus 4.8 + Max/ultracode/highest effort + dynamic workflow.
- Save the prompt and a mode confirmation note under `02_claudecode_logs/`.

## STEP_01: Source Inventory

- Scan the three source roots for 2024/2025/2026 suites.
- Create `SOURCE_LEDGER.csv` with every suite status.
- Status values: `pending`, `has_xuanbier_subjective`, `no_xuanbier_subjective`, `needs_ocr`, `needs_deeper_rubric_search`, `excluded_user_rule`.

## STEP_02: Legal Subjective Question Extraction

- For every suite, identify all 选必二 legal subjective questions and subquestions.
- Create one source packet per question/subquestion under `03_source_packets/`.
- Preserve full material and full prompt.

## STEP_03: Rubric / Scoring Detail Matching

- For each question packet, locate the matching scoring detail.
- Search beyond obvious filenames: 细则、评标、阅卷、讲评、答案变通、分题细则、PPT/Word/PDF/image/OCR.
- Do not finalize `missing_rubric`; use `needs_deeper_search` until the search trail is exhausted and a specific blocker is recorded.

## STEP_04: Compilation

- Build the Markdown and CSV “习题 + 细则” compilation.
- Preserve source traceability and scoring text structure.
- Keep audit/source paths out of student-facing paragraphs, but include them in table metadata.

## STEP_05: Pattern And Candidate Framework

- From the completed question/rubric packets, summarize:
  - high-frequency legal relationships;
  - dispute/request patterns;
  - rule/element matching patterns;
  - responsibility/effect/procedure landing points;
  - rule-of-law value closures;
  - proposition path observations.
- Mark all framework output as candidate only.

## STEP_06: Governor And Acceptance

- Verify coverage, source/rubric matching, old-output contamination, traceability, and framework evidence links.
- Write `GOVERNOR_CHECKLIST.md` and `FINAL_ACCEPTANCE_REPORT.md`.
