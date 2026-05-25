# Claude Web Opus 4.7 Full Artifact Review Packet After Style Fix

status: `READY_FOR_REAL_CLAUDE_WEB_REVIEW`

Use the Claude web/app model shown in the composer as `Opus 4.7 Adaptive`.

## Required Scope

You are the external Claude Opus 4.7 adaptive-thinking review lane for the Beijing Gaokao politics Bixiu4 recovery thread. Review the attached/current artifacts as an outside reviewer, not as a local worker.

This is not a final-acceptance request. Do not use the forbidden final-acceptance token. The correct possible outputs are:

- `external_result: pass_with_open_gates`
- `external_result: fail`
- `external_result: blocked_need_more_artifacts`

## Attached/Referenced Artifacts To Review

Primary artifacts:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md`
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv`
- `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md`
- `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.json`
- `FORMAT_RENDER_QA_20260524.md`
- `GOVERNOR_RECOVERY_REPORT_20260524.md`
- `CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`
- `MODEL_EVIDENCE_LEDGER.md`
- `SONNET_INVALIDATION_LEDGER.md`

Latest delivery files:

- `哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`

Latest render evidence:

- `word_render_qa_20260525_heading_style_fix/render_manifest.json`
- `word_render_qa_20260525_heading_style_fix/heading_style_fix_contact_sheet.png`

## Review Questions

1. Coverage: Does the matrix and risk-audit evidence support the claim that the local row-level coverage queue for 2024-2026 suites is currently zero-risk at the in-book/body level? Distinguish body rows from module-boundary rows.
2. Placement: Does the evidence discipline separate formal scoring/rubric/marking evidence from ordinary reference answers? Identify any place where the packet still appears to promote a weak reference answer into rubric support.
3. Formatting: Does the latest style audit and render manifest support the claim that new and legacy question-entry headings/labels are structurally consistent, with matching DOCX/PDF label counts and no blank-like body pages?
4. Thickness: Based on the packet, are the answer-landing chains and local governance thick enough for a zero-baseline student, or do you see unresolved weak logic areas that require more content review?
5. Model evidence: Confirm whether Sonnet/Haiku/model-unknown evidence is excluded and whether GPTPro/Claude full artifact gates remain open unless this current review is actually captured.

## Hard Boundaries

- Do not treat local Codex/Governor summaries as substitutes for row-level evidence.
- Do not count Sonnet, Haiku, or model-unknown output as qualified ClaudeCode evidence.
- Do not call GPTPro or Claude web/app review complete unless this answer is the captured real web/app answer.
- Do not accept ordinary reference answers as scoring rubrics.
- Do not call the project final accepted.

## Return Format

```
# Claude Opus 4.7 External Artifact Review

external_result: ...

## Coverage And Placement
- ...

## Formatting And Render
- ...

## Thickness / Student Use
- ...

## Open Gates
- ...

## Required Corrections Before Final Acceptance
- ...
```
