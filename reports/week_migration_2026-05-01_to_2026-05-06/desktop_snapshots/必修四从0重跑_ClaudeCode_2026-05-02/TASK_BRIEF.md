# 必修四从0重跑任务书

本轮唯一任务：让 Claude Code 重新跑一遍必修四哲学宝典，从 0 开始，不继承旧文件、旧结论、旧框架产物、旧审计表、旧脚本输出。

范围以哲学为唯一主线。文化题只可在审计中标为边界排除，不进入最终学生版。

## 必读控制源

- Skill: `/Users/wanglifei/.codex/skills/feige-politics-garden-bixiu4/SKILL.md`
- Skill hard reference: `/Users/wanglifei/.codex/skills/feige-politics-garden-bixiu4/references/philosophy-trigger-standards.md`
- 本地小本本: `/Users/wanglifei/Desktop/北京高考政治/必修四框架重做_2026-04-29/00_飞哥必修四宝典硬性要求记事本.md`
- 总督工令: `/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02/SUPERVISOR_DIRECTIVE_2026-05-02.md`

## 可用题源

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`

## 禁止继承

- 禁止把旧 `artifacts/`、旧 `reports/`、旧 `必修四框架重做_2026-04-29/outputs/`、旧 `audit/`、旧 `qa/`、旧 `PROGRESS.md`、旧脚本生成结果当作证据或内容来源。
- 旧文件只允许作为“禁止继承对象”的路径说明，不允许读取后复写、改写、拼接。
- 不能使用旧 v2/v3 总框架、旧错肢库、旧覆盖表、旧审计索引、旧 ClaudeCode 或 Codex 结论作为内容基础。
- 若为了 OCR/解析效率使用技术性 source-cache，必须回到原始题源核对；缓存结论、旧模型摘要、旧 CSV 判断不能当证据。

## 输出目标

在本目录内重新建立完整工作流和产物：

- `TASK_BRIEF.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `DECISION_LOG.md`
- `PROGRESS.md`
- `GOVERNOR_CHECKLIST.md`
- `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md`
- `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.docx`
- `audit/证据索引.csv`
- `audit/覆盖验收表.csv`
- `audit/问题与边界清单.md`
- `FINAL_ACCEPTANCE_REPORT.md`

最终学生版必须是给高三学生看的可教学成品，不是日志、审计报告、流水账或模型工作记录。
最终学生版只做哲学，不做文化。
