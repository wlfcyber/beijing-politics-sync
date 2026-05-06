# Phase12 Student-Clean Candidate GPT-5.5 Pro Digest

Captured: 2026-05-05 22:55 CST

Source raw: `08_review/gpt_phase_advice/phase_12_student_clean_candidate_gpt55_raw.md`

Verdict: `PATCH_REQUIRED_NO_WORD`

## Overall Judgment

GPT-5.5 Pro judged the 77-entry student-clean candidate close to Word preparation but not yet clean-pass. The quantity and general teachability were accepted, but Word/PDF/final remained blocked because of several local consistency and index issues.

## Must Fix

1. `2024 西城一模第11题`
   - GPT found an internal conflict: correct item was `B`, but the displayed B option and the explanation did not agree.
   - Local source lock overrides any conditional model suggestion: the official lock is `B=①③`, with options `A=①② / B=①③ / C=②④ / D=③④`.

2. `2026 丰台一模第18题第(2)问`
   - As a subjective reasoning entry it lacked the teaching trio: material signal, actual prompt, and why the student should identify the reasoning forms.
   - Must add the signal chain for 甲 as necessary conditional reasoning and 乙 as syllogism with major-term illicit process.

3. `2025 东城期末第13题`
   - Body was basically correct, but the reasoning index mislabeled the item as involving small-term illicit process.
   - Correct mount: `①③中项不周延；②大项不当扩大；④四概念`.

4. `2024 朝阳二模第19题第(2)问`
   - Thinking index falsely mounted a formal-logic conjunction judgment item as dialectical thinking / analysis and synthesis.
   - It should stay in the reasoning index under 联言判断与联言推理, not in the thinking-method index.

5. `2025 海淀二模第20题`
   - Same-type index incorrectly included `2024 朝阳二模第19题第(2)问`.
   - Keep `2024 朝阳二模第19题第(1)问`; remove `19(2)`.

## Should Fix

1. `2026 丰台一模第8题`
   - Strengthen ③ with the 限制换位 chain and move the item from auxiliary indexing to sufficient-conditional choice trap.

2. `2026 东城期末第7题`
   - Add formal propositions and substitution logic for the truth-value reasoning.

3. Global index labels
   - Replace review-flavored labels with student-facing labels:
     - `正文正例` -> `可正用例`
     - `辅助挂载` -> `相关检索`
     - `选择题陷阱` -> `易混选择题`
     - `边界陷阱` -> `边界提醒`

## Boundary

No Word, no PDF, no final PASS, no TASK_COMPLETE, no 终稿/最终稿/宝典成品 until the patch is applied, rechecked, and Governor/Confucius gates pass.
