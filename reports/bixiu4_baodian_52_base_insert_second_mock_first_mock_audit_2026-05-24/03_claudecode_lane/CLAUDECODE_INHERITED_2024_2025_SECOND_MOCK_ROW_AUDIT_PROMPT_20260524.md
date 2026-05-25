# ClaudeCode inherited 2024/2025 second-mock row audit prompt

You are ClaudeCode production lane B. This is not a ceremonial review.

Current situation:
- The final handbook already mentions all 47 source suites from Desktop 2024-2026 first/second mock folders.
- The current delta closure matrix explicitly closed 35 suites: all 2024-2026 first mocks + all 2026 second mocks.
- The remaining 12 suites are 2024/2025 second mocks inherited from the accepted base handbook. Codex extracted 135 final-handbook rows for these 12 suites.
- The user worries the handbook may only repeat a few questions and may omit many philosophy questions.

Your task:
Audit these inherited 12 second-mock suites at row level enough to decide whether there is an obvious missing philosophy-question problem or serious row weakness.

Read first:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/INHERITED_2024_2025_SECOND_MOCK_ROW_EXTRACT_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/INHERITED_2024_2025_SECOND_MOCK_ROW_EXTRACT_20260524.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv`
- final DOCX/PDF under `05_delivery/`

Inspect source files as needed under:
- `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区二模`
- `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区二模`

Audit questions:
1. For each of the 12 inherited suites, do the extracted handbook rows cover the obvious philosophy main questions from that suite?
2. Are any obvious philosophy main questions missing from the handbook row extract? If yes, list suite, question number, source file, and likely principle node.
3. Are any inherited rows seriously misplaced under the wrong principle node?
4. Are the 36 weak/missing-field rows mostly choice-question formatting artifacts, or do any student-facing rows need rewrite?
5. Does this inherited-row audit change the previous coverage boundary? That is, can the 12 remain "base covered, not reopened", or do any require immediate patch before the final handbook is safe?

Output files:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_inherited_2024_2025_second_mock_row_audit_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_inherited_2024_2025_second_mock_findings_20260524.jsonl`

JSONL schema:
`{"verdict":"SCOPED_PASS|ADD|REWRITE|DELETE|NEED_EVIDENCE","suite":"","question_no":"","principle_node":"","reason":"","source_checked":"","required_action":""}`

Rules:
- Do not invent source content. If a file cannot be read or a rubric is not available, say NEED_EVIDENCE.
- Ordinary reference answer is not a rubric unless the file is clearly a rubric/scoring/marking/lecture source.
- Distinguish choice-question row-format artifacts from real main-question weaknesses.
- Do not issue full final all-model PASS; GPTPro web remains pending.
