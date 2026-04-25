# THREAD_REGISTRY — 必修四哲学 Claude Code v2

| Role | Agent/Thread ID | Assignment | Write scope | Status | Last report |
|---|---|---|---|---|---|
| 决策者 | claude-code-main / role:决策者 | 定批次与优先级 | HANDOFF_QUEUE / DECISION_LOG | active | threads/决策者.md |
| 监管者 | claude-code-main / role:监管者 | 严格验收 | GOVERNOR_CHECKLIST / FINAL_ACCEPTANCE_REPORT | pending | threads/监管者.md |
| 补丁者 | claude-code-main / role:补丁者 | 多答题点漏归类审查 | threads/补丁者.md / DECISION_LOG | pending | threads/补丁者.md |
| 劳动者 | claude-code-main / role:劳动者 | 套卷处理与资料清点 | SOURCE_LEDGER / COVERAGE_MATRIX / threads/劳动者.md | active | threads/劳动者.md |
| 自动化检测者 | claude-code-main / role:自动化检测者 | 一致性比对 | threads/自动化检测者.md / GOVERNOR_CHECKLIST | pending | threads/自动化检测者.md |

降级说明：本 run 在 Claude Code 单会话内串行执行五角色。原因：母版改动是"形式 + 边界"敏感任务，并行 agent 容易产生覆盖冲突；母版结构必须被严格保护。
