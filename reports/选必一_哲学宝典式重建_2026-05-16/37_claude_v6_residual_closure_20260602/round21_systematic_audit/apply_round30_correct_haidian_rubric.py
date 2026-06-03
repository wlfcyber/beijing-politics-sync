from __future__ import annotations

import importlib.util
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第29轮漏项覆盖修正版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第30轮海淀二模正细则修正版_带水印_20260603.docx")
HELPER = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/37_claude_v6_residual_closure_20260602/round21_systematic_audit/apply_round29_user_omission_fix.py")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def load_helper():
    spec = importlib.util.spec_from_file_location("round29_helper", HELPER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


H = load_helper()
qn = H.qn
paragraph_text = H.paragraph_text
make_blank = H.make_blank
make_title = H.make_title
make_field = H.make_field
make_bullet = H.make_bullet

PROMPT = "任选一个议题，参考资料包中的内容，运用《当代国际政治与经济》知识，围绕所选的议题写一篇时政述评。（8分）要求：观点明确；知识运用准确；论述合乎逻辑，条理清晰。"

CANONICAL_TONG = [
    "· 时代背景：和平与发展仍是时代主题；霸权主义和强权政治、单边主义是和平与发展的现实挑战",
    "· 理论：国家间共同利益是国家合作的基础",
    "· 政治多极化：世界多极化是当今国际形势的突出特点；共商共建共享的全球治理观；推动构建人类命运共同体；推动国际关系民主化；国际组织",
]


NEW_ENTRIES = {
    "霸权主义和强权政治、单边主义是和平与发展的现实挑战": {
        "title": "2024海淀二模Q18(1)多极化世界中的民主与全球治理",
        "trigger": "资料包围绕多极化世界中的民主与全球治理展开，既写全球南方国家崛起、单极主导地位被削弱，也写全球治理代表性不足，说明旧有霸权和强权式治理结构已经难以回应各国共同参与治理的要求。",
        "why": "看到“单极主导地位”被削弱、全球治理代表性不足，就不能只写一般合作愿望；这些材料直接指向霸权主义和强权政治带来的治理失衡。时政述评要先说明这种现实挑战，再引出多极化和全球治理民主化的必要性。",
        "answer": "霸权主义和强权政治、单边主义等现实挑战造成全球治理代表性不足，各国应在世界多极化进程中推动全球治理更加民主公正。",
    },
    "共商共建共享的全球治理观": {
        "title": "2024海淀二模Q18(1)多极化世界中的民主与全球治理",
        "trigger": "论坛让不同国家、地区和国际组织围绕民主与全球治理共论互鉴，资料包又强调全球南方国家要在区域和全球治理中发出自己的声音，说明全球治理应由各方共同参与、共同建设、共享成果。",
        "why": "题目要求写“民主与全球治理”述评，资料包的重心不是某一国单独治理，而是多方共同发声、共同参与。要把“民主”落到全球治理层面，就应使用共商共建共享的全球治理观来说明治理方式。",
        "answer": "各国应秉持共商共建共享的全球治理观，让全球南方和更多国际主体共同参与全球治理体系建设，推动治理成果由各方共享。",
    },
    "推动国际关系民主化": {
        "title": "2024海淀二模Q18(1)多极化世界中的民主与全球治理",
        "trigger": "资料包写新兴国家和经济体对全球事务影响力上升，但在国际组织中的代表性仍然不够，全球南方国家要在区域和全球治理中发出声音，直接指向国际关系民主化。",
        "why": "题目选择“多极化世界中的民主与全球治理”时，“民主”不能只停在国内政治概念，而要转化为国际层面的代表性和平等参与。材料中的全球南方发声和代表性不足，正对应推动国际关系民主化。",
        "answer": "新兴国家和全球南方国家影响力上升但代表性不足，要求推动国际关系民主化，提升发展中国家在全球治理中的代表性和发言权。",
    },
}


def is_heading(p: etree._Element, text: str) -> bool:
    style = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return text.startswith("核心答题点：") or bool(style and style[0] in {"3", "4", "5"})


def is_entry_title(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s*20\d{2}", text))


def section_bounds(body: etree._Element, core: str) -> tuple[int, int]:
    children = list(body)
    start = None
    for i, child in enumerate(children):
        if paragraph_text(child) == f"核心答题点：{core}":
            start = i
            break
    if start is None:
        raise RuntimeError(f"core not found: {core}")
    end = len(children)
    for j in range(start + 1, len(children)):
        txt = paragraph_text(children[j])
        if is_heading(children[j], txt):
            end = j
            break
    return start, end


def section_has_key(body: etree._Element, start: int, end: int, key: str) -> bool:
    for p in list(body)[start:end]:
        if key in paragraph_text(p):
            return True
    return False


def next_number(body: etree._Element, start: int, end: int) -> int:
    nums = []
    for p in list(body)[start:end]:
        txt = paragraph_text(p)
        m = re.match(r"^(\d+)\.\s*20\d{2}", txt)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def entry_paragraphs(number: int, core: str) -> list[etree._Element]:
    data = NEW_ENTRIES[core]
    return [
        make_blank(),
        make_blank(),
        make_title(f"{number}. {data['title']}"),
        make_field("【材料触发点】", data["trigger"]),
        make_field("【设问】", PROMPT),
        make_field("【为什么能想到】", data["why"]),
        make_field("【答案落点】", data["answer"]),
        make_field("【同题组】", "（本题8分）"),
        *[make_bullet(x) for x in CANONICAL_TONG],
    ]


def insert_missing_entries(body: etree._Element) -> int:
    inserted = 0
    for core in NEW_ENTRIES:
        start, end = section_bounds(body, core)
        if section_has_key(body, start, end, "2024海淀二模Q18(1)"):
            continue
        n = next_number(body, start, end)
        for p in reversed(entry_paragraphs(n, core)):
            body.insert(end, p)
        inserted += 1
    return inserted


def replace_haidian_tongtizu(body: etree._Element) -> int:
    replaced = 0
    i = 0
    in_target_entry = False
    while i < len(body):
        p = body[i]
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt) or is_heading(p, txt):
            in_target_entry = "2024海淀二模Q18(1)" in txt
        if in_target_entry and txt.startswith("【同题组】"):
            j = i + 1
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("· "):
                    break
                body.remove(body[j])
            for offset, line in enumerate(CANONICAL_TONG, start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            i += len(CANONICAL_TONG)
        i += 1
    return replaced


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None
        inserted = insert_missing_entries(body)
        replaced = replace_haidian_tongtizu(body)
        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())
    print(f"wrote={OUTPUT}")
    print(f"inserted_entries={inserted}")
    print(f"replaced_tongtizu={replaced}")


if __name__ == "__main__":
    main()
