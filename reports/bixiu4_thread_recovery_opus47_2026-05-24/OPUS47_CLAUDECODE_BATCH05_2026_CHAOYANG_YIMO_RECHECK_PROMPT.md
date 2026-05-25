# OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_PROMPT

You are ClaudeCode running as a production lane, not a casual reviewer.

Required model gate:

- You must use Opus 4.7 with max effort / adaptive thinking if the runtime exposes it.
- If you cannot prove model identity and effort/adaptive-thinking from runtime/debug/JSON evidence, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Do not count Sonnet, Haiku-only, or model-unknown output as qualified evidence.
- Do not write `STRICT_FINAL_ACCEPTED`.

Repository root:

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Recovery directory:

`reports\bixiu4_thread_recovery_opus47_2026-05-24`

Run directory:

`reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24`

Batch under review:

`2026朝阳一模`

Files to inspect:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH05_2026_CHAOYANG_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2026朝阳一模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.blocked.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- current DOCX/PDF under `05_delivery`
- rendered PNGs under `07_render_check\word_pdf_pages`

Review tasks:

1. Confirm whether the Batch05 source decisions for Q1/Q2/Q3 are source-defensible:
   - Q1 key B; ① supports `一切从实际出发`; ④ supports the general practice/实干 entry.
   - Q2 key A; value-guidance entry.
   - Q3 key D; only ④ enters `辩证否定 / 守正创新`; ② stays culture-line boundary.
2. Confirm whether Q4-Q15 exclusions are source-defensible and not hiding a valid 必修四 philosophy insertion.
3. Confirm Q16 is already covered, and the evidence label refinements do not overclaim ordinary reference answers as formal scoring rubrics.
4. Confirm Q17 has no valid Q17(3) philosophy subquestion in the source; Q17(1) is logic/thinking and Q17(2) is politics-and-law.
5. Confirm Q18-Q20 module-boundary exclusions.
6. Confirm Q21 existing entries are source-defensible under the综合运用 marking rule and do not require new insertion in Batch05.
7. Verify matrix state:
   - `2026朝阳一模` loose pending rows should be 0.
   - global exact candidate and need-source rows should be 464.
8. Verify delivery state:
   - ledger rows 51, ledger heading matches 51/51.
   - DOCX/PDF render numbers after all-label normalization: DOCX 349,550 bytes; PDF 3,856,219 bytes; 232 pages; 232 PNG pages.
   - all label paragraphs 2148/2148 styled consistently.
   - no student-facing audit/source residue.

Return a concise Markdown report with:

- `runtime_model_gate`
- `content_decision`
- `corrections_required`
- `source_evidence_findings`
- `docx_pdf_ledger_findings`
- `final_boundary`

If any correction is required, name exact files/rows/headings. If content passes but model proof is blocked, write `pass_with_corrections_model_gate_blocked` or `pass_model_gate_blocked`, not final acceptance.
