# ClaudeCode after-depth audit prompt

You are ClaudeCode production lane B for Feige Politics Garden, not a ceremonial reviewer.

Scope:
- Audit the Codex lane's latest depth-expanded philosophy handbook patch.
- The user's base is the accepted 5.2 philosophy handbook. Do not rebuild the handbook.
- Check only the delta: 2026 second-mock additions and 2024-2026 first-mock missing-item coverage patches.
- The goal at this stage is "ready for audit", not final PASS.

Must read:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/COVERAGE_CLOSURE_MATRIX_V2.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/06_governor_confucius/CURRENT_ACCEPTANCE_STATUS_20260524.md`
- The latest generated Word/PDF under `05_delivery/` if needed.

Audit questions:
1. Does each accepted row have enough student-facing thickness comparable to the old handbook: material signal -> question -> why this principle -> answer landing?
2. Did Codex place any row under a wrong principle node, especially major contradiction/minor contradiction, primary/secondary aspects of contradiction, two-point theory/key-point theory, value judgment/value choice, system optimization, development view, practice, and relation view?
3. Do 2026 second-mock rows look obviously thinner than old entries? If yes, name rows and rewrite them.
4. Are 2024-2026 first-mock philosophy main questions fully covered or explicitly boundary-excluded? Do not accept vague coverage.
5. Are there any fake rubric claims, unsupported "can answer from..." claims, source-path/debug words, English audit labels, or teacher-only meta language inside student-facing fields?
6. Do the three earlier rewrite rows remain fixed:
   - 2026 Fengtai second mock Q16 question prompt must be the wetland prompt.
   - 2025 Haidian first mock Q22 system view must not contain teacher/meta tail.
   - 2025 Haidian first mock Q22 major/minor contradiction must not use bracketed option-note language.

Output files to write:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_after_depth_final_audit_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_after_depth_final_findings_20260524.jsonl`

JSONL schema, one finding per line:
`{"row_id":"","suite":"","question_no":"","principle_node":"","verdict":"KEEP|REWRITE|DELETE|NEED_EVIDENCE","reason":"","required_action":"","student_rewrite":{"material_trigger":"","why_trigger":"","answer_landing":""}}`

If there are no findings, still write one JSONL line:
`{"verdict":"KEEP","reason":"No blocking findings in scoped after-depth audit."}`

Do not mark final PASS if GPTPro web review has not run. You may say "ClaudeCode scoped PASS" only if your own lane sees no blocking findings.
