# 线程登记

| Role | Agent/Thread ID | Assignment | Write scope | Status | Last report |
| --- | --- | --- | --- | --- | --- |
| 决策者 | local-codex-controller | 选择下一批题源、维护进度和闭环口径 | 00_control, 04_fusion | active | pending |
| 劳动者-Codex | local-codex-worker | 逐题抽取 2026 二模哲学主观题和客观题链条 | 02_codex_lane | active | pending |
| 补丁者 | local-codex-patcher | 检查一题多知识点漏放、错放节点 | 02_codex_lane, 04_fusion | active | pending |
| 监管者-Governor | local-governor | 审核证据等级、覆盖矩阵、学生版污染词、最终闭环 | 06_governor_confucius | active | pending |
| 自动化检测者 | local-automation-checker | 检查控制文件、覆盖表、产物一致性 | 06_governor_confucius | active | pending |
| ClaudeCode | claude-cli-pending | 独立读取同一题源，找漏题与错位 | 03_claudecode_lane | pending | pending |

