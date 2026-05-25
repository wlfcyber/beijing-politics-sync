#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


DEFAULT_SOURCE_ROOTS = [
    Path(r"C:\Users\Administrator\Desktop\2024各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2025各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2026各区模拟题"),
]
DEFAULT_OUTPUT_ROOT = Path(r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus")
SUPPORTED_SUFFIXES = {".pdf", ".docx", ".pptx", ".rtf", ".txt", ".md", ".csv"}
LEGACY_OFFICE_SUFFIXES = {".doc", ".ppt"}


@dataclass
class ExtractResult:
    status: str
    method: str
    text: str = ""
    notes: str = ""
    rendered_pages: int = 0


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_name(text: str, max_len: int = 90) -> str:
    text = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", text, flags=re.UNICODE).strip("._")
    return text[:max_len] or "source"


def collapse_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def read_plain_text(path: Path) -> ExtractResult:
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "utf-16"):
        try:
            return ExtractResult("text-extracted", f"plain:{encoding}", path.read_text(encoding=encoding))
        except UnicodeDecodeError:
            continue
    return ExtractResult("failed", "plain", notes="could not decode text file")


def iter_xml_text_from_zip(path: Path, members: Iterable[str]) -> str:
    parts: list[str] = []
    with zipfile.ZipFile(path) as zf:
        for name in members:
            try:
                data = zf.read(name)
            except KeyError:
                continue
            try:
                root = ET.fromstring(data)
            except ET.ParseError:
                continue
            for elem in root.iter():
                tag = elem.tag.rsplit("}", 1)[-1]
                if tag in {"t", "instrText"} and elem.text:
                    parts.append(elem.text)
                elif tag in {"br", "p"}:
                    parts.append("\n")
                elif tag == "tab":
                    parts.append("\t")
    return collapse_text("".join(parts))


def extract_docx(path: Path) -> ExtractResult:
    try:
        with zipfile.ZipFile(path) as zf:
            members = [
                name
                for name in zf.namelist()
                if name == "word/document.xml"
                or name.startswith("word/header")
                or name.startswith("word/footer")
                or name.startswith("word/footnotes")
                or name.startswith("word/endnotes")
                or name.startswith("word/comments")
            ]
        text = iter_xml_text_from_zip(path, members)
        if text:
            return ExtractResult("text-extracted", "docx-xml", text)
        return ExtractResult("empty-text", "docx-xml", notes="docx parsed but no text found")
    except Exception as exc:
        return ExtractResult("failed", "docx-xml", notes=repr(exc))


def extract_pptx(path: Path) -> ExtractResult:
    try:
        with zipfile.ZipFile(path) as zf:
            members = sorted(
                name
                for name in zf.namelist()
                if name.startswith("ppt/slides/slide") and name.endswith(".xml")
            )
        text = iter_xml_text_from_zip(path, members)
        if text:
            return ExtractResult("text-extracted", "pptx-xml", text)
        return ExtractResult("empty-text", "pptx-xml", notes="pptx parsed but no slide text found")
    except Exception as exc:
        return ExtractResult("failed", "pptx-xml", notes=repr(exc))


def extract_pdf_text(path: Path) -> tuple[str, str]:
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        chunks = []
        for page in reader.pages:
            chunks.append(page.extract_text() or "")
        text = collapse_text("\n\n".join(chunks))
        if text:
            return text, "pypdf"
    except Exception:
        pass

    try:
        import fitz  # type: ignore

        doc = fitz.open(str(path))
        text = collapse_text("\n\n".join(page.get_text("text") for page in doc))
        if text:
            return text, "pymupdf"
    except Exception:
        pass

    return "", "pdf-text"


def render_pdf_pages(path: Path, render_dir: Path, max_pages: int | None = None) -> tuple[int, str]:
    try:
        import fitz  # type: ignore
    except Exception:
        return 0, "PyMuPDF unavailable; pages not rendered"

    render_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(path))
    page_count = len(doc) if max_pages is None else min(len(doc), max_pages)
    for i in range(page_count):
        page = doc[i]
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        pix.save(str(render_dir / f"page_{i + 1:03d}.png"))
    return page_count, f"rendered {page_count} page(s)"


def extract_pdf(path: Path, render_dir: Path | None, render_scan_pages: bool, max_render_pages: int | None) -> ExtractResult:
    text, method = extract_pdf_text(path)
    if len(text) >= 80:
        return ExtractResult("text-extracted", method, text)

    if render_scan_pages and render_dir is not None:
        count, note = render_pdf_pages(path, render_dir, max_render_pages)
        if count:
            return ExtractResult("rendered-ocr-needed", f"{method}+render", text, notes=note, rendered_pages=count)
        return ExtractResult("ocr-needed", method, text, notes=note)

    return ExtractResult("ocr-needed", method, text, notes="no usable text layer; rerun with --render-scan-pages to cache page images")


def find_soffice() -> str | None:
    for exe in ("soffice", "libreoffice"):
        found = shutil.which(exe)
        if found:
            return found
    common = [
        Path(r"C:\Program Files\LibreOffice\program\soffice.exe"),
        Path(r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"),
    ]
    for path in common:
        if path.exists():
            return str(path)
    return None


def convert_legacy_office(path: Path, converted_dir: Path) -> Path | None:
    soffice = find_soffice()
    converted_dir.mkdir(parents=True, exist_ok=True)
    target_ext = "docx" if path.suffix.lower() == ".doc" else "pptx"
    dest = converted_dir / f"{safe_name(path.stem)}.{target_ext}"

    if soffice:
        with tempfile.TemporaryDirectory() as tmp:
            command = [
                soffice,
                "--headless",
                "--convert-to",
                target_ext,
                "--outdir",
                tmp,
                str(path),
            ]
            subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            candidates = list(Path(tmp).glob(f"*.{target_ext}"))
            if candidates:
                shutil.copy2(candidates[0], dest)
                return dest

    if path.suffix.lower() == ".doc":
        converted = convert_doc_with_word_com(path, dest)
        if converted:
            return converted
    return None


def convert_doc_with_word_com(path: Path, dest: Path) -> Path | None:
    powershell = shutil.which("powershell")
    if not powershell:
        return None
    script = r"""
param(
  [string]$InputPath,
  [string]$OutputPath
)
$ErrorActionPreference = 'Stop'
$word = $null
$doc = $null
$pv = $null
try {
  $word = New-Object -ComObject Word.Application
  $word.Visible = $false
  $word.DisplayAlerts = 0
  try {
    $doc = $word.Documents.Open($InputPath, $false, $true)
  } catch {
    $pv = $word.ProtectedViewWindows.Open($InputPath)
    $doc = $pv.Edit()
  }
  $format = 16
  $doc.SaveAs([ref]$OutputPath, [ref]$format)
  $doc.Close($false)
  if ($pv -ne $null) { $pv.Close() | Out-Null }
  $word.Quit()
  exit 0
} catch {
  if ($pv -ne $null) { $pv.Close() | Out-Null }
  if ($doc -ne $null) { $doc.Close($false) | Out-Null }
  if ($word -ne $null) { $word.Quit() | Out-Null }
  Write-Error $_.Exception.Message
  exit 1
}
"""
    with tempfile.TemporaryDirectory() as tmp:
        script_path = Path(tmp) / "convert_doc_with_word.ps1"
        script_path.write_text(script, encoding="utf-8")
        result = subprocess.run(
            [
                powershell,
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(script_path),
                str(path),
                str(dest),
            ],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    if result.returncode == 0 and dest.exists():
        return dest
    return None


def extract_file(
    path: Path,
    output_root: Path,
    file_hash: str,
    render_scan_pages: bool,
    max_render_pages: int | None,
    converted_dir: Path,
) -> ExtractResult:
    suffix = path.suffix.lower()
    render_dir = output_root / "renders" / file_hash[:16]

    if suffix in {".txt", ".md", ".csv", ".rtf"}:
        return read_plain_text(path)
    if suffix == ".docx":
        return extract_docx(path)
    if suffix == ".pptx":
        return extract_pptx(path)
    if suffix == ".pdf":
        return extract_pdf(path, render_dir, render_scan_pages, max_render_pages)
    if suffix in LEGACY_OFFICE_SUFFIXES:
        converted = convert_legacy_office(path, converted_dir)
        if converted is None:
            return ExtractResult("conversion-needed", "legacy-office", notes="LibreOffice/soffice unavailable or conversion failed")
        result = extract_docx(converted) if converted.suffix.lower() == ".docx" else extract_pptx(converted)
        result.method = f"legacy-office->{converted.suffix.lower().lstrip('.')}:{result.method}"
        return result
    return ExtractResult("unsupported", "none", notes=f"unsupported suffix: {suffix}")


def load_existing_manifest(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            source_path = row.get("source_path", "")
            sha = row.get("sha256", "")
            if source_path and sha:
                rows[source_path] = row
    return rows


def suite_key(row: dict[str, str]) -> str:
    root_name = Path(row["source_root"]).name
    parts = Path(row["relative_path"]).parts
    if len(parts) >= 2:
        return f"{root_name}__{parts[0]}__{parts[1]}"
    if parts:
        return f"{root_name}__{parts[0]}"
    return root_name


def read_cached_text(row: dict[str, str]) -> str:
    text_path = row.get("text_path", "")
    if not text_path:
        return ""
    path = Path(text_path)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def write_gpt_markdown(output_root: Path, rows: list[dict[str, str]]) -> None:
    source_dir = output_root / "gpt_sources"
    suite_dir = output_root / "gpt_suite_bundles"
    source_dir.mkdir(parents=True, exist_ok=True)
    suite_dir.mkdir(parents=True, exist_ok=True)

    index_rows = []
    for row in rows:
        md_name = f"{row['sha256'][:16]}_{safe_name(Path(row['relative_path']).stem)}.md"
        md_path = source_dir / md_name
        text = read_cached_text(row)
        lines = [
            f"# {Path(row['relative_path']).name}",
            "",
            "## Source Metadata",
            "",
            f"- source_path: `{row['source_path']}`",
            f"- source_root: `{row['source_root']}`",
            f"- relative_path: `{row['relative_path']}`",
            f"- suffix: `{row['suffix']}`",
            f"- sha256: `{row['sha256']}`",
            f"- status: `{row['status']}`",
            f"- method: `{row['method']}`",
            f"- chars: `{row['chars']}`",
            f"- text_path: `{row.get('text_path', '')}`",
            f"- render_dir: `{row.get('render_dir', '')}`",
            f"- rendered_pages: `{row.get('rendered_pages', '0')}`",
            f"- notes: {row.get('notes', '')}",
            "",
            "## GPT-Readable Text",
            "",
        ]
        if text:
            lines.append(text)
        elif row.get("render_dir"):
            lines.append("No reliable text layer was extracted. Use the cached rendered page images in `render_dir` for OCR or visual reading.")
        else:
            lines.append("No GPT-readable text was extracted. See `status` and `notes`.")
        md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        row["gpt_markdown_path"] = str(md_path)
        row["suite_key"] = suite_key(row)
        index_rows.append(
            {
                "suite_key": row["suite_key"],
                "relative_path": row["relative_path"],
                "status": row["status"],
                "source_path": row["source_path"],
                "text_path": row.get("text_path", ""),
                "gpt_markdown_path": str(md_path),
                "render_dir": row.get("render_dir", ""),
                "sha256": row["sha256"],
            }
        )

    suites: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        suites.setdefault(row["suite_key"], []).append(row)

    for key, suite_rows in suites.items():
        bundle_path = suite_dir / f"{safe_name(key, 140)}.md"
        bundle_lines = [
            f"# Suite Bundle: {key}",
            "",
            "This bundle is generated from cached source-level extractions. Use it as a first-read packet before returning to raw Word/PDF/PPT files.",
            "",
            "## Sources",
            "",
        ]
        for row in suite_rows:
            bundle_lines.append(
                f"- `{row['relative_path']}` | status `{row['status']}` | method `{row['method']}` | chars `{row['chars']}`"
            )
        for row in suite_rows:
            text = read_cached_text(row)
            bundle_lines.extend(
                [
                    "",
                    "---",
                    "",
                    f"## {row['relative_path']}",
                    "",
                    f"- source_path: `{row['source_path']}`",
                    f"- status: `{row['status']}`",
                    f"- method: `{row['method']}`",
                    f"- sha256: `{row['sha256']}`",
                    f"- gpt_markdown_path: `{row.get('gpt_markdown_path', '')}`",
                    f"- render_dir: `{row.get('render_dir', '')}`",
                    "",
                ]
            )
            if text:
                bundle_lines.append(text)
            elif row.get("render_dir"):
                bundle_lines.append("No reliable text layer was extracted. Use cached rendered page images for OCR or visual reading.")
            else:
                bundle_lines.append(f"No GPT-readable text extracted. Notes: {row.get('notes', '')}")
        bundle_path.write_text("\n".join(bundle_lines).rstrip() + "\n", encoding="utf-8")

    (output_root / "gpt_index.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in index_rows),
        encoding="utf-8",
    )
    (output_root / "README.md").write_text(
        "# Beijing Politics Preprocessed Corpus\n\n"
        "This directory is the reusable first-read cache for all book/module workflows.\n\n"
        "- `manifest.csv`: source-level cache manifest with file hash, status, text path, render path, and GPT markdown path.\n"
        "- `manifest.jsonl`: same data as JSON Lines for programmatic filtering.\n"
        "- `texts/`: raw extracted UTF-8 text, one file per source hash.\n"
        "- `renders/`: cached page images for scan-only PDFs that need OCR or visual reading.\n"
        "- `gpt_sources/`: one Markdown packet per source file, with metadata and extracted text.\n"
        "- `gpt_suite_bundles/`: one Markdown packet per suite folder, combining papers, answer keys, rubrics, reports, and lectures.\n"
        "- `gpt_index.jsonl`: compact GPT-facing index of source markdown and suite membership.\n\n"
        "For a new book/module, read `manifest.csv` or `gpt_index.jsonl` first. Return to raw Office/PDF files only when the source hash changed or the cache status requires OCR/conversion repair.\n",
        encoding="utf-8",
    )


def iter_sources(source_roots: list[Path]) -> Iterable[tuple[Path, Path, Path]]:
    for root in source_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.name.startswith("~$"):
                continue
            suffix = path.suffix.lower()
            if suffix in SUPPORTED_SUFFIXES or suffix in LEGACY_OFFICE_SUFFIXES:
                yield root, path.relative_to(root), path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a reusable readable-text cache for Beijing politics corpus files.")
    parser.add_argument("--source-root", action="append", default=[], help="Corpus source root; can be repeated")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT), help="Preprocessed cache output root")
    parser.add_argument("--force", action="store_true", help="Reprocess even when sha256 and text cache already exist")
    parser.add_argument("--render-scan-pages", action="store_true", help="Render scan-only PDFs to PNG pages for later visual/OCR reading")
    parser.add_argument("--max-render-pages", type=int, default=None, help="Optional cap for rendered pages per PDF")
    parser.add_argument("--limit", type=int, default=None, help="Optional file limit for smoke tests")
    args = parser.parse_args()

    source_roots = [Path(p).expanduser().resolve() for p in args.source_root] or DEFAULT_SOURCE_ROOTS
    output_root = Path(args.output_root).expanduser().resolve()
    texts_dir = output_root / "texts"
    converted_dir = output_root / "converted"
    output_root.mkdir(parents=True, exist_ok=True)
    texts_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = output_root / "manifest.csv"
    jsonl_path = output_root / "manifest.jsonl"
    existing = load_existing_manifest(manifest_path)
    rows: list[dict[str, str]] = []
    processed = skipped = 0

    for index, (root, rel, path) in enumerate(iter_sources(source_roots), start=1):
        if args.limit and index > args.limit:
            break
        source_path = str(path.resolve())
        file_hash = sha256_file(path)
        text_name = f"{file_hash[:16]}_{safe_name(path.stem)}.txt"
        text_path = texts_dir / text_name
        old = existing.get(source_path)
        old_render_dir = Path(old.get("render_dir", "")) if old and old.get("render_dir") else None
        old_render_valid = bool(old_render_dir and old_render_dir.exists() and any(old_render_dir.glob("page_*.png")))
        old_reusable = text_path.exists() or (
            bool(old) and old.get("status") == "rendered-ocr-needed" and old_render_valid
        )
        if old and old.get("sha256") == file_hash and old_reusable and not args.force:
            row = dict(old)
            row["cache_action"] = "skipped-existing"
            skipped += 1
            rows.append(row)
            continue

        result = extract_file(
            path,
            output_root,
            file_hash,
            args.render_scan_pages,
            args.max_render_pages,
            converted_dir,
        )
        if result.text:
            text_path.write_text(result.text, encoding="utf-8")
        elif text_path.exists() and args.force:
            text_path.unlink()

        stat = path.stat()
        row = {
            "source_path": source_path,
            "source_root": str(root),
            "relative_path": str(rel),
            "suffix": path.suffix.lower(),
            "sha256": file_hash,
            "size": str(stat.st_size),
            "mtime": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
            "status": result.status,
            "method": result.method,
            "chars": str(len(result.text)),
            "text_path": str(text_path if result.text else ""),
            "render_dir": str((output_root / "renders" / file_hash[:16]) if result.rendered_pages else ""),
            "rendered_pages": str(result.rendered_pages),
            "notes": result.notes,
            "cache_action": "processed",
        }
        processed += 1
        rows.append(row)

    fieldnames = [
        "source_path",
        "source_root",
        "relative_path",
        "suffix",
        "sha256",
        "size",
        "mtime",
        "status",
        "method",
        "chars",
        "text_path",
        "render_dir",
        "rendered_pages",
        "notes",
        "cache_action",
        "gpt_markdown_path",
        "suite_key",
    ]
    write_gpt_markdown(output_root, rows)
    with manifest_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with jsonl_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary = {
        "output_root": str(output_root),
        "manifest": str(manifest_path),
        "jsonl": str(jsonl_path),
        "rows": len(rows),
        "processed": processed,
        "skipped_existing": skipped,
        "status_counts": {},
    }
    for row in rows:
        summary["status_counts"][row["status"]] = summary["status_counts"].get(row["status"], 0) + 1
    (output_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
