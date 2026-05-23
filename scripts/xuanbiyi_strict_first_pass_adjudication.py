from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


REPORT_ROOT_NAME = "11_strict_final_rebuild_2026-05-23"
OTHER_MODULE_RE = re.compile(
    r"《(?:经济与社会|政治与法治|法律与生活|哲学与文化|逻辑与思维)》|"
    r"运用(?:经济与社会|政治与法治|法律与生活|哲学与文化|科学思维|法治|哲学|文化)知识"
)
XUANBIYI_RE = re.compile(r"《当代国际政治与经济》|当代国际政治与经济|国际政治与经济")
STRICT_SIGNAL_RE = re.compile(
    r"阅卷细则|评标|评分标准|评分细则|细则|[\d一二三四五六七八九十]分|♣|\b[1-9]\s*分"
)
XUANBIYI_TERM_RE = re.compile(
    r"经济全球化|世界多极化|国际关系|国家利益|共同利益|新型国际关系|"
    r"人类命运共同体|全球治理|多边主义|联合国|独立自主|和平共处|"
    r"对外开放|开放型世界经济|贸易.*自由化|投资.*便利化|一带一路|"
    r"国内国际两个市场|国内国际两种资源|国际经济秩序|全球产业链|供应链"
)


def report_root() -> Path:
    for root in Path("reports").glob("*2026-05-16"):
        candidate = root / REPORT_ROOT_NAME
        if candidate.exists():
            return candidate
    raise FileNotFoundError(REPORT_ROOT_NAME)


def compact(text: str, limit: int = 180) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit] + ("..." if len(text) > limit else "")


def decide(row: dict[str, str]) -> tuple[str, str]:
    source_type = row["source_type"]
    status = row["current_status"]
    paper = row.get("paper_evidence", "")
    scoring = row.get("scoring_evidence", "")
    combined = paper + "\n" + scoring
    matched = row.get("matched_terms", "")

    if source_type == "anti_merge_residual":
        return (
            "REWRITE_FROM_ORIGINAL_DRAFT_SOURCE",
            "先前合并题例的残留项，必须回到初稿/ClaudeCode独立条目重写，禁止从合并终稿望文生义拆分。",
        )

    has_xuanbiyi = bool(XUANBIYI_RE.search(combined))
    has_other = bool(OTHER_MODULE_RE.search(combined))
    has_strict = bool(scoring.strip()) and bool(STRICT_SIGNAL_RE.search(scoring))
    has_xuanbiyi_term = bool(XUANBIYI_TERM_RE.search(scoring + "\n" + matched))

    if status == "answer_only_needs_rubric":
        return (
            "NEEDS_EVIDENCE",
            "当前只有试卷/普通答案侧证据，未定位评分细则/评标/阅卷/讲评，严格口径下暂不入主表。",
        )

    if status == "evidence_not_located":
        if has_xuanbiyi or matched:
            return (
                "NEEDS_EVIDENCE",
                "题面或命中词疑似选必一，但自动抽取未定位同题细则，需要继续回源。",
            )
        return ("EXCLUDE_OTHER_MODULE_OR_UNCLEAR", "未定位细则且没有选必一题面/术语信号。")

    if has_other and not has_xuanbiyi:
        return (
            "EXCLUDE_OTHER_MODULE",
            "题面或细则明确指向其他模块，不能因出现产业链、供应链等词误归入选必一。",
        )

    if has_strict and (has_xuanbiyi or has_xuanbiyi_term):
        return (
            "INCLUDE_STRICT_REVIEW",
            "已定位细则/评标/讲评侧证据且含选必一题面或采分术语，进入模型复核和成稿队列。",
        )

    if has_strict and has_other:
        return (
            "EXCLUDE_OTHER_MODULE",
            "虽有细则，但细则模块不是选必一。",
        )

    return (
        "NEEDS_HUMAN_REVIEW",
        "自动信号不足，需人工/模型回源判断是否为选必一正式采分点。",
    )


def main() -> None:
    root = report_root()
    in_path = root / "04_review_queue.csv"
    out_csv = root / "05_codex_first_pass_adjudication.csv"
    out_md = root / "05_codex_first_pass_adjudication.md"

    with in_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    out_rows: list[dict[str, str]] = []
    for row in rows:
        decision, reason = decide(row)
        out_rows.append(
            {
                "decision": decision,
                "suite": row.get("suite", ""),
                "question": row.get("question", ""),
                "normalized_key": row.get("normalized_key", ""),
                "source_type": row.get("source_type", ""),
                "current_status": row.get("current_status", ""),
                "matched_terms": row.get("matched_terms", ""),
                "reason": reason,
                "paper_excerpt": compact(row.get("paper_evidence", "")),
                "scoring_excerpt": compact(row.get("scoring_evidence", "")),
            }
        )

    fields = list(out_rows[0].keys()) if out_rows else []
    with out_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)

    counts = Counter(row["decision"] for row in out_rows)
    lines = ["# 选必一严格最终版 Codex 第一轮证据判定", ""]
    lines.append("## 统计")
    lines.append("")
    lines.append("| 判定 | 数量 |")
    lines.append("|---|---:|")
    for key, count in counts.most_common():
        lines.append(f"| {key} | {count} |")
    lines.append("")
    lines.append("## 明细")
    lines.append("")
    lines.append("| 判定 | 套卷 | 题号/标题 | 当前状态 | 理由 |")
    lines.append("|---|---|---|---|---|")
    for row in out_rows:
        lines.append(
            "| {decision} | {suite} | {question} | {status} | {reason} |".format(
                decision=row["decision"],
                suite=row["suite"],
                question=row["question"],
                status=row["current_status"],
                reason=row["reason"],
            )
        )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"rows={len(out_rows)}")
    for key, count in counts.most_common():
        print(f"{key}={count}")
    print(out_csv.resolve())
    print(out_md.resolve())


if __name__ == "__main__":
    main()
