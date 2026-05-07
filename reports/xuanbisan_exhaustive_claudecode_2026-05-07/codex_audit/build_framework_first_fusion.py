import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
OUT = RUN / "fusion" / "framework_first_fusion"

ENTRY_SOURCES = [
    ("batch01_haidian_xicheng", RUN / "claudecode_lane" / "batches" / "batch01_haidian_xicheng" / "entries" / "batch01_entries.jsonl"),
    ("batch02_chaoyang_controlled_input", RUN / "fusion" / "batch02_chaoyang_controlled_input" / "entries" / "batch02_entries.jsonl"),
    ("batch03_dongcheng", RUN / "claudecode_lane" / "batches" / "batch03_dongcheng" / "entries" / "batch03_entries.jsonl"),
    ("batch04_fengtai_shunyi_tongzhou", RUN / "claudecode_lane" / "batches" / "batch04_fengtai_shunyi_tongzhou" / "entries" / "batch04_entries.jsonl"),
]

TOP_ORDER = [
    "科学思维",
    "辩证思维",
    "创新思维",
    "认识发展历程",
    "推理",
    "形式逻辑",
    "判断",
    "推理边界",
    "边界陷阱",
    "选必三导论",
    "必修四联系观",
]


def load_entries():
    entries = []
    for source, path in ENTRY_SOURCES:
        with path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                item = json.loads(line)
                item["_source"] = source
                item["_line"] = line_no
                entries.append(item)
    return entries


def top_node(node: str) -> str:
    cleaned = (node or "").strip()
    for sep in [">", "→", "-"]:
        if sep in cleaned:
            return cleaned.split(sep)[0].strip()
    return cleaned


def top_sort_key(top: str):
    try:
        return (TOP_ORDER.index(top), top)
    except ValueError:
        return (len(TOP_ORDER), top)


def display_source(item):
    suite = item.get("suite_id", "")
    qno = item.get("original_qno", "")
    if suite and qno:
        return f"{suite} Q{qno}"
    return item.get("question_id", "")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    entries = load_entries()
    grouped = defaultdict(list)
    for item in entries:
        grouped[top_node(item.get("framework_node", ""))].append(item)

    node_rows = []
    recheck_rows = []
    for top, items in grouped.items():
        by_node = defaultdict(list)
        for item in items:
            by_node[item.get("framework_node", "")].append(item)
            if str(item.get("needs_codex_recheck", "")).lower() == "yes":
                recheck_rows.append(
                    {
                        "question_id": item.get("question_id", ""),
                        "source_batch": item.get("_source", ""),
                        "type": item.get("type", ""),
                        "framework_node": item.get("framework_node", ""),
                        "evidence_level": item.get("evidence_level", ""),
                        "source": display_source(item),
                        "recheck_reason": "entry marked needs_codex_recheck=yes before student final",
                    }
                )
        for node, node_items in by_node.items():
            node_rows.append(
                {
                    "top_node": top,
                    "framework_node": node,
                    "entry_count": len(node_items),
                    "main_count": sum(1 for x in node_items if "choice" not in str(x.get("type", "")).lower()),
                    "choice_count": sum(1 for x in node_items if "choice" in str(x.get("type", "")).lower()),
                    "evidence_counts": json.dumps(dict(Counter(x.get("evidence_level", "") for x in node_items)), ensure_ascii=False),
                    "question_ids": " | ".join(x.get("question_id", "") for x in node_items),
                }
            )

    with (OUT / "FRAMEWORK_NODE_INVENTORY.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fields = ["top_node", "framework_node", "entry_count", "main_count", "choice_count", "evidence_counts", "question_ids"]
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(node_rows, key=lambda r: (top_sort_key(r["top_node"]), r["framework_node"])))

    with (OUT / "RECHECK_MANIFEST.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fields = ["question_id", "source_batch", "type", "framework_node", "evidence_level", "source", "recheck_reason"]
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(recheck_rows)

    lines = [
        "# 选必三《逻辑与思维》框架优先融合草案",
        "",
        "Status: `FUSION_DRAFT_NOT_FINAL`",
        "",
        "说明：本文件是融合底稿，用于回源核验、框架挂载和后续学生版清洗；不是终稿，不授权 Word/PDF。",
        "",
        f"- entries: `{len(entries)}`",
        f"- needs Codex recheck: `{len(recheck_rows)}`",
        "",
    ]
    for top in sorted(grouped, key=top_sort_key):
        items = grouped[top]
        lines.extend([f"## {top}", ""])
        by_node = defaultdict(list)
        for item in items:
            by_node[item.get("framework_node", "")].append(item)
        for node in sorted(by_node):
            node_items = by_node[node]
            lines.extend([f"### {node}", ""])
            for item in node_items:
                recheck = "；需 Codex 回源复核" if str(item.get("needs_codex_recheck", "")).lower() == "yes" else ""
                lines.append(f"**{display_source(item)}**（{item.get('type', '')}；{item.get('evidence_level', '')}{recheck}）")
                lines.append("")
                lines.append(f"- 材料怎么看：{item.get('material_signal', '')}")
                lines.append(f"- 为什么想到：{item.get('trigger_logic', '')}")
                lines.append(f"- 卷面句：{item.get('answer_sentence', '')}")
                lines.append("")
    (OUT / "FRAMEWORK_FIRST_FUSION_DRAFT.md").write_text("\n".join(lines), encoding="utf-8")

    summary = {
        "status": "FUSION_DRAFT_NOT_FINAL",
        "entry_rows": len(entries),
        "top_node_counts": dict(Counter(top_node(e.get("framework_node", "")) for e in entries)),
        "recheck_rows": len(recheck_rows),
        "outputs": [
            str(OUT / "FRAMEWORK_FIRST_FUSION_DRAFT.md"),
            str(OUT / "FRAMEWORK_NODE_INVENTORY.csv"),
            str(OUT / "RECHECK_MANIFEST.csv"),
        ],
    }
    (OUT / "FUSION_DRAFT_SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
