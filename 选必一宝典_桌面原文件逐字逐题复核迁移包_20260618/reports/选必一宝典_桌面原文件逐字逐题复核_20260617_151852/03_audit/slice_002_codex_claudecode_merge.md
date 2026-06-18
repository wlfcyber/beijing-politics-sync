# Slice 002 Codex + ClaudeCode Merge

- slice: doc_order 6-10
- source: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- claudecode_model: `claude-opus-4-8`
- claudecode_trace:
  - `04_claudecode/slice_002_real_verbose.stream.jsonl`
  - `04_claudecode/slice_002_debug_real_verbose.log`
  - `04_claudecode/slice_002_claudecode_findings.md`

## Shared Findings

Codex and ClaudeCode agree on doc_order 6-10:

| doc_order | question_ref | merged_status | merged finding |
|---:|---|---|---|
| 6 | 2025丰台期末Q20 | LOW_EVIDENCE | 同题组形态接近正式评标且分值自洽（8=4+2+2），但缺来源类型、正式细则登记、独立【术语】和【细则位置】；不能把 docx 自带同题组直接当正式细则。 |
| 7 | 2026西城二模Q19(1) | LOW_EVIDENCE / NEEDS_FIX | “和平与发展”是背景解释层替代项，非独立赋分；设问“运用当代国际政治知识”与模块名口径不一致，需回原卷；缺独立【术语】和【细则位置】。 |
| 8 | 2026朝阳期末Q20 | LOW_EVIDENCE | 同题组最像参考答案/教学框架重构：无逐角度分值，有“兜住1分”教学口吻；冒充正式细则风险最高。 |
| 9 | 2025朝阳期末Q21 | NEEDS_FIX | 内部分值可机械验证为 7≠8，上限提醒与层值不自洽；经济环境层混入“高水平对外开放/新发展格局”等必修二邻接词；需回正式评标修正。 |
| 10 | 2026顺义一模Q20 | NEEDS_FIX | 有 protocol 样例C锚点：共同利益1分必答；但“国际政治3/国际经济3”两层无已登记背书，且“和平与发展”是层内可选项非独立赋分。 |

## Added Findings Beyond Slice 001

- The missing independent 【术语】 and 【细则位置】 structure repeats in slice 002.
- Some same-question groups contain real internal defects, not just missing source labels.
- `2025朝阳期末Q21` has a visible score mismatch: displayed layers sum to 7 while the question is marked 8.
- `2026朝阳期末Q20` should be treated as likely reference-answer or teaching-framework reconstruction until a formal scoring source is found.
- `2026顺义一模Q20` has one confirmed scoring anchor from the protocol, but not enough evidence to validate the whole displayed same-question group.

## Ledger Update

`03_audit/QUESTION_AUDIT_LEDGER.csv` rows for doc_order 6-10 were updated:

- total updated rows: 40
- cumulative source-reviewed rows: 80
- remaining rows needing source-level or book-level review: 4408

## Next Slice

Continue doc_order 11 onward. Keep prioritizing:

- formal rubric/source type for every `同题组`;
- whether the displayed core point is independent scoring term, replacement, level condition, or merely a usable angle;
- internal score arithmetic;
- module-boundary terms, especially 必修二 phrases inside economic-globalization entries.
