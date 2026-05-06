# External By-Question P0 Patch Log

Time: 2026-05-03 20:23 CST

Inputs:

- GPT by-question review digest: `08_review/gpt_content_review/by_question_review_digest_20260503.md`
- Claude by-question review digest: `08_review/claude_by_question_review_digest_20260503.md`
- Patcher triage: `codex_lane/agents/patcher/patcher_external_by_question_review_triage.md`
- Governor gate: `codex_lane/agents/governor/governor_external_by_question_review_gate.md`

## Patched Student Files

- `07_student_doc/by_question_view_draft_20260503.md`
- `07_student_doc/six_bucket_to_question_crosswalk_draft.md`

## Patch Decisions

| patch_id | issue | local basis | patch |
|---|---|---|---|
| P0-PATCH-001 | 2026顺义一模 Q20 bridge listed 和平与发展 but by-question section omitted it. | Worker Batch02 records 顺义 Q20 formal scoring PPT includes `时代主题：和平和发展`. | Added times-theme material trigger, core point, and answer-card wording in the 顺义 section. |
| P0-PATCH-002 | 2025海淀期中 Q16(2) mis-hung global economic governance under 政治多极化 and mixed subjects. | Batch01/fusion ATOM-B14 is 经济全球化; external advice matched local bucket rule. | Moved the point to 经济全球化, split enterprise / industry / government actions, and moved conditional logic into caution text. |
| P0-PATCH-003 | 2025海淀期中 Q21(2) risked using current era background to统摄 all new-China diplomacy stages. | image8 scoring supports world-change and China-change layers, but student wording needed staged framing. | Rewrote the first answer paragraph to separate early stage, reform period, and new era background. |
| P0-PATCH-004 | 2026通州期末 Q20 wording `中国提出全球治理公共产品` was not student-like. | Pure wording fix; no new scoring claim. | Rewrote to `中国把全球治理倡议作为重要国际公共产品贡献给世界`. |
| P0/P1-PATCH-005 | 2026朝阳一模 Q20 fourth paragraph looked mandatory. | Same content retained; structure risk only. | Marked paragraph as optional sweep-up. |
| P0-PATCH-006 | 2025海淀二模 Q21 bridge listed 新型国际关系 but by-question section did not. | Worker Batch02 includes it in the China-contribution line, not as UN main structure. | Added it as optional expression in by-question view and bridge usage reminder. |
| P0-PATCH-007 | 2026西城期末 Q20 stacked too many D05 concepts and used broad UN wording. | Batch03 D05 is one same-slot concept group; D08 supports UN core role under climate-governance signals. | Reduced answer-card D05 concepts, moved variants to backup expression, and narrowed UN phrasing to the UN climate-governance frame. |
| P0-PATCH-008 | Boundary/open/comprehensive questions were peer-level with main questions. | Source/fusion labels mark them as cross-module/boundary/P2 or optional. | Added a拓展迁移区, changed Q16/Q20/Q22 answer labels to `选必一可用片段`, and added front-loaded use conditions. |
| P0-PATCH-009 | China-wisdom bridge row was too broad. | Same core can stay merged, but expression must be question-specific. | Expanded use reminders by global governance, global development, UN relation, climate governance, civilization, and short essay contexts. |
| CLEAN-PATCH-010 | Student draft had preview process wording with `校对`. | Student clean-scan hygiene. | Reworded preview notes and boundary heading. |

## Current Gate

Patched files pass the current forbidden-term scan. They still require:

- internal Patcher re-review;
- Governor re-gate;
- Confucius artifact-only transfer check.

No final Markdown, DOCX, PDF, coverage close, or final acceptance is allowed yet.
