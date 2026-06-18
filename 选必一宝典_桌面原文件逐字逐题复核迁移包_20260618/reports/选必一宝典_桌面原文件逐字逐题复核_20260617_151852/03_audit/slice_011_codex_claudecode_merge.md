# Slice 011 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 51-55 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- ClaudeCode evidence: `04_claudecode/slice_011_claudecode_findings.md`
- ClaudeCode debug: `04_claudecode/slice_011_quick_debug.log` confirms dispatch to `claude-opus-4-8`
- Codex source evidence: `05_source_backcheck/slice_011/source_backcheck_slice011_notes.md`

## Merge Summary

ClaudeCode correctly found the slice-level risks: Q0051/Q0054 are the same 10-point 东城 education question split into two core points, Q0052 over-promotes `国际竞争实质`, Q0055 is a level-scored question, and all rows lack independent hard-rule `术语` and `细则位置` fields.

Codex source backcheck resolves the source-evidence gaps:

- Q0051/Q0054: formal 东城细则 confirms a 2+6+2 structure. `人才与国际竞争力` is in the optional `为什么` layer, while `科教兴国人才强国战略` is in the `怎么做` 2-point layer.
- Q0052: formal 石景山细则 does not use `国际竞争实质`; it uses `国家利益和国家实力` plus economic-globalization/common-interest layers.
- Q0053: formal 房山细则 confirms a 4-point first chain beginning with `国际竞争的实质`, but the desktop answer omits the rest of that chain.
- Q0055: formal 西城细则 confirms the term as an available angle under a 9-point level-scored question.

## Per-Entry Final Judgments

### Q0051 doc_order=51

- final status: NEEDS_FIX
- source-backed? partially; source supports talent/international-competitiveness relation, not the exact `国际竞争实质` formula
- key finding: desktop core is over-specific. This is one optional `为什么` angle inside a 10-point education comprehensive question.
- evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q21.txt:205-220`
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q21.txt:191-208`
- repair:
  - merge book-level handling with Q0054;
  - rewrite as `教育战略支撑地位、人才与国际竞争力关系` if keeping this angle;
  - add exact `为什么` layer position and module labels.

### Q0052 doc_order=52

- final status: NEEDS_FIX
- source-backed? source-backed for the question, not for the desktop core term
- key finding: formal source says `国家利益和国家实力是影响国际关系的决定性因素`; it does not say `当前国际竞争的实质`.
- evidence:
  - `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:103-108`
  - `SRC_RUBRIC_2026_SHIJINGSHAN_ERMO_Q18.txt:49-50`
  - `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:125-126`
- repair:
  - remove or demote `国际竞争实质`;
  - rebuild around basis 4分 and significance 4分;
  - label two markets/two resources, people-benefit, region/world effects by source layer.

### Q0053 doc_order=53

- final status: NEEDS_FIX
- source-backed? yes
- key finding: formal 房山细则 gives the first 4-point chain beginning with `国际竞争的实质`, but the desktop answer stops after technology strength and omits high-level opening, innovative/open world economy, and economic globalization.
- evidence:
  - `SRC_EXAM_2025_FANGSHAN_YIMO_Q18.txt:181-189`
  - `SRC_RUBRIC_2025_FANGSHAN_YIMO_Q18.txt:95-100`
- repair:
  - add exact first-chain position;
  - write the full 4-point chain, including the不可替代 open-world-economy point;
  - keep the second 3-point UN/HMC/global-governance chain separate.

### Q0054 doc_order=54

- final status: NEEDS_FIX
- source-backed? yes, as `怎么做` layer
- key finding: `科教兴国人才强国战略` is source-backed in the 2-point `怎么做` layer, but the desktop answer sentence writes a talent-advantage explanation rather than the action strategy.
- evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q21.txt:205-220`
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q21.txt:191-208`
- repair:
  - merge book-level handling with Q0051;
  - mark this as `怎么做` 2分;
  - rewrite answer落点 to include the strategy/action language rather than only talent advantage.

### Q0055 doc_order=55

- final status: NEEDS_FIX
- source-backed? yes, as one available angle in a level-scored question
- key finding: `实施科教兴国战略，强化现代化建设人才支撑` is an available angle, not a fixed independent score. Desktop wording also overstates with `引领新一轮科技革命`.
- evidence:
  - `SRC_EXAM_2024_XICHENG_ERMO_Q17.txt:101-103`
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:19-23`
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:66-76`
- repair:
  - mark as level-question available angle;
  - remove fixed-score framing;
  - soften answer to talent support for the role of the largest developing country.

## Ledger Status Plan

- doc_order 51: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1
- doc_order 52: PASS 1, NEEDS_FIX 6, PENDING_BOOK_LEVEL 1
- doc_order 53: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1
- doc_order 54: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1
- doc_order 55: PASS 2, NEEDS_FIX 5, PENDING_BOOK_LEVEL 1

Slice 011 total: PASS 9, NEEDS_FIX 26, PENDING_BOOK_LEVEL 5.

## Boundary

This merge accepts only doc_order 51-55 as source-reviewed. It does not complete the full book. After this slice, 55 of 561 entries are source-reviewed and 506 entries remain.
