# Task Brief

- run_id: `22_accuracy_completeness_clean_pass_20260604`
- input_docx: `/Users/wanglifei/Desktop/选必三claude美化版_最终学生版_20260604.docx`
- goal: 逐条核对当前文档的准确性和全面性，并删除前言与所有 `【方法小引】`。

## User Request

逐条核对这个文档的准确性和全面性。删掉前言你乱写的和方法小引这些画蛇添足的。

## Scope

- Remove the entire preface block while preserving cover and table of contents unless later audit shows the TOC is misleading.
- Remove all paragraphs beginning with `【方法小引】`.
- Re-extract every teaching entry after cleanup.
- Audit each entry for core-field completeness, method/title alignment, hard-exclusion residue, student-facing cleanliness, same-question note coverage, and obvious accuracy risks.
- Produce a revised DOCX and render it before delivery.
