# GPT-5.5 Pro Phase08 Commander Review Prompt

你是本轮“飞哥政治庄园”四线工作流里的 GPT-5.5 Pro 阶段总指挥/内容风险审稿人。

请审查 Phase08：选必三《逻辑与思维》从0重跑的 Opus review-only 教学原型。你这次要做“内容风险 + 迁移价值 + 是否可进入下一阶段”的阶段裁决。

## 当前运行背景

- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- 范围：选必三《逻辑与思维》分两部分处理：
  - 思维部分：完全模仿此前“哲学宝典”的触发链工作流；每个思维/方法相当于哲学原理方法论，要穷尽题目并能转化为学生可迁移的触发链。
  - 推理部分：按题型分类（三段论、假言推理、联言/选言、归纳/类比、定义/概念等），所有题归入对应题型下。
- GPT 和 Claude/Opus 只能做指挥/审稿/成文化建议，不是证据来源；任何新内容后续必须回本地证据验证。
- 当前仍禁止：学生稿、Word/PDF、final PASS、终稿、最终稿、宝典成品。

## 你需要给出的 verdict

请在回复开头给一个明确 verdict，最好四选一：

1. `GO_TO_PHASE09_STUDENT_DRAFT_CONSTRUCTION_NO_WORD_NO_FINAL`
2. `PATCH_PHASE08_BEFORE_STUDENT_DRAFT`
3. `RUN_ADDITIONAL_LANEB_AUDIT`
4. `STOP_SOURCE_REPAIR_REQUIRED`

然后请给：

- 你是否认可 Phase08 review-only prototype 已足够进入“受控学生稿构建阶段”。
- 如果进入 Phase09，边界是什么：能写什么、不能写什么，尤其是否仍禁止 Word/PDF/final PASS。
- 当前 29 行里你发现的具体内容风险或教学表达风险，按题号列出。
- 是否需要重新跑 ClaudeCode Lane B，还是 Codex A 的 patch + gate 足够进入 GPT 指定的下一阶段。
- 若进入 Phase09，请列出你要求 Codex/Claude/Opus 执行的 5-10 条硬规则。

---

# Phase08 GPT Commander Review Packet

Request: review the Phase08 Opus review-only teaching prototype after Codex A verification, ClaudeCode Lane B audit, and Lane B warning patch. Decide whether to patch more, run another audit, or allow the next controlled student-draft construction phase. Do not authorize final delivery yet unless you explicitly set a later gated path.

## Current Phase Boundary

- current phase: Phase08 review-only teaching prototype
- student稿: forbidden unless GPT explicitly opens the next controlled construction phase
- Word/PDF: forbidden
- final PASS: forbidden
- 终稿/最终稿/宝典成品: forbidden
- hold rows excluded: 45
- L0 rows excluded: 288

## Core Outputs To Review

- `05_coverage/phase08_opus_prototype_input_freeze.csv`
- `05_coverage/phase08_opus_prototype_input_freeze.md`
- `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md`
- `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv`
- `07_student_prototype/phase08_opus_change_log.md`
- `07_student_prototype/phase08_opus_change_log.csv`
- `opus_writer/phase08_teaching_prototype/phase08_opus_boundary_compliance.md`
- `08_review/phase08_codexA_opus_prototype_verification.md`
- `claudecode_lane/opus47_phase08_prototype_audit/phase08_laneB_opus_prototype_audit.md`
- `claudecode_lane/opus47_phase08_prototype_audit/phase08_laneB_opus_prototype_audit_findings.csv`
- `claudecode_lane/opus47_phase08_prototype_audit/phase08_laneB_opus_prototype_audit_blockers.md`
- `08_review/phase08_laneB_warning_patch_resolution.md`
- `08_review/phase08_codexA_opus_prototype_verification_after_laneB_patch.md`
- `05_coverage/phase08_Governor_prototype_boundary_gate.md`
- `05_coverage/phase08_Confucius_learning_value_gate.md`

## Counts

- Phase08 prototype input rows: 29
- allowed rows: 4 `include` + 25 `include_as_packet_candidate`
- prototype CSV rows: 29
- prototype Markdown question blocks: 29
- module counts: `思维=13 / 推理=11 / 交叉=5`
- status counts: `L3_candidate=25 / L4=4`
- hard hold rows excluded: 45
- L0 rows excluded: 288
- Codex A local post-patch failures: 0
- Lane B blockers: 0

## Lane B Audit And Patch Summary

ClaudeCode Lane B Phase08 audit verdict: `PASS_PHASE08_PROTOTYPE_AUDIT_WITH_WARNINGS`.

Warnings patched before this GPT review:

- removed `细则31` / `细则022` file-id style wording from teaching body;
- removed `phase07`, `primary_reasoning_type`, `rule_slogan` pipeline terms from teaching body;
- added explicit answer letters for `Q-2024朝阳一模-7` and `Q-2024朝阳一模-9`;
- softened the audit-flavored answer-line label in `Q-2025丰台期末-7`;
- rebuilt the prototype CSV from cleaned Markdown plus Phase08 freeze after a local CSV writer failure; rebuilt CSV passes all count/ID/cleanliness checks.

## Hard Samples

- `Q-2024西城一模-11`: not a prototype row; old wrong pairing must not reappear.
- `Q-2025海淀二模-12`: not a prototype row.
- `Q-2025海淀二模-13`: not a prototype row.
- `Q-2026顺义一模-3`: not a prototype row and must not enter reasoning prototype.
- `Q-2026丰台一模-18-2`: remains an L4 reasoning row with the locked action chain preserved.

## Questions For GPT-5.5 Pro

1. Does Phase08, after Lane B warning patch, pass as a review-only teaching prototype?
2. Are there any content risks in the current 29 rows that must be patched before moving toward a controlled student-draft construction phase?
3. Should the next phase be:
   - `GO_TO_PHASE09_STUDENT_DRAFT_CONSTRUCTION_NO_WORD_NO_FINAL`,
   - `PATCH_PHASE08_BEFORE_STUDENT_DRAFT`,
   - `RUN_ADDITIONAL_LANEB_AUDIT`,
   - or `STOP_SOURCE_REPAIR_REQUIRED`?
4. If you authorize Phase09, what exact gates should remain before Word/PDF and final delivery?


---

# Governor Gate

# Phase08 Governor Prototype Boundary Gate

Verdict: `PASS_REVIEW_ONLY_PROTOTYPE_BOUNDARY_PENDING_GPT`

This gate does not authorize student稿, Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品.

## Inputs Checked

- `05_coverage/phase08_opus_prototype_input_freeze.csv`
- `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md`
- `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv`
- `08_review/phase08_codexA_opus_prototype_verification.md`
- `claudecode_lane/opus47_phase08_prototype_audit/phase08_laneB_opus_prototype_audit.md`
- `08_review/phase08_laneB_warning_patch_resolution.md`
- `08_review/phase08_codexA_opus_prototype_verification_after_laneB_patch.md`

## Boundary Checks

- PASS: prototype CSV rows = 29.
- PASS: prototype Markdown question blocks = 29.
- PASS: prototype CSV question IDs equal Phase08 freeze question IDs.
- PASS: duplicate question IDs = 0.
- PASS: module counts = `思维=13 / 推理=11 / 交叉=5`.
- PASS: status counts = `L3_candidate=25 / L4=4`.
- PASS: no hold rows appear as prototype rows.
- PASS: no L0 rows appear as prototype rows.
- PASS: hard excluded rows remain absent as rows: `Q-2024西城一模-11`, `Q-2025海淀二模-12`, `Q-2025海淀二模-13`, `Q-2026顺义一模-3`.
- PASS: `Q-2026丰台一模-18-2` remains L4 and keeps the locked answer-action wording.
- PASS: generated_text cleanliness scan returns 0 hits for `phase07`, `Phase07`, `primary_reasoning_type`, `rule_slogan`, `细则31`, `细则022`, `cross_reference_policy`, `reduce repetitive wording`, `source locator`, `framework_node`, `LOCKED_FOR_FUSION`, `A-formal`, `B-choice-signal`, `/Users/`, `Governor`, `Confucius`, `packet`, and final-artifact terms.
- PASS: Lane B warnings F-LB08-01 through F-LB08-11 are patched; F-LB08-12 remains audit-column-only.

## Recovery Note

Codex A caught and repaired a local CSV patching failure. The prototype CSV was rebuilt from cleaned Markdown plus Phase08 freeze. The corrupt pre-rebuild file is preserved for audit as `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv.corrupt_before_rebuild_20260505_011101.bak`.

## Gate Boundary

Phase08 remains review-only. Promotion requires GPT Phase08 commander review before any student-facing drafting or document generation.


---

# Confucius Gate

# Phase08 Confucius Learning Value Gate

Verdict: `PASS_REVIEW_ONLY_PROTOTYPE_VALUE_PENDING_GPT`

This is a learning-value gate for the review-only prototype. It does not authorize student稿, Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品.

## Checks

- PASS: 思维 rows keep the teachable chain `材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题`.
- PASS: 推理 rows keep the teachable chain `题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点/易错陷阱 -> 同类题`.
- PASS: 交叉 rows keep double-mount teaching structure with `推理挂载(主挂载)` and `思维挂载(次挂载)`.
- PASS: two choice-question readability gaps are patched: `Q-2024朝阳一模-7` explicitly writes `正确选项 C(②③)`; `Q-2024朝阳一模-9` explicitly writes `正确选项 D(③④)`.
- PASS: hard-sample boundaries are teachable without leaking excluded answers: `Q-2024西城一模-11`, `Q-2025海淀二模-12`, `Q-2025海淀二模-13`, and `Q-2026顺义一模-3` are not rows.
- PASS: `Q-2026丰台一模-18-2` preserves the useful classroom action chain: identify 甲 as necessary-condition hypothetical inference and identify 乙 as major-term illicit process.
- PASS: same-type references remain question IDs rather than unverified answer expansions.
- PASS: review-body language is cleaner after Lane B patch; source locator and pipeline terms no longer sit inside generated_text.

## Learning-Value Judgment

The prototype is strong enough to send to GPT-5.5 Pro for commander review. It is not yet a final student handout: GPT should decide whether to request another patch, authorize a broader student稿 construction phase, or require further source repair.


---

# Codex A Post-Patch Verification

# Phase08 Codex A Verification After Lane B Patch

- verification_time: 2026-05-05 CST
- status: `PASS_CODEXA_PHASE08_AFTER_LANEB_PATCH`
- prototype_status: review_only
- student_permission: no
- word_pdf_permission: no
- final_pass_permission: no

## Result

Codex A patched Lane B's Phase08 warnings and locally reaudited the prototype. The prototype remains review-only.

Key checks:

- CSV rows: 29.
- Markdown question blocks: 29.
- CSV ID set equals Phase08 freeze ID set.
- duplicate IDs: 0.
- module counts: `思维=13 / 推理=11 / 交叉=5`.
- status counts: `L3_candidate=25 / L4=4`.
- generated_text forbidden-term hits: 0.
- hard-excluded rows remain absent as rows: `Q-2024西城一模-11`, `Q-2025海淀二模-12`, `Q-2025海淀二模-13`, `Q-2026顺义一模-3`.
- `Q-2024朝阳一模-7` contains `正确选项 C(②③)`.
- `Q-2024朝阳一模-9` contains `正确选项 D(③④)`.
- `Q-2026丰台一模-18-2` remains present as L4 and keeps the locked patch action wording.

## Notes

The CSV was rebuilt from the cleaned Markdown and Phase08 input freeze after a first patch script truncated the CSV. This recovery is recorded in `08_review/phase08_laneB_warning_patch_resolution.md`; the corrupt pre-rebuild file is preserved as a backup for audit.

This verification does not authorize student稿, Word/PDF, final PASS, or any final-delivery language.


---

# Lane B Warning Patch Resolution

# Phase08 Lane B Warning Patch Resolution

- patch_time: 2026-05-05 CST
- phase: Phase08 Opus teaching prototype, review-only
- source_audit: `claudecode_lane/opus47_phase08_prototype_audit/phase08_laneB_opus_prototype_audit.md`
- source_verdict: `PASS_PHASE08_PROTOTYPE_AUDIT_WITH_WARNINGS`
- blocker_status: `NO_PHASE08_PROTOTYPE_BLOCKERS_DETECTED`
- patch_status: `PATCHED_AND_LOCAL_REAUDITED`
- student_permission: no
- word_pdf_permission: no
- final_pass_permission: no

## What Was Patched

Lane B found no blockers, but it correctly caught review-body cleanliness residue:

- file-id style wording: `细则31`, `细则022`;
- pipeline-field wording: `phase07`, `primary_reasoning_type`, `rule_slogan`;
- two choice rows missing explicit answer letters in the teaching body;
- one audit-flavored answer-line label in `Q-2025丰台期末-7`.

Codex A patched only teaching expression. It did not change question IDs, answers, statuses, pairings, double mounts, freeze inputs, hold rows, or L0 exclusions.

## CSV Recovery Note

During the first patch attempt, the structured CSV writer failed on the prototype CSV and truncated `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv` to a header plus one row. This was caught immediately.

Recovery action:

- rebuilt the CSV from the already-cleaned Markdown body plus `05_coverage/phase08_opus_prototype_input_freeze.csv`;
- preserved the corrupt pre-rebuild file as `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv.corrupt_before_rebuild_20260505_011101.bak`;
- rebuilt output has 29 rows, exact freeze ID set, module counts `思维=13 / 推理=11 / 交叉=5`, status counts `L3_candidate=25 / L4=4`;
- generated_text forbidden-term scan returns 0 hits.

## Post-Patch Local Reaudit

- `phase08_opus_teaching_prototype_REVIEW_ONLY.csv`: 29 data rows.
- `phase08_opus_teaching_prototype_REVIEW_ONLY.md`: 29 `### Q-...` blocks.
- prototype CSV ID set equals Phase08 freeze ID set.
- duplicate IDs: 0.
- hard-excluded rows remain absent as rows: `Q-2024西城一模-11`, `Q-2025海淀二模-12`, `Q-2025海淀二模-13`, `Q-2026顺义一模-3`.
- `Q-2024朝阳一模-7` now explicitly contains `正确选项 C(②③)`.
- `Q-2024朝阳一模-9` now explicitly contains `正确选项 D(③④)`.
- `Q-2026丰台一模-18-2` remains present as L4 and keeps the Phase07 patch action wording.

## Boundary

This patch still does not authorize student稿, Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品. Next gate remains Governor/Confucius review-only gate and GPT Phase08 commander review.


---

# ClaudeCode Lane B Phase08 Audit Report

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


---

# Phase08 Review-Only Prototype Body To Review

prototype_status: review_only
student_permission: no
word_pdf_permission: no
final_pass_permission: no
input_freeze_rows: 29
hold_rows_excluded: 45
L0_rows_excluded: 288

# 选必三《逻辑与思维》教学原型(REVIEW ONLY)

本文件是 review-only 教学原型,不是学生稿,不是最终稿,不是 Word/PDF,不是宝典成品。所有正文条目仅来自冻结的 29 行输入,不引入新题、不改答案、不改归类、不改交叉双挂载。每条保留 question_id 供后续审核回查。

## 阅读说明

- 思维部分按"材料信号→可写思维方法→为什么能想到→答题动作→答案落点→易错陷阱→同类题"组织。
- 推理部分按"题型→规则口诀→常见陷阱→同类真题→解题动作"组织;每条保留 question_id 不脱离题目定位。
- 交叉双挂载部分保留思维和推理两次挂载;主挂载为推理题型,次挂载为思维框架,二者不可单挂。
- 任何"同类题"列表只列 question_id,不写其答案细节,以避免触动其他题目的答案锁。

---

## 第一部分 思维原型(13 题)

### Q-2024朝阳一模-7

- 题目来源简记:2024 朝阳一模 第 7 题,选择题。
- 材料信号:题干列出"原始创新、集成创新、开放创新一体设计";选项分别讨论 ①迁移想象逆向、②集成创新跨越性与逻辑推导并行、③开放创新对前人成果的继承借鉴、④发散与聚合贯通。
- 可写思维/方法:创新思维,内含发散、聚合、逆向、超前、迁移等具体方法。
- 为什么能想到:题干把"创新"与"逻辑"放在一起,让学生在创新思维总称下区分逻辑思维参与的环节;②把跨越性与逻辑推导并列、③把合作创新落在对已有成果的继承上,正好对应"创新思维与逻辑思维并行"和"辩证否定式继承"。
- 答题动作:②集成创新具有跨越性,但不排斥有步骤的逻辑推导与分析,体现创新思维与逻辑思维的并行;③开放创新中的合作创新,需要对前人和他人的已有成果进行继承与借鉴,体现辩证否定意义上的继承。
- 答案落点:正确选项 C(②③),重点写清创新思维不排斥逻辑分析、合作创新建立在对前人成果继承之上。
- 易错陷阱:①把"迁移、想象、逆向"误归入逻辑思维,实际它们是创新思维的具体方法,属于混用错;④"有效贯通...就能确保..."表述绝对化。
- 同类题:Q-2025东城期末-18-2;Q-2025海淀期末-18;Q-2025西城二模-16-3;Q-2026东城一模-19-4;Q-2026朝阳期中-21-2;Q-2026通州期末-9。

### Q-2024朝阳一模-9

- 题目来源简记:2024 朝阳一模 第 9 题,选择题。
- 材料信号:中学生模拟政协活动从"模拟提案"到"正式提案",经历调查、充实、完善、提交的多环节配合;市政协委员承接、指导、提交。
- 可写思维/方法:辩证思维与系统观念中的整体性。
- 为什么能想到:从"模拟"到"正式"涉及多主体、多环节协同,正是把多个分散动作整合为整体方案的过程;③对应系统观念的整体性体现,④涉及对中国特色社会主义制度优势的运用与理解。
- 答题动作:③系统观念在调查研究和思考任务中的整体性体现;④对中国特色社会主义制度优势的运用与理解。
- 答案落点:正确选项 D(③④),点出活动是多主体协同完成、整体性贯穿调查与提案全过程,并指向制度优势的运用。
- 易错陷阱:①把"具体政策制定"当作此活动主旨,偏离活动定位;②把活动写成"引领社会治理",拔高过度。
- 同类题:Q-2024朝阳二模-19-1;Q-2024朝阳二模-19-2;Q-2025东城期末-5;Q-2025海淀二模-20;Q-2025海淀期末-2;Q-2026朝阳期中-20;Q-2026通州期末-11;Q-2026通州期末-5;Q-2026通州期末-8;Q-2026顺义一模-3。

### Q-2024海淀二模-17-1

- 题目来源简记:2024 海淀二模 第 17 题第(1)问,主观题。
- 材料信号:全国时间利用调查围绕个人生理必需活动、有酬劳动、无酬劳动、个人自由支配活动等多类时间投入,目的是全面、真实、准确反映居民生活质量与生活模式。
- 可写思维/方法:科学思维、辩证思维、创新思维三角度并列;具体可调用客观性、整体性、发散与聚合、超前思维以及思维抽象/思维具体/感性具体。
- 为什么能想到:本题要求从三个角度分别采分,科学思维对应客观性与预见性、创新思维对应"三新"与发散聚合、超前,辩证思维对应整体性与分析综合;每一角度都要落到时间利用调查的具体动作上才不丢分。
- 答题动作:三角度多挂载、按表格化采分;科学思维 2 分(客观性、预见性),创新思维 3 分(三新、发散聚合、超前),辩证思维 2 分(整体性、分析综合);每个分点必须结合材料分析。
- 答案落点:逐角度一句话作答,每条带"调查内容/调查动作 + 思维方法 + 作用结论"。
- 易错陷阱:只列知识点而不结合材料,只能拿基础 1 分;混淆角度归属(把"整体性"写到科学思维下、把"客观性"写到创新思维下)直接丢分。
- 同类题:Q-2024朝阳二模-7;Q-2024朝阳期中-19;Q-2024海淀二模-17-2;Q-2025海淀期末-17-1;Q-2026顺义一模-19-1;Q-2026顺义一模-19-2。

### Q-2024海淀二模-17-2

- 题目来源简记:2024 海淀二模 第 17 题第(2)问,主观题。
- 材料信号:同一调查的两阶段任务——"调查了解居民时间利用情况"对应感性具体阶段;"分析研究居民时间利用情况"对应思维抽象再到思维具体阶段。
- 可写思维/方法:科学思维(认识论维度);感性具体、思维抽象、思维具体三层。
- 为什么能想到:题目把"调查了解"和"分析研究"区分开,正是"杂多现象→抽出核心概念→回到完整整体图景"链条;严禁把方向写反。
- 答题动作:调查了解 = 感性具体(1 分);分析研究 = 思维抽象 + 思维具体(1 分);两阶段相互依赖、不可割裂(2 分)。
- 答案落点:按"调查了解→感性具体→获得对象的整体表象;分析研究→思维抽象抓住本质→思维具体重建完整图景;两阶段相互依赖共同形成科学认识"作答。
- 易错陷阱:把感性具体和思维具体的方向颠倒不给分;用"实践决定认识"替代具体环节只能得 1 分。
- 同类题:Q-2024朝阳二模-7;Q-2024朝阳期中-19;Q-2024海淀二模-17-1;Q-2025海淀期末-17-1;Q-2026顺义一模-19-1;Q-2026顺义一模-19-2。

### Q-2025丰台期末-7

- 题目来源简记:2025 丰台期末 第 7 题,选择题(漫画启示)。
- 材料信号:漫画呈现纠结于昨天与明天而忽视当下的状态;选项以"超前思维""集中关注当下"等做干扰。
- 可写思维/方法:本题答案落点不在选必三的"超前思维",而在哲学唯物论的"从实际出发、从当下做起"。选必三的"超前思维"在选项里是干扰项。
- 为什么能想到:漫画反向呈现,选超前思维就掉入干扰;只有"从实际出发、从当下做起"对应漫画核心。
- 答题动作:选 C。"从实际出发,从当下做起,生活才能少些迷茫"对应哲学唯物论与实事求是。
- 答案落点:正确选项 C,落在哲学唯物论“从实际出发、从当下做起”;选必三“超前思维”只是干扰项。
- 易错陷阱:A"集中关注当下,就能活出最美的样子"绝对化;B"超前思维就能创造幸福"既夸大又与漫画反义,选必三作干扰;D"弄清意义是成功的关键"过度推论。
- 同类题:Q-2025海淀二模-12。

### Q-2025丰台期末-8

- 题目来源简记:2025 丰台期末 第 8 题,选择题(现代诗解读)。
- 材料信号:《和平是一棵树》以白天鹅翅膀、湖水云影、门、红酒、灯等多个具体形象层层展开,从不同方向表达对和平的向往。
- 可写思维/方法:发散思维 + 形象思维。
- 为什么能想到:多个具体意象向同一主题"和平"发散,正是发散思维;以白天鹅翅膀、门、红酒等具体形象触及和平本质,正是形象思维。
- 答题动作:选 D。②运用发散思维表达人们对和平的向往与追求;④以形象思维触及和平的本质特征。
- 答案落点:在"形象思维、发散思维"这一类型上得分;指出诗歌从多个意象发散表达,并以具体形象触及和平本质。
- 易错陷阱:①把"想象"当作思维的基本单元(基本单元是概念,不是想象);③把本诗当作抽象思维(本诗用形象,不用抽象)。
- 同类题:Q-2026顺义一模-5。

### Q-2025海淀二模-20

- 题目来源简记:2025 海淀二模 第 20 题,主观题(辩证思维复合题)。
- 材料信号:材料给出全民共享、全面共享、共建共享、渐进共享四个层次;设问要求运用辩证思维谈如何坚持共享发展理念推进共同富裕。
- 可写思维/方法:辩证思维总称下,可调用整体性、动态性、分析与综合、质量互变、辩证否定。
- 为什么能想到:题目要求"运用辩证思维",并把共享拆为四个层次,要求学生从角度池中选取与材料事实匹配的辩证维度作答;不是三点全必答。
- 答题动作:在角度池"整体性 / 动态性 / 分析与综合 / 质量互变 / 辩证否定"中选 2 个角度组合作答,角度池 1 + 角度池 2 赋分,选 2 上限 6 分,矛盾相关至多 2 分;每条带"共享层次 + 辩证维度 + 推进共同富裕作用"。
- 答案落点:每个角度落到具体共享层次,例如以整体性把共建共享与共同富裕的整体推进结合,以动态性把渐进共享与阶段任务结合,以质量互变把全面共享与积累—跃升结合等。
- 易错陷阱:写成"三点全必答"会触发上限保护;把辩证否定理解为"否定一切"会丢分;整体性必须含联结/综合/系统优化层面,不能只写"整体"两字。
- 同类题:Q-2024朝阳一模-9;Q-2024朝阳二模-19-1;Q-2024朝阳二模-19-2;Q-2025东城期末-5;Q-2025海淀期末-2;Q-2026朝阳期中-20;Q-2026通州期末-11;Q-2026通州期末-5;Q-2026通州期末-8;Q-2026顺义一模-3。

### Q-2025海淀期末-17-1

- 题目来源简记:2025 海淀期末 第 17 题第(1)问,主观题。
- 材料信号:杂志刊登的"永动机"设计图——盆水、架子、叶轮、毛巾,通过毛细作用吸水再滴水推动叶轮,声称无需外力实现永动。
- 可写思维/方法:科学思维(客观性维度)。
- 为什么能想到:题干明确"运用科学思维知识",材料以违反客观规律的设想登场;客观性要求"如实反映对象、把握客观规律",而毛巾毛细作用吸水高度有限,不可能维持永动。
- 答题动作:从实际出发、如实反映对象、把握客观规律;指出毛巾毛细作用吸水的高度有限,水量与摩擦消耗使设计无法实现永动。
- 答案落点:写出"科学思维要求客观性,从实际出发把握客观规律;永动机设计违背了客观规律,所以无法成立"的卷面作答句。
- 易错陷阱:用辩证思维或创新思维替代客观性会丢分。
- 同类题:Q-2024朝阳二模-7;Q-2026顺义一模-19-1;Q-2026顺义一模-19-2。

### Q-2025海淀期末-18

- 题目来源简记:2025 海淀期末 第 18 题,主观题。
- 材料信号:北京城市图书馆从"人找书"转向"书找人",建筑设计借用赤印意象,以数字技术为依托、构建立体化数字文化服务。
- 可写思维/方法:创新思维总称下,具体落到联想思维、逆向思维、迁移。
- 为什么能想到:"人找书→书找人"是把已有结构与顺序反过来,典型的逆向思维;"赤印意象→建筑设计"是从文化符号到空间形态的同化性迁移,典型的联想思维。
- 答题动作:逆向思维=对事物结构与顺序的已有认识进行反向思考(人找书→书找人);联想思维=同化性迁移(赤印意象→建筑设计)。
- 答案落点:每条带"创新思维子方法 + 材料动作 + 服务/价值结果",分别写逆向、联想两条。
- 易错陷阱:用"创新思维"总称替代逆向/联想会扣分;混淆迁移类型(把同化性写成顺应性)会扣分。
- 同类题:Q-2024朝阳一模-7;Q-2025东城期末-18-2;Q-2025西城二模-16-3;Q-2026东城一模-19-4;Q-2026朝阳期中-21-2;Q-2026通州期末-9。

### Q-2025西城二模-16-3

- 题目来源简记:2025 西城二模 第 16 题第(3)问,主观题。
- 材料信号:延庆区自然保护地管理处针对鹿叫村遗址的废弃水井和地窖,建造攀爬台阶、营造雨水收集池等改造,便于不同体型动物自由取水。
- 可写思维/方法:创新思维(改变与创造条件,建立新的具体联系)。
- 为什么能想到:旧设施(废井、地窖)长期对动物造成威胁,通过营建台阶、收集池等具体改造,把"威胁性结构"转化为"取水通道",体现创新思维改变和创造条件、建立新的具体联系。
- 答题动作:运用创新思维改变和创造条件,把废弃水井改造为可取水的设施,把雨水收集池布局成动物可达的取水点,从而建立新的人—野生动物—资源联系。
- 答案落点:写"创新思维改变和创造条件 + 改造措施 + 形成新的具体联系"卷面作答句。
- 易错陷阱:本题不是推理题;子问拆分后第(3)问归思维/创新,不可与同题第(2)问的推理类型混淆。
- 同类题:Q-2024朝阳一模-7;Q-2025东城期末-18-2;Q-2025海淀期末-18;Q-2026东城一模-19-4;Q-2026朝阳期中-21-2;Q-2026通州期末-9。

### Q-2026东城一模-19-4

- 题目来源简记:2026 东城一模 第 19 题第(4)问,主观题。
- 材料信号:中关村特色产业园围绕人工智能、生物制造等前沿领域,从"0→1 原始突破"到"把 1 拉长"的系统跃升,涉及单点突破到链式扩展的全过程。
- 可写思维/方法:系统观念 + 创新思维;具体可调用整体性、动态性、分析与综合、发散、聚合、超前。
- 为什么能想到:题干明确"运用系统观念与创新思维",材料从原始突破写到链式扩展,正好对应系统观念的整体性与创新思维的从单点到链式;两类思维并行采分。
- 答题动作:以系统观念把握整体布局与协同跃升;以创新思维实现从原始突破到链式扩展;具体到中关村产业园发展目标(人工智能、生物制造等领域),拿出可落地的措施。
- 答案落点:每条带"思维方法 + 材料事实 + 园区发展作用",一句话写到具体园区目标。
- 易错陷阱:措施缺乏具体性扣分;不符合中关村发展目标(脱离前沿产业、脱离园区载体)扣分。
- 同类题:Q-2024朝阳一模-7;Q-2025东城期末-18-2;Q-2025海淀期末-18;Q-2025西城二模-16-3;Q-2026朝阳期中-21-2;Q-2026通州期末-9。

### Q-2026朝阳期中-20

- 题目来源简记:2026 朝阳期中 第 20 题,主观题。
- 材料信号:百年未有之大变局背景下,新一轮科技革命与产业变革深入发展,国际力量对比深刻调整;同时逆全球化、单边主义、局部冲突等风险并存,我国发展面临新的战略机遇与新的动荡变革期。
- 可写思维/方法:辩证思维总称下,可调用整体性、动态性、分析与综合、质量互变。
- 为什么能想到:题干明确"运用辩证思维方法",材料把机遇与挑战并列、把当前与长远并列、把局部与全局并列;正是矛盾对立统一+整体性统筹+动态性应变。
- 答题动作:辩证思维=矛盾对立统一(机遇与挑战);整体性=统筹全局(发展、安全、内外);动态性=主动应变(把握战略机遇、化解风险);"一分为二"+"多维施策"组合作答。
- 答案落点:每条带"辩证维度 + 材料事实 + 战略意义"卷面作答句,机遇与挑战、整体与动态分别落实。
- 易错陷阱:误用单一矛盾或仅讲机遇/挑战丢分;漏整体性或动态性扣分。
- 同类题:Q-2026顺义一模-3。

### Q-2026朝阳期中-21-2

- 题目来源简记:2026 朝阳期中 第 21 题第(2)问,主观题。
- 材料信号:人文经济学强调"文化、人文、经济"三者有机统一,材料二涉及把传统物理空间转化为柔性业态、把"冷资源"开发为"热经济"、把历史/数字/社群等多业态整合。
- 可写思维/方法:创新思维总称下,具体落到联想、发散、聚合、逆向(可同步带超前)。
- 为什么能想到:"冷资源→热经济"是从一类对象迁移到另一类对象的联想;历史 + 数字 + 社群多业态铺开后再收束,是发散与聚合的组合;把"传统物理空间"反过来做柔性业态,是逆向思维。
- 答题动作:联想思维拓展价值(冷资源→热经济);发散与聚合整合业态(历史 + 数字 + 社群);逆向思维创造差异(传统物理空间→柔性业态)。
- 答案落点:每条带"创新子思维 + 材料动作 + 价值结果",分别落联想、发散与聚合、逆向三条。
- 易错陷阱:只列"运用创新思维"总称丢分;混淆联想/发散/聚合/逆向之间的归属扣分。
- 同类题:Q-2024朝阳一模-7;Q-2025东城期末-18-2;Q-2025海淀期末-18;Q-2025西城二模-16-3;Q-2026东城一模-19-4;Q-2026通州期末-9。

---

## 第二部分 推理原型(11 题)

### Q-2024朝阳一模-20-1

- 题目来源简记:2024 朝阳一模 第 20 题第(1)问,主观题。
- 题型:充分条件假言推理(否定后件式)。
- 逻辑形式:假言判断+充分条件+必要条件辨识;本题为充分条件假言推理。
- 规则口诀:"前真后必真;否定后件→否定前件"。
- 有效式或错误式:题干"如果 A 区域古代没有广泛生长竹子,就不可能有大量的炭化竹节"是充分条件假言判断,其结构允许"否定后件→否定前件"作为有效式;评分要求先指出推理类型(充分条件假言推理),再用"前真后必真,后假则前假"作为推理理由。
- 解题动作:① 识别题干为充分条件假言判断;② 套用"前真后必真;否定后件→否定前件"规则;③ 对照题干结论判断推理是否成立;④ 避开"假言推理结构识别错误""前后件颠倒""化作不完全归纳"等陷阱。
- 答案落点:写出"该推理为充分条件假言推理,依据 '前真后必真,后假则前假',否定后件可以否定前件"作答句。
- 易错陷阱:把充分条件假言写成必要条件;前后件颠倒;把演绎式假言写成不完全归纳。
- 同类题:Q-2024朝阳一模-20-2;Q-2026通州期末-19-2。

### Q-2024朝阳一模-20-2

- 题目来源简记:2024 朝阳一模 第 20 题第(2)问,主观题。
- 题型:必要条件假言推理(补充推理二)。
- 逻辑形式:假言判断+必要条件;本题为必要条件假言推理的补充。
- 规则口诀:"只有...才...;前件是后件的必要条件"。
- 有效式或错误式:补充式如"只有 A 区域古代气候温暖,A 区域古代才有可能生长竹子(必要条件假言)"+"A 区域古代广泛生长着竹子"→必要条件成立;补完整推理时必须保留"古代/当时"等时间表述,否则扣 1 分。
- 解题动作:① 识别题干为必要条件假言;② 套用"只有...才..."口诀;③ 把时间限定词(古代/当时)整体抄入,不可省略;④ 避开漏写时间表述等陷阱。
- 答案落点:写出"只有 A 区域古代气候温暖,A 区域古代才有可能生长竹子;A 区域古代广泛生长着竹子,所以..."的卷面作答句,保留"古代"。
- 易错陷阱:补完整推理时漏写"古代/当时"等时间表述会扣 1 分。
- 同类题:Q-2024朝阳一模-20-1;Q-2026通州期末-19-2。

### Q-2024朝阳期中-7

- 题目来源简记:2024 朝阳期中 第 7 题,选择题。
- 题型:三段论排序题。
- 逻辑形式:三段论(大前提+小前提+结论)。
- 规则口诀:大前提含中项与大项;小前提含中项与小项;中项必须周延一次;结论从二者推出。
- 有效式或错误式:正确排序为②大前提"北京中轴线是不可替代的文化遗产"+①小前提"北京中轴线是世界遗产委员会确认的世界遗产"+③结论"有些由世界遗产委员会确认的是不可替代的文化遗产";中项"北京中轴线"周延,推理有效,正确选项 B。
- 解题动作:① 找结论(③),确定大项;② 找包含大项的前提作大前提(②);③ 剩余为小前提(①);④ 排查中项是否周延、有无单称错位。
- 答案落点:选 B,排序为②①③;结论由两个前提关于"北京中轴线"的中项贯通推出。
- 易错陷阱:A①③④无效——中项错位;C 三个前提均为单称——中项断裂;D 结论与前提关系错位。
- 同类题:Q-2026顺义一模-19-1;Q-2026顺义一模-19-2。

### Q-2024西城一模-19-2

- 题目来源简记:2024 西城一模 第 19 题第(2)问,主观题(下定义)。
- 题型:概念定义结构题(归纳/概念/判断/推理)。
- 逻辑形式:被定义项 + 联结词 + 种差 + 邻近属。
- 规则口诀:"被定义项 = 种差 + 邻近属"。
- 有效式或错误式:① 举国体制 + ② 是 + ③ 利用国家力量动员规模性资源实现国家目标(种差) + ④ 一种任务组织方式和体制机制安排(邻近属)。
- 解题动作:① 确定被定义项;② 选种差(本质属性);③ 配邻近属(类别归属);④ 用"是"或"指"作联结词,顺序不可颠倒。
- 答案落点:按"举国体制是利用国家力量动员规模性资源实现国家目标的一种任务组织方式和体制机制安排"完整作答。
- 易错陷阱:种差与邻近属颠倒丢分;漏种差或漏邻近属丢分。
- 同类题:Q-2024西城一模-19-3;Q-2024西城一模-19-5。

### Q-2024西城一模-19-3

- 题目来源简记:2024 西城一模 第 19 题第(3)问,主观题(概念外延关系)。
- 题型:概念外延关系判定。
- 逻辑形式:相容/属种关系。
- 规则口诀:外延上一者包含另一者 → 属种(相容包含)关系。
- 有效式或错误式:举国体制包含"新型举国体制" → 属种关系(亦称包含/相容)。
- 解题动作:① 比较两个概念外延;② 判定为相容/不相容;③ 在相容下细分全同/属种(包含)/交叉。
- 答案落点:写出"举国体制与新型举国体制是属种(相容)关系,前者包含后者"卷面作答句。
- 易错陷阱:误填全同/交叉/不相容/反对均扣分。
- 同类题:Q-2024西城一模-19-2;Q-2024西城一模-19-5。

### Q-2024西城一模-19-5

- 题目来源简记:2024 西城一模 第 19 题第(5)问,主观题。
- 题型:综合推理题(实践调研 + 矛盾分析 + 推理想象 + 超前思维)。
- 逻辑形式:由实践→因果规律→矛盾分析→由过去现在推未来→超前思维的整链。
- 规则口诀:以实践为导向调研 → 把握状况因果规律 → 善用矛盾分析(内在矛盾/外在矛盾) → 运用推理与想象由过去现在推未来 → 超前思维。
- 有效式或错误式:六点框架按"调研→因果→矛盾→推理想象→超前"顺序展开;附加补点"强调实践 + 1 分,超前思维,内外矛盾"。
- 解题动作:① 立足实践调研当前状况;② 把握因果规律;③ 拆内外矛盾;④ 用推理与想象由过去/现在推未来;⑤ 用超前思维做前瞻判断。
- 答案落点:每条带"环节 + 材料事实 + 作用结论",最后落到超前思维的前瞻判断。
- 易错陷阱:只罗列概念无材料分析丢分;漏"实践"基础扣分。
- 同类题:Q-2024西城一模-19-2;Q-2024西城一模-19-3。

### Q-2025东城期末-13

- 题目来源简记:2025 东城期末 第 13 题,选择题。
- 题型:三段论谬误识别题(中项不周延+小项不当扩大+四概念)。
- 逻辑形式:三段论 + 概念 + 判断 + 周延。
- 规则口诀:中项必须周延一次;前提不周延的项,在结论中不得周延;前提为否定时不得引出未交代的肯定结论;同一推理只能有三个概念。
- 有效式或错误式:①"祥云是大国重器 + 有的大国重器是载人飞艇" → 中项"大国重器"未周延,谬误为中项不周延;③"碳纤维自行车适合山地骑行 + 山地车适合山地骑行" → 中项"适合山地骑行"未周延,两项均为属性,谬误同样为中项不周延。
- 解题动作:① 划出中项与大项小项;② 检查中项周延性;③ 检查前提与结论否定一致性;④ 检查概念是否四个错位。
- 答案落点:正确选项 B,理由是①与③均犯中项不周延的谬误。
- 易错陷阱:②"否定前提两否得结论"是错误形式,但题目要求识别谬误而非否定结构;④"石墨烯围巾有智能温控 + 智能温控能调节"=四概念错位。
- 同类题:Q-2025顺义一模-7。

### Q-2025西城二模-16-2

- 题目来源简记:2025 西城二模 第 16 题第(2)问,主观题。
- 题型:充分条件假言推理(肯定后件无效式辨析)。
- 逻辑形式:假言判断 + 充分条件;本题考察"肯定后件不能必推前件"。
- 规则口诀:充分条件假言推理"前真后必真,后真前不必真";肯定后件式无效。
- 有效式或错误式:无法据后件真确定一定有岩松鼠行动;充分条件假言判断后件真不能确定前件真。
- 解题动作:① 识别推理为充分条件假言;② 检查是否存在肯定后件式;③ 指出"后件真≠前件真";④ 把条件①(勺鸡雕鸮)与岩松鼠的无关性作为补充说明。
- 答案落点:写出"无法确定一定有岩松鼠行动;充分条件假言判断后件真不能确定前件真"卷面作答句。
- 易错陷阱:把"后件真"误推为"前件真";把无关条件①(勺鸡雕鸮)与岩松鼠强行挂钩。
- 同类题:Q-2026丰台一模-8。

### Q-2025顺义一模-7

- 题目来源简记:2025 顺义一模 第 7 题,选择题。
- 题型:三段论谬误判断纠错题(小项不当扩大+四概念+中项不周延组合)。
- 逻辑形式:三段论 + 概念 + 判断 + 周延。
- 规则口诀:前提不周延的项结论不得周延;同一推理只能有三个概念;中项必须周延一次。
- 有效式或错误式:A 选项原前提"凡共青团员都是青年 + 并非所有青年工人都是共青团员"——小项"青年工人"在结论中变全称扩大,确为小项不当扩大谬误;但题干"逻辑分析错误"指 A 选项对该谬误的"分析"本身陈述有误,即原归类正确而该选项陈述错。
- 解题动作:① 先看每个选项前提及其结论;② 划出三项,核对中项是否周延、小项是否在结论中扩大;③ 区分"谬误存在"与"谬误归类陈述本身"是否一致;④ 判断哪个选项的"陈述"错。
- 答案落点:正确选项 A;理由是 A 选项对"小项不当扩大"的描述本身存在错误。
- 易错陷阱:B"两否定前提"陈述本身正确,但本题非该选项;C"四概念"陈述正确;D"中项不周延"陈述正确,均不构成"逻辑分析错误"的指向项。
- 同类题:Q-2025东城期末-13。

### Q-2026丰台一模-18-2

- 题目来源简记:2026 丰台一模 第 18 题第(2)问,主观题。
- 题型:甲为必要条件假言推理(肯定后件式),乙为三段论(大项不当扩大)。
- 逻辑形式:甲——必要条件假言推理 · 肯定后件式;乙——三段论 · 大项在前提不周延却在结论周延 · 大项不当扩大。
- 规则口诀:"只有 P 才 Q":必要条件下肯后式有效;三段论:前提不周延的项,结论不得周延。
- 有效式或错误式:甲属必要条件假言推理的肯定后件式,前提真实,结论可成立;乙属三段论大项在前提中不周延却在结论中周延,违反三段论周延规则,大项不当扩大,结论不成立。
- 解题动作:先识别甲为必要条件假言推理的肯定后件式，并结合前提真实判定甲推理正确；再识别乙为三段论大项在前提中不周延却在结论中周延，属于大项不当扩大，判定乙推理错误。
- 答案落点:按"甲推理正确,理由是必要条件假言肯后式 + 前提真实;乙推理错误,理由是大项不当扩大,违反三段论周延规则"作答。
- 易错陷阱:甲不能写成演绎推理(应写必要条件假言推理的肯定后件式);乙在识别大项/中项/小项时,应先找结论再定大项,不能颠倒顺序。
- 同类题:Q-2024朝阳一模-20-2;Q-2024朝阳期中-7;Q-2025东城期末-13;Q-2025顺义一模-7;Q-2026朝阳期中-11;Q-2026顺义一模-19-1;Q-2026顺义一模-19-2。

### Q-2026通州期末-19-2

- 题目来源简记:2026 通州期末 第 19 题第(2)问,主观题。
- 题型:充分条件假言推理 + 必要条件假言推理(同题对照判断推理正误)。
- 逻辑形式:推理①为充分条件假言判断的肯定前件式;推理②为必要条件假言判断的肯定前件式。
- 规则口诀:充分条件:肯定前件→肯定后件,有效;必要条件:仅肯定前件不能肯定后件,无效。
- 有效式或错误式:推理①肯前式合规,有效;推理②若仅由肯定前件推出后件则结构错误,推理无效。
- 解题动作:① 识别每条推理是充分条件假言还是必要条件假言;② 套用相应有效式/错误式规则;③ 对照题干判断每条推理正误;④ 避开混淆肯前/肯后陷阱。
- 答案落点:推理①属于充分条件假言推理(肯定前件→肯定后件)结构有效;推理②属于必要条件假言推理(仅肯前件不可肯后件)结构无效。
- 易错陷阱:误识别假言推理类型扣分;肯定前件/肯定后件混淆扣分。
- 同类题:Q-2024朝阳一模-20-1;Q-2024朝阳一模-20-2。

---

## 第三部分 交叉双挂载原型(5 题)

> 主挂载:推理题型;次挂载:思维框架;两次挂载不可单挂。

### Q-2024朝阳二模-19-1

- 题目来源简记:2024 朝阳二模 第 19 题第(1)问,主观题。
- 推理挂载(主挂载)
  - 题型:类比推理 + 联言判断作辅助;本题要求填动态性 + 类比推理。
  - 逻辑形式:辩证思维动态性(填空 1) + 类比推理(填空 2)。
  - 规则口诀:动态性=用变化发展观点看问题;类比推理=由两类对象在某些属性上相同,推出在另外的属性上也相同。
  - 有效式或错误式:本题明确①动态性(替代写法限定为变化发展/矛盾运动/创新);②类比推理"无变通"——必须严格写"类比推理",不可改写。
  - 解题动作:① 在第一空写"动态性";② 在第二空写"类比推理",不变通。
  - 易错陷阱:第一空填"整体性/质量互变"丢分;第二空把"类比"改写为其他词不给分。
- 思维挂载(次挂载)
  - 题型:辩证思维 · 动态性。
  - 材料信号:中华文明"生生不息""日新""革新""不断充实"等表述呈现持续变化与革新。
  - 答题动作:用"变化发展观点看问题"理解中华优秀传统文化的革新性。
  - 易错陷阱:误填整体性、质量互变、矛盾运动等丢分。
- 同类题:Q-2024朝阳二模-19-2。

### Q-2024朝阳二模-19-2

- 题目来源简记:2024 朝阳二模 第 19 题第(2)问,主观题。
- 推理挂载(主挂载)
  - 题型:联言判断及其保真条件。
  - 逻辑形式:联言判断 = 各联言支同时成立。
  - 规则口诀:"当且仅当各联言支都真,联言判断才真;一假即假。"
  - 有效式或错误式:本题要求写出联言判断本身(2 分) + 保真条件(3 分):全真才真/一假即假。
  - 解题动作:① 把材料中的并列陈述抽为联言支;② 写明联言判断必须各支均真;③ 写明一假即假的反例边界。
  - 易错陷阱:把"联言判断"误写为"连言判断"不给分;表述为"充分/必要条件联言判断"不给分。
- 思维挂载(次挂载)
  - 题型:辩证思维 · 动态性(同题第(1)问的思维挂载延续)。
  - 答题动作:延续动态性的"变化发展观点",支持联言判断中各支共同成立的语境理解。
  - 易错陷阱:与第(1)问共用,避免把动态性写成整体性。
- 同类题:Q-2024朝阳二模-19-1。

### Q-2024朝阳期中-9

- 题目来源简记:2024 朝阳期中 第 9 题,选择题。
- 推理挂载(主挂载)
  - 题型:归纳推理 · 共变法。
  - 逻辑形式:归纳推理(因果探求方法)。
  - 规则口诀:共变法——其他条件相同,某现象随某因素的变化而共同变化,二者具有因果关联。
  - 有效式或错误式:小李实验中铃声随空气量同向变化,符合共变法,正确选项 B。
  - 解题动作:① 看材料是否存在两个变量同向/反向变化;② 排除"求异法"对实验情境的误用;③ 排除"演绎推理"误判;④ 排除"假如式想象未发生"。
  - 易错陷阱:A 误判演绎推理;C 误用求异法且夸大必然性;D 把科学实验误解为假如式想象。
- 思维挂载(次挂载)
  - 题型:思维抽象 / 思维具体。
  - 材料信号:从"空气—铃声"这一具体对照实验抽象出因果共变这一规律,再回到"声音不能在真空中传播"的整体结论。
  - 答题动作:沿"杂多现象→抽出核心因果→回到整体规律"路径理解共变法的认识价值。
  - 易错陷阱:不可把感性具体与思维具体颠倒;不可写成"实践决定认识"代替具体环节。
- 同类题:Q-2024西城一模-11;Q-2026朝阳期中-14。

### Q-2026顺义一模-19-1

- 题目来源简记:2026 顺义一模 第 19 题第(1)问,主观题。
- 推理挂载(主挂载)
  - 题型:三段论(前提真实性 + 结构正确性)。
  - 逻辑形式:三段论 + 判断 + 推理。
  - 规则口诀:演绎推理两条件——前提真实 + 结构正确。
  - 有效式或错误式:材料"未来产业由前沿技术驱动..."不能必然推出"所有...都是未来产业",因此该推理在前提真实性或结构上不能两全成立;本题要求按两条件分析判定。
  - 解题动作:① 识别推理是否为三段论;② 检查前提是否真实(由材料可否得出);③ 检查推理结构是否正确(中项是否周延、有无四概念);④ 给出"对/错 + 理由"的完整判断。
  - 易错陷阱:只判断对错而不分析理由扣分;漏前提真假/结构正确两条件之一扣分。
- 思维挂载(次挂载)
  - 题型:科学思维(对前提真实性、推理结构正确性的客观要求)。
  - 答题动作:用科学思维"如实反映对象、把握客观规律"的客观性,审视前提与结构是否符合材料事实。
  - 易错陷阱:用辩证思维或创新思维替代科学思维的客观性会丢分。
- 同类题:Q-2024朝阳期中-7;Q-2026顺义一模-19-2。

### Q-2026顺义一模-19-2

- 题目来源简记:2026 顺义一模 第 19 题第(2)问,主观题。
- 推理挂载(主挂载)
  - 题型:推理结构与科学思维三特征联结(分类列入推理范畴的题型)。
  - 逻辑形式:三段论 / 判断 / 推理(此问以"科学思维三特征"为答题骨架)。
  - 规则口诀:科学思维三特征——客观性、预见性、可检验性。
  - 有效式或错误式:客观性=从老人真实需求出发立足实际;预见性=追踪人口老龄化趋势预测市场潜力;可检验性=反复测试多轮迭代。
  - 解题动作:① 把材料事实拆为"需求出发 / 趋势预测 / 测试迭代"三块;② 分别对应客观性、预见性、可检验性;③ 每条带"特征 + 材料事实 + 作用结论"。
  - 易错陷阱:只列特征无材料分析丢分;混淆三特征扣分;漏特征扣分。
- 思维挂载(次挂载)
  - 题型:科学思维(总挂载,与推理挂载共采分点)。
  - 材料信号:从老龄化人口需求出发的产品研发、对老龄化趋势的市场判断、对产品的反复测试与迭代。
  - 答题动作:把客观性、预见性、可检验性逐条对应到材料事实,落到"科学思维要求 + 材料动作 + 价值结果"作答。
  - 易错陷阱:把三特征写成科学思维总称丢分;混淆客观性与可检验性的指向丢分。
- 同类题:Q-2024朝阳期中-7;Q-2026顺义一模-19-1。

---

## 输入边界备注

- 本原型仅由 29 行冻结输入组成,不含 hold 行(45 行)与 L0 行(288 行);hold 行与 L0 行不进入正文。
- 任何答案、归类、交叉双挂载、来源定位均与冻结输入保持一致;Q-2026丰台一模-18-2 的答题动作严格沿用 Phase07 补丁冻结的"先识别甲为必要条件假言推理的肯定后件式...再识别乙为三段论大项在前提中不周延却在结论中周延..."表述。
- 每条同类题列表只引用 question_id,以避免触动其他题目的答案锁(例如 Q-2024西城一模-11、Q-2025海淀二模-12、Q-2025海淀二模-13、Q-2026顺义一模-3 等仅作为引用 ID 出现,不写其答案/类型/挂载结论)。
- 本原型为 review only,不能作为学生稿、Word/PDF 或最终 PASS;后续审核如需进入下一阶段,必须由相应 gate 单独授权。

