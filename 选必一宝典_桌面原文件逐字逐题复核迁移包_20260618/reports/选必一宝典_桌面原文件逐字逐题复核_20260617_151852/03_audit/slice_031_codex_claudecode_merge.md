# Slice 031 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T02:39:33+08:00
- scope: doc_order 151-155 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- ClaudeCode lane: real `claude -p --model opus --effort max`, stream init resolved to `claude-opus-4-8` for doc151-doc155.

## Result Summary

| doc_order | entry_id | source | merged result | required action |
|---:|---|---|---|---|
| 151 | Q0151 | 2026门头沟一模Q20 | NEEDS_FIX | Correct trigger/why from domestic-only to China+world prompt and world-side制度型开放 facet. |
| 152 | Q0152 | 2024海淀一模Q18(1) | PASS with UQ0034 book-level hold | No entry repair; later review UQ0034. |
| 153 | Q0153 | 2026朝阳一模Q20 | PASS with UQ0002 book-level hold | Optional precision: add `24项`自贸协定; later review UQ0002. |
| 154 | Q0154 | 2026东城一模Q19(3) | PASS with UQ0021 book-level hold | No entry repair; later review UQ0021. |
| 155 | Q0155 | 2025丰台一模Q20 | NEEDS_FIX | Restore full mixed-module no-credit boundary and copy-material cap. |

## Source Evidence

- Q0151: exam `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`; rubric `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`.
- Q0152: exam `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt:251-262`; rubric `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt:55-66`.
- Q0153: exam `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:218-230,376-385`; rubric `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99`.
- Q0154: exam/reference `SRC_EXAM_2026_DONGCHENG_YIMO_Q19_3.txt:218-227,305-308`; rubric `SRC_RUBRIC_2026_DONGCHENG_YIMO_Q19_3.txt:16-28`.
- Q0155: exam/reference `SRC_EXAM_2025_FENGTAI_YIMO_Q20.txt:206-220,287-289`; rubric `SRC_RUBRIC_2025_FENGTAI_YIMO_Q20.txt:13-14`.

## Merge Notes

- Q0151's answer landing is source-backed for the world-side high-level-opening facet, but its trigger and why fields incorrectly say the prompt is domestic meaning and use a China-side cost point.
- Q0152 passes as a focused high-level-opening slice; the full factor-flow/two-markets layer remains in same-group notes, so this is not a repeat of Q0145's hard omission.
- Q0153 passes after Codex checked the full rubric lines 96-99, resolving ClaudeCode's low-evidence caveat about the later development-potential directions.
- Q0154 passes as an open-side slice because the same-group notes preserve the full 4+3+1 structure and the official落点.
- Q0155 needs repair only on scoring/boundary completeness: the formal rubric's no-credit boundary includes 《经济与社会》政府与市场知识, and the copy-material cap should also be retained.

## Boundary

This merge accepts only doc_order 151-155 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 156; 406 entries remain pending.
