# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
CLAUDE = RUN / "03_claudecode_lane"
FUSION = RUN / "04_fusion_audit"
FUSION.mkdir(parents=True, exist_ok=True)


def read_jsonl(path: Path) -> list[dict]:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def qnorm(q: str) -> str:
    m = re.search(r"(20|21|1[0-9]|[1-9])", str(q or ""))
    return m.group(1) if m else str(q or "").strip()


CULTURE_NODE_MARKERS = (
    "文化",
    "民族精神",
    "中华优秀传统",
    "文化自信",
)

GENERIC_STUDENT_FILLER = (
    "学生看到这里，关键不是只抓一个材料名词，而是抓住材料中主体行动、条件变化和关系处理方式与该原理之间的对应关系",
    "落到本题，就是把材料中的具体做法写成遵循该原理后的实际效果，避免只背原理不扣材料",
)


def ensure_period(text: str) -> str:
    text = re.sub(r"\s+", "", str(text or ""))
    text = re.sub(r"[。；;]+。", "。", text)
    text = re.sub(r"。{2,}", "。", text)
    if text and not text.endswith(("。", "！", "？")):
        text += "。"
    return text


def short_quote(text: str, limit: int = 34) -> str:
    text = re.sub(r"\s+", "", str(text or "")).strip("。；; ")
    return text[:limit] + ("……" if len(text) > limit else "")


def is_culture_node(row: dict) -> bool:
    field = f"{row.get('framework_node','')} {row.get('canonical_node','')}"
    return any(marker in field for marker in CULTURE_NODE_MARKERS)


def base_has(base_text: str, suite: str, question_no: str) -> bool:
    q = qnorm(question_no)
    if not q:
        return False
    pats = [f"{suite} 第{q}题", f"{suite}第{q}题", f"{suite} Q{q}", f"{suite}Q{q}"]
    return any(p in base_text for p in pats)


def node(framework: str) -> str:
    s = framework or ""
    if "物质决定意识" in s:
        return "物质决定意识"
    if "一切从实际" in s:
        return "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"
    if "辩证否定" in s or "守正创新" in s or "扬弃" in s:
        return "辩证否定 / 守正创新"
    if "量变" in s or "质变" in s:
        return "量变与质变 / 适度原则"
    if "尊重客观规律" in s or ("规律" in s and "主观能动" in s):
        return "尊重客观规律与发挥主观能动性相结合"
    if "主观能动" in s or "意识能动" in s or "正确意识" in s:
        return "主观能动性 / 意识的能动作用"
    if "规律" in s:
        return "尊重客观规律与发挥主观能动性相结合"
    if "实践决定认识" in s or "实践是认识" in s:
        return "实践是认识的基础"
    if "正确的认识" in s or "认识促进实践" in s:
        return "认识对实践的反作用"
    if "认识" in s and "实践" in s:
        return "实践与认识（总）"
    if "系统" in s:
        return "系统观念 / 系统优化"
    if "整体" in s:
        return "整体与部分"
    if "联系" in s:
        return "联系的普遍性 / 联系的观点（总）"
    if "主次矛盾" in s or "主要矛盾" in s or "次要矛盾" in s:
        return "主要矛盾和次要矛盾"
    if "主要方面" in s or "次要方面" in s or "主流" in s or "支流" in s:
        return "矛盾的主要方面和次要方面"
    if "两点论" in s or "重点论" in s:
        return "两点论与重点论"
    if "普遍性与特殊性" in s or "普遍特殊" in s:
        return "矛盾的普遍性和特殊性"
    if "特殊性" in s or "具体问题" in s:
        return "矛盾的特殊性 / 具体问题具体分析"
    if "对立统一" in s or "矛盾观" in s or "矛盾" in s:
        return "矛盾就是对立统一"
    if "发展" in s:
        return "发展的观点 / 发展的普遍性"
    if "上层建筑" in s or "经济基础" in s:
        return "社会发展两大基本规律和基本矛盾"
    if "社会存在" in s or "社会意识" in s:
        return "社会存在与社会意识"
    if "人民" in s:
        return "人民群众"
    if "价值判断" in s or "价值选择" in s:
        return "价值判断与价值选择"
    if "价值观" in s:
        return "价值观的导向作用"
    return s.strip() or "待定节点"


def normalize_second(row: dict) -> dict:
    return {
        "source_suite": row["source_suite"],
        "question_no": row["question_no"],
        "framework_node": row["framework_node"],
        "canonical_node": node(row["framework_node"]),
        "material_trigger": row["material_trigger"],
        "question_prompt": row["question_prompt"],
        "why_trigger": row["why_trigger"],
        "answer_landing": row["answer_landing"],
        "evidence_level": row["evidence_level"],
        "boundary_note": row.get("boundary_note", ""),
        "source_lane": "ClaudeCode B second mock",
    }


def normalize_first(row: dict) -> dict:
    framework = row.get("philosophy_node") or row.get("framework_node") or ""
    return {
        "source_suite": row["source_suite"],
        "question_no": row["question_no"],
        "framework_node": framework,
        "canonical_node": node(framework),
        "material_trigger": row.get("trigger_in_material", ""),
        "question_prompt": row.get("question_stem", ""),
        "why_trigger": row.get("why_applicable", ""),
        "answer_landing": row.get("answer_focus", ""),
        "evidence_level": row.get("evidence_level", ""),
        "boundary_note": row.get("note", ""),
        "source_lane": "ClaudeCode B first mock",
    }


def is_blocked(row: dict, base_text: str, is_second: bool) -> tuple[bool, str]:
    ev = row.get("evidence_level", "")
    prompt = row.get("question_prompt") or row.get("question_stem", "")
    note = row.get("boundary_note") or row.get("note", "")
    if is_culture_node(row):
        return True, "culture_boundary"
    if "选必三" in note or "边界" in note and "无边界" not in note:
        return True, "module_boundary"
    if "弱" in ev or "角度提示" in ev:
        return True, "weak_evidence"
    if "待回源" in prompt or "0字节" in prompt or "约：" in prompt:
        return True, "question_prompt_not_verified"
    if (not is_second) and base_has(base_text, row.get("source_suite", ""), row.get("question_no", "")):
        return True, "already_in_base_exact_source"
    return False, ""


def thicken(row: dict) -> dict:
    trigger = row["material_trigger"].strip("。；; ")
    why = row["why_trigger"].strip("。；; ")
    answer = row["answer_landing"].strip("。；; ")
    row["material_trigger"] = trigger + "。"
    row["why_trigger"] = why + "。"
    row["answer_landing"] = answer + "。"
    return row


def node_specific_why(node_name: str, trigger_core: str) -> str:
    if "系统观念" in node_name:
        return f"材料中的“{trigger_core}”不是孤立措施，而是把多个要素放到同一整体中统筹，触发整体与部分、系统优化的分析。"
    if "辩证否定" in node_name:
        return f"材料中的“{trigger_core}”同时包含保留与突破，说明发展不是全盘抛弃旧事物，而是在扬弃中实现创新。"
    if "矛盾的特殊性" in node_name:
        return f"材料中的“{trigger_core}”强调对象、类型或条件不同，说明不能套用同一模式，必须具体问题具体分析。"
    if "价值观" in node_name:
        return f"材料中的“{trigger_core}”指向行动背后的价值取向，说明正确价值观会影响人们怎样判断、怎样选择、怎样行动。"
    if "量变" in node_name:
        return f"材料中的“{trigger_core}”突出持续积累、久久为功或由小到大的过程，正是量变积累推动质变的信号。"
    if "尊重客观规律" in node_name:
        return f"材料中的“{trigger_core}”同时出现客观规律和人的主动作为，说明既不能主观蛮干，也不能消极等待。"
    if "主要矛盾" in node_name:
        return f"材料中的“{trigger_core}”要求在全局中找到关键环节，用重点突破带动整体推进。"
    if "矛盾就是对立统一" in node_name:
        return f"材料中的“{trigger_core}”把两个相反方面放在同一事物中考察，触发对立统一的分析。"
    if "实践是认识" in node_name:
        return f"材料中的“{trigger_core}”说明认识从真实活动和真实情境中来，又要回到实践中接受检验和发挥作用。"
    if "物质决定意识" in node_name:
        return f"材料中的“{trigger_core}”先给出客观条件和现实基础，再说明人的认识、课程或方案由这些实际决定。"
    if "发展" in node_name:
        return f"材料中的“{trigger_core}”强调事物处在变化推进中，要求用动态眼光看问题。"
    return f"材料中的“{trigger_core}”已经把题目从事实描述推进到该原理处理的关系和变化上。"


def node_specific_answer(node_name: str, trigger_core: str) -> str:
    if "系统观念" in node_name:
        return "答案要落到统筹各要素、优化结构、形成整体功能上，不能只罗列单个做法。"
    if "辩证否定" in node_name:
        return "答案要写出既继承合理成分又突破旧局限，在保留与创新的统一中推动发展。"
    if "矛盾的特殊性" in node_name:
        return "答案要写出针对具体对象和具体条件采取不同办法，反对照搬照套。"
    if "价值观" in node_name:
        return "答案要写出用正确价值取向引导判断和选择，使行动方向服务正确目标。"
    if "量变" in node_name:
        return "答案要写出重视长期积累、持续推进，在量的积累中促成质的提升。"
    if "尊重客观规律" in node_name:
        return "答案要写出按规律办事并主动作为，把科学施策和积极创新结合起来。"
    if "主要矛盾" in node_name:
        return "答案要写出抓关键领域和关键环节，以重点突破带动全局推进。"
    if "矛盾就是对立统一" in node_name:
        return "答案要写出承认双方差异和冲突，并在统一关系中推动问题解决。"
    if "实践是认识" in node_name:
        return "答案要写出从实践中获得认识、检验认识，并用认识反过来指导实践。"
    if "物质决定意识" in node_name:
        return "答案要写出从客观实际出发，使认识和方案符合现实条件。"
    if "发展" in node_name:
        return "答案要写出动态把握变化趋势，在推进中处理当前与长远的关系。"
    return f"答案要扣住“{trigger_core}”，把原理写成针对本题的具体做法和效果。"


def polish_student_row(row: dict) -> dict:
    trigger_core = short_quote(row.get("material_trigger", ""))
    node_name = row.get("canonical_node", "").strip()

    for key in ("why_trigger", "answer_landing"):
        text = row.get(key, "")
        for filler in GENERIC_STUDENT_FILLER:
            text = text.replace(filler, "")
        row[key] = ensure_period(text)

    row["material_trigger"] = ensure_period(row.get("material_trigger", ""))

    if len(row.get("why_trigger", "")) < 45 and trigger_core and node_name:
        row["why_trigger"] = ensure_period(
            f"{row['why_trigger'].rstrip('。')}。"
            f"{node_specific_why(node_name, trigger_core)}"
        )
    if len(row.get("answer_landing", "")) < 55 and trigger_core:
        row["answer_landing"] = ensure_period(
            f"{row['answer_landing'].rstrip('。')}。"
            f"{node_specific_answer(node_name, trigger_core)}"
        )
    return row


def entry_md(row: dict, idx: int) -> str:
    q = qnorm(row["question_no"])
    qtext = f"第{q}题" if q else row["question_no"]
    return (
        f"{idx}. {row['source_suite']} {qtext}（主观题）\n"
        f"【材料触发点】{row['material_trigger']}\n"
        f"【设问】{row['question_prompt']}\n"
        f"【为什么能想到】{row['why_trigger']}\n"
        f"【答案落点】{row['answer_landing']}\n"
    )


def main() -> int:
    base_text = (RUN / "01_source_inventory" / "accepted_base_docx_text.txt").read_text(encoding="utf-8")
    second_raw = read_jsonl(CLAUDE / "claudecode_b_second_mock_insert_candidates.jsonl")
    first_raw = read_jsonl(CLAUDE / "claudecode_b_first_mock_insert_candidates.jsonl")

    accepted: list[dict] = []
    blocked: list[dict] = []

    for raw in second_raw:
        row = normalize_second(raw)
        block, reason = is_blocked(row, base_text, is_second=True)
        if block:
            row["block_reason"] = reason
            blocked.append(row)
        else:
            accepted.append(polish_student_row(thicken(row)))

    for raw in first_raw:
        row = normalize_first(raw)
        block, reason = is_blocked(row, base_text, is_second=False)
        if block:
            row["block_reason"] = reason
            blocked.append(row)
        else:
            accepted.append(polish_student_row(thicken(row)))

    groups: dict[str, list[dict]] = defaultdict(list)
    for row in accepted:
        groups[row["canonical_node"]].append(row)

    lines = [
        "# 哲学宝典母版原地插入补丁稿（融合版）",
        "",
        "说明：本稿是供插入 5.2 母版的学生版正文补丁，按原理方法论节点组织，不是二模专题。弱证据、边界排除、题干未核实项目不进入正文，另列审计阻塞。",
        "",
    ]
    idx = 1
    for node_name in sorted(groups.keys()):
        lines.append(f"## {node_name}")
        lines.append("")
        for row in groups[node_name]:
            lines.append(entry_md(row, idx))
            idx += 1
        lines.append("")

    audit = [
        "# 插入候选审计",
        "",
        f"- accepted_student_entries: {len(accepted)}",
        f"- blocked_or_skipped_entries: {len(blocked)}",
        "",
        "## Accepted Counts By Node",
    ]
    for k in sorted(groups.keys()):
        audit.append(f"- {k}: {len(groups[k])}")
    audit.extend(["", "## Blocked / Skipped"])
    for row in blocked:
        audit.append(f"- {row['source_suite']} {row['question_no']} | {row.get('framework_node','')} | {row.get('evidence_level','')} | {row.get('block_reason','')}")

    (FUSION / "student_patch_entries.md").write_text("\n".join(lines), encoding="utf-8")
    (FUSION / "student_patch_entries.audit.md").write_text("\n".join(audit), encoding="utf-8")
    with (FUSION / "student_patch_entries.accepted.jsonl").open("w", encoding="utf-8") as f:
        for row in accepted:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with (FUSION / "student_patch_entries.blocked.jsonl").open("w", encoding="utf-8") as f:
        for row in blocked:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
