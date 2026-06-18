# Slice 039 Source Backcheck Notes

- created_at: 2026-06-18T06:22:43+08:00
- scope: doc_order 191-195
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_docx_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- note: source excerpt files are copied from earlier verified source-backcheck slices where available; 2025西城期末Q20(2) is newly registered from desktop original PDFs and existing text caches.

## doc_order 191 Q0191 2025海淀一模Q21(2)
- core_point: 中国市场红利推动互利共赢
- source excerpts: `SRC_EXAM_2025_HAIDIAN_YIMO_Q21_2.txt`; `SRC_RUBRIC_2025_HAIDIAN_YIMO_Q21_2.txt`
- watchpoints:
  - Rubric lines 90-93 support three layers: trade facilitation, green/digital trade, and super-large-market advantage/mutual benefit.
  - Prior doc93 was NEEDS_FIX only for the separate trade-facilitation row using `投资` wording; do not transfer that hard error to this market-dividend row unless source evidence requires it.
  - UQ0065 remains book-level pending across doc_orders 93/191/233.

## doc_order 192 Q0192 2026东城二模Q20(3)
- core_point: 促进国内国际双循环，让世界共享中国发展机遇
- source excerpts: `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt`; `SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt`
- watchpoints:
  - Source prompt uses quoted brand names `“购在中国”` and `“投资中国”` plus 7分; desktop prompt omits quotes and score.
  - Prior doc94 was NEEDS_FIX for missing quotes plus generic trigger wording; prior doc162 was PASS when row focus was valid and only quote punctuation was optional. Decide this row independently against its exact blocks.
  - Teacher reference line 154 has full `为世界发展提供中国机遇`; rubric line 39 is visibly truncated at `机` in the text extract.

## doc_order 193 Q0193 2026东城二模Q20(3)
- core_point: 发挥我国超大规模市场优势
- source excerpts: `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt`; `SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt`
- watchpoints:
  - Rubric first layer line 26 directly supports super-large-market advantage.
  - Check whether missing quoted brand names in the prompt field is a hard row-level prompt issue here, consistent with doc94/doc162 treatment.
  - UQ0046 remains book-level pending.

## doc_order 194 Q0194 2026东城二模Q20(3)
- core_point: 推动全球要素向中国市场集聚
- source excerpts: `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt`; `SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt`
- watchpoints:
  - Rubric lines 28 and teacher reference line 154 support consumer/investment pull, foreign investment, global capital/factor agglomeration, and mutual benefit.
  - Check whether the row overextends to technology/capital factors beyond the explicit source wording.
  - UQ0046 remains book-level pending.

## doc_order 195 Q0195 2025西城期末Q20(2)
- core_point: 加强技术创新、提高产品质量，增强竞争力
- source excerpts: `SRC_EXAM_2025_XICHENG_QIMO_Q20_2.txt`; `SRC_RUBRIC_2025_XICHENG_QIMO_Q20_2.txt`
- watchpoints:
  - This is 2025西城期末Q20(2), not 2026西城期末Q20.
  - Rubric lines 177-190 give 3-of-4 scoring angles; current row focuses on the提升竞争力/竞争新优势 angle in lines 182-183.
  - The same group should preserve rules-rights, competition, market diversification, and going-out angles; only two markets/resources without analysis is a 1分 boundary.
  - UQ0067 remains book-level pending across doc_orders 195/202/214.

## Trace Notes

- No source DOCX mutation.
- 2025西城期末 source rows added to `00_control/SOURCE_LEDGER.csv` if absent: `SRC_EXAM_2025_XICHENG_QIMO_Q20_2`, `SRC_RUBRIC_2025_XICHENG_QIMO_Q20_2`.
