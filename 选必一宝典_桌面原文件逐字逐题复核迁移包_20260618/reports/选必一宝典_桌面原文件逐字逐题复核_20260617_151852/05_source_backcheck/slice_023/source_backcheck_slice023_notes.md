# Slice 023 Source Backcheck Notes

- timestamp: 2026-06-17T22:39:00+08:00
- scope: doc_order 111-115 only.
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop original is read-only; no edits made to the `.docx`.

## Source Coverage

- Q0111 2025昌平二模Q21: reused slice017 exam + rubric evidence.
- Q0112 2025西城一模Q21: added desktop original PDF/DOCX source identity, using existing extracted text caches for prompt/rubric.
- Q0113 2026石景山二模Q18: reused slice021 exam + rubric evidence.
- Q0114 2026顺义一模Q20: extracted the desktop original PDF directly with pypdf and used the PPTX rubric cache checked against the desktop PPTX path.
- Q0115 2025朝阳期末Q21: reused slice012 exam + readable scoring PPTX, with formal rubric PDF registered.

## Pre-Claude Codex Watchpoints

- Q0111: desktop `为什么能想到` says five-direction globalization, while formal rubric only explicitly says `推动构建更加开放、包容的全球经济格局` plus `推动经济全球化发展`; strict wording review needed.
- Q0112: source and rubric both explicitly support the Belt and Road example and five-direction globalization sentence.
- Q0113: source/rubric explicitly support the world-dimension five-direction globalization sentence; verify block 1349's quoted wording is a paraphrase, not an invented source quote.
- Q0114: source and rubric support low-cost/productivity/talent/endogenous-development chain and `普惠、平衡、共赢` direction; this row's core metadata is broader than the answer sentence.
- Q0115: source and readable scoring PPTX support the external economic environment branch.

## Correction 2026-06-17T22:57:40+08:00

- Corrected doc_order 113 Claude prompt evidence ranges: prior prompt accidentally truncated Shijingshan Q18 at source lines 106-108 and cited non-Q18 answer lines. Replaced with exam lines 106-111 and 128-129 plus rubric lines 52-53 before rerunning ClaudeCode. The incomplete-evidence Claude finding was preserved as `slice_023_doc113_claudecode_findings_incomplete_evidence_prompt.md`.
