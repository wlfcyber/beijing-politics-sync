# Slice 020 Codex + ClaudeCode Merge

- timestamp: 2026-06-17T21:13:37+08:00
- scope: doc_order 96-100 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: five per-entry real `claude-opus-4-8` / max runs, files `04_claudecode/slice_020_doc096_claudecode_findings.md` through `slice_020_doc100_claudecode_findings.md`.

## Summary

- Q0096: NEEDS_FIX. Formal rubric supports the trade/investment facilitation layer, but the desktop row attributes `关键产品和服务自由流通` to material two without source support; the key-products note points to security/supply-risk, not free circulation.
- Q0097: NEEDS_FIX. The regional-integration content is source-backed, but the China-development importance layer flattens economic/security/political scoring angles into six keywords and can overcount same-angle synonyms.
- Q0098: PASS. The economic-globalization trend and `融入经济全球化进程` slice is supported by 延庆一模 Q19(2) material, answer and rubric.
- Q0099: PASS. The Hainan free-trade-port slice matches 门头沟 Q20 source and 7-point reason/China/world/logic rubric.
- Q0100: PASS with boundary note. 2024东城一模 Q20 is a broad `经济的相关知识` question; this row validly captures the external-cycle openness point, but group-level overlap with doc_order 160/175 remains pending.

## Entry Results

### Q0096 doc_order=96

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for unsupported `关键产品和服务自由流通` and inherited answer wording.
- Codex source finding: agrees. Source line 155 says higher-level FTA; line 156 defines key products by importance/supply risk. Rubric lines 71-72 support lower institutional transaction cost, trade efficiency, and trade/investment facilitation, but not the free-circulation phrase.
- evidence:
  - `SRC_EXAM_2026_XICHENG_YIMO_Q20_2.txt:155-157`
  - `SRC_RUBRIC_2026_XICHENG_YIMO_Q20_2.txt:68-80`
- repair:
  - remove or rewrite `促进关键产品和服务自由流通` in material trigger and answer;
  - use source-backed wording around `更高水平自由贸易协定 -> 降低制度性交易成本/提高贸易效率 -> 贸易投资便利化自由化`.

### Q0097 doc_order=97

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for scoring-angle overflattening in block 1169.
- Codex source finding: agrees. The row's material, prompt and answer are valid, but the China-development need layer must preserve the rubric's economic/security/political grouping.
- evidence:
  - `SRC_EXAM_2025_CHAOYANG_ERMO_Q21.txt:225-228`
  - `SRC_RUBRIC_2025_CHAOYANG_ERMO_Q21.txt:291-310`
- repair:
  - restore `经济/安全/政治` three-angle grouping under the importance layer;
  - add warning that synonyms inside the same angle do not stack.

### Q0098 doc_order=98

- final status: PASS, with duplicate-group review pending
- ClaudeCode: PASS.
- Codex source finding: agrees. `经济全球化趋势` is an allowed historical-trend angle, and `融入经济全球化进程` appears in the official answer/rubric.
- evidence:
  - `SRC_EXAM_2026_YANQING_YIMO_Q19_2.txt:213-258`
  - `SRC_EXAM_2026_YANQING_YIMO_Q19_2.txt:330-335`
  - `SRC_RUBRIC_2026_YANQING_YIMO_Q19_2.txt:102-110`
- boundary:
  - UQ0017 still needs group-level checking across nine entries.

### Q0099 doc_order=99

- final status: PASS, with duplicate-group review pending
- ClaudeCode: PASS.
- Codex source finding: agrees. Source/rubric support the Hainan mechanisms and the reason/China/world/logic structure.
- evidence:
  - `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`
  - `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`
- boundary:
  - UQ0015 still needs group-level checking across ten entries.

### Q0100 doc_order=100

- final status: PASS, with module and duplicate-group boundary note
- ClaudeCode: PASS.
- Codex source finding: agrees. The row is source-backed as the external-cycle openness point in a broader economic question.
- evidence:
  - `SRC_EXAM_2024_DONGCHENG_YIMO_Q20.txt:336-346`
  - `SRC_RUBRIC_2024_DONGCHENG_YIMO_Q20.txt:362-366`
- boundary:
  - do not claim the whole Q20 is only an 选必一 item; it is `经济的相关知识` with inner-cycle and outer-cycle points.
  - UQ0060 still needs group-level de-duplication with doc_order 160 and 175.

## Ledger Impact

- doc_order 96-100 field rows reviewed: 40.
- Field statuses in this slice: PASS 32, NEEDS_FIX 3, PENDING_BOOK_LEVEL 5.
- Reviewed entries after slice: 100 / 561.
- Reviewed field rows after slice: 800 / 4488.
- Remaining source review after slice: 461 entries.
