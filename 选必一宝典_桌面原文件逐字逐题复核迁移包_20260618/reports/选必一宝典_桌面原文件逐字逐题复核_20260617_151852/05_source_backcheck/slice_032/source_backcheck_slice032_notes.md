# Slice 032 Source Backcheck Notes

- created_at: 2026-06-18T02:46:54+08:00
- scope: doc_order 156-160
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_docx_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- note: Tongzhou Q21 source rows are newly introduced in this run from the desktop original PDF/PPTX text caches; register original file hashes when merging.

## doc_order 156 Q0156 2026房山一模Q19
- core_point: 中国扩大高水平对外开放与制度型开放
- source excerpts: `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342`, `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:58-64`
- watchpoint: Entry has two mini-chains: investment/environment and China-solution制度型开放. Check whether both map to the four-layer rubric without overclaiming the whole 8-point answer.
- watchpoint: Earlier related entries had one-line/two-line口岸 trigger confusion; verify source wording exactly.

## doc_order 157 Q0157 2026门头沟一模Q20
- core_point: 中国扩大高水平对外开放与制度型开放
- source excerpts: `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`, `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`
- watchpoint: Same source as doc151 but different facet. Check whether trigger stays world-side (market access/high-level opening example) and does not narrow the prompt to domestic meaning.
- watchpoint: Core `中国扩大高水平对外开放与制度型开放` may map to world-side制度型开放 and market-space points, not the full 7-point answer.

## doc_order 158 Q0158 2026通州期末Q21
- core_point: 中国扩大高水平对外开放与制度型开放
- source excerpts: `SRC_EXAM_2026_TONGZHOU_QIMO_Q21.txt:283-302`, `SRC_RUBRIC_2026_TONGZHOU_QIMO_Q21.txt:159-186`
- watchpoint: Prompt is a 综合运用所学 multi-module question, not a fixed 选必一同题组. Check whether high-level opening is only one optional angle.
- watchpoint: Rubric also lists independent self-reliance/tech-support angle; do not merge it into high-level opening.

## doc_order 159 Q0159 2025朝阳期末Q21
- core_point: 中国扩大高水平对外开放与制度型开放
- source excerpts: `SRC_EXAM_2025_CHAOYANG_QIMO_Q21.txt:229-237`, `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1314-1490`
- watchpoint: External-environment question has four required angle groups. Check whether this entry overstates制度型开放 because source economic environment lists 高水平对外开放, not necessarily制度型开放.
- watchpoint: Same-group caps (missing overall/political/economic/culture; textbook pile cap) must match the PPTX lines.

## doc_order 160 Q0160 2024东城一模Q20
- core_point: 中国扩大高水平对外开放与制度型开放
- source excerpts: `SRC_EXAM_2024_DONGCHENG_YIMO_Q20.txt:1-15`, `SRC_RUBRIC_2024_DONGCHENG_YIMO_Q20.txt:1-7`
- watchpoint: Source prompt is `经济的相关知识`, not 《当代国际政治与经济》. Check module/source-role boundary for a 选必一宝典 slice.
- watchpoint: This source is 4 points choose 3 in 3+3+2 form; the entry should keep item 3/4 as a slice, not the whole answer.
