# Slice 016 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 76-80 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- ClaudeCode evidence: `04_claudecode/slice_016_doc076_claudecode_findings.md` through `04_claudecode/slice_016_doc080_claudecode_findings.md`
- ClaudeCode stream traces: `04_claudecode/slice_016_doc076_stream.jsonl` through `04_claudecode/slice_016_doc080_stream.jsonl`
- Codex source evidence: `05_source_backcheck/slice_016/source_backcheck_slice016_notes.md`

## Merge Summary

ClaudeCode and Codex agree that slice 016 contains several source-label precision problems. Two entries in 2026朝阳一模Q20 split cleanly: Q0078 is an exact 1-point development-potential direction, while Q0076 uses a broad effect phrase instead of the source's exact factor-flow scoring phrase.

- Q0076: repair needed. Use `促进人才、商品、服务和生产要素在全球范围内流动` as the exact 1-point direction; treat `资源优化配置/国际贸易发展` as effect language.
- Q0077: repair needed. The desktop promotes the 2-point world-significance layer and misses the 3-point China-responsibility layer.
- Q0078: content pass with strict source-field repair. The core is source-backed as a development-potential 1-point direction.
- Q0079: source-backed main structure, but strict field repair is needed for missing no-credit boundary text.
- Q0080: repair needed. `贸易投资自由化便利化` is only one consumer/market-layer item; the answer phrase `国际循环消费端` and the `一线放开/二线管住` trigger need correction.

## Per-Entry Final Judgments

### Q0076 doc_order=76

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for promoting effect language into the core.
- Codex source finding: agrees; source label is factor flow inside the capped development-potential layer.
- evidence:
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:218-230`
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99`
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:390-393`
- repair:
  - relabel as `促进人才、商品、服务和生产要素在全球范围内流动`;
  - mark this as `发展潜力层1分方向`;
  - keep resource allocation/trade wording only as effect language.

### Q0077 doc_order=77

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX because the answer/core are mostly the world-significance layer.
- Codex source finding: agrees; source requires China-responsibility 3 points plus world-significance 2 points.
- evidence:
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-225`
  - `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-70`
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:303-306`
- repair:
  - rewrite around `开放广阔中国市场/正确义利观` and `共享发展新机遇、惠民生增福祉、互利共赢`;
  - place `普惠包容/开放型世界经济/贸易自由化` under the 2-point world-significance layer.

### Q0078 doc_order=78

- final status: CONTENT_PASS_WITH_SOURCE_FIELD_REPAIR
- ClaudeCode: PASS.
- Codex source finding: agrees, with formal source identity still missing from the desktop entry.
- evidence:
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:218-230`
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99`
- repair:
  - attach formal source identity;
  - keep the capped development-potential layer label.

### Q0079 doc_order=79

- final status: CONTENT_PASS_WITH_STRICT_FIELD_REPAIR
- ClaudeCode: NEEDS_FIX for missing the `《经济与社会》政府与市场知识` no-credit boundary.
- Codex source finding: agrees; main trade/investment structure is source-backed.
- evidence:
  - `SRC_EXAM_2025_FENGTAI_YIMO_Q20.txt:206-220`
  - `SRC_RUBRIC_2025_FENGTAI_YIMO_Q20.txt:13-14`
  - `SRC_EXAM_2025_FENGTAI_YIMO_Q20.txt:287-289`
- repair:
  - add the omitted no-credit boundary and material-copying warning;
  - attach formal source identity.

### Q0080 doc_order=80

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for nonstandard `国际循环消费端`, imprecise `一线放开` trigger, and missing OCR source identity.
- Codex source finding: agrees.
- evidence:
  - `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342` (OCR auxiliary extract for original PDF)
  - `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:59-64`
- repair:
  - relabel `贸易投资自由化便利化` as one consumer/market-layer item;
  - replace `国际循环消费端` with `助力/畅通国际循环`;
  - correct `一线放开` and add OCR source-level note.

## Ledger Status Plan

- doc_order 76: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 77: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1
- doc_order 78: PASS 6, NEEDS_FIX 1, PENDING_BOOK_LEVEL 1
- doc_order 79: PASS 4, NEEDS_FIX 3, PENDING_BOOK_LEVEL 1
- doc_order 80: PASS 3, NEEDS_FIX 4, PENDING_BOOK_LEVEL 1

Slice 016 total: PASS 20, NEEDS_FIX 15, PENDING_BOOK_LEVEL 5.

## Boundary

This merge accepts only doc_order 76-80 as source-reviewed. It does not complete the full book. After this slice, 80 of 561 entries are source-reviewed and 481 entries remain.
