You are ClaudeCode lane B reviewing a narrow patch to an already accepted Beijing politics philosophy handbook.

Do not write files. Print the report to stdout only.

Read:
- 04_fusion/fused_entries_2026_second_mock.json
- 04_fusion/evidence_ledger_2026_second_mock.csv
- 01_source_texts/*.txt as needed

Review goal:
- Check whether any inserted entry appears unsupported by the local source texts.
- Check whether any high-risk term is unsupported: dialectical negation, quantitative/qualitative change, primary/secondary contradiction, primary/secondary aspect, two-point/key-point theory, mainstream/tributary, value-guidance.
- Check whether the eight 2026 second-mock suites have at least some philosophy insertion or a recorded boundary.
- Do not rebuild or rewrite the document.

Return Markdown with:

## Verdict
PASS / PASS_WITH_BOUNDARY / FAIL.

## Must Fix
List exact entry source + section + reason. If none, write None.

## Boundary Notes
List weak-evidence boundaries that should be disclosed.

## Missing Candidates
List likely missing philosophy candidates, if any.

Keep the report concise.
