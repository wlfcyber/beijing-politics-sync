# Phase09 Prompt For GPT-5.5 Pro
请审查 Phase09：这是选必三《逻辑与思维》从0重跑的“受控学生稿草案”阶段。请只判断下一阶段是否可以进入 Phase10 polish/outline（仍不得 Word/PDF/final），或是否必须继续 patch Phase09。
你的输出必须以以下四个标签之一开头：

- GO_TO_PHASE10_POLISH_OR_OUTLINE_NO_WORD_NO_FINAL
- PATCH_PHASE09_BEFORE_NEXT_STAGE
- RUN_ADDITIONAL_LANEB_AUDIT
- STOP_SOURCE_REPAIR_REQUIRED

请列出具体 question_id 风险、边界风险、下一阶段硬规则。不要说“我会”。


---

## FILE: `08_review/phase09_GPT_commander_review_packet.md`

# Phase09 GPT Commander Review Packet

## Requested Verdict

Ask GPT-5.5 Pro to judge whether Phase09 can proceed beyond controlled student draft, or whether it needs another local patch.

Allowed verdict labels:

- `GO_TO_PHASE10_POLISH_OR_OUTLINE_NO_WORD_NO_FINAL`
- `PATCH_PHASE09_BEFORE_NEXT_STAGE`
- `RUN_ADDITIONAL_LANEB_AUDIT`
- `STOP_SOURCE_REPAIR_REQUIRED`

## Current State

- Codex A generated a controlled student-draft candidate from the 29 Phase08 prototype rows only.
- Student draft: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- Control matrix: `09_student_draft/phase09_student_draft_control_matrix.csv`
- Codex A verification: `08_review/phase09_codexA_student_draft_verification.md` = `PASS_CODEXA_PHASE09_CONTROLLED_DRAFT`
- ClaudeCode Lane B audit: `PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS`
- Lane B blockers: `NO_PHASE09_STUDENT_DRAFT_BLOCKERS_DETECTED`
- Lane B warning patch: `08_review/phase09_laneB_warning_patch_resolution.md` = `PASS_CODEXA_PHASE09_AFTER_LANEB_PATCH`
- Governor gate: `PASS_PHASE09_GOVERNOR_BOUNDARY_PENDING_GPT`
- Confucius gate: `PASS_PHASE09_CONFUCIUS_LEARNING_VALUE_PENDING_GPT`

## Counts

- input rows: 29
- draft/control rows: 29
- modules: 思维 13, 推理 11, 交叉 5
- draft sections: 思维 12, 边界陷阱 1, 推理 11, 交叉 5
- forbidden student terms: 0
- Q11 wrong pairing hits: 0
- hard-excluded expansion failures: 0
- all 29 freeze rows visible-title matched in backcheck: yes

## GPT Phase08 Must-Fix Follow-Through

- `Q-2025丰台期末-7`: moved to boundary trap; not a positive 选必三思维 method example.
- `Q-2025顺义一模-7`: corrected to 大项不当扩大; risk register records source trace.
- `Q-2026顺义一模-19-2`: scientific-thinking primary; reasoning auxiliary only.
- `Q-2024朝阳二模-19-1/19-2`: audit/source/file-id wording removed.
- `Q-2024朝阳一模-20-1/20-2` and `Q-2026通州期末-19-2`: sufficient/necessary conditional forms separated.
- `Q-2026丰台一模-18-2`: locked 甲/乙 reasoning chain preserved.
- `Q-2025海淀二模-20`: angle-pool / choose-two writing preserved.
- Hard-excluded rows remain index-only or absent.

## Still Blocked Unless GPT Explicitly Opens Next Gate

- Word
- PDF
- final PASS
- 终稿 / 最终稿 / 宝典成品
- Expanding from 29 rows to 74 evidence rows
- Adding 45 hold rows
- Adding 288 L0 rows
- Expanding hard-excluded rows into answers/explanations

## Files GPT Should Review

1. `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
2. `09_student_draft/phase09_student_draft_control_matrix.csv`
3. `09_student_draft/phase09_question_id_backcheck.csv`
4. `09_student_draft/phase09_internal_terms_scan.md`
5. `09_student_draft/phase09_QID_risk_register.md`
6. `08_review/phase09_codexA_student_draft_verification.md`
7. `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md`
8. `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit_findings.csv`
9. `08_review/phase09_laneB_warning_patch_resolution.md`
10. `08_review/phase09_Governor_student_draft_boundary_gate.md`
11. `08_review/phase09_Confucius_learning_value_gate.md`

## Question For GPT

Does the patched Phase09 controlled student draft pass the student-draft gate and move to Phase10 polishing/outline under continued no-Word/no-final constraints, or must Phase09 be patched again?


---

## FILE: `08_review/phase09_Governor_student_draft_boundary_gate.md`

# Phase09 Governor Student Draft Boundary Gate

- gate_time: 2026-05-05 CST
- target_draft: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- control_matrix: `09_student_draft/phase09_student_draft_control_matrix.csv`
- codex_verification: `08_review/phase09_codexA_student_draft_verification.md`
- laneB_audit: `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md`
- laneB_patch_resolution: `08_review/phase09_laneB_warning_patch_resolution.md`

## Boundary Checks

- 29 Phase08 prototype rows only: PASS.
- No 74-row evidence-pool expansion: PASS.
- No 45 hold-row expansion: PASS.
- No 288 L0-row expansion: PASS.
- Hard-excluded rows not expanded: PASS.
- Q11 wrong pairing absent: PASS.
- Internal terms absent from student body: PASS.
- Word/PDF/final PASS/终稿/最终稿/宝典成品 authorization absent: PASS.
- Lane B P0 checks: PASS.
- Lane B blockers: `NO_PHASE09_STUDENT_DRAFT_BLOCKERS_DETECTED`.
- Lane B warnings patched or explicitly controlled: PASS.

## Named-Risk Controls

- `Q-2025丰台期末-7`: boundary-trap only, not positive 选必三思维 mainline.
- `Q-2025顺义一模-7`: corrected to 大项不当扩大 with source trace.
- `Q-2026顺义一模-19-2`: scientific-thinking primary, reasoning auxiliary.
- `Q-2024朝阳一模-20-1`, `Q-2024朝阳一模-20-2`, `Q-2026通州期末-19-2`: sufficient/necessary conditional rules separated.
- `Q-2026丰台一模-18-2`: locked 甲/乙 reasoning chain preserved.
- `Q-2025海淀二模-20`: angle-pool / choose two and write deep preserved.

## Verdict

`PASS_PHASE09_GOVERNOR_BOUNDARY_PENDING_GPT`

This gate only permits Phase09 GPT review. It does not authorize Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品.


---

## FILE: `08_review/phase09_Confucius_learning_value_gate.md`

# Phase09 Confucius Learning Value Gate

- gate_time: 2026-05-05 CST
- target_draft: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- laneB_audit: `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md`
- patch_resolution: `08_review/phase09_laneB_warning_patch_resolution.md`

## Learning-Value Checks

- 思维部分 uses transfer schema: 材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题: PASS.
- 推理部分 uses transfer schema: 题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点 -> 易错陷阱 -> 同类题: PASS.
- 交叉题 keeps dual lines and tells students which line is main: PASS.
- 选择题 has explicit answer letters/combinations where available: PASS.
- 主观题 keeps at least one answer-paper usable action sentence: PASS.
- Boundary traps are marked rather than silently mixed into positive examples: PASS.
- Same-type IDs remain index-only and do not leak unverified answer content: PASS.
- Chinese quotation usage is clean enough for continued drafting: PASS.

## Residual Teaching Notes

- Phase09 is still a controlled student-draft candidate, not a polished final student handout.
- Later stages should decide whether to expose raw Q-IDs in headings or keep readable titles plus control-matrix traceability.
- Later stages may further add answer anchors to all cross sections if GPT requests a stricter schema.

## Verdict

`PASS_PHASE09_CONFUCIUS_LEARNING_VALUE_PENDING_GPT`

This gate only permits GPT Phase09 review. It does not authorize Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品.


---

## FILE: `08_review/phase09_codexA_student_draft_verification.md`

# Phase09 Codex A Student Draft Verification

- verdict: `PASS_CODEXA_PHASE09_CONTROLLED_DRAFT`
- student_draft: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- control_matrix: `09_student_draft/phase09_student_draft_control_matrix.csv`
- input_rows: 29
- draft_rows: 29
- module_counts: {'思维': 13, '推理': 11, '交叉': 5}
- status_counts: {'L3_candidate': 25, 'L4': 4}
- draft_section_counts: {'思维': 12, '边界陷阱': 1, '推理': 11, '交叉': 5}

## Checks

- row_count_29: PASS
- id_set_equals_phase08_freeze: PASS
- no_forbidden_student_terms: PASS
- no_q11_wrong_pairing: PASS
- hard_excluded_reference_only: PASS
- q2025_shunyi_7_corrected_to_da_xiang: PASS
- q2025_fengtai_7_boundary_trap: PASS
- q2026_shunyi_19_2_scientific_primary: PASS

## Boundary Notes

- This Phase09 draft is still a controlled student-draft candidate only.
- It does not authorize Word/PDF, final PASS, final wording, or expansion beyond the 29 Phase08 prototype rows.
- Same-type IDs are index references only and are not expanded into answers.


---

## FILE: `08_review/phase09_laneB_warning_patch_resolution.md`

# Phase09 Lane B Warning Patch Resolution

- source_audit: `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md`
- source_findings: `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit_findings.csv`
- laneB_verdict: `PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS`
- blockers: `NO_PHASE09_STUDENT_DRAFT_BLOCKERS_DETECTED`
- patch_method: patched generator `02_extraction/phase09_build_controlled_student_draft.py` and regenerated all Phase09 student-draft artifacts.
- post_patch_codex_verification: `08_review/phase09_codexA_student_draft_verification.md` = `PASS_CODEXA_PHASE09_CONTROLLED_DRAFT`

## Resolution Summary

P0 all passed in Lane B and remained unchanged after patch. The patch addressed every P1/P2 action item that affected the student draft body or audit traceability:

- F1: added missing same-type index for `Q-2026顺义一模-19-2`.
- F2: removed `思维挂载` residue from student-facing prose.
- F3: removed double terminal punctuation after the 联言判断 rule quote.
- F4: unified fill-in-blank wording as `第一空 / 第二空`.
- F5: upgraded backcheck with visible-title matching.
- F6: replaced meta `推理结构辅助线` with concrete `三段论 / 判断 / 推理` auxiliary wording.
- F7: added safe answer anchors to cross reasoning-primary sections.
- F8: accepted readable titles plus Q-ID index lists as a deliberate student/audit balance; traceability is now carried by `visible_title_match`.
- F9: added explicit source trace for the `Q-2025顺义一模-7` 大项不当扩大 correction.

## Post-Patch Checks

- `rg 思维挂载|推理结构辅助线|前半处|后半处|确为小项不当扩大|B=①④|B（①④）` on the student draft: 0 hits.
- `phase09_internal_terms_scan.md`: forbidden term hits = 0; Q11 wrong pairing hit = NO; hard-excluded expansion failures = 0.
- `phase09_question_id_backcheck.csv`: all 29 Phase08 freeze rows have `visible_title_match=yes`; hard-excluded reference checks remain PASS.

## Status

`PASS_CODEXA_PHASE09_AFTER_LANEB_PATCH`


---

## FILE: `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md`

# Phase09 Lane B Student Draft Audit

- audit_lane: ClaudeCode Lane B (Opus 4.7 maximum/adaptive thinking)
- audit_scope: review-only audit of Phase09 controlled student-draft candidate
- target_directory: `RUN_ROOT_LOCAL_REDACTED`
- audit_target_md: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- audit_target_matrix: `09_student_draft/phase09_student_draft_control_matrix.csv`
- frozen_input_freeze: `05_coverage/phase08_opus_prototype_input_freeze.csv` (29 rows)
- audit_does_not_authorize: Word, PDF, final PASS, 终稿, 最终稿, 宝典成品

## Counts

- control_matrix data rows: 29
- frozen input rows: 29
- student draft entry sections: 29 (思维 12 + 边界陷阱 1 + 推理 11 + 交叉 5)
- module distribution per matrix: 思维=13, 推理=11, 交叉=5 (matches Phase08 freeze allowed module distribution)
- L4 rows: 4 (Q-2025海淀二模-20, Q-2025西城二模-16-2, Q-2025西城二模-16-3, Q-2026丰台一模-18-2)
- L3 rows (status `L3_candidate`): 25
- hard-excluded references in body: Q-2024西城一模-11 (1), Q-2025海淀二模-12 (1), Q-2026顺义一模-3 (3) — all index-only, no answer expansion; Q-2025海淀二模-13 not in file at all

## P0 Audit Result Summary

| check | status |
|---|---|
| P0_01 required Phase09 files exist | PASS |
| P0_02 control matrix 29 rows + QID set equals freeze | PASS |
| P0_03 draft built from 29 prototype rows only | PASS |
| P0_04 no hard-excluded row expansion | PASS |
| P0_05 no old wrong Q11 pairing | PASS |
| P0_06 no forbidden internal terms | PASS |
| P0_07 no final-artifact authorization | PASS |
| P0_08 Q-2025丰台期末-7 in boundary trap | PASS |
| P0_09 Q-2025顺义一模-7 corrected to 大项不当扩大 | PASS |
| P0_10 Q-2026顺义一模-19-2 scientific primary | PASS |
| P0_11 Q-2026丰台一模-18-2 locked chain preserved | PASS |
| P0_12 Q-2025海淀二模-20 angle pool 选二写深 | PASS |
| P0_13 sufficient/necessary conditional split | PASS |
| P0_14 Q-2024朝阳二模-19-1/19-2 no audit-flavored wording | PASS |

All 14 P0 checks PASS. No blockers detected.

## P1 Audit Result Summary

| check | status |
|---|---|
| P1_15 thinking entries preserve schema | WARN (see F1) |
| P1_16 reasoning entries preserve schema | PASS |
| P1_17 choice answer letters explicit | PASS |
| P1_18 Chinese quotation marks clean | PASS |
| P1_19 cross rows preserve dual mount | PASS |

P1 has one WARN tied to a single missing `同类题索引` line in cross entry Q-2026顺义一模-19-2 (see Finding F1).

## P2/P3 Risk Notes

- F1 (P1): Q-2026顺义一模-19-2 missing `同类题索引` line; matrix has same_type_ids='Q-2024朝阳期中-7；Q-2026顺义一模-19-1' but body does not render them.
- F2 (P1): Internal jargon `思维挂载` leaked into student-facing body at line 303; rest of cross sections use `主讲线/辅助线`.
- F3 (P2): Double-period punctuation at line 297 (`一假即假。”。`).
- F4 (P2): Mixed fill-in-blank terminology (`前半处/后半处` vs `第一空/第二空`) inside Q-2024朝阳二模-19-1 section.
- F5 (P2): `phase09_question_id_backcheck.csv` reports `appears_in_student_md=no` for 5 entry control rows because it greps the raw QID literal; the entries do exist under Chinese readable visible_titles. Backcheck is technically accurate but misleading.
- F6 (P2): `推理结构辅助线` at line 350 is meta-talk; other cross 辅助线 题型 names are concrete.
- F7 (P3): Cross 推理-primary 主讲线 sections omit `答案落点` element; schema-reduced cross style is internally consistent but loses one卷面作答 anchor.
- F8 (P3): Visible titles drop the raw question_id; same-type index lists keep raw QIDs. Mix of two reference styles in the same student-facing document.
- F9 (P3): Q-2025顺义一模-7 underwent a substantive answer-interpretation change between Phase08 (`小项不当扩大`) and Phase09 (`大项不当扩大`, A误说成小项不当扩大). Codex A reports PASS; Lane B did not re-read 036顺义参考答案. Recommend Governor/Confucius re-check before final稿.

All P2/P3 notes are observations; none are blockers.

## What Is Verified

- All 29 frozen prototype rows are present in body and control_matrix; no extra/missing rows.
- No 74-row evidence pool, 45-hold-row, 288-L0-row, or hard-excluded-row expansion into body content.
- Hard-excluded IDs (Q-2024西城一模-11, Q-2025海淀二模-12, Q-2026顺义一模-3) appear only as same-type index references with no answer/option/explanation. Q-2025海淀二模-13 not in file at all.
- All GPT-flagged must-fix items resolved: boundary trap reposition, 大项不当扩大 correction, scientific-primary inversion, audit-wording cleanup, sufficient/necessary split, L4 chain preservation, angle pool preservation.
- All choice questions render explicit answer letters (and combinations where applicable).
- All cross entries preserve dual-mount structure in matrix and body.
- No forbidden internal terms (`Phase07/08`, `packet`, `lane`, `Governor`, `Confucius`, `L3/L4`, `B-choice-signal`, `LOCKED_FOR_FUSION`, `/Users/`, `@L`, `细则\\d+`) in body.
- No final-artifact authorization claims (`final PASS`, `终稿`, `最终稿`, `宝典成品`, `Word/PDF`).

## What This Audit Does Not Authorize

- Word document generation
- PDF rendering
- final PASS / 终稿 / 最终稿 / 宝典成品 labels
- Expansion beyond the 29 frozen Phase08 prototype rows
- Promotion of any hold row, L0 row, or hard-excluded row into body content
- Auto-expansion of same-type IDs into answer text

## Boundary Reminder

This audit is review-only. The Phase09 student draft remains a controlled candidate. Any next step (Governor/Confucius gates, GPT review, Word/PDF rendering, final PASS) requires its own gate authorization independent of this audit.

## Verdict

PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS


---

## FILE: `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit_findings.csv`

finding_id,severity,location,issue,requested_action
F1,P1,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md lines 341-353 (Q-2026顺义一模-19-2 cross section)","'同类题索引' line missing entirely from this section. control_matrix entry 29 same_type_ids field has 'Q-2024朝阳期中-7；Q-2026顺义一模-19-1' but neither value is rendered in body. All other 28 entries (including the 4 other cross entries) carry a '同类题索引' line at end of section.","Add a final body line under the cross section, e.g. '- 同类题索引：Q-2024朝阳期中-7；Q-2026顺义一模-19-1。'. Place it after the 辅助线 block to match the placement used in Q-2024朝阳二模-19-1/19-2/期中-9/顺义一模-19-1."
F2,P1,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md line 303","Internal jargon '思维挂载' leaked into student-facing body: '题型：辩证思维 · 动态性(同题第(1)问的思维挂载延续)'. Rest of the cross sections use 主讲线/辅助线 wording for student readability; '挂载' is residue from Phase08 prototype text.","Rewrite line 303 using student-friendly phrasing, e.g. '题型：辩证思维 · 动态性（与第(1)问辅助线一致）' or just '题型：辩证思维 · 动态性'. Run a follow-up grep for '挂载' to confirm zero hits."
F3,P2,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md line 297","Double terminal punctuation: '规则口诀：“当且仅当各联言支都真，联言判断才真；一假即假。”。' has '。' inside the closing quote and again outside. Cosmetic but noticeable for student稿.","Drop the trailing '。' outside the closing 中文 quote so the line reads '规则口诀：“当且仅当各联言支都真，联言判断才真；一假即假。”'."
F4,P2,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md lines 281-283 (Q-2024朝阳二模-19-1 主讲线)","Mixed fill-in-blank terminology within same section: lines 281-282 use '前半处' / '后半处', line 283 '易错陷阱' uses '第一空' / '第二空'. Both refer to the same blanks; inconsistency hurts readability.","Pick one wording and apply it across the whole 19-1 section. Recommend '第一空 / 第二空' since '空' is the standard term for fill-in-blank slots; or align both with '前半处 / 后半处' if that wording was intentional."
F5,P2,"09_student_draft/phase09_question_id_backcheck.csv rows for Q-2024朝阳期中-9, Q-2025丰台期末-7, Q-2025丰台期末-8, Q-2025西城二模-16-2, Q-2026丰台一模-18-2","appears_in_student_md='no' is reported for these 5 entry control rows because the search looks for the raw 'Q-...' string. In reality each entry has a body section under Chinese readable visible_title (e.g. '2024 朝阳期中第9题（选择题）'). Pure literal-match yields a misleading 'no'.","Either (a) extend backcheck to also search for the visible_title heading and split into two columns 'qid_literal_match' and 'visible_title_match', or (b) annotate the 'no' rows with the actual visible_title line number so future audit回查 is not misled. Lane B verified all 5 entries are present and correct."
F6,P2,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md line 350 (Q-2026顺义一模-19-2 辅助线)","'题型：推理结构辅助线' is meta-description rather than a concrete reasoning题型 name. Other cross entries use a concrete name (e.g. '辩证思维 · 动态性', '思维抽象 / 思维具体', '科学思维(对前提真实性、推理结构正确性的客观要求)').","Rewrite as a concrete 题型, e.g. '题型：三段论 / 判断 / 推理（作为科学思维三特征落地的推理骨架）' to match the concreteness of other cross entries' aux mounts."
F7,P3,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md (cross 主讲线 entries Q-2024朝阳二模-19-1, 19-2, 期中-9, 顺义一模-19-1)","Cross 推理-primary 主讲线 sections lack '答案落点' element while standalone 推理 entries carry it. Schema-reduced cross style is internally consistent, but loses one卷面作答 anchor for cross items.","Optional: add a one-line '答案落点' to each cross 主讲线 to match standalone 推理 entries. Not required for current gate but worth raising for readability uplift before final稿."
F8,P3,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md (cross sections), 09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md headers","Visible titles in body use Chinese readable format and lose explicit question_id traceability for entry control rows. Same-type index lists still use raw 'Q-...' format, mixing two reference styles within the same student-facing document.","Optional: align reference style — either add the raw question_id to each section header (audit-friendly) or convert same-type lists to readable Chinese format (student-friendly). Current mix is acceptable but worth deciding before final稿."
F9,P3,"09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md Q-2025顺义一模-7 section (lines 238-247)","Substantive answer-interpretation change between Phase08 prototype (谬误=小项不当扩大) and Phase09 student draft (谬误=大项不当扩大, A 误说成小项不当扩大). Codex A verification reports PASS against 036顺义参考答案; Lane B did not re-read the original rubric.","Before final稿, retain explicit re-verification trace pointing at 036顺义参考答案 line numbers in the audit/QID risk register. Governor/Confucius gates should re-check the source rubric to confirm 大项不当扩大 is the rubric-supported reading."


---

## FILE: `09_student_draft/phase09_internal_terms_scan.md`

# Phase09 Internal Terms Scan

- target: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- forbidden_term_hits: 0
- hits: NONE
- q11_wrong_pairing_hit: NO
- hard_excluded_reference_expansion_failures: 0


---

## FILE: `09_student_draft/phase09_QID_risk_register.md`

# Phase09 QID Risk Register

| question_id | GPT issue | Phase09 resolution | status |
|---|---|---|---|
| `Q-2025丰台期末-7` | 不能放入思维主链正文 | 已移入边界陷阱小节，明确答案落在哲学唯物论，不作为选必三正例 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2025顺义一模-7` | 答案落点表达自相矛盾 | 已据原答案改为大项不当扩大；A 项错在把它说成小项不当扩大；源迹：05_coverage/phase03_question_coverage_matrix.csv 的 036 顺义参考答案摘录写明“大项‘青年’在前提中不周延、在结论中周延，犯大项不当扩大，不是小项不当扩大” | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2026顺义一模-19-2` | 不能写成典型三段论题 | 已改为科学思维主讲，推理结构辅助 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2024朝阳二模-19-1` | 不得回流审稿味编号 | 已统一为学生可理解的“第一空/第二空”表达，不保留文件编号或审稿编号 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2024朝阳二模-19-2` | 不得回流审稿味编号 | 已用联言判断保真条件表述，不含文件或编号痕迹 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2024朝阳一模-20-1` | 充分条件有效式需清晰 | 已写明否定后件式有效 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2024朝阳一模-20-2` | 必要条件有效式需清晰 | 已写明肯定后件式有效并保留古代/当时 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2026通州期末-19-2` | 充分/必要条件不得混用 | 已分列充分条件肯前有效、必要条件肯前无效 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2026丰台一模-18-2` | L4 动作链不得简写 | 已保留甲必要条件肯后式真实成立、乙三段论大项不当扩大 | `RESOLVED_FOR_PHASE09_DRAFT` |
| `Q-2025海淀二模-20` | 角度池不得变三点全必答 | 已写成角度池选二写深，不写三点全必答 | `RESOLVED_FOR_PHASE09_DRAFT` |


---

## FILE: `09_student_draft/phase09_question_id_backcheck.csv`

question_id,role,in_phase08_freeze,appears_in_student_md,line_numbers,visible_title_match,visible_title_line_numbers,hard_excluded_reference_check
Q-2024朝阳一模-20-1,entry_control_row,yes,yes,170;269,yes,150,PASS
Q-2024朝阳一模-20-2,entry_control_row,yes,yes,159;258;269,yes,161,PASS
Q-2024朝阳一模-7,entry_control_row,yes,yes,94;104;114;134,yes,16,PASS
Q-2024朝阳一模-9,entry_control_row,yes,yes,74,yes,26,PASS
Q-2024朝阳二模-19-1,entry_control_row,yes,yes,34;74;308,yes,275,PASS
Q-2024朝阳二模-19-2,entry_control_row,yes,yes,34;74;291,yes,293,PASS
Q-2024朝阳二模-7,reference_only_same_type,no,yes,44;54;84,no,,PASS
Q-2024朝阳期中-19,reference_only_same_type,no,yes,44;54,no,,PASS
Q-2024朝阳期中-7,entry_control_row,yes,yes,258;343;358,yes,172,PASS
Q-2024朝阳期中-9,entry_control_row,yes,no,,yes,310,PASS
Q-2024海淀二模-17-1,entry_control_row,yes,yes,54,yes,36,PASS
Q-2024海淀二模-17-2,entry_control_row,yes,yes,44,yes,46,PASS
Q-2024西城一模-11,hard_excluded_reference_only,no,yes,326,no,,PASS
Q-2024西城一模-19-2,entry_control_row,yes,yes,203;214,yes,183,PASS
Q-2024西城一模-19-3,entry_control_row,yes,yes,192;214,yes,194,PASS
Q-2024西城一模-19-5,entry_control_row,yes,yes,192;203,yes,205,PASS
Q-2025东城期末-13,entry_control_row,yes,yes,247;258,yes,216,PASS
Q-2025东城期末-18-2,reference_only_same_type,no,yes,24;94;104;114;134,no,,PASS
Q-2025东城期末-5,reference_only_same_type,no,yes,34;74,no,,PASS
Q-2025丰台期末-7,entry_control_row,yes,no,,yes,138,PASS
Q-2025丰台期末-8,entry_control_row,yes,no,,yes,56,PASS
Q-2025海淀二模-12,hard_excluded_reference_only,no,yes,146,no,,PASS
Q-2025海淀二模-20,entry_control_row,yes,yes,34,yes,66,PASS
Q-2025海淀期末-17-1,entry_control_row,yes,yes,44;54,yes,76,PASS
Q-2025海淀期末-18,entry_control_row,yes,yes,24;104;114;134,yes,86,PASS
Q-2025海淀期末-2,reference_only_same_type,no,yes,34;74,no,,PASS
Q-2025西城二模-16-2,entry_control_row,yes,no,,yes,227,PASS
Q-2025西城二模-16-3,entry_control_row,yes,yes,24;94;114;134,yes,96,PASS
Q-2025顺义一模-7,entry_control_row,yes,yes,225;258,yes,238,PASS
Q-2026东城一模-19-4,entry_control_row,yes,yes,24;94;104;134,yes,106,PASS
Q-2026丰台一模-18-2,entry_control_row,yes,no,,yes,249,PASS
Q-2026丰台一模-8,reference_only_same_type,no,yes,236,no,,PASS
Q-2026朝阳期中-11,reference_only_same_type,no,yes,258,no,,PASS
Q-2026朝阳期中-14,reference_only_same_type,no,yes,326,no,,PASS
Q-2026朝阳期中-20,entry_control_row,yes,yes,34;74,yes,116,PASS
Q-2026朝阳期中-21-2,entry_control_row,yes,yes,24;94;104;114,yes,126,PASS
Q-2026通州期末-11,reference_only_same_type,no,yes,34;74,no,,PASS
Q-2026通州期末-19-2,entry_control_row,yes,yes,159;170,yes,260,PASS
Q-2026通州期末-5,reference_only_same_type,no,yes,34;74,no,,PASS
Q-2026通州期末-8,reference_only_same_type,no,yes,34;74,no,,PASS
Q-2026通州期末-9,reference_only_same_type,no,yes,24;94;104;114;134,no,,PASS
Q-2026顺义一模-19-1,entry_control_row,yes,yes,44;54;84;181;258;358,yes,328,PASS
Q-2026顺义一模-19-2,entry_control_row,yes,yes,44;54;84;181;258;343,yes,345,PASS
Q-2026顺义一模-3,hard_excluded_reference_only,no,yes,34;74;124,no,,PASS
Q-2026顺义一模-5,reference_only_same_type,no,yes,64,no,,PASS


---

## FILE: `09_student_draft/phase09_student_draft_control_matrix.csv`

entry_no,question_id,visible_title,module,draft_section,question_type,source_entry_status,input_permission,primary_mount,secondary_mount,same_type_ids,gpt_named_risk_status,student_body_origin,no_expansion_policy
1,Q-2024朝阳一模-7,2024 朝阳一模第7题（选择题）,思维,思维,选择题,L3_candidate,include_as_packet_candidate,思维,,Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
2,Q-2024朝阳一模-9,2024 朝阳一模第9题（选择题）,思维,思维,选择题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳二模-19-1；Q-2024朝阳二模-19-2；Q-2025东城期末-5；Q-2025海淀二模-20；Q-2025海淀期末-2；Q-2026朝阳期中-20；Q-2026通州期末-11；Q-2026通州期末-5；Q-2026通州期末-8；Q-2026顺义一模-3,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
3,Q-2024海淀二模-17-1,2024 海淀二模第17题第(1)问（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳二模-7；Q-2024朝阳期中-19；Q-2024海淀二模-17-2；Q-2025海淀期末-17-1；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
4,Q-2024海淀二模-17-2,2024 海淀二模第17题第(2)问（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳二模-7；Q-2024朝阳期中-19；Q-2024海淀二模-17-1；Q-2025海淀期末-17-1；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
5,Q-2025丰台期末-8,2025 丰台期末第8题（选择题）(现代诗解读),思维,思维,选择题,L3_candidate,include_as_packet_candidate,思维,,Q-2026顺义一模-5,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
6,Q-2025海淀二模-20,2025 海淀二模第20题（主观题）(辩证思维复合题),思维,思维,主观题,L4,include,思维,,Q-2024朝阳一模-9；Q-2024朝阳二模-19-1；Q-2024朝阳二模-19-2；Q-2025东城期末-5；Q-2025海淀期末-2；Q-2026朝阳期中-20；Q-2026通州期末-11；Q-2026通州期末-5；Q-2026通州期末-8；Q-2026顺义一模-3,resolved_angle_pool_preserved,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
7,Q-2025海淀期末-17-1,2025 海淀期末第17题第(1)问（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳二模-7；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
8,Q-2025海淀期末-18,2025 海淀期末第18题（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
9,Q-2025西城二模-16-3,2025 西城二模第16题第(3)问（主观题）,思维,思维,主观题,L4,include,思维,,Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
10,Q-2026东城一模-19-4,2026 东城一模第19题第(4)问（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026朝阳期中-21-2；Q-2026通州期末-9,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
11,Q-2026朝阳期中-20,2026 朝阳期中第20题（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2026顺义一模-3,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
12,Q-2026朝阳期中-21-2,2026 朝阳期中第21题第(2)问（主观题）,思维,思维,主观题,L3_candidate,include_as_packet_candidate,思维,,Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026通州期末-9,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
13,Q-2025丰台期末-7,2025 丰台期末第7题（选择题）(漫画启示),思维,边界陷阱,选择题,L3_candidate,include_as_packet_candidate,边界陷阱,,Q-2025海淀二模-12,resolved_boundary_trap_not_thinking_mainline,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
14,Q-2024朝阳一模-20-1,2024 朝阳一模第20题第(1)问（主观题）,推理,推理,主观题,L3_candidate,include_as_packet_candidate,推理,,Q-2024朝阳一模-20-2；Q-2026通州期末-19-2,resolved_sufficient_conditional_valid_form,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
15,Q-2024朝阳一模-20-2,2024 朝阳一模第20题第(2)问（主观题）,推理,推理,主观题,L3_candidate,include_as_packet_candidate,推理,,Q-2024朝阳一模-20-1；Q-2026通州期末-19-2,resolved_necessary_conditional_valid_form,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
16,Q-2024朝阳期中-7,2024 朝阳期中第7题（选择题）,推理,推理,选择题,L3_candidate,include_as_packet_candidate,推理,,Q-2026顺义一模-19-1；Q-2026顺义一模-19-2,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
17,Q-2024西城一模-19-2,2024 西城一模第19题第(2)问（主观题）(下定义),推理,推理,主观题,L3_candidate,include_as_packet_candidate,推理,,Q-2024西城一模-19-3；Q-2024西城一模-19-5,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
18,Q-2024西城一模-19-3,2024 西城一模第19题第(3)问（主观题）(概念外延关系),推理,推理,主观题,L3_candidate,include_as_packet_candidate,推理,,Q-2024西城一模-19-2；Q-2024西城一模-19-5,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
19,Q-2024西城一模-19-5,2024 西城一模第19题第(5)问（主观题）,推理,推理,主观题,L3_candidate,include_as_packet_candidate,推理,,Q-2024西城一模-19-2；Q-2024西城一模-19-3,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
20,Q-2025东城期末-13,2025 东城期末第13题（选择题）,推理,推理,选择题,L3_candidate,include_as_packet_candidate,推理,,Q-2025顺义一模-7,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
21,Q-2025西城二模-16-2,2025 西城二模第16题第(2)问（主观题）,推理,推理,主观题,L4,include,推理,,Q-2026丰台一模-8,standardized_from_phase08,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
22,Q-2025顺义一模-7,2025 顺义一模第7题（选择题）,推理,推理,选择题,L3_candidate,include_as_packet_candidate,推理,,Q-2025东城期末-13,resolved_answer_expression_rechecked_against_source,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
23,Q-2026丰台一模-18-2,2026 丰台一模第18题第(2)问（主观题）,推理,推理,主观题,L4,include,推理,,Q-2024朝阳一模-20-2；Q-2024朝阳期中-7；Q-2025东城期末-13；Q-2025顺义一模-7；Q-2026朝阳期中-11；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2,resolved_L4_reasoning_chain_preserved,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
24,Q-2026通州期末-19-2,2026 通州期末第19题第(2)问（主观题）,推理,推理,主观题,L3_candidate,include_as_packet_candidate,推理,,Q-2024朝阳一模-20-1；Q-2024朝阳一模-20-2,resolved_sufficient_vs_necessary_split,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
25,Q-2024朝阳二模-19-1,2024 朝阳二模第19题第(1)问（主观题）,交叉,交叉,主观题,L3_candidate,include_as_packet_candidate,推理,思维,Q-2024朝阳二模-19-2,resolved_no_audit_expression_reflux,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
26,Q-2024朝阳二模-19-2,2024 朝阳二模第19题第(2)问（主观题）,交叉,交叉,主观题,L3_candidate,include_as_packet_candidate,推理,思维,Q-2024朝阳二模-19-1,resolved_no_audit_expression_reflux,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
27,Q-2024朝阳期中-9,2024 朝阳期中第9题（选择题）,交叉,交叉,选择题,L3_candidate,include_as_packet_candidate,推理,思维,Q-2024西城一模-11；Q-2026朝阳期中-14,cross_double_mount_preserved,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
28,Q-2026顺义一模-19-1,2026 顺义一模第19题第(1)问（主观题）,交叉,交叉,主观题,L3_candidate,include_as_packet_candidate,推理,思维,Q-2024朝阳期中-7；Q-2026顺义一模-19-2,cross_double_mount_preserved,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion
29,Q-2026顺义一模-19-2,2026 顺义一模第19题第(2)问（主观题）,交叉,交叉,主观题,L3_candidate,include_as_packet_candidate,思维,推理,Q-2024朝阳期中-7；Q-2026顺义一模-19-1,resolved_scientific_thinking_primary_reasoning_auxiliary,phase08_prototype_29_only,no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion


---

## FILE: `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`

# 选必三《逻辑与思维》学生稿草案

本稿用于下一轮校对和成文化，不是可直接交付的排版稿。

## 使用方式

- 看到材料，先判断它是在考“思维方法”还是“推理规则”。
- 思维题按“材料信号 → 可写方法 → 为什么能想到 → 答题动作 → 答案落点 → 易错陷阱”走。
- 推理题按“题型 → 逻辑形式 → 规则口诀 → 有效式或错误式 → 解题动作 → 答案落点 → 易错陷阱”走。
- 同类题只作为索引，不在本稿里展开答案。

---

## 一、思维方法

### 2024 朝阳一模第7题（选择题）

- 材料信号：题干列出“原始创新、集成创新、开放创新一体设计”；选项分别讨论 ①迁移想象逆向、②集成创新跨越性与逻辑推导并行、③开放创新对前人成果的继承借鉴、④发散与聚合贯通。
- 可写思维/方法：创新思维，内含发散、聚合、逆向、超前、迁移等具体方法。
- 为什么能想到：题干把“创新”与“逻辑”放在一起，让学生在创新思维总称下区分逻辑思维参与的环节；②把跨越性与逻辑推导并列、③把合作创新落在对已有成果的继承上，正好对应“创新思维与逻辑思维并行”和“辩证否定式继承”。
- 答题动作：②集成创新具有跨越性，但不排斥有步骤的逻辑推导与分析，体现创新思维与逻辑思维的并行；③开放创新中的合作创新，需要对前人和他人的已有成果进行继承与借鉴，体现辩证否定意义上的继承。
- 答案落点：正确选项 C（②③），重点写清创新思维不排斥逻辑分析、合作创新建立在对前人成果继承之上。
- 易错陷阱：①把“迁移、想象、逆向”误归入逻辑思维，实际它们是创新思维的具体方法，属于混用错；④“有效贯通...就能确保...”表述绝对化。
- 同类题索引：Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9。

### 2024 朝阳一模第9题（选择题）

- 材料信号：中学生模拟政协活动从“模拟提案”到“正式提案”，经历调查、充实、完善、提交的多环节配合；市政协委员承接、指导、提交。
- 可写思维/方法：辩证思维与系统观念中的整体性。
- 为什么能想到：从“模拟”到“正式”涉及多主体、多环节协同，正是把多个分散动作整合为整体方案的过程；③对应系统观念的整体性体现，④涉及对中国特色社会主义制度优势的运用与理解。
- 答题动作：③系统观念在调查研究和思考任务中的整体性体现；④对中国特色社会主义制度优势的运用与理解。
- 答案落点：正确选项 D（③④），点出活动是多主体协同完成、整体性贯穿调查与提案全过程，并指向制度优势的运用。
- 易错陷阱：①把“具体政策制定”当作此活动主旨，偏离活动定位；②把活动写成“引领社会治理”，拔高过度。
- 同类题索引：Q-2024朝阳二模-19-1；Q-2024朝阳二模-19-2；Q-2025东城期末-5；Q-2025海淀二模-20；Q-2025海淀期末-2；Q-2026朝阳期中-20；Q-2026通州期末-11；Q-2026通州期末-5；Q-2026通州期末-8；Q-2026顺义一模-3。

### 2024 海淀二模第17题第(1)问（主观题）

- 材料信号：全国时间利用调查围绕个人生理必需活动、有酬劳动、无酬劳动、个人自由支配活动等多类时间投入，目的是全面、真实、准确反映居民生活质量与生活模式。
- 可写思维/方法：科学思维、辩证思维、创新思维三角度并列；具体可调用客观性、整体性、发散与聚合、超前思维以及思维抽象/思维具体/感性具体。
- 为什么能想到：本题要求从三个角度分别采分，科学思维对应客观性与预见性、创新思维对应“三新”与发散聚合、超前，辩证思维对应整体性与分析综合；每一角度都要落到时间利用调查的具体动作上才不丢分。
- 答题动作：三角度多挂载、按表格化采分；科学思维 2 分(客观性、预见性)，创新思维 3 分(三新、发散聚合、超前)，辩证思维 2 分(整体性、分析综合)；每个分点必须结合材料分析。
- 答案落点：逐角度一句话作答，每条带“调查内容/调查动作 + 思维方法 + 作用结论”。
- 易错陷阱：只列知识点而不结合材料，只能拿基础 1 分；混淆角度归属(把“整体性”写到科学思维下、把“客观性”写到创新思维下)直接丢分。
- 同类题索引：Q-2024朝阳二模-7；Q-2024朝阳期中-19；Q-2024海淀二模-17-2；Q-2025海淀期末-17-1；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2。

### 2024 海淀二模第17题第(2)问（主观题）

- 材料信号：同一调查的两阶段任务——“调查了解居民时间利用情况”对应感性具体阶段；“分析研究居民时间利用情况”对应思维抽象再到思维具体阶段。
- 可写思维/方法：科学思维(认识论维度)；感性具体、思维抽象、思维具体三层。
- 为什么能想到：题目把“调查了解”和“分析研究”区分开，正是“杂多现象→抽出核心概念→回到完整整体图景”链条；严禁把方向写反。
- 答题动作：调查了解 = 感性具体(1 分)；分析研究 = 思维抽象 + 思维具体(1 分)；两阶段相互依赖、不可割裂(2 分)。
- 答案落点：按“调查了解→感性具体→获得对象的整体表象；分析研究→思维抽象抓住本质→思维具体重建完整图景；两阶段相互依赖共同形成科学认识”作答。
- 易错陷阱：把感性具体和思维具体的方向颠倒不给分；用“实践决定认识”替代具体环节只能得 1 分。
- 同类题索引：Q-2024朝阳二模-7；Q-2024朝阳期中-19；Q-2024海淀二模-17-1；Q-2025海淀期末-17-1；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2。

### 2025 丰台期末第8题（选择题）(现代诗解读)

- 材料信号：《和平是一棵树》以白天鹅翅膀、湖水云影、门、红酒、灯等多个具体形象层层展开，从不同方向表达对和平的向往。
- 可写思维/方法：发散思维 + 形象思维。
- 为什么能想到：多个具体意象向同一主题“和平”发散，正是发散思维；以白天鹅翅膀、门、红酒等具体形象触及和平本质，正是形象思维。
- 答题动作：选 D。②运用发散思维表达人们对和平的向往与追求；④以形象思维触及和平的本质特征。
- 答案落点：在“形象思维、发散思维”这一类型上得分；指出诗歌从多个意象发散表达，并以具体形象触及和平本质。
- 易错陷阱：①把“想象”当作思维的基本单元(基本单元是概念，不是想象)；③把本诗当作抽象思维(本诗用形象，不用抽象)。
- 同类题索引：Q-2026顺义一模-5。

### 2025 海淀二模第20题（主观题）(辩证思维复合题)

- 材料信号：材料给出全民共享、全面共享、共建共享、渐进共享四个层次；设问要求运用辩证思维谈如何坚持共享发展理念推进共同富裕。
- 可写思维/方法：辩证思维总称下，可调用整体性、动态性、分析与综合、质量互变、辩证否定。
- 为什么能想到：题目要求“运用辩证思维”，并把共享拆为四个层次，要求学生从角度池中选取与材料事实匹配的辩证维度作答；不是三点全必答。
- 答题动作：从“整体性、动态性、分析与综合、质量互变、辩证否定”里选最贴材料的两个角度写深；每个角度都要带上共享发展的具体层次和推进共同富裕的作用。
- 答案落点：角度池写法：可优先选“整体性 + 动态性”或“分析与综合 + 质量互变”等组合，核心是两角度写透；不要把所有角度堆成必答清单。
- 易错陷阱：不能写成三点全必答；不能把辩证否定写成否定一切；整体性必须写出联结、综合、系统优化，不能只写“整体”两个字。
- 同类题索引：Q-2024朝阳一模-9；Q-2024朝阳二模-19-1；Q-2024朝阳二模-19-2；Q-2025东城期末-5；Q-2025海淀期末-2；Q-2026朝阳期中-20；Q-2026通州期末-11；Q-2026通州期末-5；Q-2026通州期末-8；Q-2026顺义一模-3。

### 2025 海淀期末第17题第(1)问（主观题）

- 材料信号：杂志刊登的“永动机”设计图——盆水、架子、叶轮、毛巾，通过毛细作用吸水再滴水推动叶轮，声称无需外力实现永动。
- 可写思维/方法：科学思维(客观性维度)。
- 为什么能想到：题干明确“运用科学思维知识”，材料以违反客观规律的设想登场；客观性要求“如实反映对象、把握客观规律”，而毛巾毛细作用吸水高度有限，不可能维持永动。
- 答题动作：从实际出发、如实反映对象、把握客观规律；指出毛巾毛细作用吸水的高度有限，水量与摩擦消耗使设计无法实现永动。
- 答案落点：写出“科学思维要求客观性，从实际出发把握客观规律；永动机设计违背了客观规律，所以无法成立”的卷面作答句。
- 易错陷阱：用辩证思维或创新思维替代客观性会丢分。
- 同类题索引：Q-2024朝阳二模-7；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2。

### 2025 海淀期末第18题（主观题）

- 材料信号：北京城市图书馆从“人找书”转向“书找人”，建筑设计借用赤印意象，以数字技术为依托、构建立体化数字文化服务。
- 可写思维/方法：创新思维总称下，具体落到联想思维、逆向思维、迁移。
- 为什么能想到：“人找书→书找人”是把已有结构与顺序反过来，典型的逆向思维；“赤印意象→建筑设计”是从文化符号到空间形态的同化性迁移，典型的联想思维。
- 答题动作：逆向思维=对事物结构与顺序的已有认识进行反向思考(人找书→书找人)；联想思维=同化性迁移(赤印意象→建筑设计)。
- 答案落点：每条带“创新思维子方法 + 材料动作 + 服务/价值结果”，分别写逆向、联想两条。
- 易错陷阱：用“创新思维”总称替代逆向/联想会扣分；混淆迁移类型(把同化性写成顺应性)会扣分。
- 同类题索引：Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9。

### 2025 西城二模第16题第(3)问（主观题）

- 材料信号：延庆区自然保护地管理处针对鹿叫村遗址的废弃水井和地窖，建造攀爬台阶、营造雨水收集池等改造，便于不同体型动物自由取水。
- 可写思维/方法：创新思维(改变与创造条件，建立新的具体联系)。
- 为什么能想到：旧设施(废井、地窖)长期对动物造成威胁，通过营建台阶、收集池等具体改造，把“威胁性结构”转化为“取水通道”，体现创新思维改变和创造条件、建立新的具体联系。
- 答题动作：运用创新思维改变和创造条件，把废弃水井改造为可取水的设施，把雨水收集池布局成动物可达的取水点，从而建立新的人—野生动物—资源联系。
- 答案落点：写“创新思维改变和创造条件 + 改造措施 + 形成新的具体联系”卷面作答句。
- 易错陷阱：本题不是推理题；子问拆分后第(3)问归思维/创新，不可与同题第(2)问的推理类型混淆。
- 同类题索引：Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2；Q-2026通州期末-9。

### 2026 东城一模第19题第(4)问（主观题）

- 材料信号：中关村特色产业园围绕人工智能、生物制造等前沿领域，从“0→1 原始突破”到“把 1 拉长”的系统跃升，涉及单点突破到链式扩展的全过程。
- 可写思维/方法：系统观念 + 创新思维；具体可调用整体性、动态性、分析与综合、发散、聚合、超前。
- 为什么能想到：题干明确“运用系统观念与创新思维”，材料从原始突破写到链式扩展，正好对应系统观念的整体性与创新思维的从单点到链式；两类思维并行采分。
- 答题动作：以系统观念把握整体布局与协同跃升；以创新思维实现从原始突破到链式扩展；具体到中关村产业园发展目标(人工智能、生物制造等领域)，拿出可落地的措施。
- 答案落点：每条带“思维方法 + 材料事实 + 园区发展作用”，一句话写到具体园区目标。
- 易错陷阱：措施缺乏具体性扣分；不符合中关村发展目标(脱离前沿产业、脱离园区载体)扣分。
- 同类题索引：Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026朝阳期中-21-2；Q-2026通州期末-9。

### 2026 朝阳期中第20题（主观题）

- 材料信号：百年未有之大变局背景下，新一轮科技革命与产业变革深入发展，国际力量对比深刻调整；同时逆全球化、单边主义、局部冲突等风险并存，我国发展面临新的战略机遇与新的动荡变革期。
- 可写思维/方法：辩证思维总称下，可调用整体性、动态性、分析与综合、质量互变。
- 为什么能想到：题干明确“运用辩证思维方法”，材料把机遇与挑战并列、把当前与长远并列、把局部与全局并列；正是矛盾对立统一+整体性统筹+动态性应变。
- 答题动作：辩证思维=矛盾对立统一(机遇与挑战)；整体性=统筹全局(发展、安全、内外)；动态性=主动应变(把握战略机遇、化解风险)；“一分为二”+“多维施策”组合作答。
- 答案落点：每条带“辩证维度 + 材料事实 + 战略意义”卷面作答句，机遇与挑战、整体与动态分别落实。
- 易错陷阱：误用单一矛盾或仅讲机遇/挑战丢分；漏整体性或动态性扣分。
- 同类题索引：Q-2026顺义一模-3。

### 2026 朝阳期中第21题第(2)问（主观题）

- 材料信号：人文经济学强调“文化、人文、经济”三者有机统一，材料二涉及把传统物理空间转化为柔性业态、把“冷资源”开发为“热经济”、把历史/数字/社群等多业态整合。
- 可写思维/方法：创新思维总称下，具体落到联想、发散、聚合、逆向(可同步带超前)。
- 为什么能想到：“冷资源→热经济”是从一类对象迁移到另一类对象的联想；历史 + 数字 + 社群多业态铺开后再收束，是发散与聚合的组合；把“传统物理空间”反过来做柔性业态，是逆向思维。
- 答题动作：联想思维拓展价值(冷资源→热经济)；发散与聚合整合业态(历史 + 数字 + 社群)；逆向思维创造差异(传统物理空间→柔性业态)。
- 答案落点：每条带“创新子思维 + 材料动作 + 价值结果”，分别落联想、发散与聚合、逆向三条。
- 易错陷阱：只列“运用创新思维”总称丢分；混淆联想/发散/聚合/逆向之间的归属扣分。
- 同类题索引：Q-2024朝阳一模-7；Q-2025东城期末-18-2；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026通州期末-9。

## 二、边界陷阱

### 2025 丰台期末第7题（选择题）(漫画启示)

- 材料信号：漫画把人困在“为昨天懊恼、替明天担心”的状态里，真正提醒的是回到当下现实，不是让学生去写超前思维。
- 可写思维/方法：这道题是边界陷阱：答案落在哲学唯物论的“从实际出发、从当下做起”，选必三“超前思维”只是干扰项。
- 为什么能想到：如果把“明天”二字直接等同于超前思维，就会掉入选项陷阱；漫画的重心是不要脱离现实、不要被过去和未来牵着走。
- 答题动作：先排除“超前思维创造幸福”的夸大表述，再抓住“从实际出发、把握当下”这个哲学落点。
- 答案落点：选 C，理由是从实际出发、从当下做起，生活才能少些迷茫。
- 易错陷阱：A 把关注当下说成“就能”成功，绝对化；B 借“明天”诱导写超前思维，方向反了；D 把成功关键泛化，材料支撑不足。
- 同类题索引：Q-2025海淀二模-12。

## 三、推理题型

### 2024 朝阳一模第20题第(1)问（主观题）

- 题型：充分条件假言推理(否定后件式)。
- 逻辑形式：假言判断+充分条件+必要条件辨识；本题为充分条件假言推理。
- 规则口诀：充分条件假言推理：前真后必真；否定后件，可以否定前件。
- 有效式或错误式：结构是“如果没有广泛生长竹子，就不可能有大量炭化竹节；现在有大量炭化竹节，所以并非没有广泛生长竹子”。这是充分条件假言推理的否定后件式，有效。
- 解题动作：① 识别题干为充分条件假言判断；② 套用“前真后必真；否定后件→否定前件”规则；③ 对照题干结论判断推理是否成立；④ 避开“假言推理结构识别错误”“前后件颠倒”“化作不完全归纳”等陷阱。
- 答案落点：写“这是充分条件假言推理；依据前真后必真、后假则前假，否定后件可以否定前件，所以推理成立”。
- 易错陷阱：把充分条件假言写成必要条件；前后件颠倒；把演绎式假言写成不完全归纳。
- 同类题索引：Q-2024朝阳一模-20-2；Q-2026通州期末-19-2。

### 2024 朝阳一模第20题第(2)问（主观题）

- 题型：必要条件假言推理(补充推理二)。
- 逻辑形式：假言判断+必要条件；本题为必要条件假言推理的补充。
- 规则口诀：必要条件假言推理：“只有 P 才 Q”；肯定后件，可以肯定前件；仅肯定前件，不能肯定后件。
- 有效式或错误式：可补为“只有 A 区域古代气候温暖，A 区域古代才有可能生长竹子；A 区域古代广泛生长着竹子，所以 A 区域古代气候较为温暖”。这是必要条件假言推理的肯定后件式，有效。
- 解题动作：先把竹子生长的必要条件写成“只有……才……”；再由“A 区域古代广泛生长着竹子”推出“A 区域古代气候温暖”；时间限定词“古代/当时”必须保留。
- 答案落点：补全句式时写清“只有 A 区域古代气候温暖，A 区域古代才有可能生长竹子”，再推出古代气候较为温暖。
- 易错陷阱：补完整推理时漏写“古代/当时”等时间表述会扣 1 分。
- 同类题索引：Q-2024朝阳一模-20-1；Q-2026通州期末-19-2。

### 2024 朝阳期中第7题（选择题）

- 题型：三段论排序题。
- 逻辑形式：三段论(大前提+小前提+结论)。
- 规则口诀：大前提含中项与大项；小前提含中项与小项；中项必须周延一次；结论从二者推出。
- 有效式或错误式：正确排序为②大前提“北京中轴线是不可替代的文化遗产”+①小前提“北京中轴线是世界遗产委员会确认的世界遗产”+③结论“有些由世界遗产委员会确认的是不可替代的文化遗产”；中项“北京中轴线”周延，推理有效，正确选项 B。
- 解题动作：① 找结论(③)，确定大项；② 找包含大项的前提作大前提(②)；③ 剩余为小前提(①)；④ 排查中项是否周延、有无单称错位。
- 答案落点：选 B，排序为②①③；结论由两个前提关于“北京中轴线”的中项贯通推出。
- 易错陷阱：A①③④无效——中项错位；C 三个前提均为单称——中项断裂；D 结论与前提关系错位。
- 同类题索引：Q-2026顺义一模-19-1；Q-2026顺义一模-19-2。

### 2024 西城一模第19题第(2)问（主观题）(下定义)

- 题型：概念定义结构题(归纳/概念/判断/推理)。
- 逻辑形式：被定义项 + 联结词 + 种差 + 邻近属。
- 规则口诀：“被定义项 = 种差 + 邻近属”。
- 有效式或错误式：① 举国体制 + ② 是 + ③ 利用国家力量动员规模性资源实现国家目标(种差) + ④ 一种任务组织方式和体制机制安排(邻近属)。
- 解题动作：① 确定被定义项；② 选种差(本质属性)；③ 配邻近属(类别归属)；④ 用“是”或“指”作联结词，顺序不可颠倒。
- 答案落点：按“举国体制是利用国家力量动员规模性资源实现国家目标的一种任务组织方式和体制机制安排”完整作答。
- 易错陷阱：种差与邻近属颠倒丢分；漏种差或漏邻近属丢分。
- 同类题索引：Q-2024西城一模-19-3；Q-2024西城一模-19-5。

### 2024 西城一模第19题第(3)问（主观题）(概念外延关系)

- 题型：概念外延关系判定。
- 逻辑形式：相容/属种关系。
- 规则口诀：外延上一者包含另一者 → 属种(相容包含)关系。
- 有效式或错误式：举国体制包含“新型举国体制” → 属种关系(亦称包含/相容)。
- 解题动作：① 比较两个概念外延；② 判定为相容/不相容；③ 在相容下细分全同/属种(包含)/交叉。
- 答案落点：写出“举国体制与新型举国体制是属种(相容)关系，前者包含后者”卷面作答句。
- 易错陷阱：误填全同/交叉/不相容/反对均扣分。
- 同类题索引：Q-2024西城一模-19-2；Q-2024西城一模-19-5。

### 2024 西城一模第19题第(5)问（主观题）

- 题型：综合推理题(实践调研 + 矛盾分析 + 推理想象 + 超前思维)。
- 逻辑形式：由实践→因果规律→矛盾分析→由过去现在推未来→超前思维的整链。
- 规则口诀：以实践为导向调研 → 把握状况因果规律 → 善用矛盾分析(内在矛盾/外在矛盾) → 运用推理与想象由过去现在推未来 → 超前思维。
- 有效式或错误式：六点框架按“调研→因果→矛盾→推理想象→超前”顺序展开；附加补点“强调实践 + 1 分，超前思维，内外矛盾”。
- 解题动作：① 立足实践调研当前状况；② 把握因果规律；③ 拆内外矛盾；④ 用推理与想象由过去/现在推未来；⑤ 用超前思维做前瞻判断。
- 答案落点：每条带“环节 + 材料事实 + 作用结论”，最后落到超前思维的前瞻判断。
- 易错陷阱：只罗列概念无材料分析丢分；漏“实践”基础扣分。
- 同类题索引：Q-2024西城一模-19-2；Q-2024西城一模-19-3。

### 2025 东城期末第13题（选择题）

- 题型：三段论谬误识别题(中项不周延+小项不当扩大+四概念)。
- 逻辑形式：三段论 + 概念 + 判断 + 周延。
- 规则口诀：中项必须周延一次；前提不周延的项，在结论中不得周延；前提为否定时不得引出未交代的肯定结论；同一推理只能有三个概念。
- 有效式或错误式：①“祥云是大国重器 + 有的大国重器是载人飞艇” → 中项“大国重器”未周延，谬误为中项不周延；③“碳纤维自行车适合山地骑行 + 山地车适合山地骑行” → 中项“适合山地骑行”未周延，两项均为属性，谬误同样为中项不周延。
- 解题动作：① 划出中项与大项小项；② 检查中项周延性；③ 检查前提与结论否定一致性；④ 检查概念是否四个错位。
- 答案落点：正确选项 B，理由是①与③均犯中项不周延的谬误。
- 易错陷阱：②“否定前提两否得结论”是错误形式，但题目要求识别谬误而非否定结构；④“石墨烯围巾有智能温控 + 智能温控能调节”=四概念错位。
- 同类题索引：Q-2025顺义一模-7。

### 2025 西城二模第16题第(2)问（主观题）

- 题型：充分条件假言推理(肯定后件无效式辨析)。
- 逻辑形式：假言判断 + 充分条件；本题考察“肯定后件不能必推前件”。
- 规则口诀：充分条件假言推理“前真后必真，后真前不必真”；肯定后件式无效。
- 有效式或错误式：无法据后件真确定一定有岩松鼠行动；充分条件假言判断后件真不能确定前件真。
- 解题动作：① 识别推理为充分条件假言；② 检查是否存在肯定后件式；③ 指出“后件真≠前件真”；④ 把条件①(勺鸡雕鸮)与岩松鼠的无关性作为补充说明。
- 答案落点：写出“无法确定一定有岩松鼠行动；充分条件假言判断后件真不能确定前件真”卷面作答句。
- 易错陷阱：把“后件真”误推为“前件真”；把无关条件①(勺鸡雕鸮)与岩松鼠强行挂钩。
- 同类题索引：Q-2026丰台一模-8。

### 2025 顺义一模第7题（选择题）

- 题型：三段论谬误判断纠错题。
- 逻辑形式：三段论 + 项的周延 + 逆向选择。
- 规则口诀：前提中不周延的项，结论中不得周延；一个三段论只能有三个不同的项；中项至少周延一次。
- 有效式或错误式：A 项的推理实际问题是“大项不当扩大”：大项“青年”在肯定前提中不周延，却在否定结论中周延；A 把它说成“小项不当扩大”，所以 A 的逻辑分析错误。
- 解题动作：先看题干问“逻辑分析错误的是”，这是逆向选择；再逐项划大项、小项、中项，最后判断“题目给出的谬误名称”是否与真实谬误一致。
- 答案落点：选 A，原因是 A 对谬误名称判断错了；真实错误应是大项不当扩大，不是小项不当扩大。
- 易错陷阱：B 的“两否定前提不能必然推出结论”、C 的“四概念”、D 的“中项不周延”都是可成立的分析，不是本题要选的错误分析。
- 同类题索引：Q-2025东城期末-13。

### 2026 丰台一模第18题第(2)问（主观题）

- 题型：甲：必要条件假言推理的肯定后件式；乙：三段论大项不当扩大。
- 逻辑形式：甲——必要条件假言推理 · 肯定后件式；乙——三段论 · 大项在前提不周延却在结论周延 · 大项不当扩大。
- 规则口诀：必要条件假言推理：肯定后件可以肯定前件；三段论：前提中不周延的项，结论中不得周延。
- 有效式或错误式：甲为必要条件假言推理的肯定后件式，且前提真实，推理成立；乙的大项在前提中不周延，却在结论中周延，犯大项不当扩大，推理不成立。
- 解题动作：先识别甲为必要条件假言推理的肯定后件式，并结合前提真实判定甲推理正确；再识别乙为三段论大项在前提中不周延却在结论中周延，属于大项不当扩大，判定乙推理错误。
- 答案落点：甲正确，乙错误；甲不能泛写成演绎推理，乙必须点出“大项不当扩大”。
- 易错陷阱：甲不能写成演绎推理(应写必要条件假言推理的肯定后件式)；乙在识别大项/中项/小项时，应先找结论再定大项，不能颠倒顺序。
- 同类题索引：Q-2024朝阳一模-20-2；Q-2024朝阳期中-7；Q-2025东城期末-13；Q-2025顺义一模-7；Q-2026朝阳期中-11；Q-2026顺义一模-19-1；Q-2026顺义一模-19-2。

### 2026 通州期末第19题第(2)问（主观题）

- 题型：充分条件假言推理 + 必要条件假言推理(同题对照判断推理正误)。
- 逻辑形式：推理①为充分条件假言判断的肯定前件式；推理②为必要条件假言判断的肯定前件式。
- 规则口诀：充分条件：肯定前件可以肯定后件；必要条件：肯定后件可以肯定前件，仅肯定前件不能肯定后件。
- 有效式或错误式：推理①若为充分条件假言推理的肯定前件式，则结构有效；推理②若为必要条件假言推理的肯定前件式，则结构无效，因为“有必要条件”不等于“结果一定发生”。
- 解题动作：① 识别每条推理是充分条件假言还是必要条件假言；② 套用相应有效式/错误式规则；③ 对照题干判断每条推理正误；④ 避开混淆肯前/肯后陷阱。
- 答案落点：推理①有效，推理②无效；答题时必须分别写出充分条件和必要条件的规则，不能用一个“肯定前件”口诀混答。
- 易错陷阱：误识别假言推理类型扣分；肯定前件/肯定后件混淆扣分。
- 同类题索引：Q-2024朝阳一模-20-1；Q-2024朝阳一模-20-2。

## 四、交叉题

交叉题要保留两条线：一条是卷面主讲线，一条是辅助理解线。主讲线决定正文展开重点，辅助线只帮助防误判。

### 2024 朝阳二模第19题第(1)问（主观题）

#### 主讲线：推理结构
- 题型：类比推理 + 联言判断作辅助；本题要求填动态性 + 类比推理。
- 逻辑形式：第一空考辩证思维动态性，第二空考类比推理。
- 规则口诀：动态性=用变化发展观点看问题；类比推理=由两类对象在某些属性上相同，推出在另外的属性上也相同。
- 有效式或错误式：第一空写“动态性”；第二空必须写“类比推理”，不要改写成相近词。
- 解题动作：看到“生生不息、日新、革新、不断充实”，第一空锁定动态性；看到由一个对象经验迁移到另一个对象，第二空锁定类比推理。
- 答案落点：第一空写“动态性”，第二空写“类比推理”。
- 易错陷阱：第一空填“整体性/质量互变”丢分；第二空把“类比”改写为其他词不给分。

#### 辅助线：思维方法
- 题型：辩证思维 · 动态性。
- 材料信号：中华文明“生生不息”“日新”“革新”“不断充实”等表述呈现持续变化与革新。
- 答题动作：用“变化发展观点看问题”理解中华优秀传统文化的革新性。
- 易错陷阱：误填整体性、质量互变、矛盾运动等丢分。
- 同类题索引：Q-2024朝阳二模-19-2。

### 2024 朝阳二模第19题第(2)问（主观题）

#### 主讲线：推理结构
- 题型：联言判断及其保真条件。
- 逻辑形式：联言判断 = 各联言支同时成立。
- 规则口诀：“当且仅当各联言支都真，联言判断才真；一假即假”。
- 有效式或错误式：联言判断只有在各个联言支都真实时才为真；只要有一个联言支为假，整个联言判断就为假。
- 解题动作：先把材料中的并列表述拆成若干联言支，再写清“全真才真、一假即假”的保真条件。
- 答案落点：写出联言判断本身，并写清“全真才真、一假即假”的保真条件。
- 易错陷阱：把“联言判断”误写为“连言判断”不给分；表述为“充分/必要条件联言判断”不给分。

#### 辅助线：思维方法
- 题型：辩证思维 · 动态性（与第(1)问辅助线一致）。
- 答题动作：延续动态性的“变化发展观点”，支持联言判断中各支共同成立的语境理解。
- 易错陷阱：与第(1)问共用，避免把动态性写成整体性。
- 同类题索引：Q-2024朝阳二模-19-1。

### 2024 朝阳期中第9题（选择题）

#### 主讲线：推理结构
- 题型：归纳推理 · 共变法。
- 逻辑形式：归纳推理(因果探求方法)。
- 规则口诀：共变法——其他条件相同，某现象随某因素的变化而共同变化，二者具有因果关联。
- 有效式或错误式：小李实验中铃声随空气量同向变化，符合共变法，正确选项 B。
- 解题动作：① 看材料是否存在两个变量同向/反向变化；② 排除“求异法”对实验情境的误用；③ 排除“演绎推理”误判；④ 排除“假如式想象未发生”。
- 答案落点：选 B，判断为归纳推理中的共变法。
- 易错陷阱：A 误判演绎推理；C 误用求异法且夸大必然性；D 把科学实验误解为假如式想象。

#### 辅助线：思维方法
- 题型：思维抽象 / 思维具体。
- 材料信号：从“空气—铃声”这一具体对照实验抽象出因果共变这一规律，再回到“声音不能在真空中传播”的整体结论。
- 答题动作：沿“杂多现象→抽出核心因果→回到整体规律”路径理解共变法的认识价值。
- 易错陷阱：不可把感性具体与思维具体颠倒；不可写成“实践决定认识”代替具体环节。
- 同类题索引：Q-2024西城一模-11；Q-2026朝阳期中-14。

### 2026 顺义一模第19题第(1)问（主观题）

#### 主讲线：推理结构
- 题型：三段论(前提真实性 + 结构正确性)。
- 逻辑形式：三段论 + 判断 + 推理。
- 规则口诀：演绎推理两条件——前提真实 + 结构正确。
- 有效式或错误式：材料“未来产业由前沿技术驱动...”不能必然推出“所有...都是未来产业”，因此该推理在前提真实性或结构上不能两全成立；本题要求按两条件分析判定。
- 解题动作：① 识别推理是否为三段论；② 检查前提是否真实(由材料可否得出)；③ 检查推理结构是否正确(中项是否周延、有无四概念)；④ 给出“对/错 + 理由”的完整判断。
- 答案落点：从前提真实性和结构正确性两方面判断：材料不能必然推出该结论，理由必须写完整。
- 易错陷阱：只判断对错而不分析理由扣分；漏前提真假/结构正确两条件之一扣分。

#### 辅助线：思维方法
- 题型：科学思维(对前提真实性、推理结构正确性的客观要求)。
- 答题动作：用科学思维“如实反映对象、把握客观规律”的客观性，审视前提与结构是否符合材料事实。
- 易错陷阱：用辩证思维或创新思维替代科学思维的客观性会丢分。
- 同类题索引：Q-2024朝阳期中-7；Q-2026顺义一模-19-2。

### 2026 顺义一模第19题第(2)问（主观题）

#### 主讲线：思维方法
- 题型：科学思维三特征。
- 材料信号：从老龄化人口需求出发的产品研发、对老龄化趋势的市场判断、对产品的反复测试与迭代。
- 答题动作：把客观性、预见性、可检验性逐条对应材料：从老人真实需求出发，体现客观性；研判老龄化趋势和市场潜力，体现预见性；反复测试、多轮迭代，体现可检验性。
- 易错陷阱：主讲线是科学思维，不是典型三段论；只列三个特征不分析材料会丢分。

#### 辅助线：推理结构
- 题型：三段论 / 判断 / 推理（作为科学思维三特征落地的推理骨架）。
- 逻辑形式：此问可放在交叉题中辅助理解，但卷面主骨架是科学思维三特征，不要把它写成典型三段论题。
- 解题动作：推理侧只提醒学生：结论必须由材料事实支撑；真正展开时仍回到客观性、预见性、可检验性。
- 易错陷阱：只列特征无材料分析丢分；混淆三特征扣分；漏特征扣分。
- 同类题索引：Q-2024朝阳期中-7；Q-2026顺义一模-19-1。
