from __future__ import annotations

import csv
import importlib.util
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE_SCRIPT = ROOT / "build_v14_zero_baseline_baodian.py"
OUT = ROOT / "v14_3_gpt_patch_framework_baodian"
V14_2 = ROOT / "v14_2_zero_baseline_framework_baodian"


def load_builder():
    spec = importlib.util.spec_from_file_location("v14_builder", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load v14 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_key(mapping: dict[str, object], prefix: str) -> str:
    for key in mapping:
        if key.startswith(prefix):
            return key
    raise KeyError(prefix)


def install_gpt_patch_rules(b) -> None:
    a1 = find_key(b.A_RULES, "A1")
    a2 = find_key(b.A_RULES, "A2")
    a3 = find_key(b.A_RULES, "A3")

    b.A_RULES[a1]["memory"] = "先查效力，但在行为能力、意思表示、追认直接决定诉求时，A1就是得分脊柱。"
    b.A_RULES[a1]["not_this"] = (
        "不能机械说A1只作辅助。未成年人消费、超龄超额交易、追认、效力直接决定结论时，"
        "A1先作主脊柱，再让消费者、合同、劳动等入口说明场景。"
    )
    b.A_RULES[a1]["chain"] = "行为能力/意思表示/追认 -> 效力 -> 返还/责任分担 -> 场景入口补充。"

    b.A_RULES[a2]["not_this"] = (
        "消费者、平台、邻里、校园等背景不会吞掉人格权。材料出现隐私、个人信息、名誉、肖像、安宁，"
        "先把权利名叫准，再看是否需要A3/A9副入口。"
    )
    b.A_RULES[a3]["not_this"] = (
        "审批、公示、消防、法院勘查是事实和程序证据，不自动抢成A10；但监控、门铃、采光、通行类题要同步检查人格权边界。"
    )

    b.A_SWITCHES[a1] = (
        "年龄/智力/金额是否相适应；是否同意或追认；行为效力是否直接决定诉求；"
        "若是，A1作主脊柱，具体场景只作副入口。"
    )

    b.B_RULES[
        "B2_判决/裁判/责任理由 + B5_意义/价值/保护/推动"
    ] = {
        "memory": "先判理由，再收意义。",
        "shape": "裁判结论/责任理由 -> 规则事实 -> 价值意义；意义必须从本案规则推出。",
        "first": "先回答为什么这样判，再写该判决保护了谁、规范了什么秩序。",
    }
    b.B_RULES[
        "B4_评析/认识/观点 + B6_调解/维权/纠纷解决路径"
    ] = {
        "memory": "先评边界，再给路径。",
        "shape": "观点合理处/片面处 -> 法律边界 -> 证据、协商、调解、诉讼或整改方案。",
        "first": "先评材料中做法或观点是否越界，再提出可执行处理方案。",
    }

    b.CONFUCIUS_REPAIR_RULES = b.CONFUCIUS_REPAIR_RULES + [
        "混合设问先拆动词：理由+意义写B2+B5，评析+建议写B4+B6，补全+任选展开写B7+B6；不能用一个B标签吃掉全题。",
        "题卡迁移必须写三信号、主入口和错入口排除；不能只写一句同类题识别。",
    ]

    patch_rules = {
        "CC0150_2025_朝阳_二模_20": [
            "本题按 A2主入口 + A3边界 + B4/B6 处理：先评摄像头是否侵害隐私/个人信息，再处理住宅所有权、相邻安宁和调解整改。",
            "必须写摄像范围、拍摄角度、存储功能、提示告知、邻里协商或调解方案，不能只写人格权标签。",
        ],
        "CC0364_2026_通州_期中_19_1": [
            "相邻关系不能空喊原则；必须写程序合法、业主同意/公示、审查或勘查事实、实际影响和停止妨害/合理救济。",
        ],
        "CC0054_2024_石景山_一模_17": [
            "本题是 B2+B5：先说明合同成立和裁判理由，再从诚信原则、绿色原则、交易安全和碳排放配额市场秩序收意义。",
        ],
        "CC0244_2026_东城_期中_18": [
            "责任与维权分段：合同违约先定，致损赔偿再看因果；商业损失按已告知、有证据、有因果、可预见四项判断。",
        ],
        "CC0137_2025_昌平_二模_20": [
            "A5与A4分格：知识产权/竞争秩序是主格，合同或授权关系只用于说明行为来源，不得整题写成创新意义题。",
        ],
        "CC0289_2026_朝阳_二模_18": [
            "先短句补全三个问答，再任选其一展开权利、侵害、证据、路径、请求；不能只写泛泛依法保护。",
        ],
        "CC0002_2024_丰台_一模_17": [
            "好意同乘减责不是免责；必须写侵权责任、无故意或重大过失时可减轻、受害人自身过错影响分担，再收现实意义。",
        ],
        "CC0214_2025_门头沟_一模_20_2": [
            "劳动解除或合同效力要看招聘条件、岗位关联、是否如实告知、是否严重影响录用决定和解除程序，不能把所有简历遗漏都写成可解除。",
        ],
        "CC0200_2025_西城_二模_18": [
            "A1作得分脊柱：限制民事行为能力、大额打赏、监护人未追认决定效力和返还基础；A9只说明直播平台消费场景。",
        ],
        "CC0143_2025_朝阳_一模_19": [
            "隐蔽搭售、欺诈、可撤销、退费、惩罚性赔偿分项判断；不是所有退费都自动三倍赔偿。",
        ],
    }
    for qid, rules in patch_rules.items():
        b.TARGETED_REPAIR_RULES.setdefault(qid, [])
        for rule in rules:
            if rule not in b.TARGETED_REPAIR_RULES[qid]:
                b.TARGETED_REPAIR_RULES[qid].append(rule)


def patch_rows(b, rows: list[dict[str, str]]) -> list[dict[str, str]]:
    special_b = {
        "CC0054_2024_石景山_一模_17": "B2_判决/裁判/责任理由 + B5_意义/价值/保护/推动",
        "CC0002_2024_丰台_一模_17": "B2_判决/裁判/责任理由 + B5_意义/价值/保护/推动",
        "CC0150_2025_朝阳_二模_20": "B4_评析/认识/观点 + B6_调解/维权/纠纷解决路径",
    }
    row_patch = {
        "CC0150_2025_朝阳_二模_20": {
            "a_axis_secondary_status": "有：A3_物权与相邻关系",
            "student_warning": "只写隐私权会漏相邻安宁和整改路径；只写相邻关系会漏人格权权利名。",
        },
        "CC0054_2024_石景山_一模_17": {
            "student_warning": "不能只写合同成立；本题还要把判决意义落到诚信、绿色、交易安全和碳排放配额市场秩序。",
        },
        "CC0200_2025_西城_二模_18": {
            "a_axis_secondary_status": "有：A1_民事法律关系总论作得分脊柱；A9为直播平台消费场景",
            "student_warning": "本题不能写成普通消费者退费题；先写限制民事行为能力、追认、返还和多方过错分担。",
        },
        "CC0143_2025_朝阳_一模_19": {
            "student_warning": "看到消费者和平台不能机械写三倍赔偿；必须先判断隐瞒、误导、欺诈事实是否足够。",
        },
        "CC0214_2025_门头沟_一模_20_2": {
            "student_warning": "不能把所有简历遗漏都写成可解除；要看岗位关联、录用影响、解除依据和程序。",
        },
    }

    for row in rows:
        qid = row.get("question_id", "")
        if qid in special_b:
            row["b_axis"] = special_b[qid]
        if qid in row_patch:
            row.update(row_patch[qid])
        row["v14_3_gpt_patch_status"] = "patched_from_real_gpt_pro_review" if qid in (set(special_b) | set(row_patch)) else "global_patch_applied"
    return rows


def install_runtime_overrides(b) -> None:
    old_effective_b_axis = b.effective_b_axis
    old_first_answer_sentence = b.first_answer_sentence

    def effective_b_axis_v14_3(row: dict[str, str]) -> str:
        axis = row.get("b_axis", "")
        if " + " in axis:
            return axis
        return old_effective_b_axis(row)

    def transfer_sentence_v14_3(row: dict[str, str]) -> str:
        a = row.get("a_axis_primary", "")
        b_axis = effective_b_axis_v14_3(row)
        trigger_rows = b.split_trigger(row.get("material_trigger", ""))
        facts = [x[0] for x in trigger_rows[:3]]
        while len(facts) < 3:
            facts.append("主体、行为、损害或请求能落入同一法律关系")
        warning = b.clean(row.get("student_warning")) or b.A_RULES.get(a, {}).get("not_this", "不要误入其他入口")
        return (
            f"- 同类题三信号：{facts[0]}；{facts[1]}；{facts[2]}。\n"
            f"- 优先入口和动作：先按 {b.axis_code(a)} 定法律关系，再按 {b.axis_code(b_axis)} 组织答案。\n"
            f"- 错入口排除：{warning}"
        )

    def first_answer_sentence_v14_3(row: dict[str, str]) -> str:
        parts = b.bullets_from_slashes(row.get("answer_skeleton", ""))
        first = parts[0]
        b_axis = effective_b_axis_v14_3(row)
        if " + " in b_axis:
            return f"本题先拆混合设问，再写第一得分句：{first}。"
        return old_first_answer_sentence(row)

    b.effective_b_axis = effective_b_axis_v14_3
    b.transfer_sentence = transfer_sentence_v14_3
    b.first_answer_sentence = first_answer_sentence_v14_3


def apply_framework_patch(text: str) -> str:
    text = text.replace("v14.2", "v14.3")
    text = text.replace("Confucius 盲测后补上的十条硬规则", "学生盲测后补上的十四条硬规则")
    text = text.replace("下面十条不是装饰", "下面十四条不是装饰")
    insert_after = "> 把一个生活冲突，翻译成法律关系、法律规则和法律后果。\n"
    patch = """

## 0A. 必须先背的母公式

v14.3 把所有题先压成一条母公式：

`设问定型 -> 材料翻法 -> 规则事实结论 -> 必要价值`

- 设问定型：先看题目动词，是判理由、评析、意义、表格、诉求还是路径。
- 材料翻法：把生活事实翻成法律主体、权利义务、构成条件、证据和程序。
- 规则事实结论：每一句答案都必须是规则带事实，事实落结论。
- 必要价值：只有题目问意义，或判决明显要求价值收束时才写，不能空喊法治。

## 0B. C 轴：题内开关，不增加大入口

C 轴不是新的知识目录，而是遇到特殊题时先按下的开关：

| C开关 | 看到什么就启动 | 写作硬句 |
|---|---|---|
| C1 行为能力与追认 | 未成年人、老人、金额巨大、监护人不知情 | 先查行为能力、意思表示和追认，再谈返还和过错分担。 |
| C2 三从属性 | 平台派单、考勤、奖惩、结算、组织管理 | 不看协议名称，看实际管理控制、经济依赖和组织纳入。 |
| C3 技术秘密三性 | 图纸、配方、数据、算法、研发资料 | 先写秘密性、价值性、保密措施，再写不正当获取使用。 |
| C4 消费者欺诈三倍 | 隐瞒、误导、虚假宣传、搭售 | 欺诈事实足够才写惩罚性赔偿，不足时只写退费或赔偿。 |
| C5 好意同乘减责 | 免费搭车、帮忙接送、非营运 | 减轻不等于免除；还要看驾驶人过错和受害人自身过错。 |
| C6 竞业限制平衡 | 离职、竞业、补偿、商业秘密 | 同时看劳动者就业权、单位秘密保护和限制范围是否适度。 |
| C7 多主体分责 | 平台、监护人、本人、经营者、第三人 | 一个主体一条链，不能糊成一段。 |
| C8 证据路径 | 维权、调解、诉讼、举证、公证 | 先固定争议焦点，再写证据、路径和请求。 |

## 0C. 混合设问拆分规则

题干有两个动词，就拆两个 B 动作：

- 理由 + 意义：先 B2 判理由，再 B5 收意义。
- 评析 + 建议：先 B4 评边界，再 B6 给路径。
- 补全 + 任选展开：先 B7 补短句，再 B6 展开权利、证据、路径、请求。
- 责任 + 维权：先 B2/B3 定责任或请求，再 B6 写证据、路径、请求。

## 0D. 反向筛查

落笔前用这十条排错：

1. 看见法院，不等于写公正司法；先看实体法律关系。
2. 看见平台，不等于劳动关系；先查三从属性。
3. 看见消费者，不等于三倍赔偿；先查欺诈事实。
4. 看见未成年人消费，先查行为能力和追认。
5. 看见监控门铃，不能只写物权；同步查隐私、个人信息和相邻安宁。
6. 看见技术资料，先查秘密性、价值性、保密措施。
7. 看见好意同乘，减责不等于免责。
8. 看见表格，按原表头；看不见表头就用事实、规则、裁判要点三列。
9. 看见两个动词，先拆小问再落笔。
10. 看见意义，必须从本案具体规则推出，不能空喊价值。
"""
    if insert_after in text and "## 0A. 必须先背的母公式" not in text:
        text = text.replace(insert_after, insert_after + patch, 1)
    return text


def exam_short_answer(row: dict[str, str], b) -> str:
    parts = b.bullets_from_slashes(row.get("answer_skeleton", ""))[:4]
    if not parts:
        return "先写本题法律关系，再把材料事实压进规则，最后落到结论。"
    return "\n".join(f"- {part}。" for part in parts)


def patch_card_short_answers(cards: str, rows: list[dict[str, str]], b) -> str:
    by_id = {row["question_id"]: row for row in rows}
    qids = list(by_id)
    pattern = re.compile(r"(### \d+\. (?P<qid>CC[^\n]+)\n.*?#### 9\. 最短考场写法\n\n)(?P<body>.*?)(?=\n\n### \d+\. CC|\Z)", re.S)

    def repl(match: re.Match[str]) -> str:
        qid = match.group("qid").strip()
        row = by_id.get(qid)
        if not row:
            return match.group(0)
        return match.group(1) + exam_short_answer(row, b)

    cards = pattern.sub(repl, cards)
    cards = cards.replace("v14.2", "v14.3")
    cards = cards.replace("v12.2路径：", "本题路径：")
    cards = cards.replace("Round05 guardrail：", "易错提醒：")
    cards = cards.replace("Round05补丁：", "易错提醒：")
    cards = cards.replace("Confucius", "学生盲测")
    return cards


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def write_trace(rows: list[dict[str, str]], b) -> None:
    path = OUT / "traceability" / "TRACEABILITY_MATRIX_v14_3.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) + ["v14_3_effective_b_axis", "v14_3_gpt_patch_note"]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            out = dict(row)
            out["v14_3_effective_b_axis"] = b.effective_b_axis(row)
            out["v14_3_gpt_patch_note"] = row.get("v14_3_gpt_patch_status", "")
            writer.writerow(out)


def write_claude_student_pack(rows: list[dict[str, str]]) -> None:
    wanted_prefixes = ["CC0150", "CC0364", "CC0244", "CC0103", "CC0002", "CC0214", "CC0200", "CC0325"]
    selected = []
    for prefix in wanted_prefixes:
        row = next((r for r in rows if r.get("question_id", "").startswith(prefix)), None)
        if row:
            selected.append(row)

    prompt = """# Claude zero-baseline student simulation prompt v14.3

你现在不是教师、不是审稿人，也不是法律专家。

请扮演一个“聪明但完全没学过《法律与生活》主观题框架的高三学生”。你只能使用随附的框架文件和盲测题包现场学习。不得调用你自己的法学知识来补框架，也不得假装看过答案。

## 任务

1. 先用 5-8 分钟读框架文件，写出你理解到的做题步骤。
2. 对盲测包里的 8 道题逐题作答。
3. 每题必须输出：
   - 你选的 A 入口；
   - 你选的 B 动作；
   - 是否触发 C 轴开关；
   - 你会写在答题纸上的答案；
   - 你哪里是靠框架直接学会的；
   - 你哪里仍然不确定，可能扣分。
4. 最后作为学生反骂这份框架：它到底是不是框架？能不能让零基础学生快速习得？哪里还像老师资料而不是学生工具？

## 判定格式

最后必须给一个总判定：

- `CLAUDE_STUDENT_FRAMEWORK_PASS`
- `CLAUDE_STUDENT_PASS_AFTER_PATCH`
- `CLAUDE_STUDENT_FAIL`

不要给客套话。重点看：只靠框架能不能现场做题。
"""
    lines = [
        "# Claude blind test pack v14.3",
        "",
        "Only this blind pack and the framework chapter may be shown to Claude student simulation.",
        "Do not attach the 42-question answer-analysis file for this test.",
        "",
    ]
    for idx, row in enumerate(selected, 1):
        lines += [
            f"## {idx}. {row.get('question_id')}",
            "",
            f"- 区年卷题：{row.get('year')}年 {row.get('district')} {row.get('exam_stage')} 第{row.get('question_no')}题",
            f"- 设问：{row.get('prompt_action')}",
            f"- 材料压缩：{row.get('material_core')}",
            "",
        ]
    write(OUT / "claude_student_simulation" / "CLAUDE_ZERO_BASELINE_STUDENT_PROMPT_v14_3.md", prompt)
    write(OUT / "claude_student_simulation" / "CLAUDE_BLIND_TEST_PACK_8Q_v14_3.md", "\n".join(lines) + "\n")


def build_governance() -> str:
    return """# 05 GPT补丁落实与治理边界 v14.3

## Real GPT Pro Gate

Status: `GPT_REVIEW_PASS_AFTER_PATCH_CAPTURED_AS_PATCH_SOURCE`

Evidence:

- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_PROMPT_v14_2_with_prior_framework.md`
- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md`

Boundary:

- GPT Pro did run in Chrome and read the five uploaded files.
- The clean full raw transcript was not exported because ChatGPT page extraction timed out after the long response.
- v14.3 implements the visible GPT minimum patch list and should be sent to Claude student simulation next.
- This is still not DOCX/PDF delivery.

## What v14.3 changed

1. Restored a mother formula before A/B.
2. Added C-axis in-question switches without adding main entrances.
3. Repaired A1 priority for behavior capacity/追认/效力 scenarios.
4. Added mixed-B split rules.
5. Added reverse-screening checklist.
6. Reframed hard rules as fourteen student rules.
7. Patched the ten GPT-flagged question cards.
8. Rewrote migration sections into three signals, priority entrance/action, and wrong-entrance exclusion.
9. Replaced generic shortest answer section with question-specific answer bullets.
10. Removed model/governance chatter from student-facing main text where possible.
"""


def build_governor() -> str:
    return """# 06 Final Governor Checklist v14.3

## Verdict

`MARKDOWN_FRAMEWORK_AND_42_QUESTION_BAODIAN_GPT_PATCH_APPLIED_PENDING_CLAUDE_STUDENT_SIM_AND_DOCX_PDF`

## Gate Table

| Gate | Status | Evidence |
|---|---|---|
| v14.3 framework chapter exists | PASS | `01_先背这套_法律主观题不扣分框架_v14_3.md` |
| v14.3 42-question analysis exists | PASS | `02_42题按框架拆解与解析_v14_3.md` |
| Combined v14.3 baodian exists | PASS | `选必二法律与生活_法律宝典_v14_3_GPT补丁版.md` |
| GPT Pro review used | PASS_WITH_CAPTURE_LIMIT | `external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md` |
| GPT minimum patches applied | PASS | `05_GPT补丁落实与治理边界_v14_3.md` |
| Traceability matrix updated | PASS | `traceability/TRACEABILITY_MATRIX_v14_3.csv` |
| Claude zero-baseline student simulation on v14.3 | PENDING | must run next |
| DOCX delivery | NOT PRODUCED | no DOCX claimed |
| PDF delivery | NOT PRODUCED | no PDF claimed |

## Allowed Claim

v14.3 is the GPT-patched Markdown candidate: framework chapter, 42-question framework analysis, and combined baodian exist.

## Not Allowed

- Do not claim Claude simulation has passed v14.3 yet.
- Do not claim full raw GPT transcript exists.
- Do not claim final external governance PASS.
- Do not claim DOCX/PDF delivery.
"""


def main() -> None:
    b = load_builder()
    install_gpt_patch_rules(b)
    install_runtime_overrides(b)
    rows = patch_rows(b, b.read_rows())

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    if (V14_2 / "external_gate_attempts").exists():
        shutil.copytree(V14_2 / "external_gate_attempts", OUT / "external_gate_attempts")

    framework = apply_framework_patch(b.build_framework(rows))
    cards = patch_card_short_answers(b.build_question_cards(rows), rows, b)
    open_appendix = b.build_open_appendix().replace("v14", "v14.3")
    governance = build_governance()
    combined = "\n\n---\n\n".join(
        [
            "# 选必二法律与生活：法律宝典 v14.3 GPT补丁版",
            framework,
            cards,
            open_appendix,
            governance,
        ]
    )

    readme = """# v14.3 GPT Patch Framework Baodian

This directory is the v14.3 Markdown candidate after real GPT Pro review.

It includes:

- a patched student-first framework,
- all 42 locked core questions analysed by the framework,
- a combined legal baodian Markdown,
- separated open-container appendix,
- GPT patch governance and final checklist,
- updated traceability.

Boundary: Claude zero-baseline student simulation and DOCX/PDF delivery are still pending.
"""
    write(OUT / "00_READ_ME_FIRST.md", readme)
    write(OUT / "01_先背这套_法律主观题不扣分框架_v14_3.md", framework)
    write(OUT / "02_42题按框架拆解与解析_v14_3.md", cards)
    write(OUT / "04_开放容器与不晋升题附录_v14_3.md", open_appendix)
    write(OUT / "05_GPT补丁落实与治理边界_v14_3.md", governance)
    write(OUT / "06_FINAL_GOVERNOR_CHECKLIST_v14_3.md", build_governor())
    write(OUT / "选必二法律与生活_法律宝典_v14_3_GPT补丁版.md", combined)
    write_trace(rows, b)
    write_claude_student_pack(rows)
    write(OUT / "build_manifest.txt", "built_by=build_v14_3_gpt_patch.py\nstatus=gpt_patch_applied_pending_claude_student_sim\n")


if __name__ == "__main__":
    main()
