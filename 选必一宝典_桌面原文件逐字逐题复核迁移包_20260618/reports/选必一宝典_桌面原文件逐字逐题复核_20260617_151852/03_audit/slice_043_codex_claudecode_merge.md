# Slice 043 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T08:48:59+08:00
- scope: doc_order 211-215 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 211 | Q0211 | 2026海淀一模Q20中国标准与全球经济治理参与 | PASS + LOW_EVIDENCE_GROUP | The standards/rule-voice row is source-backed, but the inventory treats it as singleton UQ0121 even though it shares the same source as UQ0082/doc208; same-question de-duplication remains low-evidence at book level. |
| 212 | Q0212 | 2025昌平二模Q21稳外资行动提升全球经济治理话语权 | NEEDS_FIX + LOW_EVIDENCE_GROUP | The 同题组 scoring details are source-backed, but the core label and blocks 2498/2500/2501 repeat the overgeneralization found in Q0209: governance voice belongs to the 投资中国/platform layer, not all稳外资 actions. UQ0102 may be a naming split from UQ0054 and remains low-evidence at book level. |
| 213 | Q0213 | 2026东城一模Q19(3) | PASS + PENDING_BOOK_LEVEL | The international-standard/rule-docking narrow card is source-backed inside the open-promotes-resilience branch, and 2514-2517 preserve the full 4+3+1 relationship structure. UQ0021 remains pending. |
| 214 | Q0214 | 2025西城期末Q20(2) | NEEDS_FIX + PENDING_BOOK_LEVEL | Enterprise subject, prompt, source and four-answer set are source-backed, but block 2523 adds `合法` to `维护自身权益`; align to source or mark as paraphrase. UQ0067 remains pending. |
| 215 | Q0215 | 2025海淀期中Q16(2) | LOW_EVIDENCE + PENDING_BOOK_LEVEL | The rules/governance sentence is source-backed, but `选必一部分2分` and the prompt score `（6分）` are not supported by the provided exam/rubric excerpt. UQ0030 remains pending. |

## Source Evidence

- Q0211: `SRC_EXAM_2026_HAIDIAN_YIMO_Q20.txt:339-355`; `SRC_RUBRIC_2026_HAIDIAN_YIMO_Q20.txt:85-89`; Claude finding `04_claudecode/slice_043_doc211_claudecode_findings.md`.
- Q0212: `SRC_EXAM_2025_CHANGPING_ERMO_Q21.txt:255-266,368-374`; `SRC_RUBRIC_2025_CHANGPING_ERMO_Q21.txt:125-143`; Claude finding `04_claudecode/slice_043_doc212_claudecode_findings.md`.
- Q0213: `SRC_EXAM_2026_DONGCHENG_YIMO_Q19_3.txt:218-227,303-308`; `SRC_RUBRIC_2026_DONGCHENG_YIMO_Q19_3.txt:8-28`; Claude finding `04_claudecode/slice_043_doc213_claudecode_findings.md`.
- Q0214: `SRC_EXAM_2025_XICHENG_QIMO_Q20_2.txt:307-317,413-418`; `SRC_RUBRIC_2025_XICHENG_QIMO_Q20_2.txt:167-190`; Claude finding `04_claudecode/slice_043_doc214_claudecode_findings.md`.
- Q0215: `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q16_2.txt:180-193`; `SRC_RUBRIC_2025_HAIDIAN_QIZHONG_Q16_2.txt:1-8`; Claude finding `04_claudecode/slice_043_doc215_claudecode_findings.md`.

## Required Repairs / Holds

- Q0211: no row-level text repair. Book-level de-duplication must decide whether UQ0121 should merge with UQ0082/doc208.
- Q0212: repair core label and blocks 2498/2500/2501. Replace unsupported `参与国际标准制定` and broad `与各国对接经贸规则` framing with the source-backed `提升全球经济治理中的话语权和影响力` under `投资中国` brand/platform and bilateral investment-promotion mechanism. Remove unsupported `世界经济不确定背景` unless source is found.
- Q0213: no row-level hard repair. Keep UQ0021 pending for eight-card normalization.
- Q0214: repair block 2523 from `积极维护自身合法权益` to source-backed `积极维护自身权益`, or explicitly mark `合法` as paraphrase. Keep UQ0067 pending.
- Q0215: do not assert `选必一部分2分` or prompt `（6分）` without a separate authoritative score split. Either add source evidence or soften/delete those point-value claims. Optional polish: restore `充分利用` and `我国政府和企业` for closer rubric wording.
- No normalized question group is accepted in this slice: UQ0121/UQ0082, UQ0102/UQ0054, UQ0021, UQ0067, and UQ0030 remain open at book level.

## Boundary

This merge accepts only doc_order 211-215 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 216; 346 entries remain pending.
