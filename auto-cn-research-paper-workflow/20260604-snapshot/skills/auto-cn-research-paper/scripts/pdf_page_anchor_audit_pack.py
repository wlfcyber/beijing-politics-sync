#!/usr/bin/env python3
"""Build a visible PDF-page audit pack for citation anchors.

The pack is meant for a reviewer who needs to inspect real PDF pages rather
than only a self-reported citation table.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path

import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont


DEFAULT_ROWS = "45,47,48,49,50"


@dataclass
class SourceRecord:
    source_id: str
    title: str
    database: str
    local_file: Path
    sha256: str
    method: str


@dataclass
class CitationRow:
    no: int
    ref: str
    source: str
    anchor: str
    context: str
    excerpt: str


def split_md_row(line: str) -> list[str]:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return cells


def parse_md_table(path: Path, first_header: str) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("|") and first_header in line:
            start = i
            break
    if start is None:
        raise ValueError(f"table with header {first_header!r} not found in {path}")
    headers = split_md_row(lines[start])
    rows: list[dict[str, str]] = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        cells = split_md_row(line)
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        rows.append(dict(zip(headers, cells)))
    return rows


def parse_rows(spec: str) -> set[int]:
    selected: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            left, right = part.split("-", 1)
            selected.update(range(int(left), int(right) + 1))
        else:
            selected.add(int(part))
    return selected


def parse_anchor_pages(anchor: str) -> list[int]:
    pages: set[int] = set()
    for match in re.finditer(r"p\.(\d+)(?:\s*-\s*p?\.(\d+))?", anchor):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if end < start:
            start, end = end, start
        pages.update(range(start, end + 1))
    return sorted(pages)


def load_sources(run_dir: Path) -> dict[str, SourceRecord]:
    records = {}
    rows = parse_md_table(run_dir / "source_provenance_ledger.md", "source_id")
    for row in rows:
        local_file = Path(row["local_file"])
        records[row["source_id"]] = SourceRecord(
            source_id=row["source_id"],
            title=row["title"],
            database=row["database"],
            local_file=local_file,
            sha256=row["sha256"].replace("sha256:", ""),
            method=row["method"],
        )
    return records


def load_citations(run_dir: Path, rows_spec: str) -> list[CitationRow]:
    selected = parse_rows(rows_spec)
    final_rows = parse_md_table(run_dir / "citation_final.md", "No.")
    workbench_rows = {
        int(row["No."]): row for row in parse_md_table(run_dir / "citation_evidence_workbench.md", "No.")
    }
    citations: list[CitationRow] = []
    for row in final_rows:
        no = int(row["No."])
        if no not in selected:
            continue
        wb = workbench_rows.get(no, {})
        citations.append(
            CitationRow(
                no=no,
                ref=row["Ref"],
                source=row["Source"],
                anchor=row["Anchor"],
                context=row.get("Context", ""),
                excerpt=wb.get("Source-page excerpt", ""),
            )
        )
    return citations


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def font_path() -> str | None:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return None


def load_font(size: int) -> ImageFont.ImageFont:
    path = font_path()
    if path:
        return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def wrap_for_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, width: int) -> list[str]:
    wrapped: list[str] = []
    for raw in text.splitlines() or [""]:
        line = ""
        for ch in raw:
            test = line + ch
            if draw.textbbox((0, 0), test, font=font)[2] <= width:
                line = test
            else:
                if line:
                    wrapped.append(line)
                line = ch
        if line:
            wrapped.append(line)
    return wrapped


def make_text_page(path: Path, title: str, fields: list[tuple[str, str]]) -> None:
    width, height = 1654, 2339
    margin = 96
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    title_font = load_font(44)
    label_font = load_font(28)
    body_font = load_font(27)
    y = margin
    draw.text((margin, y), title, font=title_font, fill=(20, 20, 20))
    y += 72
    for label, value in fields:
        draw.text((margin, y), label, font=label_font, fill=(70, 70, 70))
        y += 38
        lines = wrap_for_width(draw, value, body_font, width - margin * 2)
        for line in lines[:12]:
            draw.text((margin, y), line, font=body_font, fill=(15, 15, 15))
            y += 36
        if len(lines) > 12:
            draw.text((margin, y), "...", font=body_font, fill=(15, 15, 15))
            y += 36
        y += 22
        if y > height - 160:
            break
    image.save(path)


def render_pdf_page(pdf_path: Path, page_no: int, out_path: Path, zoom: float = 2.0) -> None:
    with fitz.open(pdf_path) as doc:
        if page_no < 1 or page_no > doc.page_count:
            raise ValueError(f"{pdf_path} has {doc.page_count} pages; requested p.{page_no}")
        page = doc.load_page(page_no - 1)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        pix.save(out_path)


def build_pdf_pack(
    run_dir: Path,
    citations: list[CitationRow],
    sources: dict[str, SourceRecord],
    out_pdf: Path,
    image_dir: Path,
    generated_at: str,
) -> list[dict[str, object]]:
    out = fitz.open()
    cover_png = image_dir / "cover.png"
    make_text_page(
        cover_png,
        "Claude visible page-anchor audit pack",
        [
            ("Run", run_dir.name),
            ("Generated at", generated_at),
            ("Rows", ", ".join(str(c.no) for c in citations)),
            (
                "Audit rule",
                "Each citation is followed by original PDF pages copied from the local source file recorded in source_provenance_ledger.md. The reviewer should inspect these pages, not trust the table alone.",
            ),
        ],
    )
    page = out.new_page(width=595, height=842)
    page.insert_image(page.rect, filename=str(cover_png))
    manifest_rows: list[dict[str, object]] = []
    for citation in citations:
        source = sources[citation.source]
        pages = parse_anchor_pages(citation.anchor)
        pdf_sha = sha256_file(source.local_file)
        if source.sha256 and pdf_sha != source.sha256:
            raise ValueError(f"sha256 mismatch for {source.source_id}: {source.local_file}")
        meta_png = image_dir / f"row_{citation.no:03d}_meta.png"
        make_text_page(
            meta_png,
            f"Row {citation.no} {citation.ref} -> {citation.source} {citation.anchor}",
            [
                ("Source title", source.title),
                ("Database/method", f"{source.database}; {source.method}"),
                ("Local PDF", str(source.local_file)),
                ("SHA256", pdf_sha),
                ("Citation context", citation.context),
                ("Workbench excerpt", citation.excerpt),
                ("Pages included after this sheet", ", ".join(f"p.{p}" for p in pages)),
            ],
        )
        meta_page = out.new_page(width=595, height=842)
        meta_page.insert_image(meta_page.rect, filename=str(meta_png))
        page_pngs: list[str] = []
        with fitz.open(source.local_file) as src_doc:
            for page_no in pages:
                if page_no < 1 or page_no > src_doc.page_count:
                    raise ValueError(f"{source.local_file} has {src_doc.page_count} pages; requested p.{page_no}")
                page_png = image_dir / f"row_{citation.no:03d}_{source.source_id}_p{page_no:03d}.png"
                render_pdf_page(source.local_file, page_no, page_png)
                page_pngs.append(str(page_png))
                out.insert_pdf(src_doc, from_page=page_no - 1, to_page=page_no - 1)
        manifest_rows.append(
            {
                "no": citation.no,
                "ref": citation.ref,
                "source": citation.source,
                "anchor": citation.anchor,
                "pages": pages,
                "source_pdf": str(source.local_file),
                "sha256": pdf_sha,
                "rendered_pngs": page_pngs,
            }
        )
    out.save(out_pdf, garbage=4, deflate=True, clean=True)
    out.close()
    return manifest_rows


def write_manifest(path: Path, run_dir: Path, out_pdf: Path, rows: list[dict[str, object]], generated_at: str) -> None:
    lines = [
        "# Independent PDF Page Anchor Audit Pack",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {generated_at}",
        f"- pdf_pack: {out_pdf}",
        f"- audited_rows: {', '.join(str(row['no']) for row in rows)}",
        "- audit_status: page_images_rendered_from_recorded_source_pdfs",
        "",
        "## Rows",
        "",
        "| No. | Source | Anchor | Pages | Source PDF SHA256 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['no']} | {row['source']} | {row['anchor']} | "
            f"{', '.join('p.' + str(p) for p in row['pages'])} | {row['sha256']} |"
        )
    lines.extend(
        [
            "",
            "## Review Instruction",
            "",
            "This pack is for independent page-level spot checking. The PDF pack contains a metadata sheet for each citation row, followed by original pages copied from the recorded source PDF. A reviewer should compare the citation context with the visible source pages before deciding whether the anchor can be treated as independently checked.",
            "",
            "## Machine Manifest",
            "",
            "```json",
            json.dumps(rows, ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--rows", default=DEFAULT_ROWS, help="Rows like 45,47,48,49,50 or 1-10")
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--generated-at", default="")
    args = parser.parse_args()

    run_dir = args.run_dir.resolve()
    out_dir = (args.out_dir or (run_dir / "pdf_page_anchor_audit")).resolve()
    image_dir = out_dir / "rendered_pages"
    image_dir.mkdir(parents=True, exist_ok=True)
    generated_at = args.generated_at or __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()

    sources = load_sources(run_dir)
    citations = load_citations(run_dir, args.rows)
    if not citations:
        raise SystemExit("no citation rows selected")
    missing = [c.source for c in citations if c.source not in sources]
    if missing:
        raise SystemExit(f"missing source records: {sorted(set(missing))}")
    for citation in citations:
        source = sources[citation.source]
        if source.local_file.suffix.lower() != ".pdf":
            raise SystemExit(f"{citation.source} is not a PDF source: {source.local_file}")
        if not source.local_file.exists():
            raise SystemExit(f"source file missing: {source.local_file}")

    out_pdf = out_dir / "30_Claude独立页锚抽查包.pdf"
    manifest_md = out_dir / "30_Claude独立页锚抽查包.md"
    rows = build_pdf_pack(run_dir, citations, sources, out_pdf, image_dir, generated_at)
    write_manifest(manifest_md, run_dir, out_pdf, rows, generated_at)
    print(f"rows={len(rows)}")
    print(f"pdf={out_pdf}")
    print(f"manifest={manifest_md}")
    print(f"image_dir={image_dir}")


if __name__ == "__main__":
    main()
