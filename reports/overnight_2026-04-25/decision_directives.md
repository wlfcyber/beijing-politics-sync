# 2026-04-25 夜间决策指令

## 1. 今晚处理优先级

总权重不变：主观题细则链 > 选择题；同类任务内按海淀、西城、东城、朝阳顺序，再处理郊区；哲学框架优先于错肢总结，文化框架只做独立文化角度，不替代哲学线。

### P0：主观题证据边界和验收收口

先由监管者核验主观题链是否都只来自细则、阅卷细则、评分标准、评标、阅卷报告或用户确认可用的讲评评分文件。普通参考答案不得作为主观题细则。当前记录显示“主观题细则链待迁入或待核”为 0 套，因此今晚不启动大规模重新拆题，只做证据边界复核和套卷级验收收口。

验收顺序：

1. 海淀：优先验收 `2025海淀二模`、`2026海淀一模`；`2025海淀期中`只允许按已找到的细则复核模块边界，不得再以“无细则”为理由排除；`2024海淀期中`属于 OCR/逐题迁入缺口，若有劳动者可处理，排在海淀内部最后。
2. 西城：验收 `2025西城一模`、`2025西城二模`；已闭环的 `2024西城一模`、`2024西城二模`、`2026西城一模`、`2026西城期末`不得重复打开。
3. 东城：验收 `2025东城一模`、`2025东城二模`、`2026东城一模`；已闭环的 `2024东城一模`、`2024东城二模`、`2026东城期末`不得重复打开。
4. 朝阳：验收 `2025朝阳一模`、`2025朝阳二模`、`2026朝阳一模`；已闭环的 `2024朝阳一模`、`2024朝阳期中`、`2024朝阳二模`、`2026朝阳期中`、`2026朝阳期末`不得重复打开。

### P1：选择题客观答案源缺口

选择题只处理三套仍卡住闭环的客观题答案源：

- `2026丰台一模`
- `2026房山一模`
- `2026丰台期末`

这三套的缺口只限客观题答案表，不是主观题细则缺失。可用本地可靠答案表或用户授权的北京题库带答案版本核验客观答案；不得用主观题细则、普通主观参考答案或猜测补客观答案。找不到可靠答案表时，记录为阻塞，不入错肢库。

### P2：文化框架验收和有限补缺

文化线以 `必修四文化_细则文化题逐题复核表.md` 和文化总框架现有 A/B/C 分类为准，不重新扫全库。若有补缺，按主观题和海西东朝权重处理：

1. 先按海淀、西城、东城、朝阳顺序验收已有文化链，不打开已闭环套卷原件，只对照复核表和 artifacts。
2. 朝阳内部再验收已核入链：`2025朝阳期末16`、`2026朝阳期末16`、`2026朝阳一模16`、`2026朝阳期中19/21(1)`。
3. 郊区文化补缺只在主线无阻塞时处理：`2025顺义一模16`、`2025门头沟一模16` 等候选不得挤占哲学主观题和三套客观答案源处理时间。

### P3：Word 生成前置门槛

文档生成角色必须等监管者给出“可导出”信号后才能生成三份桌面 docx。今晚不是先把旧 Markdown 直接转 Word，而是先完成证据边界、缺口和阻塞说明的收口。

## 2. 绝不能重复打开的套卷与仍需处理/验收项

### 绝不能重复打开/重复处理

以下套卷已经套卷级闭环，只允许在最终 Word 导出时引用既有 artifacts 和 reports，不允许再开源文件重做题目、重复入库或重复迁入框架：

- 2024：`东城一模`、`朝阳一模`、`海淀一模`、`丰台一模`、`石景山一模`、`西城一模`、`朝阳期中`、`东城二模`、`海淀二模`、`丰台二模`、`朝阳二模`、`西城二模`。
- 2025：`丰台一模`、`房山一模`、`海淀一模`、`石景山一模`、`门头沟一模`、`顺义一模`、`丰台二模`、`东城期末`、`丰台期末`、`朝阳期末`、`海淀期末`、`西城期末`。
- 2026：`西城一模`、`海淀期中`、`朝阳期中`、`朝阳期末`、`海淀期末`、`石景山期末`、`西城期末`、`东城期末`、`通州期末`。

补充限制：`2024丰台一模` 是正向线和倒序线交汇收口点；任何角色都不得再围绕它启动并行处理。`2026石景山期末` 是唯一无详细评标细则例外，只能表述为“答案及评分参考/方向性证据”，不得改称详细评分细则。

### 仍需处理

- `2026丰台一模`：只找可靠客观答案表；主观细则已在桌面整理目录核到，不再作为细则缺失处理。
- `2026房山一模`：只找可靠客观答案表；主观细则已在桌面整理目录核到。
- `2026丰台期末`：只找可靠客观答案表；第16题、第22题主观链已落地。
- `2024海淀期中`：细则 PDF 已存在；严格同步复核已按细则第3页模块分布排除于必修四主观框架，不再列为主观迁入缺口。
- `2024顺义二模`：细则 docx 已存在，缺口是逐题筛查与迁入。
- `2024门头沟一模`：已补得客观答案源，但主观部分仍只有参考答案/等级描述，保留为二级阻塞。
- `2025海淀期中`：细则 docx 已存在；若保留排除，必须按模块边界复核，不能再写“无细则”。

### 仍需验收收口

这些套卷已有处理痕迹，原则上不重开源文件，只做 artifacts、ledger、清单、governor 的一致性验收：

- 2025：`东城一模`、`延庆一模`、`朝阳一模`、`西城一模`、`东城二模`、`昌平二模`、`朝阳二模`、`海淀二模`、`西城二模`。
- 2026：`东城一模`、`延庆一模`、`朝阳一模`、`海淀一模`、`石景山一模`、`门头沟一模`、`顺义一模`。

## 3. 给其他角色的下一步指令

### 监管者

先做证据矩阵，不做内容扩写。逐项检查三份 artifacts、`choice_question_processing_ledger.md`、哲学题源清单、哲学 STEP_02 缺口清单、文化题源清单、文化逐题复核表、`governor_board.md` 是否一致。发现普通参考答案冒充细则、缺来源套卷题号、缺材料到知识点逻辑链、禁用栏目名时，直接退回对应劳动者。

### 哲学劳动者

不得重新打开已闭环套卷。只处理两类任务：一是对海淀、西城、东城、朝阳 pending 验收套卷做 artifacts 内证据收口；二是如监管者点名 `2024海淀期中`、`2024顺义二模` 可处理，则按细则文件逐题迁入。每条新增链必须写来源套卷、题号、材料信息、知识点、触发逻辑。

### 选择题劳动者

只处理 `2026丰台一模`、`2026房山一模`、`2026丰台期末` 的客观答案源。找到可靠答案表后，才允许进入第1-15题错肢分析和必修四正确项回填；没有可靠答案表就写阻塞，不猜答案。

### 文化劳动者

以文化逐题复核表为主，优先验收已核入 A/B 文化链和朝阳文化链。不得把跨模块价值点混入纯文化主干；A 类必须有明确分值口径，B 类只能写等级细则支持，C/材料识别词不得冒充得分点。

### 补丁者

只修“一个材料触发多个得分点但框架只落一个点”的漏载。修补范围必须由监管者点名，且必须能回到明确细则/评标/阅卷报告。不得为了补丁重做已闭环套卷。

### Word 生成者

等待监管者确认后再导出三份 docx。导出对象只来自已验收 Markdown 和明确阻塞说明，不得新写无来源内容。生成后必须把三份 docx 放到桌面，并交给自动化检测者渲染为 PNG。

### 自动化检测者

检查三份桌面 docx 是否存在、更新时间是否晚于本夜任务、文件大小是否合理、是否能渲染为页面图片。检查 `DEVELOPMENT_PLAN.md` 与 `PROGRESS.md` 的 STEP_ID 是否一致。未满足时必须叫醒主线程继续，不得报完成。

## 4. 验收停止条件

只有同时满足以下条件，主线程才能停止：

1. `DEVELOPMENT_PLAN.md` 的 STEP_01 到 STEP_11 全部在 `PROGRESS.md` 中完成，且没有计划外完成项未解释。
2. 桌面存在三份最终 docx：哲学大框架、选择题错肢总结、文化框架总结。
3. 三份 docx 均已渲染为 PNG 并通过可读性检查。
4. `governor_board.md` 或最终验收报告明确列出通过、失败、跳过、阻塞；三套 2026 客观答案源若未解决，必须在文档和验收报告中诚实标为阻塞，不能伪闭环。
5. 每条新增触发链都有来源套卷、题号、材料信息、知识点/错肢类型、触发逻辑。
6. 主观题没有任何普通参考答案冒充细则的记录。
7. 只有 governor 严格 `PASS` 后，最终验收报告最后一行才允许写 `TASK_COMPLETE`；若仍有未闭合套卷，必须写阻塞结论。

## 5. 本指令依据

本轮已读取：

- `C:\Users\Administrator\.codex\skills\beijing-politics-analyst\SKILL.md`
- `C:\Users\Administrator\.codex\skills\beijing-gaokao-politics-rubric\SKILL.md`
- `C:\Users\Administrator\.codex\skills\beijing-gaokao-politics-rubric\references\operating-rules.md`
- `C:\Users\Administrator\.codex\skills\beijing-gaokao-politics-rubric\references\continuous-codex-control.md`
- `C:\Users\Administrator\.codex\skills\beijing-gaokao-politics-rubric\references\current-state.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\skills\beijing-gaokao-politics-rubric\references\current-state.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\governor_board.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\choice_question_processing_ledger.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\必修四哲学_2024-2026题源穷尽清单.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\必修四哲学_STEP_02核心产物审计缺口清单.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\必修四文化_2024-2026题源穷尽清单.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\必修四文化_细则文化题逐题复核表.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\必修四文化_细则文化题复核队列.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\overnight_2026-04-25\TASK_BRIEF.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\overnight_2026-04-25\DEVELOPMENT_PLAN.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\overnight_2026-04-25\PROGRESS.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\overnight_2026-04-25\automation_monitor_checklist.md`

本轮写入：

- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\overnight_2026-04-25\decision_directives.md`
