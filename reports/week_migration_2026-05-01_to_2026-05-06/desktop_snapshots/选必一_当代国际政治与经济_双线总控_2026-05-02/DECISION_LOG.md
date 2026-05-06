# Decision Log

## 2026-05-02 Intake Decisions

- Decision: Use 选必一《当代国际政治与经济》 branch, not 必修四/选必二/选必三.
  - Reason: User explicitly said “开始跑选必一”.
- Decision: Default output is 主观题细则术语学生版.
  - Reason: 选必一 branch skill states its core output is scoring-term accumulation for main questions, and choice questions are processed only when explicitly requested.
- Decision: Treat old v12 and previous docs as hard-rule references, not final evidence.
  - Reason: This avoids repeating old mistakes while still preserving user-corrected rules.
- Decision: Exclude 2026石景山期末 unless user supplies new scoring-rule evidence.
  - Reason: User previously confirmed no usable scoring rules for all modules.
- Decision: Codex must both lead and produce.
  - Reason: User corrected the workflow: "codex除了当总控，自己也要跑". ClaudeCode is an independent comparison lane, not a replacement for Codex's own source/evidence/content lane.

## 2026-05-02 22:02 Restart Decision

- 用户再次以 `$feige-politics-garden` 发出“开始选必一”。按 router，实际执行链为：`feige-politics-garden` -> `feige-politics-garden-book-orchestrator` -> `feige-politics-garden-xuanbiyi`。
- 采用安全默认：继续使用现有 run 目录，但不承认旧草稿已经完成；进入最终学生版前必须过 Governor、融合和 Confucius。
- ClaudeCode 必须拉起且可见；本轮使用 `screen` detached session，避免普通 `nohup` 进程被执行环境清理。
- ClaudeCode 写入隔离目录，避免覆盖 Codex 线；Codex 同时继续自跑，不等待 ClaudeCode 才做内容。
