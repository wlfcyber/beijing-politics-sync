# ClaudeCode Opus 4.7 Recheck Prompt - Batch25 2025海淀期末

You are the ClaudeCode production lane for 必修四政治庄园 Batch25.

Hard requirements:

- Run as an independent production recheck, not as a casual reviewer.
- Do not use Sonnet, Haiku, or model-unknown output as qualified evidence.
- Do not claim final whole-project acceptance.
- Ordinary reference answers cannot be upgraded into scoring rubrics.
- Objective-choice answer-key evidence is objective-only unless a scoring source gives a subjective philosophy principle.
- GPTPro web review and external Claude Opus full-artifact review remain `real_call_pending` unless truly completed.
- If you cannot independently prove Opus 4.7 max effort / adaptive thinking from runtime evidence, write `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Read and verify these local artifacts:

- `BATCH25_2025_HAIDIAN_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH25_2025_HAIDIAN_FINAL_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `FORMAT_RENDER_QA_20260524.md`
- `MODEL_EVIDENCE_LEDGER.md`
- `word_render_qa_20260525_batch25_word/render_manifest.json`
- Current DOCX and `docx_insert_ledger.csv` in `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`
- `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`

Specific checks:

1. Source and coverage:
   - `2025海淀期末` source packet must include the PPT scoring/rubric cache and teacher-version paper cache.
   - Teacher answer key should be `1A 2C 3B 4C 5D 6B 7A 8D 9B 10C 11D 12A 13B 14C 15D`.
   - Matrix must contain exactly `46` Batch25 rows: `28` body rows and `18` boundary rows.
   - No Batch25 row may contain `NEED_EVIDENCE`.

2. Placement check:
   - Q4/Q5/Q6/Q7 choice-question rows must be objective-only, not subjective scoring rubrics.
   - Q16 must rely on PPT scoring/rubric support for philosophy body nodes; culture-only points must stay boundary-excluded from the current philosophy-body document.
   - Q17(1) must remain selected-compulsory-3/scientific-thinking boundary; Q17(2) philosophy scoring points may stay in body.
   - Q18 must remain selected-compulsory-3 innovation-thinking boundary.
   - Q19-Q21 must remain Legal and Life boundary rows.
   - Q22 may include only rubric-listed 必修四 philosophy points in body; CPC, modernization, Chinese dream, culture, national spirit, and human-community points must stay boundary/non-philosophy rows.

3. DOCX/ledger/render check:
   - Current DOCX must have exactly `28` governed `2025海淀期末` headings.
   - `docx_insert_ledger.csv` must have exactly `28` rows for `2025海淀期末`.
   - `student_patch_entries.accepted.jsonl` must have exactly `28` records for `2025海淀期末`.
   - Render manifest must show `257/257` PDF pages/rendered PNGs, DOCX/PDF labels `2407/2407`, and Word visible headings `28/28`.
   - Blank-like body pages must be empty except known foreword page 2.

4. Global scope check:
   - Global audit must mark `2025海淀期末` as covered by Batch25 matrix with `46` rows and `28` DOCX mentions/headings.
   - Remaining raw midterm/final gap should be `10` suites.

Return a final answer with these exact fields near the end:

```
content_result: pass|pass_with_notes|fail|blocked
local_policy_result: pass_with_model_gate_blocked|fail|blocked
model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED
required_fixes: ...
```

Use `pass` only if the Batch25 local content, placement, evidence boundaries, render status, and ledger counts are internally consistent. Use `pass_with_notes` only for non-blocking issues. Use `fail` if any count, placement, or source-evidence claim is wrong.
