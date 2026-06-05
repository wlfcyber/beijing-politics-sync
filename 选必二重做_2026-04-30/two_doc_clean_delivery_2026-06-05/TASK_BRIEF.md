# 选必二二文档干净交付 TASK_BRIEF

created_at: 2026-06-05

## 用户目标

只交付两个可以直接给学生使用的选必二文档：

1. `试题和细则汇编`：汇集 2024-2026 三年全部选必二主观题。每个条目包含：题目来源、材料、设问、细则、答案落点、同题组。
2. `学生宝典`：沿用先前从 0 生长出的 AB 双轴框架。每个 A 轴核心要点下先列核心答题点和必备知识，再穷尽放入所有相关主观题；每题字段同汇编。

## 明确删除

- 删除三十秒速记、十主题加深卡、命题人路径卡、工程审计表、制作记录、source_id、entry_id 等后台痕迹。
- 不把 A 类十主题工作稿当最终形态。
- 不把本地 QA 或 Codex 自检包装成 Claude Opus 4.8 Cowork 终审。

## 证据底座

- 题源与细则底座：`../raw_exam_subjective_compilation_2026-06-02/03_source_packets/source_packets_final.jsonl`
- 回源修复覆盖层：`../raw_exam_subjective_compilation_2026-06-02/05_output/A_THEME_SOURCE_REPAIR_OVERRIDES_20260604.json`
- pending 边界覆盖层：`../raw_exam_subjective_compilation_2026-06-02/05_output/A_THEME_PENDING_BOUNDARY_RESOLUTIONS_20260604.json`
- AB 框架底座：`../../reports/选必二法律主观题框架_从题源生长/v12_2_framework_growth_restart/v14_5_final_markdown_baodian_claude_pass_hardened/`

## 外部复核门槛

- 每完成一版，必须提交 Claude Opus 4.8 Cowork 检查完整性、准确性、可读性和是否可直接发给学生。
- Claude 反馈有瑕疵则先修文档，再回送 Claude 复核。
- Claude 通过后，还必须提交 GPT-5.5 Pro 做最终审阅；GPT-5.5 Pro 有任何瑕疵则继续修，再回送终审。
- 不得把 Codex 本地 QA、脚本自检或未完成的外部复核包装成最终通过。

## 当前最小步骤

生成第一版二文档草稿和 Claude Cowork 复查包；不得声称最终完成。
