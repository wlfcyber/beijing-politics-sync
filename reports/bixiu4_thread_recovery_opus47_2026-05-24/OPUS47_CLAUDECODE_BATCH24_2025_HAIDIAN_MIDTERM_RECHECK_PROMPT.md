# ClaudeCode Opus 4.7 Recheck Prompt - Batch24 2025海淀期中

You are the ClaudeCode production lane for 必修四政治庄园 Batch24.

Hard requirements:

- Run as an independent production recheck, not as a casual reviewer.
- Do not use Sonnet, Haiku, or model-unknown output as qualified evidence.
- Do not claim final whole-project acceptance.
- Ordinary reference answers cannot be upgraded into scoring rubrics.
- Objective-choice answer-key evidence is objective-only unless a scoring source gives a subjective philosophy principle.
- GPTPro web review and external Claude Opus full-artifact review remain `real_call_pending` unless truly completed.
- If you cannot independently prove Opus 4.7 max effort / adaptive thinking from runtime evidence, write `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Read and verify these local artifacts:

- `BATCH24_2025_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH24_2025_HAIDIAN_MIDTERM_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `FORMAT_RENDER_QA_20260524.md`
- `MODEL_EVIDENCE_LEDGER.md`
- Current DOCX in `../bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/`

Specific checks:

1. Matrix check:
   - `2025海淀期中` must have exactly `23` rows.
   - Body rows must be `0`.
   - Boundary rows must be `23`.
   - Q coverage must include Q1-Q15, Q16(1), Q16(2), Q17, Q18, Q19, Q20, Q21(1), Q21(2).

2. Placement check:
   - Q1-Q15 are economics, politics/law, national-security, international-politics, or public-governance objective rows.
   - Q16(1), Q16(2), Q17, and Q20 are economic/global-economy rows.
   - Q18 and Q19 are political/legal-governance rows.
   - Q21(1) is legal/fazhi; wording about actual conditions or social development demand must not be converted into 必修四 philosophy.
   - Q21(2) is contemporary international politics/economics.
   - No question or subquestion has scoring-source-backed 必修四 philosophy-body placement.

3. DOCX/render check:
   - Current DOCX must have `0` mentions of `2025海淀期中`.
   - Batch24 must not have inserted DOCX body entries, ledger rows, or accepted JSONL records.
   - Render status should be `NO_DOCX_CHANGE_RENDER_NOT_NEEDED`.
   - Latest full render evidence may remain Batch23 because Batch24 made no DOCX change.

4. Global scope check:
   - Global audit must mark `2025海淀期中` as covered by Batch24 boundary matrix with `23` rows and `0` DOCX mentions.
   - Remaining raw midterm/final gap should be `11` suites.

Return a final answer with these exact fields near the end:

```
content_result: pass|pass_with_notes|fail|blocked
local_policy_result: pass_with_model_gate_blocked|fail|blocked
model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED
required_fixes: ...
```

Use `pass` only if the Batch24 local content and boundary-exclusion logic are internally consistent. Use `pass_with_notes` only for non-blocking issues. Use `fail` if any count, placement, or source-evidence claim is wrong.
