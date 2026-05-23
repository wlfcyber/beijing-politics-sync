你是飞哥政治庄园的 ClaudeCode 真实工作线，不是装饰性审核员。

目标：
审查 2024-2026 共 65 套范围内，必修四哲学宝典是否遗漏题目、是否把题目放错原理节点、是否存在过度归因。你必须给出可以直接指导 Codex 修订的清单。

必须读取：
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/00_control/TASK_BRIEF.md`
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/04_review_packages/REVIEW_PACKAGE_MANIFEST.md`
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/04_review_packages/GPTPRO_WEB_BATCH_A_海西东朝主观题.md`
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/04_review_packages/GPTPRO_WEB_BATCH_B_郊区主观题.md`
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/04_review_packages/GPTPRO_WEB_BATCH_C_高风险原理.md`
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/04_review_packages/GPTPRO_WEB_BATCH_D_选择题海西东朝.md`
- `reports/bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/04_review_packages/GPTPRO_WEB_BATCH_E_选择题郊区.md`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/CURRENT_SUITE_INVENTORY_65.md`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/STRICT_GATE_REPORT.md`

可选读取：
- 桌面 `哲学宝典最终版-飞哥正志讲堂_主次矛盾全覆盖补丁v7_2026-05-23.docx`
- 桌面 `哲学宝典最终版-飞哥正志讲堂_主次矛盾全覆盖补丁v7_2026-05-23.pdf`
- `reports/philosophy_v3_reaudit_2026-04-26/artifacts/framework_entry_inventory.csv`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/*.csv`

审核标准：
1. 不能用“等角度”兜底新增原理。
2. 区分主观题评分链、选择题正确项链、选择题错肢辨析、文化-only 条目。
3. 高风险词必须严审：主要矛盾、矛盾的主要方面、两点论重点论、主流支流、辩证否定、量变质变、价值观导向。
4. 学生版不能出现补漏、补丁、审计、评分细则、CSV、证据路径等过程词。
5. 对每个问题给出：KEEP / MOVE / DELETE_OR_DOWNGRADE / NEED_EVIDENCE。

输出格式：
Markdown，分五段：
1. 总 verdict：当前能否作为最终宝典。
2. 必须 MOVE 的错位题清单。
3. 必须 DELETE_OR_DOWNGRADE 的过度归因题清单。
4. 必须 KEEP 且应重点讲的题清单。
5. 对 Codex 下一步修订的具体指令。

不要修改文件，只在 stdout 输出。
