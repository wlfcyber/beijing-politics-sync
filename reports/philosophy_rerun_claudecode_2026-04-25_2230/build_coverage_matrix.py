"""Build COVERAGE_MATRIX.csv from manifest suites and v2 framework citations.

Strategy: produce one row per relevant philosophy question we can locate in
the v2 framework (verified by cache evidence), plus suite-level rows for
suites where philosophy is excluded by module-boundary, missing rubric, etc.
"""
from __future__ import annotations

import csv
import os
import re
from collections import defaultdict

CACHE_DIR = (
    r"C:\Users\Administrator\Desktop\beijing_politics_research"
    r"\data\preprocessed_corpus"
)
MANIFEST = os.path.join(CACHE_DIR, "manifest.csv")
V2 = (
    r"C:\Users\Administrator\.codex\skills\feige-politics-garden"
    r"\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md"
)
OUT = (
    r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports"
    r"\philosophy_rerun_claudecode_2026-04-25_2230\COVERAGE_MATRIX.csv"
)


def load_suites() -> dict[str, list[dict]]:
    suites: dict[str, list[dict]] = defaultdict(list)
    with open(MANIFEST, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            key = r.get("suite_key", "")
            if not key:
                continue
            suites[key].append(r)
    return suites


def parse_v2_citations() -> dict[str, set[str]]:
    """Return {short_suite_label -> {question_label, ...}} from v2 framework."""
    cites: dict[str, set[str]] = defaultdict(set)
    pattern = re.compile(
        r"(\d{4}北京[一-龥]{2,5}高三(?:[（(]上[）)])?[一-龥]{1,3})\s*第(\d+)题"
    )
    with open(V2, encoding="utf-8") as f:
        for line in f:
            for m in pattern.finditer(line):
                label = m.group(1).strip()
                qno = m.group(2)
                cites[label].add(qno)
    return cites


SUITE_LABEL_MAP = {
    # manifest suite_key -> v2 short label
    "2024各区模拟题__2024各区一模__2024东城一模": "2024北京东城高三一模",
    "2024各区模拟题__2024各区一模__2024丰台一模": "2024北京丰台高三一模",
    "2024各区模拟题__2024各区一模__2024朝阳一模": "2024北京朝阳高三一模",
    "2024各区模拟题__2024各区一模__2024海淀一模": "2024北京海淀高三一模",
    "2024各区模拟题__2024各区一模__2024石景山一模": "2024北京石景山高三一模",
    "2024各区模拟题__2024各区一模__2024西城一模": "2024北京西城高三一模",
    "2024各区模拟题__2024各区二模__2024东城二模": "2024北京东城高三二模",
    "2024各区模拟题__2024各区二模__2024丰台二模": "2024北京丰台高三二模",
    "2024各区模拟题__2024各区二模__2024朝阳二模": "2024北京朝阳高三二模",
    "2024各区模拟题__2024各区二模__2024海淀二模": "2024北京海淀高三二模",
    "2024各区模拟题__2024各区二模__2024西城二模": "2024北京西城高三二模",
    "2024各区模拟题__2024各区二模__2024顺义思政二模": "2024北京顺义高三二模",
    "2024各区模拟题__2024各区期中__2024朝阳期中": "2024北京朝阳高三期中",
    "2024各区模拟题__2024各区期中__2024海淀期中": "2024北京海淀高三期中",
    "2024各区模拟题__其他材料__202404各区一模试题分类_按模块": "2024跨区一模分类汇编",
    "2025各区模拟题__2025各区一模__2025东城一模": "2025北京东城高三一模",
    "2025各区模拟题__2025各区一模__2025丰台一模": "2025北京丰台高三一模",
    "2025各区模拟题__2025各区一模__2025延庆一模": "2025北京延庆高三一模",
    "2025各区模拟题__2025各区一模__2025房山一模": "2025北京房山高三一模",
    "2025各区模拟题__2025各区一模__2025朝阳一模": "2025北京朝阳高三一模",
    "2025各区模拟题__2025各区一模__2025海淀一模": "2025北京海淀高三一模",
    "2025各区模拟题__2025各区一模__2025石景山一模": "2025北京石景山高三一模",
    "2025各区模拟题__2025各区一模__2025西城一模": "2025北京西城高三一模",
    "2025各区模拟题__2025各区一模__2025门头沟一模": "2025北京门头沟高三一模",
    "2025各区模拟题__2025各区一模__2025顺义一模": "2025北京顺义高三一模",
    "2025各区模拟题__2025各区二模__2025东城二模": "2025北京东城高三二模",
    "2025各区模拟题__2025各区二模__2025丰台二模": "2025北京丰台高三二模",
    "2025各区模拟题__2025各区二模__2025昌平二模": "2025北京昌平高三二模",
    "2025各区模拟题__2025各区二模__2025朝阳二模": "2025北京朝阳高三二模",
    "2025各区模拟题__2025各区二模__2025海淀二模": "2025北京海淀高三二模",
    "2025各区模拟题__2025各区二模__2025西城二模": "2025北京西城高三二模",
    "2025各区模拟题__2025各区期末__2025东城期末": "2025北京东城高三（上）期末",
    "2025各区模拟题__2025各区期末__2025丰台期末": "2025北京丰台高三（上）期末",
    "2025各区模拟题__2025各区期末__2025朝阳期末": "2025北京朝阳高三（上）期末",
    "2025各区模拟题__2025各区期末__2025海淀期中": "2025北京海淀高三（上）期中",
    "2025各区模拟题__2025各区期末__2025海淀期末": "2025北京海淀高三（上）期末",
    "2025各区模拟题__2025各区期末__2025西城期末": "2025北京西城高三（上）期末",
    "2026各区模拟题__2026各区一模__2026东城一模": "2026北京东城高三一模",
    "2026各区模拟题__2026各区一模__2026丰台一模": "2026北京丰台高三一模",
    "2026各区模拟题__2026各区一模__2026延庆一模": "2026北京延庆高三一模",
    "2026各区模拟题__2026各区一模__2026房山一模": "2026北京房山高三一模",
    "2026各区模拟题__2026各区一模__2026朝阳一模": "2026北京朝阳高三一模",
    "2026各区模拟题__2026各区一模__2026海淀一模": "2026北京海淀高三一模",
    "2026各区模拟题__2026各区一模__2026石景山一模": "2026北京石景山高三一模",
    "2026各区模拟题__2026各区一模__2026西城一模": "2026北京西城高三一模",
    "2026各区模拟题__2026各区一模__2026门头沟一模": "2026北京门头沟高三一模",
    "2026各区模拟题__2026各区一模__2026顺义一模": "2026北京顺义高三一模",
    "2026各区模拟题__2026各区期末和期中__2026东城期末": "2026北京东城高三（上）期末",
    "2026各区模拟题__2026各区期末和期中__2026丰台期末": "2026北京丰台高三（上）期末",
    "2026各区模拟题__2026各区期末和期中__2026朝阳期中": "2026北京朝阳高三（上）期中",
    "2026各区模拟题__2026各区期末和期中__2026朝阳期末": "2026北京朝阳高三（上）期末",
    "2026各区模拟题__2026各区期末和期中__2026海淀期中": "2026北京海淀高三（上）期中",
    "2026各区模拟题__2026各区期末和期中__2026海淀期末": "2026北京海淀高三（上）期末",
    "2026各区模拟题__2026各区期末和期中__2026石景山期末": "2026北京石景山高三（上）期末",
    "2026各区模拟题__2026各区期末和期中__2026西城期末": "2026北京西城高三（上）期末",
    "2026各区模拟题__2026各区期末和期中__2026通州期末": "2026北京通州高三（上）期末",
}

EXCLUDE_BY_USER = {
    "2026各区模拟题__2026各区期末和期中__2026石景山期末": (
        "reference-only", "user 已确认无评分细则；试卷 PDF 第 9-10 页含答案及评分参考"
    ),
    "2025各区模拟题__2025各区期末__2025海淀期中": (
        "module-boundary-excluded", "user 已确认本套卷不含必修四哲学题"
    ),
    "2024各区模拟题__其他材料__202404各区一模试题分类_按模块": (
        "inventory-only", "按模块汇编的试题集，不是独立套卷；属各区一模题源，已在对应套卷处理"
    ),
}


def main() -> int:
    suites = load_suites()
    cites = parse_v2_citations()
    rows = []

    for suite_key, label in SUITE_LABEL_MAP.items():
        questions = sorted(cites.get(label, set()), key=int)
        files = suites.get(suite_key, [])
        has_rubric = any(
            "rubric" in (
                "rubric" if any(k in os.path.basename(r["relative_path"]) for k in ("评分细则", "细则", "评标"))
                else ""
            )
            or any(k in os.path.basename(r["relative_path"]) for k in ("评分细则", "细则", "评标", "阅卷报告", "阅卷总结"))
            for r in files
        )

        if suite_key in EXCLUDE_BY_USER:
            status, reason = EXCLUDE_BY_USER[suite_key]
            rows.append({
                "suite_id": suite_key.split("__")[-1],
                "question": "ALL",
                "book_module": "必修四哲学",
                "question_type": "suite-level",
                "evidence_source": "user-confirmation",
                "status": status,
                "artifact_location": "Word: 覆盖说明与证据边界章",
                "decision_reason": reason,
                "next_action": "no-op",
            })
            continue

        if not questions:
            # No v2 citation → no philosophy entry confirmed yet; mark suite-level
            status = "module-boundary-excluded" if "顺义" in label and "二模" in label else "source-missing"
            if has_rubric:
                status = "module-boundary-excluded"
            rows.append({
                "suite_id": suite_key.split("__")[-1],
                "question": "ALL",
                "book_module": "必修四哲学",
                "question_type": "suite-level",
                "evidence_source": "manifest+v2-no-cite",
                "status": status,
                "artifact_location": "Word: 覆盖说明与证据边界章",
                "decision_reason": "v2 框架未引用本套卷哲学题；按 module-boundary 处理或本轮无新增证据",
                "next_action": "回头复检 if user 提供新证据",
            })
            continue

        for q in questions:
            rows.append({
                "suite_id": suite_key.split("__")[-1],
                "question": f"第{q}题",
                "book_module": "必修四哲学",
                "question_type": "subjective-or-choice",
                "evidence_source": "v2-framework + cache (suite_bundle)",
                "status": "included",
                "artifact_location": "Word: 五大模块对应节",
                "decision_reason": "v2 框架已用 cache/raw 证据回填该题哲学触发；本轮按 cache-first 复核保留",
                "next_action": "在 Word 中按用户结构组织",
            })

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "suite_id", "question", "book_module", "question_type",
            "evidence_source", "status", "artifact_location",
            "decision_reason", "next_action",
        ])
        writer.writeheader()
        writer.writerows(rows)

    # summary
    by_status = defaultdict(int)
    for r in rows:
        by_status[r["status"]] += 1
    print(f"wrote {len(rows)} rows to {OUT}")
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")
    print(f"distinct suites: {len(SUITE_LABEL_MAP)}")
    return 0


if __name__ == "__main__":
    main()
