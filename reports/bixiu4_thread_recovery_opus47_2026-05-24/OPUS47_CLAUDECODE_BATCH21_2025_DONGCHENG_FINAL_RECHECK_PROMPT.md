# ClaudeCode Opus 4.7 Recheck Prompt - Batch21 2025 Dongcheng Final

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread. You are not a casual reviewer. Recheck the Codex Batch21 work from source evidence and current artifacts.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write or claim final acceptance for the whole project.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. Verify this batch as a production lane.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending` unless actually completed elsewhere.
- If adaptive/max-effort proof cannot be confirmed, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## Files To Inspect

- `BATCH21_2025_DONGCHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH21_2025_DONGCHENG_FINAL_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md`
- `FORMAT_RENDER_QA_20260524.md`
- `word_render_qa_20260525_batch21_word/render_manifest.json`
- `docx_insert_ledger.csv`
- `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- Current DOCX/PDF under `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

## Source Facts To Verify

1. Batch21 suite is `2025东城期末`.
2. Q4 objective answer supports only objective-answer evidence. The key material is the Chinese-character stroke relation, so it may support `矛盾就是对立统一`; it is not subjective scoring-rubric evidence.
3. Q16 prompt is `器以述史、物以载道`. The third layer supports `主观能动性 / 意识的能动作用`: improve understanding of artifact value, collect/protect/research artifacts, and use the artifacts to understand history and carry meaning.
4. Q21 prompt is `民生为大是价值取向，更是实践要求`. It supports `人民群众` and `价值判断与价值选择`: correct value judgments and choices must follow social development laws and stand with the people; modernization choices should be evaluated by whether they protect and develop people's interests and convert the value orientation into livelihood practice.
5. Q5 and Q18(2) are Logic and Thinking boundaries. Q17/Q19 are law/politics boundaries. Q20 is an international politics/economics boundary. Non-Bixiu4 objective questions must remain outside the current student text.
6. Current DOCX should have exactly four governed Batch21 entries:
   - Q4 registered existing DOCX coverage under `矛盾就是对立统一`.
   - Q16 registered existing DOCX coverage under `主观能动性 / 意识的能动作用`.
   - Q21 refreshed existing DOCX coverage under `价值判断与价值选择`.
   - Q21 newly inserted coverage under `人民群众`.

## Checks Required

1. Verify the matrix has exactly `25` Batch21 rows and covers all Q1-Q21/subparts.
2. Verify body placements are exactly the four listed above, with evidence levels correctly bounded.
3. Verify Q21 value-judgment refresh is materially thicker and student-facing, not a generic one-line landing.
4. Verify render evidence is coherent: `249/249` PDF pages/rendered PNGs, labels `2315/2315`, visible suite mentions `4/4`, hit pages `20, 127, 216, 233`; raw PDF exact text count `0` is a CJK extraction limitation, not a visibility miss.
5. Verify `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl` each have four governed records for this suite.
6. Verify the global raw midterm/final gap is now `14` suites.
7. Identify any required corrections before Batch21 can be treated as locally closed.

## Required Output

Return a concise Markdown result with:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `local_policy_result`: use `pass_with_model_gate_blocked` if content passes but adaptive/max-effort proof remains insufficient
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless fully proven
- `sonnet_haiku_used`: whether any Sonnet/Haiku/model-unknown output is counted as qualified evidence
- `matrix_check`
- `docx_check`
- `render_check`
- `global_scope_check`
- `required_fixes`
- `remaining_project_blockers`
