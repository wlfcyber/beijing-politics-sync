# Master Requirements

This file is the highest-priority run instruction after direct user messages.

Resolve conflicts as:

1. Latest user message in this thread.
2. This `MASTER_REQUIREMENTS.md`.
3. Local notebook `/Users/wanglifei/Desktop/北京高考政治/选必一复查_2026-04-29/选必一_交付要求记事本.md`.
4. Branch skill and references:
   - `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
   - `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
   - `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`
5. Old artifacts, only as audit references and user-correction evidence.

## Scope

- Book/module: 选择性必修一《当代国际政治与经济》.
- Default target: 主观题细则术语积累与学生可用答题框架.
- Default evidence pool: Beijing local 2024-2026 mock/question source roots:
  - `/Users/wanglifei/Desktop/2024模拟题`
  - `/Users/wanglifei/Desktop/2025模拟题`
  - `/Users/wanglifei/Desktop/2026模拟题`
- Process choice questions only if needed for boundary/coverage notes or if the user later explicitly asks. The core 选必一 branch output is 主观题.

## Codex Role Rule

- Codex is not only the supervisor.
- Codex has two roles in this run:
  1. `Codex leader`: maintains plan, ledgers, coverage, worker supervision, fusion, governor checks, document pipeline, and final acceptance.
  2. `Codex production lane`: directly processes raw sources, extracts/renders/visually reads evidence, writes entries, closes suites, and leaves auditable outputs in `codex_lane/`.
- ClaudeCode is an independent rerun/comparison lane, not a substitute for Codex's own production work.
- A suite is not considered fully ready for fusion until Codex production evidence exists or the user explicitly narrows the task to ClaudeCode-only supervision.

## Old-Lane Boundary

- This run starts from source evidence again.
- Old v12 and earlier files must not be copied as final content.
- Old files may be read to preserve:
  - user-corrected hard samples;
  - known exclusions;
  - formatting preferences;
  - previous mistake patterns to avoid.
- Every included term must still be traceable to a source file, suite, question, scoring/rubric position, and evidence boundary in this run.

## Required Framework

Use the user's six buckets as the top-level structure:

1. 时代背景
2. 理论
3. 经济全球化
4. 政治多极化
5. 中国
6. 联合国

Do not invent a new top-level taxonomy unless the user explicitly changes the framework.

## Required Entry Unit

Every included term entry must preserve:

- `术语`：评分细则、评标、阅卷总结或用户确认细则里的原词，不写自造概括。
- `完整设问`：题目要求学生作答的完整设问句。
- `细则位置`：套卷、题号、评分细则/评标点位、分值或证据层级。
- `来源`：年份、区、题号。
- `材料触发`：题目追问什么、材料形成什么关系、为什么触发该术语。
- `答案句`：考生可直接写在答题纸上的句子，必须含术语、本题材料事实、因果/作用/结论链。

Forbidden in final student-facing content:

- `真题规律`
- 后台复查话：`v7`, `v8`, `v9`, `v10`, `v11`, `v12`, `复查`, `证据层级` as visible teaching labels
- 审计/流水线词：`pass`, `filled`, `pipeline`, source path, debug note
- 答案句制作话：`要落到`, `采分点`, `并结合材料说明`, `设问要求`, `细则要求`, `本题需要`
- 笨前缀：`材料中`

## Source Hierarchy

Use sources in this order:

1. 正式评分细则、评标、阅卷细则、阅卷总结。
2. 明确讲分、标分、替换词、必答点的讲评材料。
3. User-confirmed scoring material.
4. Ordinary reference answers only as support, never as `细则位置` unless user-confirmed.

If no scoring source is found, keep the question out of the main term table and record the blocker. Do not promote ordinary reference answer wording into scoring terms.

## Hard User Corrections To Preserve

- `2026通州期末 Q20` must preserve the six-point correction:
  1. 共商共建共享全球治理观；
  2. 时代主题、经济全球化、顺应各国人民愿望等；
  3. 符合《联合国宪章》；
  4. 推动构建国际新秩序、倡导国际关系民主化、践行多边主义、坚持正确义利观、兼顾利益等任意点；
  5. 人类命运共同体；
  6. 贡献中国智慧、中国方案、勇于大国担当。
- `2026朝阳期中 Q17` and similar `总说/分说` questions must preserve both the general layer and all sub-layers.
- `2026石景山期末` is excluded for all modules unless the user explicitly provides a new scoring-rule source.
- `2025海淀期中 Q16(2)` must be checked for trade friction, international organization rights, and participation in global economic governance/rule-making.
- `2025海淀期中 Q21(2)` has user-confirmed image/table scoring material and must not be skipped just because text extraction is imperfect.
- `2025海淀期末 Q22`, `2024东城一模 Q16`, and `2024东城一模 Q20` must be rechecked as potential included sources.
- `2026海淀期末` was user-confirmed as no 选必一 and should remain excluded unless source evidence changes.

## Non-Text Source Rule

PDF, Word, PPT, image, scan, table, and screenshot materials must be processed with available tools. If one tool fails, mutate the method: text extraction, Office conversion, QuickLook, Microsoft Word, OCR, screenshot, image render, or manual visual reading.

Do not mark a source absent merely because one converter failed.

## Document Pipeline

Follow `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/skills/feige-politics-garden-book-orchestrator/references/document-pipeline.md`.

Markdown is the canonical student-facing source. DOCX is generated from Markdown and then validated with Microsoft Word when available.

Final document preferences:

- clean lecture-handout tags, not ugly bullet rectangles before field labels;
- frequency annotation after each term in the main document, e.g. `（出现N次）`;
- separate frequency/statistics file if useful;
- readable headings with restrained accent color;
- page numbers, clickable TOC where feasible, embedded images where relevant;
- final Word open/save validation.

## Validation Gates

- `SOURCE_LEDGER.csv` must list every source file considered.
- `COVERAGE_MATRIX.csv` must include every suite/question decision.
- `suite_reports/` must contain closure reports for processed suites.
- Governor must reject entries without auditable `细则位置`.
- Confucius must read only the final student artifact and test whether it can teach a zero-baseline student to classify and write fresh 选必一 answers.
- `FINAL_ACCEPTANCE_REPORT.md` is written last.
