# ClaudeCode Phase10 Polish Audit Prompt

You are ClaudeCode Lane B for the Feige Politics Garden 选必三《逻辑与思维》四线 workflow.

Use the branch rules from:

- `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`

## Scope

Audit Phase10 polish/outline only. Do not write Word/PDF. Do not mark final PASS. Do not call this a final draft, final manuscript, or completed book.

Phase10 is allowed only because GPT-5.5 Pro Phase09 returned:

`GO_TO_PHASE10_POLISH_OR_OUTLINE_NO_WORD_NO_FINAL`

## Files To Audit

Read these local files:

- `08_review/gpt_phase_advice/phase_09_gpt55_raw.md`
- `08_review/gpt_phase_advice/phase_09_gpt55_digest.md`
- `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- `09_student_draft/phase09_student_draft_control_matrix.csv`
- `09_student_draft/phase10_polished_outline_FROM_29.md`
- `09_student_draft/phase10_polish_control_matrix.csv`
- `09_student_draft/phase10_question_id_traceability_backcheck.csv`
- `09_student_draft/phase10_same_type_index_style_decision.md`
- `09_student_draft/phase10_cross_answer_anchor_patch.md`
- `09_student_draft/phase10_internal_terms_scan.md`
- `09_student_draft/phase10_QID_risk_register.md`
- `08_review/phase10_codexA_polish_verification.md`

You may also read `02_extraction/phase10_build_polished_outline.py` to see whether Phase10 is reproducible.

## Audit Questions

1. Does Phase10 stay locked to the same 29 question rows as Phase09?
2. Did Phase10 expand 74 evidence rows, 45 hold rows, 288 L0 rows, or hard-excluded rows into正文?
3. Does student body avoid internal workflow terms: `Phase09`, `Phase10`, `packet`, `source locator`, `lane`, `Governor`, `Confucius`, `L3`, `L4`, `B-choice-signal`, `LOCKED_FOR_FUSION`, `文件路径`, `细则编号`, local paths?
4. Are choice answers now consistently expressed, especially:
   - `Q-2024朝阳一模-7`: `选 C，②③`
   - `Q-2024朝阳一模-9`: `选 D，③④`
   - `Q-2025丰台期末-8`: `选 D，②④`
   - `Q-2025东城期末-13`: `选 B，①③`
   - `Q-2025顺义一模-7`: `选 A` and 大项不当扩大, not 小项不当扩大
5. Does Phase10 preserve GPT's named risk locks:
   - `Q-2025顺义一模-7`: 大项不当扩大; A 错在说成小项不当扩大; source trace remains audit-side.
   - `Q-2025丰台期末-7`: boundary trap only, not 超前思维正例.
   - `Q-2026顺义一模-19-2`: 科学思维三特征主讲; 推理骨架辅助; not typical 三段论题.
   - `Q-2024朝阳二模-19-1/19-2`: no audit/source/file wording; 第一空/第二空 expression remains.
   - `Q-2024朝阳一模-20-1/20-2` and `Q-2026通州期末-19-2`: sufficient and necessary conditional rules remain separated.
   - `Q-2026丰台一模-18-2`: full chain for 甲 correct / 乙大项不当扩大 wrong remains.
   - `Q-2025海淀二模-20`: angle-pool approach remains; not three fixed mandatory points.
6. Is the same-type index style acceptable: body uses readable titles, control matrix keeps raw QIDs and same_type_visible?
7. Does the traceability backcheck prove every one of the 29 rows has a visible heading?
8. Did Phase10 change knowledge substance, answer pairing, reasoning validity, module ownership, or cross primary/secondary mount beyond allowed polish?
9. Are cross-entry answer anchors sufficient, especially `Q-2026顺义一模-19-2`?
10. Is Phase10 ready for Codex Governor/Confucius gates and GPT review, still with no Word/PDF/final?

## Output Requirements

Write all outputs under:

`claudecode_lane/opus47_phase10_polish_audit/`

Required files:

1. `phase10_laneB_polish_audit.csv`
   - columns: `check_id,severity,status,file_or_area,line_or_row,detail,required_patch`
   - status must be `PASS`, `WARN`, `FAIL`, or `BLOCKED`.
   - severity must be `P0`, `P1`, `P2`, or `P3`.
2. `phase10_laneB_polish_audit.md`
   - include final verdict exactly one of:
     - `PASS_PHASE10_POLISH_AUDIT`
     - `PASS_PHASE10_POLISH_AUDIT_WITH_WARNINGS`
     - `FAIL_PHASE10_POLISH_AUDIT`
     - `BLOCKED_PHASE10_POLISH_AUDIT`
3. `phase10_laneB_polish_audit_findings.csv`
   - only WARN/FAIL/BLOCKED rows; if none, write header plus `NO_FINDINGS`.
4. `phase10_laneB_polish_audit_blockers.md`
   - if no blockers, write `NO_PHASE10_POLISH_BLOCKERS_DETECTED`.
5. `progress.md`
   - short summary, files read, verdict, blockers/warnings.

## Important

- You are not alone in the codebase. Do not revert or overwrite Codex files outside your output directory.
- Do not edit the student draft. Audit only.
- Do not promote Phase10 to Word/PDF/final.
- If a problem is merely polish/readability and not a source or boundary blocker, mark it WARN rather than FAIL.
- If a student-body issue would mislead content, break a QID lock, expand excluded rows, or change an answer, mark it FAIL or BLOCKED.
