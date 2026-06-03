# RISKS

## 2026-05-21T23:20:23+08:00 - R036 v10 Auto-Match Contamination

Status: active_blocker_for_v11_framework_and_baodian.

Risk: v10's all-question chain and coverage matrix are not trustworthy because many rows used answer/rubric/analysis text as material triggers and inflated framework coverage through universal buckets such as contract, procedure, and meaning/value.

Impact: Any framework or宝典 generated directly from v10 can look complete while teaching students the wrong entrance and wrong material trigger.

Mitigation: v11 starts with `01_53题回源审判表.csv`. Rows marked `待用户确认`, `降级参考`, material-polluted, or source-repair-needed cannot enter the student chain until repaired. v10 acceptance is forbidden as a completion claim.

## 2026-05-20T00:22:15+08:00 - R035 ClaudeCode Formal Channel Mismatch

Status: active_governance_risk.

Risk: the suite-exhaustion ClaudeCode audit and patch-verification records show `claude -p` CLI commands (`tool_outputs/claudecode_suite_exhaustion_audit_command_20260519.txt`, `tool_outputs/claudecode_patch_verification_command_20260519.txt`). This does not satisfy the user's later hard rule that official ClaudeCode work must be opened through VS Code, not CLI.

Impact: the content of that audit remains useful as a source-check/provisional ClaudeCode-Cli evidence lane and was further checked by Codex, Claude Cowork, GPTPro, and local source patches. But final reporting must not call it a fully compliant "ClaudeCode VS Code audit" unless rerun/captured through VS Code.

Mitigation: keep the 65-question guarded v2 package's evidence labels and local/GPTPro validation, but mark the ClaudeCode formal-channel claim as provisional. If the user requires strict four-lane formal compliance before final release, rerun the suite-exhaustion audit and patch verification from VS Code ClaudeCode and compare against the current 65-question corpus.

| risk_id | status | risk | mitigation |
| --- | --- | --- | --- |
| R001 | open | Some PDFs or scanned pages may lack text layer, and local tesseract/pdftotext are unavailable. | Use Python PDF extraction and page rendering metadata; record OCR gaps in failed_files.csv and locator risks. |
| R002 | open | Real GPT-5.5 Pro / Claude Opus web-visible calls may not be directly callable from current tool context. | Save exact prompts in handoff_prompts and mark downstream gates real_call_pending until captured. |
| R003 | open | Source roots exist both on Desktop and in GaokaoPolitics mirror, creating duplicates. | Hash files and link duplicates in source_manifest linked_files. |
| R004 | open | Old 选必二 outputs in project workspace could contaminate new framework. | Exclude old 选必二 generated artifacts from evidence promotion; record only as risk/path context. |
| R005 | open | Reference answers may look like rubrics. | Use conservative evidence_level and require formal rubric/marking/report/explicit scoring for core nodes. |
| R006 | mitigated | Official GPT-5.5 Pro and Claude Opus web-visible open-observation calls might be unavailable or uncaptured. | Both cowork-refined open-observation calls completed naturally and were captured under `06_open_observations/` with status logs in `tool_outputs/`. |
| R007 | mitigated | First external-model packet contained only 35 high-confidence formal questions, under-covering the merged 74-question universe. | Reclassified as trial-only, rebuilt v2 full-context packet with 74 questions and 57 observation-eligible rows, and stopped/failed the old external calls. |
| R008 | mitigated | Missing-17 review showed merged evidence levels were stale: many formal rubrics existed but were not linked, while several choice-answer snippets were mis-collected as subjective questions. | v3 packet rebuilt with 70 candidates, 65 formal, 5 reference_only, missing 0; official GPT/Claude calls must use v3 only. |
| R009 | open | UI clicks on Claude/ChatGPT controls can interrupt active external-model thinking. | Do not click send, stop, retry, or regenerate while models are thinking; only observe status and capture completed output. |
| R010 | open | v1 PASS count can be misread as the total number of legal subjective questions. | Maintain separate counts for strict-core PASS, recovered formal core, open/reference container, pending legal-rubric cases, and excluded non-law/mismatch cases. |
| R011 | open | Some mixed parent rows contain a legal small question but also economics, logic, or politics material; counting the parent inflates or distorts the law corpus. | Split verified legal subquestions into new question_ids and mark parent units as not counted. |
| R012 | open | Claude Opus boundary-recovery upload is currently blocked in the UI. | Preserve the packet and prompt; do not repeatedly click send/attachment; proceed with local source checks and GPT capture while recording Claude as real_call_upload_blocked if it remains unavailable. |
| R013 | open | Existing final baodian contains provisional/bad boundary sections for CC0094, CC0229, CC0250, and CC0373. | Added a correction addendum and downgraded final delivery status; regenerate affected sections only after atom patch queue is complete. |
| R014 | open | CC0229 is a valid law question by source text but has misbound rubric atoms. | Block it from core support/final full-score closure until F0153/F0146 scoring atoms replace the bad mapping. |
| R015 | open | CC0094 looks like a legal small question but mixes law and politics and has wrong atoms. | Treat as split_or_deduplicate pending; do not count as open-container until a legal-only unit is extracted. |
| R016 | mitigated | Split patch records existed outside canonical merged files, so downstream scripts that read only 04_merge_audit could miss recovered small questions. | Generated `04_merge_audit/boundary_patched_20260519/` and `boundary_patched_canonical_corpus_20260519.zip` as the clean patched corpus. |
| R017 | mitigated | `full_score_sentence_bank.csv` reflected the earlier sentence-bank export, not a full regeneration from the boundary-patched corpus. | Regenerated to 53 rows from the boundary-patched corpus; previous version backed up. |
| R018 | mitigated | Word/WPS visual QA was not complete because local `soffice` is unavailable. | Microsoft Word opened/saved the DOCX, exported PDF, and the PDF rendered to 198 PNG pages with no suspect blank pages; see `DOCX_QA_WORD_PDF_RENDER.md`. |
| R019 | partially_mitigated | Net-17 recheck found the 53-row boundary-patched package is not source-exhaustive: three non-midterm law subjective questions were missed while excluding different non-law rows from the same suites. | Recovered 2024顺义二模 Q17, 2025海淀二模 Q18, and 2026通州一模 Q20 into `boundary_recovered_20260519` as a 56-row corpus. Remaining risk: sidecars, framework validation, handbook sections, and Word/PDF outputs still need regeneration. |
| R020 | open | The 56-row recovery still was not suite-exhaustive; suite-level audit found 10 more formal core law subjective rows and 6 boundary/blocked cases. | Generated `suite_exhaustive_20260519` as the new 66-row corpus and marked old GPT/Claude/model outputs superseded. Remaining risk: real GPT-5.5 Pro and Claude Opus must be rerun from the 66-row packet before any framework/codebook/final宝典 claim. |


## 2026-05-19T13:55:00+08:00 - Remaining Risks

- DOCX visual render could not be completed because `soffice` is unavailable; structural DOCX validation passed.
- 20 merged candidates failed the law-framework pressure test and require manual/source-level boundary confirmation before any classroom release.
- 13 PARTIAL candidates include low-frequency or reference_only cases; they should not be promoted without new formal evidence and another model/source validation round.
- Boundary recovery has reduced the “35/37 only” problem. GPT boundary recovery review is captured; CC0229 is patched; split patch records exist. Final v2/宝典 release remains blocked until canonical integration and document regeneration.
- 2026-05-19 later recheck: the 53-row patched corpus is no longer source-exhaustive. It remains useful as a bounded release candidate only. Missing recoveries 2024顺义二模 Q17, 2025海淀二模 Q18, and 2026通州一模 Q20 have been added to a 56-row recovered corpus, but final deliverables are not yet regenerated.
- 2026-05-19 suite-level exhaustion: the 56-row corpus is also superseded. Current core corpus is 66 rows; old GPT/Claude observations/framework outputs cannot be used for final framework generation until rerun on the suite-exhaustive packet.

## 2026-05-19T16:11:46+08:00 - R021 Old Model Outputs Superseded By ClaudeCode-Corrected Corpus

Status: active until GPT-5.5 Pro and Claude Opus are rerun with the corrected 65-question packet.

Risk: any observation, codebook, framework, pressure test, or handbook section generated from 53/56/66-row packets may omit `RECOVER_2026_朝阳_期末_18_1`, include removed boundary rows, or preserve wrong 期中/期末 labels.

Mitigation: use only `05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519/` for new model calls; `06_open_observations/SUPERSEDED_BY_CLAUDECODE_CORRECTED_20260519.md` records this.

## 2026-05-19T16:11:46+08:00 - R022 Remaining OCR/Source Risks After PASS

Status: visible_non_blocking_risk.

Remaining items: 2026朝阳期末 OCR recovered via rendered pages; 2026丰台期末 mixed boundary still awaits optional OCR split check; 2026西城期末 formal rubric OCR may upgrade CC0353 from reference_only if recovered; 2026石景山期末 remains user-excluded/source-blocked.

Mitigation: keep risks in audit files and do not let reference_only support core nodes alone.

## 2026-05-19T16:25:00+08:00 - R023 Claude Cowork Desktop Task May Not Write Local Files

Status: active until Cowork output is captured.

Risk: Claude Cowork may be able to read the uploaded packet but not directly write to `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/claude_cowork_question_refinement_20260519/`.

Mitigation: the prompt instructs Cowork to output the eight required files as named sections if local writing is unavailable; Codex will save the returned sections locally and keep the original prompt in `handoff_prompts/`.

## 2026-05-19T16:32:00+08:00 - R024 Question Layer Contamination Before Reasoner

Status: active_blocker.

Risk: 24 corrected-core rows have missing `ask_text` and/or question/material fields that appear to contain answer or rubric text. If sent as-is, GPT-5.5 Pro and Claude Opus could infer framework observations from评分口径 rather than from the actual题干/材料/设问.

Mitigation: hold the reasoner rerun; use `codex_question_layer_source_snippets.md`, source files, and Claude Cowork output to repair or explicitly clear these rows before rebuilding the packet.

## 2026-05-19T17:01:41+08:00 - R024 Mitigated By Cowork-Refined Packet

Status: mitigated for the current reasoner gate.

Result: `suite_exhaustive_cowork_refined_20260519` has 0 empty asks, 0 material-equals-rubric rows, 0 material contamination marker rows, 0 broken rubric-material refs, and 0 known logic-rubric leaks.

Residual risk: GPT-5.5 Pro and Claude Opus must now be rerun from the cowork-refined packet. Old 53/56/66/v3/ClaudeCode-corrected observations, codebook, framework, pressure test, and宝典 remain superseded.

## 2026-05-19T17:11:52+08:00 - R025 External Model Runs Can Be Interrupted By UI Misclicks

Status: mitigated for open-observation; still applies to future candidate-framework calls.

Risk: GPT-5.5 Pro and Claude Opus official lanes can be invalidated by extra clicks on stop/retry/regenerate/send.

Mitigation: the cowork-refined open-observation calls were captured after natural completion. For candidate-framework calls, Codex must again submit once and then wait.

## 2026-05-19T17:45:00+08:00 - R026 Codebook Is Provisional, Not Framework

Status: active.

Risk: The 7-row codebook is source-checked and dual-model supported, but it is intentionally conservative. Pending observations include IP/innovation, AI/digital, labor/new employment, module leakage, material-quote precision, and weak/reference-only patterns that may need open-container treatment.

Mitigation: do not generate the final framework locally from the codebook alone. Send the codebook-bound candidate-framework prompt to real GPT-5.5 Pro and Claude Opus, then pressure-test against all 65 core questions before any final framework or宝典 regeneration.

## 2026-05-19T17:53:35+08:00 - R027 Candidate Framework Calls Must Complete Naturally

Status: active.

Risk: The candidate-framework stage can be invalidated by accidental stop/retry/send clicks or by capturing a partial answer as if complete.

Mitigation: both candidate-framework calls have been submitted once and status files say `SUBMITTED_WAITING`. Do not click stop/retry/regenerate/send. Capture outputs only after the UI indicates completion, then save raw outputs before any Codex synthesis.

## 2026-05-19T18:08:33+08:00 - R027 Mitigated For Candidate Framework Capture

Status: mitigated for the current candidate-framework gate.

Result: both candidate-framework calls completed naturally and were captured: GPT-5.5 Pro to `09_candidate_frameworks/gpt55pro_candidate_frameworks_cowork_refined_20260519.md`, Claude Opus to `09_candidate_frameworks/claude_opus_candidate_frameworks_cowork_refined_20260519.md`.

Residual risk: the captured proposals agree that the 7-row codebook directly supports only 16/65 questions. Local synthesis must not pretend this is a final full-coverage framework; all 65 questions still require pressure testing and gap handling.

## 2026-05-19T18:18:00+08:00 - R028 Framework v1 Starts More Than It Closes

Status: active_blocker_for_final.

Risk: `framework_v1` can route many questions by设问/material signal, but only 16 rows are directly supported by the current codebook. Treating the 45 formal PARTIAL rows as PASS would repeat the earlier false-closure problem in a cleaner-looking form.

Mitigation: pressure-test report explicitly separates PASS from PARTIAL; final framework and baodian remain blocked until PARTIAL clusters are source-checked and either promoted through evidence-backed codebook expansion or quarantined as open-container examples.

## 2026-05-19T18:27:27+08:00 - R029 Claude Cowork All-Question Completion Must Not Be Interrupted

Status: mitigated for Cowork completion capture.

Risk: the user specifically reported that extra clicking can stop Claude thinking. If Codex clicks stop/retry/send again while the Cowork task is running, the output may become partial or invalid as external evidence.

Mitigation: the Cowork task completed naturally and output was captured into `04_merge_audit/claude_cowork_all_question_completion_20260519/`. No stop/retry/send action was used after submission.

## 2026-05-19T18:44:35+08:00 - R030 Cowork Expansion Candidates Could Be Over-Promoted

Status: active_blocker_for_codebook_v1.

Risk: Cowork proposes one new code and four code revisions, but they remain model-suggested observations until Codex source-checks exact rubric/material atom support and compares with GPT-5.5 Pro / Claude Opus expansion outputs.

Mitigation: keep `framework_v2` and final baodian blocked. Before promotion, verify the five source-check rows (CC0011, CC0019, CC0061, CC0254, RECOVER_2026_房山_一模_17_1), then run cross-model expansion adjudication.

## 2026-05-19T18:53:31+08:00 - R030 Partially Mitigated By Codex Source Check

Status: active_until_external_expansion_adjudication.

Result: the five Cowork-blocked rows have been source-checked. None are missing, but all need constrained handling: split collapsed scoring blocks, split/trim multi-subquestion rows, replace wrong source-segment atoms, or preserve alternative scoring dimensions.

Remaining risk: if the next GPT-5.5 Pro / Claude Opus packet omits `codex_source_check_corrected_rubric_atom_plan.csv`, models may still over-promote CC0254's student-problem lines or cumulate 房山 AI 题 alternative dimensions.

Mitigation: build the expansion packet from Cowork outputs plus Codex source-check outputs, and explicitly forbid final framework or宝典 revision during that call.

## 2026-05-19T19:03:00+08:00 - R031 Corrected Expansion Calls Must Complete Naturally

Status: mitigated_by_capture.

Risk: the corrected expansion adjudication now depends on two running external calls. Clicking stop/retry/regenerate/send, queueing extra messages, or capturing partial output would make the codebook expansion gate unreliable.

Mitigation: both calls were submitted once with the corrected packet visible. GPT and Claude outputs were captured after natural completion into `06_open_observations/`; no stop/retry/regenerate/send clicks were used after submission.

## 2026-05-19T19:44:37+08:00 - R032 Expansion Draft May Be Mistaken For Final Closure

Status: active_blocker_for_framework_v2_and_baodian.

Risk: the expansion draft raises direct core codebook support from 16 to 42 question_ids, but this can still be overread as full-score closure. It is only evidence-backed codebook support, not sentence-level framework validation.

Mitigation: `framework_v1_expansion_draft_pressure_snapshot_20260519.md` explicitly separates 42 core-support rows from 14 open-container rows, 5 reference/reject rows, 1 source-check row, and 3 no-support rows. Final framework v2 and final baodian remain blocked until all-65 sentence-level pressure test exists.

## 2026-05-19T19:44:37+08:00 - R033 CC0364 Giant Atom Still Blocks Strong Support

Status: active_source_check_needed.

Risk: `CC0364_2026_通州_期末_19_1` may support CODE_COWORK_004/006 after splitting, but the current single giant atom merges法理、事实、意义, making it unsafe to count as strong support.

Mitigation: keep `CC0364` as `SOURCE_CHECK_PENDING` in the expansion pressure snapshot. Do not count it as core support until a source split patch is written and audited.

## 2026-05-19T19:54:30+08:00 - R033 Mitigated By CC0364 Split

Status: mitigated.

Result: `CC0364` was split into seven source-checked formal scoring atoms and added only as limited 004/006 support. `PATCH_CC0364_R04` is marked alternative/non-cumulative, and value-tail atoms are explicitly blocked from standalone core-node use.

Residual risk: a later handbook writer could still over-score the fact section by adding 2+1 or start from value slogans. The v1.1 pressure test and codebook risks file now carry this warning.

## 2026-05-19T19:54:30+08:00 - R034 v1.1 Still Has 18 PARTIAL And 4 FAIL

Status: active_blocker_for_final_framework_and_baodian.

Risk: The sentence-level pressure test improved closure to PASS 43, but 18 PARTIAL rows and 4 FAIL rows remain. Treating these as solved would repeat the false-closure pattern the user objected to.

Mitigation: keep framework_v2 and final baodian blocked. The four FAIL rows require专项回源/边界 adjudication; the 14 formal open-container rows require either low-frequency node evidence or explicit quarantine; the 4 reference_only rows cannot support core nodes without formal细则.

## 2026-05-19T20:11:35+08:00 - R035 Claude Cowork FAIL4 Audit Is Stalled On Workspace Bash

Status: active_external_tool_risk.

Risk: The Claude Cowork FAIL4 task has directory access and is still responding, but repeated `mcp__workspace__bash` calls against the mounted project path timed out. A later `echo ok` diagnostic is also running. If we click Stop/Retry/Send/Queue, we may interrupt the model and invalidate the external audit lane.

Mitigation: do not click any interrupting controls. Poll only `audit.jsonl`, output folders, and the UI state. In parallel, keep local FAIL4 adjudication and patch candidates in separate files marked non-promotional until Cowork/GPT confirmation or explicit quarantine.

## 2026-05-19T20:24:00+08:00 - R035 Mitigated By Cowork Natural Completion

Status: mitigated.

Result: Claude Cowork recovered from the stalled workspace bash path by using file Glob/Read, wrote `fail4_targeted_adjudication_claude_cowork_20260519.csv` and `.md`, and agreed with local source adjudication on all four FAIL rows. No stop/retry/send/queue control was clicked after submission.

Residual risk: the v1.2 codebook still has only 44 direct core-support question_ids. The remaining PARTIAL rows are policy-classified, not full-score closed. Framework synthesis may proceed, but final baodian closure still requires a guarded 65-question rerun and explicit open/reference/boundary labels.

## 2026-05-19T20:31:00+08:00 - R036 Boundary Passes Could Be Misread As Core Full-Score Closure

Status: active_guardrail_for_final_outputs.

Risk: `framework_v1_2_pass_report_20260519.md` reports PASS 46 and FAIL 0, but two PASS rows are boundary-gate exclusions and 19 rows remain PARTIAL/open/reference. If a later writer collapses these distinctions, the project will again overclaim closure.

Mitigation: preserve the split in every downstream file: 44 core/pass, 2 boundary-gate pass, 19 PARTIAL. Final framework and baodian must label open/reference/boundary rows instead of writing them as ordinary full-score core examples.

## R037_GUARDED_V2_DOCX_VISUAL_QA_OPEN

- Status: mitigated_by_word_export_and_pdf_render.
- Risk: guarded v2 DOCX was structurally valid, but full Word/PDF page-by-page visual QA was not closed because `soffice` was unavailable and the first Word automation attempts failed.
- Update: Microsoft Word successfully opened the DOCX from an ASCII temp path and exported `12_final_baodian/选必二法律主观题满分宝典_GUARDED_V2_WORD_EXPORT.pdf`. PyMuPDF rendered all 114 pages under `12_final_baodian/visual_qa_guarded_v2/pdf_pages/`; blank-page detections: 0.
- Mitigation: final claim may now be `guarded v2 accepted with guards`, not unconditional "65 core full-score closure".

## R038_GPTPRO_RUNNING_EXTERNAL_REVIEW_CAN_BE_INTERRUPTED

- Status: mitigated_by_capture.
- Risk: GPT-5.5 Pro was running in Safari ChatGPT web after a single guarded v2 submission. Clicking Stop/Retry/Regenerate/Send, sending a follow-up, or copying partial output before completion would have made the external-review lane unreliable.
- Mitigation: GPTPro completed naturally; Codex A captured the completed output into `tool_outputs/gpt55pro_guarded_v2_review_response_20260519.md` and `06_open_observations/gpt55pro_guarded_v2_review_20260519.md`. No stop/retry/regenerate/send control was used after submission.

## R039_POST_SUBMISSION_LOCAL_PATCH_MAY_DESYNC_GPTPRO_PACKET

- Status: mitigated_by_cleanup.
- Risk: Codex A corrected `CC0380_2026_顺义_二模_18_2` locally after the GPTPro packet had already been submitted. The captured GPTPro review therefore reviewed a pre-CC0380-patch snapshot.
- Mitigation: completed GPTPro output was saved first, then compared against the local patch. GPTPro independently required `CC0380`/AI-open style rows to stay open-container/non-core, so Codex A applied the cleanup without sending an interrupting delta follow-up.

## R040_GPTPRO_CLEANUP_STILL_NOT_DOCX_PUBLICATION_PASS

- Status: mitigated.
- Risk: GPTPro cleanup made the evidence chain cleaner, but guarded v2 still needed full Word/PDF page-by-page visual QA.
- Mitigation: QA succeeded and is recorded in `12_final_baodian/DOCX_QA_GUARDED_V2.md`; accepted claim remains guarded, with core/open/reference/boundary labels preserved.
# 2026-05-20T00:06:50+08:00 - GPTPro progress-sync visible text mangled

- 风险：发往 ChatGPT 网页 / GPT-5.5 Pro 的进度同步消息在网页可见输入中出现乱码、字段名丢失或标点被吞。
- 影响：该次网页可见文本不能作为干净正式审稿 prompt；如果 GPTPro 仅依据可见文本回答，其结论不得作为 formal review gate。
- 降险：上传附件 `05_reasoner_packets/gpt55pro_guarded_v2_accepted_progress_20260519.zip` 本身完整；原始 prompt `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_ACCEPTED_PROGRESS_20260519.md` 完整；另建短版干净 prompt `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_ACCEPTED_PROGRESS_CLEAN_SHORT_20260520.md`。
- 当前处理：不点击停止、重试、重新生成或重复发送；等待当前 GPTPro 自然结束后低权重保存，必要时再用短版干净 prompt 重新同步。

## R041_ZERO_BASELINE_STUDENT_PAGE_GAPS_FOUND_AND_PATCHED

- Status: mitigated_by_micro_patch_and_reQA.
- Risk: zero-baseline students could start the core framework but still lose points on mixed contract/tort liability, consumer-fraud two-claim structure, labor value layer, open-container fallback, and boundary fallback.
- Evidence: all three lanes independently named the same gap pattern in `10_framework_validation/zero_baseline_student_pressure_20260520/`.
- Mitigation: patched the student one-page and regenerated baodian Markdown/DOCX; Word exported `12_final_baodian/选必二法律主观题满分宝典_GUARDED_V2_ZERO_BASELINE_PATCH_WORD_EXPORT.pdf`; PyMuPDF rendered 115 pages with no blank-page suspects.
- Residual guardrail: do not call this a new core evidence expansion. The accepted claim remains guarded v2 with open/reference/boundary labels preserved.

## R042_GUARDED_V2_TEACHING_FRONTEND_TOO_AUDIT_LIKE

- Status: active.
- Risk: the current guarded v2 can be accurate yet feel worse than the older strong framework because it exposes evidence labels, backend IDs, validation status, and scoring atoms too prominently, while hiding the student-startable mainline.
- Evidence: GPTPro quality challenge `06_open_observations/gptpro_framework_quality_challenge_20260520.md` says the current version is an audit ledger rather than a student-startable framework, with weak mainline, fragmented entrances, N06 residue, and core answers containing audit traces.
- Mitigation plan: rebuild the front end as `强主干 + 全量容器`; move evidence guardrails to appendix/teacher notes; rewrite student one-page, repair N06 rows, clean 43 core complete answers, and add wrong-answer correction examples.
- Residual guardrail: do not solve this by inflating open/reference/boundary rows into core. The rewrite is a teaching-presentation repair, not evidence promotion.

## R043_STUDENT_BATTLE_DOCX_NOT_FULL_VISUAL_QA_YET

- Status: active_optional.
- Risk: `选必二法律主观题满分宝典_学生战斗版.docx` is structurally valid but has not yet been exported through Microsoft Word and rendered page-by-page like guarded v2.
- Evidence: structural QA via python-docx passed: 340 paragraphs, 5 tables. No full Word/PDF render report exists yet for this derivative.
- Mitigation: use the Markdown as authoritative content draft; if the DOCX becomes the distribution copy, run Word/PDF export and page rendering before final publication.
- Residual guardrail: do not describe the student-battle DOCX as visually accepted until that QA is complete.

## R044_DOWNSTREAM_FRAMEWORK_LINE_REJECTED_BY_USER

- Status: active_mitigated_by_rollback.
- Risk: Continuing to repair guarded v2 / student-battle v1 would waste work and could keep hiding a deeper framework-design failure.
- Evidence: user explicitly said the current artifact remains unusable for full marks and ordered rollback to the Codex + ClaudeCode 65-question stage.
- Mitigation: canonical merged files have been reset to STEP_29; downstream framework/宝典 outputs are marked superseded; next work must restart from evidence-card re-audit.
- Residual guardrail: do not use STEP_30B+ observations, codebooks, candidate frameworks, pressure tests, or baodian prose as current evidence/framework input unless the user explicitly re-authorizes a specific file.

## R045_STEP29_HAS_KNOWN_QUESTION_LAYER_RECHECK_NEED

- Status: active.
- Risk: STEP_29 is the requested Codex + ClaudeCode baseline, but later STEP_30A found possible question/material/ask contamination risks. Returning to STEP_29 does not make those risks disappear.
- Evidence: `PROGRESS.md` STEP_30A recorded 24 rows with missing ask_text and/or answer/rubric text apparently leaking into question/material fields.
- Mitigation: next phase must be evidence-card re-audit before any framework; a VS Code ClaudeCode prompt has been saved at `handoff_prompts/PROMPT_FOR_VSCODE_CLAUDECODE_STEP29_65_REAUDIT_20260520.md`.
- Residual guardrail: do not send STEP_29 directly to GPT/Claude for framework generation until question-card cleanliness is rechecked or repaired.


## RISK - 2026-05-20 04:16:02 - 先前框架学习包风险

- PDF 转写依赖文本层，部分页面可能无法保留视觉布局或图片中文字。
- GPTPro 可能把旧框架结论误当证据，prompt 已明确禁止。
- 学生可读性提升不能牺牲 evidence_level 边界：reference_only 不得单独支撑核心节点。

## RISK - 2026-05-20 04:31:00 - GPTPro v0 may look better before pressure test

- Status: active.
- Risk: GPTPro v0 has stronger classroom language, but a better-looking framework can still fail if it cannot run every one of the 65 evidence rows or if it hides reference/boundary cases.
- Evidence: GPTPro v0 proposes seven action nodes and covers all 65 IDs at least by full or short ID, but it has not yet been run question-by-question against material atoms and rubric atoms.
- Mitigation: treat `gptpro_prior_framework_learned_legal_framework_v0_20260520.md` as candidate-only. Next gate is all-65 local pressure test, with special attention to N02/N03 overlap, N06 AI/boundary contamination, N07 value 必修三化, and reference_only lock.

## RISK - 2026-05-20 04:38:00 - Candidate framework overroutes too many rows

- Status: active.
- Risk: GPTPro v0 deliberately uses broad action nodes, so many rows trigger multiple nodes. This helps students start, but can also overroute into generic templates if not followed by rubric-atom sentence matching.
- Evidence: pressure test node counts exceed row count because rows often trigger several nodes: N03 63, N07 58, N02 47, N05 42, N04 29, N06 26, N01 8.
- Mitigation: next pass must choose a primary node per row and match full-score sentence patterns to rubric atoms. Rows with source-check/reference/boundary/container flags must not enter the core student answer bank.

## RISK - 2026-05-20 12:58:42 - V4 still has external-review and source-clean limits

- Status: active_with_deliverable.
- Risk: V4 is much more student-facing, but it can still overstate closure if the 26 source-clean flagged rows are read as perfectly clean question cards or if local Confucius simulation is treated as real GPTPro/Claude final review.
- Evidence: `04_merge_audit/night_v4_classification_source_clean_audit_20260520.md` flags 26 rows; `10_framework_validation/framework_v4_pass_report_20260520.md` reports 32 PASS_CORE, 20 PASS_CORE_WITH_SOURCE_NOTE, 11 CONTAINER_NOT_CORE, 2 PARTIAL_SOURCE_CLEAN; `05_reasoner_packets/night_v4_student_fullscore_council_20260520.zip` contains external-review prompts but no completed external V4 responses.
- Mitigation: Student pure version hides backend/audit terms from students; teacher audit preserves flags; final response must say V4 is current deliverable candidate with guards, not final four-lane PASS.
- Residual guardrail: before calling it final-final, submit the V4 packet once to GPTPro and once to Claude Opus, then patch only evidence-backed failures.

## RISK - 2026-05-20 13:10:00 - Learning prior framework may accidentally import old conclusions

- Status: active_mitigated_by_boundary.
- Risk: The prior frameworks include old legal framework samples. They are useful for structure but can contaminate current 65-question evidence if their old conclusions are imported directly.
- Evidence: user explicitly asked to learn prior framework, while branch notebook still says old选必二 conclusions are作废.
- Mitigation: `PRIOR_FRAMEWORK_DEEP_DNA_20260520.md` and the new GPT/Claude prompt state that prior frameworks are style/structure only; current legal evidence remains STEP_29 65 questions.
- Residual guardrail: every future framework node and full-score sentence must be reattached to current `merged_*` evidence, not copied from old legal files.
## R-20260521-STEP83：V5.2 核心扩展仍有成稿质量风险

- 风险：学生速用稿已明显变好，但逐题扩展稿仍可能保留抽取骨架痕迹，无法直接作为学生宝典。
- 已发现：Claude Opus 指出约 20 道原 31 核心样章存在后台标签、悬空标点、留白、页眉、元信息或材料/细则错位。
- 已处置：`CC0244` 清洗；4 道严重错位题降级；strict_core 从 31 改为 27。
- 剩余风险：27 核心仍需逐题做“评分细则 -> 考场成文答案”重写，不得直接发布。
- 下一步：等 GPTPro 复核后，做双审交叉验证和二次零基础压测。

## R-20260521-STEP84：27 核心清洗稿仍可能只有答案、缺学生启动动作

- Status: mitigated_by_v5_5_patch.
- 风险：V5.3 清除了后台痕迹，但“这题先判断什么”仍可能泛泛写成动作卡归类，学生遇到题并不知道先判哪一个法律事实。
- 证据：V5.4 本地硬扫描发现 27 题几乎都写成“先判断本题属于某卡”。
- 处置：V5.5 为 27 核心题逐题写入具体最小判断和满分前检查。

## R-20260521-STEP85：CC0244 第（2）问漏训导致全题不能满分

- Status: mitigated_in_v5_5_pending_retest.
- 风险：V5.4 对 CC0244 只训练了法律责任和依据，原题第（2）问“维权准备和策略选择”漏掉 4 分。
- 证据：`10_framework_validation/v5_4_zero_baseline_student_pressure_test_20260521.md` 给出 CC0244 全题 PARTIAL。
- 处置：V5.5 已把 CC0244 拆成两问，补入证据准备、请求设计、维权路径。
- 剩余风险：第（2）问的正式给分口径在当前题源中呈现较弱，需在 V5.5 压测和外审中继续确认表达是否足够保分。

## R-20260521-STEP86：V5.5 仍不是最终四线闭合

- Status: active.
- 风险：V5.5 已明显改善学生可用性，但尚未通过新的零基础压测、GPTPro V5.4 回收比较、Claude V5.4/V5.5 复审，也未生成 Word/PDF QA。
- 处置：只把 V5.5 称为“当前最佳学生稿候选”。最终宝典、DOCX/PDF、Governor PASS 和 Confucius closure 均继续 blocked。
## 2026-05-21 03:43｜R87｜V5.7 外审前残余风险

1. 24 道 `source_check_pending` 题仍可能存在原卷设问、题干或答案细则错位；学生稿已降级为最低保分卡，但教师正式讲解前必须回源。
2. 4 道 `reference_only_locked` 题只可练思路，不可支撑核心框架；若后续成稿标题不清，学生可能误以为它们与 formal 题同权重。
3. 4 道 `boundary_open_container` 题存在必修三/选必三混写风险；V5.7 已加“其他模块另开段落”，但外审仍需压测。
4. GPTPro V5.4 网页反馈只能归档可见截屏，非完整复制稿；不得把它单独当作完整外审 PASS。
5. V5.7 尚未经过真实 GPTPro/Claude 双复审，因此不得生成最终 Word/PDF。
# R88 - GPTPro visible prompt garbling risk

- time: 2026-05-21 03:49 CST
- risk: Computer Use direct typing into ChatGPT produced a partially garbled visible short prompt before GPTPro started reading the attachment.
- current mitigation: Do not interrupt the running response. The GPTPro response already stated it would follow the V5.7 packet-internal prompt and file list. On capture, validate against required V5.7 checks: 27 core, 38 non-core, P0/P1/P2, 12-question blind test, and Word/PDF gate.
- fallback: If the final GPTPro response is visibly based on malformed front text or old V5.4/V5.2 conclusions, mark it invalid and rerun with clipboard paste after natural completion.

# R89 - V5.8 candidate may be mistaken for final output

- time: 2026-05-21 04:00 CST
- severity: medium
- status: active
- risk: A later worker may see the V5.8 file and treat it as final Word/PDF-ready before GPTPro V5.7 is captured.
- mitigation: V5.8 header and control files mark `candidate_pending_gptpro_capture`; final promotion requires GPTPro capture plus cross-validation.

# R91 - GPTPro V5.8 final gate could still inherit old chat context

- time: 2026-05-21 04:17 CST
- status: active
- risk: The clean V5.8 packet was sent inside the same ChatGPT conversation that contains older V5.2/V5.4/V5.7 history, so the model could still refer to old context despite the visible instruction.
- mitigation: The uploaded packet includes `PACKET_README.md` and an internal prompt telling GPTPro to ignore previous context and review only V5.8. The visible prompt was ASCII-only and submitted once.
- acceptance rule: Capture is valid only if the response explicitly uses V5.8, `27 core + 38 non-core`, P0/P1/P2, 12-question test, and Word/PDF gate. Otherwise mark invalid and rerun in a new clean conversation.

# R97 - V5.9 Word/PDF candidate may be mistaken for all-65 closure

- time: 2026-05-21 05:00 CST
- status: active_guarded
- risk: The presence of a polished DOCX/PDF may cause later users or workers to call it the final 65-question full-score handbook.
- current mitigation: The title page, status block, redline bands, QA report, PROGRESS, and governor all state `27 核心满分训练 + 38 保分/边界/回源索引`.
- QA mitigation: PDF text scan confirms the first page contains `不是 65 题全部核心满分闭环`; warning bands remain visible across pages 24-33.
- residual guardrail: Do not promote any source-check, reference-only, low-frequency, boundary, or transfer row into strict core without source-level review and a new decision record.

# R98 - Word export path transformation bug fixed but should be watched

- time: 2026-05-21 05:00 CST
- status: mitigated
- risk: The DOCX export script previously converted inline-code paths into literal `\1`, visible on the last PDF page.
- mitigation: Patched `scripts/export_v5_9_dual_gate_docx.py`, regenerated DOCX/PDF, and re-rendered 33 pages.
- verification: Current PDF scan reports `literal_backslash_one = false`; page 33 visual sample shows the appendix path correctly.

# R99 - CC0244 ask_text differs between canonical question row and V5.9 core row

- time: 2026-05-21 05:08 CST
- status: active_p2
- risk: `CC0244_2026_东城_期末_18` is correctly trained as a two-part question in V5.9 core outputs, but the blind-test packet generated from `merged_subjective_law_questions.csv` pulled only the first ask.
- evidence: The blind-test agent noted that the题面包 seemed to ask only第（1）问, while its answer still included第（2）问 because V5.9 taught it.
- mitigation so far: The V5.9 core CSV and student handbook include both asks and the第（2）问维权准备/策略选择 training.
- next check: Repair canonical source-card or blind-pack generator so future clean题面包 uses the V5.9 corrected ask_text for this question.

# R100 - External gates can pass a document that still feels unusable to students

- time: 2026-05-21 05:27 CST
- status: active_high
- risk: GPTPro/Claude final-gate reviews may overweight evidence safety and underweight whether a real student can learn, remember, start, and transfer under exam pressure.
- trigger: User rejected V5.9 despite guarded PASS history.
- mitigation: New attack packet explicitly tells GPTPro and Claude to assume V5.9 is bad, find why students still cannot full-score, and propose V6 executable reconstruction.
- acceptance rule: V6 cannot be called final until it passes student-facing criteria: one-screen entry, strong main trunk, clear card routing, teachable wrong-answer correction, and question-by-question full-score runs.

# R101 - V6 could repeat the same false acceptance if tested with labels

- time: 2026-05-21 CST
- status: active_high
- risk: If V6 is tested again with `question_id` or core/guard labels visible, the result will overstate student transfer.
- evidence: GPTPro and Claude both identified the V5.9 blind test as label-leaked; the student answer file explicitly used category labels.
- mitigation: Next validation packet must hide ids, categories, evidence levels, and answer/rubric text from the student role. Grading may use ids internally only after answer collection.
- acceptance rule: Do not promote V6 to Word/PDF until a naked-question blind test records how the student chose entry route and where points were gained/lost.

# R102 - Topic-level phrase conflicts can make students lose points by copying a correct phrase into the wrong题

- time: 2026-05-21 CST
- status: active_mitigated_in_v6_working
- risk: Expressions such as `营商环境` and `维护双方合法权益` are rewarded in one题 but rejected in another; a general phrase bank can teach students to write a forbidden phrase.
- mitigation: V6 working draft adds a question-level forbidden-expression table and easy-confusion comparison boxes.
- residual: These tables still need naked blind testing and final proofreading against source/rubric atoms.

# R103 - Correct route but missed hard rubric term

- time: 2026-05-21 06:15 CST
- status: mitigated_in_v6_2_pending_external_review
- risk: Students may choose the right route but still miss a hard scoring phrase.
- evidence: V6 naked blind sample C answered合同/违约/侵权/证据/路径 correctly but did not explicitly foreground product liability no-fault responsibility.
- mitigation: V6.2 adds a front-loaded no-fault responsibility hard sentence and a question-level hard-check for CC0244.

# R104 - Table answers may become conditional prose

- time: 2026-05-21 06:15 CST
- status: mitigated_in_v6_2_pending_external_review
- risk: Table questions may be learned as conditional explanation rather than direct table completion.
- evidence: Naked blind sample E used “如果表格要求……” because the blind packet lacked original table columns.
- mitigation: V6.2 forbids conditional table prose in real exams and requires direct per-cell output by function.

# R105 - Student handbook can still look like an engineered framework rather than a usable lesson

- time: 2026-05-21 CST
- status: mitigated_in_v6_3_pending_external_review
- risk: Even after V6.2, the student-facing file retained terms such as “一二三四五总图”, “主卡/辅卡”, and rough labels like “认产权·抓侵权”; these can make the document feel like an internal engineering artifact, not something a smart but untrained student can immediately use.
- mitigation: V6.3 local hygiene patch removes the pre-set-sounding summary, translates backend tags into exam-room task language, and adds stronger “not memorization” warnings.
- residual: V6.3 still needs GPTPro / Claude Opus review and a follow-up naked blind test before any final claim.

# R106 - Template pollution in generated core cards can undermine trust

- time: 2026-05-21 CST
- status: mitigated_in_v6_3_pending_external_review
- risk: V6.2 table-card text included an irrelevant “先判合同” explanation and placeholder-like rows such as “第二个关键事实/最后落点”; a student or teacher may infer the whole handbook is auto-filled rather than carefully crafted.
- mitigation: V6.3 repairs the table-card explanation and relabels generic rows as “第二层材料/得分落点”.
- residual: Need final proofreading after external P0/P1 integration to find any remaining copied-template residue.

# R107 - Dual-review patches can still fail on one hard rubric word

- time: 2026-05-21 06:55 CST
- status: mitigated_by_v6_5_miniregression
- risk: Even after GPTPro/Claude review and V6.4 patching, a student can follow the correct route but miss a hard scoring expression such as `因果关系/无因果关系`.
- evidence: V6.4 C/E/G/H regression scored 3 PASS + 1 PARTIAL; the PARTIAL was the table responsibility sample.
- mitigation: V6.5 explicitly requires `事实 + 因果/非因果判断` in responsibility table material cells and passed a one-question miniregression.
- residual: This was a targeted regression, not a new 65-question full retest.

# R108 - V6.7 DOCX may be mistaken for final PDF-ready closure

- time: 2026-05-21 06:55 CST
- status: active_guarded
- risk: Because V6.7 is cleaner and exported to DOCX, later workers may call it final even though full-page visual QA and final external student-use review are still missing.
- mitigation: `DOCX_QA_V6_7_STUDENT_20260521.md`, governor, and this risk record all state that V6.7 is a current best candidate, not final封版.
- blocker: `render_docx.py` could not run because `soffice`/LibreOffice is missing; Microsoft Word AppleScript PDF export timed out.
- next check: Install/use a reliable DOCX-to-PDF renderer or manually export from Word, then render all pages to PNG and inspect page set before PDF release.

# R109 - 27 core / 38 non-core boundary remains easy to blur in student-facing prose

- time: 2026-05-21 06:55 CST
- status: active_guarded
- risk: A readable student document may over-teach the 38 non-core rows as if they were stable full-score patterns.
- mitigation: V6.7 title and opening warnings use `27核心满分训练 + 38保分索引`; raw backend labels are removed but the boundary remains student-visible.
- acceptance rule: No source-check, reference-only, low-frequency, transfer, or boundary row may enter the 27-core training set without source-level verification and a new decision record.

# R110 - Web handoff may corrupt or interrupt final external review

- time: 2026-05-21 06:58 CST
- status: active_guarded
- risk: A Chinese prompt can be garbled in GPTPro web UI, or repeated clicks can interrupt Claude/Cowork thinking before completion.
- mitigation: The current V6.9 packet includes `VISIBLE_PROMPT_ASCII_FOR_WEB_UPLOAD_20260521.txt`; status files require one deliberate upload/send and then natural completion capture.
- acceptance rule: Do not accept a model answer if it appears to review old V5/V6.2 context or ignores the packet-internal V6.9 prompt.

# R111 - Student-clean scripts can accidentally remove necessary question scaffolding

- time: 2026-05-21 07:04 CST
- status: mitigated_in_v6_8
- risk: Cleaning engineering labels from the student handbook can also remove or hide necessary question title/startup sections.
- evidence: V6.7 first `表格补全战场` core question lacked its title and sections 1-6, jumping straight to `完整考场版答案`.
- mitigation: V6.8 restores the missing core title, startup steps, material summary,争点,材料翻译表, and满分句零件; structural QA checks for this exact pattern.
- residual: Other sections should still be spot-checked by GPTPro/Claude V6.9 review and future full-page QA.

# R112 - Handbook can claim 27 core questions while containing only 26

- time: 2026-05-21 07:10 CST
- status: mitigated_in_v6_9
- risk: A generated student handbook may preserve the headline `27核心` while accidentally dropping one core case.
- evidence: V6.8 integrity audit found 26 core titles; `RECOVER_2025_海淀_二模_18` was missing.
- mitigation: V6.9 restores the missing case and passes `v6_9_core_section_integrity_audit_20260521.md`.
- residual: External reviewers should still inspect whether all 27 core entries are pedagogically useful, not merely present.

## Risk - STEP_110 External V7 Calls

- time: 2026-05-21 07:33:17
- risk: GPTPro Safari UI may show typed prompt/path with stripped underscores or garbled display.
- mitigation: all ZIP internal paths are ASCII; full prompt is inside the packet; status file records visible UI caveat.
- risk: Claude send button interruption if repeatedly clicked.
- mitigation: sent exactly once; no further clicks while Claude is responding.
- risk: V7 models may still produce a pretty but non-teachable framework.
- mitigation: prompt forces METHOD_LEARNING_NOTES, WHY_V6_9_STILL_NOT_ENOUGH, four batch findings, evidence_ids, and rejection/demotion of unusable nodes.

## Risk STEP_111

- GPTPro 网页端曾整包流错误；当前只用 split upload，禁止点击旧失败消息的 retry。
- CC0223 材料层含教师版参考答案，若不清洗会把价值答案误当题面。
- CC0150 细则层含 Q21 选必一国际政治内容，若不剔除会污染法律框架。
- CC0244 原子边界过粗，若不拆细会把设问、材料、讲评和细则混给学生。

# R113 - V7.1 candidate can still overclaim before source-card repair

- time: 2026-05-21 09:27 CST
- status: active_guarded
- risk: GPTPro/Claude 已经完成 V7 方法学习与分批建议，容易被误读为“最终宝典已闭合”；但 19 个空设问和 3 个高风险题卡仍会影响逐题满分示范可靠性。
- evidence: `04_merge_audit/v7_1_source_repair_queue_20260521.csv` lists 22 repair rows: 6 repair_now, 10 source_confirm_required, 1 split_subquestion_only, 1 downgrade_insurance_box, 1 reference_only_lock, and 3 high-risk clean/split rows.
- mitigation: V7.1 只允许进入 source repair、教师证据说明和 DOCX 草稿，不允许 final PASS；source_confirm_required 行不得进入核心满分闭环。
- acceptance_rule: 只有在修补队列被逐行处理、教师证据说明完成、必要回归通过后，才能考虑封版。

# R114 - v8.1 delivery fix may be mistaken for full final closure

- time: 2026-05-21 21:21 CST
- status: active_guarded
- risk: v8.1 已清理硬禁词、同步金样板并生成宝典，容易被误读为“53 题全部逐题人工精雕且可封版”。
- evidence: `v8_1_student_delivery_fix/08_v8_1_acceptance_report.md` 明确为 `CONDITIONAL_PASS`；49 题正文中非优先题仍需逐题人工核读；4 道设问未可靠补出题进入附录。
- mitigation: v8.1 final response and governor 均不得写 full PASS；后续必须按非优先题逐题人工精修队列推进。
- acceptance_rule: 只有非优先题逐题核读、DOCX 全页视觉 QA 完成、学生模拟再次通过后，才允许考虑提升到 PASS。

# R115 - DOCX generated but visual render QA is blocked by missing soffice

- time: 2026-05-21 21:21 CST
- status: active_guarded
- risk: `.docx` 文件可生成且可打开，但没有页面级 PNG/PDF 渲染就可能漏掉排版问题。
- evidence: `render_docx.py` 调用失败，原因是本机当前找不到 `soffice`/LibreOffice；`10_docx_QA_note.md` 已记录。
- mitigation: 本轮只交付 DOCX 文件，不宣称视觉 QA 通过；后续安装 LibreOffice 或用 Word 导出 PDF 后再做全页视觉检查。
- acceptance_rule: 未完成页面渲染检查前，DOCX 只能算结构生成成功，不能算出版级封版。

# R116 - v9 style pass may be mistaken for full 53-question appendix completion

- time: 2026-05-21 21:53 CST
- status: active_guarded
- risk: `v9_feige_style_rebuild` 已经更像飞哥课堂版，容易被误读为“完整宝典和 53 题附录也已完成”。
- evidence: `v9_feige_style_rebuild/08_v9_style_acceptance.md` 明确验收的是风格重建，不是 53 题完整附录；用户本轮也禁止重写 53 题和生成 DOCX。
- mitigation: 对外汇报只说 v9 完成课堂主框架、触发页、筛查页、句库和 10 道极简演练；不得称为最终完整宝典。
- acceptance_rule: 只有用户确认 v9 风格后，另起步骤按 v9 口吻补 53 题附录，才可考虑完整交付版。

# R117 - v10 exhaustive output still needs classroom-human review before Word/PDF

- time: 2026-05-21 22:53 CST
- status: active_guarded
- risk: v10 已完成“上篇框架穷尽 + 下篇 53 题全量题链”，但下篇由现有闭合语料和机械归类生成，后续若要做正式 Word/PDF，仍需逐题人工课堂口吻审读。
- evidence: `v10_exhaustive_framework_and_all_questions/03_下篇_53题全量题链.md` 已含 53 题；`05_v10_acceptance.md` 验收为 `EXHAUSTIVE_FRAMEWORK_PASS`，但未生成 DOCX/PDF。
- mitigation: 对外只称 v10 完成穷尽框架与全题题链，不宣称已完成出版级排版或全页视觉 QA。
- acceptance_rule: 若进入最终出版稿，必须先对 53 题题链逐题核读，再生成 Word/PDF 并做视觉检查。

# R118 - v10 automatic matching contamination invalidates acceptance

- time: 2026-05-21 23:38 CST
- status: active_blocker
- risk: v10 把大量题塞进合同、纠纷解决、意义价值等万能篮子，并把参考答案、评分细则、设问要素、分析说明和 OCR 串页误当材料触发，导致验收报告不可信。
- evidence: 用户/GPT 点名 CC0002、CC0011、CC0025、CC0137、CC0143、CC0254、CC0131、CC0289 等失败样例。
- mitigation: v11 先生成 53 题回源审判表和强分诊清单；每题只允许 1 个主入口、最多 3 个主材料触发，并必须写禁止命中点。
- acceptance_rule: 只有全部失败样例修复、待确认题不硬写、题链不再材料错配，才允许考虑 `SOURCE_LOCKED_PASS`。

# R119 - v11.1 patch pass can be mistaken for final delivery

- time: 2026-05-22 12:35 CST
- status: active_guarded
- risk: `v11_1_written_chain_patch/06_v11_1_acceptance.md` 写为 `V11_1_WRITTEN_CHAIN_PATCH_PASS`，容易被误读为 v11 已经最终通过或可以直接写最终宝典。
- evidence: v11.1 只修复 CC0200、CC0238、CC0137、CC0229、CC0305 和 01 报告残留；24 题回源回填仍未启动。
- mitigation: 所有控制文件明确写明 v11.1 不是最终宝典、不是 DOCX 交付、不是 `SOURCE_LOCKED_PASS`。
- acceptance_rule: 只有用户明确允许后才能启动 24 题回填；只有回填完成、复扫通过、GPT/人工验收后，才允许讨论最终宝典。

# R120 - v12 conditional pass still leaves 6 source gaps

- time: 2026-05-22 13:16 CST
- status: active_blocker
- risk: `v12_24_question_backfill` 已回填 18 题并生成 47 题正文题链，容易被误读为 53 题已完整闭合。
- evidence: `v12_24_question_backfill/04_无法回填或降级清单.md` 仍列出 CC0251、CC0276、CC0277、CC0317、CC0318、CC0319 六题；这些题未同时锁住真实设问和真实材料核心。
- mitigation: `03_all_53_question_chains_v12.md` 明确写为条件版，正文只保留已完成 source-locked 题链；未锁源题移入 04，不在正文伪装完成。
- acceptance_rule: 六题未补齐或未由用户确认降级/移出前，不得写最终宝典、不得生成 DOCX、不得写 `V12_24_BACKFILL_PASS` 或 `TASK_COMPLETE`。


## 2026-05-22 15:52:45 Risk: next backfill required
- 6 道未纳入题已有源寻线索，但尚未经过下一版正式回填和 GPT 审核，不能纳入 v12.1 正文闭合。
- 海淀三题的 question_id 阶段标签与源文件标题存在不一致风险，下一版需校正。
