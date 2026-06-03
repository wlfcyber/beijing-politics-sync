# READ ME FIRST

This packet is for reviewing the v8 student-usable rebuild of the Beijing Gaokao Politics elective book 2 Legal Life subjective-question framework.

## Current Locked Baseline

- Corpus: 53 boundary-patched subjective law questions.
- Atoms: 535 material atoms, 53 ask atoms, 319 rubric atoms.
- Status: 37 PASS, 11 PASS_RECOVERED, 5 OPEN_OR_REFERENCE.
- OPEN_OR_REFERENCE questions may be used only as reference runs. They must not support core framework nodes.
- Pending cases must not enter the closed body:
  - CC0094_2025_东城_期末_19_3
  - CC0259_2026_丰台_期中_19
  - CC0118_2025_丰台_期末_18_2
- Removed case must not return:
  - CC0250_2026_丰台_一模_19

## Important Guard

Do not expand the corpus to 70 candidates. Do not redo evidence extraction. Do not turn this into a law-school framework or a broad rule-of-law slogan framework. The task is to judge whether v8 is usable by a smart high-school student in the exam room.

## File Order

1. `00_PROMPT_FOR_GPT_REVIEW.md`: the task prompt.
2. `01_student_exam_framework_v8.md`: the one-page student action framework.
3. `02_full_baodian_v8.md` / `.docx`: the full handbook.
4. `03_acceptance_report_v8.md`: Codex's current verdict.
5. `04_student_usability_test_v8.md`: simulated student test.
6. `05_gold_standard_selection.md`: why the 8 gold-standard questions were chosen.
7. `06_gold_standard_question_runs.md`: detailed runs of the 8 gold-standard questions.
8. `07_full_score_sentence_bank_v8.md` / `.csv`: sentence bank.
9. `08_question_by_question_runs_v8.md` / `.csv`: 53-question runs.
10. `09_teacher_evidence_framework_v8.md` / `.csv`: teacher evidence framework.
11. `10_v7_failure_diagnosis.md`: why v7.1 failed.

## Current Codex Verdict

v8 is `CONDITIONAL_PASS`, not final full PASS. It has a usable student framework, 8 gold-standard runs, 23 sentence templates, and 53 question runs. Remaining risk: the 45 non-gold question runs still need classroom-style human polish, and some ask-missing rows need source backfill.
