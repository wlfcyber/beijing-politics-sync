# DECISIONS

## 2026-05-21T23:20:23+08:00 - D036 v10 Acceptance Voided, v11 Source-Locked Rebuild Controls

Decision: stop using v10 outputs as accepted framework or all-question chain. The v10 acceptance report is void and must not be cited as `EXHAUSTIVE_FRAMEWORK_PASS`.

Reason: GPT review and user correction identified systematic source/material/trigger mismatch: answer/rubric/analysis text was treated as material, many rows were dumped into universal buckets such as contract/procedure/meaning, and the 53-question chain was formally complete but substantively auto-matched.

New control: v11 must first source-judge each question before any framework match. Each question may have exactly one main entry, at most two sub-entries, at most three main material triggers, at most three sub-material triggers, and an explicit forbidden-hit list. If true material cannot be confirmed, the row is `待用户确认` or `降级参考`, not forced into the student chain.

## 2026-05-20T00:22:15+08:00 - D035 Do Not Overclaim ClaudeCode VS Code Compliance

Decision: downgrade any wording that says the 2026-05-19 suite-exhaustion audit was a "ClaudeCode VS Code audit." The saved command records show it was run through `claude -p` CLI. It may remain in the audit chain as provisional ClaudeCode-Cli/source-check evidence, but it is not a strict VS Code ClaudeCode formal lane.

Reason: the user explicitly required ClaudeCode to be opened in VS Code, not CLI. Future summaries and handoff prompts must not mislabel the channel. If strict four-lane compliance is required, rerun the same audit/patched 65-question corpus through VS Code ClaudeCode and record that output separately.

## 2026-05-19 13:19 - D015 Boundary Recovery Count Policy

User challenged the low v1 PASS count. Decision: do not treat 37 PASS as the whole question universe. It is only the strict v1-core closure count. After reviewing 33 non-PASS rows, restore evidence-backed legal questions into three separate buckets:

- strict core recovery: existing `recover_core` rows plus split legal subquestions with formal scoring evidence;
- open/reference recovery: low-frequency, reference_only, mixed-module, or explicit open-container legal rows;
- pending/excluded: missing legal rubric, duplicate parent rows, non-law politics/economy/logic rows, and OCR/misaligned rows.

Superseded local pre-GPT delta: 48 strict-core law units, 54 core+open/reference units, 55 tracked units if pending CC0259 legal-rubric case is included. This pre-GPT count is no longer controlling after D017. The controlling count after GPT review and CC0229 atom patch is: 48 strict closed core; 53 core+open/weak.

## 2026-05-19 13:19 - D016 Split Rather Than Count Mixed Parents

Mixed rows such as `CC0305_2026_海淀_一模_18`, `CC0373_2026_顺义_一模_17`, and `CC0380_2026_顺义_二模_18` must not be counted as whole-parent law questions. Legal subquestions are split into new units where source evidence permits. Parent rows with economic, logic, or politics content remain non-counted as old units.

## 2026-05-19 14:30 - D017 GPT Boundary Recovery Overrides

Real GPT-5.5 Pro boundary review was captured and supersedes the local pre-GPT count delta.

- `CC0094_2025_东城_期末_19_3` is changed from `keep_reference_open` to `split_or_deduplicate`; whole-row open-container use is forbidden.
- `CC0229_2026_东城_一模_18` was conditionally recoverable; its rubric atoms are now corrected from F0153/F0146 and its handbook section has been regenerated, so it may support the patched core count.
- `CC0250_2026_丰台_一模_19` is removed from framework_v2 open-container samples and final handbook body.
- Current count policy after CC0229 atom patch: strict closed core 48; core+open/weak 53. Final release remains blocked on section regeneration and split/reextract rows.

## 2026-05-19 14:30 - D018 Final Draft Downgrade

The previously generated `framework_v2` and `选必二法律主观题满分宝典` are downgraded to `provisional_boundary_patch_required`.

Reason: the documents still contain bad/provisional sections for `CC0094`, `CC0250`, and `CC0373`; `CC0229` has been repaired. A correction addendum has been added, but final classroom release is blocked until the remaining atom patch queue is completed and affected sections are regenerated.

## 2026-05-19 15:05 - D019 Split Patch Before Canonical Merge

Decision: `CC0305_2026_海淀_一模_18_3`, `CC0373_2026_顺义_一模_18`, and `CC0380_2026_顺义_二模_18_2` now have split question/material/ask/rubric patch records under `10_framework_validation`, but they are not yet merged into canonical `04_merge_audit` files.

Reason: parent rows contain economics, politics, or logic material. Patch records preserve the legal small-question evidence without inflating the parent rows or silently changing the merged corpus. Final handbook regeneration must use the patch records or a later canonical integration file.

## 2026-05-19 14:05 - D020 Boundary-Patched Canonical Corpus

Decision: Create a separate canonical patched corpus under `04_merge_audit/boundary_patched_20260519/` instead of overwriting the original `04_merge_audit/merged_*` files.

Result: the framework-ready corpus now has 53 question rows, 535 material atoms, 53 ask atoms, and 319 rubric atoms. It removes excluded, not-counted parent, and pending rows from the framework-ready corpus, then adds `CC0305_2026_海淀_一模_18_3`, `CC0373_2026_顺义_一模_18`, and `CC0380_2026_顺义_二模_18_2` as split legal units.

Extra correction: `CC0229_2026_东城_一模_18` already had corrected rubric atoms, but its question-level `answer_text/rubric_text` still contained stale logic/economy串页 text. In the patched corpus those fields are replaced with the eight corrected F0153/F0146 legal rubric atoms.

Reason: downstream scripts need one clean patched corpus, while the original merged files remain useful as audit history.

## 2026-05-19 14:10 - D021 Boundary-Patched Sidecar Regeneration

Decision: Keep the existing 70-row audit sidecars for traceability, but add 53-row `_boundary_patched.csv` sidecars aligned to the patched corpus and regenerate `full_score_sentence_bank.csv` from the same 53-row corpus.

Result: `question_by_question_framework_runs_boundary_patched.csv`, `material_trigger_bank_boundary_patched.csv`, and `full_score_sentence_bank.csv` now share the same status counts: 37 `PASS`, 11 `PASS_RECOVERED`, and 5 `OPEN_OR_REFERENCE`.

Reason: the user-facing release should not silently mix old PARTIAL/FAIL labels with recovered boundary decisions. Open/reference rows remain visible but cannot support core framework nodes alone.

## D001 Path Mapping

Windows desktop paths in the user instruction are mapped to available Mac roots under /Users/wanglifei/Desktop and /Users/wanglifei/GaokaoPolitics.

Reason: current execution environment is macOS and cwd is /Users/wanglifei/Desktop/北京高考政治.

## D002 Output Root

Use /Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长 as the active run root.

Reason: it is inside the governed Beijing politics workspace and corresponds to the requested Windows output directory name.

## D003 Evidence Reset

Old 选必二 artifacts may be used only as contamination warnings or file-location hints when unavoidable; they are not source evidence and not conclusions.

Reason: user and hard-rule notebook require old 选必二 line to be void.

## D004 Correct Reasoner Scope

The first 35-question packet is reclassified as `formal_core_trial_35` and is not official. The official reasoner packet is `05_reasoner_packets/reasoner_packet_v2_full_context_20260519.zip`, containing 74 merged candidates: 54 formal, 3 reference_only, and 17 missing-context-only.

Reason: the project target is full subjective-law coverage, not only the high-confidence formal core. Missing questions still cannot support observations, but they must remain visible as补证 and boundary context.

## D005 Missing17 Correction

The v2 packet is superseded by `05_reasoner_packets/reasoner_packet_v3_corrected_missing17_20260519.zip`.

Correction result: 70 merged subjective candidates, 65 formal, 5 reference_only, 0 missing. Four false-positive rows from the missing17 set were removed as choice-answer/non-law-subjective artifacts. `CC0162_2025_海淀_一模_18` and `CC0311_2026_海淀_二模_18` remain reference_only because no formal scoring source was located.

Reason: reference answers cannot be upgraded into formal rubrics, and official GPT/Claude observation must not run on stale missing-evidence states.

## D006 External UI Non-Interruption

While GPT-5.5 Pro or Claude Opus is actively thinking in the visible UI, Codex must not click send, stop, retry, or regenerate controls. Codex may only observe status and capture completed output.

Reason: user corrected that Claude had been manually continued and Codex UI interaction could interrupt the official model lane.

## D022 ChatGPT Web Project Progress Sync

Decision: The current boundary-patched release-candidate progress was sent once to the ChatGPT web project `必修四喂细则`, conversation `选必二框架设计`.

Message source: `handoff_prompts/REPORT_TO_GPT_WEB_BIXIU4_FEED_RUBRIC_XUANBIER_PROGRESS.md`.

Reason: user explicitly asked Codex to report current progress to the top selected 选必二 planning conversation in that GPT project while they rested. After sending, Codex must leave GPT thinking uninterrupted and only capture output if it completes naturally.

## D023 Net-17 Recheck Reopens Source Exhaustion

Decision: The 53-row boundary-patched package must no longer be described as source-exhaustive. It remains a bounded release candidate only.

Evidence: `04_merge_audit/net17_serious_recheck_20260519.csv` and `.md` show that the net 17 gap equals 20 removed original rows minus 3 added split rows. Three non-midterm suites had a different law subjective question missed while the originally excluded row was correctly non-law: `RECOVER_2024_顺义_二模_17`, `RECOVER_2025_海淀_二模_18`, and `RECOVER_2026_通州_一模_20`.

Reason: the user's challenge that non-midterm papers should usually have a law subjective question was confirmed in these cases. The correct next action is recovery patching, not defending the 53-row closure.

## D024 Boundary Recovered Corpus Becomes Working Corpus

Decision: Use `04_merge_audit/boundary_recovered_20260519/` as the next working corpus for source-exhaustion and downstream validation.

Evidence: the corpus contains 56 question rows, adding `RECOVER_2024_顺义_二模_17`, `RECOVER_2025_海淀_二模_18`, and `RECOVER_2026_通州_一模_20` to the previous 53-row boundary-patched package. Evidence labels are 51 formal and 5 reference_only.

Reason: the missing three rows are real law-subjective candidates from non-midterm suites. However, the recovered rows have not yet gone through the full framework pressure test, sidecar regeneration, final handbook section generation, or Word/PDF QA, so final classroom closure is still pending.

## D025 Suite Exhaustive Corpus Supersedes 53/56-Row Packets

Decision: The next valid evidence base is `04_merge_audit/suite_exhaustive_20260519/`, not the previous 53-row boundary-patched corpus or 56-row boundary-recovered corpus.

Evidence: suite-level exhaustion found additional missed law subjectives in suites that still had no core row after the 56-row recovery. Ten formal core rows were added: `RECOVER_2024_东城_一模_19`, `RECOVER_2024_东城_二模_19_1`, `RECOVER_2024_东城_二模_19_2`, `RECOVER_2025_丰台_二模_19_2`, `RECOVER_2026_延庆_一模_18_1`, `RECOVER_2026_房山_一模_17_1`, `RECOVER_2026_西城_二模_18_1`, `RECOVER_2026_西城_二模_18_2`, `RECOVER_2026_西城_二模_18_3`, and `RECOVER_2026_门头沟_一模_18_1`.

Result: The current core corpus is 66 rows: 61 formal and 5 reference_only. Six boundary/blocked cases are kept outside core in `boundary_mixed_or_blocked_cases.csv`.

Reason: Framework generation must follow suite exhaustion. Existing GPT/Claude observations, codebook, framework, validation, and handbook artifacts are superseded until rerun against `05_reasoner_packets/suite_exhaustive_20260519/`.


## 2026-05-19T13:55:00+08:00 - Framework v2 Promotion

- Decision: Promote the six-step v1 into framework_v2, but add an entrance gate and open-container layer based on full pressure testing.
- Evidence: v1 pressure test across 70 merged candidates produced PASS 37, PARTIAL 13, FAIL 20.
- Rationale: Expanding the trunk to cover all 70 would force false positives and weak evidence into the core; v2 keeps the evidence-backed trunk and quarantines weak/boundary cases.
- Constraint: reference_only rows remain non-core; FAIL rows are not final-body law examples.

## 2026-05-19T16:11:46+08:00 - D026 ClaudeCode Suite Exhaustion Overrides Old 66 Package

Decision: the earlier 66-row suite-exhaustive corpus is not accepted as final reasoner input. ClaudeCode B independently audited it and returned `FINAL_JUDGMENT: FAIL`.

Accepted corrections: add `RECOVER_2026_朝阳_期末_18_1`; remove `CC0051_2024_海淀_期中_21_1` and `RECOVER_2024_顺义_二模_17` from core; split `CC0311_2026_海淀_二模_18` to core-only `18_2`; correct 7 mislabeled 2026期末 rows.

Reason: current framework work must start only after every suite is exhausted and stage/module boundaries are clean.

## 2026-05-19T16:11:46+08:00 - D027 Corrected 65-Question Corpus Becomes Controlling Reasoner Input

Decision: `04_merge_audit/suite_exhaustive_claudecode_corrected_20260519/` is now the controlling corpus for open observation, replacing 53/56/66/v3 packets.

Counts: 65 core subjective law questions; formal 61; reference_only 4; missing 0; material atoms 541; ask atoms 65; rubric atoms 362.

ClaudeCode patch verification returned `PATCH_VERIFICATION: PASS`; remaining OCR/source blockers are visible risks, not blockers before GPT/Claude open observation.

## 2026-05-19T16:25:00+08:00 - D028 Claude Cowork Added As Question-Refinement Lane

Decision: start a Claude Cowork desktop task as an additional evidence-refinement lane before sending the corrected packet into the final GPT-5.5 Pro / Claude Opus open-observation rerun.

Input: `05_reasoner_packets/reasoner_packet_suite_exhaustive_claudecode_corrected_20260519.zip` plus `handoff_prompts/PROMPT_FOR_CLAUDE_COWORK_QUESTION_REFINEMENT_20260519.md`.

Scope: Cowork may inspect and improve the 65-question corpus, material atoms, ask atoms, rubric atoms, evidence levels, locators, reference_only rows, and suite-exhaustion risks. Cowork must not write frameworks, codebooks, candidate frameworks, slogans, or final student-facing answers.

Reason: the user requested trying Claude Cowork because it may directly access desktop files and asked that it participate first in improving all questions.

## 2026-05-19T16:32:00+08:00 - D029 Reasoner Rerun Paused For Question-Layer Repair

Decision: do not send the corrected 65-question packet to GPT-5.5 Pro or Claude Opus yet, despite ClaudeCode patch verification PASS.

Evidence: local mechanical check under `04_merge_audit/claude_cowork_question_refinement_20260519/` found 24 rows where `ask_text` is missing and/or `full_question_text` / `material_text` appears to equal answer/rubric text. Atom links and counts are clean, but the question layer is not clean enough for open observation.

Reason: open observation must be based on题干、材料、设问、答案、细则 all correctly separated. A packet with answer text in the material layer can contaminate model observations and framework nodes.

## 2026-05-19T17:01:41+08:00 - D030 Cowork-Refined Packet Supersedes ClaudeCode-Corrected Packet

Decision: `05_reasoner_packets/reasoner_packet_suite_exhaustive_cowork_refined_20260519.zip` is now the only valid packet for the next GPT-5.5 Pro / Claude Opus open-observation rerun.

Evidence: Claude Cowork returned `CONDITIONAL_PASS` and found hard question-layer blockers. Codex applied those patches and then repaired five more material-layer contamination rows: `CC0011_2024_丰台_二模_17`, `CC0119_2025_丰台_期末_19`, `CC0251_2026_丰台_一模_20`, `CC0254_2026_丰台_二模_18`, and `CC0283_2026_朝阳_一模_18`.

Counts after independent validation: 65 core questions, 61 formal, 4 reference_only, 0 missing, 482 material atoms, 65 ask atoms, 350 rubric atoms, hard blockers 0.

Reason: the previous ClaudeCode-corrected packet had the right suite-level count but did not cleanly separate question/material/ask layers. Framework generation from that packet would risk learning from answer/rubric text as if it were material.

## 2026-05-19T17:01:41+08:00 - D031 Core Count Is 65, Not 70

Decision: do not force the count back to 70. The current exhausted core is 65 subjective law questions.

Evidence: the suite matrix keeps non-core rows visible: true no-law midterms, law-boundary but not core rows, mixed rows, and the user-excluded/source-blocked `2026石景山期末`. These are audit rows, not hidden missing core questions.

Reason: “70左右” was a reasonable expectation during recovery, but after ClaudeCode + Cowork + Codex source checks, the evidence-supported core is 65. Forcing boundary/economic/political/logic rows into the legal core would contaminate the framework.

## 2026-05-19T17:11:52+08:00 - D032 Submit Once Then Wait

Decision: GPT-5.5 Pro and Claude Opus 4.7 Adaptive were each submitted once with the same cowork-refined packet and same open-observation task. Do not click stop, retry, regenerate, or send again while either model is thinking.

Evidence: `tool_outputs/gpt55pro_open_observation_cowork_refined_call_status_20260519.md`; `tool_outputs/claude_opus_open_observation_cowork_refined_call_status_20260519.md`.

Reason: the user explicitly flagged repeated clicking as causing Claude interruption. The official model-lane evidence must be captured from uninterrupted natural completions.

## 2026-05-19T17:45:00+08:00 - D033 Cowork-Refined Open Observations Captured

Decision: Treat the current GPT-5.5 Pro and Claude Opus 4.7 Adaptive open-observation gate as completed for the cowork-refined 65-question packet.

Evidence: `06_open_observations/gpt55pro_open_observations_cowork_refined_20260519.md`; `06_open_observations/claude_opus_open_observations_cowork_refined_20260519.md`; status files in `tool_outputs/` are both `COMPLETED_AND_CAPTURED`.

Result: GPT produced 25 parsed observations; Claude produced 19 parsed observations. No framework was accepted from this round; only observation-level data may flow into cross-validation.

## 2026-05-19T17:45:00+08:00 - D034 Provisional Codebook From Cowork-Refined Cross-Validation

Decision: Promote only 7 dual-model, source-checked, formal-supported observations into the current provisional codebook.

Evidence: `07_cross_validation/gpt_claude_observation_comparison_cowork_refined_20260519.md`; `08_codebook/provisional_codebook_v0_cowork_refined_20260519.md`.

Reason: the parser initially over-matched broad model observations, so Codex added source-ID expansion and theme-tag filtering. Weak/reference-only/single-model observations remain pending and cannot support core framework nodes.

## 2026-05-19T17:53:35+08:00 - D035 Candidate Framework Real Calls Submitted Once

Decision: Submit the codebook-bound candidate-framework packet to real GPT-5.5 Pro and real Claude Opus 4.7 Adaptive, once each, then wait for natural completion.

Evidence: `tool_outputs/gpt55pro_candidate_framework_cowork_refined_call_status_20260519.md`; `tool_outputs/claude_opus_candidate_framework_cowork_refined_call_status_20260519.md`.

Input: `09_candidate_frameworks/candidate_framework_input_cowork_refined_20260519.zip`; identical prompts under `handoff_prompts/PROMPT_FOR_*_CANDIDATE_FRAMEWORK_COWORK_REFINED_20260519.md`.

Reason: the current 7-row codebook is not a framework. The official framework gate requires real GPT-5.5 Pro and Claude Opus candidate proposals before Codex can synthesize and pressure-test `framework_v1`.

## 2026-05-19T17:55:35+08:00 - D036 Canonical Merged Files Point To Cowork-Refined Corpus

Decision: Replace the root `04_merge_audit/merged_*` canonical files with the cowork-refined 65-question corpus.

Evidence: after replacement, canonical counts are 65 questions, 61 formal, 4 reference_only, 482 material atoms, 65 ask atoms, 350 rubric atoms. Previous root canonical files were backed up under `tool_outputs/pre_cowork_refined_merged_canonical_backup_20260519_175535/`.

Reason: the uploaded candidate-framework zip was already correct, but the root canonical merged files still held the older 70-row v3口径. Leaving them stale could contaminate later framework synthesis or pressure-test scripts.

## 2026-05-19T18:08:33+08:00 - D037 Candidate Framework Real-Model Gate Completed

Decision: Treat the cowork-refined candidate-framework gate as completed. Both real GPT-5.5 Pro and real Claude Opus 4.7 Adaptive outputs were captured from the same 65-question packet and 7-row provisional codebook.

Evidence: `09_candidate_frameworks/gpt55pro_candidate_frameworks_cowork_refined_20260519.md` (399 lines, 32604 bytes) and `09_candidate_frameworks/claude_opus_candidate_frameworks_cowork_refined_20260519.md` (276 lines, 22805 bytes). Canonical unsuffixed copies now point to these captured outputs.

Reason: the project may now enter local candidate-framework comparison and `framework_v1` synthesis. This does not authorize final framework or宝典 claims; `framework_v1` must still be pressure-tested against all 65 core questions with reference_only rows kept non-core.

## 2026-05-19T18:15:00+08:00 - D038 Framework v1 Is Conservative, Not Final

Decision: synthesize `framework_v1` as “设问入口分流 + 七个 codebook 节点 + 缺口隔离记录.”

Evidence: GPT recommended the ask-function split; Claude recommended ask-identification to codebook routing. Both warned that direct codebook support is only 16/65 and that the remaining 49 questions cannot be claimed as full-score closures.

Reason: this is the smallest model-agreed framework that does not invent unsupported IP/AI/ecology/family/minor/green-principle nodes from pending observations.

## 2026-05-19T18:18:00+08:00 - D039 Framework v1 Pressure Test Blocks Final Output

Decision: `framework_v1` does not yet authorize `framework_v2` or the final baodian.

Evidence: all-65 pressure test using only question/ask/material layers for framework entry produced PASS 16, PARTIAL 49, FAIL 0. The 45 formal PARTIAL rows can start through an entry, but they lack direct codebook support; the 4 reference_only rows remain non-core.

Reason: an entry that can start a student does not equal a rubric-backed满分闭环. The next work must source-check PARTIAL clusters and either expand the codebook through evidence-backed dual-model observations or quarantine them as open-container examples.

## 2026-05-19T18:24:00+08:00 - D040 Prepare Codebook Expansion Instead Of Forcing v2

Decision: build a dedicated codebook-expansion source-check packet for the 45 formal PARTIAL rows rather than revising `framework_v1` directly into `framework_v2`.

Evidence: `10_framework_validation/framework_v1_partial_cluster_source_check.csv` and `05_reasoner_packets/codebook_expansion_partial_rows_20260519.zip` contain only pressure-test PARTIAL rows, current v1, current codebook, and source atom summaries.

Reason: the current blocker is not framework naming; it is missing evidence-backed codebook observations for the 45 formal transfer rows. Any v2 written before this check would either overclaim coverage or smuggle pending observations into core nodes.

## 2026-05-19T18:27:27+08:00 - D041 Add Claude Cowork All-Question Completion Before Final Expansion

Decision: submit an extra Claude Desktop Cowork task for all-65 completion review before relying on GPT/Claude Opus expansion calls or revising `framework_v1`.

Evidence: `05_reasoner_packets/claude_cowork_all_question_completion_20260519.zip`; `handoff_prompts/PROMPT_FOR_CLAUDE_COWORK_ALL_QUESTION_COMPLETION_20260519.md`; `tool_outputs/claude_cowork_all_question_completion_call_status_20260519.md`.

Reason: the user asked to try Claude Cowork because it may directly access Desktop files and help complete all questions. The task is restricted to source-check/codebook-expansion observations, not final framework writing.

## 2026-05-19T18:44:35+08:00 - D042 Cowork Completion Captured; Do Not Promote Directly To Framework

Decision: capture Cowork's all-question completion outputs and treat them as a high-value expansion source, but not as direct authorization for `framework_v2`.

Evidence: `04_merge_audit/claude_cowork_all_question_completion_20260519/claude_cowork_all_question_completion_report.md`; `claude_cowork_all65_completion_table.csv`; `claude_cowork_codebook_expansion_candidates.csv`.

Result: Cowork proposes only one new core candidate (`CODE_COWORK_008`), four existing-code revisions, 11 transfer/open-container rows, five source-check rows, and explicit rejection of reference_only rows as core code support.

Reason: the project still requires local source checks and cross-model adjudication before changing the codebook or framework. This prevents "追 PASS 率" from becoming unsupported framework expansion.

## 2026-05-19T18:53:31+08:00 - D043 Source-Check Five Cowork-Blocked Rows Before Expansion

Decision: mark all five Cowork-blocked rows as non-missing but not directly promotable. Use Codex's corrected atomization plan in the next GPT-5.5 Pro / Claude Opus expansion packet.

Evidence: `04_merge_audit/claude_cowork_all_question_completion_20260519/codex_source_check_five_blocked_rows.md`; `codex_source_check_five_blocked_rows.csv`; `codex_source_check_corrected_rubric_atom_plan.csv`.

Result: `CC0011` and `CC0019` are formal but collapsed scoring blocks; `CC0061` requires subquestion split/trim; `CC0254` has formal scoring on slides 29-30 but current atoms wrongly used later student-problem slides; `RECOVER_2026_房山_一模_17_1` is formal but its 2-point explanation dimensions are alternatives, not cumulative atoms.

Reason: this preserves the user's “吃干抹净” requirement without repeating false closure. The next model calls may verify expansion candidates, but cannot treat Cowork or Codex source-check alone as final framework authority.

## 2026-05-19T18:56:19+08:00 - D044 Corrected Expansion Packet Supersedes Earlier Partial Packet

Decision: use `codebook_expansion_after_cowork_sourcecheck_20260519.zip` for the next GPT-5.5 Pro and Claude Opus expansion calls, not the earlier `codebook_expansion_partial_rows_20260519.zip`.

Evidence: the corrected packet contains current canonical corpus files, pressure-test files, Cowork all-question completion outputs, and Codex source-check outputs, including `codex_source_check_corrected_rubric_atom_plan.csv`. The GPT and Claude handoff prompts are byte-identical.

Reason: the earlier partial packet did not include Cowork's all-question review or the source-check fixes for CC0011, CC0019, CC0061, CC0254, and RECOVER_2026_房山_一模_17_1. Sending it now would under-inform the external expansion gate.

## 2026-05-19T19:03:00+08:00 - D045 Corrected Expansion Calls Submitted Once

Decision: submit the corrected expansion packet once each to GPT-5.5 Pro lane and Claude Opus 4.7 Cowork, then wait without touching stop/retry/regenerate/send controls.

Evidence: `tool_outputs/gpt55pro_codebook_expansion_after_cowork_sourcecheck_call_status_20260519.md` records Safari ChatGPT submission with corrected attachment visible; `tool_outputs/claude_opus_codebook_expansion_after_cowork_sourcecheck_call_status_20260519.md` records new Claude Desktop Cowork task `local_586e609e-6613-42bf-a89d-ee2110941455`.

Reason: the project needs dual external adjudication of Cowork expansion suggestions after Codex source-check. A single Cowork run is not enough to revise the codebook, and repeated UI clicks risk interrupting model thinking.

## 2026-05-19T19:44:37+08:00 - D046 Corrected Expansion Outputs Captured And Cross-Compared

Decision: treat the corrected expansion adjudication gate as completed, but only for codebook expansion decisions, not final framework or baodian.

Evidence: `06_open_observations/gpt55pro_codebook_expansion_after_cowork_sourcecheck_20260519.md`; `06_open_observations/claude_opus_codebook_expansion_after_cowork_sourcecheck_20260519.md`; `07_cross_validation/codebook_expansion_after_cowork_sourcecheck_20260519/codebook_expansion_after_cowork_sourcecheck_comparison.md`.

Result: GPT produced 16 TSV decisions; Claude produced 17 CSV decisions. Cross-validation accepts one trimmed new core code (`CODE_COWORK_008`), accepts four existing-code revisions, rejects/open-containers the rest, and requires P0 atom patching before pressure testing.

## 2026-05-19T19:44:37+08:00 - D047 Conservative Trim Wins For CODE_COWORK_008

Decision: add `CODE_COWORK_008` only with the GPT+Codex trimmed support set: `CC0131`, `CC0206`, `CC0229`, `CC0283`, `CC0319`, `CC0103`.

Evidence: `EXP_CMP_001` in `codebook_expansion_after_cowork_sourcecheck_comparison.csv`.

Reason: Claude's broader set included `CC0143` and `RECOVER_2026_西城_二模_18_2`, but GPT and local source check showed `CC0143` is a consumer fraud/contract/consumer-rights counterexample and `RECOVER_2026_西城_二模_18_2` belongs only to AI responsibility-boundary open container.

## 2026-05-19T19:44:37+08:00 - D048 P0 Atom Patch Applied Before Codebook Draft

Decision: patch canonical `merged_rubric_atoms_subjective.csv` before building any expansion draft.

Evidence: `04_merge_audit/codebook_expansion_atom_patch_20260519/p0_atom_patch_application_report.md`; backup under `tool_outputs/pre_codebook_expansion_atom_patch_20260519_194135/`.

Result: `CC0011` 1->4 atoms; `CC0019` 1->6; `CC0061` 3->6 with 18(1)(2) procedure micro-items; `CC0254` wrong 8 student-problem/teaching-suggestion atoms replaced by 8 scoring atoms; `RECOVER_2026_房山_一模_17_1` 3->4 with `alternative_not_cumulative`; CC0143 teaching-reflection atoms annotated non-scoring.

## 2026-05-19T19:44:37+08:00 - D049 Expansion Draft Is A Pressure-Test Input, Not Framework v2

Decision: create `provisional_codebook_v1_expansion_draft_20260519` and a coverage snapshot, while keeping `framework_v2` and final baodian blocked.

Evidence: `08_codebook/provisional_codebook_v1_expansion_draft_20260519.md`; `10_framework_validation/framework_v1_expansion_draft_pressure_snapshot_20260519.md`.

Result: expansion draft has 8 code rows and 42 unique core-support question_ids. Snapshot status: 42 core support, 14 open-container only, 5 reference/reject non-core, 1 source-check pending, 3 no-expansion-support-yet.

Reason: core support is not the same as full-score sentence closure. The next gate is sentence-level all-65 pressure test plus CC0364 atom split.

## 2026-05-19T19:54:30+08:00 - D050 Split CC0364 Before Counting It As Core Support

Decision: split `CC0364_2026_通州_期末_19_1` from one collapsed formal rubric atom into seven scoring atoms, then count it only as limited support for `CODE_COWORK_004/006`.

Evidence: `04_merge_audit/cc0364_split_patch_20260519/cc0364_split_patch_report.md`; `cc0364_patch_atoms.csv`; patched canonical `04_merge_audit/merged_rubric_atoms_subjective.csv`.

Result: `CC0364` no longer remains source-check pending. The split preserves the real scoring structure: 民法典依据1, 相邻关系原则2, 业主角度事实2, 范某角度替代事实1不累加, 维护合法权益1, 邻里和谐1, 友善核心价值观1.

Reason: model agreement alone was not enough because the original atom merged法理、事实、意义. Splitting prevents over-scoring and prevents value-tail atoms from becoming independent framework nodes.

## 2026-05-19T19:54:30+08:00 - D051 v1.1 Pressure Test Allows Synthesis Work But Not Final Closure

Decision: use `provisional_codebook_v1_1_after_cc0364_split_20260519` for the next synthesis/patch round, but keep final `framework_v2` and final宝典 blocked.

Evidence: `10_framework_validation/framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv`; `framework_v1_1_sentence_pressure_pass_report_20260519.md`.

Result: all-65 sentence pressure test returns PASS 43, PARTIAL 18, FAIL 4; evidence remains 61 formal and 4 reference_only.

Reason: 43 PASS rows are enough to continue framework synthesis pressure work, but 18 PARTIAL and 4 FAIL rows mean the project still cannot honestly claim all-question full-score closure.

## 2026-05-19T20:11:35+08:00 - D052 FAIL4 Local Patch Candidates Are Not Promotions

Decision: record FAIL4 local patch candidates while Claude Cowork is still running, but do not mutate the core codebook or framework_v2 from these candidates alone.

Evidence: `10_framework_validation/fail4_source_adjudication_20260519/fail4_local_patch_candidates_20260519.md`; `fail4_local_patch_candidates_20260519.csv`.

Result: `CC0143_2025_朝阳_一模_19` is the only local core-candidate supplement, under a consumer-contract-fraud / punitive-compensation pattern. `CC0276_2026_房山_二模_17` remains涉外法治建设 boundary-only. `RECOVER_2026_西城_二模_18_2` remains an AI responsibility-boundary open container. `RECOVER_2026_西城_二模_18_3` is excluded from the 选必二 core as digital-governance / national-governance modernization.

Reason: the user asked for every suite/question to be eaten cleanly, but the method still forbids promoting a one-off local judgment into the core framework before external/cross-model confirmation or explicit quarantine.

## 2026-05-19T20:24:00+08:00 - D053 FAIL4 Cowork Agreement Unlocks A Guarded v1.2 Codebook

Decision: integrate Claude Cowork's FAIL4 targeted audit because it agrees with local source adjudication on all four v1.1 FAIL rows, while preserving open/boundary gates.

Evidence: `10_framework_validation/fail4_source_adjudication_20260519/claude_cowork_output/fail4_targeted_adjudication_claude_cowork_20260519.md`; `fail4_external_cross_check_20260519.md`; `04_merge_audit/cc0143_atom_patch_20260519/cc0143_atom_patch_report.md`; `08_codebook/provisional_codebook_v1_2_after_fail4_cowork_20260519.md`.

Result: `CC0143_2025_朝阳_一模_19` is admitted only after atom patch as a consumer fraud / contract revocation / triple compensation subtype under `CODE_COWORK_004`, with meaning-tail support for `CODE_COWORK_002`. `CC0276_2026_房山_二模_17` and `RECOVER_2026_西城_二模_18_3` are formal but non-core boundary cases. `RECOVER_2026_西城_二模_18_2` is an AI responsibility-boundary open container, not a core node.

Reason: this removes the four hard FAIL rows without pretending all PARTIAL rows are solved. Direct core support is now 44/65; 18 PARTIAL rows remain explicitly classified as reference-only demos or formal open-container pressure cases.

## 2026-05-19T20:31:00+08:00 - D054 v1.2 Pressure Uses Boundary Passes But Keeps Core Count Separate

Decision: count `CC0276_2026_房山_二模_17` and `RECOVER_2026_西城_二模_18_3` as `PASS` only for the boundary gate, not as selected-compulsory-2 core full-score cases.

Evidence: `09_candidate_frameworks/framework_v1_2_guarded.md`; `10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv`; `framework_v1_2_pass_report_20260519.md`.

Result: all-65 guarded pressure snapshot has PASS 46, PARTIAL 19, FAIL 0. The PASS 46 splits into 44 core/pass rows and 2 boundary-gate pass rows. The 19 PARTIAL rows remain open/reference cases.

Reason: a boundary filter is a real framework function: it prevents 必修三/综合法治 contamination. But those boundary passes must not be advertised as legal-subjective full-score templates.

## 2026-05-19T20:40:00+08:00 - D055 Guarded Baodian Regenerated With Labels

Decision: overwrite the baodian Markdown and sidecars with a guarded v2 version that preserves every row's evidence/use label instead of claiming unqualified full closure.

Evidence: `12_final_baodian/question_by_question_framework_runs.csv`; `12_final_baodian/选必二法律主观题满分宝典.md`; `12_final_baodian/full_score_sentence_bank.csv`; `12_final_baodian/material_trigger_bank.csv`; `12_final_baodian/common_failure_paths.md`.

Result: 65 question rows are present. Labels are: core_full_score_supported 44; formal_open_container_partial 14; reference_only_demo 4; boundary_non_core 2; open_container_only 1. DOCX was generated from Markdown by python-docx and still needs Word/PDF visual QA if the file is to be treated as publication-ready.

Reason: the user's main complaint was false exhaustion/false closure. The guarded baodian keeps all rows visible while refusing to upgrade weak/open/boundary rows into core full-score templates.

## D056_GUARDED_V2_PARTIAL_POLICY_19

- Decision: `framework_v1_2_partial_policy_20260519` must count 19 PARTIAL rows, not 18.
- Reason: the pressure table and baodian sidecar have 19 PARTIAL rows; `RECOVER_2026_西城_二模_18_2` is open-container-only and was omitted from the earlier policy ledger.
- Consequence: PARTIAL = 15 formal non-core/open rows + 4 reference_only demos; none may support a new core node without repeated formal evidence and cross-validation.

## D057_GPTPRO_REVIEW_PENDING_NOT_SIMULATED

- Decision: the guarded v2 packet is prepared for GPT-5.5 Pro, but until a visible/web GPT-5.5 Pro response is captured, the phase remains `real_call_pending`.
- Reason: 选必二 framework-phase rules require real GPT/Claude model calls; local Codex notes cannot substitute for GPT-5.5 Pro.

## D058_GPTPRO_SUBMITTED_ONCE_DO_NOT_INTERRUPT

- Decision: the guarded v2 packet was submitted once to real GPT-5.5 Pro in Safari ChatGPT web, and the phase is now `submitted_running`, not `prepared_not_submitted` and not `completed`.
- Evidence: `tool_outputs/gpt55pro_guarded_v2_review_call_status_20260519.md`; Safari conversation `https://chatgpt.com/c/6a0c3288-938c-83ea-bca9-66b8db9d9326` visibly showed `Pro 思考中`.
- Reason: repeated sends or clicking Stop/Retry/Regenerate can interrupt the external-review lane and contaminate the audit chain. Codex A may poll/read only until GPTPro completes naturally.

## D059_CC0380_DEMOTED_FROM_CORE_TO_OPEN_CONTAINER

- Decision: `CC0380_2026_顺义_二模_18_2` must not support core `CODE_COWORK_007` / `FWV1_2_N06`.
- Evidence: canonical merged row already marks `module_boundary_risk=综合` and notes that the item combines 必修三《政治与法治》 and 选必二《法律与生活》; current rubric atoms are formal but describe AI/open intelligent-agent legal risks and remedies.
- Result: `CC0380` and its atoms were removed from core `FWV1_2_N06` support and moved into `FWV1_2_OPEN 开放容器`; pressure now reports PASS 45 = 43 core/pass + 2 boundary-gate, PARTIAL 20, FAIL 0.
- Reason: formal evidence can be preserved without pretending a 综合/AI-open boundary row is a stable selected-compulsory-2 full-score template.

## D060_GPTPRO_RUNNING_PACKET_IS_PRE_CC0380_PATCH

- Decision: the GPTPro web call currently running should not be interrupted even though local files have been corrected after submission.
- Evidence: `tool_outputs/gpt55pro_guarded_v2_review_call_status_20260519.md`; `10_framework_validation/gptpro_guarded_v2_local_precheck_20260519.md`.
- Consequence: after GPTPro completes, capture the full output and compare it against the post-submit local patch. Send a delta follow-up only after natural completion if the review needs the updated CC0380 status.

## D061_GPTPRO_GUARDED_REVIEW_CAPTURED_YES_WITH_GUARDS

- Decision: treat the real GPT-5.5 Pro guarded-v2 review as captured and authoritative for the next cleanup pass, with verdict `YES_WITH_GUARDS`, not `final full closure`.
- Evidence: `tool_outputs/gpt55pro_guarded_v2_review_response_20260519.md`; `06_open_observations/gpt55pro_guarded_v2_review_20260519.md`.
- Result: 65-question factual baseline is acceptable, but GPTPro requires evidence cleanup, `CODE_COWORK_007` framework split, stronger non-core labels, and full Word/PDF QA before any guarded final claim.
- Reason: GPTPro confirmed the corpus baseline while catching exactly the false-closure risks the user objected to: other-module answer pollution, teaching/problem atoms in scoring support, and open/boundary rows presented too strongly.

## D062_GPTPRO_P0_CLEANUP_APPLIED

- Decision: apply GPTPro's P0 row/file patches locally and regenerate guarded outputs from scripts, not by hand-editing final prose.
- Evidence: `scripts/apply_gptpro_guarded_v2_cleanup.py`; `10_framework_validation/gptpro_guarded_v2_cleanup_20260519/gptpro_guarded_v2_cleanup_report.md`; `08_codebook/provisional_codebook_v1_3_after_gptpro_guarded_review_20260519.csv`; `09_candidate_frameworks/framework_v1_2_evidence_map.csv`; `10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv`; `12_final_baodian/question_by_question_framework_runs.csv`.
- Result: 46 non-scoring atoms are annotated as risk/other-question material; 7 patch scoring atoms are preserved; `CC0077`, `CC0084`, `CC0150`, `CC0245`, and `CC0251` no longer have answer-column pollution; `CC0380` is `OPEN_CONTAINER_ONLY`; `CODE_COWORK_007` is split into 007A/B/C/D framework subnodes.
- Reason: a clean evidence chain matters more than a pretty framework. The regenerated state is guarded-core-ready but still blocked from publication PASS by DOCX visual QA.

## D063_GUARDED_V2_ACCEPTED_AFTER_WORD_PDF_QA

- Decision: accept the current package as guarded v2 after successful Word export and PDF page-render QA.
- Evidence: `12_final_baodian/DOCX_QA_GUARDED_V2.md`; `12_final_baodian/选必二法律主观题满分宝典_GUARDED_V2_WORD_EXPORT.pdf`; `FINAL_ACCEPTANCE_REPORT_GUARDED_V2.md`; `FINAL_DELIVERY_REPORT_GUARDED_V2.md`.
- Result: Microsoft Word exported a 114-page PDF; PyMuPDF rendered all pages; blank-page detections were 0. The deliverable is accepted with guards: 43 core full-score supported rows, 2 boundary-gate rows, and 20 open/reference/non-core rows explicitly labeled.
- Reason: the last technical QA blocker is closed, but evidence labels still limit the claim. The correct delivery claim is `guarded v2 accepted with guards`, not `65 rows all core full-score templates`.
# 2026-05-20T00:06:50+08:00 - Treat mangled GPTPro progress-sync as low-weight

Decision: The GPT-5.5 Pro progress-sync call submitted at 2026-05-19T23:53:00+08:00 remains preserved as an attempted progress sync, but it is downgraded to low-weight because the visible web-composer text was partially mangled after submission.

Reason:

- The uploaded zip is intact and contains the exact local artifacts.
- The local prompt source is intact.
- The visible webpage prompt lost or compressed important punctuation/field markers, so the model may not receive a clean instruction surface.

Consequence:

- Do not use this call alone as a formal acceptance/review gate.
- If a new GPTPro confirmation is needed, use `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_ACCEPTED_PROGRESS_CLEAN_SHORT_20260520.md` and keep the message short, with the attachment as the authoritative source.

## D064_ZERO_BASELINE_STUDENT_PRESSURE_MICRO_PATCH

- Decision: accept the zero-baseline pressure-test consensus as a narrow teaching patch, not a framework-node expansion.
- Evidence: `10_framework_validation/zero_baseline_student_pressure_20260520/internal_agent_zero_baseline_student_answers_20260520.md`; `10_framework_validation/zero_baseline_student_pressure_20260520/claude_cowork_zero_baseline_student_answers_20260520.md`; `10_framework_validation/zero_baseline_student_pressure_20260520/gptpro_zero_baseline_student_answers_20260520.md`; `zero_baseline_student_pressure_codex_grading_report_20260520.md`.
- Result: patched `framework_v2_student_one_page.md`, `framework_v2.md`, `framework_v2_teacher_guide.md`, and regenerated the baodian Markdown/DOCX. New Word-exported PDF `选必二法律主观题满分宝典_GUARDED_V2_ZERO_BASELINE_PATCH_WORD_EXPORT.pdf` rendered 115 pages with 0 blank-page suspects.
- Reason: three independent student-simulation lanes agreed that the core framework works, but zero-baseline students need explicit short prompts for mixed contract/tort liability, consumer-fraud claim structure, labor value-layer closure, open-container fallback, and boundary fallback. These are teaching safety prompts; they do not promote open/reference/boundary rows into core evidence.

## D065_GPTPRO_QUALITY_CHALLENGE_REQUIRES_FRONTEND_REWRITE

- Decision: treat GPTPro's quality-challenge critique as a required front-facing rewrite agenda, not as a new evidence promotion.
- Evidence: `06_open_observations/gptpro_framework_quality_challenge_20260520.md`; `tool_outputs/gptpro_framework_quality_challenge_status_20260520.md`.
- Result: GPTPro agreed with the user's dissatisfaction. The current guarded v2 is evidence-correct and usable as teacher/evidence底稿, but not yet a strong classroom framework. Required rewrite direction: `强主干 + 全量容器`, with student action and teacher script in front, evidence appendix behind.
- Reason: the problem is not insufficient evidence discipline. The problem is that evidence discipline is occupying the teaching front end. The next revision must preserve 43 core + 2 boundary + 20 non-core/open/reference labels while rebuilding the visible product around mainline actions, wrong-answer correction, and exam-style answers.

## D066_STUDENT_BATTLE_VERSION_IS_PRESENTATION_REWRITE_NOT_EVIDENCE_PROMOTION

- Decision: create `选必二法律主观题满分宝典_学生战斗版` as a student-facing handbook derived from guarded v2, while keeping the evidence-limited claim intact.
- Evidence: `12_final_baodian/question_by_question_framework_runs.csv`; GPTPro critique `06_open_observations/gptpro_framework_quality_challenge_20260520.md`; generated files `12_final_baodian/选必二法律主观题满分宝典_学生战斗版.md` and `.docx`.
- Result: the new artifact foregrounds seven strong trunks, material translation, wrong-answer correction, classic examples, and all-65 placement lookup. Backend labels and audit phrases were excluded from the student prose.
- Reason: the user needs a宝典 that students can use immediately. This requires changing the visible teaching order, not inflating open/reference/boundary evidence into core templates.

## D067_USER_REJECTED_STUDENT_BATTLE_ROLLBACK_TO_STEP29

- Decision: stop patching the current framework/baodian line and roll back the active basis to `STEP_29_CLAUDECODE_CORRECTED_CORPUS`.
- Evidence: user message on 2026-05-20: current artifact still cannot make students reach full marks; user requested rollback to the Codex + ClaudeCode 65-question stage.
- Result: canonical `04_merge_audit/merged_*` files now point to STEP_29: 65 questions, 61 formal, 4 reference_only, 0 missing; 541 material atoms, 65 ask atoms, 362 rubric atoms. Later GPT/Claude observations, codebooks, frameworks, guarded v2, zero-baseline patch, GPTPro quality challenge, and student-battle handbook are marked superseded.
- Reason: the problem is not a small prose issue. The framework generation path itself produced an unusable teaching product, so the next honest move is to restart from evidence cards.


## DECISION - 2026-05-20 04:16:02 - 先前框架作为结构样本而非证据

用户要求学习桌面先前框架。决定：允许旧框架进入 GPTPro 输入包，但仅作为结构 DNA、学生可读性和讲义组织样本；当前法律内容、框架节点和满分句必须由 STEP_29 65 题及细则原子支撑。旧选必二结论不得直接继承。

## DECISION - 2026-05-20 04:31:00 - GPTPro v0 is candidate-only

Decision: GPTPro 的 prior-framework-learning 输出可作为候选框架 v0 进入本地压测，但不得直接升为最终框架或宝典。

Evidence:

- `09_candidate_frameworks/gptpro_prior_framework_learned_legal_framework_v0_20260520.md` 明确以 STEP_29 65 题为底座，写明 61 formal、4 reference_only，且 reference_only 不单独支撑核心。
- `09_candidate_frameworks/gptpro_prior_framework_v0_local_evidence_review_20260520.md` 显示 65 个 question_id 均至少以完整 ID 或短 ID 被覆盖，未发现未知 CC 编号。

Reason: 该稿是 GPTPro 单边框架候选。严格四线 gate 仍要求本地逐题压测，并在需要时引入 Claude Opus 4.7 Adaptive 独立/交叉审查。

## DECISION - 2026-05-20 04:38:00 - GPTPro v0 passes direction, not closure

Decision: GPTPro v0 的七动作主干方向保留为候选，但不得直接生成最终宝典。

Evidence:

- `10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv`
- `10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.md`

Result:

- PASS_CANDIDATE 35
- PARTIAL_SOURCE_CHECK 18
- PARTIAL_LOW_FREQ_CONTAINER 5
- PARTIAL_REFERENCE_ONLY 4
- PARTIAL_BOUNDARY_OPEN 3

Reason: 该框架显著改善学生启动感，但仍有 30 行不能直接进入核心满分模板。下一轮应先做 source-clean 和 rubric-atom 句子级对齐，而不是急着写新宝典。

## DECISION - 2026-05-20 12:58:42 - V4 student pure is current deliverable candidate, not final four-lane PASS

Decision: 生成并交付 V4 学生纯净版/训练版作为当前可阅读成品候选；同时明确保留“外部 GPTPro + Claude Opus V4 复审 pending”的限制。

Evidence:

- Active corpus remains STEP_29: 65 questions, 61 formal, 4 reference_only, 0 missing.
- V4 outputs: `11_final_framework/framework_v4_student_fullscore_20260520.md`; `12_final_baodian/选必二法律主观题满分宝典_学生纯净版_20260520.md`; `12_final_baodian/选必二法律主观题满分宝典_学生满分训练版_20260520.md`.
- Local Confucius simulation: `10_framework_validation/confucius_zero_baseline_simulation_v4_20260520.md` returned `CONDITIONAL_PASS_FOR_STUDENT_USE`.
- DOCX/PDF QA: `12_final_baodian/DOCX_PDF_QA_STUDENT_PURE_V4_20260520.md` recorded Word-exported 54-page PDF with 0 blank-text pages and readable sample renders.

Reason: 用户要求早上看到成品，且此前否定审计式成品。V4 把学生入口、材料翻译、满分句和全 65 题练习放到前台，符合“先让学生会写”的方向；但工程纪律要求不能把本地模拟和预备包冒充为真实双外部模型终验。

## DECISION - 2026-05-20 13:10:00 - Stop patching V4; prior-framework DNA becomes rewrite prerequisite

Decision: 用户再次判定框架“太烂”。停止把 V4 当作待小修成品；先把桌面先前框架作为结构老师，生成深度 DNA 和法律重写规格，再进入下一轮法律框架重写。

Evidence:

- `05_reasoner_packets/prior_framework_deep_learning_20260520/PRIOR_FRAMEWORK_DEEP_DNA_20260520.md`
- `05_reasoner_packets/prior_framework_deep_learning_20260520/LEGAL_REWRITE_SPEC_AFTER_PRIOR_STUDY_20260520.md`
- `05_reasoner_packets/prior_framework_deep_learning_20260520/rendered_samples/`

Reason: V4 虽然比旧审计稿更学生化，但没有真正学到先前框架的先导页、A->B 基本模型、主体积累页、情境触发链、争点式逐题演练和错法改法。因此下一版必须先重建教学结构，再接 65 题证据。
## D-20260521-STEP83：接受 Claude Opus V5.2 外审降级

- 决策：接受 Claude Opus 对 V5.2 的 `CONDITIONAL_PASS` 裁定。
- 依据：Claude 逐题指出 31 核心扩展中存在答案拼贴、源数据错位、句式库证据绑定虚假、动作卡路由叠卡等问题。
- 执行：
  - 保留 V5.2 学生速用稿作为有效进步。
  - `CC0244` 即刻重写干净答案。
  - `CC0137/CC0119/CC0289/CC0061` 从 strict_core 降为 source_check_pending。
  - active strict_core 改为 27。
- 约束：外审和二次压测前，不把 27 核心扩展称为最终宝典。

## D-20260521-STEP84：GPTPro 与 Claude 对 V5.2 的共同意见优先于扩题冲动

- 决策：接受 GPTPro 与 Claude Opus 对 V5.2 的共同裁定：学生速用稿方向可保留，但 31 核心扩展不能发布。
- 执行：
  - 以 27 strict_core 作为学生正文核心。
  - 24 source_check_pending 不进入核心样章。
  - 5 low_frequency、4 reference-only、4 boundary/open 只进容器或参考，不支撑核心模板。
  - 生成 V5.3 27 核心清洗学生版。
- 理由：学生可用性必须建立在干净答案和清晰证据边界上，不能用“看起来覆盖更多”牺牲满分句质量。

## D-20260521-STEP85：V5.4 不发布，直接进入 V5.5 修补

- 决策：V5.4 本地零基础压测给出 `CONDITIONAL_PASS`，但不允许作为发布稿。
- 依据：`10_framework_validation/v5_4_zero_baseline_student_pressure_test_20260521.md` 指出 CC0244 原题第（2）问未被训练，非核心题只能保分。
- 执行：保留 V5.4 包给 GPTPro 继续复审，不打断；本地先修 V5.5。
- 理由：外部模型还在审 V5.4，但已发现的 P0 学生漏分点不需要等待外部结论才能修。

## D-20260521-STEP86：V5.5 标题降调为训练宝典并补 65 题保分容器

- 决策：当前学生稿命名为“满分训练宝典”，而不是“65 题满分闭合宝典”。
- 执行：
  - 27 核心题每题增加具体最小判断和满分前检查。
  - CC0244 补全第（2）问。
  - 其余 38 题给保分容器，不升核心。
  - 机械污染扫描必须为 0 才允许进入下一轮压测。
- 理由：用户要的是学生看完能写，而不是后台审计账本；但证据边界仍必须清楚，不能假装所有题都有稳定核心模板。
## 2026-05-21 03:43｜D87｜V5.7 可外审，不可终稿

- 决定：接受 V5.6 本地压测的 `CONDITIONAL_PASS`，并将其 P1 修补为 V5.7。
- 理由：V5.6 已解决 38 道非核心题只有总括容器的问题，但仍存在标题版本、起诉状证据栏、source-check 红线和边界题误用风险。
- 执行：
  - 生成 `12_final_baodian/选必二法律主观题满分训练宝典_v5_7_27核心38题保分索引小修版_20260521.md`。
  - 生成 `05_reasoner_packets/v5_7_gptpro_claude_review_packet_20260521.zip`。
- 限制：V5.7 只允许进入 GPTPro/Claude 真实复审；不得直接宣布最终定稿。
# D88 - V5.7 external review can run, but final promotion is blocked

- time: 2026-05-21 03:49 CST
- decision: Submit the same V5.7 review packet to GPTPro and Claude Opus, then wait for natural completion before any V5.8/final Word-PDF decision.
- reason: V5.7 is locally improved but still requires dual external review of student usability, 27 core answer quality, and 38 non-core guardrails.
- constraint: GPTPro front prompt had a garbled/fragmented UI-transmission risk; accept the GPTPro output only if it visibly follows the packet-internal V5.7 prompt. Otherwise rerun after completion with a clean paste.

# D89 - V5.8 may exist only as a local candidate until GPTPro V5.7 is captured

- time: 2026-05-21 04:00 CST
- decision: Apply Claude-backed P1/P2 fixes into a new V5.8 candidate file without overwriting V5.7. Do not promote to Word/PDF or final release until GPTPro V5.7 is captured and cross-validated.
- reason: Claude Opus V5.7 returned CONDITIONAL_PASS / YES_WITH_GUARDS with no P0, but flagged one P1: core entries still violate the “1 主卡 + 最多 1 辅卡” rule.
- accepted local fixes: 27 core entries normalized; CC0025 moral/value point patched; non-core cards get question_id titles and visual redlines; CC0245 becomes a cross-reference to core question 16; 70-to-65 delta ledger is created.
- evidence boundary: model review is advisory; source evidence and current 65 corpus remain authoritative.

# D91 - Rerun GPTPro cleanly against V5.8 instead of trusting the garbled V5.7 state

- time: 2026-05-21 04:17 CST
- decision: Treat the prior GPTPro V5.7 browser status as unreliable and submit a clean V5.8 final-gate packet once.
- reason: The Safari tab showed an older V5.2 review, while the composer still contained a garbled fragment. Accepting that as V5.7/V5.8 review would violate the external-review gate.
- execution: Uploaded `05_reasoner_packets/v5_8_gptpro_final_gate_packet_20260521.zip` and sent one ASCII visible prompt pointing GPTPro to the packet-internal prompt and README.
- constraint: Do not interrupt the running GPTPro response. Valid promotion requires captured output that visibly follows V5.8 packet checks.

# D92 - Run V5.8 through both GPTPro and Claude before Word/PDF promotion

- time: 2026-05-21 04:20 CST
- decision: Submit V5.8 to Claude Opus 4.7 as a parallel final-gate reviewer instead of relying only on GPTPro plus the earlier Claude V5.7 review.
- reason: V5.8 is a patch derived from Claude V5.7 feedback, but it still needs a direct V5.8-specific external check before Word/PDF promotion.
- execution: Created `handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_V5_8_FINAL_GATE_REVIEW_20260521.md` and submitted it once in Claude desktop/Cowork.
- constraint: Final promotion remains blocked until both V5.8 final-gate outputs are captured and compared.

# D97 - Promote V5.9 only to guarded Word/PDF candidate

- time: 2026-05-21 05:00 CST
- decision: After GPTPro V5.8 and Claude Opus V5.8 both returned `PASS / YES_WITH_GUARDS`, generate V5.9 and promote it only to a guarded Word/PDF candidate.
- reason: 双审同意 V5.8 已无 P0/P1，可进入 Word/PDF candidate；但二者都要求保留 27 核心 + 38 guard/index 的边界，不允许声称 65 题全部核心满分闭环。
- accepted fixes: low-frequency visual redlines, source-check/reference/boundary/transfer warning bands, CSV 主辅卡字段同步, CC0223 material-trigger cleanup, CC0150 cross-module atom quarantine, and export-script fix for inline-code `\1` residue.
- resulting artifacts: `12_final_baodian/选必二法律主观题满分训练宝典_v5_9_27核心38题保分索引_双审门禁修补版_20260521.docx`; `12_final_baodian/word_pdf_v5_9/选必二法律主观题满分训练宝典_v5_9_27核心38题保分索引_双审门禁修补版_20260521.pdf`.
- constraint: V5.9 is readable candidate output, not evidence promotion. Source-check rows and non-core rows remain non-core until source-level review says otherwise.

# D98 - V5.9 blind test confirms learnability, not all-65 promotion

- time: 2026-05-21 05:08 CST
- decision: Treat the 8-question zero-baseline blind test as `PASS_WITH_GUARDS` for V5.9 student usability.
- reason: The simulated student wrote near-full answers for 4 strict-core samples and correctly quarantined 4 non-core samples as low-frequency/source-check/reference-only/boundary.
- accepted result: V5.9 can be shown to the user as a guarded candidate handbook.
- rejected interpretation: The blind test does not promote the 38 non-core rows into strict core and does not close the 24 source-check rows.
- follow-up: Fix the `CC0244` source-card ask_text mismatch and run source-check backtracking before any later core expansion.

# D100 - Demote V5.9 from candidate finish to attack sample

- time: 2026-05-21 05:27 CST
- decision: Treat V5.9 as an attack sample rather than a satisfactory final candidate after the user rejected its student usefulness.
- reason: Even if V5.8/V5.9 passed guarded external gates, the user judged the framework still fails the true acceptance criterion: a smart but untrained high school student should read it and immediately know how to write full-score answers.
- execution: Sent a dedicated attack-review packet to GPTPro and Claude Opus 4.7 Cowork; also launched a local zero-baseline student/harsh grader agent.
- constraint: V6 must preserve the 65-question evidence bottom line and 27 core + 38 non-core discipline, while rebuilding the student-facing framework around stronger prior-framework DNA and clearer exam-room actions.

# D101 - Accept attack-review verdict and rebuild V6 around student startup

- time: 2026-05-21 CST
- decision: Accept GPTPro and Claude Opus 4.7's shared `PASS_WITH_MAJOR_REWRITE` verdict. V5.9 remains only a material bottom draft; it is not a student-final handbook.
- reason: Both external lanes plus Codex/student-agent converged on the same failure: V5.9 is evidence safer than earlier versions but does not train naked-question entry, question-tail diagnosis, material-to-law translation, or boundary downgrading.
- accepted fixes: add question-tail diagnosis tree, three answer skeletons, question-level forbidden-expression table, easy-confusion comparison boxes, three-sentence floor answers, and per-noncore applicable/not-applicable ask conditions.
- constraint: 38 non-core rows stay non-core; reference_only rows stay reference_only; V6 must pass a new naked blind test before Word/PDF promotion.

# D102 - Void the V5.9 labeled blind test as acceptance evidence

- time: 2026-05-21 CST
- decision: Mark the V5.9 blind test as invalid for final student-transfer acceptance.
- reason: The student answer file exposed `question_id`, `category_for_grader`, `strict_core`, `source_check_pending`, `reference_only_locked`, and boundary labels. This tests label-following, not independent exam-room routing.
- consequence: V6 acceptance requires a new blind test with only original material and ask text, hiding ids, categories, and core/guard labels.

# D103 - Promote V6.2 only as external-review candidate

- time: 2026-05-21 06:15 CST
- decision: Use V6.2 as the current student-draft candidate for GPTPro / Claude Opus second review, not as final.
- reason: Naked blind testing showed real progress in independent startup, but local strict review found CC0244 no-fault product liability was not front-loaded enough.
- accepted fixes: CC0244 no-fault product liability front-loaded; table answers changed to direct per-cell output; AI copyright subject exclusion front-loaded; reference_only/source-check remain non-core.
- consequence: Word/PDF封版 and “学生读完稳定满分” remain blocked until external V6.2 reviews are captured and adjudicated.

# D104 - Create V6.3 local hygiene candidate without waiting for external review

- time: 2026-05-21 CST
- decision: Generate a V6.3 local hard-fix candidate while GPTPro / Claude Opus V6.2 reviews are still running.
- reason: Codex A found self-evident student-facing defects in V6.2: pre-set-sounding summary language, backend card labels, table-question template pollution, and placeholder-like row names. These do not require external permission to fix.
- accepted fixes: remove the “一二三四五总图” student-facing section; replace backend labels with exam-room task language; repair the table-question “先判合同” error; relabel generic material rows; warn that full-score sentence parts are not whole-paragraph memorization.
- consequence: V6.3 becomes the current local synthesis base, but not a final candidate. External V6.2 outputs still must be captured and adjudicated before V6.4 / Word/PDF promotion.

# D105 - Merge GPTPro and Claude V6.2 reviews into V6.4 instead of defending V6.2

- time: 2026-05-21 06:55 CST
- decision: Accept both external reviewers' `CONDITIONAL_PASS` verdicts and build V6.4 as a hard patch, not a cosmetic revision.
- reason: GPTPro and Claude converged on the same defects: C/E/G/H still had hard-score risks, table rows needed real material translation, CC0223 carried source/ask pollution, and CC0244 product-liability wording was too absolute.
- accepted fixes: fill the 27 core material-translation tables, clean CC0223 ask/material, force real table-cell output, and distinguish seller/producer liability in CC0244.
- consequence: V6.4 must pass a targeted naked-question regression test before any student-clean version is trusted.

# D106 - Treat V6.4 regression as conditional, then patch the exact lost term

- time: 2026-05-21 06:55 CST
- decision: Mark V6.4 C/E/G/H regression as `CONDITIONAL_PASS`, not full pass, because the table sample missed explicit causation/non-causation wording.
- reason: The student chose the correct route and filled the table directly, but a high-stakes rubric term was absent. This is exactly the kind of miss the handbook must prevent.
- accepted fix: V6.5 adds a table-cell rule: material fact cells must include `事实 + 因果/非因果判断` when responsibility depends on causation.
- verification: One-question V6.5 miniregression passed; the student wrote `自身疾病突发` and `组织行为与死亡无因果关系`.

# D107 - Promote V6.7 only as the current best student-use candidate

- time: 2026-05-21 06:55 CST
- decision: Generate V6.7 Markdown/DOCX as the best current student-use candidate, while blocking final all-65 closure and PDF封版.
- reason: V6.7 strips engineering logs and raw audit labels, keeps the 27 core / 38 non-core boundary visible, and has passed local structure hygiene plus first-page visual QA. It has not passed full-page render QA or final GPTPro/Claude student-use review.
- accepted output: `12_final_baodian/选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.md` and `.docx`.
- rejected interpretation: V6.7 is not proof that 65 questions are all core full-score templates; it is a guarded student handbook candidate grounded in the current 65-question corpus discipline.

# D108 - Prepare V6.7 external-review packet before touching web UI again

- time: 2026-05-21 06:58 CST
- decision: Create a complete V6.7 final student-usability review packet and ASCII visible prompt before any GPTPro/Claude web submission.
- reason: Earlier web handoff had two real risks: Chinese prompt garbling in GPT and repeated send-button clicks interrupting Claude. The next external review should be one deliberate upload/send only.
- accepted packet: `05_reasoner_packets/v6_7_final_student_usability_review_20260521.zip`.
- acceptance rule: GPTPro/Claude outputs count only if they explicitly review V6.7, retain the `27 核心 + 38 保分索引` boundary, and issue `PASS / CONDITIONAL_PASS / FAIL` with concrete P0/P1/P2 fixes.

# D109 - Supersede V6.7 with V6.8 before external submission

- time: 2026-05-21 07:04 CST
- decision: Do not submit the V6.7 packet. Submit V6.8 instead after repairing the missing first table-core title and startup sections.
- reason: A local hard scan found that V6.7's first `表格补全战场` core example jumped directly to `完整考场版答案`, which would make the student-facing training incomplete.
- accepted fix: V6.8 restores `核心题 19: 2026 通州 一模 第20题`, sections 1-6, material translation table, full-score parts, and causation hard term.
- consequence: V6.8 becomes the current candidate for GPTPro/Claude final student-usability review. V6.7 remains history only.

# D110 - Supersede V6.8 with V6.9 because 27-core integrity failed

- time: 2026-05-21 07:10 CST
- decision: Do not submit V6.8. Submit V6.9 instead after restoring the missing core question 18.
- reason: The automated 27-core section audit found only 26 core titles in V6.8. A student handbook that claims 27 core questions but silently omits one core case is not acceptable.
- accepted fix: Restore `RECOVER_2025_海淀_二模_18` with title, source status, sections 1-9, improved material translation table, and no placeholder rows.
- verification: `10_framework_validation/v6_9_core_section_integrity_audit_20260521.md` reports 27/27 core titles and all 1-9 sections present.
- consequence: V6.9 is the only current candidate for final GPTPro/Claude student-usability review.

## Decision - STEP_110 V7 Method-First Reset

- time: 2026-05-21 07:33:17
- decision: 回退到“先学习用户先前框架方法，再分批处理法律题”的外审路径。
- reason: 用户明确认为当前框架仍不能让学生满分；直接喂 65 题给模型会导致模型只总结材料而不学会先前框架的学生启动结构。
- accepted_method: prior-framework DNA first; V6.9 only as failed candidate to critique; four batched evidence packs; final V7 only after GPTPro and Claude Opus independent outputs.
- rejected_method: one-shot 65-question synthesis; treating V6.9 as final; using Codex local simulation as substitute for real GPTPro/Claude Opus.

## Decision STEP_111: V7 先补证据底座再写框架

Claude Opus 明确指出 V6.9 的问题不是零件缺，而是前台主轴和证据污染。决定：V7 不沿用九战场作为前台，不直接复用污染 source-card；先建立 CC0223/CC0150/CC0244 清洗台账，再等待 GPTPro 同步批判。

## Decision STEP_114: V7.1 只作为候选稿，先修 source-card 再封版

- time: 2026-05-21 09:27 CST
- decision: V7.1 的方法主轴可以继续推进，但不能称为最终宝典；必须先处理 19 个空设问和 3 个高风险题卡。
- reason: GPTPro/Claude 已完成“先学旧框架方法 + 分批处理题”的 V7 外审，但源卡层仍有空设问、答案倒推题面、跨模块细则污染和长原子混杂风险。学生文档如果越过这一步，会再次变成看似完整但踩分链不稳。
- accepted_next: 生成 `v7_1_source_repair_queue_20260521`；repair_now/clean/split 行可进入教师证据补丁，source_confirm_required 行必须回源或降级。
- rejected_interpretation: 不得因为 V7.1 定向回归无 FAIL，就宣称 65 题全部满分闭合。

## Decision STEP_117: V8 从学生可启动性重建，不再润色 V7.1

- time: 2026-05-21 17:23 CST
- decision: 启动 `v8_student_usable_rebuild`；V7.1 被判定为需要重构的学生稿，而不是待润色终稿。
- evidence_baseline: `04_merge_audit/boundary_patched_20260519/`，53 题、535 材料原子、53 设问原子、319 细则原子；37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE。
- reason: 用户明确要求从“学生看完能不能满分”重新验收。当前 V7.1 仍存在设问触发缺失、最小判断泛化、逐题运行像答案复述、学生版与证据版混杂等问题。
- accepted_next: 先完成失败诊断，再让 GPT-5.5 Pro 与 Claude Opus 同题同问审 v7.1、选 8 金样板、提出学生动作框架建议；8 道金样板完成后才能写 v8 学生框架。
- rejected_method: 继续小修 V7.1；直接把 53/65/70 题一股脑喂模型生成总框架；让 OPEN_OR_REFERENCE 单独支撑核心节点；pending 回流；恢复 CC0229 旧坏词。


## Decision STEP_119: V8 金样板采用 7 PASS + 1 PASS_RECOVERED 组合
- 时间：2026-05-21 17:53 CST
- 决策：最终 8 道金样板为 CC0137、CC0238、CC0305、CC0054、CC0103、CC0025、CC0125、CC0002。
- 理由：覆盖 8 类机制；全部 formal；OPEN_OR_REFERENCE 为 0；平台劳动题采用 CC0025 是因为其 PASS formal 且材料/细则更厚；CC0373 作为多主体表态后续验证题。
- 防污染：CC0229 不作为金样板，避免旧错配表达风险；pending 三题和 CC0250 不进入金样板。

## Decision STEP_121: V8 交付为 CONDITIONAL_PASS，不冒充终极闭合

- 时间：2026-05-21 18:18 CST
- 决策：`v8_student_usable_rebuild` 可以交付用户审阅，但验收等级只能写 `CONDITIONAL_PASS`。
- 理由：v8 已完成失败诊断、GPT/Claude 外审、8 金样板、学生版框架、教师证据版、23 条句库、53 题运行、宝典 md/docx 与学生模拟验收；但非金样板 45 题仍为批量重写稿，部分 ask 缺失仍需回源补齐，不能称为最终 full PASS。
- 接受产物：`07_选必二法律主观题满分宝典_v8.md`、`.docx`、`08_v8_student_usability_test.md`、`08_v8_acceptance_report.md`。
- 拒绝解释：不得把 v8 说成 70 candidates 全闭合；不得把 OPEN_OR_REFERENCE 当核心证据；不得把当前 DOCX 当作已完成全页视觉 QA 的最终出版稿。

## Decision STEP_123: v8.1 修交付稿，但仍不标 full PASS

- 时间：2026-05-21 21:21 CST
- 决策：启动并完成 `v8_1_student_delivery_fix`，把 v8 中不可交付的逐题运行和宝典修成可审阅的条件交付版。
- 理由：GPT 审稿指出 v8 的学生框架和金样板可保留，但 53 题逐题运行仍有自动草稿、设问缺失、材料错配和细则摘抄问题；继续润色 v8 会掩盖交付风险。
- 接受修复：
  - 8 道金样板同步替换进逐题运行。
  - 20 道设问缺失题中 16 道补设问，4 道进入附录。
  - 优先 10 题学生化重写。
  - N4 增加合同、劳动、侵权、消费者、知识产权、多方过错、竞业限制分支速查。
  - 句库补到 30 条，并加入指定七类模板。
  - 教师证据框架删除 gold 占位符。
  - 学生正文硬 QA 复扫 0 命中。
- 拒绝解释：不得把 v8.1 说成最终 full PASS；不得说 53 题全部人工精雕；不得把 DOCX 说成已通过全页视觉渲染 QA。

## Decision STEP_124: 停止 v8.1，启动 v9 飞哥风格重建

- 时间：2026-05-21 21:53 CST
- 决策：停止 `v8_1_student_delivery_fix`；不再继续修 53 题运行，不再生成 DOCX，不再做工程验收化补丁；启动 `v9_feige_style_rebuild`。
- 理由：用户明确判定 v8/v8.1 最大问题不是证据不足，而是成品风格错误，像 AI 教学法手册、工程验收报告和长篇讲义，不像已经成功的飞哥课堂框架。
- 接受方法：先学习旧框架风格 DNA，再写先导、飞哥课堂版主框架、正向触发、反向筛查、高频答题语言和 10 道极简演练。
- 拒绝方法：沿用 v8 节点 0-6；在学生正文出现工程证据语言；继续扩展 65/70；pending 回流；OPEN_OR_REFERENCE 支撑核心；把高中选必二写成法考或必修三套话。
- 当前产物：`v9_feige_style_rebuild/01_飞哥旧框架风格DNA.md` 至 `08_v9_style_acceptance.md`。

## Decision STEP_125: v10 改为“框架穷尽 + 53 题全量题链”

- 时间：2026-05-21 22:53 CST
- 决策：停止任何以少量题先行或代表题演练为中心的产品结构；v10 最终产品结构改为《选必二法律主观题穷尽框架与全题宝典》：上篇穷尽框架，下篇 53 题全量题链。
- 理由：用户明确纠正，真正需求不是挑题示范，而是前半部分把 53 题出现过的机制全部穷尽进框架，后半部分把 53 题全部逐题跑框架。
- 接受方法：先生成 `01_框架穷尽清单`，再由 01 推出上篇、下篇、覆盖矩阵和验收。
- 接受边界：唯一语料仍是 boundary-patched 53 题；37 PASS / 11 PASS_RECOVERED / 5 OPEN_OR_REFERENCE；pending 三题不纳入；CC0250 不回流。
- 拒绝方法：不再使用“金样板题”或“10 道极简演练”；不得说 53 题以后补；不得把 53 题放成可选附录；不得扩大到 65/70。
- 当前裁定：`v10_exhaustive_framework_and_all_questions/05_v10_acceptance.md` 为 `EXHAUSTIVE_FRAMEWORK_PASS`。

## Decision STEP_126: v10 PASS 作废，v11 改为先回源审判再分诊

- 时间：2026-05-21 23:38 CST
- 决策：停止 v10；`EXHAUSTIVE_FRAMEWORK_PASS` 作废，不得作为后续成品依据。
- 理由：GPT 审核指出 v10 的根本问题不是细度不足，而是题源/材料/触发错配和覆盖矩阵虚高；继续沿 v10 写宝典会把自动匹配垃圾固化。
- 接受方法：每题先回源确定真实设问、真实材料核心、真实法律主轴、1 个主入口、最多 3 个主材料触发、禁止命中点，再写强分诊清单和题链。
- 已接受修复：CC0002、CC0011、CC0025、CC0137、CC0143、CC0254、CC0131、CC0289 等失败样例必须逐一修复；其中 CC0011、CC0131、CC0137、CC0254、CC0289 已在 01A 回源补丁中修复。
- 拒绝方法：不得先用框架自动匹配题目；不得万能命中合同、纠纷解决、意义价值；不得把参考答案、评分细则、设问要素、分析说明当材料触发。

## Decision STEP_129: v11.1 只修 P0 书面题链，不进入 24 题回填

- 时间：2026-05-22 12:35 CST
- 决策：启动并完成 `v11_1_written_chain_patch`，只修 GPT 点名的已写题链 P0 错误与 01 报告版本残留。
- 理由：GPT 判定 v11 方向正确，但 CC0200、CC0238、CC0137 仍有 P0 主轴/入口/漏格错误；若直接进入 24 题回填，会把现有错链继续扩散。
- 接受修复：
  - CC0200 改为未成年人打赏、多方过错、公平原则分责。
  - CC0238 改为评析入口，一主体一链。
  - CC0137 补齐 AI 著作权格和信用卡合同违约格。
  - CC0229 强化为三案例法律手段链。
  - CC0305 标注设问待补，不伪装完全闭合。
- 验收边界：`V11_1_WRITTEN_CHAIN_PATCH_PASS` 只代表本轮补丁通过；不代表最终宝典通过，不允许自动进入 24 题回填，不允许生成 DOCX。

## Decision STEP_130: v12 只回填 source-lock 通过的 18 题，6 题不得硬写

- 时间：2026-05-22 13:16 CST
- 决策：执行 `v12_24_question_backfill`；24 题中只有 18 题同时锁住真实设问、真实材料核心和可用正式口径，进入 `02_24题回填题链`。
- 进入回填的 18 题：CC0019、CC0051、CC0077、CC0084、CC0092、CC0119、CC0157、CC0180、CC0189、CC0195、CC0206、CC0213、CC0214、CC0223、CC0245、CC0283、CC0325、CC0364。
- 不进入正文的 6 题：CC0251、CC0276、CC0277、CC0317、CC0318、CC0319。
- 理由：这 6 题当前只能看到答案/评标/讲评线索，或原题材料与设问无法可靠锁定；若硬写，会再次把答案、细则或讲评内容冒充材料。
- 接受产物：`v12_24_question_backfill/03_all_53_question_chains_v12.md/.csv` 为条件版，正文 47 题；6 题移入 `04_无法回填或降级清单.md/.csv`。
- 验收边界：`07_v12_acceptance.md` 只能写 `CONDITIONAL_PASS`；不得写最终宝典、不得生成 DOCX、不得写 `TASK_COMPLETE`。


## 2026-05-22 15:52:45 Decision: v12.1 keeps conditional stage split
- 不再说 47 道 source-locked；当前口径固定为 42 正文 + 5 OPEN_OR_REFERENCE 参考 + 6 未纳入。
- OPEN_OR_REFERENCE 不进入核心矩阵，不支撑核心框架。
- 6 道源寻题即使找到线索，也只作为下一版回填候选，本阶段不硬并入正文。
