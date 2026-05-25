# ClaudeCode Opus 4.7 Recheck Prompt - Batch20 2024海淀期中

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread. You are not a casual reviewer. Recheck the Codex Batch20 work from source evidence and current artifacts.

Hard gates:

- Use only Opus 4.7 / max effort / adaptive thinking evidence if your runtime can prove it.
- Do not count Sonnet, Haiku, or model-unknown output as qualified evidence.
- Do not write or claim final acceptance for the whole project.
- Ordinary reference answers cannot become scoring rules.
- If adaptive/max-effort proof cannot be confirmed, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.

Files to inspect:

- `BATCH20_2024_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH20_2024_HAIDIAN_MIDTERM_CODEX_20260525.md`
- `BATCH20_2024_HAIDIAN_MIDTERM_MISPLACED_REMOVAL_LEDGER.csv`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `word_render_qa_20260525_batch20_word/render_manifest.json`
- Current DOCX/PDF in `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

Source facts that must be independently checked:

- The readable source packet for `2024海淀期中` is the rubric/scoring PDF cache, not the paper text cache. The paper text cache is unreadable and should not be used to invent student-facing content.
- The formal module distribution says objective Q1-Q6 are 必修2, Q7-Q11 are 必修3, Q12-Q15 are 选择性必修1.
- The formal module distribution says subjective Q16(1), Q17, Q20 are 必修2; Q18, Q19, Q21(1) are 必修3; Q16(2), Q21(2) are 选择性必修1.
- Q18 rubric is 《政治与法治》基层民主:党的领导、全过程人民民主、基层民主、协商民主/民主决策/民主监督/民主管理、多元主体共建共治.
- Therefore the three old DOCX entries for `2024海淀期中 第18题` under `系统观念 / 系统优化`, `矛盾的特殊性 / 具体问题具体分析`, and `人民群众` should be treated as misplaced and removed.

Checks required:

1. Verify Batch20 covers every question/subpart of `2024海淀期中` in the matrix.
2. Verify the three Q18 old philosophy placements are invalid under the formal rubric and should remain removed.
3. Verify no `2024海淀期中` student-facing entries remain in the current DOCX/PDF.
4. Verify the render manifest is coherent: 249 pages, 249 PNGs, DOCX/PDF labels 2311/2311, suite mentions 0/0.
5. Verify global raw-suite gap is now 15, not 16 or 17.
6. Identify any required corrections before this batch can be considered locally closed.

Return a concise Markdown result with:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `local_policy_result`: use `pass_with_model_gate_blocked` if content passes but adaptive/max-effort proof remains insufficient
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless fully proven
- `required_fixes`
- `evidence_checked`
- `remaining_project_blockers`
