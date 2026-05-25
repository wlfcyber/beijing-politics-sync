# OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_PROMPT

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

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/COVERAGE_FUSION_BATCH04_2026_SHIJINGSHAN_ERMO_CODEX_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026石景山二模.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- current DOCX/PDF under `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

Recheck scope:

1. Verify every `2026石景山二模` matrix row now has a defensible disposition and suite-local pending count is actually zero.
2. Verify Q1 insertion:
   - official key Q1=A;
   - only correct option ② is used for `系统观念 / 系统优化`;
   - option ① political/legal chain is not misfiled as philosophy.
3. Verify Q2 insertion:
   - official key Q2=D;
   - only correct option ④ enters `矛盾就是对立统一`;
   - option ② culture/national-spirit line is not forced into the current philosophy body.
4. Verify Q3 insertions:
   - official key Q3=B;
   - `整体与部分` and `矛盾的特殊性 / 具体问题具体分析` placements are supported by correct option ①/③ wording;
   - no unsupported `适度原则` insertion was made from wrong option ④.
5. Verify Q9 insertions:
   - official key Q9=D;
   - practice and people placements are supported by correct options ③/④.
6. Verify Q17(3) evidence downgrade:
   - the three existing entries are retained only as source-listed optional paths;
   - they must not be labeled as cumulative strong scoring points.
7. Verify Q20 exclusion:
   - `系统观` appears only as broad optional multi-module angle;
   - no specific philosophy material-to-answer chain exists in the scoring reference;
   - therefore no forced DOCX insertion.
8. Verify DOCX/PDF/ledger/render claims:
   - ledger rows `47`
   - label paragraphs `188 / 188`
   - PDF pages `238`
   - inserted search pages Q1 `77`, Q2 `123`, Q3 `67`/`135`, Q9 `175`/`207`
9. Identify any overclaim where an official answer key / choice chain is being mislabeled as a scoring rubric.
10. Identify any ordinary reference-answer evidence being treated as a scoring rule.

Output a concise Markdown report with these fields:

- `runtime_model_gate`: one of `CONFIRMED_OPUS47_MAX_EFFORT`, `BLOCKED_MODEL_CONFIRMATION_REQUIRED`, or `INVALID_MODEL`
- `content_decision`: one of `pass`, `pass_with_corrections`, `blocked`, or `fail`
- `corrections_required`: bullet list or `none`
- `source_evidence_findings`: bullet list
- `docx_pdf_ledger_findings`: bullet list
- `final_boundary`: must not write `STRICT_FINAL_ACCEPTED`; must state whether this is only a batch-level recheck

Do not rewrite the artifact. Report findings only.
