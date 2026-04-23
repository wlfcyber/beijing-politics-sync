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

Current wrong-option library total: 540 reusable patterns.

Sections:

- 2026一模选择题首轮: 12
- 2025二模选择题补充（首轮）: 30
- 2025海淀二模选择题补充: 29
- 2025延庆一模选择题补充: 31
- 2025东城一模选择题补充: 27
- 2025朝阳一模选择题补充: 30
- 2025西城一模选择题补充: 33
- 2025东城期末选择题补充: 29
- 2025西城期末选择题补充: 29
- 2025海淀期末选择题补充: 33
- 2025朝阳期末选择题补充: 34
- 2025丰台期末选择题补充: 31
- 2026朝阳一模选择题补充: 35
- 2026延庆一模选择题补充: 33
- 2026石景山一模选择题补充: 28
- 2026门头沟一模选择题补充: 30
- 2026顺义一模选择题补充: 33
- 2026海淀一模选择题补充: 33

Dual-output backfill status:

- Already satisfies `错肢库 + 哲学框架` for processed choice suites: 2025二模选择题首轮、2025延庆一模、2025东城一模、2025朝阳一模、2025西城一模、2025东城期末、2025西城期末、2025海淀期末、2025朝阳期末、2025丰台期末、2025海淀二模、2026东城一模选择题首轮、2026朝阳一模、2026延庆一模、2026石景山一模、2026门头沟一模、2026顺义一模、2026海淀一模.
- Remaining framework-backfill backlog among already processed choice batches: none at this stage.

2026一模 remaining choice-question blockers:

- 2026丰台一模: no reliable objective answer table found locally.
- 2026房山一模: no reliable objective answer table found locally.
- 2026西城一模: paper text is available, but no reliable objective answer table found locally.

Important resolved item:

- 2026海淀一模 paper is scan-only, but rendered pages were read visually and paired with the scoring-standard answer key, so its choice questions were entered without inferred answers.

## Operating Rules To Preserve

- 主观题必须以细则/阅卷细则/评标为核心，不把普通参考答案冒充细则。
- 选择题可以用试题加官方答案表分析错肢。
- 选择题中的哲学相关正确项，不能只停留在错肢库；还必须按“材料信息—原理/方法论—逻辑链—来源题号”回填到哲学总框架。
- 没有答案表的选择题不推测入库。
- 本地缺失客观题答案表时，可用用户授权的“北京题库”补找带答案版本，但仅限客观题答案核对，不把其主观题答案冒充细则。
- 扫描件、图片PDF、旧版Word要自动渲染、转换或读图核查，不能只登记不处理。
- 禁止使用“可替代”“反向筛查”“教学提醒”作为栏目。
- 每条新增错肢或材料触发必须标明来源套卷和题号。
- 每轮结束必须更新监管者。

## Next Work

1. Continue 2025期末/期中 choice-question supplementation by checking whether `海淀期中` has any confirmable objective answer source and stable philosophy-related choice material; if not, keep it honestly excluded.
2. Continue 2026期末/期中 choice-question supplementation for answer-key-confirmable suites such as `东城、朝阳、海淀、西城期末` and `朝阳期中`.
3. Continue 2025一模 choice-question supplementation for the remaining suites `海淀、顺义、门头沟、石景山、房山、丰台`, only after each finished suite has both outputs: wrong-option library + philosophy framework chain.
4. For 2026丰台、房山、西城一模 choice questions, use the user-authorized `北京题库` fallback only if a reliable paper-with-answer version can be confirmed.
5. After 2026二模 is actually held and the materials arrive, scan and process them under the same rules.
6. Keep committing/pushing after each substantial update.
