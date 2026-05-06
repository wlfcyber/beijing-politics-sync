# VSCode ClaudeCode Lane V1 Prompt

你是用户在 VSCode 里单开的 ClaudeCode。注意：现在已有一个 Codex 监督的 Terminal ClaudeCode 正在跑，两个线程不能串线、不能抢同一批文件写。

## 你的身份

- Lane：`V1_VSCODE_CLAUDECODE`
- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- 默认输出目录：`claudecode_lane/vscode_lane_phase11C/`

## 先读

1. `00_control/CLAUDECODE_THREAD_ROUTING_2026-05-05.md`
2. `08_review/phase11C_bad_word_four_element_failure_audit.md`
3. `codex_lane/phase11C_bad_word_content_audit/codex_four_element_rebuild_contract.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
5. 失败样本：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04/04_delivery/选必三逻辑与思维_完全模仿哲学宝典_学生版_2026-05-04.md`
6. 哲学标杆：`/Users/wanglifei/Desktop/北京高考政治/必修四终极融合版_2026-05-02/outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_终极融合版.md`

## 不许碰

- 不要写 `claudecode_lane/phase11C_bad_word_content_audit_visible/`，这是 Terminal ClaudeCode T1 的输出区。
- 不要改 `09_student_draft/`。
- 不要生成 Word、PDF、final、终稿、宝典成品。
- 不要把失败 Word 当底稿继续美化。

## 你的任务

只做独立内容批判和样例重写，输出到 `claudecode_lane/vscode_lane_phase11C/`：

1. `vscode_lane_status.md`：确认你已识别双线程分工。
2. `four_element_quality_rubric.md`：用中文写出你认为“像哲学宝典”的四要件质量标准。
3. `worst_30_entries_review.csv`：从失败样本中挑 30 个最差条目，说明失败原因。
4. `rewrite_samples_8_entries.md`：重写 8 个样例；如果没有准确设问或来源，写 `BLOCKED_NEEDS_SOURCE`，不要猜。
5. `vscode_lane_progress.md`：记录读写文件。

## 核心标准

每个学生条目必须做到：

- `材料触发点`：学生能圈出来的具体材料信号。
- `设问`：真实题目设问，不许模板假设问。
- `为什么能想到`：材料信号 -> 总帽子 -> 小方法 -> 触发逻辑。
- `答案落点`：学生可直接写在答题纸上的答案句。

禁止正文出现：`本题要求结合材料说明其体现的思维方法`、`卷面要把`、`先写`、`要写`、`本题需要`、`设问要求`、`采分点`。
