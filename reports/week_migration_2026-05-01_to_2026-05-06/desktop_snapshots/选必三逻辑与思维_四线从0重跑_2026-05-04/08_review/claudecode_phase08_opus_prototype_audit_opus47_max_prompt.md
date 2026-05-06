# ClaudeCode Lane B Phase08 Opus Prototype Audit Prompt

Runtime requirement:

- Real Claude Opus 4.7 maximum/adaptive thinking.
- Caller launches with `--model opus --effort max`.
- This is audit-only. Do not write student稿, final稿, Word/PDF, final PASS, or 宝典成品.

## Role

You are ClaudeCode Lane B, independent audit lane. Audit the Phase08 Opus review-only teaching prototype produced by the Claude Opus teaching-text lane.

You are not asked to rewrite the prototype. You must not modify files outside your audit output directory.

## Run Directory

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## Read Inputs

Read these files:

1. `MASTER_REQUIREMENTS.md`
2. `05_coverage/phase08_opus_prototype_input_freeze.csv`
3. `05_coverage/phase08_opus_prototype_input_freeze.md`
4. `05_coverage/phase07_locked_opus_input_packet.csv`
5. `05_coverage/phase07_L0_excluded_from_opus_input.csv`
6. `06_conflicts/phase07_laneB_warning_patch_freeze.md`
7. `08_review/gpt_phase_advice/phase_07_gpt55_digest.md`
8. `08_review/claude_opus_phase08_teaching_prototype_prompt.md`
9. `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md`
10. `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv`
11. `07_student_prototype/phase08_opus_change_log.md`
12. `07_student_prototype/phase08_opus_change_log.csv`
13. `opus_writer/phase08_teaching_prototype/phase08_opus_boundary_compliance.md`
14. `opus_writer/phase08_teaching_prototype/progress.md`
15. `08_review/phase08_codexA_opus_prototype_verification.md`
16. `08_review/phase08_codexA_opus_prototype_verification.csv`
17. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`

## Write Outputs

Write only to:

`claudecode_lane/opus47_phase08_prototype_audit/`

Required files:

1. `phase08_laneB_opus_prototype_audit.csv`
2. `phase08_laneB_opus_prototype_audit.md`
3. `phase08_laneB_opus_prototype_audit_findings.csv`
4. `phase08_laneB_opus_prototype_audit_blockers.md`
5. `progress.md`

## Audit Checklist

Audit at least these checks:

P0:

1. Required 6 Opus files exist.
2. Prototype CSV has exactly 29 rows and exact required columns.
3. Change log CSV has exactly 29 rows and exact required columns.
4. Prototype question_id set exactly equals Phase08 input freeze question_id set.
5. No hold row appears as a prototype row.
6. No L0 row appears as a prototype row.
7. `student_permission=no`, `word_pdf_permission=no`, `final_pass_permission=no` remain visible.
8. Change log sentinels are all `must_be_no`.
9. `Q-2024西城一模-11` does not appear as a prototype row and old wrong `B=①④` does not appear as correct result.
10. `Q-2025海淀二模-12` and `Q-2025海淀二模-13` do not appear as prototype rows.
11. `Q-2026顺义一模-3` does not enter reasoning prototype.
12. `Q-2026丰台一模-18-2` keeps the Phase07 patched reasoning/action/locator boundary.
13. No generated_text contains forbidden internal terms: `source locator`, `lane`, `Governor`, `Confucius`, `packet`, `L3`, `L4`, `/Users/`, `@L`, `Slide`.
14. No generated_text contains final-artifact authorization such as `final PASS`, `Word/PDF`, `宝典成品`, `终稿`, `最终稿`.

P1:

15. Cross rows visibly preserve double-mount policy.
16. Reasoning rows do not collapse into generic推理知识点总论; they keep题型/规则/陷阱/同类/动作.
17. Thinking rows do not collapse into generic知识摘要; they keep材料信号/可写方法/为什么能想到/答题动作/答案落点.
18. Same-type IDs are presented as IDs only when their answer evidence is not in the prototype row.
19. Review-only body has no source paths or raw locators.

P2/P3:

20. Note style/readability or transfer risks, but do not patch them.

## Output Format

In `phase08_laneB_opus_prototype_audit.csv`, use columns:

```text
check_id,severity,status,evidence,comment
```

Statuses: `PASS`, `WARN`, `FAIL`, `BLOCK`.

In `phase08_laneB_opus_prototype_audit_findings.csv`, use columns:

```text
finding_id,severity,location,issue,requested_action
```

If no blockers, `phase08_laneB_opus_prototype_audit_blockers.md` must contain:

`NO_PHASE08_PROTOTYPE_BLOCKERS_DETECTED`

End `phase08_laneB_opus_prototype_audit.md` with one verdict:

- `PASS_PHASE08_PROTOTYPE_AUDIT`
- `PASS_PHASE08_PROTOTYPE_AUDIT_WITH_WARNINGS`
- `FAIL_PHASE08_PROTOTYPE_AUDIT`
- `BLOCK_PHASE08_PROTOTYPE_AUDIT`

Remember: this audit does not authorize student稿, Word/PDF, final PASS, or 宝典成品.
