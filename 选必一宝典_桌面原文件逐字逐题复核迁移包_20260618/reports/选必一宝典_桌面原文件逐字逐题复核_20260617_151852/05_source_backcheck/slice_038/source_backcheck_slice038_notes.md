# Slice 038 Source Backcheck Notes

- created_at: 2026-06-18T05:53:31+08:00
- scope: doc_order 186-190
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_docx_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- note: source excerpt files are copied from earlier verified source-backcheck slices into this slice-local package; Claude prompts use selected line excerpts to avoid overlarge source prompts.

## doc_order 186 Q0186 2026门头沟一模Q20
- core_point: 内外联通畅通国内国际双循环，提升国际循环质量
- source excerpts: `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt`; `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt`
- watchpoints:
  - Block 2181 says the prompt points to domestic meaning, but source lines 342-356 ask both China new momentum and world open-development vitality.
  - Rubric line 126 supports domestic double-cycle linkage, while line 127 keeps the world-side layer; preserve both.
  - Prior doc151/doc166 were NEEDS_FIX for the same domestic-only narrowing.

## doc_order 187 Q0187 2026朝阳期中Q17
- core_point: 内外联通畅通国内国际双循环，提升国际循环质量
- source excerpts: `SRC_EXAM_2026_CHAOYANG_QIZHONG_Q17.txt`; `SRC_RUBRIC_2026_CHAOYANG_QIZHONG_Q17.txt`
- watchpoints:
  - Verify whether block 2192 “维护核心利益” is merely soft phrase drift or wrongly imports the national-interest/security branch into the self-reliance/opening branch.
  - Rubric line 20 directly supports international exchange, economic globalization, two markets/resources, and double circulation.
  - UQ0003 remains book-level pending.

## doc_order 188 Q0188 2024海淀一模Q18(1)
- core_point: 内外联通畅通国内国际双循环，提升国际循环质量
- source excerpts: `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt`; `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt`
- watchpoints:
  - Verify the three-layer 6分 structure: trade/investment facilitation, factor flow/two markets/resources, high-level opening.
  - Current row centers on the factor-flow/two-market/double-cycle layer; material trigger starts from facilitation then maps to that layer.
  - UQ0034 remains book-level pending.

## doc_order 189 Q0189 2024朝阳一模Q21
- core_point: 内外联通畅通国内国际双循环，提升国际循环质量
- source excerpts: `SRC_EXAM_2024_CHAOYANG_YIMO_Q21.txt`; `SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_DOCX.txt`; `SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_PPTX.txt`
- watchpoints:
  - Prompt requires first analyzing current economic situation, then answering how to open a new path in change.
  - Block 2213 focuses on external pressure; verify whether it is enough for this row or should be repaired toward super-large-market/two-market/double-cycle response.
  - UQ0005 remains book-level pending.

## doc_order 190 Q0190 2025门头沟一模Q19
- core_point: 中国市场红利与全球经济包容性增长
- source excerpts: `SRC_EXAM_2025_MENTOUGOU_YIMO_Q19.txt`; `SRC_RUBRIC_2025_MENTOUGOU_YIMO_Q19.txt`
- watchpoints:
  - Rubric supports market dividend/shared opportunity/globalization toward mutual benefit.
  - Rubric line 29 says “充分利用两个市场两种资源不给分”; verify this is preserved as a no-credit boundary rather than misused as an answer.
  - UQ0039 remains book-level pending across six entries.

## Trace Notes

- No source DOCX mutation.
- All source files in this slice are copies of previously registered source text caches; line excerpts are selected in each prompt.
