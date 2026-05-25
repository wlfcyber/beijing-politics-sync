# GPTPro Web Full Artifact Review Packet After Claude Opus Review

status: `READY_FOR_REAL_GPTPRO_WEB_REVIEW`

Use the strongest available GPTPro/Pro reasoning model in the ChatGPT web/app UI. If the UI model identity cannot be confirmed, say so and do not count the result as a qualified GPTPro review.

## Required Scope

You are the GPTPro external reviewer for the Beijing Gaokao politics Bixiu4 recovery thread. Review the attached/current artifacts as an independent outside reviewer.

Do not issue final acceptance. The acceptable results are:

- `gptpro_external_result: pass_with_open_gates`
- `gptpro_external_result: fail`
- `gptpro_external_result: blocked_model_or_artifact_confirmation`

## Attached/Referenced Artifacts To Review

Primary artifacts:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md`
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv`
- `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md`
- `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.json`
- `FORMAT_RENDER_QA_20260524.md`
- `GOVERNOR_RECOVERY_REPORT_20260524.md`
- `MODEL_EVIDENCE_LEDGER.md`
- `SONNET_INVALIDATION_LEDGER.md`
- `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_RESULT_AFTER_STYLE_FIX_20260525.md`
- `CLAUDE_RECOMMENDED_ROW_LEVEL_REVERSE_SAMPLE_AUDIT_20260525.md`
- `CLAUDE_RECOMMENDED_SPECIAL_TAG_AUDIT_20260525.md`
- `BODY_WEAK_EVIDENCE_REVERSE_CHECK_20260525.md`
- `FORMAT_EXTRA_LABEL_BREAKDOWN_20260525.md`
- `THICKNESS_DENSITY_AUDIT_20260525.md`

Latest delivery files:

- `哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`

## Review Questions

1. Coverage: Does the matrix plus post-Claude reverse sample support zero current in-book/body risk, or is more row-level proof needed?
2. Placement: Do formal rubric/scoring/marking evidence, objective choice-key evidence, and ordinary reference-answer evidence remain clearly separated?
3. Formatting: Does style/render QA plus extra-label breakdown support local structural format pass? Does it still need every-page visual review?
4. Thickness: Does `THICKNESS_DENSITY_AUDIT_20260525` show the artifact is not yet content-thickness accepted? How should the 643 density candidates be prioritized?
5. External gates: Does captured Claude Opus 4.7 web review count only as pass-with-open-gates? Should GPTPro itself remain open if this current answer cannot prove model identity?

## Hard Boundaries

- Do not write the prohibited final-acceptance token.
- Do not call the project final accepted.
- Do not count Sonnet/Haiku/model-unknown evidence as qualified ClaudeCode evidence.
- Do not treat ordinary reference answers as scoring rubrics.
- Do not treat local Governor summaries as row-level proof.

## Return Format

```
# GPTPro External Artifact Review

gptpro_external_result: ...
model_identity_visible: yes/no/unclear

## Coverage And Placement
- ...

## Formatting And Render
- ...

## Thickness / Student Use
- ...

## Open Gates
- ...

## Required Corrections Before Acceptance
- ...
```
