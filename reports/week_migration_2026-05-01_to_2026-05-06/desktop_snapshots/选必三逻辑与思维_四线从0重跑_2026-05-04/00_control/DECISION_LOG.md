# Decision Log

## 2026-05-04 启动纠偏

- 决定：前一版选必三返工不作为最终线继承，只作为失败样本和遗漏风险提示。
- 原因：用户指出内容质量与哲学宝典无法相比，且未严格四线。
- 本轮路线：新建 `选必三逻辑与思维_四线从0重跑_2026-05-04`，按四线总控 + 选必三分支 hard rules 执行。
- Advisor 规则：GPT-5.5 Pro / Claude Opus 必须真实调用；未调用时只能标 `real_call_pending`，不得 PASS。
- 推理边界：虽然选必三分支默认把纯形式逻辑排除出“思维主链”，但用户本轮明确要求推理部分成章分类处理，所以推理题进入单独分册/章节，不混入思维触发链。
# 2026-05-04 Phase 02 Decisions

- Decision: accept GPT-5.5 Pro `CONDITIONAL GO` as current commander gate.
  - Consequence: no student-facing manuscript, no Opus final wording, no Word/PDF, no final PASS until evidence matrices and cross-lane checks close.
- Decision: process five hard samples before full-suite writing.
  - Consequence: hard samples become regression tests for the full book workflow.
- Decision: use PyMuPDF, python-docx, python-pptx, PIL, and visual page review as fallback routes when Poppler/OCR/LibreOffice are missing.
  - Consequence: missing `pdftotext`, `pdftoppm`, `soffice`, or OCR tools cannot justify skipping source forms.
- Decision: mark 2025 海淀二模 Q20 as A- pending independent visual confirmation.
  - Consequence: it cannot be used for final student wording until a second pass confirms the rendered paper page.

# 2026-05-04 Phase 03 Gate Decisions

- Decision: accept GPT-5.5 Pro Phase 02 verdict `CONDITIONAL GO`.
  - Allowed: full suite question scan, classification, thinking signal-chain matrix, reasoning attachment matrix, A/B independent diff, visual fallback queue, blocked question lock, Phase 03 review packet.
  - Still blocked: student manuscript, Claude/Opus teaching rewrite, Word/PDF, final PASS.
- Decision: treat `02_extraction/phase03_preflight_candidate_scan.py` output as a queue only, not evidence.
  - Consequence: the 748 candidate rows must be paired back to raw source, answer/rubric, and visual records before any promotion.
- Decision: enforce GPT's Phase 03 acceptance sentence as a hard gate.
  - Gate: every question must return to a source locator and be placed in either the thinking signal-chain matrix, reasoning attachment matrix, or blocked list.
- Decision: keep HS02 as `LOCKED_PENDING_VISUAL`.
  - Consequence: it may guide the Phase 03 scan, but cannot enter student-facing wording until final visual/source checks close.

# 2026-05-04 Phase 03 Visual Repair Decisions

- Decision: treat paper PDFs with blank/thin text layers as coverage blockers, not as empty suites.
  - Consequence: `2025海淀二模` and `2026丰台一模` now carry suite-level `UNPARSED-PAPER` blockers until every rendered page is visually/OCR inventoried.
- Decision: allow Codex visual recovery seeds only as non-student evidence-control rows.
  - Consequence: `2025海淀二模 Q20` and `2026丰台一模 Q18(2)` are visible in Phase 03 matrices, but remain `locked_pending_laneB_visual_confirmation`.
- Decision: launch ClaudeCode Phase 03 as independent Lane B.
  - Consequence: ClaudeCode may read raw sources, manifests, skills, GPT digest, framework extracts, and renders; it must not read Codex Phase 03 conclusion matrices or visual seed CSV before producing its own Lane B outputs.

# 2026-05-04 Phase 03 Diff Decisions

- Decision: treat ClaudeCode Lane B Phase 03 as an independent candidate scan, not as every-question closure.
  - Consequence: the run remains `NO_PASS_CONTINUE_EXTRACTION`; all student-facing drafting remains blocked.
- Decision: require a focused Lane B patch for `2026丰台一模 Q18(2)` and `2025海淀二模 Q20 / HS02` before GPT Phase 03 commander review.
  - Consequence: `2026丰台一模 Q18(2)` cannot remain hidden behind a suite-level scan blocker if 042 render page 07 and 043 scoring source confirm it.
- Decision: split Lane A question coverage into canonical paper rows and support/reference rows before fusion.
  - Consequence: answer/rubric/讲评 rows cannot be treated as original question text; `05_coverage/phase03_laneA_dedup_question_matrix.csv` becomes the cleaner Lane A question base for the next diff.

# 2026-05-04 Phase 05 Evidence Archive Decisions

- Decision: accept GPT-5.5 Pro Batch03 verdict `GO_TO_PHASE05_EVIDENCE_FUSION_ARCHIVE` as a phase-direction signal only.
  - Consequence: Codex A may build evidence archives and typology skeletons, but student manuscript, Claude/Opus teaching rewrite, Word/PDF, and final PASS remain blocked.
- Decision: freeze `05_coverage/phase04_control_base_status_after_batch03_cleaned.csv` as the Phase05 control base.
  - Consequence: downstream counts must remain 362 rows total, with `L4=4`, `L3=70`, `L0=288`, and `L1=0`.
- Decision: remove retired wrong-option strings for `2024西城一模 Q11` from Phase05 archives.
  - Consequence: audit files may remember that a correction occurred, but Phase05 and later archive/student lines must carry only correct `B=①③`; the retired `B=①④` string must not propagate as a row-level description.
- Decision: require both Codex A local audit and ClaudeCode Lane B Opus 4.7 max audit before sending Phase05 to GPT.
  - Consequence: Codex A has passed `codex_lane/phase05_local_audit/phase05_codexA_local_audit.md`; ClaudeCode Lane B audit is currently running in `claudecode_lane/opus47_phase05_archive_audit/`.

# 2026-05-04 Phase 06 Evidence Lock Decisions

- Decision: accept GPT-5.5 Pro Phase05 verdict `GO_TO_PHASE06_EVIDENCE_LOCK_AND_FRAMEWORK_FUSION_NO_STUDENT_DRAFT`.
  - Consequence: Phase06 may build evidence-lock registers, thinking framework fusion, reasoning typology fusion, cross-mount locks, L0 retention, Governor/Confucius gates, and a GPT commander packet.
- Decision: Phase06 is not a student-facing stage.
  - Consequence: student稿, Claude Opus teaching prose, Word/PDF, final PASS, and “宝典成品” language remain blocked.
- Decision: freeze Lane B P3 warning patches before Phase06.
  - Consequence: `06_conflicts/phase05_patch_freeze_after_laneB_warnings.md` records the before/after state and carries `pending_B_ack` as a Phase06 P1 audit item.
- Decision: keep L3/L4 separation as a hard structural gate.
  - Consequence: L4 may be `LOCKED_FOR_FRAMEWORK`; L3 remains `CONFIRMED_FOR_ARCHIVE` and cannot become `LOCKED_FOR_STUDENT_TEXT`.
- Decision: launch ClaudeCode Lane B Phase06 audit only after Codex A generated and locally audited Phase06.
  - Consequence: Lane B receives Phase06 internal outputs and must audit structure/locks only; it is not allowed to write student稿 or Word/PDF.
- Decision: patch Lane B Phase06 warnings before sending Phase06 to GPT.
  - Consequence: although Lane B allowed GPT review with warnings, Codex A repaired placeholder/action fields first and recorded the patch in `06_conflicts/phase06_laneB_warning_patch_resolution.md`.

# 2026-05-04 Phase 07 Locked Packet Decisions

- Decision: accept GPT-5.5 Pro Phase06 verdict `GO_TO_PHASE07_LOCKED_OPUS_INPUT_PACKET_PREP_NO_STUDENT_DRAFT`.
  - Consequence: Codex A may prepare locked Opus input packet files only; no Opus prose, student稿, Word/PDF, or final PASS.
- Decision: Phase07 must sort L3 into include/hold instead of feeding all 70 L3 rows to Opus.
  - Consequence: L3 rows with missing critical fields, B-choice-signal-only risk, visual risk, reasoning form risk, thinking signal risk, or hard-lock risk must be held.
- Decision: Phase07 must keep Opus permission as `packet_only`.
  - Consequence: even included rows are not student text and cannot be consumed by Opus until Phase07 gates and GPT review pass.

# 2026-05-04 Phase 07 Lane B Audit Decisions

- Decision: accept ClaudeCode Lane B Phase07 verdict `PASS_PHASE07_WITH_WARNINGS` as no-blocker evidence, but patch the two P3 polish warnings before GPT review.
  - Consequence: Phase07 remains packet-prep only, but future Opus packet quality is cleaner.
- Decision: repair P3 warnings in `02_extraction/phase07_build_locked_opus_packet.py`, not by one-off CSV editing.
  - Consequence: regenerated Phase07 files keep counts stable while removing the warning classes.
- Decision: treat `answer_confirmed_PASS_TO_FUSION` as too vague for a locked packet answer locator.
  - Consequence: `Q-2026丰台一模-18-2` packet locator is now `answer_confirmed_甲正确乙错误_from_043_slide35_36_rubric`.
- Decision: send the patched Phase07 packet to GPT-5.5 Pro before any Opus teaching-text prototype.
  - Consequence: no student稿, Opus prose, Word/PDF, final PASS, or 宝典成品 language is authorized yet.

# 2026-05-05 Phase 08 Prototype Start Decisions

- Decision: accept GPT-5.5 Pro Phase07 verdict `GO_TO_PHASE08_OPUS_TEACHING_PROTOTYPE_NO_FINAL`.
  - Consequence: Phase08 may start only as an Opus review-only teaching-text prototype, not a student稿 or final artifact.
- Decision: freeze the Phase07 Lane B P3 patch before Opus consumption.
  - Consequence: `06_conflicts/phase07_laneB_warning_patch_freeze.md` records W01/W02 patch status and stable counts.
- Decision: restrict Phase08 Opus input to the 29 allowed rows.
  - Consequence: `05_coverage/phase08_opus_prototype_input_freeze.csv/md` includes 4 `include` rows and 25 `include_as_packet_candidate` rows; all 45 hold rows and all 288 L0 rows remain excluded.
- Decision: require post-Opus audit before promotion.
  - Consequence: after Opus returns, Codex A verification, Lane B prototype audit, Governor/Confucius review-only gates, and GPT Phase08 review are required before any further move.

# 2026-05-05 Phase 08 Lane B Patch Decisions

- Decision: accept ClaudeCode Lane B Phase08 verdict `PASS_PHASE08_PROTOTYPE_AUDIT_WITH_WARNINGS` as no-blocker evidence, but patch the P1/P2/P3 cleanliness warnings before Governor/Confucius/GPT review.
  - Consequence: no student稿 or final artifact is promoted; the review-only prototype is cleaner for the next gate.
- Decision: treat file-id fragments and pipeline field names as forbidden in teaching body even if not listed in the earlier P0 exact-term scan.
  - Consequence: `细则31`, `细则022`, `phase07`, `primary_reasoning_type`, `rule_slogan`, `cross_reference_policy`, and similar terms must not appear in `generated_text`.
- Decision: rebuild the prototype CSV from cleaned Markdown plus Phase08 freeze after the first patch script truncated the CSV.
  - Consequence: the rebuilt CSV must pass row count, ID set, module count, status count, and generated_text cleanliness checks; the corrupt pre-rebuild backup is retained for audit.
- Decision: continue to Governor/Confucius review-only gates before GPT Phase08 commander review.
  - Consequence: no student稿, Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品 language is authorized.

# 2026-05-05 Phase 09 Controlled Student Draft Decisions

- Decision: accept GPT-5.5 Pro Phase08 verdict `GO_TO_PHASE09_STUDENT_DRAFT_CONSTRUCTION_NO_WORD_NO_FINAL`.
  - Consequence: Codex A may build only a controlled student-draft from the 29 Phase08 prototype rows; Word/PDF, final PASS, 终稿, 最终稿, and 宝典成品 remain blocked.
- Decision: keep the Phase09 input set identical to Phase08 prototype IDs.
  - Consequence: the 74-row evidence pool, 45 hold rows, 288 L0 rows, hard-excluded rows, and同类题 IDs may not be expanded into正文.
- Decision: resolve GPT's named QID risks before Phase09 first-draft freeze.
  - Consequence: `Q-2025丰台期末-7`, `Q-2025顺义一模-7`, `Q-2026顺义一模-19-2`, `Q-2024朝阳二模-19-1`, `Q-2024朝阳二模-19-2`, `Q-2024朝阳一模-20-1`, `Q-2024朝阳一模-20-2`, `Q-2026通州期末-19-2`, `Q-2026丰台一模-18-2`, and `Q-2025海淀二模-20` must receive explicit Phase09 controls.
- Decision: require Codex A verification, ClaudeCode Lane B audit, Governor/Confucius gates, and GPT Phase09 review after the controlled draft.
  - Consequence: Phase09 cannot be promoted directly into a final student artifact.

# 2026-05-05 Phase 09 Lane B Patch Decisions

- Decision: accept ClaudeCode Lane B Phase09 verdict `PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS` as no-blocker evidence, but patch the P1/P2/P3 warnings before Governor/Confucius/GPT review.
  - Consequence: Phase09 remains controlled student-draft only; no Word/PDF or final artifact is authorized.
- Decision: patch Phase09 through the generator, not by manual one-off editing.
  - Consequence: regenerated student draft, backcheck, risk register, and verification files stay reproducible from `02_extraction/phase09_build_controlled_student_draft.py`.
- Decision: keep readable student headings and raw Q-ID same-type indexes, but add visible-title backcheck.
  - Consequence: student readability is preserved while audit traceability is restored through `visible_title_match` fields.
- Decision: record the `Q-2025顺义一模-7` 大项不当扩大 correction with an explicit source trace.
  - Consequence: Governor/Confucius/GPT can re-check the correction without relying on Codex A prose alone.

# 2026-05-05 Phase 10 Polish Start Decisions

- Decision: accept GPT-5.5 Pro Phase09 verdict `GO_TO_PHASE10_POLISH_OR_OUTLINE_NO_WORD_NO_FINAL`.
  - Consequence: Phase10 may polish structure, headings, same-type index style, choice answer format, and cross-entry answer anchors, but must not generate Word/PDF or claim final PASS.
- Decision: keep Phase10 source set locked to the same 29 controlled student-draft rows.
  - Consequence: 74 evidence rows, 45 hold rows, 288 L0 rows, and hard-excluded rows may not expand into正文 through polish.
- Decision: preserve all GPT-named QID risk locks during polish.
  - Consequence: `Q-2025顺义一模-7`, `Q-2025丰台期末-7`, `Q-2026顺义一模-19-2`, `Q-2024朝阳二模-19-1/19-2`, `Q-2024朝阳一模-20-1/20-2`, `Q-2026通州期末-19-2`, `Q-2026丰台一模-18-2`, and `Q-2025海淀二模-20` become Phase10 regression rows.
- Decision: use student-friendly headings plus a traceability backcheck instead of placing raw QIDs in every student heading.
  - Consequence: the body stays readable, while `phase10_question_id_traceability_backcheck.csv` must prove every QID remains recoverable.

# 2026-05-05 Phase 10 Lane B Patch Decisions

- Decision: accept ClaudeCode Lane B verdict `PASS_PHASE10_POLISH_AUDIT_WITH_WARNINGS` as no-blocker evidence.
  - Consequence: Phase10 can proceed to Governor/Confucius after Codex records the warning decisions; Word/PDF/final remain blocked.
- Decision: patch C33 source-trace-pointer warning through the Phase10 generator.
  - Consequence: `phase10_QID_risk_register.md` now directly points to `phase09_QID_risk_register.md` for the 036 顺义 source line supporting 大项不当扩大.
- Decision: do not restore `(X分)` rubric markers for C34.
  - Consequence: student-facing polish keeps the cleaner non-scoring tone, while the audit record notes that substance was preserved and no answer changed.

# 2026-05-05 Phase 10 GPT Gate Blocked Decision

- Decision: log the ChatGPT web Pro quota message as `blocked_advisor_real_gpt55_web_quota`, not as a completed GPT gate.
  - Consequence: Phase10 remains unpromoted until a real GPT-5.5 Pro retry succeeds or the user explicitly waives this exact gate.
- Decision: continue only local non-promotional preparation while the GPT gate is blocked.
  - Consequence: Codex A may inventory remaining locked evidence rows and prepare expansion-control materials, but may not call them Phase11 authorization, Word/PDF readiness, final PASS, 终稿, 最终稿, or 宝典成品.
- Decision: name the fallback work `Phase10.5` instead of `Phase11`.
  - Consequence: `phase10_5_pre_gpt_expansion_gap_inventory.csv` is a preparation ledger only; the next phase still requires real GPT retry or explicit user waiver.
- Decision: prioritize source repair from high-risk locked rows before any future expansion.
  - Consequence: protected hard-lock rows stay P0 non-expansion, high-value same-type clusters are P1/P2 repair candidates, and absent rows stay lower priority until GPT/Governor authorize a repair path.

# 2026-05-05 User Membership Constraint Decision

- Decision: suspend all Claude and ClaudeCode lanes because the user reported both memberships have dropped.
  - Consequence: until the user explicitly says membership is restored, do not run Claude desktop/app, ClaudeCode CLI, Opus 4.7, or any Claude/ClaudeCode audit or writer gate.
- Decision: continue with `Codex + GPT` only.
  - Consequence: Codex may keep local evidence, source repair, student-draft patching, Governor/Confucius-style local checks, and GPT-5.5 Pro web reviews moving; missing Claude/ClaudeCode gates must be logged as suspended, not passed.

# 2026-05-05 Phase 11A Start Decision

- Decision: accept GPT Phase10 retry verdict `GO_TO_PHASE11_CONTROLLED_EXPANSION_OR_CONTENT_REVIEW_NO_WORD_NO_FINAL`.
  - Consequence: start Phase11A 29-row content review only; do not expand to new rows yet.
- Decision: treat GPT's suggested ClaudeCode Lane B Phase11 review as unavailable under the user's membership constraint.
  - Consequence: Phase11A will use Codex local review plus GPT review only until the user restores Claude/ClaudeCode availability.

# 2026-05-05 Phase 11A Codex Local Review Decision

- Decision: accept Codex Phase11A 29-row content review as locally clean after review-only normalization.
  - Consequence: the 29-row student body can be sent to GPT for concrete content review, but no expansion, Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品 is authorized.
- Decision: treat two Phase11A patches as formatting/template normalization rather than new evidence claims.
  - Consequence: `路径` became `链条` in the 通州共变法辅助说明, and 顺义 19(2) received missing `可写思维/方法` / `为什么能想到` fields from existing material-action content.
- Decision: keep Claude/ClaudeCode suspended during Phase11A.
  - Consequence: missing Claude/ClaudeCode Phase11 review remains a suspended lane, not a passed lane.

# 2026-05-05 Phase 11A GPT Must-Fix Decision

- Decision: accept GPT Phase11A verdict `MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION`.
  - Consequence: Phase11B expansion remains blocked until the must-fix is patched and rechecked.
- Decision: patch all GPT Phase11A must-fix / should-fix / optional transfer points through the Phase11A generator without adding new rows.
  - Consequence: `2025 丰台期末第8题` now distinguishes 形象思维的感性形象 from 抽象思维的概念; `2024 朝阳二模第19题第(1)问` no longer names 联言判断 in the 第(1)问题型; `2024 西城一模第19题第(5)问` is marked as 综合方法链 / 超前思维链 rather than formal logic type; 海淀二模17(1)/(2) received weak-student transfer hints.
- Decision: keep Word/PDF/final and broad expansion blocked after patch.
  - Consequence: next step is a short GPT patch-resolution check or an explicit local gate decision, not Phase11B free expansion.

# 2026-05-05 Phase 11B Controlled Expansion Decision

- Decision: accept GPT patch-resolution verdict `GO_PHASE11B_CONTROLLED_EXPANSION_NO_WORD_NO_FINAL`.
  - Consequence: Codex may start Phase11B controlled expansion/source repair only; Word/PDF/final PASS remain blocked.
- Decision: Phase11B must start from the existing priority queue, not from all 74 evidence rows at once.
  - Consequence: begin with P1 high-value same-type index clusters and local source repair; do not expand 45 hold rows, 288 L0 rows, hard-excluded rows, or same-type indexes automatically.
- Decision: Claude/ClaudeCode remain suspended.
  - Consequence: Phase11B uses Codex local evidence verification plus GPT review gates only until user restores memberships.

# 2026-05-05 Phase 11B Batch01 P1 Local Repair Decision

- Decision: process only the three P1 high-value index-cluster rows for Batch01.
  - Consequence: P0 protected rows, L0 rows, hard-excluded rows, and the remaining non-body rows are untouched.
- Decision: treat `Q-2025东城期末-18-2` as a repaired innovation-thinking subjective candidate, not as a formal-reasoning or 三段论 row.
  - Consequence: it may be proposed to GPT as the only Batch01 body-expansion candidate.
- Decision: treat `Q-2026通州期末-9` as choice-trap index only.
  - Consequence: its answer D and systemized/digital integration signal are useful, but it does not become a main student-body subjective entry.
- Decision: treat `Q-2024朝阳二模-7` as reasoning-typology index only.
  - Consequence: it remains out of the thought-method body and goes to GPT mainly for validation of the A-option error label.
- Decision: run a GPT-5.5 Pro Batch01 review before merging anything.
  - Consequence: local status is `PASS_FOR_GPT_BATCH_REVIEW_ONLY`, not merge/final readiness.

# 2026-05-05 Phase 11C Bad Word Content Failure Decision

- Decision: accept the user's criticism that the `选必三逻辑与思维_完全模仿哲学宝典_学生版_2026-05-04.docx` content is not acceptable.
  - Consequence: that Word/Markdown is frozen as a failure sample and may not be polished, delivered, or used as the final-content base.
- Decision: mark generic four-element placeholders as a hard failure.
  - Consequence: entries with fake prompts such as `本题要求结合材料说明其体现的思维方法...` or answer instructions such as `卷面要把材料中的具体动作写进方法里...` cannot pass the student-body gate.
- Decision: same-question multi-node mounting must be node-specific.
  - Consequence: if one question appears under multiple framework nodes, each entry must rewrite the material trigger, why-it-triggers logic, and answer landing for that exact node; copied all-method summaries are rejected.
- Decision: continue the four-line project through content rebuild, not Word polishing.
  - Consequence: next steps are Codex local failure audit, visible-window ClaudeCode independent audit/sample rewrite, real GPT/Claude content review, local evidence verification, and only later Word generation after content gate closure.
- Decision: ClaudeCode must run in a visible ClaudeCode window for this phase.
  - Consequence: non-interactive `claude -p` outputs may be used only as smoke tests or provisional notes, not as a satisfied ClaudeCode lane for user-visible production work.

# 2026-05-05 Phase11B ClaudeCode Feedback Patch Decision

- Decision: receive the restored-account visible ClaudeCode Phase11B audit as independent worker feedback, not as final authority.
  - Consequence: its `PASS_WITH_RECOMMENDED_PATCHES` can create Codex patch tasks, but cannot merge student text or authorize Word/PDF/final.
- Decision: patch `Q-2024朝阳二模-7` A-option trap from old “三段论中项不周延” to “小项不当周延/小项扩大”.
  - Consequence: regenerated Phase05/06/07/10.5 current artifacts now carry the corrected risk note; old prompt/history files may still mention the old label only as a question or past error.
- Decision: patch `Q-2025东城期末-18-2` with the rubric anchor “思路新、方法新、结果新”.
  - Consequence: the Batch01 body candidate may be sent to GPT as a stronger innovation-thinking candidate, but cannot merge before GPT review.
- Decision: keep `Q-2026通州期末-9` as choice-trap index only and demote “系统化、数字化整合” to material signal.
  - Consequence: it must not become a subjective thought-method node unless a later scoring source supports it.

# 2026-05-05 Phase11C Visible ClaudeCode Fusion Decision

- Decision: accept Terminal ClaudeCode T1's seven Phase11C files as completed visible-window worker output.
  - Consequence: T1 is no longer considered stalled for this assignment; its outputs are received under `08_review/phase11C_visible_claudecode_output_digest.md`.
- Decision: use T1's gold contract and rebuild route as supporting constraints, but do not merge T1 rewrite samples into student text without Codex source verification and GPT/Opus/Governor gates.
  - Consequence: Phase11D may start only as Markdown review-only reconstruction from source-verified rows, not as bad Word polishing.

# 2026-05-05 Phase11B Batch01 GPT Merge Decision

- Decision: accept GPT-5.5 Pro verdict `PASS_BATCH01_MERGE_ONE_BODY_CANDIDATE` for Batch01 only.
  - Consequence: `Q-2025东城期末-18-2` may be added as a review-only body candidate, while `Q-2026通州期末-9` and `Q-2024朝阳二模-7` remain index-only.
- Decision: implement the merge through `02_extraction/phase11B_apply_batch01_gpt_merge.py`, not by editing the bad Word or hand-polishing old output.
  - Consequence: generated artifacts are `phase11B_batch01_student_body_30_REVIEW_ONLY.md`, `phase11B_batch01_merge_control_matrix.csv`, and `phase11B_batch01_index_only_register.md`.
- Decision: keep Word/PDF/final PASS blocked after the Batch01 merge.
  - Consequence: the new status is `PASS_FOR_REVIEW_ONLY_BATCH01_MERGE`, not final readiness.

# 2026-05-05 VSCode ClaudeCode Lane Boundary Decision

- Decision: do not receive the currently visible VSCode ClaudeCode session as a 选必三 artifact.
  - Consequence: the observed VSCode ClaudeCode work is on 选必二《法律与生活》 C-line/framework output, so importing it would mix modules.
- Decision: keep `claudecode_lane/vscode_lane_phase11C/` as the only accepted VSCode ClaudeCode path for the current 选必三 lane unless the user explicitly identifies another path.
  - Consequence: no VSCode ClaudeCode 选必三 output is counted as received at this checkpoint.

# 2026-05-05 Phase11D Seed Rebuild Decision

- Decision: start Phase11D from source-verified four-element Markdown seeds, not from the failed `选必三逻辑与思维_完全模仿哲学宝典_学生版_2026-05-04` Word/Markdown.
  - Consequence: the bad Word remains a failure sample only; every new student-facing entry must pass source verification, four-element gate, GPT content review, and later Governor/Confucius checks before any delivery work.
- Decision: use Terminal ClaudeCode T1's Phase11C gold contract as a standard, not as source authority.
  - Consequence: ClaudeCode rewrite samples remain non-mergeable until Codex verifies the exact source and GPT/Governor approve the repaired student text.
- Decision: submit the 8-entry Phase11D seed to real GPT-5.5 Pro before broad expansion.
  - Consequence: local status is `PENDING_PHASE11D_SEED_GPT_REPLY`; Codex may continue non-promotional source work, but no Word/PDF/final PASS is allowed.

# 2026-05-05 Four-Line Closure Hard Gate

- Decision: enforce the user's renewed instruction that the run must close through four real lanes: Codex, visible ClaudeCode, GPT-5.5 Pro web, and Claude Opus 4.7 Adaptive Thinking.
  - Consequence: Codex+ClaudeCode outputs alone cannot authorize final delivery; GPT-5.5 Pro and Claude Opus 4.7 Adaptive Thinking must both leave real captured outputs before final Markdown/Word/PDF acceptance.
- Decision: record `00_control/FOUR_LINE_CLOSURE_GATE_2026-05-05.md` as a hard gate.
  - Consequence: any missing, interrupted, quota-blocked, or uncaptured GPT/Claude lane becomes `real_call_pending`, not PASS.
- Decision: keep Opus in the sequence after evidence lock and before final Word.
  - Consequence: Opus may improve teaching prose, but any new term, example, or claim must return to Codex source verification before entering the student artifact.

# 2026-05-05 Phase12 Batch01 Repair Decision

- Decision: treat the first 12 Phase12 non-body rows as repaired review-only candidates after direct source and answer/rubric verification.
  - Consequence: these 12 rows can feed the later expanded review-only body build, but cannot by themselves change the global `FAIL_PENDING_EXPANSION` gate.
- Decision: confirm `Q-2026顺义一模-6` through raw `细则.pptx` slide 1 XML extraction rather than inherited extraction output.
  - Consequence: Q6=A is now a current-run source repair, not an old conclusion.
- Decision: keep `Q-2026东城期末-17-2` under formal-logic/reasoning, not the思维方法 main chain.
  - Consequence: it can appear in the推理部分正文 and推理题型索引, but not as a scientific/dialectical/innovative thinking trigger node.

# 2026-05-05 Phase12 Batch02 Repair Decision

- Decision: process the four P0 protected rows through explicit source repair instead of leaving them silently frozen.
  - Consequence: `Q-2026顺义一模-3`, `Q-2025海淀二模-12`, `Q-2024西城一模-11`, and `Q-2025海淀二模-13` now have review-only body-after-repair decisions, but still do not authorize final merge or Word.
- Decision: use rendered visual page reading for `Q-2025海淀二模-12` and `Q-2025海淀二模-13`.
  - Consequence: the blank text layer is not treated as a blocker, and the题面/选项恢复 is tied to the rendered page evidence.
- Decision: recover `Q-2024西城一模-11` from original docx XML hidden text boxes.
  - Consequence: the row is no longer based on a broken extraction that only showed ①②③④ placeholders.
- Decision: promote `Q-2024朝阳期中-19` from same-type index-only to a review-only subjective body candidate.
  - Consequence: its innovation-thinking answer must keep method-material pairing: 超前、逆向、联想、发散与聚合.
- Decision: keep global gate at `FAIL_PENDING_EXPANSION` after Batch02.
  - Consequence: 26 repaired review-only rows are progress only; 74-row expanded body, 362 rescan, dual indexes, and four-line gates remain required before any Word/PDF/final event.

# 2026-05-05 Phase12 Batch03 Repair Decision

- Decision: process the remaining 19 P5 reasoning/logic choice rows as review-only body-after-repair candidates.
  - Consequence: the full 45-row non-body repair queue is now repaired at review-only level, but nothing is final or Word-ready.
- Decision: require each P5 choice row to carry a usable reasoning form, rule口令, and trap explanation instead of only answer letters.
  - Consequence: these rows can feed the later expanded body and reasoning typology index.
- Decision: treat `Q-2026丰台一模-9` as a current-run supplemental-source repair because the 042 PDF text layer is blank.
  - Consequence: it may enter the review-only candidate pool, but must be flagged for Governor/external review before merged delivery.
- Decision: keep global gate at `FAIL_PENDING_EXPANSION` after Batch03.
  - Consequence: next required steps are rebuilding the expanded body from 29+45/74 evidence rows, performing 362 control-base rescan, generating dual indexes, and closing Codex/ClaudeCode/GPT/Governor/Confucius gates before any Word/PDF/final event.

# 2026-05-05 Phase12 74-Row Expanded Body Decision

- Decision: assemble the 29 controlled rows and the 45 repaired non-body rows into one 74-row review-only expanded body.
  - Consequence: `phase12_expanded_body_FROM_74_REVIEW_ONLY.md` becomes the current content base for 362 rescan and dual-index generation, but remains non-final.
- Decision: use fallback body blocks for `Q-2025海淀二模-20` and `Q-2026丰台一模-18-2` because they were absent from Phase11D combined29 headings but present in older controlled body artifacts.
  - Consequence: both rows are represented in the 74 body, but must be rechecked before final delivery.
- Decision: update the global gate from expansion-pending to 362/gates-pending.
  - Consequence: current blocking status is `FAIL_PENDING_362_RESCAN_AND_GATES`; Word/PDF/final remains forbidden.

# 2026-05-05 Phase12 362-Row Rescan Decision

- Decision: finalize the 362-row control-base rescan conservatively rather than forcing the target count to 90-120 by inference.
  - Consequence: only 3 new source-confirmed rows enter the review-only body; rows with answer or visual gaps stay blocked/excluded.
- Decision: promote `Q-2024朝阳一模-6`, `Q-2025西城二模-6`, and `Q-2026通州期末-10` as new 362-rescan review-only body candidates.
  - Consequence: the expanded body is now 77 rows, with 27 主观题 and 50 选择题.
- Decision: keep `Q-2024朝阳期中-10` blocked because no reliable objective answer key was found.
  - Consequence: Codex does not guess choice answers from logic or old context.
- Decision: move the global gate to dual-index and four-line-gate pending.
  - Consequence: current blocking status is `FAIL_PENDING_DUAL_INDEX_AND_FOUR_LINE_GATES`; Word/PDF/final remains forbidden.

# 2026-05-05 Phase12 Dual Index And Local Gate Decision

- Decision: build both the thinking-method index and reasoning-typology index from the 77-row review-only body.
  - Consequence:正文排序 follows the user's district/time rule, while method/type retrieval is provided by separate indexes.
- Decision: update `phase12_sort_key_matrix.csv` from the 77-row control matrix rather than leaving the older 74-row sort table.
  - Consequence: sort audit now covers all 77 current body entries.
- Decision: create external review packets but not operate GPT/Claude browser windows from Codex.
  - Consequence: `phase_12_77body_prompt_for_gpt55_USER_SUBMIT.md`, `claudecode_phase12_visible_77body_audit_prompt.md`, and `phase_12_77body_prompt_for_claude_opus47_adaptive.md` are ready, but their lanes remain uncaptured.
- Decision: keep Governor and Confucius as hold gates until external criticism is incorporated.
  - Consequence: local status is clear for external review only; Word/PDF/final remains forbidden.

# 2026-05-05 Phase12 Choice Option Visibility Decision

- Decision: treat the user's earlier “all choice questions show four options” correction as a current 选必三 final-build hard rule.
  - Consequence: the rule is now recorded in the current run notebook and skill notebook.
- Decision: audit all 50 choice entries for visible complete options before any final clean build.
  - Consequence: 23 entries initially entered a final-clean-build repair queue, even though they could still be externally reviewed for content.
- Decision: insert recovered full-option blocks into those 23 choice entries without changing answer judgments or trap explanations, then re-run the option visibility audit.
  - Consequence: current repair queue is 0; current status remains not final because external four-line gates and final student-clean build are still incomplete.

# 2026-05-05 Phase12 External Review Packet Decision

- Decision: refresh the GPT-5.5 Pro, visible ClaudeCode, and Claude Opus 4.7 Adaptive prompts after choice-option repair.
  - Consequence: external reviewers will see that all 50 choice entries now expose full option units or A/B/C/D options.
- Decision: package the 77-row review-only body, control matrix, dual indexes, gates, option audit/repair logs, and external prompts into one upload zip.
  - Consequence: `08_review/external_packets/phase12_77row_external_review_packet_2026-05-05.zip` is ready for safe manual upload; Codex still will not click uncertain GPT/Claude browser controls.

# 2026-05-05 Phase12 Review-Only Metadata Preclean Decision

- Decision: remove duplicate review metadata from the 77-row review-only body before further handoff.
  - Consequence: 77 entry headings remain, qid anchors are reduced to one per entry, and the duplicate choice-section heading is removed; no knowledge content or answer judgment changes.
- Decision: keep this as review-only cleanup, not a final student clean build.
  - Consequence: Word/PDF/final remains blocked pending external reviews and post-external gates.

# 2026-05-05 Phase12 Final Clean Build Readiness Decision

- Decision: create a readiness audit that separates local formatting readiness from external review blockers.
  - Consequence: local structure is ready to proceed to external review, but final clean build remains blocked by missing GPT-5.5 Pro, visible ClaudeCode, and Opus 4.7 Adaptive 77-row reviews.
- Decision: explicitly avoid generating final clean body, Word, or PDF during this readiness pass.
  - Consequence: the run remains honest: no final/终稿/TASK_COMPLETE wording is permitted.

# 2026-05-05 Phase12 MUST_FIX_CONTENT Patch Decision

- Decision: accept the user-pasted GPT-5.5 Pro 77-row review as a blocking external review with verdict `MUST_FIX_CONTENT`.
  - Consequence: the run enters `Phase12 external patch round`; final clean build, Word, PDF, final/PASS, `终稿`, and `宝典成品` remain forbidden.
- Decision: recheck `Q-2024海淀二模-17-1` against 027 paper and 028/029 answer sources.
  - Consequence: source decision is `SCIENCE_ONLY_SOURCE_SUPPORTED`; the body keeps the science-thinking prompt and does not restore the older three-module prompt.
- Decision: rebuild both indexes from manual locks and evidence fields instead of body keyword matching.
  - Consequence: forced false positives are cleared: sufficient/necessary conditional cross-mounts fixed, boundary traps no longer appear as positive thinking examples, and `Q-2024朝阳二模-7` stays 小项扩大.
- Decision: keep the rebuilt indexes as review-only.
  - Consequence: conservative `NEEDS_*` auxiliary nodes may remain for non-forced rows and must be polished before final student-clean index delivery.

# 2026-05-05 Phase12 Q2025 Shunyi Yimo 7 Addendum Decision

- Decision: treat the post-MUST_FIX review verdict `PATCH_REQUIRED_BEFORE_EXTERNAL_GATES_NO_WORD_NO_FINAL` as a new hard gate before external audits.
  - Consequence: do not send the packet to ClaudeCode/Opus until `Q-2025顺义一模-7` index pollution is patched and audited.
- Decision: manually lock `Q-2025顺义一模-7` in the reasoning index generator.
  - Consequence: the row no longer inherits stale phase06 wording; true fallacy is 大项不当扩大, while 小项不当扩大 is only the wrong option's mistaken label.
- Decision: add a forced audit check for `Q-2025顺义一模-7`.
  - Consequence: `phase12_reasoning_index_rebuild_audit.csv` now includes `major_term_expansion_not_positive_small_term = PASS`.
- Decision: record that `NEEDS_TYPE_CONFIRMATION` and `NEEDS_METHOD_CONFIRMATION` are review-only nodes, not final student-clean index nodes.
  - Consequence: final clean build must replace them with student-readable non-positive labels and preserve traceability outside the student body.
