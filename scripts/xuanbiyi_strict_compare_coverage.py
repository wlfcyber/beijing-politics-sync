from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
RUN = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16"
OUT_DIR = RUN / "11_strict_final_rebuild_2026-05-23"
SCOPE_CSV = OUT_DIR / "02_subjective_question_scope.csv"
DIFF_CSV = OUT_DIR / "03_coverage_diff.csv"
DIFF_MD = OUT_DIR / "03_coverage_diff.md"
STUDENT = RUN / "06_final_handbook" / "选必一_当代国际政治与经济_主观题术语宝典_学生版.md"
ANTIMERGE = RUN / "06_final_handbook" / "选必一_反合并与覆盖复核_2026-05-23.md"
SECOND_SCOPE = RUN / "08_2026_second_mock_backfill" / "08_full_scope_recheck" / "FULL_2026_SECOND_MOCK_QUESTION_SCOPE.csv"

DISTRICTS = [
    "东城",
    "西城",
    "朝阳",
    "海淀",
    "丰台",
    "石景山",
    "门头沟",
    "房山",
    "通州",
    "顺义",
    "昌平",
    "大兴",
    "怀柔",
    "平谷",
    "密云",
    "延庆",
    "燕山",
]


@dataclass
class DiffRow:
    suite: str
    question: str
    normalized_key: str
    likely_xuanbiyi: str
    matched_terms: str
    evidence_status: str
    current_status: str
    reason: str
    next_action: str
    scoring_evidence: str
    paper_evidence: str


def normalize(text: str) -> str:
    text = re.sub(r"\s+", "", text or "")
    text = text.replace("第", "").replace("题", "")
    text = text.replace("（", "(").replace("）", ")")
    text = re.sub(r"问$", "", text)
    return text


def normalize_key(text: str) -> str | None:
    compact = normalize(text)
    year = re.search(r"20\d{2}", compact)
    if not year:
        return None
    district = next((d for d in DISTRICTS if d in compact), "")
    stage_match = re.search(r"(一模|二模|期中|期末|适应性)", compact)
    q_match = re.search(r"Q(1[6-9]|2[0-2])", compact)
    if not q_match:
        stage_pos = stage_match.end()
        q_match = re.search(r"(?:第)?(1[6-9]|2[0-2])", compact[stage_pos:])
    if not district or not stage_match or not q_match:
        return None
    return f"{year.group(0)}{district}{stage_match.group(1)}Q{int(q_match.group(1))}"


def keys_from_text(text: str) -> set[str]:
    keys: set[str] = set()
    patterns = [
        r"20\d{2}[^；;\n，,。]*?(?:一模|二模|期中|期末|适应性)[^；;\n，,。]*?(?:Q|第)?(?:1[6-9]|2[0-2])",
        r"20\d{2}[\u4e00-\u9fff]{2,4}(?:一模|二模|期中|期末|适应性)Q(?:1[6-9]|2[0-2])",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            key = normalize_key(match.group(0))
            if key:
                keys.add(key)
    return keys


def current_main_keys() -> set[str]:
    if not STUDENT.exists():
        return set()
    text = STUDENT.read_text(encoding="utf-8", errors="replace")
    keys = set()
    for line in text.splitlines():
        if line.startswith("### ") or line.startswith("【来源】"):
            keys |= keys_from_text(line)
    return keys


def antimerge_keys() -> set[str]:
    if not ANTIMERGE.exists():
        return set()
    text = ANTIMERGE.read_text(encoding="utf-8", errors="replace")
    capture = False
    keys: set[str] = set()
    for line in text.splitlines():
        if "仍残留的 12 处合并题例" in line:
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            keys |= keys_from_text(line)
    return keys


def second_mock_decisions() -> dict[str, str]:
    decisions: dict[str, str] = {}
    if not SECOND_SCOPE.exists():
        return decisions
    with SECOND_SCOPE.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            key = normalize_key(f"{row['district']}{row['question']}")
            if key:
                decisions[key] = row["current_decision"]
    return decisions


def classify(row: dict[str, str], main: set[str], anti: set[str], second: dict[str, str]) -> tuple[str, str, str]:
    key = normalize_key(f"{row['suite']}{row['question']}")
    if not key:
        return "needs_manual_key_review", "套卷或题号无法规范化", "人工修正套卷键"
    if key in main:
        return "already_in_main", "当前学生主表已有该题源", "保持，后续只做证据抽检"
    if key in anti:
        return "needs_rebuild_antimerge", "属于12个反合并残留或其题源之一，已从主表暂移出", "建立回源重做包"
    if key in second:
        decision = second[key]
        if "必须补录" in decision:
            return "must_backfill", "2026二模复查表标为必须补录", "进入BATCH_015"
        if "重点补录" in decision or "复核候选" in decision or "降级" in decision:
            return "candidate_review", f"2026二模复查表状态：{decision}", "进入BATCH_015裁决"
        if "已纳入" in decision:
            return "already_in_main_or_batch014", "2026二模复查表标为已纳入", "核验当前主表是否同步"
    if row["evidence_status"] == "scoring_not_located":
        return "evidence_not_located", "当前自动抽取未定位细则", "回源OCR/渲染页继续找细则"
    if row["evidence_status"] == "answer_only":
        return "answer_only_needs_rubric", "当前仅定位普通答案", "继续寻找细则，未定位前不入主表"
    if row["likely_xuanbiyi"] == "candidate_xuanbiyi_review":
        return "candidate_review", "有细则且命中选必一相关词，但当前主表未见该题源", "人工+模型判断是否补录"
    return "strict_exclude_or_other_module", "有细则但未命中选必一核心词或疑似其他模块", "保留排除证据，必要时抽检"


def main() -> None:
    main_keys = current_main_keys()
    anti_keys = antimerge_keys()
    second = second_mock_decisions()
    rows: list[DiffRow] = []
    with SCOPE_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        for item in csv.DictReader(f):
            key = normalize_key(f"{item['suite']}{item['question']}") or ""
            status, reason, action = classify(item, main_keys, anti_keys, second)
            rows.append(
                DiffRow(
                    suite=item["suite"],
                    question=item["question"],
                    normalized_key=key,
                    likely_xuanbiyi=item["likely_xuanbiyi"],
                    matched_terms=item["matched_terms"],
                    evidence_status=item["evidence_status"],
                    current_status=status,
                    reason=reason,
                    next_action=action,
                    scoring_evidence=item["scoring_evidence"],
                    paper_evidence=item["paper_evidence"],
                )
            )

    fields = list(DiffRow.__dataclass_fields__.keys())
    with DIFF_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)

    counts = Counter(row.current_status for row in rows)
    lines = [
        "# 选必一严格最终版覆盖对照",
        "",
        f"- 当前主表题源键：{len(main_keys)}",
        f"- 反合并回源队列题源键：{len(anti_keys)}",
        f"- 对照题目行：{len(rows)}",
        "",
        "## 状态统计",
        "",
        "| 状态 | 数量 |",
        "|---|---:|",
    ]
    for status, count in counts.most_common():
        lines.append(f"| {status} | {count} |")

    lines.extend(
        [
            "",
            "## 必须进入后续处理队列",
            "",
            "| 套卷 | 题号 | 状态 | 原因 |",
            "|---|---|---|---|",
        ]
    )
    queue_status = {
        "needs_rebuild_antimerge",
        "must_backfill",
        "candidate_review",
        "answer_only_needs_rubric",
        "evidence_not_located",
    }
    for row in rows:
        if row.current_status in queue_status:
            lines.append(f"| {row.suite} | {row.question} | {row.current_status} | {row.reason} |")
    DIFF_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"rows={len(rows)}")
    print(f"main_keys={len(main_keys)}")
    print(f"anti_keys={len(anti_keys)}")
    print(dict(counts))
    print(DIFF_CSV)
    print(DIFF_MD)


if __name__ == "__main__":
    main()
