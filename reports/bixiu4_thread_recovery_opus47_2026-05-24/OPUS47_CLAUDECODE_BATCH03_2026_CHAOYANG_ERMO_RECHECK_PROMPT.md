# OPUS47_CLAUDECODE_BATCH03_2026_CHAOYANG_ERMO_RECHECK_PROMPT

You are ClaudeCode acting as the required second production line for the 必修四政治庄园 recovery run.

Required runtime:

- model: `claude-opus-4-7`
- effort: `max`
- reasoning: adaptive thinking / high effort if exposed by runtime

Hard model gate:

- Do not count Sonnet, Haiku, or model-unknown output as qualified evidence.
- If you cannot prove Opus 4.7 and max/adaptive-thinking from the command/debug/JSON evidence available to you, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- You may still perform a content recheck, but any content decision must be labeled model-gate-blocked.

Files to inspect:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/COVERAGE_FUSION_BATCH03_2026_CHAOYANG_ERMO_CODEX_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026朝阳二模.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- current DOCX and PDF under `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

Recheck scope:

1. Verify that every `2026朝阳二模` matrix row has a defensible disposition.
2. Verify Q1/Q3/Q4 insertions:
   - Q1 must be value-guidance only from official choice key/correct-option chain.
   - Q3 must place only practice-development-of-cognition and social-existence/social-consciousness from correct options ③/④.
   - Q4 must place only contact diversity and system/integration from correct options ①/③.
3. Verify Q5 was not inserted as `辩证否定`, because that term is a wrong-option trap in this suite.
4. Verify Q16/Q21 are not duplicated unnecessarily and are already covered by source-supported final-body entries.
5. Verify Q20 is not forced into the current philosophy body from weak optional wording.
6. Verify the current DOCX/PDF/ledger/render QA claims are coherent:
   - ledger rows `41`
   - label paragraphs `164 / 164`
   - PDF pages `236`
   - inserted search pages Q1 `216`, Q3 `173` and `189-190`, Q4 `61` and `76`
7. Identify any overclaim where an official answer key / choice chain is being mislabeled as a scoring rubric.
8. Identify any ordinary reference-answer evidence being treated as a scoring rule.

Output a concise Markdown report with these fields:

- `runtime_model_gate`: one of `CONFIRMED_OPUS47_MAX_EFFORT`, `BLOCKED_MODEL_CONFIRMATION_REQUIRED`, or `INVALID_MODEL`
- `content_decision`: one of `pass`, `pass_with_corrections`, `blocked`, or `fail`
- `corrections_required`: bullet list or `none`
- `source_evidence_findings`: bullet list
- `docx_pdf_ledger_findings`: bullet list
- `final_boundary`: must not write `STRICT_FINAL_ACCEPTED`; must state whether this is only a batch-level recheck

Do not rewrite the artifact. Report findings only.
