# Slice 017 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 81-85 only
- backcheck_time: 2026-06-17T19:52:51+0800

## Overall Finding

Slice 017 has source evidence for all five entries. The source content is mostly aligned, but two strict repairs are still required:

- Q0082 must stop describing the whole question as `国内意义`; the formal prompt asks for both China and world significance.
- Q0084 must restore the short-review writing requirements in the prompt field; the current desktop prompt omits them.

The other entries are source-aligned at the content level, but they still need formal source identity added in the desktop document before student-facing closure.

## Q0081 doc_order=81

- desktop blocks: 968-977
- question: 2024海淀一模Q18(1)
- source evidence:
  - `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt:251-262` confirms the visa-facilitation material and 6-point prompt.
  - `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt:55-66` confirms the three requirements: trade/investment facilitation, factor flow/two markets and resources, and high-level opening.

Codex judgment:

- `术语/核心采分点`: PASS. This row's core point `推进贸易和投资自由化便利化` matches the first 2-point scoring requirement.
- `完整设问`: PASS.
- `细则位置`: PASS, with a minor tightening suggestion: label `促进贸易往来` as 2 points to mirror source line 62.
- `来源`: NEEDS_FIX. The local source is found and registered, but the desktop entry still lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0034 still needs group-level reconciliation after all occurrences are source-reviewed.
- `模块边界`: PASS.

## Q0082 doc_order=82

- desktop blocks: 978-988
- question: 2026门头沟一模Q20
- source evidence:
  - `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356` confirms the 海南自贸港 full-island customs-closure prompt.
  - `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131` confirms the 2-point reason, 2-point China significance, 2-point world significance and 1-point logic structure.

Codex judgment:

- `术语/核心采分点`: PASS. Trade facilitation is an official China-significance option at source line 126.
- `完整设问`: PASS.
- `细则位置`: PASS. The same-group notes preserve the reason/China/world/logic scoring frame.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity.
- `材料触发`: NEEDS_FIX. Block 979 says the question points to `国内意义`, contradicting the source prompt's China + world significance.
- `答案句`: PASS. It is acceptable as the China-significance trade-facilitation slice, not as a whole-question answer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0083 doc_order=83

- desktop blocks: 989-999
- question: 2025昌平二模Q21
- source evidence:
  - `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:255-266` confirms the prompt and three 稳外资举措.
  - `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:368-374` confirms the teacher-answer summary.
  - `SRC_RUBRIC_2025_CHANGPING_ERMO_Q21.txt:125-142` confirms the 8-point three-part scoring rule and the `举措+意义` requirement.

Codex judgment:

- `术语/核心采分点`: PASS, with source wording caveat. The rubric supports this row through `经贸合作` and `加强贸易合作`, though it does not use the exact phrase `贸易投资自由化便利化`.
- `完整设问`: PASS.
- `细则位置`: PASS.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity; the text evidence used here comes from an existing extracted cache for the official PDF/PPTX.
- `材料触发`: PASS.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0054 still needs group-level reconciliation.
- `模块边界`: PASS.

## Q0084 doc_order=84

- desktop blocks: 1000-1011
- question: 2024朝阳期中Q20(3)
- source evidence:
  - `SRC_EXAM_2024_CHAOYANG_QIZHONG_Q20_3.txt:414-447` confirms the digital-trade material, short-review prompt and writing requirements.
  - `SRC_RUBRIC_2024_CHAOYANG_QIZHONG_Q20_3.txt:232-254` confirms the example answer and the title/three comments/summary/language scoring structure.

Codex judgment:

- `术语/核心采分点`: PASS. This row's trade/investment facilitation angle is supported by the platform/investment-trade scoring lines.
- `完整设问`: NEEDS_FIX. The desktop prompt omits the source writing requirements at lines 440-447.
- `细则位置`: PASS. Lines 238-254 confirm title 1, three comments 6, summary 2 and language 1.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0033 still needs group-level reconciliation.
- `模块边界`: PASS.

Note: ClaudeCode marked several Q0084 boundary items as LOW_EVIDENCE, but the supplied source text does include line 252 for language expression, line 253 for the `最多不超过5分` boundary, and line 254 for the `最高不超过4分` boundary. Codex therefore keeps those fields source-backed.

## Q0085 doc_order=85

- desktop blocks: 1012-1021
- question: 2025东城一模Q20
- source evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q20.txt:207-216` confirms the 元首外交 material and prompt.
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q20.txt:312-313` confirms the answer-angle summary.
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q20.txt:171-194` confirms the 4+2+2 structure and the line-175 substitute status of trade facilitation.

Codex judgment:

- `术语/核心采分点`: PASS. `贸易自由化便利化` is only a 1-point substitute under the common-interest layer; the desktop answer leads with `共同利益`, so it does not overstate the term.
- `完整设问`: PASS.
- `细则位置`: PASS.
- `来源`: NEEDS_FIX. The rubric was already known from slice 006; the exam prompt source is newly registered for this row.
- `材料触发`: PASS.
- `答案句`: PASS, with optional tightening: avoid unsupported `人员往来` language if this row is later rewritten.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0028 still needs group-level reconciliation.
- `模块边界`: PASS. No cross-module misuse found, though the final teaching version should preserve the source warning about economic/political-angle mixing.
