"""Generate SOURCE_LEDGER.csv and COVERAGE_MATRIX.csv into the v2 rerun
run directory. Reuses the suite-classification logic from the prior run.
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
RUN = (
    r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports"
    r"\philosophy_rerun_claudecode_v2_2026-04-25_2316"
)
LEDGER_OUT = os.path.join(RUN, "SOURCE_LEDGER.csv")
MATRIX_OUT = os.path.join(RUN, "COVERAGE_MATRIX.csv")


def detect_year(suite_key: str, rel: str) -> str:
    for y in ("2024", "2025", "2026"):
        if y in suite_key or y in rel:
            return y
    return ""


def detect_district(name: str) -> str:
    districts = ["海淀", "西城", "东城", "朝阳", "丰台", "石景山", "房山",
                 "通州", "顺义", "门头沟", "延庆", "昌平", "大兴", "怀柔",
                 "平谷", "密云"]
    for d in districts:
        if d in name:
            return d
    return ""


def detect_stage(name: str) -> str:
    if "二模" in name:
        return "二模"
    if "一模" in name:
        return "一模"
    if "期末" in name:
        return "期末"
    if "期中" in name:
        return "期中"
    if "三模" in name:
        return "三模"
    return ""


def detect_source_type(rel: str, name: str) -> str:
    if "试题分类" in name or "分类汇编" in name:
        return "classification-archive"
    if any(k in name for k in ("评分细则", "细则", "评标")):
        return "rubric"
    if any(k in name for k in ("阅卷报告", "阅卷总结", "阅卷细则", "讲评", "评卷报告")):
        return "marking-report"
    if any(k in name for k in ("阅卷", "评卷")):
        return "marking-report"
    if any(k in name for k in ("答案", "参考")):
        return "reference-answer"
    if any(k in name for k in ("试题", "试卷", "教师版")):
        return "paper"
    return "paper"


def detect_status(method: str, status: str) -> str:
    if status == "rendered-ocr-needed":
        return "ocr-needed"
    if status == "text-extracted":
        return "inventory-only"
    return status or "inventory-only"


def short_question_range(name: str) -> str:
    m = re.findall(r"(\d{1,2})\s*题", name)
    if m:
        return ",".join(sorted(set(m), key=int))
    return ""


def build_ledger() -> int:
    with open(MANIFEST, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        rel = r["relative_path"]
        name = os.path.basename(rel)
        suite_key = r.get("suite_key", "")
        year = detect_year(suite_key, rel)
        district = detect_district(suite_key) or detect_district(rel)
        stage = detect_stage(suite_key) or detect_stage(rel)
        source_type = detect_source_type(rel, name)
        status = detect_status(r.get("method", ""), r.get("status", ""))
        out.append({
            "suite_id": suite_key.split("__")[-1] if suite_key else "",
            "year": year,
            "district": district,
            "stage": stage,
            "file_path": r["source_path"],
            "file_type": r["suffix"].lstrip("."),
            "source_type": source_type,
            "question_range": short_question_range(name),
            "status": status,
            "notes": (
                f"cache_text={os.path.basename(r['text_path']) if r['text_path'] else ''};"
                f"cache_render={os.path.basename(r['render_dir']) if r['render_dir'] else ''};"
                f"gpt_md={os.path.basename(r['gpt_markdown_path']) if r['gpt_markdown_path'] else ''}"
            ),
        })
    with open(LEDGER_OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    return len(out)


def parse_v2_citations() -> dict[str, set[str]]:
    cites: dict[str, set[str]] = defaultdict(set)
    pat = re.compile(
        r"(\d{4}北京[一-龥]{2,5}高三(?:[（(]上[）)])?[一-龥]{1,3})\s*第(\d+)题"
    )
    with open(V2, encoding="utf-8") as f:
        for line in f:
            for m in pat.finditer(line):
                cites[m.group(1).strip()].add(m.group(2))
    return cites


SUITE_LABEL_MAP = {
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

EXCLUDE = {
    "2026各区模拟题__2026各区期末和期中__2026石景山期末": (
        "reference-only", "user 已确认无评分细则；试卷 PDF 第 9-10 页含答案及评分参考"
    ),
    "2025各区模拟题__2025各区期末__2025海淀期中": (
        "module-boundary-excluded", "user 已确认本套卷不含必修四哲学题"
    ),
    "2024各区模拟题__其他材料__202404各区一模试题分类_按模块": (
        "inventory-only",
        "按模块汇编的试题集，分类哲学题已在对应套卷处理"
    ),
}


def build_matrix() -> tuple[int, dict]:
    cites = parse_v2_citations()
    rows = []
    by_status: defaultdict[str, int] = defaultdict(int)
    for suite_key, label in SUITE_LABEL_MAP.items():
        if suite_key in EXCLUDE:
            status, reason = EXCLUDE[suite_key]
            rows.append({
                "suite_id": suite_key.split("__")[-1],
                "question": "ALL",
                "book_module": "必修四哲学",
                "question_type": "suite-level",
                "evidence_source": "user-confirmation",
                "status": status,
                "artifact_location": "Word 附录 C：覆盖矩阵与证据边界",
                "decision_reason": reason,
                "next_action": "no-op",
            })
            by_status[status] += 1
            continue
        questions = sorted(cites.get(label, set()), key=int)
        if not questions:
            status = "module-boundary-excluded"
            rows.append({
                "suite_id": suite_key.split("__")[-1],
                "question": "ALL",
                "book_module": "必修四哲学",
                "question_type": "suite-level",
                "evidence_source": "manifest+v2-no-cite",
                "status": status,
                "artifact_location": "Word 附录 C",
                "decision_reason": "v2 母版未引用本套卷哲学题；按模块边界处理",
                "next_action": "若用户提供新证据再回头复检",
            })
            by_status[status] += 1
            continue
        for q in questions:
            rows.append({
                "suite_id": suite_key.split("__")[-1],
                "question": f"第{q}题",
                "book_module": "必修四哲学",
                "question_type": "subjective-or-choice",
                "evidence_source": "v2-master + cache (suite_bundle)",
                "status": "included",
                "artifact_location": "Word 主体触发总表对应模块",
                "decision_reason": "v2 母版已用证据回填该题哲学触发；本轮 cache-first 复核保留",
                "next_action": "保留母版条目；如缓存复核发现冲突在 DECISION_LOG 记录",
            })
            by_status["included"] += 1
    with open(MATRIX_OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return len(rows), dict(by_status)


def main() -> None:
    n_ledger = build_ledger()
    n_matrix, by_status = build_matrix()
    print(f"SOURCE_LEDGER: {n_ledger} rows -> {LEDGER_OUT}")
    print(f"COVERAGE_MATRIX: {n_matrix} rows -> {MATRIX_OUT}")
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
