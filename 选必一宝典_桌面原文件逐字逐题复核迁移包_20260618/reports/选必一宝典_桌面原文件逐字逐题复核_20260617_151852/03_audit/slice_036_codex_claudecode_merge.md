# Slice 036 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T04:48:53+08:00
- scope: doc_order 176-180 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc. doc180 was rerun after a prompt excerpt omitted rubric source line 6; the rerun finding is the accepted finding.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 176 | Q0176 | 2026朝阳期中Q17 | PASS + PENDING_BOOK_LEVEL | First self-reliance/opening relationship supports two-market/resources branch; UQ0003 remains pending. Soft note only: avoid “核心利益” drift. |
| 177 | Q0177 | 2024西城一模Q19(6) | NEEDS_FIX + PENDING_BOOK_LEVEL | Material trigger is written from the challenge/comprehensive-national-strength branch, while this row is the opportunity/two-market branch; UQ0026 remains pending. |
| 178 | Q0178 | 2024朝阳一模Q21 | PASS + PENDING_BOOK_LEVEL | PPTX rubric line 1228 supports super-large-market/two-market branch; economic situation and political dimension remain visible; UQ0005 remains pending. |
| 179 | Q0179 | 2025西城一模Q18 | NEEDS_FIX + PENDING_BOOK_LEVEL | Two-market market-layer is source-backed, but trigger mislabels answer words as the question and lacks cross-module boundary for a 必修2 《经济与社会》 prompt; UQ0038 remains pending. |
| 180 | Q0180 | 2025海淀期中Q16(2) | PASS + PENDING_BOOK_LEVEL | Rerun with complete rubric line 6 confirms two-resources/two-markets branch; UQ0030 remains pending. |

## Source Evidence

- Q0176: `SRC_EXAM_2026_CHAOYANG_QIZHONG_Q17.txt`; `SRC_RUBRIC_2026_CHAOYANG_QIZHONG_Q17.txt`; exam lines 148-170,243-245; rubric lines 14-30; Claude finding `04_claudecode/slice_036_doc176_claudecode_findings.md`.
- Q0177: `SRC_EXAM_2024_XICHENG_YIMO_Q19.txt`; `SRC_RUBRIC_2024_XICHENG_YIMO_Q19.txt`; exam lines 197-204; rubric lines 85-101; Claude finding `04_claudecode/slice_036_doc177_claudecode_findings.md`.
- Q0178: `SRC_EXAM_2024_CHAOYANG_YIMO_Q21.txt`; `SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_DOCX.txt`; `SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_PPTX.txt`; exam lines 372-376; DOCX rubric lines 88-99; PPTX rubric lines 1224-1228,1260-1317; Claude finding `04_claudecode/slice_036_doc178_claudecode_findings.md`.
- Q0179: `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt`; `SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt`; exam lines 221-234,342-345; rubric lines 65-78; Claude finding `04_claudecode/slice_036_doc179_claudecode_findings.md`.
- Q0180: `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q16_2.txt`; `SRC_RUBRIC_2025_HAIDIAN_QIZHONG_Q16_2.txt`; exam file lines 7-19/source lines 180-191; rubric file lines 7-15/source lines 1-8; Claude finding `04_claudecode/slice_036_doc180_claudecode_findings.md`.

## Required Repairs / Holds

- Q0177: repair block 2084 material trigger so it points to opportunity/two-market resources, not the challenge/comprehensive-national-strength branch.
- Q0179: repair blocks 2107/2109 so answer/material words are not mislabeled as the question; add a cross-module boundary note for the 《经济与社会》 prompt and its market-layer overlap with 选必一.
- Q0176/Q0178/Q0180: no row-level hard repair; keep soft notes for later edit pass where useful.
- No normalized question group is accepted in this slice: UQ0003, UQ0026, UQ0005, UQ0038, and UQ0030 remain PENDING_BOOK_LEVEL.

## Boundary

This merge accepts only doc_order 176-180 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 181; 381 entries remain pending.
