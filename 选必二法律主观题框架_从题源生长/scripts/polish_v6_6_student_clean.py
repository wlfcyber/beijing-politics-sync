from __future__ import annotations

import re
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
SRC = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_6_学生清洁候选稿_20260521.md"
OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.md"
REPORT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_7_学生使用版_抛光报告_20260521.md"


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = text.replace("副标题：学生清洁候选稿", "副标题：学生使用版（27核心满分训练 + 38保分索引）")
    text = text.replace("本表是 V6 新增的刹车。", "这张表专门防止把隔壁题的满分词误搬过来。")
    text = text.replace("### REFERENCE-ONLY 练笔区（4 题）", "### 普通答案练笔区（4 题）")
    text = text.replace("### SOURCE-CHECK 回源保分区（24 题）", "### 回源保分区（24 题）")
    text = text.replace("source-check 当满分", "回源题当满分")
    text = text.replace("reference_only 误升核心", "普通答案题误当核心")
    text = text.replace("formal 满分闭环", "正式满分闭环")
    text = text.replace("formal", "正式评分材料")
    text = text.replace("reference_only", "普通答案")
    text = text.replace("source-check", "回源题")
    text = text.replace("core", "核心")
    text = text.replace("guard/index", "保分索引")
    text = re.sub(r"- 题号证据：`([^`]+)`；证据等级：`([^`]+)`。", r"- 题源：`\1`；来源状态：`\2`。", text)
    text = re.sub(r"- 证据等级：`([^`]+)`；学生标签：", r"- 来源状态：`\1`；学生标签：", text)
    text = text.replace("来源状态：`正式评分材料`", "来源状态：`有正式评分材料支撑`")
    text = text.replace("来源状态：`普通答案`", "来源状态：`只有普通答案，不能当正式细则`")
    text = text.replace("教师不得把它说成", "课堂使用时不得把它说成")
    text = text.replace("教师再核对", "回原题再核对")
    text = text.replace("教师后台", "教师用")
    text = text.replace("后台", "教师用")
    text = text.replace("学生清洁候选稿", "学生使用版")
    # Keep traceable source ids in backticks; they help teachers locate examples while not driving student action.
    OUT.write_text(text, encoding="utf-8")
    scan_terms = ["候选稿", "reference_only", "source-check", "guard/index", "V6 新增", "教师后台"]
    counts = {t: text.count(t) for t in scan_terms}
    REPORT.write_text(
        "# V6.7 学生使用版抛光报告\n\n"
        "输入：V6.6 学生清洁候选稿。\n\n"
        "已执行：\n\n"
        "1. 剥离“候选稿”口吻，改成学生使用版。\n"
        "2. 把 reference_only/source-check/core/guard 等后台词改成人话。\n"
        "3. 把证据等级改为“来源状态”，既保留边界又减少工程味。\n"
        "4. 保留题源 ID，供教师追溯；学生可以跳过。\n\n"
        "残留扫描：\n\n"
        + "\n".join(f"- {k}: {v}" for k, v in counts.items())
        + f"\n\n输出：`{OUT}`\n",
        encoding="utf-8",
    )
    print(OUT)
    print(REPORT)


if __name__ == "__main__":
    main()
