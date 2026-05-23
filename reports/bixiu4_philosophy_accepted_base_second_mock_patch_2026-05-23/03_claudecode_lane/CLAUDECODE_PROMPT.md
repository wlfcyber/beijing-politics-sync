You are ClaudeCode lane B for a narrow patch to an already accepted Beijing Gaokao politics philosophy handbook.

Do NOT rebuild the handbook. Do NOT use old v6/v7/v8 artifacts as the base. Your job is only to independently review the 2026 second-mock source texts and find philosophy entries that should be inserted into the accepted base.

Read these files first:
- 00_control/MASTER_REQUIREMENTS.md
- 00_control/SOURCE_LEDGER.csv
- 01_source_texts/*.txt

Scope:
- Eight 2026 second-mock suites already copied into 01_source_texts.
- Include both subjective philosophy questions and objective choice questions when the correct option has a clear philosophy knowledge point.
- Main-question entries require rubric, marking rule, marking PPT, or teacher-confirmed scoring support. Teacher-version reference answers are weaker and must be labeled as such.
- Choice-question entries require the paper question/options plus reliable answer key.
- Do not use "etc." or broad alternative angles to add unsupported principles.
- High-risk terms require explicit source support: dialectical negation, quantitative/qualitative change, primary/secondary contradiction, primary/secondary aspect of contradiction, two-point theory and key-point theory, mainstream/tributary, value-guidance.

Output one Markdown report at 03_claudecode_lane/claudecode_review.md with exactly these sections:

## Coverage Verdict
State whether the eight suites are covered and list source gaps.

## Candidate Entries
For each candidate, use this fixed line format:
`suite_id | question | subjective/objective | proposed_framework_nodes | source_evidence_level | material_signal | rubric_or_answer_signal | include/exclude/need_raw_ocr | reason`

## Likely Missing Entries
List anything Codex should double-check before final insertion.

## Exclusions
List candidates that should not enter the philosophy handbook and why.

## OCR Or Source Gaps
List files/pages where cached text is insufficient and raw rendered pages are needed.

## Governor Risks
List risks that would make a final PASS unsafe.

Prefer English control words if Chinese output encoding is unreliable, but keep exact Chinese knowledge terms when necessary.
