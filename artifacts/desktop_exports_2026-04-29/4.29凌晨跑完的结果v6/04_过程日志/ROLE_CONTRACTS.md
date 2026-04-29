# Role Contracts: 全量独立重跑

本轮只在 `reports/full_all_suites_independent_rerun_2026-04-29/` 写入新产物。旧三大 artifact、旧 governor、旧 OCR 报告只能作为待审对象，不得作为证据来源。

## 共同硬规则

- cache-first：先读 `SUITE_ROSTER.csv` 中的 `bundle_path`；不清楚时回原始 PDF/Word/PPT，并记录 fallback 原因。
- `cache_status=classification-bundle-supplement` 的套卷必须单独说明证据边界，不能把分类汇编当完整细则。
- 主观题触发链必须有细则、评标、阅卷总结或明确评分来源；普通答案/教师版只能标 `reference-only`。
- 选择题必须有题面和可靠答案键；不得猜答案。
- 高风险词 `辩证否定/量变质变/主次矛盾/矛盾主次方面/两点论重点论/主流支流/价值观导向` 必须能在一手证据中找到原词或标准同义支撑。
- 每条结论都写清套卷、题号、材料信息、证据摘录、知识触发、答题落点。
- 发现旧 artifact 虚构、过度归因或证据等级错置，写入 `findings_*.csv`，不要直接改旧 artifact。

## 写入分工

- 决策者：维护 `PROGRESS.md`、`DECISION_LOG.md`、`HANDOFF_QUEUE.md`。
- 劳动者-2024：写 `worker_reports/worker_2024.md` 和 `worker_outputs/2024_entries.csv`。
- 劳动者-2025A：写 `worker_reports/worker_2025A_yimo_qimo.md` 和 `worker_outputs/2025A_entries.csv`。
- 劳动者-2025B：写 `worker_reports/worker_2025B_ermo.md` 和 `worker_outputs/2025B_entries.csv`。
- 劳动者-2026A：写 `worker_reports/worker_2026A_yimo.md` 和 `worker_outputs/2026A_entries.csv`。
- 劳动者-2026B：写 `worker_reports/worker_2026B_qizhong_qimo.md` 和 `worker_outputs/2026B_entries.csv`。
- 补丁者：写 `patcher_reports/multipoint_patch_review.md`，专查一材料多答点漏挂。
- 监管者：写 `governor_reports/evidence_governor.md`，只签 PASS/REJECT/NEED_EVIDENCE，不补写正文。
- 自动化检测者：写 `automation_reports/coverage_validation.md`，检查 56 套是否都有明确状态。
