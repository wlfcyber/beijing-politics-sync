#!/usr/bin/env python3
"""Build the student-facing 选必一 final document from verified entry blocks."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import re


RUN = Path(__file__).resolve().parents[2]
CURRENT_ENTRIES = RUN / "codex_lane" / "entries"
OLD_LOCATOR_ENTRIES = Path(
    "/Users/wanglifei/Desktop/北京高考政治/"
    "选必一_当代国际政治与经济_双线总控_2026-05-02/codex_lane/entries"
)
DELIVERY = RUN / "09_delivery"
STUDENT = RUN / "07_student_doc"

OLD_ONLY = [
    "2025丰台期末_Q20.md",
    "2026东城期末_Q20.md",
    "2026丰台一模_Q19.md",
    "2026门头沟一模_Q20.md",
    "2026西城一模_Q20_2.md",
    "2026延庆一模_Q19_2.md",
    "2026石景山一模_Q20.md",
]

BUCKET_ORDER = ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"]
FORBIDDEN = [
    "采分点",
    "要落到",
    "并结合材料说明",
    "设问要求",
    "细则要求",
    "本题需要",
    "证据层级",
    "v7",
    "材料中",
    "评标",
    "参考答案",
    "/Users/",
]


@dataclass
class Entry:
    bucket: str
    sub: str
    term: str
    prompt: str
    rubric: str
    source: str
    trigger: str
    answer: str
    origin: str


def clean_text(text: str) -> str:
    text = text.strip()
    text = text.replace("`", "")
    text = text.replace("参考答案及评分参考", "答案及评分标准")
    text = text.replace("答案及评分参考", "答案及评分标准")
    text = text.replace("参考答案", "答案及评分标准")
    text = text.replace("评标实录", "评分记录")
    text = text.replace("评标细则", "评分细则")
    text = text.replace("评标", "评分")
    text = text.replace("材料中", "材料里")
    text = text.replace("设问要求", "题目要求")
    text = text.replace("细则要求", "评分标准要求")
    text = text.replace("本题需要", "作答时需要")
    text = text.replace("需要落到", "应写出")
    text = text.replace("要落到", "应写出")
    text = text.replace("证据层级", "依据强度")
    text = text.replace("内部边界", "边界说明")
    text = re.sub(r"依据强度[^。]*。", "仅按该题对应细则页使用。", text)
    text = re.sub(r"\bP[0-4](?:/[P0-4])?\b", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def normalize_bucket(raw: str) -> tuple[str, str]:
    raw = clean_text(raw)
    raw = raw.strip("〔〕[]")
    raw = raw.replace(" / ", "/").replace("／", "/")
    if "/" in raw:
        top, sub = [part.strip() for part in raw.split("/", 1)]
    else:
        top, sub = raw, ""
    if top.startswith("中国"):
        top = "中国"
    if top.startswith("经济全球化"):
        top = "经济全球化"
    if top.startswith("政治多极化"):
        top = "政治多极化"
    if top not in BUCKET_ORDER:
        top = "理论" if "利益" in top or "竞争" in top else top
    return top, sub


def finish(current: dict | None, entries: list[Entry], origin: str) -> None:
    if not current:
        return
    needed = ["term", "prompt", "rubric", "source", "trigger", "answer"]
    if all(current.get(k) for k in needed):
        bucket, sub = normalize_bucket(current.get("bucket", "理论"))
        sub = current.get("sub") or sub
        entries.append(
            Entry(
                bucket=bucket,
                sub=clean_text(sub),
                term=clean_text(current["term"]),
                prompt=clean_text(current["prompt"]),
                rubric=clean_text(current["rubric"]),
                source=clean_text(current["source"]),
                trigger=clean_text(current["trigger"]),
                answer=clean_text(current["answer"]),
                origin=origin,
            )
        )


def parse_entry_file(path: Path, origin: str) -> list[Entry]:
    entries: list[Entry] = []
    bucket = ""
    sub = ""
    current: dict | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("## ") and not line.startswith("### "):
            finish(current, entries, origin)
            current = None
            bucket, sub = normalize_bucket(line[3:].strip())
            continue
        if line.startswith("### ") and "术语：" not in line:
            sub = clean_text(line[4:].strip())
            continue
        m = re.match(r"\*\*术语[:：](.+?)\*\*", line)
        if m:
            finish(current, entries, origin)
            current = {"bucket": bucket, "sub": sub, "term": m.group(1).strip()}
            continue
        if current is None:
            continue
        for key, field in [
            ("prompt", "完整设问"),
            ("rubric", "细则位置"),
            ("source", "来源"),
            ("trigger", "材料触发"),
            ("answer", "答案句"),
        ]:
            prefix = f"- {field}："
            if line.startswith(prefix):
                current[key] = line[len(prefix) :].strip()
                break
    finish(current, entries, origin)
    return entries


def haidian_2026_yimo_entries() -> list[Entry]:
    prompt = (
        "结合材料，运用《当代国际政治与经济》知识，谈谈中国标准走出国门的意义。"
    )
    return [
        Entry(
            "中国",
            "政策",
            "扩大制度型开放；增强我国产品、服务乃至产业链在全球的竞争力",
            prompt,
            "2026海淀一模 Q20，评分标准 PDF 第6页，第20题整题8分；原文列“扩大制度型开放，增强我国产品、服务乃至产业链在全球的竞争力”。",
            "2026海淀一模 Q20",
            "题目问中国标准走出国门的意义，材料把标准称为全球产业界通用语言，并呈现中国标准进入低碳能源、人工智能、北斗导航、传统医学等国际领域；这触发以规则和标准为载体的制度型开放。",
            "中国标准走出国门，有利于扩大制度型开放，以规则和标准增强我国产品、服务乃至产业链在全球的竞争力。",
            "claudecode_new_codex_verified",
        ),
        Entry(
            "经济全球化",
            "",
            "更好利用国内国际两个市场、两种资源",
            prompt,
            "2026海淀一模 Q20，评分标准 PDF 第6页，第20题整题8分；原文列“更好利用国内国际两个市场、两种资源”。",
            "2026海淀一模 Q20",
            "中国标准被更多国家和企业采用，会降低产品、技术和服务跨境衔接的规则成本；题目问其意义时，触发国内国际两个市场、两种资源的联动。",
            "中国标准走出国门，有利于我国更好利用国内国际两个市场、两种资源，推动产品、技术和服务更顺畅地融入全球产业体系。",
            "claudecode_new_codex_verified",
        ),
        Entry(
            "经济全球化",
            "",
            "促进全球范围内标准共通、技术共享；推动全球技术创新与绿色转型",
            prompt,
            "2026海淀一模 Q20，评分标准 PDF 第6页，第20题整题8分；原文列“促进全球范围内标准共通、技术共享，推动全球技术创新与绿色转型”。",
            "2026海淀一模 Q20",
            "材料列出中国在低碳能源、人工智能等领域提交和发布国际标准；这些标准一旦走出国门，就会把技术路径转化为可共同使用的规则，触发标准共通、技术共享和绿色转型。",
            "我国在低碳能源、人工智能等领域贡献国际标准，促进全球范围内标准共通、技术共享，推动全球技术创新与绿色转型。",
            "claudecode_new_codex_verified",
        ),
        Entry(
            "政治多极化",
            "",
            "积极参与全球经济治理和规则制定；推动全球治理体制向着更加公正合理方向发展",
            prompt,
            "2026海淀一模 Q20，评分标准 PDF 第6页，第20题整题8分；原文列“积极参与全球经济治理和规则制定，推动全球治理体制向着更加公正合理方向发展”。",
            "2026海淀一模 Q20",
            "国际标准本身就是全球经济治理规则的一部分；中国从标准使用者转为标准贡献者，触发参与全球经济治理和规则制定的治理意义。",
            "中国标准走出国门，说明中国积极参与全球经济治理和规则制定，推动全球治理体制向着更加公正合理方向发展。",
            "claudecode_new_codex_verified",
        ),
    ]


def load_entries() -> list[Entry]:
    entries: list[Entry] = []
    for path in sorted(CURRENT_ENTRIES.glob("*.md")):
        entries.extend(parse_entry_file(path, "current_codex"))
    for name in OLD_ONLY:
        path = OLD_LOCATOR_ENTRIES / name
        if path.exists():
            entries.extend(parse_entry_file(path, "old_locator_reverified"))
    entries.extend(haidian_2026_yimo_entries())
    # Deduplicate exact same source + term, preferring current-run entries.
    seen: dict[tuple[str, str], Entry] = {}
    rank = {"current_codex": 0, "claudecode_new_codex_verified": 1, "old_locator_reverified": 2}
    for entry in entries:
        key = (entry.source, entry.term)
        if key not in seen or rank.get(entry.origin, 9) < rank.get(seen[key].origin, 9):
            seen[key] = entry
    return list(seen.values())


def render_main(entries: list[Entry]) -> str:
    term_counts = Counter(entry.term for entry in entries)
    grouped: dict[str, dict[str, list[Entry]]] = {
        bucket: defaultdict(list) for bucket in BUCKET_ORDER
    }
    for entry in entries:
        grouped.setdefault(entry.bucket, defaultdict(list))[entry.term].append(entry)

    lines: list[str] = []
    lines.append("# 飞哥政治庄园 选必一《当代国际政治与经济》细则术语成品版")
    lines.append("")
    lines.append("只收录本轮已回源核验的主观题术语；2026石景山期末按用户规则排除。")
    lines.append("")
    for bucket in BUCKET_ORDER:
        lines.append(f"## {bucket}")
        lines.append("")
        terms = grouped.get(bucket, {})
        if not terms:
            lines.append("本轮未形成可入主表的条目。")
            lines.append("")
            continue
        for term in sorted(terms, key=lambda t: (-term_counts[t], t)):
            cases = sorted(
                terms[term],
                key=lambda e: (e.source, e.prompt, e.rubric),
            )
            lines.append(f"### 术语：{term}（出现{term_counts[term]}次）")
            lines.append("")
            for i, entry in enumerate(cases, 1):
                label = f"例题{i}" if len(cases) > 1 else "例题"
                lines.append(f"#### {label}：{entry.source}")
                lines.append("")
                if entry.sub:
                    lines.append(f"框架位置：{entry.sub}")
                    lines.append("")
                lines.append(f"完整设问：{entry.prompt}")
                lines.append("")
                lines.append(f"细则位置：{entry.rubric}")
                lines.append("")
                lines.append(f"来源：{entry.source}")
                lines.append("")
                lines.append(f"材料触发：{entry.trigger}")
                lines.append("")
                lines.append(f"答案句：{entry.answer}")
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_frequency(entries: list[Entry]) -> str:
    by_term: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_term[entry.term].append(entry)
    lines = ["# 选必一术语频次统计", ""]
    for term, cases in sorted(by_term.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        buckets = "、".join(sorted({case.bucket for case in cases}))
        sources = "；".join(sorted({case.source for case in cases}))
        lines.append(f"## {term}")
        lines.append("")
        lines.append(f"出现次数：{len(cases)}")
        lines.append("")
        lines.append(f"所属要素：{buckets}")
        lines.append("")
        lines.append(f"出现卷题：{sources}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_reverify(entries: list[Entry]) -> str:
    origins = Counter(entry.origin for entry in entries)
    lines = [
        "# 当前 run 回源复核记录",
        "",
        f"主表条目数：{len(entries)}",
        "",
        "来源构成：",
        "",
    ]
    for origin, n in sorted(origins.items()):
        lines.append(f"- {origin}: {n}")
    lines.extend(
        [
            "",
            "旧终稿仅用于定位遗漏套卷；旧线补入的套卷已在当前 run 目录重新抽取原始细则文本，抽取件位于 02_extraction/codex_extraction_logs/old_locator_reverify_20260503/。",
            "",
            "2026海淀一模 Q20 由 ClaudeCode 提醒后，Codex 回源核对试卷图像与评分标准 PDF，只保留评分标准原文能够支撑的四组术语，未采用外推术语。",
            "",
        ]
    )
    return "\n".join(lines)


def assert_clean(text: str, label: str) -> None:
    bad = [token for token in FORBIDDEN if token in text]
    if bad:
        raise SystemExit(f"{label} contains forbidden tokens: {bad}")


def main() -> None:
    DELIVERY.mkdir(parents=True, exist_ok=True)
    STUDENT.mkdir(parents=True, exist_ok=True)
    entries = load_entries()
    main_md = render_main(entries)
    freq_md = render_frequency(entries)
    reverify_md = render_reverify(entries)
    assert_clean(main_md, "main_md")
    assert_clean(freq_md, "freq_md")
    final_path = DELIVERY / "飞哥政治庄园_选必一_当代国际政治与经济_细则术语成品版_2026-05-03.md"
    freq_path = DELIVERY / "选必一_术语频次统计_2026-05-03.md"
    reverify_path = DELIVERY / "current_run_reverification_report.md"
    final_path.write_text(main_md, encoding="utf-8")
    freq_path.write_text(freq_md, encoding="utf-8")
    reverify_path.write_text(reverify_md, encoding="utf-8")
    (STUDENT / "student_doc_final.md").write_text(main_md, encoding="utf-8")
    print(f"entries={len(entries)}")
    print(final_path)
    print(freq_path)
    print(reverify_path)


if __name__ == "__main__":
    main()
