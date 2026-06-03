from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒全量修正_核心答题点红色强化_标点话术清理版_学生版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒全量修正_核心答题点红色强化_标点话术清理_终检完善版_学生版_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round40_final_empty_core_notes_report.json")

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}


def qn(tag: str) -> str:
    prefix, local = tag.split(":")
    assert prefix == "w"
    return f"{{{W_NS}}}{local}"


def paragraph_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def make_note_paragraph(text: str) -> etree._Element:
    p = etree.Element(qn("w:p"))
    p_pr = etree.SubElement(p, qn("w:pPr"))

    spacing = etree.SubElement(p_pr, qn("w:spacing"))
    spacing.set(qn("w:before"), "0")
    spacing.set(qn("w:after"), "80")
    spacing.set(qn("w:line"), "320")
    spacing.set(qn("w:lineRule"), "auto")

    ind = etree.SubElement(p_pr, qn("w:ind"))
    ind.set(qn("w:left"), "360")

    r = etree.SubElement(p, qn("w:r"))
    r_pr = etree.SubElement(r, qn("w:rPr"))
    color = etree.SubElement(r_pr, qn("w:color"))
    color.set(qn("w:val"), "5F6B73")
    sz = etree.SubElement(r_pr, qn("w:sz"))
    sz.set(qn("w:val"), "21")
    sz_cs = etree.SubElement(r_pr, qn("w:szCs"))
    sz_cs.set(qn("w:val"), "21")
    t = etree.SubElement(r, qn("w:t"))
    t.text = text
    return p


def analyze(root: etree._Element) -> dict:
    body = root.find(".//w:body", namespaces=NS)
    paras = body.findall(qn("w:p"))
    texts = [paragraph_text(p) for p in paras]
    core_idxs = [i for i, t in enumerate(texts) if t.startswith("核心答题点：")]
    empty = []
    for pos, i in enumerate(core_idxs):
        end = core_idxs[pos + 1] if pos + 1 < len(core_idxs) else len(texts)
        seg = texts[i + 1 : end]
        has_question = any(s and s[0].isdigit() and ". " in s[:7] and "Q" in s for s in seg)
        has_note = any("本点用于同题辨析" in s for s in seg)
        if not has_question and not has_note:
            empty.append({"index": i, "heading": texts[i]})
    full = "\n".join(texts)
    return {
        "core_heading_count": len(core_idxs),
        "empty_core_without_question_or_note": empty,
        "samegroup_count": full.count("【同题组】"),
        "answer_halfwidth_commas_remaining": sum(t.count(",") for t in texts if t.startswith("【答案落点】")),
        "forbidden_remaining": {
            "可写为": full.count("可写为"),
            "得分点": full.count("得分点"),
            "中国版本点出": full.count("中国版本点出"),
        },
    }


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(INPUT)

    targets = {
        "核心答题点：积极\"走出去\"、对外直接投资、克服贸易壁垒": "· 本点用于同题辨析：看到企业出海、海外市场、贸易壁垒等材料，先按上方【学生判别】确定方向，再与下方“技术质量、国际规则或市场多元化”等配对点合并作答。",
        "核心答题点：反对单边主义、霸权主义和强权政治": "· 本点用于同题辨析：看到单边霸凌、恃强凌弱、零和博弈等材料，先判断错误倾向，再按题意接多边主义、国际关系民主化或公正合理国际秩序。",
        "核心答题点：我国外交政策的宗旨是维护世界和平、促进共同发展": "· 本点用于同题辨析：看到中国以合作、援助、倡议或外交行动促进和平与共同发展时，先判断外交宗旨，再按题意接独立自主和平外交政策或人类命运共同体。",
    }

    with ZipFile(INPUT, "r") as zin:
        document_xml = zin.read("word/document.xml")
        root = etree.fromstring(document_xml)
        before = analyze(root)
        body = root.find(".//w:body", namespaces=NS)
        paras = body.findall(qn("w:p"))

        inserted = []
        for p in list(paras):
            text = paragraph_text(p)
            note = targets.get(text)
            if not note:
                continue
            idx = body.index(p)
            next_text = paragraph_text(body[idx + 1]) if idx + 1 < len(body) and body[idx + 1].tag == qn("w:p") else ""
            if "本点用于同题辨析" in next_text:
                continue
            body.insert(idx + 1, make_note_paragraph(note))
            inserted.append(text)

        after = analyze(root)
        new_document_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")

        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    data = new_document_xml
                zout.writestr(item, data)

    report = {"input": str(INPUT), "output": str(OUTPUT), "inserted_notes": inserted, "before": before, "after": after}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
