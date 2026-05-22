from __future__ import annotations

from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
SRC = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_4_双外审硬修候选稿_20260521.md"
OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_5_回归盲测因果硬词补丁稿_20260521.md"
REPORT = ROOT / "10_framework_validation" / "v6_4_regression_naked_test_20260521" / "v6_5_regression_patch_report_20260521.md"


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = text.replace("主观题满分训练宝典 V6.4", "主观题满分训练宝典 V6.5", 1)
    text = text.replace("副标题：双外审硬修候选稿", "副标题：回归盲测因果硬词补丁稿", 1)
    intro = """## V6.5 回归盲测补丁

V6.4 的 C/E/G/H 回归盲测结果是 3 PASS + 1 PARTIAL。唯一硬缺口：表格题 E 的“材料事实”格能直填，但没有把“死亡系自身原因、非他人行为造成、组织行为与死亡无因果关系”写硬。

本版只做一个窄补丁：

- 表格题材料事实格必须同时写“事实 + 因果/非因果判断”。
- 通州表格示范把“自身原因、非他人行为、无因果关系”写入格内。
- 不改变 27 core + 38 guard/index 边界，不升 reference_only/source_check。

"""
    text = text.replace("## V6.4 双外审硬修\n\n", intro + "## V6.4 双外审硬修\n\n", 1)
    text = text.replace(
        "| 材料事实 | 张某自愿参加活动且有基础疾病，李某长期提醒量力而行，事发后及时拨打120并实施救助。 |",
        "| 材料事实 | 张某自愿参加活动且有基础疾病，死亡系自身原因突发意外，并非他人行为造成；李某长期提醒量力而行，事发后及时拨打120并实施救助，组织行为与张某死亡无因果关系。 |",
    )
    text = text.replace(
        "- 改法：先写格子功能，再一格一句；问证据就写证据，问意义才写价值。",
        "- 改法：先写格子功能，再一格一句；问证据就写证据，问意义才写价值。材料事实格不能只堆事实，还要把因果或非因果判断写硬。",
        1,
    )
    text = text.replace(
        "真实考试必须先照抄表格列名和示例行，再按每格功能直接填写；责任判断/法律依据/材料事实/意义只是常见示例，不是固定四格。禁止写“如果表格要求……”。",
        "真实考试必须先照抄表格列名和示例行，再按每格功能直接填写；责任判断/法律依据/材料事实/意义只是常见示例，不是固定四格。材料事实格通常要写“事实 + 因果/非因果判断”。禁止写“如果表格要求……”。",
    )
    OUT.write_text(text, encoding="utf-8")
    checks = {
        "材料事实格因果提示": "事实 + 因果/非因果判断" in text,
        "通州无因果格": "组织行为与张某死亡无因果关系" in text,
        "不升非核心": "不升 reference_only/source_check" in text,
    }
    REPORT.write_text(
        "# V6.5 回归盲测补丁报告\n\n"
        "- 输入：V6.4 双外审硬修候选稿。\n"
        "- 触发：V6.4 C/E/G/H 回归盲测中，样题 2 表格题缺“因果”硬词，判 PARTIAL。\n"
        "- 输出：`12_final_baodian/选必二法律主观题满分训练宝典_v6_5_回归盲测因果硬词补丁稿_20260521.md`\n\n"
        "## 补丁\n\n"
        "1. 表格题通用规则增加：材料事实格要写“事实 + 因果/非因果判断”。\n"
        "2. 通州表格示范材料事实格写入：死亡系自身原因突发意外、非他人行为造成、组织行为与死亡无因果关系。\n"
        "3. 保持 27 core + 38 guard/index，不改变证据等级。\n\n"
        "## 机械检查\n\n"
        + "\n".join(f"- {k}: {'PASS' if v else 'FAIL'}" for k, v in checks.items())
        + "\n\n裁定：V6.5 需对样题 2 做一题最小回归，确认学生会把因果写入表格材料事实格。\n",
        encoding="utf-8",
    )
    print(OUT)
    print(REPORT)


if __name__ == "__main__":
    main()
