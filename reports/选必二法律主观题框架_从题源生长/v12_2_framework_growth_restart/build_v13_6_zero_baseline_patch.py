from __future__ import annotations

import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
V13_5 = BASE / "v13_5_zero_baseline_high_score_lock_patch"
V13_6 = BASE / "v13_6_zero_baseline_95plus_precision_patch"
TEST = BASE / "claude_zero_baseline_iterative_test_20260523_round06"
TRACE = BASE / "v13_1_round05_patched_final" / "traceability" / "TRACEABILITY_MATRIX_v13_1_round05_patched.csv"

SELECTED_IDS = [
    "CC0200_2025_西城_二模_18",
    "CC0157_2025_朝阳_期末_20",
    "CC0084_2025_东城_二模_19",
    "CC0189_2025_石景山_一模_20",
    "CC0305_2026_海淀_一模_18_3",
]

PATCH = """# 05 v13.6 95+ 行内精度补丁

生成时间：2026-05-23 22:05 +08:00

状态：`v13_6_zero_baseline_95plus_precision_patch_pending_claude_retest`

v13.6 不改 A/B 双轴，不新增主入口。它只处理 v13.5 后仍可能影响 95+ 的三件事：表格列名、合同责任并列、双链题字数和分值配比。

## 一、B1 表格列名：真实考场先沿用原列名

表格题的第一规则永远是：原表有什么列名，就用什么列名。不要为了框架默认三列而改掉原题列名。

处理顺序：

1. 列名可见：逐字沿用原列名，只在列内填入“事实 -> 规则 -> 结论”。
2. 列名部分可见：保留可见列名，缺失部分按“事实/法律关系和要件/裁判要点或责任”补足。
3. 列名完全不可见或压缩盲测：才用默认三列“材料事实 | 法律关系和要件 | 裁判要点/责任”。
4. 如果题干有“参考示例”，先观察示例的表达形状：示例如果是裁判理由句，就不要写成纯概念表；示例如果是短语填空，就不要写成长段作文。

常见列名推断：

- “分析事实，印证法理”：事实信号 | 法律规则/法理 | 裁判要点。
- “诉求能否支持”：诉求/请求 | 法律分析 | 支持或不支持及责任。
- “违反法律规定/法律责任”：行为或事实 | 违反的规则 | 应承担的责任。
- “案件/法理/启示”：案件事实 | 法律关系和规则 | 裁判结果或法治意义。

考场稳妥句：如原表列名与本框架默认三列不同，以原表列名为准；本框架只帮助你在每列里组织要点。

## 二、合同违约：返还、违约金、损害赔偿不是乱堆

高中政治主观题不要求展开复杂民法计算，但责任方式要和题面事实、诉求或判决一致。

判断顺序：

1. 先写合同成立并生效，当事人应全面履行、诚信履行。
2. 再写违约事实：未按约定标准交付、迟延履行、拒不履行、合同目的不能实现或约定成果未达成。
3. 最后按题面写责任方式：
   - 题面给“返还服务费/返还价款”：写因合同目的不能实现或约定成果未达成，返还已收款项。
   - 题面给“违约金”：写按约承担违约金责任；不需要计算数额。
   - 题面给“赔偿损失”：写赔偿因违约造成的损失。
   - 题面没有给损失事实时，不把“赔偿损失”写成主结论，可写“依法承担违约责任，如支付违约金、赔偿损失等”。

并列规则：

- “返还服务费 + 违约金”可以并列：前者处理未达成合同目的后的款项返还，后者处理违约责任。
- “违约金 + 损害赔偿”不要无条件并列成重复赔偿。稳妥写法是：按约支付违约金；如违约金不足以弥补损失或题面另有损失事实，可依法赔偿相应损失。
- 如果题面已经说“法院判返还服务费并支付违约金”，答题只需解释为什么这样判，不必质疑司法计算。

## 三、双链题：按设问顺序和分值配比写字数

双链题不是平均作文。字数和要点按三个信号分配：

1. 有分值：按分值配比。6 分链写得比 4 分链更细；总分高的链多写事实和责任方式。
2. 无分值但设问说“分别判断”：严格按设问顺序，每链至少四件套：结论 -> 权利基础/规则 -> 材料事实 -> 责任方式。
3. 无分值且两链争议程度不同：更有争议、责任更重、材料事实更多的一链多写；另一链保留必写四件套。

隐私 + 消费者欺诈常见配比：

- 隐私链必写：私密空间、私密活动、私密信息/个人信息、未经同意公开、停止侵害/删除/消除影响/赔礼道歉/赔偿损失。
- 欺诈链必写：虚假或引人误解宣传、知情权/选择权/公平交易权、错误认识购买、退还价款、退一赔三、不足五百元按五百元。
- 如果题干重点在“消费者诉求能否支持”，消费欺诈链通常责任金额更明确，可比隐私链稍多写；但不能省掉隐私链构成要件。

## 四、95+ 最后检查

交卷前再查三件事：

1. 表格是否沿用原列名；如果没看到列名，是否说明按默认三列组织。
2. 合同责任是否按题面诉求/判决写，没有把违约金和赔偿损失机械堆叠。
3. 双链题是否按分值或设问顺序分配篇幅，每条链都有结论、规则、事实、责任。
"""

README = """# v13.6 95+ 行内精度补丁说明

本目录是在真实 Claude Round05 零基础盲测后生成的窄补丁，不覆盖 v13.5。Round05 已经证明 v13.5 能稳定解决表格总入口、未成年人方向性结论、治疗功效边界、最小术语清单四个问题。

v13.6 只补 95+ 行内精度：

- 表格题真实考场必须沿用原列名；看不到列名才用默认三列。
- 合同违约责任按题面诉求或判决写，返还、违约金、损害赔偿不能机械堆叠。
- 双链题按分值、设问顺序和争议强度分配字数。
"""


def read_rows() -> dict[str, dict[str, str]]:
    with TRACE.open(encoding="utf-8-sig", newline="") as f:
        return {r["question_id"]: r for r in csv.DictReader(f)}


def build_framework() -> str:
    base = (V13_5 / "01_双轴法律主观题框架章_v13_5高分档锁分补丁.md").read_text(encoding="utf-8")
    return base + "\n\n---\n\n" + PATCH


def payload(rows: dict[str, dict[str, str]], framework: str) -> str:
    parts = [
        "# Claude Zero-Baseline Iterative Live Test Round06：选必二《法律与生活》\n",
        "任务：请你模拟一个“什么都不知道但很聪明的高三学生”。这是新的隔离测试，不参考任何历史聊天、旧答案或外部资料。你只知道下面的 v13.6 框架和题面压缩信息。\n",
        "硬规则：\n",
        "1. 你是正在考试的学生，不是老师或阅卷人。\n",
        "2. 只能使用下面的框架和题目材料，不调用外部资料，不补充题目没有给出的事实。\n",
        "3. 我不给你标准答案、评分锚点、材料触发链、答案骨架、学生预警。\n",
        "4. 每道题按固定格式回答：A轴主入口判断；B轴设问动作判断；材料信号；现场答案；自我估分和最可能丢分点。\n",
        "5. 特别压力测试：检查 v13.6 是否解决表格列名、合同责任并列、双链题分值/字数配比三个问题。\n",
        "6. 最后总评：v13.6 是否已经足够作为零基础聪明学生稳定高分框架？若仍需新框架级补丁，请明确说明。\n",
        "测试类型：targeted stress retest after v13.6 95plus precision patch\n",
        f"测试题号：{', '.join(SELECTED_IDS)}\n",
        "\n---\n\n## A. 你先学习的框架\n\n",
        README,
        "\n\n",
        framework,
        "\n\n---\n\n## B. 盲测题\n\n以下只提供题面压缩信息和设问，不提供答案骨架或评分锚点。\n",
    ]
    for i, qid in enumerate(SELECTED_IDS, 1):
        r = rows[qid]
        parts.append(
            f"""
### 题{i}: {qid}

- 区年卷题：{r["year"]}年 {r["district"]} {r["exam_stage"]} 第{r["question_no"]}题
- 设问：{r["prompt_action"]}
- 材料/题面压缩：{r["material_core"]}
"""
        )
    return "".join(parts)


def key(rows: dict[str, dict[str, str]]) -> str:
    lines = [
        "# Local Answer Key for Claude Zero-Baseline Iterative Test Round06\n\n",
        "This file is NOT sent to Claude. It is used by Codex to compare Claude live answers against locked cards.\n",
    ]
    for i, qid in enumerate(SELECTED_IDS, 1):
        r = rows[qid]
        lines.append(
            f"""
## 题{i}: {qid}

- expected_a_axis: {r["a_axis_primary"]}
- expected_b_axis: {r["b_axis"]}
- secondary_axis: {r["a_axis_secondary_status"]}
- adjudication_note: {r["a_axis_adjudication_note"]}
- prompt_action: {r["prompt_action"]}
- material_core: {r["material_core"]}
- material_trigger: {r["material_trigger"]}
- rubric_scoring_anchor: {r["rubric_scoring_anchor"]}
- proposition_path: {r["proposition_path"]}
- answer_skeleton: {r["answer_skeleton"]}
- student_warning: {r["student_warning"]}
- guardrail: {r["guardrail"]}
"""
        )
    return "\n".join(lines)


def main() -> None:
    V13_6.mkdir(parents=True, exist_ok=True)
    (TEST / "web_payloads").mkdir(parents=True, exist_ok=True)
    (TEST / "model_outputs").mkdir(parents=True, exist_ok=True)
    (TEST / "codex_adjudication").mkdir(parents=True, exist_ok=True)

    rows = read_rows()
    framework = build_framework()
    (V13_6 / "00_READ_ME_FIRST.md").write_text(README, encoding="utf-8", newline="\n")
    (V13_6 / "01_双轴法律主观题框架章_v13_6_95plus行内精度补丁.md").write_text(
        framework, encoding="utf-8", newline="\n"
    )
    (V13_6 / "02_ROUND05_TO_V13_6_CODEX_ADJUDICATION.md").write_text(
        """# Round05 To v13.6 Codex Adjudication

Round05 real Claude retest passed the v13.5 high-score lock gate but still identified three 95+ line-precision gaps.

Accepted patches:

- Table-column visibility rule and column-name inference fallback.
- Contract liability non-duplication rule for refund, liquidated damages, and damages.
- Dual-chain answer length allocation by score, prompt order, and dispute weight.

Rejected changes:

- Do not replace the A/B framework.
- Do not add new A-axis entrances.
- Do not promote open-container rows.
- Do not require exact civil-law calculations beyond the high-school rubric level.
""",
        encoding="utf-8",
        newline="\n",
    )
    p = payload(rows, framework)
    (TEST / "web_payloads" / "CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND06_PAYLOAD.md").write_text(
        p, encoding="utf-8", newline="\n"
    )
    (TEST / "codex_adjudication" / "LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md").write_text(
        key(rows), encoding="utf-8", newline="\n"
    )
    (TEST / "ROUND_PROGRESS.md").write_text(
        f"""# Claude Zero-Baseline Iterative Test Round06 Progress

Status: `v13_6_payload_prepared_pending_real_claude_web_capture`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.6 95plus precision patch
- Selected questions: {", ".join(SELECTED_IDS)}
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND06_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 46/50; Claude no longer requests a new framework-level patch for Round04/Round05 gaps.
""",
        encoding="utf-8",
        newline="\n",
    )
    print(V13_6)
    print(TEST)
    print("payload_chars", len(p))


if __name__ == "__main__":
    main()
