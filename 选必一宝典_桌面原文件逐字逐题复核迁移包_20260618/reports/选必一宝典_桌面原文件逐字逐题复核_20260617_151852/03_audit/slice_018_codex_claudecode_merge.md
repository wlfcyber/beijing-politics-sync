# Slice 018 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 86-90 only
- merge_time: 2026-06-17T20:20:17+08:00
- ClaudeCode: real opus/max per-entry stream outputs in `04_claudecode/slice_018_doc086_stream.jsonl` through `slice_018_doc090_stream.jsonl`.

## Summary

- Q0086: content-pass with source-field repair and a wording caveat around `投资`.
- Q0087: repair needed for scoring-total reconciliation and over-promoting the third-layer trade-facilitation option.
- Q0088: repair needed for incorrect `五个共同` wording.
- Q0089: repair needed for copied trigger/template text and module-boundary mismatch.
- Q0090: repair needed for omitted source answer effect points.

## Entry Results

### Q0086 doc_order=86

- final status: CONTENT_PASS_WITH_SOURCE_FIELD_REPAIR
- ClaudeCode: PASS, with a soft suggestion to weaken `投资` because source evidence is zero-tariff/trade-only.
- Codex source finding: agrees on content pass for this slice; source identity still must be attached, and a full-answer version should keep the 2-point shared-opportunity China-responsibility layer.
- evidence:
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-224`
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:303-306`
  - `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-71`
- repair:
  - attach formal source identity;
  - avoid treating zero tariff as evidence for `投资` facilitation unless explicitly framed as only the trade sub-item.

### Q0087 doc_order=87

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for scoring-total contradiction and generic trigger language.
- Codex source finding: agrees; `推动贸易自由便利` is valid only as a third-layer attitude/doings option, not the whole short-essay axis.
- evidence:
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:192-201`
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:645-657`
  - `SRC_RUBRIC_2025_DONGCHENG_QIMO_Q20_PDF.txt:127-142`
- repair:
  - reconcile the 8-point cap with the displayed sublayer point totals;
  - replace the generic `跨境交易流程、成本或市场准入` trigger with the actual anti-subsidy-tax/consultation facts.

### Q0088 doc_order=88

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX because the desktop misstates the source `五个共同` headings.
- Codex source finding: agrees; the term is source-backed under the `开放` angle, but block 1043 and 1045 need exact source wording.
- evidence:
  - `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:232-247`
  - `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:311-328`
  - `SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20.txt:49-69`
- repair:
  - replace `共同推进贸易投资自由化便利化` heading with `共同营造开放型区域经济环境`, while noting trade/investment facilitation is an item under it;
  - replace `共同促进区域繁荣` with `共同促进普惠包容发展`.

### Q0089 doc_order=89

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX because trigger and why-field contain prompt misstatement plus unsupported facts.
- Codex source finding: agrees and adds module-boundary repair: the source prompt is 《经济与社会》, and the source supports only `贸易便利化` as a material-condition point.
- evidence:
  - `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt:221-234`
  - `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt:342-345`
  - `SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt:65-78`
- repair:
  - remove `通关、准入、协议、人员往来` and replace with the actual transport/logistics/cold-chain facts;
  - mark the module boundary before treating this as a 选必一 trade-facilitation row.

### Q0090 doc_order=90

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX because block 1076 omits two source-answer effect points.
- Codex source finding: agrees; core slice answer is valid, but same-group scoring/aspect text is incomplete.
- evidence:
  - `SRC_EXAM_2024_FENGTAI_YIMO_Q20.txt:242-253`
  - `SRC_EXAM_2024_FENGTAI_YIMO_Q20.txt:369-373`
  - `SRC_RUBRIC_2024_FENGTAI_YIMO_Q20.txt:110-116`
- repair:
  - add `提高资源配置效率` to the infrastructure/factor-flow aspect;
  - add `推动全球供应链高质量发展` before the final supply-chain/economic-globalization effect.

## Ledger Impact

- doc_order 86-90 field rows reviewed: 40.
- Reviewed entries after slice: 90 / 561.
- Reviewed field rows after slice: 720 / 4488.
- Remaining source review after slice: 471 entries.
