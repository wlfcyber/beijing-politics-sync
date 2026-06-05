from __future__ import annotations

import copy
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("/Users/wanglifei/Desktop/选必二法律与生活_试题细则汇编_学生可发版_v32.docx")
BACKUP = DOCX.with_suffix(DOCX.suffix + ".before_v32_student_audit_fix_20260605.bak")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


E_BOUNDARY_OLD = "边界    E009 正式点分布细则仍待补；E057 为跨模块背景题。"
E_BOUNDARY_NEW = "边界    本册正文统一用“年份·城区·考试·题号”定位题目，不使用内部 E 编号；跨模块或细则边界以对应题目条目中的说明为准。"

EAST_CASE_OLD = (
    "案件2 冯某与其母程某约定，自2018年3月起，冯某每月向程某支付赡养费。2019年1月资料卡"
    "诉讼时效是指权利主体在法定期间内不行使权利，义务人便享有抗辩权（权利人行使其请求权时，"
    "义务人享有的拒绝其请求的权利），从而导致权利人无法胜诉的法律制度。起，冯某再未支付上述费用，"
    "程某从未催讨。2024年2月，程某将冯某诉至法庭，要求其支付5年来未支付的相关费用。冯某以诉讼时效届满为由进行抗辩。"
)
EAST_CASE_NEW = (
    "【材料·案件2】 冯某与其母程某约定，自2018年3月起，冯某每月向程某支付赡养费。"
    "2019年1月起，冯某再未支付上述费用，程某从未催讨。2024年2月，程某将冯某诉至法庭，"
    "要求其支付5年来未支付的相关费用。冯某以诉讼时效届满为由进行抗辩。"
)
EAST_CARD = (
    "【资料卡】 诉讼时效是指权利主体在法定期间内不行使权利，义务人便享有抗辩权"
    "（权利人行使其请求权时，义务人享有的拒绝其请求的权利），从而导致权利人无法胜诉的法律制度。"
)

HAIDIAN_P1_OLD = (
    "【材料】 首例涉“虚拟数字人”侵权案宣判。甲公司系一家以计算机图形学和AI技术为核心的科资料卡技公司，"
    "Ada系甲公司在发展其产品业务过程中打造的超虚拟数字人指具有数字化外形写实虚拟数字人。"
    "甲公司自称于2018年12月创作完成了的虚拟人物，与具备实体的机器人虚拟数字人Ada的正面形象，"
    "为进一步宣传和推广旗下虚 不同，虚拟人依赖显示设备存在。"
)
HAIDIAN_P2_OLD = (
    "拟数字人，又制作完成了虚拟数字人的两段相关视频，并 虚拟数字人拥有人的外观、行为和思维方式，"
    "具有识别外界环境并能于2019年10月、11月通过某平台发布。其中一段用以介与人交流互动的能力。"
    "绍虚拟数字人Ada的场景应用，另一段记录真人演员与虚拟数字人Ada的动作捕捉画面，对虚拟数字人Ada进行商业化使用。"
)
HAIDIAN_P3_OLD = (
    "2022年7月，乙公司通过某社交软件发布上述两段视频，视频的居中位置使用甲公司发布的相关视频内容，"
    "并在片头片尾替换有关标识，以及在整体视频上添加虚拟数字人课程的营销信息，其中一段视频还添加乙公司的注册商标，"
    "并将其他虚拟数字人名称作为标题一部分。甲公司向法院提起诉讼，法院判决乙公司消除影响并赔偿经济损失。"
)
HAIDIAN_MATERIAL = (
    "【材料】 首例涉“虚拟数字人”侵权案宣判。甲公司系一家以计算机图形学和AI技术为核心的科技公司，"
    "Ada系甲公司在发展其产品业务过程中打造的超写实虚拟数字人。甲公司自称于2018年12月创作完成了"
    "虚拟数字人Ada的正面形象，为进一步宣传和推广旗下虚拟数字人，又制作完成了虚拟数字人的两段相关视频，"
    "并于2019年10月、11月通过某平台发布。其中一段用以介绍虚拟数字人Ada的场景应用，另一段记录真人演员"
    "与虚拟数字人Ada的动作捕捉画面，对虚拟数字人Ada进行商业化使用。2022年7月，乙公司通过某社交软件发布"
    "上述两段视频，视频的居中位置使用甲公司发布的相关视频内容，并在片头片尾替换有关标识，以及在整体视频上添加"
    "虚拟数字人课程的营销信息，其中一段视频还添加乙公司的注册商标，并将其他虚拟数字人名称作为标题一部分。"
    "甲公司向法院提起诉讼，法院判决乙公司消除影响并赔偿经济损失。"
)
HAIDIAN_CARD = (
    "【资料卡】 虚拟数字人：指具有数字化外形的虚拟人物，与具备实体的机器人不同，虚拟人依赖显示设备存在。"
    "虚拟数字人拥有人的外观、行为和思维方式，具有识别外界环境并能与人交流互动的能力。"
)

CONTINUATION_HINT = "【提示】 设问、细则与答案落点见下方原题图续块。"


def p_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()


def set_p_text(p: etree._Element, text: str) -> None:
    runs = p.xpath("./w:r", namespaces=NS)
    if not runs:
        runs = [etree.SubElement(p, W + "r")]
    first = runs[0]
    texts = first.xpath("./w:t", namespaces=NS)
    if texts:
        texts[0].text = text
    else:
        t = etree.SubElement(first, W + "t")
        t.text = text
    for extra in first.xpath("./w:t", namespaces=NS)[1:]:
        first.remove(extra)
    for r in runs[1:]:
        p.remove(r)


def make_para_like(template: etree._Element, text: str) -> etree._Element:
    new_p = etree.Element(W + "p")
    p_pr = template.find(W + "pPr")
    if p_pr is not None:
        new_p.append(copy.deepcopy(p_pr))
    r = etree.SubElement(new_p, W + "r")
    t = etree.SubElement(r, W + "t")
    t.text = text
    return new_p


def insert_after(p: etree._Element, text: str) -> None:
    parent = p.getparent()
    parent.insert(parent.index(p) + 1, make_para_like(p, text))


def insert_before(p: etree._Element, text: str) -> None:
    parent = p.getparent()
    parent.insert(parent.index(p), make_para_like(p, text))


def remove_paragraph(p: etree._Element) -> None:
    parent = p.getparent()
    parent.remove(p)


def paragraph_map(root: etree._Element) -> dict[str, list[etree._Element]]:
    out: dict[str, list[etree._Element]] = {}
    for p in root.xpath(".//w:p", namespaces=NS):
        out.setdefault(p_text(p), []).append(p)
    return out


def patch(root: etree._Element) -> dict[str, int]:
    counts: dict[str, int] = {}
    by_text = paragraph_map(root)

    p = by_text[E_BOUNDARY_OLD][0]
    set_p_text(p, E_BOUNDARY_NEW)
    counts["boundary_replaced"] = 1

    p = paragraph_map(root)[EAST_CASE_OLD][0]
    set_p_text(p, EAST_CASE_NEW)
    insert_after(p, EAST_CARD)
    counts["east_case_repaired"] = 1

    by_text = paragraph_map(root)
    p1 = by_text[HAIDIAN_P1_OLD][0]
    p2 = by_text[HAIDIAN_P2_OLD][0]
    p3 = by_text[HAIDIAN_P3_OLD][0]
    set_p_text(p1, HAIDIAN_MATERIAL)
    set_p_text(p2, HAIDIAN_CARD)
    remove_paragraph(p3)
    counts["haidian_virtual_repaired"] = 1

    hints = 0
    for p in list(root.xpath(".//w:p", namespaces=NS)):
        if p_text(p) == "原题图":
            previous_texts = []
            prev = p.getprevious()
            while prev is not None and len(previous_texts) < 8:
                if prev.tag == W + "p":
                    text = p_text(prev)
                    if text:
                        previous_texts.append(text)
                prev = prev.getprevious()
            if CONTINUATION_HINT not in previous_texts:
                insert_before(p, CONTINUATION_HINT)
                hints += 1
    counts["continuation_hints_added"] = hints
    return counts


def main() -> None:
    shutil.copy2(DOCX, BACKUP)
    with ZipFile(DOCX) as zin:
        document_xml = zin.read("word/document.xml")
        root = etree.fromstring(document_xml)
        counts = patch(root)
        new_document_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")

        with NamedTemporaryFile(delete=False) as tmp:
            tmp_path = Path(tmp.name)
        with ZipFile(tmp_path, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = new_document_xml if item.filename == "word/document.xml" else zin.read(item.filename)
                zout.writestr(item, data)
    shutil.move(tmp_path, DOCX)
    for key, value in counts.items():
        print(f"{key}={value}")
    print(f"backup={BACKUP}")


if __name__ == "__main__":
    main()
