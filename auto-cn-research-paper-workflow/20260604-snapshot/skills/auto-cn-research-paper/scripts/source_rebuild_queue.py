#!/usr/bin/env python3
"""Generate an actionable queue for rebuilding missing source files on Mac."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath


@dataclass
class MatrixSource:
    source_id: str
    status: str
    authors: str
    year: str
    title: str
    source: str
    record: str


@dataclass
class MissingFileRow:
    recorded_source: str
    current_source: str
    recorded_text: str
    current_text: str
    evidence_status: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def split_md_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_windows_path(value: str) -> bool:
    return bool(re.match(r"^[A-Za-z]:\\", value)) or "\\" in value


def filename(value: str) -> str:
    value = value.strip().strip("`")
    if not value or value == "missing":
        return ""
    if is_windows_path(value):
        return PureWindowsPath(value).name
    return Path(value).name


def parse_matrix(text: str) -> dict[str, MatrixSource]:
    sources: dict[str, MatrixSource] = {}
    for line in text.splitlines():
        if not line.startswith("| S-"):
            continue
        cells = split_md_row(line)
        if len(cells) < 12:
            continue
        source_id = cells[0]
        sources[source_id] = MatrixSource(
            source_id=source_id,
            status=cells[1],
            authors=cells[2],
            year=cells[3],
            title=cells[4],
            source=cells[5],
            record=cells[11],
        )
    return sources


def parse_missing_rows(text: str) -> list[MissingFileRow]:
    rows: list[MissingFileRow] = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("| ---") or "Recorded source" in line:
            continue
        cells = split_md_row(line)
        if len(cells) < 5:
            continue
        current_source = cells[1]
        current_text = cells[3]
        if current_source == "missing" or current_text == "missing":
            rows.append(MissingFileRow(cells[0], current_source, cells[2], current_text, cells[4]))
    return rows


def extract_urls(record: str) -> list[str]:
    return re.findall(r"https?://[^\s`；;，,|]+", record)


def record_file_candidates(record: str) -> set[str]:
    candidates: set[str] = set()
    for value in re.findall(r"`([^`]+)`", record):
        name = filename(value)
        if name and "." in name:
            candidates.add(name)
    for value in re.findall(r"[A-Za-z]:\\[^`；;，,|]+", record):
        name = filename(value)
        if name and "." in name:
            candidates.add(name)
    return candidates


def best_public_url(source: MatrixSource) -> tuple[str, str]:
    urls = extract_urls(source.record)
    pdf_urls = [url for url in urls if ".pdf" in url.lower() or "/pdf/" in url.lower() or "download" in url.lower()]
    html_urls = [url for url in urls if url not in pdf_urls]
    if "public_journal_pdf" in source.status and pdf_urls:
        return "可公开官方下载", pdf_urls[0]
    if "official_html_full_text" in source.status and html_urls:
        return "可公开官方HTML抓取", html_urls[0]
    if pdf_urls and "cnki" not in pdf_urls[0].lower() and "libproxy.ruc.edu.cn" not in pdf_urls[0].lower():
        return "可公开官方下载", pdf_urls[0]
    return "需人大/CNKI重拉或人工迁移", urls[0] if urls else ""


def match_missing_row(source: MatrixSource, missing_rows: list[MissingFileRow]) -> MissingFileRow | None:
    record_filenames = record_file_candidates(source.record)
    for row in missing_rows:
        source_name = filename(row.recorded_source)
        text_name = filename(row.recorded_text)
        if source_name in record_filenames or text_name in record_filenames:
            return row
    return None


def synthetic_missing_row(source: MatrixSource) -> MissingFileRow | None:
    candidates = sorted(record_file_candidates(source.record))
    if not candidates:
        return None
    source_candidates = [candidate for candidate in candidates if candidate.lower().endswith((".pdf", ".caj", ".kdh", ".html", ".htm"))]
    text_candidates = [candidate for candidate in candidates if candidate.lower().endswith(".txt")]
    source_file = source_candidates[0] if source_candidates else candidates[0]
    text_file = text_candidates[0] if text_candidates else "missing"
    return MissingFileRow(source_file, "missing", text_file, "missing", source.status)


def next_script(action: str) -> str:
    if action == "可公开官方下载":
        return "下载到 `<workspace>/rebuild_sources/` 后运行 `extract_pdfs.py`、`inventory_sources.py`、`source_file_audit.py`。"
    if action == "可公开官方HTML抓取":
        return "保存官方 HTML/正文到 `<workspace>/rebuild_sources/` 和 `<workspace>/fulltext_extract/` 后运行 `source_file_audit.py`。"
    return "通过人大图书馆/CNKI 详情页重新下载 PDF/CAJ，或从旧 Windows 机器迁移同名文件；不得用公开转载替代正式来源。"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Defaults to <run_dir>/24_Mac材料重建队列.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "24_Mac材料重建队列.md"
    sources = parse_matrix(read(run_dir / "03_文献矩阵.md"))
    missing_rows = parse_missing_rows(read(run_dir / "23_材料文件迁移审计.md"))
    matched: list[tuple[MatrixSource, MissingFileRow]] = []
    for source in sources.values():
        missing = match_missing_row(source, missing_rows) or synthetic_missing_row(source)
        if missing:
            matched.append((source, missing))

    public_download_count = 0
    official_html_count = 0
    authorized_database_count = 0
    rows: list[tuple[MatrixSource, MissingFileRow, str, str, str]] = []
    for source, missing in matched:
        action, url = best_public_url(source)
        if action == "可公开官方下载":
            public_download_count += 1
        elif action == "可公开官方HTML抓取":
            public_download_count += 1
            official_html_count += 1
        else:
            authorized_database_count += 1
        rows.append((source, missing, action, url, next_script(action)))

    status = "PASS" if not rows else "INCOMPLETE"
    lines = [
        "# Mac 材料重建队列",
        "",
        "## Summary",
        "",
        f"- rebuild_queue_ready: {'yes' if rows else 'no'}",
        f"- rebuild_item_count: {len(rows)}",
        f"- public_download_count: {public_download_count}",
        f"- official_html_count: {official_html_count}",
        f"- authorized_database_count: {authorized_database_count}",
        "",
        "## Queue",
        "",
        "| Source ID | Title | Authors | Year | Action | Retrieval URL or clue | Missing recorded file | 下一步脚本 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for source, missing, action, url, script_hint in rows:
        missing_name = filename(missing.recorded_source) or missing.recorded_source
        lines.append(
            f"| {source.source_id} | {source.title} | {source.authors} | {source.year} | "
            f"{action} | {url or source.record} | {missing_name} | {script_hint} |"
        )
    lines.extend(
        [
            "",
            "## Rules",
            "",
            "- `可公开官方下载` 只适用于官方期刊、出版社、大学或数据库公开 PDF；下载后仍需本机抽取、hash/来源台账和引用锚点验证。",
            "- `可公开官方HTML抓取` 只适用于官方全文页；页码层仍需数据库版、纸刊版或可核验页面依据。",
            "- `需人大/CNKI重拉或人工迁移` 必须通过人大图书馆/CNKI 授权页重新取得，或迁移旧机器的原 PDF/CAJ/TXT 文件；不得用非官方转载顶替。",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"status={status}")
    print(f"rebuild_item_count={len(rows)}")
    print(f"public_download_count={public_download_count}")
    print(f"official_html_count={official_html_count}")
    print(f"authorized_database_count={authorized_database_count}")
    print(f"out={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
