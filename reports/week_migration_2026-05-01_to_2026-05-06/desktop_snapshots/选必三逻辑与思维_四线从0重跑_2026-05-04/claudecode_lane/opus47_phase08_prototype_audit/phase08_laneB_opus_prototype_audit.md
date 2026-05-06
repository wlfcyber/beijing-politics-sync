# Phase08 ClaudeCode Lane B Opus Prototype Audit (REVIEW ONLY)

- audit_time: 2026-05-05 CST
- model: claude-opus-4-7 (max/adaptive thinking)
- prototype_status: review_only
- student_permission: no
- word_pdf_permission: no
- final_pass_permission: no
- input_freeze_rows: 29
- hold_rows_excluded: 45
- L0_rows_excluded: 288
- audit_lane: ClaudeCode Lane B
- audit_target: Claude Opus Phase08 teaching-text prototype (review-only)

This audit does not modify Opus prototype files. It does not authorize student稿, Word/PDF, final PASS, or 宝典成品.

## 1. Inputs Read

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
17. `~/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`

## 2. Counts Cross-Check

- freeze rows: 29 (`include` 4 + `include_as_packet_candidate` 25)
- prototype CSV rows: 29 (header + 29 data; 7-column schema correct)
- change log CSV rows: 29 (header + 29 data; 10-column schema correct)
- prototype MD `### Q-` blocks: 29
- module distribution (思维 13 / 推理 11 / 交叉 5): matches freeze
- status distribution (L4 = 4 → Q-2025海淀二模-20, Q-2025西城二模-16-2, Q-2025西城二模-16-3, Q-2026丰台一模-18-2; L3_candidate = 25): matches freeze
- hold rows excluded from prototype: 45 (all absent from rows)
- L0 rows excluded from prototype: 288 (all absent from rows)
- proto_id_set ∩ hold_id_set: ∅
- proto_id_set ∩ L0_id_set: ∅

## 3. P0 Findings

| # | Check | Status | Note |
|---|---|---|---|
| 1 | Required 6 Opus files exist | PASS | All present. |
| 2 | Prototype CSV exactly 29 rows + required columns | PASS | 7 columns, exact match. |
| 3 | Change log CSV exactly 29 rows + required columns | PASS | 10 columns, exact match. |
| 4 | Prototype id_set == freeze id_set | PASS | missing=[]; extra=[]; dup=0. |
| 5 | No hold row appears as prototype row | PASS | 0 intersection over 45 hold IDs. |
| 6 | No L0 row appears as prototype row | PASS | 0 intersection over 288 L0 IDs. |
| 7 | `student_permission=no`, `word_pdf_permission=no`, `final_pass_permission=no` visible | PASS | All four required Opus files declare these in header. |
| 8 | Change log sentinels all `must_be_no` | PASS | answer_changed/status_changed/question_deleted/question_added/pairing_changed all `must_be_no`; change_type ∈ {wording_only, structure_only}. |
| 9 | Q-2024西城一模-11 not a row, no `B=①④` correct result | PASS | Q-2024西城一模-11 absent as row; substring `B=①④` absent in all 29 generated_text and full MD. |
| 10 | Q-2025海淀二模-12 / Q-2025海淀二模-13 not rows | PASS | Both absent as rows. -12 referenced as bare ID once; -13 absent everywhere. |
| 11 | Q-2026顺义一模-3 not in reasoning prototype | PASS | Absent as row; appears only as bare ID in 思维同类题 lists of three thinking entries. |
| 12 | Q-2026丰台一模-18-2 keeps Phase07 patch boundary | PASS | Patch phrase preserved verbatim in CSV generated_text and MD 解题动作 line; answer_locator kept off prototype正文. |
| 13 | No generated_text contains forbidden internal terms | PASS | Substring scan for source locator/lane/Governor/Confucius/packet/L3/L4/`/Users/`/@L/Slide returns 0 hits in generated_text. |
| 14 | No generated_text contains final-artifact authorization | PASS | Substring scan for final PASS/Word/PDF/宝典成品/终稿/最终稿 returns 0 hits in generated_text. |

All P0 checks PASS.

## 4. P1 Findings

| # | Check | Status | Note |
|---|---|---|---|
| 15 | Cross rows visibly preserve double-mount policy | PASS | All 5 cross rows show 推理挂载 + 思维挂载 with 主挂载 / 次挂载 markers. |
| 16 | Reasoning rows do not collapse into generic推理知识点总论 | PASS | All 11 reasoning rows keep 题型 / 逻辑形式 / 规则口诀 / 有效式或错误式 / 解题动作 / 答案落点 / 易错陷阱 / 同类题. |
| 17 | Thinking rows do not collapse into generic知识摘要 | PASS | All 13 thinking rows keep 材料信号 / 可写思维方法 / 为什么能想到 / 答题动作 / 答案落点 / 易错陷阱 / 同类题. |
| 18 | Same-type IDs presented as IDs only when answer evidence not in row | PASS | All 同类题 lines tokenize to bare Q- IDs; hard-sample answer locks not exposed. |
| 19 | Review-only body has no source paths or raw locators | WARN | Six rows leak source-rubric file id fragments (`细则31`, `细则022`) or pipeline-internal jargon (`原始 phase07 数据`, `primary_reasoning_type`, `rule_slogan`) into review body. Details below; not in the explicit P0 forbidden term list, but inconsistent with the Opus boundary compliance claim "未引用任何文件路径、行号". |

### 4.1 Locator-cleanliness leakage detail (#19 WARN)

CSV `generated_text` leaks:

- `Q-2024朝阳一模-20-1`: contains `细则31先指出推理类型...` and `(2分)` — source-rubric file id `031` reduced to `31`.
- `Q-2024朝阳二模-19-1`: contains `细则022填空1=动态性,填空2=类比推理` and `依据细则022填空答案2分+保真表述3分` — file id `022` twice.
- `Q-2024朝阳二模-19-2`: contains `细则022联言判断本身2分+保真条件3分` and `依细则022 2+3 分写出联言判断成立条件` — file id `022` twice.
- `Q-2026顺义一模-19-2`: contains `原始 phase07 数据将 19(2) primary_reasoning_type 置为"三段论;判断;推理",rule_slogan 为"科学思维三特征"` — three internal pipeline names exposed.

MD body leaks:

- `Q-2025东城期末-13` 答案落点 line: `正确选项 B(原始 phase07 数据已锁定 B)`
- `Q-2025顺义一模-7` 答案落点 line: `正确选项 A(原始 phase07 数据锁定)`
- `Q-2024朝阳二模-19-1`, `Q-2024朝阳二模-19-2`, `Q-2024朝阳一模-20-1`: same `细则022` / `细则31` phrasing as CSV.

These do not match the explicit P0 forbidden-term list (`source locator`, `lane`, `Governor`, `Confucius`, `packet`, `L3`, `L4`, `/Users/`, `@L`, `Slide`), so P0 check #13 still PASSes. The findings are reported under #19 as P1 WARN because:

- `细则31` / `细则022` are recognizably file-index fragments mirroring the source ledger naming convention (`031_朝阳一模_细则.pptx`, `022_朝阳二模_细则.pdf`); a student-grade or final reviewer cannot use these tokens.
- `phase07` / `primary_reasoning_type` / `rule_slogan` are pipeline-internal vocabulary; the boundary compliance file's #6 claim that 内部术语 only appear in compliance/audit columns is partially false for these strings.
- Codex A's automated `P1_generated_text_forbidden_terms` test passed because it filtered against the same exact list; Lane B's independent sweep is what flushes these out — exactly the cross-lane redundancy the run is designed to use.

## 5. P2 / P3 Style and Transfer Observations (note only, do not patch)

- `Q-2024朝阳一模-7` (answer = C) and `Q-2024朝阳一模-9` (answer = D): MD bodies discuss the correct option markers (②③ / ③④) but never lift the explicit answer letter (`选 C` / `选 D`) into 答题动作 / 答案落点. Other 选择题 rows (Q-2024朝阳期中-7, Q-2024朝阳期中-9, Q-2025东城期末-13, Q-2025丰台期末-7, Q-2025丰台期末-8, Q-2025顺义一模-7) do lift the letter. The two omissions are review-readability gaps, not boundary violations.
- `Q-2025丰台期末-7` 答案落点 reads `在"哲学题、选必三超前思维作干扰"这一类型上确认 C 项` — a slightly audit-flavored 类型标签 phrasing inside an answer line; teaching-readable but worth softening before student稿.
- `Q-2025丰台期末-8`, `Q-2025海淀期末-17-1`, `Q-2025海淀期末-18` thinking rows read cleanly and student-friendly; cross-lane consistency between MD and CSV `generated_text` is high.
- Cross 双挂载 sections are visually clean; redundant wording between thinking and reasoning挂载 has been compacted as the prompt allowed, but neither mount has been deleted.
- `opus_self_note` column intentionally carries audit phrases (`LOCKED_FOR_FUSION`, `patch freeze`, `framework_node`, `A-formal`, `primary_reasoning_type`); this is consistent with the Phase08 boundary compliance convention that classifies opus_self_note as audit, not正文. Recorded as P3 INFO only.

## 6. Hard Sample Locks (cross-check)

- `Q-2024西城一模-11` (corrected pairing `B=①③`): not a prototype row; appears once as bare ID inside `Q-2024朝阳期中-9` 同类题 list; old wrong `B=①④` does not appear anywhere as a correct result. **Lock preserved.**
- `Q-2025海淀二模-12` (answer D): not a prototype row; appears once as bare ID inside `Q-2025丰台期末-7` 同类题 list. **Lock preserved.**
- `Q-2025海淀二模-13` (answer C): not a prototype row; absent from every 同类题 list. **Lock preserved (strict).**
- `Q-2026顺义一模-3`: not a prototype row; appears only in 思维同类题 lists of `Q-2024朝阳一模-9`, `Q-2025海淀二模-20`, `Q-2026朝阳期中-20`; never enters 推理 prototype. **Lock preserved.**
- `Q-2026丰台一模-18-2`: present as L4 reasoning row; 解题动作 reproduces the Phase07 patch phrase verbatim; `answer_locator` `answer_confirmed_甲正确乙错误_from_043_slide35_36_rubric` confined to audit/compliance columns; 易错陷阱 keeps "甲不可写演绎推理 / 乙先找结论再定大项" rule. **Patch boundary preserved.**

## 7. Cross-Lane Consistency

- Codex A `phase08_codexA_opus_prototype_verification.md` reports `PASS_CODEXA_PHASE08_OPUS_PROTOTYPE_VERIFICATION` with 0 failures across 22 P0/P1 checks plus 2 P2 INFO entries.
- Lane B independently agrees on all 14 P0 checks and on P1 checks #15–#18.
- Lane B disagrees on P1 check #19 (locator cleanliness): Codex A's check used the exact P0 forbidden-term list and missed source-file-id fragments and pipeline jargon that Lane B's regex sweep flushed out.
- This is a constructive cross-lane delta, not a contradiction: Codex A's pass is correct under the strict-letter forbidden list; Lane B's WARN is correct under the spirit of #19 plus the boundary compliance file's own claim of cleanliness. Both lanes recommend the prototype move forward into Governor/Confucius and GPT review-only gates — Lane B requests the locator residues be cleaned in the next iteration.

## 8. Boundary Reaffirmation

This audit:

- does not authorize student稿;
- does not authorize Word/PDF;
- does not authorize final PASS;
- does not authorize 宝典成品;
- does not modify any Phase07 input file;
- does not modify any Opus prototype file;
- does not modify any Codex A verification file;
- writes only inside `claudecode_lane/opus47_phase08_prototype_audit/`.

## 9. Verdict

PASS_PHASE08_PROTOTYPE_AUDIT_WITH_WARNINGS
