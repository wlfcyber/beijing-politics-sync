# ClaudeCode Account-Restored Context Handoff

你是 ClaudeCode，当前账号已经切换到新 Claude Max 账号。本轮请不要继承旧账号、旧会话、旧输出的结论；只能把本提示和本工作目录内的控制文件作为继续依据。

## 最高优先级

- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- 用户任务：选必三《逻辑与思维》分成“思维部分”和“推理部分”。思维部分要完全模仿已成功的哲学宝典工作流，穷尽每一道题，形成学生能直接使用的终极教学文档；推理部分要按题型分类，把所有同类题放在相应题型下面。
- 用户已经强烈指出之前偷懒、没有穷尽、质量不像哲学宝典。你必须按严格四线工作流和证据闭环做，不得只写概念表或抽样稿。
- 现在 Claude/ClaudeCode 会员已恢复，账号已切到新账号；你可以恢复 ClaudeCode Lane B，但必须从当前控制文件接续，不要重启错目录。
- 仍然不能生成 Word/PDF/final/终稿/最终稿/宝典成品，除非后续所有 gate 通过。

## 必读文件

先读这些文件，再行动：

1. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
2. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
5. `task_plan.md`
6. `progress.md`
7. `00_control/DECISION_LOG.md`
8. `00_control/MODEL_ADVICE_LOG.md`
9. `08_review/gpt_phase_advice/gpt_phase_advice_index.md`
10. `09_student_draft/phase11A_student_body_PATCHED_REVIEW_ONLY.md`
11. `09_student_draft/phase10_5_source_repair_priority_queue.md`
12. `09_student_draft/phase10_5_source_repair_priority_queue.csv`
13. `09_student_draft/phase11B_batch01_P1_source_repair_matrix.csv`
14. `09_student_draft/phase11B_batch01_P1_candidate_entries.md`
15. `08_review/phase11B_batch01_codex_local_verification.md`
16. `08_review/phase11B_batch01_GPT_review_packet.md`

## 当前真实状态

- Phase10 GPT gate 已恢复并通过，裁决是：`GO_TO_PHASE11_CONTROLLED_EXPANSION_OR_CONTENT_REVIEW_NO_WORD_NO_FINAL`。
- Phase11A 29 行学生稿已经过 Codex 本地内容复核：29/29 PASS，内部话术 0，同类题误扩展 0，hard-lock failure false。
- Phase11A GPT 先返回 `MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION`，指出丰台期末第8题不能把“概念是思维基本单元”泛化到形象思维。
- Codex 已修补并通过 GPT patch-resolution，GPT 裁决为：`GO_PHASE11B_CONTROLLED_EXPANSION_NO_WORD_NO_FINAL`。
- 用户刚刚恢复 Claude/ClaudeCode 会员并换号；Codex 已确认 ClaudeCode CLI 当前 auth 为新账号 `[CLAUDE_ACCOUNT_REDACTED]`，subscriptionType 为 `max`。
- Codex 已完成最小烟测：`claude -p --model opus --effort max --permission-mode bypassPermissions '只回复：OK'` 返回 `OK`，说明本机 ClaudeCode CLI 已能用新账号调用 Opus。

## 当前 Phase11B 任务边界

Phase11B 只能做 controlled expansion/source repair。禁止：

- 直接扩成 74 行正文；
- 直接合并 45 条 hold rows；
- 使用 288 条 L0；
- 使用 hard-excluded rows；
- 生成 Word/PDF/final；
- 写“终稿/最终稿/宝典成品/FINAL PASS”。

Phase11B 必须从优先级队列开始。当前 Codex 已先处理 P1 三条：

1. `Q-2025东城期末-18-2`
   - 本地修源：这是创新思维主观题，不是三段论/形式推理题。
   - 候选正文：创新思维；联想思维；发散思维与聚合思维。
   - 合并策略：只作为一个 body candidate，等 GPT 和你审稿后才能合并。

2. `Q-2026通州期末-9`
   - 本地修源：医保+商保清分结算中心，答案 D。
   - 合并策略：只入选择题陷阱索引，不进主观正文。

3. `Q-2024朝阳二模-7`
   - 本地修源：科学思维离不开逻辑，答案 D。
   - 合并策略：只入推理题型索引，不进思维方法正文。

## 你这次要做什么

请做 ClaudeCode Lane B 的独立审计，不要重写全书，不要生成终稿。输出目录：

`claudecode_lane/phase11B_account_restored_context_audit/`

请至少生成：

1. `phase11B_account_restored_status.md`
   - 说明你已识别当前账号恢复、当前 Phase、禁止事项、可做事项。
2. `phase11B_batch01_independent_audit.csv`
   - 对 P1 三行逐行判断：source_ok、classification_ok、body_policy_ok、must_fix、should_fix。
3. `phase11B_batch01_independent_audit.md`
   - 用中文说明三条题的审计结论，尤其审 `Q-2025东城期末-18-2` 是否真可作为创新思维正文候选。
4. `phase11B_next_batch_recommendation.md`
   - 建议下一批从 P2/P3/P4/P5 哪些题开始，理由必须来自 priority queue，不要泛泛而谈。
5. `progress.md`
   - 记录你实际读了什么、写了什么、没有做什么。

## 审稿重点

- `Q-2025东城期末-18-2`：是否必须加入“思路新、方法新、结果新”？还是保留为联想 + 发散聚合更安全？是否容易和“创新思维总称”空喊混淆？
- `Q-2026通州期末-9`：只作选择题陷阱索引是否正确？“系统化、数字化整合”会不会误导学生以为这是主观题可写小方法？
- `Q-2024朝阳二模-7`：A 选项错误更准确应叫“小项不当扩大 / 结论主项外延扩大 / 三段论项外延错误”，还是中项不周延？请纠正旧档案里不准的表述。
- 检查候选稿是否有后台话术、源路径、英文内部字段、审计状态混入学生正文。

## 输出口径

你可以写审计文件，可以建议 patch，但不要直接覆盖 Codex 的 student body 主稿。若发现 must-fix，写清楚应 patch 的句子和理由。若认为 Batch01 可过，写 `PASS_WITH_RECOMMENDED_PATCHES` 或 `PASS_CLEAN`，但不得写 final PASS。
