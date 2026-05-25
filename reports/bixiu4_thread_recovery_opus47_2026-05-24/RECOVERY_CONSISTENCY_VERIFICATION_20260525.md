# Recovery Consistency Verification - 2026-05-25

Status: `PASS_WITH_MODEL_GATE_BLOCKED`

## Scope

- Recovery thread: `bixiu4_thread_recovery_opus47_2026-05-24`
- Latest processed batch: `Batch19 - 2024朝阳期中`
- Current execution state: `RECOVERED_EXECUTION_IN_PROGRESS`
- Forbidden final state: not claimed.

## Verified Counts

- Matrix total rows: `941`
- `2024朝阳期中` matrix rows: `28`
- `2024朝阳期中` open-ish matrix rows: `0`
- Question distribution: `Q1=1`, `Q2=1`, `Q3=1`, `Q4=2`, `Q5=1`, `Q6=1`, `Q7=1`, `Q8=1`, `Q9=1`, `Q10=1`, `Q11=1`, `Q12=1`, `Q13=1`, `Q14=1`, `Q15=1`, `Q16=4`, `Q17=5`, `Q18=1`, `Q19=1`, `Q20=1`.
- `docx_insert_ledger.csv` total rows: `139`; `2024朝阳期中` rows: `15`.
- `student_patch_entries.accepted.jsonl` total rows: `139`; `2024朝阳期中` rows: `15`.

## Render And Delivery QA

- DOCX bytes: `400952`
- PDF bytes: `4090938`
- Rendered pages: `250/250`
- Actual `page_*.png` files: `250`
- DOCX/PDF label count: `2316/2316`
- `2024朝阳期中` suite headings located in rendered PDF pages: `28`, `32`, `82`, `101`, `107`, `114`, `120`, `136`, `192`, `199`, `203`, `205`, `212`, `236`, `249`.

## Model Evidence Gate

- ClaudeCode runtime observed model: `claude-opus-4-7`
- Command lane evidence includes `--effort max` and a thinking block.
- Debug stream also mentions auxiliary `claude-haiku-4-5-20251001`; this is not counted as qualified evidence.
- Local policy result: `pass_with_model_gate_blocked`
- Model gate remains: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`

## Global Scope

- Raw suite audit rows: `64`
- Current remaining raw-suite scope gap rows: `16`
- `2024朝阳期中` global audit status: `covered_by_batch19_recovery_matrix`
- External GPTPro web full-artifact review: `real_call_pending`
- External Claude Opus full-artifact review: `real_call_pending`

## Guardrail Scan

- Forbidden final-acceptance status token found in active recovery report scan set: `false`
- Stale Batch19 pending phrases found in active recovery report scan set: `false`
- `real_call_pending` remains present in external-review-bearing reports.
- `BLOCKED_MODEL_CONFIRMATION_REQUIRED` remains present in model-evidence-bearing reports.
