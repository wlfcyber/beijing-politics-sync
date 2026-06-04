#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
PACKETS = RUN_DIR / "03_source_packets" / "source_packets_final.jsonl"
COVERAGE = RUN_DIR / "00_control" / "COVERAGE_MATRIX.csv"
SOURCE_LEDGER = RUN_DIR / "00_control" / "SOURCE_LEDGER.csv"
AUDIT = RUN_DIR / "05_output" / "NON_MID_ZERO_PATCH_AUDIT_20260604.md"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalize_text(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text


def source_id_by_prefix(ledger: dict[str, dict], prefix: str) -> str:
    matches = [source_id for source_id in ledger if source_id.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"source prefix {prefix!r} matched {matches!r}")
    return matches[0]


def make_entry(
    *,
    title: str,
    year: str,
    district: str,
    paper_type: str,
    question_no: str,
    question_prefix: str,
    rubric_prefix: str,
    evidence_type: str,
    pending_reason: str,
    material: str,
    prompt: str,
    rubric: str,
    ledger: dict[str, dict],
) -> dict:
    qid = source_id_by_prefix(ledger, question_prefix)
    rid = source_id_by_prefix(ledger, rubric_prefix)
    return {
        "entry_id": "",
        "candidate_index": 0,
        "title": title,
        "year": year,
        "district_or_exam": district,
        "paper_type": paper_type,
        "question_no": question_no,
        "question_source_id": qid,
        "question_path": ledger[qid]["path"],
        "rubric_source_id": rid,
        "rubric_path": ledger[rid]["path"],
        "evidence_type": evidence_type,
        "pending_reason": pending_reason,
        "material": normalize_text(material),
        "prompt": normalize_text(prompt),
        "rubric": normalize_text(rubric),
    }


def new_entries(ledger: dict[str, dict]) -> list[dict]:
    return [
        make_entry(
            title="2024 · 朝阳 · 一模 · 第19题",
            year="2024",
            district="朝阳",
            paper_type="一模",
            question_no="19",
            question_prefix="SRC_d3b447f0ea",
            rubric_prefix="SRC_8a924a2453",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
诚信是法治精神的重要伦理基础。民法典第七条规定：“民事主体从事民事活动，应当遵循诚信原则，秉持诚实，恪守承诺。”

镜头一：2022年12月，A公司与B公司签订购销合同约定：A公司向B公司提供产品，货款于发货后的60日内付清。2023年1月，A公司依约向B公司提供货物，但截至2023年7月，B公司欠A公司货款590万元未支付。2023年8月，A公司起诉B公司，要求其支付货款及违约金。人民法院最终判决B公司尽快付清全部欠款并支付逾期违约金。

镜头二：某购物中心为200余家商户建立了“码上诚信”二维码，消费者扫描二维码，即可查询此商户相关的行政许可、行政处罚、主动承诺、自愿注册等信用信息。有市民说：“我经常来这个商场消费，一是因为‘码上诚信’让我感觉在这里购物很放心，二是因为这里的商品质量和售后服务态度都很好。”
""",
            prompt="结合材料，运用《法律与生活》知识，分析诚信原则对促进社会主义市场经济健康发展的积极作用。",
            rubric="""
19.（7分）
社会主义市场经济本质上是法治经济。民法典将诚信原则确立为基本原则之一，凸显了社会主义核心价值观对社会主义市场经济建设的引导和规范。
诚信原则要求合同当事人按照约定全面履行义务，有利于规范民事主体行为，尊重和维护民事主体合法权利；司法机关可根据诚信原则定分止争，维护公平正义，维护诚信、健康的市场秩序。
诚信原则要求经营者依法、诚信经营，保护消费者的合法权益。这不仅有利于平衡经营者与消费者之间的关系，而且有助于守法诚信的经营者扩大市场，并最终增进社会整体福祉。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2025 · 西城 · 一模 · 第20题",
            year="2025",
            district="西城",
            paper_type="一模",
            question_no="20",
            question_prefix="SRC_062e7a5c77",
            rubric_prefix="SRC_6ea5462e02",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
全国总工会、人力资源社会保障部、中国企业联合会、全国工商联联合启动2025年度集体协商“集中要约行动”，指导工会与企业开展集体协商、签订集体合同。按照行动部署，各级工会把工资调整幅度、加班工资基数、劳动定额标准、工资支付办法等作为协商的核心议题。
""",
            prompt="结合材料，综合运用经济和法律的知识，说明上述做法能促进社会公平与经济效率的平衡。",
            rubric="""
20．（8分）劳动法的首要原则是保护劳动者权益，工会搭建协商平台，劳动者以集体力量与用人单位签订集体合同，可以确保双方协商一致，更加公平、平等自愿。更好地保护劳动者合法权益，促进广大劳动者特别是低薪劳动者群体实现体面劳动，实现社会公平。促进企业依法规范用工，构建和谐劳动关系，激发劳动者积极性，推动生产效率的提高，培育良好商誉，实现社会公平与经济效率的平衡。
【细则】
公平角度：4分
发挥工会的作用/集体的力量1分；可以确保双方协商一致、平等自愿，公平签订劳动合同（或结合订立劳动合同基本原则说明）1分；更好地保护劳动者合法权益（或获得劳动报酬的权利）1分；促进体面劳动（尊重劳动/保护苦脏险累且工资水平不高的劳动者等/分配公平）1分。
效率角度：4分
促进企业依法规范用工（合理用工）1分；激发劳动者积极性/保障收入1分；建立和谐劳动关系1分；推动生产效率的提高/培育良好商誉/企业信誉形象1分。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 丰台 · 二模 · 第18题",
            year="2026",
            district="丰台",
            paper_type="二模",
            question_no="18",
            question_prefix="SRC_14707229fb",
            rubric_prefix="SRC_b1957e7e09",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
法安天下，德润人心。

【基本案情】张某承包果园多年，果园渐成规模。自2025年春季起，李某饲养的牛群多次闯入其果园，不仅撞断树枝、损坏树体，更将正值花期的果树花苞啃食殆尽，导致大幅减产。张某虽在果园周围悬挂“果园重地，禁止放牧”的警示横幅，但2026年3月，李某家的19头牛再次闯入果园，造成果树严重受损。张某报警后，经民警现场协调，李某仅同意赔偿1000元，与张某主张的35000元实际损失差距较大，张某遂向法院提起诉讼。

《中华人民共和国民法典》第一千二百四十五条：饲养的动物造成他人损害的，动物饲养人或者管理人应当承担侵权责任；但是，能够证明损害是因被侵权人故意或者重大过失造成的，可以不承担或者减轻责任。

【调解过程及结果】案件受理后，承办法官考虑到果园既关乎当事人的财产权益，也与区域生态环境质量密切相关，予盾化解应与生态修复同步推进。因此，法官并未急于启动庭审程序，而是第一时间赴果园开展现场勘验，全面了解案件背景。在此基础上，法官多次组织双方开展调解工作。一方面，向李某释明《中华人民共和国民法典》关于饲养动物损害责任的有关规定，指出其依法应承担的赔偿责任；另一方面，结合《中华人民共和国生态环境法典》“系统治理、生态优先、绿色发展”的核心原则及“损害担责”的立法理念，引导双方充分认识果园保护的生态价值。

针对李某一次性赔偿确有困难、张某更关注果园后续保护的实际状况，法官提出了“分期赔偿+行为约束+生态修复”的调解方案，由李某分期支付赔偿款，采取围栏加固、专人看管等有效措施，同时协助张某对被损坏的果树进行补种、养护，修复果园生态。经过承办法官的耐心调解，双方当事人最终达成调解协议，李某当庭向张某支付赔偿款2600元并致歉，两家人握手言和。
""",
            prompt="司法给予我们的不仅仅是定分止争，也是一份融通情理的温暖力量。结合材料，综合运用法治知识，阐明你对这一观点的认识。",
            rubric="""
18.（8分）
该案的成功调解坚持了法治与德治相结合的原则。（1分）该案以法理定分止争，依据《民法典》，确定李某应承担无过错侵权责任，依法维护张某的合法权益。（3分）
同时，引入《生态环境法典》的核心原则和立法理念，将矛盾化解与生态修复同步推进，彰显法律的刚性；充分考虑双方当事人的实际情况，以“分期赔偿+生态修复”的方案促成当事人互谅互让，传递司法的温暖力量，有利于弘扬社会主义核心价值观。（3+1分）
细则：法治与德治相结合1分；依据《民法典》定分止争、饲养动物侵权适用无过错责任、依法维护合法财产权益、结合生态环境法典推进生态修复共4分；结合双方实际提出柔性调解方案、促成互谅互让、弘扬社会主义核心价值观共3分。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 丰台 · 期末 · 第18题",
            year="2026",
            district="丰台",
            paper_type="期末",
            question_no="18",
            question_prefix="SRC_371641aaa3",
            rubric_prefix="SRC_45c50fff44",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
《中华人民共和国未成年人保护法》第四十四条：爱国主义教育基地、图书馆、青少年宫、儿童活动中心、儿童之家应当对未成年人免费开放。博物馆、纪念馆、科技馆、展览馆、美术馆、文化馆、社区公益性互联网上网服务场所以及影剧院、体育场馆、动物园、植物园、公园等场所，应当按照有关规定对未成年人免费或者优惠开放。

某区人民检察院调查发现，有部分影院在网络票务平台和现场购票场所均未对未成年人免票或优惠购票政策作出明确提示，部分影院现场购票场所处将优惠观影的未成年人群体限定于身高1.3米或1.2米以下的未成年人，缩小了应享受观影优惠的未成年人范围，违反了《中华人民共和国未成年人保护法》第四十四条的规定。

该区人民检察院在全面梳理相关法律及规范性文件的基础上，依法对该区文化和旅游局以行政公益诉讼立案并制发检察建议。要求主管部门监督影院依法对未成年人免费或者优惠开放，对未成年人观影优惠政策在网络票务平台和现场购票场所作出明确提示。

收到检察建议后，该区文化和旅游局通过沟通督促、加强监管和宣传教育等方式整改落实，确保未成年人优惠观影政策落实。
""",
            prompt="结合材料，运用法治知识，阐述该检察公益诉讼案例的积极意义。",
            rubric="""
知识板块：政治与法治、法律与生活。能力板块：解释与论证。
检察权（法律监督）+公共利益2分：该案为各地检察机关办理类似案件提供了有效示范，推动检察机关依法行使检察权，有效维护社会公共利益。
政府积极履职+维护市场秩序2分：通过检察建议督促政府有关部门履行法定职责，切实维护良好市场秩序/文化市场健康发展。
市场主体（部分影院的法定义务+未成年人的合法权益）2分：纠正部分影院的侵权违法行为，引导电影院等市场主体自觉履行法律规定的义务，保障未成年人的合法权益。
全社会（法治意识、法治环境+弘扬社会主义核心价值观）2分：增强全社会成员的法治意识，营造全社会保护未成年人健康成长的法治环境。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 房山 · 二模 · 第17题",
            year="2026",
            district="房山",
            paper_type="二模",
            question_no="17",
            question_prefix="SRC_bfb8f196e7",
            rubric_prefix="SRC_ebbcd030de",
            evidence_type="rubric_or_marking",
            pending_reason="涉外法治综合题，法律与生活可支撑涉外民商事纠纷和权利保护部分，收入开放容器。",
            material="""
外国巨轮更名为“尊重”（RESPECT），只为向中国法治致敬。在“尼莉莎”轮扣押案中，希腊申请人主动向青岛海事法院申请扣船，法院创造性地对船舶实施“活扣押”，允许完成剩余航程，促成当事人达成和解，为利害关系人挽回巨额损失，为此希腊籍船东特意将船舶更名。这是中国法治赢得世界尊重的生动注脚。

“保障”：在法律制度层面，出台外商投资法及其实施条例，加强对内外资企业的保护；在司法实践层面，注重保护中外当事人合法权益……

“速度”：上海持续优化“调解、仲裁、诉讼”相衔接国际商事一站式线上解纷平台，当事人可全天候网上立案、在线调解、远程参加庭审、在线接收材料。

“经验”：在一起损失金额存在较大争议的船舶碰撞纠纷中，某海事法院引入外国船东保赔协会参与调解，探索人民法院引导、船舶航运相关组织共同参与的涉外海事纠纷化解模式。
""",
            prompt="中国走向世界，以负责任大国参与国际事务，必须善于运用法治。结合材料，运用法治知识，谈谈中国是如何加强涉外法治建设的。",
            rubric="""
17.（8分）
完善涉外法律法规体系，出台外商投资法及其实施条例，平等保护内外资企业合法权益；创新涉外司法实践，公正司法，创造性适用“活扣押”等措施，提升司法公信力；打造“调解、仲裁、诉讼”衔接的一站式线上多元纠纷解决平台，高效率实现公平正义；以和为贵，创新诉讼调解，构建多元主体参与的涉外海事纠纷化解模式。中国以法治方式践行大国责任和担当，推动涉外法治建设。
细则：完善涉外法律法规体系/加强涉外立法2分；创新司法实践/公正司法/完善涉外法治实施体系2分；多元纠纷解决平台/高效率2分；创新诉讼调解/构建多元主体参与的涉外海事纠纷化解模式2分；可加1分但总分不超8分：中国以法治方式和法治思维践行大国责任和担当，推动涉外法治建设。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 房山 · 二模 · 第18题第1问",
            year="2026",
            district="房山",
            paper_type="二模",
            question_no="18(1)",
            question_prefix="SRC_bfb8f196e7",
            rubric_prefix="SRC_ebbcd030de",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
当OPC（One Person Company）遇上“数字员工”，未来的创业模式，只需要一个充满创意的“头脑”，加上一个不知疲倦的“数字员工”，你就能开启自己的“商业版图”。

材料一：OPC与“数字员工”正以前所未有的速度，重塑着我们的商业生态。但在拥抱这份“未来”的同时，你是否清楚，法律的边界在哪里？

风险1 一本正经地胡说八道：你的“数字员工”撰写了一篇行业文章，其中生成了某家公司的虚假负面数据。文章发布后，该公司向你发来律师函。

风险2 “泄露”危机：为了图方便，你将公司的核心代码、独家运营策略上传到公共AI平台优化。不久后，竞争对手也拥有了类似的方案。

风险3 生成的可能只是“旧作”：你让“数字员工”设计了一款国潮风的手机壳图案，既有传统纹样又有现代元素，直接生产销售。不久，就收到法院传票。
""",
            prompt="结合材料一，运用《法律与生活》知识，分析上述场景可能涉及的法律边界，并提出应对措施。（7分）",
            rubric="""
18.（1）（7分）法律边界及应对措施。
风险1：数字员工生成虚假负面数据文章，违反《反不正当竞争法》的商业诋毁规定，同时可能侵犯该公司的名誉权。应履行审核义务，依法经营。
风险2：将公司的核心代码等上传公共AI平台，可能造成商业秘密泄露。应完善保密措施，与平台签订保密合同。
风险3：数字员工设计的图案直接用作商业用途，可能会侵犯他人的著作权。应履行审核义务。
细则：风险4分，不正当竞争/商业诋毁1分，名誉权1分，商业秘密泄露1分，著作权/外观设计1分；措施2+1分，履行审核义务2分，应完善保密措施1分。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 海淀 · 期末 · 第18题第1问",
            year="2026",
            district="海淀",
            paper_type="期末",
            question_no="18(1)",
            question_prefix="SRC_51b7508a04",
            rubric_prefix="SRC_93d2077755",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
住房问题事关民生福祉。

材料一：近年来，住房租赁市场规模持续扩大，随之而来的合同纠纷不断增加，此类纠纷所涉合同大多是由住房租赁企业提供的合同范本。

小海准备与住房租赁企业签订为期两年的租赁合同，其中有如下条款：“合同期满后，不得在住房租赁企业不知情的情况下与房屋产权人私下建立租赁关系，否则视为违约，乙方需赔偿甲方贰个月租金作为违约金。”小海对此表示不同意见，希望更改。但对方表示，合同是由企业为重复使用而预先拟定的，这一条款不能更改。小海认为该条款无效。
""",
            prompt="运用《法律与生活》知识，判断这一条款是否有效，并说明理由。（6分）",
            rubric="""
18.（1）该合同条款无效。该合同条款是住房租赁企业为了重复使用而预先拟定，并在订立合同时未与对方协商的条款，属于格式条款。民法典规定，采用格式条款订立合同的，提供格式条款的一方应当遵循公平原则确定当事人之间的权利和义务。该合同条款约定合同期满后，承租方不得与产权人私下建立合同关系，限制了承租方自由订立合同的权利，应被认定为无效。（6分）
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 海淀 · 期末 · 第18题第2问",
            year="2026",
            district="海淀",
            paper_type="期末",
            question_no="18(2)",
            question_prefix="SRC_51b7508a04",
            rubric_prefix="SRC_93d2077755",
            evidence_type="rubric_or_marking",
            pending_reason="综合法治设问，含合同示范文本、市场监管和良法善治，收入开放容器。",
            material="""
材料二：2025年9月，我国首部专门规范住房租赁市场的行政法规——《住房租赁条例》正式施行。

《住房租赁条例》第二十八条：国务院住房城乡建设主管部门会同国务院市场监督管理部门制定并公布住房租赁合同、住房租赁经纪服务合同示范文本。

第三十三条：县级以上地方人民政府房产管理部门应当会同有关部门、住房租赁相关行业组织加强住房租赁行业诚信建设，建立住房租赁企业、住房租赁经纪机构及其从业人员信用评价制度，将相关违法违规行为记入信用记录，纳入全国信用信息共享平台，并根据信用状况实施分级分类监管。
""",
            prompt="运用法治知识，分析《住房租赁条例》上述规定的现实意义。（6分）",
            rubric="""
18（2）上述规定为住房租赁市场设立了清晰、规范的行为指引，由相关政府部门提供合同示范文本，有利于规范合同内容，防止格式条款滥用，保护租赁双方合法权益，减少合同纠纷；引导市场主体依法依规从事民事活动，弘扬诚信的社会主义价值观，规范住房租赁市场秩序；明确政府法定职责，推动政府依法履行市场监管职能，推进严格执法，推动良法善治。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 海淀 · 期末 · 第19题",
            year="2026",
            district="海淀",
            paper_type="期末",
            question_no="19",
            question_prefix="SRC_51b7508a04",
            rubric_prefix="SRC_93d2077755",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
甲公司是国内较大的综合性票务平台，运营具有售票功能的应用程序。甲公司发现郑某通过网络店铺销售针对该公司售票应用程序的抢票软件，认为这款抢票软件在一定程度上规避了平台“先到先得”的购票规则，妨碍售票业务的正常开展，遂提起诉讼，主张郑某行为构成不正当竞争，请求判令郑某停止侵权、赔偿经济损失。

郑某认为，其与原告公司不存在竞争关系，其仅为涉案抢票软件的销售者并非研发者，其销售抢票软件的行为没有造成该公司票务收入减少，不构成不正当竞争。

人民法院经审理，认为被诉行为构成不正当竞争，鉴于被诉行为已经停止，故不再另行判决停止侵权，判决郑某赔偿原告公司经济损失。

《中华人民共和国反不正当竞争法》规定，本法所称的不正当竞争行为，是指经营者在生产经营活动中，违反本法规定，扰乱市场竞争秩序，损害其他经营者或者消费者的合法权益的行为。
""",
            prompt="运用《法律与生活》知识，谈谈对本案判决的认识。",
            rubric="""
19. 根据反不正当竞争法规定，不正当竞争行为是指经营者在生产经营活动中，扰乱市场竞争秩序，损害其他经营者或者消费者的合法权益的行为。郑某利用技术手段，为用户提供不正当抢票优势，破坏平台的购票规则，干扰、妨碍平台售票业务的正常开展，损害了甲公司的信誉以及其他合法权益，构成不正当竞争，应当承担侵权责任。同时郑某的行为仅为少数消费者用户提供了便利，损害了消费者的合法权益和长远利益，有违经营者公认的商业道德，不符合社会主义核心价值观，不利于社会整体福祉的增进，扰乱了市场竞争秩序。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 西城 · 期末 · 第17题",
            year="2026",
            district="西城",
            paper_type="期末",
            question_no="17",
            question_prefix="SRC_23d3adf6f1",
            rubric_prefix="SRC_0eccc84583",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
T公司在其运营的APP内设置了“青少年模式”，首页有弹窗提示，且APP服务协议明确禁止修改其软件功能或运行效果，以及任何危害未成年人的行为。B公司将“自动关闭青少年模式弹窗”设为限时免费的会员特权，以吸引用户安装其APP，并利用技术手段屏蔽了T公司APP的“青少年模式”入口弹窗。T公司发现后，向法院起诉B公司，请求认定其不正当竞争行为，并赔偿经济损失。

法院经审理认为，被告行为构成不正当竞争，全额支持原告的诉讼请求。

《中华人民共和国未成年人保护法》第七十四条第二款：网络游戏、网络直播、网络音视频、网络社交等网络服务提供者应当针对未成年人使用其服务设置相应的时间管理、权限管理、消费管理等功能。
""",
            prompt="运用法律知识，分析法院的上述判决。",
            rubric="""
17.（8分）
依据反不正当竞争法规定，禁止经营者实施不正当竞争行为。B公司利用技术手段破坏T公司产品功能，攫取其用户流量与商业机会，损害其商业信誉和形象，构成不正当竞争，应当承担赔偿损失、消除影响等侵权责任。同时，B公司的行为规避未成年人保护法定义务，剥夺用户相关知情权与选择权，损害消费者及社会公共利益，违反诚信原则和商业道德。严厉打击此类行为，有利于维护公平竞争、推动行业健康发展，引导民事主体增强法治观念，践行社会责任，发挥网络对未成年人的正向引导。
细则：法律依据2分，反不正当竞争法1分，未成年人保护法1分；法律事实分析3分，B公司利用技术手段屏蔽、损害T公司的商业利益、规避未成年人保护法定义务各1分；价值分析3分，经济视角、法律视角、道德/价值观视角各1分；可加社会视角1分但总分不超8分。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 顺义 · 一模 · 第18题",
            year="2026",
            district="顺义",
            paper_type="一模",
            question_no="18",
            question_prefix="SRC_1da70413b2",
            rubric_prefix="SRC_8d2be8df9c",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
材料一：女大学生闫某通过网络平台向某公司投递了求职简历。简历中，包含有姓名、性别、出生年月、户口所在地等个人基本信息，某公司以“仅招男性”的招聘条件拒绝对其进行面试。闫某向法院提起诉讼，请求判令该公司赔礼道歉、支付精神抚慰金以及承担诉讼相关费用。

材料二：张某原系A公司总经理。双方签订竞业限制协议，约定张某在劳动关系存续期间及两年的竞业限制期间，不得实施违反竞业限制的相关行为。张某离职后，其妻成为B公司的投资人，经营业务与A公司存在竞争关系，且B公司的关联公司为张某缴纳社会保险金。A公司认为张某违反竞业限制约定，应返还竞业经济补偿并承担违约责任。经劳动人事争议仲裁委员会裁决，张某向A公司支付违约金。张某不服，起诉至法院，请求判决无需支付违约金。

资料卡：“竞业限制”是指用人单位与劳动者之间约定，劳动者在离职后不得到生产同类产品或经营同类产业且有竞争关系的其他用人单位任职，也不得自己生产与原单位有竞争关系的同类产品或经营同类业务。

《中华人民共和国劳动合同法》第二十三条：对负有保密义务的劳动者，用人单位可以在劳动合同或者保密协议中与劳动者约定竞业限制条款，并约定在解除或者终止劳动合同后，在竞业限制期限内按月给予劳动者经济补偿。劳动者违反竞业限制约定的，应当按照约定向用人单位支付违约金。
""",
            prompt="结合材料，运用《法律与生活》知识，闫某和张某的诉求能否得到法院的支持，并说明理由。",
            rubric="""
闫某能获得法院支持。劳动者享有平等就业和选择职业的权利，不因民族、种族、性别、宗教信仰等不同而受歧视。该公司因性别对求职者进行差别对待，属于就业歧视，违反公平、平等原则，损害了闫某平等获得就业机会的权益。
张某不能获得法院支持。根据竞业限制协议，张某应按照约定履行竞业限制义务。张某之妻作为B公司投资人，其投资行为发生在张某从A公司离职后，而且在经营业务上与A公司存在竞争关系，属于竞业限制单位。张某与配偶在婚姻关系存续期间的生产、经营所得属于夫妻共同财产，具有利益一致性。共同价值：引导劳动者坚持权利义务相统一，在维护自身劳动权益的同时也要承担相应义务，平衡劳动者和用人单位利益，构建和谐劳动关系。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2026 · 顺义 · 二模 · 第18题第2问",
            year="2026",
            district="顺义",
            paper_type="二模",
            question_no="18(2)",
            question_prefix="SRC_d421a3c089",
            rubric_prefix="SRC_57615a8445",
            evidence_type="rubric_or_marking",
            pending_reason="混合必修3《政治与法治》和选必2《法律与生活》设问，本条只提取选必2民事权利与维权部分。",
            material="""
材料二：2026年一款名为OpenClaw的开源AI智能体风靡。它能接管键盘鼠标，自动整理文件、起草邮件、填写表格、分析数据，图标是一只鲜红龙虾。开源智能体能力不断扩展的同时，也出现了新的风险：有人账户里的钱被悄悄转走，有人电脑被黑客远程控制，还有人积累多年的工作文件被一键清空。
""",
            prompt="结合材料，运用法治知识，谈谈该开源智能体可能会侵犯用户的哪些民事权利，并分析如何规避该开源智能体在推广应用过程中的风险。（8分）",
            rubric="""
（2）（8分）该开源智能体可能侵犯用户的财产权、隐私权、个人信息利益等。
选必2《法律与生活》角度：民法典明确规定保护用户人身权益和财产权益。任何组织或者个人不得侵害他人的财产权、隐私权，处理个人信息应遵循合法、正当、必要原则。当用户人格权益和财产权益受到侵害时，权利人可通过协商、调解、仲裁、诉讼等途径维护自身权益，可依法请求行为人停止侵害、排除妨碍、消除危险、赔礼道歉等；造成损害的，还可依法请求损害赔偿。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2024 · 丰台 · 一模 · 第17题",
            year="2024",
            district="丰台",
            paper_type="一模",
            question_no="17",
            question_prefix="SRC_60a70dc180",
            rubric_prefix="SRC_04f136a5f8",
            evidence_type="rubric_or_marking",
            pending_reason="",
            material="""
《中华人民共和国民法典》第一千二百一十七条：非营运机动车发生交通事故造成无偿搭乘人损害，属于该机动车一方责任的，应当减轻其赔偿责任，但是机动车使用人有故意或重大过失的除外。

资料卡：好意同乘，指驾驶人基于善意互助或友情帮助，无偿搭载他人或允许他人无偿搭乘的情谊行为。

甲某搭乙某的车出行，上车后未听乙某提醒系好安全带。乙某在驾驶过程中因雨天路滑，撞到灯杆，造成甲某受伤住院。为此，乙某主动垫付了部分医疗费用。甲某认为，本次交通事故对自己造成严重人身财产损害，乙某应承担全部责任，向其赔付医疗费、误工费和护理费等损失。乙某认为自己好意让甲某免费搭乘，由于客观原因发生意外，并无过错，不应该承担全部责任。两人为此诉至法院。

法院综合考虑本案好意同乘时的具体情况、事故事实以及被告乙某主动承担部分责任的行为等，酌情减轻乙某赔偿责任。
""",
            prompt="结合材料，运用《法律与生活》知识，谈谈法院酌情减轻被告赔偿责任的法理依据和现实意义。",
            rubric="""
参考答案：法院判决应以事实为依据，以法律为准绳。本案中，驾驶人乙某和搭乘人甲某之间形成好意同乘关系。驾驶人对搭乘人的生命财产安全负有保障义务，被告乙某发生交通事故，造成原告甲某受伤，侵犯了其生命权、健康权，需要承担相应责任。被告乙某在原告甲某受伤一事上，固然存在过错，但并非故意或重大过失，原告甲某诉请其承担全部赔偿责任，有违民事活动的公平原则，根据民法典和好意同乘相关规定，应当减轻被告乙某的赔偿责任。法院判决有利于维护双方合法权益，促进社会公平，对维持人际关系和谐，弘扬社会主义核心价值观及减少交通拥堵、倡导绿色出行具有积极意义。
评分标准说明：本题8分，法理依据5分，现实意义3分。法理依据方面，“法院判决应以事实为依据，以法律为准绳”为必踩点1分；双方形成好意同乘并明确权利义务、侵权责任2分；结合好意同乘减轻赔偿责任条件和案件实际2分。现实意义可从个人、国家司法、社会发展角度作答，涉及维护双方合法权益、保障公正司法、弘扬社会主义核心价值观等，每点1分，共3分。
""",
            ledger=ledger,
        ),
        make_entry(
            title="2024 · 顺义思政 · 二模 · 第17题",
            year="2024",
            district="顺义思政",
            paper_type="二模",
            question_no="17",
            question_prefix="SRC_3019384a5b",
            rubric_prefix="SRC_0eb74816f2",
            evidence_type="rubric_or_marking",
            pending_reason="题面材料表在当前DOCX文本层缺失，仅保留题干和设问；正式细则确认财产权/产权制度法律给分。",
            material="""
某校学习小组围绕“财产制度助力经济社会发展”的议题开展探究，搜集整理的资料如下。
""",
            prompt="结合材料，运用所学知识，说明我国财产制度改革如何助力经济社会发展。",
            rubric="""
17．（7分）
①财产制度规范民事主体的财产关系，坚持物权平等保护原则，依法有效保护各种所有制经济组织和公民的财产权，确定财产归属，增强人民群众的财产财富安全感，增强社会信心，稳定市场主体投资、交易预期，促进财产的流通使用，促进经济社会持续健康发展和国家长治久安。
②建立财产权保护的长效机制，保护财产权，就是保护劳动、保护发明创造、保护和发展生产力，贯彻创新驱动发展战略，增强各类经济主体创新创业动力，促进经济高质量发展。
③完善产权制度，促进生产关系的调整，激活社会主义市场经济蓬勃发展的内生动力，夯实社会主义市场经济的基石，从而推动经济社会的进步。
""",
            ledger=ledger,
        ),
    ]


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    packet_backup = PACKETS.with_suffix(PACKETS.suffix + f".backup_before_non_mid_zero_patch_{timestamp}")
    coverage_backup = COVERAGE.with_suffix(COVERAGE.suffix + f".backup_before_non_mid_zero_patch_{timestamp}")
    shutil.copy2(PACKETS, packet_backup)
    shutil.copy2(COVERAGE, coverage_backup)

    ledger_rows = read_csv(SOURCE_LEDGER)
    ledger = {row["source_id"]: row for row in ledger_rows}
    packets = read_jsonl(PACKETS)
    additions = new_entries(ledger)
    additions_by_title = {entry["title"]: entry for entry in additions}

    preserved_id_by_title = {
        entry["title"]: (entry.get("entry_id", ""), int(entry.get("candidate_index") or 0))
        for entry in packets
        if entry.get("title") in additions_by_title
    }
    packets = [entry for entry in packets if entry.get("title") not in additions_by_title]

    max_entry_num = max(int((entry.get("entry_id") or "E000")[1:]) for entry in packets)
    max_candidate = max(int(entry.get("candidate_index") or 0) for entry in packets)
    for entry in additions:
        preserved = preserved_id_by_title.get(entry["title"])
        if preserved:
            entry["entry_id"], entry["candidate_index"] = preserved
        else:
            max_entry_num += 1
            max_candidate += 1
            entry["entry_id"] = f"E{max_entry_num:03d}"
            entry["candidate_index"] = max_candidate
        packets.append(entry)

    write_jsonl(PACKETS, packets)

    coverage_rows = read_csv(COVERAGE)
    fieldnames = list(coverage_rows[0].keys())
    updates = {
        "2024朝阳一模": ("has_xuanbier", "1", "0", "新增第19题诚信原则。"),
        "2025西城一模": ("has_xuanbier", "1", "0", "新增第20题劳动法/集体协商。"),
        "2026丰台二模": ("has_xuanbier", "1", "1", "新增第18题动物侵权与生态修复调解；综合法治边界。"),
        "2026丰台期末": ("has_xuanbier", "1", "1", "新增第18题检察公益诉讼；细则标注法律与生活。"),
        "2026房山二模": ("has_xuanbier", "2", "1", "新增第17题涉外法治、第18(1)题AI法律风险；第17题综合法治边界。"),
        "2026海淀期末": ("has_xuanbier", "3", "1", "新增第18(1)格式条款、第18(2)住房租赁条例、第19题抢票不正当竞争。"),
        "2026西城期末": ("has_xuanbier", "1", "0", "新增第17题未成年人保护与不正当竞争。"),
        "2026顺义一模": ("has_xuanbier", "1", "0", "新增第18题平等就业与竞业限制。"),
        "2026顺义二模": ("has_xuanbier", "1", "1", "新增第18(2)开源智能体民事权利风险；混合必修3/选必2边界。"),
        "2024丰台一模": ("has_xuanbier", "1", "0", "新增第17题好意同乘侵权责任。"),
        "2024顺义思政二模": ("has_xuanbier", "1", "1", "新增第17题财产制度；题面材料表缺失待回补。"),
    }
    touched = []
    for row in coverage_rows:
        suite = row.get("suite_id", "")
        if suite in updates:
            status, legal_count, pending_count, note = updates[suite]
            row["status"] = status
            row["legal_subjective_count"] = legal_count
            row["pending_confirm_count"] = pending_count
            row["blockers"] = "" if pending_count == "0" else "module_boundary_or_material_gap"
            row["notes"] = note
            touched.append(suite)
    write_csv(COVERAGE, coverage_rows, fieldnames)

    audit_lines = [
        "# 非期中 no_xuanbier 补题审计 20260604",
        "",
        f"- packet_backup: `{packet_backup.name}`",
        f"- coverage_backup: `{coverage_backup.name}`",
        f"- added_or_replaced_entries: {len(additions)}",
        f"- touched_suites: {len(touched)}",
        "",
        "## 套卷处理",
    ]
    for suite in touched:
        audit_lines.append(f"- {suite}: {updates[suite][3]}")
    audit_lines.extend(
        [
            "",
            "## 边界说明",
            "- 2026丰台二模、2026丰台期末、2026房山二模第17题、2026海淀期末第18(2)题、2026顺义二模第18(2)题属于综合法治或模块混合场景，已用 pending_reason 标注，进入开放容器，不作为单一核心模板的唯一依据。",
            "- 2024顺义思政二模第17题正式细则确认财产权/产权制度给分，但当前DOCX题面材料表缺失，保留为题面材料缺口。",
            "- 本次补题依据当前原始PDF/扫描页/文本层回源，不沿用旧索引作为独立证据；旧索引仅用于定位疑点。",
        ]
    )
    AUDIT.write_text("\n".join(audit_lines) + "\n", encoding="utf-8")
    print(f"patched entries={len(additions)} touched_suites={len(touched)}")
    print(AUDIT)


if __name__ == "__main__":
    main()
