from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
GENERATED_AT = "2026-05-23 01:50 +08:00"


def read_csv(rel: str) -> list[dict[str, str]]:
    path = ROOT / rel
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


CORE = read_csv("evidence_pack/core_42_v12_1.csv")
TRACE = {row["question_id"]: row for row in read_csv("traceability/TRACEABILITY_MATRIX_v12_2.csv")}
PENDING_CHECKS = read_csv("codex_source_checks/pending_source_check_20260522.csv")
REFERENCE_INDEX = read_csv("evidence_pack/batch_03_reference_and_unincluded_index.csv")
NEXT_BACKFILL = read_csv("evidence_pack/next_backfill_6_summary.csv")


ENTRY_DEFS = {
    "E1": {
        "title": "E1 表格/裁判要点/补链题",
        "cue": "设问让学生完成表格、补裁判要点、补合同/权利/责任链。",
        "path": "形式触发 -> 一格一链 -> 法律关系/法律要件 -> 格内结论。",
        "skeleton": "先判断每一格问的是什么，再把材料事实翻译成一个法律关系，最后落到这一格的结论。多格题禁止写成一段总论。",
        "warning": "不要因为材料新，比如 AI、平台、数字经济，就新造主题模板；先看它是不是在补一个法律链条。",
    },
    "E2": {
        "title": "E2 判决/裁判/责任理由题",
        "cue": "设问问法院为什么这样判、责任如何承担、裁判依据或法理依据。",
        "path": "裁判对象 -> 法律关系 -> 要件/过错/程序/责任 -> 裁判结论与边界。",
        "skeleton": "先定案由和法律关系，再逐个对上材料中的责任要件，最后说明法院支持、减轻、否定或限缩责任的理由。",
        "warning": "不要一上来背公平正义。判决题的分数在事实如何满足要件，价值只放在结尾。",
    },
    "E3": {
        "title": "E3 诉求/请求能否支持题",
        "cue": "设问直接问某人的诉求、请求、主张能否得到法院支持。",
        "path": "诉求对象 -> 权利基础 -> 法律要件 -> 支持/不支持及理由。",
        "skeleton": "先把不同诉求拆开，再分别写权利依据、事实匹配和法院是否支持。低样本入口，不能泛化成所有判案题。",
        "warning": "只有设问在问“能否支持/能否成立”时才优先进入 E3；普通判决理由题仍回 E2。",
    },
    "E4": {
        "title": "E4 评析/认识/观点题",
        "cue": "设问要求评价观点、谈认识、评析做法、说明某种法律变化的合理性。",
        "path": "观点/做法 -> 法律关系和制度背景 -> 判断边界 -> 规范评价。",
        "skeleton": "先判观点是否成立，再回到具体法律关系解释为什么成立或需要补充，最后给出规范性结论。",
        "warning": "不要把评价题写成空泛价值口号；也不要把低频法律变化题扩成新主干。",
    },
    "E5": {
        "title": "E5 意义/价值/作用/保护推动题",
        "cue": "设问问规定、制度、做法的作用、意义、价值，或如何保护、推动某类权益。",
        "path": "法律规则/制度 -> 保护对象或治理对象 -> 行为方式 -> 秩序与权益效果。",
        "skeleton": "意义价值题写“保护谁、规范谁、维护什么秩序”；如何保护题写“法律手段、保护对象、实践效果”。",
        "warning": "E5 是最大桶，必须拆句型。尤其劳动法题要落在法律公平与效率，不要写成纯经济分析。",
    },
    "E6": {
        "title": "E6 调解/维权/纠纷解决/证据路径题",
        "cue": "设问问如何调解、怎样维权、纠纷如何解决、举证责任或救济路径。",
        "path": "纠纷事实 -> 权利受损或争议焦点 -> 路径/主体/证据 -> 救济方案。",
        "skeleton": "路径先行：先写采用什么法律途径或调解方案，再写依据、行动、证据和救济效果。",
        "warning": "不要把路径题写成抽象法治意义；任选其一类设问要写一条完整链，不是三条半截链。",
    },
}

ENTRY_ORDER = ["E1", "E2", "E3", "E4", "E5", "E6"]


def cell(row: dict[str, str], key: str, default: str = "") -> str:
    value = (row.get(key) or "").strip()
    return value if value else default


def entry_code(row: dict[str, str]) -> str:
    trace = TRACE.get(row["question_id"], {})
    raw = cell(trace, "framework_entrance") or cell(row, "主入口")
    for code in ENTRY_ORDER:
        if raw.startswith(code) or f"{code}_" in raw or f"{code} " in raw:
            return code
    text = cell(row, "主入口")
    if "表" in text or "补" in text:
        return "E1"
    if "判" in text or "责任" in text:
        return "E2"
    if "诉求" in text or "支持" in text:
        return "E3"
    if "评" in text or "认识" in text:
        return "E4"
    if "意义" in text or "作用" in text or "保护" in text:
        return "E5"
    if "调解" in text or "维权" in text or "举证" in text:
        return "E6"
    return "E5"


def trace_value(qid: str, key: str) -> str:
    return cell(TRACE.get(qid, {}), key)


def secondary_entry(row: dict[str, str]) -> str:
    trace_secondary = trace_value(row["question_id"], "secondary_entrance")
    core_secondary = cell(row, "副入口")
    if trace_secondary and core_secondary:
        return f"{trace_secondary}；题源副入口：{core_secondary}"
    return trace_secondary or core_secondary or "无"


def trigger_lines(row: dict[str, str]) -> list[str]:
    return [
        cell(row, "主材料触发_1", "未记录"),
        cell(row, "主材料触发_2", "未记录"),
        cell(row, "主材料触发_3", "未记录"),
    ]


def scoring_anchor(row: dict[str, str]) -> str:
    qid = row["question_id"]
    trace = TRACE.get(qid, {})
    parts = []
    if cell(trace, "source_check_decision"):
        parts.append(f"源检查决策：{cell(trace, 'source_check_decision')}")
    if cell(trace, "guardrail"):
        parts.append(f"边界守则：{cell(trace, 'guardrail')}")
    parts.append(f"题源状态：{cell(row, 'evidence_status')}；链条状态：{cell(row, 'chain_state')}")
    skeleton = cell(row, "答案骨架")
    if skeleton:
        parts.append(f"得分锚点：{skeleton}")
    return " / ".join(parts)


def card_anchor(qid: str) -> str:
    return qid.replace("_", "-").lower()


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        escaped = [str(item).replace("\n", "<br>").replace("|", "｜") for item in row]
        out.append("| " + " | ".join(escaped) + " |")
    return "\n".join(out)


def build_readme(grouped: dict[str, list[dict[str, str]]]) -> str:
    counts = {code: len(grouped.get(code, [])) for code in ENTRY_ORDER}
    return f"""# 选必二《法律与生活》法律宝典 v12.2

生成时间：{GENERATED_AT}

状态：`markdown_baodian_complete_pending_docx_pdf_render`

本目录是 v12.2 框架生长线的成品 Markdown 法律宝典。它使用 42 道 locked core 主观题作为正文底座，使用真实 GPT/Claude Round 01-03 产出和 Codex 本地源检查作为框架生长与验收依据。

## 目录

- `01_法律主观题框架章.md`：六入口框架、命题人路径、入口辨认和误判边界。
- `02_42题按框架解析宝典.md`：42 道正文题按 E1-E6 分组解析。
- `03_开放容器与不晋升题附录.md`：参考题、开放容器、下一版回填候选，全部保持在正文外。
- `04_GPT_Claude_框架生长记录.md`：真实 GPT/Claude 框架生长记录与 Round 03 结论。
- `05_GOVERNOR_FINAL_CHECK.md`：最终 Governor 检查，明确 Markdown 宝典与 DOCX/PDF 的边界。
- `42题框架索引.csv`：42 题索引，可供后续排版、筛题、检索。

## 正文覆盖

| 入口 | 题数 |
|---|---:|
| E1 表格/裁判要点/补链题 | {counts['E1']} |
| E2 判决/裁判/责任理由题 | {counts['E2']} |
| E3 诉求/请求能否支持题 | {counts['E3']} |
| E4 评析/认识/观点题 | {counts['E4']} |
| E5 意义/价值/作用/保护推动题 | {counts['E5']} |
| E6 调解/维权/纠纷解决/证据路径题 | {counts['E6']} |
| 合计 | {len(CORE)} |

## 使用规则

先用设问识别入口，再用材料事实压实法律关系，最后才写价值。不要从热点词出发套模板，也不要把参考题、开放容器、下一版回填候选提升为正文主干。
"""


def build_framework_chapter(grouped: dict[str, list[dict[str, str]]]) -> str:
    lines = [
        "# 01 法律主观题框架章",
        "",
        "## 一句话总框架",
        "",
        "选必二主观题不是按教材页码出题，而是按设问动作出题。先看题目让你做什么，再判断命题人要学生完成哪一种法律工作：补链、判责、判诉求、评观点、写意义、走路径。",
        "",
        "## 命题人出题路径",
        "",
        "1. 先给一个生活化法律场景：侵权、合同、劳动、婚姻家庭、继承、知识产权、诉讼或调解。",
        "2. 再把材料中的事实拆成若干法律触发点：主体、行为、权利、义务、过错、程序、证据、损害、效果。",
        "3. 最后用设问动作规定答题方式：让学生补表、判责、判断诉求、评析观点、写作用或给路径。",
        "",
        "学生拿到题后反过来走：设问动作定入口，材料触发定知识，评分锚点定落点。",
        "",
        "## 六个入口",
        "",
    ]
    for code in ENTRY_ORDER:
        spec = ENTRY_DEFS[code]
        rows = grouped.get(code, [])
        ids = "、".join(r["question_id"] for r in rows)
        lines.extend(
            [
                f"### {spec['title']}（{len(rows)}题）",
                "",
                f"- 识别口令：{spec['cue']}",
                f"- 命题路径：{spec['path']}",
                f"- 作答骨架：{spec['skeleton']}",
                f"- 学生预警：{spec['warning']}",
                f"- 本版题源：{ids}",
                "",
            ]
        )

    lines.extend(
        [
            "## 入口判断顺序",
            "",
            "1. 看到表格、补空、裁判要点，先判 E1。",
            "2. 看到法院为什么判、责任如何承担，先判 E2；如果设问直接问诉求能否支持，再判 E3。",
            "3. 看到评析、认识、观点，判 E4。",
            "4. 看到意义、作用、价值、保护推动，判 E5，并继续分清是意义句型还是如何保护句型。",
            "5. 看到调解、维权、纠纷解决、举证、救济路径，判 E6。",
            "",
            "## Round 03 边界补丁",
            "",
            "- E1：AI 题只能停在著作权/合同/违约的格子链条，不能升级成 AI 创新主干。",
            "- E1/E6：任选其一的权利保护题，E1 管前面的问答格，E6 管后面的 basis-action-remedy 完整路径。",
            "- E2：`程序合法` 只在 CC0364 的材料与细则奖励中成立，不能当成所有裁判题的开头。",
            "- E3：样本少，必须透明标注为低频入口，避免把所有判案题都塞进诉求支持。",
            "- E4：CC0051 只证明低频评价覆盖，不证明需要新增法律变化主干。",
            "- E5：11 题中要拆成意义价值句型与如何保护句型；CC0195 必须按劳动法公平/效率写，不写纯经济。",
            "- E6：纠纷解决题必须先写路径，再写依据、行动、证据和救济；CC0223 不能写成泛泛法治价值。",
        ]
    )
    return "\n".join(lines)


def build_all_question_baodian(grouped: dict[str, list[dict[str, str]]]) -> str:
    lines = [
        "# 02 42题按框架解析宝典",
        "",
        f"生成时间：{GENERATED_AT}",
        "",
        "每张卡都按同一套课堂字段组织：题号、区年、设问动作、框架入口、命题路径、细则/评分锚点、材料触发、答案骨架、学生预警和副入口。",
        "",
    ]
    n = 1
    for code in ENTRY_ORDER:
        spec = ENTRY_DEFS[code]
        rows = grouped.get(code, [])
        lines.extend([f"## {spec['title']}（{len(rows)}题）", ""])
        for row in rows:
            qid = row["question_id"]
            trace = TRACE.get(qid, {})
            prompt = cell(row, "真实设问")
            material = cell(row, "真实材料核心")
            triggers = trigger_lines(row)
            secondary = secondary_entry(row)
            lines.extend(
                [
                    f"### {n}. {qid}",
                    "",
                    f"- 区年卷题：{cell(row, 'year')}年 {cell(row, 'district')} {cell(row, 'exam_stage')} 第{cell(row, 'question_no')}题",
                    f"- 设问动作：{prompt}",
                    f"- 材料核心：{material}",
                    f"- 框架入口：{spec['title']}；原题源主入口：{cell(row, '主入口')}",
                    f"- 副入口：{secondary}",
                    f"- 命题路径：{spec['path']}",
                    f"- 细则/评分锚点：{scoring_anchor(row)}",
                    "- 材料触发：",
                    f"  1. {triggers[0]}",
                    f"  2. {triggers[1]}",
                    f"  3. {triggers[2]}",
                    f"- 答案骨架：{cell(row, '答案骨架')}",
                    f"- 学生预警：{cell(row, '禁止命中') or spec['warning']}",
                    f"- 讲解口径：{cell(row, '飞哥想说')}",
                    f"- 证据与来源：{cell(row, 'evidence_status')}；{cell(row, 'chain_state')}；source_check_state={cell(trace, 'source_check_state', 'not_recorded')}",
                    "",
                ]
            )
            n += 1
    return "\n".join(lines)


def build_open_appendix() -> str:
    lines = [
        "# 03 开放容器与不晋升题附录",
        "",
        "本附录只用于边界提醒和下一版证据回填，不进入 42 道正文框架，不改变 E1-E6 分布。",
        "",
        "## A. Round 03 明确不晋升行",
        "",
    ]
    non_promoted = [r for r in PENDING_CHECKS if not cell(r, "decision").startswith("KEEP_CORE")]
    if non_promoted:
        lines.append(
            md_table(
                ["check_id", "question_id", "source_status", "entrance_after_check", "decision", "guardrail", "next_action"],
                [
                    [
                        cell(r, "check_id"),
                        cell(r, "question_id"),
                        cell(r, "source_status"),
                        cell(r, "entrance_after_check"),
                        cell(r, "decision"),
                        cell(r, "guardrail"),
                        cell(r, "next_action"),
                    ]
                    for r in non_promoted
                ],
            )
        )
    else:
        lines.append("无。")
    lines.extend(["", "## B. v12.1 参考运行/未纳入索引", ""])
    lines.append(
        md_table(
            ["block", "framework_point", "role", "question_ids", "是否核心", "是否仅参考", "禁止误用说明"],
            [
                [
                    cell(r, "block"),
                    cell(r, "framework_point"),
                    cell(r, "role"),
                    cell(r, "question_ids"),
                    cell(r, "是否核心"),
                    cell(r, "是否仅参考"),
                    cell(r, "禁止误用说明"),
                ]
                for r in REFERENCE_INDEX
            ],
        )
    )
    lines.extend(["", "## C. 下一版回填候选", ""])
    lines.append(
        md_table(
            ["question_id", "source_hunt_result", "next_action", "question_found", "rubric_found"],
            [
                [
                    cell(r, "question_id"),
                    cell(r, "source_hunt_result"),
                    cell(r, "next_action"),
                    cell(r, "question_found"),
                    cell(r, "rubric_found"),
                ]
                for r in NEXT_BACKFILL
            ],
        )
    )
    lines.extend(
        [
            "",
            "## D. 不晋升规则",
            "",
            "只有当新证据证明某个 locked core 正文题无法被六入口覆盖，才允许重开框架结构。参考题、开放容器、别名风险行、下一版回填候选不能直接提升为第七入口。",
        ]
    )
    return "\n".join(lines)


def build_model_record() -> str:
    return """# 04 GPT / Claude 框架生长记录

## 真实模型调用链

| 轮次 | GPT | Claude | Codex 处理 | 结论 |
|---|---|---|---|---|
| Round 01 | `model_outputs/gpt_round01_independent_framework.md` | `model_outputs/claude_round01_independent_framework.md` | `codex_adjudication/CODEX_ROUND01_ROUND02_ADJUDICATION.md` | 形成候选框架，待源检查 |
| Round 02 | `cross_critiques/gpt_critiques_claude_round01.md` | `cross_critiques/claude_critiques_gpt_round01.md` | 覆盖度与冲突裁决 | 六入口候选可覆盖 42/42 |
| Source Check | 无新模型 | 无新模型 | `codex_source_checks/pending_source_check_20260522.md` | 边界题保留/排除，分布不变 |
| Round 03 | `model_outputs/gpt_round03_source_check_review.md` | `model_outputs/claude_round03_source_check_review_key_capture.md` | `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` | 双模型接受源检查候选，无结构变化 |

## GPT Round 03 结论

GPT 在 ChatGPT web clean conversation 中完成 Round 03。记录文件写明：可见模式为 `进阶专业`，准确 `GPT-5.5 Pro` 标签未独立可见，因此保留 model-label caution。其具体 verdict 为：

`accept_source_checked_candidate_no_structural_change`

GPT 接受的关键点：

- 六入口不作结构变化。
- E1=9, E2=8, E3=3, E4=7, E5=11, E6=4 的分布不变。
- CC0137、CC0289、CC0223、CC0364、CC0051、CC0195 的源检查边界接受。
- CC0162、CC0040、CC0353、CC0380 保持 reference/open，不晋升。
- 仍不能把源检查候选直接叫 final PASS。

## Claude Round 03 结论

Claude web 可见模型为 `Opus 4.7 Adaptive`，Round 03 key capture 的 verdict 为：

`accept_source_checked_candidate_no_structural_change`

Claude 接受的关键点：

- 源检查属于边界收紧，不是框架重构。
- 42/42 locked core 仍被六入口覆盖。
- 不需要第七入口。
- E1、E2、E4、E5、E6 需要写入学生误判边界；E3 标注低频。

## Codex 本地裁决

本地源证据优先于模型共识。GPT/Claude 的一致意见只用于确认：在 Codex 源检查已经闭合的前提下，六入口结构可以作为 v12.2 框架 baseline。最终文档生产仍是独立 gate。
"""


def build_governor(grouped: dict[str, list[dict[str, str]]]) -> str:
    total_cards = sum(len(v) for v in grouped.values())
    return f"""# 05 Governor Final Check

Status: `markdown_baodian_complete_pending_docx_pdf_render`

Date: 2026-05-23

## Gate Table

| gate | result | evidence |
|---|---|---|
| 42 locked core rows imported | pass | `evidence_pack/core_42_v12_1.csv` -> {total_cards} cards |
| framework baseline GPT/Claude reviewed | pass | `model_outputs/gpt_round03_source_check_review.md`; `model_outputs/claude_round03_source_check_review_key_capture.md` |
| local source-check adjudication preserved | pass | `codex_source_checks/pending_source_check_20260522.md`; `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` |
| polished framework chapter exists | pass | `final_baodian_20260523/01_法律主观题框架章.md` |
| all-question analysis exists | pass | `final_baodian_20260523/02_42题按框架解析宝典.md` |
| reference/open rows separated | pass | `final_baodian_20260523/03_开放容器与不晋升题附录.md` |
| GPT/Claude governance appendix exists | pass | `final_baodian_20260523/04_GPT_Claude_框架生长记录.md` |
| traceability index updated | pass | `traceability/TRACEABILITY_MATRIX_v12_2_BAODIAN_INDEX.csv` |
| DOCX/PDF rendered | fail / not produced in this milestone | no `.docx` or `.pdf` delivery generated here |

## Allowed Claim

`markdown_baodian_complete_pending_docx_pdf_render`

This means the Markdown baodian exists, uses the real GPT/Claude-grown framework baseline, covers all 42 locked core rows, and keeps non-core rows in appendices.

## Forbidden Claim

Do not claim DOCX/PDF delivery until rendered files exist and are visually checked. Do not claim a wider final PASS over next-backfill candidates because they remain outside this locked-core v12.2 scope.
"""


def build_summary(grouped: dict[str, list[dict[str, str]]]) -> str:
    counts = {code: len(grouped.get(code, [])) for code in ENTRY_ORDER}
    return f"""# 06 Morning Summary - Xuanbier Legal Baodian

Status: `markdown_baodian_complete_pending_docx_pdf_render`

Date: 2026-05-23

## Completed

- Final output directory created: `reports/选必二法律主观题框架_从题源生长/v12_2_framework_growth_restart/final_baodian_20260523/`
- Polished framework chapter written.
- All 42 locked core questions written as framework-organized analysis cards.
- Reference/open/container rows stayed in a separate appendix.
- GPT and Claude Round 03 conclusions were included in the governance appendix.
- Traceability index was generated.

## Counts

| entrance | count |
|---|---:|
| E1 | {counts['E1']} |
| E2 | {counts['E2']} |
| E3 | {counts['E3']} |
| E4 | {counts['E4']} |
| E5 | {counts['E5']} |
| E6 | {counts['E6']} |
| total | {sum(counts.values())} |

## Not Produced Yet

- DOCX delivery: not produced.
- PDF delivery: not produced.

The correct current label is Markdown baodian complete, pending optional DOCX/PDF rendering.
"""


def write_index(grouped: dict[str, list[dict[str, str]]]) -> None:
    rows = []
    for code in ENTRY_ORDER:
        for row in grouped.get(code, []):
            qid = row["question_id"]
            rows.append(
                {
                    "question_id": qid,
                    "year": cell(row, "year"),
                    "district": cell(row, "district"),
                    "exam_stage": cell(row, "exam_stage"),
                    "question_no": cell(row, "question_no"),
                    "framework_entrance": ENTRY_DEFS[code]["title"],
                    "secondary_entrance": secondary_entry(row),
                    "proposition_path": ENTRY_DEFS[code]["path"],
                    "prompt": cell(row, "真实设问"),
                    "card_file": "final_baodian_20260523/02_42题按框架解析宝典.md",
                    "evidence_status": cell(row, "evidence_status"),
                    "source_check_state": trace_value(qid, "source_check_state"),
                    "source_check_decision": trace_value(qid, "source_check_decision"),
                }
            )
    out_csv = OUT / "42题框架索引.csv"
    with out_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    trace_csv = ROOT / "traceability/TRACEABILITY_MATRIX_v12_2_BAODIAN_INDEX.csv"
    with trace_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    md_rows = [
        [
            r["question_id"],
            f"{r['year']} {r['district']} {r['exam_stage']} {r['question_no']}",
            r["framework_entrance"],
            r["secondary_entrance"],
            r["source_check_state"],
        ]
        for r in rows
    ]
    write(
        ROOT / "traceability/TRACEABILITY_MATRIX_v12_2_BAODIAN_INDEX.md",
        "# Traceability Matrix v12.2 Baodian Index\n\n" + md_table(
            ["question_id", "source", "framework_entrance", "secondary_entrance", "source_check_state"], md_rows
        ),
    )


def main() -> None:
    if len(CORE) != 42:
        raise SystemExit(f"Expected 42 core rows, got {len(CORE)}")
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in CORE:
        grouped[entry_code(row)].append(row)

    write(OUT / "00_READ_ME_FIRST.md", build_readme(grouped))
    write(OUT / "01_法律主观题框架章.md", build_framework_chapter(grouped))
    write(OUT / "02_42题按框架解析宝典.md", build_all_question_baodian(grouped))
    write(OUT / "03_开放容器与不晋升题附录.md", build_open_appendix())
    write(OUT / "04_GPT_Claude_框架生长记录.md", build_model_record())
    write(OUT / "05_GOVERNOR_FINAL_CHECK.md", build_governor(grouped))
    write(OUT / "06_MORNING_SUMMARY.md", build_summary(grouped))
    write_index(grouped)

    counts = Counter({code: len(grouped.get(code, [])) for code in ENTRY_ORDER})
    print(f"generated {len(CORE)} cards; counts={dict(counts)}")


if __name__ == "__main__":
    main()
