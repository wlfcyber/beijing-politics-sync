# 选必二《法律与生活》严格四线闭环：ClaudeCode B 独立生产线任务

你是 ClaudeCode 独立生产线 B，本项目专用会话。不要继承其他项目上下文，不要复用其他项目结论。

## 任务背景

用户要求补齐严格四线工作流。本轮不是普通审稿，而是要检查最新版“零基础强补版”两份文档能否补上先前学会性缺口，并形成 ClaudeCode B 的独立生产线输出。

## 只读取这两份最新版学生文档

- `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/strict_four_lane_closure_2026-05-04/delivery/选必二法律框架踩分逻辑_零基础强补版_2026-05-04.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/strict_four_lane_closure_2026-05-04/delivery/选必二考过情境细则汇总_零基础强补版_2026-05-04.md`

必要时可以读取本地小本本和 skill 以确认规则，但不要把旧选必二成果当内容证据。

## 请直接写入两个输出文件

你不是独自在代码库里工作，可能还有 Codex、GPT、Claude 网页端并行。不要改动 delivery 下的学生文档，不要回滚任何文件。只写这两个文件：

1. `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/strict_four_lane_closure_2026-05-04/claudecode_lane/outputs/CLAUDECODE_B_STRICT_REVIEW_2026-05-04.md`
2. `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/strict_four_lane_closure_2026-05-04/claudecode_lane/outputs/CLAUDECODE_B_PATCH_AND_ACCEPTANCE_MATRIX_2026-05-04.md`

## 检查标准

请以“聪明但零基础高三学生能否用它做新题”为中心，检查：

1. 是否已经补上争点生成方法，而不是只靠旧题检索。
2. 高频要件卡是否足以堵住先前暴露的系统性丢分点：竞业限制经济补偿、遗赠扶养书面形式、无过错责任免责减责、消费者欺诈/违约/知情权分线、民事公益诉讼 vs 行政公益诉讼。
3. 五域划分是否更清楚，尤其消费者/合同/劳动是否不会混淆。
4. 主观题和选择题是否仍分开，选择题是否被明确限制为识别池。
5. 新增内容是否有法考化风险、超教材风险、宏观价值空转风险。
6. 是否存在学生文档不应出现的后台词、模型词、路径、debug、pipeline、PASS/FAIL 等。
7. 哪些补丁可以直接采纳，哪些必须回本地题源核验，哪些应该拒绝。

## 输出格式

第一个文件写：

- overall_verdict: PASS / CONDITIONAL_PASS / FAIL
- can_student_do_new_questions: YES / ALMOST / NO
- can_student_stably_full_score: YES / ALMOST / NO
- strengths
- remaining_blockers
- exact_lines_or_sections_to_fix
- risk_of_overlegalization
- risk_of_macro_value_empty_talk
- risk_of_choice_question_misuse
- final_recommendation_to_codex

第二个文件写表格：

| issue_id | location | issue | severity | proposed_patch | source_check_needed | decision_suggestion |

severity 只能用：must_fix / should_fix / optional / reject。

注意：如果你提出任何新的具体法律要件或结论，必须标注 `source_check_needed=yes`，因为最终是否进入学生文档由 Codex 本地证据裁决。
