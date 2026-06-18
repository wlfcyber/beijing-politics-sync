# Slice 033 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T03:29:40+08:00
- scope: doc_order 161-165 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 161 | Q0161 | 2026海淀一模Q20 | PASS + PENDING_BOOK_LEVEL | Source/rubric support the opening branch; same-theme notes preserve the standards/innovation and governance/rules branches. UQ0072/UQ0082/UQ0121/UQ0122 remain book-level pending. |
| 162 | Q0162 | 2026东城二模Q20(3) | PASS + PENDING_BOOK_LEVEL | Source and rubric preserve the 3+3+1 frame; this row validly focuses on the 投资中国/制度型开放 layer. UQ0046 remains pending. |
| 163 | Q0163 | 2026丰台二模Q20 | PASS source-limited + LOW_EVIDENCE + PENDING_BOOK_LEVEL | Teacher-version answer supports high-level opening/free-trade-platform direction, but no matching formal Q20 rubric is located and `制度型开放` is only material-inferred, not a teacher-answer scoring term. UQ0048 remains pending. |
| 164 | Q0164 | 2026门头沟一模Q21 | PASS + PENDING_BOOK_LEVEL | Comprehensive question is correctly limited to material-three 国政经/互利共赢 branch; materials one/two are not expanded into 选必一. UQ0059 remains pending. |
| 165 | Q0165 | 2026顺义二模Q20 | PASS + PENDING_BOOK_LEVEL | Source/rubric support the international-economic/互利共赢 branch while the same-group notes preserve the political branch. UQ0013 remains pending. |

## Source Evidence

- Q0161: `SRC_EXAM_2026_HAIDIAN_YIMO_Q20.txt:339-355`; `SRC_RUBRIC_2026_HAIDIAN_YIMO_Q20.txt:85-89`; Claude finding `04_claudecode/slice_033_doc161_claudecode_findings.md`.
- Q0162: `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt:119-127,151-154`; `SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt:16-39`; Claude finding `04_claudecode/slice_033_doc162_claudecode_findings.md`.
- Q0163: `SRC_EXAM_2026_FENGTAI_ERMO_Q20.txt:343-362,487-492`; `SRC_RUBRIC_2026_FENGTAI_ERMO_Q20_PPTX_MISMATCH.txt` as mismatch/absence evidence; Claude finding `04_claudecode/slice_033_doc163_claudecode_findings.md`.
- Q0164: `SRC_EXAM_2026_MENTOUGOU_YIMO_Q21.txt:357-371`; `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q21.txt:133-149`; Claude finding `04_claudecode/slice_033_doc164_claudecode_findings.md`.
- Q0165: `SRC_EXAM_2026_SHUNYI_ERMO_Q20.txt:350-362`; `SRC_RUBRIC_2026_SHUNYI_ERMO_Q20.txt:71-88`; Claude finding `04_claudecode/slice_033_doc165_claudecode_findings.md`.

## Required Repairs / Holds

- Q0163: keep `制度型开放` source-limited/material-inferred and keep formal `细则位置` LOW_EVIDENCE unless a matching official Q20 rubric is later found.
- Q0161, Q0162, Q0164, Q0165: no row-level repair; all retain book-level group holds.
- No normalized question group is accepted in this slice.

## Boundary

This merge accepts only doc_order 161-165 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 166; 396 entries remain pending.
