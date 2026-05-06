# External By-Question Review Combined Digest

Inputs:

- GPT raw: `08_review/gpt_content_review/by_question_review_response_20260503.md`
- Claude raw: `08_review/claude_by_question_review_response_20260503.md`
- Student draft: `07_student_doc/by_question_view_draft_20260503.md`
- Bridge draft: `07_student_doc/six_bucket_to_question_crosswalk_draft.md`

## Combined Judgment

Current status: `NEEDS_FIX`, not student preview, not final.

Both external advisors agree the work has moved from backend six-bucket table to real by-question training form. They also agree the remaining blockers are not cosmetic: they affect student transfer and could teach wrong usage boundaries.

## P0 Repair Queue

1. Patch crosswalk/by-question consistency:
   - 2026顺义一模 Q20 must either include 和平与发展 in by-question view or be downgraded in the bridge. Local evidence supports inclusion.
   - 2025海淀二模 Q21 must either include 新型国际关系 as a supported optional expression or be removed from the bridge. Local evidence supports optional expression.
2. Patch 2025海淀期中 Q16(2):
   - main bucket should be 经济全球化/global economic governance, not 政治多极化;
   - split enterprise compliance, industry support, and government/global-rule mechanisms;
   - keep business-operation points deferred until local recheck.
3. Patch 2025海淀期中 Q21(2):
   - write historical-stage change more carefully;
   - do not let current `和平与发展成为时代主题`统摄 all stages of new-China diplomacy.
4. Patch 2026西城期末 Q20:
   - reduce D05 concept stacking in answer card;
   - keep D05 as same-slot concept group in bridge, with main/backup expression rule;
   - keep UN core-role wording tied to UN climate governance / Paris Agreement / NDC context.
5. Reclassify boundary questions:
   - 2024东城一模 Q16;
   - 2024东城一模 Q20;
   - 2025海淀期末 Q22.
6. Patch high-frequency China-wisdom bridge usage:
   - make scenario-specific expression reminders for global governance, global development, UN relation, climate governance, civilization, and short essay use.

## P1 Queue

- Add 主干点/可选点/慎用点 by question.
- Convert `材料抓手` to a more uniform `看到... -> 想到...` structure.
- Split `慎用提醒` into `使用条件` and `易错提醒`.
- Shorten answer-card paragraphs to 40-70 character scoring units where possible.

## Gate

After P0 patch, rerun local scans and internal Patcher/Governor. Confucius is required after any student artifact patch.
