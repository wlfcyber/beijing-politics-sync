# GPT-5.5 Pro By-Question Review Digest

Source: same ChatGPT Pro conversation used for the earlier commander and section-batch content review.

Raw response: `08_review/gpt_content_review/by_question_review_response_20260503.md`

Trigger object: `07_student_doc/by_question_view_draft_20260503.md` plus `07_student_doc/six_bucket_to_question_crosswalk_draft.md`.

Boundary: GPT is advisory only. It did not inspect local source files and cannot decide evidence status, scoring status, or final inclusion.

## Verdict

`NEEDS_FIX`.

GPT judged that the section-batch structural defects are mostly repaired: the draft now has by-question training, whole-question answer cards, and caution notes. It still blocks student preview until P0 consistency and content-risk issues are repaired.

## Accepted P0 Tasks

| issue_id | GPT issue | Codex local decision |
|---|---|---|
| GPT-BQ-001 | Crosswalk lists 2026顺义一模 Q20 under 和平与发展, but by-question view omits it. | ACCEPT. Local worker Batch02 records 顺义 Q20 `时代主题：和平和发展` from formal scoring PPT. Patch by-question view to include it. |
| GPT-BQ-002 | 2025海淀期中 Q21(2) uses current era wording too broadly across all new-China diplomacy stages. | ACCEPT WITH LOCAL WORDING. Local image8 supports world-change background, but student wording must be stage-aware and not use current background to统摄全程. |
| GPT-BQ-003 | 2025海淀期中 Q16(2) mixes enterprise/government/organization subjects and mis-hangs global economic governance under political multipolarity. | ACCEPT. Local fusion already classifies ATOM-B14 under 经济全球化; patch subject split and main bucket. |
| GPT-BQ-004 | 2026西城期末 Q20 over-stacks D05 variants and may over-generalize UN core role. | ACCEPT WITH LOCAL EVIDENCE. D05 is one same-slot optional group; student answer should pick a few fitting expressions. D08 has local visual support, but wording should be climate-governance-frame specific. |
| GPT-BQ-005 | 2025海淀二模 Q21 crosswalk lists 新型国际关系 but by-question view does not. | ACCEPT AS OPTIONAL EXPRESSION. Local worker Batch02 records it in the `联合国需要中国` contribution line; patch by-question view as optional, not as the main structure. |
| GPT-BQ-006 | 2024东城一模 Q16/Q20 and 2025海淀期末 Q22 should not sit as full peer templates with core 选必一主线题. | ACCEPT. Patch headings and section structure to mark them as拓展迁移/可用片段. |
| GPT-BQ-007 | `中国全球治理理念与价值取向` is too broad as one student-memorizable package. | ACCEPT. Keep it as one same-slot group in the teacher/evidence layer, but student bridge should split主干 expression and备选 expression. |

## Deferred / Not Auto-Promoted

| issue_id | Advice | Reason |
|---|---|---|
| GPT-BQ-008 | Add market-difference/cost/brand/localization points to 2025海淀期中 Q16(2). | DEFER. The current by-question preview is selected 选必一 angle training. Business-operation points need a fresh local check before inclusion. |
| GPT-BQ-009 | Rebuild all material-catch sections as two-column tables. | DEFER TO P1. Useful transfer improvement, but not required before the P0 content-risk patch. |

## Immediate Patch Set

Patch `by_question_view_draft_20260503.md` and `six_bucket_to_question_crosswalk_draft.md`, then rerun:

- forbidden student-term scan;
- by-question/crosswalk consistency scan;
- Patcher and Governor gates;
- Confucius artifact-only check after the student artifact changes.
