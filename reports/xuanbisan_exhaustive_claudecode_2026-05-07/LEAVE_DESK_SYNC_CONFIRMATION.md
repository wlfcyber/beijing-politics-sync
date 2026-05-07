# 离机后同步确认

这份文件是看到用户离开电脑后的追加同步说明。

## 用户最新要求

- 用户已经离开本机，需要在另一台电脑上通过 GitHub 拉取本下午全部成果。
- 不只同步最终学生稿，也要同步 Codex 自己的监督、修补、QA、Governor/Confucius、GitHub 交接说明。
- ClaudeCode 真实跑出的厚内容线、批次输出、P0/P1/P2 重审输出、stdout/stderr、supervisor patch、entries、suite reports 都要保留。
- 本轮依赖的 skill 与流程口径也要同步，避免另一台电脑缺上下文。

## 已追加进入同步包

- `skill_snapshots/feige-politics-garden/`
- `skill_snapshots/feige-politics-garden-xuanbisan/`
- `skill_snapshots/feige-politics-garden-book-orchestrator/`
- `automation_snapshot/claudecode_automation.toml`
- 本文件 `LEAVE_DESK_SYNC_CONFIRMATION.md`

## 拉取后先看

1. `HANDOFF_README.md`
2. `delivery/选必三_逻辑与思维_学生版_框架闭合稿.md`
3. `delivery/选必三_逻辑与思维_学生版_框架闭合稿.docx`
4. `delivery/STUDENT_DELIVERY_QA.md`
5. `governor_confucius/GOVERNOR_CONFUCIUS_PRECHECK.md`
6. `skill_snapshots/feige-politics-garden-xuanbisan/SKILL.md`

## 边界

- 本次仍按二线闭合，不是四线终极。
- 未调用 GPT/Claude 网页外审。
- PDF 因本机 Word COM 导出超时未纳入；DOCX 已渲染 36 页 PNG 并抽查。
