# Slice 025 Codex + ClaudeCode Merge

- timestamp: 2026-06-17T23:56:33+08:00
- scope: doc_order 121-125 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 121 | Q0121 | 2026丰台二模Q20 | PASS + LOW_EVIDENCE on formal rubric + PENDING_BOOK_LEVEL | Teacher-version answer explicitly supports the five-direction globalization point and the row correctly warns not to use it as fixed scoring. Matching formal Q20 rubric is still absent, so `细则位置` stays LOW_EVIDENCE. UQ0048 remains pending. |
| 122 | Q0122 | 2026房山二模Q20 | NEEDS_FIX + LOW_EVIDENCE on raw material + PENDING_BOOK_LEVEL | Formal rubric supports six 1-point directions plus material 2分. The book internally conflicts on `智慧` vs `中国智慧`, and the source package lacks the original prompt/material needed to settle the wording. UQ0050 remains pending. |
| 123 | Q0123 | 2026通州一模Q19 | NEEDS_FIX + PENDING_BOOK_LEVEL | Formal rubric supports the economic-globalization branch, but block 1473 omits `外交政策（多边主义）`, and block 1472 misses the cap rules: 堆砌≤3, 有知识有分析不体现作用≤6, 材料部分体现作用可7-8. UQ0052 remains pending. |
| 124 | Q0124 | 2025朝阳二模Q21 | PASS + PENDING_BOOK_LEVEL | Formal exam/rubric support the world-development 2分 branch and the 3+3+2 周边工作 structure. Material trigger can be more material-anchored but is not source-conflicting. UQ0045 remains pending. |
| 125 | Q0125 | 2025昌平二模Q21 | NEEDS_FIX | Formal rubric supports the `更加开放、包容的全球经济格局` branch, but blocks 1490/1492 add unsupported `外部保护主义抬头`; block 1493 adds unsupported `共享中国市场和发展机遇` and omits `提升中国在全球经济治理中的话语权和影响力`; blocks 1495-1498 omit the cross-material `见点给分` flexibility. UQ0100 is singleton. |

## Source Evidence

- Q0121: `SRC_EXAM_2026_FENGTAI_ERMO_Q20.txt:343-362,487-492`; `SRC_RUBRIC_2026_FENGTAI_ERMO_Q20_PPTX_MISMATCH.txt:1-6,64-75`; Claude finding `04_claudecode/slice_025_doc121_claudecode_findings.md`.
- Q0122: `SRC_EXAM_2026_FANGSHAN_ERMO_Q20.txt:106-118`; `SRC_RUBRIC_2026_FANGSHAN_ERMO_Q20.txt:134-146`; Claude finding `04_claudecode/slice_025_doc122_claudecode_findings.md`.
- Q0123: `SRC_EXAM_2026_TONGZHOU_YIMO_Q19.txt:3-10`; `SRC_RUBRIC_2026_TONGZHOU_YIMO_Q19.txt:160-192`; Claude finding `04_claudecode/slice_025_doc123_claudecode_findings.md`.
- Q0124: `SRC_EXAM_2025_CHAOYANG_ERMO_Q21.txt:215-228`; `SRC_RUBRIC_2025_CHAOYANG_ERMO_Q21.txt:283-314`; Claude finding `04_claudecode/slice_025_doc124_claudecode_findings.md`.
- Q0125: `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:255-266,368-374`; `SRC_RUBRIC_2025_CHANGPING_ERMO_Q21.txt:125-142`; Claude finding `04_claudecode/slice_025_doc125_claudecode_findings.md`.

## Required Repairs / Holds

- Q0121: keep the formal `细则位置` source-limited until a matching official Q20 rubric is found.
- Q0122: locate the true original prompt/material and unify `智慧` vs `中国智慧` from source, not inference.
- Q0123: add `外交政策（多边主义）` and the three formal cap rules.
- Q0125: delete the unsupported protectionism contrast; replace the answer addition with source-backed `提升中国在全球经济治理中的话语权和影响力`; add the formal cross-material `见点给分` rule.
- Q0121-Q0124: duplicate-group merge remains book-level pending; no normalized question group is accepted in this slice.
