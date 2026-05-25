# COVERAGE_FUSION_BATCH05_2026_CHAOYANG_YIMO_CODEX_20260525

Status: `CODEX_BATCH05_DONE__CLAUDECODE_RECHECK_CORRECTION_APPLIED__MODEL_GATE_BLOCKED`

Timestamp: 2026-05-25 01:12 +08

## Scope

Batch05 covers `2026朝阳一模` inside `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.

Rows closed this round:

- existing boundary/base rows: `M0053` through `M0057`
- cross-lane candidate rows: `M0162`, `M0223`, `M0224`
- Codex A suite rows: `M0571` through `M0591`
- suite-level mirror row: `M0843`

Result: all `2026朝阳一模` rows now have explicit inserted / already-covered / excluded / residue dispositions. Suite-local loose pending rows: `0`.

Global recovery matrix after Batch05:

- exact production-line candidate rows still open: `464`
- rows still marked as needing source/fusion adjudication: `464`

## Source Authority Used

Primary source bundle:

`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026朝阳一模.md`

Key source positions:

- lines 25-36: Q1 stem/options. Official key lines 365-400 give Q1=`B`, so ①④ are correct.
- lines 37-44: Q2 stem/options. Official key gives Q2=`A`.
- lines 45-55: Q3 stem/options. Official key gives Q3=`D`, so ②④ are correct.
- lines 71-146: Q5-Q15 selection questions; official key lines 365-400 fixes their answer-key boundaries.
- lines 227-234 and 403-428: Q16 prompt and teacher-version reference answer.
- lines 586-595: formal Q16 marking rule. Required angles: `尊重客观规律与发挥主观能动性的辩证关系` and culture/cultural confidence; optional angle bucket: `认识论/实践与认识、联系观/系统优化、对立统一` plus culture, capped at 3 points.
- lines 601-636: Q17 formal marking rules; Q17(1) is logic/thinking, Q17(2) is politics-and-law.
- lines 637-647: Q18 law marking rules.
- lines 648-665: Q19 economics marking rules.
- lines 666-682: Q20 international politics/economy marking rules.
- lines 683-696: Q21 comprehensive marking rules; explicitly allows social existence/social consciousness, superstructure/economic base, people-centered implementation, and comprehensive module use.

## DOCX Changes

New final-body entries inserted:

| node | heading | basis |
|---|---|---|
| 一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一 | `18. 2026朝阳一模 第1题（选择题）` | Q1 official key B; option ① directly says `从边区的实际出发` |
| 实践与认识（总） | `29. 2026朝阳一模 第1题（选择题）` | Q1 official key B; option ④ and stem stress `实干` / `拼出来、干出来` / `务实` |
| 价值观的导向作用 | `29. 2026朝阳一模 第2题（选择题）` | Q2 official key A; option A says 古澹克制功利冲动, showing value guidance |
| 辩证否定 / 守正创新 | `21. 2026朝阳一模 第3题（选择题）` | Q3 official key D; option ④ directly says 辩证否定 makes traditional culture shine through technology empowerment |

No insertion was made for:

- Q3 option ②: culture/cultural-confidence line, not current philosophy mainline.
- Q4: culture/international cultural exchange.
- Q5-Q7: logic/thinking module.
- Q8-Q9: politics-and-law.
- Q10-Q11 and Q18: law.
- Q12-Q14 and Q19: economics.
- Q15 and Q20: contemporary international politics/economy.
- Q17: Q17(1) logic/thinking and Q17(2) politics-and-law; no source Q17(3) philosophy subquestion exists.

Q16 and Q21 were not reinserted because the current DOCX already contains supported final-body entries:

- Q16 DOCX hits: `6`.
- Q21 DOCX hits: `3`.

## Evidence Label Corrections

The Q16 matrix and blocked JSONL metadata were refined to avoid overclaiming:

- Q16 `尊重客观规律与发挥主观能动性相结合`: `正式阅卷细则必答角度`.
- Q16 `系统观念 / 系统优化`: `正式阅卷细则选答角度`.
- Q16 `实践是认识的基础`: `正式阅卷细则选答角度`.
- Q16 `矛盾的普遍性和特殊性`: `教师版参考答案+正式阅卷细则宽角度`; not a strict point-by-point strong rubric claim.
- Q16 culture/cultural confidence remains culture-line boundary, not philosophy-mainline insertion.

## Matrix And Ledger Verification

Updated files:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `05_delivery/docx_insert_ledger.csv`
- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- `04_fusion_audit/student_patch_entries.blocked.jsonl`
- current DOCX/PDF in `05_delivery/`

Backups:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch05_2026_chaoyang_yimo_20260525_010451.csv`
- `docx_insert_ledger_backup_before_batch05_chaoyang_yimo_20260525_010451.csv`
- `student_patch_entries.accepted_backup_before_batch05_chaoyang_yimo_20260525_010451.jsonl`
- `student_patch_entries.blocked_backup_before_batch05_chaoyang_yimo_20260525_010451.jsonl`
- DOCX backups before content insertion and all-label style normalization.

Post-update verification:

- `2026朝阳一模` matrix rows: `32`
- `2026朝阳一模` loose pending rows: `0`
- global active candidate rows: `464`
- insert ledger rows: `51`
- inserted ledger headings found in DOCX: `51 / 51`
- accepted JSONL Batch05 new entries: `4`

DOCX exact text hits after insertion:

- `2026朝阳一模 第1题`: `2`
- `2026朝阳一模 第2题`: `1`
- `2026朝阳一模 第3题`: `1`
- `2026朝阳一模 第16题`: `6`
- `2026朝阳一模 第21题`: `3`

## Render QA

Render command completed successfully through:

`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/tools/export_docx_pdf_and_pages.py`

Render results after all-label style normalization:

- DOCX size: `349,550` bytes
- PDF size: `3,856,219` bytes
- PDF page count: `232`
- rendered page PNGs: `232`
- contact sheet exists: `07_render_check/word_pdf_pages/contact_every_12_pages.png`
- all rendered pages are `993 x 1404 px`
- near-blank page scan: only `page_002.png`, the intended foreword page
- full-document label style check: `2148 / 2148` label paragraphs pass
- student-facing residue scan: `0` hits in DOCX/PDF for the current banlist

PDF normalized search pages:

- Q1 inserted entries: pages `15`, `159`
- Q2 inserted entry: page `213`
- Q3 inserted entry: page `104`
- Q16 existing entries: pages `29`, `42`, `67`, `134`, `164`, `171`
- Q21 existing entries: pages `183`, `188`, `195`

Visual samples manually checked after Batch05: pages `15`, `104`, `159`, and `213`.

## Boundary

This is not final acceptance. It is a Codex production-line batch closure for one suite. ClaudeCode Opus 4.7 max-effort/adaptive-thinking confirmation remains model-gate-blocked unless the runtime exposes sufficient proof. GPTPro web / Claude Opus external full-artifact review remains `real_call_pending`.


## ClaudeCode Recheck Amendment

ClaudeCode Opus 4.7 Batch05 recheck returned `pass_with_corrections_model_gate_blocked`.

Correction applied after recheck:

- Added `M0861` for `2026朝阳一模 Q7`: official answer C; classified as `选必三逻辑与思维边界`; no DOCX insertion.
- Patched `M0591` remark: original Codex-A export skipped Q7, so the suite closure statement now points to `M0861` instead of overclaiming direct Q1-Q21 row coverage.
- Post-correction `2026朝阳一模` suite rows: `32`; loose pending rows: `0`.

Model boundary: this was a real ClaudeCode review call with `claude-opus-4-7` runtime evidence, but strict max-effort/adaptive-thinking proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
