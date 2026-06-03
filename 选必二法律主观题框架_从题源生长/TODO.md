# TODO

## 2026-05-21T23:20:23+08:00 - TODO_V11_SOURCE_LOCKED_REBUILD

- [x] 停止 v10，不再使用 v10 acceptance 作为验收结论。
- [x] 生成 `v11_source_locked_rebuild/01_53题回源审判表.csv`。
- [x] 生成 `v11_source_locked_rebuild/01_53题回源审判报告.md`。
- [ ] P0：回源修复或明确处理 29 个 `待用户确认` 行，尤其是 CC0011、CC0131、CC0137、CC0254、CC0289。
- [ ] P0：基于 01 表写 `02_强分诊框架清单.md/.csv`，不得恢复 v10 万能命中。
- [ ] P0：只有完成强分诊后，才能写 `03_下篇_53题全量题链_v11.md/.csv`。
- [ ] P0：`OPEN_OR_REFERENCE` 题只能参考运行，不支撑核心框架。
- [ ] P0：最终验收不得出现 `EXHAUSTIVE_FRAMEWORK_PASS`；v11 结论只能在真实回源审判后使用 SOURCE_LOCKED_PASS / CONDITIONAL_PASS / FAIL。

## 2026-05-20T00:22:15+08:00 - Pending Strict VS Code ClaudeCode Rerun

- [ ] If the user requires strict four-lane formal compliance before treating guarded v2 as final-final, rerun the suite-exhaustion audit and patch verification through VS Code ClaudeCode, not `claude -p` CLI.
- [ ] Compare the VS Code ClaudeCode output against the current 65-question guarded v2 corpus and record any deltas before changing the framework/宝典.
- [ ] Until then, do not describe the existing ClaudeCode audit as "VS Code completed"; describe it as `ClaudeCode CLI/provisional source-check lane + Claude Cowork + GPTPro + Codex source verification`.

- 手工回源复核 v1 压测 FAIL 的 20 道边界题，确认是否从最终选必二法律正文剔除。
- 对 PARTIAL 的 13 道题补正式细则/评标后，再决定是否进入下一轮 codebook。
- 如需 Word 视觉验收，请在装有 LibreOffice/Word/WPS 的环境打开 `12_final_baodian/选必二法律主观题满分宝典.docx` 抽查页面；本机 `soffice` 不可用，未完成 PNG 渲染。
- 后续若用户要求继续精修，优先处理 `framework_v1_failure_cases.md` 中“漏节点”的低频法律题，不扩张边界误收题。
- DONE: GPT-5.5 Pro 边界恢复复核已保存为 `10_framework_validation/gpt55pro_boundary_recovery_review.md`。
- DONE: 已生成 after-GPT 控制口径 `10_framework_validation/framework_v2_boundary_recovery_delta_after_gpt.csv`，并把原 v2/宝典降级为 provisional。
- DONE: `CC0229_2026_东城_一模_18` rubric atoms 已用 `F0153:page 7-8` 与 `F0146:slide 3-4` 修复，且最终宝典对应段落已重生成。
- DONE: 已为 `CC0305_2026_海淀_一模_18_3`、`CC0373_2026_顺义_一模_18`、`CC0380_2026_顺义_二模_18_2` 建立 split question/material/ask/rubric patch records。
- 下一步 P0：拆分 `CC0094_2025_东城_期末_19_3`，只保留法律与生活相邻关系 2 分层，政治民主程序层不进法律框架。
- 下一步 P0：把 split patch records 集成到 canonical merged files 或 final regeneration 输入包。
- DONE: 已从最终宝典 Markdown 主文删除/改写 `CC0250`、`CC0094`、`CC0373` 旧父题段落，并基于 split patches 生成 `选必二法律主观题满分宝典_BOUNDARY_PATCHED.docx`。
- DONE: 已定点同步 sidecar CSV：`question_by_question_framework_runs.csv`、`material_trigger_bank.csv`，并修订 `common_failure_paths.md`。
- DONE：已生成 canonical patched corpus，把 split patch records 合并进 `04_merge_audit/boundary_patched_20260519/`，并打包为 `04_merge_audit/boundary_patched_canonical_corpus_20260519.zip`。
- DONE：已统一重导 `full_score_sentence_bank.csv`，并生成 `full_score_sentence_bank_boundary_patched.csv`；三张 53 行 boundary sidecar 的状态口径已对齐。
- 下一步 P1：`CC0259_2026_丰台_期中_19_LAW` 继续补正式法律细则；未补到前不得进入框架归纳或满分闭环。
- DONE：已完成 Microsoft Word 打开/保存/PDF 导出，并渲染 198 页 PNG；无疑似空白页，详见 `12_final_baodian/DOCX_QA_WORD_PDF_RENDER.md`。
- 下一步 P0：更新最终交付报告，把状态改为“53 行 patched corpus 有界 release candidate”，并明确 CC0094/CC0259/CC0118 仍在 pending ledger 外。
- DONE：已将当前 53 行 boundary-patched 进度同步到 ChatGPT 网页项目 `必修四喂细则` 的 `选必二框架设计` 对话；同步稿留存在 `handoff_prompts/REPORT_TO_GPT_WEB_BIXIU4_FEED_RUBRIC_XUANBIER_PROGRESS.md`。
- DONE：GPT 网页对话已自然完成回复，回执已保存为 `tool_outputs/gpt_web_bixiu4_xuanbier_progress_sync_response_20260519.md`；全程未点击停止、重试或重复发送。
- DONE：已完成“70 到 53 净少 17”认真复核，产物为 `04_merge_audit/net17_serious_recheck_20260519.csv` 与 `04_merge_audit/net17_serious_recheck_20260519.md`。
- DONE：已补回 `RECOVER_2024_顺义_二模_17`、`RECOVER_2025_海淀_二模_18`、`RECOVER_2026_通州_一模_20` 的 question/material/ask/rubric atoms，并生成 56 行 `boundary_recovered_20260519` corpus。
- DONE：已完成 63 套 suite-level exhaustion matrix，并补入 10 道核心 formal 法律主观题，生成 66 行 `suite_exhaustive_20260519` corpus。
- DONE：已把旧 GPT/Claude 观察、交叉验证、代码本、候选框架、压测和宝典标记为 superseded；下一轮必须使用 `05_reasoner_packets/suite_exhaustive_20260519/`。
- 下一步 P0：用 66 行 `suite_exhaustive_20260519` 重新跑 GPT-5.5 Pro 与 Claude Opus 开放观察；未完成前不得生成或定稿框架。
- 下一步 P0：基于 66 行 corpus 重跑交叉验证、代码本、候选框架、全题压测、sidecars、句库和宝典新增段落；未重跑前，旧最终宝典不能宣称闭合。
- 下一步 P1：把 `2026丰台期末 Q18` 放入 `uncertain_mixed_law_boundary` 复核表；它不在原 70->53 净差内，但评标显示“政治与法治 + 法律与生活”混合，不能静默丢弃，也不能直接进核心闭合。

## 2026-05-19T16:11:46+08:00 Next Tasks After ClaudeCode-Corrected PASS

- [ ] Wait for Claude Cowork question-refinement task to complete; capture output under `04_merge_audit/claude_cowork_question_refinement_20260519/`.
- [ ] Apply any Cowork `must_fix_before_reasoner=yes` patches before rerunning GPT-5.5 Pro / Claude Opus open observation.
- [ ] Repair or explicitly clear the 24 locally flagged question-layer rows in `codex_question_layer_contamination_or_missing_ask.csv`.
- [ ] Rebuild the corrected reasoner packet after question/material/ask fields are clean.
- [ ] Start fresh GPT-5.5 Pro open observation using `handoff_prompts/PROMPT_FOR_GPT55PRO_OPEN_OBSERVATION_CLAUDECODE_CORRECTED_20260519.md` and corrected packet zip.
- [ ] Start fresh Claude Opus 4.7 Adaptive open observation using `handoff_prompts/PROMPT_FOR_CLAUDE_OPUS_OPEN_OBSERVATION_CLAUDECODE_CORRECTED_20260519.md` and corrected packet zip.
- [ ] Save both outputs under `06_open_observations/` with `_claudecode_corrected_20260519` filenames.
- [ ] Rebuild cross-validation, codebook, candidate framework, pressure test, and handbook only after the two corrected model outputs exist.
- [ ] Do not use old 53/56/66/v3 observation or framework files except as superseded audit history.

## 2026-05-19T17:01:41+08:00 Next Tasks After Cowork-Refined PASS

- [x] Capture Claude Cowork output under `04_merge_audit/claude_cowork_question_refinement_20260519/`.
- [x] Apply Cowork must-fix patches.
- [x] Repair the 24 local question-layer flagged rows, including five extra material contamination rows found after Cowork PASS.
- [x] Rebuild the reasoner packet as `05_reasoner_packets/reasoner_packet_suite_exhaustive_cowork_refined_20260519.zip`.
- [x] Save new GPT and Claude prompts: `PROMPT_FOR_GPT55PRO_OPEN_OBSERVATION_COWORK_REFINED_20260519.md` and `PROMPT_FOR_CLAUDE_OPUS_OPEN_OBSERVATION_COWORK_REFINED_20260519.md`.
- [x] Start fresh GPT-5.5 Pro open observation using the cowork-refined prompt and zip only.
- [x] Start fresh Claude Opus 4.7 Adaptive open observation using the cowork-refined prompt and zip only.
- [x] Save both outputs under `06_open_observations/` with `_cowork_refined_20260519` filenames.
- [x] Rebuild cross-validation and provisional codebook from the two cowork-refined model outputs.
- [x] Generate and send codebook-bound candidate-framework prompts to real GPT-5.5 Pro and Claude Opus 4.7 Adaptive; if UI call is unavailable, save handoff prompts and mark candidate-framework gate `real_call_pending`.
- [x] Wait without clicking stop/retry/send while GPT-5.5 Pro and Claude Opus candidate-framework calls run.
- [x] Capture GPT output to `09_candidate_frameworks/gpt55pro_candidate_frameworks_cowork_refined_20260519.md` and canonical `gpt55pro_candidate_frameworks.md`.
- [x] Capture Claude output to `09_candidate_frameworks/claude_opus_candidate_frameworks_cowork_refined_20260519.md` and canonical `claude_opus_candidate_frameworks.md`.
- [ ] Rebuild candidate-framework comparison, framework_v1, pressure test, sidecars, and handbook only after the two cowork-refined candidate-framework model outputs exist.
- [x] Next immediate gate: synthesize `09_candidate_frameworks/candidate_framework_comparison.md`, `framework_synthesis_plan.md`, `framework_v1.md`, and `framework_v1_evidence_map.csv` from the captured GPT/Claude candidate frameworks.
- [x] Run entry-clean all-65 pressure test using only question/ask/material layers for entry matching.
- [x] Build source-check packet for the 45 formal PARTIAL rows and 4 reference_only non-core rows.
- [x] Save identical GPT/Claude codebook-expansion prompts.
- [x] User-requested extra check: send a dedicated all-65 completion packet once to Claude Desktop Cowork before final expansion/adjudication.
- [x] Wait for Claude Cowork `Review 65 law questions for codebook expansion` to complete naturally; do not click stop/retry/send.
- [x] Capture Cowork output under `04_merge_audit/claude_cowork_all_question_completion_20260519/`.
- [x] Next P0: source-check five Cowork-blocked rows before promoting uncertain candidates: CC0011, CC0019, CC0061, CC0254, RECOVER_2026_房山_一模_17_1.
- [x] Next P0: build a corrected codebook-expansion packet that includes Cowork outputs plus Codex source-check files (`codex_source_check_five_blocked_rows.*` and `codex_source_check_corrected_rubric_atom_plan.csv`).
- [x] Next P0 after Cowork capture: send the corrected expansion packet once each to GPT-5.5 Pro and Claude Opus, then wait without stop/retry/send clicks.
- [x] Next P0: capture GPT expansion output after natural completion to `06_open_observations/gpt55pro_codebook_expansion_after_cowork_sourcecheck_20260519.md` or equivalent, preserving raw text before parsing.
- [x] Next P0: capture Claude Opus/Cowork expansion output after natural completion to `06_open_observations/claude_opus_codebook_expansion_after_cowork_sourcecheck_20260519.md` or equivalent, preserving raw text before parsing.
- [x] Next P0: cross-compare the two expansion decisions before modifying `provisional_codebook_v0`; do not promote Cowork-only or one-model-only nodes without local evidence裁决.
- [x] Next P0: keep final framework v2 and final baodian blocked until PARTIAL rows either gain evidence-backed nodes or are explicitly quarantined as open-container examples.
- [x] Next P0: apply five required canonical atom patches before expansion codebook draft; report saved under `04_merge_audit/codebook_expansion_atom_patch_20260519/`.
- [x] Next P0: build expansion draft codebook and coverage snapshot; current direct core support is 42/65, not a final full-score closure.
- [x] Next P0: split `CC0364_2026_通州_期末_19_1` giant rubric atom before counting it as strong CODE_COWORK_004/006 support.
- [x] Next P0: run sentence-level all-65 pressure test using `provisional_codebook_v1_1_after_cc0364_split_20260519.csv`; do not generate framework_v2 or final baodian until this pressure test exists.
- [ ] Next P1: adjudicate three no-expansion-support-yet rows: `CC0143_2025_朝阳_一模_19`, `RECOVER_2026_西城_二模_18_2`, `RECOVER_2026_西城_二模_18_3`.

## 2026-05-19T19:54:30+08:00 Next Tasks After v1.1 Sentence Pressure Test

- [x] P0: 专项回源/模型复核 4 个 FAIL：`CC0143_2025_朝阳_一模_19`, `CC0276_2026_房山_二模_17`, `RECOVER_2026_西城_二模_18_2`, `RECOVER_2026_西城_二模_18_3`。本地裁定与候选补丁已写入 `10_framework_validation/fail4_source_adjudication_20260519/`；Claude Cowork 专项审计仍在运行/工具超时自救中，未自然完成前不升核心。
- [x] P0: 等待 Claude Cowork FAIL4 专项审计自然完成；不得点击 Stop/Retry/Send/Queue。Cowork 已改用 Read/Glob 自救并自然完成，输出已捕获。
- [x] P0: Cowork 与本地裁定一致，已生成 `fail4_external_cross_check_20260519.md/.csv`，并将 `CC0143` 经原子补丁后写入 `CODE_COWORK_004`，不是直接裸升核心。
- [x] P0: 对 14 个 open-container formal rows 判定：保持开放容器；不得用单例/低频 open row 创造 unsupported core node。
- [x] P0: 对 4 个 reference_only rows 只保留弱示范；除非补到 formal 细则，不得进入核心框架。
- [x] P0: 基于 `provisional_codebook_v1_2_after_fail4_cowork_20260519.csv` 重新综合 guarded framework，并用 65 题重新压测。
- [ ] P1: 生成最终 framework_v2/宝典前，必须确认 open-container/reference/boundary rows 在逐题示范中被正确标注，不能被写成“满分闭环核心样本”。
- [x] P0: 将 `framework_v1_2_guarded.md` 修订为 `11_final_framework/framework_v2.md` 的教师版/学生版，但必须保留 44 core + 19 partial/open/reference + 2 boundary 的证据口径。
- [x] P0: 基于 `framework_v1_2_question_by_question_test_20260519.csv` 生成新的逐题运行 sidecars；open/reference/boundary 行必须带标签，不能生成伪满分闭环。
- [ ] P1: 对 guarded v2 DOCX 做 Word 打开/保存/PDF 渲染 QA；当前 DOCX 已生成但未做视觉验收。

## TODO_GPTPRO_GUARDED_V2_REVIEW

- [x] Submit `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_PROGRESS_20260519.md` plus `05_reasoner_packets/gpt55pro_guarded_v2_review_20260519.zip` to real GPT-5.5 Pro.
- [x] Locally patch the post-submit `CC0380` inconsistency: move it from core `CODE_COWORK_007` support to `FWV1_2_OPEN`.
- [x] Capture GPT-5.5 Pro output under `06_open_observations/` and `tool_outputs/`.
- [x] Compare the completed GPTPro output with `10_framework_validation/gptpro_guarded_v2_local_precheck_20260519.md`.
- [x] Decide no interrupting delta follow-up is needed because GPTPro's required guarded cleanup is compatible with the CC0380 local patch.
- [x] Apply only evidence-supported row/file patches after GPT-5.5 Pro review.
- [x] Retry full Word/PDF visual QA for guarded v2 before final delivery PASS.

## TODO_AFTER_GPTPRO_CLEANUP_20260519

- [x] Mark non-scoring student-problem/teaching/other-question atoms as risk material.
- [x] Preserve 7 patch scoring atoms for CC0245 and CC0251.
- [x] Regenerate `framework_v1_2_evidence_map.csv` with `node_class`.
- [x] Split broad procedure node into 007A/B/C/D framework subnodes.
- [x] Regenerate pressure table, sidecars, sentence bank, Markdown and DOCX shell.
- [x] Verify answer-generation columns have zero hits for `当代国际政治`, `学生问题`, `建议`, `复练试题`, `反复训练`, `继续短周期`, `教学启示`.
- [x] Complete full Word/PDF visual QA and then write guarded final acceptance.

## TODO_AFTER_GUARDED_V2_ACCEPTANCE_20260519

- [ ] Optional: send one concise guarded-v2 progress sync to GPTPro using the updated acceptance/QA files; do not click stop/retry/regenerate/send repeatedly.
- [ ] If GPTPro returns new changes, apply only evidence-supported patches and preserve guarded labels.
# 2026-05-20T00:06:50+08:00 - Pending clean GPTPro progress sync

- [ ] Wait for the current GPTPro progress-sync attempt to finish naturally; do not click stop/retry/regenerate/send while it is running.
- [ ] Save the response as low-weight if it appears to rely on the mangled visible prompt.
- [ ] If clean external confirmation is still needed, send `handoff_prompts/REPORT_TO_GPT55PRO_GUARDED_V2_ACCEPTED_PROGRESS_CLEAN_SHORT_20260520.md` with the same zip and record it as the clean progress-sync call.

## TODO_ZERO_BASELINE_STUDENT_PRESSURE_20260520

- [x] Send learning-only packet to Claude Cowork / Opus 4.7 and capture completed student-simulation answer.
- [x] Send learning-only packet to GPTPro web (`进阶专业`) and capture completed student-simulation answer.
- [x] Run internal agent student simulation with no rubric/baodian access.
- [x] Grade all three outputs against the hidden Codex-only scoring key.
- [x] Patch the student one-page with the consensus missing prompts.
- [x] Regenerate baodian Markdown/DOCX after the micro-patch.
- [x] Export the regenerated DOCX through Microsoft Word and render the zero-baseline-patched PDF page-by-page.
- [ ] Optional: if distributing this exact patched artifact, update any external handoff zip to point to the zero-baseline-patched PDF rather than the pre-patch guarded-v2 PDF.

## TODO_GPTPRO_FRAMEWORK_QUALITY_CHALLENGE_20260520

- [x] Send `framework_quality_challenge_gptpro_20260520.zip` plus the quality-challenge prompt to GPTPro web (`进阶专业`) exactly once.
- [x] Capture completed GPTPro critique to `06_open_observations/gptpro_framework_quality_challenge_20260520.md`.
- [x] Convert GPTPro's critique into a student-facing guarded rewrite: `强主干 + 全量容器`.
- [x] Generate a separate student-startable handbook instead of only patching the audit-style guarded v2: `12_final_baodian/选必二法律主观题满分宝典_学生战斗版.md`.
- [x] Repair visible N06A/N06C/N06D contamination in the new student-facing examples, especially AI risk,调解,公益诉讼, and mixed-liability demonstrations.
- [x] Remove backend/audit traces from the new student-facing artifact: no `细则原子覆盖草句`, `给分逻辑`, `1分/2分`, `可酌情给分`, backend IDs, or OCR notes in the student prose.
- [x] Add wrong-answer paths and correction examples to the student-battle version.
- [x] Export a DOCX version: `12_final_baodian/选必二法律主观题满分宝典_学生战斗版.docx`.
- [ ] Optional: run full Microsoft Word/PDF visual QA on the new student-battle DOCX before treating it as the distribution copy.
- [ ] Optional: send the student-battle version to GPTPro/Claude for pure teachability review, with evidence promotion explicitly forbidden.

## TODO_ROLLBACK_TO_STEP29_CLAUDECODE_65_20260520

- [x] Stop treating guarded v2 / student-battle v1 as current deliverables.
- [x] Copy STEP_29 Codex+ClaudeCode corrected 65-question corpus into `04_merge_audit/rollback_to_step29_claudecode_corrected_65_20260520/`.
- [x] Reset canonical `04_merge_audit/merged_*` files to STEP_29 baseline.
- [x] Preserve backup of pre-rollback canonical files under `tool_outputs/pre_20260520_rollback_step29_active_canonical_backup/`.
- [x] Create restart packet copy under `05_reasoner_packets/rollback_to_step29_claudecode_corrected_65_20260520/`.
- [x] Mark downstream observation/framework/baodian directories as superseded by rollback.
- [x] Save VS Code ClaudeCode re-audit prompt for the 65-question baseline.
- [ ] Run VS Code ClaudeCode re-audit of STEP_29 65 rows before any framework rebuild.
- [ ] Repair or explicitly clear question/material/ask contamination risks before asking GPTPro/Claude Opus for new framework ideas.
- [ ] Rebuild future framework only after each of the 65 question cards has a student-startable proposition path and a clean scoring chain.


## TODO Update - 2026-05-20 04:16:02

- [x] 桌面先前框架转写为 GPTPro 可读包。
- [x] 生成结构 DNA 摘要。
- [x] 生成当前 65 题法律证据 compact CSV。
- [x] 提交 GPTPro prior-framework-learning 包。
- [ ] 保存 GPTPro 输出。
- [ ] 用 GPTPro v0 回到 65 题逐题压测。

## TODO Update - 2026-05-20 04:18:12 CST

- [x] 上传 `prior_framework_learning_gptpro_20260520.zip` 给 GPTPro。
- [x] 发送 GPTPro prior-framework-learning 任务说明。
- [x] 等待并保存 GPTPro 输出。
- [ ] 对 GPTPro v0 做 65 题逐题压测。
- [ ] 依据压测再决定是否进入新宝典重写。

## TODO Update - 2026-05-20 04:31:00 CST

- [x] 备份误复制的上一条质量审查。
- [x] 保存正确 GPTPro v0：`09_candidate_frameworks/gptpro_prior_framework_learned_legal_framework_v0_20260520.md`。
- [x] 写入本地证据边界审查：`09_candidate_frameworks/gptpro_prior_framework_v0_local_evidence_review_20260520.md`。
- [x] 逐题压测 GPTPro v0 的七个动作节点是否能覆盖 65 题。
- [ ] 若要进入严格四线候选框架 gate，向 Claude Opus 4.7 Adaptive 发送同一 prior-framework-learning 包或 GPTPro v0 交叉审查包。

## TODO Update - 2026-05-20 04:38:00 CST

- [x] 生成 GPTPro v0 65 题压测表。
- [ ] P0：回源清洗 18 个 `PARTIAL_SOURCE_CHECK` 行的 ask_text / question-layer。
- [ ] P0：对 35 个 `PASS_CANDIDATE` 行做 rubric_atom 句子级满分句对齐。
- [ ] P0：把 4 个 reference_only、3 个 boundary/open、5 个 low-frequency container 行分别放入参考区/边界区/开放容器，不写成核心满分模板。
- [ ] P1：清洗后再决定是否把 GPTPro v0 发给 Claude Opus 做交叉审查。

## TODO Update - 2026-05-20 12:58:42 CST

- [x] 从 STEP_29 65 题底座生成 V4 学生前台框架、学生纯净版宝典、训练版宝典、教师稿和侧边 CSV。
- [x] 用本地 Confucius/零基础聪明学生模拟抽题压力测试 V4。
- [x] 根据模拟反馈补入程序救济、起诉状、AI 主体资格、举证责任、价值绑定和 reference/boundary 隔离。
- [x] 导出学生纯净版 DOCX，并通过 Microsoft Word 导出 PDF。
- [x] 渲染 PDF 抽样页并完成技术 QA 报告。
- [x] 准备 GPTPro/Claude Opus V4 学生压测包：`05_reasoner_packets/night_v4_student_fullscore_council_20260520.zip`。
- [ ] 把 V4 压测包发给 GPTPro，捕获完整答复。
- [ ] 把 V4 压测包发给 Claude Opus，捕获完整答复。
- [ ] 根据两边 V4 复审结果修订 V4，必要时生成 V5。
- [ ] 对 26 个 source-clean flagged 行继续回源清洗，尤其是 ask_text 串入答案/其他模块的小问。

## TODO Update - 2026-05-20 13:10:00 CST

- [x] 停止把 V4 当作可小修最终稿。
- [x] 定位并读取桌面 `先前框架`。
- [x] 渲染先前框架关键样张，保存在 `05_reasoner_packets/prior_framework_deep_learning_20260520/rendered_samples/`。
- [x] 生成先前框架深度学习报告。
- [x] 生成法律框架重写规格。
- [x] 生成给 GPTPro/Claude 的“先学结构，再写法律”的新 prompt。
- [x] 打包 `prior_framework_deep_learning_20260520` + 当前 65 题证据，形成新一轮 model packet：`05_reasoner_packets/prior_framework_deep_learning_20260520.zip`。
- [x] 发送给 GPTPro：当前失败 V4 + 先前框架学习结果 + 65题证据基线合审，让 GPTPro 先出重建对策。
- [ ] 发送给 Claude Opus：同题同问，独立提出法律框架重写提案。
- [ ] 捕获 GPTPro 当前对策输出，保存到 `09_candidate_frameworks/`。
- [ ] Codex 本地把两边提案回源裁决，生成真正的新框架 v5。


## STEP_73_V5_ACTION_CARD_REBUILD_STARTED_AND_FIRST10_BUILT (2026-05-21 01:52:32)

- GPTPro 当前 V4 + 先前框架学习结果合审回答已落盘：`09_candidate_frameworks/gptpro_current_framework_prior_learning_countermeasures_20260520.md`。
- 已按 GPTPro 对策生成 V5 动作卡候选框架、证据映射、分批计划、学生一页纸和十题样章。
- 当前仍不声明最终 PASS：Claude Opus 真实复核、十题零基础学生压测、35 道核心题扩展仍待完成。


## STEP_74_CLAUDE_OPUS_V5_COUNTER_REVIEW_RUNNING (2026-05-21 01:56 CST)

- 已通过 Claude Desktop / Cowork / Opus 4.7 发送 V5 动作卡复核任务。
- 不触碰 Stop response，不重复发送。
- 目标输出：`06_open_observations/claude_opus_v5_action_card_counter_review_20260521.md`。
- 后续门槛：必须读取 Claude 输出后再决定是否生成 V5.1。

## TODO Update - 2026-05-21 04:08 CST

- [x] 对 V5.8 候选稿做本地机械预检，确认 27 核心入口、38 非核心标题与红线计数。
- [ ] 继续只读轮询 GPTPro V5.7；自然完成后保存到 `06_open_observations/gptpro_v5_7_review_20260521.md`。
- [ ] 验证 GPTPro 输出是否真正遵守 V5.7 包内 prompt：27 核心、38 非核心、P0/P1/P2、12 题抽测、Word/PDF gate。
- [ ] 生成 `07_cross_validation/v5_7_gptpro_claude_review_comparison_20260521.md`。
- [ ] 只有在双审无未修 P0/P1 后，才允许把 V5.8 候选推进为 Word/PDF 候选。


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

## STEP_79 后续 TODO

- [ ] 制作 V5.1 干净题面压测包，不放答案、不放细则。
- [ ] 零基础学生模拟学习 `framework_v5_1_student_one_page_20260521.md` 后作答。
- [ ] Codex 按清洗后细则给分，记录丢分原因。
- [ ] 若无法接近满分，继续补最小法律规则句库。
- [ ] 压测通过后再扩展 35 道核心题样章。

## STEP_80 后续 TODO

- [ ] 生成 V5.2 35 道核心题样章，排除 source_check_pending/reference_only。
- [ ] 为每题写“入口、材料分层、最小判断、必踩硬词、考场答案、易错刹车”。
- [ ] 生成 V5.2 满分句库和材料触发库。
- [ ] 打包给 GPTPro 与 Claude Opus 复核 V5.2 核心扩展版。


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
## STEP_83 TODO (2026-05-21 02:38:28 CST)

- [x] 捕获并保存 GPTPro V5.2 复核结果到 `06_open_observations/gptpro_v5_2_review_20260521.md`。
- [x] 生成 `07_cross_validation/v5_2_gptpro_claude_review_comparison_20260521.md`。
- [x] 对 27 strict_core 做答案成文质量清洗：删除后台标签、留白、页眉、评分说明、伪句式库绑定。
- [ ] 对 24 source_check_pending 逐题回源，决定恢复、低频容器、边界容器或剔除。
- [x] 重新抽样零基础学生压测 V5.4，发现 CC0244 第（2）问和非核心保分不足。
- [x] 生成 V5.5：具体最小判断、CC0244 第（2）问、非核心保分容器。
- [ ] 等待 V5.5 零基础学生二次压测报告 `10_framework_validation/v5_5_zero_baseline_student_pressure_test_20260521.md`。
- [ ] 回收 GPTPro V5.4 复审，保存到 `06_open_observations/gptpro_v5_4_review_20260521.md`。
- [ ] 必要时把 V5.5 包重新提交给 GPTPro/Claude，避免只审旧 V5.4。
- [ ] 外审和压测通过前，不生成最终宝典 DOCX/PDF。
## 2026-05-21 03:43｜Next

- [x] 将 `05_reasoner_packets/v5_7_gptpro_claude_review_packet_20260521.zip` 发送给 GPTPro。
- [x] 将同一包发送给 Claude Opus / Claude cowork。
- [x] 判定 GPTPro V5.7 页面状态不可靠：页面实际为旧 V5.2 回复，底部有乱码残留，不得伪装为有效复核。
- [x] 生成并提交 V5.8 干净 GPTPro 终审包：`05_reasoner_packets/v5_8_gptpro_final_gate_packet_20260521.zip`。
- [ ] 捕获 GPTPro V5.8 自然完成输出到 `06_open_observations/gptpro_v5_8_final_gate_review_20260521.md`；若仍受旧上下文污染，记录并转新会话/新包，不得伪装为有效复核。
- [x] 将 V5.8 同步提交给 Claude Opus 4.7 终审。
- [x] 捕获 Claude Opus V5.8 自然完成输出到 `06_open_observations/claude_opus_v5_8_final_gate_review_20260521.md`。
- [ ] 等 GPTPro V5.8 完成后，生成 `07_cross_validation/v5_8_gptpro_claude_final_gate_comparison_20260521.md`。
- [ ] 若 GPTPro 也无 P0/P1，执行 Claude 指出的 4 个 P2 收尾：低频红线、27 核心细则对账、CC0150 底座清理、CSV 主辅卡字段同步。
- [x] 先生成 27 核心 clean rubric atom 机械追踪留痕：`10_framework_validation/v5_8_27_core_rubric_alignment_audit_20260521.md`。
- [ ] 对 `PASS_WITH_MANUAL_CHECK` 的 17 个核心题做人工语义确认或让 GPTPro/Claude 终审意见合流后确认。
- [x] 捕获 Claude Opus V5.7 自然完成输出。
- [x] 按 Claude V5.7 的 P1/P2 生成不覆盖正式稿的 V5.8 候选补丁。
- [ ] 收回双审后生成 `07_cross_validation/v5_7_gptpro_claude_review_comparison_20260521.md`。
- [ ] 若外审无 P0，生成 V5.8 Word/PDF 候选；若有 P0，先补学生稿。
- [ ] source-check 24 题后续交给 ClaudeCode VS Code 或回源脚本逐题核设问与细则，不得自动升核心。

## 2026-05-21 05:00｜V5.9 Candidate Next

- [x] 捕获 GPTPro V5.8 自然完成输出到 `06_open_observations/gptpro_v5_8_final_gate_review_20260521.md`。
- [x] 生成 `07_cross_validation/v5_8_gptpro_claude_final_gate_comparison_20260521.md`。
- [x] 执行双审门禁修补并生成 V5.9 Markdown/CSV/清洗副本。
- [x] 生成 V5.9 DOCX。
- [x] 通过 Microsoft Word 导出 V5.9 PDF。
- [x] 渲染 PDF 33 页 PNG 并抽查 page 1、page 24、page 33。
- [x] 修复 DOCX 导出脚本的 `\1` 残留问题并重新生成 DOCX/PDF。
- [x] 写入 `12_final_baodian/DOCX_PDF_QA_V5_9_20260521.md`。
- [ ] 如要继续冲最终发布：做学生抽样盲测，至少覆盖核心题、source-check 题、reference-only 题、boundary 题、low-frequency 题。
- [ ] 如要提升 38 非核心中的任一题：必须先回源核设问、题干、材料、正式细则，再写入新的 decision record。

## 2026-05-21 05:08｜V5.9 Blind Test Follow-up

- [x] 完成 V5.9 8 题抽样盲测，覆盖 strict_core / low_frequency / source_check / reference_only / boundary。
- [x] 写入学生作答：`10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/agent_student_answers_v5_9_20260521.md`。
- [x] 写入 Codex 阅卷：`10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/codex_grading_report_v5_9_20260521.md`。
- [x] 生成 V5.9 非核心护栏 CSV：`12_final_baodian/non_core_guardrails_v5_9_20260521.csv`。
- [x] 生成 `CC0244_2026_东城_期末_18` 的 V5.9 derived ask_text patch，同步第（2）问但不覆盖 STEP_29 canonical。
- [ ] 后续 source-card review 后，再决定是否把 `CC0244` ask_text patch 晋升为 canonical 覆盖。
- [ ] 继续排 24 个 source-check 题的回源复核队列；不得因为 V5.9 盲测通过就把它们升核心。

## 2026-05-21 05:27｜V5.9 Attack Review and V6 Rebuild

- [x] 构造 `v5_9_attack_review_council_20260521` 攻击审查包。
- [x] 发送给 GPTPro，要求攻击 V5.9 而不是验收。
- [x] 发送给 Claude Opus 4.7 Cowork，要求写入 `06_open_observations/claude_opus_v5_9_attack_review_20260521.md`。
- [x] 启动本地零基础学生/刻薄阅卷人 agent，要求写入 `06_open_observations/codex_agent_student_attack_review_v5_9_20260521.md`。
- [x] 捕获 GPTPro 自然完成输出，写入 `06_open_observations/gptpro_v5_9_attack_review_20260521.md`。
- [x] 捕获 Claude Opus 自然完成输出。
- [x] 合并 GPTPro / Claude / Codex agent 三方攻击意见，生成 `07_cross_validation/v5_9_attack_review_synthesis_20260521.md`。
- [x] 生成 V6 重构方案：学生首屏、强主干、题型场景、逐题示范、错误答案改写、证据附录分层。
- [ ] V6 不得把 38 非核心升核心；不得把 reference_only 升级；不得丢掉 65 题 corpus 纪律。

## 2026-05-21｜V6 Naked Blind Test Next

- [x] 生成 `12_final_baodian/选必二法律主观题满分训练宝典_v6_攻击审查融合工作稿_20260521.md`。
- [x] 在 V6 中加入设问尾词诊断树、三型答案骨架、题级禁用词表、易混题对照、三句保底答案、非核心适用/不适用设问。
- [x] 构造 V6 裸题盲测包：隐藏 question_id、category、evidence_level、core/guard 标签，只给材料与设问。
- [x] 让零基础聪明学生 agent 学习 V6 后作答。
- [x] Codex 按 rubric atoms 严格评分，并记录入口选择是否真实可迁移。
- [x] 若裸题盲测未达满分/接近满分，继续修 V6；通过前不生成 Word/PDF。
- [x] 根据本地严判生成 V6.2：前置 CC0244 无过错责任、表格直接按格写、AI 著作权主体排除。
- [x] 在等待外审时生成 V6.3 本地硬修候选：删除预设口诀味、后台标签学生化、修表格题模板污染。
- [ ] 捕获 GPTPro V6.2 裸题二审输出。
- [ ] 捕获 Claude Opus V6.2 裸题二审输出。
- [ ] 生成 V6.2 双审比较与 V6.3 本地硬修合并表。
- [ ] 若外审有 P0/P1，把 V6.3 继续修成 V6.4；若无 P0/P1，再重新裸题抽测后考虑 Word/PDF candidate。

## 2026-05-21 06:55｜V6.7 Student Candidate Next

- [x] 捕获 GPTPro V6.2 裸题二审输出。
- [x] 捕获 Claude Opus V6.2 裸题二审输出。
- [x] 生成 V6.2 双审比较与 V6.4 双外审硬修候选稿。
- [x] 构造 C/E/G/H 回归裸题包，隐藏题号、证据等级、core/guard 标签。
- [x] 让零基础聪明学生 agent 只读 V6.4 与干净题面作答。
- [x] Codex 严判 V6.4 回归结果，记录 3 PASS + 1 PARTIAL。
- [x] 生成 V6.5 因果硬词窄补丁。
- [x] 对表格题做 V6.5 一题最小回归，裁定 PASS。
- [x] 生成 V6.7 学生使用版 Markdown。
- [x] 导出 V6.7 学生使用版 DOCX。
- [x] 完成 V6.7 结构 QA 与 QuickLook 首屏视觉检查。
- [x] 构造 V6.7 GPTPro/Claude 最终学生可用性审稿包。
- [x] 本地硬审发现 V6.7 表格核心题头部缺失，生成 V6.8 修复稿、DOCX 和 QA。
- [x] 构造 V6.8 GPTPro/Claude 最终学生可用性审稿包，V6.7 外审包作废。
- [x] 完成 27 核心题小节完整性审计，发现 V6.8 只有 26 个核心标题。
- [x] 恢复 `RECOVER_2025_海淀_二模_18`，生成 V6.9 Markdown/DOCX/QA。
- [x] 构造 V6.9 GPTPro/Claude 最终学生可用性审稿包，V6.8 外审包作废。
- [x] 完成 V6.9 学生版文本卫生扫描，后台标签与占位词为 0。
- [ ] 将 V6.9 包发送给 GPTPro 与 Claude Opus，要求扮演零基础高三学生 + 严苛阅卷人，不得只做证据安全审稿。
- [ ] 直接 UI 投递时必须一次上传/一次发送；ChatGPT app 当前被 Computer Use 安全策略禁止控制，Safari 附件入口不稳定，不得硬点。
- [ ] 捕获 GPTPro / Claude V6.9 最终审稿结果并生成比较表。
- [ ] 解决 DOCX 全页视觉 QA：安装/调用 LibreOffice 或人工 Word 导出 PDF 后，渲染全页 PNG 检查。
- [ ] 继续排 38 非核心/source-check/reference-only 的回源复核队列；不得因 V6.7 学生版变干净而升核心。

## TODO - after STEP_110 submission

- [ ] Capture GPTPro V7 method-first output into `06_open_observations/gptpro_v7_method_first_batched_rebuild_20260521.md`.
- [ ] Capture Claude Opus V7 method-first output into `06_open_observations/claude_opus_v7_method_first_batched_rebuild_20260521.md`.
- [ ] Compare GPTPro and Claude V7 outputs; isolate shared method-learning conclusions, conflicts, and batch mechanism disagreements.
- [ ] Build V7 rewrite plan only after both real outputs are captured.
- [ ] Do not generate final宝典 until V7 candidate has passed student simulation and question-by-question stress test.

## TODO STEP_111

- [ ] Capture GPTPro METHOD_LEARNING_NOTES and WHY_V6_9_STILL_NOT_ENOUGH.
- [ ] Upload BATCH_01 zip and capture GPTPro batch findings.
- [ ] Upload BATCH_02 zip and capture GPTPro batch findings.
- [ ] Upload BATCH_03 zip and capture GPTPro batch findings.
- [ ] Upload BATCH_04 zip and capture GPTPro batch findings.
- [ ] Produce GPTPro-Claude V7 comparison and synthesis plan.
- [ ] Write V7 framework only after synthesis and source-card guardrails are applied.

## TODO STEP_114 V7.1 Source Repair

- [x] 核验 GPTPro/Claude V7 输出真实存在：method stage、BATCH_01—04、final proposal、Claude Cowork 输出、交叉对照均已落盘。
- [x] 生成 19 个空设问 + 3 个高风险题卡的 source-card repair 队列。
- [x] 对 6 个 `repair_now` 行生成可并入教师证据说明的 ask_text patch。
- [x] 对 `CC0223` 生成清洁题卡，剔除答案化材料原子；价值问如仍未锁原设问，进保险箱。
- [x] 对 `CC0150` 清理 Q21 当代国际政治与经济污染原子，不让其进入法律句库。
- [x] 对 `CC0244` 拆分合同链、侵权链、维权准备链细则原子。
- [ ] 对 10 个 `source_confirm_required` 行回源；不能回源的降级为保险箱或待确认，不进核心闭环。
- [ ] 生成 V7.1 教师证据说明和 DOCX 草稿；仍不得标最终 PASS。

## TODO STEP_117 V8 Student Usable Rebuild

- [x] 创建 `v8_student_usable_rebuild/`。
- [x] 完成 `01_v7_failure_diagnosis.md` 与 `.csv`。
- [x] 构造 GPT-5.5 Pro / Claude Opus 同题同问 v8 诊断包，确保文件名 ASCII、提示词 UTF-8、压缩包可直接上传。
- [x] 调用或交付 GPT-5.5 Pro：只做 v7.1 失败诊断、8 金样板建议、学生版动作框架建议、2 题样板运行。
- [x] 调用或交付 Claude Opus：同上，输入与输出格式完全一致。
- [x] 综合双模型建议，确定 8 道 formal/PASS_RECOVERED 金样板题。
- [x] 先重写 8 道金样板题；未完成前禁止写总框架。
- [x] 从金样板反推 `03_student_exam_framework_v8.md`。
- [x] 生成 `04_teacher_evidence_framework_v8.md/.csv`。
- [x] 生成 `05_full_score_sentence_bank_v8.md/.csv`。
- [x] 逐题重写 53 题 `06_question_by_question_runs_v8.md/.csv`。
- [x] 生成 `07_选必二法律主观题满分宝典_v8.md/.docx`。
- [x] 完成 `08_v8_student_usability_test.md` 与 `08_v8_acceptance_report.md`。
- [ ] 下一轮若继续：人工课堂口吻精修非金样板 45 题。
- [ ] 下一轮若继续：回源补齐 ask-missing 行，能补则补，不能补则继续降级。
- [ ] 下一轮若继续：对 v8 DOCX 做全页视觉 QA，并按需要导出 PDF。

## TODO STEP_123 v8.1 Student Delivery Fix

- [x] 对 v8 学生框架、宝典、金样板、句库、逐题运行和教师证据框架做硬 QA 初扫。
- [x] 将 8 道金样板同步替换进逐题运行。
- [x] 处理 20 道设问缺失题：16 道回填，4 道移入附录。
- [x] 优先重写 10 道非合格运行题。
- [x] 在节点 4 增加分支速查表。
- [x] 补充 7 类满分句模板。
- [x] 修教师证据框架，删除 gold 占位符并列真实证据编号。
- [x] 重新生成 v8.1 宝典 Markdown 和 DOCX。
- [x] 完成学生正文硬 QA 复扫，命中数 0。
- [ ] 下一轮若继续：对 v8.1 的非优先题逐题人工核读并课堂化重写。
- [ ] 下一轮若继续：安装/调用 LibreOffice 或通过 Word 导出 PDF，完成 DOCX 全页视觉 QA。

## TODO STEP_124 v9 Feige Style Rebuild

- [x] 停止 `v8_1_student_delivery_fix`，不再继续工程式 53 题修补。
- [x] 创建 `v9_feige_style_rebuild/`。
- [x] 学习桌面先前框架风格，输出 `01_飞哥旧框架风格DNA.md`。
- [x] 输出 `02_选必二法律主观题_先导.md`。
- [x] 输出 `03_选必二法律主观题_飞哥课堂版框架.md`。
- [x] 输出 `04_正向触发.md`。
- [x] 输出 `05_反向筛查.md`。
- [x] 输出 `06_高频答题语言.md`。
- [x] 输出 `07_10道极简演练.md`。
- [x] 输出 `08_v9_style_acceptance.md`。
- [x] 自检学生正文未命中 v8 工程词和 CC0229 四个禁用坏词。
- [ ] 用户确认 v9 风格后：再按 v9 口吻补 53 题附录题链。
- [ ] 用户确认 v9 风格后：再考虑整合成课堂版完整宝典；不得直接复用 v8/v8.1 逐题长稿。

## TODO STEP_125 v10 Exhaustive Framework And All Questions

- [x] 停止少量题先行/代表题演练结构。
- [x] 创建 `v10_exhaustive_framework_and_all_questions/`。
- [x] 读取 boundary-patched 53 题、材料原子、设问原子、细则原子、题链运行、句库、覆盖矩阵。
- [x] 生成 `01_框架穷尽清单.csv/.md`。
- [x] 生成 `02_上篇_选必二法律主观题穷尽框架.md`。
- [x] 生成 `03_下篇_53题全量题链.md/.csv`，53 题全量进入。
- [x] 生成 `04_框架_题目_细则覆盖矩阵.csv/.md`。
- [x] 生成 `05_v10_acceptance.md`。
- [x] 复扫并清理少量题先行结构禁词、CC0229 坏词、page/slide/评分说明残留。
- [ ] 若进入正式成书：逐题人工审读 53 题题链的课堂表达和材料匹配。
- [ ] 若进入正式成书：生成《选必二法律主观题穷尽框架与全题宝典》Word/PDF 并做视觉 QA。

## TODO STEP_126 v11 Source Locked Rebuild

- [x] 停止 v10，并在控制文件中作废 `EXHAUSTIVE_FRAMEWORK_PASS`。
- [x] 创建 `v11_source_locked_rebuild/`。
- [x] 生成 `01_53题回源审判表.csv` 与 `01_53题回源审判报告.md`。
- [x] 对 GPT 点名污染样例生成 `01A_关键污染题回源修复补丁.csv/.md`。
- [x] 生成 `02_强分诊框架清单.csv/.md`，用分诊闸门替代 v10 泛化清单。
- [x] 生成 `03_下篇_53题全量题链_v11.md/.csv`；未确认真实材料的题已待确认，不硬写。
- [x] 生成 `04_上篇_选必二法律主观题强分诊框架.md`。
- [x] 生成 `05_真实覆盖矩阵.csv/.md`，只统计真实主入口和主触发。
- [x] 生成 `06_v11_acceptance.md`，结论为 `CONDITIONAL_PASS`。
- [ ] 下一轮：建立 24 题回源修复队列，逐题补真实设问/材料核心。
- [ ] 下一轮：将补完的题从“待确认”升级为正式题链并复扫。
- [ ] 下一轮：全部补完后再评估是否有资格写 `SOURCE_LOCKED_PASS`。

## TODO STEP_129 v11.1 Written Chain Patch

- [x] 停止 v11 的下一步回填，不启动 24 题回填。
- [x] 重生成 `01_source_judgment_report_final.md` 与 `01_source_judgment_table_final.csv`，删除旧裁断残留。
- [x] 重写 CC0137，补齐 AI 著作权格和信用卡合同违约格。
- [x] 重写 CC0200，改为未成年人打赏、多方过错、公平原则分责。
- [x] 重写 CC0238，改为评析题，一主体一链。
- [x] 增强 CC0229，改为三案例法律手段链。
- [x] 处理 CC0305 标注，写明设问待补，不伪装完全闭合。
- [x] 更新强分诊框架，增加判决结果/责任分担、未成年人打赏、多案例意义题等分诊点。
- [x] 重新生成 v11.1 题链和真实覆盖矩阵。
- [x] 生成 `06_v11_1_acceptance.md`，结论为 `V11_1_WRITTEN_CHAIN_PATCH_PASS`。
- [x] 用户明确允许后，启动 24 题回源回填队列。
- [ ] 只有 24 题全部回填或用户确认降级/移出后，才讨论最终宝典。

## TODO STEP_130 v12 24 Question Backfill

- [x] 创建 `v12_24_question_backfill/`。
- [x] 生成 `01_24题待回源清单.csv/.md`。
- [x] 为 24 题生成 `source_lock_cards/` 与 `source_lock_cards_index.csv`。
- [x] 只回填 source lock 通过的 18 题，生成 `02_24题回填题链.csv/.md`。
- [x] 将 6 个无法锁源题移入 `04_无法回填或降级清单.csv/.md`。
- [x] 合并生成条件版 `03_all_53_question_chains_v12.csv/.md`，正文 47 题，不保留待回源占位。
- [x] 更新 `05_upper_strong_triage_framework_v12_patch.md`。
- [x] 更新 `06_true_coverage_matrix_v12.csv/.md`。
- [x] 完成硬 QA，02/03 正文未命中待回源占位、参考答案、评分说明、page/slide、R_/M_编号等污染词。
- [x] 生成 `07_v12_acceptance.md`，结论为 `CONDITIONAL_PASS`。
- [ ] 下一轮：用户提供或确认 CC0251、CC0276、CC0277、CC0317、CC0318、CC0319 的原题材料/设问；否则保持降级或移出。
- [ ] 下一轮：六题处理完毕后，再决定是否重建最终宝典与 DOCX。


## 2026-05-22 15:52:45 TODO after v12.1
- 基于 continue_source_hunt_6 对 6 道题做下一版 source-locked 回填。
- 回填后再更新强分诊框架和最终宝典，当前不得生成 DOCX。
