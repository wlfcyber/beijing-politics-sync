# Batch21 Consistency Verification - 2025 Dongcheng Final

Status: `LOCAL_CLOSED_CONTENT_PASS_WITH_MODEL_GATE_BLOCKED`

Updated: 2026-05-25 07:35 +08

## Counts

- Matrix total rows: `992`.
- Batch21 matrix rows: `25`.
- Batch21 body rows: `4`.
- Batch21 boundary rows: `21`.
- Current `docx_insert_ledger.csv` rows: `143`.
- Current `student_patch_entries.accepted.jsonl` rows: `143`.
- Batch21 ledger records: `4`.
- Batch21 accepted records: `4`.
- Current DOCX Batch21 entries: `4`.
- Global remaining midterm/final source-scope gap: `14`.

## Body Placement Check

- Q4: registered existing DOCX coverage under `矛盾就是对立统一`; evidence is objective-answer evidence only.
- Q16: registered existing DOCX coverage under `主观能动性 / 意识的能动作用`; evidence is formal lecture/rubric support.
- Q21: inserted DOCX coverage under `人民群众`; evidence is formal value-orientation rubric support.
- Q21: refreshed existing DOCX coverage under `价值判断与价值选择`; the answer landing now gives a concrete people-interest value-evaluation chain.

## Render Check

- DOCX bytes / PDF bytes: `400390` / `4084179`.
- PDF pages / rendered PNGs: `249/249`.
- Label count DOCX/PDF: `2315/2315`.
- DOCX/rendered-PDF visible suite mentions: `4/4`.
- Raw PDF exact text-extraction suite mentions: `0`, treated as CJK text-extraction limitation rather than a visibility miss.
- Hit pages: `20`, `127`, `216`, `233`.
- Visual inspection opened the hit-page contact sheet plus pages `233` and `234`; no overlap, blank-gap, or obvious style defect was found.

## ClaudeCode Recheck

- Evidence id: `OPUS47_BATCH21_DONGCHENG_FINAL_RECHECK_001`.
- Runtime model evidence: stream events report `claude-opus-4-7`; command flags include `--model claude-opus-4-7 --effort max`; stream includes a thinking block/signature.
- Auxiliary Haiku mention exists in debug/runtime evidence for CLI support work; it is not counted as qualified evidence.
- Content result: `pass`.
- Local policy result: `pass_with_model_gate_blocked`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## Open Gates

- GPTPro web full-artifact review: `real_call_pending`.
- External Claude Opus full-artifact review: `real_call_pending`.
- `14` raw midterm/final suites remain outside the governed coverage system.
- Whole-project final acceptance is not claimed.
