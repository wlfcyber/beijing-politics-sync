# Supervisor Patch 01 — 不接受 pending 伪闭合

Codex QA verdict: `HARD_FAIL_NOT_CLOSED_YET`

## 当前失败点

1. `QUESTION_COVERAGE_MATRIX.csv` 只有 528 行，低于 Codex union matrix 的 534 行。
2. 缺少 6 个 Phase12 后增 canonical rows：
   - `Q-2025海淀二模-12`
   - `Q-2025海淀二模-13`
   - `Q-2026丰台一模-4`
   - `Q-2026丰台一模-7`
   - `Q-2026丰台一模-8`
   - `Q-2026丰台一模-9`
3. `QUESTION_COVERAGE_MATRIX.csv` 仍有 330 行含 `pending` 或 `evidence-recheck`，这不是用户要求的“穷尽所有考题”。
4. `入正文-pending-evidence-recheck` 不能算入正文；除非已经读到题面、答案/细则/讲评或可靠选择题答案源，否则必须改为 `blocked`，并在 blocker 写明缺什么。
5. `同类索引-pending` 不能算同类索引终态；必须改为：
   - `同类索引`：已有 canonical 或同类题可追踪，且说明为什么不独立入正文；
   - `blocked`：缺题面/选项/答案/细则/视觉核读；
   - `excluded`：其他模块、纯形式逻辑或用户排除源。

## 必须修补的文件

- `QUESTION_COVERAGE_MATRIX.csv`
- `BLOCKED_OR_BOUNDARY.md`
- `EXHAUSTIVENESS_AUDIT.md`
- 相关 `suite_reports/*.md`
- 若新增入正文题，必须同步 `MAIN_THINKING_LEDGER.csv`、`CHOICE_TRAP_LEDGER.csv`、`FRAMEWORK_NODE_MATRIX.csv`、`entries/*.jsonl`

## 修补口径

结论字段必须能规整到四类：

- `入正文`
- `同类索引`
- `blocked`
- `excluded`

可以在 reason/evidence_level/blocker 中写细分原因，但 `本轮结论` 不要保留 pending。

## 继续顺序

1. 先补入 6 个缺失 qids。
2. 再从 `入正文-pending-evidence-recheck` 行开始，逐套卷改为 `入正文` 或 `blocked`。
3. 再处理 `同类索引-pending` 行，改为 `同类索引`、`blocked` 或 `excluded`。
4. 最后重写 `EXHAUSTIVENESS_AUDIT.md`，明确仍未完成额外 30+ source root 套卷扩展，不得写 PASS。
