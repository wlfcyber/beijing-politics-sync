# Slice 040 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T07:20:25+08:00
- scope: doc_order 196-200 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 196 | Q0196 | 2026房山一模Q19海南"一线放开"自由便利 | NEEDS_FIX + PENDING_BOOK_LEVEL | Production/technology layer is source-backed, but block 2318 wrongly links "一线放开" to 进出岛 and uses the consumption layer instead of the 3D-printer tax-saving to core-technology trigger; UQ0049 remains pending. |
| 197 | Q0197 | 2026朝阳期中Q17 | PASS + PENDING_BOOK_LEVEL | AI self-reliance/open-cooperation layer is source-backed; `核心利益` is a soft drift only, not a hard safety/sovereignty import; UQ0003 remains pending. |
| 198 | Q0198 | 2024西城一模Q19(6) | NEEDS_FIX + PENDING_BOOK_LEVEL | Answer landing is source-backed, but the core label overstates `技术创新/提高产品质量`; source supports product/service competitiveness, product structure, high added value, and trade-rule voice; UQ0026 remains pending. |
| 199 | Q0199 | 2025西城一模Q18 | NEEDS_FIX + PENDING_BOOK_LEVEL | Technology/quality/competition layer is source-backed, but block 2351 misstates answer/rubric terms as the question wording; cross-module 《经济与社会》 overlap should remain visible; UQ0038 remains pending. |
| 200 | Q0200 | 2026海淀一模Q20中国标准走出国门撬动两个市场两种资源 | PASS + PENDING_BOOK_LEVEL | Standard-going-global competitiveness layer is source-backed; no hard desktop-text repair; UQ0072 remains pending. |

## Source Evidence

- Q0196: `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342`; `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:58-65`; Claude finding `04_claudecode/slice_040_doc196_claudecode_findings.md`.
- Q0197: `SRC_EXAM_2026_CHAOYANG_QIZHONG_Q17.txt:148-170,243-245`; `SRC_RUBRIC_2026_CHAOYANG_QIZHONG_Q17.txt:14-30`; Claude finding `04_claudecode/slice_040_doc197_claudecode_findings.md`.
- Q0198: `SRC_EXAM_2024_XICHENG_YIMO_Q19.txt:197-204`; `SRC_RUBRIC_2024_XICHENG_YIMO_Q19.txt:85-101`; Claude finding `04_claudecode/slice_040_doc198_claudecode_findings.md`.
- Q0199: `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt:221-234,342-345`; `SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt:65-78`; Claude finding `04_claudecode/slice_040_doc199_claudecode_findings.md`.
- Q0200: `SRC_EXAM_2026_HAIDIAN_YIMO_Q20.txt:339-355`; `SRC_RUBRIC_2026_HAIDIAN_YIMO_Q20.txt:85-89`; Claude finding `04_claudecode/slice_040_doc200_claudecode_findings.md`.

## Required Repairs / Holds

- Q0196: repair block 2318 only. Remove the claim that "一线放开" corresponds to 进出岛; source places 进出岛 under 二线口岸. Retarget the trigger to the 3D-printer tax saving invested into core technology攻坚 and rubric production layer.
- Q0197: no row-level hard repair. Keep a soft note that `核心利益` is broader than the source's `核心技术自主可控`/`维护本国利益`, but it does not corrupt the answer landing.
- Q0198: narrow the core label away from `提高产品质量/加强技术创新` as a formal source phrase; use source/rubric language such as product/service international competitiveness, product structure, high-added-value production, and trade-rule voice. Treat block 2342's `产品质量` wording as soft precision to tag or remove during repair.
- Q0199: repair block 2351 only. Do not say the question asks `开拓海外市场` or `提升国际循环质量`; those are answer/rubric terms. Keep the actual prompt in block 2352 unchanged and use the 川鳗 32-process/养殖近地加工/工艺品质 trigger already expressed in block 2353.
- Q0200: no row-level hard repair. Preserve the source-backed standard/competition/two-markets distinction; UQ0072 must later confirm that doc161/doc172/doc200 do not double-count the same rubric sentence.
- No normalized question group is accepted in this slice: UQ0049, UQ0003, UQ0026, UQ0038, and UQ0072 remain PENDING_BOOK_LEVEL.

## Boundary

This merge accepts only doc_order 196-200 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 201; 361 entries remain pending.
