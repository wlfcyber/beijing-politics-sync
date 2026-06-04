#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parents[1]
PACKETS = RUN_DIR / "03_source_packets" / "source_packets_final.jsonl"
AUDIT_JSON = RUN_DIR / "05_output" / "A_THEME_SOURCE_REPAIR_AUDIT_20260604.json"
OUT_JSON = RUN_DIR / "05_output" / "A_THEME_SOURCE_REPAIR_OVERRIDES_20260604.json"
OUT_MD = RUN_DIR / "05_output" / "A_THEME_SOURCE_REPAIR_OVERRIDES_20260604.md"

sys.path.insert(0, str((RUN_DIR / "tools").resolve()))
import audit_a_theme_source_repairs as audit  # noqa: E402


def clean(text: str) -> str:
    return audit.clean(text)


def load_packets() -> dict[str, dict]:
    rows = [json.loads(line) for line in PACKETS.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {row["entry_id"]: row for row in rows}


def source_paths_by_entry() -> dict[str, dict]:
    if not AUDIT_JSON.exists():
        raise FileNotFoundError(AUDIT_JSON)
    rows = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
    return {row["entry_id"]: row for row in rows}


def extract_doc_rubric(entry_id: str, packets: dict[str, dict]) -> str:
    files = audit.file_index()
    entry = packets[entry_id]
    path = audit.resolve_path(entry["rubric_path"], files, entry_id, "rubric")
    text = audit.extract_text(path)
    if entry_id == "E036":
        start = text.find("20（1）")
        end = text.find("21（1）", start)
        if start < 0:
            raise RuntimeError("E036 rubric start not found")
        return clean(text[start:end if end > start else len(text)])
    raise KeyError(entry_id)


def extract_docx_rubric(entry_id: str, packets: dict[str, dict]) -> str:
    files = audit.file_index()
    entry = packets[entry_id]
    path = audit.resolve_path(entry["rubric_path"], files, entry_id, "rubric")
    text = audit.extract_text(path)
    if entry_id == "E006":
        start = text.find("19（8分）")
        end = text.find("20.", start)
        if start < 0:
            raise RuntimeError("E006 rubric start not found")
        return clean(text[start:end if end > start else len(text)])
    raise KeyError(entry_id)


def build_overrides(packets: dict[str, dict], audit_rows: dict[str, dict]) -> dict[str, dict]:
    e022_e023_material = clean(
        """案件情况 | 处理结果 | 裁判理由
李某是一名AI绘图软件爱好者，他使用人工智能软件制作了一张图片，并加上“AI 绘画”等标签，发布在自己的社交平台上。网友刘某看到图片后，感觉非常契合自己的文章，便直接拿来作为配图使用，还抹去了平台署名水印。李某认为刘某的行为侵犯了自己的著作权。遂将刘某诉至北京互联网法院。 | 法院支持李某诉讼请求。 | （1）
小王向银行申请开通信用卡，且宣称已阅览申请材料，明晰信用卡相关信息，愿意遵循领用合约及申请表中所列的所有条款。后来小王使用该卡透支消费，却未依照合同约定履行还款义务。银行屡次向小王催告，然而小王迄今仍未还款。为维护自身的合法权益，银行将其诉至法院，恳请依法判决小王偿还信用卡欠款2万元及利息。 | 法院判决小王偿还信用卡欠款本金2万元，并按合同约定支付利息。 | （2）"""
    )

    e024_material = clean(
        """人民法院审理案件，必须坚持以事实为根据、以法律为准绳，做到公正司法。了解案件，分析事实，印证法理。
案件事实 | 拟写裁判要点
示例：案件一 甲公司在2016年与乙公司终止合作后，继续在甲公司运营的相关地图软件、应用和第三方服务中使用乙公司数据。乙公司以甲公司侵犯署名权、修改权、复制权、信息网络传播权等理由向人民法院提起诉讼。 | 裁判理由：根据著作权法，甲公司在应用软件中使用被诉侵权电子地图，侵害了乙公司对涉案导航电子地图的署名权、修改权、复制权、信息网络传播权。裁判结果：被告停止侵害、赔礼道歉、消除影响并赔偿损失。
案件二 丙公司依托电子地图收集的电子地图数据、用户出行数据和实时交通信息等原始数据，通过特定算法并经分析处理形成数据产品“拥堵延时指数”。被告丁公司采用变换IP地址和伪造浏览器标识等不正当手段抓取“拥堵延时指数”数据，并在其经营的某金融终端付费软件上以商业化为目的使用了上述数据。丙公司就此诉至人民法院。 | 裁判理由：① 裁判结果：②
案件三 甲向乙旅游公司购买门票，并于当日参加“摇摆桥”项目。在该项目进行过程中，乙旅游公司工作人员过度摇晃桥面，甲从摆桥上摔落、受伤。经医院诊断，甲左肱骨髁上髁间粉碎性骨折，共住院13天。经鉴定，甲的损伤及目前后遗症评定为九级伤残。甲向人民法院起诉，请求判令乙旅游公司赔偿医疗费等经济损失。 | 裁判理由：③ 裁判结果：④"""
    )

    e074_material = clean(
        """某校学习小组围绕“财产制度助力经济社会发展”的议题开展探究，搜集整理的资料如下。
我国财产制度改革重要节点：
2002年：党的十六大报告提出完善保护私人财产的法律制度。
2004年：宪法修正案在宪法第十三条增加规定：“公民的合法私有财产不受侵犯。”
2007年：十届全国人大五次会议通过物权法，它是我国规范财产关系的民事基本法律。
2016年：《中共中央、国务院关于完善产权保护制度依法保护产权的意见》发布，这是我国首次以中央名义出台关于产权保护的顶层设计文件。这一文件指出：“改革开放以来，通过大力推进产权制度改革，我国基本形成了归属清晰、权责明确、保护严格、流转顺畅的现代产权制度和产权保护法律框架，全社会产权保护意识不断增强，保护力度不断加大。”
2020年：十三届全国人大三次会议通过民法典，进一步完善物权法律制度和其他财产制度。
2022年：党的二十大报告指出：“加强知识产权法治保障，形成支持全面创新的基础制度。”"""
    )

    e005_material = clean(
        """人力资源社会保障部和最高人民法院联合发布了一批涉及平台经济的劳动人事争议典型案例，供各地仲裁机构、人民法院在办案中予以参照。
【资料包】中华人民共和国劳动和社会保障部发布的《关于确立劳动关系有关事项的通知》指出：劳动关系的核心特征为劳动者与用人单位之间具有人格、经济、组织的从属性。认定新就业形态劳动者与平台企业之间是否存在劳动关系，应做如下考量：
人格从属性：体现为平台企业的劳动纪律、奖惩办法等是否适用于劳动者；劳动者是否须按照平台指令完成工作任务等。
经济从属性：体现为平台企业是否掌握劳动者从业所必需的数据信息等重要生产资料，是否允许劳动者商定服务价格等。
组织从属性：体现在劳动者是否被纳入平台企业的组织体系当中，并以平台名义对外提供服务等。
【基本案情】王某于2022年6月14日与甲公司订立为期1年的《车辆管理协议》约定：王某与甲公司建立合作关系，王某自备面包车1辆，通过公司平台接受派单提供货物运输服务。甲公司与客户结算运输费，每月向王某支付包月服务费6000元及奖励金。王某每日在公司平台签到并接受派单，跑单时长均在8小时以上；甲公司通过平台对王某的订单完成情况进行全程跟踪；王某每日接单量超过4单时享有加单奖励，出现接单量不足、无故拒单、货物损毁等情形时按照公司制度扣减部分服务费。2023年3月2日，甲公司因调整运营规划，提出提前终止与王某的合作关系。王某认为其与甲公司之间实际上已构成劳动关系，甲公司应当支付解除劳动合同经济补偿，甲公司以双方是合作关系为由拒绝，王某遂向仲裁委员会申请仲裁。
【处理结果】仲裁委员会裁决：甲公司向王某支付解除劳动合同经济补偿。"""
    )

    e035_material = clean(
        """17岁的小刘背着家长、绕过平台监管打赏多名网络主播，金额高达45万余元。
家长：我们发现之后，先跟主播沟通，有几位主播退了一部分钱，总计5万余元。后与平台客服沟通，想要回其余40万余元的打赏款，遭到拒绝。所以，我们现在将平台告上人民法院，要求返还充值款项。
平台：注意到小刘账号的异常消费后，采取了消费限制措施，停止了该账户的充值和打赏权限。但随后，小刘冒充监护人的身份与平台客服电话沟通，平台才解除了涉案账号的全部限制措施，平台不应承担责任。
人民法院一审判定，由被告平台退还未成年人充值款24万元。平台不服提出上诉，二审法院维持了一审判决。
【资料卡】《中华人民共和国民法典》第一百五十七条规定：民事法律行为无效、被撤销或者确定不发生效力后，行为人因该行为取得的财产应当予以返还；不能返还或者没有必要返还的应当折价补偿。有过错的一方应当赔偿对方由此所受到的损失；各方都有过错的，应当各自承担相应的责任。"""
    )

    e015_prompt = clean(
        """阅读材料，完成下表。
案件 | 解决机制 | 以案说法 | 典型意义
案件一 | ① | 某公司未能按时完工，应承担违约责任。该案争议点不大，诉讼标的额较小，承办法官本着以和为贵的理念，经征求双方同意后，以该方式圆满解决纠纷。 | 有效化解矛盾，避免双方损失进一步扩大，有利于规范市场秩序，促进社会和谐。
案件二 | 仲裁 | 医院与柳某签订的合同与协议被依法认定有效，柳某签订协议并支付违约金是真实意思表示，其要求返还违约金有违诚信原则，故驳回。 | ②
案件三 | 诉讼 | 顾氏三兄弟无法定赡养义务，但对杨某进行生活照顾、精神慰藉等构成事实上的扶养，符合民法典规定的“可以分给适当遗产”情形，有权作为利害关系人申请人民法院指定遗产管理人。 | ③"""
    )

    e016_prompt = clean(
        """阅读材料，完成下表。
案件 | 体现的民法原则 | 以案说法 | 典型意义
案件一 | 守法和公序良俗原则 | ① | 对规范商家经营，保障未成年人合法权益、呵护未成年人健康成长具有重要意义。
案件二 | 诚信原则 | ② | 引导自媒体经营者树立法治意识，规范其行为，有利于提升媒体公信力，同时有利于维护良性市场竞争秩序。
案件三 | ③ | 本案所涉“服务条款”属于格式条款，公司负有向用户提示、说明的义务，只在内容复杂繁多的服务条款中约定，不足以起到提示作用，故认定公司违约。 | ④"""
    )

    overrides = {
        "E005": {
            "material": e005_material,
            "prompt": "结合材料，说明仲裁委员会作出上述裁决的理由，并分析该典型案例的意义。（9分）",
            "repair_source": audit_rows["E005"]["question_path"],
            "repair_note": "从2024朝阳二模原卷第17题回源重排，修复双栏OCR将资料包和案情交叉的问题。",
        },
        "E006": {
            "prompt": "运用《法律与生活》知识，谈谈对本案判决的认识。",
            "rubric": extract_docx_rubric("E006", packets),
            "repair_source": audit_rows["E006"]["rubric_path"],
            "repair_note": "从2024海淀一模细则DOCX补齐第19题评分细则，并删除设问中的页脚残留。",
        },
        "E015": {
            "prompt": e015_prompt,
            "repair_source": audit_rows["E015"]["question_path"],
            "repair_note": "从2025东城一模原卷第19题重排设问表格，修复文本层行列错位。",
        },
        "E016": {
            "prompt": e016_prompt,
            "repair_source": audit_rows["E016"]["question_path"],
            "repair_note": "从2025东城二模原卷第19题重排设问表格，修复文本层行列错位。",
        },
        "E022": {
            "material": e022_e023_material,
            "prompt": "（1）阅读材料，运用《法律与生活》知识，完成裁判理由。（6分）",
            "repair_source": audit_rows["E022"]["question_path"],
            "repair_note": "从2025昌平二模原卷第20题表格回源重排，修复当前文本层只保留半行材料的问题。",
        },
        "E023": {
            "material": e022_e023_material,
            "prompt": "（2）阅读材料，运用《法律与生活》知识，完成裁判理由。（6分）",
            "repair_source": audit_rows["E023"]["question_path"],
            "repair_note": "从2025昌平二模原卷第20题表格回源重排，修复当前材料/设问串行问题。",
        },
        "E024": {
            "material": e024_material,
            "prompt": "参考示例，完成下表。",
            "repair_source": audit_rows["E024"]["question_path"],
            "repair_note": "从2025朝阳期末原卷第20题回源重排，将裁判要点表从设问字段移回材料字段。",
        },
        "E036": {
            "rubric": extract_doc_rubric("E036", packets),
            "repair_source": audit_rows["E036"]["rubric_path"],
            "repair_note": "用Word COM从2025门头沟一模.doc细则回源抽取第20题完整评分细则，替换当前仅一行的细则。",
        },
        "E035": {
            "material": e035_material,
            "repair_source": audit_rows["E035"]["question_path"],
            "repair_note": "从2025西城二模原卷第18题回源重排，修复案情和民法典资料卡在文本层交叉的问题。",
        },
        "E074": {
            "material": e074_material,
            "prompt": "结合材料，运用所学知识，说明我国财产制度改革如何助力经济社会发展。",
            "repair_source": str(RUN_DIR / "05_output" / "shunyi_2024_docx_media_20260604" / "image6.png"),
            "repair_note": "顺义思政二模原卷DOCX文本层缺失第17题资料图；已根据原卷嵌入图image6.png人工校对转写财产制度时间轴。",
        },
    }
    return overrides


def write_report(overrides: dict[str, dict], packets: dict[str, dict]) -> None:
    lines = ["# A类回源修复覆盖层", ""]
    for eid, item in overrides.items():
        lines.extend([
            f"## {eid} {packets[eid]['title']}",
            "",
            f"- repair_source: `{item.get('repair_source', '')}`",
            f"- repair_note: {item.get('repair_note', '')}",
            f"- fields: {', '.join(k for k in item if k in {'material', 'prompt', 'rubric'})}",
            "",
        ])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    packets = load_packets()
    audit_rows = source_paths_by_entry()
    overrides = build_overrides(packets, audit_rows)
    OUT_JSON.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(overrides, packets)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
