# COVERAGE_FUSION_BATCH04_2026_SHIJINGSHAN_ERMO_CODEX_20260525

Status: `CODEX_BATCH04_DONE__CLAUDECODE_PRELIMINARY_PASS_WITH_CORRECTION_APPLIED__MODEL_GATE_BLOCKED`

Timestamp: 2026-05-25 00:58 +08

## Scope

Batch04 covers `2026石景山二模` inside `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.

Rows closed this round:

- existing candidate rows: `M0155`, `M0156`, `M0244`
- suite-source rows: `M0736` through `M0755`
- ClaudeCode mirror correction rows: `M0034`, `M0035`, `M0036`

Result: all active `2026石景山二模` rows now have explicit covered / inserted / excluded / residue dispositions. Suite-local active pending rows: `0`.

Global recovery matrix after Batch04:

- exact production-line candidate rows still open: `485`
- rows still marked as needing source/fusion adjudication: `485`

## Source Authority Used

Primary source bundle:

`01_source_inventory/suite_source_bundles/2026石景山二模.md`

Key source positions:

- lines 17-19: official choice answer key, Q1-Q15 = `A D B C C D B D D B B A A A D`.
- lines 21-22: Q16 is `经济与社会`.
- lines 23-50: Q17 scoring reference; Q17(1) is `政治与法治`, Q17(2) is `逻辑与思维`, Q17(3) is philosophy optional-angle scoring.
- lines 49-71: Q17(3) says one philosophy viewpoint may be used and lists `联系、矛盾、实践与认识关系` as allowed angles. This supports inclusion but not cumulative three-point scoring.
- lines 72-78: Q18 is international politics/economy, Q19 is law, and Q20 lists `系统观` only as one broad optional angle in a multi-module comprehensive question.
- lines 116-121: Q1 stem/options; correct option ② supports the system node.
- lines 122-127: Q2 stem/options; correct option ④ supports contradiction; option ② is culture/national spirit and is excluded from this philosophy body.
- lines 128-133: Q3 stem/options; correct options ①③ support whole/part and concrete analysis; wrong option ④ is not used.
- lines 158-163: Q9 stem/options; correct options ③④ support practice and people.

## DOCX Changes

New final-body entries inserted:

| node | heading | basis |
|---|---|---|
| 系统观念 / 系统优化 | `25. 2026石景山二模 第1题（选择题）` | official key Q1=A; only correct option ② is used for the system chain |
| 矛盾就是对立统一 | `36. 2026石景山二模 第2题（选择题）` | official key Q2=D; only correct option ④ is used for the opposition-unity chain |
| 整体与部分 | `16. 2026石景山二模 第3题（选择题）` | official key Q3=B; correct options ①③ link big-picture planning and detailed implementation |
| 矛盾的特殊性 / 具体问题具体分析 | `27. 2026石景山二模 第3题（选择题）` | official key Q3=B; correct option ① says 因地制宜、精准发力 |
| 实践是认识的基础 | `27. 2026石景山二模 第9题（选择题）` | official key Q9=D; correct options ③④ emphasize actual work and practice testing |
| 人民群众 | `26. 2026石景山二模 第9题（选择题）` | official key Q9=D; correct option ④ says performance must withstand people's test |

Existing Q17(3) final-body entries retained, but evidence labels are downgraded to `正式评分参考角度`:

- `联系的普遍性 / 联系的观点（总）`
- `矛盾就是对立统一`
- `实践与认识（总）`

No DOCX insertion was made for Q20. Its scoring reference lists `系统观` only as one broad optional angle in a multi-module comprehensive question, without a specific philosophy material-to-answer chain.

## ClaudeCode Correction

Real ClaudeCode Opus 4.7 Batch04 recheck completed under a blocked model gate.

Required correction found and applied:

- `M0034`, `M0035`, `M0036` were still labeled `强细则` in the structured matrix column.
- They now match accepted JSONL and candidate rows as `正式评分参考角度`.
- Backup: `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch04_claudecode_mirror_correction_20260525_005508.csv`

## Matrix And Ledger Verification

Updated files:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `05_delivery/docx_insert_ledger.csv`
- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- current DOCX/PDF in `05_delivery/`

Post-update verification:

- `2026石景山二模` matrix rows: `36`
- `2026石景山二模` active suite-pending rows: `0`
- global active candidate rows: `485`
- insert ledger rows: `47`
- inserted ledger headings found in DOCX: `47 / 47`
- inserted label paragraphs: `188 / 188` pass style check

DOCX exact text hits after insertion:

- `2026石景山二模 第1题`: `1`
- `2026石景山二模 第2题`: `1`
- `2026石景山二模 第3题`: `2`
- `2026石景山二模 第9题`: `2`
- `2026石景山二模 第17(3)题`: `3`

## Render QA

Render results after Batch04:

- DOCX size: `353,607` bytes
- PDF size: `3,548,768` bytes
- PDF page count: `238`
- rendered page PNGs: `238`
- contact sheet exists: `07_render_check/word_pdf_pages/contact_every_12_pages.png`
- automated page-image scan: `238` pages checked; only `page_002.png` is near-blank and is the intended foreword title page

PDF normalized search pages:

- Q1 inserted entry: page `77`
- Q2 inserted entry: page `123`
- Q3 inserted entries: pages `67`, `135`
- Q9 inserted entries: pages `175`, `207`
- existing Q17(3) entries: pages `54`, `122`, `164`
- Q20: no final-body hit, as intended

Student-facing residue scan returned `0` hits in DOCX/PDF for the current banlist, including audit residues, source-lane terms, reference-answer residues, local paths, and the removed 2024海淀一模 Q17(2) misplacement.

## Boundary

This is not final acceptance. It is a Codex production-line batch closure for one suite, with a real but model-gate-blocked ClaudeCode Opus 4.7 recheck. GPTPro web / Claude Opus external full-artifact review remains `real_call_pending`.
