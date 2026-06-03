# v8 Student Usable Rebuild Packet

This packet is for GPT-5.5 Pro and Claude Opus 4.7 to review the same locked corpus and the same v7.1 failure diagnosis.

Hard baseline:

- Canonical corpus: `boundary_patched_20260519`
- Closed framework-ready questions: 53
- Material atoms: 535
- Ask atoms: 53
- Rubric atoms: 319
- Status: 37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE

Do not expand to 65 or 70 candidates.
Do not bring pending cases back into the closed body.
Do not let OPEN_OR_REFERENCE independently support a core framework node.

Pending cases excluded from the closed body:

- `CC0094_2025_东城_期末_19_3`
- `CC0259_2026_丰台_期中_19`
- `CC0118_2025_丰台_期末_18_2`

Removed:

- `CC0250_2026_丰台_一模_19`

Still-forbidden CC0229 bad terms:

- `逃逸粒子`
- `创新资源集聚`
- `空间布局精准`
- `全链条产业生态`

Main files:

- `01_v7_failure_diagnosis.md`
- `01_v7_failure_diagnosis.csv`
- `merged_subjective_law_questions_boundary_patched.csv`
- `merged_material_atoms_subjective_boundary_patched.csv`
- `merged_ask_atoms_subjective_boundary_patched.csv`
- `merged_rubric_atoms_subjective_boundary_patched.csv`
- `question_by_question_framework_runs_boundary_patched.csv`
- `material_trigger_bank_boundary_patched.csv`
- `full_score_sentence_bank.csv`
- `QUESTION_COVERAGE_MATRIX.csv`
- `v71_current_baodian_core.md`
- `v71_pressure_patch_candidate.md`

Task:

Use `00_SHARED_PROMPT_FOR_GPT_AND_CLAUDE.md`. The task is diagnosis and gold-sample recommendation only. It is not a free framework invention task.
