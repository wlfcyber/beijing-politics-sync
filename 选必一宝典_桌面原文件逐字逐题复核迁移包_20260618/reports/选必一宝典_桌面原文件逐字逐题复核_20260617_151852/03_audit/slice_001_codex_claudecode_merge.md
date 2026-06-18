# Slice 001 Codex + ClaudeCode Merge

- slice: doc_order 1-5
- source: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- claudecode_model: `claude-opus-4-8`
- claudecode_trace:
  - `04_claudecode/slice_001_real_verbose.stream.jsonl`
  - `04_claudecode/slice_001_debug_real_verbose.log`
  - `04_claudecode/slice_001_claudecode_findings.md`

## Shared Findings

Codex and ClaudeCode agree on the first five entries:

| doc_order | question_ref | merged_status | merged finding |
|---:|---|---|---|
| 1 | 2026通州期末Q20 | NEEDS_FIX | 同题组六点与用户复核确认方向一致，但正文缺独立【术语】和【细则位置】；逐点分值/证据层级还需回溯或标明来源类型。 |
| 2 | 2025海淀期中Q21(2) | LOW_EVIDENCE | 用户确认存在图片表格形式正式细则，但当前未转写；“按答案链训练、不展示固定分值层次”不能冒充正式细则。 |
| 3 | 2024海淀二模Q18(1) | LOW_EVIDENCE | 8分等级题缺正式来源/证据层级；和平与发展更像可用角度，不可直接当固定赋分术语。 |
| 4 | 2025延庆一模Q20(2) | LOW_EVIDENCE / NEEDS_FIX | “四角度×2分”缺正式来源；“高质量发展/高水平对外开放”需标必修二模块边界，不应充当选必一主链术语。 |
| 5 | 2024西城二模Q19 | LOW_EVIDENCE / NEEDS_FIX | “和平与发展”在同题组中像总判断替代项，却作为主条目归档；需标证据层级，答案落点也偏角度说明。 |

## Structural Finding

The current document fields are not enough to pass the 选必一 hard rules:

- 【设问】 can serve as 完整设问.
- 【材料触发点】 can serve as 材料触发 after content review.
- 【答案落点】 can serve as 答案句 only if it is a real answer-sheet sentence.
- 【同题组】 can be useful evidence only after it states source type, point/layer, score, replacement terms, and evidence level.
- The document lacks independent 【术语】 and 【细则位置】 fields in this slice.

## Ledger Update

`03_audit/QUESTION_AUDIT_LEDGER.csv` rows for doc_order 1-5 were updated with Codex/ClaudeCode merged findings:

- total updated rows: 40
- remaining pending rows: 4448

## Next Slice

Continue doc_order 6 onward. The next pass must keep checking whether repeated questions across different buckets share the same formal rubric layer and whether each bucket placement is a true scoring-function placement rather than a framework convenience.
