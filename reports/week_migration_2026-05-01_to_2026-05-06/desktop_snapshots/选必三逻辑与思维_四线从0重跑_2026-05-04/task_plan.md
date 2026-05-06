# Task Plan

Goal: Run 选必三逻辑与思维 思维部分+推理部分 through the full four-lane workflow into a final teaching document: Codex controller + Codex production lane A, ClaudeCode production lane B, Claude Opus teaching-text lane, GPT-5.5 Pro commander/content-review lane, then Governor and Confucius gates.

## Current Status

- status: phase11B_controlled_expansion_authorized_no_word_no_final
- current_phase: Phase 11B controlled expansion/source repair, Codex+GPT only

## Phase Boundary Rule

After each phase or substantial milestone: write a sanitized phase report, send it to GPT-5.5 Pro when available, save the raw commander advice, digest it into local tasks, and continue. If GPT/web/thread stalls, log the fallback and keep running authorized local work. Governor, not GPT, owns phase release; fallback phases need late review when GPT returns.

## GPT Content Review Rule

After each fixed trigger object (`outline`, `section_batch`, `final_markdown`, `word_pdf`): send the generated content itself to GPT-5.5 Pro in chunks, save raw review, digest concrete content corrections, locally verify substantive fixes, patch, and rerun until no unresolved `must_fix_content` remains and no `should_fix_transfer` blocks student transfer. Missing trigger objects need fallback/waiver. Markdown PASS and Word/PDF PASS are separate. Final PASS is blocked until this is complete unless the user disables it.

## Phases

- [ ] Phase 0: Intake and user framework lock
- [ ] Phase 1: Workspace, notebooks, and master requirements
- [ ] Phase 2: Source inventory and evidence map
- [ ] Phase 3: Four-lane production by suite/question: Codex A + ClaudeCode B + pending Opus/GPT gates
- [ ] Phase 4: GPT commander/content review, Claude Opus teaching pass, and Governor checks
- [ ] Phase 5: Fusion into student artifact
- [ ] Phase 6: Word/PDF production and visual QA
- [ ] Phase 7: Confucius artifact-only learning verification
- [ ] Phase 8: Final acceptance report

## Decisions Made

- Previous 选必三 output is treated as failed reference only, not inherited evidence.
- 推理部分 is handled as a separate reasoning chapter, not mixed into the 思维主链.
- Real GPT-5.5 Pro and Claude Opus calls are required for PASS; if unavailable, record pending/fallback and block final four-lane closure.
- 2026-05-05 用户暂停 Claude/ClaudeCode/Opus，因为会员掉了；当前仅允许 Codex + GPT，Claude/ClaudeCode gate 只能记 suspended，不能记 PASS。
- Phase11A Codex local review passed 29/29 after two review-only formatting/template normalizations; next gate is GPT-5.5 Pro concrete content review, still no expansion or final delivery.
- Phase11A GPT returned `MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION`; Codex patched the named concept risk and transfer issues, then rechecked 29/29 PASS with no expansion.
- Phase11A patch-resolution GPT returned `GO_PHASE11B_CONTROLLED_EXPANSION_NO_WORD_NO_FINAL`; Phase11B may start from the repair priority queue, still with no Word/PDF/final and no Claude/ClaudeCode.
- Phase11B Batch01 Codex local repair processed only three P1 rows. One row is a possible body candidate after GPT review; two rows remain index-only. No Word/PDF/final and no Claude/ClaudeCode.

## Errors Encountered

| Attempt | Error/Symptom | Different Next Step | Resolution |
|---|---|---|---|
