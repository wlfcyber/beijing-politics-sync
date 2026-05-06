# GPT-5.5 Pro Section Batch Review Digest

Source:

- Raw review: `08_review/gpt_content_review/section_batch_review_response_20260503.md`
- Trigger object: `section_batch`

## GPT Verdict

`NEEDS_FIX`

GPT treated the current section-batch draft as a useful teacher后台术语库, but not as a student final.

## Must-Fix Items Adopted As Local Tasks

1. Multi-question merged terms need `总公式 + 分题卷面句`, not one answer sentence for all sources.
2. Source-chain gaps must be fixed or quarantined, especially `和平与发展仍是时代主题` mentioning 2025海淀期中 Q21(2) without a matched prompt/answer variant.
3. `时代主题` triggers are too broad; they need strong/weak trigger levels.
4. Relation-type Q17 items should be separated from general theory into a relation-question template area.
5. High-information core titles should be restored, e.g. `国家间共同利益是国家合作的基础`, `充分利用国内国际两个市场、两种资源`.
6. 2025海淀期中 Q16(2) must keep IP/compliance risk separate from trade friction / international-organization mechanism.
7. `新型国际关系` needs China-diplomacy attribute or cross-bucket note.
8. UN three-pillar wording must be locally checked before student release.
9. China wisdom / China solution needs separate question-specific answer variants.

## Transfer Fixes Adopted

1. Final student document should become `按题视图 + 六桶索引`, not pure six-bucket body.
2. Each high-frequency question needs审题结论、材料分层、答案骨架、答题卡版答案.
3. Backend fields such as scoring positions, page numbers,分值 and mandatory labels should move to teacher evidence docs.
4. High-risk terms need禁用或慎用提醒.
5. Material triggers should split into `材料原词` and `推导`.
6. Merge rules should be three-tier: hard merge, cross-reference, no merge.

## Codex Local Decision

- GPT advice is accepted as teaching-structure and transfer-review advice only.
- It is not used as local scoring evidence.
- Current `section_batch_draft_for_external_review.md` remains a review draft; it is not a student final.
- Next student-facing revision must prioritize按题视图 and分题卷面句 before Word/PDF.
