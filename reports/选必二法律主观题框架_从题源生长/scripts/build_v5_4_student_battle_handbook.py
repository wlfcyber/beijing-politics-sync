#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now().strftime("%Y%m%d")
STAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def after_heading(text: str, heading: str) -> str:
    idx = text.find(heading)
    if idx == -1:
        return text
    return text[idx:].strip()


def strip_title(text: str) -> str:
    lines = text.splitlines()
    while lines and (not lines[0].strip() or lines[0].startswith("# ") or lines[0].startswith("生成时间：")):
        lines.pop(0)
    return "\n".join(lines).strip()


def main() -> None:
    framework = read(ROOT / f"11_final_framework/framework_v5_2_student_one_page_{TODAY}.md")
    examples = read(ROOT / f"12_final_baodian/选必二法律主观题满分宝典_v5_3_27核心清洗学生版_{TODAY}.md")

    examples_part = after_heading(examples, "## 27 道核心题逐题示范")
    framework_part = strip_title(framework)

    front = f"""# 选必二法律主观题满分宝典 V5.4 学生战斗清洗版

生成时间：{STAMP}

## 当前身份

这不是“65 题全部核心满分闭环”的冒进版，而是基于 65 题证据池里已经清洗出的 **27 道严格核心题** 做成的学生可用版。

- 65 题事实基线：61 道有正式细则，4 道只有普通答案，暂未发现无答案细则题。
- 本稿只把已清洗的 27 道核心题放进学生正文。
- 只有普通答案的题、开放容器题、边界题不支撑核心套路，不能乱背乱套。

## 使用顺序

1. 先读“20 秒启动”和“六张动作卡”，知道陌生题第一笔写什么。
2. 再看“必踩硬词句库”，把常丢分的法律链背成完整句。
3. 最后刷 27 道核心题示范，学会把材料事实改写成法律语言。
4. 考场上每道题只选一张主卡，最多加一张辅卡。卡太多，说明你还没看懂设问。

## 入口总表

| 设问/材料信号 | 主卡 | 第一笔 |
|---|---|---|
| 表格、完成下表、补全笔记 | 一格一答 | 先看每个格子要机制、理由、结果还是意义 |
| 是否支持、是否有效、是否构成、判决依据 | 分关系·定责任 | 先表态，再写规则和事实 |
| 知识产权、商标、商业秘密、技术秘密、不正当竞争 | 认产权·抓侵权 | 先认保护对象，再抓侵害行为 |
| 如何维权、调解、仲裁、诉讼、起诉状、举证、公益诉讼 | 排维权步骤 | 写路径、证据、请求、效力 |
| 风险、边界、合规、应对措施、涉嫌违法 | 划风险边界 | 一项风险配一条规则和一项措施 |
| 意义、价值、作用、典型案例 | 推价值 | 因为本案怎么处理，所以保护谁、规范谁、弘扬什么 |

## 答案生成公式

**结论句 + 规则句 + 材料句 + 落点句。**

- 结论句：某请求应支持/不支持；某合同成立/有效/可撤销；某行为构成/不构成侵权、违约、欺诈或不正当竞争。
- 规则句：写民法典、消费者权益保护法、劳动法、反不正当竞争法、著作权法等规则，别只写“依据法律”。
- 材料句：把题干里的付款、派单、搭售、损害、过错、调解、证据等事实塞进规则。
- 落点句：落到责任、救济、程序效力，或从本案推出价值。

---

"""

    out = front + "\n## 第一部分：20 秒启动和必踩硬词\n\n" + framework_part + "\n\n---\n\n## 第二部分：核心题逐题示范\n\n" + examples_part + "\n"

    out_path = ROOT / f"12_final_baodian/选必二法律主观题满分宝典_v5_4_学生战斗清洗版_{TODAY}.md"
    framework_path = ROOT / f"11_final_framework/framework_v5_4_student_core_{TODAY}.md"
    out_path.write_text(out, encoding="utf-8")
    framework_path.write_text(front + "\n## 20 秒启动和必踩硬词\n\n" + framework_part + "\n", encoding="utf-8")

    print(out_path)
    print(framework_path)
    print(f"bytes={out_path.stat().st_size}")


if __name__ == "__main__":
    main()
