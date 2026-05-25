# Opus 4.7 ClaudeCode Recheck Result - Batch18 2024石景山一模

Updated: 2026-05-25 +08

Lane: ClaudeCode production-lane recheck, normalized by Codex local evidence parsing.

## model_gate

`BLOCKED_MODEL_CONFIRMATION_REQUIRED`

- Runtime stream/message events report `claude-opus-4-7`.
- Command flags requested `--model claude-opus-4-7 --effort max`.
- The stream contains a thinking block/signature.
- Runtime artifacts still do not expose machine-readable proof that max effort/adaptive thinking was active. Therefore this remains blocked under the local hard rule.

## content_result

`pass_with_notes`

Batch18 source/insert/matrix/render decisions are coherent. The notes are the unresolved model gate and the external-review blockers.

## sonnet_haiku_used

`no qualified Sonnet/Haiku evidence counted`

Local runtime evidence shows auxiliary CLI usage for `claude-haiku-4-5-20251001`; it is not counted as qualified ClaudeCode evidence. No Sonnet evidence is counted.

## answer_key_check

`pass`

- Objective answer key: `1C 2B 3D 4A 5C 6A 7B 8B 9C 10A 11D 12D 13B 14C 15C`.
- Q2 enters only from correct item 1: `农业生产实践具有历史性，其形式和水平不断发展`.
- Item 3 remains economy/productive-force background, not a separate philosophy insertion.
- Objective answer-key evidence is labeled as choice-question evidence only, not subjective scoring rules.

## matrix_check

`pass`

- `2024石景山一模` matrix rows: `23`.
- Open-ish suite rows: `0`.
- Q2 inserted under `实践是认识的基础`.
- Q3 retained as existing DOCX coverage under `社会存在与社会意识`.
- Q5 retained as existing DOCX coverage under `根据固有联系建立新的具体联系 / 把握本质和规律`.
- Q16 retained as existing DOCX coverage with teacher-version reference-answer support only; no broad reference-answer angle was promoted to a detailed scoring rule.
- Q19 remains a Logic and Thinking boundary because Q19(3) explicitly requires `《逻辑与思维》` knowledge even though the reference answer mentions `辩证否定观`.

## docx_check

`pass`

Current DOCX XML strip:

- suite mentions: `5`
- Q2: `1`
- Q3: `1`
- Q5: `1`
- Q16: `2`

Ledger and accepted JSONL each contain the new Q2 record under `实践是认识的基础`.

## render_check

`pass`

`word_render_qa_20260525_batch18_word/render_manifest.json` reports:

- Word COM PDF export: `word_com_pdf_export_ok`
- PDF pages / rendered PNGs: `247 / 247`
- DOCX/PDF label counts: `2296 / 2296`
- Q2 PDF page: `182`
- page 2 blank-like flag is the intentional `前言` divider, visually confirmed.

Page `182` was visually inspected and the Batch18 Q2 entry renders cleanly with heading, green bold labels, body text, and page number.

## required_fixes

No DOCX, ledger, accepted JSONL, matrix, or render-content fixes required.

Required bookkeeping:

- append Batch18 to `FORMAT_RENDER_QA_20260524.md`;
- append Batch18 to `GOVERNOR_RECOVERY_REPORT_20260524.md`;
- append Batch18 to `CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`;
- append Batch18 runtime evidence to `MODEL_EVIDENCE_LEDGER.md`.

External GPTPro web and external Claude Opus full-artifact reviews remain `real_call_pending`.
