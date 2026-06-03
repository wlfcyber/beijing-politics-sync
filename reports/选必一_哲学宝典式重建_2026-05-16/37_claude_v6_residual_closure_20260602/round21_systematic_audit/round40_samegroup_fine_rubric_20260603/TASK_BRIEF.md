# TASK BRIEF

## Objective

User found that same-question groups are still too coarse. The exemplar is `2025延庆一模Q20(2)`: the current student DOCX records four 2-point angles but omits the formal rubric's replacement note `国家利益、国际关系、多边主义等角度可替代，不重复给分`. Re-audit and repair all comparable same-question groups so each group preserves formal rubric fine structure, not just broad angle labels.

## Current Base

- Input DOCX: `/Users/wanglifei/Desktop/选必一6.1终极版_同题组全量细则复核最终修正版_核心答题点红色强化_学生版_带水印_20260603.docx`
- Previous run: `round35_samegroup_rubric_relock`
- New output should keep the student-facing style, watermark, and red/bold `核心答题点：`.

## Hard Rules

- Same-question group acceptance now requires: total score, each scoring angle/layer, per-angle score, optional/replacement expressions, upper limits, and explicit non-scoring/deduction boundaries when present in formal rubric/marking notes.
- Do not treat a broad "OK" verdict as enough if fine scoring text is missing.
- Do not expose backend terms in student DOCX: `细则`, `评分`, `评标`, `采分`, `证据`, source paths, audit terms, etc.
- If a formal rubric lacks fine details, use the best formal level available and mark the backend audit, but keep the student-facing text clean.

## First Exemplar

`2025延庆一模Q20(2)` must include:

- 8分，四个角度各2分.
- 时代主题2分.
- 经济全球化方向2分.
- 多极化2分.
- 人类命运共同体2分.
- 国家利益、国际关系、多边主义等角度可替代，不重复给分.

## Completion Gate

- Every unique same-question key in the current DOCX has a fine-rubric audit verdict.
- All confirmed omissions are patched in every duplicate same-question block.
- Final DOCX passes structural extraction: no empty groups, no inconsistent groups, no backend terms, core headings red/bold.
- Final DOCX renders to page images and key pages are visually inspected.
