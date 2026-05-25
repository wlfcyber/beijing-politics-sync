# OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_PROMPT

You are ClaudeCode production lane for the 必修四政治庄园 recovery package.

## Hard Model Gate

You must verify your runtime model and reasoning setting before giving any content pass.

Required:

- model: `claude-opus-4-7`
- effort / reasoning: max effort or adaptive thinking equivalent

If you cannot prove both from the runtime/debug/JSON evidence visible to you, write:

`Status: BLOCKED_MODEL_CONFIRMATION_REQUIRED`

and do not claim PASS.

Do not use Sonnet, Haiku, model unknown, or inherited Sonnet outputs as qualified evidence.

## Current Task

Independently recheck Codex source-recitation batch:

`reports/bixiu4_thread_recovery_opus47_2026-05-24/ROW_SOURCE_RECITATION_BATCH01_20260524.md`

You must inspect the current files, not rely on the summary alone:

- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/04_fusion_audit/student_patch_entries.accepted.jsonl`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/docx_insert_ledger.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2025海淀一模.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026海淀二模_Q16_readable_evidence.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026通州一模.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/2026石景山二模.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/STYLE_CONSISTENCY_FIX_20260524.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/FORMAT_RENDER_QA_20260524.md`

## Rows To Recheck

Accepted JSONL rows:

- 21, 22: `2025海淀一模 Q22`
- 23, 24: `2026通州一模 Q18`
- 25, 26: `2026海淀二模 Q16`
- 34, 35, 36: `2026石景山二模 Q17(3)`

For each row, verify:

1. The current accepted JSONL row exists and matches the described question/framework node.
2. The claimed principle/method is explicitly supported by the cited scoring/rubric/lecture-scoring source.
3. The row is placed under the correct framework node.
4. The student-facing trigger and answer landing are tied to the material, not generic template prose.
5. `2026海淀二模 Q16` is not upgraded beyond `讲评细则 / optional angle`.
6. `2026石景山二模 Q17(3)` rows are optional paths, not three cumulative points.
7. Row 35 no longer contains the off-question 隆福寺-style examples in the material trigger.

## Required Output

Write:

`reports/bixiu4_thread_recovery_opus47_2026-05-24/OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_RESULT.md`

Required sections:

- Model Gate
- Files Inspected
- Row-by-Row Findings
- Any Corrections Required
- Decision

Decision must be one of:

- `blocked_model_confirmation_required`
- `pass_with_model_gate_blocked`
- `needs_correction`

If model/effort proof is blocked, use `blocked_model_confirmation_required` or `pass_with_model_gate_blocked`; do not write a qualified PASS.
