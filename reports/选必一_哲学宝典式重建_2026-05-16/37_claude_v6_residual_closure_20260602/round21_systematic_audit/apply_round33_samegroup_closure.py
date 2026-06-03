from __future__ import annotations

import importlib.util
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第32轮回源漏项收敛修正版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第33轮同题组闭合修正版_带水印_20260603.docx")
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
make_bullet = H.make_bullet


def set_text(p: etree._Element, text: str) -> None:
    runs = p.xpath(".//w:t", namespaces=NS)
    if runs:
        runs[0].text = text
        for r in runs[1:]:
            r.text = ""


PROMPT_CANON = {
    "2025朝阳二模Q21": "结合材料，运用《当代国际政治与经济》知识，说明我国为什么要努力开创周边工作新局面。",
    "2025石景山一模Q17(2)": "结合材料二，运用《当代国际政治与经济》知识，概述完善全球治理的“中国主张”。（8分）",
}


SAME_GROUPS = {
    "2025朝阳二模Q21": [
        "· 理论：共同利益是合作的基础；维护国家利益是主权国家对外活动的出发点和落脚点",
        "· 经济全球化：推进贸易和投资自由化便利化；推动区域经济融合与区域经济一体化；通过区域经济合作维护自由贸易和以世界贸易组织为核心的多边贸易体制；推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "· 政治多极化：相互尊重、公平正义、合作共赢的新型国际关系；维护地区和平与稳定；推动国际秩序和全球治理体系更加公正合理；推动国际关系民主化；推动全球治理体系变革完善，建立更加公正合理的国际政治经济新秩序；推动构建人类命运共同体；践行真正的多边主义",
        "· 中国：周边工作新局面四定位：发展繁荣的重要基础、维护国家安全的重点、运筹外交全局的首要、推动构建人类命运共同体的关键；中国推动构建人类命运共同体；民心相通与文明互鉴",
    ],
    "2025石景山一模Q17(2)": [
        "· 经济全球化：推进普惠包容的经济全球化，推动构建更加开放、包容的全球经济格局；推进普惠包容的经济全球化",
        "· 政治多极化：共商共建共享的全球治理观；推动国际关系民主化；践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序；践行真正的多边主义",
        "· 联合国：坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序",
    ],
}


def is_heading(p: etree._Element, text: str) -> bool:
    style = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return text.startswith("核心答题点：") or bool(style and style[0] in {"1", "2", "3", "4", "5"})


def is_entry_title(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s*20\d{2}", text))


def clean_key_title(title: str) -> str | None:
    m = re.search(r"(20\d{2}.+?Q\d+(?:\(\d+\))?)", title.replace(" ", ""))
    return m.group(1) if m else None


def replace_samegroups_and_prompts(body: etree._Element) -> tuple[int, int]:
    replaced = 0
    prompts = 0
    i = 0
    current_key = None
    while i < len(body):
        p = body[i]
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
        elif is_heading(p, txt):
            current_key = None
        if current_key in PROMPT_CANON and txt.startswith("【设问】"):
            new = f"【设问】  {PROMPT_CANON[current_key]}"
            if txt != new:
                set_text(p, new)
                prompts += 1
        if current_key in SAME_GROUPS and txt.startswith("【同题组】"):
            j = i + 1
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("· "):
                    break
                body.remove(body[j])
            for offset, line in enumerate(SAME_GROUPS[current_key], start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            i += len(SAME_GROUPS[current_key])
        i += 1
    return replaced, prompts


def remove_xicheng_2024_q17_extra_samegroup(body: etree._Element) -> int:
    key = "2024西城二模Q17"
    changed = 0
    current_key = None
    for p in body:
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
        elif is_heading(p, txt):
            current_key = None
        if current_key == key and txt.startswith("· 理论：") and "国家安全与核心利益" in txt:
            new = txt.replace("；国家安全与核心利益", "")
            set_text(p, new)
            changed += 1
    return changed


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None

        replaced, prompts = replace_samegroups_and_prompts(body)
        xicheng = remove_xicheng_2024_q17_extra_samegroup(body)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())

    print(f"wrote={OUTPUT}")
    print(f"replaced_samegroups={replaced}")
    print(f"prompt_changes={prompts}")
    print(f"xicheng_removed_extra={xicheng}")


if __name__ == "__main__":
    main()
