# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
INV = RUN / "01_source_inventory"
LANE = RUN / "02_codex_lane"
AGENTS = LANE / "agents"
CONTROL = RUN / "00_control"
AGENTS.mkdir(parents=True, exist_ok=True)


def rows(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open("r", encoding="utf-8-sig", newline="")))


def write_csv(path: Path, data: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(data)


def old_second_mock_counts() -> Counter:
    p = Path("reports/bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23/04_fusion/fused_entries_2026_second_mock.json")
    if not p.exists():
        return Counter()
    data = json.loads(p.read_text(encoding="utf-8"))
    out = Counter()
    for item in data:
        src = item.get("source", "")
        key = src.split(" 第")[0]
        out[key] += 1
    return out


def fmt(row: dict) -> str:
    q = row.get("question_no", "")
    qtxt = f"第{q}题" if q and q != "unknown" else "题号待回源定位"
    terms = row.get("terms", "")
    note = row.get("note", "").replace("\n", " ")[:220]
    return f"- {row['suite']} {qtxt} | {row['evidence_level']} | {terms} | {note}"


def main() -> int:
    matrix = rows(LANE / "codex_a_coverage_matrix.csv")
    source = rows(INV / "source_suite_inventory.csv")
    extract = rows(INV / "source_text_extraction_ledger.csv")

    yi = "一模"
    er = "二模"
    strong = "philosophy_candidate"
    no_base = "base_no_local_match"

    first_strong_no_base = [r for r in matrix if r["phase"] == yi and r["base_status"] == no_base and r["module_judgment"] == strong]
    first_patch_no_base = [r for r in matrix if r["phase"] == yi and r["base_status"] == no_base and r["patch_term_hit"] == "yes"]
    second_strong = [r for r in matrix if r["phase"] == er and r["module_judgment"] == strong]
    second_patch = [r for r in matrix if r["phase"] == er and r["patch_term_hit"] == "yes"]
    all_second = [r for r in matrix if r["phase"] == er]

    source_counts = Counter((r["year"], r["phase"]) for r in source)
    extract_status = Counter(r["status"] for r in extract)
    old_counts = old_second_mock_counts()

    write_csv(
        LANE / "codex_a_review_queue.csv",
        first_strong_no_base + first_patch_no_base + second_strong + second_patch,
        ["suite", "year", "phase", "question_no", "module_judgment", "evidence_level", "base_status", "proposed_framework_node", "decision", "terms", "source_kinds", "patch_term_hit", "note"],
    )

    worker = [
        "# Codex A 劳动者报告",
        "",
        "## 已完成",
        f"- 目标套卷：{sum(source_counts.values())} 套。",
        f"- 其中 2024一模 {source_counts[('2024', yi)]} 套，2025一模 {source_counts[('2025', yi)]} 套，2026一模 {source_counts[('2026', yi)]} 套，2026二模 {source_counts[('2026', er)]} 套。",
        f"- 源文件抽取状态：{dict(extract_status)}。",
        f"- 题号级候选行：{len(matrix)} 行；其中 2026二模候选行 {len(all_second)} 行。",
        "",
        "## 2026 二模旧候选定位",
    ]
    for suite, count in sorted(old_counts.items()):
        worker.append(f"- {suite}: 旧候选 {count} 条，只能作定位，必须回源核验和加厚。")
    worker.extend([
        "",
        "## 2026 二模强候选",
        *[fmt(r) for r in second_strong],
        "",
        "## 一模母版未精确命中的强候选",
        *[fmt(r) for r in first_strong_no_base],
    ])
    (AGENTS / "worker_report.md").write_text("\n".join(worker), encoding="utf-8")

    omissions = [
        "# Codex A 一模穷尽审计清单",
        "",
        "说明：这是融合前的审计清单，不是最终结论。`base_no_local_match` 表示在 5.2 母版中没有找到“年份+区+一模+题号”的局部命中，需要回源判断是否漏收、是否非哲学、是否题号定位错误。",
        "",
        "## 强候选：需优先回源复核",
        *[fmt(r) for r in first_strong_no_base],
        "",
        "## 主次矛盾/矛盾主次方面/两点论专项但母版未精确命中",
        *[fmt(r) for r in first_patch_no_base],
    ]
    (LANE / "codex_a_first_mock_omissions.md").write_text("\n".join(omissions), encoding="utf-8")

    patcher = [
        "# Codex A 补丁者专项报告",
        "",
        "专项检查对象：主要矛盾和次要矛盾、矛盾的主要方面和次要方面、两点论与重点论、主流支流。",
        "",
        f"- 一模母版未精确命中专项行：{len(first_patch_no_base)}。",
        f"- 2026二模专项行：{len(second_patch)}。",
        "",
        "## 一模专项待核",
        *[fmt(r) for r in first_patch_no_base],
        "",
        "## 2026二模专项候选",
        *[fmt(r) for r in second_patch],
        "",
        "补丁意见：专项词只要来自正式细则/评标/讲评，融合时必须拆入对应节点；不能因为旧目录写“暂无稳定挂点”而漏收。若只是选择题正确项链或文化/选必边界，则应标注边界，不进主观题给分链。",
    ]
    (AGENTS / "patcher_report.md").write_text("\n".join(patcher), encoding="utf-8")

    governor = [
        "# Codex A Governor 预审",
        "",
        "当前不得进入最终 Word/PDF，也不得宣布全穷尽 PASS。",
        "",
        "原因：",
        "- 2026二模虽然已有 52 条旧候选和本轮源文本，但旧候选还没有完成逐条回源、加厚、节点插入裁决。",
        "- 一模审计出现母版未精确命中的强候选和专项候选，必须与 ClaudeCode B 输出对照后再裁决。",
        "- 2026西城二模评标 PDF、2026顺义二模试卷 PDF 等扫描源文本为 0，需要在后续融合前补 OCR/视觉核验或记录证据边界。",
        "",
        "允许继续：启动 ClaudeCode B 独立生产线；Codex A 可继续回源核验高优先候选。",
    ]
    (AGENTS / "governor_precheck.md").write_text("\n".join(governor), encoding="utf-8")

    (CONTROL / "PROGRESS.md").write_text(
        (CONTROL / "PROGRESS.md").read_text(encoding="utf-8")
        + "\n| 2026-05-24 | Codex A | audit_ready_for_claudecode | 已形成源清单、抽取底稿、Codex A 题号级审计、补丁者专项和 Governor 预审。 |\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
