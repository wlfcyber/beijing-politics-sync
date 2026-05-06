# Codex A Governor Gate - External By-Question Review

- Role: Governor / 外部二审门禁
- Inputs read:
  - `08_review/gpt_content_review/by_question_review_response_20260503.md`
  - `opus_writer/web_external/claude_by_question_review_response_20260503.md`
  - `07_student_doc/by_question_view_draft_20260503.md`
  - `07_student_doc/six_bucket_to_question_crosswalk_draft.md`
- Conclusion: `PASS_INTERNAL_PREVIEW_WITH_P0_BLOCKERS / BLOCK_FINAL`

## Gate Decision

1. Student preview:
   - Allowed only as `内部小范围学生预览 / 二审预览稿`, with the current `教学预览版，非终稿` label retained.
   - Not allowed as `正式学生预览版` until the P0 blockers below are fixed and re-gated.
2. Final release:
   - `BLOCK`.
   - Do not generate Word/PDF.
   - Do not write `FINAL_ACCEPTANCE`.
   - Do not mark coverage closed.

## Advisory Boundary

GPT and Claude reviews are advisory only. They may guide teaching structure, transfer clarity, wording compression, and student usability, but they do not decide:

- whether a term is real scoring evidence;
- whether P0/P1/P2 evidence can be promoted;
- whether a reference answer can become scoring rule;
- whether a point is mandatory, optional, same-slot variant, or boundary-only.

All evidence decisions remain with Codex local source review, scoring atom tables, Governor gates, and original rubric/marking materials.

## Minimal P0 Blockers Before Formal Student Preview

1. Bridge consistency blockers:
   - `2026顺义一模 Q20`: crosswalk lists `和平与发展仍是时代主题`, but the by-question answer/core list does not surface it. Either add it as a locally confirmed optional/background answer variant, or downgrade/remove it from bridge hit list.
   - `2025海淀二模 Q21`: crosswalk lists `推动建设合作共赢的新型国际关系`, but by-question view does not surface it. Either add as locally confirmed optional point or remove/downgrade from bridge hit list.
   - `2025海淀期中 Q16(2)`: `利用国际组织赋予的权利，积极参与全球经济治理和规则制定` must not主挂政治多极化; current question context points to经济全球化/全球经济治理规则风险, with international-organization mechanism as cross-reference.
2. `2025海淀期中 Q16(2)`主体分工 blocker:
   - Separate enterprise, industry organization, and government actions.
   - Move conditional language such as `如果材料进一步呈现...` out of answer-card prose and into use-condition / caution text.
   - Locally recheck whether business-operation advice such as market research, localization, cost/supply-chain risk is required by the evidence; if unsupported, do not invent it.
3. `2025海淀期中 Q21(2)`历史阶段 blocker:
   - The current expression risks using present-era `和平与发展 / 政治多极化 / 经济全球化` to cover all of New China's diplomatic history.
   - Rewrite as staged change plus stable principles, after local evidence confirms the scoring-image wording.
4. `2026西城期末 Q20`术语堆叠 and UN-signal blocker:
   - Reduce the China-global-governance concepts from a six-term pile into主干 + 备选.
   - Confirm locally that `维护联合国在国际事务中的核心作用` is supported by the scoring rule/material signal; avoid overgeneralizing any climate agreement into generic UN-core-role usage.
5. Boundary section blocker:
   - `2024东城一模 Q16`, `2024东城一模 Q20`, and `2025海淀期末 Q22` must be visibly separated as拓展迁移/边界题, not same-level main templates.
   - Keep P2/P1/optional evidence from being read as P0 mandatory core.
6. China contribution blocker:
   - `贡献中国智慧、中国方案、中国力量` is too broad in the crosswalk. It needs question-type sub-usages: global governance, global development, UN relation, climate governance, civilization/short essay, each only where local evidence supports that usage.

## Post-Fix Required Rechecks

After P0 fixes, rerun all of the following before any formal student preview or final artifact:

1. 清洁扫描:
   - Scan student-facing files for backend/audit terms, local paths, P0/P1/P2 labels, scoring-position residue, `采分点`, `要落到`, `材料中`, `终稿`, `FINAL_ACCEPTANCE`, Word/PDF claims, and over-dense slogan piles.
2. 桥接一致性:
   - Every crosswalk hit must appear in the corresponding by-question section as a main point, optional point, or clearly marked expression variant.
   - Every by-question core must map back to a six-bucket row or a boundary/extension row.
   - Main bucket, cross bucket, and forbidden bucket must be explicit for high-risk items.
3. Governor:
   - Rerun Governor gate on the repaired by-question draft and crosswalk.
   - Confirm no P2/P1/boundary-only item has been silently promoted to P0 frequency or mandatory student core.
4. Confucius:
   - Run a learnability/transfer check on the student-facing artifact: can a zero-baseline student use it to identify trigger signals, select main/optional/caution points, and write a fresh unseen answer without overusing万能句?

## Current Permission Boundary

- Continue local repair and internal preview review.
- Do not edit evidence status from GPT/Claude comments alone.
- Do not generate final Markdown/Word/PDF.
- Do not close coverage.
- Do not claim external review is satisfied until P0 blockers are fixed and re-gated.
