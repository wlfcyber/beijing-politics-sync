# Run Protocol

Use this protocol when the user wants a whole-book or whole-module deliverable produced while they are away.

## Always-On Phase Boundary Rule

At the end of every phase below, run the Phase Boundary GPT Commander Gate from `whole-book-sop.md` unless the user explicitly disables GPT review for that run.

- Write `08_review/phase_reports/phase_XX_summary.md`.
- Send only the sanitized phase report to GPT-5.5 Pro when available.
- Save the raw GPT commander recommendation in `08_review/gpt_phase_advice/phase_XX_gpt.md`.
- Digest the advice into `08_review/codex_response_to_advice.md`, `00_control/MODEL_ADVICE_LOG.md`, and concrete local tasks.
- If GPT/web/another thread stalls, log `08_review/gpt_phase_fallback_log.md`, continue under Codex local protocol, and retry at the next phase boundary.
- Governor, not GPT, owns phase release. GPT can recommend GO; Governor decides whether the run may promote, continue, or must return to补证据/返修.
- If fallback was used and GPT later returns, run a late review against the skipped phase before final promotion.

## Always-On GPT Content Review Rule

For every completed student-facing artifact, chapter, section batch, final Markdown draft, and Word/PDF text extraction, run the GPT-5.5 Pro Content Review And Correction Gate from `whole-book-sop.md` unless the user explicitly disables it. The fixed trigger objects are `outline`, `section_batch`, `final_markdown`, and `word_pdf`; a missing trigger requires a logged fallback or explicit user waiver.

- Send the generated content itself in chunks, not only a progress summary.
- Ask GPT for concrete content corrections: conceptual errors, missing triggers, unsupported answer landings, weak transfer chains, contradictions, and revised wording.
- Save raw GPT review under `08_review/gpt_content_review/content_review_XX_gpt.md`.
- Digest every issue into `08_review/gpt_content_review/content_correction_log.md`.
- Codex must verify substantive corrections against local source evidence before patching.
- `must_fix_content` issues require local evidence checking before patching; `should_fix_transfer` issues require a transfer-chain check covering material trigger, why-this-knowledge, answer landing, and reusable wording.
- Final PASS is blocked until GPT content review and Codex evidence-verified correction are complete, with no unresolved `must_fix_content` and no transfer-blocking unresolved `should_fix_transfer`.
- Markdown PASS and Word/PDF PASS are separate gates; never use Markdown content approval as Word/PDF delivery approval.

## Phase 0: Intake

- For whole-book or overnight work, load `whole-book-sop.md` and use its sleep-start card. Do not ask broad questions after the user is ready to leave; collect book/scope/mode/start boundary/framework/source range/evidence default/deliverables, then keep moving with logged assumptions.
- Identify the book and exact scope. Examples: 必修四哲学 only, 选必一主观题 only, 选必二预处理 only, 选必三思维部分 only.
- Ask for the user's framework or exam logic. If the user gives only a rough framework, write it into `USER_FRAMEWORK.md` and mark uncertain nodes.
- Ask what old work is void. If the user says `从0`, old products may locate source files but must not provide conclusions.
- Ask whether the user authorizes long-running conversion, OCR/vision, rendering, worker restarts, and Word validation.
- Collect all high-risk examples the user has previously corrected and add them to `MASTER_REQUIREMENTS.md`.
- Ask questions one at a time until the book boundary, evidence boundary, output contract, and must-include/must-exclude samples are clear enough to run overnight.
- If there are multiple viable approaches, propose 2-3 options with tradeoffs and a recommendation. Record the accepted approach in `DECISION_LOG.md`.

## Phase 1: Workspace And Rules

- Create the run folder and required control files.
- For full-book runs, create or emulate the numbered layout from `whole-book-sop.md`: `00_control/`, `01_source_inventory/`, `02_extraction/`, `03_entries/`, `04_suite_reports/`, `05_coverage/`, `06_conflicts/`, `07_student_doc/`, `08_review/`, and `09_delivery/`.
- Create `task_plan.md`, `findings.md`, and `progress.md` for persistent working memory. Re-read these before major decisions.
- Create `08_review/phase_reports/` and `08_review/gpt_phase_advice/`; do not rely on chat memory for GPT commander checkpoints.
- Add `G10 GPT phase gate` to Governor: phase report complete, GPT raw advice saved or fallback logged, Codex digestion complete, and any late review scheduled.
- Create `08_review/gpt_content_review/`.
- Add `G11 GPT content review gate` to Governor: every fixed trigger object reviewed by GPT-5.5 Pro or covered by fallback/waiver, raw review saved, correction log written, substantive fixes evidence-verified, accepted fixes patched and verified closed, rejected fixes locally justified, deferred fixes moved to user decision, unresolved must-fix and transfer-blocking issues cleared or blocked.
- Copy or reference the lane notebook into the run folder.
- Write a single `MASTER_REQUIREMENTS.md` that resolves conflicts: user message > lane notebook > branch skill > prior artifacts.
- Record source roots and exclusion rules.
- During source inventory, after every two view/browser/search/PDF/image operations, write the key discovery to `findings.md` and the action to `progress.md`.

## Phase 2: Source Inventory

- Scan 2024, 2025, and 2026 local district-paper roots unless the user limits the range.
- Build or refresh cache according to the branch skill.
- For each suite, record paper, answer key, rubric, marking report, lecture/PPT, duplicate status, and confidence.
- Mark no-module suites honestly instead of forcing a fake entry.

## Phase 3: Dual Production

- Codex has two responsibilities: leader and producer. The leader maintains control files, supervises, compares, and fuses; the production lane works from local cache plus original sources and writes structured entries with evidence.
- Codex production is mandatory unless the user explicitly asks for supervision only. Do not let Codex merely dispatch ClaudeCode and wait.
- Claude Code lane independently reruns from the same scope and writes its own entries and suite reports.
- Each lane must close one suite before moving on: question list, evidence, entries, and suite report agree.
- Both lanes must process non-textual material with tools: render pages, OCR/vision, screenshots, Office conversion, or manual visual extraction.
- Dispatch parallel workers only for independent domains: different suites, different source-recovery tasks, or disjoint validation jobs. Do not assign two writers to the same output file unless one is explicitly review-only.

## Phase 4: Advisor Review

- GPT advisor receives only a sanitized context pack: goal, user framework, notebook digest, source/coverage statistics, sanitized entry samples, student draft excerpts, and explicit questions. Ask it for missing framework slots, high-risk confusions, wrong-option traps, and verification prompts.
- GPT content reviewer receives the completed generated student-facing content itself, chunked when necessary, plus enough evidence/fusion status to critique concrete content. Do not send accounts, paths, full source files, or large raw exam/scoring passages.
- Claude advisor receives a sanitized long-form review pack: student outline/draft, target student profile, user framework, notebook digest, and Confucius failures if any. Ask it to critique readability, chain clarity, and final document structure.
- GPT and Claude may act as co-commanders only at the recommendation layer. They can issue a structured plan, division of labor, risk list, and acceptance criteria, but Codex local supervisor must translate that into direct worker prompts.
- Do not forward a raw `commander packet` to Claude Code as authority. Phrase worker prompts as direct user/Codex assignments with scoped files and acceptance criteria.
- Advisor claims are not evidence. Add useful suggestions to `DECISION_LOG.md` only after local source review.
- Never send accounts, secrets, local absolute paths, large raw exam passages, large raw scoring-rule passages, or unverified conclusions to GPT/Claude advisors.
- For routine phase-end commander review, use the phase-boundary template in `cross-model-invocation.md` instead of inventing a fresh prompt.
- Do not treat "GPT reviewed it" as quality evidence. It is a planning signal until Governor and local source checks pass.
- Do not treat "GPT rewrote it" as content approval. Every substantive rewrite needs a Codex local evidence check before patching.

## Phase 5: Fusion

- Compare Codex production and Claude Code entries by suite, question, framework node, material trigger, answer/rubric boundary, and student-facing explanation.
- If both lanes agree, still check source traceability.
- If lanes disagree, open the original source. Do not delete or promote by model preference.
- Preserve the accepted user framework. If a term does not fit, record the closest node and why.
- Generate the student artifact from fused entries only after conflicts are resolved or explicitly marked as excluded/needs_user_ruling.
- After each meaningful student-facing section is drafted, run GPT content review and correction before promoting it to final draft status.

## Phase 6: Document Production

- Produce Markdown first for traceability, then Word for delivery.
- The student document must be organized by the user's framework unless the user asks for another order.
- Before Word production, extract the final Markdown content into GPT content-review chunks and clear the correction log.
- Keep audit evidence separate from student content.
- For Word: create page numbers, native clickable TOC when requested, stable heading styles, readable labels, visible images, and consistent choice-question formatting.
- Render or export PDF for visual QA. When Microsoft Word is active, open/save/validate the file in Word.

## Phase 7: Confucius And Final Acceptance

- Confucius reads only the final student artifact, not audit files or source packs.
- If Confucius finds unreadable logic, missing triggers, bad formatting, or failed transfer, return to the relevant phase.
- Final acceptance requires `FINAL_ACCEPTANCE_REPORT.md`, final Markdown, final Word, rendered/PDF validation when practical, source ledger, coverage matrix, suite reports, and Confucius report.
- Final acceptance also requires GPT content review records and an evidence-verified correction log with no unresolved `must_fix_content` issues.
- Completion claims require fresh evidence from this run. Re-read the control files, check the final artifacts, and cite the validation outputs before saying the task is done.

## Failure Handling

- If a worker stalls, inspect process state, debug logs, stream growth, file mtimes, network/auth errors, and tool calls before killing it.
- If GPT/web/another advisor thread stalls, do not wait passively. Record the symptom in `08_review/gpt_phase_fallback_log.md`, continue local Codex work that does not depend on the missing answer, and retry the advisor checkpoint later.
- Restart the same suite and same scope when needed. Do not skip ahead silently.
- If user input is needed but not immediately available, write `USER_QUESTIONS.md`, make a conservative temporary decision only when it does not alter evidence boundaries, and keep the item out of final PASS until resolved.
- Use the 3-strike error rule: first diagnose and fix, second try a different method, third rethink assumptions and log the blocker. After three failures, escalate with exact attempts and error text.
