#!/usr/bin/env python3
"""Build clean Phase12 dual indexes from the 77-row review-only body."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
CONTROL = BASE / "09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv"
BODY = BASE / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
THINKING_INDEX = BASE / "09_student_draft/phase12_thinking_method_index.md"
REASONING_INDEX = BASE / "09_student_draft/phase12_reasoning_typology_index.md"
SORT_KEY_MATRIX = BASE / "09_student_draft/phase12_sort_key_matrix.csv"
VERIFY = BASE / "08_review/phase12_dual_index_verification.md"


THINKING_FAMILIES = [
    {
        "name": "科学思维",
        "rule": "调查、数据、验证、规律、预测，先看是否在追求真实认识和可检验结论。",
        "trap": "不要把任何科技材料都写成创新；科学思维必须落到客观性、预见性或可检验性等具体特征。",
        "keys": ["科学思维", "客观性", "预见性", "可检验性", "探索性", "科学调查"],
    },
    {
        "name": "科学思维：客观性",
        "rule": "材料强调真实、准确、从实际出发、尊重规律，就优先看客观性。",
        "trap": "不能只写“符合科学”，要写出材料中的事实约束或客观规律。",
        "keys": ["客观性", "真实", "准确", "客观规律", "从实际出发"],
    },
    {
        "name": "科学思维：预见性",
        "rule": "材料由趋势、未来、提前研判推出行动安排，抓预见性。",
        "trap": "预见性不是空想未来，必须有现实依据和趋势判断。",
        "keys": ["预见性", "趋势", "未来", "研判", "预测", "前瞻"],
    },
    {
        "name": "科学思维：可检验性",
        "rule": "材料出现测试、验证、迭代、实践检验，就抓可检验性。",
        "trap": "不要把测试迭代泛化成创新，先看是否服务于验证结论。",
        "keys": ["可检验性", "测试", "验证", "迭代", "检验"],
    },
    {
        "name": "辩证思维",
        "rule": "多主体、多环节、整体与部分、过程变化、适度推进，进入辩证思维。",
        "trap": "不能只喊辩证思维，要下沉到整体性、动态性、分析与综合、质量互变等小方法。",
        "keys": ["辩证思维", "整体性", "动态性", "分析与综合", "质量互变", "适度", "辩证否定"],
    },
    {
        "name": "辩证思维：整体性",
        "rule": "材料把多要素、多环节作为系统来统筹，抓整体性。",
        "trap": "整体性不是把材料全部复述一遍，要写要素之间的联结和整体效果。",
        "keys": ["整体性", "整体", "系统", "统筹", "协同", "一盘棋"],
    },
    {
        "name": "辩证思维：动态性",
        "rule": "材料强调阶段、过程、长远、渐进、发展变化，抓动态性。",
        "trap": "动态性不是简单写变化，要写事物在过程中展开和推进。",
        "keys": ["动态性", "阶段", "过程", "长远", "渐进", "发展变化"],
    },
    {
        "name": "辩证思维：分析与综合",
        "rule": "材料先拆要素、再综合成整体认识或整体方案，抓分析与综合。",
        "trap": "分析与综合不是“合在一起”，必须有拆分和综合两个动作。",
        "keys": ["分析与综合", "分析", "综合", "拆", "分解"],
    },
    {
        "name": "辩证思维：质量互变",
        "rule": "材料强调由量的积累推动阶段性变化，抓质量互变。",
        "trap": "不要把任何渐进都写成质变，必须有量变积累与节点转换。",
        "keys": ["质量互变", "量变", "质变", "积累"],
    },
    {
        "name": "辩证思维：辩证否定",
        "rule": "材料对旧资源、旧模式进行保留、改造、升级，抓辩证否定。",
        "trap": "辩证否定不是否定一切，也不是只写继承。",
        "keys": ["辩证否定", "守正创新", "继承", "改造", "升级"],
    },
    {
        "name": "创新思维",
        "rule": "材料出现新思路、新方法、新结果，或打破旧路径解决问题，进入创新思维。",
        "trap": "不能只写创新思维总称，至少拆出联想、发散聚合、逆向、超前等具体方法。",
        "keys": ["创新思维", "思路新", "方法新", "结果新", "联想", "发散", "聚合", "逆向", "超前", "迁移"],
    },
    {
        "name": "创新思维：思路新、方法新、结果新",
        "rule": "材料明确呈现设计路径、解决方法和成果变化，按三新拆开写。",
        "trap": "三新不能互相替代，要让每一新都对应一个材料动作。",
        "keys": ["思路新", "方法新", "结果新", "探索性"],
    },
    {
        "name": "创新思维：联想与迁移",
        "rule": "把一个领域的经验、形象、意象、功能迁到另一个对象，抓联想或迁移。",
        "trap": "联想不是类比推理本身；要写清被迁移的经验和新对象。",
        "keys": ["联想", "迁移", "想象", "同化性迁移", "意象"],
    },
    {
        "name": "创新思维：发散与聚合",
        "rule": "先打开多方案，再收束成可行方案，抓发散与聚合。",
        "trap": "只列很多方案是发散，不等于完成聚合。",
        "keys": ["发散", "聚合", "多方案", "收束"],
    },
    {
        "name": "创新思维：逆向思维",
        "rule": "把关系、顺序、方向、功能反过来思考，抓逆向思维。",
        "trap": "逆向不是唱反调，要服务于解决问题。",
        "keys": ["逆向", "反向", "从“人找书”向“书找人”", "书找人"],
    },
    {
        "name": "创新思维：超前思维",
        "rule": "由现实依据推断未来趋势，并提前布局，抓超前思维。",
        "trap": "超前思维必须有调查、预测和行动安排，不能只写想得远。",
        "keys": ["超前", "前瞻", "未来产业", "提前布局"],
    },
    {
        "name": "认识发展历程：感性具体、思维抽象、思维具体",
        "rule": "杂多现象 -> 抽出本质 -> 回到完整整体图景。",
        "trap": "看到“合、融、整体”不要自动选系统整合；先判断是不是认识深化链。",
        "keys": ["感性具体", "思维抽象", "思维具体", "认识发展的历程", "认识历程"],
    },
    {
        "name": "形象思维与抽象思维",
        "rule": "形象、画面、感性表达对应形象思维；概念、判断、推理对应抽象思维。",
        "trap": "不要把形象表达直接等同于低级思维，关键看思维基本单元。",
        "keys": ["形象思维", "抽象思维", "感性形象", "概念"],
    },
]


REASONING_FAMILIES = [
    {
        "name": "概念与定义",
        "rule": "下定义按“被定义项 + 联结词 + 种差 + 邻近属”。",
        "trap": "定义过宽、定义过窄、循环定义、比喻定义、否定定义。",
        "keys": ["下定义", "被定义项", "联结词", "种差", "邻近属", "定义过宽", "定义"],
    },
    {
        "name": "概念外延关系",
        "rule": "先判断两个概念是否相容，再判全同、属种、种属、交叉或不相容。",
        "trap": "把集合成员、空间隶属、特征描述误判为种属关系。",
        "keys": ["外延", "种属", "属种", "相容关系", "反对关系", "交叉", "全同"],
    },
    {
        "name": "判断类型识别",
        "rule": "看判断断定的是性质、关系、联结、选择还是条件。",
        "trap": "把关系判断误判成性质判断，把选言判断误判成联言判断。",
        "keys": ["判断", "关系判断", "性质判断", "联言判断", "选言判断", "假言判断"],
    },
    {
        "name": "联言判断与联言推理",
        "rule": "联言判断全真才真，一假即假；可以由合取到各支，也可以由各支合成。",
        "trap": "把部分真当整体真，或把联言支的顺序当因果。",
        "keys": ["联言", "合取", "全真才真", "一假即假"],
    },
    {
        "name": "相容选言推理",
        "rule": "相容选言可以同时真；否定一支可肯定另一支，肯定一支不能否定另一支。",
        "trap": "把相容选言当不相容选言处理。",
        "keys": ["相容选言", "可以同时", "否定一支", "肯定一支"],
    },
    {
        "name": "不相容选言推理",
        "rule": "不相容选言只能有一支为真；肯定一支可否定另一支，否定一支可肯定另一支。",
        "trap": "看到“要么”要警惕不相容选择，不要写成相容选言。",
        "keys": ["不相容选言", "要么", "只能有一", "二者不可兼得"],
    },
    {
        "name": "充分条件假言推理",
        "rule": "肯定前件、否定后件有效；肯定后件、否定前件无效。",
        "trap": "后件为真不能倒推出前件必真。",
        "keys": ["充分条件", "若", "如果", "后件为真", "肯定后件", "否定前件"],
    },
    {
        "name": "必要条件假言推理",
        "rule": "否定前件、肯定后件有效；肯定前件、否定后件无效。",
        "trap": "把必要条件当充分条件，最容易把“只有才”倒推错。",
        "keys": ["必要条件", "只有", "才", "否定前件", "肯定后件"],
    },
    {
        "name": "假言推理综合题",
        "rule": "先翻译条件关系，再逐条检查有效式和无效式。",
        "trap": "多个条件叠加时，不要跳步推出题目没有给出的结论。",
        "keys": ["假言推理", "条件假言", "前件", "后件", "推出"],
    },
    {
        "name": "三段论结构题",
        "rule": "找大项、小项、中项，再看中项是否至少周延一次、结论项是否不被扩大。",
        "trap": "中项不周延、大项扩大、小项扩大、四概念。",
        "keys": ["三段论", "中项", "大项", "小项", "周延", "四概念"],
    },
    {
        "name": "逻辑三律",
        "rule": "同一律管偷换概念，矛盾律管不能同真，排中律管不能同假。",
        "trap": "把矛盾关系与反对关系混同，把排中律误用到可同时假的命题。",
        "keys": ["同一律", "矛盾律", "排中律", "思维必须合乎逻辑"],
    },
    {
        "name": "归纳推理",
        "rule": "从个别到一般，结论具有或然性；样本越有代表性越可靠。",
        "trap": "把不完全归纳写成必然推理。",
        "keys": ["归纳", "完全归纳", "不完全归纳", "样本", "或然"],
    },
    {
        "name": "求同法、求异法、共变法、剩余法",
        "rule": "看变量怎样同在、相异、同步变化或被排除剩余。",
        "trap": "只看到相关不等于因果，必须看题目给出的变量控制。",
        "keys": ["求同法", "求异法", "共变法", "剩余法", "变量"],
    },
    {
        "name": "类比推理",
        "rule": "由两个对象相似属性迁移到新属性，结论是或然的。",
        "trap": "相似点越表面，类比越弱；不能把类比当必然证明。",
        "keys": ["类比", "相似", "相似属性", "迁移边界"],
    },
    {
        "name": "论证评价与逻辑错误",
        "rule": "先找论点、论据和论证方式，再查偷换概念、越级划分、以偏概全等错误。",
        "trap": "不要只背错误名，要说明错在材料的哪一步。",
        "keys": ["论证", "逻辑错误", "越级划分", "划分", "定义过宽", "犯了"],
    },
    {
        "name": "复合推理与综合方法链",
        "rule": "一题有多个条件或多个逻辑动作时，先分解再合并结论。",
        "trap": "不能把综合链压成单一题型；要逐步写出每个推理动作。",
        "keys": ["综合方法链", "复合", "多个条件", "逐步", "链条"],
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", text, re.M))
    out: dict[str, str] = {}
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
        out[title] = body
    return out


def match_families(text: str, families: list[dict[str, object]]) -> list[str]:
    hits: list[str] = []
    for family in families:
        keys = family["keys"]
        if any(key in text for key in keys):  # type: ignore[union-attr]
            hits.append(str(family["name"]))
    return hits


def entry_line(row: dict[str, str]) -> str:
    return f"- 第{row['order']}条：{row['visible_title']}（正文位置：{row['question_type_group']} / {row['district']} / {row['year']} / {row['exam_stage']}）"


def render_index(
    title: str,
    status: str,
    intro: str,
    families: list[dict[str, object]],
    index_map: dict[str, list[dict[str, str]]],
) -> str:
    parts = [f"# {title}", "", f"Status: `{status}`", "", intro, ""]
    total_links = 0
    for family in families:
        name = str(family["name"])
        rows = index_map.get(name, [])
        parts.append(f"## {name}")
        parts.append("")
        parts.append(f"- 规则口令：{family['rule']}")
        parts.append(f"- 常见陷阱：{family['trap']}")
        parts.append(f"- 正文挂载数：{len(rows)}")
        parts.append("")
        if rows:
            parts.append("### 全部同类题清单")
            parts.append("")
            for row in rows:
                parts.append(entry_line(row))
                total_links += 1
            parts.append("")
        else:
            parts.append("本轮 77 条 review-only 正文中暂未挂载该家庭；不得为了凑索引而扩写未入正文题。")
            parts.append("")
    parts.append("## 索引核验")
    parts.append("")
    parts.append(f"- 索引挂载总数：{total_links}")
    parts.append("- 只索引已入 77 条 review-only 正文的题，不扩写 blocked 或 index-only 题。")
    parts.append("- 正文排序仍按用户规则执行；本索引用于方法/题型反查。")
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    rows = read_csv(CONTROL)
    sections = parse_sections(BODY.read_text(encoding="utf-8"))

    thinking_map: dict[str, list[dict[str, str]]] = defaultdict(list)
    reasoning_map: dict[str, list[dict[str, str]]] = defaultdict(list)
    unindexed_thinking: list[str] = []
    unindexed_reasoning: list[str] = []

    for row in rows:
        text = row["visible_title"] + "\n" + sections.get(row["visible_title"], "")
        thinking_hits = match_families(text, THINKING_FAMILIES)
        reasoning_hits = match_families(text, REASONING_FAMILIES)

        if row["module"] == "思维" or (row["module"] == "交叉" and thinking_hits):
            if not thinking_hits:
                unindexed_thinking.append(row["visible_title"])
            for hit in thinking_hits:
                thinking_map[hit].append(row)
        if row["module"] == "推理" or (row["module"] == "交叉" and reasoning_hits):
            if not reasoning_hits:
                unindexed_reasoning.append(row["visible_title"])
            for hit in reasoning_hits:
                reasoning_map[hit].append(row)

    THINKING_INDEX.write_text(
        render_index(
            "Phase12 思维方法索引",
            "REVIEW_ONLY_NO_WORD_NO_FINAL",
            "本索引把 77 条 review-only 正文中已经入正文的思维题、交叉题按方法反挂，方便从“方法”回到“题”。它不收 blocked 题，也不把索引当正文覆盖。",
            THINKING_FAMILIES,
            thinking_map,
        ),
        encoding="utf-8",
    )
    REASONING_INDEX.write_text(
        render_index(
            "Phase12 推理题型索引",
            "REVIEW_ONLY_NO_WORD_NO_FINAL",
            "本索引把 77 条 review-only 正文中已经入正文的推理题、交叉题按题型反挂，保证推理部分不是只放代表例。它只索引已入正文题，不替 blocked 题补答案。",
            REASONING_FAMILIES,
            reasoning_map,
        ),
        encoding="utf-8",
    )

    sort_rows = [
        {
            "question_id": row["question_id"],
            "visible_title": row["visible_title"],
            "question_type_group": row["question_type_group"],
            "district": row["district"],
            "year": row["year"],
            "exam_stage": row["exam_stage"],
            "question_no": row["question_no"],
            "subquestion_no": row["subquestion_no"],
            "sort_key": row["sort_key"],
            "phase12_decision": row["phase12_decision"],
        }
        for row in rows
    ]
    write_csv(
        SORT_KEY_MATRIX,
        sort_rows,
        [
            "question_id",
            "visible_title",
            "question_type_group",
            "district",
            "year",
            "exam_stage",
            "question_no",
            "subquestion_no",
            "sort_key",
            "phase12_decision",
        ],
    )

    thinking_links = sum(len(v) for v in thinking_map.values())
    reasoning_links = sum(len(v) for v in reasoning_map.values())
    verify = [
        "# Phase12 Dual Index Verification",
        "",
        "Status: `DUAL_INDEX_BUILT_REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "",
        f"- expanded body rows: {len(rows)}",
        f"- sort-key matrix rows: {len(sort_rows)}",
        f"- thinking index families: {len(THINKING_FAMILIES)}",
        f"- thinking index links: {thinking_links}",
        f"- reasoning index families: {len(REASONING_FAMILIES)}",
        f"- reasoning index links: {reasoning_links}",
        f"- thinking rows without keyword family: {len(unindexed_thinking)}",
        f"- reasoning rows without keyword family: {len(unindexed_reasoning)}",
        "",
        "## Outputs",
        "",
        f"- `{THINKING_INDEX.relative_to(BASE)}`",
        f"- `{REASONING_INDEX.relative_to(BASE)}`",
        f"- `{SORT_KEY_MATRIX.relative_to(BASE)}`",
        "",
        "## Remaining Gate",
        "",
        "- 索引已经生成，但仍是 review-only。",
        "- Word/PDF/final 仍需 Codex/ClaudeCode/GPT/Governor/Confucius 后续验收。",
    ]
    if unindexed_thinking:
        verify.extend(["", "## Thinking Rows Needing Manual Index Review", ""])
        verify.extend(f"- {title}" for title in unindexed_thinking)
    if unindexed_reasoning:
        verify.extend(["", "## Reasoning Rows Needing Manual Index Review", ""])
        verify.extend(f"- {title}" for title in unindexed_reasoning)
    VERIFY.write_text("\n".join(verify).rstrip() + "\n", encoding="utf-8")

    print(f"thinking_links: {thinking_links}")
    print(f"reasoning_links: {reasoning_links}")
    print(f"unindexed_thinking: {len(unindexed_thinking)}")
    print(f"unindexed_reasoning: {len(unindexed_reasoning)}")


if __name__ == "__main__":
    main()
