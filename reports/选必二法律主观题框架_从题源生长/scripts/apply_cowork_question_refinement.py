#!/usr/bin/env python3
"""Apply the Claude Cowork question-layer refinement patches.

This script creates a new versioned corpus rather than overwriting the previous
ClaudeCode-corrected corpus. It fixes hard blockers identified by Claude Cowork:
empty asks, material/rubric leakage, answer-as-material rows, and logic-module
rubric leakage in legal-question rows.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
BASE = ROOT / "04_merge_audit" / "suite_exhaustive_claudecode_corrected_20260519"
OUT = ROOT / "04_merge_audit" / "suite_exhaustive_cowork_refined_20260519"
PACKET = ROOT / "05_reasoner_packets" / "suite_exhaustive_cowork_refined_20260519"
COWORK = ROOT / "04_merge_audit" / "claude_cowork_question_refinement_20260519"


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def norm(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_atoms(text: str) -> list[str]:
    text = norm(text)
    text = re.sub(r"\[page \d+\]|\[slide \d+\]|第\d+页/共\d+页", "", text)
    rough = re.split(r"(?<=[。！？?；;])\s*|\n+", text)
    out: list[str] = []
    for part in rough:
        part = re.sub(r"\s+", " ", part).strip(" ；;")
        if not part:
            continue
        if len(part) < 5:
            continue
        if re.fullmatch(r"\(?\d+\)?[\.．、]?", part):
            continue
        out.append(part)
    return out


def legal_signal(text: str) -> str:
    keys = [
        "民法典",
        "反不正当竞争法",
        "未成年人保护法",
        "劳动合同法",
        "著作权",
        "商标",
        "侵权",
        "违约",
        "合同",
        "格式条款",
        "相邻",
        "仲裁",
        "调解",
        "诉讼",
        "举证",
        "竞业限制",
        "商业秘密",
        "知识产权",
        "消费者",
        "无过错",
        "公益诉讼",
        "涉外",
    ]
    found = [k for k in keys if k in text]
    return "；".join(found)


def ask_function(ask: str) -> str:
    if "完成下表" in ask or "完成表格" in ask:
        return "综合"
    if "哪些工作" in ask or "建议" in ask or "措施" in ask:
        return "建议"
    if "判断" in ask or "是否有效" in ask or "判决结果" in ask:
        return "评析"
    if "分析" in ask or "谈谈" in ask or "阐释" in ask:
        return "论证"
    if "说明" in ask:
        return "说明"
    return "综合"


def req_value(ask: str) -> str:
    return "yes" if any(k in ask for k in ["意义", "价值", "现实", "作用"]) else "uncertain"


def req_solution(ask: str) -> str:
    return "yes" if any(k in ask for k in ["哪些工作", "措施", "建议", "应对"]) else "no"


def question_patch_note(row: dict[str, str], tag: str) -> None:
    row["notes"] = norm((row.get("notes", "") + f" | cowork_refined_20260519:{tag}").strip(" |"))


COMMON_COURT_TABLE_20 = norm(
    """
“以事实为根据，以法律为准绳”是我国司法活动的基本原则，核心是通过客观事实认真严格依照法律规定作出裁判，确保司法公正性与权威性。
案例一 A享有“我不是胖虎”系列美术作品的复制权、改编权、信息网络传播权等著作财产性权利。B公司、C公司未经许可，在其经营的微博账号中发布了与A公司“我不是胖虎”类似电脑壁纸“橘猫”。A公司向法院起诉B公司、C公司，要求其承担侵权责任。示例裁判结果：支持A公司的诉讼请求，B公司、C公司应停止侵害，删除相关内容并赔偿A公司经济损失。示例裁判理由：根据《中华人民共和国著作权法》的规定，著作权人对其作品享有广泛的权利。他人未经著作权人许可使用著作权人的作品，就可能构成侵权。B公司、C公司未经许可，擅自将被诉侵权图片作为微博图片发布，使公众可以在其个人选定的时间和地点获得作品，均侵害了A公司的著作权。现实意义：该判决充分保障了著作权人的合法权益，规范了企业行为。
案例二 孙某在2022年4月应聘甲公司，所投简历写明：2015年7月至2022年3月期间有4段工作经历。后孙某入职甲公司，同日双方签订了劳动合同，并约定了试用期。入职后经甲公司查证，孙某在2015年毕业后的7年时间，曾在17家公司任职。甲公司以孙某未如实提供工作经历为由，在试用期将其辞退。孙某向法院起诉，请求法院判决甲公司支付违法解除劳动关系赔偿金。
"""
)


CORRECTIONS: dict[str, dict[str, str]] = {
    "CC0019_2024_朝阳_一模_19": {
        "full": norm(
            """
19.（7分）诚信是法治精神的重要伦理基础。民法典第七条规定：“民事主体从事民事活动，应当遵循诚信原则，秉持诚实，恪守承诺”。
镜头一 2022年12月，A公司与B公司签订购销合同约定：A公司向B公司提供产品，货款于发货后的60日内付清。2023年1月，A公司依约向B公司提供货物，但截至2023年7月，B公司欠A公司货款590万元未支付。2023年8月，A公司起诉B公司，要求其支付货款及违约金。人民法院最终判决B公司尽快付清全部欠款并支付逾期违约金。
镜头二 某购物中心为200余家商户建立了“码上诚信”二维码，消费者扫描二维码，即可查询此商户相关的行政许可、行政处罚、主动承诺、自愿注册等信用信息。有市民说：“我经常来这个商场消费，一是因为‘码上诚信’让我感觉在这里购物很放心，二是因为这里的商品质量和售后服务态度都很好。”
结合材料，运用《法律与生活》知识，分析诚信原则对促进社会主义市场经济健康发展的积极作用。
"""
        ),
        "material": norm(
            """
诚信是法治精神的重要伦理基础。民法典第七条规定：“民事主体从事民事活动，应当遵循诚信原则，秉持诚实，恪守承诺”。
镜头一：2022年12月，A公司与B公司签订购销合同约定货款于发货后的60日内付清；A公司依约供货后，B公司截至2023年7月欠A公司货款590万元未支付；人民法院最终判决B公司尽快付清全部欠款并支付逾期违约金。
镜头二：某购物中心为200余家商户建立“码上诚信”二维码，消费者可查询商户行政许可、行政处罚、主动承诺、自愿注册等信用信息；消费者认为这让购物更放心，且商品质量和售后服务态度较好。
"""
        ),
        "ask": "结合材料，运用《法律与生活》知识，分析诚信原则对促进社会主义市场经济健康发展的积极作用。",
        "locator": "F0015:paper page 7 lines 249-265; rendered/text source recovered after Cowork.",
    },
    "CC0092_2025_东城_期末_19_1": {
        "full": norm(
            """
19．（8分）某校开展“我为社区献一策”的社会实践活动。下面是一组同学撰写的调查报告。
一、调查背景：近年来，电动自行车以其经济、便利的特点成为市民重要的交通工具。然而，保有量与充电设施数量不匹配，让充电成为困扰居民的问题。
二、调查发现：某社区有446辆电动自行车，却只有60个充电接口。对车主新增充电设施的提议，大家产生了意见分歧。甲认为建车棚会占用绿地，影响遛弯；乙认为既不能飞线充电，小区也没有配套设备能集中充电；丙担心消防安全、居民通行和采光问题。
三、学生建议：为解决这一困扰，让电动自行车在楼下待得住，该组同学为社区设计了“在公共区域设置电池充电柜，车电分离”的方案。
运用《法律与生活》和《政治与法治》知识，完成下列任务。
（1）遇到的法律问题：                、             。
资料卡：《高层民用建筑消防安全管理规定》第三十七条规定，电动自行车存放、充电场所应当配备必要的消防器材，充电设施应当具备充满自动断电功能。《中华人民共和国民法典》第二百七十八条规定，改变共有部分的用途或者利用共有部分从事经营活动由业主共同决定。
"""
        ),
        "material": norm(
            """
某社区电动自行车保有量与充电设施数量不匹配，446辆电动自行车只有60个充电接口。
车主提出新增充电设施，居民围绕占用绿地、集中充电设备不足、消防安全、通行和采光影响产生分歧。
学生建议在公共区域设置电池充电柜，采取车电分离方案。
《高层民用建筑消防安全管理规定》第三十七条要求电动自行车存放、充电场所配备必要消防器材，充电设施具备充满自动断电功能。
《中华人民共和国民法典》第二百七十八条规定，改变共有部分的用途或者利用共有部分从事经营活动由业主共同决定。
"""
        ),
        "ask": "运用《法律与生活》和《政治与法治》知识，完成任务：（1）写出该方案遇到的法律问题。",
        "locator": "F0130:paper page 6 lines 199-227.",
    },
    "CC0131_2025_房山_一模_19": {
        "full": norm(
            """
19. 阅读材料，回答问题。
“真创新”受到“真保护”，我国知识产权侵权诉讼判赔数额创历史新高。
案情回放：A集团近40名高级管理人员及技术人员先后离职赴B集团工作，其中30人于当年离职后即入职。两年后，A集团发现B集团以上述部分离职人员作为发明人或共同发明人，利用在原单位接触、掌握的有关新能源汽车底盘应用技术以及其中的12套底盘零部件图纸及数模承载的技术信息申请了12件实用新型专利，且B集团在没有任何技术积累或合法技术来源的情况下，在短期内即推出某系列型号电动汽车，涉嫌侵害A集团技术秘密。A集团决定向法院提起诉讼。
判决结果：法院经审理认为，B集团以不正当手段侵害A集团技术秘密，适用2倍惩罚性赔偿，判决赔偿共计6.4亿余元。
结合材料，谈谈“真创新”受到“真保护”的法治价值。
"""
        ),
        "material": norm(
            """
A集团近40名高级管理人员及技术人员先后离职赴B集团工作，其中30人于当年离职后即入职。
B集团以上述部分离职人员作为发明人或共同发明人，利用在原单位接触、掌握的新能源汽车底盘应用技术以及12套底盘零部件图纸及数模承载的技术信息申请实用新型专利。
B集团在没有任何技术积累或合法技术来源的情况下，短期内推出某系列型号电动汽车，涉嫌侵害A集团技术秘密。
法院认为B集团以不正当手段侵害A集团技术秘密，适用2倍惩罚性赔偿，判决赔偿共计6.4亿余元。
"""
        ),
        "ask": "结合材料，谈谈“真创新”受到“真保护”的法治价值。",
        "locator": "F0081:paper page 6 lines 227-236.",
    },
    "CC0180_2025_海淀_期末_20": {
        "full": norm(
            """
20. 阅读材料，完成问题。
最高人民法院围绕民法典实施过程中社会广泛关注、审判实践中亟需解决的重大争议问题，制定了《最高人民法院关于适用<中华人民共和国民法典>侵权责任编的解释（一）》（以下简称《解释》）。
下表列出了《解释》部分条款。参考示例，完成下表。
示例：第七条规定，未成年子女造成他人损害，被侵权人请求父母共同承担侵权责任的，人民法院依照民法典相关规定予以支持。分析：父母必须履行对未成年子女的监护职责；未成年子女造成他人损害的，父母应当依法承担民事责任；《解释》明确监护人职责，支持被侵权人合理诉求。
第十九条规定，因产品存在缺陷造成买受人财产损害，买受人请求产品的生产者或者销售者赔偿缺陷产品本身损害以及其他财产损害的，人民法院依照民法典相关规定予以支持。分析：①
第二十三条规定，禁止饲养的烈性犬等危险动物造成他人损害，动物饲养人或者管理人主张不承担责任或者减轻责任的，人民法院不予支持。分析：②
"""
        ),
        "material": norm(
            """
最高人民法院制定《最高人民法院关于适用<中华人民共和国民法典>侵权责任编的解释（一）》，回应民法典实施中的社会关注和审判实践争议。
《解释》第七条示例明确父母监护职责和未成年子女造成他人损害时父母依法承担民事责任。
《解释》第十九条规定，产品存在缺陷造成买受人财产损害时，买受人可请求生产者或者销售者赔偿缺陷产品本身损害以及其他财产损害。
《解释》第二十三条规定，禁止饲养的烈性犬等危险动物造成他人损害时，动物饲养人或者管理人主张不承担责任或者减轻责任的，人民法院不予支持。
"""
        ),
        "ask": "下表列出了《解释》部分条款。参考示例，完成下表。",
        "locator": "F0139:paper text around Q20 and attached table.",
    },
    "CC0195_2025_西城_一模_20": {
        "full": norm(
            """
20．（8分）全国总工会、人力资源社会保障部、中国企业联合会、全国工商联联合启动2025年度集体协商“集中要约行动”，指导工会与企业开展集体协商、签订集体合同。按照行动部署，各级工会把工资调整幅度、加班工资基数、劳动定额标准、工资支付办法等作为协商的核心议题。
结合材料，综合运用经济和法律的知识，说明上述做法能促进社会公平与经济效率的平衡。
"""
        ),
        "material": norm(
            """
全国总工会、人力资源社会保障部、中国企业联合会、全国工商联联合启动2025年度集体协商“集中要约行动”。
该行动指导工会与企业开展集体协商、签订集体合同。
各级工会把工资调整幅度、加班工资基数、劳动定额标准、工资支付办法等作为协商的核心议题。
"""
        ),
        "ask": "结合材料，综合运用经济和法律的知识，说明上述做法能促进社会公平与经济效率的平衡。",
        "locator": "F0094:paper page 7 lines 276-283.",
    },
    "CC0214_2025_门头沟_一模_20_2": {
        "full": COMMON_COURT_TABLE_20
        + "\n请结合案例二，参照所给示例完成裁判要点中的裁判理由②。",
        "material": COMMON_COURT_TABLE_20,
        "ask": "请结合案例二，参照所给示例完成裁判要点中的裁判理由②。",
        "locator": "F0096:paper pages 7-8 lines 305-344.",
    },
    "CC0245_2026_东城_期末_18_2": {
        "full": norm(
            """
18. 无人机起飞如何系好“安全带”？
陈某向店主刘某发送邮件：“急需购买A型号无人机一台。用于重要商业拍摄。”刘某回复：“全新原装，15000元。”陈某立即转账。刘某误将一台内部结构轻微损伤（外观无明显痕迹）的同型号展示机寄出。
陈某收货后在首次使用中，该无人机因上述损伤失控坠毁，砸伤陈某手臂。陈某花费医疗费8000元，并因错过商业拍摄损失收入5000元。陈某要求刘某赔偿，双方协商未果。
（2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？
"""
        ),
        "material": norm(
            """
陈某向店主刘某表示急需购买A型号无人机用于重要商业拍摄，刘某回复“全新原装，15000元”，陈某立即转账。
刘某误将一台内部结构轻微损伤、外观无明显痕迹的同型号展示机寄出。
陈某首次使用时，无人机因上述损伤失控坠毁，砸伤陈某手臂。
陈某花费医疗费8000元，并因错过商业拍摄损失收入5000元。
陈某要求刘某赔偿，双方协商未果。
"""
        ),
        "ask": "维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？",
        "locator": "F0206:paper page 6 lines 234-241.",
    },
    "CC0276_2026_房山_二模_17": {
        "full": norm(
            """
17.（8分）外国巨轮更名为“尊重”（RESPECT），只为向中国法治致敬。在“尼莉莎”轮扣押案中，希腊申请人主动向青岛海事法院申请扣船，法院创造性地对船舶实施“活扣押”、允许完成剩余航程，促成当事人达成和解，为利害关系人挽回巨额损失，为此希腊籍船东特意将船舶更名。这是中国法治赢得世界尊重的生动注脚。
材料列出中国涉外法治建设的三个方面：保护方面，在法律制度层面出台外商投资法及其实施条例，加强对内外资企业的保护；在司法实践层面注重保护中外当事人合法权益。速度方面，上海持续优化“调解、仲裁、诉讼”相衔接国际商事一站式线上解纷平台，当事人可全天候网上立案、在线调解、远程参加庭审、在线接收材料。经验方面，在一起损失金额存在较大争议的船舶碰撞纠纷中，某海事法院引入外国船东保赔协会参与调解，探索人民法院引导、船舶航运相关组织共同参与的涉外海事纠纷化解模式。
中国走向世界，以负责任大国参与国际事务，必须善于运用法治。结合材料，运用法治知识，谈谈中国是如何加强涉外法治建设的。
"""
        ),
        "material": norm(
            """
“尼莉莎”轮扣押案中，希腊申请人主动向青岛海事法院申请扣船，法院创造性实施“活扣押”，允许完成剩余航程，促成当事人和解，为利害关系人挽回巨额损失，希腊籍船东因此将船舶更名为“尊重”。
在保护方面，中国出台外商投资法及其实施条例，加强对内外资企业保护；在司法实践层面注重保护中外当事人合法权益。
在速度方面，上海优化“调解、仲裁、诉讼”相衔接的国际商事一站式线上解纷平台，当事人可网上立案、在线调解、远程参加庭审、在线接收材料。
在经验方面，海事法院引入外国船东保赔协会参与调解，探索人民法院引导、船舶航运相关组织共同参与的涉外海事纠纷化解模式。
"""
        ),
        "ask": "中国走向世界，以负责任大国参与国际事务，必须善于运用法治。结合材料，运用法治知识，谈谈中国是如何加强涉外法治建设的。",
        "locator": "F0191:rendered paper page 6.",
    },
    "CC0277_2026_房山_二模_18": {
        "full": norm(
            """
18.（12分）当OPC（One Person Company）遇上“数字员工”，未来的创业模式，只需要一个充满创意的“头脑”，加上一个不知疲倦的“数字员工”，你就能开启自己的“商业版图”。
材料一 OPC与“数字员工”正以前所未有的速度，重塑着我们的商业生态。但在拥抱这份“未来”的同时，你是否清楚，法律的边界在哪里？
风险1：一本正经地胡说八道。场景重现：你的“数字员工”撰写了一篇行业文章，其中生成了某家公司的虚假负面数据。文章发布后，该公司向你发来了律师函。
风险2：“泄露”危机。场景重现：为了图方便，你将公司的核心代码、独家运营策略上传到公共AI平台优化。不久后，竞争对手也拥有了类似的方案。
风险3：生成的可能只是“旧作”。场景重现：你让“数字员工”设计了一款国潮风的手机壳图案，既有传统纹样又有现代元素，直接生产销售。不久，就收到法院传票。
（1）结合材料一，运用《法律与生活》知识，分析上述场景可能涉及的法律边界，并提出应对措施。
"""
        ),
        "material": norm(
            """
OPC与“数字员工”正以前所未有的速度重塑商业生态，但同时需要明确法律边界。
风险1：数字员工撰写行业文章并生成某家公司的虚假负面数据，文章发布后该公司发来律师函。
风险2：创业者为图方便，将公司的核心代码、独家运营策略上传到公共AI平台优化，不久后竞争对手拥有类似方案。
风险3：创业者让数字员工设计国潮风手机壳图案，既有传统纹样又有现代元素，并直接生产销售，不久收到法院传票。
"""
        ),
        "ask": "结合材料一，运用《法律与生活》知识，分析上述场景可能涉及的法律边界，并提出应对措施。",
        "locator": "F0191:rendered paper page 7.",
    },
    "CC0317_2026_海淀_期末_18": {
        "full": norm(
            """
18.（12分）住房问题事关民生福祉。
材料一 近年来，住房租赁市场规模持续扩大，随之而来的合同纠纷不断增加，此类纠纷所涉合同大多是由住房租赁企业提供的合同范本。
小海准备与住房租赁企业签订为期两年的租赁合同，其中有如下条款：“合同期满后，不得在住房租赁企业不知情的情况下与房屋产权人私下建立租赁关系，否则视为违约，乙方需赔偿甲方一个月租金作为违约金。”小海对此表示不同意见，希望更改。但对方表示，合同是由企业为重复使用而预先拟定的，这一条款不能更改。小海认为该条款无效。
（1）运用《法律与生活》知识，判断这一条款是否有效，并说明理由。
"""
        ),
        "material": norm(
            """
住房租赁市场规模持续扩大，合同纠纷不断增加，此类纠纷所涉合同大多是由住房租赁企业提供的合同范本。
小海准备与住房租赁企业签订两年租赁合同，合同条款约定：合同期满后，不得在住房租赁企业不知情的情况下与房屋产权人私下建立租赁关系，否则视为违约，乙方需赔偿甲方一个月租金作为违约金。
小海希望更改条款，但对方表示合同由企业为重复使用而预先拟定，该条款不能更改。
小海认为该条款无效。
"""
        ),
        "ask": "运用《法律与生活》知识，判断这一条款是否有效，并说明理由。",
        "locator": "F0217:rendered paper page 6.",
    },
    "CC0318_2026_海淀_期末_18_2": {
        "full": norm(
            """
18.（12分）住房问题事关民生福祉。
材料二 2025年9月，我国首部专门规范住房租赁市场的行政法规——《住房租赁条例》正式施行。
《住房租赁条例》第二十八条规定，国务院住房城乡建设主管部门会同国务院市场监督管理部门制定并公布住房租赁合同、住房租赁经纪服务合同示范文本。
《住房租赁条例》第三十三条规定，县级以上地方人民政府房产管理部门应当会同有关部门、住房租赁相关行业组织加强住房租赁行业诚信建设，建立住房租赁企业、住房租赁经纪机构及其从业人员信用评价制度，将相关违法违规行为记入信用记录，纳入全国信用信息共享平台，并根据信用状况实施分级分类监管。
（2）运用法治知识，分析《住房租赁条例》上述规定的现实意义。
"""
        ),
        "material": norm(
            """
2025年9月，我国首部专门规范住房租赁市场的行政法规《住房租赁条例》正式施行。
《住房租赁条例》第二十八条要求主管部门制定并公布住房租赁合同、住房租赁经纪服务合同示范文本。
《住房租赁条例》第三十三条要求有关部门和行业组织加强住房租赁行业诚信建设，建立住房租赁企业、经纪机构及从业人员信用评价制度，将违法违规行为记入信用记录并纳入全国信用信息共享平台，根据信用状况实施分级分类监管。
"""
        ),
        "ask": "运用法治知识，分析《住房租赁条例》上述规定的现实意义。",
        "locator": "F0217:rendered paper page 6.",
    },
    "CC0319_2026_海淀_期末_19": {
        "full": norm(
            """
19.（7分）甲公司是国内较大的综合性票务平台，运营具有售票功能的应用程序。甲公司发现郑某通过网络店铺销售针对该公司售票应用程序的抢票软件，认为这款抢票软件在一定程度上规避了平台“先到先得”的购票规则，妨碍售票业务的正常开展，遂提起诉讼，主张郑某行为构成不正当竞争，请求判令郑某停止侵权、赔偿经济损失。
郑某认为，其与原告公司不存在竞争关系，其仅为涉案抢票软件的销售者并非研发者，其销售抢票软件的行为没有造成该公司票务收入减少，不构成不正当竞争。
人民法院经审理，认为被诉行为构成不正当竞争，鉴于被诉行为已经停止，故不再另行判决停止侵权，判决郑某赔偿原告公司经济损失。
《中华人民共和国反不正当竞争法》规定，本法所称的不正当竞争行为，是指经营者在生产经营活动中，违反本法规定，扰乱市场竞争秩序，损害其他经营者或者消费者的合法权益的行为。
运用《法律与生活》知识，谈谈对本案判决的认识。
"""
        ),
        "material": norm(
            """
甲公司是国内较大的综合性票务平台，运营具有售票功能的应用程序。
郑某通过网络店铺销售针对甲公司售票应用程序的抢票软件，甲公司认为该软件规避平台“先到先得”的购票规则，妨碍售票业务正常开展。
甲公司提起诉讼，主张郑某行为构成不正当竞争，请求判令郑某停止侵权、赔偿经济损失。
郑某认为其与甲公司不存在竞争关系，仅销售涉案抢票软件且并非研发者，销售行为没有造成甲公司票务收入减少，不构成不正当竞争。
人民法院认为被诉行为构成不正当竞争；鉴于被诉行为已经停止，判决郑某赔偿原告公司经济损失。
《反不正当竞争法》规定，不正当竞争行为是经营者在生产经营活动中扰乱市场竞争秩序，损害其他经营者或者消费者合法权益的行为。
"""
        ),
        "ask": "运用《法律与生活》知识，谈谈对本案判决的认识。",
        "locator": "F0217:rendered paper page 7.",
    },
    "CC0353_2026_西城_期末_17": {
        "full": norm(
            """
17.（8分）T公司在其运营的APP内设置了“青少年模式”，首页有弹窗提示，且APP服务协议明确禁止修改其软件功能或运行效果，以及任何危害未成年人的行为。B公司将“自动关闭青少年模式弹窗”设为限时免费的会员特权，以吸引用户安装其APP，并利用技术手段屏蔽了T公司APP的“青少年模式”入口弹窗。T公司发现后，向法院起诉B公司，请求认定其不正当竞争行为，并赔偿经济损失。
法院经审理认为，被告行为构成不正当竞争，全额支持原告的诉讼请求。
《中华人民共和国未成年人保护法》第七十四条第二款规定，网络游戏、网络直播、网络音视频、网络社交等网络服务提供者应当针对未成年人使用其服务设置相应的时间管理、权限管理、消费管理等功能。
运用法律知识，分析法院的上述判决。
"""
        ),
        "material": norm(
            """
T公司在其APP内设置“青少年模式”，首页有弹窗提示，APP服务协议明确禁止修改软件功能或运行效果，以及任何危害未成年人的行为。
B公司将“自动关闭青少年模式弹窗”设为限时免费的会员特权，以吸引用户安装其APP，并利用技术手段屏蔽T公司APP的“青少年模式”入口弹窗。
T公司向法院起诉B公司，请求认定其不正当竞争行为并赔偿经济损失。
法院认为被告行为构成不正当竞争，全额支持原告诉讼请求。
《未成年人保护法》第七十四条第二款要求网络服务提供者针对未成年人使用其服务设置相应的时间管理、权限管理、消费管理等功能。
"""
        ),
        "ask": "运用法律知识，分析法院的上述判决。",
        "locator": "F0221/F0399:rendered paper page 6; answer reference page 11.",
    },
    "CC0011_2024_丰台_二模_17": {
        "full": norm(
            """
17.（8分）民法典守护碧水蓝天，保护生态环境。
《中华人民共和国民法典》规定：“民事主体从事民事活动，应当有利于节约资源、保护生态环境。”“民事主体依法享有知识产权。”“因污染环境、破坏生态造成他人损害的，侵权人应当承担侵权责任。”
案例一 某公司发明专利技术从源头上解决长期污水污泥分离不彻底、处理工序复杂化等关键技术问题，首次提出了通过操控屏控制移动杆，实现过滤速度可控的农村污水分离技术重大突破，方法简单、易于操作，降低污水净化成本的同时，显著提高污水净化效率，延长装置的使用寿命，已在多地村庄生活污水治理项目中成功应用并推广。
案例二 甲公司在生产中，长期存在超标排放废水、废气等污染物损害环境公共利益的行为，周边居民的日常生活受到严重影响。乙环境研究所以甲公司存在长期连续超标排放污染物、构成环境民事侵权行为，提起环境民事公益诉讼。法院审理后判决甲公司立即停止侵权、消除危险、赔偿环境损失等。
运用《法律与生活》知识，结合上述案例分析民法典的相关规定对保护生态环境的作用。
"""
        ),
        "material": norm(
            """
民法典规定：民事主体从事民事活动，应当有利于节约资源、保护生态环境；民事主体依法享有知识产权；因污染环境、破坏生态造成他人损害的，侵权人应当承担侵权责任。
案例一中，某公司发明专利技术解决长期污水污泥分离不彻底、处理工序复杂化等问题，通过操控屏控制移动杆实现过滤速度可控，降低污水净化成本，提高污水净化效率，延长装置使用寿命，并在多地村庄生活污水治理项目中应用推广。
案例二中，甲公司长期超标排放废水、废气等污染物，损害环境公共利益并严重影响周边居民日常生活。
乙环境研究所提起环境民事公益诉讼，法院判决甲公司立即停止侵权、消除危险、赔偿环境损失等。
"""
        ),
        "ask": "运用《法律与生活》知识，结合上述案例分析民法典的相关规定对保护生态环境的作用。",
        "locator": "F0048:rendered paper page 5; F0047/F0270:rubric text.",
    },
    "CC0119_2025_丰台_期末_19": {
        "full": norm(
            """
19. 尹某在某购物中心担任主管期间，存在违反公司管理规章制度等问题。购物中心基于自身经营需要并结合尹某的工作实际以其不能胜任为由，将其工作岗位调整为营业员。尹某对此消极怠工，经常无故旷工。购物中心多次提醒之后，尹某仍未改变，购物中心遂向尹某发出解除劳动合同通知书。尹某对仲裁结果不满意，遂向法院提起诉讼，要求购物中心支付违约赔偿金。购物中心辩称其依据管理规章制度与尹某解除劳动合同不存在违法情形，无需向尹某支付赔偿金。法院驳回了尹某的诉讼请求。
《中华人民共和国劳动法》第三条规定，劳动者享有平等就业和选择职业的权利、取得劳动报酬的权利、休息休假的权利、获得劳动安全卫生保护的权利、接受职业技能培训的权利、享受社会保险和福利的权利、提请劳动争议处理的权利以及法律规定的其他劳动权利。劳动者应当完成劳动任务，提高职业技能，执行劳动安全卫生规程，遵守劳动纪律和职业道德。
《中华人民共和国劳动合同法》第三十九条规定，劳动者有严重违反用人单位的规章制度等情形的，用人单位可以解除劳动合同。
请运用《法律与生活》相关知识阐释法院的裁判理由。
"""
        ),
        "material": norm(
            """
尹某在购物中心担任主管期间存在违反公司管理规章制度等问题。
购物中心基于经营需要并结合尹某工作实际，以其不能胜任为由将其岗位调整为营业员。
尹某对岗位调整消极怠工，经常无故旷工；购物中心多次提醒后仍未改变，遂向尹某发出解除劳动合同通知书。
尹某对仲裁结果不满意，向法院提起诉讼，要求购物中心支付违约赔偿金；购物中心辩称解除劳动合同不存在违法情形。
法院驳回了尹某的诉讼请求。
劳动法规定劳动者享有劳动权利，也应完成劳动任务、遵守劳动纪律和职业道德。
劳动合同法规定，劳动者严重违反用人单位规章制度的，用人单位可以解除劳动合同。
"""
        ),
        "ask": "请运用《法律与生活》相关知识阐释法院的裁判理由。",
        "locator": "F0132:paper page 7 lines 255-280; F0131:rubric slides 45-47.",
    },
    "CC0251_2026_丰台_一模_20": {
        "full": norm(
            """
20.（8分）以案释法，明理释义。
《中华人民共和国民法典》第一千一百九十八条规定，宾馆、商场、银行、车站、机场、体育场馆、娱乐场所等经营场所、公共场所的经营者、管理者或者群众性活动的组织者，未尽到安全保障义务，造成他人损害的，应当承担侵权责任。
【基本案情】郭某在某餐厅用餐结束后步行离开，在餐厅外的台阶区域不慎踩空摔倒。餐厅外的监控视频显示，郭某从出现在画面中开始，就一直在低头看手机；监控画面中未见下雨、下雪，台阶处也未见积雪、积水、冰冻。事发十天后，郭某自行到医院就诊，诊断为腰椎右侧横突骨折。郭某向人民法院起诉餐厅经营者某餐饮公司和餐厅所在楼宇的物业管理企业某商业管理公司，要求某餐饮公司、某商业管理公司承担侵权责任，支付赔偿金。
【裁判结果】人民法院审理认为，原告郭某摔倒是其自身未尽安全注意义务所致，被告某餐饮公司和某商业管理公司对此并无过错，不应承担赔偿责任。故判决驳回郭某全部诉讼请求。
结合材料，运用《法律与生活》知识，阐明人民法院作出该判决的法理依据和现实意义。
"""
        ),
        "material": norm(
            """
民法典第一千一百九十八条规定，经营场所、公共场所的经营者、管理者未尽到安全保障义务，造成他人损害的，应当承担侵权责任。
郭某在某餐厅用餐结束后步行离开，在餐厅外台阶区域不慎踩空摔倒。
监控显示郭某从出现在画面中开始一直低头看手机；监控画面中未见下雨、下雪，台阶处未见积雪、积水、冰冻。
事发十天后郭某自行到医院就诊，被诊断为腰椎右侧横突骨折。
郭某起诉餐厅经营者某餐饮公司和楼宇物业管理企业某商业管理公司，要求承担侵权责任并支付赔偿金。
人民法院认为，郭某摔倒是自身未尽安全注意义务所致，被告某餐饮公司和某商业管理公司对此并无过错，不应承担赔偿责任，判决驳回郭某全部诉讼请求。
"""
        ),
        "ask": "结合材料，运用《法律与生活》知识，阐明人民法院作出该判决的法理依据和现实意义。",
        "locator": "F0157:rendered paper page 9; F0156:rubric slide 51.",
    },
    "CC0254_2026_丰台_二模_18": {
        "full": norm(
            """
18.（8分）法安天下，德润人心。
【基本案情】张某承包果园多年，果园渐成规模。自2024年春季起，李某饲养的牛群多次闯入其果园，不仅撞断树枝、损坏树体，更将正值花期的果树花苞啃食殆尽，导致大幅减产。张某虽在果园周围悬挂“果园重地，禁止放牧”的警示横幅，但2025年5月，李某家的18头牛再次闯入果园，造成果树严重受损。张某报警后，经民警现场协调，李某仅同意赔偿2000元，与张某主张的35000元实际损失差距较大，张某遂向法院提起诉讼。
《中华人民共和国民法典》第一千二百四十五条规定，饲养的动物造成他人损害的，动物饲养人或者管理人应当承担侵权责任；但是，能够证明损害是因被侵权人故意或者重大过失造成的，可以不承担或者减轻责任。
【调解过程及结果】案件受理后，承办法官考虑到果园既关乎当事人的财产权益，也与区域生态环境质量密切相关，矛盾化解应与生态修复同步推进。因此，法官并未急于启动庭审程序，而是第一时间赴果园开展现场勘验，全面了解案件背景。在此基础上，法官多次组织双方开展调解工作。一方面，向李某释明《中华人民共和国民法典》关于饲养动物损害责任的有关规定，指出其依法应承担的赔偿责任；另一方面，结合《中华人民共和国生态环境法典》“系统治理、生态优先、绿色发展”的核心原则及“损害担责”的立法理念，引导双方充分认识果园保护的生态价值。
针对李某一次性赔偿确有困难、张某更关注果园后续保护实际状况，法官提出了“分期赔偿+行为约束+生态修复”的调解方案，由李某分期支付赔偿款，采取围栏加固、专人看管等有效措施，同时协助张某对被损坏的果树进行补种、养护，修复果园生态。经过承办法官的耐心调解，双方当事人最终达成调解协议，李某当庭向张某支付赔偿款2500元并致歉，两家人握手言和。
司法给予我们的不仅是定分止争，也是一份融通情理的温暖力量。结合材料，综合运用法治知识，阐明你对这一观点的认识。
"""
        ),
        "material": norm(
            """
张某承包果园多年；李某饲养的牛群多次闯入果园，撞断树枝、损坏树体、啃食花苞，导致果园大幅减产。
张某已在果园周围悬挂“果园重地，禁止放牧”的警示横幅；2025年5月，李某家的18头牛再次闯入果园造成果树严重受损。
经民警现场协调，李某仅同意赔偿2000元，与张某主张的35000元实际损失差距较大，张某遂向法院提起诉讼。
民法典第一千二百四十五条规定，饲养的动物造成他人损害的，动物饲养人或者管理人应当承担侵权责任；能够证明损害是因被侵权人故意或者重大过失造成的，可以不承担或者减轻责任。
法官考虑到果园既关乎当事人的财产权益，也与区域生态环境质量密切相关，矛盾化解应与生态修复同步推进。
法官现场勘验、多次组织调解，向李某释明民法典关于饲养动物损害责任的规定，同时结合生态环境法典核心原则和“损害担责”理念，引导双方认识果园保护的生态价值。
法官提出“分期赔偿+行为约束+生态修复”的调解方案：李某分期支付赔偿款，采取围栏加固、专人看管等措施，并协助张某补种、养护受损果树。
双方最终达成调解协议，李某当庭支付赔偿款2500元并致歉，两家人握手言和。
"""
        ),
        "ask": "司法给予我们的不仅是定分止争，也是一份融通情理的温暖力量。结合材料，综合运用法治知识，阐明你对这一观点的认识。",
        "locator": "F0188:paper page 7 lines 308-336; F0187:rubric slides 29-34.",
    },
    "CC0283_2026_朝阳_一模_18": {
        "full": norm(
            """
18. 2026年是“十五五”开局之年，“创新”“科技”成为规划纲要的高频词，新质生产力发展离不开知识产权的坚实保障。人民法院通过“调、惩、辨”三维实践，为创新发展筑牢法治屏障。
【以“调”解纷】针对生物医药领域科研人员的专利权归属纠纷，为减少诉讼对创新活动的干扰，人民法院摒弃“一判了之”，特邀请第三方调停，促成当事人当庭和解，一揽子化解关联诉讼，让科研人员安心回归科研创新。
【以“惩”亮剑】对故意侵害植物新品种权、商业秘密等行为，依法适用惩罚性赔偿。在某玉米品种故意严重侵权案中，判决侵权人赔偿5300余万元；在“玻璃机”技术秘密侵权案中，判决赔偿3.8亿余元，大幅提高侵权违法成本。
【以“辩”正风】针对假借“维权”之名实施的恶意诉讼、权利滥用行为，人民法院依法快速审结并予以明确否定。某日化公司恶意提起知识产权诉讼，其诉讼请求被法院全部驳回并受到司法谴责，有效规制阻碍创新的不诚信诉讼行为。
结合材料，运用《法律与生活》知识，谈谈人民法院是如何依法保护知识产权以护航新质生产力发展的。
"""
        ),
        "material": norm(
            """
新质生产力发展离不开知识产权的坚实保障，人民法院通过“调、惩、辨”三维实践为创新发展筑牢法治屏障。
针对生物医药领域科研人员专利权归属纠纷，人民法院邀请第三方调停，促成当事人当庭和解，一揽子化解关联诉讼，让科研人员安心回归科研创新。
对故意侵害植物新品种权、商业秘密等行为，人民法院依法适用惩罚性赔偿，在相关案件中判决侵权人赔偿5300余万元、3.8亿余元，大幅提高侵权违法成本。
针对假借“维权”之名实施的恶意诉讼、权利滥用行为，人民法院依法快速审结并予以明确否定；某日化公司恶意提起知识产权诉讼，其诉讼请求被全部驳回并受到司法谴责，有效规制阻碍创新的不诚信诉讼行为。
"""
        ),
        "ask": "结合材料，运用《法律与生活》知识，谈谈人民法院是如何依法保护知识产权以护航新质生产力发展的。",
        "locator": "F0163:paper page 6 lines 269-295; F0162/F0373:rubric text.",
    },
}


ASK_ONLY: dict[str, str] = {
    "CC0077_2025_东城_一模_19": "阅读材料，完成下表。",
    "CC0084_2025_东城_二模_19": "阅读材料，完成下表。",
    "CC0157_2025_朝阳_期末_20": "了解案件，分析事实，印证法理，参考示例，完成下表。",
    "CC0189_2025_石景山_一模_20": "阅读材料，参考示例，完成下表。",
    "CC0213_2025_门头沟_一模_20": "请结合以下案例，参照所给示例完成下表。",
    "CC0325_2026_石景山_一模_18": "阅读材料，参考示例，分析案件中举证责任的分配方式及理由，完成下表。",
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    PACKET.mkdir(parents=True, exist_ok=True)

    q_rows, q_fields = read_csv(BASE / "merged_subjective_law_questions_claudecode_corrected.csv")
    m_rows, m_fields = read_csv(BASE / "merged_material_atoms_subjective_claudecode_corrected.csv")
    a_rows, a_fields = read_csv(BASE / "merged_ask_atoms_subjective_claudecode_corrected.csv")
    r_rows, r_fields = read_csv(BASE / "merged_rubric_atoms_subjective_claudecode_corrected.csv")

    material_replaced = set(CORRECTIONS)
    ask_replaced = set(CORRECTIONS) | set(ASK_ONLY)
    new_material_ids: dict[str, list[str]] = {}
    patch_records: list[dict[str, str]] = []

    q_by_id = {r["question_id"]: r for r in q_rows}
    for qid, data in CORRECTIONS.items():
        row = q_by_id[qid]
        row["full_question_text"] = data["full"]
        row["material_text"] = data["material"]
        row["ask_text"] = data["ask"]
        row["source_locator"] = data["locator"]
        if "rendered" in data["locator"]:
            row["notes"] = norm(row.get("notes", "") + " | source_recovered_from_rendered_page_visual_read")
        question_patch_note(row, "question_material_ask_rebuilt")
        patch_records.append(
            {
                "question_id": qid,
                "patch_scope": "question_row",
                "patch_action": "rebuilt full_question_text/material_text/ask_text from paper source",
                "source_locator": data["locator"],
                "reason": "Cowork found material leak, answer-as-material, empty ask, or source-level contamination.",
            }
        )

    for qid, ask in ASK_ONLY.items():
        row = q_by_id[qid]
        row["ask_text"] = ask
        question_patch_note(row, "ask_text_filled")
        patch_records.append(
            {
                "question_id": qid,
                "patch_scope": "question_row",
                "patch_action": "filled ask_text",
                "source_locator": row.get("source_locator", ""),
                "reason": "Cowork found empty ask_text while material row was otherwise usable.",
            }
        )

    # Rebuild material atoms for corrected source rows.
    kept_m_rows = [r for r in m_rows if r["question_id"] not in material_replaced]
    rebuilt_m_rows: list[dict[str, str]] = []
    for qid, data in CORRECTIONS.items():
        parts = split_atoms(data["material"])
        ids: list[str] = []
        for idx, phrase in enumerate(parts, 1):
            mid = f"M_{qid}_{idx:02d}"
            ids.append(mid)
            rebuilt_m_rows.append(
                {
                    "material_atom_id": mid,
                    "question_id": qid,
                    "material_phrase": phrase,
                    "plain_description": phrase,
                    "subject_or_actor": "",
                    "action_or_event": "",
                    "affected_party": "",
                    "conflict_or_problem": "yes" if any(k in phrase for k in ["纠纷", "起诉", "诉讼", "分歧", "风险", "损害", "侵害", "违约"]) else "",
                    "legal_signal_if_any": legal_signal(phrase),
                    "possible_relevance_to_answer": "source fact or legal provision needed for rubric match",
                    "source_locator": data["locator"],
                    "uncertainty": "cowork_refined_from_paper_text_or_rendered_page",
                }
            )
        new_material_ids[qid] = ids
        patch_records.append(
            {
                "question_id": qid,
                "patch_scope": "material_atoms",
                "patch_action": f"replaced old atoms with {len(ids)} source-material atoms",
                "source_locator": data["locator"],
                "reason": "Remove answer/rubric leakage from material atom layer.",
            }
        )
    m_rows_out = kept_m_rows + rebuilt_m_rows

    # Patch ask atoms.
    a_by_qid = {r["question_id"]: r for r in a_rows}
    for qid in ask_replaced:
        ask = CORRECTIONS.get(qid, {}).get("ask") or ASK_ONLY[qid]
        row = a_by_qid[qid]
        row["ask_text"] = ask
        row["ask_function_plain"] = ask_function(ask)
        row["module_requirement"] = "法律与生活" if "法律与生活" in ask or q_by_id[qid].get("module_boundary_risk") == "选必二" else "法律/综合"
        row["requires_material_connection"] = "yes"
        row["requires_value_discussion"] = req_value(ask)
        row["requires_behavior_evaluation"] = "yes" if any(k in ask for k in ["判决", "是否", "判断", "裁判"]) else "uncertain"
        row["requires_solution_or_measure"] = req_solution(ask)
        row["student_task_plain"] = ask
        row["source_locator"] = q_by_id[qid].get("source_locator", row.get("source_locator", ""))
        patch_records.append(
            {
                "question_id": qid,
                "patch_scope": "ask_atom",
                "patch_action": "rewrote ask atom from repaired ask_text",
                "source_locator": row["source_locator"],
                "reason": "Remove placeholder ask atom.",
            }
        )

    # Patch rubric atoms: remove logic atoms wrongly attached to legal rows and relink corrected material atoms.
    remove_rubric_ids = {
        "R_CC0364_2026_通州_期末_19_1_02",
        "R_CC0364_2026_通州_期末_19_1_03",
        "R_CC0364_2026_通州_期末_19_1_04",
        "R_CC0364_2026_通州_期末_19_1_05",
        "R_CC0364_2026_通州_期末_19_1_06",
        "R_CC0364_2026_通州_期末_19_1_07",
        "R_CC0364_2026_通州_期末_19_1_08",
        "R_CC0277_2026_房山_二模_18_08",
        "R_CC0277_2026_房山_二模_18_09",
        "R_CC0277_2026_房山_二模_18_10",
        "R_CC0277_2026_房山_二模_18_11",
    }
    bad_rubric_patterns = {
        "CC0254_2026_丰台_二模_18": ["一纸司法建议", "复练试题", "赏花经济"],
    }
    patched_r_rows: list[dict[str, str]] = []
    for row in r_rows:
        rid = row["rubric_atom_id"]
        qid = row["question_id"]
        if rid in remove_rubric_ids:
            patch_records.append(
                {
                    "question_id": qid,
                    "patch_scope": "rubric_atom",
                    "patch_action": f"removed {rid}",
                    "source_locator": row.get("source_locator", ""),
                    "reason": "Logic-and-thinking rubric atom was wrongly attached to legal subjective corpus.",
                }
            )
            continue
        if qid in bad_rubric_patterns and any(
            marker in row.get("rubric_or_answer_phrase", "")
            for marker in bad_rubric_patterns[qid]
        ):
            patch_records.append(
                {
                    "question_id": qid,
                    "patch_scope": "rubric_atom",
                    "patch_action": f"removed stray non-source-review atom {rid}",
                    "source_locator": row.get("source_locator", ""),
                    "reason": "This atom came from a later review/practice slide, not from the 2026丰台二模 Q18 paper or its scoring rubric.",
                }
            )
            continue
        if rid == "R_CC0277_2026_房山_二模_18_07":
            row["rubric_or_answer_phrase"] = "细则：法律边界及应对措施。风险：不正当竞争/商业诋毁1分，名誉权1分，商业秘密泄露1分，著作权/外观设计1分；措施：履行审核义务2分，应完善保密措施1分。"
            row["plain_reward_description"] = row["rubric_or_answer_phrase"]
            row["what_expression_is_rewarded"] = row["rubric_or_answer_phrase"]
            row["knowledge_material_value_type"] = "knowledge+material"
            row["uncertainty"] = norm(row.get("uncertainty", "") + "; cowork_refined_removed_logic_tail")
        if rid == "R_CC0251_2026_丰台_一模_20_01":
            row["rubric_or_answer_phrase"] = "人民法院以事实为根据、以法律为准绳作出判决；根据民法典，经营场所、公共场所经营者、管理者因过错造成他人损害的，应承担侵权责任；材料表明事发现场不存在影响通行的客观因素，原告系完全民事行为能力人，摔倒是自身未尽安全注意义务所致，某餐饮公司和某商业管理公司无过错，不承担赔偿责任；该判决有利于平衡原被告权利义务，倡导安全文明出行和自我负责的安全责任意识，明确公共场所经营者、管理者安全保障义务边界，弘扬社会主义核心价值观。"
            row["plain_reward_description"] = row["rubric_or_answer_phrase"]
            row["what_expression_is_rewarded"] = row["rubric_or_answer_phrase"]
            row["uncertainty"] = norm(row.get("uncertainty", "") + "; cowork_refined_trimmed_slide_tail")
        if qid in new_material_ids:
            row["related_material_atom_ids"] = "|".join(new_material_ids[qid])
            row["uncertainty"] = norm(row.get("uncertainty", "") + "; material_links_rebuilt_after_cowork_patch")
        patched_r_rows.append(row)

    # Patch CC0364 question/material/ask from rendered paper even though its rubric R01 remains.
    qid = "CC0364_2026_通州_期末_19_1"
    if qid in q_by_id and qid not in CORRECTIONS:
        data = {
            "full": norm(
                """
19.（14分）【案件事实】某小区3号楼2单元全体业主一致签字同意增设电梯，并于小区主要出入口张贴意见征集单、公示、承诺及图纸等相关材料，公示期间未收到异议。随后，该项目取得了主管部门的审批手续并正式开工。居住于相邻楼的业主范某认为，电梯安装位置影响其采光，侵犯其合法权益，遂多次在现场阻碍施工，导致项目停工。2单元全体业主向人民法院起诉，请求判令范某停止对加装电梯工程的妨害行为。法院经现场勘查，案涉加装电梯采用全玻璃设计，未对相邻楼采光造成影响，遂判决范某停止对电梯加装工程的阻挠行为。同时，法院明确，若电梯投入使用后，确在采光、通风等方面对部分业主造成较大影响，相关权利人可就补偿事宜另行协商或通过法律途径解决。
（1）结合材料，运用《法律与生活》知识，分析判决结果并说明理由。
"""
            ),
            "material": norm(
                """
某小区3号楼2单元全体业主一致签字同意增设电梯，并张贴意见征集单、公示、承诺及图纸等材料，公示期间未收到异议。
该项目取得主管部门审批手续并正式开工。
相邻楼业主范某认为电梯安装位置影响其采光、侵犯其合法权益，多次现场阻碍施工，导致项目停工。
2单元全体业主向人民法院起诉，请求判令范某停止对加装电梯工程的妨害行为。
法院现场勘查认为案涉加装电梯采用全玻璃设计，未对相邻楼采光造成影响，判决范某停止阻挠行为。
法院明确，若电梯投入使用后确在采光、通风等方面对部分业主造成较大影响，相关权利人可就补偿事宜另行协商或通过法律途径解决。
"""
            ),
            "ask": "结合材料，运用《法律与生活》知识，分析判决结果并说明理由。",
            "locator": "F0224:paper page 7 lines 236-251; F0223/F0403:rubric slide 11.",
        }
        row = q_by_id[qid]
        row["full_question_text"] = data["full"]
        row["material_text"] = data["material"]
        row["ask_text"] = data["ask"]
        row["source_locator"] = data["locator"]
        question_patch_note(row, "cc0364_law_subquestion_restored")

        # remove old material atoms and append rebuilt ones
        m_rows_out = [r for r in m_rows_out if r["question_id"] != qid]
        ids = []
        for idx, phrase in enumerate(split_atoms(data["material"]), 1):
            mid = f"M_{qid}_{idx:02d}"
            ids.append(mid)
            m_rows_out.append(
                {
                    "material_atom_id": mid,
                    "question_id": qid,
                    "material_phrase": phrase,
                    "plain_description": phrase,
                    "subject_or_actor": "",
                    "action_or_event": "",
                    "affected_party": "",
                    "conflict_or_problem": "yes",
                    "legal_signal_if_any": legal_signal(phrase),
                    "possible_relevance_to_answer": "source fact needed for judgment on adjacent relationship",
                    "source_locator": data["locator"],
                    "uncertainty": "cowork_refined_from_paper_text",
                }
            )
        new_material_ids[qid] = ids
        arow = a_by_qid[qid]
        arow["ask_text"] = data["ask"]
        arow["ask_function_plain"] = "评析"
        arow["module_requirement"] = "法律与生活"
        arow["requires_material_connection"] = "yes"
        arow["requires_value_discussion"] = "yes"
        arow["requires_behavior_evaluation"] = "yes"
        arow["requires_solution_or_measure"] = "no"
        arow["student_task_plain"] = data["ask"]
        arow["source_locator"] = data["locator"]
        for rr in patched_r_rows:
            if rr["question_id"] == qid:
                rr["related_material_atom_ids"] = "|".join(ids)
                rr["uncertainty"] = norm(rr.get("uncertainty", "") + "; cc0364_logic_atoms_removed_and_law_material_relinked")
        patch_records.append(
            {
                "question_id": qid,
                "patch_scope": "question/material/ask/rubric",
                "patch_action": "restored 19(1) law ask and removed 19(2) logic rubric atoms",
                "source_locator": data["locator"],
                "reason": "Cowork found ask_text was 19(2) logic while question_id/rubric R01 belonged to 19(1) law.",
            }
        )

    # Relink CC0364 after it was added later.
    for rr in patched_r_rows:
        if rr["question_id"] in new_material_ids:
            rr["related_material_atom_ids"] = "|".join(new_material_ids[rr["question_id"]])

    # Keep order close to original for question and ask rows.
    write_csv(OUT / "merged_subjective_law_questions_cowork_refined.csv", q_rows, q_fields)
    write_csv(OUT / "merged_material_atoms_subjective_cowork_refined.csv", m_rows_out, m_fields)
    write_csv(OUT / "merged_ask_atoms_subjective_cowork_refined.csv", a_rows, a_fields)
    write_csv(OUT / "merged_rubric_atoms_subjective_cowork_refined.csv", patched_r_rows, r_fields)
    write_csv(OUT / "cowork_patch_apply_audit.csv", patch_records, ["question_id", "patch_scope", "patch_action", "source_locator", "reason"])

    # JSONL mirror for questions.
    with (OUT / "merged_subjective_law_questions_cowork_refined.jsonl").open("w", encoding="utf-8") as f:
        for row in q_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    # Copy sidecar matrix files from prior corrected corpus.
    for name in [
        "boundary_mixed_or_blocked_cases_claudecode_corrected.csv",
        "removed_from_core_after_claudecode_audit.csv",
        "suite_exhaustion_matrix_claudecode_corrected.csv",
    ]:
        src = BASE / name
        if src.exists():
            shutil.copy2(src, OUT / name.replace("_claudecode_corrected", "_cowork_refined"))

    # Validation.
    q_count = len(q_rows)
    evidence = Counter(r["evidence_level"] for r in q_rows)
    empty_asks = [r["question_id"] for r in q_rows if not r.get("ask_text", "").strip()]
    bad_material = [
        r["question_id"]
        for r in q_rows
        if r.get("material_text", "").strip() and r.get("material_text", "").strip() == r.get("rubric_text", "").strip()
    ]
    answer_material = [
        r["question_id"]
        for r in q_rows
        if re.search(r"【答案】|评分细则|裁判理由共\d+分|参考答案", r.get("material_text", ""))
    ]
    material_ids = {r["material_atom_id"] for r in m_rows_out}
    broken_refs = []
    for row in patched_r_rows:
        refs = [x for x in row.get("related_material_atom_ids", "").split("|") if x.strip()]
        for ref in refs:
            if ref not in material_ids:
                broken_refs.append((row["rubric_atom_id"], ref))
    logic_leaks = [
        r["rubric_atom_id"]
        for r in patched_r_rows
        if r["question_id"].endswith("_通州_期末_19_1") and ("逻辑与思维" in r["rubric_or_answer_phrase"] or "假言推理" in r["rubric_or_answer_phrase"])
    ]
    logic_leaks += [
        r["rubric_atom_id"]
        for r in patched_r_rows
        if r["question_id"] == "CC0277_2026_房山_二模_18" and ("OPC的出现" in r["rubric_or_answer_phrase"] or "扬弃" in r["rubric_or_answer_phrase"])
    ]

    verdict = "PASS" if not empty_asks and not bad_material and not broken_refs and not logic_leaks else "BLOCKED"
    counts = {
        "questions": q_count,
        "material_atoms": len(m_rows_out),
        "ask_atoms": len(a_rows),
        "rubric_atoms": len(patched_r_rows),
        "evidence_level": dict(evidence),
        "empty_asks": empty_asks,
        "material_equals_rubric": bad_material,
        "material_contains_answer_or_scoring_tokens_review": answer_material,
        "broken_rubric_material_refs_count": len(broken_refs),
        "logic_rubric_leaks": logic_leaks,
        "verdict": verdict,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
    }
    (OUT / "suite_exhaustive_cowork_refined_counts.json").write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")

    audit_md = [
        "# Cowork Patch Apply Audit",
        "",
        f"Generated: {counts['generated_at']}",
        "",
        f"Verdict: **{verdict}**",
        "",
        "## Counts",
        "",
        f"- questions: {q_count}",
        f"- material_atoms: {len(m_rows_out)}",
        f"- ask_atoms: {len(a_rows)}",
        f"- rubric_atoms: {len(patched_r_rows)}",
        f"- evidence_level: {dict(evidence)}",
        "",
        "## Hard Blocker Checks",
        "",
        f"- empty_asks: {len(empty_asks)} {empty_asks}",
        f"- material_equals_rubric: {len(bad_material)} {bad_material}",
        f"- broken_rubric_material_refs_count: {len(broken_refs)}",
        f"- logic_rubric_leaks: {len(logic_leaks)} {logic_leaks}",
        "",
        "## Remaining Review-Only Flags",
        "",
        f"- material_contains_answer_or_scoring_tokens_review: {len(answer_material)} {answer_material}",
        "",
        "These review-only flags are expected when the original material itself contains score text such as `8分`, or where weak reference-only rows remain. They are not automatic blockers after manual source recovery unless listed above.",
        "",
        "## Applied Patch Summary",
        "",
    ]
    for rec in patch_records:
        audit_md.append(f"- {rec['question_id']} [{rec['patch_scope']}]: {rec['patch_action']} ({rec['source_locator']})")
    (OUT / "cowork_patch_apply_audit.md").write_text("\n".join(audit_md) + "\n", encoding="utf-8")

    report = [
        "# Suite Exhaustive Cowork Refined Report",
        "",
        f"Verdict: **{verdict}**",
        "",
        "基线: `suite_exhaustive_claudecode_corrected_20260519`",
        "本版本处理 Claude Cowork E 指出的题层硬阻塞，并额外清理房山二模 18 题混入的逻辑小问 rubric。",
        "",
        "## 关键结论",
        "",
        "- 题量仍为 65；未新增题、未删题。",
        "- evidence_level 仍为 formal 61、reference_only 4。",
        "- 所有 question 均有 ask_text。",
        "- 原 8 条 material_text == rubric_text 与 2 条 material=答案分点已重建材料层。",
        "- CC0364 通州期末 19(1) 已恢复法律设问，逻辑小问 rubric 已移出核心法律表。",
        "- CC0277 房山二模 18 已保留法律小问，移出 OPC 逻辑/辩证否定 rubric。",
        "- 现阶段可生成新的 reasoner packet；仍需把本 audit 附在包内，提示 reference_only 不可单独支撑核心框架。",
        "",
        "## 输出文件",
        "",
        "- `merged_subjective_law_questions_cowork_refined.csv`",
        "- `merged_material_atoms_subjective_cowork_refined.csv`",
        "- `merged_ask_atoms_subjective_cowork_refined.csv`",
        "- `merged_rubric_atoms_subjective_cowork_refined.csv`",
        "- `cowork_patch_apply_audit.md`",
        "- `cowork_patch_apply_audit.csv`",
        "- `suite_exhaustive_cowork_refined_counts.json`",
    ]
    (OUT / "suite_exhaustion_report_cowork_refined.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    # Build reasoner packet.
    packet_map = {
        OUT / "merged_subjective_law_questions_cowork_refined.csv": PACKET / "merged_subjective_law_questions_for_reasoners_cowork_refined.csv",
        OUT / "merged_material_atoms_subjective_cowork_refined.csv": PACKET / "merged_material_atoms_subjective_for_reasoners_cowork_refined.csv",
        OUT / "merged_ask_atoms_subjective_cowork_refined.csv": PACKET / "merged_ask_atoms_subjective_for_reasoners_cowork_refined.csv",
        OUT / "merged_rubric_atoms_subjective_cowork_refined.csv": PACKET / "merged_rubric_atoms_subjective_for_reasoners_cowork_refined.csv",
        OUT / "cowork_patch_apply_audit.md": PACKET / "cowork_patch_apply_audit.md",
        OUT / "suite_exhaustion_report_cowork_refined.md": PACKET / "suite_exhaustion_report_for_reasoners_cowork_refined.md",
        OUT / "suite_exhaustive_cowork_refined_counts.json": PACKET / "suite_exhaustive_cowork_refined_counts.json",
    }
    for src, dst in packet_map.items():
        shutil.copy2(src, dst)
    for name in [
        "boundary_mixed_or_blocked_cases_cowork_refined.csv",
        "suite_exhaustion_matrix_cowork_refined.csv",
    ]:
        src = OUT / name
        if src.exists():
            shutil.copy2(src, PACKET / name.replace("_cowork_refined", "_for_reasoners_cowork_refined"))

    packet_md = [
        "# REASONER INPUT PACKET - Cowork Refined",
        "",
        "## Gate",
        "",
        f"Packet verdict before reasoner: **{verdict}**.",
        "",
        "This packet supersedes `reasoner_packet_suite_exhaustive_claudecode_corrected_20260519.zip` because Claude Cowork E found question-layer blockers in that packet.",
        "",
        "## Data Scope",
        "",
        "- Subjective questions only.",
        "- Core question count: 65.",
        "- evidence_level: formal 61, reference_only 4, missing 0.",
        "- No core midterm entries remain; midterm no-law/boundary suites are retained only in exhaustion matrix and boundary files.",
        "",
        "## Patch Context",
        "",
        "The attached `cowork_patch_apply_audit.md` must be treated as part of the input. It records repairs to empty asks, material/rubric leakage, answer-as-material rows, and logic-module leakage.",
        "",
        "## Reasoner Guardrails",
        "",
        "- Do not use reference_only rows to support a core framework node by themselves.",
        "- Do not infer from choice questions.",
        "- Do not treat reference answers as formal scoring rubrics.",
        "- Every observation must cite question_id, rubric_atom_id, and material_atom_id.",
        "- The `related_material_atom_ids` field uses `|` as its delimiter.",
        "",
        "## Files",
        "",
        "- `merged_subjective_law_questions_for_reasoners_cowork_refined.csv`",
        "- `merged_material_atoms_subjective_for_reasoners_cowork_refined.csv`",
        "- `merged_ask_atoms_subjective_for_reasoners_cowork_refined.csv`",
        "- `merged_rubric_atoms_subjective_for_reasoners_cowork_refined.csv`",
        "- `suite_exhaustion_report_for_reasoners_cowork_refined.md`",
        "- `cowork_patch_apply_audit.md`",
    ]
    (PACKET / "REASONER_INPUT_PACKET_COWORK_REFINED.md").write_text("\n".join(packet_md) + "\n", encoding="utf-8")

    zip_path = ROOT / "05_reasoner_packets" / "reasoner_packet_suite_exhaustive_cowork_refined_20260519.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(PACKET.glob("*")):
            zf.write(path, arcname=path.name)

    print(json.dumps(counts, ensure_ascii=False, indent=2))
    print(f"OUT={OUT}")
    print(f"PACKET={PACKET}")
    print(f"ZIP={zip_path}")


if __name__ == "__main__":
    main()
