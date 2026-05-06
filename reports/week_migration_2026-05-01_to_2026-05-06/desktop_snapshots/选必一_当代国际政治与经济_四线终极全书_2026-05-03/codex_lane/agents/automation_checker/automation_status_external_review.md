# 自动化检测状态：external_review

检测时间：2026-05-03 20:17 CST

检测范围：外部二审落盘后，`task_plan.md`、`progress.md`、`00_control/MODEL_ADVICE_LOG.md`、`reports/督工验收状态.md`、`00_control/PROGRESS_LEDGER.jsonl`、GPT review index / correction log、delivery gate 是否一致。

## 总判定

WARN

理由：外部二审原始回复已经落盘，但多个控制文件仍写着“已提交 / 等待回收 / pending capture”。最终交付门禁仍保持阻断，未误宣称完成；但当前状态台账需要同步，且二审意见尚未消化为本地可验证修补任务。

## 1. 已落盘文件检查

| 文件 | 状态 | 行数 | 备注 |
|---|---:|---:|---|
| `07_student_doc/by_question_view_draft_20260503.md` | 存在 | 361 | 按题视图草稿；本轮未编辑 |
| `07_student_doc/six_bucket_to_question_crosswalk_draft.md` | 存在 | 87 | 六桶桥接草稿；本轮未编辑 |
| `08_review/gpt_content_review/by_question_review_prompt_20260503.md` | 存在 | 20 | GPT 二审提示词 |
| `08_review/gpt_content_review/by_question_review_response_20260503.md` | 存在 | 169 | GPT 二审回复已落盘，判定为 `NEEDS_FIX` |
| `opus_writer/web_external/claude_by_question_review_prompt_20260503.md` | 存在 | 20 | Claude 二审提示词 |
| `opus_writer/web_external/claude_by_question_review_response_20260503.md` | 存在 | 226 | Claude 二审回复已落盘 |
| `08_review/claude_by_question_review_response_20260503.md` | 存在 | 226 | Claude 二审兼容副本已落盘 |
| `00_control/MODEL_ADVICE_LOG.md` | 存在 | 57 | 但 by-question 二审状态仍写 pending capture/digest |
| `task_plan.md` | 存在 | 60 | 但仍写二审回复 pending capture/digest |
| `progress.md` | 存在 | 60 | 但仍写 Claude responding / GPT thinking |
| `00_control/PROGRESS_LEDGER.jsonl` | 存在 | 38 | 仅有 submitted 事件，缺 captured/digest-pending 事件 |
| `reports/督工验收状态.md` | 存在 | 22 | 仍写等待回收 |
| `FINAL_ACCEPTANCE_REPORT.md` | 存在 | 3 | `not_started`，安全但未更新 |
| `09_delivery/acceptance_report.md` | 存在 | 2 | 空壳状态 |
| `09_delivery/delivery_manifest.md` | 存在 | 2 | 空壳状态 |

## 2. 尚需同步的控制文件

1. `task_plan.md`
   - 当前仍称 by-question 外部二审“pending capture/digest”。
   - 应同步为：Claude/GPT 原始回复已回收；进入本地消化、证据核验、补丁者/Governor 再审阶段。

2. `progress.md`
   - 当前末尾仍写 Claude 正在响应、ChatGPT 正在思考。
   - 应追加外部二审已回收、GPT verdict=`NEEDS_FIX`、Claude 为教学迁移建议、均不能直接改学生稿或提升证据状态。

3. `00_control/PROGRESS_LEDGER.jsonl`
   - 缺少 `external_by_question_reviews_captured`、`external_by_question_digest_pending` 或同义事件。
   - 需要记录两个 raw response 路径，以及“advisory only / local verification required / no final release”边界。

4. `00_control/MODEL_ADVICE_LOG.md`
   - External By-Question Preview Reviews 段仍只记录 prompt，状态为 pending。
   - 应补充 `response_saved_claude`、`response_saved_gpt`、GPT `NEEDS_FIX`、Claude “内部预览可试读但非终稿”的边界摘要。

5. `reports/督工验收状态.md`
   - 当前仍写按题视图二次 review 正在等待回收。
   - 应改为：已回收但未消化；外部意见显示仍有 must-fix/transfer-fix，不能进入终稿。

6. `08_review/gpt_content_review/gpt_content_review_index.md`
   - 当前只登记 `section_batch`。
   - 应新增 `by_question_preview` trigger row，raw review 指向 `08_review/gpt_content_review/by_question_review_response_20260503.md`，Markdown PASS/Word-PDF PASS 均为 no。

7. `08_review/gpt_content_review/content_correction_log.md`
   - 当前只有 `GPT-SB-001` 至 `GPT-SB-009`。
   - 应消化并新增 by-question 二审问题行，至少覆盖 GPT 指出的桥接表与按题视图不一致、Q16(2) 主体/桶位边界、西城 Q20 术语堆叠、联合国表述需核验、综合/开放题分层等问题。

8. `SOURCE_LEDGER.csv` / `COVERAGE_MATRIX.csv`
   - 暂不建议仅因外部二审直接改源证据状态。
   - 若后续本地核验证实某题漏点、桶位或术语归属需要变更，再由 Worker/Patcher/Governor 后同步。

## 3. 当前不能宣称完成的缺口

- 外部二审只是 advisory，尚未消化为本地可验证修补任务。
- GPT 二审明确给出 `NEEDS_FIX`，不能作为学生预览正式版、Markdown 终稿、Word/PDF 的放行依据。
- Claude 二审虽认为结构明显优于纯六桶表，但仍要求若干迁移性返修，且其本身不裁定术语真假、分值口径或细则边界。
- `by_question_view_draft_20260503.md` 与 `six_bucket_to_question_crosswalk_draft.md` 仍是草稿/审查稿，不是最终学生稿。
- 外部二审意见尚未经过本地源文件核验，尤其是 Q16(2) 企业/政府/行业组织主体边界、西城 Q20 联合国气候治理表述、顺义 Q20 时代主题是否命中、海淀二模 Q21 是否命中新型国际关系。
- Patcher/Governor 尚未对二审消化后的补丁进行复审。
- 全书 coverage close 未完成，`SOURCE_LEDGER.csv` 与 `COVERAGE_MATRIX.csv` 不能据此关门。
- 最终 Markdown、Word/PDF、视觉 QA、Confucius artifact-only 学会性验收均未完成。
- `FINAL_ACCEPTANCE_REPORT.md` 仍为 `not_started`，`09_delivery/acceptance_report.md` 与 `09_delivery/delivery_manifest.md` 仍为空壳。

## 4. 当前最终交付门禁一致性

- 安全门禁：一致。当前没有文件宣称 FINAL PASS，最终交付仍被阻断。
- 状态门禁：不一致。二审 raw response 已经落盘，但 `task_plan.md`、`progress.md`、`MODEL_ADVICE_LOG.md`、`PROGRESS_LEDGER.jsonl`、`reports/督工验收状态.md` 仍停留在“等待回收 / pending capture”。
- 内容门禁：未放行。GPT 二审为 `NEEDS_FIX`，Claude 二审也只允许内部预览/小范围试读，不允许对外学生终稿。

## 5. 下一步叫醒任务

建议叫醒 Decision Maker / Patcher / Governor：

> 按 `codex_lane/agents/automation_checker/automation_status_external_review.md` 处理外部二审回收后的同步缺口。先不要改学生正文。第一步把 `08_review/gpt_content_review/by_question_review_response_20260503.md` 和 `08_review/claude_by_question_review_response_20260503.md` 消化成本地待核验修补清单，更新 `MODEL_ADVICE_LOG.md`、`PROGRESS_LEDGER.jsonl`、`gpt_content_review_index.md`、`content_correction_log.md`、`progress.md`、`task_plan.md`、`reports/督工验收状态.md`。所有 substantive 修补必须先回源核验，再交 Patcher/Governor，不得直接把外部建议写进学生稿。
