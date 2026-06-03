# REASONER INPUT PACKET - Cowork Refined

## Gate

Packet verdict before reasoner: **PASS**.

This packet supersedes `reasoner_packet_suite_exhaustive_claudecode_corrected_20260519.zip` because Claude Cowork E found question-layer blockers in that packet.

## Data Scope

- Subjective questions only.
- Core question count: 65.
- evidence_level: formal 61, reference_only 4, missing 0.
- No core midterm entries remain; midterm no-law/boundary suites are retained only in exhaustion matrix and boundary files.

## Patch Context

The attached `cowork_patch_apply_audit.md` must be treated as part of the input. It records repairs to empty asks, material/rubric leakage, answer-as-material rows, and logic-module leakage.

## Reasoner Guardrails

- Do not use reference_only rows to support a core framework node by themselves.
- Do not infer from choice questions.
- Do not treat reference answers as formal scoring rubrics.
- Every observation must cite question_id, rubric_atom_id, and material_atom_id.
- The `related_material_atom_ids` field uses `|` as its delimiter.

## Files

- `merged_subjective_law_questions_for_reasoners_cowork_refined.csv`
- `merged_material_atoms_subjective_for_reasoners_cowork_refined.csv`
- `merged_ask_atoms_subjective_for_reasoners_cowork_refined.csv`
- `merged_rubric_atoms_subjective_for_reasoners_cowork_refined.csv`
- `suite_exhaustion_report_for_reasoners_cowork_refined.md`
- `cowork_patch_apply_audit.md`
- `codex_independent_validation_after_cowork_patch_20260519.md`
- `no_core_suite_review_20260519.md`
