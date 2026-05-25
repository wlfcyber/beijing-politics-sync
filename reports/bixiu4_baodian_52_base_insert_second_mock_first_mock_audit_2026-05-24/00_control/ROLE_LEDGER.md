# ROLE_LEDGER

| role | lane | assignment | output |
|---|---|---|---|
| 决策者 | Codex A | 维护范围、阶段、阻塞与下一步 | `00_control/` |
| 劳动者 | Codex A | 盘点一模/二模源文件，抽取覆盖矩阵和候选 | `01_source_inventory/`, `02_codex_lane/` |
| 补丁者 | Codex A | 检查一题多原理、主次矛盾、矛盾主次方面、两点论重点论遗漏 | `02_codex_lane/agents/patcher_report.md` |
| 监管者 | Codex A | 禁止假闭环、弱证据、脱离母版、专题堆砌 | `05_governor/` |
| 自动化检测者 | Codex A | 对照控制文件、覆盖矩阵、两线产物一致性 | `04_fusion_audit/` |
| 生产线 B | ClaudeCode | 独立跑同一任务，不作为 reviewer 降级 | `03_claudecode_lane/` |
| Codex-A 独立子线程 | multi_agent `019e5976-9f38-7891-b77d-9a205ac134e0` | 独立倒查 2024-2026 一模与 2026 二模覆盖，不生成 Word | `02_codex_lane/agents/codex_a_independent_coverage_rerun_20260524.*` |
| ClaudeCode-B 复跑线程 | local ClaudeCode process | 独立生产线复跑 2026 二模厚度与 2024-2026 一模漏项，到融合审核前停止 | `03_claudecode_lane/claudecode_b_full_coverage_rerun_*_20260524.*` |
