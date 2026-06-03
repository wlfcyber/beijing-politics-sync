# V6.7 Final Student Usability Review Packet

## Purpose

This packet is for GPTPro and Claude Opus final review of the current student-facing candidate:

- `选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.md`
- `选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.docx`

The review target is not "is the evidence safer than before". The target is:

> Can a smart but zero-baseline Grade 12 student read this document and then start unfamiliar 选必二《法律与生活》 subjective questions, transform material into legal language, and write close-to-rubric full-score answers?

## Current Project State

- Corpus baseline: 65 subjective-law questions.
- Evidence status: 61 formal / 4 reference-only / 0 missing.
- Student-training boundary: 27 strict core full-score training questions + 38 non-core guard/index/reference/boundary rows.
- V6.7 must not be treated as "65 questions all have stable core full-score templates".
- V6.7 is the current best student-use candidate after GPTPro/Claude V6.2 review, V6.4 regression, V6.5 causation patch, and V6.7 student-clean polish.

## Included Files

- `PROMPT_FOR_GPTPRO_AND_CLAUDE_V6_7_FINAL_STUDENT_REVIEW_20260521.md`: internal review prompt.
- `VISIBLE_PROMPT_ASCII_FOR_WEB_UPLOAD_20260521.txt`: short visible prompt to paste after uploading this packet if web UI risks garbling Chinese.
- `选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.md`: main review target.
- `选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.docx`: DOCX candidate.
- `v6_2_gptpro_claude_naked_review_comparison_20260521.md`: prior GPTPro/Claude comparison that drove V6.4.
- `V6_4_REGRESSION_VERDICT_20260521.md`: targeted regression result before V6.5.
- `grading_report_CEGH_v6_4_regression_20260521.md`: detailed C/E/G/H grading.
- `V6_5_MINI_REGRESSION_VERDICT_20260521.md`: one-question causation mini-regression after V6.5.
- `DOCX_QA_V6_7_STUDENT_20260521.md`: DOCX QA status and render limitation.
- `选必二法律主观题满分训练宝典_v6_6_教师证据说明_20260521.md`: teacher/evidence caveat.

## Non-Negotiable Review Rule

If the document is readable but still cannot make a student write answers, return `FAIL` or `CONDITIONAL_PASS`, not `PASS`.
