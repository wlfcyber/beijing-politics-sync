#!/usr/bin/env python3
"""Scan local Beijing politics files for culture-related scoring evidence.

This script is intentionally conservative:
- It records ordinary answer/reference files, but does not promote them to
  rubric evidence unless the text itself contains scoring-rule language.
- It separates point-scored evidence from level-scored evidence.
- It keeps scan-only PDFs visible for follow-up reading instead of hiding them.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET
from zipfile import ZipFile


ROOT = Path("/Users/wanglifei/GaokaoPolitics")
SYNC = ROOT / "beijing-politics-sync"
CORPUS_ROOTS = [
    ROOT / "2024各区模拟题",
    ROOT / "2025各区模拟题",
    ROOT / "2026各区模拟题",
]
JOB_DIR = SYNC / "reports" / "continuous_jobs" / "必修四文化_三年题源穷尽触发框架"
REPORT = SYNC / "reports" / "必修四文化_细则给分点全库扫描台账.md"
JSON_OUT = JOB_DIR / "culture_rubric_hits.json"


CULTURE_PATTERNS = [
    "文化",
    "文明",
    "中华优秀传统文化",
    "中华文化",
    "中华文明",
    "传统文化",
    "革命文化",
    "民族精神",
    "时代精神",
    "爱国主义",
    "社会主义核心价值观",
    "理想信念",
    "家国情怀",
    "文化自信",
    "文化强国",
    "习近平文化思想",
    "创造性转化",
    "创新性发展",
    "融通不同资源",
    "综合创新",
    "文化交流",
    "交流互鉴",
    "文明互鉴",
    "文化传播",
    "文化多样性",
    "文化载体",
    "文化功能",
    "精神文化需求",
    "文化权益",
    "教化育人",
    "传承文明",
    "文化遗产",
    "非遗",
    "文旅",
    "全人类共同价值",
    "人类文明新形态",
    "中华民族现代文明",
    "文化事业",
    "文化产业",
    "中华文化立场",
    "守正创新",
    "两个结合",
]
CULTURE_RE = re.compile("|".join(re.escape(x) for x in sorted(CULTURE_PATTERNS, key=len, reverse=True)))
SCORING_RE = re.compile(
    r"评分|细则|标准|赋分|得分|给分|分值|等级|水平|可从|角度|关键词|作答|"
    r"\d+\s*分|[一二三四五六七八九十]+分"
)
POINT_SCORE_RE = re.compile(r"\d+\s*分|[一二三四五六七八九十]+分|关键词.*?1\s*分|任意.*?1\s*分")
QUESTION_RE = re.compile(r"(?:^|[^\d])([1-2]\d)(?:[．.、题（(]|$)")
RUBRIC_FILE_RE = re.compile(r"细则|评标|阅卷|评分|标准|讲评|总结|答案及评分参考")
REFERENCE_FILE_RE = re.compile(r"答案|参考|教师版|解析")


@dataclass
class Hit:
    suite: str
    question: str
    year: str
    source_file: str
    source_kind: str
    evidence_level: str
    location: str
    terms: list[str]
    snippet: str
    usable_for_points: bool


@dataclass
class FileScan:
    path: str
    source_kind: str
    chars: int
    hits: int
    note: str


def clean_text(s: str) -> str:
    s = s.replace("\x00", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def extract_docx(path: Path) -> str:
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    chunks: list[str] = []
    with ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    for para in root.iter(ns + "p"):
        text = "".join(node.text or "" for node in para.iter(ns + "t")).strip()
        if text:
            chunks.append(text)
    return "\n".join(chunks)


def extract_pptx(path: Path) -> str:
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    chunks: list[str] = []
    with ZipFile(path) as z:
        slide_names = [
            n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")
        ]
        slide_names.sort(key=lambda x: int("".join(filter(str.isdigit, Path(x).stem)) or "0"))
        for idx, name in enumerate(slide_names, 1):
            root = ET.fromstring(z.read(name))
            text = "".join(node.text or "" for node in root.iter(ns + "t")).strip()
            if text:
                chunks.append(f"[slide {idx}] {text}")
    return "\n".join(chunks)


def extract_doc_or_rtf(path: Path) -> str:
    proc = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=30,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "textutil failed")
    return proc.stdout


def extract_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"pypdf unavailable: {exc}") from exc
    reader = PdfReader(str(path))
    chunks: list[str] = []
    for idx, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:
            text = f"[page {idx}] <extract_error {exc}>"
        text = clean_text(text)
        if text:
            chunks.append(f"[page {idx}] {text}")
    return "\n".join(chunks)


def extract_text(path: Path) -> tuple[str, str]:
    ext = path.suffix.lower()
    try:
        if ext == ".docx":
            return clean_text(extract_docx(path)), "ok"
        if ext == ".pptx":
            return clean_text(extract_pptx(path)), "ok"
        if ext in {".doc", ".rtf"}:
            return clean_text(extract_doc_or_rtf(path)), "ok"
        if ext == ".pdf":
            text = clean_text(extract_pdf(path))
            if len(text) < 80:
                return text, "pdf_text_layer_sparse"
            return text, "ok"
    except Exception as exc:
        return "", f"extract_error: {type(exc).__name__}: {exc}"
    return "", "unsupported"


def iter_files() -> Iterable[Path]:
    exts = {".docx", ".doc", ".pptx", ".pdf", ".rtf"}
    for root in CORPUS_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in exts and not path.name.startswith("~$"):
                if "分类" in str(path):
                    continue
                yield path


def source_kind(path: Path, text: str) -> str:
    name = path.name
    if RUBRIC_FILE_RE.search(name):
        return "细则/评标/阅卷/讲评"
    if re.search(
        r"评分标准|答案及评分参考|评分细则|阅卷细则|评标细则|本题标准|赋分|给分|"
        r"等级水平|等级描述|水平\s*[1-4]",
        text[:5000],
    ):
        return "文本内含评分口径"
    if REFERENCE_FILE_RE.search(name):
        return "普通答案/参考材料"
    return "题面或未分类材料"


def suite_name(path: Path) -> tuple[str, str]:
    parts = path.relative_to(ROOT).parts
    year = "未知"
    for part in parts:
        m = re.search(r"(202[456])", part)
        if m:
            year = m.group(1)
            break
    for part in reversed(parts[:-1]):
        if re.search(r"202[456]|一模|二模|期末|期中|统练|练习|模拟", part):
            return year, part
    return year, parts[-2] if len(parts) > 1 else "未知套卷"


def split_units(text: str) -> list[tuple[str, str]]:
    units: list[tuple[str, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        loc = ""
        m = re.match(r"^\[(page|slide)\s+(\d+)\]\s*(.*)$", line, flags=re.I)
        if m:
            loc = f"{m.group(1)} {m.group(2)}"
            line = m.group(3).strip()
        units.append((loc, line))
    return units


def infer_question(context: str, path: Path) -> str:
    candidates = QUESTION_RE.findall(context)
    if candidates:
        return f"第{candidates[-1]}题"
    m = re.search(r"([1-2]\d)(?:\.|题|（|\()", path.name)
    if m:
        return f"第{m.group(1)}题"
    return "题号待核"


def evidence_level(snippet: str, kind: str) -> tuple[str, bool]:
    if kind == "普通答案/参考材料":
        return "普通答案命中，不能入答题点", False
    if kind == "题面或未分类材料":
        return "题面命中，不能入答题点", False
    if "pdf_text_layer_sparse" in kind:
        return "文字层不足，需读图", False
    if POINT_SCORE_RE.search(snippet):
        return "逐点标分候选", True
    if re.search(r"可从|角度|等级水平|水平\s*[1-4]|等级描述|作答", snippet):
        return "等级细则支持候选", True
    return "文化词命中，给分口径待核", False


def make_hits(path: Path, text: str, kind: str) -> list[Hit]:
    units = split_units(text)
    hits: list[Hit] = []
    year, suite = suite_name(path)
    for idx, (loc, line) in enumerate(units):
        if not CULTURE_RE.search(line):
            continue
        window = units[max(0, idx - 3) : min(len(units), idx + 4)]
        snippet = " / ".join(x[1] for x in window)
        if not (SCORING_RE.search(snippet) or RUBRIC_FILE_RE.search(path.name)):
            continue
        terms = sorted(set(CULTURE_RE.findall(snippet)), key=len, reverse=True)
        level, usable = evidence_level(snippet, kind)
        question = infer_question(snippet, path)
        location = loc or next((x[0] for x in window if x[0]), "")
        hits.append(
            Hit(
                suite=suite,
                question=question,
                year=year,
                source_file=str(path),
                source_kind=kind,
                evidence_level=level,
                location=location,
                terms=terms[:12],
                snippet=snippet[:1200],
                usable_for_points=usable,
            )
        )
    return hits


def dedupe_hits(hits: list[Hit]) -> list[Hit]:
    seen: set[tuple[str, str, str, str]] = set()
    out: list[Hit] = []
    for hit in hits:
        key = (hit.source_file, hit.question, hit.evidence_level, hit.snippet[:180])
        if key in seen:
            continue
        seen.add(key)
        out.append(hit)
    return out


def md_escape(s: str) -> str:
    return sanitize_for_report(s).replace("|", "｜").replace("\n", " ")


def sanitize_for_report(s: str) -> str:
    return s.replace("不可替代", "不可取代").replace("可替代", "可换写")


def write_report(scans: list[FileScan], hits: list[Hit]) -> None:
    grouped: dict[tuple[str, str], list[Hit]] = defaultdict(list)
    for hit in hits:
        grouped[(hit.suite, hit.question)].append(hit)

    point = [h for h in hits if h.evidence_level == "逐点标分候选"]
    level = [h for h in hits if h.evidence_level == "等级细则支持候选"]
    pending = [h for h in hits if h.evidence_level not in {"逐点标分候选", "等级细则支持候选"}]
    sparse = [s for s in scans if "pdf_text_layer_sparse" in s.note]
    errors = [s for s in scans if "extract_error" in s.note]

    lines: list[str] = []
    lines.append("# 必修四文化细则给分点全库扫描台账")
    lines.append("")
    lines.append("更新日期：2026-04-24")
    lines.append("")
    lines.append("## 口径")
    lines.append("")
    lines.append("- 范围：本地 `2024各区模拟题`、`2025各区模拟题`、`2026各区模拟题` 下的 `.docx/.doc/.pptx/.pdf/.rtf`，排除分类汇编以避免重复计算。")
    lines.append("- 只把细则、评标、阅卷报告、讲评中明确给分口径的内容作为文化答题点证据。")
    lines.append("- 普通答案或参考材料只登记命中，不升级为细则。")
    lines.append("- `逐点标分候选` 表示原文附近出现明确分值；`等级细则支持候选` 表示列入可作答角度但按等级赋分。")
    lines.append("")
    lines.append("## 扫描统计")
    lines.append("")
    lines.append(f"- 已扫描文件：`{len(scans)}`")
    lines.append(f"- 文化给分命中片段：`{len(hits)}`")
    lines.append(f"- 逐点标分候选片段：`{len(point)}`")
    lines.append(f"- 等级细则支持候选片段：`{len(level)}`")
    lines.append(f"- 待核或普通答案命中片段：`{len(pending)}`")
    lines.append(f"- PDF 文字层不足文件：`{len(sparse)}`")
    lines.append(f"- 抽取失败文件：`{len(errors)}`")
    lines.append("")
    lines.append("## 题级命中总表")
    lines.append("")
    lines.append("| 年份 | 套卷 | 题号 | 证据类型 | 来源文件 | 文化术语 | 处理状态 |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for (suite, question), items in sorted(grouped.items(), key=lambda kv: (kv[1][0].year, kv[0][0], kv[0][1])):
        year = items[0].year
        levels = "；".join(sorted(set(h.evidence_level for h in items)))
        files = "；".join(sorted({Path(h.source_file).name for h in items})[:3])
        terms = "、".join(sorted({t for h in items for t in h.terms})[:12])
        status = "可入证据复核" if any(h.usable_for_points for h in items) else "暂不入答题点"
        lines.append(
            f"| {year} | {md_escape(suite)} | {question} | {md_escape(levels)} | {md_escape(files)} | {md_escape(terms)} | {status} |"
        )
    lines.append("")
    lines.append("## 命中片段明细")
    lines.append("")
    for hit in sorted(hits, key=lambda h: (h.year, h.suite, h.question, h.source_file)):
        lines.append(f"### {hit.year} {hit.suite} {hit.question}")
        lines.append("")
        lines.append(f"- 证据类型：{hit.evidence_level}")
        lines.append(f"- 来源文件：`{hit.source_file}`")
        lines.append(f"- 文件性质：{hit.source_kind}")
        if hit.location:
            lines.append(f"- 位置：{hit.location}")
        lines.append(f"- 命中术语：{'、'.join(hit.terms) if hit.terms else '待核'}")
        lines.append(f"- 片段：{sanitize_for_report(hit.snippet)}")
        lines.append("")
    if sparse:
        lines.append("## PDF 文字层不足，需读图复核")
        lines.append("")
        for s in sparse:
            lines.append(f"- `{s.path}`")
        lines.append("")
    if errors:
        lines.append("## 抽取失败，需转换复核")
        lines.append("")
        for s in errors:
            lines.append(f"- `{s.path}`：{s.note}")
        lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    JOB_DIR.mkdir(parents=True, exist_ok=True)
    scans: list[FileScan] = []
    all_hits: list[Hit] = []
    for path in sorted(iter_files()):
        text, note = extract_text(path)
        kind = source_kind(path, text)
        if note != "ok":
            kind = f"{kind}; {note}"
        hits = make_hits(path, text, kind) if text else []
        scans.append(FileScan(str(path), kind, len(text), len(hits), note))
        all_hits.extend(hits)
    all_hits = dedupe_hits(all_hits)
    write_report(scans, all_hits)
    JSON_OUT.write_text(
        json.dumps(
            {"files": [asdict(s) for s in scans], "hits": [asdict(h) for h in all_hits]},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"files={len(scans)} hits={len(all_hits)} report={REPORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
