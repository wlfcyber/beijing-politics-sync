# ORDER_060_BIXIU4_PLAN_UNSTICK_2250

时间：2026-05-24 22:50 +08

触发：用户追问“必修四政治庄园这个目标+计划怎么一直卡在这不动啊”。

## 总判定

必修四不是没有产物，而是停在“v10 二模同流程修订候选已完成、但严格最终验收未闭环”的状态。当前检查未见本线程 attached terminal、未见 active Codex goal、未见正在运行的 ClaudeCode/claude 生产进程；因此它不是还在后台稳定推进，而是需要重新下达控制层补丁。

## 已确认产物

- `bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23/07_delivery/5.24二模同流程修订v10/` 已生成学生版主宝典、选择题专册、二模加厚卡、严审报告的 Markdown/DOCX/PDF。
- `08_governor/GOVERNOR_REPORT_SECOND_MOCK_V10.md` 可签“2026 二模新增题按原宝典同流程修订 PASS”。
- `09_render_check_v10_second_mock/v10_second_mock_render_check.md` 已抽样渲染 PDF：主宝典 117 页、选择题专册 65 页、二模加厚卡 11 页、状态报告 1 页。
- `03_claudecode_lane/CLAUDECODE_SECOND_MOCK_NODE_V10_RECHECK_20260524.md` 显示上一轮二模修订 MUST_FIX 已关闭，剩余为可选加厚项。

## 卡住原因

1. GPT Pro web 外审仍为 `WAITING_FOR_WEB_GPTPRO_REVIEW`。`05_model_reviews/GPTPRO_WEB_STATUS.md` 记录 ChatGPT web 可打开但输入、粘贴、提交和最小 READY_TEST 均超时，未提交任何 GPT Pro review batch，不能把 GPT Pro 审核写成完成。
2. v10 只解决“2026 二模新增题太薄、未按原宝典同流程嵌入”的问题，不等于 2024-2026 全题源严格最终闭环。
3. 严审报告仍保留旧缺口数字：旧主观题质量失败组 68、旧选择题待闭环 174。选择题虽已专册化，但缺少逐行 closure matrix，因此控制层无法验证每题处置状态。
4. 严格验收控制文件缺失：`00_39_BLOCKER_STATUS.md`、`old_gap_closure_matrix_0039.csv`、`MODEL_EVIDENCE_LEDGER.md`、`CONFUCIUS_ARTIFACT_CHECK.md`、`FINAL_ACCEPTANCE_REPORT.md`、`GOVERNOR_STRICT_FINAL_ACCEPTANCE.md`。
5. 用户新增模型硬要求后，必修四当前检查未发现 Sonnet/Haiku 证据，但也没有 `MODEL_EVIDENCE_LEDGER.md` 证明 ClaudeCode 使用 Opus/max effort；因此 ClaudeCode 复核只能作为候选证据，不能作为严格合格证据。

## 立即补丁命令

必修四线程必须先补控制层，而不是继续只润色正文。

1. 新建或更新 blocker 状态文件，明确写：
   - `STATUS = DELIVERED_WITH_GOVERNANCE_GAPS`
   - `STRICT_FINAL_ACCEPTED = false`
   - `ACTIVE_WORKER = false`
   - `BLOCKER_1 = WAITING_FOR_WEB_GPTPRO_REVIEW`
   - `BLOCKER_2 = OLD_GAP_CLOSURE_MATRIX_MISSING`
   - `BLOCKER_3 = MODEL_EVIDENCE_LEDGER_MISSING`
2. 建立 `old_gap_closure_matrix_0039.csv`，至少包含 68 个旧主观质量缺口与 174 个旧选择题缺口，每行给出：
   - 题源
   - 题号
   - 缺口类型
   - v10 去向：`integrated_to_main_handbook`、`moved_to_choice_booklet`、`needs_source_recheck`、`excluded_with_reason`
   - 对应文件与小标题
   - 证据状态
3. 建立 `MODEL_EVIDENCE_LEDGER.md`：
   - 每条 ClaudeCode/Claude 证据必须写明真实调用来源、模型名、时间、输出文件。
   - 任何 Sonnet/Haiku 或模型不明输出不得计入合格硬证据。
4. 建立 `CONFUCIUS_ARTIFACT_CHECK.md`：
   - 对 v10 学生版、选择题专册、二模加厚卡逐项检查零基础高三学生是否可直接使用。
   - 禁止把审计、模型、源码、debug 语言混入学生稿。
5. 建立 `FINAL_ACCEPTANCE_REPORT.md`：
   - 当前只允许写 `DELIVERED_WITH_GOVERNANCE_GAPS`。
   - 只有 GPT Pro web 真实外审、ClaudeCode Opus/max 证据、逐行缺口矩阵、Governor/Confucius、Word/PDF QA 全部闭合后，才允许改写 `STRICT_FINAL_ACCEPTED`。
6. GPT Pro web gate：
   - 若 Chrome/ChatGPT 可稳定输入提交，立即提交 `04_review_packages/GPTPRO_WEB_BATCH_*.md`。
   - 若仍超时，写明 `BLOCKED_ADVISOR_USER_ACTION_REQUIRED`，不要伪造 GPT Pro 审核。

## 监督结论

下一轮不要再把 v10 候选说成最终完成。必修四现在需要“重新启动控制层补丁”，优先补矩阵、模型证据账、Confucius 检查和最终验收报告；GPT Pro web 外审不恢复前，严格最终仍然不能签。
