from __future__ import annotations

import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_系统复审美化终稿_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第29轮漏项覆盖修正版_带水印_20260603.docx")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def qn(tag: str) -> str:
    prefix, name = tag.split(":")
    return f"{{{NS[prefix]}}}{name}"


def make_ppr(
    *,
    style: str | None = None,
    before: int | None = None,
    after: int | None = None,
    left: int | None = None,
    first_line: int | None = None,
    fill: str | None = None,
    border: str | None = None,
) -> etree._Element:
    ppr = etree.Element(qn("w:pPr"))
    if style:
        ps = etree.SubElement(ppr, qn("w:pStyle"))
        ps.set(qn("w:val"), style)
    if before is not None or after is not None:
        sp = etree.SubElement(ppr, qn("w:spacing"))
        if before is not None:
            sp.set(qn("w:before"), str(before))
        if after is not None:
            sp.set(qn("w:after"), str(after))
    if left is not None or first_line is not None:
        ind = etree.SubElement(ppr, qn("w:ind"))
        if left is not None:
            ind.set(qn("w:left"), str(left))
        if first_line is not None:
            ind.set(qn("w:firstLine"), str(first_line))
    if fill:
        shd = etree.SubElement(ppr, qn("w:shd"))
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), fill)
    if border:
        pbdr = etree.SubElement(ppr, qn("w:pBdr"))
        left_b = etree.SubElement(pbdr, qn("w:left"))
        left_b.set(qn("w:val"), "single")
        left_b.set(qn("w:sz"), "10")
        left_b.set(qn("w:space"), "4")
        left_b.set(qn("w:color"), border)
    return ppr


def make_rpr(*, bold: bool, color: str, size: int = 21, font: str = "Hiragino Sans GB") -> etree._Element:
    rpr = etree.Element(qn("w:rPr"))
    fonts = etree.SubElement(rpr, qn("w:rFonts"))
    for attr in ["ascii", "hAnsi", "eastAsia", "cs"]:
        fonts.set(qn(f"w:{attr}"), font)
    b = etree.SubElement(rpr, qn("w:b"))
    if not bold:
        b.set(qn("w:val"), "0")
    color_el = etree.SubElement(rpr, qn("w:color"))
    color_el.set(qn("w:val"), color)
    sz = etree.SubElement(rpr, qn("w:sz"))
    sz.set(qn("w:val"), str(size))
    return rpr


def add_run(p: etree._Element, text: str, *, bold: bool, color: str, size: int = 21) -> None:
    r = etree.SubElement(p, qn("w:r"))
    r.append(make_rpr(bold=bold, color=color, size=size))
    t = etree.SubElement(r, qn("w:t"))
    if text[:1].isspace() or text[-1:].isspace() or "  " in text:
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def paragraph_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()


def make_blank() -> etree._Element:
    return etree.Element(qn("w:p"))


def make_title(text: str) -> etree._Element:
    p = etree.Element(qn("w:p"))
    p.append(make_ppr(before=120, after=75, left=0, first_line=0))
    add_run(p, text, bold=True, color="1F5E8C", size=24)
    return p


def make_field(label: str, body: str) -> etree._Element:
    p = etree.Element(qn("w:p"))
    if label == "【材料触发点】":
        p.append(make_ppr(before=45, after=65, left=0, first_line=0, fill="EAF3F8"))
        label_color = "2F6F9F"
    elif label == "【设问】":
        p.append(make_ppr(before=45, after=65, left=0, first_line=0))
        label_color = "536471"
    elif label == "【为什么能想到】":
        p.append(make_ppr(before=45, after=65, left=0, first_line=0))
        label_color = "1F5E8C"
    elif label == "【答案落点】":
        p.append(make_ppr(before=80, after=100, left=0, first_line=0, fill="FFF2CC", border="D2691E"))
        add_run(p, f"{label}  ", bold=True, color="8A3B12", size=21)
        add_run(p, body, bold=True, color="111111", size=21)
        return p
    elif label == "【同题组】":
        p.append(make_ppr(before=80, after=35, left=0, first_line=0))
        add_run(p, label, bold=True, color="697780", size=20)
        if body:
            add_run(p, f"  {body}", bold=False, color="697780", size=19)
        return p
    else:
        p.append(make_ppr(before=45, after=65, left=0, first_line=0))
        label_color = "1F5E8C"
    add_run(p, f"{label}  ", bold=True, color=label_color, size=21)
    add_run(p, body, bold=False, color="202124", size=21)
    return p


def make_bullet(text: str) -> etree._Element:
    p = etree.Element(qn("w:p"))
    p.append(make_ppr(before=0, after=45, left=260, first_line=0))
    if "：" in text:
        prefix, rest = text.split("：", 1)
        add_run(p, f"{prefix}：", bold=True, color="1F5E8C", size=19)
        add_run(p, rest, bold=False, color="27323A", size=19)
    else:
        add_run(p, text, bold=False, color="27323A", size=19)
    return p


def make_new_entry() -> list[etree._Element]:
    prompt = "任选一个议题，参考资料包中的内容，运用《当代国际政治与经济》知识，围绕所选的议题写一篇时政述评。（8分）要求：观点明确；知识运用准确；论述合乎逻辑，条理清晰。"
    return [
        make_blank(),
        make_blank(),
        make_title("15. 2024海淀二模Q18(1)多极化世界中的民主与全球治理"),
        make_field(
            "【材料触发点】",
            "资料包呈现全球南方国家崛起、金砖国家等机制作用增强，以及人工智能、大数据带来的共同治理难题；各国之所以需要围绕民主与全球治理展开互鉴和协作，是因为在提升全球治理代表性、弥合技术治理缺口上存在共同利益。",
        ),
        make_field("【设问】", prompt),
        make_field(
            "【为什么能想到】",
            "题目要求围绕“多极化世界中的民主与全球治理”写时政述评，资料包把全球南方发声、国际组织作用增强和人工智能治理缺口放在一起，说明全球治理不是单个国家能独自完成的事务。回答各国为什么能够通过论坛和国际机制共同推动治理改革时，应先写国家间共同利益是国家合作的基础，再接到各方围绕共同挑战推动全球治理民主化。",
        ),
        make_field(
            "【答案落点】",
            "国家间共同利益是国家合作的基础，人工智能治理缺口、全球南方代表性不足等共同挑战，使各国需要依托国际组织和合作机制推动全球治理更加民主、有效。",
        ),
        make_field("【同题组】", "（本题8分）"),
        make_bullet("· 时代背景：和平与发展仍是时代主题"),
        make_bullet("· 理论：国家间共同利益是国家合作的基础"),
        make_bullet("· 政治多极化：推动构建人类命运共同体；国际组织；世界多极化是当今国际形势的突出特点"),
    ]


def is_entry_title(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s*20\d{2}", text))


def is_heading(p: etree._Element, text: str) -> bool:
    style = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return text.startswith("核心答题点：") or bool(style and style[0] in {"3", "4", "5"})


def insert_theory_bullet_after_time_background(body: etree._Element) -> int:
    inserted = 0
    i = 0
    in_target_entry = False
    in_target_tong = False
    while i < len(body):
        child = body[i]
        txt = paragraph_text(child) if child.tag == qn("w:p") else ""
        if is_entry_title(txt) or is_heading(child, txt):
            in_target_entry = "2024海淀二模Q18(1)" in txt
            in_target_tong = False
        elif in_target_entry and txt.startswith("【同题组】"):
            in_target_tong = True
        elif in_target_entry and in_target_tong and txt.startswith("· 时代背景："):
            next_txt = paragraph_text(body[i + 1]) if i + 1 < len(body) and body[i + 1].tag == qn("w:p") else ""
            if not (next_txt.startswith("· 理论：") and "共同利益" in next_txt):
                body.insert(i + 1, make_bullet("· 理论：国家间共同利益是国家合作的基础"))
                inserted += 1
                i += 1
        elif in_target_tong and txt and not txt.startswith("· "):
            in_target_tong = False
        i += 1
    return inserted


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None

        inserted_existing = insert_theory_bullet_after_time_background(body)

        children = list(body)
        insert_at = None
        for i, child in enumerate(children):
            if paragraph_text(child) == "核心答题点：共同利益是合作的基础":
                insert_at = i
                break
        if insert_at is None:
            raise RuntimeError("Cannot find duplicate共同利益 heading insertion point")
        for p in reversed(make_new_entry()):
            body.insert(insert_at, p)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())
    print(f"wrote={OUTPUT}")
    print(f"updated_existing_tongtizu={inserted_existing}")


if __name__ == "__main__":
    main()
