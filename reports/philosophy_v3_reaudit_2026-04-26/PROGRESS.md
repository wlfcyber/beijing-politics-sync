# 必修四哲学 v3 重跑进度

日期：2026-04-26

## 已完成

- [x] STEP_00: 已建立 `reports/philosophy_v3_reaudit_2026-04-26/` 工作区；冻结 5 个旧核心产物；创建 `TASK_BRIEF.md`、`DEVELOPMENT_PLAN.md`、`PROGRESS.md`、`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`GOVERNOR_CHECKLIST.md`、`旧产物核验表.md`、`artifacts/删除与降级清单.md`、`artifacts/第一批抽查报告.md`。第一批高风险抽查完成：ClaudeCode v2 正文降级为控制层证据；2026西城期末第21题标为 B 级评标角度清单；2026石景山期末主观链标为 D/reference-direction 边界；2024石景山一模第16/20题标为 D/reference-direction；2024门头沟一模主观16-21维持 reference-only，不得入正式主观细则链。
- [x] STEP_01: 已从冻结旧框架抽取 496 条触发条目，写入 `artifacts/framework_entry_inventory.csv`；形成 310 个不同来源键，6 条旧框架来源未映射到 suite bundle，但已在 v3 来源复核中用 worker 报告边界处理。
- [x] STEP_02/03: 已完成旧框架 496 条触发条目的来源层复核，写入 `artifacts/all_framework_entry_source_reaudit.csv` 与 `artifacts/all_framework_source_key_reaudit.csv`。最终等级：A 126、B 143、C 186、D 12、E 29。E 不是未处理，而是已复核后判定为缺原件、缺 OCR、缺答案键或用户补充材料不在工作区。
- [x] STEP_04: 已完成错肢库 1583 条来源行复核，写入 `artifacts/wrong_option_source_reaudit.csv`。其中 C_verified_choice_source 1434、C_worker_report_source 23、E_choice_key_not_detected 126。
- [x] STEP_05: 已完成旧题源清单 56 行复核，写入 `artifacts/suite_inventory_reaudit.csv`。判定：source-reviewed 20、closed-with-angle-boundary 23、closed-with-reference-boundary 3、old-closed-needs-boundary-or-evidence 8、confirmed-excluded 2。
- [x] STEP_06: 已生成 `artifacts/all_source_reaudit_summary.md` 和 `artifacts/全来源复核_边界与缺口清单.md`。结论：旧 `已闭环` 不能原样继承；D/E 行不得进入正式 v3 正文；B 行只能写成角度清单或整理链；A 但触发词未直接命中的 44 条需在正文草案阶段人工复看材料链。
- [x] STEP_06A: 已按用户要求补做“内容回源复核”：对 V2 496 条框架条目逐条回到原题/细则片段，写入 `artifacts/content_backtrace_review.csv`、`artifacts/content_backtrace_summary.md`、`artifacts/content_backtrace_non_direct_full.md`。结果：SUPPORTED_DIRECT_RUBRIC 202、SUPPORTED_DIRECT_CHOICE_TEXT 75、WEAK_INFERRED_FROM_MATERIAL 97、NEEDS_HUMAN_CONTENT_CHECK 75、BLOCKED_SOURCE_GAP 29、WEAK_REFERENCE_ONLY 12、BLOCKED_NO_CHOICE_KEY 6。后续 v3 正文只能自动保留直接支撑条目；其余 219 条必须删除、降级、补证或人工复看。

## 下一步

- [ ] STEP_07: 按全来源复核表生成 v3 修订版框架和错肢库草案；旧正本仍不得直接覆盖。
- [ ] STEP_08: 做最终 governor 终审；当前不得写 `TASK_COMPLETE`。

## 当前边界

- `2026朝阳期末`：试卷/细则在本机和 bundle 中均为 scan-only 或未同步 OCR，涉及框架 12 条 E 和错肢库 32 条 E；不得作为正式闭环。
- `2026西城一模`、`2026丰台期末`、`2025海淀二模`：选择题答案键在当前 bundle/本机复核中未检测到，相关框架/错肢库行已标 E，不能沿用旧闭环口径。
- 用户补充截图/PDF类证据未在当前工作区原件化的条目已标 E_user_supplement_not_in_workspace，不能写成已回源确认。
- 本轮完成的是来源层复核，不是 v3 正文修订完成。
- 内容回源复核显示 219 条旧 V2 条目不能由原题/细则直接支撑，不能再按旧正文口径继承。
