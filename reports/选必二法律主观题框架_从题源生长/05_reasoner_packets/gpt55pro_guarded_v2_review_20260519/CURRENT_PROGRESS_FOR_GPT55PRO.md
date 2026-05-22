# REPORT TO GPT-5.5 PRO - Guarded v2 Progress Review

You are GPT-5.5 Pro in the `选必二《法律与生活》主观题框架从题源生长工程`.

This is a progress/review packet, not a request to invent a new framework from memory. Please review only the attached/current evidence artifacts and tell Codex what is acceptable, what must be patched, and what must remain non-core.

## Current Verified Progress

- Current canonical corpus: 65 subjective-law question rows.
- Evidence levels: formal 61, reference_only 4, missing 0.
- Current rubric atoms: 370 after CC0143 scoring-only patch.
- Guarded v1.2 pressure result: PASS 46, PARTIAL 19, FAIL 0.
- PASS interpretation: 44 core full-score supported rows + 2 boundary-gate pass rows. Boundary-gate pass is not a selected-compulsory-2 full-score template.
- PARTIAL interpretation: 19 non-core rows = formal/open or reference-only demos; they cannot support new framework core nodes without repeated formal evidence and cross-validation.
- Current baodian labels: {'core_full_score_supported': 44, 'formal_open_container_partial': 14, 'reference_only_demo': 4, 'boundary_non_core': 2, 'open_container_only': 1}.
- DOCX status: structurally valid and first-page Quick Look preview passes, but full Word/PDF page-by-page visual QA is not closed for guarded v2.

## What Changed Since Earlier Versions

1. The earlier 35-question and later 53/56/66-row packages are superseded.
2. ClaudeCode VS Code audit and Claude Cowork checks forced a 65-question canonical corpus: 61 formal, 4 reference_only, 0 missing.
3. CC0143 was patched into the consumer-contract/fraud-compensation code with scoring-only atoms. Teaching-reflection-only atoms were demoted as non-core support.
4. CC0276 and `RECOVER_2026_西城_二模_18_3` are boundary exclusions, not core 选必二 framework evidence.
5. `RECOVER_2026_西城_二模_18_2` is open-container-only, not a core template.
6. `framework_v2` is a guarded teaching framework: teachable core path exists, but the handbook must preserve core/open/reference/boundary labels and cannot advertise all 65 as full-score core closure.

## Attached Inputs

The packet directory contains copied current artifacts under `files/`, including:

- 04_merge_audit/merged_subjective_law_questions.csv
- 04_merge_audit/merged_material_atoms_subjective.csv
- 04_merge_audit/merged_ask_atoms_subjective.csv
- 04_merge_audit/merged_rubric_atoms_subjective.csv
- 08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.csv
- 08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.md
- 08_codebook/codebook_v1_2_after_fail4_cowork_source_evidence_map_20260519.csv
- 08_codebook/codebook_v1_2_after_fail4_cowork_risks_20260519.md
- 09_candidate_frameworks/framework_v1_2_guarded.md
- 09_candidate_frameworks/framework_v1_2_evidence_map.csv
- 10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv
- 10_framework_validation/framework_v1_2_pass_report_20260519.md
- 10_framework_validation/framework_v1_2_partial_policy_20260519.csv
- 10_framework_validation/framework_v1_2_partial_policy_20260519.md
- 11_final_framework/framework_v2.md
- 11_final_framework/framework_v2_evidence_map.csv
- 11_final_framework/framework_v2_student_one_page.md
- 11_final_framework/framework_v2_teacher_guide.md
- 11_final_framework/framework_v2_validation_summary.md
- 12_final_baodian/选必二法律主观题满分宝典.md
- 12_final_baodian/question_by_question_framework_runs.csv
- 12_final_baodian/full_score_sentence_bank.csv
- 12_final_baodian/material_trigger_bank.csv
- 12_final_baodian/common_failure_paths.md
- 12_final_baodian/DOCX_QA_GUARDED_V2.md
- 10_framework_validation/fail4_source_adjudication_20260519/claude_cowork_output/fail4_targeted_adjudication_claude_cowork_20260519.md
- 10_framework_validation/fail4_source_adjudication_20260519/fail4_external_cross_check_20260519.md

Missing expected artifacts:

- none

## Review Tasks

Please output a structured review with these sections:

1. `ACCEPTABLE_PROGRESS`
   - State whether the 65-question corpus and guarded v2 can be treated as the current factual baseline.
   - State whether the 44 core + 2 boundary + 19 partial policy is evidence-safe.

2. `BLOCKERS_BEFORE_FINAL_CLAIM`
   - List anything that prevents Codex from claiming final full closure.
   - Include DOCX visual QA if you agree it remains a blocker.

3. `ROW_LEVEL_PATCH_TABLE`
   - TSV columns: `question_id`, `current_label`, `decision`, `required_patch`, `evidence_needed`, `severity`.
   - Only include rows that need change, source check, promotion, demotion, or stronger warning.

4. `FRAMEWORK_PATCH_TABLE`
   - TSV columns: `node_id_or_file`, `issue`, `required_patch`, `why`, `severity`.

5. `BAODIAN_PATCH_TABLE`
   - TSV columns: `section_or_file`, `issue`, `required_patch`, `why`, `severity`.

6. `CAN_CONTINUE_TO_NEXT_STEP`
   - Choose one: `YES_WITH_GUARDS`, `NO_BLOCKED`, or `ONLY_LOCAL_POLISH`.
   - Explain exactly what Codex should do next.

## Hard Rules

- Do not promote reference_only evidence into formal support.
- Do not turn open-container rows into core nodes without repeated formal support and explicit question/rubric/material IDs.
- Do not法考化, do not必修三化, do not make a textbook-directory framework.
- If a claim lacks question_id and rubric_atom_id support, mark it `reject_or_pending`.
- Keep the two-layer structure: high-frequency core trunk + open/boundary/reference containers.
