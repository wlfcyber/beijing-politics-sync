from __future__ import annotations

import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
V13_6 = BASE / "v13_6_zero_baseline_95plus_precision_patch"
V13_7 = BASE / "v13_7_zero_baseline_b1_b3_final_precision_patch"
TEST = BASE / "claude_zero_baseline_iterative_test_20260523_round07"
TRACE = BASE / "v13_1_round05_patched_final" / "traceability" / "TRACEABILITY_MATRIX_v13_1_round05_patched.csv"

SELECTED_IDS = [
    "CC0200_2025_西城_二模_18",
    "CC0157_2025_朝阳_期末_20",
    "CC0084_2025_东城_二模_19",
    "CC0189_2025_石景山_一模_20",
    "CC0305_2026_海淀_一模_18_3",
]

PATCH = """# 06 v13.7 B1/B3 最终精度补丁

生成时间：2026-05-23 22:35 +08:00

状态：`v13_7_zero_baseline_b1_b3_final_precision_patch_pending_claude_retest`

v13.7 不改 A/B 双轴，不新增主入口。它只补 v13.6 后剩下的三处 95+ 精度：表格口令映射、双链字数配比量化、启示/价值列触发规则。

## 一、B1 表格口令映射表

原表列名优先；若列名只部分可见，就用题干口令和示例形状推断。

### 1. 题干说“了解案件，分析事实，印证法理，参考示例”

默认列形：案件事实 | 法理印证 | 裁判要点/启示。

- 案件事实：只放材料事实，不放抽象价值。
- 法理印证：写法律关系、构成要件、关键词。
- 裁判要点/启示：先写裁判责任；若列名或示例含“启示/意义/作用”，再加一句价值收束。

### 2. 题干说“阅读材料，完成下表”

默认列形：材料事实 | 法律关系和要件 | 裁判要点/责任。

- 不额外加表外总入口。
- 每行必须自洽，不让第一行主入口压过其他行。

### 3. 题干说“参考示例，完成下表”

先模仿示例长短：

- 示例是短语：每格写短语，少写长段。
- 示例是完整句：每格写“事实 -> 规则 -> 结论”的完整句。
- 示例最后一列如果是“意义/启示”，该列必须有价值收束；如果只是“裁判要点/责任”，不要强塞价值。

### 4. 题干说“诉求/请求能否支持”

列形或段落形：诉求 | 法律分析 | 支持/不支持及责任。

- 每个诉求先给结论。
- 再写权利基础、构成要件、材料事实、责任方式。

## 二、启示/价值列触发规则

只有出现下列口令，表格最后一格才升级为“裁判要点 + 价值收束”：

- 启示、意义、作用、价值、保护了什么、推动了什么、说明了什么法治道理。

价值收束固定句式：

法律规则保护____，约束____，维护____秩序/促进____发展。

常见填法：

- 数据抓取：保护合法投入形成的数据产品和创新成果，约束不正当抓取、商业化利用行为，维护公平竞争秩序。
- 旅游安全：保护消费者人身安全，约束经营者安全保障义务，促进文旅市场安全有序。
- 未成年人文身：保护未成年人身心健康，约束涉未成年人经营行为，维护公序良俗。
- 格式条款扣款：保护消费者知情权和公平交易权，约束平台格式条款，维护公平消费秩序。
- 研发委托合同：保护创新交易和合同预期，约束违约行为，维护诚信交易秩序。
- 混淆竞争：保护有一定影响的商业标识，约束搭便车行为，维护公平竞争秩序。

如果列名没有启示/意义/价值，价值句可放最后一句，不要喧宾夺主。

## 三、双链题字数配比量化

无分值时，按下面的量化规则：

1. 明显主诉求链 + 副链：6:4。主链多写一个责任方式或一个边界句。
2. 设问“分别判断 A 与 B”且无主副：5:5。两链各有结论、规则、事实、责任。
3. 一链事实明显更多或责任金额更明确：6:4。事实更多/金额更明确的一链多写。
4. 一链只是副轴脊柱：7:3。副轴只写得分关键词，不展开成长段。

隐私 + 消费者欺诈：

- 如果题干重心是“消费者诉求能否支持”，且欺诈责任涉及退一赔三，写成隐私 4、欺诈 6。
- 隐私链写够：私密空间/活动/信息、未经同意公开、停止/删除/消除影响/道歉/赔偿。
- 欺诈链多写：虚假宣传、错误认识购买、退还价款、退一赔三、五百元保底、食品药品边界句。

## 四、最终停止条件

如果真实 Claude 在下一轮仍只提出以下问题，不再进入新框架补丁，只记入宝典写作注意：

- 原题列名不可见导致的压缩测试不确定。
- 具体分值未知导致的字数比例微调。
- 个别责任金额、比例或法条编号不确定。

这些不是框架缺陷，而是原题信息缺失或考试现场信息问题。框架已经给出处理规则即可。
"""

README = """# v13.7 B1/B3 最终精度补丁说明

本目录是在真实 Claude Round06 零基础盲测后生成的窄补丁，不覆盖 v13.6。

v13.7 只补三件事：

- B1 表格题按题干口令和示例形状推断列名。
- 表格最后一列只有出现“启示/意义/价值”等口令时才升级价值收束。
- 双链题无分值时用 6:4、5:5、7:3 等可执行配比。

若下一轮只剩原题列名不可见、分值未知、责任比例未知等问题，视为原题信息缺失，不再升级为框架缺陷。
"""


def read_rows() -> dict[str, dict[str, str]]:
    with TRACE.open(encoding="utf-8-sig", newline="") as f:
        return {r["question_id"]: r for r in csv.DictReader(f)}


def build_framework() -> str:
    base = (V13_6 / "01_双轴法律主观题框架章_v13_6_95plus行内精度补丁.md").read_text(encoding="utf-8")
    return base + "\n\n---\n\n" + PATCH


def payload(rows: dict[str, dict[str, str]], framework: str) -> str:
    parts = [
        "# Claude Zero-Baseline Iterative Live Test Round07：选必二《法律与生活》\n",
        "任务：请你模拟一个“什么都不知道但很聪明的高三学生”。这是新的隔离测试，不参考任何历史聊天、旧答案或外部资料。你只知道下面的 v13.7 框架和题面压缩信息。\n",
        "硬规则：\n",
        "1. 你是正在考试的学生，不是老师或阅卷人。\n",
        "2. 只能使用下面的框架和题目材料，不调用外部资料，不补充题目没有给出的事实。\n",
        "3. 我不给你标准答案、评分锚点、材料触发链、答案骨架、学生预警。\n",
        "4. 每道题按固定格式回答：A轴主入口判断；B轴设问动作判断；材料信号；现场答案；自我估分和最可能丢分点。\n",
        "5. 特别压力测试：检查 v13.7 是否解决表格口令映射、启示/价值列触发、双链字数配比三个问题。\n",
        "6. 最后总评：若只剩原题列名不可见、分值未知、责任比例未知等问题，请不要再要求新框架补丁；请判断是否已经可进入最终宝典写作。\n",
        "测试类型：targeted stress retest after v13.7 final precision patch\n",
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
        "# Local Answer Key for Claude Zero-Baseline Iterative Test Round07\n\n",
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
    V13_7.mkdir(parents=True, exist_ok=True)
    (TEST / "web_payloads").mkdir(parents=True, exist_ok=True)
    (TEST / "model_outputs").mkdir(parents=True, exist_ok=True)
    (TEST / "codex_adjudication").mkdir(parents=True, exist_ok=True)

    rows = read_rows()
    framework = build_framework()
    (V13_7 / "00_READ_ME_FIRST.md").write_text(README, encoding="utf-8", newline="\n")
    (V13_7 / "01_双轴法律主观题框架章_v13_7_B1B3最终精度补丁.md").write_text(
        framework, encoding="utf-8", newline="\n"
    )
    (V13_7 / "02_ROUND06_TO_V13_7_CODEX_ADJUDICATION.md").write_text(
        """# Round06 To v13.7 Codex Adjudication

Round06 real Claude retest identified final B1/B3 precision gaps.

Accepted patches:

- B1 prompt-to-column mapping.
- Value/meaning column trigger rule.
- Quantified dual-chain length allocation.
- Final stop condition distinguishing framework defects from missing original exam information.

Rejected changes:

- Do not replace the A/B framework.
- Do not add new A-axis entrances.
- Do not promote open-container rows.
- Do not continue infinite patching for unknown original column names, point values, exact ratios, or law article numbers.
""",
        encoding="utf-8",
        newline="\n",
    )
    p = payload(rows, framework)
    (TEST / "web_payloads" / "CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND07_PAYLOAD.md").write_text(
        p, encoding="utf-8", newline="\n"
    )
    (TEST / "codex_adjudication" / "LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md").write_text(
        key(rows), encoding="utf-8", newline="\n"
    )
    (TEST / "ROUND_PROGRESS.md").write_text(
        f"""# Claude Zero-Baseline Iterative Test Round07 Progress

Status: `v13_7_payload_prepared_pending_real_claude_web_capture`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.7 final precision patch
- Selected questions: {", ".join(SELECTED_IDS)}
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND07_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 46/50; no new framework-level patch requested beyond missing original exam information.
""",
        encoding="utf-8",
        newline="\n",
    )
    print(V13_7)
    print(TEST)
    print("payload_chars", len(p))


if __name__ == "__main__":
    main()
