#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治")
WORK = ROOT / "必修四学生可读融合版_2026-05-02"
AUDIT = WORK / "audit"
REPORTS = WORK / "reports"

CODEX_ENTRIES = ROOT / "必修四最终整合_2026-05-02" / "audit" / "final_entries.json"
CLAUDE_DIR = ROOT / "必修四从0重跑_ClaudeCode_2026-05-02" / "audit" / "entries"
FUSION_SCRIPT = ROOT / "必修四终极融合版_2026-05-02" / "scripts" / "build_ultimate_fusion.py"
REBUILD_PATH = ROOT / "哲学宝典5.2原地修订" / "scripts" / "rebuild_in_place_baodian.py"

STUDENT_KEYS = ["材料触发点", "设问", "为什么能想到", "答案落点"]

spec = importlib.util.spec_from_file_location("fusion", FUSION_SCRIPT)
fusion = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(fusion)

rebuild_spec = importlib.util.spec_from_file_location("rebuild", REBUILD_PATH)
rebuild = importlib.util.module_from_spec(rebuild_spec)
assert rebuild_spec.loader is not None
rebuild_spec.loader.exec_module(rebuild)


def entry_key(e: dict) -> tuple[str, str, str, str, str]:
    return (
        e["module"],
        e["node"],
        rebuild.normalize_suite(e["suite"]),
        rebuild.normalize_q(e["q"]),
        e["qtype"],
    )


def key_id(key: tuple[str, str, str, str, str]) -> str:
    return "||".join(key)


def text_score(fields: dict[str, str]) -> int:
    score = 0
    for k in STUDENT_KEYS:
        v = fields.get(k, "")
        score += min(len(v), 220)
        if "材料" in v and k in {"材料触发点", "为什么能想到"}:
            score += 8
        if "因此" in v or "所以" in v:
            score += 6
        if k == "答案落点" and any(x in v for x in ["要", "应", "必须", "不能"]):
            score += 10
    return score


def load_codex() -> list[dict]:
    rows = json.loads(CODEX_ENTRIES.read_text(encoding="utf-8"))
    out = []
    for row in rows:
        e = json.loads(json.dumps(row, ensure_ascii=False))
        e["source_system"] = "codex"
        e["source_entry_id"] = ""
        e["evidence_level"] = e.get("evidence_level", "")
        out.append(e)
    return out


def load_claude() -> tuple[list[dict], list[dict]]:
    candidates, rejected = fusion.load_claude_candidates()
    out = []
    for e in candidates:
        e = json.loads(json.dumps(e, ensure_ascii=False))
        e["source_system"] = "claude"
        out.append(e)
    return out, rejected


def best_by_key(rows: list[dict]) -> tuple[dict[tuple[str, str, str, str, str], dict], list[dict]]:
    groups = defaultdict(list)
    for row in rows:
        groups[entry_key(row)].append(row)
    best = {}
    dupes = []
    for key, group in groups.items():
        group.sort(key=lambda e: (text_score(e.get("fields", {})), len("".join(e.get("fields", {}).values()))), reverse=True)
        best[key] = group[0]
        for row in group[1:]:
            dupes.append({"key": key_id(key), "source_system": row.get("source_system"), "source_entry_id": row.get("source_entry_id", ""), "reason": "weaker duplicate in same source"})
    return best, dupes


def compact_fields(fields: dict[str, str]) -> dict[str, str]:
    return {k: re.sub(r"\s+", " ", str(fields.get(k, "")).strip()) for k in STUDENT_KEYS}


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    codex_rows = load_codex()
    claude_rows, claude_rejected = load_claude()
    codex_by_key, codex_dupes = best_by_key(codex_rows)
    claude_by_key, claude_dupes = best_by_key(claude_rows)

    codex_keys = set(codex_by_key)
    claude_keys = set(claude_by_key)
    common_keys = sorted(codex_keys & claude_keys, key=str)
    codex_only_keys = sorted(codex_keys - claude_keys, key=str)
    claude_only_keys = sorted(claude_keys - codex_keys, key=str)

    common_path = AUDIT / "common_entry_pairs_for_student_agent.jsonl"
    with common_path.open("w", encoding="utf-8") as f:
        for idx, key in enumerate(common_keys, 1):
            c = codex_by_key[key]
            d = claude_by_key[key]
            record = {
                "pair_id": f"P{idx:04d}",
                "key": {
                    "module": key[0],
                    "node": key[1],
                    "suite": key[2],
                    "q": key[3],
                    "qtype": key[4],
                },
                "codex": {
                    "heading_base": c.get("heading_base", ""),
                    "origin": c.get("origin", ""),
                    "evidence_level": c.get("evidence_level", ""),
                    "fields": compact_fields(c.get("fields", {})),
                },
                "claude": {
                    "heading_base": d.get("heading_base", ""),
                    "source_entry_id": d.get("source_entry_id", ""),
                    "source_target_node_path": d.get("source_target_node_path", ""),
                    "evidence_level": d.get("evidence_level", ""),
                    "map_reason": d.get("map_reason", ""),
                    "fields": compact_fields(d.get("fields", {})),
                },
                "instruction": "从零基础高中生视角比较同一条目的两个版本。优先选择更清楚的材料信号、原理触发和答案落点；不要引入外部知识；不要保留审计话术。",
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def side_rows(keys: list[tuple[str, str, str, str, str]], source: str) -> list[dict]:
        side = codex_by_key if source == "codex" else claude_by_key
        rows = []
        for key in keys:
            e = side[key]
            rows.append(
                {
                    "key": {
                        "module": key[0],
                        "node": key[1],
                        "suite": key[2],
                        "q": key[3],
                        "qtype": key[4],
                    },
                    "heading_base": e.get("heading_base", ""),
                    "source_system": source,
                    "origin": e.get("origin", ""),
                    "source_entry_id": e.get("source_entry_id", ""),
                    "evidence_level": e.get("evidence_level", ""),
                    "fields": compact_fields(e.get("fields", {})),
                }
            )
        return rows

    (AUDIT / "codex_only_entries.json").write_text(json.dumps(side_rows(codex_only_keys, "codex"), ensure_ascii=False, indent=2), encoding="utf-8")
    (AUDIT / "claude_only_entries.json").write_text(json.dumps(side_rows(claude_only_keys, "claude"), ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "codex_entries": len(codex_by_key),
        "claude_entries": len(claude_by_key),
        "common_entries": len(common_keys),
        "codex_only": len(codex_only_keys),
        "claude_only": len(claude_only_keys),
        "codex_duplicate_skipped": len(codex_dupes),
        "claude_duplicate_skipped": len(claude_dupes),
        "claude_rejected_before_comparison": len(claude_rejected),
        "common_pairs_path": str(common_path),
        "codex_only_path": str(AUDIT / "codex_only_entries.json"),
        "claude_only_path": str(AUDIT / "claude_only_entries.json"),
        "common_by_module": dict(Counter(key[0] for key in common_keys)),
        "codex_only_by_module": dict(Counter(key[0] for key in codex_only_keys)),
        "claude_only_by_module": dict(Counter(key[0] for key in claude_only_keys)),
    }
    (AUDIT / "presence_diff_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 双终版条目有无差异报告",
        "",
        f"- Codex 可比较条目：{summary['codex_entries']}",
        f"- Claude 可比较条目：{summary['claude_entries']}",
        f"- 两边都有：{summary['common_entries']}",
        f"- Codex 独有：{summary['codex_only']}",
        f"- Claude 独有：{summary['claude_only']}",
        f"- Claude 预过滤拒收：{summary['claude_rejected_before_comparison']}",
        "",
        "## 输出",
        "",
        f"- 共同条目对照：`{common_path}`",
        f"- Codex 独有：`{AUDIT / 'codex_only_entries.json'}`",
        f"- Claude 独有：`{AUDIT / 'claude_only_entries.json'}`",
        f"- 摘要 JSON：`{AUDIT / 'presence_diff_summary.json'}`",
    ]
    (REPORTS / "双终版条目有无差异报告.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
