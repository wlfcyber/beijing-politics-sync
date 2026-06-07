# GOVERNOR_STATUS

- generated_at: 2026-06-05 23:22 CST
- run: `选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05`
- current_candidate: v45_style-consistent_hierarchy-clean_candidate
- final_status: NOT_FINAL

## Gate Status

| Gate | Status | Evidence |
| --- | --- | --- |
| Scope | PASS | Still exactly two student-facing documents: question/rubric compilation and AB-axis handbook. |
| Local build | PASS | `outputs/*_v45.docx`, `outputs/*_v45.md`; `qa/TWO_DOC_CLEAN_DRAFT_QA_v45_20260605.md`. |
| User structure repair | PASS_LOCAL | Handbook remains `A轴 -> 需要掌握的知识和踩分点 -> 相关例题（2024-2026）`; rejected generic scaffolding remains absent. |
| Scoring-point truncation repair | PASS_LOCAL | v45 keeps the v38 no-cap scoring strategy. QA reports 74 questions, 1027 total rubric scoring points, min=3, max=34. |
| Screenshot-first repair | PASS_LOCAL | Image-backed entries now show original-question image before material/prompt text. Handbook DOCX has 23 inline images and 23 `原题图` labels. |
| Table wording repair | PASS_LOCAL | Student-facing headings use `原题图` or `表格文字版`; `重建` and `表格重建` have zero hits in v45 Markdown and DOCX XML. |
| Markdown hierarchy repair | PASS_LOCAL | Handbook Markdown now uses A-axis `##`, knowledge/related-example sections `###`, core examples `####`, and entry fields `#####`; cross-module background remains a separate `##` section. |
| Color/background consistency | PASS_LOCAL | v45 QA DOCX color audit passes: materials `F7FAFC`, prompts `FFFBF2`, rubrics `F7F7F7`, scoring points and A-axis knowledge points `EEF7F0`. |
| Text regression scan | PASS_LOCAL | v45 Markdown and DOCX XML have zero hits for `第一判断`, `易错边界`, `必背句`, `答案落点`, `同题组 64`, `合同归于无效`, `交易行为无效`, `社会主义和谐价值观`, `重建`, and other old-error terms checked. |
| DOCX structural QA | PASS_LOCAL | Both v45 DOCX files unzip and load through `python-docx`; handbook has 10 A-axis sections, 74 `细则踩分点` labels, and 23 inline images. |
| Render QA | BLOCKED_LOCAL | `render_docx.py` failed with `[WinError 2]` because LibreOffice/soffice is unavailable on this machine. No render PASS is claimed for v45. |
| External GPT | PENDING | Full GPT-5.5 Pro web/app sequence still pending; CLI outputs remain invalid for acceptance. |
| External Claude | PENDING | Need fresh Claude Opus 4.8 Max web/app review of v45; local Claude/review reports are applied repair queues, not final acceptance. |
| GitHub final sync | BLOCKED | Do not final-push as closed until valid web/app GPT and Claude reviews pass and render/visual QA is either completed or explicitly waived. |

## v45 Implemented Items

- Kept v37/v38's user-requested organization: each A-axis title is followed by rubric-derived knowledge/scoring points and then all 2024-2026 related examples.
- Kept full scoring-point output with no fixed per-question or per-A-axis cap.
- Removed source-level old generic front matter and unused old prompt-column function so future generation does not reintroduce generic scaffolding.
- Changed image-backed entries to original-question-image first, then material text, prompt text, rubric, and rubric scoring points.
- Disabled Word table reconstruction for screenshot-backed rows; visible student wording now uses original images first and `表格文字版` only when no screenshot asset exists.
- v45 additionally fixes Markdown heading hierarchy under `相关例题（2024-2026）`.
- v45 applies paragraph-level background consistency for all material, prompt, rubric, scoring-point, and A-axis knowledge/scoring-point paragraphs.
- v45 strips redundant source-label shells such as isolated `【细则】` from displayed rubric/scoring text.
- Regenerated both DOCX/MD deliverables, QA, and Claude review packet for v45.

## Open Boundaries

- v45 is a repaired candidate, not final closure.
- E009, E043, and E051 remain formal point-distribution rubric risks.
- E057 remains a cross-module/background retention decision, not a fully closed 选必二 core item.
- 2026顺义一模第18题 score split remains a source-recovery risk.
- Formal final closure requires GPT-5.5 Pro web/app review and Claude Opus 4.8 Max web/app review, both with no blockers.
- Visual render QA remains blocked by missing LibreOffice/soffice on this machine.
