#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
RUN = ROOT / "10_framework_validation" / "v7_method_first_zero_baseline_pressure_20260521"
V71 = ROOT / "12_final_baodian" / "选必二法律主观题满分宝典_v7_1_压测补丁候选稿_20260521.md"
OLD_PACKET = RUN / "clean_student_packet_v7_method_first_20260521.md"
OUT = RUN / "clean_student_packet_v7_1_targeted_regression_20260521.md"

TARGET_LABELS = ["样题 1", "样题 4", "样题 5", "样题 7", "样题 10"]


def section_by_label(text: str, label: str) -> str:
    pattern = rf"## {re.escape(label)}：.*?(?=\n## 样题 \d+：|\Z)"
    m = re.search(pattern, text, flags=re.S)
    return m.group(0).strip() if m else ""


def main() -> None:
    guide = V71.read_text(encoding="utf-8").split("## 第十一部分 27 个核心题逐题运行", 1)[0].strip()
    old = OLD_PACKET.read_text(encoding="utf-8")
    questions = "\n\n".join(section_by_label(old, label) for label in TARGET_LABELS)
    OUT.write_text(
        f"""# V7.1 定向回归压力测试包

身份：聪明但此前不会选必二法律主观题的高三学生。

这次只测试 V7.1 新补丁能否修正上一轮 PARTIAL 的 5 道题。只许使用下面的 V7.1 前台方法和题面，不许看内部评分 key。

{guide}

## 作答任务

对每道题写：

1. 框架入口；
2. 第一判断；
3. 材料翻译；
4. 考场答案；
5. 这次补丁有没有帮到我。

{questions}
""",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
