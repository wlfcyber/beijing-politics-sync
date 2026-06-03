#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = dt.datetime.now().strftime("%Y%m%d")
STAMP = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def clean(s: str | None) -> str:
    return " ".join((s or "").replace("\n", " ").split())


def short(s: str | None, n: int = 240) -> str:
    s = clean(s)
    return s if len(s) <= n else s[: n - 1] + "…"


questions = {r["question_id"]: r for r in read_csv(ROOT / "04_merge_audit/merged_subjective_law_questions.csv")}
rubrics = read_csv(ROOT / "04_merge_audit/merged_rubric_atoms_subjective.csv")
materials = read_csv(ROOT / "04_merge_audit/merged_material_atoms_subjective.csv")
pressure_rows = read_csv(ROOT / "10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv")
pressure = {r["question_id"]: r for r in pressure_rows}

rubrics_by_q: dict[str, list[dict[str, str]]] = {}
for r in rubrics:
    rubrics_by_q.setdefault(r["question_id"], []).append(r)

materials_by_q: dict[str, list[dict[str, str]]] = {}
for r in materials:
    materials_by_q.setdefault(r["question_id"], []).append(r)


NODES = [
    {
        "id": "LAW_V5_N01",
        "name": "一格一答",
        "student_line": "看到表格、补充完整、参考示例，先看格子问什么，一格只写一件事。",
        "ask_trigger": "完成表格；阅读材料完成下表；补充完整；参考示例；裁判要点；案件事实；拟写裁判理由。",
        "material_trigger": "表格有示例行；一行一个案例；每个空格对应机制、理由、结果、意义、证据或权利名称。",
        "minimum_judgment": "先判断这一格问机制、规则、事实、结果、意义还是证据类型。",
        "translation": "表格问机制就写调解、诉讼调解、诉讼、仲裁、和解；问理由就写规则加事实；问结果就写支持、不支持、责任；问意义就写保护谁、规范谁、维护什么秩序。",
        "sentence": "机制格：本案通过某机制解决纠纷，因为材料中出现某程序事实。理由格：依据某法律规则，材料中的某行为符合某条件，所以产生某法律后果。",
        "keywords": "表格示例；机制；裁判理由；裁判结果；调解；诉讼；证据；材料对应",
        "risk": "最怕跨格写大段模板，或把意义格写成法条、把理由格写成价值。",
        "qids": "CC0077_2025_东城_一模_19|CC0084_2025_东城_二模_19|CC0157_2025_朝阳_期末_20|CC0189_2025_石景山_一模_20|CC0213_2025_门头沟_一模_20|CC0289_2026_朝阳_二模_18|CC0325_2026_石景山_一模_18|RECOVER_2025_海淀_二模_18|RECOVER_2026_通州_一模_20",
        "strength": "strong",
    },
    {
        "id": "LAW_V5_N02",
        "name": "先判后证",
        "student_line": "问是否支持、是否有效、是否构成、判决依据，第一句先给结论。",
        "ask_trigger": "是否支持；能否得到法院支持；说明判决依据；说明裁判理由；评析行为；谈对判决的认识。",
        "material_trigger": "法院、仲裁委员会、原告诉讼请求、被告抗辩、判决结果、支持/驳回、有效/无效、成立/不成立。",
        "minimum_judgment": "先判断请求支持还是不支持，再判断合同有效、侵权成立、劳动解除合法、权利行使越界还是责任不成立。",
        "translation": "原告请求退款或赔偿翻译成诉讼请求；法院支持翻译成规则条件满足；法院驳回翻译成条件不满足或权利越界。",
        "sentence": "某请求应予支持或不予支持。依据某法律规则，判断该请求要看某条件。本案中，某事实符合或不符合该条件，所以法院作出上述判决。",
        "keywords": "支持；不支持；事实为根据；法律为准绳；合同成立；侵权责任；违约责任；证据；因果关系",
        "risk": "不能不表态直接分析；不能只写公正司法，不写具体法律关系。",
        "qids": "CC0002_2024_丰台_一模_17|CC0025_2024_朝阳_二模_17|CC0054_2024_石景山_一模_17|CC0119_2025_丰台_期末_19|CC0137_2025_昌平_二模_20|CC0143_2025_朝阳_一模_19|CC0200_2025_西城_二模_18|CC0213_2025_门头沟_一模_20|CC0214_2025_门头沟_一模_20_2|CC0238_2026_东城_二模_19|CC0244_2026_东城_期末_18|CC0251_2026_丰台_一模_20|CC0305_2026_海淀_一模_18_3|CC0364_2026_通州_期末_19_1|CC0373_2026_顺义_一模_18|RECOVER_2026_房山_一模_17_1|RECOVER_2026_西城_二模_18_1|RECOVER_2026_朝阳_期末_18_1",
        "strength": "strong",
    },
    {
        "id": "LAW_V5_N03",
        "name": "切责成链",
        "student_line": "一看到责任题，先分清合同、侵权、消费、劳动、相邻，再按关系、规则、事实、责任写。",
        "ask_trigger": "法律责任；法律依据；法院支持诉求的理由；能否赔偿；是否承担责任；合同成立；违约；侵权。",
        "material_trigger": "付款、中标、合同条款、搭售、虚假宣传、受伤、隐私、派单、奖惩、辞退、公共区域、相邻通行。",
        "minimum_judgment": "先判法律关系，再判责任成立条件；混合题分段写，合同和侵权不能糊成一段。",
        "translation": "付款出票是合同成立；公开隐私是人格权侵害；虚假宣传是知情权受损或欺诈；派单奖惩是劳动从属性；公共区域安全是安全保障义务边界。",
        "sentence": "本案中，甲乙形成某法律关系。依据相关法律，某责任成立需要满足某条件。材料中某行为符合该条件并造成某结果，所以某方应承担某责任。",
        "keywords": "要约；承诺；合同有效；违约责任；侵权责任；过错；损害；因果关系；欺诈；惩罚性赔偿；相邻关系；合理限度",
        "risk": "不要法考化；不写超教材复杂要件；不要见买卖只写消费者权益、见受伤就直接赔。",
        "qids": "CC0002_2024_丰台_一模_17|CC0054_2024_石景山_一模_17|CC0063_2024_西城_二模_16|CC0084_2025_东城_二模_19|CC0119_2025_丰台_期末_19|CC0143_2025_朝阳_一模_19|CC0150_2025_朝阳_二模_20|CC0180_2025_海淀_期末_20|CC0181_2025_海淀_期末_21|CC0195_2025_西城_一模_20|CC0200_2025_西城_二模_18|CC0213_2025_门头沟_一模_20|CC0238_2026_东城_二模_19|CC0244_2026_东城_期末_18|CC0251_2026_丰台_一模_20|CC0254_2026_丰台_二模_18|CC0289_2026_朝阳_二模_18|CC0305_2026_海淀_一模_18_3|CC0317_2026_海淀_期末_18|CC0364_2026_通州_期末_19_1|CC0373_2026_顺义_一模_18|RECOVER_2024_东城_二模_19_1|RECOVER_2024_东城_二模_19_2|RECOVER_2026_房山_一模_17_1|RECOVER_2026_西城_二模_18_1|RECOVER_2026_朝阳_期末_18_1",
        "strength": "strong",
    },
    {
        "id": "LAW_V5_N04",
        "name": "护创新",
        "student_line": "看到作品、数据、商标、商业秘密、AI 图片、不正当竞争，先判保护对象，再判侵害行为，再写创新秩序。",
        "ask_trigger": "保护科技创新；知识产权；著作权；商业秘密；植物新品种；数据；商标；商业诋毁；新质生产力。",
        "material_trigger": "未经许可使用作品或商标；抓取数据；虚假宣传；商业诋毁；技术秘密；恶意诉讼；惩罚性赔偿。",
        "minimum_judgment": "先判断保护对象，再判断行为，再判断法院用停止侵害、赔偿、惩罚性赔偿、调解或驳回恶意诉讼保护创新。",
        "translation": "未经许可用图是著作权风险；抓取并商用数据是不正当竞争；窃取技术秘密是商业秘密侵害；恶意起诉是滥用诉权。",
        "sentence": "某成果或标识受法律保护。材料中某主体未经许可或以不诚信方式实施某行为，损害权利人权益和竞争秩序，法院通过某方式保护创新主体、维护公平竞争、激发创新活力。",
        "keywords": "知识产权；著作权；商业秘密；植物新品种权；数据权益；不正当竞争；商业诋毁；惩罚性赔偿；创新活力",
        "risk": "不能一看到创新就空写新质生产力；不能把著作权、商标、商业秘密混用。",
        "qids": "CC0103_2025_丰台_一模_19|CC0131_2025_房山_一模_19|CC0137_2025_昌平_二模_20|CC0157_2025_朝阳_期末_20|CC0181_2025_海淀_期末_21|CC0189_2025_石景山_一模_20|CC0206_2025_西城_期末_19|CC0229_2026_东城_一模_18|CC0238_2026_东城_二模_19|CC0277_2026_房山_二模_18|CC0283_2026_朝阳_一模_18|CC0319_2026_海淀_期末_19|RECOVER_2025_海淀_二模_18|RECOVER_2025_丰台_二模_19_2|RECOVER_2026_延庆_一模_18_1",
        "strength": "strong",
    },
    {
        "id": "LAW_V5_N05",
        "name": "走救济",
        "student_line": "问如何维权、如何调解、起诉状、举证、公益诉讼，就写路径、证据、请求、效力。",
        "ask_trigger": "如何维权；做好哪些工作；调解；起诉状；诉讼请求；举证责任；回避；司法确认；公益诉讼。",
        "material_trigger": "协商未果、调解员、仲裁、起诉、法院调解、司法确认、证据、公益组织、强制执行力、回避申请。",
        "minimum_judgment": "先判程序阶段，再判主体，最后写法律效果。",
        "translation": "协商未果可进入调解、仲裁或诉讼；准备维权要写起诉状、证据、诉讼时效、合理诉求；法院确认调解协议是司法确认且有强制执行力。",
        "sentence": "当事人可通过某路径解决纠纷，并准备某类证据和诉讼材料。其诉讼请求应围绕某权利或责任提出，做到事实清楚、证据充分、请求合理。",
        "keywords": "调解；仲裁；诉讼；起诉状；诉讼请求；证据；诉讼时效；举证责任；公益诉讼；司法确认；强制执行力",
        "risk": "不能只写协商；不能只写诉讼不写证据；公益诉讼不能写成个人维权。",
        "qids": "CC0061_2024_西城_一模_18|CC0077_2025_东城_一模_19|CC0125_2025_延庆_一模_19|CC0150_2025_朝阳_二模_20|CC0223_2025_顺义_一模_19|CC0244_2026_东城_期末_18|CC0245_2026_东城_期末_18_2|CC0283_2026_朝阳_一模_18|CC0325_2026_石景山_一模_18|RECOVER_2024_东城_一模_19|RECOVER_2024_东城_二模_19_1|RECOVER_2025_海淀_二模_18|RECOVER_2026_门头沟_一模_18_1",
        "strength": "strong",
    },
    {
        "id": "LAW_V5_N06",
        "name": "划边界",
        "student_line": "问法律边界、风险、应对措施，就按一项风险、一条规则、一项措施写。",
        "ask_trigger": "法律边界；应对措施；违法行为；法律风险；治理；合规；AI 幻觉；生成式 AI 权责边界。",
        "material_trigger": "数字员工、AI 平台、核心代码、商业用途图案、虚假负面数据、公共区域、消防规定、共有权、提示义务。",
        "minimum_judgment": "先判具体民事风险还是宏观治理影响；具体风险进本节点，宏观影响进开放容器。",
        "translation": "虚假负面数据是商业诋毁或名誉权风险；上传核心代码是商业秘密风险；AI 图案商用是著作权风险；公共区域充电柜是共有、消防、相邻边界。",
        "sentence": "材料中的某行为存在某法律风险，触碰某法律边界。对此，相关主体应采取某措施。这样既划清权利义务边界，也为技术或社区方案留下合法空间。",
        "keywords": "法律边界；风险；名誉权；商业秘密；著作权；审核义务；保密措施；民事主体资格；提示义务；共有部分；消防规定",
        "risk": "AI 宏观产业影响、开源智能体治理、国家治理不要硬塞进具体侵权模板。",
        "qids": "CC0092_2025_东城_期末_19_1|CC0277_2026_房山_二模_18|CC0305_2026_海淀_一模_18_3|RECOVER_2025_丰台_二模_19_2|RECOVER_2026_延庆_一模_18_1|RECOVER_2026_房山_一模_17_1|RECOVER_2026_西城_二模_18_1|RECOVER_2026_西城_二模_18_2",
        "strength": "medium",
    },
    {
        "id": "LAW_V5_N07",
        "name": "补价值",
        "student_line": "意义题先写本案怎么处理，再写保护谁、规范什么、弘扬什么。",
        "ask_trigger": "意义；价值；作用；认识；如何推动；如何护航；如何守护；促进产业发展影响。",
        "material_trigger": "法院判决、典型案例、司法建议、惩罚性赔偿、调解优先、保护创新、劳动关系、公平效率、理性维权、绿色发展。",
        "minimum_judgment": "先判断评价对象，再判断受益主体，最后按个案权利、秩序规范、价值导向三层写。",
        "translation": "减轻赔偿是保护双方、保障公正、弘扬友善；消费者首单支持加购不支持是食品安全与经营秩序平衡；保护创新案例是权益、竞争秩序、司法公信。",
        "sentence": "本案通过某法律处理保护了某主体合法权益，进一步规范某类行为或行业秩序，并引导社会成员依法行使权利、诚信履行义务，弘扬公平、诚信、友善等具体价值。",
        "keywords": "合法权益；权利边界；市场秩序；劳动关系；司法公信；公平竞争；理性维权；诚信；友善；公共利益",
        "risk": "价值必须后置，不能直接写全面依法治国；没有材料铺垫就写法治中国不得分。",
        "qids": "CC0002_2024_丰台_一模_17|CC0011_2024_丰台_二模_17|CC0019_2024_朝阳_一模_19|CC0025_2024_朝阳_二模_17|CC0045_2024_海淀_二模_19|CC0054_2024_石景山_一模_17|CC0063_2024_西城_二模_16|CC0103_2025_丰台_一模_19|CC0119_2025_丰台_期末_19|CC0131_2025_房山_一模_19|CC0143_2025_朝阳_一模_19|CC0180_2025_海淀_期末_20|CC0181_2025_海淀_期末_21|CC0195_2025_西城_一模_20|CC0200_2025_西城_二模_18|CC0223_2025_顺义_一模_19|CC0229_2026_东城_一模_18|CC0251_2026_丰台_一模_20|CC0254_2026_丰台_二模_18|CC0283_2026_朝阳_一模_18|CC0318_2026_海淀_期末_18_2|CC0332_2026_石景山_二模_19|CC0340_2026_西城_一模_17|RECOVER_2024_东城_一模_19|RECOVER_2025_丰台_二模_19_2|RECOVER_2026_通州_一模_20|RECOVER_2026_西城_二模_18_2",
        "strength": "strong-with-container-limits",
    },
]


SAMPLE_RUNS = {
    "CC0077_2025_东城_一模_19": {
        "entry": "LAW_V5_N01 一格一答，叠加 LAW_V5_N05 走救济、LAW_V5_N07 补价值",
        "material_layering": "先把三个案例拆成三行，再看每个空格问的是解决机制还是案例意义。案件一已有诉讼程序和调解书；案件二是劳动者与医院的权利义务；案件三看具体表格格子功能。",
        "minimum_judgment": "每个空格先判功能，不跨格写大段。",
        "legal_trigger": "调解/诉讼调解/诉讼；劳动者权利义务统一；用人单位合法权益；构建和谐劳动关系。",
        "answer": "机制格写：本案虽未进入审判裁判，但已经启动诉讼程序，并以调解书方式化解争议，可以写调解、诉讼调解或诉讼。意义格写：对劳动者而言，该案例有利于树立权利和义务相统一的法治意识，督促劳动者依法履行义务；对医院而言，有利于维护用人单位合法权益，构建和谐劳动关系。",
        "wrong_path": "把三个意义揉成一段，或者只写法治公平正义，不按格子给最短得分句。",
    },
    "CC0143_2025_朝阳_一模_19": {
        "entry": "LAW_V5_N02 先判后证，叠加 LAW_V5_N03 切责成链、LAW_V5_N07 补价值",
        "material_layering": "王某付款出票是合同成立；A 公司隐藏/搭售 10 元外卖红包是欺诈事实；王某不能清楚知悉费用且不能拒绝是违背真实意思；法院支持请求。",
        "minimum_judgment": "王某诉讼请求应予支持，且不能漏写合同成立。",
        "legal_trigger": "合同成立；合同成立不等于生效；经营者欺诈；消费者惩罚性赔偿；在线文旅平台经营规范。",
        "answer": "王某通过平台购买机票并付款，机票已经出票，双方合同成立。合同成立不等于合同当然生效，A 公司通过技术手段擅自搭售外卖红包，使王某不能清楚知悉费用细节且无法拒绝，属于欺诈，使消费者在违背真实意思的情况下订立合同。经营者提供服务有欺诈行为的，应承担惩罚性赔偿责任，所以法院应支持王某三倍赔偿请求。该判决有利于维护消费者合法权益，规范在线文旅平台经营行为。",
        "wrong_path": "只写三倍赔偿，漏掉付款出票导致合同成立；或者只写消费者权益，漏欺诈事实。",
    },
    "CC0229_2026_东城_一模_18": {
        "entry": "LAW_V5_N04 护创新，叠加 LAW_V5_N05 走救济、LAW_V5_N07 补价值",
        "material_layering": "三案分别对应调解专利权归属、植物新品种侵权惩罚性赔偿、恶意诉讼规制。",
        "minimum_judgment": "法院不是泛泛保护创新，而是用三种司法手段分别护创新。",
        "legal_trigger": "诉讼调解；知识产权侵权；惩罚性赔偿；规制滥用诉权；司法裁判导向作用。",
        "answer": "人民法院坚持以事实为根据、以法律为准绳，发挥司法裁判导向作用。案例一中，法院通过诉讼调解化解专利权归属纠纷，提高纠纷解决效率，让创新主体回归研发。案例二中，法院对故意侵害植物新品种权行为适用惩罚性赔偿，提高侵权违法成本，保护知识产权。案例三中，法院驳回并谴责恶意诉讼，规制滥用诉权行为，维护司法秩序和创新环境。",
        "wrong_path": "只写保护新质生产力、优化营商环境，漏三案分别对应的司法手段。",
    },
    "CC0277_2026_房山_二模_18": {
        "entry": "LAW_V5_N06 划边界，叠加 LAW_V5_N04 护创新",
        "material_layering": "三类风险分列：虚假负面数据文章、上传核心代码、AI 图案直接商用。",
        "minimum_judgment": "这是具体合规风险题，不是 AI 宏观产业意义题；一项风险配一条边界和一项措施。",
        "legal_trigger": "商业诋毁/名誉权；商业秘密；著作权或外观设计权；审核义务；保密措施；授权使用。",
        "answer": "数字员工生成虚假负面数据文章，可能构成商业诋毁并侵犯相关公司的名誉权，应履行审核义务、依法经营。将公司核心代码上传公共 AI 平台，可能造成商业秘密泄露，应完善保密措施并与平台签订保密协议。数字员工设计图案直接用作商业用途，可能侵犯他人著作权或外观设计权，应进行权利审核并取得必要授权。",
        "wrong_path": "把它写成普通维权路径，或者只写科技向善，不写风险、规则和措施三列。",
    },
    "RECOVER_2026_门头沟_一模_18_1": {
        "entry": "LAW_V5_N05 走救济，叠加开放容器的公益公共利益写法",
        "material_layering": "公益社会组织提起环境民事公益诉讼；法院审查和解协议；经技术论证达成调解协议；民事调解书确认并履行。",
        "minimum_judgment": "这不是个人损害赔偿题，而是公益诉讼主体、多元纠纷解决和司法确认效力题。",
        "legal_trigger": "环境民事公益诉讼；和解；司法调解；诉讼；司法确认；强制执行效力；生态环境公共利益。",
        "answer": "从诉讼主体看，公益社会组织承担社会责任，依法提起环境民事公益诉讼，目的在于维护生态环境公共利益。从纠纷解决方式看，本案通过和解、司法调解、诉讼等多元方式消除损害风险。从法律效力看，经人民法院依法确认有效的和解或调解协议具有强制执行效力，有助于切实维护生态环境公共利益。",
        "wrong_path": "写成个人维权、一般生态意义，漏公益主体和司法确认强制执行力。",
    },
    "CC0305_2026_海淀_一模_18_3": {
        "entry": "LAW_V5_N02 先判后证，叠加 LAW_V5_N03 切责成链、LAW_V5_N06 划边界",
        "material_layering": "包间活动具有私密性，公开监控和聊天信息对应隐私权；夸大治疗功效诱导消费对应知情权、虚假宣传和欺诈。",
        "minimum_judgment": "支持原告诉讼请求，并分两条责任链写：人格权侵权和消费欺诈。",
        "legal_trigger": "隐私权；停止侵权、赔礼道歉；消费者知情权；真实全面信息；虚假宣传/欺诈；退款和惩罚性赔偿。",
        "answer": "原告诉讼请求应予支持。任何组织或者个人不得以刺探、侵扰、泄露、公开等方式侵害他人的隐私权；商家公开包厢监控录像和聊天信息，构成对消费者隐私权的侵害，应承担停止侵权、赔礼道歉等侵权责任。经营者应保护消费者知情权，提供真实、全面信息，不得作虚假或者引人误解的宣传；赵某夸大治疗功效诱导消费，构成欺诈，应退款并承担惩罚性赔偿责任。",
        "wrong_path": "只写隐私权，漏消费知情权和欺诈；或只写消费者权益，漏公开监控信息的侵权责任。",
    },
    "CC0063_2024_西城_二模_16": {
        "entry": "LAW_V5_N07 补价值，叠加 LAW_V5_N02 先判后证、LAW_V5_N03 切责成链",
        "material_layering": "首单未超合理消费需要，应支持惩罚性赔偿；后续加购超出正常生活消费需要，不支持；判决平衡食品安全与经营秩序。",
        "minimum_judgment": "先分首单和加购，不能把消费者请求全部支持或全部否定。",
        "legal_trigger": "经营者依法诚信经营；消费者合法权益；民事权利不得滥用；理性维权；食品安全和生产经营秩序平衡。",
        "answer": "经营者应依法、诚信经营，保护消费者合法权益。人民法院支持甲就首单购买行为适用食品安全法中的惩罚性赔偿请求，打击违法生产经营行为，维护消费者合法权益。同时，民事主体行使民事权利不能超过正当界限，不得滥用民事权利损害他人合法权益；甲的加购行为超出正常生活消费需要，法院不支持其就加购部分提出的惩罚性赔偿请求，有利于引导消费者依法、诚信、理性维权。该判决平衡了保证食品安全和维护生产经营秩序两种价值取向。",
        "wrong_path": "只喊保护消费者，漏权利边界；或把优化营商环境当万能结尾。",
    },
    "CC0251_2026_丰台_一模_20": {
        "entry": "LAW_V5_N02 先判后证，叠加 LAW_V5_N03 切责成链、LAW_V5_N06 划边界、LAW_V5_N07 补价值",
        "material_layering": "公共场所经营者安全保障义务要在合理限度内；现场无影响通行的客观因素；原告完全民事行为能力且自身未尽注意义务。",
        "minimum_judgment": "餐饮公司和商业管理公司不承担赔偿责任；法理依据和现实意义必须分开。",
        "legal_trigger": "事实为根据、法律为准绳；安全保障义务合理限度；过错；自我负责；权利义务平衡；友善价值。",
        "answer": "人民法院以事实为根据、以法律为准绳作出判决。依据民法典，公共场所经营者、管理者因过错造成他人损害的，应承担侵权责任。本案中，被告安全保障义务应保持在合理限度内，且证据表明事发现场不存在影响原告通行的客观因素；原告作为完全民事行为能力人，摔倒系自身未尽安全注意义务所致，因此被告无过错，不应承担赔偿责任。该判决有利于平衡双方权利义务，明确公共场所经营者、管理者安全保障义务边界，倡导安全文明出行和自我负责的安全责任意识，弘扬社会主义核心价值观。",
        "wrong_path": "法理依据和现实意义揉在一起；把事实为根据、法律为准绳写反；背法治社会模板。",
    },
    "CC0283_2026_朝阳_一模_18": {
        "entry": "LAW_V5_N04 护创新，叠加 LAW_V5_N05 走救济、LAW_V5_N07 补价值",
        "material_layering": "人民法院通过调解、惩罚性赔偿、规制不诚信诉讼、整合司法手段四层保护知识产权。",
        "minimum_judgment": "措施题要写人民法院做了什么，再写做得怎么样。",
        "legal_trigger": "调解提高效率；惩罚性赔偿提高侵权成本；公平诚信原则规制恶意诉讼；保护知识产权和社会公共利益。",
        "answer": "人民法院通过特邀第三方调解，高效化解知识产权纠纷，既维护当事人合法权益，又降低诉讼成本、提高纠纷解决效率。针对故意侵权行为，法院适用惩罚性赔偿规定，提高侵权违法成本，维护公平竞争的市场秩序。依据民法公平、诚信等基本原则，法院谴责并规制不诚信诉讼行为，保障诉讼秩序和经营秩序，避免“假维权”拖垮“真创新”。通过整合调解、惩罚、规制等司法手段，法院保护知识产权人的合法权益，兼顾社会公共利益，为新质生产力发展提供稳定、可预期的法治环境。",
        "wrong_path": "只写创新活力，不写调解、惩罚性赔偿、规制恶意诉讼三个司法动作。",
    },
    "CC0103_2025_丰台_一模_19": {
        "entry": "LAW_V5_N04 护创新，叠加 LAW_V5_N07 补价值",
        "material_layering": "近 40 名技术人员离职后利用原单位技术信息申请专利；法院适用 2 倍惩罚性赔偿；典型案例有示范价值。",
        "minimum_judgment": "意义题不是空写法治中国，必须先写企业权利、侵权惩戒、市场竞争秩序和司法示范。",
        "legal_trigger": "商业秘密/技术秘密；惩罚性赔偿；知识产权保护；公平市场环境；同类案件范例；司法公信力。",
        "answer": "本案判决维护原告方合法权益，严惩侵害技术秘密的行为，保护知识产权。法院依法适用惩罚性赔偿，提高侵权成本，规范市场竞争秩序，营造公平市场环境，以法治力量鼓励创新。作为人民法院保护科技创新典型案例，本案为同类案件提供范例，有利于提高审判质量和效率，增强司法公信力。它还引导公民和企业依法办事，增强法治信仰。",
        "wrong_path": "写维护公民合法权益、维护社会公平正义、优化营商环境，或者没有铺垫直接写法治中国建设。",
    },
}


def rubric_ids_for(qid: str, max_n: int = 8) -> str:
    return "|".join(r["rubric_atom_id"] for r in rubrics_by_q.get(qid, [])[:max_n])


def rubric_lines_for(qid: str, max_n: int = 6) -> list[str]:
    out = []
    for r in rubrics_by_q.get(qid, [])[:max_n]:
        out.append(f"- `{r['rubric_atom_id']}`：{short(r['rubric_or_answer_phrase'], 180)}")
    return out or ["- 暂无可用细则原子。"]


def material_core(qid: str) -> str:
    q = questions.get(qid, {})
    atoms = [short(a["material_phrase"], 80) for a in materials_by_q.get(qid, [])[:4]]
    if atoms:
        return "；".join(atoms)
    return short(q.get("material_text", ""), 300)


def node_by_id(node_id: str) -> dict[str, str]:
    return next(n for n in NODES if n["id"] == node_id)


def markdown_node(n: dict[str, str]) -> str:
    qids = n["qids"].split("|")
    formal = sum(1 for qid in qids if questions.get(qid, {}).get("evidence_level") == "formal")
    ref = sum(1 for qid in qids if questions.get(qid, {}).get("evidence_level") == "reference_only")
    return f"""## {n['id']}：{n['name']}

学生先记：{n['student_line']}

看到这些设问就进来：{n['ask_trigger']}

看到这些材料就进来：{n['material_trigger']}

第一判断：{n['minimum_judgment']}

材料翻译：{n['translation']}

满分句：{n['sentence']}

必写词：{n['keywords']}

误用刹车：{n['risk']}

证据：{formal} 道 formal；{ref} 道 reference_only；强度 {n['strength']}。

支持题号：{', '.join(qids)}
"""


def sample_markdown(qid: str, idx: int) -> str:
    q = questions[qid]
    s = SAMPLE_RUNS[qid]
    p = pressure.get(qid, {})
    return f"""## 样章 {idx}：{qid}

题源：{q.get('year')} {q.get('district')} {q.get('exam_stage')} 第 {q.get('question_no')} 题

证据等级：{q.get('evidence_level')}；压测状态：{p.get('pass_status', '')}

设问：{clean(q.get('ask_text')) or '设问需回源补正，当前以评分细则和题干结构定位。'}

材料核心：{material_core(qid)}

### 一、框架入口

这道题从这里进入：{s['entry']}

为什么这样进：{s['minimum_judgment']}

### 二、材料分层

{s['material_layering']}

### 三、学生最先必须判断什么

{s['minimum_judgment']}

### 四、法律知识触发

{s['legal_trigger']}

### 五、细则对应与满分句

{chr(10).join(rubric_lines_for(qid))}

满分句骨架：

{s['answer']}

### 六、易错路径

{s['wrong_path']}

### 七、对框架的验证意义

这道题检验学生是否能先用动作卡启动，再把材料事实转成法律语言，而不是背一个大而空的法治模板。
"""


def build_evidence_map() -> None:
    rows = []
    sample_ids = set(SAMPLE_RUNS.keys())
    for n in NODES:
        for qid in n["qids"].split("|"):
            q = questions.get(qid, {})
            p = pressure.get(qid, {})
            pass_status = p.get("pass_status", "")
            if q.get("evidence_level") == "reference_only" or "REFERENCE_ONLY" in pass_status:
                role = "reference_only_locked"
            elif pass_status == "PASS_CANDIDATE":
                role = "sample_calibration_core" if qid in sample_ids else "core_support"
            elif pass_status == "PARTIAL_SOURCE_CHECK":
                role = "sample_pending_source" if qid in sample_ids else "source_check_pending"
            elif pass_status == "PARTIAL_LOW_FREQ_CONTAINER":
                role = "container_only"
            elif pass_status == "PARTIAL_BOUNDARY_OPEN":
                role = "boundary_open_only"
            else:
                role = "pending"
            rows.append(
                {
                    "node_id": n["id"],
                    "node_name": n["name"],
                    "question_id": qid,
                    "evidence_level": q.get("evidence_level", "missing"),
                    "pass_status": pass_status,
                    "role_in_node": role,
                    "rubric_atom_ids_sample": rubric_ids_for(qid),
                    "boundary_note": p.get("source_check_flags", ""),
                }
            )
    write_csv(
        ROOT / f"09_candidate_frameworks/framework_v5_evidence_map_{TODAY}.csv",
        rows,
        ["node_id", "node_name", "question_id", "evidence_level", "pass_status", "role_in_node", "rubric_atom_ids_sample", "boundary_note"],
    )


def build_batch_plan() -> None:
    status_to_name = {
        "PASS_CANDIDATE": "第二批：35 道核心可扩展题",
        "PARTIAL_SOURCE_CHECK": "第三批：18 道先回源补设问/页码/题干的题",
        "PARTIAL_LOW_FREQ_CONTAINER": "第四批：5 道低频 formal 容器题",
        "PARTIAL_REFERENCE_ONLY": "第五批 A：4 道 reference_only 锁死参考题",
        "PARTIAL_BOUNDARY_OPEN": "第五批 B：3 道边界/综合开放题",
    }
    rows = []
    sample_ids = list(SAMPLE_RUNS.keys())
    for i, qid in enumerate(sample_ids, 1):
        q = questions[qid]
        rows.append(
            {
                "batch": "第一批：10 道样章校准题",
                "order": str(i),
                "question_id": qid,
                "reason": "覆盖表格、裁判、责任、创新、程序、风险、价值七类动作卡，并先校准学生能否照着写。",
                "evidence_level": q["evidence_level"],
                "pass_status": pressure.get(qid, {}).get("pass_status", ""),
                "action": "写成样章并用零基础学生压测",
            }
        )
    for r in pressure_rows:
        if r["question_id"] in sample_ids:
            continue
        rows.append(
            {
                "batch": status_to_name.get(r["pass_status"], "未分批"),
                "order": "",
                "question_id": r["question_id"],
                "reason": r.get("pressure_notes", ""),
                "evidence_level": r.get("evidence_level", ""),
                "pass_status": r.get("pass_status", ""),
                "action": "按批次处理，不再一次性喂 65 道。",
            }
        )
    write_csv(
        ROOT / f"09_candidate_frameworks/v5_batch_plan_{TODAY}.csv",
        rows,
        ["batch", "order", "question_id", "reason", "evidence_level", "pass_status", "action"],
    )


def build_sample_csv() -> None:
    rows = []
    for qid, s in SAMPLE_RUNS.items():
        q = questions[qid]
        p = pressure.get(qid, {})
        rows.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "evidence_level": q.get("evidence_level", ""),
                "framework_entry_node": s["entry"],
                "ask_text": clean(q.get("ask_text")) or "设问待回源补正",
                "material_core": material_core(qid),
                "minimum_judgment_required": s["minimum_judgment"],
                "legal_knowledge_triggered": s["legal_trigger"],
                "rubric_atom_ids_matched": rubric_ids_for(qid, 12),
                "complete_answer_generated": s["answer"],
                "easy_wrong_path": s["wrong_path"],
                "pass_status": p.get("pass_status", ""),
            }
        )
    write_csv(
        ROOT / f"10_framework_validation/framework_v5_first10_sample_runs_{TODAY}.csv",
        rows,
        [
            "question_id",
            "year",
            "district",
            "exam_stage",
            "question_no",
            "evidence_level",
            "framework_entry_node",
            "ask_text",
            "material_core",
            "minimum_judgment_required",
            "legal_knowledge_triggered",
            "rubric_atom_ids_matched",
            "complete_answer_generated",
            "easy_wrong_path",
            "pass_status",
        ],
    )


def build_framework_docs() -> None:
    counts = {}
    for r in pressure_rows:
        counts[r["pass_status"]] = counts.get(r["pass_status"], 0) + 1

    decision = f"""# V5 重写决策：从 V4 失败样本退回动作卡框架

生成时间：{STAMP}

## 结论

V4 不再修补为最终成品。它的问题不是证据不足，而是学生学习顺序错了：证据后台太重，学生前台缺少“拿到陌生题先做什么”的动作。

GPTPro 已读取当前失败框架、先前框架学习结果和 65 题证据包，给出的核心对策是：不要一次性把 65 题压成一个大目录，而是先用 10 道样章校准学生动作，再按核心题、回源题、低频容器题、reference_only 和边界题分批扩展。

## 当前证据底座

- 主观题总数：65
- formal：61
- reference_only：4
- missing：0

## 压测分层

- PASS_CANDIDATE：{counts.get('PASS_CANDIDATE', 0)}
- PARTIAL_SOURCE_CHECK：{counts.get('PARTIAL_SOURCE_CHECK', 0)}
- PARTIAL_LOW_FREQ_CONTAINER：{counts.get('PARTIAL_LOW_FREQ_CONTAINER', 0)}
- PARTIAL_REFERENCE_ONLY：{counts.get('PARTIAL_REFERENCE_ONLY', 0)}
- PARTIAL_BOUNDARY_OPEN：{counts.get('PARTIAL_BOUNDARY_OPEN', 0)}

## V5 接受的重写方向

1. 学生首屏只给动作：圈主体、抓行为、判任务、生成句。
2. 主框架用七张动作卡，不用教材目录作前台。
3. 参考旧框架的“启动感”和“材料翻译感”，但不把旧框架当证据来源。
4. 每个节点必须能落到题号和细则原子。
5. 价值句后置，必须从本案处理推出。
6. AI、涉外、国家治理、生态、校园欺凌、诉讼时效等先进入开放容器，不能污染核心私法动作卡。
7. CC0040、CC0162、CC0311、CC0353 锁为 reference_only，不支撑核心。

## 尚未关闭

Claude Opus 对 V5 对策的真实外部复核尚未在本步骤落盘；V5 目前是 Codex 根据 GPTPro 真调用和本地证据生成的候选版本，不声明最终 PASS。
"""
    (ROOT / f"09_candidate_frameworks/v5_rebuild_decision_from_gptpro_{TODAY}.md").write_text(decision, encoding="utf-8")

    framework = f"""# 选必二《法律与生活》主观题框架 V5 候选：七张动作卡

生成时间：{STAMP}

本稿用途：替代被用户否定的 V4，作为下一轮 GPTPro/Claude Opus 交叉复核和十题样章压测的候选框架。

## 学生首屏：20 秒启动法

只记一句：

> 圈主体，抓行为，先判结论，法材对位，最后收责任或价值。

拿到题先圈四样：

1. 圈主体：谁告谁，谁买谁卖，谁用谁管，谁受损，法院或仲裁委怎么处理。
2. 圈行为：签、买、付、退、用、传、抓取、辞退、搭售、调解、起诉、判决。
3. 圈请求：支持不支持，赔不赔，有效无效，构不构成，怎么维权。
4. 圈收尾词：意义、价值、作用、认识、法律边界、应对措施。

答案四句：

1. 结论句：请求支持不支持，行为构成不构成，条款有效无效。
2. 规则句：写清法律规则，不写法考式复杂理论。
3. 材料句：把材料事实塞进规则。
4. 落点句：落到责任、救济、边界、意义。

## 七张动作卡

{chr(10).join(markdown_node(n) for n in NODES)}

## 开放容器和边界刹车

出现国家治理能力现代化、涉外法治、依法行政、AI 产业发展、开源智能体综合治理、绿色发展、生态文明、校园欺凌惩教、诉讼时效制度、法治德治结合等信号，先不要套合同侵权劳动模板。

开放容器三句法：

1. 这个制度或规则是什么。
2. 材料中怎么体现。
3. 它发挥什么具体作用。

AI 题专门刹车：

- 具体民事问题：AI 不具民事主体资格、AI 作品权属、隐私个人信息、商业秘密、著作权、欺诈、提示义务，进入 N03、N04、N06。
- 宏观影响问题：AI 产业发展、开源智能体治理、国家数字治理，进入开放容器。
- 不能一看到 AI 就写创新活力，也不能一看到 AI 就写侵权责任。
"""
    (ROOT / f"09_candidate_frameworks/framework_v5_action_card_candidate_{TODAY}.md").write_text(framework, encoding="utf-8")

    student = f"""# 选必二法律主观题 V5 学生一页纸

生成时间：{STAMP}

## 一句话

圈主体，抓行为，先判结论，法材对位，最后收责任或价值。

## 先圈四样

- 主体：谁和谁发生关系，谁受损，谁裁判。
- 行为：签、买、付、退、用、传、抓取、辞退、搭售、调解、起诉、判决。
- 请求：支持吗，赔吗，有效吗，构成吗，怎么维权。
- 收尾：责任、救济、边界、意义、价值。

## 七张动作卡

1. 一格一答：表格题先看每一格问什么，一格只写一个得分点。
2. 先判后证：问是否支持、是否有效、是否构成，第一句先表态。
3. 切责成链：责任题先分合同、侵权、消费、劳动、相邻，再按关系、规则、事实、责任写。
4. 护创新：作品、数据、商标、商业秘密、不正当竞争，先判保护对象，再判侵害行为。
5. 走救济：维权、调解、起诉、举证、公益诉讼，写路径、证据、请求、效力。
6. 划边界：风险题一项风险配一条法律边界和一项措施。
7. 补价值：意义题先写本案怎么处理，再写保护谁、规范什么、弘扬什么。

## 四句满分答案

第一句：某请求应支持或不支持，某行为构成或不构成，某条款有效或无效。

第二句：依据相关法律，某规则要求某条件。

第三句：本案中，材料事实一、事实二、事实三符合或不符合这个条件。

第四句：所以某方应承担某责任、通过某程序救济，或该处理有利于保护某主体、规范某秩序、弘扬某具体价值。

## 五个不能

- 不能只背口号，不处理本案。
- 不能把意义题写成全面依法治国空话。
- 不能把 AI、涉外、国家治理题硬塞进合同侵权模板。
- 不能把 reference_only 题当核心套路。
- 不能把表格题写成整段大作文。
"""
    (ROOT / f"11_final_framework/framework_v5_student_one_page_draft_{TODAY}.md").write_text(student, encoding="utf-8")


def build_sample_docs() -> None:
    ids = list(SAMPLE_RUNS.keys())
    sample_md = "# V5 十题样章：先让学生真的会用\n\n"
    sample_md += f"生成时间：{STAMP}\n\n"
    sample_md += "这不是最终宝典全量稿，而是先用 10 道代表题检验七张动作卡能否让学生立刻写出接近细则的答案。\n\n"
    for i, qid in enumerate(ids, 1):
        sample_md += sample_markdown(qid, i) + "\n"
    (ROOT / f"10_framework_validation/framework_v5_first10_sample_runs_{TODAY}.md").write_text(sample_md, encoding="utf-8")

    baodian = f"""# 选必二法律主观题满分宝典 V5 十题样章

生成时间：{STAMP}

## 第一部分：最终框架候选

当前采用“七张动作卡”：

{chr(10).join(f'- {n["id"]} {n["name"]}：{n["student_line"]}' for n in NODES)}

## 第二部分：学生速记

圈主体，抓行为，先判结论，法材对位，最后收责任或价值。

## 第三部分：十题逐题运行示范

{chr(10).join(sample_markdown(qid, i) for i, qid in enumerate(ids, 1))}

## 第四部分：当前验收状态

这份样章已吸收 GPTPro 对 V4 的失败诊断，并回到 65 题证据底座。它尚未替代最终宝典：还需要 Claude Opus 复核、十题零基础学生压测、再扩展到 35 道 PASS_CANDIDATE 核心题，然后才可进入全量 65 题宝典。
"""
    (ROOT / f"12_final_baodian/选必二法律主观题满分宝典_v5_十题样章_{TODAY}.md").write_text(baodian, encoding="utf-8")


def build_banks() -> None:
    sentence_rows = []
    trigger_rows = []
    for n in NODES:
        sentence_rows.append(
            {
                "node_id": n["id"],
                "node_name": n["name"],
                "sentence_template": n["sentence"],
                "must_have_keywords": n["keywords"],
                "use_condition": n["ask_trigger"],
                "do_not_use_when": n["risk"],
                "supporting_question_ids": n["qids"],
            }
        )
        trigger_rows.append(
            {
                "node_id": n["id"],
                "node_name": n["name"],
                "ask_trigger": n["ask_trigger"],
                "material_trigger": n["material_trigger"],
                "minimum_judgment": n["minimum_judgment"],
                "translation_pattern": n["translation"],
            }
        )
    write_csv(
        ROOT / f"12_final_baodian/full_score_sentence_bank_v5_draft_{TODAY}.csv",
        sentence_rows,
        ["node_id", "node_name", "sentence_template", "must_have_keywords", "use_condition", "do_not_use_when", "supporting_question_ids"],
    )
    write_csv(
        ROOT / f"12_final_baodian/material_trigger_bank_v5_draft_{TODAY}.csv",
        trigger_rows,
        ["node_id", "node_name", "ask_trigger", "material_trigger", "minimum_judgment", "translation_pattern"],
    )


def append_status() -> None:
    note = f"""

## STEP_73_V5_ACTION_CARD_REBUILD_STARTED_AND_FIRST10_BUILT ({STAMP})

- GPTPro 当前 V4 + 先前框架学习结果合审回答已落盘：`09_candidate_frameworks/gptpro_current_framework_prior_learning_countermeasures_20260520.md`。
- 已按 GPTPro 对策生成 V5 动作卡候选框架、证据映射、分批计划、学生一页纸和十题样章。
- 当前仍不声明最终 PASS：Claude Opus 真实复核、十题零基础学生压测、35 道核心题扩展仍待完成。
"""
    for rel in ["PROGRESS.md", "TODO.md", "governor_board.md"]:
        path = ROOT / rel
        path.write_text(path.read_text(encoding="utf-8") + note, encoding="utf-8")


def main() -> None:
    build_framework_docs()
    build_evidence_map()
    build_batch_plan()
    build_sample_csv()
    build_sample_docs()
    build_banks()
    append_status()
    print("built V5 action-card framework artifacts for", TODAY)


if __name__ == "__main__":
    main()
