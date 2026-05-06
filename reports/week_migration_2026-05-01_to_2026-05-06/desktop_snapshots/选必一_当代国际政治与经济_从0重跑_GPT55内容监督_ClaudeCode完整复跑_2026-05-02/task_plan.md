# Task Plan

Goal: Run 选必一 当代国际政治与经济_主观题_从0重跑_GPT55内容监督_ClaudeCode独立线 through three lanes into a final teaching document: Codex leader, Codex production, and Claude Code independent rerun.

## Current Status

- status: completed_with_recorded_gpt_exception
- current_phase: final delivery completed; heartbeat automation closure verified
- phase_01_gate_status: Valid GPT clipboard recovery accepted; invalid GPT UI outputs rejected.
- overnight_authorization: 2026-05-03 user is sleeping and authorized continuing to a morning finished version. Claude may direct ClaudeCode, but Codex keeps local evidence and final artifact authority.

## Phase Boundary Rule

After each phase or substantial milestone: write a sanitized phase report, send it to GPT-5.5 Pro when available, save the raw commander advice, digest it into local tasks, and continue. If GPT/web/thread stalls, log the fallback and keep running authorized local work. Governor, not GPT, owns phase release; fallback phases need late review when GPT returns.

## GPT Content Review Rule

After each fixed trigger object (`outline`, `section_batch`, `final_markdown`, `word_pdf`): send the generated content itself to GPT-5.5 Pro in chunks, save raw review, digest concrete content corrections, locally verify substantive fixes, patch, and rerun until no unresolved `must_fix_content` remains and no `should_fix_transfer` blocks student transfer. Missing trigger objects need fallback/waiver. Markdown PASS and Word/PDF PASS are separate. Final PASS is blocked until this is complete unless the user disables it.

## Phases

- [x] Phase 0: Intake and user framework lock
- [x] Phase 1: Workspace, notebooks, and master requirements
- [x] Phase 2: Source inventory, source locking, and P0/P2 evidence matrix
- [x] Phase 3: Three-lane production by suite/question
- [x] Phase 4: Advisor review and governor checks
- [x] Phase 5: Fusion into student artifact
- [x] Phase 6: Word/PDF production and visual QA
- [x] Phase 7: Confucius artifact-only learning verification
- [x] Phase 8: Final acceptance report

## Overnight Sprint: 2026-05-03

Goal: finish the book run into a morning deliverable, without deleting or overwriting the old final artifact.

- [x] Update heartbeat automation to supervise the current Phase 02 restart screen and final-delivery gates.
- [x] Run Claude advisor/commander lane and convert its advice into Codex-owned ClaudeCode tasks.
- [x] Keep ClaudeCode running or restart it with small-context prompts if it stalls, drifts, early-stops, or hits large-payload errors.
- [x] Close Phase 02 enough for final production: source eligibility, high-priority P0/P2 recheck, visual/OCR blockers, and conflict register.
- [x] Finish must-check suites from the notebook: 2025海淀期末 Q22, 2024东城一模 Q16/Q20, 2026西城期末 Q20 blocker, plus already verified 2026通州期末、2026朝阳期中、2025海淀期中.
- [x] Fuse Codex and ClaudeCode outputs only after local source evidence settles conflicts.
- [x] Produce student-facing outline, section batches, final Markdown, DOCX, PDF, and final acceptance report.
- [x] Run GPT-5.5 Pro content review/fallback logs for outline, section_batch, final_markdown, and word_pdf.
- [x] Run Governor, Confucius artifact-only learning verification, Markdown residue check, and Word/PDF QA before marking PASS.

## Decisions Made

- From-zero rerun; old final preserved and old conclusions invalid as evidence.
- ClaudeCode runs complete independent version with no budget cap.
- GPT-5.5 Pro content supervision uses the current already-open Safari ChatGPT Pro conversation.
- Fixed GPT content review triggers are `outline`, `section_batch`, `final_markdown`, and `word_pdf`.
- Primary source roots are Desktop 2024/2025/2026 mock-paper folders; mirrors/cache only supplement.
- GPT-5.5 Pro is strategy/review advice only; source evidence and artifact inclusion are decided locally by original sources, notebook/skill rules, Codex evidence checks, and Governor gates.
- Claude advisor may now direct ClaudeCode at the user's request, but only through Codex digestion into local worker prompts; Claude advice is not evidence.
- Invalid GPT UI outputs are excluded from advice and not counted for G10.
- Do not start whole-book final term document until Phase 02 matrix and P0/P2 recheck have passed.

## Phase 02: Source Locking And Evidence Matrix

Goal: lock the effective evidence pool for 选必一主观题 scoring-term accumulation before batch production.

Required artifacts:

- [x] `01_source_inventory/source_ledger_updated.csv`
- [x] `03_entries/suite_question_matrix.csv`
- [x] `03_entries/evidence_level_recheck.csv`
- [x] `03_entries/xuanbiyi_subjective_index.csv`
- [x] `03_entries/xuanbiyi_subjective_entries_phase02.jsonl`
- [x] `08_review/phase_reports/phase02_codex_source_lock_report.md`
- [x] `08_review/phase_reports/hard_sample_review_2026_tongzhou_q20.md`
- [x] `08_review/phase_reports/hard_sample_review_2026_chaoyang_q17.md`
- [x] `08_review/phase_reports/hard_sample_review_2025_haidian_midterm_q16_q21.md`
- [x] `05_coverage/phase02_blockers.md`

Codex production tasks:

- [x] Verify all 177 source files have stable `source_id` and current-run source-root provenance.
- [ ] Recheck 98 P0 candidates by content and classify into verified scoring/rubric/marking, reference answer, teaching/lecture, paper-only, unknown visual-check, or excluded.
- [x] Build initial suite/question matrix for xuanbiyi subjective questions.
- [ ] Preserve 2026石景山期末 exclusion and 2026海淀期末 user-confirmed no-module status pending current-run check.
- [x] Standardize 2026通州期末 Q20 six-entry sample against original paper/scoring PPTX.
- [x] Standardize 2026朝阳期中 Q17 three-layer sample against original paper/scoring DOCX and supplemental scoring DOCX.
- [x] Reopen 2025海淀期中 Q16(2)/Q21(2), locate embedded image/table scoring details, and index the user-notebook required terms.
- [ ] Mark any PDF/PPT/image/table/OCR-dependent entry as provisional until visual or original-file validation is done.

ClaudeCode supervision tasks:

- [x] Confirm original screen session `xuanbiyi_claudecode_zero_20260502_r2` stopped after `413 Request too large`.
- [x] Inspect ClaudeCode entries for missing evidence matrix, source blockers, and provisional claims.
- [x] If needed, send a Codex-owned Phase 02 corrective prompt; do not paste GPT raw advice as authority.
- [ ] Confirm restarted screen session `xuanbiyi_claudecode_phase02_restart_20260502` remains healthy and produces Phase 02 outputs.
- [ ] Compare ClaudeCode hard samples with Codex only after both have source locators.

G11 trigger state:

- outline: not_triggered
- section_batch: not_triggered
- final_markdown: not_triggered
- word_pdf: not_triggered


## Errors Encountered

| Attempt | Error/Symptom | Different Next Step | Resolution |
|---|---|---|---|
| ClaudeCode launch #1 | `stream-json` output requires `--verbose`; process exited before work. | Add `--verbose` and relaunch in a new screen session. | Fixed in `claudecode_lane/START_CLAUDECODE.sh`; relaunched as `xuanbiyi_claudecode_zero_20260502_r2`. |
| GPT Phase 01 send #1 | Safari JavaScript injection disabled; System Events keyboard injection failed with `-25200`; Computer Use could not access Safari key window. | Log G10 fallback and continue local source work; retry GPT handoff later or ask user to paste prepared prompt if needed. | Fallback recorded in `08_review/gpt_phase_fallback_log.md`; prompt is saved in `advisor_prompts/gpt_phase_01_commander_prompt.md`. |
| GPT Phase 01 send #2 | Computer Use multiline `type_text` fragmented the prompt into separate ChatGPT user bubbles; GPT answered broken fragments. | Reject the output and mutate delivery route. | Marked invalid in fallback log; not saved as advice. |
| GPT Phase 01 send #3 | Computer Use single-line `type_text` preserved one bubble but corrupted/dropped Chinese content. | Stop response and switch to macOS clipboard paste. | Marked invalid in fallback log; not saved as advice. |
| GPT Phase 01 send #4 | Clipboard paste into already-open Safari ChatGPT Pro composer preserved Chinese and produced a coherent Phase 01 commander packet. | Save raw response and digest locally before phase promotion. | Raw saved at `08_review/gpt_phase_advice/phase_01_gpt_raw.md`; digestion in progress. |


## Heartbeat Closure: 2026-05-03 01:18 CST

- Final artifacts verified present: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02/09_delivery/飞哥政治庄园_选必一_当代国际政治与经济_细则术语成品版_2026-05-03.md`, `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02/09_delivery/飞哥政治庄园_选必一_当代国际政治与经济_细则术语成品版_2026-05-03.docx`, `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02/09_delivery/飞哥政治庄园_选必一_当代国际政治与经济_细则术语成品版_2026-05-03.pdf`, `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02/FINAL_ACCEPTANCE_REPORT.md`.
- ClaudeCode screens verified absent; overnight final log ended successfully.
- Final QA verified 81 term headings, 84 example blocks, 24-page PDF, and empty Markdown/DOCX/PDF forbidden-term scans.
- Remaining exception: GPT-5.5 Pro final content review not obtained due UI/automation failures; fallback logged.
- Automation `claudecode-0` is now obsolete and should be deleted.
