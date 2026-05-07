import json
from collections import Counter, defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
OUT = RUN / "fusion" / "overall_batch_closure"

ENTRY_SOURCES = [
    ("batch01_haidian_xicheng", RUN / "claudecode_lane" / "batches" / "batch01_haidian_xicheng" / "entries" / "batch01_entries.jsonl"),
    ("batch02_chaoyang_controlled_input", RUN / "fusion" / "batch02_chaoyang_controlled_input" / "entries" / "batch02_entries.jsonl"),
    ("batch03_dongcheng", RUN / "claudecode_lane" / "batches" / "batch03_dongcheng" / "entries" / "batch03_entries.jsonl"),
    ("batch04_fengtai_shunyi_tongzhou", RUN / "claudecode_lane" / "batches" / "batch04_fengtai_shunyi_tongzhou" / "entries" / "batch04_entries.jsonl"),
]

VALID_EVIDENCE = {"A-formal", "A-support", "B-choice-signal", "C-boundary", "missing"}
FORBIDDEN_STUDENT_PHRASES = [
    "固定分析流程",
    "source path",
    "correct_option_chain",
    "A-formal",
    "B-choice-signal",
    "needs_codex_recheck",
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


def parent_qid(question_id, valid_qids):
    if question_id in valid_qids:
        return question_id
    current = question_id
    while "-" in current:
        current = current.rsplit("-", 1)[0]
        if current in valid_qids:
            return current
    return ""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    entries = load_entries()
    with (OUT / "QUESTION_DECISIONS_ALL.csv").open("r", encoding="utf-8-sig", newline="") as f:
        valid_qids = {row["question_id"] for row in __import__("csv").DictReader(f)}
    evidence_counts = Counter(e.get("evidence_level", "") for e in entries)
    source_counts = Counter(e["_source"] for e in entries)
    type_counts = Counter(e.get("type", "") for e in entries)
    framework_counts = Counter(e.get("framework_node", "") for e in entries)
    needs_recheck = [e for e in entries if str(e.get("needs_codex_recheck", "")).lower() == "yes"]

    issues = []
    synthetic_child_entries = 0
    for e in entries:
        qid = e.get("question_id", "")
        parent = parent_qid(qid, valid_qids)
        if not parent:
            issues.append({"kind": "entry_question_id_not_in_decisions", "question_id": qid, "source": e["_source"]})
        elif parent != qid:
            synthetic_child_entries += 1
        if e.get("evidence_level", "") not in VALID_EVIDENCE:
            issues.append({"kind": "invalid_evidence_level", "question_id": qid, "source": e["_source"], "value": e.get("evidence_level", "")})
        for field in ["framework_node", "material_signal", "trigger_logic", "answer_sentence"]:
            text = str(e.get(field, ""))
            if not text.strip():
                issues.append({"kind": f"empty_{field}", "question_id": qid, "source": e["_source"]})
            for phrase in FORBIDDEN_STUDENT_PHRASES:
                if phrase in text:
                    issues.append({"kind": "forbidden_phrase", "question_id": qid, "source": e["_source"], "field": field, "phrase": phrase})
        if len(str(e.get("answer_sentence", ""))) < 24:
            issues.append({"kind": "short_answer_sentence", "question_id": qid, "source": e["_source"], "answer_sentence": e.get("answer_sentence", "")})

    by_top_node = defaultdict(int)
    for node, count in framework_counts.items():
        top = node.split(">")[0].split("→")[0].strip()
        by_top_node[top] += count

    audit = {
        "verdict": "FUSION_ENTRY_CONTENT_QA_OK_NOT_FINAL" if not issues else "FUSION_ENTRY_CONTENT_QA_NEEDS_FIX",
        "entry_rows": len(entries),
        "source_counts": dict(source_counts),
        "type_counts": dict(type_counts),
        "evidence_counts": dict(evidence_counts),
        "needs_codex_recheck_rows": len(needs_recheck),
        "synthetic_child_entries_with_parent_decision": synthetic_child_entries,
        "top_framework_counts": dict(sorted(by_top_node.items(), key=lambda kv: (-kv[1], kv[0]))),
        "top_20_framework_nodes": dict(framework_counts.most_common(20)),
        "issues": issues[:200],
        "issue_count": len(issues),
    }
    (OUT / "FUSION_ENTRY_CONTENT_QA.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Fusion Entry Content QA",
        "",
        f"Verdict: `{audit['verdict']}`",
        "",
        f"- entry rows: `{audit['entry_rows']}`",
        f"- source counts: `{audit['source_counts']}`",
        f"- evidence counts: `{audit['evidence_counts']}`",
        f"- needs_codex_recheck rows: `{audit['needs_codex_recheck_rows']}`",
        f"- synthetic child entries with parent decision: `{audit['synthetic_child_entries_with_parent_decision']}`",
        f"- issue count: `{audit['issue_count']}`",
        "",
        "## Top Framework Groups",
        "",
    ]
    for node, count in audit["top_framework_counts"].items():
        lines.append(f"- `{node}`: {count}")
    lines.extend(["", "## Issues", ""])
    if issues:
        for issue in issues[:50]:
            lines.append(f"- `{issue['kind']}`: `{issue.get('question_id', '')}` ({issue.get('source', '')})")
    else:
        lines.append("- none")
    lines.extend(["", "## Boundary", "", "- This is only a fusion-content precheck. It does not authorize final Word/PDF."])
    (OUT / "FUSION_ENTRY_CONTENT_QA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
