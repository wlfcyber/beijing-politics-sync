# Continuous Codex Control Protocol

This protocol preserves the user's best long-task prompts as durable operating rules. Use it whenever a task may span multiple turns, devices, Codex sessions, background runners, or parallel workers.

## Core Rule

Codex is not done when it says it is done. Codex is done only when the written plan, written progress, required artifacts, governor record, and strict acceptance test all agree.

## Required Control Files

For any substantial task, keep these documents:

- `TASK_BRIEF.md`: task target, scope, constraints, required outputs, completion standard.
- `DEVELOPMENT_PLAN.md`: ordered executable steps using stable `STEP_XX` ids.
- `PROGRESS.md`: completed steps using the same `STEP_XX` ids.
- `governor_board.md`: what passed, what failed, what was skipped, why, and what remains.
- final acceptance checklist or report when the task has a student-facing or research-facing deliverable.

If an existing project uses older names such as `codex_连续任务_任务步骤文档.md` and `codex_连续任务_任务进度文档.md`, treat them as the plan/progress pair.

## Canonical Runner Prompt

Use this prompt shape when continuing a long task:

```text
你现在在执行一个“连续任务闭环”。

工作目录：
- <WORKDIR>

任务说明文档：
- <TASK_BRIEF>

开发计划文档：
- <DEVELOPMENT_PLAN>

进度文档：
- <PROGRESS>

本轮目标：
- 读取任务说明、计划和进度
- 推进下一个未完成步骤：<STEP_ID>

严格规则：
1. 只能推进一个“最小但完整”的下一步。
2. 必须先真正完成对应开发工作，再把它记入进度文档。
3. 进度文档中的完成记录必须使用严格格式：- [x] STEP_XX: 完成说明
4. 不要删除已有完成记录。
5. 不要把未完成的事情写成已完成。
6. 如果执行中发现计划需要细化，可以补充计划文档，但不能抹掉已有步骤。
7. 本轮完成后保存全部修改并停止。
8. 如果全部计划都已完成，最后一行只输出：TASK_COMPLETE
9. 如果只是完成了本轮步骤，最后一行只输出：STEP_DONE: <STEP_ID>
```

Older two-document prompt, still valid:

```text
你正在执行一个需要持续推进的 Codex 任务。

本轮要求：
1. 阅读任务步骤文档。
2. 阅读任务进度文档。
3. 真正推进至少一个尚未完成的任务步骤，而不是只输出计划。
4. 每完成一个步骤，都要同时更新两个文档：
   - 在任务步骤文档中，把对应步骤从 [ ] 改成 [x]
   - 在任务进度文档中，用完全相同的步骤 ID 和步骤标题记录为 [x]
5. 若步骤标题不一致，优先以任务步骤文档为准修正任务进度文档。
6. 若全部任务完成，确保任务步骤文档中不再有 [ ]，且任务进度文档与其完全一致。
```

## Stop Conditions

Stop only when all are true:

- every plan `STEP_ID` appears as completed in progress;
- no progress entry is outside the plan unless it is explicitly explained;
- required artifacts exist and have been updated;
- governor board records pass/fail/skip status and remaining blockers;
- strict acceptance test passes;
- the final line or report says `TASK_COMPLETE`.

Do not stop merely because a model produced a fluent summary, a session compacted, a runner exited, or a partial artifact exists.

## Anti-Fake-Completion Rules

- Do not mark a step complete before the real work is written to the required artifact.
- Do not convert unknowns into completion language.
- Do not hide a missing source, missing rubric, missing answer key, failed OCR, or unresolved module boundary.
- Do not let ordinary reference answers become scoring rubrics.
- Do not let a final teaching manuscript count as validated unless it works on fresh or not-directly-memorized questions.

## Beijing Politics Evidence Rules

For this project, these constraints override speed:

- Main-question work must use scoring rubrics, marking rules, marking reports, confirmed lecture scoring rules, or user-confirmed usable scoring files.
- Choice-question work may use paper questions plus reliable objective answer keys.
- Beijing-question-bank fallback may verify objective answers only; do not upgrade its subjective answers into rubrics.
- Scan-only PDFs, image PDFs, old Word files, malformed files, and PPTs must be rendered, OCRed, converted, or visually read if possible.
- Every new wrong-option pattern or material trigger must include source suite and question number.
- Every material trigger must include the logic chain from material information to the knowledge point.
- Forbidden section labels remain forbidden: `可替代`, `反向筛查`, `教学提醒`.

## Philosophy Three-Line Closure

For 必修四哲学 suite-level work, a suite is not closed until all evidence-supported lines are settled:

- `选择题错肢线`: objective answers verified; reusable wrong options entered into the wrong-option library.
- `选择题框架线`: philosophy-related correct options backfilled as `材料信息 -> 原理/方法论 -> 逻辑链 -> 来源题号`.
- `主观题框架线`: rubric-supported main-question chains backfilled into the framework.

If a suite lacks a reliable rubric or answer key, record the blocker honestly instead of forcing closure.

## Strict Acceptance Prompt

Use this before declaring a student-facing manuscript complete:

```text
新标准不是“最终稿里提过这类细则点，我就能把评分点对上”。
新标准是：只当一个高三学生，脑子里只有最终教学稿/最终 markdown 教我的框架、术语和答题逻辑；进入考场后，面对同板块但最好不是成品里已被逐题讲过的新题，能否自己完成审题、搭框架、组织完整答案，并最终对照细则拿满分。
```

Acceptance should use fresh or at least not-directly-scripted questions where possible. Answer first from the final manuscript, then compare against the source answer/rubric.

## Supervisor Resume Prompt

When a workflow is alive but incomplete:

```text
继续，达到最终目标为止。不要等待确认。
```

Pair it with status checks:

- if logs are growing and processes are alive, do not restart blindly;
- if logs stop growing, the runner exits, or the agent waits for confirmation, resume immediately;
- if final artifacts are missing, do not validate.
- for Claude Code, judge stalls from data: process state, elapsed time, stream-json growth, debug log growth, output file mtimes, tool calls, and auth/network errors. Do not kill a run only because there is a pause in visible prose.
- if a Claude Code suite must be restarted, restart the same suite with the same source scope. Do not bypass the suite, skip to the next one, or feed only preselected answer fragments unless the user explicitly asks for that narrow rescue.

## Parallel-Line Boundary Rules

When multiple Codex lines work in parallel:

- each line must declare its current suite or module boundary;
- no two lines should process the same suite unless one is explicitly reviewing the other's completed output;
- when splitting a large suite queue, it is acceptable to run multiple Claude/Codex lines from different thirds of the queue, for example one line from the front, one from the middle, and one from the end backward, as long as each line has a disjoint suite range and records writes separately;
- if one line works backward from the end, its outputs must still merge into the same framework-node final structure rather than preserving reverse suite order;
- if two lines meet at the same remaining suite or adjacent unavoidable overlap, stop both workers after the latest complete write;
- a governor then merges artifacts, resolves ledger/framework/governor/current-state consistency, and runs final acceptance.

Canonical instruction:

```text
防止两条线重复劳动；当两线正好交汇时，由督工出手让它们停止，并生成最终版。
若两线剩余未闭环对象只剩同一套、相邻同一小批次，或继续续推将不可避免处理同一套卷，立即停止继续 resume 两条工作线。
交汇后由督工接管总审、合并错肢库/知识触发框架/ledger/governor/current-state，并生成最终 markdown 或教学稿成品，再进入严格抽题验收。
```

## Reusable Master Prompt

For any new long Codex job in this project:

```text
你现在执行一个连续任务闭环。

先读任务说明、开发计划、进度文档和监管记录。
每轮只能推进一个最小但完整的下一步。
必须先完成真实工作，再更新进度。
不得把未完成事项写成完成。
不得删除已有完成记录。
若计划不够细，可以补充计划，但不能抹掉已有步骤。
若遇到扫描件、旧文档、无文本层 PDF，必须主动 OCR、渲染或转换，不能只挂起。
所有成果必须写入指定交付物，并更新 governor_board。
只有当开发计划中的全部 STEP_ID 都在进度文档中完成，且交付物、监管记录、验收清单互相一致时，任务才允许停止。
最后一行只输出 STEP_DONE: STEP_XX 或 TASK_COMPLETE。
```
