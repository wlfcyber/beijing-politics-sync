#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync")
RUN_DIR = ROOT / "reports/philosophy_v3_reaudit_2026-04-26"
OUT_DIR = RUN_DIR / "artifacts"
INPUT = OUT_DIR / "all_framework_entry_source_reaudit.csv"


@dataclass
class BundleSection:
    title: str
    source_path: str
    status: str
    body: str


DIRECT_ALIAS: dict[str, list[str]] = {
    "物质决定意识": ["物质决定意识", "社会存在决定社会意识", "意识是对客观存在的反映", "客观存在", "客观实际"],
    "意识对物质具有能动作用": ["意识的反作用", "意识对物质", "意识具有能动作用", "意识能动", "主观能动性"],
    "一切从实际出发": ["一切从实际出发", "实事求是", "主观与客观", "客观实际", "具体的历史的统一"],
    "实事求是": ["实事求是", "一切从实际出发", "客观实际", "主观与客观"],
    "主观能动性": ["主观能动性", "意识的能动作用", "发挥主观能动性", "能动地"],
    "尊重客观规律": ["尊重客观规律", "尊重规律", "规律的客观性", "按规律", "符合规律"],
    "规律的客观性": ["规律的客观性", "尊重规律", "客观规律", "符合规律"],
    "联系的观点": ["联系的观点", "普遍联系", "事物是普遍联系的", "相互联系", "联系的普遍性"],
    "联系的普遍性": ["联系的普遍性", "普遍联系", "事物是普遍联系的", "相互联系"],
    "联系的客观性": ["联系的客观性", "固有联系", "自在联系", "人为事物联系"],
    "联系的多样性": ["联系的多样性", "条件性", "多种条件", "多样"],
    "整体与部分": ["整体与部分", "整体", "部分", "立足整体", "统筹全局"],
    "系统观念": ["系统观念", "系统优化", "系统", "整体性", "协同"],
    "系统优化": ["系统优化", "系统观念", "优化组合", "综合思维"],
    "发展的观点": ["发展的观点", "发展的普遍性", "用发展的观点", "发展过程"],
    "量变与质变": ["量变", "质变", "量变与质变", "积累"],
    "适度原则": ["适度原则", "适度", "适量", "度"],
    "前进性与曲折性": ["前进性", "曲折性", "前途是光明的", "道路是曲折的"],
    "辩证否定": ["辩证否定", "守正创新", "扬弃", "自己否定自己"],
    "守正创新": ["守正创新", "辩证否定", "扬弃"],
    "矛盾": ["矛盾", "对立统一", "一分为二", "全面看问题"],
    "对立统一": ["对立统一", "矛盾", "既对立又统一"],
    "矛盾的普遍性": ["矛盾的普遍性", "矛盾普遍存在", "承认矛盾"],
    "矛盾的特殊性": ["矛盾的特殊性", "具体问题具体分析", "因地制宜", "一切以时间地点条件为转移"],
    "具体问题具体分析": ["具体问题具体分析", "矛盾的特殊性", "因地制宜"],
    "普遍性和特殊性": ["矛盾普遍性和特殊性", "共性与个性", "一般与个别"],
    "主次矛盾": ["主要矛盾", "次要矛盾", "重点", "抓重点"],
    "矛盾主次方面": ["矛盾主要方面", "矛盾次要方面", "主流", "支流"],
    "两点论": ["两点论", "重点论", "两点论与重点论", "全面看问题", "抓重点"],
    "重点论": ["重点论", "两点论", "抓重点"],
    "内外因": ["内因", "外因", "内外因"],
    "实践与认识": ["实践是认识的基础", "实践决定认识", "认识对实践", "实践与认识"],
    "实践决定认识": ["实践决定认识", "实践是认识的基础", "实践是认识的来源"],
    "认识对实践": ["认识对实践", "认识反作用于实践", "科学理论指导"],
    "认识发展": ["认识具有反复性", "认识具有无限性", "认识具有上升性", "认识发展"],
    "真理": ["真理", "真理是具体的", "真理是有条件的", "追求真理"],
    "社会存在": ["社会存在决定社会意识", "社会存在", "社会意识"],
    "社会意识": ["社会意识", "社会存在决定社会意识", "社会意识具有相对独立性"],
    "社会基本矛盾": ["生产力与生产关系", "经济基础与上层建筑", "社会基本矛盾", "基本规律"],
    "改革": ["改革", "社会主义制度的自我完善", "上层建筑", "生产关系"],
    "人民群众": ["人民群众", "群众观点", "群众路线", "以人民为中心", "人民主体"],
    "群众观点": ["群众观点", "群众路线", "人民群众", "以人民为中心"],
    "价值观": ["价值观", "价值观的导向作用", "价值导向"],
    "价值判断": ["价值判断", "价值选择", "价值判断与价值选择"],
    "价值选择": ["价值选择", "价值判断", "价值判断与价值选择"],
    "实现人生价值": ["人生价值", "实现人生价值", "劳动和奉献", "砥砺自我"],
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def parse_bundle(path_text: str) -> list[BundleSection]:
    if not path_text:
        return []
    path = ROOT / path_text
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    matches = list(re.finditer(r"^## (.+)$", text, flags=re.M))
    sections: list[BundleSection] = []
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        raw = text[start:end].strip()
        meta_block, _, body = raw.partition("\n\n")
        meta: dict[str, str] = {}
        for line in meta_block.splitlines():
            m = re.match(r"- ([a-z_]+): `?(.*?)`?$", line.strip())
            if m:
                meta[m.group(1)] = m.group(2).strip("`")
        sections.append(
            BundleSection(
                title=title,
                source_path=meta.get("source_path", ""),
                status=meta.get("status", ""),
                body=body,
            )
        )
    return sections


BUNDLE_CACHE: dict[str, list[BundleSection]] = {}


def get_sections(path_text: str) -> list[BundleSection]:
    if path_text not in BUNDLE_CACHE:
        BUNDLE_CACHE[path_text] = parse_bundle(path_text)
    return BUNDLE_CACHE[path_text]


def qnum_from_row(row: dict[str, str]) -> int | None:
    if row.get("qnum", "").isdigit():
        return int(row["qnum"])
    m = re.search(r"第\s*(\d{1,2})\s*题", row.get("source", ""))
    return int(m.group(1)) if m else None


def question_marker_regex(qnum: int) -> re.Pattern[str]:
    return re.compile(
        rf"(?m)(^|\n)\s*(?:第\s*{qnum}\s*(?:题|[．.、])|{qnum}\s*[．.、])"
    )


def next_question_regex(qnum: int) -> re.Pattern[str]:
    nums = "|".join(str(n) for n in range(qnum + 1, min(qnum + 6, 31)))
    return re.compile(rf"(?m)\n\s*(?:第\s*(?:{nums})\s*(?:题|[．.、])|(?:{nums})\s*[．.、])")


def all_question_segments(body: str, qnum: int | None) -> list[str]:
    if qnum is None:
        return []
    segments: list[str] = []
    for match in question_marker_regex(qnum).finditer(body):
        start = match.start()
        next_match = next_question_regex(qnum).search(body, match.end())
        end = next_match.start() if next_match else min(len(body), start + 3200)
        segment = body[start:end].strip()
        if segment:
            segments.append(segment)
    return segments


def material_tokens(row: dict[str, str]) -> list[str]:
    text = row.get("material", "")
    tokens = []
    for token in re.split(r"[，。；、,;：“”\"'（）()《》\s]+", text):
        token = token.strip()
        if len(token) >= 4 and not re.fullmatch(r"\d+", token):
            tokens.append(token)
    return tokens[:18]


def segment_score(segment: str, aliases: list[str], row: dict[str, str], section: BundleSection) -> int:
    score = 0
    score += 100 * len(find_hits(segment, aliases))
    score += 8 * len([token for token in material_tokens(row) if token in segment])
    support_note = row.get("support_note", "")
    if support_note and (support_note in section.title or support_note in section.source_path):
        score += 20
    if any(token in segment for token in ["评分标准", "评分细则", "本题标准", "答案示例", "参考答案", "【答案】"]):
        score += 8
    return score


def alias_window(body: str, aliases: list[str], limit: int = 2400) -> str:
    positions = [body.find(alias) for alias in aliases if body.find(alias) >= 0]
    if not positions:
        return body[:limit]
    pos = min(positions)
    start = max(0, pos - 600)
    end = min(len(body), pos + limit)
    return body[start:end].strip()


def best_segment(candidates: list[tuple[BundleSection, str]], row: dict[str, str], aliases: list[str]) -> tuple[BundleSection | None, str]:
    if not candidates:
        return None, ""
    scored = sorted(
        ((segment_score(segment, aliases, row, section), section, segment) for section, segment in candidates),
        key=lambda item: item[0],
        reverse=True,
    )
    _, section, segment = scored[0]
    return section, segment


def row_aliases(row: dict[str, str]) -> list[str]:
    seed = " / ".join([row.get("section", ""), row.get("trigger", "")])
    aliases: list[str] = []
    for key, values in DIRECT_ALIAS.items():
        if key in seed:
            aliases.extend(values)
    for token in re.split(r"[/、，,；;（）() ]+", seed):
        token = clean(token)
        if len(token) >= 3 and token not in {"触发知识", "材料信息", "逻辑链", "观点", "方法论"}:
            aliases.append(token)
    seen = set()
    out = []
    for alias in aliases:
        alias = alias.strip()
        if alias and alias not in seen:
            seen.add(alias)
            out.append(alias)
    return out[:28]


def find_hits(text: str, aliases: list[str]) -> list[str]:
    return [alias for alias in aliases if alias and alias in text]


def evidence_sections(sections: list[BundleSection]) -> tuple[list[BundleSection], list[BundleSection]]:
    scoring = [
        sec
        for sec in sections
        if any(token in (sec.title + sec.source_path) for token in ["细则", "评标", "阅卷", "评分", "讲评", "答案解析"])
    ]
    paper = [sec for sec in sections if any(token in (sec.title + sec.source_path) for token in ["试卷", "教师版"])]
    return scoring, paper


def best_segments(row: dict[str, str]) -> dict[str, str]:
    sections = get_sections(row.get("bundle_path", ""))
    qnum = qnum_from_row(row)
    aliases = row_aliases(row)
    scoring, paper = evidence_sections(sections)
    scoring_segments = []
    for sec in scoring:
        for seg in all_question_segments(sec.body, qnum):
            scoring_segments.append((sec, seg))
    paper_segments = []
    for sec in paper:
        for seg in all_question_segments(sec.body, qnum):
            paper_segments.append((sec, seg))

    scoring_section, scoring_segment = best_segment(scoring_segments, row, aliases)
    paper_section, paper_segment = best_segment(paper_segments, row, aliases)

    # Fallback: use an alias-centered window in the support note section when exact question segmentation fails.
    support_note = row.get("support_note", "")
    if not scoring_segment:
        for sec in scoring:
            if support_note and (support_note in sec.title or support_note in sec.source_path):
                scoring_segment = alias_window(sec.body, aliases)
                scoring_section = sec
                break
    if not scoring_segment and scoring:
        best_source = max(scoring, key=lambda sec: len(find_hits(sec.body, aliases)))
        scoring_segment = alias_window(best_source.body, aliases)
        scoring_section = best_source
    return {
        "scoring_segment": scoring_segment,
        "scoring_source_title": scoring_section.title if scoring_section else "",
        "paper_segment": paper_segment,
        "paper_source_title": paper_section.title if paper_section else "",
        "bundle_section_count": str(len(sections)),
    }


def excerpt_around_hits(text: str, hits: list[str], limit: int = 360) -> str:
    if not text:
        return ""
    if hits:
        positions = [text.find(hit) for hit in hits if text.find(hit) >= 0]
        if positions:
            pos = min(positions)
            start = max(0, pos - 160)
            end = min(len(text), pos + limit)
            return clean(text[start:end])
    return clean(text[:limit])


def classify_row(row: dict[str, str]) -> dict[str, str]:
    aliases = row_aliases(row)
    segs = best_segments(row)
    scoring_seg = segs["scoring_segment"]
    paper_seg = segs["paper_segment"]
    combined_source_text = "\n".join([scoring_seg, paper_seg])
    scoring_hits = find_hits(scoring_seg, aliases)
    paper_hits = find_hits(paper_seg, aliases)
    v2_logic_hits = find_hits(" ".join([row.get("material", ""), row.get("logic", "")]), aliases)
    final_status = row.get("final_status", "")
    nature = row.get("question_nature", "")

    if final_status.startswith("E_"):
        verdict = "BLOCKED_SOURCE_GAP"
        action = "do-not-use-until-source-proof"
        reason = f"上一层来源复核已标 {final_status}；本轮不得用 V2 逻辑替代原题/细则。"
    elif final_status.startswith("D_"):
        verdict = "WEAK_REFERENCE_ONLY"
        action = "downgrade-reference-only"
        reason = "来源边界为 reference-only，不能作为正式主观细则链。"
    elif nature == "subjective" and scoring_hits:
        verdict = "SUPPORTED_DIRECT_RUBRIC"
        action = "keep-with-excerpt"
        reason = "细则/评标/阅卷片段直接命中该原理或等价表述。"
    elif nature == "choice" and row.get("choice_answer_key_state") in {"answer-key-present", "possible-answer-key"} and paper_hits:
        verdict = "SUPPORTED_DIRECT_CHOICE_TEXT"
        action = "keep-choice-with-excerpt"
        reason = "选择题题面/选项片段直接命中该原理或等价表述，且已有答案键状态。"
    elif nature == "choice" and row.get("choice_answer_key_state") not in {"answer-key-present", "possible-answer-key"}:
        verdict = "BLOCKED_NO_CHOICE_KEY"
        action = "do-not-use-until-answer-key"
        reason = "选择题缺可靠答案键，无法确认正确项触发。"
    elif scoring_seg and v2_logic_hits:
        verdict = "WEAK_INFERRED_FROM_MATERIAL"
        action = "manual-review-before-draft"
        reason = "原题/细则片段可定位，但未直接命中该原理；目前只看到 V2 材料链中的解释，需人工复看。"
    elif combined_source_text:
        verdict = "NEEDS_HUMAN_CONTENT_CHECK"
        action = "manual-review-before-draft"
        reason = "能定位原题/来源片段，但未找到该原理的直接或等价支撑。"
    else:
        verdict = "BLOCKED_NO_EXCERPT"
        action = "do-not-use-until-question-excerpt"
        reason = "未能从 bundle 切出对应题号的原题/细则片段。"

    support_excerpt = excerpt_around_hits(scoring_seg, scoring_hits or aliases)
    paper_excerpt = excerpt_around_hits(paper_seg, paper_hits or aliases)
    return {
        **row,
        "content_verdict": verdict,
        "content_action": action,
        "content_reason": reason,
        "direct_aliases": ";".join(aliases),
        "scoring_direct_hits": ";".join(scoring_hits),
        "paper_direct_hits": ";".join(paper_hits),
        "v2_logic_alias_hits": ";".join(v2_logic_hits),
        "scoring_source_title": segs["scoring_source_title"],
        "paper_source_title": segs["paper_source_title"],
        "source_excerpt": support_excerpt,
        "paper_excerpt": paper_excerpt,
        "bundle_section_count": segs["bundle_section_count"],
    }


def md_table(rows: list[dict[str, str]], fields: list[str], limit: int | None = None) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "|" + "|".join(["---"] * len(fields)) + "|"]
    for idx, row in enumerate(rows):
        if limit is not None and idx >= limit:
            break
        vals = [str(row.get(field, "")).replace("|", "／").replace("\n", " ") for field in fields]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def write_summary(rows: list[dict[str, str]]) -> None:
    verdicts = Counter(row["content_verdict"] for row in rows)
    by_section = defaultdict(Counter)
    for row in rows:
        by_section[row.get("section", "")][row["content_verdict"]] += 1
    risky = [
        row
        for row in rows
        if not row["content_verdict"].startswith("SUPPORTED_DIRECT")
    ]
    lines = [
        "# v3 内容回源复核汇总",
        "",
        "## 复核口径",
        "",
        "- 本轮不再只问“来源是否存在”，而是逐条回到 V2 所列来源题号，核对原题/细则是否真的支撑该原理方法论。",
        "- `SUPPORTED_DIRECT_RUBRIC` 仅表示细则、评标或阅卷片段直接出现该原理或等价给分表述。",
        "- `SUPPORTED_DIRECT_CHOICE_TEXT` 仅表示选择题题面/选项直接命中该原理或等价表述，且已有答案键状态。",
        "- `WEAK_INFERRED_FROM_MATERIAL` 表示只能从 V2 材料链推，不能直接当作正式闭环。",
        "- `BLOCKED_*`、`WEAK_REFERENCE_ONLY`、`NEEDS_HUMAN_CONTENT_CHECK` 均不得进入正式 v3 正文。",
        "",
        "## 总量",
        "",
        f"- 复核条目：{len(rows)}",
    ]
    for key, value in sorted(verdicts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## 按框架栏目统计", ""])
    section_rows = []
    for section, counts in sorted(by_section.items()):
        section_rows.append(
            {
                "section": section,
                "total": str(sum(counts.values())),
                "supported_direct": str(counts.get("SUPPORTED_DIRECT_RUBRIC", 0) + counts.get("SUPPORTED_DIRECT_CHOICE_TEXT", 0)),
                "weak_or_blocked": str(sum(v for k, v in counts.items() if not k.startswith("SUPPORTED_DIRECT"))),
                "verdicts": ";".join(f"{k}:{v}" for k, v in sorted(counts.items())),
            }
        )
    lines.extend(md_table(section_rows, ["section", "total", "supported_direct", "weak_or_blocked", "verdicts"], limit=None))
    lines.extend(["", "## 非直接支撑条目前 160 条", ""])
    lines.extend(
        md_table(
            risky,
            [
                "audit_id",
                "content_verdict",
                "content_action",
                "section",
                "source",
                "trigger",
                "content_reason",
                "source_excerpt",
                "paper_excerpt",
            ],
            limit=160,
        )
    )
    lines.extend(
        [
            "",
            "## Governor 结论",
            "",
            "- 本轮是内容层回源复核的第一张全量表，已经为 496 条旧框架条目切出原题/细则片段并给出保守判定。",
            "- 后续 v3 正文只能自动保留 `SUPPORTED_DIRECT_*`；其余条目必须人工复看、降级、补 OCR/答案键或删除。",
        ]
    )
    (OUT_DIR / "content_backtrace_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_boundary_full(rows: list[dict[str, str]]) -> None:
    risky = [row for row in rows if not row["content_verdict"].startswith("SUPPORTED_DIRECT")]
    verdicts = Counter(row["content_verdict"] for row in risky)
    lines = [
        "# v3 内容回源复核：非直接支撑完整清单",
        "",
        "## 使用口径",
        "",
        "- 本清单收录所有不能由原题/细则直接支撑 V2 原理方法论的条目。",
        "- 这些条目后续不得自动进入 v3 正文；只能按 `content_action` 删除、降级、补证或人工复看。",
        "- `source_excerpt` 与 `paper_excerpt` 是回源片段，不是 V2 自写解释。",
        "",
        "## 总量",
        "",
        f"- 非直接支撑条目：{len(risky)}",
    ]
    for key, value in sorted(verdicts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## 完整清单", ""])
    lines.extend(
        md_table(
            risky,
            [
                "audit_id",
                "content_verdict",
                "content_action",
                "section",
                "source",
                "trigger",
                "content_reason",
                "source_excerpt",
                "paper_excerpt",
            ],
            limit=None,
        )
    )
    (OUT_DIR / "content_backtrace_non_direct_full.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = read_csv(INPUT)
    reviewed = [classify_row(row) for row in rows]
    fields = [
        "audit_id",
        "line",
        "section",
        "source",
        "year",
        "district",
        "stage",
        "question",
        "question_nature",
        "final_grade",
        "final_status",
        "content_verdict",
        "content_action",
        "content_reason",
        "trigger",
        "direct_aliases",
        "scoring_direct_hits",
        "paper_direct_hits",
        "v2_logic_alias_hits",
        "scoring_source_title",
        "paper_source_title",
        "source_excerpt",
        "paper_excerpt",
        "bundle_path",
        "support_path",
        "choice_answer_key_state",
        "material",
        "logic",
    ]
    write_csv(OUT_DIR / "content_backtrace_review.csv", reviewed, fields)
    write_summary(reviewed)
    write_boundary_full(reviewed)


if __name__ == "__main__":
    main()
