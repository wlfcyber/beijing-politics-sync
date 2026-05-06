#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
from collections import defaultdict
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
CONTROL = BASE / "09_student_draft" / "phase12_expanded_body_FROM_362_control_matrix.csv"
REASONING_FUSION = BASE / "05_coverage" / "phase06_reasoning_typology_fusion.csv"
OUT_STUDENT = BASE / "09_student_draft"
OUT_REVIEW = BASE / "08_review"
OUT_COVERAGE = BASE / "05_coverage"
AUDIT = BASE / "audit"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def backup(path: Path, name: str) -> None:
    if path.exists():
        AUDIT.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, AUDIT / name)


def load_meta() -> dict[str, dict[str, str]]:
    return {row["question_id"]: row for row in read_csv(CONTROL)}


def load_reasoning_fusion() -> dict[str, dict[str, str]]:
    return {row["question_id"]: row for row in read_csv(REASONING_FUSION)}


def add_mount(mounts: list[dict[str, str]], *, kind: str, qid: str, node: str, label: str, basis: str, meta: dict[str, dict[str, str]]) -> None:
    row = meta.get(qid, {})
    mounts.append(
        {
            "index_kind": kind,
            "node": node,
            "label": label,
            "question_id": qid,
            "visible_title": row.get("visible_title", qid),
            "body_order": row.get("order", ""),
            "question_type_group": row.get("question_type_group", ""),
            "module": row.get("module", ""),
            "source_basis": basis,
        }
    )


def reasoning_mounts(meta: dict[str, dict[str, str]], fusion: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    mounts: list[dict[str, str]] = []

    locked = {
        "Q-2024朝阳一模-20-1": [
            ("充分条件假言推理", "正文正例", "manual_lock:充分条件假言推理_否定后件式; external_forced_check"),
        ],
        "Q-2024朝阳一模-20-2": [
            ("必要条件假言推理", "正文正例", "manual_lock:必要条件假言推理_肯定后件式; external_forced_check"),
        ],
        "Q-2025西城二模-16-2": [
            ("充分条件假言推理", "正文正例", "manual_lock:充分条件假言推理_肯定后件无效; external_forced_check"),
        ],
        "Q-2026通州期末-19-2": [
            ("充分条件假言推理", "正文正例", "manual_lock:推理1充分条件肯定前件有效; external_forced_check"),
            ("必要条件假言推理", "正文正例", "manual_lock:推理2必要条件仅肯定前件不能肯定后件; external_forced_check"),
        ],
        "Q-2026丰台一模-18-2": [
            ("必要条件假言推理", "正文正例", "manual_lock:甲_必要条件假言推理_肯定后件式; external_forced_check"),
            ("三段论结构题", "正文正例", "manual_lock:乙_三段论大项不当扩大; external_forced_check"),
        ],
        "Q-2024朝阳二模-7": [
            ("三段论结构题", "选择题陷阱", "manual_lock:A项小项扩大_小项娱乐工具前提不周延结论扩大; not_middle_term"),
            ("必要条件假言推理", "选择题陷阱", "manual_lock:C项必要条件误用"),
            ("归纳推理", "选择题陷阱", "manual_lock:B项归纳结论确定性夸大"),
        ],
        "Q-2025西城二模-7": [
            ("演绎推理与前提真实性", "选择题陷阱", "manual_lock:演绎强度比较_结构正确还要前提真实"),
            ("归纳推理", "选择题陷阱", "manual_lock:求异法_归纳结论或然"),
            ("类比推理", "选择题陷阱", "manual_lock:类比可信度低于演绎与求异法"),
        ],
        "Q-2025顺义一模-7": [
            ("三段论结构题", "选择题陷阱", "manual_lock:三段论周延规则; 真实错误=大项不当扩大; A项误称小项不当扩大; 谬误名称纠错"),
            ("三段论周延规则 / 大项不当扩大 / 谬误名称纠错", "选择题陷阱", "manual_lock:真实错误=大项不当扩大; 小项不当扩大仅为A项错误命名陷阱"),
        ],
        "Q-2025东城期末-13": [
            ("三段论结构题", "选择题陷阱", "manual_lock:①③中项不周延; ②大项不当扩大; ④四概念; 三段论谬误辨析"),
        ],
        "Q-2026丰台一模-8": [
            ("充分条件假言推理", "选择题陷阱", "manual_lock:P→Q; 否定后件可否前; 肯定后件无效; 限制换位链条"),
        ],
        "Q-2026东城期末-17-2": [
            ("逻辑三律", "正文正例", "manual_lock:主张1_矛盾律_联言判断"),
            ("联言判断与联言推理", "正文正例", "manual_lock:主张1_联言支不能同真"),
            ("充分条件假言推理", "正文正例", "manual_lock:主张2_肯定后件误推"),
            ("三段论结构题", "正文正例", "manual_lock:主张3_中项不周延"),
        ],
    }
    for qid, items in locked.items():
        for node, label, basis in items:
            add_mount(mounts, kind="reasoning", qid=qid, node=node, label=label, basis=basis, meta=meta)

    for qid, row in meta.items():
        if qid in locked:
            continue
        if row.get("module") not in {"推理", "交叉"}:
            continue
        f = fusion.get(qid)
        if not f:
            add_mount(mounts, kind="reasoning", qid=qid, node="NEEDS_TYPE_CONFIRMATION", label="辅助挂载", basis="no_phase06_locked_reasoning_row", meta=meta)
            continue
        logical = f.get("logical_form", "")
        basis = "phase06_logical_form_locked:" + logical
        nodes: list[tuple[str, str]] = []
        if "充分条件" in logical:
            nodes.append(("充分条件假言推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if "必要条件" in logical:
            nodes.append(("必要条件假言推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if "联言" in logical:
            nodes.append(("联言判断与联言推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if "不相容选言" in logical:
            nodes.append(("不相容选言推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        elif "相容选言" in logical or "选言" in logical:
            nodes.append(("相容选言推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if any(k in logical for k in ["三段论", "周延", "中项", "大项", "小项"]):
            nodes.append(("三段论结构题", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if any(k in logical for k in ["矛盾律", "同一律", "排中律"]):
            nodes.append(("逻辑三律", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if "归纳" in logical or any(k in logical for k in ["求同", "求异", "共变", "剩余"]):
            nodes.append(("归纳推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if "类比" in logical:
            nodes.append(("类比推理", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if any(k in logical for k in ["概念", "定义", "外延", "属种", "种属"]):
            nodes.append(("概念外延关系", "正文正例" if row.get("question_type_group") == "主观题" else "选择题陷阱"))
        if not nodes:
            nodes.append(("NEEDS_TYPE_CONFIRMATION", "辅助挂载"))
        seen = set()
        for node, label in nodes:
            if node in seen:
                continue
            seen.add(node)
            add_mount(mounts, kind="reasoning", qid=qid, node=node, label=label, basis=basis, meta=meta)

    return sorted(mounts, key=lambda r: (r["node"], int(r["body_order"] or 9999), r["question_id"], r["label"]))


def thinking_mounts(meta: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    mounts: list[dict[str, str]] = []
    locked = {
        "Q-2025海淀二模-20": [
            ("辩证思维", "正文正例", "manual_lock:角度池_整体性_动态性_分析综合_质量互变_辩证否定"),
            ("辩证思维：整体性", "正文正例", "manual_lock:共享发展四层次整体推进"),
            ("辩证思维：动态性", "正文正例", "manual_lock:渐进共享_逐步推进共同富裕"),
            ("辩证思维：分析与综合", "正文正例", "manual_lock:共享层次拆分后综合推进"),
            ("辩证思维：质量互变", "辅助挂载", "manual_lock:渐进积累到共同富裕"),
            ("辩证思维：辩证否定", "辅助挂载", "manual_lock:角度池可选_非三点全必答"),
        ],
        "Q-2025海淀期末-17-1": [
            ("科学思维", "正文正例", "manual_lock:永动机_客观规律"),
            ("科学思维：客观性", "正文正例", "manual_lock:从实际出发_如实反映对象"),
        ],
        "Q-2025海淀期末-18": [
            ("创新思维", "正文正例", "manual_lock:城市图书馆创新服务"),
            ("创新思维：逆向思维", "正文正例", "manual_lock:人找书到书找人"),
            ("创新思维：联想思维", "正文正例", "manual_lock:赤印意象迁移到建筑设计"),
        ],
        "Q-2024海淀二模-17-1": [
            ("科学思维", "正文正例", "manual_lock:SCIENCE_ONLY_SOURCE_SUPPORTED"),
            ("科学思维：客观性", "正文正例", "manual_lock:全面真实准确_客观反映生活模式"),
            ("科学思维：探索性与方法更新", "正文正例", "manual_lock:范围对象采集方式分类方式更新_答案源支持"),
            ("科学思维：整体安排", "正文正例", "manual_lock:分阶段实施任务明确_答案源支持"),
        ],
        "Q-2024海淀二模-17-2": [
            ("认识发展历程", "正文正例", "manual_lock:调查了解到分析研究"),
            ("认识发展历程：感性具体", "正文正例", "manual_lock:调查了解阶段"),
            ("认识发展历程：思维抽象", "正文正例", "manual_lock:分析研究阶段"),
            ("认识发展历程：思维具体", "正文正例", "manual_lock:认识发展到整体把握"),
        ],
        "Q-2025东城期末-18-2": [
            ("创新思维", "正文正例", "manual_lock:登月服设计"),
            ("创新思维：联想思维", "正文正例", "manual_lock:传统文化火箭形象登月服联结"),
            ("创新思维：发散思维与聚合思维", "正文正例", "manual_lock:任务需求发散并聚焦方案"),
            ("创新思维：思路新方法新结果新", "正文正例", "manual_lock:文化表达任务适配技术防护"),
        ],
        "Q-2026东城一模-19-4": [
            ("系统观念", "正文正例", "manual_lock:基础研究研发转化应用整体统筹"),
            ("创新思维", "正文正例", "manual_lock:从0到1再把1拉长"),
            ("创新思维：发散思维与聚合思维", "正文正例", "manual_lock:拓展场景并聚合产业链资源"),
            ("创新思维：超前思维", "辅助挂载", "manual_lock:制度机制提前完善"),
        ],
        "Q-2026朝阳期中-20": [
            ("辩证思维", "正文正例", "manual_lock:机遇挑战对立统一"),
            ("辩证思维：整体性", "正文正例", "manual_lock:局部风险整体格局"),
            ("辩证思维：动态性", "正文正例", "manual_lock:当前长远国际变化"),
            ("辩证思维：分析与综合", "正文正例", "manual_lock:综合考量机遇挑战"),
            ("辩证思维：质量互变", "正文正例", "manual_lock:逐步积累条件转化机遇"),
        ],
        "Q-2026朝阳期中-21-2": [
            ("创新思维", "正文正例", "manual_lock:工业城市文旅转型"),
            ("创新思维：超前思维", "正文正例", "manual_lock:预测消费趋势和旅游期待"),
            ("创新思维：联想思维", "正文正例", "manual_lock:冰雪音乐文化叙事联结"),
            ("创新思维：逆向思维", "正文正例", "manual_lock:冷资源转化为热经济"),
            ("创新思维：发散思维与聚合思维", "正文正例", "manual_lock:多角度挖潜后聚焦融合街区"),
        ],
        "Q-2026顺义一模-19-2": [
            ("科学思维", "正文正例", "manual_lock:scientific_thinking_primary"),
            ("科学思维：客观性", "正文正例", "manual_lock:真实生活习惯与养老需求"),
            ("科学思维：预见性", "正文正例", "manual_lock:老龄化趋势与市场潜力"),
            ("科学思维：可检验性", "正文正例", "manual_lock:多轮测试打磨迭代"),
        ],
        "Q-2025丰台期末-7": [
            ("边界陷阱 / 选必三干扰项 / 哲学唯物论伪装", "边界陷阱", "manual_lock:only_boundary_trap_not_超前思维_positive"),
        ],
        "Q-2026通州期末-9": [
            ("选择题陷阱 / 数字化治理材料事实与选必三方法区分", "选择题陷阱", "manual_lock:choice_trap_material_fact_not_subjective_method_positive"),
        ],
        "Q-2026通州期末-11": [
            ("认识发展历程", "选择题陷阱", "manual_lock:感性具体到思维抽象再到思维具体"),
            ("认识发展历程：感性具体", "选择题陷阱", "manual_lock:水脉文脉人脉材料"),
            ("认识发展历程：思维抽象", "选择题陷阱", "manual_lock:河合和理念"),
            ("认识发展历程：思维具体", "选择题陷阱", "manual_lock:时代精神整体诠释"),
        ],
        "Q-2024朝阳一模-7": [
            ("创新思维", "选择题陷阱", "manual_lock:开放创新与继承借鉴_choice_signal"),
        ],
        "Q-2024朝阳二模-19-1": [
            ("辩证思维：动态性", "正文正例", "manual_lock:动态把握对象变化"),
            ("类比推理", "辅助挂载", "manual_lock:如正文涉及类比则辅助挂载"),
        ],
        "Q-2024朝阳期中-19": [
            ("创新思维", "正文正例", "manual_lock:文旅或方案创新"),
            ("创新思维：超前思维", "辅助挂载", "manual_lock:趋势预判"),
            ("创新思维：联想思维", "辅助挂载", "manual_lock:要素联结"),
            ("创新思维：发散思维与聚合思维", "辅助挂载", "manual_lock:方案生成与收束"),
        ],
        "Q-2025海淀二模-12": [
            ("创新思维：超前思维", "选择题陷阱", "manual_lock:耐心资本长期趋势_source_locked_D"),
        ],
    }

    for qid, items in locked.items():
        for node, label, basis in items:
            if qid in meta:
                add_mount(mounts, kind="thinking", qid=qid, node=node, label=label, basis=basis, meta=meta)

    for qid, row in meta.items():
        if qid in locked:
            continue
        if row.get("module") not in {"思维", "交叉"}:
            continue
        add_mount(
            mounts,
            kind="thinking",
            qid=qid,
            node="NEEDS_METHOD_CONFIRMATION",
            label="辅助挂载",
            basis="no_manual_positive_mount_after_MUST_FIX_CONTENT; kept out of positive nodes",
            meta=meta,
        )

    return sorted(mounts, key=lambda r: (r["node"], int(r["body_order"] or 9999), r["question_id"], r["label"]))


def render_index(title: str, mounts: list[dict[str, str]], intro: str) -> str:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in mounts:
        grouped[row["node"]].append(row)
    lines = [
        f"# {title}",
        "",
        "Status: `REBUILT_AFTER_MUST_FIX_CONTENT_REVIEW_ONLY`",
        "",
        intro,
        "",
        "本索引不由正文关键词自动挂载生成；每条挂载依据为 source/control/manual lock，条目标签用于区分正例、陷阱和辅助挂载。",
        "",
    ]
    for node in sorted(grouped):
        rows = sorted(grouped[node], key=lambda r: (int(r["body_order"] or 9999), r["question_id"], r["label"]))
        lines.append(f"## {node}")
        lines.append("")
        for r in rows:
            order = r["body_order"] or "NA"
            lines.append(f"- [{r['label']}] `{order}` {r['visible_title']} (`{r['question_id']}`) - {r['source_basis']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def audit_reasoning(mounts: list[dict[str, str]]) -> list[dict[str, str]]:
    by_qid: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in mounts:
        by_qid[row["question_id"]].append(row)

    def nodes(qid: str) -> str:
        return " | ".join(row["node"] for row in by_qid.get(qid, []))

    checks = [
        ("Q-2024朝阳一模-20-1", "only_sufficient_conditional", "PASS" if "充分条件假言推理" in nodes("Q-2024朝阳一模-20-1") and "必要条件假言推理" not in nodes("Q-2024朝阳一模-20-1") else "FAIL"),
        ("Q-2024朝阳一模-20-2", "only_necessary_conditional", "PASS" if "必要条件假言推理" in nodes("Q-2024朝阳一模-20-2") and "充分条件假言推理" not in nodes("Q-2024朝阳一模-20-2") else "FAIL"),
        ("Q-2025西城二模-16-2", "only_sufficient_conditional", "PASS" if "充分条件假言推理" in nodes("Q-2025西城二模-16-2") and "必要条件假言推理" not in nodes("Q-2025西城二模-16-2") else "FAIL"),
        ("Q-2026通州期末-19-2", "sufficient_and_necessary", "PASS" if "充分条件假言推理" in nodes("Q-2026通州期末-19-2") and "必要条件假言推理" in nodes("Q-2026通州期末-19-2") else "FAIL"),
        ("Q-2026丰台一模-18-2", "necessary_plus_syllogism_major_term", "PASS" if "必要条件假言推理" in nodes("Q-2026丰台一模-18-2") and "三段论结构题" in nodes("Q-2026丰台一模-18-2") else "FAIL"),
        ("Q-2024朝阳二模-7", "small_term_expansion_not_middle_term", "PASS" if "小项扩大" in " ".join(r["source_basis"] for r in by_qid.get("Q-2024朝阳二模-7", [])) and "中项不周延" not in " ".join(r["source_basis"] for r in by_qid.get("Q-2024朝阳二模-7", [])) else "FAIL"),
        ("Q-2025顺义一模-7", "major_term_expansion_not_positive_small_term", "PASS" if "大项不当扩大" in " ".join(r["source_basis"] for r in by_qid.get("Q-2025顺义一模-7", [])) and "phase06_logical_form_locked" not in " ".join(r["source_basis"] for r in by_qid.get("Q-2025顺义一模-7", [])) and all(("小项不当扩大" not in r["source_basis"] or any(k in r["source_basis"] for k in ["误称", "错误命名", "陷阱"])) for r in by_qid.get("Q-2025顺义一模-7", [])) else "FAIL"),
    ]
    return [{"question_id": qid, "forced_check": check, "status": status, "nodes": nodes(qid)} for qid, check, status in checks]


def audit_thinking(mounts: list[dict[str, str]]) -> list[dict[str, str]]:
    by_qid: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in mounts:
        by_qid[row["question_id"]].append(row)

    def nodes(qid: str) -> str:
        return " | ".join(row["node"] for row in by_qid.get(qid, []))

    ft7_nodes = nodes("Q-2025丰台期末-7")
    tz9_nodes = nodes("Q-2026通州期末-9")
    hd17_nodes = nodes("Q-2024海淀二模-17-1")
    checks = [
        ("Q-2025丰台期末-7", "boundary_only_not_positive_method", "PASS" if "边界陷阱" in ft7_nodes and all(k not in ft7_nodes for k in ["超前思维", "预见性", "创新思维"]) else "FAIL", ft7_nodes),
        ("Q-2026通州期末-9", "choice_trap_material_fact_only", "PASS" if "数字化治理材料事实" in tz9_nodes and all(k not in tz9_nodes for k in ["发散思维", "辩证思维：整体性", "创新思维"]) else "FAIL", tz9_nodes),
        ("Q-2026顺义一模-19-2", "scientific_thinking_primary", "PASS" if all(k in nodes("Q-2026顺义一模-19-2") for k in ["科学思维", "客观性", "预见性", "可检验性"]) else "FAIL", nodes("Q-2026顺义一模-19-2")),
        ("Q-2024海淀二模-17-1", "science_only_source_supported", "PASS" if "科学思维" in hd17_nodes and all(k not in hd17_nodes for k in ["创新思维", "辩证思维"]) else "FAIL", hd17_nodes),
    ]
    return [{"question_id": qid, "forced_check": check, "status": status, "nodes": node_text} for qid, check, status, node_text in checks]


def main() -> None:
    meta = load_meta()
    fusion = load_reasoning_fusion()
    r_mounts = reasoning_mounts(meta, fusion)
    t_mounts = thinking_mounts(meta)

    backup(OUT_STUDENT / "phase12_reasoning_typology_index.md", "phase12_reasoning_typology_index_before_MUST_FIX_CONTENT_rebuild.md")
    backup(OUT_STUDENT / "phase12_thinking_method_index.md", "phase12_thinking_method_index_before_MUST_FIX_CONTENT_rebuild.md")

    fields = ["index_kind", "node", "label", "question_id", "visible_title", "body_order", "question_type_group", "module", "source_basis"]
    write_csv(OUT_COVERAGE / "phase12_locked_index_mounts.csv", r_mounts + t_mounts, fields)
    write_csv(OUT_REVIEW / "phase12_reasoning_index_rebuild_audit.csv", audit_reasoning(r_mounts), ["question_id", "forced_check", "status", "nodes"])
    write_csv(OUT_REVIEW / "phase12_thinking_index_rebuild_audit.csv", audit_thinking(t_mounts), ["question_id", "forced_check", "status", "nodes"])

    reasoning_md = render_index(
        "Phase12 推理题型索引 REBUILT",
        r_mounts,
        "重建原因：外审发现充分条件/必要条件假言推理交叉污染。本版依据人工锁定样本与 phase06 logical_form evidence 生成，不使用正文关键词泛挂。",
    )
    thinking_md = render_index(
        "Phase12 思维方法索引 REBUILT",
        t_mounts,
        "重建原因：外审发现边界陷阱被挂成正向思维方法。本版将正例、选择题陷阱、边界陷阱和辅助挂载分开。",
    )
    for name, content in [
        ("phase12_reasoning_typology_index_REBUILT.md", reasoning_md),
        ("phase12_reasoning_typology_index.md", reasoning_md),
        ("phase12_thinking_method_index_REBUILT.md", thinking_md),
        ("phase12_thinking_method_index.md", thinking_md),
    ]:
        (OUT_STUDENT / name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
