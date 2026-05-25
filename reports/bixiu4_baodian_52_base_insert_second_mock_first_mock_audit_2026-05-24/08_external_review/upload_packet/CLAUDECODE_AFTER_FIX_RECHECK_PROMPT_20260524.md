# ClaudeCode after-fix recheck prompt

You are ClaudeCode production lane B. Recheck only the blockers you found in `claudecode_after_depth_final_audit_20260524.md`.

Read:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/claudecode_after_depth_fix_applied_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/system_optimization_language_polish_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- latest DOCX/PDF under `05_delivery/` if needed.

Check:
1. Row 26, 2026 Haidian second mock Q16, relation/universal connection: no longer contains system-optimization template language and answer ends in connection-language.
2. Row 36, 2026 Shijingshan second mock Q17(3), relation/universal connection: no longer contains system-optimization template language and answer ends in connection-language.
3. Row 16, 2026 Fengtai second mock Q16, development view: question prompt is exactly the wetland prompt with `《哲学与文化》` and Chinese quotes.
4. The five system-optimization rows no longer use the meta sentence `所以这里触发的是...`.
5. Do not reopen old accepted base-handbook wording unless it is directly created by this delta.

Write:
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_after_fix_recheck_20260524.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_after_fix_recheck_findings_20260524.jsonl`

JSONL schema:
`{"verdict":"SCOPED_PASS|REWRITE|DELETE|NEED_EVIDENCE","row_id":"","suite":"","question_no":"","reason":"","required_action":""}`

Do not call full final PASS because GPTPro web review remains pending. If all five checks pass, say `ClaudeCode scoped PASS after fixes`.
