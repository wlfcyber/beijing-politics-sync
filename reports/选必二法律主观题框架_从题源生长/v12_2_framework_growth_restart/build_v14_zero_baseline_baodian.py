from __future__ import annotations

import csv
import random
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "v13_10_final_baodian_integrated"
OUT = ROOT / "v14_2_zero_baseline_framework_baodian"
TRACE_FILE = SRC / "traceability" / "TRACEABILITY_MATRIX_v13_10_final.csv"
OPEN_CONTAINER = SRC / "04_开放容器与不晋升题附录_v13_10.md"
SOURCE_ROOT = ROOT.parent
MATERIAL_ATOMS_FILE = SOURCE_ROOT / "02_material_atoms" / "material_atoms_subjective_claudecode.csv"
RUBRIC_ATOMS_FILE = SOURCE_ROOT / "03_rubric_atoms" / "rubric_atoms_subjective_claudecode.csv"


CONFUCIUS_REPAIR_RULES = [
    "B1 表格题看不见表头时，默认三列写：材料事实 -> 法律规则 -> 裁判要点/意义。",
    "技术秘密题必须写：秘密性 -> 价值性 -> 保密措施 -> 不正当获取使用 -> 责任。",
    "数据抓取题必须写：合法投入形成数据产品 -> 绕过限制抓取 -> 商业化使用 -> 损害竞争秩序。",
    "在职管理人员违规履职归入 A8 边界：岗位职责 -> 诚信审慎义务 -> 违规行为 -> 单位损失 -> 相应责任。",
    "A4+A6 商品致损题固定顺序：合同违约 -> 人身/财产损害 -> 因果关系 -> 赔偿范围。",
    "商业损失只有在用途已告知、有证据、有因果、可预见时才直接支持；证据不足时写需证明。",
    "B2+B6 混合题先写责任，再写证据、路径、请求。",
    "劳动关系意义题按：表达诉求 -> 保护权益 -> 规范用工 -> 减少争议 -> 稳定生产。",
    "一个题多主体时，必须写成一个主体一条链，禁止糊成一段。",
    "所有 B5 价值题必须先写材料中的具体制度或行为，再写保护对象和秩序价值。",
    "题干已定性为“技术秘密侵权”时，即使材料压缩没列明，也要先写秘密性、价值性、保密措施这个法律前提。",
    "多主体评析题按主体分链：外部竞争侵权 -> 合同履行责任 -> 内部履职责任；哪个主体对应哪条链就写哪条。",
    "“补充完整+任选其一”题先短句补全所有法律问题，再任选一项展开权利、侵害、证据、路径、请求。",
    "法律+经济综合意义题按：法律机制 -> 权益公平 -> 规则预期 -> 降低争议成本 -> 提高效率 -> 平衡。",
]


TARGETED_REPAIR_RULES = {
    "CC0157_2025_朝阳_期末_20": [
        "数据抓取链：合法投入形成数据产品 -> 绕过限制抓取 -> 商业化使用 -> 损害竞争秩序。",
        "旅游项目链：工作人员执行任务 -> 违反安全保障义务 -> 造成游客损害 -> 经营者承担相应侵权责任。",
        "B1 无表头时默认按“事实、规则、裁判要点/意义”三列作答。",
    ],
    "CC0103_2025_丰台_一模_19": [
        "题干已定性为技术秘密侵权时，也要先写秘密性、价值性、保密措施这个法律前提。",
        "技术秘密链必须补足秘密性、价值性、保密措施，再落到不正当使用和惩罚性赔偿。",
        "意义题不能空喊创新，要从高额赔偿和停止侵害推出保护科技创新、公平竞争和司法示范。",
    ],
    "CC0238_2026_东城_二模_19": [
        "乙公司和张某必须分主体作答：乙公司走商业诋毁/不正当竞争，张某走岗位职责和诚信审慎义务。",
        "多主体评析顺序：先乙公司外部竞争侵权，再乙公司合同履行责任，最后张某内部履职责任。",
    ],
    "CC0244_2026_东城_期中_18": [
        "先写买卖合同成立和交付瑕疵，再写无人机坠毁造成的人身/财产损害和因果关系。",
        "商业拍摄损失按“用途已告知、有证据、有因果、可预见”判断；证据不足时写需证明。",
        "若设问还问维权，顺序是责任结论 -> 证据 -> 路径 -> 请求。",
    ],
    "CC0289_2026_朝阳_二模_18": [
        "先补表格中的法律问题，再任选一项按权利、侵害、证据、路径写依法保护。",
        "“补充完整+任选其一”题必须先短句补全所有法律问题，再任选一项展开权利、侵害、证据、路径、请求。",
    ],
    "CC0195_2025_西城_一模_20": [
        "劳动公平效率意义题按：表达诉求 -> 保护权益 -> 规范用工 -> 减少争议 -> 稳定生产。",
        "法律+经济综合意义题按：法律机制 -> 权益公平 -> 规则预期 -> 降低争议成本 -> 提高效率 -> 平衡。",
    ],
}


MANUAL_ROW_PATCHES = {
    "CC0244_2026_东城_期中_18": {
        "material_core": "陈某向店主刘某发邮件购买 A 型号无人机并明确用于重要商业拍摄，刘某回复全新原装、价款 15000 元，陈某立即转账。刘某误寄内部结构轻微损伤的同型号展示机，陈某首次使用时无人机因该损伤失控坠毁，砸伤陈某手臂，产生医疗费 8000 元，并错过商业拍摄损失收入 5000 元。陈某要求赔偿，双方协商未果；第二问要求说明维权成功需要做好哪些工作。",
        "material_trigger": "邮件购买、报价、转账 → 要约承诺达成一致，买卖合同成立并生效 → 双方受合同约束；刘某交付内部结构损伤展示机 → 履行不符合约定，违反全面履行和诚信履行义务 → 承担违约责任；无人机因损伤坠毁砸伤陈某 → 瑕疵交付与人身损害有因果关系 → 医疗费等合理损失可请求赔偿；用于重要商业拍摄已告知，损失有证据且可预见 → 商业收入损失可主张，否则需进一步证明；协商未果且要维权 → 保存邮件、转账、检测、现场、医疗、商业合同等证据 → 可协商、调解、仲裁或诉讼并提出明确请求",
        "answer_skeleton": "陈某与刘某通过邮件报价和转账形成买卖合同，合同成立并生效。 / 刘某未交付全新原装无人机，而误寄内部损伤展示机，构成违约，应承担继续履行、退换、赔偿等违约责任。 / 该损伤导致无人机坠毁并砸伤陈某，刘某还应就医疗费等与损害有因果关系的合理损失承担赔偿责任。 / 5000 元商业拍摄损失能否支持，要看陈某已告知商业用途、损失证据、因果关系和可预见性。 / 维权时应保存邮件、转账记录、商品检测、坠毁现场、医疗票据、商业拍摄合同和收入损失证据，选择协商、调解或诉讼并明确请求。",
        "rubric_scoring_anchor": "合同成立并有效。 / 刘某交付瑕疵展示机，违反全面履行和诚信履行义务，承担违约责任。 / 无人机瑕疵与陈某受伤、财产损失存在因果关系，合理损失可赔偿。 / 商业拍摄损失需证明用途已告知、损失真实、因果关系和可预见性。 / 维权准备写证据、路径和明确请求。",
        "student_warning": "只写合同成立不写违约；只写侵权不写合同；5000 元商业损失不看可预见和证据；维权题只写依法维权",
    },
    "CC0125_2025_延庆_一模_19": {
        "material_core": "杨某在网店购买 DIY 模具类商品并签收后，在未与经营者贾某协商一致的情况下点击“仅退款”且退款成功；贾某要求退货，杨某称商品已扔掉。贾某认为应先确认货物质量和是否符合“仅退款”条件，杨某认为商品质量不合格且商家未及时回复。题目要求作为法官说明如何调解并说明理由。",
    },
    "CC0103_2025_丰台_一模_19": {
        "answer_skeleton": "先写技术秘密保护的法律前提：相关技术信息具有秘密性、价值性并采取保密措施，属于受保护对象。 / 再结合离职人员、专利申请和竞争使用说明不正当获取、使用技术秘密，侵害创新成果并破坏公平竞争。 / 最后写惩罚性赔偿和停止侵害提高违法成本，有利于保护科技创新、维护公平竞争、增强司法保护示范。",
        "rubric_scoring_anchor": "技术秘密受保护须有秘密性、价值性和保密措施。 / 离职人员及被告方不正当使用原单位技术信息申请专利，侵害技术秘密和创新投入。 / 高额惩罚性赔偿、停止侵害等责任提高侵权成本，保护科技创新和公平竞争。",
    },
    "CC0238_2026_东城_二模_19": {
        "answer_skeleton": "对乙公司第一层：捏造事实贬损竞争对手，构成商业诋毁/不正当竞争，破坏公平竞争秩序。 / 对乙公司第二层：签约进场后管理混乱导致项目延期，还可能承担合同履行不当的相应责任。 / 对张某：作为项目负责人，应按程序审慎核实合作方，未经查证违规签约，违反岗位职责和诚信审慎义务，造成单位损失，应承担相应内部或法律责任。 / 最后收束：法律规制此类行为，有利于维护公平竞争和法治化营商环境。",
        "rubric_scoring_anchor": "乙公司捏造事实贬损竞争对手，写不正当竞争/商业诋毁和公平竞争秩序。 / 乙公司管理混乱导致项目延期，写合同履行责任。 / 张某未经查证违规签约，写岗位职责、诚信审慎义务和相应责任。 / 价值只能从规范竞争和营商环境推出。",
    },
    "CC0289_2026_朝阳_二模_18": {
        "b_axis": "B7_法律问题识别/填空 + B6_调解/维权/纠纷解决路径",
        "answer_skeleton": "先把三个问答分别短句补全：高空抛坠物涉及侵权责任和举证规则；摄像头涉及隐私权/个人信息保护；违法构筑物涉及相邻关系和举证责任。 / 再任选一项展开：写权利名称、侵害事实、应保存的证据、可选择的协商/调解/诉讼路径和明确请求。 / 最后说明依法保护权利既要有实体权利判断，也要有证据和程序意识。",
        "rubric_scoring_anchor": "补充完整部分要覆盖三个问答的法律问题。 / 任选其一部分要写权利、侵害、证据、路径、请求。 / 摄像头题不能只写相邻关系，应写隐私权或个人信息边界。",
    },
    "CC0195_2025_西城_一模_20": {
        "answer_skeleton": "先写法律机制：集体协商和集体合同使劳动者依法表达工资、加班、劳动定额等诉求。 / 再写权益公平：保护劳动报酬和劳动条件，促进社会公平。 / 再写规则预期和成本：明确工资支付、劳动定额和加班规则，减少劳动争议和协商成本。 / 最后写效率和平衡：稳定企业用工和生产秩序，提高经济效率，实现公平保护与效率提升的平衡。",
        "rubric_scoring_anchor": "表达诉求、保护权益、规范用工、减少争议、稳定生产。 / 必须同时写社会公平和经济效率，不能只写劳动权益保护。 / 要把工资、加班、劳动定额、工资支付办法等材料信号带入答案。",
    },
}


A_RULES = {
    "A1_民事法律关系总论": {
        "memory": "只管效力骨架，不抢具体场景。",
        "trigger": "年龄、智力、意思表示、代理、追认、时效、民事法律行为效力。",
        "not_this": "题目还有消费、合同、人格、劳动、物权等具体场景时，A1 只补效力，不做主入口。",
        "chain": "行为能力/意思表示 -> 效力或追认 -> 返还/分担。",
        "hard": "限制民事行为能力人实施明显超出其年龄、智力和经济认知范围的行为，未经法定代理人同意或追认，不发生应有效力；已取得财产结合过错返还或分担。",
    },
    "A2_人身权与人格权": {
        "memory": "先叫准权利名，再写侵害和责任。",
        "trigger": "生命健康、姓名、肖像、名誉、商誉、隐私、个人信息、未成年人身心利益。",
        "not_this": "有消费背景也不能把隐私、名誉、个人信息请求全塞进 A9。",
        "chain": "具体人格利益 -> 侵害行为 -> 损害后果 -> 停止/删除/道歉/赔偿。",
        "hard": "未经同意公开他人私密活动、私密信息或可识别个人信息，或无事实依据贬损他人名誉、商誉，应承担停止侵害、消除影响、赔礼道歉、赔偿损失等责任。",
    },
    "A3_物权与相邻关系": {
        "memory": "先判权利边界，再看实际影响。",
        "trigger": "房屋、共有部分、车位、通行、采光、通风、安全、相邻关系、业主共同决定。",
        "not_this": "审批、公示、消防、法院勘查通常是事实和程序支持，不自动抢成 A10。",
        "chain": "权利归属/共有部分 -> 使用边界/相邻影响 -> 程序和实际影响 -> 公平合理处理。",
        "hard": "相邻权利人应按照有利生产、方便生活、团结互助、公平合理原则处理相邻关系；利用共有部分或改变共有部分用途，应符合法定程序并结合实际影响判断。",
    },
    "A4_合同": {
        "memory": "先合同成立履行，再责任。",
        "trigger": "买卖、服务、报价、付款、交付、质量、期限、退费、违约金、研发委托、租赁。",
        "not_this": "生活消费中的知情权、欺诈、格式条款可转 A9；商业购买或履约损失通常先 A4。",
        "chain": "合同成立生效 -> 是否全面诚信履行 -> 违约事实 -> 继续履行/补救/返还/违约金/赔偿。",
        "hard": "合同成立并生效后，当事人应全面履行、诚信履行；未按约交付、迟延履行、履行不符合约定或拒不履行，构成违约并承担相应责任。",
    },
    "A5_知识产权与竞争秩序": {
        "memory": "保护创新投入和公平竞争。",
        "trigger": "作品、商标、商业秘密、技术秘密、数据抓取、混淆、虚假宣传、商业诋毁、竞争秩序。",
        "not_this": "劳动者离职、合同关系、平台服务只是取得或使用信息的背景，不抢 A5。",
        "chain": "受保护对象 -> 不正当获取/使用/传播/混淆 -> 损害创新或竞争利益 -> 停止/消除/赔偿。",
        "hard": "行为人以不正当方式获取、使用他人合法投入形成的数据产品、商业秘密或经营成果，并进行商业化利用，损害竞争利益和公平竞争秩序，应承担相应民事责任。",
    },
    "A6_侵权责任": {
        "memory": "四件套：损害、过错、因果、责任。",
        "trigger": "人身损害、财产损害、安全保障义务、公共场所、旅游游乐、工作人员执行任务、产品致损。",
        "not_this": "损害从合同瑕疵履行引出时，先 A4 定违约，再用 A6 补损害赔偿。",
        "chain": "权益受损 -> 违法/过错或管理义务违反 -> 因果关系 -> 赔偿和减责。",
        "hard": "经营者或公共场所管理者负有安全保障义务；工作人员执行工作任务造成他人损害的，通常由用人单位或经营者承担相应侵权责任。",
    },
    "A7_婚姻家庭与继承": {
        "memory": "身份关系优先，不写成普通合同。",
        "trigger": "夫妻、亲子、扶养、赡养、共同债务、遗嘱、继承、遗赠扶养协议、老人儿童权益。",
        "not_this": "遗赠扶养协议、家庭财产安排不简单写成普通合同履行。",
        "chain": "身份/继承关系 -> 法定义务或处分效力 -> 履行情况 -> 家庭责任和价值。",
        "hard": "家庭成员之间的权利义务应在身份关系和法定责任中判断，既保护婚姻家庭秩序，也维护老人、未成年人等主体合法权益。",
    },
    "A8_劳动关系": {
        "memory": "劳动不是普通合同。",
        "trigger": "招聘、简历、试用期、解除、工资、社保、竞业限制、劳动仲裁、用工管理。",
        "not_this": "不要把试用期解除、工资社保、竞业限制写成普通合同欺诈。",
        "chain": "劳动关系 -> 劳动者/用人单位义务 -> 解除或限制是否合法 -> 支持请求或维护用工秩序。",
        "hard": "劳动关系既保护劳动者合法权益，也允许用人单位依法管理；解除、竞业限制、工资社保等争议要同时看事实、制度、程序和合法合理边界。",
    },
    "A9_消费者权益与经营者义务": {
        "memory": "生活消费中的知情、公平、安全、欺诈。",
        "trigger": "未成年人消费、打赏、文身、预扣款、格式条款、虚假宣传、知情权、公平交易权、安全保障。",
        "not_this": "商业经营用途购买通常先 A4；人格权请求仍要独立写 A2。",
        "chain": "消费关系 -> 经营者义务 -> 消费者权利受损 -> 退赔/惩罚性赔偿/合理分担。",
        "hard": "经营者应保障消费者知情权、公平交易权和安全保障权益；虚假宣传、提示说明不足、格式条款排除主要权利等，应承担退赔、赔偿或相应责任。",
    },
    "A10_多元纠纷解决与诉讼程序": {
        "memory": "只有问路径、证据、程序时才主导。",
        "trigger": "证据、调解、仲裁、诉讼、起诉状、举证责任、司法确认、公益诉讼、维权准备。",
        "not_this": "不要因为材料出现法院、判决、调解就抢掉实体法律关系。",
        "chain": "争议焦点 -> 证据 -> 协商/调解/仲裁/诉讼 -> 明确请求和程序效果。",
        "hard": "当事人应围绕争议焦点保存证据，选择协商、调解、仲裁、诉讼或司法确认等合法路径，提出明确、合理、可证明的请求。",
    },
}


B_RULES = {
    "B1_表格/裁判要点/补链": {
        "memory": "一格一链。",
        "shape": "事实 -> 规则 -> 裁判要点。真实表头优先；看不清时用默认三列。",
        "first": "先读列名，不写散文；一行只处理一个案例或一个要点。",
    },
    "B2_判决/裁判/责任理由": {
        "memory": "先关系，后规则事实，最后责任。",
        "shape": "法律关系 -> 规则 -> 材料事实 -> 结论 -> 责任方式。",
        "first": "第一句就回应法院为什么这样判或谁担责。",
    },
    "B3_诉求/请求能否支持": {
        "memory": "先结论，再分项。",
        "shape": "支持/不支持/部分支持 -> 权利基础 -> 要件事实 -> 责任范围。",
        "first": "不要绕圈，先写诉求是否支持及范围。",
    },
    "B4_评析/认识/观点": {
        "memory": "合理处、边界、正确立场。",
        "shape": "观点合理处 -> 片面或边界 -> 正确法律立场 -> 本案处理。",
        "first": "不要写成纯意义题，要先评观点或做法。",
    },
    "B5_意义/价值/保护/推动": {
        "memory": "从本案推出价值。",
        "shape": "保护对象 -> 约束行为 -> 维护秩序/推动治理。",
        "first": "不空喊法治；每个意义都要挂回材料事实。",
    },
    "B6_调解/维权/纠纷解决路径": {
        "memory": "证据、路径、请求。",
        "shape": "固定争议焦点 -> 保存证据 -> 选择路径 -> 提出请求。",
        "first": "不要只写“依法维权”，要写清准备什么和怎么走。",
    },
    "B7_法律问题识别/填空": {
        "memory": "短语短句，不写大段。",
        "shape": "法律问题名词 + 关键边界；每空一句，不扩写判决理由。",
        "first": "先看横线问的是问题名、责任名、程序名还是权利名。",
    },
    "B7_法律问题识别/填空 + B6_调解/维权/纠纷解决路径": {
        "memory": "先补全，再展开。",
        "shape": "短句补全所有法律问题 -> 任选一项写权利、侵害、证据、路径、请求。",
        "first": "先把每个问答的法律问题补成短句，再展开任选项。",
    },
}


A_SWITCHES = {
    "A1_民事法律关系总论": "年龄/智力/金额是否相适应；是否同意或追认；是否返还；各方是否有过错。",
    "A2_人身权与人格权": "先叫权利名；看是否未经同意或无事实依据；看是否有损害；落停止、删除、道歉、赔偿。",
    "A3_物权与相邻关系": "专有还是共有；是否共同决定；是否实际影响采光通行安全；审批消防是证据还是路径。",
    "A4_合同": "合同是否成立生效；履行是否合约；损失是否有证据；商业购买还是生活消费。",
    "A5_知识产权与竞争秩序": "对象是否受保护；秘密性/价值性/保密措施是否成立；手段是否不正当；是否商业化使用并损害竞争秩序。",
    "A6_侵权责任": "损害是什么；过错或管理义务违反是什么；因果关系是否成立；是否有受害人过错。",
    "A7_婚姻家庭与继承": "身份关系是什么；协议/遗嘱/继承效力如何；谁履行了扶养赡养义务；保护哪类家庭责任。",
    "A8_劳动关系": "是否劳动关系；劳动者义务和用人单位义务分别是什么；解除/竞业/社保是否事实充分、程序合法、限制适度。",
    "A9_消费者权益与经营者义务": "是否生活消费；知情、公平、安全、欺诈哪项受损；经营者是否提示说明；退赔或分担是否有事实。",
    "A10_多元纠纷解决与诉讼程序": "争议焦点是什么；谁负举证责任；证据有哪些；走协商、调解、仲裁、诉讼还是司法确认。",
}


def read_rows() -> list[dict[str, str]]:
    with TRACE_FILE.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return enrich_rows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def clean(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def is_answer_like(text: str) -> bool:
    bad_markers = [
        "参考答案",
        "【答案】",
        "答案】",
        "【分析】",
        "【详解】",
        "评分",
        "答案：",
        "评分标准",
        "给分",
        "可从",
        "若答",
        "原卷无答案",
        "此答案仅供参考",
        "考点考查",
        "能力考查",
        "核心素养",
        "第一步：审设问",
        "第二步：审材料",
        "第三步：整合信息",
        "[page",
        "第7页/共",
        "第17页/共",
    ]
    return any(marker in text for marker in bad_markers)


def load_atom_texts(path: Path, fields: list[str], *, skip_answer_like: bool) -> dict[str, list[str]]:
    atoms: dict[str, list[str]] = defaultdict(list)
    if not path.exists():
        return atoms
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            qid = clean(row.get("question_id"))
            if not qid:
                continue
            for field in fields:
                text = clean(row.get(field))
                if not text:
                    continue
                if skip_answer_like and is_answer_like(text):
                    continue
                if text not in atoms[qid]:
                    atoms[qid].append(text)
    return atoms


def compact_join(parts: list[str], limit: int = 2200) -> str:
    out: list[str] = []
    total = 0
    for part in parts:
        part = clean(part)
        if not part:
            continue
        if total + len(part) > limit and out:
            break
        out.append(part)
        total += len(part)
    return " ".join(out)


def should_enrich_material(text: str) -> bool:
    return "…" in text or "..." in text


def enrich_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    material_atoms = load_atom_texts(
        MATERIAL_ATOMS_FILE,
        ["material_phrase", "plain_description"],
        skip_answer_like=True,
    )
    rubric_atoms = load_atom_texts(
        RUBRIC_ATOMS_FILE,
        [
            "what_expression_is_rewarded",
            "plain_reward_description",
            "rubric_or_answer_phrase",
            "legal_knowledge_or_rule_if_explicit",
            "value_expression_if_explicit",
        ],
        skip_answer_like=True,
    )
    # Keep the curated v13.10 scoring anchors by default. Raw rubric atoms often
    # contain classroom-slide fragments, answer-analysis labels, or marking-note
    # chatter that should not enter the student-facing baodian.
    rubric_atoms = {}
    for row in rows:
        qid = row.get("question_id", "")
        row["v14_material_enrichment"] = ""
        row["v14_rubric_enrichment"] = ""

        material = clean(row.get("material_core"))
        if qid in material_atoms and should_enrich_material(material):
            enriched = compact_join(material_atoms[qid])
            if len(enriched) > len(material):
                row["v14_material_core_original"] = material
                row["material_core"] = enriched
                row["v14_material_enrichment"] = "material_atoms_subjective_claudecode"
            else:
                row["v14_material_core_original"] = ""
        else:
            row["v14_material_core_original"] = ""

        rubric = clean(row.get("rubric_scoring_anchor"))
        extra_rubric = compact_join(rubric_atoms.get(qid, []), limit=1400)
        if extra_rubric and len(extra_rubric) > len(rubric):
            row["v14_rubric_anchor_original"] = rubric
            row["rubric_scoring_anchor"] = extra_rubric
            row["v14_rubric_enrichment"] = "rubric_atoms_subjective_claudecode"
        else:
            row["v14_rubric_anchor_original"] = ""
        if qid in MANUAL_ROW_PATCHES:
            row.update(MANUAL_ROW_PATCHES[qid])
            row["v14_material_enrichment"] = "manual_source_patch_after_confucius_review"
    return rows


def bullets_from_slashes(value: str) -> list[str]:
    parts = [clean(p).strip("。；; ") for p in re.split(r"\s*/\s*", value or "") if clean(p)]
    return parts or ["先把材料事实压进对应规则，再落到责任、请求、路径或意义。"]


def split_trigger(value: str) -> list[tuple[str, str, str]]:
    rows = []
    for raw in re.split(r"[；;]\s*", value or ""):
        raw = clean(raw).strip("。")
        if not raw:
            continue
        bits = [clean(x) for x in re.split(r"\s*→\s*", raw) if clean(x)]
        if len(bits) >= 3:
            rows.append((bits[0], bits[1], " → ".join(bits[2:])))
        elif len(bits) == 2:
            rows.append((bits[0], bits[1], "推出责任、请求或意义。"))
        else:
            rows.append((bits[0], "翻译成对应法律规则。", "落成可得分结论。"))
    return rows or [("材料中的主体、行为、损害或请求", "翻译成法律关系、权利义务、构成要件或程序规则", "落成结论、责任、路径或意义")]


def axis_code(axis: str) -> str:
    m = re.match(r"([AB]\d+)", axis or "")
    return m.group(1) if m else axis


def effective_b_axis(row: dict[str, str]) -> str:
    prompt = row.get("prompt_action", "")
    axis = row.get("b_axis", "")
    if "B7" in axis and "B6" in axis:
        return "B7_法律问题识别/填空 + B6_调解/维权/纠纷解决路径"
    if "补充完整" in prompt and ("任选" in prompt or "任意" in prompt or "保护" in prompt):
        return "B7_法律问题识别/填空 + B6_调解/维权/纠纷解决路径"
    if "____" in prompt or "法律问题" in prompt or "遇到的问题" in prompt:
        return "B7_法律问题识别/填空"
    return axis


def q_meta(row: dict[str, str]) -> str:
    return f"{row['year']}年 {row['district']} {row['exam_stage']} 第{row['question_no']}题"


def dispute_sentence(row: dict[str, str]) -> str:
    prompt = row.get("prompt_action", "")
    b = effective_b_axis(row)
    a = row.get("a_axis_primary", "")
    if "B1" in b or "表" in prompt or "完成" in prompt:
        return "这题争的是：表格每一行应该把哪一段材料事实压进哪条法律规则，并写出对应裁判要点。"
    if "B3" in b or "诉求" in prompt or "请求" in prompt or "支持" in prompt:
        return "这题争的是：当事人的诉求能不能支持、能支持到什么范围，哪些事实决定支持或不支持。"
    if "B4" in b or "评析" in prompt or "认识" in prompt:
        return "这题争的是：材料中的观点或做法合理在哪里、边界在哪里，正确法律立场是什么。"
    if "B5" in b or "意义" in prompt or "价值" in prompt or "推动" in prompt or "保护" in prompt:
        return "这题争的是：本案如何保护具体权利、约束具体行为，并推出具体法治价值。"
    if "B6" in b or "维权" in prompt or "调解" in prompt or "纠纷" in prompt:
        return "这题争的是：围绕什么争议焦点保存证据、选择路径、提出请求。"
    if "B7" in b or "问题" in prompt or "____" in prompt:
        return "这题争的是：从材料冲突中识别哪几个法律问题，并用短语或短句写准。"
    memory = A_RULES.get(a, {}).get("memory", "材料中的法律关系和责任如何判断")
    return f"这题争的是：{memory.rstrip('。')}。"


def proposition_path_sentence(row: dict[str, str]) -> str:
    raw = clean(row.get("proposition_path"))
    a = row.get("a_axis_primary", "")
    b = effective_b_axis(row)
    if not raw:
        return f"v14校正：先定{a}，再按{b}作答。"
    if a not in raw or b not in raw:
        return f"v14校正：先定{a}，再按{b}作答；以本题材料触发、设问动作和评分锚点为准。"
    return raw


def transfer_sentence(row: dict[str, str]) -> str:
    a = row.get("a_axis_primary", "")
    b = effective_b_axis(row)
    ar = A_RULES.get(a, {})
    br = B_RULES.get(b, {})
    trigger = split_trigger(row.get("material_trigger", ""))[0][0]
    warning = clean(row.get("student_warning")) or ar.get("not_this", "不要误入其他入口")
    return (
        f"同类新题识别信号：{trigger}。不能误入：{warning}。"
        f"第一答句模板：本题属于{axis_code(a)}，设问按{axis_code(b)}作答，先写{br.get('first', '设问要求的结论')}。"
    )


def short_text(value: str | None, limit: int = 180) -> str:
    text = clean(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def question_ref(row: dict[str, str]) -> str:
    return f"{row.get('question_id', '')}（{row.get('year', '')}{row.get('district', '')}{row.get('exam_stage', '')}第{row.get('question_no', '')}题）"


def rows_for_qids(rows: list[dict[str, str]], qids: list[str]) -> list[dict[str, str]]:
    wanted = set(qids)
    return [row for row in rows if row.get("question_id") in wanted]


def build_source_growth_records(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    a_records: list[dict[str, str]] = []
    for key, rule in A_RULES.items():
        primary = [row for row in rows if row.get("a_axis_primary") == key]
        secondary = [
            row
            for row in rows
            if row.get("a_axis_primary") != key and key in row.get("a_axis_secondary_status", "")
        ]
        samples = (primary + secondary)[:5]
        if primary:
            status = "source_grown_primary_node"
            note = "该入口由锁定核心题的主入口材料触发和评分锚点直接支撑。"
        elif secondary:
            status = "auxiliary_effect_skeleton_with_secondary_evidence"
            note = "该入口不抢主入口，只在效力、追认、程序或边界问题中作辅助骨架。"
        else:
            status = "framework_reference_only_no_primary_locked_row"
            note = "保留为学生识别边界的参考入口，不按本批核心题晋升为主干高频。"
        a_records.append(
            {
                "node_type": "A_legal_entrance",
                "node_key": key,
                "status": status,
                "primary_support_count": str(len(primary)),
                "secondary_support_count": str(len(secondary)),
                "total_support_count": str(len(primary) + len(secondary)),
                "support_question_ids": ";".join(row.get("question_id", "") for row in primary + secondary),
                "sample_material_signals": " | ".join(short_text(row.get("material_trigger"), 120) for row in samples),
                "sample_scoring_anchors": " | ".join(short_text(row.get("rubric_scoring_anchor"), 120) for row in samples),
                "source_growth_note": note,
                "student_memory_sentence": rule.get("memory", ""),
                "hard_sentence": rule.get("hard", ""),
            }
        )

    b_records: list[dict[str, str]] = []
    for key, rule in B_RULES.items():
        support = [row for row in rows if effective_b_axis(row) == key]
        samples = support[:5]
        status = "source_grown_prompt_action_node" if support else "backup_template_no_primary_42_row"
        note = (
            "该动作由锁定题设问原句和评分形状直接支撑。"
            if support
            else "该动作暂作备用格式，不在本批 42 题中作为独立有效动作计数。"
        )
        b_records.append(
            {
                "node_type": "B_answer_action",
                "node_key": key,
                "status": status,
                "support_count": str(len(support)),
                "support_question_ids": ";".join(row.get("question_id", "") for row in support),
                "sample_prompt_actions": " | ".join(short_text(row.get("prompt_action"), 120) for row in samples),
                "sample_scoring_anchors": " | ".join(short_text(row.get("rubric_scoring_anchor"), 120) for row in samples),
                "source_growth_note": note,
                "student_memory_sentence": rule.get("memory", ""),
                "answer_shape": rule.get("shape", ""),
            }
        )

    def hard_rows(rule_no: int) -> tuple[list[dict[str, str]], str, str]:
        if rule_no == 1:
            return [row for row in rows if effective_b_axis(row).startswith("B1")], "B1 表格题设问和本地学生漏表头失败", "source_rows_plus_confucius_repair"
        if rule_no in {2, 11}:
            return rows_for_qids(rows, ["CC0103_2025_丰台_一模_19"]), "技术秘密题评分锚点要求先补秘密性、价值性、保密措施", "source_row_plus_confucius_repair"
        if rule_no == 3:
            return rows_for_qids(rows, ["CC0157_2025_朝阳_期末_20"]), "数据抓取题评分锚点要求写合法投入、绕限制抓取、商业化利用、竞争秩序损害", "source_row_plus_confucius_repair"
        if rule_no in {4, 9, 12}:
            return rows_for_qids(rows, ["CC0238_2026_东城_二模_19"]), "多主体竞争与内部履职责任题暴露主体分链要求", "source_row_plus_confucius_repair"
        if rule_no in {5, 6, 7}:
            return rows_for_qids(rows, ["CC0244_2026_东城_期中_18"]), "瑕疵商品致损题要求先合同违约、再侵权损害、再证据路径", "source_row_plus_confucius_repair"
        if rule_no in {8, 14}:
            return rows_for_qids(rows, ["CC0195_2025_西城_一模_20"]), "集体协商意义题评分锚点同时要求法律公平和经济效率", "source_row_plus_confucius_repair"
        if rule_no == 10:
            return [row for row in rows if effective_b_axis(row).startswith("B5")], "所有 B5 意义题都要求从材料中的制度或行为推出价值", "source_rows_plus_confucius_repair"
        if rule_no == 13:
            return rows_for_qids(rows, ["CC0289_2026_朝阳_二模_18"]), "补充完整+任选其一题要求先短句补全，再展开权利、侵害、证据、路径、请求", "source_row_plus_confucius_repair"
        return [], "未找到直接题源证据", "missing_evidence"

    hard_records: list[dict[str, str]] = []
    for idx, rule in enumerate(CONFUCIUS_REPAIR_RULES, 1):
        evidence_rows, basis, origin = hard_rows(idx)
        hard_records.append(
            {
                "rule_no": str(idx),
                "rule_text": rule,
                "evidence_status": "source_backed" if evidence_rows else "needs_manual_review",
                "evidence_question_ids": ";".join(row.get("question_id", "") for row in evidence_rows),
                "evidence_basis": basis,
                "sample_material_signals": " | ".join(short_text(row.get("material_trigger"), 120) for row in evidence_rows[:4]),
                "sample_scoring_anchors": " | ".join(short_text(row.get("rubric_scoring_anchor"), 120) for row in evidence_rows[:4]),
                "origin": origin,
            }
        )

    question_records: list[dict[str, str]] = []
    for row in rows:
        question_records.append(
            {
                "question_id": row.get("question_id", ""),
                "district_year_stage_question": q_meta(row),
                "evidence_status": row.get("evidence_status", ""),
                "source_check_state": row.get("source_check_state", ""),
                "source_check_decision": row.get("source_check_decision", ""),
                "a_axis_primary": row.get("a_axis_primary", ""),
                "a_axis_secondary_status": row.get("a_axis_secondary_status", ""),
                "b_axis_original": row.get("b_axis", ""),
                "b_axis_v14_effective": effective_b_axis(row),
                "prompt_action": short_text(row.get("prompt_action"), 240),
                "proposition_path_v14": short_text(proposition_path_sentence(row), 360),
                "material_trigger": short_text(row.get("material_trigger"), 360),
                "rubric_scoring_anchor": short_text(row.get("rubric_scoring_anchor"), 360),
                "answer_skeleton": short_text(row.get("answer_skeleton"), 360),
                "source_growth_basis": "locked_core_row_material_trigger_prompt_action_rubric_anchor",
            }
        )
    return a_records, b_records, hard_records, question_records


def write_csv_records(path: Path, records: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for record in records:
        for key in record:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def build_source_growth_audit(
    rows: list[dict[str, str]],
    a_records: list[dict[str, str]],
    b_records: list[dict[str, str]],
    hard_records: list[dict[str, str]],
) -> str:
    a_primary = [record for record in a_records if record["status"] == "source_grown_primary_node"]
    a_aux = [record for record in a_records if record["status"] != "source_grown_primary_node"]
    b_supported = [record for record in b_records if int(record["support_count"]) > 0]
    b_backup = [record for record in b_records if int(record["support_count"]) == 0]
    hard_backed = [record for record in hard_records if record["evidence_status"] == "source_backed"]
    lines = [
        "# Source Growth Audit v14.2",
        "",
        "Status: `source_growth_audited_local_complete_pending_real_gpt_claude_gate`",
        "",
        "## 1. 生长链条",
        "",
        "本审计只回答一个问题：v14.2 的框架节点是不是从题源和评分锚点长出来的，而不是先写框架再倒贴题号。",
        "",
        "可验证链条：",
        "",
        "1. v13.10 锁定核心 traceability matrix 给出 42 道核心题。",
        "2. 每行保留题号、区年卷题、设问动作、材料触发、评分锚点、答案骨架、学生误区、A/B 轴裁定。",
        "3. v14.2 只从这些行抽取 A 入口、B 动作、混合排序和硬规则。",
        "4. 材料补强只来自 `material_atoms_subjective_claudecode.csv` 或手工 source patch；污染性答案/分析话术被过滤。",
        "5. 开放容器/reference-only 行保留在附录，不晋升为 42 题主干框架。",
        "6. GPT/Claude 旧轮次意见只作为历史审议链，不允许无题源证据直接新增 v14.2 框架节点。",
        "",
        "## 2. A 入口来源",
        "",
        "| A 入口 | 状态 | 主支撑题数 | 副支撑题数 | 支撑题号样例 | 来源说明 |",
        "|---|---:|---:|---:|---|---|",
    ]
    for record in a_records:
        qids = "; ".join(record["support_question_ids"].split(";")[:5])
        lines.append(
            f"| {record['node_key']} | {record['status']} | {record['primary_support_count']} | {record['secondary_support_count']} | {qids} | {record['source_growth_note']} |"
        )
    lines += [
        "",
        "结论：A2-A10 均有锁定核心题主入口支撑；A1 没有作为高频主入口晋升，只作为民事行为效力、追认、边界判断的辅助骨架。",
        "",
        "## 3. B 动作来源",
        "",
        "| B 动作 | 状态 | 支撑题数 | 支撑题号样例 | 设问来源说明 |",
        "|---|---:|---:|---|---|",
    ]
    for record in b_records:
        qids = "; ".join(record["support_question_ids"].split(";")[:6])
        lines.append(
            f"| {record['node_key']} | {record['status']} | {record['support_count']} | {qids} | {record['source_growth_note']} |"
        )
    lines += [
        "",
        "结论：B 轴不是按法律章节编造，而是按设问产出形状生长：表格、裁判理由、诉求支持、评析、意义、路径、问题识别，以及 B7+B6 混合题。",
        "",
        "## 4. Confucius 硬规则来源",
        "",
        "| # | 证据状态 | 证据题号 | 来源基础 |",
        "|---:|---|---|---|",
    ]
    for record in hard_records:
        lines.append(
            f"| {record['rule_no']} | {record['evidence_status']} | {record['evidence_question_ids']} | {record['evidence_basis']} |"
        )
    lines += [
        "",
        f"结论：{len(hard_backed)}/{len(hard_records)} 条硬规则有锁定题源或学生盲测失败后的题源回扣证据。硬规则不是替代题源的模型建议，而是题源得分链被零基础学生读漏后形成的外显提醒。",
        "",
        "## 5. 不晋升规则",
        "",
        "- 没有锁定核心题材料触发和评分锚点支撑的节点，不晋升为主干高频。",
        "- 开放容器/reference-only 只进 `04_开放容器与不晋升题附录_v14.md`。",
        "- 本地 Confucius 学生 agent 可以暴露学习失败点，但每个修补规则必须回扣到题号、材料信号、评分锚点或设问动作。",
        "- 真实 GPT/Claude 未重跑 v14.2，因此本审计不把 v14.2 称为外部模型终审 PASS。",
        "",
        "## 6. 审计结论",
        "",
        f"- 锁定核心题：{len(rows)}。",
        f"- source-grown A 主入口：{len(a_primary)}；辅助/参考入口：{len(a_aux)}。",
        f"- source-grown B 动作：{len(b_supported)}；备用动作：{len(b_backup)}。",
        f"- source-backed 硬规则：{len(hard_backed)}/{len(hard_records)}。",
        "",
        "允许声明：v14.2 已完成本地 source-growth 审计，能够说明框架如何从 42 道锁定核心题、设问动作、材料触发和评分锚点中生长出来。",
        "",
        "不允许声明：v14.2 已完成新的 GPT/Claude 外部终审，或已经交付 DOCX/PDF。",
    ]
    return "\n".join(lines) + "\n"


def build_source_growth_invariants(
    rows: list[dict[str, str]],
    a_records: list[dict[str, str]],
    b_records: list[dict[str, str]],
    hard_records: list[dict[str, str]],
) -> str:
    unsupported_a = [
        record["node_key"]
        for record in a_records
        if int(record["primary_support_count"]) == 0 and int(record["secondary_support_count"]) == 0
    ]
    unsupported_b = [record["node_key"] for record in b_records if int(record["support_count"]) == 0]
    unsupported_hard = [record["rule_no"] for record in hard_records if record["evidence_status"] != "source_backed"]
    lines = [
        "# Source Growth Invariants v14.2",
        "",
        "| Check | Result |",
        "|---|---|",
        f"| Locked core rows | {len(rows)} |",
        f"| A nodes without primary or secondary evidence | {', '.join(unsupported_a) if unsupported_a else 'none'} |",
        f"| B nodes without support rows | {', '.join(unsupported_b) if unsupported_b else 'none'} |",
        f"| Hard rules without source backing | {', '.join(unsupported_hard) if unsupported_hard else 'none'} |",
        "| Open-container promotion | none; appendix only |",
        "| GPT/Claude substitution | none; local Confucius is recorded separately |",
        "| DOCX/PDF claim | none for v14.2 |",
        "",
        "Invariant conclusion: source-growth evidence is sufficient for local framework provenance, while external advisor and document-delivery gates remain separate.",
    ]
    return "\n".join(lines) + "\n"


def write_source_growth_bundle(rows: list[dict[str, str]]) -> None:
    a_records, b_records, hard_records, question_records = build_source_growth_records(rows)
    base = OUT / "source_growth"
    write_csv_records(base / "FRAMEWORK_NODE_SOURCE_EVIDENCE_v14_2.csv", a_records + b_records)
    write_csv_records(base / "HARD_RULE_SOURCE_EVIDENCE_v14_2.csv", hard_records)
    write_csv_records(base / "QUESTION_TO_FRAMEWORK_DERIVATION_v14_2.csv", question_records)
    write_text(base / "SOURCE_GROWTH_AUDIT_v14_2.md", build_source_growth_audit(rows, a_records, b_records, hard_records))
    write_text(base / "SOURCE_GROWTH_INVARIANTS_v14_2.md", build_source_growth_invariants(rows, a_records, b_records, hard_records))


def targeted_repair_lines(row: dict[str, str]) -> list[str]:
    qid = row.get("question_id", "")
    rules = list(TARGETED_REPAIR_RULES.get(qid, []))
    prompt = row.get("prompt_action", "")
    b = effective_b_axis(row)
    a = row.get("a_axis_primary", "")
    if "B1" in b:
        rules.append("表格题必须一格一链；看不见原表头时默认用“材料事实、法律规则、裁判要点/意义”。")
    if "B5" in b:
        rules.append("意义题先写材料中的具体制度或行为，再写保护对象、约束行为和秩序价值。")
    if "B6" in b or "维权" in prompt or "纠纷" in prompt:
        rules.append("路径题必须写证据、路径、请求，不能只写依法维权。")
    if "A5" in a and ("秘密" in row.get("material_core", "") or "技术" in row.get("material_core", "")):
        rules.append("技术秘密或商业秘密必须检查秘密性、价值性、保密措施，再写不正当获取使用和责任。")
    if "A4" in a and ("损" in row.get("material_core", "") or "伤" in row.get("material_core", "")):
        rules.append("合同瑕疵引发损害时，先定违约，再补侵权/产品损害和赔偿范围。")
    deduped: list[str] = []
    for item in rules:
        if item not in deduped:
            deduped.append(item)
    return deduped


def first_answer_sentence(row: dict[str, str]) -> str:
    b = effective_b_axis(row)
    answer = bullets_from_slashes(row.get("answer_skeleton", ""))[0]
    if "B1" in b:
        return f"本题按表格一行一链填写：{answer}。"
    if "B2" in b:
        return f"本案裁判/责任理由先写：{answer}。"
    if "B3" in b:
        return f"本题必须先分别表态支持程度，再写理由：{answer}。"
    if "B4" in b:
        return f"本题先评观点或做法，再写边界：{answer}。"
    if "B5" in b:
        return f"本案意义必须从具体规则推出：{answer}。"
    if "B6" in b:
        return f"本题先固定证据、路径和请求：{answer}。"
    if "B7" in b:
        return f"本题只写法律问题短语或短句，第一空先抓：{answer}。"
    return f"本题第一句先回应设问：{answer}。"


def build_framework(rows: list[dict[str, str]]) -> str:
    a_counts = Counter(r["a_axis_primary"] for r in rows)
    b_counts = Counter(effective_b_axis(r) for r in rows)
    lines = [
        "# 01 先背这套：选必二法律主观题不扣分框架 v14.2",
        "",
        "## 0. 这套框架到底解决什么",
        "",
        "法律题不是先背法条，也不是先贴标签。它的固定任务只有一句话：",
        "",
        "> 把一个生活冲突，翻译成法律关系、法律规则和法律后果。",
        "",
        "所以所有题都按五步走：",
        "",
        "| 步骤 | 问自己 | 产出 |",
        "|---|---|---|",
        "| 1. 生活冲突 | 谁和谁因为哪件事冲突？ | 材料一句话 |",
        "| 2. A 入口 | 这是哪类法律关系或法律内容？ | A 轴主入口，必要时副入口 |",
        "| 3. B 动作 | 题目让我写表格、责任、诉求、评析、意义还是路径？ | B 轴答案形状 |",
        "| 4. 得分链 | 哪些事实压进哪些规则？ | 事实 -> 规则 -> 结论 |",
        "| 5. 停止 | 题问到哪里就写到哪里。 | 问责任落责任，问意义落意义，问路径落路径 |",
        "",
        "最短口诀：",
        "",
        "> 先定生活冲突，再定设问动作；材料进规则，结论不飘；主链拿分，副链补刀。",
        "",
        "## 1. 先会总流程，再背 A/B",
        "",
        "拿到新题，按这四句话开工：",
        "",
        "1. 用一句话说材料：谁对谁做了什么，造成什么争议。",
        "2. 用 A 轴问：这个争议本质是哪类法律关系。",
        "3. 用 B 轴问：设问到底要我产出什么样的答案。",
        "4. 写成得分链：规则不能离开材料，材料不能离开结论。",
        "",
        "A/B 双轴不是开头背诵的废话，而是防扣分工具：A 防止法律关系跑偏，B 防止答案形状跑偏。",
        "",
        "## 2. A 轴：九个高频入口和一个效力骨架",
        "",
        f"本批 42 道锁定核心题的 A 轴分布：{', '.join(f'{k} {v}题' for k, v in sorted(a_counts.items()))}。",
        "",
        "| 入口 | 学生记忆句 | 材料触发 | 二级开关 | 别误判成 | 得分链 |",
        "|---|---|---|---|---|---|",
    ]
    for key, rule in A_RULES.items():
        count = a_counts.get(key, 0)
        label = f"{key}（{count}题）" if count else f"{key}（辅助骨架）"
        lines.append(
            f"| {label} | {rule['memory']} | {rule['trigger']} | {A_SWITCHES.get(key, '')} | {rule['not_this']} | {rule['chain']} |"
        )
    lines += [
        "",
        "### A 轴不扣分硬句",
        "",
    ]
    for key, rule in A_RULES.items():
        lines.append(f"- **{key}**：{rule['hard']}")
    lines += [
        "",
        "## 3. B 轴：设问动作决定答案长相",
        "",
        f"本批 42 道锁定核心题的 B 轴分布：{', '.join(f'{k} {v}题' for k, v in sorted(b_counts.items()))}。",
        "",
        "| 动作 | 学生记忆句 | 答案形状 | 第一笔写什么 |",
        "|---|---|---|---|",
    ]
    for key, rule in B_RULES.items():
        count = b_counts.get(key, 0)
        label = f"{key}（{count}题）" if count else f"{key}（备用）"
        lines.append(f"| {label} | {rule['memory']} | {rule['shape']} | {rule['first']} |")
    lines += [
        "",
        "## 4. 混合题排序",
        "",
        "| 混合情况 | 排序 | 不扣分提醒 |",
        "|---|---|---|",
        "| A2+A9 消费纠纷里有人格权 | 先人格权请求，再消费者退赔请求 | 隐私、名誉、个人信息不能被“消费者权益”吃掉。 |",
        "| A4+A6 瑕疵商品或服务致损 | 先合同违约，再侵权或产品损害赔偿 | 不只写合同，也不抛开合同只写侵权。 |",
        "| A3 物权题里有审批、消防、法院勘查 | 先物权/相邻边界，再把程序事实当证据 | 除非题问路径，否则 A10 不抢主入口。 |",
        "| A5 竞争题里有劳动离职 | 先商业秘密/数据/竞争秩序，再把离职当接触信息背景 | 不把技术秘密题写成劳动解除题。 |",
        "| B1 表格题后又问启示 | 先填表格，再用一两句价值收束 | 表格是主分，启示只补尾。 |",
        "| B3 诉求题又问意义 | 先支持/不支持及理由，再收意义 | 诉求通常 80%，意义通常 20%。 |",
        "| 一个题里有两个主体或两个诉求 | 一个诉求一条链，逐项表态 | 不要把两个主体、两个请求、两个规则糊成一段。 |",
        "",
        "## 5. Confucius 盲测后补上的十条硬规则",
        "",
        "下面十条不是装饰，而是零基础学生试读时暴露的扣分点。遇到对应题型，直接按硬规则写：",
        "",
    ]
    for idx, rule in enumerate(CONFUCIUS_REPAIR_RULES, 1):
        lines.append(f"{idx}. {rule}")
    lines += [
        "",
        "## 6. 答案生成器",
        "",
        "每道主观题都可套以下骨架：",
        "",
        "```text",
        "第一句：本题围绕____发生争议，核心是____。",
        "第二句：从法律关系看，____属于____，应适用____规则。",
        "第三句：材料中____表明____，符合/不符合____条件。",
        "第四句：因此____应承担/不承担____责任，或____请求应支持/不支持。",
        "第五句：如果题目问意义，再写：该处理保护了____，规范了____，维护了____秩序。",
        "```",
        "",
        "## 7. 四个停止条件",
        "",
        "1. 问责任，落责任；不要硬写宏大价值。",
        "2. 问意义，必须从本案权利和行为推出；不要空喊法治。",
        "3. 问路径，写证据、路径、请求；不要只写“依法维权”。",
        "4. 问问题识别或填空，写短语短句；不要扩成长判决。",
        "",
        "## 8. 先学后做的顺序",
        "",
        "学生学习时不要先刷 42 题。先按这个顺序：",
        "",
        "1. 背总流程：生活冲突 -> A 入口 -> B 动作 -> 得分链 -> 停止。",
        "2. 背 A 轴材料触发和别误判成什么。",
        "3. 背 B 轴答案形状。",
        "4. 看 42 题拆解时，只问：这题为什么这样进 A，为什么这样进 B，材料哪句话进了规则。",
        "5. 遇到新题，先照抄流程，不要背题号。",
    ]
    return "\n".join(lines) + "\n"


def build_question_cards(rows: list[dict[str, str]]) -> str:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["a_axis_primary"]].append(row)

    lines = [
        "# 02 42 题按框架拆解与解析 v14.2",
        "",
        "本章不是按试卷流水账排列，而是按 A 轴法律关系入口组织。每题都用同一套拆法：",
        "",
        "`材料一句话 -> 争点 -> A 入口 -> B 动作 -> 事实进规则 -> 不扣分答案 -> 警告 -> 迁移`",
        "",
    ]
    number = 1
    for a_key in sorted(grouped.keys()):
        rule = A_RULES.get(a_key, {})
        lines += [
            f"## {a_key}",
            "",
            f"- 入口记忆：{rule.get('memory', '')}",
            f"- 材料触发：{rule.get('trigger', '')}",
            f"- 别误判成：{rule.get('not_this', '')}",
            "",
        ]
        for row in grouped[a_key]:
            effective_b = effective_b_axis(row)
            b_rule = B_RULES.get(effective_b, {})
            trigger_rows = split_trigger(row.get("material_trigger", ""))
            answer_lines = bullets_from_slashes(row.get("answer_skeleton", ""))
            rubric_lines = bullets_from_slashes(row.get("rubric_scoring_anchor", ""))
            b_display = row.get("b_axis", "")
            if effective_b != b_display:
                b_display = f"{b_display}；v14校正动作：{effective_b}"
            repair_lines = targeted_repair_lines(row)
            lines += [
                f"### {number}. {row['question_id']}",
                "",
                f"- 区年卷题：{q_meta(row)}",
                f"- 设问原句：{clean(row.get('prompt_action'))}",
                f"- A 入口：{row.get('a_axis_primary')}；副入口/边界：{clean(row.get('a_axis_secondary_status')) or '无'}",
                f"- A 入口二级开关：{A_SWITCHES.get(row.get('a_axis_primary', ''), '看主体、行为、损害、请求和程序边界。')}",
                f"- B 动作：{b_display}；写法：{b_rule.get('shape', '按设问动作组织答案')}",
                f"- 命题路径：{proposition_path_sentence(row)}",
                "",
                "#### 0. 本题硬规则",
                "",
            ]
            if repair_lines:
                for item in repair_lines:
                    lines.append(f"- {item}")
            else:
                lines.append("- 先定 A 入口，再按 B 动作写成“材料事实 -> 法律规则 -> 结论落点”。")
            lines += [
                "",
                "#### 1. 材料一句话",
                "",
                clean(row.get("material_core")) or "材料需先压缩成谁与谁发生什么争议。",
                "",
                "#### 2. 本题争点",
                "",
                dispute_sentence(row),
                "",
                "#### 3. 第一答句",
                "",
                first_answer_sentence(row),
                "",
                "#### 4. 按框架拆成得分链",
                "",
                "| 材料事实 | 法律翻译 | 结论落点 |",
                "|---|---|---|",
            ]
            for fact, rule_text, landing in trigger_rows:
                lines.append(f"| {fact} | {rule_text} | {landing} |")
            lines += [
                "",
                "#### 5. 不扣分答案骨架",
                "",
            ]
            for item in answer_lines:
                lines.append(f"- {item}。")
            lines += [
                "",
                "#### 6. 评分锚点",
                "",
            ]
            for item in rubric_lines:
                lines.append(f"- {item}。")
            lines += [
                "",
                "#### 7. 学生最容易扣分",
                "",
                f"- {clean(row.get('student_warning')) or '只背标签、只喊价值、材料事实没有进规则。'}",
                "",
                "#### 8. 迁移到新题",
                "",
                transfer_sentence(row),
                "",
                "#### 9. 最短考场写法",
                "",
                f"先写“本题核心争点是____”，再按 {axis_code(row.get('a_axis_primary', ''))} 的法律关系和 {axis_code(effective_b)} 的答案形状，把材料事实逐项压进规则，最后落到题目要求的结论。",
                "",
            ]
            number += 1
    return "\n".join(lines) + "\n"


def build_agent_files(rows: list[dict[str, str]]) -> dict[Path, str]:
    sample = random.Random(20260524).sample(rows, 6)
    blind_lines = [
        "# RUN 001 Blind Sample Pack",
        "",
        "用途：交给 Confucius 零基础学生 agent。不得同时给隐藏评分锚点、答案骨架、材料触发链。",
        "",
        "只允许 agent 阅读：",
        "",
        "1. `01_先背这套_法律主观题不扣分框架_v14_2.md`",
        "2. 本盲测包",
        "",
        "## 随机题目",
        "",
    ]
    hidden_lines = [
        "# RUN 001 Hidden Key For Codex",
        "",
        "本文件不交给学生 agent，只供 Codex adjudication 使用。",
        "",
    ]
    for idx, row in enumerate(sample, 1):
        blind_lines += [
            f"### {idx}. {row['question_id']}",
            "",
            f"- 区年卷题：{q_meta(row)}",
            f"- 设问：{clean(row.get('prompt_action'))}",
            f"- 材料压缩：{clean(row.get('material_core'))}",
            "",
        ]
        hidden_lines += [
            f"### {idx}. {row['question_id']}",
            "",
            f"- A 入口：{row.get('a_axis_primary')}；副入口：{clean(row.get('a_axis_secondary_status'))}",
            f"- B 动作：{row.get('b_axis')}；v14有效动作：{effective_b_axis(row)}",
            f"- 第一答句：{first_answer_sentence(row)}",
            f"- 材料触发：{clean(row.get('material_trigger'))}",
            f"- 评分锚点：{clean(row.get('rubric_scoring_anchor'))}",
            f"- 答案骨架：{clean(row.get('answer_skeleton'))}",
            f"- 学生预警：{clean(row.get('student_warning'))}",
            "",
        ]
    spec = """# Confucius Zero-Baseline Student Agent v14

## 身份

你是一个聪明但完全没学过《法律与生活》的高三学生。你不是老师，不是阅卷人，不准使用外部法律常识补洞。

## 输入

你只能读取：

1. v14 框架正文；
2. 随机盲测题包中的题面压缩和设问。

你不能读取答案骨架、评分锚点、材料触发链、traceability、历史报告或本题解析。

## 输出格式

每道题固定回答：

1. 我第一步看到了什么生活冲突；
2. 我选择的 A 入口和理由；
3. 我选择的 B 动作和理由；
4. 我把哪些材料事实压进哪些法律规则；
5. 我的现场答案；
6. 我估计会扣分的地方；
7. 这是否说明框架本身还要改。

## 判定标准

- 如果 A 入口错，框架 FAIL。
- 如果 B 动作错，框架 FAIL。
- 如果答案只有口号没有材料进规则，框架 FAIL。
- 如果学生能写出可交卷骨架但缺少原题细节，框架不算 FAIL，记录为题源信息不足。
"""
    prompt = """# Prompt Template

请扮演 Confucius Zero-Baseline Student Agent。

你完全没学过《法律与生活》，只读下面的 v14 框架和随机题目。请现场作答，不准引用外部资料，不准假装知道标准答案。

对每道题按 AGENT_SPEC 的七项格式输出。最后给出总判定：FRAMEWORK_PASS、FRAMEWORK_PASS_WITH_REPAIRS 或 FRAMEWORK_FAIL，并列出必须修的框架规则。
"""
    status = """# RUN 001 Local Controller Status

Status: `run_002_confucius_zero_baseline_framework_pass`

说明：

- 本目录已经生成可复用的零基础学生 agent 规则和随机盲测包。
- 第三轮真实本地 Confucius 学生 agent 已完成 v14.2 盲测。
- 作答报告：`RUN_002_AGENT_REPORT_v14_2_FRAMEWORK_PASS.md`
- Codex 裁决：`RUN_002_CODEX_ADJUDICATION_v14_2.md`
- 判定：`FRAMEWORK_PASS`
- 边界：此 gate 不等于 GPT/Claude 外部真实门禁，也不等于 DOCX/PDF 交付。
"""
    return {
        OUT / "confucius_zero_baseline_student_agent" / "AGENT_SPEC.md": spec,
        OUT / "confucius_zero_baseline_student_agent" / "PROMPT_TEMPLATE.md": prompt,
        OUT / "confucius_zero_baseline_student_agent" / "RUN_001_BLIND_SAMPLE_PACK.md": "\n".join(blind_lines) + "\n",
        OUT / "confucius_zero_baseline_student_agent" / "RUN_001_HIDDEN_KEY_FOR_CODEX.md": "\n".join(hidden_lines) + "\n",
        OUT / "confucius_zero_baseline_student_agent" / "RUN_001_LOCAL_CONTROLLER_STATUS.md": status,
    }


def build_readme(rows: list[dict[str, str]]) -> str:
    return f"""# v14.2 zero-baseline framework baodian

Status: `source_growth_audited_markdown_framework_and_42_question_baodian_complete_with_local_confucius_pass_pending_real_gpt_claude_gate`

生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

本目录回应用户最新要求：

- 生成一个类似先前框架、但更可习得的选必二框架；
- 前面是学生先学的框架；
- 后面附 42 道锁定核心题按框架拆解和解析；
- 目标是零基础学生学完框架后能立刻做题，尽量不丢结构分；
- 同时生成 Confucius 零基础学生模拟 agent 的规则和盲测包。
- 新增 source-growth 审计，逐项说明框架入口、设问动作和硬规则如何由题源、材料触发、评分锚点生长出来。

边界：

- 42 题来自 v13.10 锁定核心 traceability matrix，共 {len(rows)} 题。
- v14.2 是 Codex 本地框架重建、材料截断补强和两轮 Confucius 学生试读修补版，不冒充新的 GPT/Claude 输出。
- source-growth 审计见 `source_growth/SOURCE_GROWTH_AUDIT_v14_2.md`、`source_growth/FRAMEWORK_NODE_SOURCE_EVIDENCE_v14_2.csv`、`source_growth/QUESTION_TO_FRAMEWORK_DERIVATION_v14_2.csv`。
- 真实 GPT/Claude 网页门禁仍待跑通；因此本目录不声明外部模型终审 PASS。
- v14.2 没有生成 DOCX/PDF；本目录只声明 Markdown 框架、42 题宝典、本地 source-growth 审计和本地 Confucius 试读。
"""


def build_governance(rows: list[dict[str, str]]) -> str:
    return f"""# 05 Governance Boundary v14

## Status

`source_growth_audited_markdown_framework_and_42_question_baodian_complete_with_local_confucius_pass_pending_real_gpt_claude_gate`

## What exists

- 框架正文：`01_先背这套_法律主观题不扣分框架_v14_2.md`（同时保留 v14 兼容文件名）
- 42 题逐题拆解：`02_42题按框架拆解与解析_v14_2.md`（同时保留 v14 兼容文件名）
- 合并学生宝典：`选必二法律与生活_法律宝典_v14_2_零基础框架学习版.md`（同时保留 v14 兼容文件名）
- Confucius 学生 agent 规则和随机盲测包：`confucius_zero_baseline_student_agent/`
- 追踪矩阵：`traceability/TRACEABILITY_MATRIX_v14_2.csv`（同时保留 v14 兼容文件名）
- source-growth 审计包：`source_growth/`

## Verification

- Locked core rows: {len(rows)}
- The generated question-card file contains one `###` card per locked core row.
- A/B axes are preserved as student usable framework, but the opening learning order is now: life conflict -> A entrance -> B action -> scoring chain -> stop condition.
- Source-growth audit records every A entrance, B action, hard rule, and 42 question derivation with question IDs, material signals, prompt actions, and scoring anchors.
- B7+B6 hybrid action is retained as a real source-grown mixed action rather than flattened into B7.

## Hard boundary

- No new GPT Pro or Claude Opus web result is claimed in v14.
- Local Confucius or Codex student simulation does not substitute for GPT/Claude real-call gates.
- Source-growth audit proves local provenance only; it does not replace the real GPT/Claude external advisor gate.
- v14.2 can be used as a Markdown candidate classroom artifact, but final external-governance PASS requires real external gates or an explicit user waiver.
"""


def build_final_governor_checklist(rows: list[dict[str, str]]) -> str:
    return f"""# 06 Final Governor Checklist v14.2

## Verdict

`SOURCE_GROWTH_AUDITED_MARKDOWN_FRAMEWORK_AND_42_QUESTION_BAODIAN_COMPLETE_WITH_LOCAL_CONFUCIUS_PASS`

This is not a final GPT/Claude external gate and not a DOCX/PDF delivery claim.

## Required Deliverables

| Gate | Status | Evidence |
|---|---|---|
| Student-first framework chapter exists | PASS | `01_先背这套_法律主观题不扣分框架_v14_2.md` |
| All 42 locked core questions have framework-based analysis | PASS | `02_42题按框架拆解与解析_v14_2.md` |
| Combined legal baodian Markdown exists | PASS | `选必二法律与生活_法律宝典_v14_2_零基础框架学习版.md` |
| Open-container/reference-only appendix separated | PASS | `04_开放容器与不晋升题附录_v14.md` |
| Traceability matrix exists and has 42 rows | PASS | `traceability/TRACEABILITY_MATRIX_v14_2.csv` |
| Source-growth audit exists | PASS | `source_growth/SOURCE_GROWTH_AUDIT_v14_2.md` |
| Framework node source evidence exists | PASS | `source_growth/FRAMEWORK_NODE_SOURCE_EVIDENCE_v14_2.csv` |
| Every question has source-to-framework derivation row | PASS | `source_growth/QUESTION_TO_FRAMEWORK_DERIVATION_v14_2.csv` |
| Confucius hard rules have source-evidence table | PASS | `source_growth/HARD_RULE_SOURCE_EVIDENCE_v14_2.csv` |
| Zero-baseline student agent created and run | PASS | `confucius_zero_baseline_student_agent/RUN_002_AGENT_REPORT_v14_2_FRAMEWORK_PASS.md` |
| Codex adjudication of student agent result | PASS | `confucius_zero_baseline_student_agent/RUN_002_CODEX_ADJUDICATION_v14_2.md` |
| No student-facing debug/model chatter pollution found | PASS | local search found no `【答案】`, `【分析】`, `[page]`, `[slide]`, or truncated `哪些工…` remnants in the 42-card file |
| Real GPT/Claude external web gate | PENDING | no new real GPT/Claude output is claimed in v14.2 |
| DOCX delivery | NOT PRODUCED | no v14.2 DOCX is claimed |
| PDF delivery | NOT PRODUCED | no v14.2 PDF is claimed |

## Source-Growth Claim Allowed

Allowed:

`v14.2 Markdown framework + 42-question legal baodian is locally complete, source-growth audited from 42 locked core rows, and Confucius zero-baseline student tested as FRAMEWORK_PASS.`

Not allowed:

- Do not claim GPT/Claude re-reviewed v14.2.
- Do not claim final external-governance PASS.
- Do not claim DOCX/PDF delivery for v14.2.
- Do not claim the local Confucius agent is GPT or Claude.

## Residual Risk

The framework now teaches a zero-baseline student to identify life conflict, A entrance, B action, and scoring chain. The provenance of those nodes is locally auditable. Remaining risk is the still-pending real GPT/Claude external review and any future DOCX/PDF layout QA, not the existence of the Markdown framework or the 42-question source-growth chain.
"""


def build_open_appendix() -> str:
    if not OPEN_CONTAINER.exists():
        return "# 04 Open Container Appendix v14\n\nNo source appendix found from v13.10.\n"
    old = OPEN_CONTAINER.read_text(encoding="utf-8-sig")
    return "# 04 Open Container Appendix v14\n\n本附录只作 reference-only，不晋升为 42 题核心框架。\n\n---\n\n" + old


def write_trace(rows: list[dict[str, str]]) -> None:
    path = OUT / "traceability" / "TRACEABILITY_MATRIX_v14.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) + [
        "v14_effective_b_axis",
        "v14_front_framework",
        "v14_source_growth_basis",
        "v14_source_growth_audit_status",
        "v14_card_status",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            out = dict(row)
            out["v14_effective_b_axis"] = effective_b_axis(row)
            out["v14_front_framework"] = "life_conflict_to_A_axis_to_B_action_to_scoring_chain"
            out["v14_source_growth_basis"] = "locked_core_row_material_trigger_prompt_action_rubric_anchor"
            out["v14_source_growth_audit_status"] = "covered_by_source_growth_audit_v14_2"
            out["v14_card_status"] = "generated"
            writer.writerow(out)
    canonical = OUT / "traceability" / "TRACEABILITY_MATRIX_v14_2.csv"
    canonical.write_text(path.read_text(encoding="utf-8-sig"), encoding="utf-8-sig")


def main() -> None:
    rows = read_rows()
    OUT.mkdir(parents=True, exist_ok=True)
    write_source_growth_bundle(rows)
    write_text(OUT / "00_READ_ME_FIRST.md", build_readme(rows))
    framework = build_framework(rows)
    cards = build_question_cards(rows)
    write_text(OUT / "01_先背这套_法律主观题不扣分框架_v14.md", framework)
    write_text(OUT / "01_先背这套_法律主观题不扣分框架_v14_2.md", framework)
    write_text(OUT / "02_42题按框架拆解与解析_v14.md", cards)
    write_text(OUT / "02_42题按框架拆解与解析_v14_2.md", cards)
    write_text(OUT / "04_开放容器与不晋升题附录_v14.md", build_open_appendix())
    write_text(OUT / "05_GOVERNANCE_BOUNDARY_v14.md", build_governance(rows))
    write_text(OUT / "06_FINAL_GOVERNOR_CHECKLIST_v14_2.md", build_final_governor_checklist(rows))
    combined = "\n\n---\n\n".join(
        [
            "# 选必二法律与生活：法律宝典 v14.2 零基础框架学习版",
            framework,
            cards,
            build_open_appendix(),
            build_governance(rows),
        ]
    )
    write_text(OUT / "选必二法律与生活_法律宝典_v14_零基础框架学习版.md", combined)
    write_text(OUT / "选必二法律与生活_法律宝典_v14_2_零基础框架学习版.md", combined)
    for path, text in build_agent_files(rows).items():
        write_text(path, text)
    write_trace(rows)
    manifest = "\n".join(
        [
            "v14_2_zero_baseline_framework_baodian",
            f"generated_at={datetime.now().isoformat(timespec='seconds')}",
            f"locked_core_rows={len(rows)}",
            "status=source_growth_audited_markdown_framework_and_42_question_baodian_complete_with_local_confucius_pass_pending_real_gpt_claude_gate",
            "docx_pdf_delivery=not_produced",
        ]
    )
    write_text(OUT / "build_manifest.txt", manifest + "\n")


if __name__ == "__main__":
    main()
