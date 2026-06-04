from __future__ import annotations

import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
ET.register_namespace("w", W)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def para_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        if node.tag == qn("t"):
            parts.append(node.text or "")
        elif node.tag == qn("tab"):
            parts.append("\t")
        elif node.tag in {qn("br"), qn("cr")}:
            parts.append("\n")
    return "".join(parts)


def set_para_text_preserve_first_run(p: ET.Element, text: str) -> None:
    runs = p.findall("w:r", NS)
    if not runs:
        r = ET.SubElement(p, qn("r"))
        t = ET.SubElement(r, qn("t"))
        t.text = text
        return
    first_t = None
    for r in runs:
        for child in list(r):
            if child.tag == qn("t") and first_t is None:
                first_t = child
            elif child.tag in {qn("t"), qn("tab"), qn("br"), qn("cr")}:
                r.remove(child)
    if first_t is None:
        first_t = ET.SubElement(runs[0], qn("t"))
    first_t.text = text
    first_t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def clean_text(text: str) -> str | None:
    stripped = text.strip()

    # Remove audit-only blocks entirely.
    if stripped.startswith("【证据边界】"):
        return None
    if stripped.startswith("【细则边界】"):
        return None
    if stripped.startswith("【使用提醒】"):
        return None

    replacements = {
        "（参考答案讲评复练题）": "（拓展训练题）",
        "（讲评复练迁移题）": "（拓展训练题）",
        "（综合题讲评复练题）": "（综合迁移题）",
        "（逻辑错误与建议部分）": "（建议部分）",
        "评标讲评 “界”复练题（拓展训练题）": "“界”迁移训练题（拓展训练题）",
        "评标讲评 “界”复练题（讲评复练迁移题）": "“界”迁移训练题（拓展训练题）",
        "【背景提示】": "【答题提醒】",
        "【设问说明】": "【答题提醒】",
        "【防误写】": "【答题提醒】",
        "【同题提醒】": "【答题提醒】",
        "【原题问卷图】": "【图示信息】",
        "推理宝典或逻辑规则线": "逻辑规则题型",
        "推理宝典/逻辑规则": "逻辑规则",
        "讲评复练题若来自评标/细则，会标注为“讲评复练迁移题”。": "拓展训练题仅作迁移练习，不与正式主观题混同。",
        "本条只作参考答案讲评复练迁移，不计正式题源。": "本条只作拓展迁移练习。",
        "本题只作综合题讲评复练题，用来练习": "本题作为综合迁移题，用来练习",
        "本题作为综合题讲评复练题，用来练习": "本题作为综合迁移题，用来练习",
        "本题是综合题复练迁移": "本题是综合迁移题",
        "参考答案": "作答提示",
        "评标": "评分口径",
        "评分口径细则": "评分口径",
        "正式细则": "评分要求",
        "终审报告附图显示": "题图信息显示",
        "终审报告附图": "题图信息",
    }
    out = text
    for old, new in replacements.items():
        out = out.replace(old, new)

    # Student-facing cleanup for repeated wide-scope explanatory note.
    out = out.replace(
        "原卷设问确为“蕴含的科学思维”。丰台期末评分口径把这里的“科学思维”作为宽口径统称，说明它不是与逻辑思维、辩证思维、创新思维并列，而是实践中遵循逻辑思维要求、运用辩证思维方法并创新性解决问题的思维方式，所以本题可在科学、辩证、创新三类方法下拆解。",
        "本题中的“科学思维”是宽口径表达，可从科学、辩证、创新三类思维方法中择取与材料最贴合的角度作答。",
    )
    out = out.replace(
        "本条只处理“结论二”对事故归因是否客观的问题；“结论一”属于形式逻辑中的矛盾律/思维一致性规则，应放到逻辑规则题型，不在本条展开。",
        "本条只处理“结论二”对事故归因是否客观的问题；“结论一”属于形式逻辑中的一致性规则，不在本条展开。",
    )
    out = out.replace(
        "本题设问要求“运用科学思维知识”，且评分细则明确“写超前思维、发散思维、联想思维（作为方法名）不得分”，必须先写出具体研究方法（如问卷调查法、访谈法、抽样调查法），思维方法仅用于“说明理由”。",
        "本题要先写出具体研究方法，如问卷调查法、访谈法、抽样调查法；科学思维只用于说明这些方法为什么合理，不要把超前思维、发散思维、联想思维直接当作方法名。",
    )
    out = out.replace(
        "用辩证思维看“界”，要具体分析不同边界的性质：原则底线、法律规则和公共秩序需要守住，不合理隔阂、信息壁垒和创新阻滞则需要在共同利益和发展需要中突破；因此既要守住必要边界维护秩序，也要在协作、跨界融合和创新实践中打开新的联系。",
        "用矛盾分析法看“界”，要在对立统一中具体分析不同边界的性质：原则底线、法律规则和公共秩序需要守住，不合理隔阂、信息壁垒和创新阻滞则需要在共同利益和发展需要中突破；因此既要守住必要边界维护秩序，也要在协作、跨界融合和创新实践中打开新的联系。",
    )
    if not stripped.startswith("【同题说明】"):
        out = out.replace("细则", "评分要求")
    return out


def finalize_docx(src: Path, dst: Path) -> dict:
    tmp = dst.with_suffix(".tmp.docx")
    shutil.copy2(src, tmp)

    with zipfile.ZipFile(tmp, "r") as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    root = ET.fromstring(files["word/document.xml"])
    body = root.find("w:body", NS)
    assert body is not None
    children = list(body)

    remove_indices: set[int] = set()
    remove_titles: list[str] = []
    in_removed_entry = False
    for i, child in enumerate(children):
        text = para_text(child) if child.tag == qn("p") else ""
        if "2026石景山期末 第18题第（2）问" in text:
            in_removed_entry = True
            remove_titles.append(text)
        elif in_removed_entry and (
            text.startswith("补充：")
            or text.startswith("12.")
            or text.startswith("量变与质变")
            or text.startswith("矛盾分析法")
        ):
            in_removed_entry = False
        if in_removed_entry:
            remove_indices.add(i)

    audit_removed = 0
    changed = 0
    for i, child in enumerate(children):
        if i in remove_indices or child.tag != qn("p"):
            continue
        text = para_text(child)
        if not text.strip():
            continue
        cleaned = clean_text(text)
        if cleaned is None:
            remove_indices.add(i)
            audit_removed += 1
        elif cleaned != text:
            set_para_text_preserve_first_run(child, cleaned)
            changed += 1

    for i in sorted(remove_indices, reverse=True):
        body.remove(children[i])

    files["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    with zipfile.ZipFile(dst, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    tmp.unlink(missing_ok=True)
    return {
        "removed_entry_paragraphs": len([i for i in remove_indices if i < len(children)]),
        "removed_titles": remove_titles,
        "audit_paragraphs_removed": audit_removed,
        "paragraphs_changed": changed,
    }


def main() -> None:
    src = Path("选必三双宝典_哲学宝典完全对齐返工_2026-05-25/21_downloads_final_beautify_20260604/inputs/选必三claude美化版.docx")
    dst = Path("选必三双宝典_哲学宝典完全对齐返工_2026-05-25/21_downloads_final_beautify_20260604/delivery/选必三claude美化版_最终学生版_20260604.docx")
    result = finalize_docx(src, dst)
    print(result)


if __name__ == "__main__":
    main()
