# ClaudeCode Phase04 Batch03 A-only Subjective Verification Prompt

You are ClaudeCode lane B for Feige Politics Garden 选必三《逻辑与思维》. Continue the current from-zero four-lane run. You are not alone in the codebase: Codex lane A is working in parallel. Do not revert, overwrite, or silently reshape Codex files outside the explicit write set below. Preserve raw outputs and add your own lane-B files.

## Current Run Directory

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

Work from this directory.

## Highest Rules To Read First

1. `MASTER_REQUIREMENTS.md`
2. `00_control/NOTEBOOK_DIGEST.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
5. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
6. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
7. `08_review/gpt_phase_advice/phase_04_batch02_gpt55_digest.md`
8. `05_coverage/phase04_batch02_status_freeze.md`

## GPT Batch02 Binding Direction

GPT-5.5 Pro gave `GO_TO_BATCH03_AONLY_QUEUE`.

This means:

- Batch02 visual/scope repair is accepted only as targeted evidence-control progress.
- The next priority is the remaining A-only/L1 queue, not writing a student document.
- Existing 17 L3/L4 rows may be used only as internal evidence-pool checks.
- Student稿, Claude/Opus 成文化, Word/PDF, and final PASS are still forbidden.

## Your Batch

Verify exactly the first Batch03 queue:

`05_coverage/phase04_batch03_A_subjective_queue.csv`

It has 56 rows. Treat every row as A-only pending B verification. Do not skip rows because they look like another book or module; if out of scope, record it explicitly as `B_TARGET_SCOPE_OUT` with the boundary reason. Do not silently delete it.

## What To Do For Each Row

For each row, return to the source indicated by `source_id` / `stable_locator`. Use cached extracted text first, but cache-first is not cache-only:

- if the text is corrupt, incomplete, missing options, missing subquestions, missing rubrics, or visually suspicious, open/render/OCR/inspect the original PDF/Word/PPT/image/source file;
- use Python/Office extraction, PDF rendering, XML extraction, OCR/vision, screenshot, or any local tool needed;
- do not give up merely because one tool fails.

For each row verify:

1. full question/subquestion prompt;
2. module boundary: 思维, 推理, 交叉, C-boundary, or missing;
3. answer/rubric/marking source pairing;
4. whether the evidence is formal rubric, support source, choice-signal, or only reference/inventory;
5. exact thinking method or reasoning type, if supported;
6. trap/boundary note;
7. whether it can enter evidence fusion only.

## Evidence Rules

- `A-formal`: formal scoring rubric, marking rule, evaluation/阅卷/评标 report, or explicit scoring source matched to the suite/question.
- `A-support`: lecture/讲评 material with explicit scoring口径, not formal rubric.
- `B-choice-signal`: choice question with paper text plus reliable objective answer key. This batch is subjective, so use this only if a row turns out to be a choice row.
- `C-boundary`: source exists but it is another module/book or pure non-target task.
- `missing`: source, question, answer/rubric, OCR, visual confirmation, or boundary is not reliable enough.

Never promote ordinary reference answers into formal rubrics. If a source is only a reference answer, record that boundary.

## Hard Contamination Guards

- `2024西城一模 Q11` correct pairing is `B=①③`; if any file you read says or implies the old Codex A error `B=①④`, flag contamination and keep the Lane B corrected pairing in conflict notes.
- `2025海淀二模 Q12/Q13` must retain answer-source locators if mentioned; no source-free lock.
- Archive skeletons are internal check tools only. Do not write student prose.
- Do not create or edit final student docs, Word, PDF, or delivery files.

## Required Output Files

Write these files only:

1. `claudecode_lane/phase04_batch03_A_subjective_results.csv`
2. `claudecode_lane/phase04_batch03_A_subjective_conflicts.csv`
3. `claudecode_lane/phase04_batch03_A_subjective_blockers.md`
4. `04_suite_reports/claudecode_suite_reports/phase04_batch03_Aonly_subjective_report.md`
5. append a dated entry to `claudecode_lane/progress.md`

CSV header for results:

```csv
target_id,suite_id,qno,question_type,section_scope,laneB_result,evidence_level,visual_status,answer_status,rubric_status,node,logical_or_method_form,rule_slogan,trap_or_boundary,can_enter_fusion,can_enter_student_draft,blocker_reason,source_evidence,notes
```

Allowed `laneB_result` values:

- `B_TARGET_CONFIRMED`
- `B_TARGET_BLOCKED`
- `B_TARGET_NEEDS_VISUAL`
- `B_TARGET_SCOPE_OUT`
- `B_TARGET_CONFLICT`

`can_enter_student_draft` must be `no` for every row.

## Completion Standard

Do not stop after a sample. Process all 56 rows. The report must include:

- total processed count;
- counts by `laneB_result`;
- counts by evidence level;
- suites processed;
- every blocker/conflict;
- rows that can enter evidence fusion only;
- rows that must remain blocked/scope-out;
- confirmation that no student稿/Word/PDF/final PASS was created.
