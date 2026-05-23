from __future__ import annotations

import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
V13_3 = BASE / "v13_3_zero_baseline_responsibility_terms_patch"
V13_4 = BASE / "v13_4_zero_baseline_boundary_decision_patch"
TEST = BASE / "claude_zero_baseline_iterative_test_20260523_round04"
TRACE = BASE / "v13_1_round05_patched_final" / "traceability" / "TRACEABILITY_MATRIX_v13_1_round05_patched.csv"

SELECTED_IDS = [
    "CC0200_2025_西城_二模_18",
    "CC0157_2025_朝阳_期末_20",
    "CC0084_2025_东城_二模_19",
    "CC0189_2025_石景山_一模_20",
    "CC0305_2026_海淀_一模_18_3",
]

PATCH = """# 03 v13.4 边界决策树补丁

生成时间：2026-05-23 21:15 +08:00

状态：`v13_4_zero_baseline_boundary_decision_patch_pending_claude_retest`

v13.4 不增加新主轴，只解决 v13.3 后仍让零基础学生自疑的边界问题。

## 一、过错分担：不需要猜具体比例

高考主观题一般不要求写 80%、60% 这类具体比例，除非题面直接给出比例或判决结果。得分关键词是：

- 综合各方过错程度。
- 依据公平原则。
- 酌定返还或赔偿范围。
- 既保护未成年人/消费者，也规范平台经营者和监护责任。

未成年人打赏固定写法：

- 先写大额打赏未经监护人追认，返还有基础。
- 再写平台/主播、监护人、未成年人本人均可能有过错。
- 最后写法院综合过错程度合理分担，不必给出具体返还比例。
- 不要因为不知道比例而自扣大分。

## 二、安全保障责任：没有受害人过错时，不主动减责

游乐项目、旅游服务、公共场所伤害题：

- 如果题面只给“工作人员过度操作/设施管理不当/未尽安全保障义务”，且没有给游客违规、冒险、不听劝阻等事实，就写经营者承担赔偿责任。
- 可以写“若受害人有过错，可相应减轻经营者责任”，但不要在无事实依据时主动把责任降成“可能主要责任”。
- 考场稳妥句：题面未显示游客自身存在过错，旅游公司应对工作人员执行工作任务造成的损害承担相应赔偿责任。

## 三、法人商誉 vs 商业诋毁

先问行为人和受害企业是否存在竞争关系或经营竞争语境：

- 普通自媒体、个人、非竞争者无事实依据贬损企业，造成负面影响：走 A2 法人名誉/商誉，写停止侵害、消除影响、赔礼道歉或声明、赔偿损失。
- 竞争者、经营者在竞争语境中编造传播虚假信息，损害竞争对手商誉：可走 A5 商业诋毁/不正当竞争。
- 题面没有竞争关系，不要为了“企业”二字强行写 A5。

## 四、食品药品特殊赔偿 vs 一般消费者欺诈

先看题面有没有三个信号：

1. 商品身份：食品、药品、保健食品、医疗器械等。
2. 安全问题：不符合安全标准、危及健康、造成健康损害。
3. 设问或材料明确要求适用食品药品安全责任。

三者不全时，先按一般消费者欺诈写退一赔三。遇到治疗功效虚假宣传但未明示食品药品安全标准，可写：

- 至少构成虚假宣传或欺诈，支持退还价款并退一赔三。
- 如题面进一步证明属于食品药品安全责任，可依法适用更高惩罚性赔偿。

这样既不漏一般欺诈，也不贸然套十倍。

## 五、格式条款/提示不清 vs 欺诈

判断顺序：

- 只有预扣、提示不清、格式条款、消费者不知情、未实际服务：优先 A9 知情权/公平交易权 + A4 格式条款，写退还款项。
- 有虚构事实、隐瞒决定性事实、明知不能履行仍诱导购买、虚假承诺服务效果：才升为欺诈，写退一赔三。
- 不确定时写边界句：本题材料足以支持返还；若另能证明经营者故意虚构或隐瞒关键事实诱导消费，可另主张欺诈惩罚性赔偿。

## 六、术语精度分层

每个答案按两层写：

- 必得层：主入口、要件、结论、责任方式。
- 加分层：标准术语和边界句。

不要因为加分层不确定而破坏必得层。先把必得层写稳，再用“若题面进一步证明……”写边界。
"""

README = """# v13.4 零基础边界决策树补丁说明

本目录是在 v13.3 真实 Claude Round03 盲测后生成的窄补丁，不覆盖旧版本。

v13.3 已经接近通过，但 Claude 仍在边界题上自疑。v13.4 的目标是让零基础学生知道：

- 过错分担通常不需要猜比例。
- 没有受害人过错事实时，不主动给经营者减责。
- 无竞争关系的商誉损害优先 A2，不强行 A5。
- 治疗功效虚假宣传先保底退一赔三，食品药品特殊赔偿要看安全标准信号。
- 预扣/提示不清先格式条款返还，欺诈要有诱导或虚构事实。
"""


def rows() -> dict[str, dict[str, str]]:
    with TRACE.open(encoding="utf-8-sig", newline="") as f:
        return {r["question_id"]: r for r in csv.DictReader(f)}


def framework() -> str:
    base = (V13_3 / "01_双轴法律主观题框架章_v13_3责任方式术语补丁.md").read_text(encoding="utf-8")
    return base + "\n\n---\n\n" + PATCH


def make_payload(rs: dict[str, dict[str, str]], fw: str) -> str:
    parts = [
        "# Claude Zero-Baseline Iterative Live Test Round04：选必二《法律与生活》\n",
        "任务：请你模拟一个“什么都不知道但很聪明的高三学生”。这是新的隔离测试，不参考任何历史聊天、旧答案或外部资料。你只知道下面的 v13.4 框架和题面压缩信息。\n",
        "硬规则：\n",
        "1. 你是正在考试的学生，不是老师或阅卷人。\n",
        "2. 只能使用下面的框架和题目材料，不调用外部资料，不补充题目没有给出的事实。\n",
        "3. 我不给你标准答案、评分锚点、材料触发链、答案骨架、学生预警。\n",
        "4. 每道题按固定格式回答：A轴主入口判断；B轴设问动作判断；材料信号；现场答案；自我估分和最可能丢分点。\n",
        "5. 最后总评：v13.4 是否已经足够让零基础但聪明学生稳定高分？若仍不足，缺口在哪里？\n",
        "测试类型：targeted stress retest after v13.4 boundary decision patch\n",
        f"测试题号：{', '.join(SELECTED_IDS)}\n\n---\n\n## A. 你先学习的框架\n\n",
        README,
        "\n\n",
        fw,
        "\n\n---\n\n## B. 盲测题\n\n以下只提供题面压缩信息和设问，不提供答案骨架或评分锚点。\n",
    ]
    for i, qid in enumerate(SELECTED_IDS, 1):
        r = rs[qid]
        parts.append(
            f"""
### 题{i}: {qid}

- 区年卷题：{r["year"]}年 {r["district"]} {r["exam_stage"]} 第{r["question_no"]}题
- 设问：{r["prompt_action"]}
- 材料/题面压缩：{r["material_core"]}
"""
        )
    return "".join(parts)


def make_key(rs: dict[str, dict[str, str]]) -> str:
    out = ["# Local Answer Key for Claude Zero-Baseline Iterative Test Round04\n\n", "This file is NOT sent to Claude.\n"]
    for i, qid in enumerate(SELECTED_IDS, 1):
        r = rs[qid]
        out.append(
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
    return "\n".join(out)


def main() -> None:
    V13_4.mkdir(parents=True, exist_ok=True)
    (TEST / "web_payloads").mkdir(parents=True, exist_ok=True)
    (TEST / "model_outputs").mkdir(parents=True, exist_ok=True)
    (TEST / "codex_adjudication").mkdir(parents=True, exist_ok=True)
    rs = rows()
    fw = framework()
    (V13_4 / "00_READ_ME_FIRST.md").write_text(README, encoding="utf-8", newline="\n")
    (V13_4 / "01_双轴法律主观题框架章_v13_4边界决策树补丁.md").write_text(fw, encoding="utf-8", newline="\n")
    (V13_4 / "02_ROUND03_TO_V13_4_CODEX_ADJUDICATION.md").write_text(
        """# Round03 To v13.4 Codex Adjudication

Accepted patches:

- Boundary decision tree for fault apportionment.
- Safety-liability no-unfounded-reduction rule.
- A2商誉 vs A5商业诋毁 decision tree.
- General consumer fraud vs food/drug special compensation decision tree.
- Format clause refund vs fraud compensation decision tree.

No locked question is reclassified. No open-container row is promoted.
""",
        encoding="utf-8",
        newline="\n",
    )
    p = make_payload(rs, fw)
    (TEST / "web_payloads" / "CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND04_PAYLOAD.md").write_text(p, encoding="utf-8", newline="\n")
    (TEST / "codex_adjudication" / "LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md").write_text(make_key(rs), encoding="utf-8", newline="\n")
    (TEST / "ROUND_PROGRESS.md").write_text(
        f"""# Claude Zero-Baseline Iterative Test Round04 Progress

Status: `v13_4_payload_prepared_pending_real_claude_web_capture`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.4 boundary decision patch
- Selected questions: {", ".join(SELECTED_IDS)}
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND04_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 43/50; no unresolved framework-level patch required by Claude or Codex.
""",
        encoding="utf-8",
        newline="\n",
    )
    print(V13_4)
    print(TEST)
    print("payload_chars", len(p))


if __name__ == "__main__":
    main()
