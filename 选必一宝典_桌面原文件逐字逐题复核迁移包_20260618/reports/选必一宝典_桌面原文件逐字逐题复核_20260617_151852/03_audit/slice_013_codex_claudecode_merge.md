# Slice 013 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 61-65 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- ClaudeCode evidence: `04_claudecode/slice_013_claudecode_findings.md`
- ClaudeCode debug: `04_claudecode/slice_013_quick_debug.log` confirms dispatch to `claude-opus-4-8`
- Codex source evidence: `05_source_backcheck/slice_013/source_backcheck_slice013_notes.md`

## Merge Summary

ClaudeCode correctly flagged the main structural risk in all five entries: the desktop source over-promotes national-interest material. Codex source backcheck confirms the exact source positions and tightens the final status:

- Q0061: source supports `当前国际竞争的实质` plus maintaining national interest, but only inside one layer of a cross-module answer.
- Q0062: source is a three-relationship rubric; `维护本国利益` is a sub-item under the China/world relationship.
- Q0063: source supports `国家利益和国家实力是影响国际关系的决定性因素` and common interests, not the single `出发点和落脚点` formula.
- Q0064: source supports a national-interest option inside the theoretical-logic layer, but value meaning remains separate and the wording is not the desktop's stronger formula.
- Q0065: source treats `国家利益` as a replaceable angle; the four main angles must remain visible.

## Per-Entry Final Judgments

### Q0061 doc_order=61

- final status: NEEDS_FIX
- source-backed? yes, as part of the international-competition/national-interest layer
- key finding: the desktop's selected answer sentence is usable as a partial 选必一 layer, but the core formula is not independently scored and the item crosses `政治与法治` and `当代国际政治与经济`.
- evidence:
  - `SRC_EXAM_2024_SHUNYI_ERMO_Q19_2.txt:164-171`
  - `SRC_RUBRIC_2024_SHUNYI_ERMO_Q19_2.txt:32-34`
- repair:
  - rename the point around `当前国际竞争的实质` and `维护国家利益`;
  - mark it as one layer inside a cross-module 8-point response;
  - keep social-development and government-duty layers outside this subpoint.

### Q0062 doc_order=62

- final status: NEEDS_FIX
- source-backed? yes, as one sub-item in the third relationship
- key finding: `维护本国利益` appears in the third relationship, but the answer must also keep the world-development side, such as public goods, correct义利观, Global South and human community.
- evidence:
  - `SRC_RUBRIC_2026_CHAOYANG_QIZHONG_Q17.txt:14-30`
  - `SRC_EXAM_2026_CHAOYANG_QIZHONG_Q17.txt:148-168`
  - `SRC_EXAM_2026_CHAOYANG_QIZHONG_Q17.txt:243-245`
- repair:
  - use `处理好中国发展和世界发展的关系` as the local position;
  - demote national interest to the China-development side of that relationship;
  - keep autonomous/opening and development/security layers separate.

### Q0063 doc_order=63

- final status: NEEDS_FIX
- source-backed? yes, but not under the desktop formula
- key finding: the answer sentence is source-aligned because it uses `决定性因素/共同利益`; the title-level core formula still needs repair.
- evidence:
  - `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:103-108`
  - `SRC_RUBRIC_2026_SHIJINGSHAN_ERMO_Q18.txt:49-50`
  - `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:125-126`
- repair:
  - replace the core point with `国家利益和国家实力是影响国际关系的决定性因素` and `共同利益`;
  - mark the basis layer as 4 points and meaning layer as 4 points;
  - do not use `出发点和落脚点` as the rubric label.

### Q0064 doc_order=64

- final status: NEEDS_FIX
- source-backed? yes, but only as one theoretical-logic angle
- key finding: the source has `国家利益角度：共同利益/维护国家利益是主权国家对外活动的出发点/正确的义利观`, so the desktop's `出发点和落脚点` and own-energy-security-centered answer are too narrow.
- evidence:
  - `SRC_EXAM_2026_YANQING_YIMO_Q19_2.txt:213-258`
  - `SRC_RUBRIC_2026_YANQING_YIMO_Q19_2.txt:102-110`
  - `SRC_EXAM_2026_YANQING_YIMO_Q19_2.txt:330-335`
- repair:
  - place this under theoretical logic, national-interest/common-interest angle, 2 points;
  - rewrite the answer around common interests, correct义利观 and energy-governance interest community;
  - keep value meaning as a separate 4-point layer.

### Q0065 doc_order=65

- final status: NEEDS_FIX
- source-backed? yes, as a replaceable angle
- key finding: the official source has four main angles. The desktop line `国家利益、国际关系、多边主义等角度可替代作答` itself proves national interest is not the main structure.
- evidence:
  - `SRC_EXAM_2025_YANQING_YIMO_Q20_2.txt:212-225`
  - `SRC_RUBRIC_2025_YANQING_YIMO_Q20_2.txt:87-90`
- repair:
  - restore the four main angles: era theme, globalization direction, multipolarity, human community;
  - label national interest as optional/replaceable and non-duplicate;
  - mark supply-chain and opening content rather than filing the whole item as pure `国家安全`.

## Ledger Status Plan

- doc_order 61: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1
- doc_order 62: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1
- doc_order 63: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 64: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1
- doc_order 65: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1

Slice 013 total: PASS 15, NEEDS_FIX 20, PENDING_BOOK_LEVEL 5.

## Boundary

This merge accepts only doc_order 61-65 as source-reviewed. It does not complete the full book. After this slice, 65 of 561 entries are source-reviewed and 496 entries remain.
