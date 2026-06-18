# Slice 010 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 46-50 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- ClaudeCode evidence: `04_claudecode/slice_010_claudecode_findings.md`
- ClaudeCode debug: `04_claudecode/slice_010_quick_debug.log` confirms dispatch to `claude-opus-4-8`
- Codex source evidence: `05_source_backcheck/slice_010/source_backcheck_slice010_notes.md`

## Merge Summary

ClaudeCode correctly identified the main slice-level pattern: several entries promote a source-backed phrase into a stronger role than the source supports, and every entry lacks independent hard-rule fields for `术语/核心采分点` and `细则位置`.

Codex then checked local original exam/rubric sources. This resolves two ClaudeCode low-evidence points:

- Q0048: the term is present in the reference answer, but there is no independent subscore split in the extracted source. Final status remains repair-needed, not accepted.
- Q0050: the term is formally present as a 2-point required point. Final status is source-backed but still repair-needed because the desktop file lacks independent `术语` and exact `细则位置`.

## Per-Entry Final Judgments

### Q0046 doc_order=46

- final status: NEEDS_FIX
- source-backed? yes, but only in a narrow position
- key finding: `共同利益` appears in the official rubric only inside the `对世界` comprehensive-significance 1-point layer. The desktop file over-promotes it into the cooperation root and answer main chain.
- evidence:
  - `SRC_EXAM_2026_XICHENG_YIMO_Q20_2.txt:155-157`
  - `SRC_RUBRIC_2026_XICHENG_YIMO_Q20_2.txt:68-80`
- repair:
  - add exact source and `细则位置`;
  - move `共同利益` to the comprehensive/world-significance layer;
  - make standard rules and industry/supply-chain layers the main scoring structure;
  - boundary-label industry/supply-chain/economic-effect terms.

### Q0047 doc_order=47

- final status: NEEDS_FIX
- source-backed? yes, as a variation
- key finding: `当前国际竞争实质` is an accepted variation inside the 2-point challenge layer. It is not the whole question's main point; the 6-point core is the `卡脖子` open-development support chain.
- evidence:
  - `SRC_EXAM_2024_XICHENG_YIMO_Q19.txt:203-204`
  - `SRC_RUBRIC_2024_XICHENG_YIMO_Q19.txt:86-101`
- repair:
  - mark the term as challenge-layer variation;
  - keep product structure, standards/rules voice, and product/service competitiveness as the 6-point support structure;
  - retain boundary warning for new-quality productive forces and modern industrial-system wording.

### Q0048 doc_order=48

- final status: NEEDS_FIX
- source-backed? yes, but no independent subscore split found
- key finding: the source answer contains `当前国际竞争的实质`, but Q19(2) is a mixed `政治与法治` + `当代国际政治与经济` cause-analysis question. The desktop row needs explicit module separation.
- evidence:
  - `SRC_EXAM_2024_SHUNYI_ERMO_Q19_2.txt:170-171`
  - `SRC_RUBRIC_2024_SHUNYI_ERMO_Q19_2.txt:32-34`
- repair:
  - add exact source position;
  - mark the term as part of the international-competition/national-interest layer;
  - separate social-development law, government duty, and people-centered material from the 选必一 main term.

### Q0049 doc_order=49

- final status: NEEDS_FIX
- source-backed? yes, as one available angle in a level-scored question
- key finding: the source lists `当前国际竞争实质` as one possible angle, while the scoring is a 9-point level table. The desktop file must not imply a fixed independent score.
- evidence:
  - `SRC_EXAM_2024_XICHENG_ERMO_Q17.txt:134-137`
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:21-25`
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:75-85`
- repair:
  - mark it as a level-question argument tool;
  - preserve the role framing around `最大的发展中国家应当扮演的角色`;
  - add exact source and level-table position.

### Q0050 doc_order=50

- final status: NEEDS_FIX
- source-backed? yes, strongest in this slice
- key finding: official rubric marks `当前国际竞争的实质...` plus innovation-driven strategy/technology strength as a `2分（1+1）必答点`. The desktop answer aligns materially, but the entry still lacks independent hard-rule source fields and needs boundary labels for the broader open-development terms.
- evidence:
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:318-330`
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:96-112`
- repair:
  - add exact `必答点 2分（1+1）` position;
  - keep the innovation/technology evidence as the required point;
  - separate broader development-potential/opening/economic-globalization directions from the core international-competition required point.

## Ledger Status Plan

- doc_order 46: PASS 1, NEEDS_FIX 6, PENDING_BOOK_LEVEL 1
- doc_order 47: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 48: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1
- doc_order 49: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 50: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1

Slice 010 total: PASS 15, NEEDS_FIX 20, PENDING_BOOK_LEVEL 5.

## Boundary

This merge accepts only doc_order 46-50 as source-reviewed. It does not complete the full book. After this slice, 50 of 561 entries are source-reviewed and 511 entries remain.
