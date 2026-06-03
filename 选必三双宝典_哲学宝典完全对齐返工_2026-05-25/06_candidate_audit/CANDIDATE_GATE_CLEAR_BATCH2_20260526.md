# CANDIDATE_GATE_CLEAR_BATCH2_20260526

time: 2026-05-26T01:12:00+08:00

verdict: `FOUR_MAIN_ENTRIES_GATE_CLEARED_FINAL_STILL_BLOCKED`

本批次只清理“题面 + 答案/细则”双锁的推理主观题门禁，并把程序化触发句改成更接近哲学宝典的学生可迁移表达。它不是最终验收。

## 清理条目

| 条目 | 原卷题面证据 | 答案/细则证据 | 处理 |
| --- | --- | --- | --- |
| 2024丰台一模 Q19(1) | `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.md:235-250` | 同文件 `:332` | 删除 `候选稿门禁`；重写“为什么能想到”为“横线后果 -> 补充分条件前件”的触发链。 |
| 2025丰台二模 Q19(1) | `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/9f3b486088840b52_2025北京丰台高三二模政治_教师版.md:313-314` | 同文件 `:409-412` | 删除 `候选稿门禁`；重写为“只要……就…… -> 技术措施不是充分条件”的触发链。 |
| 2025东城二模 Q18(2) | `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/9b287871f660f23d_2025北京东城高三二模政治_教师版.md:184-187` | 同文件 `:276-278` | 删除 `候选稿门禁`；重写为“形式像肯前肯后，但前提把必要条件误作充分条件”的触发链。 |
| 2025朝阳一模 Q17(1) | `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/e051761a7fc68fef_2025北京朝阳高三一模政治_教师版.md:190-198` | 同文件 `:310-315` | 删除 `候选稿门禁`；重写为“离不开 -> 必要条件 -> 肯定前件不能推出后件”的触发链。 |

## 正文改写原则

- 保留哲学宝典式四件套：`题干触发点 / 设问 / 为什么能想到 / 答案落点`。
- 不再用“看到题目把前提和结论组织成……”这类后台归类话术作主体。
- 每条都从题面中的语言信号出发，说明为什么触发对应推理形式，再落到学生能写的答案句。

## 当前计数影响

- 推理候选稿 `候选稿门禁`：由 54 条降为 50 条。
- 思维候选稿 `候选稿门禁`：仍为 36 条。

## 继续阻断

- 推理候选稿仍有 50 条 `候选稿门禁`，其中大量是选择题逐项错因待回源。
- 思维候选稿仍有 36 条 `候选稿门禁`。
- DOCX/PDF、目录页码、视觉 QA、真实 GPT Pro / Claude 对齐审查尚未完成。
