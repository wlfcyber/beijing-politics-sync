from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from docx import Document


RUN_DIR = Path(__file__).resolve().parents[1]
BASE_BUILDER = RUN_DIR / "tools" / "build_handbook_docs.py"
MD_PATH = RUN_DIR / "05_candidate_md" / "选必三_逻辑与思维_思维宝典_终审锁源版_20260531.md"
OUT_DOCX = RUN_DIR / "07_docx_pdf" / "选必三_逻辑与思维_思维宝典_终极版_20260531.docx"


def load_builder():
    spec = importlib.util.spec_from_file_location("handbook_builder", BASE_BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load builder: {BASE_BUILDER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["handbook_builder"] = module
    spec.loader.exec_module(module)
    return module


def build_with_live_pageref_fields(builder, book: dict) -> Path:
    doc = Document()
    builder.configure_document(doc, book["title"])
    builder.add_title_block(doc, book["title"], book["subtitle"])
    doc.add_page_break()
    builder.emit_front_matter(doc, book["md"], book["title"])

    manual_toc = book["manual_toc"]
    bookmarks = builder.toc_bookmark_map(manual_toc)
    builder.add_toc(doc, manual_toc, bookmarks)
    builder.add_body_section(doc)
    builder.emit_content(doc, book["md"], book["title"], bookmarks)

    book["docx"].parent.mkdir(parents=True, exist_ok=True)
    doc.save(book["docx"])
    builder.normalize_toc_styles(book["docx"])
    return book["docx"]


def main() -> int:
    builder = load_builder()
    thinking_book = {
        "kind": "thinking_ultimate",
        "title": "2026北京高考政治选必三《逻辑与思维》思维宝典",
        "subtitle": "终极版｜三年模拟全触发全链条",
        "md": MD_PATH,
        "docx": OUT_DOCX,
        "manual_toc": [
            ("一、科学思维", 4),
            ("追求认识的客观性", 4),
            ("结果具有预见性", 8),
            ("结果具有可检验性", 9),
            ("二、辩证思维", 11),
            ("整体性", 11),
            ("动态性", 14),
            ("分析与综合", 15),
            ("矛盾分析法", 17),
            ("量变与质变", 19),
            ("适度原则", 20),
            ("辩证否定", 21),
            ("认识发展历程", 22),
            ("三、创新思维", 23),
            ("特点与三新", 23),
            ("联想思维", 26),
            ("发散思维与聚合思维", 29),
            ("逆向思维", 32),
            ("超前思维", 33),
        ],
    }
    out = build_with_live_pageref_fields(builder, thinking_book)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
