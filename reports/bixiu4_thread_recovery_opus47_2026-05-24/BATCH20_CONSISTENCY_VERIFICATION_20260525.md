# Batch20 Consistency Verification - 2026-05-25

Status: `PASS_WITH_MODEL_GATE_BLOCKED`

## Scope

- Batch: `Batch20 - 2024海淀期中`
- Current execution state: `RECOVERED_EXECUTION_IN_PROGRESS`
- Whole-project final acceptance: not claimed.

## Verified Counts

- Matrix total rows: `967`
- `2024海淀期中` matrix rows: `26`
- Removed misplacement matrix rows: `3`
- Removal ledger rows: `3`
- `2024海淀期中` DOCX mentions after removal: `0`
- Global remaining midterm/final source gap: `15`

## Render And Delivery QA

- DOCX bytes: `399828`
- PDF bytes: `4080925`
- Rendered pages: `249/249`
- DOCX/PDF label count: `2311/2311`
- Blank-like pages excluding cover/foreword: `0`
- Visual pages inspected after deletion: `71`, `132`, `197`

## ClaudeCode Evidence

- Evidence id: `OPUS47_BATCH20_HAIDIAN_MIDTERM_RECHECK_001`
- Runtime observed model: `claude-opus-4-7`
- Command lane included `--effort max`
- Thinking block seen: `true`
- Content result: `pass`
- Local policy result: `pass_with_model_gate_blocked`
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`

## Guardrails

- Stale Batch20 pending phrases found in active report scan set: `false`
- Forbidden final-acceptance status token found in active report scan set: `false`
- GPTPro web full-artifact review: `real_call_pending`
- External Claude Opus full-artifact review: `real_call_pending`
