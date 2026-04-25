# 自动化检测清单

## 必要输入

- `artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `artifacts\北京高考政治错肢库_持续更新版.md`
- `artifacts\必修四文化材料-知识触发总框架_持续更新版.md`
- `reports\governor_board.md`
- `reports\choice_question_processing_ledger.md`
- `reports\必修四哲学_2024-2026题源穷尽清单.md`
- `reports\必修四哲学_STEP_02核心产物审计缺口清单.md`
- `reports\必修四文化_2024-2026题源穷尽清单.md`
- `reports\必修四文化_细则文化题复核队列.md`
- `reports\必修四文化_细则文化题逐题复核表.md`

## 必要输出

- `C:\Users\Administrator\Desktop\必修四哲学材料-知识触发总框架_穷尽修订版.docx`
- `C:\Users\Administrator\Desktop\北京高考政治选择题错肢总结_穷尽版.docx`
- `C:\Users\Administrator\Desktop\必修四文化材料-知识触发总框架_穷尽修订版.docx`
- `reports\overnight_2026-04-25\final_acceptance_report.md`
- `reports\overnight_2026-04-25\rendered_pages\...`

## 必须叫醒继续的条件

- 任一最终 Word 不存在。
- 任一最终 Word 未生成渲染 PNG。
- `DEVELOPMENT_PLAN.md` 仍有未完成 STEP_ID。
- `PROGRESS.md` 中缺少计划里的完成项。
- governor 未说明通过/失败/跳过/阻塞。
- 三份文档只是由旧 Markdown 直接导出，未经过缺口和补丁审查。

## 可以停止的条件

- 三份 Word 存在并渲染通过。
- 所有 STEP_ID 完成，或未完成 STEP_ID 被 governor 明确判定为 `BLOCKED` 且用户要求暂停。
- final acceptance report 写明三份产物路径、渲染证据、阻塞说明和最终结论；只有严格 `PASS` 时才允许末行写 `TASK_COMPLETE`，若为阻塞则必须写 `STRICT_ACCEPTANCE_BLOCKED`。
