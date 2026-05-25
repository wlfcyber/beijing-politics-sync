# ClaudeCode Post-Repair Recheck Prompt - Bixiu4 In-Body Evidence

You are ClaudeCode production/recheck lane for the Beijing politics Bixiu4 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive/deep thinking where available. If the runtime cannot prove that, say so. Do not count Sonnet, Haiku, or model-unknown output as qualified evidence.

Read these local artifacts in the current directory:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md`
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv`
- `SHIJINGSHAN_2024_YIMO_Q16_SOURCE_EXHAUSTION_AND_DOCX_REMOVAL_20260525.md`
- `XICHENG_2026_ERMO_Q20_FORMAL_PINGBIAO_REPAIR_20260525.md`
- `FORMAT_RENDER_QA_20260524.md`
- `STYLE_NORMALIZATION_AUDIT_20260525.md`
- `SONNET_INVALIDATION_LEDGER.md`
- `MODEL_EVIDENCE_LEDGER.md`

Tasks:

1. Verify the latest risk audit claim: matrix rows audited, rows marked in-book/body, total risk rows, and in-book/body risk rows.
2. Verify whether `2024石景山一模 Q16/Q哲学` has been removed from current DOCX body placement and is now treated only as a non-body evidence boundary because no formal scoring source was found.
3. Verify whether `2026西城二模 Q20` now has formal rendered pingbiao evidence, and state whether that support is broad-angle scoring support rather than point-by-point unique scoring.
4. Verify whether DOCX/PDF render QA after the latest removal/export has matching label counts and no blank-like body pages.
5. State whether local row-level in-body evidence is content-pass, and separately state which gates remain open.

Hard boundaries:

- Do not write the forbidden final-acceptance token anywhere.
- Do not call the whole project final accepted.
- Do not count Sonnet, Haiku, or model-unknown output as qualified ClaudeCode evidence.
- Do not treat GPTPro web or Claude web/app review as complete unless a real captured response exists.
- Ordinary reference answers are not scoring rubrics.
- Use `content_result: pass`, `content_result: pass_with_notes`, `content_result: fail`, or `content_result: blocked`.

Return format:

```
# Post-Repair In-Body Evidence Recheck

content_result: ...

## Findings
- ...

## Open Gates
- ...

## Model Evidence Boundary
- ...
```
