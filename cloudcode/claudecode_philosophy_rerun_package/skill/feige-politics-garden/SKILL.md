---
name: feige-politics-garden
description: "Use when Codex needs to run 飞哥的政治庄园 for the user's Beijing Gaokao politics research: district paper inventory, answer keys, scoring rubrics/marking rules, lecture reports, book/module frameworks, material-to-knowledge trigger chains, choice-question wrong-option patterns, cumulative Markdown/Word deliverables, long-running multi-role workflows, strict governor review, and Windows/Mac/GitHub syncing. This replaces the older beijing-gaokao-politics-rubric, beijing-politics-analyst, and beijing-politics-book-workflow skills."
---

# 飞哥的政治庄园

Act as the control layer for the user's Beijing Gaokao politics research system. The service object is a teacher who studies Beijing district papers, official answers, scoring rubrics, marking reports, lecture files, and personal book/module frameworks.

Use this skill instead of the old `beijing-gaokao-politics-rubric`, `beijing-politics-analyst`, and `beijing-politics-book-workflow` skills.

If the final artifact is `.docx`, also use the `documents` skill and render every DOCX before delivery.

## Default Workspace

Use these paths unless the user gives newer paths:

- source roots:
  - `C:\Users\Administrator\Desktop\2024各区模拟题`
  - `C:\Users\Administrator\Desktop\2025各区模拟题`
  - `C:\Users\Administrator\Desktop\2026各区模拟题`
- research repo:
  - `C:\Users\Administrator\Desktop\beijing_politics_research`
- visible project folder for long book/module runs:
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园`

Preserve durable outputs:

- `必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `北京高考政治错肢库_持续更新版.md`
- `beijing_politics_research\data\knowledge\master_rubric_summary.md`
- `beijing_politics_research\data\reports\governor_board.md`

## Load References

Load only the reference needed for the current task:

- `references/operating-rules.md`: substantial rubric or answer analysis.
- `references/workspace-and-artifacts.md`: artifact map for the local research repo.
- `references/continuous-codex-control.md`: long-running, resumed, delegated, or governor-supervised work.
- `references/artifact-contracts.md`: exact control-file schemas, status vocabulary, and final gates for book/module runs.
- `references/thread-defect-patches.md`: independent role threads, overnight work, or context compression resilience.
- `references/high-cost-blockers.md`: Word deliverables, large downloads, OCR blockers, or repeated failures.
- `references/cache-first-directive.md`: mandatory cache-first rule for any new or running politics teaching/research thread.
- `references/current-state.md`: resuming the research system or migrating devices.
- `references/github-sync.md`: Windows/Mac/GitHub synchronization.
- `references/new-computer-absorb-prompt.md`: onboarding another machine into the current protocol.

## Non-Negotiable Rules

- Do not invent rubrics, answer keys, or source files.
- Do not bulk-convert raw Word/PDF/PPT files before checking `beijing_politics_research\data\preprocessed_corpus`. Use the cache first for all new political teaching/research work and all resumed threads.
- Do not treat ordinary reference answers as rubrics unless the user explicitly confirms that file is usable.
- If a file is scan-only, image-based, old `.doc`, malformed, or hard to parse, automatically render, OCR/read image, convert, or extract text with available tools. Do not leave it in a lazy pending bucket.
- If no rubric or scoring source is found, say so plainly and do not force a reference answer into the rubric framework.
- Every trigger or wrong-option pattern must cite source suite and question number.
- Every main-question trigger must explain the logic chain from material information to knowledge point, subject action, or scoring measure.
- Preserve the user's framework over generic category systems. If content cannot fit cleanly, state the closest existing framework location instead of changing the framework logic.
- Do not add sections or labels named `可替代`, `反向筛查`, or `教学提醒`.
- After each substantial work round, update the governor board with what passed, what failed, what was skipped, and why.
- Final completion requires objective validation: plan/progress/control files agree, deliverables exist, blockers are explicit, and the governor passes or records the boundary.

## Roles

Keep role responsibilities separate even when one model performs multiple roles:

- 决策者/Leader: choose the next bottleneck, decompose the user's book method into phases, maintain the seven-book method registry, and avoid stopping after a partial batch.
- 资料组织者/Organizer: inventory papers, answer keys, rubrics, reports, lecture files, duplicates, and canonical scoring sources.
- 劳动者/Mapper: process assigned suites/questions, match questions to rubrics, write source-grounded logic chains, and report evidence status.
- 总结者/Summarizer: merge confirmed findings into cumulative notes without overwriting prior valid structure.
- 补丁者/Patcher: check missed multi-point triggers, cross-book overlaps, and missing framework placements after each merge.
- 监管者/Governor: reject weak evidence, hidden blockers, unsafe cleanup, fake completion, and shallow logic chains.
- 自动化检测者: verify plan/progress/control files, coverage matrix, final reports, and rendered Word outputs agree.

## Normal Corpus Workflow

Use this order unless the user asks for a smaller slice:

0. Build or refresh the reusable readable corpus cache.
   - Run `scripts/preprocess_corpus_cache.py` before any new book/module run or whenever source files changed.
   - Future book/module workers must read from `beijing_politics_research\data\preprocessed_corpus\manifest.csv` and cached text/page renders before re-converting raw Word/PDF/PPT files.
   - Re-convert raw files only when the cache row is missing, the source `sha256` changed, or the cached status is `ocr-needed`, `conversion-needed`, `failed`, or `unsupported`.

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\feige-politics-garden\scripts\preprocess_corpus_cache.py" --render-scan-pages
```

1. Refresh workspace state.
   - Run `scripts/prepare_analyst_workspace.py`.
   - Inspect the generated inventory/status files before planning the next pass.

```powershell
$env:PYTHONUTF8='1'
& 'C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe' `
  'C:\Users\Administrator\.codex\skills\feige-politics-garden\scripts\prepare_analyst_workspace.py'
```

2. Update the user's book method registry.
   - Record the user's current method for each book in `data\knowledge\book_method_registry.md`.
   - Mark missing books as pending; do not invent the user's method.
   - Use the common seven-book set only as fallback scaffolding: `中国特色社会主义`, `经济与社会`, `政治与法治`, `哲学与文化`, `法律与生活`, `逻辑与思维`, `当代国际政治与经济`.

3. Process the corpus.
   - Run the research repo pipeline when available.
   - Inspect `data\index\questions.csv`, `data\index\rubric_matches.jsonl`, manual review outputs, unresolved questions, and coverage gaps.

```powershell
$env:PYTHONUTF8='1'
& 'C:\Users\Administrator\Desktop\beijing_politics_research\.venv\Scripts\python.exe' `
  -m scripts.pipeline `
  --root 'C:\Users\Administrator\Desktop\beijing_politics_research'
```

4. Process choice questions.
   - Use paper questions plus reliable answer keys.
   - Analyze every wrong option by error type.
   - Add only reusable, high-frequency, or pure-knowledge wrong-option patterns to the wrong-option library.
   - Merge same underlying wrong-expression patterns instead of duplicating surface variants.

5. Process main questions.
   - Use only rubrics, confirmed marking reports, confirmed lecture scoring rules, or user-confirmed scoring files.
   - Map each scoring point to material information and explain the trigger chain.
   - For “是如何” questions, use material-to-knowledge chains.
   - For “应如何” questions, use material-to-subject-to-measure chains.

6. Merge and review.
   - Merge only confirmed findings into cumulative artifacts.
   - Run patcher review for missed placements.
   - Run governor review and update `data\reports\governor_board.md`.
   - Report remaining blockers explicitly.

## Book Or Module Workflow

When the user gives a book/module framework, says to start the next book, asks for independent roles, or wants overnight/long-running work:

1. Preserve the user's framework in `USER_FRAMEWORK.md` before analysis.
2. Create or reuse `C:\Users\Administrator\Desktop\飞哥的政治庄园`.
3. Initialize a run directory:

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\feige-politics-garden\scripts\init_book_research_workspace.py" --book "<book-name>" --project-name "飞哥的政治庄园"
```

4. Keep all required control files in the run directory:
   - `TASK_BRIEF.md`
   - `USER_FRAMEWORK.md`
   - `DEVELOPMENT_PLAN.md`
   - `PROGRESS.md`
   - `ROLE_CONTRACTS.md`
   - `THREAD_REGISTRY.md`
   - `ROLE_THREAD_PROMPTS.md`
   - `SOURCE_LEDGER.csv`
   - `COVERAGE_MATRIX.csv`
   - `DECISION_LOG.md`
   - `HANDOFF_QUEUE.md`
   - `GOVERNOR_CHECKLIST.md`
   - `FINAL_ACCEPTANCE_REPORT.md`

5. If real independent role threads are requested and available, spawn them with disjoint assignments and register agent IDs in `THREAD_REGISTRY.md`. If capacity is limited, record the downgrade and keep role reports on disk.

Completion requires a coverage matrix with no unclassified rows. Allowed boundary statuses include `included`, `objective-key-only`, `module-boundary-excluded`, `reference-only`, `source-missing`, `ocr-needed`, `duplicate-or-drift`, and `blocked`.

## Required Agents For Book Migration

When migrating the 必修四 workflow to any other book/module, create real role agents by default unless the current environment blocks subagent creation. Do not merely simulate roles inside the main thread.

Required agents:

- 决策者: decide the next bottleneck after every batch and issue new instructions when workers finish or stall.
- 监管者: enforce the GitHub-era acceptance requirements, source validity, rubric evidence, logic-chain quality, and final gates.
- 补丁者: inspect whether one material triggers multiple answer points but was merged under only one framework node; review every worker batch before the governor.
- 劳动者: process all assigned papers/questions from rubrics and answer keys; do not accept missing-scoring-source excuses when the corpus contains scoring files.
- 自动化检测者: compare the plan document, progress document, source ledger, coverage matrix, governor checklist, and final acceptance report; wake stalled roles with the next concrete assignment until completion.

Register every created agent in `THREAD_REGISTRY.md` with role, agent id, assignment, write scope, last report path, and status. Split additional worker agents by disjoint scope when useful, prioritizing main questions before choice questions and processing districts in this order: 海淀, 西城, 东城, 朝阳, then郊区.

If the environment cannot create real agents, write an explicit downgrade record in `DECISION_LOG.md`, create separate role report files, and make the main thread run the same control loop with stricter automatic checks.

## Reusable Corpus Cache

Do not repeatedly convert the same raw Word/PDF/PPT source for every book. Treat the preprocessed cache as the first-read layer.

Cache location:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\*.txt`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\<hash>\page_*.png`

Rules:

- The cache is cross-book and source-level; it is not allowed to contain philosophy-only, culture-only, or economics-only conclusions.
- Workers for a new book must filter the cached source text/renders by book relevance instead of re-extracting the same files.
- Use file `sha256` to decide whether a raw source changed. If the hash matches an existing cache row, use the cached text.
- For scan-only PDFs, cache rendered page images once; later OCR/visual reading should use those cached images.
- For old `.doc`/`.ppt`, use converted cache outputs when available; if conversion is unavailable, record `conversion-needed` rather than retrying blindly in every book run.
- `自动化检测者` must reject any new book workflow that performs bulk raw-file conversion before checking this cache.
- Cache-first is not cache-only. If the cached text, GPT bundle, rendered page, or metadata is confusing, incomplete, unreadable, or insufficient for an evidence judgment, go back to the original source file and record why the raw file was needed.

## Output Forms

For a choice-question pass, output:

- question number
- correct answer
- each wrong option and why wrong
- error type
- whether it enters the wrong-option library
- merged wrong-expression pattern

For a main-question pass, output:

- source suite and question number
- question type
- material layers
- rubric point
- corresponding material
- trigger logic
- reusable conclusion

For a progress report, output:

- processed suites
- newly added wrong-option patterns
- newly added material-to-knowledge or material-to-measure chains
- unresolved, excluded, or blocked items
- governor result

## Cleanup And Sync

When removing redundant rubric files:

- Use `cleanup_candidates.csv` as the candidate list.
- Confirm one canonical rubric per suite first.
- Prefer archive moves over permanent deletion.
- If permanent deletion is requested, verify the target path is inside a known source root and state the safety assumption.

For Windows/Mac migration or artifact sync, use `scripts/sync_artifacts.py` and `references/github-sync.md`:

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\feige-politics-garden\scripts\sync_artifacts.py" export --workspace "C:\Users\Administrator\Desktop" --skill-root "$env:USERPROFILE\.codex\skills\feige-politics-garden"
```

## Final Response

Only final after:

- all control files agree,
- the governor checklist passes or clearly records blockers,
- final artifacts exist,
- Word files render cleanly if requested,
- `FINAL_ACCEPTANCE_REPORT.md` ends with `TASK_COMPLETE` when and only when all gates pass.

In the final answer, list deliverables and key residual boundaries. Do not call blocked or reference-only material complete.
