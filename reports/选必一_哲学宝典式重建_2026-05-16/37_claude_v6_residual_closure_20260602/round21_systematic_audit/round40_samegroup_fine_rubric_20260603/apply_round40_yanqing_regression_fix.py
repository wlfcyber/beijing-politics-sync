#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


RUN_DIR = Path(__file__).resolve().parent
ROUND38 = RUN_DIR.parent / "round35_samegroup_rubric_relock" / "apply_round38_rubric_audit_fixes.py"
ROUND39 = RUN_DIR.parent / "round35_samegroup_rubric_relock" / "apply_round39_final_slice3_and_core_emphasis.py"
INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组全量细则复核最终修正版_核心答题点红色强化_学生版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒修正_延庆回归版_学生版_带水印_20260603.docx")
AUDIT_JSON = RUN_DIR / "round40_yanqing_regression_fix.json"

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


R38 = load_module(ROUND38, "round38_helpers")
R39 = load_module(ROUND39, "round39_helpers")

qn = R38.qn
paragraph_text = R38.paragraph_text
set_text = R38.set_text
make_bullet = R38.make_bullet
is_entry_title = R38.is_entry_title
clean_key_title = R38.clean_key_title
is_heading = R38.is_heading


YANQING_KEY = "2025延庆一模Q20(2)"
YANQING_MARKER = "【同题组】 （按原题答题层次）"
YANQING_LINES = [
    "· 答题层次：本题8分，四个角度，每个角度2分；四个角度可以直接写，也可以用相关角度替代，但不重复给分。",
    "· 时代主题（2分）：维护全球产供链韧性和稳定，是推动世界经济可持续发展的重要保障，符合国际社会共同利益，顺应和平与发展的时代主题。",
    "· 经济全球化方向（2分）：中国坚持高质量发展和高水平对外开放，反对“脱钩断链”，推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展。",
    "· 世界多极化（2分）：世界多极化是当今国际形势的突出特点，“脱钩断链”损人不利己；中国在追求本国利益的同时兼顾他国合理关切，推动各国深化产供链合作、共建“世界共赢链”。",
    "· 人类命运共同体（2分）：中国愿同各国携手维护全球产业链供应链稳定畅通，凝聚合作共识，共筑人类命运共同体。",
    "· 可替代角度：国家利益、国际关系、多边主义等角度可以替代相关表达；同一意思不能重复得分。",
]

FORBIDDEN = [
    "证据卡",
    "证据边界",
    "证据层级",
    "源卡",
    "回源",
    "细则复练",
    "待复核",
    "可锁定",
    "未锁定",
    "正式主链",
    "正文条目",
    "工程痕迹",
    "后台",
    "raw_cards",
    "BLOCKED",
    "backend",
    "audit",
    "source",
    "risk",
    "round",
    "参考答案",
    "正式细则",
    "细则",
    "评分",
    "评标",
    "采分",
    "证据",
]


def replace_yanqing(body: etree._Element) -> dict:
    replaced = 0
    details = []
    current_key: str | None = None
    i = 0
    while i < len(body):
        p = body[i]
        text = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(text):
            current_key = clean_key_title(text)
        elif is_heading(text, p):
            current_key = None

        if current_key == YANQING_KEY and text.startswith("【同题组】"):
            set_text(p, YANQING_MARKER)
            j = i + 1
            removed = 0
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("· "):
                    break
                body.remove(body[j])
                removed += 1
            for offset, line in enumerate(YANQING_LINES, start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            details.append({"paragraph_index": i, "removed_lines": removed, "inserted_lines": len(YANQING_LINES)})
            i += len(YANQING_LINES)
        i += 1
    return {"yanqing_replaced": replaced, "details": details}


def audit(body: etree._Element) -> dict:
    paras = [paragraph_text(p) for p in body.xpath(".//w:p", namespaces=NS)]
    full = "\n".join(paras)
    return {
        "forbidden_counts": {token: full.count(token) for token in FORBIDDEN if full.count(token)},
        "yanqing_replacement_phrase_count": full.count("国家利益、国际关系、多边主义等角度可以替代相关表达；同一意思不能重复得分"),
        "yanqing_key_count": full.count(YANQING_KEY),
        "core_style": R39.audit_core_style(body),
    }


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None

        report = replace_yanqing(body)
        R39.force_core_answer_style(body)
        report["audit"] = audit(body)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())

    AUDIT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"wrote={OUTPUT}")


if __name__ == "__main__":
    main()
