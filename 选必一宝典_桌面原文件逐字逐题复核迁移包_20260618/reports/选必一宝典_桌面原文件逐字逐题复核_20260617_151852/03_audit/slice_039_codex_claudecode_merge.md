# Slice 039 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T06:47:14+08:00
- scope: doc_order 191-195 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 191 | Q0191 | 2025海淀一模Q21(2) | PASS + PENDING_BOOK_LEVEL | Market-dividend/mutual-benefit layer is source-backed; doc93 `投资` wording error is absent; UQ0065 remains pending. |
| 192 | Q0192 | 2026东城二模Q20(3) | NEEDS_FIX + PENDING_BOOK_LEVEL | Total double-cycle layer is source-backed, but the prompt field drops quoted brand names `“购在中国”`/`“投资中国”` and omits `（7分）`; strict word-by-word review follows doc94/doc194. |
| 193 | Q0193 | 2026东城二模Q20(3) | NEEDS_FIX + PENDING_BOOK_LEVEL | Super-large-market layer is source-backed, but the same prompt-field quote/score repair is required for consistency. |
| 194 | Q0194 | 2026东城二模Q20(3) | NEEDS_FIX + PENDING_BOOK_LEVEL | Global-factor layer is source-backed and `资本、技术等要素` is acceptable, but the prompt-field quote/score repair is required. |
| 195 | Q0195 | 2025西城期末Q20(2) | PASS + PENDING_BOOK_LEVEL | 2025西城期末 source/rubric support the technology-quality-competitiveness angle; UQ0067 remains pending. |

## Source Evidence

- Q0191: `SRC_EXAM_2025_HAIDIAN_YIMO_Q21_2.txt:222-234`; `SRC_RUBRIC_2025_HAIDIAN_YIMO_Q21_2.txt:71-93`; Claude finding `04_claudecode/slice_039_doc191_claudecode_findings.md`.
- Q0192: `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt:119-127,151-154`; `SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt:16-39`; Claude finding `04_claudecode/slice_039_doc192_claudecode_findings.md`.
- Q0193: same Dongcheng source files as Q0192; Claude finding `04_claudecode/slice_039_doc193_claudecode_findings.md`.
- Q0194: same Dongcheng source files as Q0192; Claude finding `04_claudecode/slice_039_doc194_claudecode_findings.md`.
- Q0195: `SRC_EXAM_2025_XICHENG_QIMO_Q20_2.txt:307-317,413-418`; `SRC_RUBRIC_2025_XICHENG_QIMO_Q20_2.txt:167-190`; Claude finding `04_claudecode/slice_039_doc195_claudecode_findings.md`.

## Required Repairs / Holds

- Q0191: no row-level repair; UQ0065 remains PENDING_BOOK_LEVEL.
- Q0192/Q0193/Q0194: repair the `【设问】` field to restore quoted brand names and score: `分析“购在中国”与“投资中国”如何协同发力，释放我国独特的开放红利。（7分）`.
- Q0194: no repair needed for `全球资本、技术等要素`; source wording `全球资本等要素`/`全球要素集聚` supports this as an example expansion.
- Q0195: no row-level repair; preserve the no-credit/low-credit boundary that merely writing two markets/resources without concrete analysis gives only 1分.
- No normalized question group is accepted in this slice: UQ0065, UQ0046, and UQ0067 remain PENDING_BOOK_LEVEL.

## Boundary

This merge accepts only doc_order 191-195 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 196; 366 entries remain pending.
