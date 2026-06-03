# Codebook Expansion After Cowork + Codex Source Check Input Packet

- generated_at: 2026-05-19T18:56:19+08:00
- purpose: Ask real GPT-5.5 Pro and real Claude Opus 4.7 Adaptive to independently adjudicate codebook expansion candidates only.
- current corpus: 65 core subjective law questions; evidence levels {'formal': 61, 'reference_only': 4}; missing 0.
- current pressure test: {'PASS': 16, 'PARTIAL': 49}; PASS rows are already closed by the 7-row codebook, PARTIAL rows need expansion or open-container quarantine.
- current provisional codebook rows: 7
- Cowork completion rows: 65
- Cowork expansion candidate rows: 10
- Codex source-check rows: 5 blocked rows, corrected atom plan rows 28

## Hard Gates

1. This packet is not for final framework or handbook writing.
2. Do not output a final framework, framework v2, student mnemonic, or baodian section.
3. Accept/revise/reject only evidence-backed codebook expansion observations.
4. Every accepted observation must cite question_id, rubric_atom_id or corrected proposed_rubric_atom_id, material_atom_id, and evidence level.
5. Reference-only rows cannot support core codes.
6. CC0254 current rubric atoms R01-R08 must not be used as scoring support; use `codex_source_check_corrected_rubric_atom_plan.csv` instead.
7. RECOVER_2026_房山_一模_17_1 alternative 2-point dimensions must not be treated as cumulative scoring atoms.
8. CC0061 must not be treated as one unified mechanism unless split/trim is explicitly handled.

## Files

- merged corpus: `merged_subjective_law_questions.csv`, `merged_material_atoms_subjective.csv`, `merged_ask_atoms_subjective.csv`, `merged_rubric_atoms_subjective.csv`
- current codebook: `provisional_codebook_v0.csv`, `provisional_codebook_v0.md`, `codebook_source_evidence_map.csv`, `codebook_risks.md`
- current framework/pressure test context: `framework_v1.md`, `framework_v1_evidence_map.csv`, `framework_v1_question_by_question_test.csv`, `framework_v1_partial_cluster_source_check.*`, `framework_v1_pass_report.md`
- previous model comparison: `gpt_claude_observation_comparison.*`, `observations_needing_source_check.csv`
- Cowork review: `claude_cowork_all_question_completion_report.md`, `claude_cowork_all65_completion_table.csv`, `claude_cowork_codebook_expansion_candidates.csv`, `claude_cowork_source_check_needed.csv`, `claude_cowork_transfer_only_or_open_container.csv`, `claude_cowork_source_check_questions.csv`
- Codex source check: `codex_source_check_five_blocked_rows.*`, `codex_source_check_corrected_rubric_atom_plan.csv`

## Missing From Packet

- none
