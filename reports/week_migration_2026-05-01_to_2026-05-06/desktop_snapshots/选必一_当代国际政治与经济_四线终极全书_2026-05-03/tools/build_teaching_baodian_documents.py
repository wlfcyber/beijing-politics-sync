#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


RUN = Path("/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03")
BUILDER = RUN / "tools" / "build_delivery_documents.py"
DELIVERY = RUN / "10_teaching_rebuild_20260504" / "04_delivery"

MD_PATH = DELIVERY / "选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.md"
DOCX_PATH = DELIVERY / "选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.docx"
PDF_PATH = DELIVERY / "选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.pdf"
QA_PATH = DELIVERY / "document_generation_qa_触发宝典_20260504.md"


def load_builder():
    spec = importlib.util.spec_from_file_location("xby1_delivery_builder", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BUILDER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    builder = load_builder()
    builder.MD_PATH = MD_PATH
    builder.DOCX_PATH = DOCX_PATH
    builder.PDF_PATH = PDF_PATH
    builder.QA_PATH = QA_PATH
    builder.TITLE = "选必一《当代国际政治与经济》全题触发宝典"

    text = MD_PATH.read_text(encoding="utf-8")
    builder.build_docx(text)
    builder.build_pdf(text)
    QA_PATH.write_text("\n".join(builder.structural_qa(text)) + "\n", encoding="utf-8")

    print(DOCX_PATH)
    print(PDF_PATH)
    print(QA_PATH)


if __name__ == "__main__":
    main()
