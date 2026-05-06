---
name: feige-politics-garden-book-orchestrator
description: "Use when the user wants to pick one Beijing Gaokao politics book/module and have Codex plus ClaudeCode plus Claude Opus plus GPT-5.5 Pro run it end-to-end into a final teaching document, especially overnight or long-running workflows where Codex and ClaudeCode are both production workhorse lanes, Claude Opus is the teaching-text output lane, GPT-5.5 Pro is chief content reviewer/pressure tester, with source exhaustion, framework mapping, Word/PDF delivery, Governor, and Confucius zero-baseline learning verification. Trigger on requests such as 选一本书跑完, 两线一起跑, 三线一起跑, 四线一起跑, 四线终极版, Codex自己也跑, Codex和ClaudeCode协作, GPT和Claude指导, GPT 5.5 Pro检查修正, Claude Opus成品化, 睡觉后生成终极文档, or 飞哥政治庄园整本书总控."
---

# 飞哥政治庄园-整本书四线终极总控

This skill orchestrates a full book/module run: the user selects one book, gives the book's exam logic and framework, Codex leads the run and also runs production lane A, ClaudeCode runs production lane B from the same raw sources, Claude Opus 4.7 Adaptive turns evidence-locked material into strong student-facing teaching prose, GPT-5.5 Pro acts as chief content reviewer / pressure tester, Governor blocks false completion, and Confucius validates whether the final artifact can teach a zero-baseline student.

## First Move

1. Load `feige-politics-garden` first, then route to the correct branch skill for the chosen book.
2. For whole-book or overnight work, read `references/whole-book-sop.md` after this file and treat it as the concrete team SOP for sleep-start cards, numbered run folders, role boundaries, advisor packs, phase-boundary GPT commander gates, GPT content-review/correction gates, Claude Code prompts, conflict resolution, and failure gates.
3. Search the Beijing politics workspace for the book's local notebook or hard-rule file and read it before planning.
4. Ask the user only the questions needed to avoid a wrong run:
   - Which book/module and exact scope?
   - What is the user's framework or exam logic for this book?
   - Which old lanes are void, excluded, or allowed only as audit references?
   - Are there must-include, must-exclude, or user-corrected hard samples?
5. If the user is going to sleep, collect the eight-item start card from `references/whole-book-sop.md` if possible. If the user gives only a one-line start command, infer safe defaults from the SOP and log unresolved items in `USER_QUESTIONS.md` instead of stopping unless the source boundary is impossible.

## Project Bootstrap

Create a dedicated run folder, usually under `/Users/wanglifei/Desktop/北京高考政治`, with a name containing the book, scope, and date. Prefer running:

```bash
python3 scripts/init_book_run.py --root /Users/wanglifei/Desktop/北京高考政治 --book "必修四" --scope "哲学" --date 2026-05-02
```

The run folder must contain at least:

- `task_plan.md`
- `findings.md`
- `progress.md`
- `TASK_BRIEF.md`
- `MASTER_REQUIREMENTS.md`
- `USER_FRAMEWORK.md`
- `USER_QUESTIONS.md`
- `PROGRESS.md`
- `DECISION_LOG.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `advisor_prompts/`
- `advisor_reports/`
- `08_review/phase_reports/`
- `08_review/gpt_phase_advice/`
- `08_review/gpt_content_review/`
- `08_review/gpt_phase_fallback_log.md`
- `codex_lane/`
- `claudecode_lane/`
- `fusion/`
- `suite_reports/`
- `audit/confucius/`
- `outputs/`

See `references/control-files.md` for schemas and status language.

The lowercase files are the file-backed working memory layer absorbed from `planning-with-files`: `task_plan.md` tracks phases and decisions, `findings.md` stores research/source discoveries, and `progress.md` logs session actions. The uppercase files are the stricter Feige Politics Garden control layer used for final governance.

For full-book runs, also prefer the numbered directory layout from `references/whole-book-sop.md` (`00_control/` through `09_delivery/`). Keep the older root-level files for compatibility when needed, but do not let compatibility files replace the numbered folders' detailed audit trail.

## Lanes

Run Codex leadership plus two workhorse evidence production lanes, one teaching-text output lane, one chief content review lane, Governor, and Confucius:

- `Mandatory real-call rule`: GPT-5.5 Pro and Claude Opus 4.7 Adaptive lanes must be satisfied by real calls to those models/services. Do not substitute Codex subagents, local simulations, generic advisor notes, or Codex roleplay for either lane. Codex subagents may help prepare sanitized packs, summarize evidence, or preflight questions, but their outputs cannot be logged as GPT-5.5 Pro or Claude Opus results. If a real call is unavailable, log `blocked_advisor` / `real_call_pending`, continue only safe local evidence work, and block phase promotion/final PASS until the real call succeeds or the user explicitly waives that exact gate.
- `Codex leader lane`: plan the run, maintain control files, assign/monitor workers, compare lanes, make source-boundary decisions, run governor checks, and own final fusion. Leadership does not replace Codex production.
- `Codex production lane A`: Codex must directly process sources, read/render/OCR files, write its own entries, close suites, update ledgers, and produce source-backed draft content. Codex is not allowed to act only as supervisor unless the user explicitly narrows the task to supervision.
- `Codex production lane A internal agents`: the user's original Garden roles belong inside Codex A and must be generated or explicitly ledgered for substantial work. `决策者` decides next bottlenecks and wakes stalled work; `劳动者` handles assigned suites/questions and source-backed entries; `补丁者` checks one-material-multiple-answer-point misses, same-core merge errors, expression accumulation, and framework placement; `监管者/Governor` performs Codex-A-level vetoes before final Governor; `自动化检测者` checks that plan, progress, source ledger, coverage matrix, suite reports, final report, and rendered artifacts agree. These agents do not replace ClaudeCode, Claude Opus, GPT-5.5 Pro, the final Governor, or Confucius.
- `ClaudeCode production lane B`: independent suite-by-suite or batch rerun from the same raw sources and same user notebook; it must produce source ledger, entries, suite reports, coverage matrix, blockers, suspected conflicts, and draft source-backed content. It is a workhorse production lane, not merely a reviewer.
- `Claude Opus 4.7 Adaptive teaching-text lane`: after Codex/ClaudeCode evidence is locked or provisionally tagged, rewrite and organize the content into student-facing teaching prose, transfer chains, answer-sentence language, section structure, and readability improvements. It must not introduce unsupported scoring terms or decide evidence.
- `GPT-5.5 Pro strategic commander / GPT advisor lane`: stress-test the user's framework, missing trigger types, wrong-option patterns, possible student confusion, run strategy, division of labor, risks, and acceptance criteria. Use prompts from `references/role-prompt-templates.md`. Its output is a recommendation packet for Codex local supervisor, not worker authority.
- `GPT-5.5 Pro content review lane`: after each completed student-facing deliverable, chapter, section batch, or final draft, review the actual generated content for conceptual mistakes, missing triggers, unsupported leaps, weak answer logic, student-transfer failures, and concrete wording fixes. Its output is correction advice; Codex must verify every substantive correction against local evidence before patching.
- `Governor lane`: reject weak evidence, fake closure, source/rubric mixing, missing suite reports, and final artifacts that contain audit language.
- `Confucius lane`: read only the final student artifact from zero, in a harsh student role, then run three-layer learning verification. See `references/confucius-acceptance.md`.
- `Role ledger`: every meaningful patch, even a Codex-only patch, must record which Garden roles were run, which were not rerun, and why. A narrow wording/format patch may reuse existing GPT/Claude/ClaudeCode evidence if it creates no new source claim, but Governor and Confucius must be refreshed whenever the student artifact changes.

For substantial whole-book runs, Codex A should create visible files such as `codex_lane/agents/decision_maker.md`, `codex_lane/agents/worker.md`, `codex_lane/agents/patcher.md`, `codex_lane/agents/governor.md`, and `codex_lane/agents/automation_checker.md` or equivalent per-role outputs. If actual subagent execution is available, use real subagents/threads with separated responsibilities; if not, record the local simulated pass and the reason in the role ledger.

Advisor/text outputs are advisory even when GPT-5.5 Pro is acting as strategic commander or Claude Opus is improving prose. Never promote a claim because GPT or Claude said it; promote it only when local source evidence and the user's framework support it.
The phase release authority is Governor, not GPT. A GPT `GO` means "useful planning signal"; it does not mean the phase is complete.

## Execution Loop

1. Write `MASTER_REQUIREMENTS.md` as the highest-priority instruction for this run: scope, old-lane inheritance boundary, source roots, output contract, validation gates, and authorization level.
2. Write `task_plan.md`, `findings.md`, and `progress.md`; re-read them before major decisions. After every two source/PDF/browser/image reads, save key findings to `findings.md` so visual and transient evidence is not lost.
3. Before starting production, run a brief design gate: ask unresolved questions one at a time, propose 2-3 execution approaches when meaningful, record the chosen approach in `DECISION_LOG.md`, and only then launch lanes.
4. Build or refresh the readable corpus cache if the branch skill requires it. Cache-first is not cache-only; return to original Word/PDF/PPT/images when cache misses options, rubrics, tables, cartoons, or layout.
5. Inventory source suites and classify each as `in_scope`, `excluded`, `no_module`, `uncertain`, or `needs_user_ruling`.
6. Process by suite/question. Do not advance a suite to closed until entries, source evidence, coverage, and suite report agree.
7. Compare Codex production lane A and ClaudeCode production lane B outputs:
   - agreement raises confidence but does not replace evidence;
   - disagreement goes back to source;
   - keep the stronger student-facing explanation only after source placement is settled.
8. After every completed phase or substantial milestone, run the Phase Boundary GPT Commander Gate from `references/whole-book-sop.md`: write a sanitized phase report, send it to GPT-5.5 Pro when available, save the raw reply, digest accepted/rejected advice locally, and continue from Codex-owned tasks. If the web/other thread stalls, log the fallback and keep moving under the local protocol instead of freezing the book run.
9. After every fixed content-review trigger (`outline`, `section_batch`, `final_markdown`, `word_pdf`), run the GPT-5.5 Pro Content Review Gate from `references/whole-book-sop.md`. Send the generated content itself in chunks when needed, collect concrete content corrections, verify each substantive correction locally, patch the artifact, and repeat while `must_fix_content` or transfer-blocking `should_fix_transfer` issues remain. Missing triggers require fallback or user waiver.
10. Send the evidence-locked fusion pack to Claude Opus 4.7 Adaptive for teaching-text成品化: structure, readability, transfer logic, answer sentence fluency, and student-facing wording. Codex must reject or return for evidence checks any new unsupported content.
11. Fuse into a student artifact organized by the user's framework, not by suite order, unless the user explicitly asks otherwise.
12. Generate final Markdown and Word through the simplified document pipeline in `references/document-pipeline.md`. If final output is `.docx`, also use the `documents` skill, render/export for visual QA when the renderer is available, and use Microsoft Word validation when available.
13. Run Governor checks, GPT content review, then Confucius checks. Any FAIL or unresolved high-risk question sends the work back to the relevant lane.
14. Finish only when fresh verification evidence exists and `FINAL_ACCEPTANCE_REPORT.md` states the final paths, validation evidence, known exclusions, and remaining user questions if any.

For Codex solo/narrow continuations, do a compact version of the same closure: update the role ledger, write a Governor patch gate, run Confucius artifact-only on the changed student artifact, and append the results to the local acceptance report.

## Overnight Rules

- Treat "I am going to sleep" as authorization to continue through non-destructive reading, writing, conversion, OCR/vision, rendering, script execution, worker restarts, and validation within the run folder, unless the user set narrower limits.
- Do not wait on cosmetic uncertainty. Make conservative choices, record them in `DECISION_LOG.md`, and keep the accepted version as the base once the user praises it.
- Stop only for source-boundary questions that would make the artifact factually unsafe, such as whether a disputed book/module is in scope or whether a non-rubric file may be used as scoring evidence.

## Must-Not-Fail Gates

- Do not inherit old conclusions after `从0`, `全部作废`, or `不继承旧结论`.
- Do not mix books/modules when the user narrows scope.
- Do not call ordinary reference answers scoring rubrics unless the user confirms.
- Do not leave PDF, Word, PPT, image, scan, table, or comic sources unprocessed because one tool failed.
- Do not let student-facing artifacts contain paths, debug notes, audit statuses, `评标`, `参考答案`, `可从...角度作答`, `pass`, `filled`, or pipeline field names as teaching content.
- Do not treat a generated `.docx` as final before rendered visual QA and Word validation when available.
- Do not hand-edit final Word styling repeatedly when a deterministic Markdown normalization, OOXML post-process, or Word automation script can do the same check safely.
- Do not let Codex become only a dispatcher or monitor. Unless the user explicitly asks for supervision only, Codex must run its own source/evidence/content lane and leave auditable outputs under `codex_lane/`.
- Do not let ClaudeCode become only a challenge reviewer. In the four-lane final workflow it is a second production workhorse and must leave auditable outputs under `claudecode_lane/`.
- Do not let Claude Opus rewrite outside the evidence-locked pack. If it adds terms, examples, or claims, route them back to Codex/ClaudeCode source verification before inclusion.
- Do not let GPT-5.5 Pro or Claude Opus advisor/text-review delays, web pauses, or another stopped thread halt safe local evidence work. However, delay or failure does not satisfy the lane: record `blocked_advisor` / `real_call_pending`, proceed only with local work that does not require that advice, and block phase promotion, final framework acceptance, content-review PASS, and final delivery PASS until the real call succeeds or the user explicitly waives that exact gate.
- Do not create a new "GPT假闭环": phase reports must contain gaps and risks, GPT advice must be digested into local tasks, and fallback phases must receive a late review before final promotion.
- Do not treat a student-facing artifact as final until GPT-5.5 Pro has reviewed its concrete content and Codex has evidence-verified the correction log under Governor G11. A raw review plus a filled log is not enough: accepted issues need patched and verified-closed status, rejected issues need local evidence reasons, deferred issues need user-decision routing, and Markdown PASS cannot substitute for Word/PDF PASS.
- Do not accept final content before Confucius proves artifact-only learning transfer.
- Do not repeat the same failed tool action three times. Log every error, mutate the approach, and escalate source-boundary blockers to the user.
- Do not dispatch multiple agents unless their scopes are independent and write sets are separated.

## Reference Files

- `references/whole-book-sop.md`: concrete SOP for the user's desired "pick a book, explain the framework, sleep, wake up to final document" workflow; includes sleep-start questions, numbered run layout, role boundaries, advisor context packs, Claude Code prompt rules, three modes, and failure gates.
- `references/run-protocol.md`: full workflow details and phase gates.
- `references/external-workflow-patterns.md`: selected rules absorbed from planning-with-files and Superpowers, plus explicit rules not adopted.
- `references/cross-model-invocation.md`: tested Claude Code and Codex/GPT advisor invocation commands and caveats.
- `references/document-pipeline.md`: simpler Markdown-to-Word workflow, local tool findings, and repeatable checks for page numbers, TOC, figures, watermarks, and choice-option formatting.
- `references/role-prompt-templates.md`: prompts for Codex, ClaudeCode, Claude Opus teaching-text lane, GPT advisor/content reviewer, Governor, and Confucius.
- `references/control-files.md`: required files, fields, and status values.
- `references/confucius-acceptance.md`: harsh zero-baseline review and three-layer learning exam.
