# Current Project State

This file preserves the state of the Windows session so a Mac session can resume without losing context.

## Main Artifacts

Windows originals:

- `C:\Users\Administrator\Desktop\必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `C:\Users\Administrator\Desktop\北京高考政治错肢库_持续更新版.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\reports\governor_board.md`

Copies are bundled in this skill under:

- `assets/current-artifacts/必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `assets/current-artifacts/北京高考政治错肢库_持续更新版.md`
- `assets/current-artifacts/governor_board.md`

On Mac, keep equivalent working copies in a private synced repository, for example:

- `~/GaokaoPolitics/beijing-politics-sync/artifacts/必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `~/GaokaoPolitics/beijing-politics-sync/artifacts/北京高考政治错肢库_持续更新版.md`
- `~/GaokaoPolitics/beijing-politics-sync/reports/governor_board.md`

## Source Corpus Known From Windows

Windows corpus roots:

- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`
- `C:\Users\Administrator\Desktop\哲学与文化  2026班课.pdf`

Mac should map them to local folders, for example:

- `~/GaokaoPolitics/source/2025各区模拟题`
- `~/GaokaoPolitics/source/2026各区模拟题`
- `~/GaokaoPolitics/source/哲学与文化  2026班课.pdf`

## Current Completion Boundary

### 2025

Main-question/rubric-trigger work is basically cleared for the local 2025 set, subject to the exclusions below.

Known included categories:

- 2025二模 six districts were already in the philosophy framework: 昌平、朝阳、东城、丰台、海淀、西城.
- 2025一模 was redone and backfilled using available rubrics, marking reports, teacher papers, and user-confirmed files: 朝阳、东城、房山、丰台、海淀、门头沟、石景山、顺义、西城、延庆.
- 2025期末/期中 cleanup handled:
  - 2025东城期末: user supplied `2025。1东城讲评 修改.pdf`; 第16题 has usable `答案细则`.
  - 2025丰台期末: `丰台期末细则.pptx`; 第16 and relevant 第17 philosophy points migrated.
  - 2025朝阳期末: `朝阳期末评标.pdf` rendered and read; 第16 and 第22 migrated.
  - 2025海淀期末: user confirmed `2025届期末考试0118(2).pptx`; 第16 and 第17 scoring口径 migrated.
  - 2025西城期末: user confirmed `西城期末答案 解析.pdf`; 第18哲学评分参考 migrated.

Known excluded/unresolved:

- 2025海淀期中: only reference answer found; no usable 必修四哲学 rubric; not merged.
- 2025海淀二模客观题: paper is scan-only and was rendered; lecture/rubric files available did not contain a reliable choice-answer table, so no inferred choice answers were written into the wrong-option library.

Choice-question work:

- `北京高考政治错肢库_持续更新版.md` currently has 42 reusable patterns:
  - 12 from 2026东城一模 philosophy-related choice questions.
  - 30 from 2025二模 first pass, from 东城、丰台、昌平、朝阳、西城.

### 2026

Current local 2026 source folders:

- `2026各区一模`
- `2026各区期末和期中`

No local 2026二模 folder or zip was found under Desktop or `2026各区模拟题` as of 2026-04-23.

2026一模 main-question mapping has 16 source-labeled rubric-supported chains:

- 2026东城一模 第16题、第20题
- 2026朝阳一模 第16题
- 2026丰台一模 第16题
- 2026延庆一模 第16题
- 2026房山一模 第16（2）题、第18（1）题
- 2026海淀一模 第16题
- 2026石景山一模 第17（1）题
- 2026西城一模 第16题、第21题
- 2026门头沟一模 第16题、第18（2）题、第21题
- 2026顺义一模 第16题、第21题

Important correction:

- 2026朝阳一模第16题 rubric exists in the user-supplied `chat_file_1040g3c831um895dphu105n2bsq04dit0lj2bojo_202604朝阳高三政治一模阅卷细则(1).docx`.
- It was initially missed because the docx starts directly with the question text, not a `16.` heading.
- It has now been added to the framework.

2026期中/期末 known points:

- 2026朝阳期中 第18题: user directly provided three scoring-rule variants for AI emotional value; migrated.
- 2026朝阳期末 第16题: rubric PDF scan was read with user-provided page image; migrated.
- 2026海淀期末 第16题: scoring standard PDF readable; migrated.
- 2026西城期末 第16（2）题: user provided scoring-page screenshot; migrated.
- 2026东城期末 第16题: user provided scoring-page screenshot; migrated.
- 石景山期末: user confirmed no rubric; skip.
- 海淀期中: user confirmed no philosophy question in that specific context; do not process philosophy.

## Important User-Provided Rubric Text

### 2026朝阳期中18

The user provided three official scoring-rule paths for the AI emotional-value question:

- Comprehensive/balanced path:
  - total statement: 矛盾普遍性 / 对立统一 / 一分为二 / 全面观点.
  - support reason: 按规律办事 / 从实际出发 / 矛盾特殊性 / 具体问题具体分析.
  - opposition reason: 主观能动性 / 意识依赖于物质 / 适度原则 / 实践.
  - how-to: 辩证否定观 / 正确价值观导向 / 价值判断与价值选择.
- Support path:
  - positive AI emotional-value function;
  - analyze user needs and adjust dialogue model;
  - use correct technology ethics.
- Opposition path:
  - AI emotional-value defects;
  - overdependence weakens real interaction ability;
  - use correct technology ethics.

### 2025/2026 Culture-Related Rubric Reminder

For questions like 2025朝阳一模16 and 丰台一模家风, the user supplied/confirmed rubrics can include broad culture/philosophy angles such as:

- 践行社会主义核心价值观
- 传承中华优秀传统文化 / 中华传统美德
- 坚持理想信念 / 坚持马克思主义指导
- 正确价值观、价值判断和价值选择
- 弘扬民族精神和时代精神
- 筑牢中华民族共同体意识
- 坚持习近平文化思想指导
- 培养家国情怀

Do not force pure-culture points into the philosophy table unless they also carry a philosophy trigger or the user asks for a culture table.

## Current Generated/Extracted Supporting Files

Windows generated support:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\extracted_text\2025_ermo`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\ocr_pages\2025_ermo_haidian_paper`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\extracted_text\2026_yimo`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\ocr_pages\2026_yimo_scan_pages`

These are useful but secondary. The three main artifacts above are the source of continuity.

## Resume Checklist

When a new Codex instance starts:

1. Load this skill.
2. Read `references/operating-rules.md`.
3. Read this file.
4. Open the three current artifacts in `assets/current-artifacts` or synced repo.
5. Ask only if the local source corpus path is unknown; otherwise search automatically.
6. Continue from the explicit blockers above.
7. After new work, update artifacts, update governor board, and commit/push if GitHub sync is configured.
