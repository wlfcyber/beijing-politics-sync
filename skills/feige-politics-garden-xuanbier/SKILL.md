---
name: feige-politics-garden-xuanbier
description: "Use when Codex needs 飞哥政治庄园-选必二 for 选择性必修二《法律与生活》, especially rebuilding from scratch, legal-question preprocessing, matching each legal question with its rubric, choice-question legal-basic-knowledge summaries, and main-question question/rubric source packs."
---

# 飞哥政治庄园-选必二

本分支只服务新选必二线。旧选必二成果已由用户判定作废，不得继承旧结论、旧框架、旧题型、旧清单或旧错肢。

## Load First

Before any 选必二 work, pass the project three-layer SOP by reading `reports/master_governor/latest_master_governor_report.md`, `reports/master_governor/worker_daily_orders.md`, and the shared SOP at `../feige-politics-garden/references/project-governor-three-layer-sop.md`. Then read the active notebook:

- `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/00_飞哥选必二法律与生活要求小本本.md`

If that file does not exist, create it from the user's current requirements before doing any research.

If the master governor marks this lane stale, missing governor/coverage, or possible false closure, repair the run control layer before content work. If the lane is absent from the report, register the run and refresh the report.

Do not read old `选必二_*.md` files as evidence or conclusions. If old files still exist, treat them as contamination to delete or ignore.

## Current Goal

The current phase is preprocessing only:

- do not decide the final framework;
- do not classify into mother-question templates;
- do not write classroom full drafts;
- find every stable 选必二《法律与生活》 question from the original three-year district papers;
- match each main question with its corresponding rubric/scoring source;
- write choice questions in a student-facing legal-basic-knowledge format.

## Framework Phase Real-Call Rule

When the user explicitly releases 选必二 from preprocessing into framework generation, whole-book synthesis, classroom compression, or final document production, the four-lane Garden rule applies with a stricter model boundary:

- GPT-5.5 Pro and Claude Opus 4.7 Adaptive must be truly called as those external/model lanes for framework design, framework pressure testing, teaching-text shaping, or final content review.
- Do not use Codex subagents, local simulations, generic advisor reports, or Codex-written "as-if GPT/Claude" notes as substitutes for GPT-5.5 Pro or Claude Opus 4.7 Adaptive.
- Codex subagents may only prepare context packs, evidence summaries, local prechecks, and questions for the real GPT/Claude calls.
- For this 选必二 lane, when the user says `GPT-5.5 Pro` and `Claude Opus 4.7 Adaptive Thinking`, prefer fresh user-visible web/app conversations with those exact modes selected or clearly confirmed. CLI/API calls, including `codex exec -m gpt-5.5` or `claude -p --model opus`, do not satisfy the official framework gate unless the user explicitly waives the web-visible mode requirement; record them only as `cli_provisional_advice`.
- If the real call is unavailable or not yet completed, mark the phase `blocked_advisor` or `real_call_pending`; local evidence preprocessing and source verification may continue, but framework定稿、学生版成品化、Governor PASS、Confucius closure, and final delivery PASS are blocked unless the user explicitly waives the real-call gate for that exact phase.

## Framework Self-Evolution Rule

When 选必二 enters framework generation, do not use a one-shot outline. Use a recurring framework council with real GPT-5.5 Pro and real Claude Opus 4.7 Adaptive:

1. Codex builds a local evidence pack from the current batch: question cards, scoring/rubric excerpts summarized by source id, frequency counts, hard-to-place cases, and current framework version.
2. GPT-5.5 Pro independently proposes or revises the framework for high-frequency trunk, full coverage, risk areas, and version-change criteria.
3. Claude Opus 4.7 Adaptive independently proposes or revises the framework for learnability, student-facing structure, transfer language, and over-abstract-node risks.
4. Codex sends GPT's raw proposal to Claude Opus and Claude's raw proposal to GPT for cross-critique. The two real models must each respond to the other's structure, not merely produce isolated comments.
5. Codex prepares a convergence brief: agreements, conflicts, suggested node additions/deletions/renames, evidence required, and student-facing risks.
6. Codex performs local evidence裁决. A framework change is accepted only if it improves at least one of: high-frequency trunk clarity, all-question coverage, placement of previously hard cases, student transfer, or evidence hygiene.
7. Every accepted change creates a new framework version. Every rejected or deferred suggestion remains in the model-advice log with the local evidence reason.

Framework self-evolution gates:

- No framework version can be promoted without: local batch evidence, GPT real-call proposal, Claude real-call proposal, cross-critique from both, Codex evidence裁决, and a coverage/gap delta.
- If GPT and Claude agree but local evidence disagrees, local evidence wins and the agreement is rejected with reasons.
- If local evidence supports a change but GPT or Claude is unavailable, keep the change as `candidate_pending_real_call`, not accepted.
- The framework must keep two layers: `主干高频层` for what students must know first, and `开放容器层` for low-frequency/new-case accommodation. Do not flatten everything into one big list.

## Proposition Path Rule

For 选必二 frameworking, every question must be analyzed through the proposition-maker's path before framework placement:

- What law-governance thinking or student capability is the question trying to cultivate?
- Why did the proposition choose this carrier: case, legal provision, legal phenomenon, or social-governance scene?
- What is the question path: front-to-back, general-to-specific, fact-to-rule, rule-to-value, dispute-to-social-meaning, or another route?
- What answer action does the rubric reward: legal relationship judgment, dispute identification, element matching, responsibility/effect/procedure landing, or rule-of-law value explanation?
- Does this path reinforce the high-frequency trunk, expose a new open container, or reveal a framework gap?

The user's authoritative legal-proposition image must be treated as a framework-design reference for this rule. Its key warning is that legal-module questions balance legal knowledge, legal reasoning, political/value orientation, practical governance, and student subjectivity. Do not reduce the framework to either legal-detail memorization or broad rule-of-law value slogans. If the proposition path is unclear, mark `proposition_path_uncertain` instead of forcing placement.

## Source Roots

Use original source directories:

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`

Use only as supplementary evidence when necessary:

- `/Users/wanglifei/GaokaoPolitics/2025各区模拟题`
- Notability exports under `/Users/wanglifei/Library/Mobile Documents/ZP9ZJ4EF3S~com~gingerlabs~Notability/Documents`

## Active Output Directory

Use:

- `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/`

Required outputs:

- `00_飞哥选必二法律与生活要求小本本.md`
- `TASK_BRIEF.md`
- `DEVELOPMENT_PLAN.md`
- `PROGRESS.md`
- `LEGAL_QUESTION_INDEX.csv`
- `SOURCE_MATCH_LEDGER.csv`
- `CHOICE_PREPROCESS.md`
- `CHOICE_PREPROCESS.csv`
- `SUBJECTIVE_PREPROCESS.md`
- `SUBJECTIVE_PREPROCESS.csv`
- `NO_XUANBIER_SUITES.md`
- `MISSING_OR_UNCERTAIN.md`

## Preprocessing Rules

- If a midterm or other suite clearly contains no 选必二, mark it `no_xuanbier` and skip it.
- Do not force a suite into 选必二 because of stray words like `法律`, `权利`, or `规则`.
- `2026石景山期末` remains excluded unless the user provides a new usable scoring source.
- Classification compilations are location aids only; they are not independent suites and must not be double counted.
- Ordinary reference answers are not formal rubrics.
- Scan-only or text-empty files must be marked as OCR/conversion gaps if they cannot be read; do not pretend they contain no 选必二.

## Choice Question Output

Use a two-layer structure:

1. One overview sentence per question:
   - must include basic scenario, correct legal judgment, what is wrong, and why it is wrong.
2. One sentence per wrong option:
   - `<option> 不对在 <mistake>, 因为 <legal rule / fact boundary>.`

The purpose is to let students learn basic legal knowledge from the document.

## Main Question Output

For main questions, only prepare an analysis-ready source pack:

- full material/question text;
- complete prompt;
- matching rubric/scoring source original text;
- source file and position;
- evidence type;
- notes about OCR, missing rubric, or uncertain module boundary.

Do not backfill a framework, summarize mother-question patterns, or write classroom templates in this phase.

## Acceptance

- Every suite scanned has status `has_xuanbier`, `no_xuanbier`, or `uncertain`.
- Every main-question candidate has status `matched`, `missing`, `uncertain`, or `excluded`.
- Every processed choice question has overview sentence and wrong-option sentences.
- New outputs do not cite old `选必二_*.md` conclusions.
- Progress is updated only after the corresponding output exists.
