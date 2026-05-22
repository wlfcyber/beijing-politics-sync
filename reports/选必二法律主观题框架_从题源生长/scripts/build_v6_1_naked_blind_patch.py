from __future__ import annotations

from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
SRC = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_学生可用工作稿_20260521.md"
OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_1_裸题盲测修补稿_20260521.md"
PATCH_PLAN = ROOT / "09_candidate_frameworks" / "framework_v6_1_naked_blind_patch_plan_20260521.md"


INTRO_PATCH = """## V6.1 裸题盲测后硬修补

V6.1 只改裸题压测暴露出的学生使用问题，不扩证据、不升题、不把低频题包装成核心题。

1. **CC0206 必须写硬词**：本题不是普通“法治环境”，要写“营商环境/法治化营商环境”；但 CC0103 仍禁写“优化营商环境”。
2. **表格题先看列名**：裸题训练看不到真实表格时，只能练方法；真实考试必须按每一列、每一空的功能作答。
3. **source-check 会写也不升核心**：学生能保分，不等于题面和细则已经清洗闭合。
4. **reference-only 只练表达**：普通参考答案题不能支撑框架节点，也不能作为 formal 满分闭环。
5. **低频/边界题用保分容器**：能答，不代表它是高频主干；先保底，再看题目是否要求其他模块。

"""


def build() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = text.replace("主观题满分训练宝典 V6", "主观题满分训练宝典 V6.1")
    text = text.replace("副标题：学生可用工作稿", "副标题：裸题盲测修补稿")
    marker = "## 开卷第一页：你到底要做什么\n\n"
    text = text.replace(marker, INTRO_PATCH + marker, 1)
    text = text.replace(
        "| 表格型 | 完成下表、补充笔记、补全裁判理由 | 先看示例行和空格功能。每格只写一个功能：机制/理由/证据/结果/意义。不能把整篇答案塞进一个格。 |",
        "| 表格型 | 完成下表、补充笔记、补全裁判理由 | 先看表格列名、示例行和空格功能。真实考试必须按每一格问的功能答；每格只写一个功能：机制/理由/证据/结果/意义。不能把整篇答案塞进一个格。 |",
    )
    text = text.replace(
        "| CC0206 不正当竞争 | 营商环境、法治化营商环境 | 不要套 CC0103 的禁词规则 | 本题细则奖励营商环境表达。 |",
        "| CC0206 不正当竞争 | 必须写：营商环境、法治化营商环境 | 不要只写“法治环境”，也不要套 CC0103 的禁词规则 | 本题细则奖励“营商环境”表达，少这四个字容易弱化得分。 |",
    )
    text = text.replace(
        "| CC0103 vs CC0206 | CC0103 写技术秘密、严惩侵权、营造公平市场环境，禁写优化营商环境。 | CC0206 写混淆、虚假宣传、不正当竞争、营商环境。 | 看到科技创新典型案例先查禁词；看到混淆宣传再写营商环境。 |",
        "| CC0103 vs CC0206 | CC0103 写技术秘密、严惩侵权、营造公平市场环境，禁写优化营商环境。 | CC0206 写混淆、虚假宣传、不正当竞争，必须写营商环境/法治化营商环境。 | 看到科技创新典型案例先查禁词；看到混淆宣传再写营商环境。 |",
    )
    text = text.replace(
        "- 改法：先写格子功能，再一格一句；问证据就写证据，问意义才写价值。",
        "- 改法：先写格子功能，再一格一句；问证据就写证据，问意义才写价值。裸题训练如果没呈现真实表格，只能练方法；真实考试必须按列名逐格作答。",
        1,
    )
    text = text.replace(
        "- 适用：只按问法保最低分方向；正式课堂使用前必须回原题和细则。",
        "- 适用：只按问法保最低分方向；正式课堂使用前必须回原题和细则。学生答得好也不自动升入核心。",
    )
    text = text.replace(
        "- 适用：只借表达，不借结论，不支撑核心节点。",
        "- 适用：只借表达，不借结论，不支撑核心节点；教师不得把它说成 formal 满分闭环。",
    )
    text = text.replace(
        "- 怎么用：只借表达，不借结论，不支撑核心节点。",
        "- 怎么用：只借表达，不借结论，不支撑核心节点；教师不得把它说成 formal 满分闭环。",
    )
    text = text.replace(
        "- 怎么用：只按问法保最低分方向；正式课堂使用前必须回原题和细则。",
        "- 怎么用：只按问法保最低分方向；正式课堂使用前必须回原题和细则。学生答得好也不自动升入核心。",
    )
    OUT.write_text(text, encoding="utf-8")

    PATCH_PLAN.write_text(
        """# V6.1 裸题盲测修补计划

输入：

- `10_framework_validation/v6_naked_blind_test_20260521_v2/codex_grading_report_v6_naked_20260521_v2.md`
- `10_framework_validation/v6_naked_blind_test_20260521_v2/agent_student_answers_v6_naked_20260521_v2.md`
- `12_final_baodian/选必二法律主观题满分训练宝典_v6_学生可用工作稿_20260521.md`

修补：

1. CC0206 把“营商环境/法治化营商环境”升为硬词。
2. 表格型答案骨架增加“真实考试按列名逐格作答”。
3. source-check 保分区增加“学生会写也不升核心”。
4. reference-only 练笔区增加“不得说成 formal 满分闭环”。
5. 保持 27 core + 38 non-core，不新增、不升题。

输出：

- `12_final_baodian/选必二法律主观题满分训练宝典_v6_1_裸题盲测修补稿_20260521.md`

裁定：

V6.1 是裸题压测后的学生稿 candidate，不是最终 Word/PDF 封版。下一关应交 GPTPro/Claude 对 V6.1 + 裸题报告做二次攻击复核。
""",
        encoding="utf-8",
    )
    print(OUT)
    print(PATCH_PLAN)


if __name__ == "__main__":
    build()
