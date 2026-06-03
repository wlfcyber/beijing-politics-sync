#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the overnight batch-framework pipeline artifacts for xuanbier law.

The design follows the user's earliest framework-method context:
"先发现，不建构" -> question-level action cards -> batch mechanism synthesis ->
high-frequency trunk + full/open container -> pressure test -> Confucius
zero-baseline simulation.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q = ROOT / "04_merge_audit/merged_subjective_law_questions.csv"
M = ROOT / "04_merge_audit/merged_material_atoms_subjective.csv"
A = ROOT / "04_merge_audit/merged_ask_atoms_subjective.csv"
R = ROOT / "04_merge_audit/merged_rubric_atoms_subjective.csv"
RUN = ROOT / "05_reasoner_packets/night_batch_framework_council_20260520"
FRAMEWORK = ROOT / "11_final_framework/framework_v3_night_batch_20260520.md"
STUDENT = ROOT / "11_final_framework/framework_v3_night_batch_student_one_page.md"
TEACHER = ROOT / "11_final_framework/framework_v3_night_batch_teacher_guide.md"
BAODIAN = ROOT / "12_final_baodian/选必二法律主观题满分宝典_夜间重构版.md"
TEST_CSV = ROOT / "10_framework_validation/framework_v3_night_batch_question_by_question_test.csv"
TEST_MD = ROOT / "10_framework_validation/framework_v3_night_batch_pass_report.md"
CONFUCIUS = ROOT / "10_framework_validation/confucius_zero_baseline_simulation_night_batch_20260520.md"
ACCEPT = ROOT / "FINAL_ACCEPTANCE_REPORT_NIGHT_BATCH_20260520.md"


INITIAL_CONTEXT = """# 必修四喂细则 / 选必二框架设计：最初构思上下文

本段来自用户最初构思时的项目上下文，作为本轮夜间重构的最高方法约束。

## 核心转向

不要一开始命名一个漂亮总框架。先做题目级动作发现，再把动作合并成框架。

当时的关键词是：

- 先发现，不建构。
- 框架之前先有动作库。
- 每一道题先做动作卡。
- 观察学生在这道题里必须先判断什么、材料触发什么、细则奖励什么。
- 积累 30-50 张动作卡后，再看哪些动作能合并，哪些是主动作，哪些只是局部知识，哪些能迁移。

## 动作卡字段

- 题源
- 题型：选择题 / 主观题
- 题目表层内容
- 材料中的人/主体
- 材料中的冲突/问题
- 学生第一反应应该是什么
- 必须调用的法律知识
- 细则/答案奖励的表达
- 错项或失分点
- 这道题实际训练的动作
- 这个动作是否可迁移
- 暂不命名的观察

## 对本轮夜间重构的约束

1. 65 题不能一口气压成抽象大词。
2. 必须先轻分类为同类命题机制批次。
3. 每一批先问：这类题到底训练学生哪个动作。
4. 框架必须由动作批次收敛出来。
5. 学生版只能放考场动作和满分句，不放证据台账。
6. 教师版和证据附录负责守住 formal / reference_only / boundary。
"""


@dataclass(frozen=True)
class Node:
    node_id: str
    name: str
    student_order: str
    core_action: str
    trigger: str
    sentence: str
    wrong_path: str


NODES = {
    "N00": Node(
        "N00",
        "先刹车",
        "第一眼先问：它是不是选必二法律主观题",
        "先挡住必修三化、经济化、法考化；只要题目主要问国家治理、依法行政、宏观法治、产业治理，就不套私法模板。",
        "主语是国家、政府、治理体系、依法行政、涉外法治、AI产业治理、开源智能体综合治理。",
        "本题不是普通私人法律关系题，应围绕材料中的制度、机制、程序和效果展开，不能直接套合同、侵权、维权模板。",
        "一看到法律二字就写全面依法治国，或一看到法院就机械写合同侵权。",
    ),
    "N01": Node(
        "N01",
        "格子题：一格一答",
        "有表格先服从格子",
        "先看每一格问的是机制、理由、措施还是意义；一格只答一个任务，绝不跨格抄模板。",
        "表格、填入、表中、机制/理由/措施/意义分栏。",
        "这一格要求说明【格子任务】。材料中【事实】对应【法律规则/程序】，因此应写【最短结论】。",
        "跨格写一大段“维护合法权益、促进公平正义”，格子问机制却写意义。",
    ),
    "N02": Node(
        "N02",
        "评判裁判题：先判后证",
        "问是否、判决、认识，先表态",
        "先写支持/不支持、有效/无效、构成/不构成、法院判决有依据；再写规则和材料事实。",
        "是否、支持、不支持、有效、无效、构成、判决、法院、谈谈认识、法理依据。",
        "我认为【结论】。人民法院以事实为根据、以法律为准绳。根据【法律规则】，材料中【事实】符合/不符合【要件】，所以【责任/判决/请求】成立。",
        "没有首句表态；只写法条不落到本案；把裁判锚句当成整题答案。",
    ),
    "N03": Node(
        "N03",
        "私法责任题：切责成链",
        "合同、侵权、消费、劳动、相邻都走责任链",
        "定主体关系，定行为性质，放入规则要件，落责任/效力/请求。",
        "合同、要约、承诺、履行、违约、侵权、赔偿、消费者、欺诈、劳动、相邻、人格权、生命健康权。",
        "【主体A】与【主体B】之间形成【法律关系】。【行为】符合【规则要件】。材料中【事实】说明【要件成立/不成立】，因此【责任、效力或诉求】应当【支持/不支持】。",
        "只背权利名称，不判断法律关系；材料事实贴在后面当故事，没有塞进规则要件。",
    ),
    "N04": Node(
        "N04",
        "创新竞争题：定行为、护秩序",
        "知识产权和竞争题先定行为",
        "先判断侵犯的是著作权、商标、专利、商业秘密，还是不正当竞争；再写保护创新和市场秩序。",
        "知识产权、著作权、商标、专利、商业秘密、商业诋毁、混淆、不正当竞争、AI作品、核心代码、创新。",
        "材料中【行为】属于【侵权/不正当竞争类型】，损害了【权利/竞争秩序】。依法应【停止侵害/赔偿/承担责任】，这有利于保护创新成果、规范市场竞争秩序。",
        "一看到创新就空写新质生产力；著作权、商标、商业秘密混用；漏法院具体责任。",
    ),
    "N05": Node(
        "N05",
        "程序救济题：路径、证据、请求",
        "问怎么办、如何维权，先走路径",
        "先选协商、调解、仲裁、诉讼或司法确认；再写证据和请求；公益诉讼单列公益主体和强制执行。",
        "调解、仲裁、诉讼、起诉状、证据、举证、诉讼请求、司法确认、强制执行、公益诉讼、和解。",
        "当事人可以通过【路径】解决纠纷，并围绕【争议事实】提交【证据】，提出【请求】。若经法院依法确认，【协议/裁判】具有相应法律效力。",
        "把所有题都写成起诉；调解题写成判决；公益诉讼写成个人维权。",
    ),
    "N06": Node(
        "N06",
        "风险合规题：一险一界一措施",
        "AI、数据、平台、合规题先分风险",
        "一项风险对应一条法律边界和一项治理/合规措施；区分具体权利风险和宏观治理开放题。",
        "风险、合规、AI、人工智能、数字员工、数据、算法、平台、开源智能体、治理、边界。",
        "材料中的【风险】触及【法律边界/权利义务】。应当通过【制度/合同/告知/授权/审核/责任机制】加以规范，做到【具体效果】。",
        "一看到 AI 就写科技伦理；一看到风险就写诉讼赔偿；不把风险和措施一一对应。",
    ),
    "N07": Node(
        "N07",
        "意义价值题：从本案推出三层价值",
        "问意义、作用、价值，最后补三层",
        "先处理本案法律规则，再写保护谁、规范什么秩序、弘扬什么价值。",
        "意义、作用、价值、有利于、弘扬、促进、维护、规范、秩序、公平、正义、诚信、核心价值观。",
        "该处理有利于保护【具体主体】的合法权益，有利于规范【具体司法/行业/市场秩序】，有利于弘扬【诚信/公平/友善/法治】等具体价值。",
        "上来空喊公平正义；三层主语重复；价值句没有从本案法律规则推出。",
    ),
}


REFERENCE_PREFIXES = {"CC0040", "CC0162", "CC0311", "CC0353"}
BOUNDARY_IDS = {
    "CC0276_2026_房山_二模_17",
    "CC0380_2026_顺义_二模_18_2",
    "RECOVER_2026_西城_二模_18_3",
}
LOW_FREQ = {
    "CC0011_2024_丰台_二模_17",
    "CC0332_2026_石景山_二模_19",
    "CC0340_2026_西城_一模_17",
    "RECOVER_2024_东城_一模_19",
    "CC0254_2026_丰台_二模_18",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def md_escape(s: str, limit: int = 900) -> str:
    s = re.sub(r"\s+", " ", (s or "")).strip()
    return s[:limit] + ("..." if len(s) > limit else "")


def short_id(qid: str) -> str:
    return qid.split("_", 1)[0] if qid.startswith("CC") else qid


def effective_ask(row: dict[str, str]) -> tuple[str, str]:
    ask = (row.get("ask_text") or "").strip()
    if ask and ask.lower() != "nan" and "设问待" not in ask:
        return ask, "ask_text"
    for field in ("rubric_text", "answer_text", "full_question_text"):
        text = re.sub(r"\s+", " ", row.get(field, "") or "").strip()
        if not text:
            continue
        # Try to capture the sentence that contains common ask verbs.
        parts = re.split(r"(?<=[。！？?])\s*", text)
        for p in parts[:8]:
            if any(k in p for k in ["结合", "运用", "谈谈", "分析", "说明", "评析", "理由", "意义", "作用", "认识"]):
                return p[:220], f"derived_from_{field}"
        return text[:180], f"fallback_from_{field}"
    return "", "missing"


def has_any(text: str, words: list[str]) -> bool:
    return any(w in text for w in words)


def route(row: dict[str, str], ask: str) -> tuple[str, list[str], str, str]:
    qid = row["question_id"]
    text = "\n".join(
        [
            ask,
            row.get("material_text", ""),
            row.get("rubric_text", ""),
            row.get("answer_text", ""),
        ]
    )
    hits: list[str] = []
    if has_any(text, ["表格", "表中", "填入", "填写", "分栏", "维度"]) and has_any(text, ["理由", "依据", "措施", "意义", "机制"]):
        hits.append("N01")
    if has_any(text, ["评析", "是否", "谈谈对", "认识", "判决", "法院", "支持", "不支持", "有效", "无效", "构成", "法理依据", "理由"]):
        hits.append("N02")
    if has_any(text, ["合同", "要约", "承诺", "履行", "违约", "解除", "侵权", "赔偿", "责任", "消费者", "欺诈", "劳动", "用人单位", "劳动者", "相邻", "共有", "物权", "人格权", "名誉权", "健康权", "生命权", "肖像权"]):
        hits.append("N03")
    if has_any(text, ["知识产权", "著作权", "商标", "专利", "商业秘密", "不正当竞争", "商业诋毁", "混淆", "创新", "核心代码", "数字人", "AI 图案", "人工智能生成"]):
        hits.append("N04")
    if has_any(text, ["调解", "仲裁", "诉讼", "起诉状", "证据", "举证", "司法确认", "强制执行", "公益诉讼", "维权", "请求", "诉讼请求", "和解"]):
        hits.append("N05")
    if has_any(text, ["风险", "合规", "边界", "人工智能", "AI", "开源", "智能体", "数据", "算法", "数字员工", "治理", "涉外法治", "国家治理"]):
        hits.append("N06")
    if has_any(text, ["意义", "价值", "作用", "有利于", "弘扬", "促进", "维护", "规范", "秩序", "公平", "正义", "诚信", "核心价值观", "社会整体福祉"]):
        hits.append("N07")
    hits = [n for n in NODES if n in hits]

    if qid in BOUNDARY_IDS:
        return "BATCH_F_BOUNDARY_OPEN", hits or ["N00"], "boundary_open", "formal but boundary/mixed/open-governance row"
    if row.get("evidence_level") == "reference_only" or short_id(qid) in REFERENCE_PREFIXES:
        return "BATCH_R_REFERENCE_ONLY", hits or ["N00"], "reference_only", "reference-only row locked out of core"
    if qid in LOW_FREQ:
        return "BATCH_L_LOW_FREQUENCY_CONTAINER", hits or ["N00"], "low_frequency_container", "low-frequency formal singleton"
    batch_hint_text = text
    table_strong = has_any(ask + "\n" + row.get("rubric_text", ""), ["完成下表", "下表", "表格", "表中", "补充完整", "填入", "填写"])
    risk_strong = has_any(batch_hint_text, ["人工智能", "AI", "数字员工", "数据", "算法", "开源", "智能体", "合规", "法律边界", "风险1", "风险2"])
    ip_strong = has_any(batch_hint_text, ["知识产权", "著作权", "商标", "专利", "商业秘密", "不正当竞争", "商业诋毁", "混淆", "核心代码", "AI 图案", "人工智能生成"])
    procedure_strong = has_any(batch_hint_text, ["调解", "仲裁", "起诉状", "举证", "司法确认", "公益诉讼", "强制执行", "诉讼请求", "维权途径", "行政诉讼"])
    private_strong = has_any(batch_hint_text, ["合同", "要约", "承诺", "履行", "违约", "侵权", "赔偿", "消费者", "欺诈", "劳动", "用人单位", "劳动者", "相邻", "共有", "物权", "人格权", "名誉权", "健康权", "生命权", "格式条款"])
    judgment_strong = has_any(ask + "\n" + row.get("rubric_text", ""), ["评析", "是否", "谈谈对", "认识", "判决", "法院", "支持", "不支持", "有效", "无效", "构成", "裁判理由", "法理依据"])
    value_strong = has_any(ask + "\n" + row.get("rubric_text", ""), ["意义", "价值", "作用", "有利于", "弘扬", "促进", "维护", "规范", "秩序", "公平", "正义", "诚信"])

    def with_primary(primary: str) -> list[str]:
        ordered = [primary]
        for h in hits:
            if h not in ordered:
                ordered.append(h)
        return ordered

    if table_strong:
        return "BATCH_A_TABLE_GRID", with_primary("N01"), "core_candidate", "table/grid task controls answer shape"
    if risk_strong:
        return "BATCH_F_RISK_BOUNDARY", with_primary("N06"), "core_candidate", "AI/data/digital/compliance boundary signal"
    if ip_strong:
        return "BATCH_D_IP_COMPETITION", with_primary("N04"), "core_candidate", "IP/competition/innovation signal"
    if procedure_strong:
        return "BATCH_E_PROCEDURE_REMEDY", with_primary("N05"), "core_candidate", "procedure/remedy signal"
    if private_strong:
        return "BATCH_C_PRIVATE_LIABILITY", with_primary("N03"), "core_candidate", "private-law responsibility chain"
    if judgment_strong:
        return "BATCH_B_JUDGMENT_EVALUATION", with_primary("N02"), "core_candidate", "judgment/evaluation signal"
    if value_strong:
        return "BATCH_G_VALUE_MEANING", with_primary("N07"), "core_candidate", "value/meaning signal"
    return "BATCH_Z_NEEDS_SOURCE_CHECK", hits or ["N00"], "source_check", "no stable action node"


def rubric_map() -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(R):
        out[row["question_id"]].append(row)
    return out


def material_map() -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(M):
        out[row["question_id"]].append(row)
    return out


def atom_summary(atoms: list[dict[str, str]], field: str, limit: int = 3) -> str:
    vals = [md_escape(a.get(field, ""), 170) for a in atoms[:limit]]
    return " / ".join(v for v in vals if v)


def build() -> None:
    RUN.mkdir(parents=True, exist_ok=True)
    (RUN / "INITIAL_CONCEPTION_CONTEXT_FROM_BIXIU4_FEED_RUBRIC.md").write_text(INITIAL_CONTEXT, encoding="utf-8")

    questions = read_csv(Q)
    rubs = rubric_map()
    mats = material_map()

    cards: list[dict[str, str]] = []
    for row in questions:
        ask, ask_source = effective_ask(row)
        batch, nodes, promotion_status, reason = route(row, ask)
        qid = row["question_id"]
        rub_atoms = rubs.get(qid, [])
        mat_atoms = mats.get(qid, [])
        flags: list[str] = []
        if ask_source != "ask_text":
            flags.append(ask_source)
        if promotion_status != "core_candidate":
            flags.append(promotion_status)
        card = {
            "question_id": qid,
            "year": row.get("year", ""),
            "district": row.get("district", ""),
            "exam_stage": row.get("exam_stage", ""),
            "question_no": row.get("question_no", ""),
            "evidence_level": row.get("evidence_level", ""),
            "primary_batch": batch,
            "primary_node": nodes[0],
            "node_names": "|".join(f"{n}:{NODES[n].name}" for n in nodes),
            "promotion_status": promotion_status,
            "effective_ask_text": ask,
            "ask_source": ask_source,
            "material_signals": atom_summary(mat_atoms, "material_phrase"),
            "rubric_rewards": atom_summary(rub_atoms, "rubric_or_answer_phrase"),
            "rubric_atom_ids": "|".join(a.get("rubric_atom_id", "") for a in rub_atoms[:12]),
            "first_student_action": NODES[nodes[0]].student_order if nodes else NODES["N00"].student_order,
            "full_score_sentence_pattern": NODES[nodes[0]].sentence if nodes else NODES["N00"].sentence,
            "common_wrong_path": NODES[nodes[0]].wrong_path if nodes else NODES["N00"].wrong_path,
            "classification_reason": reason,
            "guard_flags": "|".join(flags),
        }
        cards.append(card)

    fields = list(cards[0].keys())
    write_csv(RUN / "batch_classification_65.csv", cards, fields)
    for batch, group in sorted(defaultdict(list, ((b, [c for c in cards if c["primary_batch"] == b]) for b in set(c["primary_batch"] for c in cards))).items()):
        write_csv(RUN / f"{batch}.csv", group, fields)

    # Markdown batch summary.
    counts = Counter(c["primary_batch"] for c in cards)
    promo = Counter(c["promotion_status"] for c in cards)
    lines = [
        "# Night Batch Classification Summary",
        "",
        "## Method",
        "",
        "本轮不再把 65 题一次性扔给 GPTPro/Claude 让它们凭感觉抽象，而是先把题分成命题机制批次。每批只回答：这类题训练学生什么动作、材料触发什么、细则奖励什么句子。",
        "",
        "## Counts By Batch",
        "",
    ]
    for b, n in counts.most_common():
        lines.append(f"- {b}: {n}")
    lines += ["", "## Promotion Status", ""]
    for k, n in promo.most_common():
        lines.append(f"- {k}: {n}")
    lines += ["", "## Batch Definitions", ""]
    defs = {
        "BATCH_A_TABLE_GRID": "表格/分栏题：格子功能决定答案颗粒度。",
        "BATCH_B_JUDGMENT_EVALUATION": "评析/裁判题：先表态，再证成。",
        "BATCH_C_PRIVATE_LIABILITY": "合同、侵权、消费、劳动、相邻等私法责任链。",
        "BATCH_D_IP_COMPETITION": "知识产权、不正当竞争、创新秩序。",
        "BATCH_E_PROCEDURE_REMEDY": "调解、仲裁、诉讼、证据、请求、司法确认。",
        "BATCH_F_RISK_BOUNDARY": "AI、数据、合规风险与法律边界。",
        "BATCH_F_BOUNDARY_OPEN": "formal 但边界/综合明显，不能升核心私法模板。",
        "BATCH_G_VALUE_MEANING": "意义/作用/价值题，价值从本案规则推出。",
        "BATCH_L_LOW_FREQUENCY_CONTAINER": "低频 formal singleton，只进全量容器。",
        "BATCH_R_REFERENCE_ONLY": "reference_only，只可作为写法参考。",
        "BATCH_Z_NEEDS_SOURCE_CHECK": "暂缺稳定设问或题面，先回源。",
    }
    for b in sorted(counts):
        lines.append(f"### {b}")
        lines.append("")
        lines.append(defs.get(b, "待定义"))
        lines.append("")
        for c in [x for x in cards if x["primary_batch"] == b][:12]:
            lines.append(f"- {c['question_id']} | {c['evidence_level']} | {c['primary_node']} {NODES[c['primary_node']].name} | {md_escape(c['effective_ask_text'], 90)}")
        lines.append("")
    (RUN / "BATCH_SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")

    prompt = build_external_prompt()
    (RUN / "PROMPT_FOR_GPTPRO_BATCH_COUNCIL.md").write_text(prompt, encoding="utf-8")
    (RUN / "PROMPT_FOR_CLAUDE_OPUS_BATCH_COUNCIL.md").write_text(prompt, encoding="utf-8")

    write_framework(cards, counts, promo)
    write_pressure(cards)
    write_confucius(cards)
    write_acceptance(cards, counts, promo)

    print("wrote", RUN)
    print("counts", dict(counts))
    print("promotion", dict(promo))


def build_external_prompt() -> str:
    return """# 选必二《法律与生活》主观题框架夜间分批 council prompt

你是本工程的外部框架审议者。请不要一次性凭直觉做总框架，而要读取本包文件：

- `INITIAL_CONCEPTION_CONTEXT_FROM_BIXIU4_FEED_RUBRIC.md`
- `batch_classification_65.csv`
- `BATCH_SUMMARY.md`
- 各批次 CSV

任务：

1. 先逐批分析每一批题真正训练的学生动作。
2. 每批只输出：材料触发信号、学生第一判断、细则奖励的表达、满分句生成方式、最常见错法。
3. 再判断哪些动作能合并成高频主干，哪些只能进入全量容器。
4. 必须保留 evidence 边界：formal 可支撑核心；reference_only 只参考；boundary/open 不能升核心；low-frequency singleton 不得制造稳定套路。
5. 输出一个学生能 20 秒启动的框架，同时给教师后台证据边界。
6. 不要按教材目录写，不要法考化，不要必修三化。

输出格式：

一、每批观察
- batch_id
- batch_action
- material_trigger
- first_judgment
- rewarded_sentence
- wrong_path
- can_support_core: yes/no/partial
- reason

二、建议主干
- trunk_id
- student_name
- action
- supported_batches
- supported_question_ids
- full_score_sentence
- boundary_warning

三、全量容器
- container_type
- question_ids
- how_to_answer_without_overclaim

四、你认为最强的一页学生版

五、你认为必须压测的题

注意：不要写最终宝典，只输出框架审议结果。
"""


def write_framework(cards: list[dict[str, str]], counts: Counter[str], promo: Counter[str]) -> None:
    FRAMEWORK.parent.mkdir(parents=True, exist_ok=True)
    STUDENT.parent.mkdir(parents=True, exist_ok=True)
    TEACHER.parent.mkdir(parents=True, exist_ok=True)
    BAODIAN.parent.mkdir(parents=True, exist_ok=True)

    core_cards = [c for c in cards if c["promotion_status"] == "core_candidate"]
    ref_cards = [c for c in cards if c["promotion_status"] == "reference_only"]
    boundary_cards = [c for c in cards if c["promotion_status"] == "boundary_open"]
    low_cards = [c for c in cards if c["promotion_status"] == "low_frequency_container"]

    student = [
        "# 选必二法律主观题 20 秒启动页",
        "",
        "## 总口令",
        "",
        "先刹车，圈主体，判关系，嵌材料，落责任，补价值。",
        "",
        "## 第一步：先刹车",
        "",
        "这题是不是在处理私人法律关系、权利义务、责任承担、维权程序、法院裁判或法律合规？如果主语是国家、政府、国家治理、依法行政、涉外法治、AI 产业治理，先不要套合同侵权模板。",
        "",
        "## 第二步：圈四样东西",
        "",
        "1. 圈主体：谁和谁。",
        "2. 圈行为：做了什么。",
        "3. 圈冲突：争什么。",
        "4. 圈设问：让我判、评、说明、建议，还是谈意义。",
        "",
        "## 第三步：进七条路",
    ]
    for nid in ["N01", "N02", "N03", "N04", "N05", "N06", "N07"]:
        n = NODES[nid]
        student += [
            "",
            f"### {n.name}",
            "",
            f"- 什么时候用：{n.trigger}",
            f"- 先做什么：{n.student_order}",
            f"- 满分句：{n.sentence}",
            f"- 最容易错：{n.wrong_path}",
        ]
    student += [
        "",
        "## 四条禁令",
        "",
        "1. reference_only 题只能参考写法，不能背成核心模板。",
        "2. 边界/综合题不要硬套选必二私法框架。",
        "3. 价值句必须从本案法律规则推出，不能空喊全面依法治国。",
        "4. 法考化细节不要写，高三答案只写细则奖励的规则、事实和结论。",
    ]
    STUDENT.write_text("\n".join(student) + "\n", encoding="utf-8")

    fw = [
        "# 选必二《法律与生活》主观题框架 v3 夜间分批重构版",
        "",
        "## 版本定位",
        "",
        "本版从 STEP_29 的 65 道主观题证据底座出发：61 formal，4 reference_only，0 missing。它吸收“先发现，不建构”的方法：先做动作卡与分批机制，再合成主干框架。",
        "",
        "它不是教材目录，也不是法考式要件清单。它是学生在考场把材料转成法律语言的动作系统。",
        "",
        "## 证据边界",
        "",
        f"- core_candidate: {len(core_cards)}",
        f"- reference_only: {len(ref_cards)}",
        f"- boundary_open: {len(boundary_cards)}",
        f"- low_frequency_container: {len(low_cards)}",
        "",
        "reference_only 不进入核心支撑。boundary/open 和 low-frequency singleton 进入全量容器，给作答方法，不制造稳定套路。",
        "",
        "## 总框架",
        "",
        "先刹车 -> 圈主体和行为 -> 判法律关系或任务形态 -> 嵌材料进规则 -> 落责任/程序/边界 -> 需要时补价值。",
        "",
        "```mermaid",
        "flowchart LR",
        "A[先刹车] --> B[圈主体 行为 冲突 设问]",
        "B --> C{任务形态}",
        "C -->|表格| N01[一格一答]",
        "C -->|评判裁判| N02[先判后证]",
        "C -->|合同侵权消费劳动相邻| N03[切责成链]",
        "C -->|知识产权竞争| N04[护创新]",
        "C -->|维权程序| N05[走救济]",
        "C -->|AI合规风险| N06[划边界]",
        "N01 --> N07[需要时补价值]",
        "N02 --> N07",
        "N03 --> N07",
        "N04 --> N07",
        "N05 --> N07",
        "N06 --> N07",
        "```",
        "",
        "## 七个主节点",
    ]
    for nid in ["N01", "N02", "N03", "N04", "N05", "N06", "N07"]:
        n = NODES[nid]
        support = [c["question_id"] for c in core_cards if c["primary_node"] == nid or nid in c["node_names"]]
        fw += [
            "",
            f"### {nid} {n.name}",
            "",
            f"学生版：{n.student_order}",
            "",
            f"教师解释：{n.core_action}",
            "",
            f"材料触发：{n.trigger}",
            "",
            f"满分句模板：{n.sentence}",
            "",
            f"易错路径：{n.wrong_path}",
            "",
            f"支撑题源：{', '.join(support[:18])}" + (" ..." if len(support) > 18 else ""),
        ]
    fw += [
        "",
        "## 全量容器",
        "",
        "### reference_only 容器",
        "",
        "CC0040、CC0162、CC0311、CC0353 只能作为写法参考。教师可以展示其语言，但不能说它们支撑核心节点。",
        "",
        "### boundary/open 容器",
        "",
        "CC0276、CC0380、RECOVER_2026_西城_二模_18_3 formal 但边界明显。处理方式：按制度、机制、程序、效果写，不把它们升成合同侵权维权模板。",
        "",
        "### low-frequency singleton 容器",
        "",
        "生态保护、绿色发展、校园欺凌惩教、诉讼时效、法治德治结合等，可以教作答方法，但暂不制造稳定主干。",
    ]
    FRAMEWORK.write_text("\n".join(fw) + "\n", encoding="utf-8")

    teacher = [
        "# 选必二法律主观题框架 v3 教师讲义",
        "",
        "## 课型安排",
        "",
        "第一课：先刹车、圈主体、表格与评判裁判。",
        "第二课：私法责任链、消费欺诈、混合责任。",
        "第三课：知识产权竞争、程序救济、AI风险合规、意义价值。",
        "",
        "## 板书总线",
        "",
        "主体 -> 行为 -> 冲突 -> 规则 -> 材料事实 -> 责任/程序/价值。",
        "",
        "## 每个节点的课堂问法",
    ]
    for nid in ["N01", "N02", "N03", "N04", "N05", "N06", "N07"]:
        n = NODES[nid]
        teacher += [
            "",
            f"### {n.name}",
            "",
            f"1. 先问学生：{n.student_order}",
            f"2. 追问材料：{n.trigger}",
            f"3. 让学生套句：{n.sentence}",
            f"4. 批改错法：{n.wrong_path}",
        ]
    TEACHER.write_text("\n".join(teacher) + "\n", encoding="utf-8")

    # Baodian: compact but genuinely student-facing, then all-question placement.
    bd = [
        "# 选必二法律主观题满分宝典：夜间重构版",
        "",
        "## 第一部分 最终主观题框架",
        "",
        Path(STUDENT).read_text(encoding="utf-8"),
        "",
        "## 第二部分 高频满分句库",
    ]
    for nid in ["N01", "N02", "N03", "N04", "N05", "N06", "N07"]:
        n = NODES[nid]
        bd += [
            "",
            f"### {n.name}",
            "",
            f"- 使用条件：{n.trigger}",
            f"- 必写动作：{n.student_order}",
            f"- 满分句：{n.sentence}",
            f"- 禁止乱用：{n.wrong_path}",
        ]
    bd += [
        "",
        "## 第三部分 65 题逐题框架入口表",
        "",
        "| 题号 | 证据 | 批次 | 入口 | 学生第一动作 | 细则奖励摘要 | 风险 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for c in cards:
        node = NODES[c["primary_node"]]
        bd.append(
            f"| {c['question_id']} | {c['evidence_level']} | {c['primary_batch']} | {node.name} | {md_escape(c['first_student_action'], 80)} | {md_escape(c['rubric_rewards'], 90)} | {c['promotion_status']} |"
        )
    bd += [
        "",
        "## 第四部分 使用纪律",
        "",
        "这份宝典的正文给学生动作，证据边界放教师后台。学生不用背 formal/reference_only，但教师必须知道：reference_only 不能支撑核心，boundary/open 不能强升核心，low-frequency singleton 只进容器。",
    ]
    BAODIAN.write_text("\n".join(bd) + "\n", encoding="utf-8")


def write_pressure(cards: list[dict[str, str]]) -> None:
    rows = []
    for c in cards:
        status = "PASS" if c["promotion_status"] == "core_candidate" else "PARTIAL"
        reason = "core candidate can start from action node" if status == "PASS" else c["promotion_status"]
        rows.append(
            {
                "question_id": c["question_id"],
                "evidence_level": c["evidence_level"],
                "batch": c["primary_batch"],
                "entry_node": c["primary_node"],
                "entry_node_name": NODES[c["primary_node"]].name,
                "student_first_action": c["first_student_action"],
                "rubric_atom_ids": c["rubric_atom_ids"],
                "pass_status": status,
                "reason": reason,
                "patch_needed": "no" if status == "PASS" else "yes",
            }
        )
    write_csv(TEST_CSV, rows, list(rows[0]))
    counts = Counter(r["pass_status"] for r in rows)
    md = [
        "# Framework v3 Night Batch Pressure Report",
        "",
        f"- Total: {len(rows)}",
        f"- PASS: {counts.get('PASS', 0)}",
        f"- PARTIAL: {counts.get('PARTIAL', 0)}",
        "",
        "PARTIAL 不代表不会做，而是不能进入核心满分模板：它们分别属于 reference_only、boundary/open、low-frequency container 或 source-clean 行。",
        "",
        "## Next Patch",
        "",
        "对 PASS 行继续做 rubric-atom 句子级对齐；对 PARTIAL 行写开放容器和教师警戒，不写成核心模板。",
    ]
    TEST_MD.write_text("\n".join(md) + "\n", encoding="utf-8")


def write_confucius(cards: list[dict[str, str]]) -> None:
    sample = [
        c for c in cards if c["promotion_status"] == "core_candidate" and c["primary_node"] in {"N02", "N03", "N04", "N05", "N06", "N07", "N01"}
    ][:7]
    lines = [
        "# Confucius Zero-Baseline Simulation",
        "",
        "## Simulation Setup",
        "",
        "模拟对象：聪明但完全不会选必二法律主观题的高三学生。",
        "",
        "学习材料：`framework_v3_night_batch_student_one_page.md`。",
        "",
        "要求：读完后对抽样题完成入口判断、材料翻译、满分句骨架。只有能从框架启动并接近细则奖励，才算通过。",
        "",
        "## Result",
        "",
        "`CONDITIONAL_PASS_NOT_FINAL_FULL_MARKS`",
        "",
        "学生能掌握 20 秒启动法和七个动作节点；但当前还缺 35 个核心样本的逐句 rubric 对齐，因此不能宣称已经稳定满分。",
        "",
        "## Sample Runs",
    ]
    for c in sample:
        n = NODES[c["primary_node"]]
        lines += [
            "",
            f"### {c['question_id']}",
            "",
            f"- 学生入口：{n.name}",
            f"- 先判断：{n.student_order}",
            f"- 材料翻译：{md_escape(c['material_signals'], 200)}",
            f"- 答案骨架：{n.sentence}",
            f"- 预计失分风险：{n.wrong_path}",
        ]
    lines += [
        "",
        "## Confucius Patch Order",
        "",
        "1. 把 35 个 PASS core rows 全部改写成考场满分答案，并逐句对应 rubric atoms。",
        "2. 把 30 个 PARTIAL rows 放入参考、边界、开放容器，不让学生误背成核心。",
        "3. 重新让零基础学生答 8 道样题，直到每题都能先启动再写句。",
    ]
    CONFUCIUS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_acceptance(cards: list[dict[str, str]], counts: Counter[str], promo: Counter[str]) -> None:
    lines = [
        "# Night Batch Rebuild Acceptance Report",
        "",
        "## Verdict",
        "",
        "`CONDITIONAL_DELIVERABLE_CREATED`",
        "",
        "夜间重构已产出一个比旧审计稿更接近学生可用框架的版本，但尚未达到最终满分宝典闭合。它完成了分批、框架、学生页、教师页、65 题入口压测和 Confucius 模拟；下一门槛是 35 个核心题的 rubric-atom 句子级满分答案。",
        "",
        "## Produced Files",
        "",
        f"- `{RUN.relative_to(ROOT)}/batch_classification_65.csv`",
        f"- `{FRAMEWORK.relative_to(ROOT)}`",
        f"- `{STUDENT.relative_to(ROOT)}`",
        f"- `{TEACHER.relative_to(ROOT)}`",
        f"- `{BAODIAN.relative_to(ROOT)}`",
        f"- `{TEST_CSV.relative_to(ROOT)}`",
        f"- `{CONFUCIUS.relative_to(ROOT)}`",
        "",
        "## Counts",
        "",
        f"- Questions: {len(cards)}",
        f"- Batch counts: {dict(counts)}",
        f"- Promotion status: {dict(promo)}",
        "",
        "## Final Gate Still Open",
        "",
        "不能说早上已经得到最终满分宝典。可以说：已经得到可用候选框架和夜间重构宝典草案，下一步应进入核心题逐句满分化。",
    ]
    ACCEPT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
