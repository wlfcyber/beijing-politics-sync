# THREAD_REGISTRY

| Role | Agent/Thread ID | Assignment | Write scope | Status | Last report |
| --- | --- | --- | --- | --- | --- |
| 决策者 | main Codex thread | Keep run boundary and next-step decisions | `00_control/DECISION_LOG.md` | completed_with_blockers | `00_control/DECISION_LOG.md` |
| 资料组织者 | main Codex thread | Build source inventory | `01_source_inventory/`, `00_control/SOURCE_LEDGER.csv` | completed | `01_source_inventory/source_inventory_summary.md` |
| 劳动者 | main Codex thread | Build question candidates and preliminary labels | `03_question_index/`, `04_module_classification/` | completed_with_blockers | `05_reports/classification_readiness_report.md` |
| 补丁者 | main Codex thread | Boundary and duplicate checks | `role_reports/` | completed_with_blockers | `05_reports/question_gap_review.md` |
| 监管者 | main Codex thread | Governor checklist | `00_control/GOVERNOR_CHECKLIST.md` | completed_with_blockers | `role_reports/governor_initial_review_20260617.md` |
| 自动化检测者 | main Codex thread | Matrix/report consistency checks | `role_reports/` | completed_with_blockers | `role_reports/automation_check_20260617.md` |
| Confucius | main Codex thread | Reusability check for future workers | `role_reports/` | completed_with_blockers | `00_control/FINAL_ACCEPTANCE_REPORT.md` |

Note: Real subagents were not spawned at run initialization because the current minimal step is control setup and source inventory. If the run expands into a long classification/rebuild workflow, split real workers by year/district or question type and register them here.
