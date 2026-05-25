# COVERAGE_FUSION_BATCH03_2026_CHAOYANG_ERMO_CODEX_20260525

Status: `CODEX_BATCH03_DONE__CLAUDECODE_RECHECK_PENDING`

Timestamp: 2026-05-25 00:28 +08

## Scope

Batch03 handles `2026朝阳二模` in `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.

Primary row group:

- Existing final-body rows: `M0007` through `M0012`
- Additional ClaudeCode candidate rows closed this round: `M0239`, `M0240`
- Suite-source candidate rows closed this round: `M0698` through `M0717`

Result: all 32 rows for `2026朝阳二模` now have explicit covered / inserted / excluded / residue dispositions. Suite-local pending rows: `0`.

Global recovery matrix after Batch03:

- exact `待核：生产线候选，非最终正文证据` rows: `506`
- exact `是：需逐题回源/融合裁决` rows: `506`

## Source Authority Used

Primary source bundle:

`01_source_inventory/suite_source_bundles/2026朝阳二模.md`

Key source positions:

- lines 18, 123-148, 505-524: Q16 scoring standard and detailed scoring dimensions. It supports the existing final-body nodes `矛盾就是对立统一`, `辩证否定 / 守正创新`, `矛盾的特殊性 / 具体问题具体分析`, and `价值观的导向作用`.
- lines 106-122, 424-440: Q21 detailed scoring. It supports `系统观念 / 系统优化` and `量变与质变 / 适度原则`; the mandatory party-leadership / Xi Jinping Thought points are political-module content and remain excluded from this philosophy handbook.
- lines 182-188 and 484: Q1 stem/options and official choice key `A`.
- lines 194-199 and 484: Q3 stem/options and official choice key `D`; correct options ③/④ map to `实践是认识发展的动力` and `社会存在决定社会意识`.
- lines 200-205 and 484: Q4 stem/options and official choice key `A`; correct options ①/③ map to system integration and contact diversity.
- lines 206-211 and 484: Q5 official key `C`; `辩证否定` is a wrong-option trap, so it is not inserted.
- lines 212-221 and 484: Q6/Q7 are logic/innovative-thinking boundaries, not 必修四 philosophy body entries.
- lines 292-297 and 401-414: Q20 is mainly 选必一 politics/economics; optional `对立统一` wording is not enough to add a current philosophy-body mainline entry.

Choice-question rows use the official choice key and correct-option chain only. They are not recorded as scoring rubrics.

## DOCX Changes

New final-body entries inserted:

| node | heading | basis |
|---|---|---|
| 价值观的导向作用 | `28. 2026朝阳二模 第1题（选择题）` | official key Q1=A; only correct option ① is used for the value-pursuit chain |
| 实践是认识的基础 | `26. 2026朝阳二模 第3题（选择题）` | official key Q3=D; correct option ③ maps to practice as the driving force of cognition |
| 社会存在与社会意识 | `12. 2026朝阳二模 第3题（选择题）` | official key Q3=D; correct option ④ maps to social existence determining social consciousness |
| 联系的多样性 | `7. 2026朝阳二模 第4题（选择题）` | official key Q4=A; correct option ③ maps to contact diversity in community governance |
| 系统观念 / 系统优化 | `24. 2026朝阳二模 第4题（选择题）` | official key Q4=A; correct option ① maps to integrated data/resource governance |

No DOCX insertion was made for Q16 or Q21 because the final body already contained rubric-supported entries for those questions.

Q1 correction note after ClaudeCode recheck: official answer `A` contains ①②, but only ① is a 必修四 value-guidance landing. Option ② is an economics/high-quality-development line and is explicitly excluded from this philosophy-body insertion.

## Row Decisions

| matrix row | question | decision | evidence level | placement result |
|---|---|---|---|---|
| M0007-M0012 | Q16/Q21 | keep existing final-body coverage | strong scoring standard / detailed scoring | no duplicate insertion |
| M0239 | Q16 | candidate closed as already covered | 强细则 | Q16 nodes already in final DOCX |
| M0240 | Q21 | candidate closed as already covered | 强细则 | Q21 nodes already in final DOCX |
| M0698 | Q1 | inserted one value node | official choice key + correct-option chain | final DOCX entry added |
| M0699 | Q2 | excluded | culture-line boundary | no philosophy insertion |
| M0700 | Q3 | inserted two nodes | official choice key + correct-option chain | final DOCX entries added |
| M0701 | Q4 | inserted two nodes | official choice key + correct-option chain | final DOCX entries added |
| M0702 | Q5 | excluded | wrong-option trap | `辩证否定` appears in a wrong option, not the correct chain |
| M0703 | Q6 | excluded | 选必三 logic boundary | no philosophy insertion |
| M0704 | Q7 | excluded | 选必三 innovation-thinking boundary | no philosophy insertion |
| M0705-M0713 | Q8-Q18 boundaries | excluded or already handled | official key / module boundary / existing final body | no unsupported insertion |
| M0714 | Q19 | excluded | logic/economics boundary | no philosophy insertion |
| M0715 | Q20 | excluded from current body | 选必一 mainline; optional philosophy wording weak | no philosophy insertion |
| M0716 | Q21 | already covered | strong scoring standard / detailed scoring | no duplicate insertion |
| M0717 | Qunknown | excluded | extraction residue | no independent row |

## Matrix And Ledger Verification

Updated files:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `05_delivery/docx_insert_ledger.csv`
- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- current DOCX/PDF in `05_delivery/`

Backups:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch03_2026_chaoyang_ermo_20260525_001504.csv`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch03_chaoyang_pending_cleanup_20260525_001834.csv`
- `docx_insert_ledger_backup_before_batch03_chaoyang_ermo_20260525_001504.csv`
- `student_patch_entries.accepted_backup_before_batch03_chaoyang_ermo_20260525_001504.jsonl`
- DOCX backups before Batch03 insertion at `05_delivery/*backup_before_2026_chaoyang_ermo_choice_insert_20260525_001455.docx` and `...001504.docx`

Post-update verification:

- `2026朝阳二模` matrix rows: `32`
- `2026朝阳二模` suite-local pending rows: `0`
- insert ledger rows: `41`
- inserted ledger headings found in DOCX: `41 / 41`
- inserted label paragraphs: `164 / 164` pass bold/color style check

DOCX exact text hits after insertion:

- `2026朝阳二模 第1题`: `1`
- `2026朝阳二模 第3题`: `2`
- `2026朝阳二模 第4题`: `2`
- `2026朝阳二模 第16题`: `4`
- `2026朝阳二模 第21题`: `2`

## Render QA

Rerender command completed successfully through the existing Word COM export script:

`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/tools/export_docx_pdf_and_pages.py`

Render results:

- DOCX size: `350,031` bytes
- PDF size: `3,510,198` bytes
- PDF page count: `236`
- rendered page PNGs: `236`
- contact sheet exists: `07_render_check/word_pdf_pages/contact_every_12_pages.png`
- automated page-image scan: `236` pages checked; only `page_002.png` is near-blank, manually verified as the intended `前言` title page

PDF normalized search pages:

- Q1 inserted entry: page `216`
- Q3 inserted entries: pages `173`, `189-190`
- Q4 inserted entries: pages `61`, `76`
- existing Q16 entries: pages `105`, `120`, `133`, `215`
- existing Q21 entries: pages `74`, `94`

Student-facing residue scan returned `0` hits in DOCX and PDF for:

- `评标`
- `NEED_EVIDENCE`
- `source_lane`
- `correct_option_chain`
- `参考答案`
- `答案写`
- `可从`
- `/Users/`
- `source_repair_basis`
- `2024海淀一模 第17题第（2）问`

Visual samples manually checked after Batch03: contact sheet, pages `2`, `61`, `74`, `76`, `173`, `189`, `190`, and `216`.

## Boundary

This is not final acceptance. It is a Codex production-line batch closure for one suite. ClaudeCode Opus 4.7 max-effort/adaptive-thinking confirmation remains model-gate-blocked unless the runtime exposes sufficient proof. GPTPro web / Claude Opus external full-artifact review remains `real_call_pending`.
