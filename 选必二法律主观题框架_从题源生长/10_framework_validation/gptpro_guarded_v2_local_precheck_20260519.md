# GPTPro Guarded v2 Local Precheck While External Review Runs

Timestamp: 2026-05-19 23:12:51 +0800

Status: local patch applied while GPTPro web review is still running. This is a Codex A local correction, not a captured GPTPro decision.

## Trigger

GPTPro's visible partial text flagged three risks before completion:

1. `CC0276` label/boundary inconsistency.
2. `CC0380` label/core-support inconsistency.
3. possible stale `CC0254` atom references.

Codex A did not click Stop/Retry/Regenerate/Send. Safari still shows GPTPro thinking, so the visible GPT text is not yet treated as a final review.

## Source-Checked Local Decisions

### CC0254

Current canonical `merged_rubric_atoms_subjective.csv` already uses `PATCH_CC0254_R01` through `PATCH_CC0254_R08`, all formal scoring atoms. The old student-problem atoms remain only in superseded backups/pre-guarded files. No current canonical patch required.

Decision: keep current status as formal open-container after source patch; do not promote to a stable core node.

### CC0276

Current framework and baodian already place `CC0276_2026_房山_二模_17` behind `FWV1_2_GATE 边界先判`. It remains a formal boundary-gate pass, not a selected-compulsory-2 core full-score template.

Residual inconsistency: `merged_subjective_law_questions.csv` still records `module_boundary_risk=选必二`, with notes warning about 必修三/涉外法治边界. This does not affect current framework/baodian core evidence, but it should be corrected or annotated in the next canonical merge cleanup.

### CC0380

`CC0380_2026_顺义_二模_18_2` was inconsistent before this patch:

- merged question row: `module_boundary_risk=综合`, note says it only enters the open/综合 boundary container and cannot support a core node alone.
- old framework/baodian: treated it as `CODE_COWORK_007` core support and `core_full_score_supported`.

Applied local patch:

1. Excluded `CC0380_2026_顺义_二模_18_2` and its rubric/material atoms from core `FWV1_2_N06 程序维权三层` evidence.
2. Added it to `FWV1_2_OPEN 开放容器`.
3. Reran guarded v1.2 pressure, framework_v2, baodian sidecars, markdown, docx, and DOCX QA note.

## Updated Counts

- Corpus: 65 question rows.
- Evidence levels: 61 formal, 4 reference_only, 0 missing.
- Pressure: PASS 45, PARTIAL 20, FAIL 0.
- PASS split: 43 core/pass rows + 2 boundary-gate pass rows.
- Baodian labels:
  - core_full_score_supported: 43
  - formal_open_container_partial: 14
  - reference_only_demo: 4
  - boundary_non_core: 2
  - open_container_only: 2

## Updated Files

- `09_candidate_frameworks/framework_v1_2_guarded.md`
- `09_candidate_frameworks/framework_v1_2_evidence_map.csv`
- `10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv`
- `10_framework_validation/framework_v1_2_pass_report_20260519.md`
- `10_framework_validation/framework_v1_2_partial_policy_20260519.csv`
- `10_framework_validation/framework_v1_2_partial_policy_20260519.md`
- `11_final_framework/framework_v2.md`
- `11_final_framework/framework_v2_evidence_map.csv`
- `11_final_framework/framework_v2_teacher_guide.md`
- `11_final_framework/framework_v2_validation_summary.md`
- `12_final_baodian/选必二法律主观题满分宝典.md`
- `12_final_baodian/选必二法律主观题满分宝典.docx`
- `12_final_baodian/question_by_question_framework_runs.csv`
- `12_final_baodian/full_score_sentence_bank.csv`
- `12_final_baodian/material_trigger_bank.csv`
- `12_final_baodian/DOCX_QA_GUARDED_V2.md`

## External Review Handling

The current GPTPro web call was submitted before this local `CC0380` correction. Do not interrupt it. When GPTPro completes, capture the full output, compare it against this local correction, then decide whether a short follow-up/delta needs to be sent.

