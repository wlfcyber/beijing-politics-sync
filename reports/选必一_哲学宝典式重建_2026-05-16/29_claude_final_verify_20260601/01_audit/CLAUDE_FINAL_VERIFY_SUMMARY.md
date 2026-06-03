# Claude Final Verification Summary

## File Identity

- Claude DOCX: `/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_ea19f1a6-c672-4010-9aa6-235ad1631aa4/outputs/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx`
- Prior local Codex handoff: `/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终审修订版_20260601.docx`
- Claude SHA256: `f65aebb40723bb281f6b9b4af3f6a9657577d4e6038ad44db227d2f64985fe81`
- Codex SHA256: `cb5c3c0d906c13dd055b86760a75871cbec060b21dcc66c0a148f47a1bf10603`

## Structure Metrics

|file|entries|core_points|unique_core_points|why_fields|answer_fields|question_fields|trigger_fields|template_这不是单个材料细节|book_missing_exact|fake_page_exact|fengtai_qimo_q20|dongcheng_q19_3|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_ea19f1a6-c672-4010-9aa6-235ad1631aa4/outputs/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx|461|108|108|472|472|472|472|0|0|0|11|9|
|/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终审修订版_20260601.docx|450|108|108|461|461|461|461|223|8|2|0|9|

## Auto Findings

- Claude file is not byte-identical to prior local Codex handoff and has different structure counts.
- Template residue in Claude file: 0 / 0 / 0.
- Exact missing-book-title `《国际政治与经济》` occurrences: 0.
- Exact fake-page references `原卷第8页` / `原卷第 8 页`: 0.
- `2026丰台期末Q20` entries restored in Claude file: 11 blocks.
- `东城一模Q19(3)` blocks found in Claude file: 9 blocks.
- Residue hits requiring manual inspection: 0 rows in `claude_residue_hits.csv`.

## Manual-Review Queues

- `claude_fengtai_2026_qimo_q20_entries.csv`: restored Q20 blocks; source closure must be checked against desktop paper and rubric.
- `claude_dongcheng_q19_3_entries.csv`: all Dongcheng Q19(3) blocks with automatic flags.
- `claude_residue_hits.csv`: template, fake page, book-title, backend-label, and path residue hits.
