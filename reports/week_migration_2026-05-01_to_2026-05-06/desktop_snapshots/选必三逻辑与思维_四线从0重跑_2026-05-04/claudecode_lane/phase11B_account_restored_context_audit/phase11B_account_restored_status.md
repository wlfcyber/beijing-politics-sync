# Phase11B Account-Restored Status (ClaudeCode Lane B 独立审计)

时间：2026-05-05（窗口可见、前台执行；不另起后台、不用 -p 非交互）
账号：`[CLAUDE_ACCOUNT_REDACTED]`，subscriptionType=`max`（Codex 已确认）。
模型：Claude Opus 4.7（claude-opus-4-7）。
任务边界：Phase11B controlled expansion / source repair 审计；不重写全书、不出终稿。

## 一、上下文识别

- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`。
- 当前阶段：`phase11B_controlled_expansion_authorized_no_word_no_final`（来自 `task_plan.md`）。
- GPT 当前授权：`GO_PHASE11B_CONTROLLED_EXPANSION_NO_WORD_NO_FINAL`（来自 Phase11A patch-resolution）。
- 处理批次：Batch01，仅 P1 三行；P0/L0/hard-excluded/45 hold rows/74 行整体扩张/同类题自动扩展全部禁止。
- ClaudeCode 之前因会员失效被全线 suspended；现在账号已恢复，本审计是 Lane B 重新接续后的第一次输出，不继承旧账号、旧会话、旧结论。

## 二、本轮禁止事项

- 不直接覆盖 Codex 学生稿主稿（`09_student_draft/phase11A_student_body_PATCHED_REVIEW_ONLY.md`）。
- 不扩成 74 行正文。
- 不合并 45 条 hold rows。
- 不使用 288 条 L0、hard-excluded rows。
- 不生成 Word/PDF/final/终稿/最终稿/宝典成品/FINAL PASS。
- 不写 final PASS；最多写 `PASS_WITH_RECOMMENDED_PATCHES` 或 `PASS_CLEAN`。
- 不以 ClaudeCode 名义在缺乏证据时拍板裁决；只能写"建议 patch / 待 GPT 与 Codex 确认"。
- 不放任何源路径、line id、英文内部字段、审计状态、模型话术进入审计建议中可能被复制进学生正文的句子。

## 三、本轮可做事项

- 读 P1 三行的本地源证据（试卷正文+答案表/答案解析），独立校验 source/classification/body-policy。
- 对比旧档案 (`05_coverage/phase06_evidence_lock_register.csv`、`phase06_reasoning_typology_fusion.csv`) 与本批 candidate entries 的术语差异。
- 写：
  - `phase11B_account_restored_status.md`（本文件）
  - `phase11B_batch01_independent_audit.csv`
  - `phase11B_batch01_independent_audit.md`
  - `phase11B_next_batch_recommendation.md`
  - `progress.md`
- 给出 must_fix / should_fix 句级建议；裁决限于 `PASS_WITH_RECOMMENDED_PATCHES`。

## 四、关键证据指针（仅供本目录审计追溯，不进学生正文）

- `Q-2025东城期末-18-2`：
  - 题面：`02_extraction/priority_queue_sources/text/012_…2025东城期末_试卷.pdf.txt` 行 199-203、205-208。
  - 答案解析：同文件行 681-688；分项答案：行 695-698。
- `Q-2026通州期末-9`：
  - 题面：`02_extraction/priority_queue_sources/text/006_…2026通州期末_试卷.pdf.txt` 行 126-132。
  - 客观题答案表：同文件行 318-328（Q9=D，第 9 列）。
- `Q-2024朝阳二模-7`：
  - 题面：`02_extraction/priority_queue_sources/text/021_…2024朝阳二模_试卷.pdf.txt` 行 109-127。
  - 答案表：`023_…2024朝阳二模_细则_补充材料_细则.docx.txt` TABLE 1（Q7=D）。

## 五、与旧档案的偏差

- `05_coverage/phase06_evidence_lock_register.csv` 第 9 行与 `phase06_reasoning_typology_fusion.csv` 第 7 行均把 `Q-2024朝阳二模-7` A 选项错挂为"三段论中项不周延"。本独立审计判定该术语错误，应改为"小项不当周延 / 小项扩大（illicit minor）"。Codex Batch01 候选条目方向已对（"扩大了娱乐工具的外延"），但术语未规范化。

## 六、结论

- 本 Lane B 审计接续点干净：账号已恢复、上下文已锁定、禁止事项已识别。
- Batch01 三行的源证据局部可核验；存在 1 条 must_fix（朝阳二模7 A 错项术语）+ 多条 should_fix。详见 `phase11B_batch01_independent_audit.md`。
- 本目录最终裁决由 `phase11B_batch01_independent_audit.md` 出，限于 `PASS_WITH_RECOMMENDED_PATCHES`，绝不写 final PASS。
