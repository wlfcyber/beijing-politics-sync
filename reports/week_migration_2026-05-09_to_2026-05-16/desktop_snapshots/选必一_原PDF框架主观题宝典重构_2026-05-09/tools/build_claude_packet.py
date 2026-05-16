#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


RUN = Path("/Users/wanglifei/Desktop/北京高考政治/选必一_原PDF框架主观题宝典重构_2026-05-09")


def read(rel: str) -> str:
    return (RUN / rel).read_text(encoding="utf-8-sig" if rel.endswith(".csv") else "utf-8")


def main():
    out = RUN / "04_claude_packet" / "claude_task_packet.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf_table = read("01_framework/pdf_original_framework.csv")
    subjective_pool = read("03_subjective_filter/subjective_question_pool.csv")
    pollution = read("02_old_doc_audit/old_doc_pollution_report.md")
    unclear = read("01_framework/pdf_unclear_items.md")
    packet = f"""# ClaudeCode 任务包：选必一 PDF 原框架主观题宝典初稿

你是 ClaudeCode B 生产线。本任务必须只生成初稿，不做最终审计。最终裁决由 Codex 完成。

## 绝对规则

1. 正文原框架只来自 `01_framework/pdf_original_framework.csv`。
2. 不得从旧 Word 中抽取或新增小框架。
3. 旧 Word 只作为主观题素材池：题源、材料触发点、设问、踩分词、答案落点。
4. 任何 PDF 没有但主观题答案/细则给分的术语，只能标为【考题增补术语】，挂靠在 PDF 已有小框架下。
5. 不能挂靠的内容不要写入正文，留给 Codex 放入 candidate_new_angle_report。
6. 一级标题只能是六要素，且顺序固定：一、时代背景；二、理论；三、经济全球化；四、政治多极化；五、中国；六、联合国。
7. 每个一级标题下必须先列 PDF 小框架，再列答题术语，再列主观题出处。
8. 禁止出现：选择题、客观题、30秒读题法、六桶读题总图、按题训练闭环、慎用与跨模块表达专章、后台字段、路径、debug、audit。
9. 制度型开放、NDC、全球南方、治理赤字、全球性挑战、逆全球化、零和博弈等不得伪装成 PDF 小框架。

## 输出目标

请输出完整 Markdown 初稿，供 Codex 保存为 `05_claude_draft/claude_draft.md`。

正文结构：

封面
目录
前言（最多一页）
一、时代背景
二、理论
三、经济全球化
四、政治多极化
五、中国
六、联合国

每个答题术语用以下格式：

### 术语标题

【答题术语】
只写本术语及其同层表述，不得堆其他要素术语。

【触发材料】
写材料中哪些词、动作、对象会触发该术语。

【大题出处】

1. 年份区县考试 题号（主观题）

【材料触发点】
写材料中真正触发该术语的词、句、动作或结构。

【设问】
完整写原设问，不得改写成占位句，不得添加人工标签。

【为什么能想到】
必须写清：看到材料中的什么信号；先归入哪个六要素；再归入哪个 PDF 小框架；为什么触发当前答题术语；为什么不优先写相邻术语；这道主观题如何踩分。

【答案落点】
格式必须是：答题术语 + 材料事实 + 设问回扣。

## PDF 原框架表

```csv
{pdf_table}
```

## PDF 不清楚项

{unclear}

## 旧稿污染项清单

{pollution}

## 旧稿筛选出的主观题素材池

```csv
{subjective_pool}
```

## 哲学宝典式四段触发链样板

不照搬哲学内容，只借鉴结构：

1. 【材料触发点】材料中可圈出来的词、动作、对象、矛盾或结构。
2. 【设问】完整题问。
3. 【为什么能想到】材料信号 -> 六要素 -> PDF 小框架 -> 当前术语 -> 排除相邻术语 -> 如何踩分。
4. 【答案落点】术语 + 材料事实 + 设问回扣，写成学生可直接上卷面的句子。
"""
    out.write_text(packet, encoding="utf-8")
    print(out)
    print(f"bytes={out.stat().st_size}")


if __name__ == "__main__":
    main()
