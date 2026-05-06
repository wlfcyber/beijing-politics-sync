# ClaudeCode Phase 02 Restart Prompt

You are ClaudeCode running the independent rerun lane for the user's Beijing Gaokao politics 选必一《当代国际政治与经济》 project.

This is a restart after the previous ClaudeCode run hit `413 Request too large (max 32MB)` while handling a large PDF/image payload. Do not repeat that failure.

## Non-Negotiable Runtime Rules

- Do not read `claudecode_lane/logs/claude.stream.json` or any huge debug/log file.
- Do not directly upload/read whole large PDFs, scanned images, or binary Office files into the model.
- For PDF/PPT/DOCX work, use shell extraction tools and save short text extracts, page screenshots, or OCR snippets under `02_extraction/claudecode_extraction_logs/`; only read small, targeted text snippets back into context.
- If extraction is too large or visual-heavy, mark the item as `needs_visual_check` instead of pushing binary/base64 into the model.
- Existing `claudecode_lane/entries/*.md` are provisional drafts, not final evidence. Keep them, but do not treat them as closed.
- You are not alone in the codebase. Do not revert or overwrite Codex files outside `claudecode_lane/` and `02_extraction/claudecode_extraction_logs/`. Write your lane outputs in disjoint files.

## Must Read First

Read only these small control files before work:

- `MASTER_REQUIREMENTS.md`
- `00_control/NOTEBOOK_DIGEST.md`
- `00_control/GOVERNOR_GATES.md`
- `task_plan.md`
- `08_review/codex_response_to_advice.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

Do not read the raw GPT advice as authority. It is already digested by Codex.

## Current Mission

Switch from premature entry writing back to Phase 02:

`选必一主观题源锁定与 P0/P2 证据矩阵建设`

Your goal is to produce an independent evidence matrix from the primary raw roots:

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`

Use `/Users/wanglifei/Desktop/北京高考政治` and `/Users/wanglifei/GaokaoPolitics` only as cache/mirror/source-locator supplements.

## Required Outputs Under claudecode_lane/

Create or update these files:

- `claudecode_lane/phase02_restart_status.md`
- `claudecode_lane/claudecode_source_inventory_phase02.csv`
- `claudecode_lane/claudecode_evidence_level_recheck.csv`
- `claudecode_lane/claudecode_xuanbiyi_subjective_index.csv`
- `claudecode_lane/claudecode_entries_phase02.jsonl`
- `claudecode_lane/claudecode_suite_reports_phase02/`
- `claudecode_lane/claudecode_hard_sample_tongzhou_q20.md`
- `claudecode_lane/claudecode_hard_sample_chaoyang_q17.md`
- `claudecode_lane/claudecode_blockers_phase02.md`
- `claudecode_lane/claudecode_conflicts_suspected.md`

## Required Fields

For every source row, include:

`source_id,year,district_or_exam_scope,exam_type,file_type,raw_category,candidate_evidence_level,verified_evidence_level,contains_xuanbiyi,contains_subjective_question,question_numbers_detected,has_scoring_detail,has_reference_answer,has_teaching_or_lecture,has_pdf_visual_risk,has_ppt_visual_risk,has_image_or_table,needs_ocr,status,blocker`

For every candidate subjective question row, include:

`entry_id,source_id,year,district_or_exam_scope,exam_type,question_no,sub_question_no,question_type,module,unit_or_topic,material_trigger,scoring_term,term_function,why_this_term,answer_landing,evidence_level,evidence_source_type,needs_visual_check,needs_codex_compare,old_final_quality_reference_used,status`

## Evidence Classification

Do not trust filenames. Classify by content:

- `P0_verified_scoring_rule`
- `P0_verified_marking_detail`
- `P0_verified_rubric`
- `P1_reference_answer`
- `P2_teaching_or_lecture`
- `P3_paper_only`
- `unknown_needs_visual_check`
- `excluded_not_relevant`

Special rules:

- `答案及评分参考` is not automatically P0.
- `讲评材料` is not automatically P0.
- PPT answer language is not automatically scoring-rule language.
- Old final artifacts are never evidence.
- 2026石景山期末 is excluded unless a new scoring source appears.
- 2026海淀期末 is user-confirmed no 选必一, but record whether the current-run source check supports that.
- 2026西城期末 Q20 cannot be closed if the original question/paper text is missing. Mark it provisional/blocker until the original prompt is found.

## Hard Samples

Recheck these independently from original sources:

1. `2026通州期末 Q20`: six scoring-term items. Confirm the original question, scoring source, exact point, score, material trigger, and whether each item is P0/P2/user-confirmed.
2. `2026朝阳期中 Q17`: three relationship layers. Confirm total layer plus sublayer evidence, source file, exact scoring position, and module-boundary exclusions.

## Stop Condition

Do not claim final completion. Stop after Phase 02 evidence matrices, hard-sample reviews, blockers, and suspected conflicts are written. If a source is too large or visual-heavy, mark it and continue with other sources.
