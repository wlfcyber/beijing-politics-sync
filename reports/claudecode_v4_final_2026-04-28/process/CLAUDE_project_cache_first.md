# Claude Code 独立重跑规则

## 2026-04-28 接管修订：cache-first 优先

本文件最初用于防止模型抄旧结论。现在根据用户最新要求，规则必须精确区分：

- 旧分析结论、旧框架条目、旧 CSV 判断、旧 candidate JSON、旧模型总结，仍然不得当作证据。
- 但从原始试卷、答案、细则转换出来的 txt、suite bundle、manifest、render 图片、可读缓存，是一手来源缓存，必须优先使用。
- 如果缓存为空、缺页、不可读、无法确认完整设问/材料/答案键/细则边界，再回到原始 PDF/PPT/Word 文件。
- 已经渲染过的 scan-only 页面不要重复渲染；直接读已有 render 图片。
- 审计文件可以记录缓存路径、原始路径、页码和证据状态；学生最终版不得出现路径、F04、L24、slide、OCR/debug log。

本次继续工作时，优先遵守本“2026-04-28 接管修订”。下方早期规则中关于“禁止读取任何缓存、同步仓库、旧工程”的表述，只保留为“禁止引用旧结论”的安全提醒，不再禁止读取一手来源缓存和接管指令。

你正在进行一次全新的、从零开始的“必修四哲学与文化-哲学部分”重跑。

## 绝对目标

只基于本机三年模拟题原始资料，重新穷尽北京各区 2024、2025、2026 模拟题中与必修四哲学相关的选择题、主观题、评分细则、评标、阅卷总结，独立生成新的材料-知识触发框架、错肢库、题源清单和验收报告。

## 允许读取的来源

你只允许读取以下三个原始资料目录，以及你在本工作区自己创建的文件：

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27`

## 禁止读取或引用的资料

以下路径和资料全部禁止读取、引用、复用、对照或抄写：

- `/Users/wanglifei/Desktop/北京高考政治`
- `/Users/wanglifei/GaokaoPolitics`
- 任何 `beijing-politics-sync` 文件
- 任何 `data/preprocessed_corpus`、`gpt_suite_bundles`、`gpt_sources`
- 任何 `必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- 任何 v2/v3、Codex、ClaudeCode 旧报告、旧框架、旧错肢库、旧题源清单
- 任何来自旧工程的 governor、ledger、progress、summary

如果你发现自己误读了禁止路径，立刻停止，把污染路径写入 `CONTAMINATION_REPORT.md`，不得继续生成正文。

## 证据规则

- 主观题哲学触发链只可依据评分细则、评标、阅卷总结、明确给分口径。
- 普通参考答案、教师版答案、答案及评分参考，只能作为 reference-only，不得冒充细则。
- 选择题必须同时具备题面和可靠客观答案表，才能分析正确项触发和错肢。
- 扫描 PDF、图片、旧 doc、不可读文件必须尝试转换、渲染、OCR 或读取；仍不可读时标 `ocr-needed` 或 `conversion-needed`，不得假装已核。
- 每条触发必须写清：来源套卷、题号、题型、原题/细则证据摘录、材料信息、触发知识、为什么支撑。
- 若来源题号本身不支撑某哲学原理，必须写 `not-supported`，不得用泛化解释硬挂。

## 必修四哲学范围

以高中《哲学与文化》哲学部分为范围，优先包括：

- 唯物论：物质与意识、一切从实际出发、实事求是、主观能动性、尊重客观规律与发挥主观能动性、规律客观性。
- 辩证法：联系、发展、矛盾、整体与部分、系统观念、量变质变、适度、辩证否定、具体问题具体分析、两点论重点论等。
- 认识论：实践与认识、认识发展、真理观。
- 历史唯物主义：社会存在与社会意识、社会基本矛盾、改革、人民群众。
- 价值观人生观：价值观导向、价值判断与价值选择、实现人生价值。

文化题只在哲学评分点明确出现时纳入哲学框架；纯文化知识另标 `module-boundary-cultural`，不要混入哲学。

## 必交付物

全部输出写入 `outputs/`：

- `FILE_INVENTORY.csv`：三年模拟题全部文件清单，含 year、suite、path、file_type、read_status。
- `SOURCE_LEDGER.csv`：每套题的试卷、答案表、细则/评标/阅卷总结状态。
- `PHILOSOPHY_FRAMEWORK_INDEPENDENT.md`：独立生成的必修四哲学材料-知识触发框架。
- `PHILOSOPHY_FRAMEWORK_ENTRIES.csv`：逐条框架结构化表。
- `CHOICE_WRONG_OPTION_LIBRARY.md`：独立错肢库。
- `CHOICE_REVIEW.csv`：选择题逐题核验表。
- `SUBJECTIVE_REVIEW.csv`：主观题逐题核验表。
- `SOURCE_GAPS.md`：缺答案表、缺细则、OCR 阻塞、模块边界、reference-only 清单。
- `PROGRESS.md`：持续进度。
- `FINAL_ACCEPTANCE_REPORT.md`：只有全部验收通过才可写完成；否则写未完成边界。

## 完成门槛

不得写 `TASK_COMPLETE`，除非全部满足：

- 三年模拟题原始文件已完整 inventory。
- 每套题的试卷、答案表、细则/评标/阅卷总结状态明确。
- 所有可读来源已处理，所有不可读来源有明确阻塞原因。
- 选择题没有缺答案键却被分析为闭环的情况。
- 主观题没有普通参考答案冒充细则的情况。
- 最终框架每条都有可回源摘录。
- `SOURCE_GAPS.md` 中没有未解释的空白项。

宁可少收，不可幻觉。
