# Phase11B Batch01 GPT-5.5 Pro Review Prompt

你是本项目的 GPT-5.5 Pro 内容总审稿。补充最新状态：用户的 Claude/ClaudeCode 会员已经恢复，且用户要求 ClaudeCode 必须在可见窗口真实工作。Codex 已接收到一个可见窗口 ClaudeCode 对本批的独立审计 CSV；它只给 `PASS_WITH_RECOMMENDED_PATCHES`，不写 final PASS。Codex 已先按它的 must-fix 做本地补丁，现在把补丁后的 Batch01 交给你审稿。

## Context

本项目是北京高考政治选必三《逻辑与思维》从 0 重跑。Phase10 已形成 29 条受控学生稿；Phase11A 已经经过你的内容审稿和补丁闭合。你给出的最新门禁是：

`GO_PHASE11B_CONTROLLED_EXPANSION_NO_WORD_NO_FINAL`

因此 Codex 现在只处理 Phase10.5 优先级队列里的 P1 三条，不扩 74 行，不出 Word/PDF/final。

## Files Produced For This Batch

- `09_student_draft/phase11B_batch01_P1_source_repair_matrix.csv`
- `09_student_draft/phase11B_batch01_P1_candidate_entries.md`
- `08_review/phase11B_batch01_codex_local_verification.md`
- `claudecode_lane/phase11B_account_restored_context_audit/phase11B_batch01_independent_audit.csv`
- `08_review/phase11B_claudecode_account_restored_feedback_digest.md`

## Codex Local Decisions

1. `Q-2025东城期末-18-2`
   - 修源结论：题干明确要求“运用《逻辑与思维》知识，说明登月服设计是如何体现创新思维的”。
   - 证据：材料支持“飞天飘带/火箭尾焰/服装造型”的联想思维；月面出舱任务的行走、攀爬、驾车、科考、防护、防眩光支持发散与聚合。
   - ClaudeCode must-fix 后 Codex 补丁：补入细则锚点“思路新、方法新、结果新”，但必须与登月任务、月面环境、航天员行动需要和登月服设计事实绑定。
   - Codex 决定：修掉旧档案中“形式推理/三段论”误挂风险，作为创新思维主观题候选，等待你审稿后才进入正文。

2. `Q-2026通州期末-9`
   - 题面：医保+商保清分结算中心打通数据壁垒，一站式结算，实现“数据多跑路，群众少跑腿”。
   - 答案：D。
   - ClaudeCode must-fix 后 Codex 补丁：把“系统化、数字化整合”改为材料事实信号，不把它写成可迁移的选必三小方法；补 B/C 错项说明。
   - Codex 决定：只作为选择题陷阱索引，不作为主观题正文扩展。

3. `Q-2024朝阳二模-7`
   - 题面：科学思维离不开逻辑，四个选项分别涉及逻辑结构判断。
   - 答案：D。
   - ClaudeCode must-fix 后 Codex 补丁：A 项不再叫“中项不周延”，改为“小项不当周延/小项扩大”，理由是小项“娱乐工具”在前提中不周延，却在结论中变全称。
   - Codex 决定：只作为推理题型索引，不作为思维方法正文扩展。

## Please Review

请只做内容审稿，给出明确 verdict：

- `PASS_BATCH01_MERGE_ONE_BODY_CANDIDATE`：允许把东城期末18(2)并入学生正文，通州9/朝阳二模7只入索引；
- `MUST_FIX_BATCH01_BEFORE_MERGE`：指出必须修的概念错误、题型误判或学生表达问题；
- `BLOCK_BATCH01`：如果三条中有源证据或分类不可接受的问题。

重点请检查：

1. 东城期末18(2)是否可以作为“创新思维：联想 + 发散聚合”的正文候选？
2. 通州期末9只作选择题陷阱索引是否合理？“系统化、数字化整合”是否会误导成选必三主观题方法？
3. 朝阳二模7只作推理题型索引是否合理？A 选项错误改为“小项不当周延/小项扩大（娱乐工具外延扩大）”是否准确？
4. 当前候选条目是否有会误导弱学生的表达？

禁止输出 Word/PDF/final PASS。请直接给出：verdict、must_fix、should_fix、approved_merge_policy。
