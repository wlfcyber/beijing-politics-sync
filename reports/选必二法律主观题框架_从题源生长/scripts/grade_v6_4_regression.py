from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
TEST_DIR = ROOT / "10_framework_validation" / "v6_4_regression_naked_test_20260521"
ANSWERS = TEST_DIR / "student_answers_CEGH_v6_4_regression_20260521.md"
KEY = TEST_DIR / "internal_grading_key_CEGH_v6_4_regression_20260521.csv"
OUT_CSV = TEST_DIR / "grading_report_CEGH_v6_4_regression_20260521.csv"
OUT_MD = TEST_DIR / "grading_report_CEGH_v6_4_regression_20260521.md"
VERDICT = TEST_DIR / "V6_4_REGRESSION_VERDICT_20260521.md"


CHECKS = {
    "样题 1": {
        "must": ["要约", "承诺", "合同", "有效", "违约", "侵权", "损害", "因果", "证据", "起诉"],
        "good_any": [("生产者", "无过错"), ("产品责任", "无过错")],
        "bad": ["销售者承担无过错责任", "刘某承担无过错责任", "过错推定", "欺诈"],
        "core_test": "C：合同/侵权/维权两问与产品责任条件辨析",
    },
    "样题 2": {
        "must": ["自愿参加", "安全保障", "故意", "重大过失", "自身原因", "因果", "不承担", "公平", "社区"],
        "good_any": [],
        "bad": ["如果表格要求", "如果要求", "商业经营者", "当然承担"],
        "core_test": "E：表格题逐格直填",
    },
    "样题 3": {
        "must": ["权利边界", "相邻", "合理", "有利生产", "方便生活", "团结互助", "公平合理", "调解", "企业名称", "行政裁决", "诉讼", "多元", "和谐"],
        "good_any": [],
        "bad": ["法治中国", "全面依法治国"],
        "core_test": "G：定分止争干净材料与相邻原则",
    },
    "样题 4": {
        "must": ["AI不能", "著作权主体", "自然人", "法人", "非法人组织", "智力成果", "独创", "信息网络传播权", "署名权", "信用卡", "合同", "有效", "违约", "诚信", "全面履行"],
        "good_any": [],
        "bad": ["AI享有著作权", "AI自动享有", "刑事诈骗"],
        "core_test": "H：AI主体排除前置与信用卡违约表格",
    },
}


def norm(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def answer_body_only(answer: str) -> str:
    """Bad phrases in the student's explicit caution section are not wrong answers."""
    markers = ["我不敢乱写/需要刹车的地方：", "我不敢乱写/需要刹车的地方:"]
    body = answer
    for marker in markers:
        if marker in body:
            body = body.split(marker, 1)[0]
            break
    return body


def phrase_is_negated(compact: str, phrase: str) -> bool:
    idx = compact.find(norm(phrase))
    if idx < 0:
        return False
    window = compact[max(0, idx - 18) : idx]
    return any(x in window for x in ["不敢", "不能", "不要", "不应", "不得", "刹车", "排除"])


def has_unnegated_phrase(compact: str, phrase: str) -> bool:
    target = norm(phrase)
    start = 0
    while True:
        idx = compact.find(target, start)
        if idx < 0:
            return False
        window = compact[max(0, idx - 18) : idx]
        if not any(x in window for x in ["不敢", "不能", "不要", "不应", "不得", "刹车", "排除"]):
            return True
        start = idx + len(target)


def split_answers(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(样题\s+\d+)\s*$", text, flags=re.M))
    parts: dict[str, str] = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        parts[m.group(1)] = text[start:end].strip()
    return parts


def judge(label: str, answer: str) -> dict[str, str]:
    rule = CHECKS[label]
    compact = norm(answer)
    body_compact = norm(answer_body_only(answer))
    hits = [kw for kw in rule["must"] if norm(kw) in compact]
    misses = [kw for kw in rule["must"] if norm(kw) not in compact]
    bad_hits = [kw for kw in rule["bad"] if has_unnegated_phrase(body_compact, kw)]
    good_any_missing = []
    for group in rule["good_any"]:
        if not all(norm(x) in compact for x in group):
            good_any_missing.append("+".join(group))

    table_direct = "不适用"
    if label in {"样题 2", "样题 4"}:
        table_direct = "yes" if "|" in answer or "（1）" in answer or "(1)" in answer else "uncertain"
        if any(has_unnegated_phrase(body_compact, x) for x in ["如果表格要求", "如果要求"]):
            table_direct = "no"

    # Human-readable synonym adjustments for this narrow C/E/G/H regression.
    if label == "样题 2":
        if "基础心脏病" in compact or "突发倒地" in compact:
            if "自身原因" in misses:
                misses.remove("自身原因")
                hits.append("自身原因[同义:基础心脏病/突发]")
    if label == "样题 4":
        for kw in ["法人", "非法人组织"]:
            if kw in misses and "AI不能成为著作权主体" in compact:
                misses.remove(kw)
                hits.append(f"{kw}[由AI主体排除句概括]")
        if "智力成果" in misses and ("智力投入" in compact or "创作劳动" in compact):
            misses.remove("智力成果")
            hits.append("智力成果[同义:智力投入/创作劳动]")

    if bad_hits:
        status = "FAIL"
    elif not misses and not good_any_missing and table_direct != "no":
        status = "PASS"
    elif len(misses) <= 4 and table_direct != "no":
        status = "PARTIAL"
    else:
        status = "FAIL"

    return {
        "sample": label,
        "core_test": rule["core_test"],
        "keyword_hits": "；".join(hits),
        "keyword_misses": "；".join(misses),
        "bad_hits": "；".join(bad_hits),
        "conditional_misses": "；".join(good_any_missing),
        "table_direct_fill": table_direct,
        "pass_status": status,
    }


def main() -> None:
    if not ANSWERS.exists():
        raise SystemExit(f"missing answers: {ANSWERS}")
    answers = split_answers(ANSWERS.read_text(encoding="utf-8"))
    rows = []
    for label in ["样题 1", "样题 2", "样题 3", "样题 4"]:
        rows.append(judge(label, answers.get(label, "")))

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    counts = {s: sum(1 for r in rows if r["pass_status"] == s) for s in ["PASS", "PARTIAL", "FAIL"]}
    overall = "PASS" if counts["FAIL"] == 0 and counts["PARTIAL"] == 0 else "CONDITIONAL_PASS" if counts["FAIL"] == 0 else "FAIL"

    lines = [
        "# V6.4 C/E/G/H 回归盲测阅卷报告",
        "",
        f"- 学生答案：`{ANSWERS}`",
        f"- 评分钥匙：`{KEY}`",
        f"- 总判：`{overall}`",
        f"- 统计：PASS={counts['PASS']}；PARTIAL={counts['PARTIAL']}；FAIL={counts['FAIL']}",
        "",
        "| 样题 | 检验点 | 命中 | 缺漏 | 错误命中 | 表格直填 | 判定 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        lines.append(
            f"| {r['sample']} | {r['core_test']} | {r['keyword_hits'] or '无'} | {r['keyword_misses'] or '无'}"
            f" | {r['bad_hits'] or '无'}{('；条件缺漏：' + r['conditional_misses']) if r['conditional_misses'] else ''}"
            f" | {r['table_direct_fill']} | {r['pass_status']} |"
        )
    lines.extend(
        [
            "",
            "## 裁定",
            "",
            "- `PASS`：允许进入下一轮干净学生版整理，但仍需保留 27 core + 38 guard/index 表述。",
            "- `CONDITIONAL_PASS`：先按缺漏补 V6.5，再做最小回归。",
            "- `FAIL`：禁止 Word/PDF，回到 V6.4 逐题修。",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    VERDICT.write_text(
        "# V6.4 回归盲测裁定\n\n"
        f"总判：`{overall}`。\n\n"
        f"- PASS={counts['PASS']}\n- PARTIAL={counts['PARTIAL']}\n- FAIL={counts['FAIL']}\n\n"
        f"详见：`{OUT_MD}`。\n",
        encoding="utf-8",
    )
    print(OUT_MD)
    print(OUT_CSV)
    print(VERDICT)


if __name__ == "__main__":
    main()
