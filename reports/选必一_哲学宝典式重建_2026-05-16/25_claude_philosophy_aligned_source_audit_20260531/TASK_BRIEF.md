# TASK_BRIEF

## 任务

对 Claude 修订稿逐条回到桌面原始试卷与评分细则核查，确认题号、设问、材料/卷面句、得分层次、分值标注、模块归属是否可靠。

## 输入文档

`/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_ea19f1a6-c672-4010-9aa6-235ad1631aa4/outputs/选必一_当代国际政治与经济_主观题术语宝典_哲学对齐版_20260531.docx`

## 原始来源范围

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`
- 必要时使用 `/Users/wanglifei/Desktop/北京高考政治` 与同步仓库中已登记的抽取缓存作为定位线索，但结论必须回到桌面原卷/细则。

## 验收标准

- 每条至少登记来源题号、试卷文件、细则文件或无法核实原因。
- 设问必须与原卷一致，不能擅自改写。
- 得分层次必须保留细则原文核心动作词、层级和分值上限。
- 材料触发/卷面句必须能在原卷材料中找到，不能凭空补写。
- 模块边界必须符合选必一；明显属于哲学、经济与社会等其他模块的条目要标出。
- 只有全部条目达到 `PASS` 或有明确、可解释的 `BLOCKED` 清单后，才能说“确认没问题”。
