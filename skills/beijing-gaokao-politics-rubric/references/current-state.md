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
- 2026朝阳期中 now includes rubric-supported framework chains for 第18题 and 第20题 from the local `docx` marking files.
- 2026二模 is not a current blocker: the user clarified on 2026-04-23 that the exam has not been held yet, so this batch should stay out of the active queue for now.

### Choice-Question Wrong-Option Library

Current wrong-option library total: 890 reusable patterns.

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
- 2026东城期末选择题补充: 35
- 2026朝阳期中选择题补充: 34
- 2026海淀期末选择题补充: 36
- 2026西城期末选择题补充: 32
- 2026通州期末哲学相关选择题补充: 9
- 2026石景山期末哲学相关选择题补充: 8
- 2025房山一模选择题补充: 37
- 2025海淀一模选择题补充: 32
- 2025石景山一模选择题补充: 32
- 2025门头沟一模选择题补充: 33
- 2025顺义一模选择题补充: 31
- 2025丰台一模选择题补充: 31
- 2026朝阳一模选择题补充: 35
- 2026延庆一模选择题补充: 33
- 2026石景山一模选择题补充: 28
- 2026门头沟一模选择题补充: 30
- 2026顺义一模选择题补充: 33
- 2026海淀一模选择题补充: 33

Dual-output backfill status:

- Already satisfies `错肢库 + 哲学框架` for processed choice suites: 2025二模选择题首轮、2025延庆一模、2025东城一模、2025朝阳一模、2025西城一模、2025丰台一模、2025房山一模、2025海淀一模、2025石景山一模、2025门头沟一模、2025顺义一模、2025东城期末、2025西城期末、2025海淀期末、2025朝阳期末、2025丰台期末、2025海淀二模、2026东城一模选择题首轮、2026东城期末、2026朝阳期中、2026海淀期末、2026西城期末、2026朝阳一模、2026延庆一模、2026石景山一模、2026门头沟一模、2026顺义一模、2026海淀一模.
- Remaining framework-backfill backlog among already processed choice batches: none at this stage.

2026一模 remaining choice-question blockers:

- 2026丰台一模: no reliable objective answer table found locally.
- 2026房山一模: no reliable objective answer table found locally.
- 2026西城一模: paper text is available, but no reliable objective answer table found locally.

Important resolved item:

- 2026海淀一模 paper is scan-only, but rendered pages were read visually and paired with the scoring-standard answer key, so its choice questions were entered without inferred answers.
- 2025海淀期中 local answer key exists in the accompanying `docx`, but the suite still has no stable 必修四 choice-material trigger and no usable philosophy rubric, so it remains honestly excluded instead of being forced into closure.
- 2025丰台一模 now closes within the philosophy boundary: the teacher-version PDF answer key supports 第1-15题 choice processing, two stable philosophy choice chains were merged, and 第16题 was re-checked against `丰台高三一模阅卷细则 2025.docx` as a pure-culture main question that stays outside the philosophy framework.

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

1. Start the `2024` high-evidence framework-first bucket: `东城一模、朝阳一模、海淀一模、丰台一模、石景山一模、西城一模、朝阳二模、东城二模、海淀二模、西城二模`.
2. Continue full choice-line closure where answer sources exist: `2026通州期末、2026海淀期中、2026石景山期末`.
3. For `2026丰台一模 / 房山一模 / 西城一模 / 丰台期末 / 朝阳期末`, only use the fallback path to confirm objective answers; keep the main-question evidence boundary unchanged.
4. After 2026二模 is actually held and the materials arrive, scan and process them under the same rules.
5. Keep committing/pushing after each substantial update.

## 2026-04-24 Inventory Update

- Created `reports/必修四哲学_2024-2026题源穷尽清单.md` as the first full local inventory table for the current philosophy closure task.
- The table currently records `56` suite-level entries: `16` 已闭环, `39` 待补证据, `1` 明确排除.
- `2025海淀期中` remains the only explicit exclusion in the local philosophy queue.
- `2026丰台一模 / 房山一模 / 西城一模 / 丰台期末 / 朝阳期末` are still blocked only on reliable objective answer keys for the choice-question line.
- The next blocker is no longer “find the corpus”, but “audit every unresolved suite against the four durable artifacts and produce the missing-work gap list” for STEP_02.

## 2026-04-24 STEP_02 Audit Update

- Created `reports/必修四哲学_STEP_02核心产物审计缺口清单.md` as the first suite-level missing-work map after the inventory pass.
- The rolling open suite backlog after the latest STEP_03 framework-first closure is split into four actionable buckets:
  - `16` suites: content basically present, pending suite-level acceptance closure only
  - `8` suites: choice-question line still open
  - `0` suites: main-question rubric-chain work still open
  - `15` suites: 2024 entries are inventoried but not yet durably landed in the core philosophy artifacts
- Re-check confirmed that there is currently no remaining backlog of the form “choice wrong-option batch already processed but philosophy correct-option framework chain still missing”.
- The explicit choice-answer-key blockers remain `2026丰台一模 / 房山一模 / 西城一模 / 丰台期末 / 朝阳期末`; these should still use the user-authorized `北京题库` fallback only for objective-answer verification if a reliable paper-with-answer version can be confirmed.
- `2026通州期末` is not an answer-key blocker, but its full 第1-15题 wrong-option line remains open because this round only processed the philosophy-related choice slice.
- `2026海淀期中` now has a confirmed 第22（2） scoring-chain entry, but its full 第1-15题 wrong-option line remains open.
- `2026石景山期末` now has confirmed local `答案及评分参考` on pages 9-10. The framework now includes philosophy-related choice chains for 第2、6、8、9题 and main-question chains for 第18（1）“乡村非遗漫游” and 第20题“永定河治理”. The full 第1-15题 wrong-option line remains open.
- A consistency caveat is now explicit: `choice_question_processing_ledger.md` still uses batch rows for `2025二模选择题补充（首轮）` and `2026一模选择题首轮`, so final suite-level acceptance will need either suite-mapped ledger notes or the acceptance checklist to absorb that mapping.

## Updated Next Work

1. Continue STEP_03 by closing the remaining answer-key-confirmable choice suite `2026朝阳期末` if a reliable objective answer table can be obtained. `2026西城期末` is now closed with 32 wrong-option patterns, 3 choice-framework chains, the existing 第16（2） rubric-supported chain kept in place, and governor review; `2025丰台一模` is now closed with 31 wrong-option patterns, 2 choice-framework chains, a pure-culture 第16题 exclusion re-check, and governor review; `2025丰台二模` is now closed for the philosophy framework with 第16（1）大思政课实践育人链 and 第21题“势”的智慧综合哲学链, while 第16（2）三段论、17法治、18经济、19逻辑/法律、20国政经 remain outside 必修四哲学; `2025房山一模` is now closed with 37 wrong-option patterns, 5 choice-framework chains, and governor review; `2025海淀一模` is now closed with 32 wrong-option patterns, 4 choice-framework chains, 第22题系统观念主观链, and governor review; `2025石景山一模` is now closed with 32 wrong-option patterns, 4 choice-framework chains, 第21题破立关系主观链, and governor review; `2025门头沟一模` is now closed with 33 wrong-option patterns, 12 framework chains, 第16题扩展细则链 and 第21题高质量发展哲学链, and governor review; `2025顺义一模` is now closed with 31 wrong-option patterns, 9 framework chains, 第16题评分细则链, and governor review.
2. For `2026丰台一模 / 房山一模 / 西城一模 / 丰台期末 / 朝阳期末`, only use the fallback path to confirm objective answers; keep the main-question evidence boundary unchanged.
3. `2026丰台期末` now has rubric-supported framework chains for 第16题“留白”和第22题“五年规划”; it remains a choice-question blocker only because no reliable objective answer table has been found locally.
4. `2026通州期末` now has philosophy-related choice backfill for 第5、7、8、9题 plus rubric-supported framework chains for 第16题“都江堰治水智慧”和 第21题“十四五规划”; it remains suite-level pending because only the philosophy-related choice slice, not the full 第1-15题 wrong-option line, has been processed.
5. `2026海淀期中` now has a rubric-supported framework chain for 第22（2）“中华民族伟大复兴势不可挡”; the teacher-version ordinary reference answer was not used by itself as a rubric.
6. Main-question framework-first backlog is now cleared for the 2025-2026 local corpus within the current evidence boundary.
7. Next framework-first target is the `2024` high-evidence bucket: `东城一模、朝阳一模、海淀一模、丰台一模、石景山一模、西城一模、朝阳二模、东城二模、海淀二模、西城二模`.

## 2026-04-24 Supervisor Migration Update

- The Codex App heartbeat automation `四线程督工` has been migrated from the old governor thread to the current governor thread `019dbe09-cc94-73b0-9c5c-f982409d8dfd`.
- `选必一` strict revalidation is now passed under the corrected standard, using `2024朝阳二模 Q20`, `2025西城二模 Q19(2)`, and `2026延庆一模 Q19(2)`.
- `选必二` strict revalidation is now passed under the corrected standard, using `2024朝阳二模 Q17`, `2025西城二模 Q18`, and `2026延庆一模 Q18(1)`.
- `选必三` remains passed after the earlier targeted correction and revalidation.
- `哲学/必修四` remains the only unfinished workflow. Its continuous runner is active on `STEP_03`, so it should not be validated yet.
