# Beijing Politics Project Agent Rules

本项目执行任何代码、资料、题库、评分细则、教学文档、skill 或同步仓库相关任务前，必须先确认需求边界。若有不确定问题，应先向用户追问，直到能按用户要求完成。

## Mandatory Gate

任何 AI 线程、Codex 线程、ClaudeCode 线程或手工脚本，在读取、改写、压缩、同步、交付本项目资料前，必须先经过项目三层 SOP：

1. 项目总管层：读取 `reports/master_governor/latest_master_governor_report.md` 和 `reports/master_governor/PROJECT_GOVERNOR_THREE_LAYER_SOP.md`。
2. 分项 skill 层：读取当前书目/模块对应 skill 及其 hard-rule notebook。
3. 执行任务层：读取当前 run 目录的 `TASK_BRIEF.md`、`DEVELOPMENT_PLAN.md`、`PROGRESS.md`、ledger、governor/acceptance 文件后，只推进一个最小完整步骤。

如果三层 SOP 缺失、报告过期、当前任务没有对应 run/control 文件，先补齐控制文件或写入 `BLOCKED`，不得直接根据记忆或旧成果动资料。

