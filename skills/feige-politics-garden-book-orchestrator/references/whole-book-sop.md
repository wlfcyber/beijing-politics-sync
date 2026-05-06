# Whole-Book AI Teaching SOP

Use this SOP when the user starts a whole-book or whole-module Beijing Gaokao politics run through `飞哥政治庄园`, especially before an overnight run.

## Operating Principle

Default every substantial whole-book/module run to the four-lane final workflow. Codex is the local controller, local evidence judge, production lane A, final fusion owner, and delivery generator. ClaudeCode is production lane B, an independent full-source workhorse that hunts omissions and produces auditable matrices, entries, blockers, and suite reports. Claude Opus 4.7 Adaptive is the teaching-text output lane that turns evidence-locked material into readable, transferable student-facing prose. GPT-5.5 Pro is the chief content reviewer and pressure tester. Governor blocks false completion. Confucius validates whether the final student artifact can teach transfer from zero. Facts are decided by local source evidence, not by model confidence.

## GPT-5.5 Pro Strategic Commander Mode

Default relationship after the four-lane workflow decision:

```text
Codex 20x: local controller, local evidence judge, production lane A, final fusion and delivery
ClaudeCode 20x: production lane B, independent full-source rerun and omission hunter
Claude Opus 4.7 Adaptive: teaching-text output lane and student-readability editor
GPT-5.5 Pro: strategic commander, chief content reviewer, and pressure tester
Governor: hard gatekeeper
Confucius: zero-baseline student verifier
```

Use GPT-5.5 Pro for:

- Overall run design, stage sequencing, division-of-labor suggestions, risk lists, and acceptance criteria.
- Detecting likely false closure, missing framework areas, weak student transfer chains, and bad document structure.
- Producing a "commander recommendation packet" for Codex local supervisor.

Do not use GPT-5.5 Pro for:

- Direct local evidence decisions.
- Direct file/source/rubric claims.
- Direct orders to ClaudeCode, Claude Opus, or local workers.
- Reading local paths or unsanitized source files unless the user explicitly approves that exact data and destination.

Required conversion step:

```text
GPT-5.5 Pro recommendation
  -> Codex local digestion
  -> local task in MODEL_ADVICE_LOG.md / DECISION_LOG.md
  -> direct worker prompt with MASTER_REQUIREMENTS, notebook, source scope, tools, write scope, and acceptance criteria
  -> local evidence verification
  -> possible student artifact inclusion
```

If GPT-5.5 Pro disagrees with Codex, Claude Opus, or ClaudeCode, resolve by reopening local source evidence and applying the user's framework. Never resolve by model prestige.

## Four-Lane Final Workflow

Use this for all substantial 飞哥政治庄园 work unless the user explicitly narrows the task to a small single-lane job.

```text
Codex production lane A + ClaudeCode production lane B
  -> Codex local source/evidence fusion and conflict裁决
  -> Claude Opus 4.7 teaching-text成品化
  -> GPT-5.5 Pro content review / pressure test
  -> Codex evidence-verified patching
  -> Governor
  -> Confucius artifact-only learning verification
  -> Markdown / DOCX / PDF / acceptance report delivery
```

Rules:

- Codex and ClaudeCode both do real work. Codex cannot be only a monitor; ClaudeCode cannot be only a challenger. Both must leave file-backed, auditable outputs.
- Codex owns final evidence and final fusion. Agreement between Codex and ClaudeCode raises confidence but never replaces local source evidence.
- Claude Opus receives an evidence-locked pack, not raw authority. Its job is to make the content teachable: structure, transitions, answer language, transfer chains, and zero-baseline readability.
- GPT-5.5 Pro reviews concrete generated content and pressure-tests omissions, conceptual mistakes, unsupported answer landings, and weak student transfer. GPT does not decide source facts.
- Any new term, correction, deletion, or conceptual claim from Claude Opus or GPT must return to Codex local evidence verification before inclusion.
- The standard folders for a full run should include or map to: `codex_lane/`, `claudecode_lane/`, `fusion/`, `opus_writer/`, `gpt55_review/`, `governor_confucius/`, and `09_delivery/`.

## Phase Boundary GPT Commander Gate

Run this gate after every meaningful phase, suite batch, fusion pass, document pass, or verification loop. The user wants GPT-5.5 Pro to command from above after each stage, but Codex must keep local evidence control.

1. Write `08_review/phase_reports/phase_XX_summary.md` before contacting GPT. A phase report is invalid unless it includes the required field set below. If the report is thin or only says good news, do not request GPT commander advice yet; improve the report first.
2. Sanitize the report before sending it out: no accounts, secrets, local absolute paths, environment details, large raw exam passages, large raw scoring-rule passages, private drafts, or unverified source claims.
3. Send the sanitized phase report to GPT-5.5 Pro when the web Pro route or a GPT advisor route is available. Ask for a commander packet: next priority, Codex production assignment, ClaudeCode production assignment, Claude Opus teaching-text task, reviewer tasks, risks, stop/go judgment, and exact local checks before promotion.
4. Save the raw GPT answer under `08_review/gpt_phase_advice/phase_XX_gpt.md` and, when using the older compatibility layout, also under `advisor_reports/`.
5. Write Codex's digestion in `08_review/codex_response_to_advice.md` and `00_control/MODEL_ADVICE_LOG.md`: accepted suggestions, rejected suggestions, local evidence checks required, worker prompts to issue, and items deferred to the user.
6. Continue only from Codex-owned local tasks. Never paste GPT's raw commander packet into ClaudeCode or Claude Opus as higher authority.

Required phase report fields:

```text
phase_name
phase_goal
completed_actions
unfinished_actions
changed_artifacts
source_coverage_summary
non_text_material_summary
evidence_level_counts_P0_P1_P2_P3_P4
missing_suites_questions_or_file_types
codex_vs_claudecode_differences
conflict_summary
blockers
governor_gate_status
three_uncertainties
most_likely_missing_material_types
most_likely_evidence_level_mislabels
most_likely_student_misleading_phrases
do_not_enter_student_doc_list
questions_for_gpt_commander
candidate_next_tasks
```

The sanitized version sent to GPT may replace local filenames with stable `source_id`, year, district/exam type, file type, question type, evidence level, processing status, non-text flags, and blocker status. Do not remove those structural fields so aggressively that GPT can only give generic advice.

Required Codex digestion fields for each GPT suggestion:

```text
suggestion_id
raw_gpt_suggestion_summary
decision: accepted / partially_accepted / rejected / deferred
reason
local_task_created
local_evidence_to_check
execution_status
affects_student_doc: yes / no
follow_up_phase
```

GPT advice automatically expires and must be re-requested if local evidence scope changes, the user framework changes, a P0/P1 evidence-level error is found, a large missing-question block is discovered, non-text materials were skipped, a run changes from continuation to zero-start, or Claude Code conflicts with Codex at large scale.

Fallback rule:

- If GPT-5.5 Pro, the web page, browser automation, or another advisor thread stalls, stops, or is unavailable, write `08_review/gpt_phase_fallback_log.md` with time, phase, symptom, last successful advisor checkpoint, and Codex fallback decision.
- Do not let the full run stop solely because GPT did not answer. Continue under `MASTER_REQUIREMENTS.md`, the branch skill, local source evidence, Governor checks, and Confucius. Retry GPT at the next phase boundary.
- When GPT returns after a fallback, run a late review of the fallback phase. If it finds a meaningful gap, open a返修 task before promotion.
- If the user explicitly says a phase cannot proceed without GPT approval, then mark the phase `blocked_user` or `blocked_advisor` and surface the exact blocker.

## GPT-5.5 Pro Content Review And Correction Gate

Run this gate after every completed student-facing deliverable, chapter, section batch, mini-card, final Markdown draft, and Word/PDF text extraction. The user has explicitly asked for GPT-5.5 Pro to check and修正 the concrete content, and is willing to wait overnight.

Fixed trigger objects:

- `outline`: whole-book table of contents, chapter structure, and four-lane master frame.
- `section_batch`: every chapter/section draft, especially high-frequency test units, choice-question logic, graph/cartoon/table methods, legal case units, and philosophy method units.
- `final_markdown`: the final student-facing Markdown, checked for content, structure, transfer chains, and audit residue.
- `word_pdf`: Word/PDF text extraction plus visual QA notes, checked separately for table of contents, page numbers, images, cartoons, tables, option line breaks, heading hierarchy, readability, and student handoff risk.

Skipping any fixed trigger object requires a logged fallback or explicit user waiver. A skipped trigger without fallback/waiver fails Governor G11.

What may be sent:

- Generated student-facing content: outline, chapter text, trigger chains, answer-landing templates, choice-question explanations, examples, review cards, and final draft chunks.
- Necessary review context: book/scope, user framework, target student, evidence-level summary, source ids, year/district/exam type, question type, and blocker status.
- Local evidence summaries written by Codex, as long as they are not large raw exam/scoring passages.

What must not be sent:

- Accounts, secrets, credentials, local absolute paths, private machine details, raw logs, or unsent third-party drafts.
- Large raw exam passages, large raw scoring-rule passages, or full source files.
- Anything that would turn GPT into the evidence authority. GPT reviews the generated artifact; Codex checks facts locally.

Chunking rule:

- If an artifact is long, split by chapter or section. Each chunk must include its heading path and the local evidence/fusion status summary.
- Do not rely on one global summary when the user asked for concrete content review. GPT must see the actual generated content that a student would read.

Ask GPT-5.5 Pro to check:

```text
1. conceptual mistake or overgeneralization
2. missing material trigger
3. unsupported answer landing
4. weak "why this principle/term" bridge
5. content that may mislead a zero-baseline student
6. wrong or incomplete choice-question logic
7. missing graph/cartoon/table handling method
8. contradictions across sections
9. places where the example does not prove the method
10. concrete revised wording or structure
```

Save and digest:

- Save raw GPT content review under `08_review/gpt_content_review/content_review_XX_gpt.md`.
- Record every issue in `08_review/gpt_content_review/content_correction_log.md` with: issue id, artifact, location, severity, GPT claim, proposed correction, local evidence check needed, local evidence check result, Codex decision, patch status, whether it affects the student document, and verified-closed time.
- Severity values: `must_fix_content`, `should_fix_transfer`, `style_or_readability`, `rejected_no_evidence`, `deferred_user`.
- Any substantive correction must be checked against local source evidence, branch skill rules, the user's framework, and Claude Code/Codex lane conflict records before patching.

G11 PASS conditions:

- `outline` reviewed by GPT-5.5 Pro or covered by a logged fallback/waiver.
- `section_batch` chunks reviewed by GPT-5.5 Pro or covered by a logged fallback/waiver.
- `final_markdown` reviewed by GPT-5.5 Pro.
- `word_pdf` reviewed separately from Markdown after Word/PDF production or text extraction.
- Raw GPT review files saved and linked from the review index.
- `content_correction_log.md` has complete fields for every issue.
- No unresolved `must_fix_content`.
- No unresolved `should_fix_transfer` that blocks student transfer.
- Every accepted or partially accepted issue has `patch_status = verified_closed`.
- Every rejected issue has a local evidence check result explaining rejection.
- Every deferred issue is on the user-decision list before final delivery.

Iteration rule:

- In overnight mode, repeat GPT content review after corrections until there are no unresolved `must_fix_content` issues and no unresolved `should_fix_transfer` issues that would stop student transfer.
- GPT delay may not stop local evidence work, but final PASS is blocked until GPT content review is completed or the user explicitly disables it.
- If GPT content advice contradicts local evidence, reject it, log why, and keep the evidence-backed text.
- Markdown PASS and Word/PDF PASS are separate. Markdown PASS means content, structure, transfer chains, and audit residue passed. Word/PDF PASS means the delivered document's table of contents, page numbers, images, cartoons, tables, choice-option layout, heading hierarchy, and visual readability passed. Never let Markdown PASS substitute for Word/PDF PASS.

## Sleep Start Card

Before the user leaves, collect only what is needed to avoid a wrong run:

1. Book/module: 必修四, 选必一, 选必二, 选必三, or a narrowed topic.
2. Exact scope: whole book, unit, topic, question type, or named exclusion.
3. Mode: `30分钟小任务`, `半天深跑`, or `整夜终极文档`.
4. Start boundary: `从0开始`, `续跑`, or `旧线作废但可用于定位源材料`.
5. User framework: the user's exam logic, framework nodes, hard samples, and known traps.
6. Source range: default to local 2024-2026 Beijing district papers, answers, scoring rules, marking reports, and lecture materials unless narrowed.
7. Evidence priority: default to scoring/marking rules first; ordinary reference answers are not scoring rubrics unless the user confirms.
8. Deliverables: default to Markdown + Word + acceptance report; overnight mode should also try PDF/rendered visual evidence.

If the user is tired, this is enough:

```text
/飞哥政治庄园 选必二 整本书 整夜 从0开始。
框架：按材料触发点、法律关系、权利义务、争议解决、答案落点来写。
交付：Markdown、Word、PDF、验收报告。
```

## Role Boundaries

`Codex controller`:

- Route to the branch skill and read the local notebook first.
- Create the run folder and control files.
- Maintain progress, source ledgers, coverage, conflicts, advisor logs, and final acceptance.
- Dispatch Codex production lane A and ClaudeCode production lane B with scoped tasks.
- Send only sanitized packs to GPT Pro or Claude Opus.
- Convert advisor suggestions into local tasks before adoption.
- Fuse the lanes, return to local evidence for conflicts, and own the final artifact.

`Codex production lane A`:

- Process local Word/PDF/PPT/image/scan/cartoon/table sources directly.
- Write its own entries, suite reports, coverage, blockers, and student draft.
- Never become only a dispatcher unless the user explicitly asked for supervision only.

`ClaudeCode production lane B`:

- Independently rerun from the same raw local sources and local notebook.
- Do not copy Codex entries.
- Close each suite by question list, evidence, entries, coverage, and suite report.
- Must produce `entries`, `suite_reports`, `coverage`, `missing_blockers`, and suspected conflicts.
- Treat ClaudeCode as a second workhorse production lane, not only a challenge reviewer.

`GPT-5.5 Pro strategic commander / GPT Pro advisor`:

- Review workflow, framework gaps, possible false closure, student transfer gaps, stage priorities, and补跑任务.
- May produce commander-style recommendations for Codex local supervisor.
- Must not decide source facts, scoring levels, or directly command ClaudeCode or Claude Opus.

`GPT-5.5 Pro content reviewer`:

- Review completed student-facing content itself, not only the workflow report.
- Find concrete content issues and propose corrections.
- Must state the local evidence check needed for every substantive correction.
- Must not become the evidence source or final authority.

`Claude Opus 4.7 Adaptive teaching-text lane`:

- Receive only evidence-locked or clearly tagged fusion packs from Codex.
- Rewrite and organize student-facing content for clarity, transfer, classroom usefulness, and answer-sheet fluency.
- Improve section order, headings, examples, trigger chains, and natural Chinese expression.
- Must not add unsupported scoring terms, invent source claims, decide evidence level, or override Codex/ClaudeCode source conflicts.
- Any new conceptual suggestion must be sent back to Codex as a candidate correction requiring local source verification.

`Governor`:

- Enforce gates before promotion or delivery: notebook read, source inventory, non-text processing, evidence levels, coverage, conflict resolution, student artifact cleanliness, Word/PDF visual QA, and Confucius.

`Confucius`:

- Read only the final student artifact.
- Test whether a smart zero-baseline student can identify material triggers, choose the correct principle/term, and write answer landings.
- A Confucius fail sends the work back to drafting or evidence fusion.

## Standard Run Directory

Prefer a dedicated folder under `/Users/wanglifei/Desktop/北京高考政治`. A full run should create this structure or an equivalent one:

```text
00_control/
  RUN_MANIFEST.yaml
  START_CARD.md
  ZERO_START_DECLARATION.md
  MASTER_REQUIREMENTS.md
  NOTEBOOK_DIGEST.md
  EVIDENCE_PRIORITY_RULES.md
  PROGRESS_LEDGER.jsonl
  GOVERNOR_GATES.md
  MODEL_ADVICE_LOG.md
  DECISION_LOG.md
01_source_inventory/
  SOURCE_INVENTORY.csv
  FILE_TYPE_ROUTING.csv
  SOURCE_DEDUP_REPORT.md
02_extraction/
  codex_extraction_logs/
  claudecode_extraction_logs/
  screenshots/
  ocr_outputs/
  ppt_outputs/
  table_outputs/
  failed_extractions.md
03_entries/
  codex_entries.jsonl
  claudecode_entries.jsonl
  merged_entries.jsonl
  evidence_level_index.csv
04_suite_reports/
  codex_suite_reports/
  claudecode_suite_reports/
  merged_suite_reports/
  suite_completion_matrix.csv
05_coverage/
  coverage_by_book_unit.csv
  coverage_by_question_type.csv
  coverage_by_year_district_exam.csv
  missing_questions.md
  unresolved_blockers.md
06_conflicts/
  conflict_register.md
  resolved_conflicts.md
  unresolved_conflicts.md
07_student_doc/
  student_doc_outline.md
  student_doc_draft.md
  student_doc_final.md
  figures/
  tables/
08_review/
  phase_reports/
    phase_report_template.md
    phase_XX_summary.md
  gpt_phase_advice/
    gpt_phase_advice_index.md
    phase_XX_gpt.md
  gpt_content_review/
    content_review_template.md
    gpt_content_review_index.md
    content_review_XX_gpt.md
    content_correction_log.md
  gpt_context_pack.md
  gpt_advice.md
  gpt_phase_fallback_log.md
  claude_context_pack.md
  claude_advice.md
  codex_response_to_advice.md
  confucius_report.md
  confucius_fix_log.md
09_delivery/
  final_student_document.md
  final_student_document.docx
  final_student_document.pdf
  word_visual_check.md
  pdf_visual_check.md
  acceptance_report.md
  delivery_manifest.md
```

The older root-level control files (`MASTER_REQUIREMENTS.md`, `SOURCE_LEDGER.csv`, `COVERAGE_MATRIX.csv`, `FINAL_ACCEPTANCE_REPORT.md`) may still be created for compatibility, but the numbered folders are preferred for full-book runs.

## Evidence Levels

- `P0`: formal scoring rubrics, marking rules, marking reports, or lecture/report fragments that explicitly state marking standards.
- `P1`: official or school/district reference answers and "答案及评分参考". Do not call P1 a scoring rubric unless the user confirms.
- `P2`: lecture slides, teacher explanations, test analysis, and teaching materials.
- `P3`: paper text, question materials, options, charts, cartoons, and tables.
- `P4`: AI summaries, advisor suggestions, and working drafts. P4 never proves facts.

## Advisor Context Packs

Allowed for GPT Pro/Claude:

- Goal, book, scope, mode, and final artifact target.
- User framework and hard-rule notebook digest.
- Source and coverage statistics.
- Sanitized entry samples: material trigger, question type, knowledge node, answer landing.
- Student draft excerpts and explicit review questions.

Forbidden for GPT Pro/Claude:

- Accounts, secrets, environment variables, local absolute paths, or machine details.
- Unsanitized source filenames where avoidable.
- Long raw exam passages or long raw scoring-rule passages.
- Unverified local conclusions.
- Requests to decide local evidence, source identity, or scoring level.

Every advisor suggestion must be logged with: source, suggestion, adoption decision, local task, local evidence result, and whether it enters the student artifact.

## Claude Code Prompt Rules

Every Claude Code instruction must include:

- RUN ID, book/scope/mode, start boundary, branch skill, notebook, `MASTER_REQUIREMENTS`, source range, evidence hierarchy, and output paths.
- A direct instruction to rerun from local sources, not from Codex entries.
- A requirement for `entries`, `suite_reports`, `coverage`, `missing_blockers`, and suspected conflicts.
- A requirement to process or explicitly block PDF, Word, PPT, image, scan, cartoon, and table sources.
- A ban on calling ordinary reference answers scoring rubrics.
- A ban on declaring completion without compatible entries, suite reports, and coverage.

If Claude Code stalls, asks broad confirmation, drifts scope, skips non-text sources, or reports completion without matrices, the controller must correct or restart it.

## Conflict Resolution

Classify conflicts as source extraction, evidence level, knowledge/framework placement, answer landing, student wording, or coverage.

Resolution order:

1. Reopen the local source: paper, answer, rubric, lecture, rendered page, OCR output, screenshot, image, table.
2. Apply evidence hierarchy: P0 > P1 > P2 > P3; P4 cannot decide facts.
3. Apply the user's framework only after the source fact is settled.
4. Re-extract visual/non-text materials when conflict depends on layout, image, cartoon, or table content.
5. Record the decision in `conflict_register.md`.
6. Keep conflict traces out of the student document.

Unresolved core conflicts block final PASS. Minor unresolved examples may be excluded while preserving the method.

## Student Artifact Contract

The student artifact must teach:

```text
材料触发点 -> 为什么想到 -> 答案落点
```

It must not expose paths, debug text, source ids, entries, coverage, confidence, blockers, scoring-rubric labels, pipeline fields, or advisor chatter.

Final Markdown requirements:

- Clear heading hierarchy.
- Images and cartoons preserved via `figures/`.
- Tables usable in Word.
- Choice options complete and readable.
- No unverified local fact.

Final Word/PDF requirements:

- Native clickable TOC when requested.
- Page numbers.
- Images/cartoons/tables not lost or distorted.
- Choice options consistently split.
- Chinese quotes normalized to `“”`.
- Title/body/table styles visually checked.
- Watermark only when requested and verified not to harm reading.
- PDF exported from the validated Word when practical.

## Three Modes

`30分钟小任务`:

- One unit, topic, question type, or 3-5 representative suites.
- Codex production first; Claude Code can sample-rerun.
- Deliver `mini_student_card.md`, mini coverage, blockers, and next-step advice.
- Never claim whole-book exhaustion.

`半天深跑`:

- One large module, several units, or core book slice.
- Codex runs the whole scoped slice; Claude Code independently reruns core suites.
- Add GPT review and Claude Opus teaching-text review if useful.
- Deliver stage Markdown/Word, coverage, conflict register, and stage acceptance.

`整夜终极文档`:

- Full source inventory, file-type routing, dual production, coverage/conflict fusion, advisor review, student final draft, Word/PDF production, Confucius, and final acceptance.
- Must leave status for every blocker and conflict.
- Must pass visual QA and Confucius or record返修 loops before final delivery.

## Ten Failure Rules

1. No `NOTEBOOK_DIGEST.md`, no production.
2. Reference answers default to P1, not P0.
3. `从0开始` requires `ZERO_START_DECLARATION.md`; old artifacts locate sources only.
4. Every non-text source needs a method or blocker.
5. Every suite report must list original and processed question numbers.
6. Claude Code natural-language completion without entries/suite reports/coverage is invalid.
7. Advisor suggestions require local tasks before adoption.
8. Student document must not become an audit report.
9. No Word/PDF delivery without visual checks.
10. No conflict is decided by model prestige; reopen local evidence.
