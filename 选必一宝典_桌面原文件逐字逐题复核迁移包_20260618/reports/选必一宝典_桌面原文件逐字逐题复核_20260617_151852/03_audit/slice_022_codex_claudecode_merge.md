# Slice 022 Codex + ClaudeCode Merge

- timestamp: 2026-06-17T22:20:49+08:00
- scope: doc_order 106-110 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: five per-entry real `claude-opus-4-8` / max runs, files `04_claudecode/slice_022_doc106_claudecode_findings.md` through `slice_022_doc110_claudecode_findings.md`.

## Summary

- Q0106: PASS at slice level, with source-limited rubric evidence. 丰台二模 Q20 teacher answer supports the globalization/opening answer direction; the matching Q20 formal rubric remains missing, and the row correctly avoids fixed scoring claims.
- Q0107: NEEDS_FIX on `完整设问` only. 朝阳期中 Q20(3) answer/scoring structure is source-backed, but the desktop `【设问】` omits the original short-review requirements (`围绕主题/逻辑清晰/术语规范/200字左右`).
- Q0108: NEEDS_FIX. 东城一模 Q20 rubric supports the economic-globalization first-layer option, but the desktop answer sentence changes the fixed subject from `经济全球化` to `多边经贸合作`; material trigger also uses `方向调整` rather than the source-backed `方向发展` formula.
- Q0109: PASS. 延庆一模 Q20(2) source/rubric support the four 2分 angles and this row's economic-globalization branch.
- Q0110: PASS, duplicate-group pending. 顺义一模 Q20 official rubric supports the 8分 four-layer structure and includes `推动经济全球化朝开放包容普惠方向发展` as a world-contribution point.

## Entry Results

### Q0106 doc_order=106

- final status: PASS, source-limited rubric evidence, duplicate-group pending
- ClaudeCode: PASS.
- Codex source finding: agrees on content PASS but marks the `细则位置` field LOW_EVIDENCE because no matching formal Q20 scoring rubric was located; only the teacher answer and mismatch/absence evidence are available. The row does not claim fixed分值, so no repair is required.
- evidence:
  - `SRC_EXAM_2026_FENGTAI_ERMO_Q20.txt:343-362`
  - `SRC_EXAM_2026_FENGTAI_ERMO_Q20.txt:487-492`
  - `SRC_RUBRIC_2026_FENGTAI_ERMO_Q20_PPTX_MISMATCH.txt:416-418`
- boundary:
  - UQ0048 remains pending for five-way split review.

### Q0107 doc_order=107

- final status: NEEDS_FIX on complete-prompt field
- ClaudeCode: PASS, with optional note that original writing requirements could be added.
- Codex source finding: stricter under the user's逐字逐题要求. The main prompt sentence is correct, and the 10分 short-review structure is source-backed, but `【设问】` omits the attached requirements from the original prompt: `围绕主题、观点明确`, `论证充分、逻辑清晰`, `学科术语使用规范`, and `总字数在200字左右`.
- evidence:
  - `SRC_EXAM_2024_CHAOYANG_QIZHONG_Q20_3.txt:436-447`
  - `SRC_RUBRIC_2024_CHAOYANG_QIZHONG_Q20_3.txt:238-253`
- repair:
  - add the four short-review requirements to block 1280 or immediately after it;
  - optional wording cleanup: replace `双向签约` with source-closer `签约项目/中非双向商贸` if editing later.
- boundary:
  - UQ0033 remains pending for six-way split review.

### Q0108 doc_order=108

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for replacing the fixed subject `经济全球化` with `多边经贸合作` in the answer sentence.
- Codex source finding: agrees. The row is allowed to isolate the first-layer economic-globalization option in this 8分 three-layer question, but the answer sentence must keep the scoring formula's subject as `经济全球化`.
- evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q20.txt:207-216`
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q20.txt:171-181`
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q20.txt:183-189`
- repair:
  - revise block 1294 so the final clause is `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展`;
  - revise block 1291's `方向调整` to the source-backed `方向发展` formula;
  - optionally add the source warning that this question should focus on the recent `此行/此次` rather than over-expanding the中拉背景.

### Q0109 doc_order=109

- final status: PASS
- ClaudeCode: PASS.
- Codex source finding: agrees. The source/rubric support the chain expo / free-trade agreement / connectivity / supply-chain cooperation evidence and the 8分 four-angle rubric. This row's answer落点 is the official `经济全球化方向` 2分 branch.
- evidence:
  - `SRC_EXAM_2025_YANQING_YIMO_Q20_2.txt:214-226`
  - `SRC_RUBRIC_2025_YANQING_YIMO_Q20_2.txt:80-90`
- boundary:
  - UQ0096 has one member in the current inventory; still no full-book completion claim.

### Q0110 doc_order=110

- final status: PASS, duplicate-group pending
- ClaudeCode: PASS.
- Codex source finding: agrees. The desktop row tracks the official 8分 four-layer rubric, and the `开放包容普惠` economic-globalization point appears in the official world-contribution layer.
- evidence:
  - `SRC_EXAM_2025_SHUNYI_YIMO_Q20.txt:229-237`
  - `SRC_RUBRIC_2025_SHUNYI_YIMO_Q20.txt:65-70`
- boundary:
  - UQ0007 remains pending for twelve-way split review.

## Ledger Impact

- doc_order 106-110 field rows reviewed: 40.
- Field statuses in this slice: PASS 33, NEEDS_FIX 3, LOW_EVIDENCE 1, PENDING_BOOK_LEVEL 3.
- Reviewed entries after slice: 110 / 561.
- Reviewed field rows after slice: 880 / 4488.
- Remaining source review after slice: 451 entries.
