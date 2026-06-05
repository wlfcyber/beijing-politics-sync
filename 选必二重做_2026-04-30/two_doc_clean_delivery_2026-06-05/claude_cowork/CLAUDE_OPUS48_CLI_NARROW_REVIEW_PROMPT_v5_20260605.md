# Claude Opus 4.8 v5 复审请求

你是外部质检。请只做审查，不改文件。

请读取并审查以下文件：

- `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/outputs/选必二法律与生活_试题细则汇编_学生可发版_v5.md`
- `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v5.md`
- `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/qa/TWO_DOC_CLEAN_DRAFT_QA_v5_20260605.md`

v4 你判定 CONDITIONAL_PASS，并要求先修：

1. 2026 东城一模第18题串入太阳风/星际/新质生产力产业题，必须删除并整理三案例细则。
2. 2025 石景山一模第20题细则文字为空，必须补案例一和案例二评分点。
3. 2025 海淀期末第20题材料缺《解释》条款，必须补表格条款文字。
4. 宝典中 2026 西城二模第18题第3问不能挂在 A10 核心轴，应移到跨模块背景题。
5. 学生稿同题组不能泄露 E0xx 内部编号。

请重点复核 v5 是否已经解决以上问题，并抽查整体学生可发性：

- 两份文档是否仍然只有学生需要的题目来源、材料、设问、细则、答案落点、同题组；宝典另有框架归位和 A 轴核心知识是允许的。
- 是否还存在三十秒速记、工程痕迹、路径、E0xx 编号、source_id、TODO/BLOCKED 等不该出现在学生稿里的内容。
- 三个 P0 修订题的材料、设问、细则、答案落点是否足以学生直接使用，且没有另造答案。
- E057 是否已经不再作为 A10 核心题呈现。
- 是否允许进入 GPT-5.5 Pro 终审。

请按以下格式输出：

1. verdict：PASS / CONDITIONAL_PASS / FAIL
2. 是否允许进入 GPT-5.5 Pro：YES / NO
3. 必改项：如无写“无”
4. 仍建议改但不阻断项：如无写“无”
5. 对三项 P0 和 E057 的逐项裁决
