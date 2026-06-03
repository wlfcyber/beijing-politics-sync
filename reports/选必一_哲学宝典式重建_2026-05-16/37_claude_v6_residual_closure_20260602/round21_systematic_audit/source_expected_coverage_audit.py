from __future__ import annotations

import importlib.util
import json
import re
from collections import defaultdict
from pathlib import Path


DOCX = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第29轮漏项覆盖修正版_带水印_20260603.docx")
RAW_DIR = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/02_source_cards/raw_cards")
OUT_DIR = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/37_claude_v6_residual_closure_20260602/round21_systematic_audit/source_expected_coverage_audit")
SYSTEMATIC = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/37_claude_v6_residual_closure_20260602/round21_systematic_audit/systematic_audit.py")


EXPECTED = [
    {
        "bucket": "理论",
        "term": "国家间共同利益是国家合作的基础",
        "patterns": [
            r"共同利益.{0,10}合作.{0,8}基础",
            r"合作.{0,8}基础.{0,10}共同利益",
            r"国家间的?共同利益是国家合作的基础",
            r"共同利益是合作的基础",
            r"基于.{0,12}共同利益",
            r"符合.{0,12}共同利益",
        ],
    },
    {
        "bucket": "理论",
        "term": "维护国家利益是主权国家对外活动的出发点和落脚点",
        "patterns": [r"维护国家利益", r"国家利益.{0,12}出发点", r"兼顾他国合理关切"],
    },
    {
        "bucket": "理论",
        "term": "当前国际竞争的实质是以经济和科技实力为基础的综合国力较量",
        "patterns": [r"国际竞争的实质", r"综合国力较量", r"经济和科技实力"],
    },
    {
        "bucket": "经济全球化",
        "term": "推进贸易和投资自由化便利化",
        "patterns": [r"贸易.{0,6}投资.{0,6}自由化.{0,6}便利化", r"贸易投资便利化", r"投资自由化便利化"],
    },
    {
        "bucket": "经济全球化",
        "term": "利用两个市场两种资源优化全球资源配置",
        "patterns": [r"两个市场.{0,4}两种资源", r"国内国际.{0,8}资源", r"全球资源配置"],
    },
    {
        "bucket": "经济全球化",
        "term": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "patterns": [r"经济全球化.{0,16}开放.{0,4}包容.{0,4}普惠.{0,4}平衡.{0,4}共赢", r"普惠包容的经济全球化"],
    },
    {
        "bucket": "经济全球化",
        "term": "维护全球产业链供应链稳定畅通",
        "patterns": [r"产业链供应链.{0,12}稳定", r"产供链.{0,12}稳定", r"供应链.{0,12}稳定"],
    },
    {
        "bucket": "政治多极化",
        "term": "共商共建共享的全球治理观",
        "patterns": [r"共商共建共享", r"全球治理观"],
    },
    {
        "bucket": "政治多极化",
        "term": "践行真正的多边主义",
        "patterns": [r"真正的多边主义", r"践行多边主义"],
    },
    {
        "bucket": "政治多极化",
        "term": "推动国际关系民主化",
        "patterns": [r"国际关系民主化"],
    },
    {
        "bucket": "政治多极化",
        "term": "推动构建人类命运共同体",
        "patterns": [r"人类命运共同体"],
    },
    {
        "bucket": "中国",
        "term": "贡献中国智慧、中国方案、中国力量",
        "patterns": [r"中国智慧.{0,6}中国方案", r"中国方案", r"中国力量"],
    },
    {
        "bucket": "中国",
        "term": "中国是负责任大国并勇于担当",
        "patterns": [r"负责任大国", r"大国担当", r"勇于担当"],
    },
    {
        "bucket": "中国",
        "term": "坚持正确义利观",
        "patterns": [r"正确义利观"],
    },
    {
        "bucket": "联合国",
        "term": "维护《联合国宪章》宗旨和原则",
        "patterns": [r"联合国宪章.{0,10}宗旨.{0,8}原则", r"宪章宗旨和原则"],
    },
    {
        "bucket": "联合国",
        "term": "坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序",
        "patterns": [r"以联合国为核心", r"以国际法为基础"],
    },
]


ALIASES = {
    "共同利益是合作的基础": "国家间共同利益是国家合作的基础",
    "共同的国家利益是国际合作的基础": "国家间共同利益是国家合作的基础",
    "国家间共同利益是国家合作的基础": "国家间共同利益是国家合作的基础",
    "维护国家利益是主权国家对外活动的出发点和落脚点": "维护国家利益是主权国家对外活动的出发点和落脚点",
    "推进普惠包容的经济全球化": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
    "推进普惠包容的经济全球化，推动构建更加开放、包容的全球经济格局": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
    "中国推动构建人类命运共同体": "推动构建人类命运共同体",
    "中国推动构建人类命运共同体；与发展中国家共享发展新机遇，惠民生增福祉，实现互利共赢；习近平外交思想指导中国特色大国外交（外交为民、服务中国式现代化）": "推动构建人类命运共同体",
}


def load_audit_module():
    spec = importlib.util.spec_from_file_location("systematic_audit", SYSTEMATIC)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def card_to_key(path: Path) -> str:
    stem = path.stem
    m = re.match(r"(20\d{2})_(.+?)_(期末|期中|一模|二模)_Q(\d+)(?:_(\d+))?$", stem)
    if not m:
        return stem
    year, district, exam, q, sub = m.groups()
    return f"{year}{district}{exam}Q{q}" + (f"({sub})" if sub else "")


def relevant_card_text(text: str) -> str:
    # Keep source-card guidance and rubric/answer areas; this avoids matching unrelated full-paper tails too often.
    chunks = []
    for marker in ["## 细则片段", "### CLEAN_PROMPT_VERIFICATION", "答案逻辑", "细则核心", "可采点"]:
        if marker in text:
            chunks.append(text.split(marker, 1)[1])
    if chunks:
        return "\n".join(chunks)
    return text[:4000]


def normalize_term(term: str) -> str:
    term = re.sub(r"\s+", "", term)
    term = term.strip("；;，,。 ")
    return ALIASES.get(term, term)


def parse_doc_terms():
    mod = load_audit_module()
    _, _, entries = mod.parse_docx(DOCX)
    by_key: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for e in entries:
        if e["h1"] and e["h3"]:
            by_key[e["key"]].add((e["h1"], normalize_term(e["h3"])))
        for bucket, term in mod.parse_tong_terms(e["tong_lines"]):
            for part in re.split(r"[；;]", term):
                part = normalize_term(part)
                if part:
                    by_key[e["key"]].add((bucket, part))
    return by_key


def has_expected(doc_terms: set[tuple[str, str]], bucket: str, term: str) -> bool:
    wanted = normalize_term(term)
    for b, t in doc_terms:
        if b == bucket and (normalize_term(t) == wanted or wanted in normalize_term(t) or normalize_term(t) in wanted):
            return True
    return False


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc_terms = parse_doc_terms()
    issues = []
    debug_expected = defaultdict(list)
    for card in sorted(RAW_DIR.glob("*.md")):
        key = card_to_key(card)
        raw = card.read_text(errors="ignore")
        rel = relevant_card_text(raw)
        for item in EXPECTED:
            matched = [pat for pat in item["patterns"] if re.search(pat, rel)]
            if not matched:
                continue
            debug_expected[key].append((item["bucket"], item["term"], matched[0]))
            if not has_expected(doc_terms.get(key, set()), item["bucket"], item["term"]):
                evidence = ""
                for line in rel.splitlines():
                    if any(re.search(pat, line) for pat in item["patterns"]):
                        evidence = line.strip()
                        break
                issues.append(
                    {
                        "key": key,
                        "bucket": item["bucket"],
                        "term": item["term"],
                        "matched_pattern": matched[0],
                        "evidence": evidence[:300],
                        "doc_terms": sorted([f"{b}:{t}" for b, t in doc_terms.get(key, set())])[:30],
                        "card": str(card),
                    }
                )

    (OUT_DIR / "source_expected_coverage_issues.json").write_text(json.dumps(issues, ensure_ascii=False, indent=2))
    (OUT_DIR / "source_expected_debug.json").write_text(json.dumps(debug_expected, ensure_ascii=False, indent=2))
    md = ["# 源卡应有点位覆盖审计", "", f"- docx: `{DOCX}`", f"- raw_cards: `{RAW_DIR}`", f"- issues: {len(issues)}", ""]
    for it in issues:
        md.append(f"## {it['key']}｜{it['bucket']}｜{it['term']}")
        md.append(f"- evidence: {it['evidence']}")
        md.append(f"- card: `{it['card']}`")
        md.append("")
    (OUT_DIR / "source_expected_coverage_summary.md").write_text("\n".join(md))
    print(json.dumps({"issues": len(issues), "out": str(OUT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
