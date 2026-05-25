# ClaudeCode follow-up: verify batch_03 cleanup

You previously returned `SCOPED_PASS_WITH_NOTES` because `08_external_review/batch_03_summary_and_gate.md` still contained stale current-state assertions such as `Current accepted JSONL rows: 41` and `accepted JSONL（26条）`.

Recheck only this cleanup:

- `08_external_review/batch_03_summary_and_gate.md`
- `06_governor_confucius/CURRENT_ACCEPTANCE_STATUS_20260524.md`
- `04_fusion_audit/gptpro_web_scoped_fixes_applied_20260524.md`
- `05_delivery/docx_insert_ledger.csv`
- `04_fusion_audit/student_patch_entries.accepted.jsonl`

Hard pass criteria:

1. `batch_03_summary_and_gate.md` must present the active current state as 36 accepted rows, 36 ledger rows, and 236 PDF pages.
2. It must not contain stale current-state assertions for 26/38/41 accepted rows or 227/232/234/237 PDF pages. Mentions of old counts are acceptable only if clearly inside `CURRENT_ACCEPTANCE_STATUS` supersession wording or attached historical files outside `batch_03`, not as batch_03 current state.
3. The GPTPro audit report may still exist as a separate attached file, but `batch_03` must not inline the old GPTPro table that quotes superseded counts.
4. The verdict must remain scoped, not final all-model PASS.

Output:

- First line: `SCOPED_PASS` or `NOT_PASS`.
- Then a table: `severity | location | finding | required_fix`.
- End with one short boundary statement.
