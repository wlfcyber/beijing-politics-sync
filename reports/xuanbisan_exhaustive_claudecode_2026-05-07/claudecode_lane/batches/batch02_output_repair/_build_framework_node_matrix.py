"""Generate FRAMEWORK_NODE_MATRIX.csv and FRAMEWORK_NODE_MATRIX_SUMMARY.csv.

Detail matrix (6 cols): framework_node, question_id, suite_id, type,
evidence_level, mount_role
Summary (11 cols): framework_node, total_count, subjective_count,
choice_count, suites, evidence_levels, primary_role_count,
auxiliary_role_count, hard_sample_count, sample_question_ids, notes
"""
import csv
from collections import defaultdict
from pathlib import Path

OUT_DETAIL = Path(__file__).parent / "FRAMEWORK_NODE_MATRIX.csv"
OUT_SUMMARY = Path(__file__).parent / "FRAMEWORK_NODE_MATRIX_SUMMARY.csv"

DETAIL_HEADER = [
    "framework_node", "question_id", "suite_id", "type",
    "evidence_level", "mount_role",
]
SUMMARY_HEADER = [
    "framework_node", "total_count", "subjective_count", "choice_count",
    "suites", "evidence_levels", "primary_role_count",
    "auxiliary_role_count", "hard_sample_count", "sample_question_ids", "notes",
]


def m(node, qid, suite, t, lvl, role):
    return [node, qid, suite, t, lvl, role]


# Build detail rows from MAIN_THINKING_LEDGER (20 rows) + CHOICE_TRAP_LEDGER
# (12 rows) + 同类索引 (2 auxiliary mounts)
DETAIL_ROWS = [
    # ----- 主观题挂载 (20 行) -----
    m("推理>演绎>充分条件假言推理", "Q-2024朝阳一模-20-1", "S-2024朝阳一模", "主观题", "A-formal", "primary·hard_sample§十八"),
    m("推理>演绎>必要条件假言推理", "Q-2024朝阳一模-20-2", "S-2024朝阳一模", "主观题", "A-formal", "primary·hard_sample§十八"),
    m("辩证思维>动态性", "Q-2024朝阳二模-19-1", "S-2024朝阳二模", "主观题", "A-formal", "primary"),
    m("推理>类比推理", "Q-2024朝阳二模-19-1", "S-2024朝阳二模", "主观题", "A-formal", "primary"),
    m("形式逻辑>判断>联言判断（真值条件）", "Q-2024朝阳二模-19-2", "S-2024朝阳二模", "主观题", "A-formal", "primary"),
    m("推理>归纳>不完全归纳·轻率概括", "Q-2024朝阳期中-18", "S-2024朝阳期中", "主观题", "A-formal", "primary"),
    m("推理>类比推理", "Q-2024朝阳期中-18", "S-2024朝阳期中", "主观题", "A-formal", "primary"),
    m("创新思维>超前思维", "Q-2024朝阳期中-19", "S-2024朝阳期中", "主观题", "A-formal", "primary"),
    m("创新思维>逆向思维", "Q-2024朝阳期中-19", "S-2024朝阳期中", "主观题", "A-formal", "primary"),
    m("创新思维>联想思维", "Q-2024朝阳期中-19", "S-2024朝阳期中", "主观题", "A-formal", "primary"),
    m("创新思维>发散思维与聚合思维", "Q-2024朝阳期中-19", "S-2024朝阳期中", "主观题", "A-formal", "primary"),
    m("辩证思维>矛盾分析法", "Q-2026朝阳期中-20", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("辩证思维>分析与综合", "Q-2026朝阳期中-20", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("辩证思维>质量互变", "Q-2026朝阳期中-20", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("辩证思维>动态性", "Q-2026朝阳期中-20", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("创新思维>超前思维", "Q-2026朝阳期中-21-2", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("创新思维>联想思维", "Q-2026朝阳期中-21-2", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("创新思维>逆向思维", "Q-2026朝阳期中-21-2", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),
    m("创新思维>思路新方法新结果新（三新）", "Q-2026朝阳期中-21-2", "S-2026朝阳期中", "主观题", "A-support", "primary·hard_sample§十三"),
    m("创新思维>发散思维与聚合思维", "Q-2026朝阳期中-21-2", "S-2026朝阳期中", "主观题", "A-formal", "primary·hard_sample§十三"),

    # ----- 选择题挂载 (12 行) -----
    m("形式逻辑>逻辑规则综合（排中律/矛盾律/越级划分/四概念）", "Q-2024朝阳一模-6", "S-2024朝阳一模", "选择题", "B-choice-signal", "primary"),
    m("创新思维>多角度判断（创新思维 vs 逻辑思维边界）", "Q-2024朝阳一模-7", "S-2024朝阳一模", "选择题", "B-choice-signal", "primary"),
    m("推理>三段论>小项不当扩大", "Q-2024朝阳二模-7", "S-2024朝阳二模", "选择题", "B-choice-signal", "primary·hard_sample§十八"),
    m("推理>三段论>第三格AAI式", "Q-2024朝阳期中-7", "S-2024朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("形式逻辑>判断>必要条件假言判断（三种等价表达式）", "Q-2024朝阳期中-8", "S-2024朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("推理>归纳>共变法（因果探求三法）", "Q-2024朝阳期中-9", "S-2024朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("形式逻辑>概念>外延关系>属种关系", "Q-2024朝阳期中-10", "S-2024朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("推理>三段论>第二格补大前提", "Q-2026朝阳期中-11", "S-2026朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("形式逻辑>判断>相容选言判断", "Q-2026朝阳期中-12", "S-2026朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("创新思维>联想思维（与认识发展历程综合）", "Q-2026朝阳期中-13", "S-2026朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("认识发展历程>感性具体>思维抽象", "Q-2026朝阳期中-13", "S-2026朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("推理>归纳>不完全归纳推理或然性", "Q-2026朝阳期中-14", "S-2026朝阳期中", "选择题", "B-choice-signal", "primary"),
    m("形式逻辑>判断>联言判断（真值条件）", "Q-2026朝阳期中-15", "S-2026朝阳期中", "选择题", "B-choice-signal", "primary"),

    # ----- 同类索引/辅助挂载 (2 行) -----
    m("创新思维>改变条件创造条件（建立新具体联系）", "Q-2024朝阳一模-4", "S-2024朝阳一模", "选择题", "B-choice-signal", "auxiliary·辅助挂载（题干主线在必修四）"),
    m("导论>系统观念", "Q-2024朝阳一模-9", "S-2024朝阳一模", "选择题", "B-choice-signal", "auxiliary·辅助挂载（题干主线在必修三政治协商）"),
]


def main():
    # Validate detail rows
    assert len(DETAIL_ROWS) == 35, f"expected 35 detail rows, got {len(DETAIL_ROWS)}"

    with open(OUT_DETAIL, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(DETAIL_HEADER)
        for r in DETAIL_ROWS:
            w.writerow(r)
    print(f"wrote {OUT_DETAIL} rows={len(DETAIL_ROWS) + 1}")

    # Build summary view
    by_node = defaultdict(list)
    for r in DETAIL_ROWS:
        by_node[r[0]].append(r)

    summary_rows = []
    for node in sorted(by_node.keys()):
        items = by_node[node]
        total = len(items)
        subj = sum(1 for it in items if it[3] == "主观题")
        ch = sum(1 for it in items if it[3] == "选择题")
        suites = sorted(set(it[2] for it in items))
        levels = sorted(set(it[4] for it in items))
        primary = sum(1 for it in items if it[5].startswith("primary"))
        aux = sum(1 for it in items if it[5].startswith("auxiliary"))
        hard = sum(1 for it in items if "hard_sample" in it[5])
        qids = sorted(set(it[1] for it in items))
        # Build a brief "notes" column reflecting hard sample tags / role ratio
        notes = []
        if hard:
            notes.append(f"硬样本{hard}个")
        if aux:
            notes.append(f"辅助挂载{aux}个")
        if subj and ch:
            notes.append("跨主观题+选择题")
        notes_text = "；".join(notes) if notes else ""
        summary_rows.append([
            node, total, subj, ch,
            "；".join(suites),
            "；".join(levels),
            primary, aux, hard,
            "；".join(qids),
            notes_text,
        ])

    with open(OUT_SUMMARY, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(SUMMARY_HEADER)
        for r in summary_rows:
            w.writerow(r)
    print(f"wrote {OUT_SUMMARY} rows={len(summary_rows) + 1} (unique framework_nodes={len(summary_rows)})")


if __name__ == "__main__":
    main()
