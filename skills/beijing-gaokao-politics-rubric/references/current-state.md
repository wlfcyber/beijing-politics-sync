# Current Project State

This file preserves the Windows working state so a Mac Codex session can resume without losing context.

## Main Artifacts

Windows originals:

- `C:\Users\Administrator\Desktop\必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `C:\Users\Administrator\Desktop\北京高考政治错肢库_持续更新版.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\reports\governor_board.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\reports\choice_question_processing_ledger.md`

GitHub sync copies:

- `artifacts/必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `artifacts/北京高考政治错肢库_持续更新版.md`
- `reports/governor_board.md`
- `reports/choice_question_processing_ledger.md`
- `skills/beijing-gaokao-politics-rubric/assets/current-artifacts/*`

## Completion Boundary

### Main-Question Rubric Mapping

- 2025 philosophy main-question/rubric-trigger work is basically cleared for the local corpus, except explicitly excluded no-rubric cases.
- 2026一模 main-question mapping has 16 source-labeled rubric-supported chains.
- 2026朝阳一模第16题 rubric exists in the user-supplied docx and has been corrected into the framework.
- 2026二模 is not a current blocker: the user clarified on 2026-04-23 that the exam has not been held yet, so this batch should stay out of the active queue for now.

### Choice-Question Wrong-Option Library

Current wrong-option library total: 321 reusable patterns.

Sections:

- 2026一模选择题首轮: 12
- 2025二模选择题补充（首轮）: 30
- 2025海淀二模选择题补充: 29
- 2025延庆一模选择题补充: 31
- 2025东城一模选择题补充: 27
- 2026朝阳一模选择题补充: 35
- 2026延庆一模选择题补充: 33
- 2026石景山一模选择题补充: 28
- 2026门头沟一模选择题补充: 30
- 2026顺义一模选择题补充: 33
- 2026海淀一模选择题补充: 33

2026一模 remaining choice-question blockers:

- 2026丰台一模: no reliable objective answer table found locally.
- 2026房山一模: no reliable objective answer table found locally.
- 2026西城一模: paper text is available, but no reliable objective answer table found locally.

Important resolved item:

- 2026海淀一模 paper is scan-only, but rendered pages were read visually and paired with the scoring-standard answer key, so its choice questions were entered without inferred answers.

## Operating Rules To Preserve

- 主观题必须以细则/阅卷细则/评标为核心，不把普通参考答案冒充细则。
- 选择题可以用试题加官方答案表分析错肢。
- 没有答案表的选择题不推测入库。
- 扫描件、图片PDF、旧版Word要自动渲染、转换或读图核查，不能只登记不处理。
- 禁止使用“可替代”“反向筛查”“教学提醒”作为栏目。
- 每条新增错肢或材料触发必须标明来源套卷和题号。
- 每轮结束必须更新监管者。

## Next Work

1. Continue 2025一模选择题补充; 延庆、东城已完成，继续朝阳、海淀、西城、顺义、门头沟、石景山、房山、丰台.
2. Continue 2025期末/期中选择题补充 when paper plus answer table can be confirmed.
3. Continue 2026期末/期中选择题补充.
4. After 2026二模 is actually held and the materials arrive, scan and process them under the same rules.
5. Keep committing/pushing after each substantial update.
