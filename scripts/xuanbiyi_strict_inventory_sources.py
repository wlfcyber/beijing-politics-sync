from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path.cwd()
OUT_DIR = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16" / "11_strict_final_rebuild_2026-05-23"
CSV_OUT = OUT_DIR / "00_source_inventory.csv"
MD_OUT = OUT_DIR / "00_source_inventory.md"

SOURCE_ROOTS = [
    Path(r"C:\Users\Administrator\Desktop\2024各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2025各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2026各区模拟题"),
]

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

STAGE_PATTERNS = [
    ("一模", ["一模", "1模", "yimo"]),
    ("二模", ["二模", "2模", "ermo"]),
    ("期中", ["期中", "qizhong"]),
    ("期末", ["期末", "qimo"]),
    ("适应性", ["适应性", "适应"]),
]

ROLE_PATTERNS = [
    ("rubric", ["细则", "评标", "阅卷", "标准", "评分", "标答", "讲评"]),
    ("answer", ["答案", "参考答案"]),
    ("lecture", ["ppt", "课件", "讲评"]),
    ("paper", ["试卷", "教师版", "政治", "题"]),
]


@dataclass
class SourceRow:
    year_root: str
    year: str
    district: str
    stage: str
    suite_guess: str
    role: str
    extension: str
    size: int
    modified: str
    relative_path: str
    absolute_path: str


def guess_year(root: Path, path: Path) -> str:
    text = f"{root.name} {path.name}"
    match = re.search(r"20\d{2}", text)
    return match.group(0) if match else ""


def guess_district(path: Path) -> str:
    # Prefer directory names over filenames. Some lecture filenames mention
    # another district, but the containing suite folder is authoritative.
    for part in reversed(path.parent.parts):
        for district in DISTRICTS:
            if district in part:
                return district
    for district in DISTRICTS:
        if district in path.name:
            return district
    return ""


def guess_stage(path: Path) -> str:
    text = " ".join(path.parts).lower()
    for stage, patterns in STAGE_PATTERNS:
        if any(pattern.lower() in text for pattern in patterns):
            return stage
    return ""


def guess_role(path: Path) -> str:
    text = " ".join(path.parts).lower()
    suffix = path.suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg"}:
        if any(k in text for k in ["answer", "ans", "答案", "细则", "评标"]):
            return "rubric"
        return "image"
    if suffix in {".txt", ".md", ".json", ".csv"}:
        if "ocr" in text:
            return "ocr"
    for role, patterns in ROLE_PATTERNS:
        if any(pattern.lower() in text for pattern in patterns):
            return role
    if suffix in {".ppt", ".pptx"}:
        return "lecture"
    if suffix in {".doc", ".docx", ".pdf"}:
        return "paper"
    return "other"


def suite_guess(year: str, district: str, stage: str) -> str:
    parts = [part for part in [year, district, stage] if part]
    return "".join(parts)


def iter_files() -> list[SourceRow]:
    rows: list[SourceRow] = []
    for root in SOURCE_ROOTS:
        if not root.exists():
            continue
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            try:
                stat = path.stat()
                modified = datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds")
            except OSError:
                continue
            year = guess_year(root, path)
            district = guess_district(path)
            stage = guess_stage(path)
            role = guess_role(path)
            rows.append(
                SourceRow(
                    year_root=root.name,
                    year=year,
                    district=district,
                    stage=stage,
                    suite_guess=suite_guess(year, district, stage),
                    role=role,
                    extension=path.suffix.lower(),
                    size=stat.st_size,
                    modified=modified,
                    relative_path=str(path.relative_to(root)),
                    absolute_path=str(path),
                )
            )
    return rows


def write_csv(rows: list[SourceRow]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fields = list(SourceRow.__dataclass_fields__.keys())
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def write_md(rows: list[SourceRow]) -> None:
    by_root = defaultdict(list)
    for row in rows:
        by_root[row.year_root].append(row)

    lines = ["# 选必一严格最终版三年模拟题源文件清单", "", f"- 生成时间：{datetime.now().isoformat(timespec='seconds')}", f"- 源文件总数：{len(rows)}", ""]
    lines.append("## 总览")
    lines.append("")
    lines.append("| 年份目录 | 文件数 | 试卷 | 细则/评标/讲评 | 答案 | OCR/文本 | 其他 |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for root in SOURCE_ROOTS:
        group = by_root.get(root.name, [])
        counts = Counter(row.role for row in group)
        rubric_like = counts["rubric"] + counts["lecture"]
        text_like = counts["ocr"]
        other = len(group) - counts["paper"] - rubric_like - counts["answer"] - text_like
        lines.append(
            f"| {root.name} | {len(group)} | {counts['paper']} | {rubric_like} | {counts['answer']} | {text_like} | {other} |"
        )

    lines.extend(["", "## 分目录明细", ""])
    for root_name in sorted(by_root):
        group = by_root[root_name]
        lines.extend([f"### {root_name}", "", "| 套卷猜测 | 角色 | 文件 |", "|---|---|---|"])
        for row in group:
            lines.append(f"| {row.suite_guess or '未识别'} | {row.role} | `{row.relative_path}` |")
        lines.append("")
    MD_OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    rows = iter_files()
    write_csv(rows)
    write_md(rows)
    print(f"rows={len(rows)}")
    print(CSV_OUT)
    print(MD_OUT)


if __name__ == "__main__":
    main()
