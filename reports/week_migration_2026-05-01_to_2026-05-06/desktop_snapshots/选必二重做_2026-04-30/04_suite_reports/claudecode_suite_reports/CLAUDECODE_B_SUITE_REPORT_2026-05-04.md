# ClaudeCode Lane B 选必二全套报告（2026-05-04）

## 1. 角色与边界

- 身份：ClaudeCode Production Lane B（独立生产线）
- 不是：GPT-5.5 Pro 真实 gate / Claude Opus 4.7 Adaptive 真实 gate / Codex 子智能体
- 写域：仅 `claudecode_lane/outputs/`、`04_suite_reports/claudecode_suite_reports/`、`06_conflicts/`
- 不动：Codex A 脚本、最终合集 .md/.docx、`final_legal_outputs/` 框架文档、`00_control/` 控制文件、`00_飞哥...小本本.md`

## 2. 复算结论（独立）

| 项 | Codex A | Lane B 复算 |
| --- | --- | --- |
| 原始候选 | 148 | 148 |
| included（三类） | 113 | 113（90+14+9）|
| formal/scoring 匹配 | 78 | 78 |
| 候选答案-only | 9 | 9 |
| 模块边界排除 | 3 | 3 |
| 策展排除 | 32 | 32 |
| paper_source（题面即唯一来源） | 未单列 | 22 |
| evidence_type=unknown | 未单列 | 4 |

Lane B 关键判定：Codex A "rubric pending: 0" 实为 78/113，应将 22 paper_source + 4 unknown = **26** 改为 `rubric_match_pending`。

## 3. 套卷层抽样审计（54 套卷）

- has_xuanbier 48 套：Lane B 复扫 SOURCE_MATCH_LEDGER_V2 与 LEGAL_QUESTION_INDEX_V2，套卷扫描完整性可信。
- uncertain 6 套（2024朝阳一模 / 2024朝阳期中 / 2024海淀期中 / 2024丰台一模 / 2026顺义一模 / 2026西城期末）：Lane B 同意保持 uncertain；其中 2026 西城期末是文本层不足，需 OCR 复核；2024 朝阳一模题面未锁定但讲评 PPT 有法律信号，建议优先做 vision OCR。
- no_xuanbier 0：Lane B 同意（54 套中 6 套不确定，48 套有，无明确"无选必二"）。

## 4. 题目层结论

- 113 入框题：Lane B 在 `CLAUDECODE_B_QUESTION_CHALLENGE_LEDGER_2026-05-04.csv` 中逐项给出 confirm / confirm_with_caveat / challenge_evidence 判定。
- 32 排除题：1 项 challenge（2024 海淀一模 Q13），其余 confirm。
- 14 needs_review 混合题：Lane B 全部 confirm 现状（待拆分小问后再正式入框）；建议在域频次统计中分两套口径（C-006）。
- 9 候选答案：Lane B 对每题给出"倾向答案 + 风险等级"，并强调严禁升格为官方答案，详见 `CLAUDECODE_B_CHOICE_ANSWER_PENDING_REVIEW_2026-05-04.md`。

## 5. 框架层结论

- 一核二线三问四步 + 8 域结构：confirm。
- 频次：confirm。
- 命题路径：8 域抽样均能解释，无新增 `proposition_path_uncertain`。
- 修改建议（弱建议、不强制）：分层标签（主干高频层 vs 开放容器层）显式化；候选答案标签统一；待补正式细则清单显式化。

## 6. 阻塞与下一步

- 真实 GPT-5.5 Pro 网页 / Claude Opus 4.7 Adaptive 网页 gate 仍 `real_call_pending`；Lane B 不充当模型 gate。
- 26 道题的 `rubric_match_pending` 应在 Codex 本地裁决后回写至 QUALITY_REPORT_V2 与框架文档脚注。
- 9 道候选答案在官方答案锁定前不得进入"高频示范"。
- 3 道模块边界排除应在框架文档附录显式列出。
- 14 道 `included_needs_review` 需拆分小问后再定计入域频次的口径。
- 在四线（Codex A、Lane B、真实 GPT-5.5 Pro、真实 Claude Opus 4.7 Adaptive）真实闭合前，Final Governor / Confucius / Delivery PASS 全部 blocked。

## 7. Lane B 提交清单

- `claudecode_lane/outputs/CLAUDECODE_B_PROGRESS_2026-05-04.md`
- `claudecode_lane/outputs/CLAUDECODE_B_SOURCE_AUDIT_MATRIX_2026-05-04.csv`
- `claudecode_lane/outputs/CLAUDECODE_B_QUESTION_CHALLENGE_LEDGER_2026-05-04.csv`
- `claudecode_lane/outputs/CLAUDECODE_B_FRAMEWORK_REVIEW_2026-05-04.md`
- `claudecode_lane/outputs/CLAUDECODE_B_CHOICE_ANSWER_PENDING_REVIEW_2026-05-04.md`
- `claudecode_lane/outputs/CLAUDECODE_B_CONFLICTS_FOR_CODEX_2026-05-04.md`
- `04_suite_reports/claudecode_suite_reports/CLAUDECODE_B_SUITE_REPORT_2026-05-04.md`（本文件）
