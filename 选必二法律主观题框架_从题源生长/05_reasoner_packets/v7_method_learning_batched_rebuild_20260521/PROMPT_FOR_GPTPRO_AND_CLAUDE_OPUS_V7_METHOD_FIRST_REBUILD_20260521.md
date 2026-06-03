# GPTPro / Claude Opus V7 Task: Learn The User's Framework Method First, Then Rebuild Xuanbier Law

You are participating in the user's 选必二《法律与生活》主观题框架重建工程.

## Absolute order

Do not immediately write a new law framework.

Step 1: Learn the user's previous strong framework style from:
- `prior_framework_learning/PRIOR_FRAMEWORK_DEEP_DNA_20260520.md`
- `prior_framework_learning/LEGAL_REWRITE_SPEC_AFTER_PRIOR_STUDY_20260520.md`
- `rendered_prior_samples/`

Output first: `METHOD_LEARNING_NOTES`.
You must explain what makes those frameworks usable for a smart but zero-baseline Gaokao student.

Step 2: Read the current law candidate V6.9 in `current_law_candidate/`.
Output: `WHY_V6_9_STILL_NOT_ENOUGH`.
Be harsh. The user's complaint is that the current framework still does not let a student reliably answer full marks.

Step 3: Process legal evidence by batches, in this order:
- `batches/BATCH_01_HIGH_FREQ_CORE_JUDGMENT.md`
- `batches/BATCH_02_PROCEDURE_TABLE.md`
- `batches/BATCH_03_INNOVATION_AI_VALUE.md`
- `batches/BATCH_04_NON_CORE_OPEN_CONTAINER.md`

For each batch output:
- `batch_mechanisms`: what scoring mechanisms really recur.
- `student_start_moves`: what the student should do first when seeing this batch type.
- `material_to_legal_translation`: material signal -> legal language -> scoring sentence.
- `full_score_sentence_rules`: sentence formulas, not empty slogans.
- `bad_framework_nodes_to_delete_or_demote`: anything pretty but not useful.
- `evidence_ids`: question_id + rubric_atom_id, mandatory.

Step 4: Only after all batches, create a V7 candidate framework.

Please write your answer in Chinese. Keep all evidence ids unchanged.

## Required V7 output

1. `METHOD_LEARNING_NOTES`
2. `WHY_V6_9_STILL_NOT_ENOUGH`
3. `BATCH_01_FINDINGS`
4. `BATCH_02_FINDINGS`
5. `BATCH_03_FINDINGS`
6. `BATCH_04_FINDINGS`
7. `V7_FRAMEWORK_PROPOSAL`
8. `V7_STUDENT_FIRST_10_PAGES_PLAN`
9. `QUESTION_BY_QUESTION_STRESS_TEST_PLAN`
10. `WHAT_YOU_NEED_FROM_CODEX_NEXT`

## Framework constraints

- The framework must keep `主干高频层 + 开放容器层`.
- Every node must be traceable to question_id and rubric_atom_id.
- Do not use textbook chapter names as the front-stage framework.
- Do not write a law-exam style framework.
- Do not write broad 必修三 rule-of-law slogans.
- A smart zero-baseline high-school student must know: first sentence, material translation, legal rule, scoring endpoint.
- If a node cannot help the student write a sentence, delete it or demote it.

## Output verdict

End with one of:
- PASS_TO_REWRITE: enough to let Codex write V7.
- CONDITIONAL_PASS_TO_REWRITE: Codex can write V7 only if listed fixes are applied.
- FAIL_RETHINK: the batch evidence still does not support a useful framework.
