# Claude Cowork All-Question Completion Input Packet

## Current Baseline

- Project: 选必二《法律与生活》主观题框架从题源生长工程
- Current corpus: 65 core subjective law questions
- Evidence levels: 61 formal, 4 reference_only, 0 missing
- Current provisional codebook: 7 rows
- Current framework_v1 direct closure: PASS 16 / PARTIAL 49 / FAIL 0
- Formal rows still requiring source-check/codebook expansion: 45
- Reference-only non-core rows: 4, may not support core codebook nodes

## Why This Packet Exists

The current `framework_v1` is intentionally conservative. It can start many questions, but only 16 questions are directly closed by the current codebook. This packet asks Claude Cowork to help complete the all-question evidence review before any final framework or handbook regeneration.

This is not a final-framework task. It is a source-check and codebook-expansion task.

## Files In This Folder

- `merged_subjective_law_questions.csv`: 65-question current canonical corpus.
- `merged_material_atoms_subjective.csv`: material atoms for the 65 questions.
- `merged_ask_atoms_subjective.csv`: ask atoms for the 65 questions.
- `merged_rubric_atoms_subjective.csv`: rubric/answer atoms for the 65 questions.
- `provisional_codebook_v0.csv`: current 7-row codebook.
- `provisional_codebook_v0.md`: readable codebook.
- `framework_v1.md`: conservative v1 framework, not final.
- `framework_v1_evidence_map.csv`: v1 node evidence map.
- `framework_v1_question_by_question_test.csv`: all-65 pressure test.
- `framework_v1_partial_cluster_source_check.csv`: 45 formal PARTIAL rows grouped for source-check.
- `framework_v1_partial_cluster_source_check.md`: short cluster report.
- `gpt_claude_observation_comparison.csv`: current cross-validation comparison.
- `observations_needing_source_check.csv`: pending observations, if present.

## Hard Rules For This Packet

1. Do not output a final framework.
2. Do not output a handbook or student-facing final draft.
3. Do not analyze choice questions.
4. Do not promote reference_only evidence into formal evidence.
5. Do not create a codebook observation unless it has `question_id`, `rubric_atom_id`, and `material_atom_id`.
6. Do not use textbook目录, law-school doctrine, or pretty labels as the source of a code.
7. Do not turn the answer into broad 必修三法治话语.
8. Do not turn the answer into overly complex law-exam analysis.
9. If a row remains only transfer/open-container, say so instead of forcing a code.
10. Every promoted observation must explain how it helps a student start the answer and generate a scoring sentence.

## Expected Output

Please return:

1. A per-question completion table for all 65 rows.
2. Codebook expansion candidates for the 45 formal PARTIAL rows.
3. Existing-code revisions, if evidence supports them.
4. Transfer-only/open-container rows that should not be promoted.
5. Rows needing source recheck.
6. Rows that must remain outside core because they are reference_only.
7. A concise recommendation on whether `framework_v1` can become `framework_v2` after the proposed codebook expansion, without writing framework_v2.
