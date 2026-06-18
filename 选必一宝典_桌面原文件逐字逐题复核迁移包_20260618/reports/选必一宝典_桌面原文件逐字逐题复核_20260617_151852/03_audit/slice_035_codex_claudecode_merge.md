# Slice 035 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T04:14:53+08:00
- scope: doc_order 171-175 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 171 | Q0171 | 2026门头沟一模Q20 | PASS + PENDING_BOOK_LEVEL | Two-market branch restores China+world frame and preserves 7-point group notes. UQ0015 remains pending. |
| 172 | Q0172 | 2026海淀一模Q20 | PASS + PENDING_BOOK_LEVEL | Two-market branch is rubric-backed while standards/governance branches remain in same-theme notes. 海淀Q20 groups remain pending. |
| 173 | Q0173 | 2025昌平二模Q21 | PASS + PENDING_BOOK_LEVEL | Two-market branch is source-backed; `资本/技术/人才` and cap wording are soft precision notes, not hard errors. Raw-source family remains pending. |
| 174 | Q0174 | 2026石景山二模Q18 | PASS + PENDING_BOOK_LEVEL | Two-market/economic-transition meaning branch is source-backed and basis/meaning split is preserved. UQ0023 remains pending. |
| 175 | Q0175 | 2024东城一模Q20 | PASS + PENDING_BOOK_LEVEL | Rubric point 4 supports market-access/two-market branch and the broad `经济的相关知识` boundary is preserved. UQ0060 remains pending. |

## Source Evidence

- Q0171: `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`; `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`; Claude finding `04_claudecode/slice_035_doc171_claudecode_findings.md`.
- Q0172: `SRC_EXAM_2026_HAIDIAN_YIMO_Q20.txt:339-355`; `SRC_RUBRIC_2026_HAIDIAN_YIMO_Q20.txt:85-89`; Claude finding `04_claudecode/slice_035_doc172_claudecode_findings.md`.
- Q0173: `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:255-266,368-374`; `SRC_RUBRIC_2025_CHANGPING_ERMO_Q21.txt:125-142`; Claude finding `04_claudecode/slice_035_doc173_claudecode_findings.md`.
- Q0174: `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:103-108,125-126`; `SRC_RUBRIC_2026_SHIJINGSHAN_ERMO_Q18.txt:49-50`; Claude finding `04_claudecode/slice_035_doc174_claudecode_findings.md`.
- Q0175: `SRC_EXAM_2024_DONGCHENG_YIMO_Q20.txt:336-346`; `SRC_RUBRIC_2024_DONGCHENG_YIMO_Q20.txt:360-366`; Claude finding `04_claudecode/slice_035_doc175_claudecode_findings.md`.

## Required Repairs / Holds

- No row-level hard repair in this slice.
- Q0173, Q0174, Q0175 carry soft precision notes only; keep for later edit pass if the user asks to repair the DOCX.
- No normalized question group is accepted in this slice.

## Boundary

This merge accepts only doc_order 171-175 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 176; 386 entries remain pending.
