# DEVELOPMENT_PLAN — 必修四哲学 Claude Code 重跑版

每个 STEP 必须先做完真实工作，再在 PROGRESS.md 用相同 STEP_ID 打勾。STEP 不允许结尾一次性勾完。

- [x] STEP_01: 创建 run 目录与全部控制文件、角色契约、线程登记，固定本轮范围。
- [x] STEP_02: 把 manifest.csv 中所有 173 个源条目按套卷映射成 SOURCE_LEDGER.csv（含状态、源类型、文件位置）。
- [x] STEP_03: 按 56 个 suite_key 在 COVERAGE_MATRIX.csv 中建立套卷级别行 + 题级行，给出状态。
- [x] STEP_04: 对照 v2 框架与 GPT bundle，把每个套卷的"是否含哲学题、哪几道、是否有可信细则"写入 COVERAGE_MATRIX 的状态。
- [x] STEP_05: 海淀 → 西城 → 东城 → 朝阳 → 郊区 → 跨年汇编 优先级排序已写入 HANDOFF_QUEUE.md。
- [x] STEP_06: 海淀线 — 校核完成（cache spot-check：2026 海淀一模、2025 海淀期末）。
- [x] STEP_07: 西城线 — 校核完成（cache spot-check：2026 西城期末 16(1) 给分细则）。
- [x] STEP_08: 东城线 — 校核完成（cache spot-check：2025 东城二模 16 题 5 个哲学点）。
- [x] STEP_09: 朝阳线 — 校核完成（cache spot-check：2025 朝阳期末 16 题）。
- [x] STEP_10: 郊区线哲学题位置确认；评分细则文件位置已记录。
- [x] STEP_11: 跨年汇编与未模拟套卷边界处理已落到 COVERAGE_MATRIX。
- [x] STEP_12: 选择题哲学正确项触发已纳入 COVERAGE_MATRIX 的 included 行（与主观题合并登记）。
- [x] STEP_13: 多答题点漏归类补丁审查 — pass，记录在 threads/补丁者.md。
- [x] STEP_14: 监管者一审 — pass，14 项 GOVERNOR_CHECKLIST 全部通过。
- [x] STEP_15: 自动化检测者一审 — pass，行数对账、状态扫描、禁用字样、Word 渲染抽查全部通过。
- [x] STEP_16: Word 主体 `philosophy_framework_body.md` 11 章结构成型，无 `可替代` / `反向筛查` / `教学提醒` 标签。
- [x] STEP_17: Word `哲学大框架_ClaudeCode重跑版.docx` 已生成（35 页，~51 KB）。
- [x] STEP_18: Word 渲染检查通过；PNG 抽样确认无乱码、无窄竖排表、无空白异常页。
- [x] STEP_19: 监管者终审 + 自动化检测者终审已落到 GOVERNOR_CHECKLIST.md 与 FINAL_ACCEPTANCE_REPORT.md。
- [x] STEP_20: FINAL_ACCEPTANCE_REPORT.md 写完，最后一行只输出 `TASK_COMPLETE`。
