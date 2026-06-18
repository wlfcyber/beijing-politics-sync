# Slice 034 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T03:56:19+08:00
- scope: doc_order 166-170 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 166 | Q0166 | 2026门头沟一模Q20 | NEEDS_FIX + PENDING_BOOK_LEVEL | Material trigger narrows a China+world prompt to domestic-only meaning; other fields are source-backed. UQ0015 remains pending. |
| 167 | Q0167 | 2024朝阳期中Q20(3) | PASS + PENDING_BOOK_LEVEL | Short-review structure and the 打造新平台/two-market branch are source-backed. UQ0062 remains pending. |
| 168 | Q0168 | 2026朝阳一模Q20 | PASS + PENDING_BOOK_LEVEL | Development-potential branch supports two markets/two resources and factor flow. UQ0002 remains pending. |
| 169 | Q0169 | 2026房山一模Q19 | PASS + PENDING_BOOK_LEVEL | Formal rubric supports the two-market/two-resource China-solution layer and four-layer frame. UQ0068 remains pending. |
| 170 | Q0170 | 2024海淀一模Q18(1) | PASS + PENDING_BOOK_LEVEL | Visa-facilitation layers are source-backed; trigger wording has only soft precision notes. UQ0034/UQ0088 remain pending. |

## Source Evidence

- Q0166: `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`; `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`; Claude finding `04_claudecode/slice_034_doc166_claudecode_findings.md`.
- Q0167: `SRC_EXAM_2024_CHAOYANG_QIZHONG_Q20_3.txt:414-447`; `SRC_RUBRIC_2024_CHAOYANG_QIZHONG_Q20_3.txt:218-254`; Claude finding `04_claudecode/slice_034_doc167_claudecode_findings.md`.
- Q0168: `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt`; `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99`; Claude finding `04_claudecode/slice_034_doc168_claudecode_findings.md`.
- Q0169: `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342`; `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:58-64`; Claude finding `04_claudecode/slice_034_doc169_claudecode_findings.md`.
- Q0170: `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt:251-262`; `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt:55-66`; Claude finding `04_claudecode/slice_034_doc170_claudecode_findings.md`.

## Required Repairs / Holds

- Q0166: repair block 1965. It must not say the question points only to domestic meaning; it needs the China+world two-sided prompt and world-side opening/market-access triggers.
- Q0167, Q0168, Q0169, Q0170: no row-level hard repair; keep book-level group holds.
- No normalized question group is accepted in this slice.

## Boundary

This merge accepts only doc_order 166-170 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 171; 391 entries remain pending.
