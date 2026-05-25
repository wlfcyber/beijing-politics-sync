# ClaudeCode full source-vs-DOCX coverage audit prompt

You are ClaudeCode production lane B. This is a scoped coverage audit, not a rewrite.

User concern:
- When adding 2026 second-mock questions, also check whether the accepted philosophy handbook really covered the 2024-2026 first-mock papers.
- The final artifact should be the accepted old handbook plus new papers, with no obvious source suite omitted.
- The user also worries that only a few repeated questions appear, so suite-level omission must be checked independently.

Read:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/COVERAGE_CLOSURE_MATRIX_V2.csv`
- latest DOCX/PDF under `05_delivery/`

You may also independently inspect these Desktop folders:
- `C:\Users\Administrator\Desktop\2024各区模拟题`
- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`

Audit questions:
1. Does the current Desktop source inventory contain exactly 47 recognizable 2024-2026 first/second mock suite names?
2. Does the final DOCX mention every one of those 47 suite names at least once?
3. Does the report correctly distinguish current-delta closure (`35`) from inherited base coverage (`12`)?
4. Are any of the 2026 second-mock suites missing from the DOCX or current closure matrix?
5. Are any 2024-2026 first-mock suites missing from the DOCX or current closure matrix?
6. If a suite is only inherited base coverage, state that this is suite-name coverage, not fresh row-level re-scoring.

Write:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_full_source_docx_coverage_audit_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_full_source_docx_coverage_findings_20260524.jsonl`

JSONL schema:
`{"verdict":"SCOPED_PASS|REWRITE|NEED_EVIDENCE|MISSING","suite":"","reason":"","required_action":""}`

Do not issue full final all-model PASS. GPTPro web review remains pending.
