# Development Plan

1. 前置控制
   - 固化本轮硬规则、双线分工、真实外审闸门。
   - 读取旧 2026-05-06 选必三二线闭合版，只作为候选索引和失败/成功样本。

2. 源扫描
   - 扫描 `2024各区模拟题`、`2025各区模拟题`、`2026各区模拟题`。
   - 同步扫描缓存 `beijing_politics_research/data/preprocessed_corpus` 与历史选必三产物。
   - 建立 `SOURCE_LEDGER.csv` 与 `QUESTION_COVERAGE_MATRIX.csv`。

3. Codex A 线制作
   - 先做候选题源分类：思维、推理、选择题陷阱、边界、missing。
   - 建立 `MAIN_THINKING_LEDGER.csv`、`REASONING_FORM_LEDGER.csv`、`CHOICE_TRAP_LEDGER.csv`。

4. ClaudeCode B 线制作
   - 真实启动 ClaudeCode，保存版本、命令、模型、日志。
   - 要求它按套卷闭环：source rows、coverage rows、entries、suite report、blocker。

5. 融合
   - Codex 对照 A/B 两线，按证据优先裁决，不按表达漂亮程度裁决。
   - 思维条目进入框架节点；推理条目进入推理形式节点。

6. 外审
   - 生成 GPT Pro 与 Claude 的真实审核包。
   - 捕获原始反馈，并回源裁决每条采纳/拒绝/待定。

7. 交付
   - 先交 Markdown。
   - 如生成 DOCX/PDF，必须渲染检查。
   - 最终报告列明未闭合、已排除、真实外审证据和同步状态。
