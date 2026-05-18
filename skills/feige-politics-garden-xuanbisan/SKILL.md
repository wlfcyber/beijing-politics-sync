---
name: feige-politics-garden-xuanbisan
description: "Use when Codex needs 飞哥政治庄园-选必三 for 选择性必修三《逻辑与思维》思维部分 Beijing district-paper work: source inventory, evidence grading, material-to-thinking trigger chains, scientific/dialectical/innovative thinking methods, thinking-abstraction choice traps, zero-baseline classroom templates, and full-suite exhaustion."
---

# 飞哥政治庄园-选必三

This branch handles 选择性必修三《逻辑与思维》的思维部分. Its output is not a concept glossary. It is a source-grounded, trigger-chain driven, classroom-ready system that teaches students how to move from material actions to thinking methods and answer sentences.

If the final artifact is `.docx`, also use the `documents` skill and render every DOCX before delivery.

## 2026-05-06 Production Stance

For full 选必三 book/module runs, follow the successful 必修四哲学宝典 production pattern:

- ClaudeCode must be the thick-content mining lane first, not a lightweight reviewer. In the 2026-05-02 philosophy run, ClaudeCode's source-backed body was materially fuller than Codex's thin candidate; the final accepted artifact depended on importing and replacing many Codex rows with ClaudeCode rows.
- Codex must still run its own production lane, but its main responsibility is total control, evidence judgment, framework normalization, conflict resolution, student/audit cleanup, external-review digestion, Governor/Confucius gates, and Word/PDF validation.
- Do not let Codex's thinner candidate become the main student body merely because it is cleaner or easier to format. If ClaudeCode produces source-backed fuller entries, fusion should preserve that content density unless local evidence or the user's framework rejects it.
- For 选必三 specifically, the final body must be framework-first: `思维类型 -> 三性/三新/子方法 -> 对应模拟题` for 思维部分, and `推理题型树 -> 全部对应题` for 推理部分. Paper-order or district-order bodies are audit tools, not the final student-book structure.
- Before Word/PDF, run a ClaudeCode-thick-content gate: every evidence/control row is body/index/blocked, every core framework node has real question挂载 or a blocker, choice questions have full options, reasoning questions have logical forms, and the body is not a small representative packet.
- Supervise ClaudeCode by file evidence, not chat impressions. It should close work suite-by-suite, not as one vague whole-book pass: each suite needs entries, a suite report, coverage rows, progress updates, and blockers before it is treated as done. Heartbeat checks must inspect logs plus `PROGRESS`, `DECISION_LOG`, ledgers, coverage, `suite_reports/`, `audit/entries/`, and outputs; if any disagree, issue a supervisor patch and block final wording.

## Load First

Before any 选必三 work, pass the project three-layer SOP by reading `reports/master_governor/latest_master_governor_report.md`, `reports/master_governor/worker_daily_orders.md`, and the shared SOP at `../feige-politics-garden/references/project-governor-three-layer-sop.md`. Then read:

- `references/xuanbisan-hard-rules-notebook.md`: hard requirements distilled from the user's 必修四, 选必一, 选必二, and 选必三 correction history.
- `reports/master_governor/CROSS_BOOK_WORKFLOW_V3_FOR_XUANBIER_XUANBISAN.md`: cross-book preflight, evidence ledger, model authority chain, ClaudeCode model lock, anti-merge rule, final-claim audit, and GitHub sync rule.

If the master governor report is missing or stale, refresh it before worker execution. Oversized logs, ledgers, and candidate CSV/JSON files must be opened through `context_compression_manifest.csv` and context capsules first, then the original file only for exact evidence.

Then inspect current workspace artifacts, if present:

- `/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_框架+三年题链_穷尽版.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_逐题材料-思维路径积累_穷尽版.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_零基础满分课稿.md`
- `/Users/wanglifei/Desktop/北京高考政治/codex_continuous/jobs/选必三_思维触发穷尽/TASK_BRIEF.md`
- `/Users/wanglifei/Desktop/北京高考政治/codex_continuous/jobs/选必三_思维触发穷尽/DEVELOPMENT_PLAN.md`
- `/Users/wanglifei/Desktop/北京高考政治/codex_continuous/jobs/选必三_思维触发穷尽/PROGRESS.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/governor_board.md`

Treat existing 选必三 artifacts as verified experience and an index, not as proof for new work. When a suite is newly processed or disputed, return to the paper, answer source, rubric, marking report, evaluation/讲评 material, page render, or OCR evidence.

## Core Goal

Build a student-facing, zero-baseline full-mark system for 选必三《逻辑与思维》思维部分:

- exhaust all accessible Beijing district questions that test thinking methods;
- separate main-question scoring chains from choice-question thinking signals;
- classify every candidate as `A-formal`, `A-support`, `B-choice-signal`, `C-boundary`, or `missing`;
- convert every usable point into the fixed chain `材料动作 -> 总帽子 -> 小方法 -> 触发逻辑 -> 答案句`;
- preserve module boundaries so pure formal-logic questions and other-book questions do not enter the thought-method main chain;
- compress results into classroom language that weak students can transfer to fresh questions.

## Source Roots

Use the local Mac paths unless the user gives newer paths:

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`
- `/Users/wanglifei/GaokaoPolitics/2025各区模拟题`
- `/Users/wanglifei/Library/Mobile Documents/ZP9ZJ4EF3S~com~gingerlabs~Notability/Documents`
- `/Users/wanglifei/Desktop/北京高考政治`

Run-time date matters. Do not permanently reuse old statements such as "2026二模尚未开考". At the start of each full run, rescan the source roots; if 2026二模 materials exist, classify them under the same evidence rules. If no source is found, record `missing` with the exact scan boundary.

## Evidence Levels

Every row must carry one evidence level:

- `A-formal`: formal scoring rubric, marking rule, evaluation/阅卷/评标 report, or explicit scoring source matched to the suite and question.
- `A-support`: lecture or讲评 material with explicit scoring口径 and a matching question, but not a formal rubric. Use as support and label it.
- `B-choice-signal`: choice question with paper text plus a reliable objective answer key; usable for stable thinking-signal and trap extraction, not as a main-question scoring chain.
- `C-boundary`: source exists, but it is pure formal logic, pure reasoning-rule recognition, 必修四 philosophy, 选必一, 选必二, or another comprehensive-module task rather than 选必三思维部分.
- `missing`: question number, paper text, answer key, scoring source, OCR, or module boundary is not reliable enough.

Never invent rubrics. Never promote ordinary reference answers into `A-formal`.

Special exclusion:

- `2026石景山期末`: the user previously confirmed no usable scoring rubric. Exclude it for all books/modules unless the user explicitly provides a new scoring source.

## Required Run Files

For a full or long-running 选必三 pass, create or reuse a visible run directory such as:

- `/Users/wanglifei/Desktop/北京高考政治/选必三思维研究_YYYY-MM-DD/`

Maintain these files:

- `00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `TASK_BRIEF.md`
- `DEVELOPMENT_PLAN.md`
- `PROGRESS.md`
- `SOURCE_LEDGER.csv`
- `QUESTION_COVERAGE_MATRIX.csv`
- `MAIN_THINKING_LEDGER.csv`
- `CHOICE_TRAP_LEDGER.csv`
- `FRAMEWORK_TRIGGER_BACKFILL.md`
- `CLASSROOM_DRAFT.md`
- `PATCH_REVIEW.md`
- `GOVERNOR_CHECKLIST.md`
- `FINAL_ACCEPTANCE_REPORT.md`

Do not mark a step complete until real output exists and the corresponding ledger rows are updated.

## Programmed Workflow

### 0. Hard-Rule Intake

Tool action:

- Read `references/xuanbisan-hard-rules-notebook.md`.
- Read the current run's `00_飞哥选必三逻辑与思维硬性要求记事本.md` if it exists.
- When migrating rules from other branches, read only the relevant hard-rule files, especially 必修四 trigger standards, 选必一 term protocol, and 选必二 hard-rule notebook.

Thinking action:

- Convert every user correction into a checkable rule.
- If a new rule conflicts with old output, patch output and record the audit note. Do not silently overwrite or forget older rules.

Output:

- A `DECISION_LOG` or `PROGRESS` note naming the active hard rules for the round.

### 1. Source Inventory

Tool action:

- Use `rg --files` over the source roots and the project directory.
- Search by year, district, stage, and terms such as `逻辑与思维`, `科学思维`, `辩证思维`, `创新思维`, `超前思维`, `分析与综合`, `发散`, `聚合`, `逆向`, `联想`, `迁移`, `想象`, `思维抽象`, `思维具体`, `感性具体`, `系统观念`, `形式逻辑`, `推理`.
- Use cached text first when a reliable cache exists; if cache is missing, confusing, incomplete, or too shallow for evidence judgment, return to the raw PDF/Word/PPT/source image.

Thinking action:

- Match paper, answer key, rubric, 评标, 阅卷, 讲评, and补充材料 by suite, year, district, stage, title, question number, and visible content.
- Deduplicate classification compilations and mirror copies. Record canonical source and supplementary evidence separately.

Output:

- `SOURCE_LEDGER.csv`
- preliminary rows in `QUESTION_COVERAGE_MATRIX.csv`

### 2. Text/OCR/Render Recovery

Tool action:

- PDF with text layer: use `pdftotext` or Python PDF extraction.
- Scan/image PDF: render pages, then OCR or visually inspect images.
- `.docx` / `.pptx`: extract structured text; if extraction is incomplete, inspect rendered pages/slides.
- old `.doc` / `.ppt`: convert when possible; if conversion fails, record exact failure and try an alternate reader before marking `conversion-needed`.

Thinking action:

- Decide whether the extracted text is enough to identify the module, question number, objective answer, and scoring position.
- If not enough, use raw visual evidence and record the boundary.

Output:

- extracted text path or page-image path in the ledger;
- `extracted`, `ocr-needed`, `conversion-needed`, or `missing-source` status.

### 3. Module Boundary And Evidence Grading

Tool action:

- Open the paper question and paired answer/scoring source.
- Search the full suite for explicit prompts such as `运用《逻辑与思维》`, `运用辩证思维`, `运用创新思维`, `运用科学思维`, `运用超前思维`, `用联想思维`, `分析与综合`, `思维抽象`.

Thinking action:

- Classify each candidate as `A-formal`, `A-support`, `B-choice-signal`, `C-boundary`, or `missing`.
- Do not let words like `辩证`, `系统`, `创新`, `整体`, `合`, `融` decide module ownership by themselves. The question stem, answer key/rubric, and tested knowledge must agree.
- Pure formal-logic or reasoning-rule questions stay out of the thought-method main chain, unless a later sub-question clearly asks for thinking-method application.

Output:

- updated `QUESTION_COVERAGE_MATRIX.csv`;
- excluded rows must name the boundary reason.

### 4. Main-Question Thinking Extraction

Tool action:

- Read the full question prompt, material, and scoring source.
- For tables, rubric levels,总说/分说, angle-plus-material layers, or alternatives, extract every scoring layer.

Thinking action:

- For each scoring point, determine:
  - material action: what the material is doing, such as investigation, prediction, coordination, transformation, cross-domain linking, reverse thinking, or abstraction;
  - total hat: `科学思维`, `辩证思维`, or `创新思维`;
  - small method: `客观性`, `预见性`, `可检验性`, `分析与综合`, `整体性`, `动态性`, `质量互变`, `辩证否定`, `超前思维`, `联想`, `发散`, `聚合`, `逆向`, `迁移和想象`, `思维抽象与思维具体`;
  - trigger logic: why this material action triggers this method, in knowledge terms;
  - answer sentence: what a candidate can write on the answer sheet for this question.

Output unit:

```markdown
**思维方法/给分点：<rubric original phrase or precise thinking-method scoring term>**

- 完整设问：<only the actual question prompt; do not mix material into this field>
- 细则位置：<suite, question, scoring source, point/level/score/evidence level>
- 来源：<year, district, stage, question>
- 材料动作：<concrete action or relation in the material>
- 总帽子：<科学思维 / 辩证思维 / 创新思维 / other supported total category>
- 小方法：<specific method supported by the source>
- 触发逻辑：<material action -> why it requires this thinking method; not material copying>
- 答案句：<candidate answer-sheet sentence: method term + material fact + cause/effect/conclusion>
- 框架落点：<existing user framework node>
- 题型标签：<stable transferable question family>
- 证据等级：<A-formal / A-support / missing>
```

### 5. Choice-Question Trap Extraction

Tool action:

- Use paper text plus a reliable objective answer key. Do not infer the correct answer from the explanation alone.
- If answer keys conflict, record the conflict and do not add trap patterns until resolved.

Thinking action:

- Explain why the correct option fits the material signal and the thought method.
- For every wrong option, identify why it is tempting and why it is wrong.
- Pay special attention to `思维抽象与思维具体` versus `分析与综合`, `系统整合`, `联想/类比推理`, and `发散与聚合`.

Trap types include:

- total-hat/small-method confusion;
- scientific/dialectical/innovative thinking flattening;
- analysis-synthesis vs abstraction-concretion confusion;
- system-integration vs abstraction-chain confusion;
- analogy/association vs abstraction-chain confusion;
- future-layout without real evidence for超前思维;
- cross-domain linking overread as创新思维;
- pure formal-logic question misclassified as thinking method;
- material keyword overreach;
- module-boundary error.

Output:

- `CHOICE_TRAP_LEDGER.csv`;
- reusable traps may enter the choice trap library only when source suite, question number, question text, and answer key are clear.

### 6. Framework Backfill And Classroom Compression

Tool action:

- Open the current 选必三 framework and prior path accumulation manuscripts.
- Read only confirmed framework/backfill rows and student-facing drafts when compressing.

Thinking action:

- Place every confirmed scoring point under the user's existing thinking-method structure or a deliberately added node.
- Same question may enter multiple nodes when the rubric supports multiple thinking methods. Do not let one placement hide other scoring points.
- Convert research rows into a weak-student routine:
  1. 先看材料动作;
  2. 再判总帽子;
  3. 再拆小方法;
  4. 再写材料为什么触发它;
  5. 最后写成卷面答案句或选择题排错口令.

Default stable trigger chains:

- `调查/数据/验证/迭代 -> 科学思维 -> 客观性/可检验性`
- `趋势研判/未来布局/提前规划 -> 科学思维或超前思维 -> 预见性`
- `多主体/多环节/协同治理/一盘棋 -> 辩证思维 -> 分析与综合/整体性`
- `当前与长远/由低到高/渐进推进 -> 辩证思维 -> 动态性/质量互变`
- `旧产业/旧资源/旧模式升级 -> 辩证否定`
- `跨界组合/文旅融合/文创设计 -> 创新思维 -> 联想/迁移和想象`
- `多方案铺开再收束 -> 发散思维 -> 聚合思维`
- `关系、方向、状态反过来 -> 逆向思维`
- `杂多现象 -> 抽出核心概念 -> 回到完整整体图景 -> 思维抽象与思维具体`

Output:

- `FRAMEWORK_TRIGGER_BACKFILL.md`
- `CLASSROOM_DRAFT.md`
- optional `.docx` after render verification.

### 7. Patcher Review

Tool action:

- Compare `QUESTION_COVERAGE_MATRIX.csv`, `MAIN_THINKING_LEDGER.csv`, `CHOICE_TRAP_LEDGER.csv`, and `FRAMEWORK_TRIGGER_BACKFILL.md`.
- Search for `missing`, `C-boundary`, incomplete fields, forbidden words, and total-hat-only entries.

Thinking action:

- Look for one-material-many-method omissions,总说/分说 omissions, module-boundary errors, hidden OCR failures, shallow triggers, and answer sentences that are not candidate-facing.

Output:

- `PATCH_REVIEW.md` with pass/fail rows and required repairs.

### 8. Governor Review

Governor must veto if any of these are true:

- ordinary reference answers are presented as formal scoring sources;
- a main-question row lacks full prompt, scoring position, material action, trigger logic, or answer sentence;
- trigger logic is just copied material or backstage process talk;
- answer sentence contains `要写`, `落到`, `采分点`, `设问要求`, `细则要求`, `本题需要`, `v7漏了`, `材料明确写到`, `材料中`, or similar production language;
- final student artifact contains source paths, line ids, OCR/debug notes, internal status fields, evidence labels, or audit language;
- a suite is marked complete while coverage has unclassified, missing, or unresolved rows;
- a rubric has总说/分说 or等级层次 but only the total layer was extracted;
- choice questions are processed without a reliable objective answer key;
- plan/progress files claim completion before ledgers and artifacts support it;
- a pure formal-logic or other-book question enters the 选必三思维主链.

Output:

- `GOVERNOR_CHECKLIST.md`;
- update `/Users/wanglifei/Desktop/北京高考政治/reports/governor_board.md` for substantial rounds.

## Trial Before Full Run

Before launching full-suite exhaustion with a new or revised skill, test these five hard samples:

- `2026顺义一模 Q19(2)`: scientific thinking three features; must extract `客观性`, `预见性`, and `可检验性`.
- `2025海淀二模 Q20`: dialectical compound thinking; must distinguish `分析与综合`, `整体性`, `动态性/质量互变`, and supported `辩证否定`.
- `2026朝阳期中 Q21(2)`: innovative compound thinking; must handle `超前`, `联想`, `逆向`, and `发散聚合`.
- `2026通州期末 Q11`: choice-question trap; must teach `感性具体 -> 思维抽象 -> 思维具体` and distinguish it from `系统整合`, `类比/联想`, and `分析与综合`.
- `2026东城期末 Q17(2)`: boundary counterexample; must not misclassify a pure formal-logic sub-question as a thinking-method main-chain item.

The trial passes only if:

- all five samples have ledger records;
- all five samples have Patcher and Governor conclusions;
- positive samples contain material triggers and candidate-facing answer sentences;
- the boundary sample gives a clear exclusion reason;
- no forbidden backstage wording appears;
- the router maps `选必三` / `逻辑与思维` / thinking-method terms to this skill.

Do not start full-suite exhaustion until the trial passes. If the trial fails, patch the skill or hard-rule notebook first.

## Final Acceptance

Full completion requires all of the following:

- every discovered candidate row is classified as `A-formal`, `A-support`, `B-choice-signal`, `C-boundary`, or `missing`;
- every `A-formal` main question has complete required output fields;
- every choice trap entry has a reliable answer key and full wrong-option analysis;
- every formal thinking-method scoring point is either backfilled into the framework or explicitly rejected with a reason;
- all `C-boundary` and `missing` rows are preserved with honest boundaries;
- the classroom draft is readable without audit files and uses candidate-facing answer sentences;
- `PATCH_REVIEW.md`, `GOVERNOR_CHECKLIST.md`, and `FINAL_ACCEPTANCE_REPORT.md` agree;
- `PROGRESS.md` and `DEVELOPMENT_PLAN.md` agree only after the work exists.

## Final Response

Only final after:

- all control files agree;
- the governor checklist passes or clearly records blockers;
- final artifacts exist;
- Word files render cleanly if requested;
- `FINAL_ACCEPTANCE_REPORT.md` ends with `TASK_COMPLETE` when and only when all gates pass.

In the final answer, list deliverables and key residual boundaries. Do not call blocked or reference-only material complete.
