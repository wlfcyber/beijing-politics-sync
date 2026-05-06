# Suite Count Reconciliation

time: 2026-05-04 12:28 CST
status: PASS_COUNT_RECONCILED

## What Was Counted

- Source suite groups inventoried from the local 2024-2026 original-source roots: 56.
- Coverage matrix coverage: 56 / 56 source suite groups have an explicit row or boundary row.
- Coverage matrix rows: 75, because some suites have multiple relevant questions or boundary questions.
- Final teacher index: 57 question anchors from 52 source suite groups.
- Final student-facing main training questions after GPT/Claude v2 pruning: 47.
- Final student-facing answer-point chains after GPT/Claude v2 pruning: 176.
- Final student-facing answer-sentence variants: 177.

## Why 47 Is Not the Suite Count

`47` is the number of student-facing main training questions after fusion, compression, and GPT/Claude v2 pruning. It is not the number of source suites processed.

The workflow first scans the near-60 source suite groups, then routes each source suite into one of these outcomes:

- promoted main question / expression accumulation;
- guarded candidate because evidence is not point-by-point formal scoring;
- reference-only because only reference answers are present;
- no-xuanbiyi boundary because the suite has no 选必一 subjective question;
- prompt-only blocker because the question exists but current scoring/rubric evidence is missing;
- excluded because the user explicitly excluded it.

## The Four Inventory Suites Not Represented As Final Main Questions

- `2026海淀期末`: `no_xuanbiyi_boundary`; no 选必一 subjective main-question promotion.
- `2026丰台期末`: `blocked_prompt_only`; LAC prompt found, current scoring/rubric missing, so it cannot be promoted.
- `2024模块分类汇编`: `source_bundle_boundary`; bundle/source collection, not an independent scoring-rubric suite.
- `2026石景山期末`: `excluded`; user-confirmed full-module exclusion.

## V2 Pruning Note

The earlier 11:47 count was 48 main training questions. After the GPT/Claude v2 deep review, `2025丰台一模 Q20` was kept only in the 慎用/跨模块 chapter because it is a mixed `经济与社会 + 当代国际政治与经济` question. That reduced the main training count to 47 without changing the 56/56 source coverage closure.

## Decision

No evidence was found that the run only processed "四十多套". The confusing number came from mixing two different metrics:

- 56 = source suite groups / coverage scope.
- 47 = final student-facing main training questions after evidence filtering, teaching compression, and v2 cross-module pruning.
