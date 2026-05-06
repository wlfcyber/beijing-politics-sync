# Codex-A Governor Startup Gate

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex production lane A / 监管者-Governor

结论：FAIL / 需返修

本轮启动闸门不放行到正式条目生产、学生版融合、coverage 闭合或最终验收。当前只允许返修 Phase 1C 五角色产物、源定位清单、证据台账和 notebook digest。

## 已读依据

- `MASTER_REQUIREMENTS.md`
- `task_plan.md`
- `00_control/RUN_MANIFEST.yaml`
- `/Users/wanglifei/Desktop/北京高考政治/选必一复查_2026-04-29/选必一_交付要求记事本.md`
- `00_control/NOTEBOOK_DIGEST.md`
- `00_control/START_CARD.md`
- `00_control/EVIDENCE_PRIORITY_RULES.md`
- `00_control/ZERO_START_DECLARATION.md`
- `codex_lane/agents/ROLE_LEDGER.md`
- `codex_lane/agents/decision_maker/decision_maker_findings.md`
- `codex_lane/agents/automation_checker/automation_status.md`
- `feige-politics-garden-xuanbiyi/SKILL.md`
- `feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## 启动闸门总表

| 检查项 | 结论 | Governor 判定 |
|---|---|---|
| 参考答案冒充细则 | PASS 但需继续设闸 | 当前未发现已有条目把 P1 参考答案升格为 P0 细则；但 `SOURCE_LEDGER.csv`、`03_entries/evidence_level_index.csv` 均只有表头，尚无真实证据样本可验收。后续必须先写 source/evidence level，再写术语。 |
| 2026 石景山期末误入 | PASS | 当前只在控制文件中作为排除禁区出现，未在 source ledger、entries、student doc、delivery 中发现误入。继续保持全模块排除，除非用户明确给新评分细则。 |
| 旧结论直接继承 | PASS 但需继续设闸 | `ZERO_START_DECLARATION.md` 与决策者产物均声明旧成果只可定位源/查漏/格式借鉴；当前未发现旧结论直接进入本轮 entries。但因为 entries 与 source ledger 为空，后续每条结论必须回源登记，不能从旧版搬运。 |
| Codex-A 五角色生成 | FAIL / 需返修 | 目录存在，`ROLE_LEDGER.md` 列出五角色，但状态全部为 `bootstrapping`；当前可见 `decision_maker/decision_maker_findings.md` 与 `automation_checker/automation_status.md`，本报告生成后 `governor/`也有本文件；但 `worker/`、`patcher/`仍为空，五角色未各自产出可审计首轮结果。Phase 1C 未完成。 |
| 学生版风险词 | PASS 但无内容验收意义 | `07_student_doc/*.md` 目前基本为空壳，未检出路径、debug、audit、模型聊天、后台语、评标、细则要求、采分点、要落到、材料中、v7/v8 等风险词。由于尚无正文，不能据此判定学生版可用。 |
| Coverage 假闭合 | PASS: 未发现假闭合；FAIL: 不得使用当前 coverage | `FINAL_ACCEPTANCE_REPORT.md` 为 `not_started`，`task_plan.md` 仍为 running，coverage/suite matrix 均只有表头，未发现伪装成 100% 或已闭合。但这也意味着当前 coverage 不能支持任何 PASS、闭环或终稿宣称。 |
| Notebook 吸收 | FAIL / 需返修 | 外部交付要求记事本已存在且规则明确，但 `00_control/NOTEBOOK_DIGEST.md` 只有标题，未形成可审计吸收摘要。需要补写 digest 后再放行后续角色。 |
| 源定位与证据台账 | FAIL / 需返修 | `01_source_inventory/SOURCE_INVENTORY.csv`、`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`03_entries/evidence_level_index.csv` 均只有表头；当前没有本轮可追踪源证据。 |

## 需返修清单

1. 完成 Phase 1C：为劳动者、补丁者生成首轮真实产物；自动化检测者需在真实 source/coverage 产生后复检；Governor 本报告生成后仍需后续复查；不要只更新 `ROLE_LEDGER.md` 的状态。
2. 补写 `00_control/NOTEBOOK_DIGEST.md`：把交付要求记事本、xuanbiyi skill、term protocol 中的硬规则压成可执行检查项，尤其是 P0/P1 边界、石景山排除、答案句风险词、总说/分说全收。
3. 先做源定位，不写正式术语：填充 `01_source_inventory/SOURCE_INVENTORY.csv` 与 `SOURCE_LEDGER.csv`，每个候选题标明评分材料类型、位置、可读状态、是否 P0、是否 reference-only。
4. 建立 `03_entries/evidence_level_index.csv` 后再允许条目生产；普通参考答案、答案及评分参考只能 P1/reference-only，不能写成 `细则位置` 的 P0。
5. coverage 文件在出现真实 source/question/entry 前全部不得作为闭合依据；任何 “PASS/已闭环/完成” 必须能回链到 source ledger、entry index 和 suite matrix。
6. 学生版生成后必须再跑风险词闸门：路径、debug、audit、模型聊天、后台语、评标、细则要求、采分点、要落到、材料中、设问要求、本题需要、v7/v8、证据层级。

## 当前允许动作

- 允许：Phase 1C 角色返修、notebook digest、源定位清单、证据分级台账、首批高权重套卷定位。
- 禁止：正式术语入主表、学生版成文、coverage 闭合、Word/PDF 交付、FINAL_ACCEPTANCE PASS。

Governor 签发：启动闸门未通过，必须返修后复检。
