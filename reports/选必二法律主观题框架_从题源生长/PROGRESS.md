# PROGRESS

| Step | Status | Artifact | Notes |
| --- | --- | --- | --- |
| STEP_00_GATE | completed | TASK_BRIEF.md, DEVELOPMENT_PLAN.md, PROGRESS.md, governor_board.md, DECISIONS.md, RISKS.md, TODO.md | Three-layer SOP read; new run registered locally. |
| STEP_01_SOURCE_MANIFEST | completed | 00_manifest/source_manifest.csv | 403 source files; 51 failed/OCR-gap rows. |
| STEP_02_CODEX_CANDIDATES | completed | 01_subjective_candidates/all_candidate_subjective_law_questions_codex.csv | Codex heuristic extraction: 103 candidates; requires audit. |
| STEP_03_CODEX_ATOMS | completed | 02_material_atoms, 03_rubric_atoms | Codex heuristic atoms written. |
| STEP_04_CLAUDECODE_HANDOFF | completed | 04_merge_audit/claudecode_independent_audit_report.md | Real Claude Code B call completed; CONDITIONAL_PASS. |
| STEP_05_MERGE_AUDIT | completed | 04_merge_audit/merge_audit_report.md | Merged canonical set: 74 candidates. |
| STEP_06_REASONER_PACKET | corrected | 05_reasoner_packets/reasoner_packet_v2_full_context_20260519.zip | First 35-question formal-core packet reclassified as trial; official v2 packet contains 74 merged questions, 57 observation-eligible, 17 missing-context-only. |
| STEP_06A_MISSING_17_REVIEW | completed | 04_merge_audit/missing_evidence_17_review.csv; 04_merge_audit/missing_evidence_17_review.md | User flagged missing count; review found no midterm rows, 11 upgrade_formal, 2 upgrade_reference_only, 4 delete_false_positive after conservative source check. |
| STEP_06B_REBUILD_PACKET_V3 | completed | 05_reasoner_packets/reasoner_packet_v3_corrected_missing17_20260519.zip | Corrected packet: 70 merged subjective candidates, 65 formal, 5 reference_only, missing 0, 504 rubric/answer atoms. |
| STEP_07_OPEN_OBSERVATION | completed | 06_open_observations/gpt55pro_open_observations.md; 06_open_observations/claude_opus_open_observations.md | Official GPT-5.5 Pro and Claude Opus 4.7 Adaptive v3 outputs both captured from reasoner_packet_v3_corrected_missing17_20260519.zip. GPT parsed 32 observations; Claude parsed 29 observations. |
| STEP_08_CROSS_VALIDATION | completed | 07_cross_validation/gpt_claude_observation_comparison.md; 07_cross_validation/strong_shared_observations.csv | 51 comparison rows; 17 strong shared observations; 18 pending/source-check rows; weak/reference/conflict observations not promoted. |
| STEP_09_CODEBOOK | completed | 08_codebook/provisional_codebook_v0.md; 08_codebook/provisional_codebook_v0.csv; 08_codebook/codebook_source_evidence_map.csv; 08_codebook/codebook_risks.md | 10 provisional codes generated from cross-validated observations; risky mixed IDs removed from supporting evidence fields. |
| STEP_10_CANDIDATE_FRAMEWORKS | completed | 09_candidate_frameworks/gpt55pro_candidate_frameworks.md; 09_candidate_frameworks/claude_opus_candidate_frameworks.md | Real GPT-5.5 Pro and Claude Opus 4.7 Adaptive candidate-framework outputs captured from the unified packet. |
| STEP_11_FRAMEWORK_V1 | completed | 09_candidate_frameworks/candidate_framework_comparison.md; 09_candidate_frameworks/framework_synthesis_plan.md; 09_candidate_frameworks/framework_v1.md; 09_candidate_frameworks/framework_v1_evidence_map.csv | Synthesized six-step v1 from GPT closed-loop proposal and Claude six-step action-chain proposal. |
| STEP_12_PRESSURE_TEST | completed | 10_framework_validation/framework_v1_question_by_question_test.csv; 10_framework_validation/framework_v1_pass_report.md | 70-question pressure test: PASS 37, PARTIAL 13, FAIL 20. |
| STEP_13_FRAMEWORK_V2 | completed | 11_final_framework/framework_v2.md; 11_final_framework/framework_v2_student_one_page.md; 11_final_framework/framework_v2_teacher_guide.md; 11_final_framework/framework_v2_validation_summary.md | v2 keeps high-frequency trunk and adds entrance gate plus open-container/boundary layer. |
| STEP_14_FINAL_BAODIAN | completed | 12_final_baodian/选必二法律主观题满分宝典.md; 12_final_baodian/选必二法律主观题满分宝典.docx; 12_final_baodian/question_by_question_framework_runs.csv | Final handbook generated; DOCX structurally validated, visual render skipped because soffice is unavailable. |
| STEP_15_BOUNDARY_RECOVERY | completed | 10_framework_validation/gpt55pro_boundary_recovery_review.md; 10_framework_validation/framework_v2_boundary_recovery_delta_after_gpt.csv; 10_framework_validation/atom_mapping_patch_queue.csv; 10_framework_validation/boundary_recovery_after_gpt_report.md | User challenged low PASS count. GPT-5.5 Pro review captured. Corrected count policy: v1 PASS 37 is only strict test status; current strict closed core is 48 after CC0229 rubric_atom patch; current core+open/weak container is 53. Final release remains blocked on section regeneration and other split/reextract rows. CC0094 moved from open to split/deduplicate; CC0250 removed; original v2/baodian downgraded to provisional pending atom patches. |
| STEP_16_ATOM_PATCH_QUEUE | completed | 10_framework_validation/cc0229_rubric_atom_patch.csv; 10_framework_validation/split_question_patch_records.csv; 10_framework_validation/split_material_atoms_patch.csv; 10_framework_validation/split_ask_atoms_patch.csv; 10_framework_validation/split_rubric_atoms_patch.csv | CC0229 misbound rubric atoms fixed and baodian section regenerated. Split patch records created for CC0305_18_3, CC0373_18, CC0380_18_2. Remaining blockers: integrate patch records into canonical merged files, remove CC0250/CC0094 bad final sections, and regenerate final baodian/docx. |
| STEP_17_BOUNDARY_PATCHED_DOC | completed | 12_final_baodian/选必二法律主观题满分宝典.md; 12_final_baodian/选必二法律主观题满分宝典_BOUNDARY_PATCHED.docx; 12_final_baodian/DOCX_QA_BOUNDARY_PATCHED.md | Markdown has patched sections for CC0094, CC0229, CC0250, CC0305_18_3, CC0373_18, CC0380_18_2. Boundary-patched DOCX generated and structurally validated; visual render skipped because soffice is unavailable. |
| STEP_18_SIDECAR_PATCH | completed | 12_final_baodian/question_by_question_framework_runs.csv; 12_final_baodian/material_trigger_bank.csv; 12_final_baodian/common_failure_paths.md | Sidecars patched for CC0094, CC0229, CC0250, CC0305_18_3, CC0373_18, CC0380_18_2. Backups saved with `.pre_boundary_patch_20260519.csv`. |
| STEP_19_CANONICAL_INTEGRATION | completed | 04_merge_audit/boundary_patched_20260519/*; 04_merge_audit/boundary_patched_canonical_corpus_20260519.zip | Generated a clean boundary-patched canonical corpus: 53 framework-ready question rows, 535 material atoms, 53 ask atoms, 319 rubric atoms. Removed 20 excluded/parent/pending original IDs and added 3 split legal question IDs. CC0229 question-layer answer/rubric text also cleaned from corrected F0153/F0146 atoms. |
| STEP_20_BOUNDARY_SIDECARS_REGEN | completed | 12_final_baodian/question_by_question_framework_runs_boundary_patched.csv; 12_final_baodian/material_trigger_bank_boundary_patched.csv; 12_final_baodian/full_score_sentence_bank.csv; 12_final_baodian/full_score_sentence_bank_boundary_patched.csv | Regenerated 53-row boundary-patched sidecars and sentence bank. Status counts now align: PASS 37, PASS_RECOVERED 11, OPEN_OR_REFERENCE 5. Old sentence bank backed up as full_score_sentence_bank.pre_boundary_canonical_regen_20260519.csv. |
| STEP_21_WORD_PDF_QA | completed | 12_final_baodian/DOCX_QA_WORD_PDF_RENDER.md; 12_final_baodian/选必二法律主观题满分宝典.docx; 12_final_baodian/选必二法律主观题满分宝典_BOUNDARY_PATCHED_WORDSAVED.pdf | Microsoft Word opened/saved the boundary-patched DOCX, exported PDF, and PyMuPDF rendered 198 pages with no suspect blank pages. Word-saved DOCX promoted to canonical filename; old canonical DOCX backed up. |
| STEP_22_FINAL_ACCEPTANCE_REPORT | completed | FINAL_ACCEPTANCE_REPORT_BOUNDARY_PATCHED.md; FINAL_DELIVERY_REPORT.md | Boundary-patched release candidate accepted for the 53-row patched corpus, with explicit non-claims for CC0094, CC0259, and CC0118. |
| STEP_23_COVERAGE_MATRIX | completed | QUESTION_COVERAGE_MATRIX.csv; QUESTION_COVERAGE_MATRIX_SUMMARY.md | Added 53-row coverage matrix aligned to the boundary-patched framework-ready corpus to close the master-governor acceptance-without-coverage gap. |
| STEP_24_GPT_WEB_PROJECT_SYNC | completed | handoff_prompts/REPORT_TO_GPT_WEB_BIXIU4_FEED_RUBRIC_XUANBIER_PROGRESS.md; tool_outputs/gpt_web_bixiu4_xuanbier_progress_sync_response_20260519.md | Sent the current 53-row boundary-patched progress update once to ChatGPT web project `必修四喂细则` conversation `选必二框架设计` at 2026-05-19 14:15 +0800. GPT completed naturally and accepted the 53-row patched corpus as the current factual baseline; no stop/retry/send control was clicked after submission. |
| STEP_25_NET17_SERIOUS_RECHECK | completed | 04_merge_audit/net17_serious_recheck_20260519.csv; 04_merge_audit/net17_serious_recheck_20260519.md | User challenged the 70-to-53 gap. Recheck found the net 17 is actually 20 removed original rows minus 3 split additions. Three non-midterm suites have missed law subjective questions that must be recovered: 2024顺义二模 Q17, 2025海淀二模 Q18, 2026通州一模 Q20. The 53-row package is downgraded from source-exhaustive closure to bounded release candidate pending recovery. |
| STEP_26_BOUNDARY_RECOVERED_CORPUS | completed | 04_merge_audit/boundary_recovered_20260519/*; 04_merge_audit/boundary_recovered_canonical_corpus_20260519.zip; QUESTION_COVERAGE_MATRIX_BOUNDARY_RECOVERED.csv | Added the three recovered questions into a new 56-row corpus: 51 formal, 5 reference_only; 547 material atoms, 56 ask atoms, 337 rubric/answer atoms. Coverage marks the three additions as recovered_pending_framework_validation until pressure test, sidecars, handbook sections, and Word/PDF are regenerated. |
| STEP_27_SUITE_EXHAUSTION_RECOVERY | completed | 04_merge_audit/suite_exhaustive_20260519/*; 04_merge_audit/suite_exhaustive_canonical_corpus_20260519.zip; 05_reasoner_packets/suite_exhaustive_20260519/*; 06_open_observations/SUPERSEDED_BY_SUITE_EXHAUSTIVE_20260519.md | User challenged whether every suite had been exhausted. Suite-level matrix now covers 63 suites. Added 10 more core formal recoveries, producing a 66-row corpus: 61 formal, 5 reference_only; 571 material atoms, 66 ask atoms, 367 rubric atoms. Old GPT/Claude observations/framework outputs are superseded until rerun against the suite-exhaustive packet. |

| STEP_28_CLAUDECODE_SUITE_EXHAUSTION_AUDIT | completed | 04_merge_audit/claudecode_suite_exhaustion_audit_20260519/* | ClaudeCode B returned FINAL_JUDGMENT: FAIL for the old 66-row package: 1 missed formal core question, 2 downgrade/remove items, 1 split item, 7 stage mismatches, OCR/source risks. |
| STEP_29_CLAUDECODE_CORRECTED_CORPUS | completed | 04_merge_audit/suite_exhaustive_claudecode_corrected_20260519/*; 05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519/*; 04_merge_audit/claudecode_suite_exhaustion_audit_20260519/claudecode_patch_verification_report.md | Applied ClaudeCode hard fixes. Corrected core = 65 questions, formal 61, reference_only 4. ClaudeCode patch verification returned PASS; corrected packet may be sent to GPT-5.5 Pro / Claude Opus open observation. |
| STEP_30_CLAUDE_COWORK_QUESTION_REFINEMENT | completed | handoff_prompts/PROMPT_FOR_CLAUDE_COWORK_QUESTION_REFINEMENT_20260519.md; 05_reasoner_packets/COWORK_INPUT_README_20260519.md; 04_merge_audit/claude_cowork_question_refinement_20260519/ | Claude Cowork desktop task completed with CONDITIONAL_PASS; Codex applied Cowork question-layer fixes plus five extra repairs before reasoner rerun. |
| STEP_30A_LOCAL_QUESTION_LAYER_BLOCKER_CHECK | completed | 04_merge_audit/claude_cowork_question_refinement_20260519/codex_question_layer_contamination_or_missing_ask.md; 04_merge_audit/claude_cowork_question_refinement_20260519/codex_flagged_rows_suite_paper_snippets.md | Local mechanical check found 24 rows with missing ask_text and/or question/material fields apparently carrying answer/rubric text. Reasoner rerun is paused until these rows are repaired or explicitly cleared by Cowork/source check. |
| STEP_30B_COWORK_REFINED_PACKET | completed | 04_merge_audit/suite_exhaustive_cowork_refined_20260519/*; 05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/*; 05_reasoner_packets/reasoner_packet_suite_exhaustive_cowork_refined_20260519.zip | Claude Cowork E returned CONDITIONAL_PASS with no new missing questions but hard question-layer blockers. Codex applied Cowork fixes plus five extra material-layer repairs found by independent validation. Current verified packet: 65 core questions, 61 formal, 4 reference_only, 0 missing; 482 material atoms, 65 ask atoms, 350 rubric atoms; hard blockers 0. Old claudecode-corrected packet is superseded. |
| STEP_31_REAL_OPEN_OBSERVATION_COWORK_REFINED | completed | 06_open_observations/gpt55pro_open_observations_cowork_refined_20260519.md; 06_open_observations/claude_opus_open_observations_cowork_refined_20260519.md; tool_outputs/gpt55pro_open_observation_cowork_refined_call_status_20260519.md; tool_outputs/claude_opus_open_observation_cowork_refined_call_status_20260519.md | Fresh GPT-5.5 Pro and Claude Opus 4.7 Adaptive calls both completed naturally and were captured. GPT parsed 25 observations; Claude parsed 19 observations. |
| STEP_32_COWORK_REFINED_CROSS_VALIDATION_CODEBOOK | completed | 07_cross_validation/gpt_claude_observation_comparison_cowork_refined_20260519.md; 07_cross_validation/strong_shared_observations_cowork_refined_20260519.csv; 08_codebook/provisional_codebook_v0_cowork_refined_20260519.md; 08_codebook/provisional_codebook_v0_cowork_refined_20260519.csv | Parsed current model outputs, source-checked imprecise model IDs against the 65-question cowork-refined corpus, and promoted 7 dual-strong observations into the provisional codebook. Canonical open-observation/cross-validation/codebook filenames now point to the cowork-refined outputs; stale canonical files were backed up under tool_outputs. |
| STEP_33_COWORK_REFINED_CANDIDATE_FRAMEWORK_CALLS | completed | 09_candidate_frameworks/gpt55pro_candidate_frameworks_cowork_refined_20260519.md; 09_candidate_frameworks/claude_opus_candidate_frameworks_cowork_refined_20260519.md; tool_outputs/gpt55pro_candidate_framework_cowork_refined_call_status_20260519.md; tool_outputs/claude_opus_candidate_framework_cowork_refined_call_status_20260519.md | Real GPT-5.5 Pro and Claude Opus 4.7 Adaptive candidate-framework calls completed naturally and were captured from the cowork-refined 65-question packet and 7-row codebook. Gate now opens for candidate-framework comparison and local framework_v1 synthesis; framework_v1 still must be pressure-tested before any final framework or宝典 regeneration. |
| STEP_33A_CANONICAL_MERGED_REFRESH | completed | 04_merge_audit/merged_subjective_law_questions.csv; 04_merge_audit/merged_material_atoms_subjective.csv; 04_merge_audit/merged_ask_atoms_subjective.csv; 04_merge_audit/merged_rubric_atoms_subjective.csv | Root canonical merged files now match the cowork-refined 65-question corpus: 61 formal, 4 reference_only, 0 missing; 482 material atoms, 65 ask atoms, 350 rubric atoms. Previous stale 70-row canonical files backed up under `tool_outputs/pre_cowork_refined_merged_canonical_backup_20260519_175535/`. |
| STEP_34_CANDIDATE_FRAMEWORK_SYNTHESIS | completed | 09_candidate_frameworks/candidate_framework_comparison.md; 09_candidate_frameworks/framework_synthesis_plan.md; 09_candidate_frameworks/framework_v1.md; 09_candidate_frameworks/framework_v1_evidence_map.csv | Synthesized conservative `framework_v1`: 设问入口分流 + 7 codebook nodes + gap isolation. GPT and Claude both warned direct codebook support is only 16/65; no pending observation was promoted to a core node. |
| STEP_35_FRAMEWORK_V1_PRESSURE_TEST | completed | 10_framework_validation/framework_v1_question_by_question_test.csv; 10_framework_validation/framework_v1_failure_cases.md; 10_framework_validation/framework_v1_patch_suggestions.md; 10_framework_validation/framework_v1_pass_report.md | Entry-clean pressure test used only question/ask/material layers for framework entry. Result: PASS 16, PARTIAL 49, FAIL 0. The 49 PARTIAL rows are not full-score closures; final framework and baodian remain blocked pending source-check/codebook expansion. |
| STEP_36_CODEBOOK_EXPANSION_PACKET | completed | 10_framework_validation/framework_v1_partial_cluster_source_check.csv; 10_framework_validation/framework_v1_partial_cluster_source_check.md; 05_reasoner_packets/codebook_expansion_partial_rows_20260519.zip; handoff_prompts/PROMPT_FOR_GPT55PRO_CODEBOOK_EXPANSION_PARTIALS_20260519.md; handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_CODEBOOK_EXPANSION_PARTIALS_20260519.md | Built a source-check packet for the 45 formal PARTIAL rows and 4 reference_only non-core rows. This packet asks real models to propose evidence-backed codebook expansions only; final framework remains forbidden. |
| STEP_37_CLAUDE_COWORK_ALL_QUESTION_COMPLETION | completed | 04_merge_audit/claude_cowork_all_question_completion_20260519/*; 05_reasoner_packets/claude_cowork_all_question_completion_20260519.zip; tool_outputs/claude_cowork_all_question_completion_call_status_20260519.md | Claude Desktop Cowork completed naturally and was captured. Result: 1 promotable new code candidate, 4 existing-code revision candidates, 11 transfer/open-container rows, 5 source-check rows, reference_only rows rejected as core support. Final framework and baodian remain blocked pending source checks and cross-model expansion adjudication. |
| STEP_38_COWORK_BLOCKED_SOURCE_CHECK | completed | 04_merge_audit/claude_cowork_all_question_completion_20260519/codex_source_check_five_blocked_rows.md; codex_source_check_five_blocked_rows.csv; codex_source_check_corrected_rubric_atom_plan.csv | Codex回源核查 Cowork 点名 5 道：均非 missing；CC0011/CC0019 confirmed formal but must split; CC0061 must split/trim by subquestion; CC0254 current rubric atoms are wrong source segment and must be replaced by slide 29-30 scoring atoms; 房山 AI 题 formal but 2-point alternative dimensions must not be cumulated. Final framework remains blocked pending GPT/Claude expansion adjudication. |
| STEP_39_CORRECTED_EXPANSION_PACKET | completed | 05_reasoner_packets/codebook_expansion_after_cowork_sourcecheck_20260519.zip; 05_reasoner_packets/codebook_expansion_after_cowork_sourcecheck_20260519/*; handoff_prompts/PROMPT_FOR_GPT55PRO_CODEBOOK_EXPANSION_AFTER_COWORK_SOURCECHECK_20260519.md; handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_CODEBOOK_EXPANSION_AFTER_COWORK_SOURCECHECK_20260519.md | Built corrected expansion packet containing current 65-question corpus, 7-row codebook, pressure test, Cowork outputs, and Codex source-check atom plan. GPT/Claude prompts are byte-identical. Next gate is one visible submission each to GPT-5.5 Pro and Claude Opus; final framework remains blocked. |
| STEP_40_CORRECTED_EXPANSION_REAL_MODEL_CALLS | completed | 06_open_observations/gpt55pro_codebook_expansion_after_cowork_sourcecheck_20260519.md; 06_open_observations/claude_opus_codebook_expansion_after_cowork_sourcecheck_20260519.md; tool_outputs/gpt55pro_codebook_expansion_after_cowork_sourcecheck_call_status_20260519.md; tool_outputs/claude_opus_codebook_expansion_after_cowork_sourcecheck_call_status_20260519.md | Corrected GPT-5.5 Pro and Claude Opus/Cowork expansion outputs captured after natural completion. GPT output 30909 bytes with 16 TSV decisions; Claude output 49846-byte MD plus 17-row CSV. No stop/retry/regenerate/send clicks were used after submission. |
| STEP_41_EXPANSION_CROSS_VALIDATION | completed | 07_cross_validation/codebook_expansion_after_cowork_sourcecheck_20260519/codebook_expansion_after_cowork_sourcecheck_comparison.md; accepted_codebook_expansion_decisions.csv; rejected_or_open_container_expansion_decisions.csv; source_check_needed_after_expansion.csv | Cross-compared GPT and Claude expansion decisions: accept trimmed CODE_COWORK_008; revise 001/002/007/004/006; keep CC0276/reference_only/open-container rows out of core; require P0 atom patch before pressure testing. |
| STEP_42_P0_ATOM_PATCH | completed | 04_merge_audit/codebook_expansion_atom_patch_20260519/p0_atom_patch_application_report.md; 04_merge_audit/merged_rubric_atoms_subjective.csv | Applied dual-model/Codex source-check atom patch: CC0011 1->4 atoms, CC0019 1->6, CC0061 3->6 split, CC0254 wrong 8 atoms replaced by scoring atoms, 房山 AI 3->4 with alternative-not-cumulative logic; CC0143 teaching-reflection atoms annotated non-scoring. Rubric atom count now 362. |
| STEP_43_CODEBOOK_EXPANSION_DRAFT | completed | 08_codebook/provisional_codebook_v1_expansion_draft_20260519.csv; 08_codebook/provisional_codebook_v1_expansion_draft_20260519.md; 08_codebook/transfer_open_container_after_expansion_20260519.csv | Built expansion draft codebook: 8 code rows, adding trimmed CODE_COWORK_008 and revising existing codes. Core support now covers 42 unique question_ids; open/reject containers kept separate and cannot support core nodes. |
| STEP_44_EXPANSION_PRESSURE_SNAPSHOT | completed | 10_framework_validation/framework_v1_expansion_draft_pressure_snapshot_20260519.csv; 10_framework_validation/framework_v1_expansion_draft_pressure_snapshot_20260519.md | Coverage snapshot after expansion draft: 42 core codebook support, 14 open-container only, 5 reference/reject non-core, 1 source-check pending (CC0364), 3 no-expansion-support-yet. This is not final framework validation; framework_v2 and baodian remain blocked. |
| STEP_45_CC0364_SPLIT_AND_CODEBOOK_V1_1 | completed | 04_merge_audit/cc0364_split_patch_20260519/cc0364_split_patch_report.md; 08_codebook/provisional_codebook_v1_1_after_cc0364_split_20260519.md; 10_framework_validation/framework_v1_1_after_cc0364_split_pressure_snapshot_20260519.md | Split CC0364 collapsed atom into 7 formal scoring atoms; added limited CC0364 support to CODE_COWORK_004/006. Snapshot now: 43 core support, 14 open-container only, 5 reference/reject non-core, 0 source-check pending, 3 no-expansion-support-yet. |
| STEP_46_V1_1_SENTENCE_PRESSURE_TEST | completed | 10_framework_validation/framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv; 10_framework_validation/framework_v1_1_sentence_pressure_pass_report_20260519.md; 10_framework_validation/framework_v1_1_sentence_pressure_failure_cases_20260519.md; 10_framework_validation/framework_v1_1_sentence_pressure_patch_suggestions_20260519.md | Sentence-level all-65 pressure test result: PASS 43, PARTIAL 18, FAIL 4. This improves evidence closure but still blocks framework_v2/final baodian until FAIL/PARTIAL policy is adjudicated. |
| STEP_47_FAIL4_LOCAL_ADJUDICATION_AND_COWORK_CALL | running | 10_framework_validation/fail4_source_adjudication_20260519/fail4_source_adjudication_20260519.md; 05_reasoner_packets/fail4_targeted_adjudication_20260519.zip; handoff_prompts/PROMPT_FOR_CLAUDE_COWORK_FAIL4_TARGETED_ADJUDICATION_20260519.md; tool_outputs/claude_cowork_fail4_targeted_adjudication_call_status_20260519.md | Local source adjudication written for 4 FAIL rows. Claude Cowork targeted task submitted once and directory access allowed; waiting for natural completion. |
| STEP_47A_FAIL4_LOCAL_PATCH_CANDIDATES | completed | 10_framework_validation/fail4_source_adjudication_20260519/fail4_local_patch_candidates_20260519.md; 10_framework_validation/fail4_source_adjudication_20260519/fail4_local_patch_candidates_20260519.csv | While Claude Cowork is still running/stalled on workspace bash, Codex wrote a non-promotional local patch-candidate sheet: CC0143 is a consumer-contract-fraud core candidate pending Cowork/GPT confirmation; CC0276 and RECOVER_2026_西城_二模_18_3 are boundary/exclude; RECOVER_2026_西城_二模_18_2 remains open-container pending confirmation. |
| STEP_47B_FAIL4_COWORK_INTEGRATION | completed | 10_framework_validation/fail4_source_adjudication_20260519/claude_cowork_output/fail4_targeted_adjudication_claude_cowork_20260519.md; 10_framework_validation/fail4_source_adjudication_20260519/fail4_external_cross_check_20260519.md; 04_merge_audit/cc0143_atom_patch_20260519/cc0143_atom_patch_report.md; 08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.md; 10_framework_validation/framework_v1_2_fail4_resolution_snapshot_20260519.md; 10_framework_validation/framework_v1_2_partial_policy_20260519.md | Claude Cowork completed naturally. Cowork and local source adjudication agree on all four FAIL rows. CC0143 patched into CODE_COWORK_004/002 with scoring-only atoms; CC0276 and RECOVER_2026_西城_二模_18_3 are boundary excluded; RECOVER_2026_西城_二模_18_2 is open container. Core direct support now 44/65; PARTIAL rows are explicitly quarantined as reference-only or formal open-container cases. |
| STEP_48_FRAMEWORK_V1_2_GUARDED_PRESSURE | completed | 09_candidate_frameworks/framework_v1_2_guarded.md; 09_candidate_frameworks/framework_v1_2_evidence_map.csv; 10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv; 10_framework_validation/framework_v1_2_pass_report_20260519.md | Built guarded v1.2 framework from codebook v1.2 and reran all-65 pressure snapshot. Result: PASS 46 (44 core + 2 boundary-gate passes), PARTIAL 19, FAIL 0. This removes hard failure but does not make open/reference rows full-score core closure. |
| STEP_49_GUARDED_FRAMEWORK_V2_DOCS | completed | 11_final_framework/framework_v2.md; 11_final_framework/framework_v2_evidence_map.csv; 11_final_framework/framework_v2_student_one_page.md; 11_final_framework/framework_v2_teacher_guide.md; 11_final_framework/framework_v2_validation_summary.md | Generated guarded framework_v2 documents from v1.2. Validation summary explicitly preserves PASS 46 = 44 core + 2 boundary-gate, PARTIAL 19, FAIL 0; final baodian sidecars still need regeneration with labels. |
| STEP_50_GUARDED_BAODIAN_REGEN | completed | 12_final_baodian/选必二法律主观题满分宝典.md; 12_final_baodian/选必二法律主观题满分宝典.docx; 12_final_baodian/question_by_question_framework_runs.csv; 12_final_baodian/full_score_sentence_bank.csv; 12_final_baodian/material_trigger_bank.csv; 12_final_baodian/common_failure_paths.md | Regenerated guarded v2 baodian and sidecars from all-65 pressure rows. Sidecar labels: core_full_score_supported 44, formal_open_container_partial 14, reference_only_demo 4, boundary_non_core 2, open_container_only 1. DOCX generated via python-docx; Word/PDF visual QA not yet rerun. |

| STEP_51_GUARDED_V2_QA_AND_GPTPRO_PACKET | completed_local | 10_framework_validation/framework_v1_2_partial_policy_20260519.md; 12_final_baodian/DOCX_QA_GUARDED_V2.md; handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md; 05_reasoner_packets/gpt55pro_guarded_v2_review_20260519.zip | Corrected PARTIAL policy to 19 rows, recorded guarded-v2 DOCX structural/QuickLook QA with full Word/PDF still open, and prepared GPT-5.5 Pro progress-review packet. Real GPTPro submission remains pending. |
| STEP_52_GPTPRO_GUARDED_V2_REVIEW_SUBMITTED | running | tool_outputs/gpt55pro_guarded_v2_review_call_status_20260519.md | Real GPTPro submission completed once in Safari ChatGPT web with the guarded v2 review zip and pasted prompt text. Page shows `Pro 思考中`; completion is not captured yet, and Codex A must poll/read only without clicking Stop/Retry/Regenerate/Send. |
| STEP_53_CC0380_OPEN_CONTAINER_LOCAL_PATCH | completed_local_while_gptpro_running | 10_framework_validation/gptpro_guarded_v2_local_precheck_20260519.md; 09_candidate_frameworks/framework_v1_2_evidence_map.csv; 10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv; 11_final_framework/framework_v2.md; 12_final_baodian/question_by_question_framework_runs.csv | Source-checked GPTPro visible partial risk hint. `CC0380_2026_顺义_二模_18_2` moved from core `CODE_COWORK_007` support to open container. Current local pressure: PASS 45 = core/pass 43 + boundary-gate 2; PARTIAL 20; FAIL 0. GPTPro web call remains running on the pre-patch packet and must not be interrupted. |
| STEP_54_GUARDED_V2_DOCX_WORD_QA_RETRY | blocked | 12_final_baodian/DOCX_QA_GUARDED_V2.md | Retried current guarded-v2 Word/PDF QA after the CC0380 patch. Direct Word AppleScript save/export failed with `-1708`; `docx2pdf` via ASCII temp path stalled on Word file-access permission and was cancelled/killed. DOCX remains structurally valid, but full Word/PDF page-render acceptance is still open. |
| STEP_55_GPTPRO_GUARDED_V2_REVIEW_CAPTURED | completed | tool_outputs/gpt55pro_guarded_v2_review_response_20260519.md; 06_open_observations/gpt55pro_guarded_v2_review_20260519.md | Real GPT-5.5 Pro web review completed naturally and was captured. Verdict: YES_WITH_GUARDS. GPTPro accepted the 65-question factual baseline but blocked final full closure until evidence cleanup, CODE_COWORK_007 split, non-core labels, and Word/PDF visual QA are handled. |
| STEP_56_GPTPRO_GUARDED_V2_EVIDENCE_CLEANUP | completed | scripts/apply_gptpro_guarded_v2_cleanup.py; 10_framework_validation/gptpro_guarded_v2_cleanup_20260519/gptpro_guarded_v2_cleanup_report.md; 08_codebook/provisional_codebook_v1_3_after_gptpro_guarded_review_20260519.csv; 09_candidate_frameworks/framework_v1_2_evidence_map.csv; 10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv; 12_final_baodian/question_by_question_framework_runs.csv | Applied GPTPro row/file patches: marked 46 non-scoring atoms as risk/other-question material, preserved 7 patch scoring atoms, split framework N06 into 007A/B/C/D subnodes, moved CC0380 to open container, removed answer-column contamination from CC0077/CC0084/CC0150/CC0245/CC0251, and regenerated guarded sidecars. Current pressure remains PASS 45 = 43 core + 2 boundary, PARTIAL 20, FAIL 0; DOCX full visual QA remains blocked. |
| STEP_57_GUARDED_V2_WORD_PDF_QA_AND_ACCEPTANCE | completed | 12_final_baodian/DOCX_QA_GUARDED_V2.md; 12_final_baodian/选必二法律主观题满分宝典_GUARDED_V2_WORD_EXPORT.pdf; FINAL_ACCEPTANCE_REPORT_GUARDED_V2.md; FINAL_DELIVERY_REPORT_GUARDED_V2.md | Microsoft Word opened the DOCX from an ASCII temp path and exported a 114-page PDF. PyMuPDF rendered every page; blank-page detections 0. Guarded v2 accepted with guards: 43 core full-score supported rows, 2 boundary-gate rows, 20 non-core/open/reference rows preserved. |
| STEP_58_ZERO_BASELINE_STUDENT_PRESSURE_TEST | completed | 10_framework_validation/zero_baseline_student_pressure_20260520/internal_agent_zero_baseline_student_answers_20260520.md; 10_framework_validation/zero_baseline_student_pressure_20260520/claude_cowork_zero_baseline_student_answers_20260520.md; 10_framework_validation/zero_baseline_student_pressure_20260520/gptpro_zero_baseline_student_answers_20260520.md; 10_framework_validation/zero_baseline_student_pressure_20260520/zero_baseline_student_pressure_codex_grading_report_20260520.md; 10_framework_validation/zero_baseline_student_pressure_20260520/zero_baseline_student_pressure_scores_20260520.csv; 12_final_baodian/DOCX_QA_GUARDED_V2.md | User-requested zero-baseline high-school-student simulation completed through internal agent, Claude Cowork/Opus, and GPTPro (`进阶专业`) using learning-only packet. Verdict: core path works strongly for T1/T2/T3/T4 but needs micro-prompts for mixed liability, consumer fraud claim chain, labor value layer, open-container fallback, and boundary fallback. Student one-page, framework v2, teacher guide, baodian Markdown/DOCX regenerated; Word-exported PDF rendered 115 pages with blank-page suspects 0. |
| STEP_59_GPTPRO_FRAMEWORK_QUALITY_CHALLENGE | completed | 05_reasoner_packets/framework_quality_challenge_gptpro_20260520.zip; handoff_prompts/PROMPT_FOR_GPTPRO_FRAMEWORK_QUALITY_CHALLENGE_20260520.md; 06_open_observations/gptpro_framework_quality_challenge_20260520.md; tool_outputs/gptpro_framework_quality_challenge_status_20260520.md | User challenged the quality/feel of guarded v2 compared with the earlier stronger framework. Sent a clean GPTPro quality-challenge packet once through ChatGPT web (`进阶专业`) and captured the completed critique. GPTPro agrees the current version is evidence-correct but too much like an audit ledger, not enough like a student-startable framework. It recommends strong-mainline plus full-container rewrite: replace the student one-page/opening, repair N06 contamination, remove audit traces from 43 core answers, and split future deliverables into student battle version, teacher script, and evidence appendix. |
| STEP_60_STUDENT_BATTLE_BAODIAN_V1 | completed_local | scripts/build_student_battle_baodian.py; scripts/export_student_battle_docx.py; 12_final_baodian/选必二法律主观题满分宝典_学生战斗版.md; 12_final_baodian/选必二法律主观题满分宝典_学生战斗版.docx | Converted GPTPro's quality critique into a student-facing battle handbook: strong mainline + full-container front end, seven student-startable trunks, material-to-law translation bank, wrong-answer corrections, eight classic worked examples, and all-65 source placement table. Backend/audit terms were scanned and removed from the student artifact. DOCX structural QA passed via python-docx: 340 paragraphs, 5 tables. Full Word/PDF visual QA remains optional/open for this new student-battle derivative. |
| STEP_61_ROLLBACK_TO_STEP29_CLAUDECODE_65 | completed | ROLLBACK_TO_STEP29_ACTIVE_BASELINE_20260520.md; 04_merge_audit/rollback_to_step29_claudecode_corrected_65_20260520/*; 05_reasoner_packets/rollback_to_step29_claudecode_corrected_65_20260520/*; handoff_prompts/PROMPT_FOR_VSCODE_CLAUDECODE_STEP29_65_REAUDIT_20260520.md | User rejected the current framework/宝典 direction and ordered rollback to the Codex+ClaudeCode 65-question evidence layer. Canonical `04_merge_audit/merged_*` files were reset to STEP_29: 65 questions, 61 formal, 4 reference_only, 0 missing; 541 material atoms, 65 ask atoms, 362 rubric atoms. Later observations/codebooks/frameworks/baodian are marked superseded history and must not be used as the current basis. |


## STEP_62_PRIOR_FRAMEWORK_LEARNING_PACKET - 2026-05-20 04:16:02

- 已按用户要求读取桌面 `先前框架`，并转写为 GPTPro 可读 Markdown/CSV 包。
- 输出目录：`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/05_reasoner_packets/prior_framework_learning_gptpro_20260520`
- 打包文件：`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/05_reasoner_packets/prior_framework_learning_gptpro_20260520.zip`
- 先前框架用途：只学习结构、表达、学生可启动性；不得作为选必二法律证据。
- 当前法律证据底座仍为 STEP_29 回退基线：65 题，evidence_level={'formal': 61, 'reference_only': 4}。
- 下一步：把 `PROMPT_FOR_GPTPRO_PRIOR_FRAMEWORK_LEARNING_LEGAL_V0_20260520.md` 与 zip 包提交给 GPTPro，要求生成法律主观题框架 v0。

## STEP_63_GPTPRO_PRIOR_FRAMEWORK_CALL_SUBMITTED - 2026-05-20 04:18:12 CST

- 已通过 Safari ChatGPT 网页将 `prior_framework_learning_gptpro_20260520.zip` 上传给 GPTPro。
- 已发送任务说明：要求 GPTPro 读取包内 prompt、结构 DNA 摘要、65 题 compact CSV 和 `references_md/`，学习先前框架的结构表达，再基于 65 题生成法律主观题框架 v0。
- 操作纪律：只点击发送一次；当前 GPTPro 状态为 `Pro 思考中`。
- 下一步：等待 GPTPro 输出，保存到 `09_candidate_frameworks/gptpro_prior_framework_learned_legal_framework_v0_20260520.md`，再进入 Codex 回源压测。

## STEP_64_GPTPRO_PRIOR_FRAMEWORK_V0_CAPTURED - 2026-05-20 04:31:00 CST

- GPTPro 已自然完成，页面显示“已思考 12m27s”。
- 正确输出已保存到 `09_candidate_frameworks/gptpro_prior_framework_learned_legal_framework_v0_20260520.md`。
- 先前误复制的上一条质量审查已备份到 `tool_outputs/gptpro_wrong_previous_quality_review_clipboard_20260520.md`。
- 本地核查：canonical 仍为 STEP_29 基线 65 题，61 formal，4 reference_only，0 missing；GPTPro v0 明确禁止 reference_only 单独支撑核心。
- 本地扫描：65 个 question_id 均至少以完整 ID 或短 ID 被 GPTPro v0 覆盖；未发现未知 CC 编号。
- 当前裁定：GPTPro v0 可作为候选框架进入本地逐题压测，但不是最终框架或宝典。

## STEP_65_LOCAL_PRESSURE_TEST_GPTPRO_V0 - 2026-05-20 04:38:00 CST

- 已用 GPTPro v0 七个动作节点回跑 STEP_29 65 题。
- 输出：`10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv`
- 输出：`10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.md`
- 结果：PASS_CANDIDATE 35；PARTIAL_SOURCE_CHECK 18；PARTIAL_LOW_FREQ_CONTAINER 5；PARTIAL_REFERENCE_ONLY 4；PARTIAL_BOUNDARY_OPEN 3。
- 节点覆盖：N03 切责成链 63；N07 补价值 58；N02 先判后证 47；N05 走救济 42；N04 护创新 29；N06 划边界 26；N01 一格一答 8。
- 当前裁定：GPTPro v0 是比旧审计稿更强的候选框架，但不能直接变成最终宝典；下一步应先清洗 18 个 ask/source-check 行，再对 35 个 PASS_CANDIDATE 做 rubric-atom 句子级对齐。

## STEP_66_NIGHT_V4_STUDENT_FULLSCORE_REBUILD - 2026-05-20 12:54:00 CST

- 已从 STEP_29 65 题证据底座重新生成 V4 学生可用框架与宝典，而不是沿用被用户否定的 guarded v2/student-battle 旧线。
- 生成脚本：`scripts/build_student_fullscore_v4.py`
- 主要输出：
  - `05_reasoner_packets/night_v4_student_fullscore_council_20260520/refined_classification_65_v4.csv`
  - `05_reasoner_packets/night_v4_student_fullscore_council_20260520.zip`
  - `04_merge_audit/night_v4_classification_source_clean_audit_20260520.md`
  - `11_final_framework/framework_v4_student_fullscore_20260520.md`
  - `11_final_framework/framework_v4_student_one_page_20260520.md`
  - `11_final_framework/framework_v4_teacher_guide_20260520.md`
  - `12_final_baodian/选必二法律主观题满分宝典_学生满分训练版_20260520.md`
  - `12_final_baodian/选必二法律主观题满分宝典_学生纯净版_20260520.md`
  - `12_final_baodian/question_by_question_framework_runs_v4_20260520.csv`
  - `12_final_baodian/full_score_sentence_bank_v4_20260520.csv`
  - `12_final_baodian/material_trigger_bank_v4_20260520.csv`
  - `10_framework_validation/framework_v4_question_by_question_test_20260520.csv`
  - `10_framework_validation/framework_v4_pass_report_20260520.md`
- 65 题状态：61 formal，4 reference_only，0 missing。
- V4 分类：53 core_candidate，5 low_frequency_container，4 reference_only_container，3 boundary_open_container。
- V4 信任度：39 high，24 medium，2 source_check。
- 当前裁定：V4 是一个学生前台成品候选；它比旧审计式稿更像能上课使用的框架，但四线外部终验仍未完成。

## STEP_67_CONFUCIUS_ZERO_BASELINE_V4_AND_PATCH - 2026-05-20 12:54:00 CST

- 已调用本地 agent 模拟“聪明但零基础高三学生”学习 V4 后抽题作答。
- 输出：`10_framework_validation/confucius_zero_baseline_simulation_v4_20260520.md`
- 结果：`CONDITIONAL_PASS_FOR_STUDENT_USE`。
- 模拟覆盖：消费者欺诈、平台劳动关系、举证责任、AI 风险、起诉状、无过错侵权、AI 责任边界、相邻关系。
- 根据模拟反馈已补入 V4：
  - 程序/证据/救济分叉；
  - 起诉状三件套；
  - AI 主体资格与 AI 幻觉责任；
  - 举证责任；
  - 价值表达必须绑定本案规则；
  - reference_only/边界题隔离。
- 当前裁定：学生可启动性明显提高，但外部 GPTPro/Claude V4 复审仍是 gate。

## STEP_68_STUDENT_PURE_DOCX_PDF_QA - 2026-05-20 12:58:42 CST

- 已生成学生纯净版 DOCX：`12_final_baodian/选必二法律主观题满分宝典_学生纯净版_20260520.docx`
- 已用 Microsoft Word 导出 PDF：`12_final_baodian/word_pdf_v4/选必二法律主观题满分宝典_学生纯净版_20260520.pdf`
- 已渲染抽样页：`12_final_baodian/word_pdf_v4/rendered_pngs/`
- QA 报告：`12_final_baodian/DOCX_PDF_QA_STUDENT_PURE_V4_20260520.md`
- 结果：PDF 54 页，0 个空白文本页；抽样页可读；学生纯净 Markdown 后端术语扫描通过。
- 当前裁定：技术/渲染层面可以交付阅读，但不是四线最终 PASS。

## STEP_69_V4_EXTERNAL_REVIEW_PACKET_READY - 2026-05-20 12:58:42 CST

- 已生成 GPTPro/Claude Opus V4 学生压测包：`05_reasoner_packets/night_v4_student_fullscore_council_20260520.zip`
- 包内 prompt：
  - `PROMPT_FOR_GPTPRO_V4_STUDENT_PRESSURE_TEST.md`
  - `PROMPT_FOR_CLAUDE_OPUS_V4_STUDENT_PRESSURE_TEST.md`
- 当前状态：real_call_pending。
- 当前裁定：不得声称 GPTPro/Claude 已对 V4 成品完成二次压测；只能说已经准备好统一输入包。

## STEP_70_PRIOR_FRAMEWORK_DEEP_RELEARNING - 2026-05-20 13:10:00 CST

- 用户再次否定当前框架质量，要求先学习桌面先前框架。
- 已读取三层 SOP、选必二 skill、小本本、当前 run 控制文件。
- 已定位桌面先前框架目录：`/Users/wanglifei/Desktop/先前框架`。
- 已渲染先前框架抽样页：`05_reasoner_packets/prior_framework_deep_learning_20260520/rendered_samples/`。
- 已深读/抽样：
  - 选必一手写框架；
  - 必修二五四三二一；
  - 经济与社会二轮习题课；
  - 经济主体积累页；
  - 哲学与文化手写框架；
  - 逻辑与思维框架；
  - 旧法律框架样本（仅作结构样本，不作当前证据）。
- 新增输出：
  - `05_reasoner_packets/prior_framework_deep_learning_20260520/PRIOR_FRAMEWORK_DEEP_DNA_20260520.md`
  - `05_reasoner_packets/prior_framework_deep_learning_20260520/LEGAL_REWRITE_SPEC_AFTER_PRIOR_STUDY_20260520.md`
  - `handoff_prompts/PROMPT_FOR_GPTPRO_CLAUDE_PRIOR_FRAMEWORK_RELEARN_20260520.md`
- 当前裁定：V4 不继续修补；下一版必须先模仿先前框架的“先导页 -> 基本模型 -> 主体积累 -> 情境触发 -> 争点演练 -> 错法改法”，再回到 65 题证据。

## STEP_71_PRIOR_RELEARN_MODEL_PACKET - 2026-05-20 13:20:00 CST

- 已把深度学习文件、GPTPro/Claude prompt、当前 65 题 merged evidence、V4 逐题运行失败样本打成统一包。
- 输出：`05_reasoner_packets/prior_framework_deep_learning_20260520.zip`
- 包内 README：`05_reasoner_packets/prior_framework_deep_learning_20260520/MODEL_PACKET_README.md`
- 当前裁定：可以进入 GPTPro/Claude “先学结构，再写法律框架提案”的外部审议；不得直接拿 V4 继续改。

## STEP_72_GPTPRO_CURRENT_V4_PLUS_PRIOR_DNA_COUNTERMEASURES_SUBMITTED - 2026-05-20 14:56:51 CST

- 已按用户要求，把“当前 V4 框架 + 先前框架深度学习结果 + 65 题证据基线 + V4 压测材料”上传到先前指定 GPTPro 对话 `质量审查与框架重构`。
- 上传包：`05_reasoner_packets/current_framework_plus_prior_learning_for_gptpro_20260520.zip`
- 包内主 prompt：`05_reasoner_packets/current_framework_plus_prior_learning_for_gptpro_20260520/00_prompt/PROMPT_FOR_GPTPRO_COUNTERMEASURES_AFTER_V4_AND_PRIOR_LEARNING_20260520.md`
- 本地状态记录：`tool_outputs/gptpro_current_framework_prior_learning_countermeasures_status_20260520.md`
- 发送规则：附件和短提示词就位后，只按了一次 `发送提示`。
- 当前状态：GPTPro 显示 `Pro 思考中`，等待输出。
- 当前裁定：这是“让 GPTPro 出重建对策”的外部审议步骤，不代表新框架已经完成；V4 仍保持失败诊断对象身份。


## STEP_73_V5_ACTION_CARD_REBUILD_STARTED_AND_FIRST10_BUILT (2026-05-21 01:52:32)

- GPTPro 当前 V4 + 先前框架学习结果合审回答已落盘：`09_candidate_frameworks/gptpro_current_framework_prior_learning_countermeasures_20260520.md`。
- 已按 GPTPro 对策生成 V5 动作卡候选框架、证据映射、分批计划、学生一页纸和十题样章。
- 当前仍不声明最终 PASS：Claude Opus 真实复核、十题零基础学生压测、35 道核心题扩展仍待完成。


## STEP_74_CLAUDE_OPUS_V5_COUNTER_REVIEW_RUNNING (2026-05-21 01:56 CST)

- 已通过 Claude Desktop / Cowork / Opus 4.7 发送 V5 动作卡复核任务。
- 不触碰 Stop response，不重复发送。
- 目标输出：`06_open_observations/claude_opus_v5_action_card_counter_review_20260521.md`。
- 后续门槛：必须读取 Claude 输出后再决定是否生成 V5.1。

## STEP_75_V11_SOURCE_LOCKED_REBUILD_STARTED (2026-05-21 23:20 CST)

- 用户明确停止 v10；GPT 审核判定 v10 验收报告作废，原因是 53 题题源错配、材料错配、触发错配、覆盖矩阵虚高和自动匹配垃圾化。
- 已启动 `v11_source_locked_rebuild`，本阶段不继承 v10 acceptance，不写 `EXHAUSTIVE_FRAMEWORK_PASS`。
- 已完成第一步：`v11_source_locked_rebuild/01_53题回源审判表.csv` 与 `v11_source_locked_rebuild/01_53题回源审判报告.md`。
- 53 题仍按 boundary-patched 口径处理：37 PASS、11 PASS_RECOVERED、5 OPEN_OR_REFERENCE。
- v11 第一轮审判结果：保留 14、重写 5、降级参考 5、待用户确认 29；需要回源修复 34；材料层答案/细则/分析混入 9；OCR/串页/非法律污染 21；设问缺失或待确认 20。
- 当前门槛：未完成 02 强分诊框架清单、03 下篇全量题链、04 上篇强分诊框架、05 覆盖矩阵、06 验收；不得进入最终交付或 PASS。


## STEP_75_V5_SOURCE_QUEUE_AND_65_PLACEMENT_MATRIX (2026-05-21 02:01 CST)

- 已生成 V5 设问回源队列：`10_framework_validation/v5_ask_text_source_check_queue_20260521.csv` / `.md`，共 21 个设问字段空白或待 OCR/回源。
- 已生成 V5 65题放置矩阵：`10_framework_validation/framework_v5_65_question_placement_matrix_20260521.md`。
- 当前原则：回源队列不否定 65 题穷尽，只限制进入学生版样章/核心扩展前必须补正设问或标注 inferred。


## STEP_76_V5_EVIDENCE_ROLE_FIX (2026-05-21 02:06 CST)

- 修正 `framework_v5_evidence_map_20260521.csv` 的 role_in_node：formal 但待回源的题不再标成 core_support，而标为 `sample_pending_source` 或 `source_check_pending`。
- 当前证据纪律：只有 PASS_CANDIDATE 且非 reference_only 的题才作为核心支撑；低频题为 `container_only`。


## STEP_77_V5_INTERNAL_ZERO_BASELINE_RESULT (2026-05-21 02:10 CST)

- Codex 内部零基础学生压测完成：`10_framework_validation/zero_baseline_student_pressure_v5_20260521/codex_agent_zero_baseline_answers_20260521.md`。
- 摘要：`10_framework_validation/zero_baseline_student_pressure_v5_20260521/codex_agent_zero_baseline_summary_20260521.md`。
- 结论：V5 能让学生不空不乱，但不足以稳定满分；V5.1 必须在七张动作卡下补“最小法律规则句库”。
- 注意：该压测是 Codex 内部 agent，不替代 GPTPro/Claude 真实复核。


## STEP_78_V5_1_CLAUDE_PATCH_APPLIED (2026-05-21 02:08:48)

- 已读取 Claude Opus 复核：`06_open_observations/claude_opus_v5_action_card_counter_review_20260521.md`。
- 已按 Claude 硬问题生成 V5.1：六张动作卡 + 起手表态铁律。
- 已清洗 CC0277/CC0251 脏细则，降级 AI 宏观和低频容器，返工 CC0077/CC0143/CC0103 样章。
- 新文件：
  - `09_candidate_frameworks/framework_v5_1_action_card_candidate_20260521.md`
  - `09_candidate_frameworks/framework_v5_1_evidence_map_20260521.csv`
  - `09_candidate_frameworks/v5_1_batch_plan_20260521.csv`
  - `11_final_framework/framework_v5_1_student_one_page_20260521.md`
  - `10_framework_validation/framework_v5_1_first10_sample_runs_20260521.md`
  - `12_final_baodian/选必二法律主观题满分宝典_v5_1_十题样章_20260521.md`
- 当前仍不声明最终 PASS：必须做干净题面零基础压测和 35 道核心扩展。

## STEP_79_V5_1_PATCH_VERIFICATION (2026-05-21)

- 已修正 V5.1 脚本中 CC0251 R01 被 `slide` 噪音误杀的问题，并重建 V5.1 产物。
- 已完成机器核验：CC0277 只保留 R01-R06；CC0251 只保留 R01；V5.1 关键输出中不再出现 CC0277 R07-R11 或 CC0251 R02-R16。
- 已生成补丁核验报告：`10_framework_validation/v5_1_patch_verification_report_20260521.md`。
- 当前状态：V5.1 可进入干净题面零基础压测；不得进入最终宝典或 35 核心扩展前跳过压测。

## STEP_80_V5_2_ZERO_BASELINE_PRESSURE_PASS (2026-05-21)

- 已制作 V5.1/V5.2 共用干净题面包：`10_framework_validation/zero_baseline_student_pressure_v5_1_20260521/clean_questions_no_rubric_v5_1_20260521.md`。
- 已用 V5.1 一页纸压测并评分：`codex_agent_zero_baseline_answers_v5_1_20260521.md`; `codex_grading_report_v5_1_20260521.md`。
- 已根据失分点生成 V5.2 学生速用稿：`11_final_framework/framework_v5_2_student_one_page_20260521.md`。
- 已用同一题包重测 V5.2：`codex_agent_zero_baseline_answers_v5_2_20260521.md`; `codex_grading_report_v5_2_20260521.md`。
- 分数从 `4.5/8, 7/8, 6.5/8, 4/6, 6.5/8, 6/8, 6/10` 提升为 `7.5/8, 7.5/8, 7.5/8, 6/6, 8/8, 8/8, 9.5/10`。
- 当前裁定：V5.2 通过小样本零基础可学会性测试，允许进入 35 道核心题样章扩展；仍非最终宝典。


## STEP_81_V5_2_STRICT_CORE_EXPANSION (2026-05-21 02:23:22)

- 已按 V5.2 证据纪律从旧 35 个 PASS_CANDIDATE 中重算严格核心：31 道。
- 已降级 4 道：CC0251、CC0283、CC0364、RECOVER_2026_西城_二模_18_2，原因见 `10_framework_validation/v5_2_strict_core_downgraded_from_35_20260521.csv`。
- 已生成 31 道严格核心逐题运行：`12_final_baodian/选必二法律主观题满分宝典_v5_2_31严格核心扩展_20260521.md`。
- 已生成逐题运行 CSV 和满分句库。
- 当前仍不最终定稿：需要 GPTPro/Claude 复核，且开放容器/待回源/reference_only 题还需按标签进宝典。


## STEP_82_V5_2_REVIEW_PACKET_AND_65_COVERAGE (2026-05-21 02:25:46)

- 已生成 V5.2 65 题覆盖矩阵：`10_framework_validation/v5_2_65_question_coverage_matrix_20260521.csv`。
- 已生成 GPTPro/Claude 复核包：`05_reasoner_packets/v5_2_gptpro_claude_review_packet_20260521.zip`。
- 当前允许：发送真实 GPTPro/Claude 复核。
- 当前不允许：最终定稿或 DOCX/PDF 交付。
## STEP_83_CLAUDE_OPUS_V5_2_REVIEW_AND_PATCH (2026-05-21 02:38:28 CST)

- Claude Opus 4.7 已完成 V5.2 真实复核并写入：`06_open_observations/claude_opus_v5_2_review_20260521.md`。
- 外审裁定：`CONDITIONAL_PASS`。学生速用稿通过；31 道核心扩展不得直接进入最终宝典。
- 已接收并执行 P0 修补：重写 `CC0244_2026_东城_期末_18` 考场答案；降级 `CC0137/CC0119/CC0289/CC0061` 为 source_check_pending；修正 `CC0276/CC0380` 为 boundary_open_container。
- 当前 active strict_core 由 31 降为 27，输出为：`12_final_baodian/选必二法律主观题满分宝典_v5_2_27严格核心扩展_20260521.md`。
- 已生成修补说明：`10_framework_validation/v5_2_claude_opus_review_response_patch_20260521.md`。
- GPTPro 真实复核仍在 Safari 中运行，待输出后进行双审交叉验证。

## STEP_84_V5_2_DUAL_REVIEW_AND_V5_3_CLEAN_CORE (2026-05-21 03:05 CST)

- 已保存真实 GPTPro V5.2 复核：`06_open_observations/gptpro_v5_2_review_20260521.md`。
- 已保存 Claude Opus V5.2 复核：`06_open_observations/claude_opus_v5_2_review_20260521.md`。
- 已生成双审比较：`07_cross_validation/v5_2_gptpro_claude_review_comparison_20260521.md`。
- 双审共同裁定：V5.2 速用稿有进步，但 31 核心扩展不能发布；接受 27 strict_core，24 source_check_pending，5 low_frequency_container，4 reference_only_locked，4 boundary_open_container，1 excluded_logic_boundary。
- 已生成 V5.3 27 核心清洗学生版与侧边表：
  - `12_final_baodian/选必二法律主观题满分宝典_v5_3_27核心清洗学生版_20260521.md`
  - `12_final_baodian/question_by_question_framework_runs_v5_3_27core_clean_20260521.csv`
  - `12_final_baodian/full_score_sentence_bank_v5_3_27core_clean_20260521.csv`
  - `10_framework_validation/v5_3_clean_core_answer_audit_20260521.md`
- V5.3 机械污染扫描：0。
- 当前裁定：V5.3 是 27 核心清洗稿，不是 65 题最终宝典。

## STEP_85_V5_4_REVIEW_PACKET_AND_ZERO_BASELINE_TEST (2026-05-21 03:10 CST)

- 已生成 V5.4 学生战斗清洗版：
  - `12_final_baodian/选必二法律主观题满分宝典_v5_4_学生战斗清洗版_20260521.md`
  - `11_final_framework/framework_v5_4_student_core_20260521.md`
- 已生成外部复审包：`05_reasoner_packets/v5_4_gptpro_claude_review_packet_20260521.zip`。
- 已通过 Safari ChatGPT 网页把 V5.4 包提交给 GPTPro；状态记录：`tool_outputs/gptpro_v5_4_review_status_20260521.md`，当前 `submitted_running`。
- 本地零基础学生压测已完成：`10_framework_validation/v5_4_zero_baseline_student_pressure_test_20260521.md`。
- 压测结论：`CONDITIONAL_PASS`。V5.4 能启动核心题，但 CC0244 漏原题第（2）问，非核心题只能保分，不能称 65 题满分闭合。
- 当前裁定：V5.4 不发布，进入 V5.5 修补。

## STEP_86_V5_5_STUDENT_USABILITY_PATCH (2026-05-21 03:17 CST)

- 已按 V5.4 压测和本地硬扫描生成 V5.5：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v5_5_27核心65保分版_20260521.md`
  - `11_final_framework/framework_v5_5_student_core_20260521.md`
  - `12_final_baodian/question_by_question_framework_runs_v5_5_27core65guard_20260521.csv`
  - `12_final_baodian/non_core_guardrails_v5_5_20260521.csv`
  - `10_framework_validation/v5_5_student_usability_patch_report_20260521.md`
- 修补内容：
  - 将 V5.4 每题泛泛的“属于某卡”改为具体最小判断。
  - CC0244 补回第（2）问：证据准备、请求设计、维权路径。
  - 每道核心题增加“满分前检查”。
  - 增加其余 38 题的保分容器：低频规则题、边界综合题、组合型题、多小问和表格题。
  - 标题降调为“满分训练宝典”，不再暗示 65 题全部核心满分闭合。
- V5.5 机械污染扫描：0。
- 已启动 V5.5 新一轮零基础学生压测 agent；目标文件：`10_framework_validation/v5_5_zero_baseline_student_pressure_test_20260521.md`。
- 当前裁定：V5.5 是当前最佳学生稿候选；最终发布仍等待 V5.5 压测、GPTPro V5.4 回收、必要的 Claude V5.4/V5.5 复审和本地裁决。

## STEP_87_V5_6_V5_7_NON_CORE_GUARDRAIL_AND_REVIEW_PACKET (2026-05-21 03:43 CST)

- 已完成 V5.6 本地零基础学生压测：`10_framework_validation/v5_6_zero_baseline_student_pressure_test_20260521.md`。
- 压测裁定：`CONDITIONAL_PASS`。V5.6 比 V5.5 明显改善，核心是补齐 38 道非核心逐题保分索引；仍不能替代 GPTPro/Claude 真实复核。
- 已生成 V5.7 学生稿小修版：`12_final_baodian/选必二法律主观题满分训练宝典_v5_7_27核心38题保分索引小修版_20260521.md`。
- V5.7 已修：标题版本混乱、核心题 20 起诉状证据栏、source-check 红线、reference-only 红线、综合边界红线、`CC0061` 回避填空例句。
- 已保存 GPTPro V5.4 真实网页反馈的可见截屏归档：`06_open_observations/gptpro_v5_4_review_20260521.md`；状态为可见归档，不冒充完整复制稿。
- 已生成 V5.7 GPTPro/Claude 复审包：`05_reasoner_packets/v5_7_gptpro_claude_review_packet_20260521.zip`。
- 当前覆盖账本：65 题总数；27 strict_core；38 非核心，其中 24 source_check_pending、5 low_frequency_container、4 reference_only_locked、4 boundary_open_container、1 excluded_logic_boundary。
- 当前裁定：V5.7 可进入真实 GPTPro/Claude 复审；不得宣称最终 Word/PDF 定稿，source-check 题仍需回源核对。

## STEP_88_V5_7_REAL_REVIEW_SUBMITTED (2026-05-21 03:49 CST)

- 已向 GPTPro 网页对话提交 V5.7 复审包：`05_reasoner_packets/v5_7_gptpro_claude_review_packet_20260521.zip`。
- GPTPro 状态文件：`tool_outputs/gptpro_v5_7_review_status_20260521.md`；当前 `submitted_running`。
- 风险记录：前台短提示曾因 Computer Use 直接输入出现中文丢失/片段化，GPTPro 当前回答明确表示会按 V5.7 包内 prompt 与文件清单复核；输出回收时必须检查是否真正遵守 V5.7、27核心/38非核心、P0/P1/P2、12题抽测、Word/PDF gate。
- 已向 Claude Desktop / Cowork / Opus 4.7 提交同一 V5.7 复审任务。
- Claude 状态文件：`tool_outputs/claude_opus_v5_7_review_status_20260521.md`；当前 `submitted_running`。
- 当前操作纪律：两边均不得点击 Stop / Retry / Regenerate / Send / Queue；只允许轮询读取自然完成结果。

## STEP_89_V5_8_CLAUDE_GUARDED_PATCH_CANDIDATE (2026-05-21 04:00 CST)

- Claude Opus V5.7 终审已自然完成并落盘：`06_open_observations/claude_opus_v5_7_review_20260521.md`。
- Claude 裁定：`CONDITIONAL_PASS / YES_WITH_GUARDS`，无 P0；必须先修 P1 卡入口过宽，并给 source-check/reference/boundary/transfer 做醒目红线。
- 已生成不覆盖 V5.7 的 V5.8 本地候选补丁：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v5_8_27核心38题保分索引_P1入口修补候选版_20260521.md`
  - `10_framework_validation/v5_8_claude_guarded_patch_report_20260521.md`
  - `12_final_baodian/non_core_guardrails_v5_8_20260521.csv`
  - `12_final_baodian/question_by_question_framework_runs_v5_8_27core65guard_20260521.csv`
  - `04_merge_audit/candidate70_to_current65_delta_ledger_20260521.csv`
  - `04_merge_audit/candidate70_to_current65_delta_summary_20260521.md`
- 已修：27 核心入口统一为 1 主卡 + 最多 1 辅卡；CC0025 补公平诚信原则/社会主义核心价值观；38 非核心标题补 question_id；非核心红线入正文；CC0245 改为核心题 16 交叉引用；70->65 去向台账补齐。
- 当前仍不最终定稿：GPTPro V5.7 尚未捕获，V5.8 状态为 `candidate_pending_gptpro_capture`。

Governor decision: V5_8_LOCAL_PATCH_CANDIDATE_PENDING_GPTPRO.

## STEP_90_V5_8_CANDIDATE_PREFLIGHT_CHECK (2026-05-21 04:08 CST)

- 已完成 V5.8 候选稿本地机械预检：`10_framework_validation/v5_8_candidate_preflight_check_20260521.md`。
- 检查结论：27 个核心题入口行均为 `主卡 + 最多 1 辅卡`，未发现 `+` 或多卡乱入口；38 个非核心题标题均带 question_id；非核心红线计数为 source-check 23、reference-only 4、boundary 4、transfer 1、duplicate-crossref 1。
- CSV 对账：27 核心逐题运行 CSV 行数为 27；38 非核心护栏 CSV 行数为 38；70->65 去向台账行为 53。
- 当前裁定：V5.8 通过本地候选预检，但仍为 `candidate_pending_gptpro_capture`；GPTPro V5.7 尚未自然完成并捕获，不能进入最终 Word/PDF。

## STEP_91_V5_8_CLEAN_GPTPRO_FINAL_GATE_SUBMITTED (2026-05-21 04:17 CST)

- 已确认 Safari 原 GPTPro 标签页实际停留在旧 V5.2 回复，并且底部存在乱码残留；因此不再承认 `gptpro_v5_7_review_status` 为有效完成状态。
- 已生成并提交 V5.8 干净终审包：`05_reasoner_packets/v5_8_gptpro_final_gate_packet_20260521.zip`。
- 已用 ASCII 短提示提交一次，要求 GPTPro 只读取压缩包内 `PACKET_README.md` 与 `00_prompt/PROMPT_FOR_GPTPRO_V5_8_FINAL_GATE_REVIEW_20260521.md`，忽略旧上下文与乱码。
- 状态文件：`tool_outputs/gptpro_v5_8_final_gate_status_20260521.md`，当前 `submitted_running`。
- 当前纪律：只允许等待自然完成和捕获输出；不得点击 Stop / Retry / Regenerate / Send。

Governor decision: V5_8_CLEAN_GPTPRO_FINAL_GATE_RUNNING_NOT_FINAL.

## STEP_92_V5_8_CLAUDE_FINAL_GATE_SUBMITTED (2026-05-21 04:20 CST)

- 已生成 Claude Opus 4.7 V5.8 终审 prompt：`handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_V5_8_FINAL_GATE_REVIEW_20260521.md`。
- 已向 Claude Desktop / Cowork / Opus 4.7 提交 V5.8 终审任务，输入为同一 V5.8 final gate packet 目录。
- 状态文件：`tool_outputs/claude_opus_v5_8_final_gate_status_20260521.md`，当前 `submitted_running`。
- 预期输出：`06_open_observations/claude_opus_v5_8_final_gate_review_20260521.md`。
- 当前纪律：GPTPro 和 Claude 均已提交 V5.8 终审；只允许等待自然完成和捕获输出，不得打断。

Governor decision: V5_8_DUAL_FINAL_GATE_RUNNING_NOT_FINAL.

## STEP_93_CLAUDE_V5_8_FINAL_GATE_CAPTURED (2026-05-21 04:25 CST)

- Claude Opus V5.8 终审已自然完成并写入：`06_open_observations/claude_opus_v5_8_final_gate_review_20260521.md`。
- Claude 裁定：`PASS / YES_WITH_GUARDS`。
- 关键结论：
  - V5.7 唯一 P1（核心入口过宽）已实测修复，27 核心入口均为主卡/辅卡格式。
  - 无 P0、无 P1。
  - 12 题抽测中 7 核心接近满分，5 非核心没有误升核心。
  - 剩余 4 个 P2：低频题视觉红线、27 核心全量细则对账留痕、CC0150 底座串入原子清理、后台 CSV `minimum_judgment` 同步。
- 当前仍不最终定稿：等待 GPTPro V5.8 自然完成并捕获，再做双审比较。

Governor decision: CLAUDE_V5_8_PASS_WAIT_GPTPRO.

## STEP_94_V5_8_27_CORE_RUBRIC_TRACE_PREPARED (2026-05-21 04:27 CST)

- 已先处理 Claude P2-2 的“27 核心全量细则对账留痕”，生成机械追踪表：
  - `10_framework_validation/v5_8_27_core_rubric_alignment_audit_20260521.md`
  - `10_framework_validation/v5_8_27_core_rubric_alignment_audit_20260521.csv`
  - `10_framework_validation/v5_8_27_core_rubric_atom_trace_20260521.csv`
- 对账结果：
  - 27 核心 clean rubric atom 总数 133。
  - clean atom ID 在 `merged_rubric_atoms_subjective.csv` 中缺失 0。
  - 审计残留命中 0。
  - 机械追踪分布：10 个 `PASS_TRACE`，17 个 `PASS_WITH_MANUAL_CHECK`。
- 注意：该表是留痕与机械追踪，不替代最终语义阅卷；Word/PDF 前仍需结合 GPTPro/Claude 双审对弱追踪项做人工语义确认。

Governor decision: P2_TRACE_PREPARED_NOT_FINAL.

## STEP_95_GPTPRO_V5_8_FINAL_GATE_CAPTURED (2026-05-21 04:42 CST)

- GPTPro V5.8 终审已自然完成并写入：`06_open_observations/gptpro_v5_8_final_gate_review_20260521.md`。
- GPTPro 裁定：`PASS / YES_WITH_GUARDS`。
- 关键结论：
  - V5.8 已解决 V5.7 的 P1 入口过宽问题。
  - 可以进入 Word/PDF candidate，但必须保留 27 核心 + 38 保分/边界/回源索引口径。
  - 不得把本稿说成 65 题全部核心满分闭环。
- 状态文件已同步：`tool_outputs/gptpro_v5_8_final_gate_status_20260521.md`。

## STEP_96_V5_8_DUAL_GATE_COMPARISON_AND_V5_9_PATCH (2026-05-21 04:50 CST)

- 已生成 GPTPro 与 Claude Opus V5.8 终审交叉比较：
  - `07_cross_validation/v5_8_gptpro_claude_final_gate_comparison_20260521.md`
  - `07_cross_validation/v5_8_gptpro_claude_final_gate_comparison_20260521.csv`
- 双审共同结论：无 P0；V5.8 可进入带 guard 的 Word/PDF candidate。
- Codex 按更严格口径生成 V5.9 门禁修补版：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v5_9_27核心38题保分索引_双审门禁修补版_20260521.md`
  - `12_final_baodian/question_by_question_framework_runs_v5_9_27core65guard_20260521.csv`
  - `04_merge_audit/merged_rubric_atoms_subjective_v5_9_cleaned_cc0150_20260521.csv`
  - `04_merge_audit/cc0150_cross_module_rubric_atoms_excluded_v5_9_20260521.csv`
  - `04_merge_audit/merged_material_atoms_subjective_v5_9_cleaned_cc0223_20260521.csv`
  - `04_merge_audit/cc0223_reference_explanation_material_atoms_marked_audit_v5_9_20260521.csv`
  - `10_framework_validation/v5_9_dual_gate_patch_report_20260521.md`
- 修补内容：低频题视觉红线、CSV 主辅卡字段同步、CC0223 材料触发清理、CC0150 跨模块原子副本清洗、CC0103/RECOVER_2026_西城二模等空泛表达收束。

## STEP_97_V5_9_DOCX_PDF_QA_CANDIDATE (2026-05-21 05:00 CST)

- 已生成 V5.9 DOCX：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v5_9_27核心38题保分索引_双审门禁修补版_20260521.docx`
- 已用 Microsoft Word 导出 V5.9 PDF：
  - `12_final_baodian/word_pdf_v5_9/选必二法律主观题满分训练宝典_v5_9_27核心38题保分索引_双审门禁修补版_20260521.pdf`
- 已渲染 33 页 PNG：
  - `12_final_baodian/word_pdf_v5_9/rendered_pngs/`
- QA 报告：
  - `12_final_baodian/DOCX_PDF_QA_V5_9_20260521.md`
- QA 结论：
  - PDF 33 页。
  - 空白页嫌疑 0。
  - 首页面明确 V5.9、GPTPro/Claude 均 PASS / YES_WITH_GUARDS、27 核心 + 38 保分索引。
  - source-check/reference-only/boundary/low-frequency/transfer 红线均保留。
  - 已修复一次导出脚本中的 `\1` 残留问题并重新生成 DOCX/PDF。
- 当前裁定：V5.9 可作为 Word/PDF candidate 给用户阅读，但仍不能宣称 65 题全部核心满分闭环；后续若要最终发布，应继续做抽样盲测和 source-check 回源。

## STEP_98_V5_9_ZERO_BASELINE_BLIND_TEST (2026-05-21 05:08 CST)

- 已构造 V5.9 抽样盲测题面包：
  - `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/clean_questions_no_rubric_v5_9_20260521.md`
  - `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/sample_manifest_v5_9_20260521.csv`
  - `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/grading_key_v5_9_20260521.csv`
- 已调用零基础学生 agent 作答：
  - `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/agent_student_answers_v5_9_20260521.md`
- Codex 阅卷报告：
  - `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/codex_grading_report_v5_9_20260521.md`
  - `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/codex_grading_report_v5_9_20260521.csv`
- 结果：`PASS_WITH_GUARDS`。
- 样本覆盖：4 道 strict_core、1 道 low_frequency、1 道 source_check、1 道 reference_only、1 道 boundary。
- 关键结论：学生能对核心题写出接近满分答案；对非核心题没有误升核心，能保留低频/source-check/reference-only/boundary 边界。
- 新增同步文件：
  - `12_final_baodian/non_core_guardrails_v5_9_20260521.csv`
- 发现的 P2：`CC0244` 在 V5.9 核心 CSV 中已有两问，但盲测题面包从 canonical question row 抽取 `ask_text` 时只带出第（1）问；后续应修 source-card 或题面包生成逻辑。

## STEP_99_CC0244_DERIVED_ASK_PATCH (2026-05-21 05:12 CST)

- 已为 `CC0244_2026_东城_期末_18` 生成 V5.9 派生 ask_text 补丁，不覆盖 STEP_29 canonical：
  - `04_merge_audit/cc0244_ask_text_patch_v5_9_20260521.csv`
  - `04_merge_audit/cc0244_ask_text_patch_v5_9_20260521.md`
  - `04_merge_audit/merged_subjective_law_questions_v5_9_ask_patch_cc0244_20260521.csv`
- 补丁内容：把 ask_text 从单问“分析法律责任及法律依据”同步为 V5.9 核心 CSV 中的两问文本，包括“维权成功需要做好充分准备和策略选择”。
- 裁定：这是 derived patch，方便 V5.9/盲测/后续生成使用；正式覆盖 canonical 仍需 source-card review。

## STEP_100_V5_9_ATTACK_REVIEW_COUNCIL (2026-05-21 05:27 CST)

- 用户明确否定 V5.9 的学生可用性后，本阶段不再把 V5.9 视为可满意成稿，而是视为待攻击样稿。
- 已构造攻击审查包：
  - `05_reasoner_packets/v5_9_attack_review_council_20260521/`
  - `05_reasoner_packets/v5_9_attack_review_council_20260521.zip`
- 已提交 GPTPro 攻击审查：
  - `tool_outputs/gptpro_v5_9_attack_review_status_20260521.md`
  - 状态：`submitted_running`
- 已提交 Claude Opus 4.7 Cowork 攻击审查：
  - `tool_outputs/claude_opus_v5_9_attack_review_status_20260521.md`
  - 预期输出：`06_open_observations/claude_opus_v5_9_attack_review_20260521.md`
  - 状态：`submitted_running`
- 已启动本地零基础学生/刻薄阅卷人并行压测 agent：
  - 预期输出：`06_open_observations/codex_agent_student_attack_review_v5_9_20260521.md`
- 当前策略：等待 GPTPro、Claude、本地 agent 三方攻击结论后，合并为 V6 重构方案；V6 必须吸收先前框架 DNA 的学生启动性，同时保留 65 题证据底座与 27 核心 + 38 非核心边界纪律。

## STEP_101_V5_9_ATTACK_REVIEW_SYNTHESIS_AND_V6_WORKING_DRAFT (2026-05-21 CST)

- 已捕获 GPTPro V5.9 攻击审查：
  - `06_open_observations/gptpro_v5_9_attack_review_20260521.md`
  - 裁定：`PASS_WITH_MAJOR_REWRITE`
- 已确认 Claude Opus 4.7 Cowork 攻击审查落盘：
  - `06_open_observations/claude_opus_v5_9_attack_review_20260521.md`
  - 裁定：`PASS_WITH_MAJOR_REWRITE`
- 已合并 GPTPro / Claude / Codex A / 本地零基础学生 agent 四方攻击结论：
  - `07_cross_validation/v5_9_attack_review_synthesis_20260521.md`
- 已生成 V6 学生启动重构工作稿：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_学生可用工作稿_20260521.md`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_攻击审查融合工作稿_20260521.md`
  - `09_candidate_frameworks/framework_v6_student_working_rebuild_plan_20260521.md`
  - `scripts/build_v6_student_working_handbook.py`
- V6 已吸收的硬修正：
  - 首页改为设问尾词诊断树。
  - 新增三型答案骨架：判断型、意义型、表格型。
  - 新增题级禁用词总表和易混题对照框。
  - 27 核心按战场/学习单元重排，不再按题源流水堆叠。
  - 每道核心题新增三句保底答案。
  - 38 非核心题新增适用设问与不适用设问。
- 当前裁定：V5.9 带标签盲测作废；V6 后续必须做裸题盲测，隐藏 question_id、category、core/guard 标签，只给材料和设问。

## STEP_102_V6_NAKED_BLIND_TEST_AND_V6_2_EXTERNAL_REVIEW_RUNNING (2026-05-21 06:15 CST)

- 已完成 V6 裸题盲测 v2：
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/clean_questions_no_labels_v6_20260521_v2.md`
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/agent_student_answers_v6_naked_20260521_v2.md`
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/internal_grading_key_v6_20260521_v2.csv`
- Codex 严判已落盘：
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/codex_grading_report_v6_naked_20260521_v2.md`
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/codex_grading_report_v6_naked_20260521_v2.csv`
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/V6_NAKED_BLIND_TEST_VERDICT_20260521.md`
- 本地零基础学生复核 agent 严判已落盘：
  - `06_open_observations/codex_agent_v6_naked_blind_review_20260521.md`
- 已生成 V6.1 与 V6.2 学生稿候选：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_1_裸题盲测修补稿_20260521.md`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_2_裸题严判硬点修补稿_20260521.md`
- V6.2 修补内容：
  - CC0244 产品责任无过错责任前置。
  - 表格题禁止“如果表格要求……”式条件答法，改为按格直接填写。
  - CC0137 AI 著作权主体排除前置。
  - source-check/reference-only 继续不得升核心。
- 已构造 V6.2 外部二审包：
  - `05_reasoner_packets/v6_2_naked_blind_external_review_20260521/`
  - `05_reasoner_packets/v6_2_naked_blind_external_review_20260521.zip`
  - `handoff_prompts/PROMPT_FOR_GPTPRO_AND_CLAUDE_V6_2_NAKED_BLIND_REVIEW_20260521.md`
- 已提交 GPTPro 与 Claude Opus 4.7 二次攻击复核：
  - `tool_outputs/gptpro_v6_2_naked_blind_review_status_20260521.md`
  - `tool_outputs/claude_opus_v6_2_naked_blind_review_status_20260521.md`
- 当前裁定：允许等待并捕获双模型二审；不允许 Word/PDF 封版，不允许宣布“学生读完稳定满分”。

## STEP_103_V6_3_LOCAL_HYGIENE_PATCH_WHILE_EXTERNAL_REVIEW_RUNNING (2026-05-21 CST)

- 在等待 GPTPro / Claude Opus V6.2 二审期间，Codex A 对 V6.2 做本地自查，不等外审也能确认的硬伤先修。
- 已生成本地硬修候选：
  - `scripts/build_v6_3_local_hygiene_patch.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_3_本地自查硬修候选稿_20260521.md`
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/v6_3_local_hygiene_patch_report_20260521.md`
- 本地修补点：
  - 删除 V6.2 中类似预设口诀的“一二三四五总图 / 两条线 / 三问 / 四步 / 五类”前台表达。
  - 把“主卡/辅卡”及“认产权·抓侵权”等后台标签改成学生可理解的“考场入口/可补方向/知识产权或竞争侵权判断”等任务语言。
  - 修正表格题中“三句保底”误写“先判合同”的模板污染。
  - 把“第二个关键事实/最后落点”改成“第二层材料/得分落点”，降低未填模板感。
  - 在满分句零件前增加“可拼装零件，不是整段背诵”的刹车。
- 当前裁定：V6.3 只是本地自查硬修候选，不替代 GPTPro / Claude Opus 二审；最终仍需捕获双审输出后形成 V6.4 或封版裁定。

## STEP_104_V6_2_DUAL_EXTERNAL_REVIEW_CAPTURED_AND_V6_4_PATCH (2026-05-21 CST)

- 已捕获 GPTPro V6.2 裸题二审：`06_open_observations/gptpro_v6_2_naked_blind_review_20260521.md`。
- 已捕获 Claude Opus V6.2 裸题二审：`06_open_observations/claude_opus_v6_2_naked_blind_review_20260521.md`。
- 已生成双审比较：
  - `07_cross_validation/v6_2_gptpro_claude_naked_review_comparison_20260521.md`
  - `07_cross_validation/v6_2_gptpro_claude_naked_review_comparison_20260521.csv`
- 双审共同裁定：V6.2 为 `CONDITIONAL_PASS`，不得宣称学生读完稳定满分；必须修 C/E/G/H 和 source/ask 口径。
- 已生成 V6.4 双外审硬修候选：
  - `scripts/build_v6_4_dual_review_patch.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_4_双外审硬修候选稿_20260521.md`
  - `10_framework_validation/v6_naked_blind_test_20260521_v2/v6_4_dual_review_patch_report_20260521.md`

## STEP_105_V6_4_REGRESSION_AND_V6_5_PATCH (2026-05-21 CST)

- 已构造 V6.4 C/E/G/H 回归裸题包：
  - `10_framework_validation/v6_4_regression_naked_test_20260521/clean_questions_CEGH_v6_4_regression_20260521.md`
  - `10_framework_validation/v6_4_regression_naked_test_20260521/internal_grading_key_CEGH_v6_4_regression_20260521.csv`
- 已调用零基础聪明学生 agent 只读 V6.4 与干净题包作答：
  - `10_framework_validation/v6_4_regression_naked_test_20260521/student_answers_CEGH_v6_4_regression_20260521.md`
- Codex 严判结果：`CONDITIONAL_PASS`，3 PASS + 1 PARTIAL；唯一缺口是通州表格题材料事实格缺“因果/非因果”硬词：
  - `10_framework_validation/v6_4_regression_naked_test_20260521/grading_report_CEGH_v6_4_regression_20260521.md`
  - `10_framework_validation/v6_4_regression_naked_test_20260521/V6_4_REGRESSION_VERDICT_20260521.md`
- 已生成 V6.5 窄补丁：
  - `scripts/build_v6_5_regression_patch.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_5_回归盲测因果硬词补丁稿_20260521.md`
  - `10_framework_validation/v6_4_regression_naked_test_20260521/v6_5_regression_patch_report_20260521.md`
- 已做样题 2 一题最小回归，裁定 `PASS`：
  - `10_framework_validation/v6_4_regression_naked_test_20260521/student_answer_sample2_v6_5_miniregression_20260521.md`
  - `10_framework_validation/v6_4_regression_naked_test_20260521/V6_5_MINI_REGRESSION_VERDICT_20260521.md`

## STEP_106_V6_7_STUDENT_USABLE_VERSION_DOCX (2026-05-21 CST)

- 已从 V6.5 剥离工程修补记录，生成学生清洁候选稿和教师证据说明：
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_6_学生清洁候选稿_20260521.md`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_6_教师证据说明_20260521.md`
- 已进一步抛光为学生使用版：
  - `scripts/polish_v6_6_student_clean.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.md`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_7_学生使用版_抛光报告_20260521.md`
- 已导出 DOCX：
  - `scripts/export_v6_7_student_docx.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.docx`
  - `12_final_baodian/DOCX_EXPORT_V6_7_STUDENT_20260521.md`
- 已做结构 QA 与 QuickLook 首屏缩略图 QA：
  - `12_final_baodian/DOCX_QA_V6_7_STUDENT_20260521.md`
  - `12_final_baodian/word_pdf_v6_7_student/qlthumb/选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.docx.png`
- 注意：本机缺少 `soffice`，Microsoft Word AppleScript 导出 PDF 超时；因此 V6.7 DOCX 不能标为全页视觉 QA 通过，也暂未生成最终 PDF。

## STEP_107_V6_7_FINAL_STUDENT_REVIEW_PACKET_READY (2026-05-21 CST)

- 已构造 V6.7 GPTPro / Claude Opus 最终学生可用性审稿包：
  - `05_reasoner_packets/v6_7_final_student_usability_review_20260521/`
  - `05_reasoner_packets/v6_7_final_student_usability_review_20260521.zip`
  - `05_reasoner_packets/v6_7_final_student_usability_review_20260521/PACKET_README.md`
  - `05_reasoner_packets/v6_7_final_student_usability_review_20260521/PROMPT_FOR_GPTPRO_AND_CLAUDE_V6_7_FINAL_STUDENT_REVIEW_20260521.md`
  - `05_reasoner_packets/v6_7_final_student_usability_review_20260521/VISIBLE_PROMPT_ASCII_FOR_WEB_UPLOAD_20260521.txt`
- 已同步 handoff prompt：
  - `handoff_prompts/PROMPT_FOR_GPTPRO_V6_7_FINAL_STUDENT_REVIEW_20260521.md`
  - `handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_V6_7_FINAL_STUDENT_REVIEW_20260521.md`
- 已写入待投递状态：
  - `tool_outputs/gptpro_v6_7_final_student_review_status_20260521.md`
  - `tool_outputs/claude_opus_v6_7_final_student_review_status_20260521.md`
- 审稿包要求 GPTPro / Claude 不再只审证据安全，而是扮演“零基础聪明高三学生 + 严苛阅卷人”，给出 `PASS / CONDITIONAL_PASS / FAIL` 与 P0/P1/P2 可执行修订意见。
- 由于用户此前指出 GPT 页面乱码、Claude 被重复发送按钮打断，本步先固化干净审稿包和 ASCII 可见提示；直接 UI 投递必须一次完成并等待自然输出，不得多次点击发送。

## STEP_108_V6_8_TABLE_HEAD_REPAIR_AND_REVIEW_PACKET_READY (2026-05-21 CST)

- Codex A 对 V6.7 做本地硬审，发现第一个“表格补全战场”核心题缺少题源标题与 1-6 小节，直接从“完整考场版答案”开始，属于学生使用硬伤。
- 已生成 V6.8 窄修复稿：
  - `scripts/build_v6_8_table_head_patch.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_8_表格题头部修复学生使用版_20260521.md`
  - `12_final_baodian/V6_8_TABLE_HEAD_PATCH_REPORT_20260521.md`
- 已导出 V6.8 DOCX 并完成结构 QA + QuickLook 首屏检查：
  - `scripts/export_v6_8_student_docx.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_8_表格题头部修复学生使用版_20260521.docx`
  - `12_final_baodian/DOCX_EXPORT_V6_8_STUDENT_20260521.md`
  - `12_final_baodian/DOCX_QA_V6_8_STUDENT_20260521.md`
  - `12_final_baodian/word_pdf_v6_8_student/qlthumb/选必二法律主观题满分训练宝典_v6_8_表格题头部修复学生使用版_20260521.docx.png`
- V6.7 外审包已作废，改为 V6.8 外审包：
  - `05_reasoner_packets/v6_8_final_student_usability_review_20260521/`
  - `05_reasoner_packets/v6_8_final_student_usability_review_20260521.zip`
  - `handoff_prompts/PROMPT_FOR_GPTPRO_V6_8_FINAL_STUDENT_REVIEW_20260521.md`
  - `handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_V6_8_FINAL_STUDENT_REVIEW_20260521.md`
  - `tool_outputs/gptpro_v6_8_final_student_review_status_20260521.md`
  - `tool_outputs/claude_opus_v6_8_final_student_review_status_20260521.md`
- V6.8 只修复表格核心题头部，不改变 65 题 corpus，不改变 61/4/0 证据统计，不把 38 非核心升核心。

## STEP_109_V6_9_RESTORE_CORE18_AND_REPLACE_REVIEW_PACKET (2026-05-21 CST)

- 对 V6.8 做 27 核心题完整性审计，发现只有 26 个 `核心题` 标题；缺失的是 `RECOVER_2025_海淀_二模_18`（2025 海淀二模第18题，商标/回避/旁听笔记补全题）。
- 已恢复核心题 18，并生成 V6.9：
  - `scripts/build_v6_9_restore_core18.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_9_恢复27核心完整学生使用版_20260521.md`
  - `12_final_baodian/V6_9_RESTORE_CORE18_REPORT_20260521.md`
  - `10_framework_validation/v6_9_core_section_integrity_audit_20260521.md`
  - `10_framework_validation/v6_9_core_section_integrity_audit_20260521.csv`
- V6.9 已导出 DOCX 并完成结构 QA + QuickLook 首屏检查：
  - `scripts/export_v6_9_student_docx.py`
  - `12_final_baodian/选必二法律主观题满分训练宝典_v6_9_恢复27核心完整学生使用版_20260521.docx`
  - `12_final_baodian/DOCX_EXPORT_V6_9_STUDENT_20260521.md`
  - `12_final_baodian/DOCX_QA_V6_9_STUDENT_20260521.md`
- V6.8 外审包已作废，改为 V6.9 外审包：
  - `05_reasoner_packets/v6_9_final_student_usability_review_20260521/`
  - `05_reasoner_packets/v6_9_final_student_usability_review_20260521.zip`
  - `handoff_prompts/PROMPT_FOR_GPTPRO_V6_9_FINAL_STUDENT_REVIEW_20260521.md`
  - `handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_V6_9_FINAL_STUDENT_REVIEW_20260521.md`
  - `tool_outputs/gptpro_v6_9_final_student_review_status_20260521.md`
  - `tool_outputs/claude_opus_v6_9_final_student_review_status_20260521.md`
- 当前裁定：V6.9 才是目前可投 GPTPro/Claude 的学生使用版候选；V6.7、V6.8 仅保留为历史修补链。
- 直接 UI 投递状态：ChatGPT app 被 Computer Use 安全策略禁止控制；Safari web 页面虽可见，但附件入口无法稳定命中，未发送任何消息、未上传任何文件。保持 `v6_9_final_student_usability_review_20260521.zip` 为待安全一次性投递包。
- 已完成 V6.9 学生版文本卫生扫描：
  - `10_framework_validation/v6_9_student_text_hygiene_scan_20260521.md`
  - 结果：`候选稿/reference_only/source-check/source_check/guard/index/主卡/辅卡/一二三四五/第二层材料/得分落点/placeholder/TODO` 均为 0。

## STEP_110_V7_METHOD_FIRST_BATCHED_EXTERNAL_REBUILD_PACKET (2026-05-21 CST)

- 用户最新裁定：不要继续让 GPTPro / Claude 直接吞 65 题硬推框架；必须先学习用户桌面先前优秀框架，再分批处理法律题后创建新框架。
- 已重新通过三层 SOP、选必二 skill、小本本和 cross-book workflow gate。
- 已生成 V7 方法学习优先包：
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521/`
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521.zip`
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521_METHOD_PACK.zip`
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521_BATCH_01.zip`
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521_BATCH_02.zip`
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521_BATCH_03.zip`
  - `05_reasoner_packets/v7_method_learning_batched_rebuild_20260521_BATCH_04.zip`
- 包内路径已全部 ASCII 化，`non_ascii_zip_paths=0`，避免 GPT 网页端文件名乱码。
- V7 包结构：先前框架 DNA + rendered samples + V6.9 失败候选 + 65 题证据全表 + 四个分批题包。
- 分批口径：BATCH_01 高频实体判断 10 题；BATCH_02 程序/表格 8 题；BATCH_03 创新/AI/价值 9 题；BATCH_04 非核心开放容器 38 题。
- 证据基线仍为 65 题，61 formal，4 reference_only，362 rubric atoms。
- 已投递 GPTPro：Safari ChatGPT conversation `https://chatgpt.com/c/6a0c3288-938c-83ea-bca9-66b8db9d9326`，上传完整 ZIP 并提交 method-first 短提示；状态 running/thinking。
- 已投递 Claude Opus 4.7：Claude Desktop Cowork local session `local_b69508aa-75f6-4ed5-abeb-a64598c7336e`，使用本地目录和同一 prompt；状态 running/responding。
- 当前裁定：外审结果尚未捕获，不得生成 V7 定稿，不得宣布学生满分闭合；允许等待并捕获双模型输出。

## STEP_111_V7_SOURCE_CARD_PATCH_AND_GPT_SPLIT_RETRY_2026-05-21

- Claude Opus Cowork completed V7 method-first rebuild output and returned `CONDITIONAL_PASS_TO_REWRITE`.
- Captured Claude output to `06_open_observations/claude_opus_v7_method_first_rebuild_20260521.md`.
- GPTPro full-zip retry was replaced by split submission: METHOD_PACK uploaded first; prompt asks only for METHOD_LEARNING_NOTES and WHY_V6_9_STILL_NOT_ENOUGH.
- Created source-card patch files before V7 writing:
  - `04_merge_audit/v7_source_card_patch_plan_20260521.md`
  - `04_merge_audit/v7_source_card_patch_decisions_20260521.csv`
  - `04_merge_audit/v7_cleaned_source_cards_preview_20260521.md`
- Current gate: do not write final V7 until GPTPro method-stage output is captured and batch 01-04 are either processed externally or explicitly marked pending.

## STEP_112_V7_GPTPRO_FINAL_CAPTURED_AND_METHOD_SYNTHESIS_2026-05-21

- GPTPro method stage、BATCH_01、BATCH_02、BATCH_03、BATCH_04 与 final proposal 均已捕获。
- GPTPro final output:
  - `09_candidate_frameworks/gptpro_v7_framework_proposal_20260521.md`
- 已生成双模型方法交叉对照：
  - `07_cross_validation/gptpro_claude_v7_method_comparison_20260521.md`
- 已生成 V7 方法优先综合稿：
  - `09_candidate_frameworks/framework_v7_method_first_synthesis_20260521.md`
- 共同裁定：放弃 V6.9 “九个战场”学生前台，改为“八个答案产品门 + 三大责任逻辑链 + 三档归责卡 + 材料翻译 + 五类保险箱”。
- 证据基线不变：65 题；61 formal；4 reference_only；0 missing；362 rubric/answer atoms。
- 当前裁定：允许生成 V7 学生候选稿与零基础压测；不允许终稿封版。

## STEP_113_V7_ZERO_BASELINE_PRESSURE_AND_V7_1_PATCH_2026-05-21

- 已生成 V7 候选学生稿：
  - `12_final_baodian/选必二法律主观题满分宝典_v7_方法先行候选稿_20260521.md`
  - `12_final_baodian/V7_METHOD_FIRST_BAODIAN_BUILD_REPORT_20260521.md`
- 已生成零基础压力包并调用学生 agent 作答：
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/clean_student_packet_v7_method_first_20260521.md`
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/student_answers_v7_method_first_zero_baseline_20260521.md`
- 首轮严判结果：
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/grading_report_v7_method_first_zero_baseline_20260521.md`
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/V7_METHOD_FIRST_ZERO_BASELINE_VERDICT_20260521.md`
  - 统计：PASS=3；CONDITIONAL_PASS=2；PARTIAL=5；FAIL=0。
- 已按压力测试缺口生成 V7.1 压测补丁候选稿：
  - `12_final_baodian/选必二法律主观题满分宝典_v7_1_压测补丁候选稿_20260521.md`
  - `12_final_baodian/V7_1_PRESSURE_PATCH_BAODIAN_BUILD_REPORT_20260521.md`
- 已进行 5 题定向回归：
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/clean_student_packet_v7_1_targeted_regression_20260521.md`
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/student_answers_v7_1_targeted_regression_20260521.md`
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/grading_report_v7_1_targeted_regression_20260521.md`
  - `10_framework_validation/v7_method_first_zero_baseline_pressure_20260521/V7_1_TARGETED_REGRESSION_VERDICT_20260521.md`
- 定向回归结果：PASS=3；CONDITIONAL_PASS=2；PARTIAL=0；FAIL=0。
- 本轮已修复的学生失分点：
  - 消费欺诈：从“搭售/不知情/不能拒绝”稳定落到欺诈和三倍赔偿。
  - 无人机责任：区分销售者过错、合同损失、人身侵权损害。
  - AI 幻觉：稳定判断 AI 非民事主体、公司真实意思表示、实际损害。
- 仍不可封版的原因：
  - 海淀二模商标表格题真实空格未回源入压力包。
  - 4 道 reference_only 题不能进入核心满分闭环。
  - 19 个 canonical ask_text 为空题仍需 source-card repair 或降级。
  - `CC0223`、`CC0150`、`CC0244` 仍需题卡清洗和教师证据说明。

## STEP_114_V7_1_SOURCE_REPAIR_QUEUE_2026-05-21

- 已按用户“先让 GPTPro/Claude 学先前框架方法，再分批上传题”的方向核验 V7 线：GPTPro method stage、BATCH_01—04、final proposal 均已捕获；Claude Opus Cowork 输出已捕获。
- 已确认当前证据底座：65 道主观题，61 formal，4 reference_only，0 missing；V7.1 候选稿不封版。
- 已整理 V7.1 source-card repair 队列：
  - `04_merge_audit/v7_1_source_repair_queue_20260521.csv`
  - `04_merge_audit/v7_1_source_repair_queue_20260521.md`
- 队列覆盖：19 个 canonical ask_text 为空题 + `CC0223`、`CC0150`、`CC0244` 三张高风险题卡，共 22 行。
- 决策分布：repair_now 6；source_confirm_required 10；split_subquestion_only 1；downgrade_insurance_box 1；reference_only_lock 1；clean/split high-risk cards 3。
- 当前裁定：允许继续做 source repair、教师证据说明、DOCX 草稿；不允许把 V7.1 称为最终满分宝典。

## STEP_115_V7_1_TEACHER_EVIDENCE_PATCH_2026-05-21

- 已从 source repair queue 中筛出可安全用于 V7.1 教师证据草稿的 10 行，不包含 source_confirm_required、downgrade_insurance_box、reference_only_lock 行。
- 新增输出：
  - `04_merge_audit/v7_1_teacher_evidence_patch_20260521.csv`
  - `04_merge_audit/v7_1_teacher_evidence_patch_20260521.md`
- 补丁范围：6 个 ask_text_patch；1 个法律小问拆分；`CC0223` 清洁材料/设问；`CC0150` 剔除跨模块 rubric 污染；`CC0244` 拆责任链与维权准备链。
- 当前裁定：V7.1 教师证据说明可以使用这些补丁；canonical 合并表仍不直接覆盖，source_confirm_required 行继续阻断最终封版。

## STEP_116_V7_1_CORE_ARTIFACTS_FOR_USER_GPT_2026-05-21

- 用户认为当前框架仍不够好，要求把当前核心产物整理给用户自行发 GPT。
- 已生成干净上传包：
  - `05_reasoner_packets/v7_1_core_artifacts_for_user_gpt_20260521/`
  - `05_reasoner_packets/v7_1_core_artifacts_for_user_gpt_20260521.zip`
- 包内 22 个文件，路径和文件名全部 ASCII，包含：当前 V7.1 候选宝典、旧框架 DNA、法律改写规格、GPTPro/Claude V7 输出、交叉对照、压测结论、source repair 队列、教师证据补丁、65 题 merged evidence CSV。
- 包内提示词：
  - `00_PROMPT_FOR_GPT_REVIEW_AND_REBUILD.md`
  - `VISIBLE_PROMPT_SHORT_FOR_GPT.txt`
- 当前裁定：这是给 GPT 继续批判和重做的核心包，不是最终交付包。

## STEP_117_V8_STUDENT_USABLE_REBUILD_DIAGNOSIS_2026-05-21

- 用户明确否定 V7.1 学生可用性，要求停止小修小补，启动 `v8_student_usable_rebuild`。
- 当前唯一闭合语料口径改回并锁定为：
  - `04_merge_audit/boundary_patched_20260519/`
  - 53 道 framework-ready 主观题。
  - 535 个材料原子。
  - 53 个设问原子。
  - 319 个细则原子。
  - 37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE。
- 明确禁止进入闭合正文：
  - `CC0094_2025_东城_期末_19_3`
  - `CC0259_2026_丰台_期中_19`
  - `CC0118_2025_丰台_期末_18_2`
  - 已剔除 `CC0250_2026_丰台_一模_19`
  - 继续禁止 CC0229 旧坏词：`逃逸粒子`、`创新资源集聚`、`空间布局精准`、`全链条产业生态`
- 已创建 v8 工作目录：
  - `v8_student_usable_rebuild/`
- 已完成 STEP 2 失败诊断：
  - `v8_student_usable_rebuild/01_v7_failure_diagnosis.md`
  - `v8_student_usable_rebuild/01_v7_failure_diagnosis.csv`
- 诊断结论：`FAIL_TO_REBUILD`。V7.1 当前形态仍像工程验收包、证据侧栏和答案汇编，不能作为学生考场可启动版本。
- 关键诊断数据：
  - 诊断记录 78 条。
  - `question_by_question_framework_runs_boundary_patched.csv` 中 23 行设问触发缺失或需回源。
  - 53 行最小必要判断均为同一泛化句，无法教学生第一步判断。
  - 24 行完整答案/满分句字段存在原答案、参考答案、评分说明式复述。
  - 5 行 OPEN_OR_REFERENCE 已确认只能参考运行，不能支撑核心节点。
- 当前裁定：允许进入 STEP 3，构造 GPT-5.5 Pro 与 Claude Opus 同题同问诊断/金样板建议包；仍禁止写 v8 总框架，直到 8 道金样板完成。

## STEP_118_V8_EXTERNAL_MODEL_PACKET_SUBMITTED_2026-05-21

- 已生成 v8 外审输入包：
  - `v8_student_usable_rebuild/00_model_packet/v8_diagnosis_gold_selection_packet_20260521.zip`
  - 同步副本：`05_reasoner_packets/v8_diagnosis_gold_selection_packet_20260521.zip`
- 包内 25 个文件，文件名全部 ASCII，中文正文为 UTF-8；包含 STEP 2 失败诊断、53 题 boundary-patched 合并表、逐题运行、触发库、句库、覆盖矩阵和 v7.1 候选稿。
- 已保存统一 prompt：
  - `v8_student_usable_rebuild/PROMPT_FOR_GPT55PRO_V8_DIAGNOSIS_GOLD_SELECTION.md`
  - `v8_student_usable_rebuild/PROMPT_FOR_CLAUDE_OPUS_V8_DIAGNOSIS_GOLD_SELECTION.md`
  - `v8_student_usable_rebuild/00_model_packet/00_SHARED_PROMPT_FOR_GPT_AND_CLAUDE.md`
- 已真实投递 GPT-5.5 Pro / ChatGPT 项目对话：
  - Safari 标题：`必修四喂细则 - 选必二框架设计`
  - 状态：`Pro 思考中`
- 已真实投递 Claude Opus 4.7 / Cowork：
  - Claude Desktop local session: `local_5bf2fdae-6bdf-470b-bdfd-11a9465aeefe`
  - 状态：`Running / Starting up`
- 已记录外审调用状态：
  - `v8_student_usable_rebuild/00_model_packet/external_model_call_status_20260521.md`
- 当前裁定：等待并捕获 GPT/Claude 输出；在等待期间只允许做本地候选池扫描，不允许最终确定 8 金样板，不允许写 v8 总框架。


## STEP_119_V8_GPT_CLAUDE_CAPTURE_AND_GOLD_SELECTION_20260521
- 时间：2026-05-21 17:53 CST
- 已完成：GPT-5.5 Pro 完整输出保存为 `v8_student_usable_rebuild/02_model_outputs/gpt55pro_v8_diagnosis_gold_framework.md`（1496 行）。
- 已完成：Claude Opus 4.7 输出保存为 `v8_student_usable_rebuild/02_model_outputs/claude_opus_v8_diagnosis_gold_framework.md`（443 行）。
- 已完成：`v8_student_usable_rebuild/02_gold_standard_question_selection.md`。
- 已完成：`v8_student_usable_rebuild/02_gold_standard_question_runs.md`。
- 金样板正式 8 题：CC0137、CC0238、CC0305、CC0054、CC0103、CC0025、CC0125、CC0002。
- 门槛状态：8 道金样板完成，允许进入 STEP 6 学生版框架；仍禁止跳过学生版框架直接写 53 题或最终宝典。


## STEP_120_V8_STUDENT_FRAMEWORK_SENTENCEBANK_AND_53_RUNS_20260521
- 时间：2026-05-21 18:02 CST
- 已完成：`v8_student_usable_rebuild/03_student_exam_framework_v8.md`。
- 已完成：`v8_student_usable_rebuild/04_teacher_evidence_framework_v8.md` 与 `.csv`。
- 已完成：`v8_student_usable_rebuild/05_full_score_sentence_bank_v8.md` 与 `.csv`，21 条可迁移句式。
- 已完成：`v8_student_usable_rebuild/06_question_by_question_runs_v8.md` 与 `.csv`，53 行全量运行；47 PASS_RUN_DRAFT，5 REFERENCE_RUN，1 BOUNDARY_RUN。
- 门槛状态：允许进入 STEP 10 重写宝典；仍需完成学生可用性模拟验收后才能标记 v8 完成。

## STEP_121_V8_BAODIAN_AND_ACCEPTANCE_20260521
- 时间：2026-05-21 18:18 CST
- 已完成：`v8_student_usable_rebuild/07_选必二法律主观题满分宝典_v8.md`。
- 已完成：`v8_student_usable_rebuild/07_选必二法律主观题满分宝典_v8.docx`。
- 已完成：`v8_student_usable_rebuild/08_v8_student_usability_test.md`。
- 已完成：`v8_student_usable_rebuild/08_v8_acceptance_report.md`。
- 验收结果：`CONDITIONAL_PASS`。
- 关键数据：8 道金样板全部 formal，0 OPEN_OR_REFERENCE；53 题运行完整，47 PASS_RUN_DRAFT，5 REFERENCE_RUN，1 BOUNDARY_RUN；学生模拟抽测 5/5 PASS。
- 句库修订：学生模拟验收后新增消费者欺诈/撤销权句式与多方过错/未成年打赏句式，`05_full_score_sentence_bank_v8.csv` 增至 23 条。
- 边界控制：OPEN_OR_REFERENCE 仅参考运行；pending 三题未回流；CC0250 未回流；CC0229 四个旧坏词未进入学生/宝典核心产物。
- 未标 full PASS 的原因：非金样板 45 题仍属批量草拟运行，需下一轮人工课堂口吻精修；部分原始 ask 缺失仍需回源补齐。

## STEP_122_V8_USER_GPT_REVIEW_PACKET_20260521

- 时间：2026-05-21 20:42 CST
- 用户要求：打包需要发给 GPT 的内容。
- 已完成目录：`v8_student_usable_rebuild/09_packet_for_user_gpt_review_20260521/`。
- 已完成压缩包：`05_reasoner_packets/v8_student_usable_for_gpt_review_20260521.zip`。
- 包内文件：17 个，含 README、GPT 审稿 prompt、学生框架、v8 宝典 MD/DOCX、验收报告、学生模拟验收、8 金样板、句库、53 题运行、教师证据框架、v7 失败诊断。
- 包大小：约 313K。
- 质量检查：包内核心学生/宝典稿件未命中 CC0229 四个禁用词；pending/CC0250 只在边界说明中出现。

## STEP_123_V8_1_STUDENT_DELIVERY_FIX_20260521

- 时间：2026-05-21 21:21 CST
- 触发原因：GPT 审稿判定 v8 学生框架和 8 金样板方向正确，但 53 题逐题运行与完整宝典不可交付。
- 已创建目录：`v8_1_student_delivery_fix/`。
- 已完成 v8 硬 QA 扫描：
  - `00_hard_QA_scan.md`
  - `00_hard_QA_scan.csv`
  - 初扫结论：v8 学生/逐题/宝典正文存在大量自动草稿、证据语言和占位痕迹，不能直接交付。
- 已完成 v8.1 修复产物：
  - `01_gold_runs_synced_report.md`
  - `02_ask_backfill_report.md`
  - `02_ask_missing_to_appendix_list.csv`
  - `03_priority_10_rewritten.md/.csv`
  - `04_student_framework_v8_1.md`
  - `05_full_score_sentence_bank_v8_1.md/.csv`
  - `06_teacher_evidence_framework_v8_1.md/.csv`
  - `07_选必二法律主观题满分宝典_v8_1.md/.docx`
  - `08_question_by_question_runs_v8_1_gold_synced.md/.csv`
  - `08_v8_1_acceptance_report.md`
  - `09_v8_1_hard_QA_rescan.md/.csv`
  - `10_docx_QA_note.md`
- 设问缺失处理：20 道中 16 道补设问；4 道移入附录，不进入学生版逐题正文。
- 逐题运行口径：49 题进入学生/参考运行正文；4 题附录；pending 三题和 CC0250 未回流。
- 硬 QA 复扫：学生正文命中数 0；教师证据框架未命中 gold 占位符和 CC0229 坏词。
- 已打包：`05_reasoner_packets/v8_1_student_delivery_fix_20260521.zip`。
- 验收结果：`CONDITIONAL_PASS`。原因是非优先题仍是清洗后的运行稿，不是逐题人工精雕版；DOCX 因本机缺少 `soffice` 未完成视觉渲染 QA。

## STEP_124_V9_FEIGE_STYLE_REBUILD_20260521

- 时间：2026-05-21 21:53 CST
- 用户裁定：停止 `v8_1_student_delivery_fix`，当前版本风格仍不像已成功的飞哥框架；不得继续修 53 题运行，不得继续工程验收化。
- 已启动新阶段：`v9_feige_style_rebuild`。
- 已完成旧框架风格学习，输入包括桌面“先前框架”中的哲学与文化、经济主体积累页、必修三、选必一、选必三 PDF，以及既有飞哥庄园/成熟框架 Markdown。
- 已完成文件：
  - `v9_feige_style_rebuild/01_飞哥旧框架风格DNA.md`
  - `v9_feige_style_rebuild/02_选必二法律主观题_先导.md`
  - `v9_feige_style_rebuild/03_选必二法律主观题_飞哥课堂版框架.md`
  - `v9_feige_style_rebuild/04_正向触发.md`
  - `v9_feige_style_rebuild/05_反向筛查.md`
  - `v9_feige_style_rebuild/06_高频答题语言.md`
  - `v9_feige_style_rebuild/07_10道极简演练.md`
  - `v9_feige_style_rebuild/08_v9_style_acceptance.md`
- 自检：v9 学生正文未命中 v8 工程词、证据编号词、CC0229 四个禁用坏词。
- 当前口径：v9 是“飞哥课堂主框架版”，不是 53 题完整附录版；后续若继续，应沿 v9 风格补题链，不得回到工程报告腔。

## STEP_125_V10_EXHAUSTIVE_FRAMEWORK_AND_ALL_QUESTIONS_20260521

- 时间：2026-05-21 22:53 CST
- 用户裁定：停止 `v9.1_classroom_booklet_polish`；用户从未要“金样板题/10 道演练”环节，真正结构应为“前面框架穷尽，后面所有题穷尽”。
- 已启动新阶段：`v10_exhaustive_framework_and_all_questions`。
- 唯一语料：`04_merge_audit/boundary_patched_20260519/` 的 53 道主观题；37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE。
- 已完成文件：
  - `v10_exhaustive_framework_and_all_questions/01_框架穷尽清单.csv`
  - `v10_exhaustive_framework_and_all_questions/01_框架穷尽清单.md`
  - `v10_exhaustive_framework_and_all_questions/02_上篇_选必二法律主观题穷尽框架.md`
  - `v10_exhaustive_framework_and_all_questions/03_下篇_53题全量题链.md`
  - `v10_exhaustive_framework_and_all_questions/03_下篇_53题全量题链.csv`
  - `v10_exhaustive_framework_and_all_questions/04_框架_题目_细则覆盖矩阵.csv`
  - `v10_exhaustive_framework_and_all_questions/04_框架_题目_细则覆盖矩阵.md`
  - `v10_exhaustive_framework_and_all_questions/05_v10_acceptance.md`
- 01 清单规模：65 个框架点，覆盖设问入口、材料触发、法律动作、得分语言、反向筛查五类。
- 03 下篇规模：53 道题全量进入；按 37/11/5 分组；5 道 OPEN_OR_REFERENCE 明确降级参考运行。
- 04 覆盖矩阵规模：65 行，记录每个框架点支撑题、支撑细则数量、formal/PASS_RECOVERED/OPEN_OR_REFERENCE 数量。
- 复扫结果：v10 上篇/下篇未命中“金样板/10 道极简演练/代表题演练/后续补 53 题”等禁用结构语；未命中 CC0229 四个坏词；未命中 page/slide/评分说明残留。
- 验收结果：`EXHAUSTIVE_FRAMEWORK_PASS`。

## STEP_126_V11_SOURCE_LOCKED_REBUILD_20260521

- 时间：2026-05-21 23:38 CST
- 用户/GPT 裁定：停止 v10，`v10_exhaustive_framework_and_all_questions/05_v10_acceptance.md` 作废；不得再引用 `EXHAUSTIVE_FRAMEWORK_PASS` 作为有效结论。
- 失败原因：v10 下篇 53 题存在题源错配、材料错配、触发错配；覆盖矩阵虚高；把评分细则、参考答案、分析说明或 OCR 串页误当材料触发。
- 已启动新阶段：`v11_source_locked_rebuild/`。
- 已完成文件：
  - `v11_source_locked_rebuild/01_53题回源审判表.csv`
  - `v11_source_locked_rebuild/01_53题回源审判报告.md`
  - `v11_source_locked_rebuild/01_53题回源审判_stats.json`
  - `v11_source_locked_rebuild/01A_关键污染题回源修复补丁.csv`
  - `v11_source_locked_rebuild/01A_关键污染题回源修复补丁.md`
  - `v11_source_locked_rebuild/02_强分诊框架清单.csv`
  - `v11_source_locked_rebuild/02_强分诊框架清单.md`
- 01 表口径：仍为 boundary-patched 53 题；37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE。
- 01A 修复：已回源修复 CC0011、CC0131、CC0137、CC0254、CC0289 五个 GPT 点名污染样例；连同 CC0002、CC0025、CC0143 等点名样例进入“重写”队列。
- 当前统计：保留 14；重写 10；降级参考 5；待用户确认 24；仍需回源修复 29。
- v11 当前结论：不得 PASS；只完成回源审判和强分诊闸门。下一步只能基于 01/02 写 source-locked 题链，待确认题不得硬写。

## STEP_127_V11_SOURCE_LOCKED_SKELETON_COMPLETED_20260521

- 时间：2026-05-21 23:59 CST
- 已继续完成 v11 后续骨架文件：
  - `v11_source_locked_rebuild/03_下篇_53题全量题链_v11.md`
  - `v11_source_locked_rebuild/03_下篇_53题全量题链_v11.csv`
  - `v11_source_locked_rebuild/04_上篇_选必二法律主观题强分诊框架.md`
  - `v11_source_locked_rebuild/05_真实覆盖矩阵.csv`
  - `v11_source_locked_rebuild/05_真实覆盖矩阵.md`
  - `v11_source_locked_rebuild/06_v11_acceptance.md`
  - `v11_source_locked_rebuild/06_v11_acceptance_stats.json`
- 03 题链状态：53 题全入名单；24 题正式题链；5 题降级参考题链；24 题待确认不硬写。
- 04 上篇：改用“强分诊”结构，不沿用 v10 泛化穷尽堆表。
- 05 矩阵：只统计真实支撑；待确认题不计入核心覆盖；OPEN_OR_REFERENCE 不单独支撑核心。
- 06 验收结论：`CONDITIONAL_PASS`。不得写 `SOURCE_LOCKED_PASS`。
- 硬 QA：02/03/04/05/06 正文向文件对硬污染词复扫 0 命中。

## STEP_128_V11_GPT_REVIEW_PACKET_20260521

- 时间：2026-05-21 23:42 CST
- 用户要求：给出可发给 GPT 审核的包。
- 已生成展开目录：
  - `v11_source_locked_rebuild/07_packet_for_gpt_review_20260521/`
  - `v11_source_locked_rebuild/07_packet_for_gpt_review_ascii_20260521/`
- 已生成压缩包：
  - `05_reasoner_packets/v11_source_locked_for_gpt_review_20260521.zip`
  - `05_reasoner_packets/v11_source_locked_for_gpt_review_ascii_20260521.zip`
- 推荐上传：ASCII 文件名版本 `v11_source_locked_for_gpt_review_ascii_20260521.zip`，避免网页端附件名乱码。
- 包内含 README、GPT 审核 prompt、01/01A/02/03/04/05/06 全部 v11 核心产物。

## STEP_129_V11_1_WRITTEN_CHAIN_PATCH_20260522

- 时间：2026-05-22 12:35 CST
- 用户/GPT 裁定：v11 方向正确，但不能进入 24 题回填；先修已写题链中的 P0 错误和版本残留。
- 已启动并完成阶段：`v11_1_written_chain_patch/`。
- 已完成文件：
  - `v11_1_written_chain_patch/01_source_judgment_table_final.csv`
  - `v11_1_written_chain_patch/01_source_judgment_report_final.md`
  - `v11_1_written_chain_patch/03_all_53_question_chains_v11_1.csv`
  - `v11_1_written_chain_patch/03_all_53_question_chains_v11_1.md`
  - `v11_1_written_chain_patch/04_upper_strong_triage_framework_v11_1.md`
  - `v11_1_written_chain_patch/05_true_coverage_matrix_v11_1.csv`
  - `v11_1_written_chain_patch/05_true_coverage_matrix_v11_1.md`
  - `v11_1_written_chain_patch/06_v11_1_acceptance.md`
- 题链数量：53 行保持不变；37 PASS；10 PASS_RECOVERED；1 题标注 `PASS_RECOVERED_FORMAL_BUT_ASK_TEXT_TO_BACKFILL`；5 OPEN_OR_REFERENCE。
- 已修复 GPT 点名 P0：
  - CC0200 从合同/格式条款改为未成年人打赏、多方过错、公平原则分责。
  - CC0238 从裁判理由改为评析；按乙公司一链、张某一链处理。
  - CC0137 补齐 AI 著作权格和信用卡合同违约格。
  - CC0229 改为三案例法律手段链。
  - CC0305 题头标明设问待补，不伪装完全闭合。
- 验收结论：`V11_1_WRITTEN_CHAIN_PATCH_PASS`，只表示本轮书面题链补丁通过；仍不得写最终宝典、不得生成 DOCX、不得进入 24 题回填，除非用户另行允许。

## STEP_130_V12_24_QUESTION_BACKFILL_20260522

- 时间：2026-05-22 13:16 CST
- 用户/GPT 裁定：v11.1 可以通过书面题链补丁验收，但不是最终宝典；当前只能进入 `v12_24_question_backfill`，目标是 24 题回源回填。
- 已完成目录：`v12_24_question_backfill/`。
- 已完成文件：
  - `v12_24_question_backfill/01_24题待回源清单.csv`
  - `v12_24_question_backfill/01_24题待回源清单.md`
  - `v12_24_question_backfill/source_lock_cards/` 下 24 张 source lock card
  - `v12_24_question_backfill/source_lock_cards_index.csv`
  - `v12_24_question_backfill/02_24题回填题链.csv`
  - `v12_24_question_backfill/02_24题回填题链.md`
  - `v12_24_question_backfill/03_all_53_question_chains_v12.csv`
  - `v12_24_question_backfill/03_all_53_question_chains_v12.md`
  - `v12_24_question_backfill/04_无法回填或降级清单.csv`
  - `v12_24_question_backfill/04_无法回填或降级清单.md`
  - `v12_24_question_backfill/05_upper_strong_triage_framework_v12_patch.md`
  - `v12_24_question_backfill/06_true_coverage_matrix_v12.csv`
  - `v12_24_question_backfill/06_true_coverage_matrix_v12.md`
  - `v12_24_question_backfill/07_v12_acceptance.md`
- 24 题 source lock 结果：18 题可回填；6 题待用户确认/不进入学生题链正文。
- 可回填题已写入 02：CC0019、CC0051、CC0077、CC0084、CC0092、CC0119、CC0157、CC0180、CC0189、CC0195、CC0206、CC0213、CC0214、CC0223、CC0245、CC0283、CC0325、CC0364。
- 无法回填/待确认题已移入 04：CC0251、CC0276、CC0277、CC0317、CC0318、CC0319。
- 03 v12 正文题链数量：47 题；未锁源 6 题不在正文伪装完成。
- 硬 QA：`02_24题回填题链.md` 与 `03_all_53_question_chains_v12.md` 未命中“待回源确认/暂不写/参考答案/评分说明/page/slide/R_编号/M_编号”等硬污染词。
- 验收结论：`CONDITIONAL_PASS`。原因是仍有 6 题未同时锁住真实设问和真实材料核心；不得写最终宝典、不得生成 DOCX、不得写 `TASK_COMPLETE`。


## 2026-05-22 15:52:45 v12.1 reference cleanup and stage integration
- 输出 v12_1_reference_cleanup_and_stage_integration：42 道正文、5 道 OPEN_OR_REFERENCE 参考附录、6 道未纳入/下一版回填候选。
- 修正 CC0162：删除平台劳动三从属性错链，改为主题乐园年卡/格式合同参考运行。
- 未生成最终宝典、DOCX、TASK_COMPLETE。
