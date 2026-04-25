# 2026-04-25 夜间闭环任务简报

## 终极目标

明早桌面上必须有三份可打开、可教学使用的 Word 文档：

1. `C:\Users\Administrator\Desktop\必修四哲学材料-知识触发总框架_穷尽修订版.docx`
2. `C:\Users\Administrator\Desktop\北京高考政治选择题错肢总结_穷尽版.docx`
3. `C:\Users\Administrator\Desktop\必修四文化材料-知识触发总框架_穷尽修订版.docx`

## 工作区

- 同步仓库：`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`
- 核心 artifacts：`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\artifacts`
- 监管与审计：`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports`
- 三年套卷源：
  - `C:\Users\Administrator\Desktop\2024各区模拟题`
  - `C:\Users\Administrator\Desktop\2025各区模拟题`
  - `C:\Users\Administrator\Desktop\2026各区模拟题`
- 用户给的过程性 Word：
  - `C:\Users\Administrator\Documents\xwechat_files\wxid_4y3r1odupy3e12_ec31\msg\file\2026-04\必修四哲学材料-知识触发总框架_持续更新版_v2.docx`

## 权重

1. 大题/主观题细则链优先于选择题。
2. 同一任务内，按海淀、西城、东城、朝阳优先，再处理郊区。
3. 哲学框架优先于错肢总结，错肢总结与文化框架并行推进。

## 证据规则

- 主观题只认细则、阅卷细则、评分标准、评标、阅卷报告、用户确认可用的讲评评分文件。
- 普通参考答案不能冒充细则。
- 选择题必须有可靠客观答案表；没有答案表不推测。
- 扫描件、图片 PDF、旧 Word、PPT 必须尽量转写、OCR、渲染或读图，不得懒挂 pending。
- 每条新增材料触发或错肢模式必须有来源套卷和题号。
- 材料触发必须有材料信息到知识点/答题点的逻辑链。
- 禁止作为栏目名使用：`可替代`、`反向筛查`、`教学提醒`。

## 角色

- 决策者：决定下一步优先级和停止条件。
- 监管者：审核证据、来源、逻辑链、计划进度一致性。
- 补丁者：检查一个材料触发多个答题点但只落一个框架点的漏收。
- 劳动者-哲学：审查哲学主观题细则链和选择题正确项触发链。
- 劳动者-选择：审查错肢库和剩余客观答案源缺口。
- 劳动者-文化：审查文化框架和文化题穷尽缺口。
- 自动化检测者：由主线程承担，检查文件存在、时间戳、大小、渲染证据、计划进度一致性。

## 完成标准

任务只有在以下条件全部满足时才允许停止：

- `DEVELOPMENT_PLAN.md` 中全部 STEP_ID 在 `PROGRESS.md` 中完成。
- 三份最终 Word 均存在于桌面，大小合理，且更新时间晚于本任务开始。
- 三份 Word 均已渲染为页面图片并通过视觉检查。
- governor 记录明确列出通过、失败、跳过、阻塞；未解决项不得隐藏。
- 三份文档的内容均来自已有 artifacts 和经审查可合并补充，不编造来源。
- 最后一行验收报告只有在严格 `PASS` 时才允许写 `TASK_COMPLETE`；若存在未闭合套卷或 governor `BLOCKED`，必须写阻塞结论而不是完成标记。
