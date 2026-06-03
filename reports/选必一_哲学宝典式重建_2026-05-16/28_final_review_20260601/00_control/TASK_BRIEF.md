# TASK_BRIEF

## User Request

用户要求对已经生成的选必一《当代国际政治与经济》终极版宝典再做一遍最终审查，并允许使用多 agent 并行审查。

## Objective

对 `/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终极版_20260531.docx` 做终审二次复核：

1. 所有条目的来源必须绝对真实，能回到桌面原试卷和细则。
2. 所有条目的叙述必须准确，尤其逐条核准：设问、同题组、试卷序号。
3. 以聪明且勤奋、马上高考的高三学生视角，正向阅读“为什么能想到”和“答案落点”，判断是否读得懂、能迁移，并对不顺处提出修改。
4. 排版必须对齐先前哲学宝典，不出现字体和格式问题。

## Current Inputs

- Word 终稿：`/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终极版_20260531.docx`
- 先前验收矩阵：`../27_from_zero_source_locked_rebuild_20260531/05_qa/FINAL_ACCEPTANCE_MATRIX.csv`
- 证据卡目录：`../27_from_zero_source_locked_rebuild_20260531/02_source_cards/raw_cards/`
- 哲学宝典样式参考：`/Users/wanglifei/Desktop/桌面整理_20260529/政治成品文档/哲学宝典最终版-飞哥正志讲堂.docx`

## Non-Negotiable Rules

- 不因上一轮 PASS 就默认这轮通过；必须重新检查当前文件。
- 多 agent 只能辅助发现问题，最终判断以原试卷、细则、终稿 DOCX、可复现脚本为准。
- 发现错项优先修正文档和证据链；不能用解释掩盖。
- 学生版仍不得展示 `细则依据/细则位置/源文件/证据层级` 等后台审计字段。
