# ClaudeCode Phase04 Batch03 B Choice Verification Prompt

You are ClaudeCode lane B for Feige Politics Garden 选必三《逻辑与思维》. Continue the current from-zero four-lane run after the subjective Batch03A lane. You are not alone in the codebase: Codex lane A has already produced a local precheck, but your job is independent source verification, not accepting Codex's result.

## Current Run Directory

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

Work from this directory.

## Read First

1. `MASTER_REQUIREMENTS.md`
2. `00_control/NOTEBOOK_DIGEST.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
5. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
6. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
7. `08_review/gpt_phase_advice/phase_04_batch02_gpt55_digest.md`
8. `05_coverage/phase04_batch03_Aonly_queue_plan.md`
9. `codex_lane/phase04_batch03_B_choice_scope_answer_precheck.md` as a challenge aid only, not as authority.

## Batch

Verify exactly:

`05_coverage/phase04_batch03_B_choice_queue.csv`

It has 56 choice rows.

## Mission

For every choice row:

1. recover the full stem and all four option groups from the original paper;
2. pair a reliable objective answer source;
3. decide module boundary: 思维 / 推理 / 交叉 / C-boundary / missing;
4. identify exact reasoning type or thinking-method signal if supported;
5. explain the correct option signal and wrong-option trap/boundary;
6. decide whether it can enter evidence fusion only.

## Hard Requirements

- Do not infer the answer letter from Codex, old output, or explanation alone.
- If the answer key is missing or conflicting, write `B_TARGET_BLOCKED` or `B_TARGET_CONFLICT`.
- If the full options are missing from text extraction, render/inspect the source PDF/Word/PPT/image. Do not give up because one parser fails.
- Pure other-book rows should become `B_TARGET_SCOPE_OUT`, not disappear.
- B-choice-signal can support choice-trap/evidence archive only. It cannot authorize student稿 by itself.
- Student稿, Claude/Opus 成文化, Word/PDF, and final PASS remain forbidden.

## Contamination Guards

- `2024西城一模 Q11`: correct pairing is `B=①③`. If a source or old note still shows `B=①④`, flag it as contamination and do not propagate it.
- `2025海淀二模 Q12/Q13`: answer-source locator must stay explicit if referenced.

## Output Files

Write only:

1. `claudecode_lane/phase04_batch03_B_choice_results.csv`
2. `claudecode_lane/phase04_batch03_B_choice_conflicts.csv`
3. `claudecode_lane/phase04_batch03_B_choice_blockers.md`
4. `04_suite_reports/claudecode_suite_reports/phase04_batch03_B_choice_report.md`
5. `claudecode_lane/phase04_batch03_B_choice_progress.md`

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

Process all 56 rows. The report must include counts by result, evidence level, suite, answer-source status, visual/full-options status, and every conflict/blocker. Do not stop after a sample.
