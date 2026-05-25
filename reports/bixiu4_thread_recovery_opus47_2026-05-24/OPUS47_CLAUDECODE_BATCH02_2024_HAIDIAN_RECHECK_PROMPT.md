# OPUS47_CLAUDECODE_BATCH02_2024_HAIDIAN_RECHECK_PROMPT

You are ClaudeCode production lane B for the recovered 必修四政治庄园 workflow.

Hard gates:

- You must not use Sonnet/Haiku/model unknown as qualified evidence.
- The caller is using `claude-opus-4-7 --effort max`. If you cannot independently expose/confirm max effort and adaptive thinking, say `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Do not write `STRICT_FINAL_ACCEPTED`.
- Do not treat ordinary reference answers as scoring rubrics.
- Codex and ClaudeCode are both production lanes. Review the batch as a production-line source/fusion recheck, not as casual proofreading.

Files to inspect:

1. `reports/bixiu4_thread_recovery_opus47_2026-05-24/COVERAGE_FUSION_BATCH02_2024_HAIDIAN_YIMO_CODEX_20260524.md`
2. `reports/bixiu4_thread_recovery_opus47_2026-05-24/MISPLACED_ENTRY_REMOVAL_2024_HAIDIAN_YIMO_Q17_2_20260524.md`
3. `reports/bixiu4_thread_recovery_opus47_2026-05-24/FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
4. `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2024海淀一模.md`
5. Current DOCX/PDF in `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

Recheck tasks:

1. Verify that rows `M0142`, `M0194`, and `M0286` through `M0303` are no longer left as `待核`.
2. Verify that Q16 is legitimately kept as already covered under 主观能动性 / 联系 / 发展 / 实践, with source-bundle rubric support.
3. Verify that Q2, Q3, and Q5 are properly treated as covered choice questions, with official answer key + stem, not falsely upgraded to scoring-rule support.
4. Verify that Q6, Q8, Q9, Q11, Q12, Q13, Q15, Q18, Q19 are excluded for module boundary reasons.
5. Verify that Q20 is not smuggled in as a philosophy principle when the source is an activity-design task without a specific philosophy scoring rule.
6. Verify that Q17(2) was correctly removed from the current philosophy DOCX because the source asks `分析与综合的思维方法`, and that this should route to 选必三思维 rather than `系统观念 / 系统优化`.
7. Verify that the `系统观念 / 系统优化` section numbering and `docx_insert_ledger.csv` synchronization are coherent after removal.
8. Identify any remaining content corrections required for Batch02.

Required output:

- `model_gate`: one of `qualified_opus47_max_effort_confirmed` or `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `content_decision`: one of `pass`, `pass_with_corrections`, `fail`
- `required_corrections`: list
- `batch02_row_decision_summary`: concise summary
- `source_authority_notes`: note where reference-answer-only evidence was downgraded or bounded
- `final_acceptance`: must be `not_final`
