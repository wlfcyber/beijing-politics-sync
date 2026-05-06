# THREAD_REGISTRY

| Role | Agent/Thread ID | Assignment | Write scope | Status | Last report |
|---|---|---|---|---|---|
| 决策者 | main-thread | 建立 v3 重跑边界、冻结旧产物、确定第一批抽查对象 | 本目录控制文件 | active | `DECISION_LOG.md` |
| 资料组织者 | main-thread | 登记旧产物、证据报告、缓存 bundle 与历史 worker 报告 | `SOURCE_LEDGER.csv` | active | `SOURCE_LEDGER.csv` |
| 补丁者 | main-thread | 识别旧产物中证据等级误标、reference-only 误升格风险 | `旧产物核验表.md`、`artifacts/删除与降级清单.md` | active | `artifacts/第一批抽查报告.md` |
| 监管者 | main-thread | 检查本轮未改正本、未把待证写成完成 | `GOVERNOR_CHECKLIST.md` | active | `GOVERNOR_CHECKLIST.md` |
| 自动化检测者 | main-thread | 核对 frozen artifact hash、plan/progress step | `FINAL_ACCEPTANCE_REPORT.md` | active | `FINAL_ACCEPTANCE_REPORT.md` |

说明：本轮用户只要求开始 v3，未要求真实并行线程；因此角色由 main-thread 分担，并在后续需要时再拆真实线程。

