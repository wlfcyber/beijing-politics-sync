from __future__ import annotations

import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
V13_2 = BASE / "v13_2_zero_baseline_toolbox_patch"
V13_3 = BASE / "v13_3_zero_baseline_responsibility_terms_patch"
TEST = BASE / "claude_zero_baseline_iterative_test_20260523_round03"
TRACE = BASE / "v13_1_round05_patched_final" / "traceability" / "TRACEABILITY_MATRIX_v13_1_round05_patched.csv"

SELECTED_IDS = [
    "CC0200_2025_西城_二模_18",
    "CC0157_2025_朝阳_期末_20",
    "CC0084_2025_东城_二模_19",
    "CC0189_2025_石景山_一模_20",
    "CC0305_2026_海淀_一模_18_3",
]


PATCH = """# 02 v13.3 责任方式与考场术语补丁

生成时间：2026-05-23 21:35 +08:00

状态：`v13_3_zero_baseline_responsibility_terms_patch_pending_claude_retest`

v13.3 继续保留 v13.2 的 A/B 双轴和入口工具箱，只补三件事：责任方式触发表、考场标配术语、B1 多案例总入口规则。

## 一、责任方式触发表

### 1. 消费者欺诈

事实信号：虚假宣传、夸大功效、隐瞒重要事实、诱导消费、消费者因错误认识购买。

写法：

- 先写经营者侵害消费者知情权、选择权和公平交易权，构成欺诈。
- 一般消费者欺诈：退还价款或赔偿损失，并按消费者要求增加赔偿，通常写“退一赔三；增加赔偿不足五百元的，按五百元”。
- 食品药品安全特殊规则：只有题面明示食品、药品、安全不符合标准或造成健康风险时，才考虑“十倍价款或三倍损失”等特殊惩罚性赔偿。普通保健功效虚假宣传若题面不明示食品药品安全，不要贸然套十倍。

### 2. 平台预扣、格式条款、提示不清

事实信号：预设条款、自动扣款、预扣房款、消费者不知情、未实际接受服务、经营者未提示说明。

写法：

- 先写格式条款提供者应履行提示说明义务，不得排除消费者主要权利、加重消费者责任。
- 再写该条款对消费者不发生应有约束力，经营者不能据此免责或强扣款。
- 责任方式优先写退还已扣款、返还价款、赔偿损失；只有题面另有欺诈事实，才写退一赔三。

### 3. 未成年人打赏、文身等限制行为能力

事实信号：未成年人年龄、金额或行为明显超出认知范围、监护人不知情/不追认、经营者未审查或平台审核不足。

写法：

- A1 脊柱写限制民事行为能力、行为与年龄智力不相适应、未经追认不发生效力、已取得财产原则上返还。
- A9/A2 场景写经营者或平台对未成年人负有更高审慎义务。
- 责任方式写返还、退费、赔偿损失；同时写平台/经营者、监护人、未成年人本人过错分担。不要写消费者欺诈惩罚性赔偿，除非题面另有虚假宣传。

### 4. 合同违约、返还服务费和违约金

事实信号：约定标准和期限、履行不达标、超期、拒不交付、法院判返还服务费并支付违约金。

写法：

- 先写合同成立生效，当事人应全面、诚信履行。
- 再写履行不符合约定或迟延履行构成违约。
- 若题面给出“返还服务费”，可写违约导致合同目的不能实现或约定成果未达成，返还已收服务费并支付违约金、赔偿损失。不要只写“保护创新”。

### 5. 人格权、隐私、名誉、商誉

事实信号：公开监控、聊天记录、私密活动；无事实依据贬损、侮辱、诽谤，造成社会评价降低。

写法：

- 隐私/个人信息：停止侵害、删除信息、消除影响、赔礼道歉、赔偿损失；严重精神损害可写精神损害抚慰金。
- 名誉/商誉：停止侵害、消除影响、赔礼道歉或发布声明、赔偿损失。法人商誉可归 A2 人格权益链。

### 6. 知识产权和不正当竞争

事实信号：商业秘密、技术秘密、数据抓取、混淆、商业诋毁、虚假宣传。

写法：

- 责任方式：停止侵害、消除影响、赔偿损失；严重故意侵权可写惩罚性赔偿或提高违法成本。
- 数据抓取不要写“混淆”，除非题面有名称、图标、来源误认。数据抓取写“规避技术措施、不正当获取、商业化使用、损害数据产品权益和公平竞争秩序”。
- 混淆类写“使用与他人有一定影响的名称、标识等近似标识，足以造成相关公众混淆”。

### 7. 经营场所安全保障和侵权赔偿

事实信号：游乐项目、旅游服务、公共场所、工作人员操作、摔伤住院、伤残。

写法：

- 先写经营者负有安全保障义务，工作人员执行工作任务造成损害的，由经营者或用人单位承担相应责任。
- 再写过错、损害、因果关系。
- 责任方式：医疗费、护理费、误工费、交通费、住院伙食补助费、残疾赔偿金、精神损害抚慰金等。
- 若题面有受害人违规、冒险、未尽注意义务，写过错分担；若题面只有工作人员过度操作，经营者承担主要责任甚至全部责任，不要过度保守。

## 二、考场标配术语清单

- A2 隐私：私密空间、私密活动、私密信息、个人信息、停止侵害、删除、消除影响、赔礼道歉、精神损害抚慰金。
- A2 名誉/商誉：无事实依据、社会评价降低、法人名誉/商誉、消除影响、赔礼道歉、赔偿损失。
- A4 合同：合同成立并生效、全面履行、诚信履行、履行不符合约定、迟延履行、合同目的不能实现、返还服务费、违约金。
- A5 数据抓取：合法投入形成数据产品、规避技术措施、伪造身份或变换 IP、不正当获取、商业化使用、损害竞争利益、公平竞争秩序。
- A5 混淆：有一定影响的名称/包装/装潢等标识、近似使用、足以造成相关公众混淆、停止使用、赔偿损失。
- A6 安全保障：经营场所或公共场所安全保障义务、工作人员执行工作任务、过错、因果关系、人身损害赔偿、自身过错减责。
- A9 消费者：知情权、选择权、公平交易权、安全保障权、真实全面信息、虚假或引人误解宣传、退一赔三、格式条款提示说明义务。

## 三、B1 多案例题总入口规则

B1 表格题经常一题多案。作答时要分两层写：

1. 先声明整题总入口：根据题卡最核心法益、第一格主干或多数案例主干，给出一个总入口。
2. 再在表格里写每一行的局部入口和副入口。

常见规则：

- 多案例中出现未成年人身心利益、法人名誉/商誉、隐私/个人信息等人格权益，并且另有消费者或合同副链时，整题可先定 A2，人格权益是总入口，A9/A4 进表格行内副链。
- 多案例中第一格是合同违约，第二格是不正当竞争，且题目围绕研发委托和创新交易秩序，整题可先定 A4，第二格 A5 作为行内入口。
- 多案例中第一格或主干是数据抓取、不正当竞争，另有旅游安全保障案例，整题可先定 A5，旅游行内写 A6/A9。
- 如果原题表格已经给了列名，沿用原列名；压缩盲测看不到列名时，默认三列不算结构错误。

一句话：整题有一个总入口，表格每行可以有局部入口。不要只写局部入口而忘了总入口。
"""


README = """# v13.3 零基础责任方式与术语补丁说明

本目录是在 v13.2 真实 Claude Round02 盲测后生成的窄补丁，不覆盖 v13.1/v13.2。

v13.2 已解决 A/B 分诊和表格形状问题，但 Round02 仍暴露：

- 责任方式颗粒度不够，如退一赔三、精神损害抚慰金、违约金、解除/返还、过错分担。
- 考场标准术语不够稳，如“有一定影响”“规避技术措施”“安全保障义务”。
- B1 多案例题缺少“整题总入口 + 每行局部入口”的写法。

v13.3 只补这三点，并继续用真实 Claude 新聊天进行零基础盲测。
"""


def read_rows() -> dict[str, dict[str, str]]:
    with TRACE.open(encoding="utf-8-sig", newline="") as f:
        return {r["question_id"]: r for r in csv.DictReader(f)}


def build_framework() -> str:
    base = (V13_2 / "01_双轴法律主观题框架章_v13_2零基础工具箱补丁.md").read_text(encoding="utf-8")
    return base + "\n\n---\n\n" + PATCH


def payload(rows: dict[str, dict[str, str]], framework: str) -> str:
    parts = [
        "# Claude Zero-Baseline Iterative Live Test Round03：选必二《法律与生活》\n",
        "任务：请你模拟一个“什么都不知道但很聪明的高三学生”。这是新的隔离测试，不参考任何历史聊天、旧答案或外部资料。你只知道下面的 v13.3 框架和题面压缩信息。\n",
        "硬规则：\n",
        "1. 你是正在考试的学生，不是老师或阅卷人。\n",
        "2. 只能使用下面的框架和题目材料，不调用外部资料，不补充题目没有给出的事实。\n",
        "3. 我不给你标准答案、评分锚点、材料触发链、答案骨架、学生预警。\n",
        "4. 每道题按固定格式回答：A轴主入口判断；B轴设问动作判断；材料信号；现场答案；自我估分和最可能丢分点。\n",
        "5. 最后总评：v13.3 是否已经让零基础但聪明学生稳定达到高分？若仍不足，缺口在哪里？\n",
        "测试类型：targeted stress retest after v13.3 responsibility/terms patch\n",
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
        "# Local Answer Key for Claude Zero-Baseline Iterative Test Round03\n\n",
        "This file is NOT sent to Claude. It is used by Codex to compare Claude live answers against locked v13.1/v13.3 cards.\n",
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
    V13_3.mkdir(parents=True, exist_ok=True)
    (TEST / "web_payloads").mkdir(parents=True, exist_ok=True)
    (TEST / "model_outputs").mkdir(parents=True, exist_ok=True)
    (TEST / "codex_adjudication").mkdir(parents=True, exist_ok=True)

    rows = read_rows()
    framework = build_framework()
    (V13_3 / "00_READ_ME_FIRST.md").write_text(README, encoding="utf-8", newline="\n")
    (V13_3 / "01_双轴法律主观题框架章_v13_3责任方式术语补丁.md").write_text(
        framework, encoding="utf-8", newline="\n"
    )
    (V13_3 / "02_ROUND02_TO_V13_3_CODEX_ADJUDICATION.md").write_text(
        """# Round02 To v13.3 Codex Adjudication

Round02 real Claude retest improved the framework but did not close the zero-baseline high-score gate.

Accepted patches:

- Add responsibility trigger table.
- Add standard exam-term list.
- Add B1 multi-case total-entry plus row-entry rule.

Rejected changes:

- Do not replace the A/B framework.
- Do not promote open-container rows.
- Do not overwrite v13.1 rendered DOCX/PDF in this narrow patch.
""",
        encoding="utf-8",
        newline="\n",
    )
    p = payload(rows, framework)
    (TEST / "web_payloads" / "CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND03_PAYLOAD.md").write_text(
        p, encoding="utf-8", newline="\n"
    )
    (TEST / "codex_adjudication" / "LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md").write_text(
        key(rows), encoding="utf-8", newline="\n"
    )
    (TEST / "ROUND_PROGRESS.md").write_text(
        f"""# Claude Zero-Baseline Iterative Test Round03 Progress

Status: `v13_3_payload_prepared_pending_real_claude_web_capture`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.3 responsibility/terms patch
- Selected questions: {", ".join(SELECTED_IDS)}
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND03_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; rough total >= 43/50; no single item below 8/10 in Claude self-eval or below 7.5 in Codex hidden-key evaluation.
""",
        encoding="utf-8",
        newline="\n",
    )
    print(V13_3)
    print(TEST)
    print("payload_chars", len(p))


if __name__ == "__main__":
    main()
