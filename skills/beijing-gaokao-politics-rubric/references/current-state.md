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

Current wrong-option library table row count: 1429 reusable patterns.

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
- 2026通州期末选择题补充: 35
- 2026石景山期末选择题补充: 34
- 2026海淀期中选择题补充: 31
- 2024东城一模哲学相关选择题补充: 8
- 2024东城一模选择题补充（整套收口）: 26
- 2024东城二模选择题补充: 23
- 2024海淀二模选择题补充: 36
- 2024朝阳一模哲学相关选择题补充: 14
- 2024朝阳一模选择题补充（整套收口）: 21
- 2024海淀一模选择题补充: 35
- 2024丰台一模哲学相关选择题补充: 9
- 2024丰台一模选择题补充（整套收口）: 26
- 2024石景山一模选择题补充: 26
- 2024西城一模哲学相关选择题补充: 20
- 2024西城一模选择题补充（整套收口）: 16
- 2024朝阳二模哲学相关选择题补充: 8
- 2024朝阳二模选择题补充（整套收口）: 26
- 2024西城二模选择题补充: 35
- 2024朝阳期中选择题补充: 35
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
- 2026西城一模选择题补充: 34

Dual-output backfill status:

- Already satisfies `错肢库 + 哲学框架` for processed choice suites/slices: 2025二模选择题首轮、2025延庆一模、2025东城一模、2025朝阳一模、2025西城一模、2025丰台一模、2025房山一模、2025海淀一模、2025石景山一模、2025门头沟一模、2025顺义一模、2025东城期末、2025西城期末、2025海淀期末、2025朝阳期末、2025丰台期末、2025海淀二模、2026东城一模选择题首轮、2026东城期末、2026朝阳期中、2026朝阳期末、2026海淀期中、2026海淀期末、2026石景山期末、2026西城期末、2026通州期末、2026西城一模、2026朝阳一模、2026延庆一模、2026石景山一模、2026门头沟一模、2026顺义一模、2026海淀一模、2024东城一模、2024朝阳一模、2024海淀一模、2024丰台一模、2024石景山一模、2024西城一模、2024朝阳期中、2024朝阳二模、2024海淀二模、2024西城二模.
- Remaining framework-backfill backlog among already processed choice batches: none at this stage.

2026一模 / 2026期末 remaining choice-question blockers:

- 2026丰台一模: no reliable objective answer table found locally.
- 2026房山一模: no reliable objective answer table found locally.
- 2026丰台期末: no reliable objective answer table found locally.

Rubric-source correction from the user on 2026-04-25:

- Use the organized desktop corpus as source of truth: `C:\Users\Administrator\Desktop\2024各区模拟题`, `C:\Users\Administrator\Desktop\2025各区模拟题`, and `C:\Users\Administrator\Desktop\2026各区模拟题`.
- Except `2026石景山期末`, every suite should be treated as having rubric/marking-rule evidence until the corresponding desktop `细则` folder has been checked directly.
- The three remaining 2026 blockers above are objective-answer-table blockers only; they are not main-question rubric blockers. Desktop checks show `2026丰台一模细则.pptx`, `2026房山一模细则.docx`, and `2026丰台期末细则.pdf` exist in the organized corpus.
- `2026石景山期末` is the sole no-detailed-rubric exception. Its PDF has `答案及评分参考`, but that must be described as scoring-direction/reference evidence, not detailed评标细则.

Important resolved item:

- 2026西城一模 now closes at suite level: the objective answer source is `2026北京西城高三一模政治.pdf` page 10, titled “思想政治答案及评分参考”, visually verified by the governor; 第1-15题答案为 `1B 2C 3B 4D 5C 6D 7B 8C 9A 10D 11D 12B 13A 14A 15D`; 34 reusable wrong-option patterns were added and 第1、5、6、7题 stable 必修四 correct-option chains were backfilled.
- 2024朝阳二模 now closes at suite level: local paper PDF, answer docx and main-question marking-summary PDF were rechecked; 第1-15题答案为 `1B 2C 3B 4A 5D 6C 7D 8A 9D 10C 11B 12C 13B 14D 15D`; the existing 第1、2、4、6题 philosophy/culture slice remains, 26 reusable wrong-option patterns were added for 第3、5、7-15题, and no additional stable 必修四 correct-option trigger was found in those remaining questions.
- 2024西城二模 now closes at suite level: local paper docx, answer docx and answer-rubric docx were rechecked; 第1-15题答案为 `1B 2D 3D 4D 5C 6D 7A 8C 9B 10B 11B 12A 13C 14A 15C`; 35 reusable wrong-option patterns were added, 第1、2、7、8、9题 stable 必修四/文化 correct-option chains were backfilled, and existing 第17、18（4） rubric-supported main-question chains remain valid.
- 2024朝阳期中 now closes at suite level: local paper PDF and `阅卷细则总.rtf` were rechecked; 第1-15题答案为 `1B 2D 3D 4C 5A 6C 7B 8D 9B 10D 11C 12C 13C 14A 15B`; 35 reusable wrong-option patterns were added, 第1、2、3、4、5、6、10题 stable 必修四/文化 correct-option chains were backfilled, and existing 第16、17题 rubric-supported main-question chains remain valid.
- 2024西城一模 now closes at suite level: local paper docx, answer docx and adjusted rubric docx were rechecked; 第1-15题答案为 `1C 2A 3D 4B 5B 6C 7A 8D 9D 10A 11B 12C 13B 14A 15C`; 16 reusable wrong-option patterns were added for 第5、6、7、8、11、13、14题, making 36 total with the existing philosophy/culture slice. No additional stable 必修四 correct-option chain was found in those newly closed questions; existing 第1、2、3、4、9、10、12、15题 chains and 第17题 rubric chain remain valid.
- 2026海淀一模 paper is scan-only, but rendered pages were read visually and paired with the scoring-standard answer key, so its choice questions were entered without inferred answers.
- 2025海淀期中 local answer key exists in the accompanying `docx`, and the organized desktop folder now confirms `2025海淀期中细则.docx` exists. The older “no usable philosophy rubric” wording is withdrawn. It remains tentatively excluded only on the earlier module-boundary judgment that no stable 必修四 choice-material trigger or usable philosophy item was found; final acceptance must re-check the rubric before preserving that exclusion.
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

1. Forward and reverse philosophy lines met at `2024丰台一模`; the merged closeout is now recorded, so neither line should reopen that suite.
2. Continue full choice-line closure only on remaining evidence gaps: `2024朝阳期中` is now closed and must not be reopened; `2024丰台二模` remains blocked on a reliable objective answer source.
3. For `2026丰台一模 / 房山一模 / 丰台期末`, only use the fallback path to confirm objective answers; keep the main-question evidence boundary unchanged.
4. After 2026二模 is actually held and the materials arrive, scan and process them under the same rules.
5. Keep committing/pushing after each substantial update.

## 2026-04-24 Inventory Update

- Created `reports/必修四哲学_2024-2026题源穷尽清单.md` as the first full local inventory table for the current philosophy closure task.
- The table currently records `56` suite-level entries: `32` 已闭环, `23` 待补证据, `1` 明确排除.
- `2025海淀期中` remains the only explicit exclusion in the local philosophy queue.
- `2026丰台一模 / 房山一模 / 丰台期末` are still blocked on reliable objective answer keys for the choice-question line; `2024丰台二模` has been unblocked by the saved evidence PDF page 8 objective-answer source, and `2026西城一模` has been unblocked by the PDF page 10 answer-and-scoring-reference source.
- The next blocker is no longer “find the corpus”, but “audit every unresolved suite against the four durable artifacts and produce the missing-work gap list” for STEP_02.

## 2026-04-24 STEP_02 Audit Update

- Created `reports/必修四哲学_STEP_02核心产物审计缺口清单.md` as the first suite-level missing-work map after the inventory pass.
- The rolling open suite backlog after the latest STEP_03 closure is split into four actionable buckets:
  - `16` suites: content basically present, pending suite-level acceptance closure only
  - `3` suites: choice-question line still open or lacks reliable objective answer source
  - `0` suites: main-question rubric-chain work still open
  - `3` suites: 2024 entries are inventoried but not yet durably landed in the core philosophy artifacts
- Re-check confirmed that there is currently no remaining backlog of the form “choice wrong-option batch already processed but philosophy correct-option framework chain still missing”.
- The explicit choice-answer-key blockers remain `2026丰台一模 / 房山一模 / 丰台期末`; these should still use reliable objective-answer verification only, without turning ordinary main-question references into rubrics. `2024丰台二模` has been unblocked by the saved objective-answer evidence PDF.
- `2026通州期末` now has full 第1-15题 wrong-option closure, with 35 reusable patterns and suite-level `已闭环`.
- `2026海淀期中` now has full 第1-15题 wrong-option closure with 31 reusable patterns, no additional stable 必修四 choice trigger requiring merge, and suite-level `已闭环` on the strength of the existing 第22（2） scoring-chain entry.
- `2026石景山期末` now has full 第1-15题 wrong-option closure, with 34 reusable patterns and suite-level `已闭环`; the framework includes 第1、2、6、8、9题 philosophy/culture choice chains and main-question chains for 第18（1）“乡村非遗漫游” and 第20题“永定河治理”.
- `2026西城一模` now has full 第1-15题 wrong-option closure, with 34 reusable patterns and suite-level `已闭环`; the framework includes 第1、5、6、7题 stable 必修四 correct-option chains and keeps the existing 第16、21题主观细则链.
- `2024东城一模` is now suite-level closed. The scanned paper and answer PDF were rendered and read locally; the answer key is `1C 2B 3A 4A 5D 6D 7A 8D 9B 10C 11A 12B 13D 14C 15C`. The framework includes 第1、2、3、15题 choice correct-option chains and main-question chains for 第16题文明交流、第18（1）新质生产力 and 第21题首都都市圈; the wrong-option library has 34 reusable patterns across its philosophy-related and whole-suite closure rows.
- `2024朝阳一模` is now suite-level closed. The paper PDF, answer docx and choice-lecture PPT were rechecked; 第1-15题答案为 `1B 2C 3B 4A 5A 6B 7C 8D 9D 10C 11B 12C 13D 14A 15C`. The existing 第1、2、3、4、5、9题 philosophy/culture slice remains, 21 reusable wrong-option patterns were added for 第6、7、8、10-15题, and 第8题 stable 必修四 correct-option chain was backfilled while 第6、7、10-15题 were kept outside the framework by module boundary.
- `2024海淀一模` is now suite-level closed. The framework keeps the philosophy/culture choice chains for 第1、2、3、4、5题 and the main-question chain for 第16题“梦舟/揽月/登陆月球何以自信”; the full 第1-15题 wrong-option line has been completed with no additional stable 必修四 correct-option trigger found in 第6-15题.
- `2024丰台一模` is now suite-level closed after the forward and reverse lines met there. The framework keeps philosophy/culture choice chains for 第1、2、8、9题 and main-question chains for 第18（1）“新质生产力”、第21题“全人类共同价值”; the full 第1-15题 wrong-option line adds 26 rows for 第3、4、5、6、7、10-15题, giving 35 total reusable wrong-option patterns. 第3、4、5、6、7、10-15题 were reviewed with no additional stable 必修四 correct-option trigger.
- `2024石景山一模` is now suite-level closed. The framework keeps the philosophy/culture choice chains for 第2、3、4、5题 and the main-question chains for 第16题“习近平文化思想举旗定向”、第20题“中国式现代化战略性有利条件”; the full 第1-15题 wrong-option line has been completed with no additional stable 必修四 correct-option trigger found in 第1、6-15题.
- `2024东城二模` is now suite-level closed. The scanned paper and scanned answer table were rendered and read locally; the answer key is `1D 2B 3B 4A 5C 6C 7A 8C 9B 10D 11D 12C 13B 14A 15A`. The framework includes 第1、2、3、11题 choice correct-option chains, 第16题“桑基鱼塘仍未老”, 第18（2）题“新就业形态劳动关系”, and 第21题“战略性有利条件”; the wrong-option library adds 23 reusable patterns.
- `2024海淀二模` is now suite-level closed. 试题 docx/PDF 与两份答案 docx 已核；第1-15题答案为 `1C 2D 3C 4B 5A 6C 7D 8B 9D 10B 11A 12B 13A 14C 15D`。The framework includes 第1、2、3、4、15题 choice correct-option chains, 第16题“以调频促同频”、第17题调查研究认识链、第21题“循新出发”；the wrong-option library adds 36 reusable patterns.
- `2024西城二模` is now suite-level closed. 本地试卷 docx、答案 docx 与答案细则 docx 已核；第1-15题答案为 `1B 2D 3D 4D 5C 6D 7A 8C 9B 10B 11B 12A 13C 14A 15C`；wrong-option library adds 35 reusable patterns. The framework includes 第1、2、7、8、9题 choice correct-option chains, plus rubric-supported main-question chains for 第17题社会基本矛盾/改革 and 第18（4）题规律能动性、矛盾特殊性、系统优化、人民群众、价值判断与价值选择.
- `2024朝阳期中` is now suite-level closed. `阅卷细则总.rtf` 文末客观答案表确认第1-15题答案为 `1B 2D 3D 4C 5A 6C 7B 8D 9B 10D 11C 12C 13C 14A 15B`; wrong-option library adds 35 reusable patterns; the framework includes 第1、2、3、4、5、6、10题 choice correct-option chains and rubric-supported 第16、17题 main-question chains. 第18-20题按逻辑、创新思维、经济/国政经边界排除。
- `2024丰台二模` now closes at suite level after the 2026-04-25 host-computer continuation. The objective answer key was verified from the saved evidence PDF `reports/evidence_2024_fengtai_ermo_answer.pdf` page 8: `1D 2B 3A 4C 5A 6B 7B 8C 9D 10C 11C 12B 13D 14D 15A`; 34 reusable wrong-option patterns were added, and 第1、10、11、12、13题 stable 必修四/文化 correct-option chains were backfilled. Its earlier framework-first main-question chains remain: 第18（2）从实际出发/具体问题具体分析/尊重规律，第20题联系、矛盾、认识发展，第21题整体部分、量变质变、价值观导向、人生价值；第16、17、18（1）、18（3）、19按模块边界排除.
- `2024西城一模` is now suite-level closed. The framework keeps philosophy/culture choice chains for 第1、2、3、4、9、10、12、15题 and the rubric-supported main-question chain for 第17题“避免人类中心主义”; the full 第1-15题 wrong-option line has been completed with 36 reusable patterns across the 20-row philosophy/culture slice and the 16-row whole-suite closure; 第5、6、7、8、11、13、14题 were reviewed with no additional stable 必修四 correct-option trigger.
- `2024朝阳二模` is now suite-level closed. The framework keeps philosophy/culture choice chains for 第1、2、4、6题 and rubric-supported main-question chains for 第16（2）题“人与人工智能相互塑造”、第19（3）题“中华优秀传统文化赋予中国式现代化深厚底蕴”. The full 第1-15题 wrong-option line is complete with 34 reusable patterns across the 8-row philosophy slice and the 26-row whole-suite closure; 第3、5、7-15题 were reviewed with no additional stable 必修四 correct-option trigger.
- A consistency caveat is now explicit: `choice_question_processing_ledger.md` still uses batch rows for `2025二模选择题补充（首轮）` and `2026一模选择题首轮`, so final suite-level acceptance will need either suite-mapped ledger notes or the acceptance checklist to absorb that mapping.

## Updated Next Work

1. Continue STEP_03 by closing remaining evidence gaps without overlap: `2024丰台一模`, `2024朝阳期中`, and `2024丰台二模` are closed and must not be reopened by either line. `2024东城一模`、`2024朝阳一模`、`2024海淀一模`、`2024丰台一模`、`2024石景山一模`、`2024西城一模`、`2024朝阳期中`、`2024东城二模`、`2024海淀二模`、`2024丰台二模`、`2024朝阳二模`、`2024西城二模`、`2026海淀期中`、`2026朝阳期末`、`2026石景山期末` and `2026西城一模` are now suite-level closed.
2. For `2026丰台一模 / 房山一模 / 丰台期末`, only use the fallback path or other reliable source to confirm objective answers; keep the main-question evidence boundary unchanged.
3. `2026丰台期末` now has rubric-supported framework chains for 第16题“留白”和第22题“五年规划”; it remains a choice-question blocker only because no reliable objective answer table has been found locally.
4. `2026通州期末` now has full 第1-15题 choice wrong-option closure plus rubric-supported framework chains for 第16题“都江堰治水智慧”和 第21题“十四五规划”; it is suite-level `已闭环`.
5. `2026海淀期中` now has full 第1-15题 wrong-option closure plus the rubric-supported 第22（2）“中华民族伟大复兴势不可挡” chain; the teacher-version ordinary reference answer was not used by itself as a rubric.
6. Main-question framework-first backlog is now cleared for the 2025-2026 local corpus within the current evidence boundary.
7. Do not let the forward and reverse lines duplicate work; they have met at `2024丰台一模`, so the merged closeout is the final shared state for that suite. Continue any remaining work with one line only.

## 2026-04-25 Host Continuation Update

- `2024丰台二模` is now suite-level closed, not a remaining answer-source blocker. The saved evidence PDF `reports/evidence_2024_fengtai_ermo_answer.pdf` page 8 provided the objective answer table `1D 2B 3A 4C 5A 6B 7B 8C 9D 10C 11C 12B 13D 14D 15A`.
- Wrong-option library count is now `1429` reusable rows after adding the 34-row `2024丰台二模选择题补充` batch.
- Philosophy framework now includes `2024丰台二模套卷级三线闭环`, with 第1、10、11、12、13题 correct-option trigger chains and the prior rubric-supported 第18（2）、20、21 main-question chains preserved.
- Source inventory now reads `已闭环 33 / 待补证据 22 / 明确排除 1`; STEP_02 choice-answer-source blockers are now only `2026丰台一模 / 2026房山一模 / 2026丰台期末`.
- `哲学/必修四` remains on `STEP_03`; do not validate, do not create the final full-score teaching manuscript, and do not mark `TASK_COMPLETE` until the remaining three answer-source blockers are resolved or honestly closed as blockers and strict acceptance passes.

## 2026-04-25 User Rubric-Source Correction

- User clarified: except `2026石景山期末`, all suites have rubrics/marking rules. Future work must not conclude “no rubric” until the organized desktop three-year mock folders have been checked.
- The authoritative local source roots are now the organized folders on Desktop:
  - `C:\Users\Administrator\Desktop\2024各区模拟题`
  - `C:\Users\Administrator\Desktop\2025各区模拟题`
  - `C:\Users\Administrator\Desktop\2026各区模拟题`
- Verified immediately after the correction: `2026丰台一模`, `2026房山一模`, `2026丰台期末`, `2025海淀期中`, `2024顺义二模`, and `2024海淀期中` all have `细则` files in those organized folders. Their remaining blockers are answer-table/OCR/逐题迁入/module-boundary issues, not rubric existence.
- Verified exception: `2026石景山期末` has an empty `细则` folder and only the paper PDF with `答案及评分参考`; keep it as the only no-detailed-rubric exception.

## 2026-04-24 Culture-Line Parallel State

- A separate culture trigger artifact now exists at `artifacts/必修四文化材料-知识触发总框架_持续更新版.md`, with the user-corrected top-level structure: `0载体 / 1特点 / 2作用 / 3横向 / 4纵向 / 5建设文化强国与文化自信 / 6民族精神 / 7坚持习近平文化思想`.
- The culture inventory exists at `reports/必修四文化_2024-2026题源穷尽清单.md`, and the continuous-task notes live under `reports/continuous_jobs/必修四文化_三年题源穷尽触发框架/`.
- Culture line boundary: it records pure-culture items and culture angles inside mixed philosophy-and-culture questions; it does not replace the philosophy framework, wrong-option library, or philosophy suite inventory.
- Culture terminology has been tightened: only terms with explicit original scoring support may be treated as scoring terms; the culture artifact now separates `逐点标分术语`, `等级细则支持术语`, and `材料识别词`.
- Current culture table has `28` source-labeled trigger chains after the user-corrected 0-7 reorganization. Next culture-line targets are `2025顺义一模16`、`2025门头沟一模16`、`2025朝阳期末16`、`2026朝阳期末16`, but the active urgent priority remains finishing the philosophy knowledge-trigger framework.

## 2026-04-24 Supervisor Migration Update

- The Codex App heartbeat automation `四线程督工` has been migrated from the old governor thread to the current governor thread `019dbe09-cc94-73b0-9c5c-f982409d8dfd`.
- `选必一` strict revalidation is now passed under the corrected standard, using `2024朝阳二模 Q20`, `2025西城二模 Q19(2)`, and `2026延庆一模 Q19(2)`.
- `选必二` strict revalidation is now passed under the corrected standard, using `2024朝阳二模 Q17`, `2025西城二模 Q18`, and `2026延庆一模 Q18(1)`.
- `选必三` remains passed after the earlier targeted correction and revalidation.
- `哲学/必修四` remains the only unfinished workflow. It is still on `STEP_03`, so it should not be validated yet.

## 2026-04-24 GitHub Handoff Update

- This sync round is for continuing on the home computer. The lightweight Markdown artifacts, skill state, governor records, and continuous-job progress have been staged for GitHub.
- `选必一`、`选必二`、`选必三` are preserved as completed/revalidated artifacts under `artifacts/`, with their job notes under `reports/continuous_jobs/`.
- The latest durable philosophy artifacts remain in the sync repository, not the older desktop root copies: `artifacts/必修四哲学材料-知识触发总框架_持续更新版_v2.md`, `artifacts/北京高考政治错肢库_持续更新版.md`, `reports/governor_board.md`, and matching `skills/.../assets/current-artifacts/` copies.
- A local process check at `2026-04-24 20:18 CST` did not find a live continuous runner. On the next computer, continue `哲学/必修四` from `reports/continuous_jobs/哲学必修四_三线闭环穷尽满分课/PROGRESS.md`, currently `STEP_03`, before final validation.

## 2026-04-24 Continuous-Control Handoff Update

- The user's reusable long-task prompts have been consolidated into `skills/beijing-gaokao-politics-rubric/references/continuous-codex-control.md`.
- The new-computer absorption prompt is stored at `skills/beijing-gaokao-politics-rubric/references/new-computer-absorb-prompt.md`.
- `SKILL.md` now instructs Codex to read the continuous-control protocol before long-running, resumed, multi-step, delegated, or governor-supervised work.
- The current local Codex skill should be refreshed from the synced `skills/beijing-gaokao-politics-rubric` folder after pulling on any device.
