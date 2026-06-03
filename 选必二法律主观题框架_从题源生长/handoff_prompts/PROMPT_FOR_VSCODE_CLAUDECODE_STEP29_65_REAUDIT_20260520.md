# 给 VS Code ClaudeCode 的提示词：复核 STEP_29 的 65 题证据层

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 VS Code ClaudeCode 正式复核者。

注意：用户已经否定后续框架和宝典，要求退回到 Codex + ClaudeCode 共同生成 65 题的证据层。

你本轮不要写框架，不要写宝典，不要总结规律。

## 输入目录

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/rollback_to_step29_claudecode_corrected_65_20260520/`

## 任务

请只复核这 65 题证据层是否适合进入下一轮“重新建框架”。

重点检查：

1. 每个 question_id 是否确实是选必二《法律与生活》相关主观题。
2. 题干、材料、设问、答案/细则是否分栏干净。
3. 是否有答案或细则文字污染到题干/材料/设问字段。
4. 是否有题目其实是必修三、经济、哲学、逻辑或综合题，不应进入选必二核心框架。
5. evidence_level 是否保守：reference_only 不得被当作 formal。
6. 2026 期中/期末标注是否仍有错。
7. 是否有遗漏的法律主观题仍不在 65 题内。
8. 是否有多小问混在一个 parent row，必须拆分后才能进框架。

## 输出文件

请在同一工程中输出：

`04_merge_audit/vscode_claudecode_step29_65_reaudit_20260520/vscode_claudecode_step29_65_reaudit_report.md`

`04_merge_audit/vscode_claudecode_step29_65_reaudit_20260520/vscode_claudecode_step29_65_must_fix.csv`

`04_merge_audit/vscode_claudecode_step29_65_reaudit_20260520/vscode_claudecode_step29_65_can_enter_framework.csv`

`04_merge_audit/vscode_claudecode_step29_65_reaudit_20260520/vscode_claudecode_step29_65_exclude_or_boundary.csv`

最终报告必须给出：

PASS / CONDITIONAL_PASS / FAIL

如果不是 PASS，必须列出阻止进入框架的具体 question_id 和修复方式。

