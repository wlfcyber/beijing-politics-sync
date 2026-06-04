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


def norm(text: str) -> str:
    return "".join(text.split()).replace("\u3000", "")


def clean_docx(src: Path, dst: Path) -> dict:
    tmp = dst.with_suffix(".tmp.docx")
    shutil.copy2(src, tmp)

    with zipfile.ZipFile(tmp, "r") as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    root = ET.fromstring(files["word/document.xml"])
    body = root.find("w:body", NS)
    assert body is not None
    children = list(body)

    remove_indices: set[int] = set()
    removed_preface: list[str] = []
    removed_method_intro = 0
    removed_toc = 0
    changed_paragraphs = 0
    in_preface = False
    in_toc = False

    for i, child in enumerate(children):
        if child.tag != qn("p"):
            continue
        text = para_text(child).strip()
        compact = norm(text)

        if compact == "前言":
            in_preface = True
            remove_indices.add(i)
            removed_preface.append(text)
            continue

        if in_preface and compact == "目录":
            in_preface = False
            in_toc = True
            remove_indices.add(i)
            removed_toc += 1
            continue

        if in_preface:
            remove_indices.add(i)
            if text:
                removed_preface.append(text)
            continue

        if compact == "目录":
            in_toc = True
            remove_indices.add(i)
            removed_toc += 1
            continue

        if in_toc:
            if compact == "一、科学思维" and "\t" not in text:
                in_toc = False
            else:
                remove_indices.add(i)
                removed_toc += 1
                continue

        if text.startswith("【方法小引】"):
            remove_indices.add(i)
            removed_method_intro += 1
            continue

        cleaned = text
        if "内容审核修正版" in cleaned:
            cleaned = cleaned.replace("内容审核修正版", "逐条核对清洁版")

        cleaned = cleaned.replace(
            "【逻辑错误】（2分）①\"身份\"选项划分标准不一，违反划分应使用同一标准的逻辑要求（同一组选项不能混用身份、职业、年龄等不同标准）；②无障碍设施主要问题的选言判断遗漏其他有选择价值的情况，违反不相容选言判断穷尽选项的要求（各选项要互斥且不漏可选情况）。【改进建议】（4分）",
            "",
        )
        cleaned = cleaned.replace(
            "（另：逻辑错误2分为形式逻辑考点，本册不收）",
            "（另：前半问为形式逻辑考点，本条只训练建议部分）",
        )
        cleaned = cleaned.replace(
            "同一大题第(1)问属于形式逻辑/推理规则线，本条只处理第(2)问超前思维建议，不与第(1)问混写。",
            "同一大题第(1)问考形式逻辑和推理规则，本条只处理第(2)问超前思维建议，不与第(1)问混写。",
        )

        if cleaned != text:
            set_para_text_preserve_first_run(child, cleaned)
            changed_paragraphs += 1

    for i in sorted(remove_indices, reverse=True):
        body.remove(children[i])

    files["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with zipfile.ZipFile(dst, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    tmp.unlink(missing_ok=True)

    return {
        "removed_preface_paragraphs": len(removed_preface),
        "removed_preface_text": removed_preface,
        "removed_method_intro_count": removed_method_intro,
        "removed_toc_paragraphs": removed_toc,
        "removed_total_elements": len(remove_indices),
        "changed_paragraphs": changed_paragraphs,
    }


def main() -> None:
    run = Path("选必三双宝典_哲学宝典完全对齐返工_2026-05-25/22_accuracy_completeness_clean_pass_20260604")
    src = run / "inputs/选必三claude美化版_最终学生版_20260604.docx"
    dst = run / "delivery/选必三claude美化版_逐条核对清洁版_20260604.docx"
    result = clean_docx(src, dst)
    print(result)


if __name__ == "__main__":
    main()
