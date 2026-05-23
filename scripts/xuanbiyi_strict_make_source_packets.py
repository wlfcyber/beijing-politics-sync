from __future__ import annotations

import csv
import math
import re
from pathlib import Path


ROOT = Path.cwd()
RUN = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16"
OUT_DIR = RUN / "11_strict_final_rebuild_2026-05-23"
DIFF_CSV = OUT_DIR / "03_coverage_diff.csv"
PACKET_DIR = OUT_DIR / "04_source_packets"
QUEUE_CSV = OUT_DIR / "04_review_queue.csv"
QUEUE_MD = OUT_DIR / "04_review_queue.md"
ANTIMERGE = RUN / "06_final_handbook" / "选必一_合并题例_初稿回源拆分审计.md"


QUEUE_STATUSES = {"must_backfill", "candidate_review", "answer_only_needs_rubric"}


def include_in_queue(row: dict[str, str]) -> bool:
    if row["current_status"] in QUEUE_STATUSES:
        return True
    if row["current_status"] == "evidence_not_located" and row["matched_terms"].strip():
        return True
    return False


def extract_antimerge_items() -> list[dict[str, str]]:
    if not ANTIMERGE.exists():
        return []
    text = ANTIMERGE.read_text(encoding="utf-8", errors="replace")
    capture = False
    items: list[dict[str, str]] = []
    current_core = ""
    current_title = ""
    reasons: list[str] = []
    for line in text.splitlines():
        if line.strip() == "## 未拆分保留":
            capture = True
            continue
        if not capture:
            continue
        if line.startswith("### "):
            if current_core:
                items.append(
                    {
                        "source_type": "anti_merge_residual",
                        "suite": "反合并残留",
                        "question": "",
                        "current_status": "needs_rebuild_antimerge",
                        "core": current_core,
                        "original_title": current_title,
                        "reason": "\n".join(reasons),
                    }
                )
            current_core = re.sub(r"^###\s*\d+\.\s*", "", line).strip()
            current_title = ""
            reasons = []
            continue
        if current_core and line.startswith("- 原合并标题："):
            current_title = line.split("：", 1)[1].strip()
        elif current_core and line.startswith("- 原因："):
            reasons.append(line[5:].strip())
    if current_core:
        items.append(
            {
                "source_type": "anti_merge_residual",
                "suite": "反合并残留",
                "question": "",
                "current_status": "needs_rebuild_antimerge",
                "core": current_core,
                "original_title": current_title,
                "reason": "\n".join(reasons),
            }
        )
    return items


def one_line(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit]


def write_queue(rows: list[dict[str, str]], anti_items: list[dict[str, str]]) -> None:
    fields = [
        "source_type",
        "suite",
        "question",
        "normalized_key",
        "current_status",
        "matched_terms",
        "reason",
        "next_action",
        "paper_evidence",
        "scoring_evidence",
    ]
    with QUEUE_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "source_type": "coverage_diff",
                    "suite": row["suite"],
                    "question": row["question"],
                    "normalized_key": row["normalized_key"],
                    "current_status": row["current_status"],
                    "matched_terms": row["matched_terms"],
                    "reason": row["reason"],
                    "next_action": row["next_action"],
                    "paper_evidence": row["paper_evidence"],
                    "scoring_evidence": row["scoring_evidence"],
                }
            )
        for item in anti_items:
            writer.writerow(
                {
                    "source_type": item["source_type"],
                    "suite": item["suite"],
                    "question": item["original_title"],
                    "normalized_key": "",
                    "current_status": item["current_status"],
                    "matched_terms": item["core"],
                    "reason": item["reason"],
                    "next_action": "回原题和细则重做单题七字段；不得从合并稿拆句子",
                    "paper_evidence": "",
                    "scoring_evidence": "",
                }
            )

    lines = [
        "# 选必一严格最终版后续处理队列",
        "",
        f"- 覆盖缺口候选：{len(rows)}",
        f"- 反合并残留：{len(anti_items)}",
        f"- 队列总数：{len(rows) + len(anti_items)}",
        "",
        "| 类型 | 套卷 | 题号/原标题 | 状态 | 关键词/核心 |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| coverage | {row['suite']} | {row['question']} | {row['current_status']} | {row['matched_terms'] or '未命中'} |"
        )
    for item in anti_items:
        lines.append(
            f"| anti-merge | {item['suite']} | {item['original_title']} | {item['current_status']} | {item['core']} |"
        )
    QUEUE_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def packet_header(index: int, total: int) -> str:
    return f"""# 选必一严格最终版源包 {index:02d}/{total:02d}

## 任务

请只处理本包列出的主观题候选。每道题必须先裁决：

1. `INCLUDE_STRICT_MAIN`：有可核验细则/评标/阅卷/讲评中的选必一采分点，可入选必一主表。
2. `EXCLUDE_OTHER_MODULE`：属于必修二、必修三、必修四、选必二、选必三、逻辑、法律或其他模块，不入选必一主表。
3. `NEEDS_EVIDENCE`：题面疑似选必一，但本包证据不足，必须继续回源找细则。

若入主表，按六桶归类：时代背景、理论、经济全球化、政治多极化、中国、联合国。

硬规则：
- 题例层面必须单题展示，禁止把两个题合并成一个案例。
- `术语` 必须是评分源原词，不准自造概括。
- `答案句` 必须像考生卷面作答句，包含术语、本题材料事实、因果/作用/结论。
- 普通参考答案不能冒充正式细则；只能标注为降级证据或要求继续找细则。
"""


def write_packets(rows: list[dict[str, str]], anti_items: list[dict[str, str]], chunk_size: int = 8) -> None:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    combined: list[dict[str, str]] = []
    for row in rows:
        combined.append({"kind": "coverage", **row})
    for item in anti_items:
        combined.append({"kind": "anti_merge", **item})

    total = max(1, math.ceil(len(combined) / chunk_size))
    for idx in range(total):
        chunk = combined[idx * chunk_size : (idx + 1) * chunk_size]
        lines = [packet_header(idx + 1, total)]
        for n, item in enumerate(chunk, start=1):
            lines.append(f"\n## 项目 {n}")
            if item["kind"] == "coverage":
                lines.extend(
                    [
                        f"- 套卷：{item['suite']}",
                        f"- 题号：{item['question']}",
                        f"- 当前状态：{item['current_status']}",
                        f"- 命中词：{item['matched_terms'] or '未命中'}",
                        f"- 当前判断理由：{item['reason']}",
                        f"- 下一步：{item['next_action']}",
                        "",
                        "### 题面/答案侧摘录",
                        "",
                        one_line(item["paper_evidence"]) or "未从自动抽取中定位题面摘录，请回源文件。",
                        "",
                        "### 细则/评标/讲评侧摘录",
                        "",
                        one_line(item["scoring_evidence"]) or "未从自动抽取中定位细则摘录，请继续回源查找。",
                    ]
                )
            else:
                lines.extend(
                    [
                        f"- 类型：反合并残留",
                        f"- 核心答题点：{item['core']}",
                        f"- 原合并标题：{item['original_title']}",
                        f"- 未拆原因：{item['reason'] or '未记录'}",
                        "",
                        "### 必做",
                        "",
                        "回原题、原细则、原初稿或重新生成单题稿；只要能找到单题细则，就拆成单题七字段。不得从现有合并稿望文生义拆句子。",
                    ]
                )
        (PACKET_DIR / f"SOURCE_PACKET_{idx + 1:02d}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    with DIFF_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        rows = [row for row in csv.DictReader(f) if include_in_queue(row)]
    anti_items = extract_antimerge_items()
    write_queue(rows, anti_items)
    write_packets(rows, anti_items)
    print(f"coverage_queue={len(rows)}")
    print(f"anti_merge={len(anti_items)}")
    print(f"total={len(rows) + len(anti_items)}")
    print(QUEUE_CSV)
    print(QUEUE_MD)
    print(PACKET_DIR)


if __name__ == "__main__":
    main()
