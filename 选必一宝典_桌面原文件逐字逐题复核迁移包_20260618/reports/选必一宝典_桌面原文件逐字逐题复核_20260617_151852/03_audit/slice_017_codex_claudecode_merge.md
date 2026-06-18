# Slice 017 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 81-85 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- ClaudeCode evidence: `04_claudecode/slice_017_doc081_claudecode_findings.md` through `04_claudecode/slice_017_doc085_claudecode_findings.md`
- ClaudeCode stream traces: `04_claudecode/slice_017_doc081_stream.jsonl` through `04_claudecode/slice_017_doc085_stream.jsonl`
- Codex source evidence: `05_source_backcheck/slice_017/source_backcheck_slice017_notes.md`

## Merge Summary

ClaudeCode and Codex agree on the most important repair in this slice: Q0082 cannot frame the whole 门头沟Q20 as merely `国内意义`, because the source asks for both China and world significance. Codex is stricter than ClaudeCode on Q0084's prompt completeness: the source includes four short-review writing requirements, and the desktop prompt omits them.

- Q0081: content pass; add formal source identity later. Optional scoring wording tightening: `促进贸易往来（2分）`.
- Q0082: repair needed for domestic-only framing in `材料触发点` and `为什么能想到`.
- Q0083: content pass; source supports the row through `经贸合作/加强贸易合作`, not by the exact phrase `贸易投资自由化便利化`.
- Q0084: content pass but strict prompt repair needed; the full short-review writing requirements are omitted.
- Q0085: content pass; `贸易自由化便利化` is correctly treated as a substitute under the `共同利益` layer rather than as the whole question core.

## Per-Entry Final Judgments

### Q0081 doc_order=81

- final status: CONTENT_PASS_WITH_SOURCE_FIELD_REPAIR
- ClaudeCode: PASS, with optional tightening of the `促进贸易往来` substitute point.
- Codex source finding: agrees; source lines 55-66 support the same three scoring requirements.
- evidence:
  - `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt:251-262`
  - `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt:55-66`
- repair:
  - attach formal 海淀一模 Q18(1) source identity;
  - optionally mark `促进贸易往来` as a 2-point substitute to match source line 62.

### Q0082 doc_order=82

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX because desktop wording says the question points to domestic significance.
- Codex source finding: agrees; source prompt and rubric both require China + world significance.
- evidence:
  - `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`
  - `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`
- repair:
  - replace `题目指向分析国内意义` and `问国内意义` with wording such as `本条聚焦中国意义中的贸易自由化便利化落点`;
  - keep the same-group reason/China/world/logic structure.

### Q0083 doc_order=83

- final status: CONTENT_PASS_WITH_SOURCE_FIELD_REPAIR
- ClaudeCode: PASS.
- Codex source finding: agrees with a wording caveat: the official source supports `经贸合作/加强贸易合作`, while `贸易投资自由化便利化` is a teaching abstraction.
- evidence:
  - `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:255-266`
  - `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:368-374`
  - `SRC_RUBRIC_2025_CHANGPING_ERMO_Q21.txt:125-142`
- repair:
  - attach formal 昌平二模 Q21 source identity;
  - if rewritten later, label `贸易投资自由化便利化` as a teaching abstraction supported by `经贸合作/加强贸易合作`.

### Q0084 doc_order=84

- final status: CONTENT_PASS_WITH_STRICT_PROMPT_REPAIR
- ClaudeCode: PASS, but misread several supplied source-boundary lines as low evidence.
- Codex source finding: source lines 440-447 prove the desktop prompt omits the short-review writing requirements; source lines 252-254 prove the language and upper-bound boundaries.
- evidence:
  - `SRC_EXAM_2024_CHAOYANG_QIZHONG_Q20_3.txt:414-447`
  - `SRC_RUBRIC_2024_CHAOYANG_QIZHONG_Q20_3.txt:232-254`
- repair:
  - add the writing requirements:围绕主题、观点明确；论证充分、逻辑清晰；学科术语使用规范；总字数200字左右;
  - attach formal source identity.

### Q0085 doc_order=85

- final status: CONTENT_PASS_WITH_SOURCE_FIELD_REPAIR
- ClaudeCode: PASS.
- Codex source finding: agrees; source line 175 places `贸易自由化便利化` as a 1-point substitute under common interests, and the desktop answer does not over-promote it.
- evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q20.txt:207-216`
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q20.txt:312-313`
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q20.txt:171-194`
- repair:
  - attach formal 东城一模 Q20 exam source identity;
  - if rewritten later, remove unsupported `人员往来` wording and preserve the source warning about economic/political-angle mixing.

## Slice 017 Acceptance

- scope accepted as source-reviewed: doc_order 81-85
- not accepted as full book: doc_order 86-561 and all normalized book-level groups remain open.
- source DOCX mutation: none.
