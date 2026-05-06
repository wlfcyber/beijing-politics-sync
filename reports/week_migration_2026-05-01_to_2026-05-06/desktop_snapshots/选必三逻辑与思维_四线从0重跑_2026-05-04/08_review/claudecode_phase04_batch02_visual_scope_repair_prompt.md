You are ClaudeCode Lane B in Feige Politics Garden four-lane workflow.

Working directory:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

You are not alone in the codebase. Codex A is editing control files in parallel. Do not revert or overwrite unrelated changes. You own only the Lane B Batch02 verification outputs listed below.

Highest rules:

1. This is 选择性必修三《逻辑与思维》 from-zero rerun. Old artifacts are locator-only unless reopened as raw source in this run.
2. Do not write student-facing prose, student稿, Claude/Opus rewrite, Word/PDF, or final PASS.
3. You must use available tools for PDF/PPTX/DOCX/images/renders/XML; do not stop just because a normal text layer is thin.
4. You must independently verify. Do not trust Codex A conclusions unless you can point to the source/renders/XML/supplemental source.
5. Keep every row conservative: if no answer source, no fusion; never infer an answer from logic.

Read first:

- `08_review/gpt_phase_advice/phase_04_batch01_gpt55_digest.md`
- `08_review/gpt_phase_advice/phase_04_batch01_gpt55_raw.md`
- `05_coverage/phase04_control_base_status_after_laneB_batch01.csv`
- `05_coverage/phase04_blocked_type_split.csv`
- `05_coverage/phase04_2026_chaoyang_q12_formal_patch.csv`
- `05_coverage/phase04_batch02_codex_visual_scope_repair_addendum.csv`
- `02_extraction/supplemental_answer_sources/phase04_batch02_supplemental_source_ledger.csv`
- `05_coverage/phase04_2026_fengtai_yimo_visual_suite_scan.csv`
- `05_coverage/phase04_2026_fengtai_yimo_selected3_candidates.md`
- `05_coverage/phase04_2025_haidian_ermo_Q12_Q13_answer_search.md`
- `05_coverage/phase04_2025_haidian_ermo_Q12_Q13_status.csv`
- `05_coverage/phase04_2024_xicheng_yimo_Q11_B_recheck.csv`
- `05_coverage/phase04_2025_haidian_qimo_Q2_scope_decision.md`
- `06_conflicts/phase04_batch02_codex_visual_scope_repair.md`

Source/renders you will likely need:

- `02_extraction/priority_queue_sources/renders/042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf/`
- `02_extraction/priority_queue_sources/renders/042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf_contact.jpg`
- `02_extraction/supplemental_answer_sources/2026北京丰台高三一模政治试题有答案_北京高考在线.txt`
- `02_extraction/priority_queue_sources/renders/008_Desktop_2025模拟题_2025各区二模_2025海淀二模_试卷_试卷.pdf/page_04.png`
- `02_extraction/supplemental_answer_sources/2025北京海淀高三二模政治试题及答案.txt`
- `02_extraction/priority_queue_sources/text/003_Desktop_2026模拟题_2026各区期末和期中_2026朝阳期中_试卷_试卷.pdf.txt`
- `/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx`
- `02_extraction/priority_queue_sources/text/025_Desktop_2024模拟题_西城一模_细则_细则.docx.txt`
- `02_extraction/priority_queue_sources/text/026_Desktop_2024模拟题_西城一模_细则_补充材料_2024.4高三统一测试思想政治答案.docx.txt`

Batch02 tasks:

## A. Formalize 2026朝阳期中 Q12

Independently verify Q12 full stem/options, answer B, and 推理/逻辑规则 classification from source `003`.

Also re-evaluate Q14/Q15:

- Q14 answer B, 不完全归纳/或然性.
- Q15 answer D, 联言判断否定.

For Q12/Q14/Q15, decide whether Lane B can set `can_enter_fusion=yes`. If yes, explain why; if no, list exact blocker.

## B. 2026丰台一模 full visual scan

Independently scan rendered 042 pages and supplemental answer source.

Verify whether Codex A's newly recovered selected-compulsory-three candidates are correct:

- Q4: 思维 / 综合思维 / answer A.
- Q7: 思维 / 发散聚合 + 超前思维 / answer B.
- Q8: 推理 / 充分条件假言推理 / answer C.
- Q9: 推理 / 概念外延关系 + 联言判断 / answer D.
- Q18(2): already L4, but ensure no conflict.

Also confirm whether any other Q1-Q21 row should be selected-compulsory-three relevant. If none, say so and identify boundaries.

## C. 2025海淀二模 Q12/Q13

Independently verify:

- Q12 full options from render page_04, answer D from supplemental answer source, classification 思维/超前思维.
- Q13 full options from render page_04, answer C from supplemental answer source, classification 推理/三段论 and logic rules.

Do not infer answers from logic. If you cannot verify the supplemental answer source, keep blocked.

## D. 2024西城一模 Q11

Independently recover the four Word textbox options from the DOCX or render it.

Verify answer B from 025/026 and explain answer B means ①④.

If independent recovery succeeds, set can_enter_fusion yes; if not, keep pending.

## E. 2025海淀期末 Q2 scope

Review GPT/Codex decision and independently verify from source:

- answer C = ②③.
- ② is 场景迁移/联想思维.
- ③ is 辩证思维整体性.
- ① is philosophy lure, not answer.

Decide whether it can be 思维 with boundary note and whether can_enter_fusion yes.

## Required outputs

Write these files:

- `claudecode_lane/phase04_batch02_laneB_results.csv`
- `claudecode_lane/phase04_batch02_fengtai_visual_recheck.csv`
- `claudecode_lane/phase04_batch02_fengtai_visual_recheck.md`
- `claudecode_lane/phase04_batch02_haidian_q12q13_recheck.csv`
- `claudecode_lane/phase04_batch02_haidian_q12q13_recheck.md`
- `claudecode_lane/phase04_batch02_xicheng_q11_recheck.csv`
- `claudecode_lane/phase04_batch02_xicheng_q11_recheck.md`
- `claudecode_lane/phase04_batch02_scope_and_upgrade_decisions.csv`
- `04_suite_reports/claudecode_suite_reports/phase04_batch02_visual_scope_repair_report.md`
- update `claudecode_lane/progress.md`

CSV schema for `phase04_batch02_laneB_results.csv`:

`target_id,suite,qno,section_scope,laneB_result,evidence_level,visual_status,answer_status,rubric_status,node,logical_or_method_form,rule_slogan,trap_or_boundary,can_enter_fusion,can_enter_student_draft,blocker_reason,source_evidence,notes`

Remember:

- `can_enter_student_draft` must always be `no`.
- `can_enter_fusion=yes` is allowed only for evidence fusion, not student稿.
- If a row is based on supplemental answer source, say exactly which source file and whether you verified it.
