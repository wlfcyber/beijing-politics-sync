# Slice 019 Codex + ClaudeCode Merge

- timestamp: 2026-06-17T20:49:46+08:00
- scope: doc_order 91-95 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: five per-entry real `claude-opus-4-8` / max runs, files `04_claudecode/slice_019_doc091_claudecode_findings.md` through `slice_019_doc095_claudecode_findings.md`.

## Summary

- Q0091: NEEDS_FIX. Core regional-facilitation content is valid, but desktop says 8分 while source exam says 9分 and rubric breakdown requires 总结1分.
- Q0092: NEEDS_FIX. Source says 中国成为18国的最大贸易伙伴, not 与18国互为最大贸易伙伴; 常态化 also overstates source wording.
- Q0093: NEEDS_FIX by Codex strict source rule. Claude passed with caution, but formal scoring says 贸易自由化便利化 and does not support 投资 for this layer.
- Q0094: NEEDS_FIX. Dedicated rubric supports investment facilitation, but prompt loses source quotation marks and block 1126 imports generic 通关/协议/人员往来 language.
- Q0095: SOURCE-LIMITED PASS / LOW-EVIDENCE fields. Teacher answer and material support the topic, but no matching Q20 rubric page was found and `贸易和投资自由化便利化` is not named in the teacher answer.

## Entry Results

### Q0091 doc_order=91

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for 9分/8分 conflict and missing 总结1分.
- Codex source finding: agrees. The regional cooperation slice is source-backed, but scoring layer must not state the whole question as 8分 without noting the source conflict.
- evidence:
  - `SRC_EXAM_2025_CHAOYANG_YIMO_Q20.txt:241-252`
  - `SRC_RUBRIC_2025_CHAOYANG_YIMO_Q20.txt:85-112`
- repair:
  - reconcile `20.(9分)` in the exam with the rubric header `20(8分)`;
  - mark `总结提升` as 1分 or explicitly record the scoring-source conflict.

### Q0092 doc_order=92

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for `互为最大贸易伙伴`.
- Codex source finding: agrees; `常态化` is also not a source phrase and should be weakened or removed.
- evidence:
  - `SRC_EXAM_2025_CHAOYANG_ERMO_Q21.txt:225-228`
  - `SRC_RUBRIC_2025_CHAOYANG_ERMO_Q21.txt:291-310`
- repair:
  - replace `与18国互为最大贸易伙伴` with `中国成为18国的最大贸易伙伴`;
  - avoid overstating the trade/investment relation as `常态化` unless separately sourced.

### Q0093 doc_order=93

- final status: NEEDS_FIX (strict term repair)
- ClaudeCode: PASS with a caution that the source says trade facilitation only.
- Codex source finding: stricter than Claude; this run should not let `投资` ride on a source that only scores `贸易自由化便利化`.
- evidence:
  - `SRC_EXAM_2025_HAIDIAN_YIMO_Q21_2.txt:222-234`
  - `SRC_RUBRIC_2025_HAIDIAN_YIMO_Q21_2.txt:90-93`
- repair:
  - replace `贸易投资自由化便利化` with `贸易自由化便利化` in this slice;
  - keep green/digital trade and market-potential layers for the duplicate group, not this row.

### Q0094 doc_order=94

- final status: NEEDS_FIX
- ClaudeCode: NEEDS_FIX for missing quotation marks around the two brand names.
- Codex source finding: additionally requires removing imported generic trigger language; source/rubric support investment catalog, international standards, service-sector access, tax credit, business environment and investment facilitation.
- evidence:
  - `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt:119-127`
  - `SRC_EXAM_2026_DONGCHENG_ERMO_Q20_3.txt:151-154`
  - `SRC_RUBRIC_2026_DONGCHENG_ERMO_Q20_3.txt:16-39`
- repair:
  - restore quotation marks around `“购在中国”` and `“投资中国”` in the prompt;
  - replace `通关、准入、协议和人员往来` with source-specific investment/opening facts.

### Q0095 doc_order=95

- final status: SOURCE-LIMITED PASS; ledger keeps low-evidence fields for term/scoring/answer.
- ClaudeCode: PASS with explicit limitations: official answer does not name trade/investment facilitation and no matching rubric page was found.
- Codex source finding: agrees with the limitation. The desktop text honestly says this is a same-theme exercise and not a fixed scoring layer, but the core point cannot be promoted as formal-rubric-backed.
- evidence:
  - `SRC_EXAM_2026_FENGTAI_ERMO_Q20.txt:343-362`
  - `SRC_EXAM_2026_FENGTAI_ERMO_Q20.txt:487-492`
  - `SRC_RUBRIC_2026_FENGTAI_ERMO_Q20_PPTX_MISMATCH.txt:246-285`
  - `SRC_RUBRIC_2026_FENGTAI_ERMO_Q20_PPTX_MISMATCH.txt:401-444`
- repair / boundary:
  - do not add fixed rubric layers without a true Q20 rubric;
  - keep this point as source-limited/reference-style unless group review confirms it should remain.

## Ledger Impact

- doc_order 91-95 field rows reviewed: 40.
- Field statuses in this slice: PASS 26, NEEDS_FIX 6, LOW_EVIDENCE 3, PENDING_BOOK_LEVEL 5.
- Reviewed entries after slice: 95 / 561.
- Reviewed field rows after slice: 760 / 4488.
- Remaining source review after slice: 466 entries.
