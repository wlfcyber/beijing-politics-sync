from __future__ import annotations

import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
V13_4 = BASE / "v13_4_zero_baseline_boundary_decision_patch"
V13_5 = BASE / "v13_5_zero_baseline_high_score_lock_patch"
TEST = BASE / "claude_zero_baseline_iterative_test_20260523_round05"
TRACE = BASE / "v13_1_round05_patched_final" / "traceability" / "TRACEABILITY_MATRIX_v13_1_round05_patched.csv"

SELECTED_IDS = [
    "CC0200_2025_西城_二模_18",
    "CC0157_2025_朝阳_期末_20",
    "CC0084_2025_东城_二模_19",
    "CC0189_2025_石景山_一模_20",
    "CC0305_2026_海淀_一模_18_3",
]

PATCH = """# 04 v13.5 高分档锁分补丁

生成时间：2026-05-23 21:40 +08:00

状态：`v13_5_zero_baseline_high_score_lock_patch_pending_claude_retest`

v13.5 不增加新主轴，不改变已锁定题目的分类。它只解决 v13.4 后零基础学生还能自疑的高分档问题：表格题总入口、方向性结论、治疗功效边界、最小术语清单。

## 一、B1 表格题：总入口是审题定位，不是每次都要写进正式答案

B1 多案例表格题要先在草稿上定“整题总入口”，防止审题散掉；但正式答案以题干和表格列名为准。

硬规则：

1. 原题如果要求“完成下表/参考示例”，正式答案优先按表格逐行写，不必强行在表格外另写一段总入口。
2. 总入口可以作为开头一句，但只能是“本表主要围绕……，各行分别判断……”，不能压过每行的局部入口。
3. 每一行必须自洽：材料事实 -> 法律关系和要件 -> 裁判要点/责任。阅卷主要看行内链条是否命中。
4. 如果一题多案差异很大，正式答案可以不写总入口，只在每行第一句写清局部入口。
5. 总入口选错的风险大于不写总入口。拿不准时，把总入口留在草稿，不写进正式答案。

稳定写法：

- 草稿：先定整题总入口。
- 正式答案：表格内每行写“本案属于 A__，因为……，所以……”。需要总括时只写一句，不展开。

## 二、未成年人打赏：不猜比例，但要写方向性结论

未成年人网络打赏、文身、充值等题，不要求学生猜 80%、60% 这类具体比例，但必须写出方向性结论。

必写三句：

1. 行为效力句：限制民事行为能力人大额消费/打赏明显超出年龄、智力和经济认知范围，未经监护人追认，不发生应有效力或返还有基础。
2. 过错分担句：平台/经营者、监护人、未成年人本人均可能有过错，法院综合各方过错程度，依据公平原则酌定返还或赔偿范围。
3. 结论方向句：一般不支持全额返还或全额免责，而是酌定部分返还/合理分担；谁有较大过错，谁承担更大不利后果。

平台已经采取限制措施时：

- 可以写“该事实影响平台责任大小”。
- 不能直接写“平台完全无过错”。
- 如果未成年人冒充监护人、绕过限制，要写“未成年人本人较大过错/监护人监管不足会影响返还范围”。

## 三、治疗功效/医疗健康宣传：先锁一般欺诈，再看特殊高倍赔偿

看到“治疗疾病、改善并发症、医疗功效、保健功效”时，不要立刻套食品药品高倍赔偿，也不要因不确定而弱化欺诈结论。

三层判断：

1. 必得层：虚假或引人误解的治疗/医疗/保健功效宣传，足以影响消费者选择，构成虚假宣传或欺诈，侵害知情权、选择权和公平交易权。责任先写退还价款、赔偿损失、退一赔三；增加赔偿不足五百元的，按五百元。
2. 特殊层：只有题面明示商品属于食品、药品、保健食品、医疗器械等，且有不符合安全标准、危及健康、造成健康损害，或设问要求适用食品药品安全责任时，才写十倍价款或三倍损失等更高惩罚性赔偿。
3. 边界句：如题面进一步证明属于食品药品安全责任范畴，可依法适用更高惩罚性赔偿。没有这些信号时，不因没写十倍而自扣大分。

一句话：治疗功效虚假宣传一定先保住“退一赔三”；高倍赔偿要有商品身份和安全风险信号。

## 四、常见行的最小命中术语清单

正式答案不必每行都长篇大论，但每类至少命中下面的关键词。

### 1. 未成年人文身/大额消费

最小词：限制民事行为能力；与年龄智力不相适应；未成年人身心健康；公序良俗或未成年人保护；经营者审慎义务；退费/赔偿/返还；过错分担。

### 2. 法人名誉/商誉

最小词：无事实依据；贬损或侮辱；社会评价降低；法人名誉/商誉；停止侵害；消除影响；赔礼道歉或声明；赔偿损失。

### 3. 平台预扣/格式条款

最小词：格式条款；未尽提示说明义务；排除或限制消费者主要权利/加重消费者责任；知情权；公平交易权；条款不发生应有约束力；退还已扣款。

### 4. 合同违约/研发委托

最小词：合同成立并生效；全面履行；诚信履行；约定标准和期限；履行不符合约定或迟延履行；合同目的不能实现或约定成果未达成；返还服务费；违约金；赔偿损失。

### 5. 数据抓取不正当竞争

最小词：合法投入形成数据产品；规避技术措施；伪造身份/变换 IP；不正当获取；商业化使用；损害竞争利益；破坏公平竞争秩序；停止侵害；赔偿损失。

### 6. 混淆类不正当竞争

最小词：有一定影响；名称/图标/标识；近似使用；业务相同或相近；足以造成相关公众混淆；停止使用；赔偿损失。

### 7. 经营场所安全保障

最小词：经营场所或游乐项目；安全保障义务；工作人员执行工作任务；过错；损害；因果关系；题面未显示受害人过错则不主动减责；医疗费/护理费/误工费/残疾赔偿金/精神损害抚慰金。

### 8. 隐私/个人信息

最小词：私密空间；私密活动；私密信息；个人信息；未经同意公开；停止侵害；删除信息；消除影响；赔礼道歉；赔偿损失；严重时精神损害抚慰金。

### 9. 消费者欺诈

最小词：虚假或引人误解宣传；真实全面信息义务；知情权；选择权；公平交易权；错误认识购买；退还价款；退一赔三；不足五百元按五百元。

## 五、B3 诉求题：必写层和加分层分开

B3 问“能否支持诉求/请求”时，按三层写：

1. 结论层：能支持/不能支持/部分支持。
2. 必写层：权利基础、构成要件、材料事实、责任方式。
3. 加分层：精神损害抚慰金、五百元保底、撤销/返还、特殊高倍赔偿、边界句。

加分层何时写：

- 精神损害抚慰金：材料有隐私公开、人格严重受损、明显精神痛苦等信号时写“严重时可主张”。
- 五百元保底：写退一赔三时顺手补“不足五百元按五百元”，这是消费者欺诈稳定加分词。
- 撤销/返还：合同或消费欺诈题可写，但不要替代退一赔三和赔偿损失。
- 特殊高倍赔偿：只在食品药品安全、医疗器械安全或题面明示特殊责任时写为主结论；不确定时只写边界句。

## 六、考场闭眼检查

写完后问五个问题：

1. 表格题每行是否都有“事实 -> 规则 -> 结论”，有没有被总入口带偏？
2. 是否写出了方向性结论，而不是只写“合理分担”？
3. 治疗功效宣传是否先锁住一般消费者欺诈退一赔三？
4. 每行是否至少命中 3-6 个最小术语？
5. 边界句是否放在最后，没有冲掉必得层？
"""

README = """# v13.5 高分档锁分补丁说明

本目录是在真实 Claude Round04 零基础盲测后生成的窄补丁，不覆盖 v13.4。Round04 已经证明双轴框架能让零基础聪明学生稳定进入高分区，但还没有稳定到 95+。

v13.5 只补四件事：

- B1 表格题总入口是审题定位，正式答案以行内链条为主。
- 未成年人打赏不猜比例，但必须写方向性结论。
- 治疗功效虚假宣传先锁一般消费者欺诈，再看食品药品特殊赔偿信号。
- 给常见责任行最小命中术语清单，让学生不用凭感觉取舍加分词。
"""


def read_rows() -> dict[str, dict[str, str]]:
    with TRACE.open(encoding="utf-8-sig", newline="") as f:
        return {r["question_id"]: r for r in csv.DictReader(f)}


def build_framework() -> str:
    base = (V13_4 / "01_双轴法律主观题框架章_v13_4边界决策树补丁.md").read_text(encoding="utf-8")
    return base + "\n\n---\n\n" + PATCH


def payload(rows: dict[str, dict[str, str]], framework: str) -> str:
    parts = [
        "# Claude Zero-Baseline Iterative Live Test Round05：选必二《法律与生活》\n",
        "任务：请你模拟一个“什么都不知道但很聪明的高三学生”。这是新的隔离测试，不参考任何历史聊天、旧答案或外部资料。你只知道下面的 v13.5 框架和题面压缩信息。\n",
        "硬规则：\n",
        "1. 你是正在考试的学生，不是老师或阅卷人。\n",
        "2. 只能使用下面的框架和题目材料，不调用外部资料，不补充题目没有给出的事实。\n",
        "3. 我不给你标准答案、评分锚点、材料触发链、答案骨架、学生预警。\n",
        "4. 每道题按固定格式回答：A轴主入口判断；B轴设问动作判断；材料信号；现场答案；自我估分和最可能丢分点。\n",
        "5. 特别压力测试：检查 v13.5 是否解决 B1 总入口、未成年人返还方向、治疗功效边界、最小术语清单四个问题。\n",
        "6. 最后总评：v13.5 是否已经足够让零基础但聪明学生稳定高分？若仍不足，缺口在哪里？\n",
        "测试类型：targeted stress retest after v13.5 high-score lock patch\n",
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
        "# Local Answer Key for Claude Zero-Baseline Iterative Test Round05\n\n",
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
    V13_5.mkdir(parents=True, exist_ok=True)
    (TEST / "web_payloads").mkdir(parents=True, exist_ok=True)
    (TEST / "model_outputs").mkdir(parents=True, exist_ok=True)
    (TEST / "codex_adjudication").mkdir(parents=True, exist_ok=True)

    rows = read_rows()
    framework = build_framework()
    (V13_5 / "00_READ_ME_FIRST.md").write_text(README, encoding="utf-8", newline="\n")
    (V13_5 / "01_双轴法律主观题框架章_v13_5高分档锁分补丁.md").write_text(
        framework, encoding="utf-8", newline="\n"
    )
    (V13_5 / "02_ROUND04_TO_V13_5_CODEX_ADJUDICATION.md").write_text(
        """# Round04 To v13.5 Codex Adjudication

Round04 real Claude retest reached high-score transfer but did not close the perfect-framework gate.

Accepted patches:

- B1 total-entry as draft orientation, not mandatory formal-answer content.
- Directional conclusion terms for minor reward/refund cases.
- Treatment/medical-effect fraud boundary with general consumer fraud locked first.
- Minimal term checklists for common B1/B3 lines.

Rejected changes:

- Do not replace the A/B framework.
- Do not add new A-axis entrances.
- Do not promote open-container rows.
- Do not treat Claude self-eval as source evidence without hidden-key Codex adjudication.
""",
        encoding="utf-8",
        newline="\n",
    )
    p = payload(rows, framework)
    (TEST / "web_payloads" / "CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND05_PAYLOAD.md").write_text(
        p, encoding="utf-8", newline="\n"
    )
    (TEST / "codex_adjudication" / "LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md").write_text(
        key(rows), encoding="utf-8", newline="\n"
    )
    (TEST / "ROUND_PROGRESS.md").write_text(
        f"""# Claude Zero-Baseline Iterative Test Round05 Progress

Status: `v13_5_payload_prepared_pending_real_claude_web_capture`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.5 high-score lock patch
- Selected questions: {", ".join(SELECTED_IDS)}
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND05_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 45/50; Claude no longer requests a new framework-level patch for the four Round04 gaps.
""",
        encoding="utf-8",
        newline="\n",
    )
    print(V13_5)
    print(TEST)
    print("payload_chars", len(p))


if __name__ == "__main__":
    main()
