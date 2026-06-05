# Claude Opus 4.8 窄版外审 prompt v4

你现在只做外部审查，不改写任何文件。请只读取以下三个文本文件，不读取 DOCX/PDF：

- 试题细则汇编 Markdown：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/outputs/选必二法律与生活_试题细则汇编_学生可发版_v4.md`
- AB 双轴学生宝典 Markdown：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v4.md`
- QA 清单：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/qa/TWO_DOC_CLEAN_DRAFT_QA_v4_20260605.md`

用户要求只有两个最终学生文档：

1. 试题和细则汇编。汇集 2024-2026 全部选必二主观题；每条必须有题目来源、材料、设问、细则、答案落点、同题组。
2. AB 双轴学生宝典。沿用从题源生长的 A/B 双轴框架；每个 A 轴核心要点下必须先列核心答题点和必备知识，再穷尽相关主观题，每题字段同上。

硬规则：

- 删掉三十秒速记、工程痕迹、制作记录、画蛇添足栏目。
- 学生稿不能出现本机路径、source_id、entry_E、教师复核提示、待核、TODO、BLOCKED。
- 答案落点必须来自细则，不能另造。
- 对需要图片的题，必须判断文字还原是否足够；不够就指出必须用精准截图。
- 重点裁决 E009 是否能保留，E057 是否应移出选必二。

请输出：

1. verdict: PASS / CONDITIONAL_PASS / NOT_PASS / BLOCKED
2. P0 必改项：没有就写 none；有就列 entry/title/problem/fix。
3. P1 进入 GPT-5.5 Pro 前必须处理项：没有就写 none。
4. 图片/文字保真裁决：逐条指出 E005、E009、E074、E015、E016、E022、E023、E024、E029、E033、E035、E036、E050、E052、E057、E059、E072 是否还需要更精准截图。
5. A/B 归位硬伤：没有就写 none。
6. E009/E057 裁决。
7. 是否允许进入 GPT-5.5 Pro 终审。
