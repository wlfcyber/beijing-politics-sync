from __future__ import annotations

import importlib.util
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第31轮正式细则漏项修正版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第32轮回源漏项收敛修正版_带水印_20260603.docx")
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


def set_text(p: etree._Element, text: str) -> None:
    runs = p.xpath(".//w:t", namespaces=NS)
    if runs:
        runs[0].text = text
        for r in runs[1:]:
            r.text = ""


PROMPT_CANON = {
    "2026通州一模Q19": "结合材料，运用《当代国际政治与经济》知识，分析中国元首外交如何为世界注入稳定性与正能量。（8分）",
    "2026西城期末Q20": "结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。",
    "2026朝阳二模Q20(2)": "结合材料，运用《当代国际政治与经济》知识，分析人类命运共同体理念为什么能维护世界和平与发展。",
    "2026房山二模Q20": "结合材料，运用《当代国际政治与经济》知识，分析世界数据组织完善全球数据治理，服务全球数字经济发展的智慧。",
}


PROMPTS = {
    **PROMPT_CANON,
    "2025朝阳二模Q21": "结合材料，运用《当代国际政治与经济》知识，分析周边工作如何服务中国特色大国外交。",
    "2025石景山一模Q17(2)": "结合材料，运用《当代国际政治与经济》知识，说明中国是如何推动全球治理体系完善的。",
}


SAME_GROUPS = {
    "2026通州期末Q21": [
        "· 经济全球化：中国扩大高水平对外开放与制度型开放",
        "· 中国：坚持独立自主、自力更生，增强发展主动权",
    ],
    "2025朝阳二模Q21": [
        "· 中国：周边工作新局面四定位：发展繁荣的重要基础、维护国家安全的重点、运筹外交全局的首要、推动构建人类命运共同体的关键；中国特色大国外交与人类命运共同体",
        "· 理论：共同利益是合作的基础；维护国家利益是主权国家对外活动的出发点和落脚点",
        "· 经济全球化：推进贸易和投资自由化便利化；推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "· 政治多极化：相互尊重、公平正义、合作共赢的新型国际关系；推动国际关系民主化；践行真正的多边主义；推动全球治理体系变革完善，建立更加公正合理的国际政治经济新秩序；推动构建人类命运共同体",
    ],
    "2025石景山一模Q17(2)": [
        "· 政治多极化：共商共建共享的全球治理观；推动国际关系民主化；践行真正的多边主义",
        "· 经济全球化：推进普惠包容的经济全球化",
        "· 联合国：坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序",
    ],
}


NEW_ENTRIES = [
    {
        "key": "2025朝阳二模Q21",
        "core": "周边工作新局面四定位：发展繁荣的重要基础、维护国家安全的重点、运筹外交全局的首要、推动构建人类命运共同体的关键",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式评分细则把周边工作定位为实现发展繁荣的重要基础、维护国家安全的重点、运筹外交全局的首要、推动构建人类命运共同体的关键。",
        "why": "看到题目围绕周边工作与中国特色大国外交，不能只写一般对外合作。细则的“四定位”就是本题总领，提示学生从发展、安全、外交全局和命运共同体四个维度组织答案。",
        "answer": "开创周边工作新局面，是实现发展繁荣的重要基础，是维护国家安全的重点，是运筹外交全局的首要，是推动构建人类命运共同体的关键。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "共同利益是合作的基础",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则变通说明含“共同利益”，材料涉及我国与周边国家开展贸易、促进经济融合和共同发展。",
        "why": "周边工作能够展开合作，不只是因为地理相邻，而是因为各方在发展、稳定和经贸往来中存在共同利益。细则给出共同利益，提示应把周边合作的原因讲清楚。",
        "answer": "共同利益是合作的基础。我国与周边国家在贸易往来、经济融合、地区稳定中具有共同利益，因而能够通过周边合作实现共同发展。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "维护国家利益是主权国家对外活动的出发点和落脚点",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则含“维护国家安全的重点”和“独立自主和平外交政策”等变通方向，材料要求分析周边工作服务中国特色大国外交。",
        "why": "周边工作首先服务国家发展和安全，同时也通过合作机制兼顾地区稳定。看到“维护国家安全的重点”，应迁移到维护国家利益是对外活动的出发点和落脚点。",
        "answer": "维护国家利益是主权国家对外活动的出发点和落脚点。做好周边工作有利于维护我国国家安全和发展利益，也为地区和平稳定创造条件。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "推进贸易和投资自由化便利化",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则写明“贸易、经济融合、贸易投资自由化便利化”，材料涉及与周边国家开展贸易、促进经济融合和共同发展。",
        "why": "周边工作中的经贸合作不是泛泛交流，而是通过贸易和投资便利化降低合作成本、促进要素流动。细则点名贸易投资自由化便利化，应作为经济全球化落点。",
        "answer": "我国通过周边经贸合作推进贸易和投资自由化便利化，促进经济融合和共同发展，为周边稳定繁荣提供经济基础。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则含“经济全球化开放包容普惠平衡共赢”，并要求说明周边工作服务世界发展需要。",
        "why": "周边经贸合作要上升为经济全球化方向，不能只写双边贸易。细则明确开放包容普惠平衡共赢，提示学生把周边合作放入正确经济全球化方向中理解。",
        "answer": "中国通过周边合作推动经济全球化朝更加开放、包容、普惠、平衡、共赢方向发展，使周边国家共享发展机遇。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "相互尊重、公平正义、合作共赢的新型国际关系",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则点名“新型国际关系”，材料涉及创新区域合作机制、搭建合作平台、维护地区和平稳定。",
        "why": "周边工作不只是发展经贸，也要处理好国家间关系。区域合作机制和平稳定平台，正对应相互尊重、公平正义、合作共赢的新型国际关系。",
        "answer": "中国通过创新区域合作机制、搭建合作平台，推动建设相互尊重、公平正义、合作共赢的新型国际关系，维护地区和平稳定。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "推动国际关系民主化",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则把“国际关系民主化”列入区域合作和全球治理变革方向。",
        "why": "周边合作强调各国平等参与、协商解决问题，而不是少数国家主导。细则中的国际关系民主化提示学生从国际关系平等化、民主化角度说明周边工作的世界意义。",
        "answer": "中国推动周边国家平等协商、共同参与区域治理，有利于推动国际关系民主化，增强地区合作的稳定性和包容性。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "践行真正的多边主义",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则点名“真正的多边主义”，材料涉及创新区域合作机制、搭建合作平台、维护地区和平稳定。",
        "why": "区域合作机制和合作平台体现的不是单边安排，而是多方共同参与。细则列出真正的多边主义，说明周边工作可从多边协同角度作答。",
        "answer": "中国在周边工作中践行真正的多边主义，通过区域合作机制和合作平台推动各方共同维护地区和平稳定。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "推动全球治理体系变革完善，建立更加公正合理的国际政治经济新秩序",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则含“全球治理变革”，材料要求说明周边工作服务中国特色大国外交和世界发展需要。",
        "why": "周边工作既是地区外交，也体现中国参与全球治理变革的实践路径。看到区域合作机制、新型国际关系、国际关系民主化，应进一步落到公正合理的国际政治经济新秩序。",
        "answer": "中国通过周边工作推动全球治理体系变革完善，促进国际政治经济秩序朝更加公正合理方向发展。",
    },
    {
        "key": "2025朝阳二模Q21",
        "core": "推动构建人类命运共同体",
        "title": "2025朝阳二模Q21周边工作服务中国特色大国外交",
        "trigger": "正式细则四定位之一是“推动构建人类命运共同体的关键”，并涉及周边命运共同体。",
        "why": "周边是构建人类命运共同体的重要起点。题目问周边工作服务大国外交，细则直接给出命运共同体定位，必须作为独立落点。",
        "answer": "开创周边工作新局面，有利于推动构建周边命运共同体，进而推动构建人类命运共同体。",
    },
    {
        "key": "2025石景山一模Q17(2)",
        "core": "共商共建共享的全球治理观",
        "title": "2025石景山一模Q17(2)中国推动全球治理体系完善",
        "trigger": "正式细则四个2分点之一为“中国主张坚持共商共建共享的全球治理观”。",
        "why": "题目问中国如何推动全球治理体系完善，细则第一点就落在共商共建共享。这里不能只概括为中国方案，应把全球治理方式说清。",
        "answer": "中国坚持共商共建共享的全球治理观，主张各国共同参与全球治理体系建设，共同推动治理成果共享。",
    },
    {
        "key": "2025石景山一模Q17(2)",
        "core": "推动国际关系民主化",
        "title": "2025石景山一模Q17(2)中国推动全球治理体系完善",
        "trigger": "正式细则四个2分点之一为“坚持国家不分大小、强弱、贫富一律平等，共同推动国际关系民主化”。",
        "why": "细则把国家一律平等和国际关系民主化绑定，说明本题不是泛泛讲合作，而是要强调全球治理中的平等参与和民主化方向。",
        "answer": "中国坚持国家不分大小、强弱、贫富一律平等，推动各国平等参与全球治理，共同推动国际关系民主化。",
    },
    {
        "key": "2025石景山一模Q17(2)",
        "core": "推进普惠包容的经济全球化",
        "title": "2025石景山一模Q17(2)中国推动全球治理体系完善",
        "trigger": "正式细则四个2分点之一为“推进普惠包容的经济全球化”。",
        "why": "全球治理体系完善既包括政治治理，也包括经济全球化方向。细则单列普惠包容经济全球化，提示学生把经济治理方向纳入答案。",
        "answer": "中国推动经济全球化朝更加普惠包容方向发展，使不同国家特别是发展中国家更好共享全球化成果。",
    },
    {
        "key": "2025石景山一模Q17(2)",
        "core": "践行真正的多边主义",
        "title": "2025石景山一模Q17(2)中国推动全球治理体系完善",
        "trigger": "正式细则四个2分点之一为“践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序”。",
        "why": "题目涉及全球治理体系完善，细则明确多边主义和联合国核心体系。要避免只写中国担当，必须写出多边主义这一治理路径。",
        "answer": "中国践行真正的多边主义，支持各国在多边机制中协商合作，共同完善全球治理体系。",
    },
    {
        "key": "2025石景山一模Q17(2)",
        "core": "坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序",
        "title": "2025石景山一模Q17(2)中国推动全球治理体系完善",
        "trigger": "正式细则明确要求“坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序”。",
        "why": "全球治理体系完善必须依托国际体系和国际法秩序。细则点名联合国核心体系和国际法基础，说明这是本题稳定的联合国模块迁移点。",
        "answer": "中国坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序，推动全球治理在多边规则框架内完善。",
    },
]


def is_heading(p: etree._Element, text: str) -> bool:
    style = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return text.startswith("核心答题点：") or bool(style and style[0] in {"1", "2", "3", "4", "5"})


def is_entry_title(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s*20\d{2}", text))


def clean_key_title(title: str) -> str | None:
    m = re.search(r"(20\d{2}.+?Q\d+(?:\(\d+\))?)", title.replace(" ", ""))
    return m.group(1) if m else None


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
        m = re.match(r"^(\d+)\.\s*20\d{2}", paragraph_text(p))
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def entry_paragraphs(number: int, data: dict[str, str]) -> list[etree._Element]:
    key = data["key"]
    return [
        make_blank(),
        make_blank(),
        make_title(f"{number}. {data['title']}"),
        make_field("【材料触发点】", data["trigger"]),
        make_field("【设问】", PROMPTS[key]),
        make_field("【为什么能想到】", data["why"]),
        make_field("【答案落点】", data["answer"]),
        make_field("【同题组】", ""),
        *[make_bullet(x) for x in SAME_GROUPS[key]],
    ]


def unify_prompts(body: etree._Element) -> int:
    changed = 0
    current_key = None
    for p in body:
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
        elif is_heading(p, txt):
            current_key = None
        if current_key in PROMPT_CANON and txt.startswith("【设问】"):
            new = f"【设问】  {PROMPT_CANON[current_key]}"
            if txt != new:
                set_text(p, new)
                changed += 1
    return changed


def replace_samegroups(body: etree._Element, only_keys: set[str] | None = None) -> int:
    replaced = 0
    i = 0
    current_key = None
    while i < len(body):
        p = body[i]
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
        elif is_heading(p, txt):
            current_key = None
        if current_key in SAME_GROUPS and (only_keys is None or current_key in only_keys) and txt.startswith("【同题组】"):
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
    return replaced


def remove_entry_for_key_under_core(body: etree._Element, key: str, core: str) -> int:
    start, end = section_bounds(body, core)
    removed = 0
    i = start + 1
    while i < end and i < len(body):
        txt = paragraph_text(body[i])
        if is_entry_title(txt) and key in txt:
            j = i + 1
            while j < len(body):
                t = paragraph_text(body[j])
                if is_entry_title(t) or is_heading(body[j], t):
                    break
                j += 1
            for _ in range(j - i):
                body.remove(body[i])
            removed += 1
            end -= (j - i)
            continue
        i += 1
    return removed


def insert_missing_entries(body: etree._Element) -> int:
    inserted = 0
    for data in NEW_ENTRIES:
        key = data["key"]
        core = data["core"]
        start, end = section_bounds(body, core)
        if section_has_key(body, start, end, key):
            continue
        n = next_number(body, start, end)
        for p in reversed(entry_paragraphs(n, data)):
            body.insert(end, p)
        inserted += 1
    return inserted


def augment_xicheng_2024_q17_tongtizu(body: etree._Element) -> int:
    key = "2024西城二模Q17"
    target = "· 理论：维护国家利益是主权国家对外活动的出发点和落脚点；国家安全与核心利益；当前国际竞争的实质是以经济和科技实力为基础的综合国力较量；科教兴国战略与人才强国战略（人才与国际竞争力）"
    changed = 0
    i = 0
    current_key = None
    in_tong = False
    while i < len(body):
        txt = paragraph_text(body[i]) if body[i].tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
            in_tong = False
        elif is_heading(body[i], txt):
            current_key = None
            in_tong = False
        elif current_key == key and txt.startswith("【同题组】"):
            in_tong = True
        elif current_key == key and in_tong and txt.startswith("· 理论："):
            if "国家安全与核心利益" not in txt:
                set_text(body[i], target)
                changed += 1
        elif in_tong and txt.startswith("【"):
            in_tong = False
        i += 1
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

        removed = remove_entry_for_key_under_core(body, "2026通州期末Q21", "贡献中国智慧、中国方案、中国力量")
        prompt_changes = unify_prompts(body)
        inserted = insert_missing_entries(body)
        replaced = replace_samegroups(body, {"2026通州期末Q21", "2025朝阳二模Q21", "2025石景山一模Q17(2)"})
        xicheng_changes = augment_xicheng_2024_q17_tongtizu(body)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())

    print(f"wrote={OUTPUT}")
    print(f"removed={removed}")
    print(f"prompt_changes={prompt_changes}")
    print(f"inserted={inserted}")
    print(f"replaced_samegroups={replaced}")
    print(f"xicheng_2024_q17_tong_changes={xicheng_changes}")


if __name__ == "__main__":
    main()
