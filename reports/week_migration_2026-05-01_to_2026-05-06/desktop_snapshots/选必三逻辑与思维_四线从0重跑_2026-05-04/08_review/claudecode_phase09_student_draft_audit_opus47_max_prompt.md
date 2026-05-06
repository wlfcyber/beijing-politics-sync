# ClaudeCode Lane B Phase09 Controlled Student Draft Audit Prompt

Runtime requirement:

- Real Claude Opus 4.7 maximum/adaptive thinking.
- Caller launches with `--model opus --effort max`.
- This is audit-only. Do not write student稿正文, final稿, Word/PDF, final PASS, or 宝典成品.

## Role

You are ClaudeCode Lane B, independent audit lane. Audit Codex A's Phase09 controlled student-draft candidate for 选必三《逻辑与思维》.

You are not asked to rewrite the draft. You must not modify files outside your audit output directory.

## Run Directory

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## Read Inputs

Read these files:

1. `MASTER_REQUIREMENTS.md`
2. `08_review/gpt_phase_advice/phase_08_gpt55_digest.md`
3. `08_review/gpt_phase_advice/phase_08_gpt55_raw.md`
4. `05_coverage/phase08_opus_prototype_input_freeze.csv`
5. `05_coverage/phase08_opus_prototype_input_freeze.md`
6. `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv`
7. `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md`
8. `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
9. `09_student_draft/phase09_student_draft_control_matrix.csv`
10. `09_student_draft/phase09_question_id_backcheck.csv`
11. `09_student_draft/phase09_opus_or_codex_change_log.csv`
12. `09_student_draft/phase09_internal_terms_scan.md`
13. `09_student_draft/phase09_QID_risk_register.md`
14. `08_review/phase09_codexA_student_draft_verification.md`
15. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`

## Write Outputs

Write only to:

`claudecode_lane/opus47_phase09_student_draft_audit/`

Required files:

1. `phase09_laneB_student_draft_audit.csv`
2. `phase09_laneB_student_draft_audit.md`
3. `phase09_laneB_student_draft_audit_findings.csv`
4. `phase09_laneB_student_draft_audit_blockers.md`
5. `progress.md`

## Audit Checklist

Audit at least these checks:

P0:

1. Required Phase09 files exist.
2. Control matrix has exactly 29 rows and question_id set exactly equals the Phase08 input freeze.
3. Student draft is built from the 29 Phase08 prototype rows only; no 74-row evidence pool expansion, no 45 hold-row expansion, no 288 L0-row expansion.
4. No hard-excluded row is expanded into正文: `Q-2024西城一模-11`, `Q-2025海淀二模-12`, `Q-2025海淀二模-13`, `Q-2026顺义一模-3` may appear only as same-type/index references and not with answers or explanations.
5. No old wrong Q11 pairing such as `B=①④` or `B（①④）`.
6. No student-draft body contains forbidden internal terms: `Phase07`, `Phase08`, `packet`, `source locator`, `lane`, `Governor`, `Confucius`, `L3`, `L4`, `B-choice-signal`, `LOCKED_FOR_FUSION`, `primary_reasoning_type`, `rule_slogan`, `/Users/`, `@L`, raw file paths, source-file ids such as `细则31` or `细则022`.
7. No final-artifact authorization in student draft: `final PASS`, `终稿`, `最终稿`, `宝典成品`, `Word/PDF`.
8. `Q-2025丰台期末-7` is in boundary-trap/easy-misdiagnosis treatment, not a positive 选必三思维方法 mainline example.
9. `Q-2025顺义一模-7` is corrected: A's real issue is 大项不当扩大, not 小项不当扩大; the draft must not preserve the contradictory Phase08 expression.
10. `Q-2026顺义一模-19-2` is scientific-thinking primary, reasoning auxiliary only; not treated as a typical三段论题.
11. `Q-2026丰台一模-18-2` preserves the locked reasoning/action chain: 甲 = 必要条件假言推理肯定后件式 with true premises; 乙 = 三段论大项不当扩大.
12. `Q-2025海淀二模-20` keeps angle-pool/选二写深 treatment; it must not become 三点全必答 or `3点乘2分`.
13. `Q-2024朝阳一模-20-1`, `Q-2024朝阳一模-20-2`, and `Q-2026通州期末-19-2` clearly separate sufficient-condition and necessary-condition valid/invalid forms.
14. `Q-2024朝阳二模-19-1` and `Q-2024朝阳二模-19-2` do not contain source ids, file ids, rubric ids, or audit-flavored wording.

P1:

15. Thinking entries preserve the transfer schema: 材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题.
16. Reasoning entries preserve the transfer schema: 题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点 -> 易错陷阱 -> 同类题.
17. Choice questions show explicit answer letters and combinations when available, e.g. `正确选项 C（②③）`, `选 A`.
18. Chinese quotation marks are clean enough for student use; no obvious `“...“` broken quote pairs in body.
19. Cross rows preserve dual mount in the control matrix and readable draft sections.

P2/P3:

20. Note content, style, readability, or transfer risks, but do not patch them.

## Output Format

In `phase09_laneB_student_draft_audit.csv`, use columns:

```text
check_id,severity,status,evidence,comment
```

Statuses: `PASS`, `WARN`, `FAIL`, `BLOCK`.

In `phase09_laneB_student_draft_audit_findings.csv`, use columns:

```text
finding_id,severity,location,issue,requested_action
```

If no blockers, `phase09_laneB_student_draft_audit_blockers.md` must contain:

`NO_PHASE09_STUDENT_DRAFT_BLOCKERS_DETECTED`

End `phase09_laneB_student_draft_audit.md` with one verdict:

- `PASS_PHASE09_STUDENT_DRAFT_AUDIT`
- `PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS`
- `FAIL_PHASE09_STUDENT_DRAFT_AUDIT`
- `BLOCK_PHASE09_STUDENT_DRAFT_AUDIT`

Remember: this audit does not authorize Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品.
