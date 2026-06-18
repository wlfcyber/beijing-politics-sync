# Slice 032 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T03:04:23+08:00
- scope: doc_order 156-160 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- ClaudeCode lane: real `claude -p --model opus --effort max`, stream init resolved to `claude-opus-4-8` for doc156-doc160.

## Result Summary

| doc_order | entry_id | source | merged result | required action |
|---:|---|---|---|---|
| 156 | Q0156 | 2026房山一模Q19 | PASS with UQ0068 book-level hold | No entry repair; later review UQ0068. |
| 157 | Q0157 | 2026门头沟一模Q20 | PASS with UQ0015 book-level hold | No entry repair; later review UQ0015. |
| 158 | Q0158 | 2026通州期末Q21 | NEEDS_FIX | Narrow visible core label to high-level opening; source does not support制度型开放 for this综合题 slice. |
| 159 | Q0159 | 2025朝阳期末Q21 | NEEDS_FIX | Remove or demote `制度型开放/深化国际经贸合作`; use source economic-environment wording. |
| 160 | Q0160 | 2024东城一模Q20 | PASS with UQ0060 book-level hold | No entry repair; later review UQ0060. |

## Source Evidence

- Q0156: exam `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342`; rubric `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:58-64`.
- Q0157: exam `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`; rubric `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`.
- Q0158: exam `SRC_EXAM_2026_TONGZHOU_QIMO_Q21.txt:283-302`; rubric `SRC_RUBRIC_2026_TONGZHOU_QIMO_Q21.txt:159-186`.
- Q0159: exam `SRC_EXAM_2025_CHAOYANG_QIMO_Q21.txt:229-237,298-305`; operative PPTX `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1314-1490`.
- Q0160: exam `SRC_EXAM_2024_DONGCHENG_YIMO_Q20.txt:1-15`; rubric `SRC_RUBRIC_2024_DONGCHENG_YIMO_Q20.txt:1-7`.

## Merge Notes

- Q0156 passes as two valid mini-chains: investment/environment and China-solution制度型开放. Full four-layer source structure is present in same-group notes.
- Q0157 passes and avoids Q0151's domestic-only trigger error; it stays on world-side market access and制度型开放.
- Q0158 is stricter than ClaudeCode's total PASS: the正文 is usable, but the visible core label overstates `制度型开放` where the source only supports high-level opening as one comprehensive-question angle.
- Q0159 needs answer-landing repair because the source economic-environment scoring point is 高水平对外开放/服务构建新发展格局, not independent制度型开放 or深化国际经贸合作.
- Q0160 passes with a clear broad `经济的相关知识` boundary; its 选必一 slice is source item 3/4, while same-group notes preserve the full 3+3+2 structure.

## Boundary

This merge accepts only doc_order 156-160 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 161; 401 entries remain pending.
