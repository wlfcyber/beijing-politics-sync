# TASK_BRIEF: 选必二法律主观题习题与细则汇编 Dynamic Workflow

- run_id: `opus48_dynamic_workflow_subjective_compilation_2026-05-29`
- date: 2026-05-29
- owner_lane: VS Code ClaudeCode visible workflow
- required_model: Claude Opus 4.8
- required_effort: Max / ultracode / highest available
- required_mode: dynamic workflow

## User Request

汇总 2024、2025、2026 三年北京各区政治模拟题中所有选必二《法律与生活》法律主观题。每道题下面附对应评分细则，形成“习题 + 细则”汇编。整理过程中可以同步思考选必二考题规律，并生成候选框架。

## Locked Boundaries

1. Source roots:
   - `/Users/wanglifei/Desktop/2024模拟题`
   - `/Users/wanglifei/Desktop/2025模拟题`
   - `/Users/wanglifei/Desktop/2026模拟题`
2. Scope:
   - only 选必二《法律与生活》法律主观题;
   - include all legal subjective questions from the three-year source roots;
   - do not include choice questions in the main compilation unless they are only used as separate framework/pattern context.
3. Rubric rule:
   - user states every legal subjective question has scoring details;
   - if not found, expand search; do not finalize as missing;
   - acceptable scoring evidence includes formal 细则、评标、阅卷总结、讲评 PPT/文档、分题细则、答案变通说明, and user-confirmed scoring source.
4. Old-output rule:
   - all old 选必二 conclusions are void;
   - old files may only be used as location hints or QA contrast, not as evidence or inherited prose.
5. Framework rule:
   - framework is candidate only in this run;
   - every pattern/framework node must cite supporting question ids and rubric terms.

## Target Deliverables

- `04_outputs/选必二法律主观题_习题与细则汇编_20260529.md`
- `04_outputs/选必二法律主观题_习题与细则汇编_20260529.csv`
- `03_source_packets/*.md` one packet per question or subquestion
- `00_control/SOURCE_LEDGER.csv`
- `00_control/RUBRIC_SEARCH_LEDGER.csv`
- `00_control/QUESTION_COVERAGE_MATRIX.csv`
- `05_framework_candidate/选必二考题规律与候选框架_20260529.md`
- `06_governor/GOVERNOR_CHECKLIST.md`
- `07_acceptance/FINAL_ACCEPTANCE_REPORT.md`

## Completion Standard

No final completion claim is allowed until:

- every source suite is scanned or has a named blocker;
- every legal subjective question has a source packet;
- every source packet has a matched scoring detail source or an active deeper-search task;
- no entry uses old 选必二 conclusions as evidence;
- the compilation can be traced back to source path + page/position;
- framework notes are marked candidate and evidence-linked;
- Governor records unresolved cases by exact file/question, not vague summaries.
