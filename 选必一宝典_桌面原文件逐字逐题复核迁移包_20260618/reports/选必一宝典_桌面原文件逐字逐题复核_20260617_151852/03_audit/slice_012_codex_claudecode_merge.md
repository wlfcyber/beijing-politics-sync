# Slice 012 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 56-60 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- ClaudeCode evidence: `04_claudecode/slice_012_claudecode_findings.md`
- ClaudeCode debug: `04_claudecode/slice_012_quick_debug.log` confirms dispatch to `claude-opus-4-8`
- Codex source evidence: `05_source_backcheck/slice_012/source_backcheck_slice012_notes.md`

## Merge Summary

ClaudeCode correctly caught the internal risks from the slice text: Q0057, Q0059 and Q0060 over-promote national-interest material; Q0058 is only one of four angles; Q0056 is an answer-chain item rather than a fixed scoring point. ClaudeCode also correctly noted that all five rows lack independent hard-rule `术语` and `细则位置` fields.

Codex source backcheck resolves the evidence level:

- Q0056: formal 海淀 source supports `维护我国的主权、安全和发展利益` as a `不变` aspect/basic goal, but not as an independently scored `出发点和落脚点` formula.
- Q0057: formal 东城 source confirms the short essay has title/form, China contribution, EU critique, and China attitude/doings layers. `坚定维护本国利益` belongs to the China attitude/doings layer.
- Q0058: rendered 朝阳 formal scoring page confirms an 8-point four-angle structure. National interest is angle 4 only.
- Q0059: formal 西城 source confirms a 9-point level question. `国家安全与核心利益` is an available angle, not a fixed score.
- Q0060: source PPT/scoring material confirms the four-environment answer frame. `维护我国主权、安全和发展利益` is one item inside the `总体外部环境` bundle.

## Per-Entry Final Judgments

### Q0056 doc_order=56

- final status: NEEDS_FIX
- source-backed? yes, but only as a `不变` aspect/basic-goal sentence
- key finding: the desktop answer sentence is source-aligned, but the exact core formula is not independently positioned in the formal source.
- evidence:
  - `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q21_2.txt:239-256`
  - `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q21_2.txt:311-315`
  - `SRC_RUBRIC_2025_HAIDIAN_QIZHONG_Q21_2.txt:15-17`
- repair:
  - mark the layer as `不变` aspect/basic goal;
  - avoid fixed-score wording;
  - add source identity and exact position.

### Q0057 doc_order=57

- final status: NEEDS_FIX
- source-backed? yes, as a China attitude/doings sublayer
- key finding: `坚定维护本国利益` is a valid answer item, but it is one optional item inside a 3-point layer of a short essay, not the whole question's core.
- evidence:
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:192-201`
  - `SRC_RUBRIC_2025_DONGCHENG_QIMO_Q20_PDF.txt:127-142`
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:645-655`
- repair:
  - demote national interest to the China attitude/doings layer;
  - keep contribution, EU critique, and negotiation/common-interest layers separate;
  - reconsider the `国家安全` sub-bucket.

### Q0058 doc_order=58

- final status: NEEDS_FIX
- source-backed? yes
- key finding: the national-interest formula is real, but it is angle 4 in a four-angle 8-point rubric.
- evidence:
  - `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_VISUAL.txt:4-16`
  - `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_CACHE_FROM_SAME_SOURCE.txt:119-134`
- repair:
  - add exact scoring position: angle 4, background 1 + goal 1;
  - label the answer as partial, not full 8分;
  - keep peace/development, political, economic and national-interest angles distinct.

### Q0059 doc_order=59

- final status: NEEDS_FIX
- source-backed? yes, but only as a level-question available angle
- key finding: the source says `国家安全与核心利益`; the desktop writes a stronger fixed theory formula and treats it as a core采分点.
- evidence:
  - `SRC_EXAM_2024_XICHENG_ERMO_Q17.txt:101-103`
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:19-23`
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:66-76`
- repair:
  - rewrite as a level-question angle;
  - remove fixed-score/fixed-formula framing;
  - preserve cross-module labels for economic, theory, international and security roles.

### Q0060 doc_order=60

- final status: NEEDS_FIX
- source-backed? yes, but only as one item inside the overall-environment bundle
- key finding: the desktop answer is too narrow because it does not answer the four-environment frame for营造良好外部环境.
- evidence:
  - `SRC_EXAM_2025_CHAOYANG_QIMO_Q21.txt:229-237`
  - `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1314-1350`
  - `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1368-1489`
- repair:
  - demote `维护主权、安全和发展利益` to the `总体外部环境` layer;
  - rebuild answer around overall, political, economic, cultural/public-opinion external environments;
  - preserve the source warning that mere textbook piling can cap the score.

## Ledger Status Plan

- doc_order 56: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 57: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1
- doc_order 58: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 59: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1
- doc_order 60: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1

Slice 012 total: PASS 15, NEEDS_FIX 20, PENDING_BOOK_LEVEL 5.

## Boundary

This merge accepts only doc_order 56-60 as source-reviewed. It does not complete the full book. After this slice, 60 of 561 entries are source-reviewed and 501 entries remain.
