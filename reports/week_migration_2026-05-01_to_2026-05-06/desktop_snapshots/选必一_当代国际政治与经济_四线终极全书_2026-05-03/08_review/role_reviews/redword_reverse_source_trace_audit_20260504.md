# Redword Reverse Source Trace Audit

time: 2026-05-04 21:33 CST
verdict: `PASS`

## Scope

- Checks every red span inside `按题训练闭环` against that question's `red_scoring_terms` in `all_question_rubric_point_repair_matrix_20260504.csv`.
- Separately rejects red spans in framework-only contexts such as `本题命中框架`, `框架落点`, and numbered `框架归类` headings.
- Red spans in the front six-bucket index and six-bucket review are counted as framework-level red terms, not question-specific redwords.

## Counts

- total red spans in Markdown: 3640
- question-loop red spans audited: 3182
- framework-level red spans outside question-loop: 458
- bad-context red spans: 0
- unsourced question red spans: 0
- suspect rows: 0

## Decision

PASS: no red span in the question loop appears in a framework-only context, and every audited question-loop red span traces back to that question's recorded scoring terms.
