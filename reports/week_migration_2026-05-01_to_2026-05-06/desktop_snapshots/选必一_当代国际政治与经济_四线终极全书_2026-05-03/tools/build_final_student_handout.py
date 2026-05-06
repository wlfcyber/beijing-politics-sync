#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


RUN = Path("/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03")
ATOMS_CSV = RUN / "fusion" / "all_scoring_atoms_combined_20260504.csv"
CLUSTERS_CSV = RUN / "fusion" / "six_bucket_core_clusters_20260504.csv"
PROMPTS_CSV = RUN / "fusion" / "prompt_map_20260504.csv"
OUT_MD = RUN / "09_delivery" / "选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md"
OUT_FREQ = RUN / "09_delivery" / "选必一_核心点频次统计_最终闭环版_20260504.csv"
OUT_TEACHER = RUN / "09_delivery" / "选必一_教师核查索引_最终闭环版_20260504.csv"
OUT_RUBRIC_REPAIR = RUN / "08_review" / "role_reviews" / "all_question_rubric_point_repair_matrix_20260504.csv"

BUCKETS = ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"]
BUCKET_ORDER = {b: i for i, b in enumerate(BUCKETS)}
DISTRICT_ORDER = {
    "海淀": 0,
    "西城": 1,
    "东城": 2,
    "朝阳": 3,
    "丰台": 4,
    "石景山": 5,
    "通州": 6,
    "顺义": 7,
    "门头沟": 8,
    "房山": 9,
    "昌平": 10,
    "延庆": 11,
}

MAIN_STATUSES = {
    "candidate_with_fixes",
    "candidate_with_guard",
    "candidate_with_boundary_guard",
    "candidate_with_fixes_boundary_guard",
    "candidate_p2_guard",
}
SIDE_STATUSES = {
    "boundary_only",
    "reference_only",
    "excluded_boundary_subpoint",
    "result_expression_only",
}

PUBLIC_REPLACEMENTS = {
    "参考答案": "答案提示",
    "评分参考": "答案提示",
    "评分标准": "作答标准",
    "替代表述": "可换写法",
    "同槽": "同一层",
    "不并入": "不放入",
    "评分细则": "答案口径",
    "评标": "答案口径",
    "阅卷细则": "答案口径",
    "阅卷总结": "答案口径",
    "答案口径要求": "作答时要",
    "答案口径在": "作答时在",
    "答案口径": "作答方向",
    "采分点": "答题点",
    "采分": "答题",
    "赋分": "作答层次",
    "分值": "作答层次",
    "得分": "作答",
    "经济全球化正确方向": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
    "共商共建共享全球治理观": "共商共建共享的全球治理观",
    "PPTX": "",
    "DOCX": "",
    "PDF": "",
    "HMC": "人类命运共同体",
    "candidate": "",
    "guard": "",
    "boundary": "",
    "要落到": "要写成",
    "可从": "可以按",
}

PROMPT_OVERRIDES = {
    "2024朝阳二模 Q20": "结合研讨背景，运用《当代国际政治与经济》知识，完成下表：完善全球气候治理应遵循的基本原则；概括本次研讨各方达成的共识。",
    "2026朝阳期末 Q20": "结合材料，运用《当代国际政治与经济》知识，说明如何通过开展中国特色大国外交为推进中国式现代化营造良好外部环境。",
    "2025东城期末 Q20": "运用《当代国际政治与经济》知识，写一篇短文，谈谈你对我国新能源汽车出口与欧盟反补贴税争议的认识。",
    "2026海淀期中 Q22": "运用《当代国际政治与经济》知识，说明全球治理倡议为什么能获得国际社会广泛认同。",
    "2025海淀一模 Q21(2)": "结合材料，运用《当代国际政治与经济》知识，说明我国外贸为何能连上两个万亿级台阶。",
    "2024海淀二模 Q18(1)": "任选一个议题，参考资料包中的内容，运用《当代国际政治与经济》知识，围绕所选议题写一篇时政述评。",
    "2025西城一模 Q18": "结合材料，运用《经济与社会》所学，谈谈中国经济增长新空间是如何拓展的。",
    "2026东城一模 Q19(3)": "结合材料二，运用《当代国际政治与经济》知识，分析在推动未来产业中，北京是如何统筹高水平对外开放与提升产业链韧性之间关系的。",
}

QUESTION_TRIGGER_OVERRIDES = {
    "2024朝阳二模 Q20": "本题是全球气候治理填表题，先填基本原则，再写研讨共识；答案只围绕气候治理，不写成产业链供应链题。",
    "2026朝阳期末 Q20": "本题问中国特色大国外交怎样营造外部环境，按和平发展背景、政治格局、经济全球化、国家利益四层展开。",
    "2025东城期末 Q20": "本题是认识类短文：先说明中国新能源汽车对世界市场的贡献，再批判欧盟贸易保护主义，最后写中国维护利益与互利共赢的应对。",
    "2025海淀期中 Q16(2)": "本题只收本册的国际经济规则层：企业先做市场与合规，行业组织提供风险和法律支持，政府再运用国际规则与治理机制。",
    "2024海淀期中 Q16(2)": "本题只收本册的国际经济规则层：企业先做市场与合规，行业组织提供风险和法律支持，政府再运用国际规则与治理机制。",
    "2026西城期末 Q20": "本题是全球气候治理题，答案分成共同利益、全球治理框架、中国行动三层；同一组理念不要一口气堆成一句。",
    "2026东城期末 Q20": "本题不是只写人类命运共同体，要把四大全球倡议分别写成发展、安全、文明、治理四条路径，再用人类命运共同体总收束。",
    "2024东城二模 Q20": "本题按三大倡议分层：发展倡议写发展合作，安全倡议写和平解决争端和联合国宪章，文明倡议写交流互鉴，最后再收束到美好未来。",
    "2024东城一模 Q20": "本题主属经济相关知识，放入主线只是因为本册可提取制度型开放、经济全球化和两个市场两种资源等辅助链；不要把它当作纯选必一固定模板。",
    "2026延庆一模 Q19(2)": "本题问理论逻辑和价值意蕴：共同利益解释为什么能合作，正确义利观解释中国怎样合作，人类命运共同体只放在结果层收束。",
    "2025房山一模 Q18(2)": "本题要把开源战略写成技术发展与全球合作的结合：先说明中国维护自身人工智能技术发展和安全利益，再说明兼顾国际社会开放合作、技术共享和人工智能治理的合理关切。本题不要再额外加共商共建共享或人类命运共同体作冗余收束，“全球合作新模式”落到兼顾国际社会合理关切即可。",
    "2026海淀一模 Q20": "本题按颜色细则分三层：对我国写制度型开放、两个市场两种资源、双循环和竞争力；对世界经济写开放包容普惠平衡共赢、国际合作、资源优化配置和低碳能源人工智能领域的标准共通、技术共享；对全球治理写参与全球经济治理和规则制定、治理体制公正合理、话语权、国际影响力和国际经济新秩序。",
}

QUESTION_FORCE_MAIN = {
    "2024东城一模 Q20",
}

ATOM_CORE_OVERRIDES = {
    "ATOM-B12": ("理论", "处理好发展和安全的关系；统筹发展和安全"),
    "ATOM-YQ26-01": ("理论", "国家间共同利益是国家合作的基础"),
    "ATOM-XC15": ("理论", "当前国际竞争的实质是以经济和科技实力为基础的综合国力较量"),
    "ATOM-DC12": ("理论", "国家间共同利益是国家合作的基础"),
    "ATOM-CY02": ("理论", "国家间共同利益是国家合作的基础"),
    "ATOM-D01": ("中国", "中国作为负责任大国积极参与全球气候治理"),
    "ATOM-D03": ("时代背景", "和平与发展仍是时代主题"),
    "ATOM-D08": ("联合国", "在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善"),
}

QUESTION_CORE_DISPLAY_OVERRIDES = {
    ("2026西城期末 Q20", "维护联合国在国际事务中的核心作用，完善全球治理体系"):
        "在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善",
    ("2026海淀一模 Q20", "充分利用国内国际两个市场、两种资源，增强国内国际循环联动"):
        "扩大制度型开放；更好利用国内国际两个市场、两种资源，增强国内国际循环联动",
    ("2026海淀一模 Q20", "建设开放型世界经济，参与全球经济治理和规则制定"):
        "参与全球经济治理和规则制定；推进制度型开放与国际标准规则共通",
}

QUESTION_HEADER_NOTES = {
    "2024东城一模 Q20": "【混合模块题：主属经济模块，选必一为辅】本题保留在主线，是为了积累制度型开放、经济全球化和两个市场两种资源等本册可迁移链条。",
}

CORE_INDEX_NOTES = {
    "建设开放型世界经济，参与全球经济治理和规则制定": "（含制度型开放 / 对标国际规则、规制、管理和标准）",
    "充分利用国内国际两个市场、两种资源，增强国内国际循环联动": "（2026海淀一模等题会写成“扩大制度型开放 + 两个市场两种资源”）",
    "提升贸易投资合作质量和水平": "（仅由混合经济主属题命中，作选必一辅助链慎用）",
    "霸权主义、强权政治、单边主义、零和博弈": "（作时代背景/旧逻辑识别；写回应时转到国际关系民主化、真正多边主义和公正合理国际秩序）",
}

MANUAL_CORE_OVERLAYS = {
    ("时代背景", "霸权主义、强权政治、单边主义、零和博弈"): {
        "source_questions": "2024西城二模 Q19；2026朝阳期末 Q20；2025朝阳期末 Q21",
        "expression_accumulation": "霸权主义；强权政治；单边主义；霸权强权；零和博弈；实力至上逻辑；集团政治小圈子规则；封闭排他；强权霸凌；单边霸凌；发展鸿沟；安全赤字；旧式国际关系逻辑。",
        "question_count": "3",
        "atom_count": "3",
        "distinct_source_count": "3",
    },
}

QUESTION_CORE_SUBPATHS = {
    ("2026东城期末 Q20", "推动构建人类命运共同体"): "全球安全倡议写和平与安全，全球文明倡议写交流互鉴，全球治理倡议写公平治理；人类命运共同体是总目标，不替代四条路径。",
    ("2024东城二模 Q20", "推动构建人类命运共同体"): "全球发展倡议写发展合作和共同繁荣，全球文明倡议写交流互鉴和开放包容；全球安全倡议另在联合国宪章条目中展开。",
    ("2026延庆一模 Q19(2)", "国家间共同利益是国家合作的基础"): "共同利益解释绿色能源合作为什么能成立，正确义利观解释中国在合作中怎样兼顾道义和合理利益。",
}

CORE_REMOVES = {
    "共商共建共享的全球治理观": (
        "人类命运共同体",
        "正确义利观",
        "全人类共同价值",
        "真正的多边主义",
        "新型国际关系",
        "共同利益",
        "全球发展倡议",
        "全球气候治理体系",
    ),
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": (
        "中国智慧",
        "中国方案",
        "人类命运共同体",
        "正确义利观",
        "全人类共同价值",
        "全球治理变革",
        "和平共处五项原则",
    ),
    "维护国家利益并兼顾他国合理关切，坚持正确义利观": (
        "联合国",
        "人类命运共同体",
        "和平与发展",
        "全球治理",
    ),
}

CORE_FORCE = {
    "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展": [
        "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "开放、包容、普惠、平衡、共赢",
        "让发展成果更普惠、更平衡、更共赢",
        "让经济全球化更具活力",
        "惠及全体人民",
    ],
    "国际发展合作、南南合作与“小而美”项目": [
        "国际发展合作、南南合作与“小而美”项目",
        "坚持正确义利观",
        "改善发展中国家民生",
        "增强全球发展内生动力",
        "共享发展新机遇",
        "小而美、惠民生、可持续",
    ],
    "处理好发展和安全的关系；统筹发展和安全": [
        "处理好发展和安全的关系",
        "统筹发展和安全",
        "总体国家安全观",
        "底线思维",
        "维护国家经济安全、科技安全",
        "在释放发展动能的同时防范数据安全、模型缺陷、伦理失控等风险",
    ],
    "和平与发展仍是时代主题": [
        "和平与发展仍是时代主题",
        "顺应和平与发展的世界大势",
        "中国做法符合和平与发展时代主题",
        "各国人民渴望和平稳定和共同发展",
        "回应治理赤字和共同挑战",
    ],
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": [
        "推动建设相互尊重、公平正义、合作共赢的新型国际关系",
        "合作共赢的新型国际关系",
        "互利共赢",
        "共享发展成果",
    ],
    "建设开放型世界经济，参与全球经济治理和规则制定": [
        "建设开放型世界经济",
        "参与全球经济治理和规则制定",
        "推进制度型开放",
        "对标国际规则、规制、管理和标准",
        "提升国际技术标准和贸易规则制定话语权",
        "依法运用国际规则和争端解决机制",
    ],
    "全球治理应坚持开放、合作、共享、共赢、包容和共商共建": [
        "全球治理应坚持开放、合作、共享、共赢、包容和共商共建",
        "在共商共建中求同存异",
        "开放合作而不是封闭对抗",
        "共享共赢而不是零和博弈",
    ],
    "霸权主义、强权政治、单边主义、零和博弈": [
        "霸权主义",
        "强权政治",
        "单边主义",
        "霸权强权",
        "零和博弈",
        "实力至上逻辑",
        "集团政治小圈子规则",
        "封闭排他",
        "强权霸凌",
        "单边霸凌",
        "发展鸿沟",
        "安全赤字",
    ],
    "推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展": [
        "推动国际关系民主化",
        "坚持真正的多边主义",
        "推动国际秩序朝公正合理方向发展",
        "推动构建国际新秩序",
        "推动构建更加公正合理的国际新秩序",
        "反对霸权主义、强权政治",
        "反霸权主义",
        "反强权政治",
        "反对单边主义",
        "反对霸权强权",
        "维护国际公平正义",
        "发展中国家代表性和话语权",
        "赋予发展中国家更多发言权",
    ],
    "核心技术自主可控；把握创新主动权": [
        "核心技术自主可控",
        "把握创新主动权",
        "自主研发",
        "核心竞争力",
        "把核心技术掌握在自己手里",
        "不受制于人",
    ],
    "共商共建共享的全球治理观": [
        "共商共建共享的全球治理观",
        "共同商量、共同建设、共同分享",
        "各国平等参与全球治理",
        "建立公平合理的全球治理体系",
    ],
    "推动构建人类命运共同体": [
        "推动构建人类命运共同体",
        "人类命运共同体理念",
        "建设持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界",
        "四大全球倡议围绕发展、安全、文明、治理系统发力",
        "同球共济",
        "命运与共",
        "周边命运共同体",
        "中非命运共同体",
        "把中国发展同世界共同发展联系起来",
    ],
    "坚持正确义利观，在发展合作中义利相兼、互利共赢": [
        "坚持正确义利观",
        "义利相兼、互利共赢",
        "兼顾他国合理关切",
        "在国际合作中既讲共同利益又重国际道义",
    ],
    "中国特色大国外交、独立自主和平外交政策与周边命运共同体": [
        "中国特色大国外交",
        "习近平外交思想",
        "独立自主和平外交政策",
        "维护世界和平、促进共同发展",
        "和平共处五项原则",
        "主权、安全、发展利益",
        "周边命运共同体",
        "新中国外交始终服务于我国人民民主专政的国家性质",
    ],
    "以联合国为核心的国际体系、联合国作用与中国的联合国身份": [
        "以联合国为核心的国际体系、联合国作用与中国的联合国身份",
        "最具普遍性、代表性和权威性的政府间国际组织",
        "集体安全机制核心",
        "实践多边主义最佳场所",
        "和平与安全、发展、人权三大支柱",
        "中国作为联合国创始会员国和安理会常任理事国",
    ],
    "中国作为负责任大国积极参与全球气候治理": [
        "中国作为负责任大国积极参与全球气候治理",
        "积极履行气候治理国际责任",
        "提交NDC行动目标",
        "支持多边气候治理机制",
        "推动绿色低碳转型",
    ],
    "中国作为负责任大国积极参与全球治理并推动全球南方现代化": [
        "中国以最大发展中国家身份积极参与全球治理",
        "推动全球南方现代化",
        "国际政治经济格局中的重要力量",
        "负责任大国",
        "发挥建设性作用",
    ],
}

PLAIN_NOTES = {
    "和平与发展仍是时代主题": "看到合作、倡议、中国方案为什么有现实必要，先判断是不是在问当今世界大背景。",
    "全球性挑战、逆全球化、保护主义和治理赤字凸显": "治理赤字就是该有的国际治理没跟上；逆全球化常表现为贸易保护、脱钩断链和单边壁垒。",
    "霸权主义、强权政治、单边主义、零和博弈": "这组先当世界乱象/旧式逻辑识别：材料出现恃强凌弱、强权霸凌、脱钩断链、封闭排他、零和博弈时，先判断它是不是题目的时代背景；如果设问问“怎么回应”，再转到国际关系民主化、真正多边主义和公正合理国际秩序。",
    "推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展": "这组是回应旧式国际关系逻辑的秩序方向；材料若只是在描述霸权强权存在，先放时代背景，问中国或国际社会怎样改变秩序时才写本点。",
    "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展": "核心名不能压成“正确方向”，五个词最好完整写出；材料只强调普惠、平衡、共赢时再用侧重式写法。",
    "共商共建共享的全球治理观": "不要只背六个字，卷面上要写出各国共同讨论、共同建设、共同分享治理成果。",
    "坚持正确义利观，在发展合作中义利相兼、互利共赢": "义是国际道义和共同责任，利是各方合理利益；这点常用来防止答案写成中国单方施予。",
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": "核心必须保留“新型国际关系”，合作共赢、互利共赢只是常用承接表述。",
    "建设开放型世界经济，参与全球经济治理和规则制定": "这一核心只背开放型世界经济、全球经济治理、规则制定和制度型开放；企业出海、反补贴税、标准规则等题目专用表达只在对应题里用。",
    "国际发展合作、南南合作与“小而美”项目": "这点用于发展合作、民生改善和全球南方能力建设题；如果材料只讲气候治理，就不要硬套“小而美”。",
    "中国作为负责任大国积极参与全球气候治理": "只在NDC、《巴黎协定》、绿色低碳转型、气候治理责任等材料信号明确时使用。",
    "提升贸易投资合作质量和水平": "这个点目前只作为混合经济题里的本册辅助表达积累，不能当成选必一所有开放题都能套的固定主点。",
}

QUESTION_CORE_OVERRIDES = {
    ("2025海淀期中 Q21(2)", "和平与发展仍是时代主题"): {
        "material": "题目追问新中国外交的变，材料呈现不同阶段世界格局和时代主题变化，就要想到和平与发展仍是时代主题及其对外交重点的影响。",
        "answer": "和平与发展仍是时代主题，政治多极化、经济全球化深入发展，顺应各国人民愿望和共同发展期待，这是新中国外交因势而变的重要时代背景。",
    },
    ("2026通州期末 Q20", "坚持正确义利观，在发展合作中义利相兼、互利共赢"): {
        "material": "全球治理倡议既回应国际社会共同治理需求，又强调兼顾各方合理利益，就要想到正确义利观和义利相兼、互利共赢。",
        "answer": "全球治理倡议坚持正确义利观，既回应国际社会共同治理需求，又兼顾各方合理利益，展现中国义利相兼、互利共赢的担当。",
    },
    ("2026通州期末 Q20", "和平与发展仍是时代主题"): {
        "material": "设问第一层是“正逢其时”，材料围绕全球治理倡议回应治理赤字、倡导主权平等、国际法治、多边主义和以人为本，就要先写和平与发展时代主题和共同治理需求。",
        "answer": "和平与发展成为时代主题，经济全球化深入发展，但各国仍面对治理赤字和共同挑战；全球治理倡议强调主权平等、国际法治、多边主义和以人为本，顺应各国人民愿望，因而正逢其时。",
    },
    ("2026朝阳期中 Q17", "坚持正确义利观，在发展合作中义利相兼、互利共赢"): {
        "material": "材料把人工智能发展同全球南方能力建设、发展成果共享联系起来，就要想到发展合作中的正确义利观。",
        "answer": "推进人工智能国际合作要坚持正确义利观，在发展人工智能时兼顾各方合理利益，帮助全球南方共享技术发展成果。",
    },
    ("2026通州期末 Q20", "推动构建人类命运共同体"): {
        "material": "全球治理倡议回应治理赤字和共同挑战，并把中国方案提供给国际社会，就要想到推动构建人类命运共同体。",
        "answer": "全球治理倡议回应治理赤字和共同挑战，服务于推动构建人类命运共同体，为完善全球治理贡献中国力量。",
    },
    ("2026朝阳期中 Q17", "推动构建人类命运共同体"): {
        "material": "材料把中国人工智能发展同世界共同发展、全球南方能力建设联系起来，就要想到中国发展和世界发展相协调。",
        "answer": "推进人工智能发展要把中国发展同世界共同发展联系起来，通过国际合作和能力建设推动构建人类命运共同体。",
    },
    ("2026顺义一模 Q20", "和平与发展仍是时代主题"): {
        "material": "科技小院通过农业合作改善民生、促进发展，材料重点不是空泛友好，而是共同发展需求。",
        "answer": "科技小院通过农业合作改善民生、促进发展，顺应和平与发展的时代主题和各国人民共同发展愿望。",
    },
    ("2026顺义一模 Q20", "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展"): {
        "material": "科技小院把农业技术、人才培养和减贫增收连在一起，说明发展成果要更普惠、更平衡、更共赢。",
        "answer": "科技小院通过农业技术合作、人才培养和减贫增收，让发展成果更普惠、更平衡、更共赢，推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展。",
    },
    ("2026顺义一模 Q20", "推动建设相互尊重、公平正义、合作共赢的新型国际关系"): {
        "material": "科技小院以农业技术和人才培养开展互利合作，材料强调的不是单方输出，而是合作共赢。",
        "answer": "科技小院以农业技术和人才培养开展互利合作，推动建设相互尊重、公平正义、合作共赢的新型国际关系。",
    },
    ("2026朝阳一模 Q20", "和平与发展仍是时代主题"): {
        "material": "本题问中国为什么能为全球发展注入稳定性和正能量，材料用鲁班工坊、菌草技术、现代化经验共享和开放合作说明中国回应的是各国共同发展诉求。",
        "answer": "中国通过鲁班工坊、菌草技术、现代化经验共享和开放合作回应各国共同发展诉求，顺应和平与发展的时代主题，为全球发展注入稳定性和正能量。",
    },
    ("2025海淀二模 Q21", "以联合国为核心的国际体系、联合国作用与中国的联合国身份"): {
        "answer": "联合国是当今世界最具普遍性、代表性和权威性的政府间国际组织，是集体安全机制的核心和实践多边主义的最佳场所，能够通过和平与安全、发展、人权三大支柱推动全球治理。",
    },
    ("2025海淀期中 Q16(2)", "建设开放型世界经济，参与全球经济治理和规则制定"): {
        "material": "材料呈现海外消费习惯差异、供应链成本、商标败诉和贸易摩擦风险，说明企业、行业组织和政府要分主体应对。",
        "answer": "中国咖啡企业出海要先做好海外市场调研、商标和知识产权合规，尊重当地消费习惯并提升产品与品牌竞争力；行业组织可提供风险预警、协调和法律支持；政府应依法运用国际组织规则和争端解决机制，积极参与全球经济治理和规则制定，为企业出海营造良好国际环境。",
    },
    ("2024海淀期中 Q16(2)", "建设开放型世界经济，参与全球经济治理和规则制定"): {
        "material": "材料呈现咖啡企业出海中的市场差异、供应链成本、知识产权和贸易摩擦风险，说明企业、行业组织和政府要分主体应对。",
        "answer": "中国咖啡企业出海要先做好海外市场调研、商标和知识产权合规，尊重当地消费习惯并提升产品与品牌竞争力；行业组织可提供风险预警、协调和法律支持；政府应依法运用国际组织规则和争端解决机制，积极参与全球经济治理和规则制定，为企业出海营造良好国际环境。",
    },
    ("2026西城期末 Q20", "共商共建共享的全球治理观"): {
        "material": "全球气候治理需要在联合国和《巴黎协定》框架下协商合作，各国共同参与而不是单方主导。",
        "answer": "中国参与全球气候治理坚持共商共建共享，推动各方在联合国和《巴黎协定》框架下协商合作、共同应对气候变化。",
    },
    ("2026西城期末 Q20", "国家间共同利益是国家合作的基础"): {
        "material": "NDC和《巴黎协定》说明气候治理关系各国生存发展和可持续发展，各国存在共同利益。",
        "answer": "气候变化关系各国生存发展和可持续发展，国家间共同利益是合作的基础，各方需要在共同利益上推动全球气候治理合作。",
    },
    ("2026西城期末 Q20", "和平与发展仍是时代主题"): {
        "material": "NDC置于联合国和《巴黎协定》框架下，说明气候变化不是单个国家内部问题，而是需要各国共同应对的全球治理问题。",
        "answer": "和平发展合作共赢是时代潮流，气候变化属于全球性非传统安全威胁，需要各国共同应对；中国参与气候治理顺应这一潮流。",
    },
    ("2026西城期末 Q20", "维护联合国在国际事务中的核心作用，完善全球治理体系"): {
        "material": "NDC属于《巴黎协定》框架下的气候行动目标，中国提交目标体现对多边气候治理机制的支持。",
        "answer": "中国在联合国和《巴黎协定》框架下参与全球气候治理，有利于维护多边气候治理机制，推动全球气候治理体系完善。",
    },
    ("2026西城期末 Q20", "在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善"): {
        "material": "NDC属于《巴黎协定》框架下的气候行动目标，中国提交目标体现对多边气候治理机制的支持。",
        "answer": "中国在联合国和《巴黎协定》框架下参与全球气候治理，有利于维护多边气候治理机制，推动全球气候治理体系完善。",
    },
    ("2025西城期末 Q20(2)", "建设开放型世界经济，参与全球经济治理和规则制定"): {
        "material": "欧盟对中国电动汽车征收高额反补贴税，题目问中国汽车企业如何应对外部贸易壁垒，就要想到国际规则和争端解决渠道，但不能写成企业直接行使国际组织成员权利。",
        "answer": "面对欧盟反补贴税，中国汽车企业应依法运用国际规则和争端解决渠道，在政府和行业组织支持下通过磋商、申诉和合规应对维护自身权益。",
    },
    ("2025房山一模 Q18(2)", "维护国家利益并兼顾他国合理关切，坚持正确义利观"): {
        "material": "开源战略既服务我国人工智能技术发展和安全利益，又回应国际社会对开放合作、技术共享和人工智能治理的共同需求。",
        "answer": "中国推进开源战略，在维护自身人工智能技术发展和安全利益的同时，兼顾国际社会对开放合作、技术共享和人工智能治理的合理关切，坚持正确义利观，推动形成互利共赢的全球合作新模式。",
    },
    ("2026延庆一模 Q19(2)", "国家间共同利益是国家合作的基础"): {
        "material": "绿色能源合作关系能源开发利用、绿色转型和可持续发展，中国与共建国家存在共同利益，同时中国合作要兼顾道义和各方合理利益。",
        "answer": "国家间共同利益是国家合作的基础，中国与共建国家在绿色能源开发利用和可持续发展上存在共同利益；中国坚持正确义利观，在合作中兼顾国际道义和各方合理利益，推动形成能源治理利益共同体。",
    },
    ("2026朝阳期中 Q17", "处理好中国发展和世界发展的关系"): {
        "material": "材料把我国人工智能发展同全球智能鸿沟、全球南方能力建设联系起来，就要想到中国发展和世界发展之间的关系。",
        "answer": "我国推进人工智能发展要处理好中国发展和世界发展的关系，在提升我国人工智能能力的同时，关注全球智能鸿沟，帮助全球南方国家加强人工智能能力建设，以中国发展促进世界共同发展。",
    },
}

QUESTION_SUMMARY_OVERRIDES = {
    "2026朝阳一模 Q20": [
        "首先，中国科技实力和综合国力增强，并通过科技创新、发展经验共享和开放合作回应各国共同发展诉求，为全球产业链供应链稳定提供支撑。",
        "其次，中国通过自贸协定、免签政策和市场开放促进人才、商品、服务、资金等生产要素全球流动，联动国内国际两个市场、两种资源，推动贸易投资自由化便利化，推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展。",
        "此外，中国同各国分享减贫、职业教育和现代化经验，坚持共商共建共享，扩大互利合作，推动建设合作共赢的新型国际关系。",
        "最后，鲁班工坊、菌草技术和现代化经验帮助发展中国家改善民生、增强发展内生动力，中国贡献中国智慧和中国方案，推动构建人类命运共同体，为全球发展注入稳定性和正能量。",
    ],
    "2026朝阳期中 Q17": [
        "第一，处理好自力更生和对外开放的关系：既要推进核心技术自主可控、把握创新主动权，又要积极参与国际分工，联动国内国际两个市场、两种资源。",
        "第二，处理好发展和安全的关系：既要释放人工智能降本增效和发展动能，又要坚持总体国家安全观和底线思维，防范数据安全、科技安全等风险。",
        "第三，处理好中国发展和世界发展的关系：在提升我国人工智能能力的同时，关注全球智能鸿沟，帮助全球南方加强能力建设，以中国发展促进世界共同发展。",
        "第四，处理好义与利的关系：推进人工智能国际合作要坚持正确义利观，兼顾各方合理利益，让更多国家共享技术发展成果。",
    ],
    "2025海淀期中 Q21(2)": [
        "变：①和平与发展仍是时代主题，政治多极化、经济全球化深入发展，推动新中国外交因势而变；②中国综合国力不断增强、国际地位不断提升，推动中国特色大国外交不断发展；③习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南。",
        "不变：①新中国外交始终服务于我国人民民主专政的国家性质，以维护我国主权、安全和发展利益为重要依据；②始终坚持独立自主的基本立场，按照国家发展需要自主决定外交方针；③始终贯彻维护世界和平、促进共同发展的宗旨，坚持和平共处五项原则作为对外关系基本准则。",
    ],
    "2026西城期末 Q20": [
        "和平发展合作共赢是时代潮流，气候变化属于全球性非传统安全威胁，关系各国生存发展和可持续发展；国家间共同利益是合作基础，中国坚持共商共建共享，推动各方协商合作、共同应对气候变化。",
        "中国自觉履行《巴黎协定》下的国际义务，遵循国际法，在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善。",
        "中国向联合国提交并落实2035年NDC（国家自主贡献目标），推进绿色低碳转型，积极参与全球气候治理，以自身行动贡献中国智慧、中国方案和中国力量。",
    ],
}

QUESTION_PRIORITY_NOTES = {
    "2026朝阳一模 Q20": "**主干必写四层**：科技能力、开放联通、发展合作、中国方案；考场删减规则：时间不足时合并开放联通和经济全球化方向，保留五词原话。",
    "2026西城期末 Q20": "**主干必写三层**：共同利益与共商共建共享；联合国和《巴黎协定》框架下的多边气候治理；中国提交并落实NDC（国家自主贡献目标）、贡献中国智慧中国方案。",
    "2026朝阳期中 Q17": "**主干必写四组关系**：自力更生与对外开放、发展与安全、中国发展与世界发展、义与利。",
    "2025海淀期中 Q21(2)": "**主干必写两栏**：先写“变”，再写“不变”；不要把双栏题写成一串平行句。",
    "2026东城期末 Q20": "**主干必写四条路径加总收束**：全球发展倡议、全球安全倡议、全球文明倡议、全球治理倡议，最后收束到推动构建人类命运共同体。",
}

QUESTION_EXACT_SCORING_GROUPS = {
    "2026海淀一模 Q20": [
        {
            "bucket": "经济全球化",
            "label": "扩大制度型开放，畅通双循环和新发展格局",
            "level": "角度1 对我国（3分；替代2分）",
            "terms": [
                "扩大制度型开放",
                "国内国际两个市场、两种资源",
                "畅通双循环",
                "新发展格局",
                "技术、产品、服务走出国门",
                "竞争力",
            ],
            "material": "题面说中国标准走出国门、融入全球产业发展体系，说明这不是一般开放口号，而是制度型开放、双循环和产业竞争力的意义题。",
            "accumulation": "扩大制度型开放；推进高水平对外开放；国内国际两个市场、两种资源；畅通双循环；新发展格局；技术、产品、服务走出国门；增强产品、服务乃至产业链全球竞争力。",
            "answer": "中国标准走出国门有利于扩大制度型开放，推进高水平对外开放，更好利用国内国际两个市场、两种资源，畅通双循环，推动构建新发展格局；也有利于推动我国技术、产品、服务走出国门，增强我国产品、服务乃至产业链在全球的竞争力。",
        },
        {
            "bucket": "经济全球化",
            "label": "推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展",
            "level": "角度2 对世界经济（2分；结合材料1分）",
            "terms": [
                "开放、包容、普惠、平衡、共赢",
                "国际合作",
                "互利共赢",
                "全球资源优化配置",
                "低碳能源、人工智能等领域",
                "国际标准",
                "标准共通",
                "技术共享",
                "全球技术创新与绿色转型",
            ],
            "material": "题面点名低碳能源、人工智能等领域的国际标准，说明要从世界经济意义写到标准共通、技术共享和经济全球化方向。",
            "accumulation": "推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展；促进国际合作、互利共赢；推动全球资源优化配置；低碳能源、人工智能等领域；国际标准；标准共通；技术共享；全球技术创新与绿色转型。",
            "answer": "中国在低碳能源、人工智能等领域贡献国际标准，促进全球范围内标准共通、技术共享，推动全球技术创新与绿色转型；这有利于推动经济全球化朝着开放、包容、普惠、平衡、共赢的方向发展，促进国际合作和全球资源优化配置。",
        },
        {
            "bucket": "经济全球化",
            "label": "积极参与全球经济治理和规则制定，推动国际经济新秩序",
            "level": "角度3 对全球治理（2分）",
            "terms": [
                "参与全球经济治理和规则制定",
                "全球治理体制",
                "更加公正合理方向发展",
                "话语权",
                "国际影响力",
                "国际经济新秩序",
            ],
            "material": "题面说中国贡献国际标准并参与规则制定，说明答案要写到全球经济治理、规则制定、话语权和国际经济秩序。",
            "accumulation": "积极参与全球经济治理和规则制定；推动全球治理体制向更加公正合理方向发展；提升话语权和国际影响力；推动构建国际经济新秩序。",
            "answer": "我国积极参与全球经济治理和规则制定，有利于推动全球治理体制向更加公正合理方向发展，提升中国在国际标准制定中的话语权和国际影响力，推动构建国际经济新秩序。",
        },
    ],
}

SIDE_REASON_OVERRIDES = {
    "2025海淀期末 Q22": "主属模块：哲学与文化；这道愚公移山短文只有在把个人奋斗上升到中国与世界、共同挑战、共同发展或全球治理时，才可借用人类命运共同体、中国智慧中国方案等表达；如果题目只写个人坚持、青春奋斗、家庭或人生困境，不要套用本册国际政治与经济答案。",
}


@dataclass(frozen=True)
class Atom:
    atom_id: str
    seq: int
    question: str
    prompt: str
    bucket: str
    core: str
    expression: str
    material: str
    answer: str
    status: str
    note: str
    scoring_position: str
    evidence_level: str
    source_boundary: str
    source_refs: str


def read_csv_dict(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def public(text: str) -> str:
    text = (text or "").strip()
    for old, new in PUBLIC_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = re.sub(r"\bP[0-4][_\w-]*\b", "", text)
    text = re.sub(r"材料\d+分", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_core(text: str) -> str:
    text = public(text)
    text = text.replace("；包容；普惠；平衡；共赢", "、包容、普惠、平衡、共赢")
    text = text.replace("开放包容普惠平衡共赢", "开放、包容、普惠、平衡、共赢")
    text = text.replace("普惠平衡共赢开放", "开放、包容、普惠、平衡、共赢")
    if "开放、包容、普惠、平衡、共赢" in text and "推动经济全球化" in text:
        return "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展"
    if text == "《联合国宪章》宗旨和原则":
        return "《联合国宪章》宗旨和原则"
    return text


def split_questions(value: str) -> list[str]:
    parts = re.split(r"[;；]", value or "")
    seen: set[str] = set()
    out: list[str] = []
    for part in parts:
        q = part.strip()
        if q and q not in seen:
            out.append(q)
            seen.add(q)
    return out


def parallel_piece(value: str, index: int, expected: int) -> str:
    parts = [p.strip() for p in re.split(r"[;；]", value or "") if p.strip()]
    if expected > 1 and len(parts) == expected:
        return parts[index]
    return value or ""


def split_terms(value: str) -> list[str]:
    value = public(value)
    value = value.replace("；包容；普惠；平衡；共赢", "、包容、普惠、平衡、共赢")
    terms: list[str] = []
    seen: set[str] = set()
    for raw in re.split(r"[;；/]", value):
        item = raw.strip(" 。；;、,，")
        item = normalize_core(item)
        if item in {"材料事实", "材料要点"}:
            continue
        if item and item not in seen:
            terms.append(item)
            seen.add(item)
    return terms


RED_OPEN = '<span style="color:#c00000">'
RED_CLOSE = "</span>"
RED_SPAN_RE = re.compile(r'(<span style="color:#c00000">.*?</span>)')


def red(text: str) -> str:
    return f"{RED_OPEN}{text}{RED_CLOSE}"


def score_term_parts(value: str) -> list[str]:
    value = public(value)
    value = value.replace("；包容；普惠；平衡；共赢", "、包容、普惠、平衡、共赢")
    value = re.sub(r"\s+", " ", value).strip()
    parts: list[str] = []
    for raw in re.split(r"[;；]", value):
        item = normalize_core(raw.strip(" 。；;，,、"))
        if item:
            parts.append(item)
    return parts


def valid_score_term(term: str) -> bool:
    term = term.strip(" 。；;，,、")
    if len(term) < 2 or len(term) > 48:
        return False
    blocked = (
        "作答",
        "答案方向",
        "材料事实",
        "材料要点",
        "白话提醒",
        "例题来源",
        "非累计",
        "替代表述",
        "同一评分位置",
        "同槽",
        "兜底",
        "fallback",
        "负面清单",
        "酌情",
    )
    return not any(word in term for word in blocked)


def scoring_terms_for_group(question: str, atom_group: list[Atom], accumulation: str) -> list[str]:
    atom = atom_group[0]
    # Per-question scoring words must come from this question's scoring/marking
    # expression, not from the broader framework accumulation. Framework
    # accumulation is useful for review, but it can overstate what a specific
    # colored rubric actually awards.
    sources = [item.expression for item in atom_group if item.expression]
    if not sources:
        sources = [display_core(question, atom.core), atom.core]

    terms: list[str] = []
    seen: set[str] = set()
    for source in sources:
        for term in score_term_parts(source):
            if not valid_score_term(term):
                continue
            if term in seen:
                continue
            # Avoid filling the line with both a long phrase and a tiny substring of it.
            if any(term in existing and term != existing for existing in terms):
                continue
            terms.append(term)
            seen.add(term)
            if len(terms) >= 9:
                return terms
    return terms


def scoring_terms_for_atom(atom: Atom) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()
    for term in score_term_parts(atom.expression):
        if not valid_score_term(term):
            continue
        if term in seen:
            continue
        terms.append(term)
        seen.add(term)
    if not terms:
        for term in score_term_parts(display_core(atom.question, atom.core)):
            if valid_score_term(term) and term not in seen:
                terms.append(term)
                seen.add(term)
    return terms[:10]


def scoring_position_public(atom: Atom) -> str:
    raw = (atom.scoring_position or "").strip()
    if "PPTX slide42 paragraph" in raw:
        match = re.search(r"paragraph\s*(\d+(?:-\d+)?)", raw)
        para = match.group(1) if match else ""
        suffix = f"第{para}段" if para else ""
        return f"答案示例性质{suffix}（非逐点细则，按等级口径给分）"
    if "P2讲评PPT slide" in raw:
        match = re.search(r"slide\s*(\d+)", raw)
        page = match.group(1) if match else ""
        return f"朝阳讲评 PPT 第{page}页点位（非正式阅卷细则）" if page else "朝阳讲评 PPT 点位（非正式阅卷细则）"
    if "试题分析PPT slide64第" in raw:
        match = re.search(r"第(\d+)点", raw)
        point = match.group(1) if match else ""
        return f"试题分析 PPT 第64页第{point}点（非正式细则，按教研讲评口径）" if point else "试题分析 PPT 第64页点位（非正式细则，按教研讲评口径）"
    if "答案提示四方面" in raw:
        text = public(raw)
        text = re.sub(r"\s+", " ", text).strip(" ；。")
        return f"{text}（本题为等级说明，非逐点细则）"
    if "image" in raw or "内嵌图片" in raw or "图片" in raw:
        text = raw
        text = re.sub(r"内嵌图片image\d+", "", text)
        text = re.sub(r"图片image\d+", "", text)
        text = re.sub(r"image\d+", "", text)
        text = text.replace("海淀图片表格细则", "")
        text = text.replace("图片表格细则", "")
        text = public(text)
        text = text.replace("变4分-", "变：")
        text = re.sub(r"\s+", " ", text).strip(" ；。")
        return f"海淀题面表格细则—{text}" if text else "海淀题面表格细则"
    text = public(raw)
    text = text.replace("答案口径第", "第")
    text = text.replace("答案口径", "答案点位")
    text = text.replace("内嵌图片", "图片")
    text = re.sub(r"\s+", " ", text).strip(" ；。")
    return text or "题内答案点位"


def evidence_level_for_atom(atom: Atom) -> str:
    return atom.evidence_level


def source_boundary_for_atom(atom: Atom) -> str:
    if atom.question == "2026通州期末 Q20" and "通州评分细则第2点" in atom.scoring_position:
        return "formal_scoring_pptx_user_notebook_six_point_verified"
    return atom.source_boundary


def student_point_label(atom: Atom) -> str:
    level = evidence_level_for_atom(atom)
    boundary = source_boundary_for_atom(atom)
    if "user_confirmed" in level or "colored" in boundary:
        return "本题踩分点（彩色细则）"
    if "image" in level or "image" in boundary or "图片" in scoring_position_public(atom):
        return "本题踩分点（题内图片细则）"
    if "formal" in level or "rubric" in boundary or "scoring" in boundary or "marking" in boundary:
        return "本题踩分点（正式细则）"
    if "level" in boundary or "guarded" in boundary or "answer" in boundary or "PPT" in scoring_position_public(atom):
        return "本题可得分表达（等级答案或讲评口径）"
    return "本题参考点（按题使用）"


def scoring_point_atoms(q: str, main_q_atoms: list[Atom], side_q_atoms: list[Atom]) -> list[Atom]:
    seen: set[tuple[str, str, str, str]] = set()
    out: list[Atom] = []
    for atom in sorted(main_q_atoms + side_q_atoms, key=lambda a: (a.seq, a.atom_id)):
        key = (atom.atom_id, atom.scoring_position, atom.expression, atom.answer)
        if key in seen:
            continue
        seen.add(key)
        out.append(atom)
    return out


def atom_boundary_label(atom: Atom, is_side: bool) -> str:
    if atom.question == "2026西城期末 Q20" and atom.core == "共商共建共享的全球治理观":
        return "【同一层备用】本组红字属于同一层治理理念表达，材料贴哪个就写哪个，不要把命运共同体、全人类共同价值、正确义利观、共商共建共享、真正多边主义、互利共赢全部硬塞进一句。"
    if atom.question == "2026顺义一模 Q20" and "国际政治3分同一评分功能位" in atom.scoring_position:
        return "【同一层备用】本组为顺义国际政治3分角度的等价表达池，任选一组贴材料写，不必四串全背。"
    if not is_side:
        return ""
    if atom.status in {"boundary_only", "excluded_boundary_subpoint"} or is_cross_module(atom.prompt):
        return "【本题辅助点】只在本题用，不进六桶主框架。"
    if atom.status in {"reference_only", "result_expression_only"}:
        return "【本题补充表达】写卷面结果或作语言积累，不进六桶主框架。"
    return "【本题辅助点】按题使用，不脱离设问硬套。"


def term_line_from_atom(atom: Atom) -> str:
    return format_scoring_terms(scoring_terms_for_atom(atom))


def answer_line_from_atom(atom: Atom) -> str:
    terms = scoring_terms_for_atom(atom)
    return highlight_scoring_terms(atom.answer, terms)


def format_scoring_terms(terms: list[str]) -> str:
    return "；".join(red(term) for term in terms) if terms else red("本条核心术语")


def missing_score_terms_in_answer(terms: list[str], answer: str) -> list[str]:
    clean_answer = re.sub(r"<.*?>", "", answer or "")
    missing: list[str] = []
    for term in terms:
        plain = re.sub(r"<.*?>", "", term)
        if plain and plain not in clean_answer:
            missing.append(plain)
    return missing


def alternate_terms_note(terms: list[str], answer: str) -> str:
    missing = missing_score_terms_in_answer(terms, answer)
    if len(missing) < 2:
        return ""
    used = [term for term in terms if term not in missing]
    if not used:
        return ""
    return f"同一层择写提醒：卷面句已示范“{'、'.join(used[:3])}”；“{'、'.join(missing[:5])}”作同层备用表达，材料贴哪个就写哪个，不要机械全塞。"


def replace_outside_red_span(text: str, term: str) -> str:
    if not term or term not in text:
        return text
    pieces = RED_SPAN_RE.split(text)
    pattern = re.compile(re.escape(term))
    for idx, piece in enumerate(pieces):
        if not piece or piece.startswith(RED_OPEN):
            continue
        pieces[idx] = pattern.sub(lambda m: red(m.group(0)), piece)
    return "".join(pieces)


def highlight_scoring_terms(text: str, terms: list[str]) -> str:
    result = text
    for term in sorted(terms, key=len, reverse=True):
        result = replace_outside_red_span(result, term)
    return result


def scoring_terms_for_core(core: str, row: dict[str, str]) -> list[str]:
    accumulation = compact_accumulation(core, row.get("expression_accumulation", core))
    pseudo_atom = Atom(
        atom_id="",
        seq=0,
        question="",
        prompt="",
        bucket="",
        core=core,
        expression=accumulation,
        material="",
        answer="",
        status="",
        note="",
        scoring_position="",
        evidence_level="",
        source_boundary="",
        source_refs="",
    )
    return scoring_terms_for_group("", [pseudo_atom], accumulation)


def compact_accumulation(core: str, raw: str) -> str:
    core = normalize_core(core)
    if core in CORE_FORCE:
        terms = CORE_FORCE[core][:]
    else:
        terms = split_terms(raw)
        removes = CORE_REMOVES.get(core, ())
        if removes:
            terms = [t for t in terms if not any(r in t for r in removes)]
        if core not in terms:
            terms.insert(0, core)
    cleaned: list[str] = []
    seen: set[str] = set()
    for term in terms:
        term = term.strip()
        if not term or term in seen:
            continue
        if len(term) > 42 and term != core:
            continue
        cleaned.append(term)
        seen.add(term)
        if len(cleaned) >= 7:
            break
    return "；".join(cleaned) + "。"


def question_trigger(prompt: str) -> str:
    p = prompt or ""
    if any(k in p for k in ["为什么", "深层逻辑", "理论逻辑", "为何"]):
        return "追问原因或深层逻辑时，先找合作为什么成立、能力从哪里来、时代背景是什么，再接到对应核心点。"
    if any(k in p for k in ["应如何", "如何", "怎样", "措施", "做法"]):
        return "追问做法或路径时，按“具体做法 -> 对应机制 -> 对中国或世界的作用”来取点。"
    if any(k in p for k in ["意义", "价值", "彰显", "作用", "贡献"]):
        return "追问意义、价值或担当时，分清对象：对中国、对合作方、对世界秩序或全球治理分别作答。"
    if any(k in p for k in ["理解", "阐释", "分析", "谈谈", "说明"]):
        return "分析说明类题要同时写理论依据、材料信息和作用结论，不能只列术语。"
    if any(k in p for k in ["短评", "发言人", "概述"]):
        return "写作类题先定中心论点，再把核心术语变成分层论证段。"
    return "先判断题目问的是原因、措施、意义还是评价，再把材料关系接到对应框架。"


def polish_sentence(text: str) -> str:
    text = public(text)
    text = text.replace("发展与和平、人权三大支柱", "和平与安全、发展、人权三大支柱")
    text = text.replace(" ;", "；").replace(" ,", "，")
    text = re.sub(r"\s+", " ", text).strip()
    if " " in text and not any(p in text for p in "，；、。"):
        text = text.replace(" ", "，")
    else:
        text = re.sub(r"(?<=[\u4e00-\u9fff]) (?=[\u4e00-\u9fff])", "，", text)
    text = text.strip(" ，；。")
    if text:
        text += "。"
    return text


def question_specific_material(question: str, core: str, material: str) -> str:
    override = QUESTION_CORE_OVERRIDES.get((question, core), {})
    if override.get("material"):
        return override["material"]
    return material


def question_specific_answer(question: str, core: str, answer: str) -> str:
    override = QUESTION_CORE_OVERRIDES.get((question, core), {})
    if override.get("answer"):
        return polish_sentence(override["answer"])
    return answer


def display_core(question: str, core: str) -> str:
    return QUESTION_CORE_DISPLAY_OVERRIDES.get((question, core), core)


def adjusted_bucket_core(atom_id: str, bucket: str, core: str) -> tuple[str, str]:
    return ATOM_CORE_OVERRIDES.get(atom_id, (bucket, core))


def district_key(question: str) -> tuple[int, int, int, str]:
    m = re.match(r"(\d{4})(.+?)(期末|期中|一模|二模)?\s*Q", question)
    year = int(m.group(1)) if m else 0
    rest = m.group(2) if m else question
    district = next((d for d in DISTRICT_ORDER if d in rest), rest)
    exam = m.group(3) if m and m.group(3) else ""
    exam_order = {"期末": 0, "期中": 1, "一模": 2, "二模": 3}.get(exam, 9)
    return (DISTRICT_ORDER.get(district, 99), -year, exam_order, question)


def is_cross_module(prompt: str) -> bool:
    prompt = prompt or ""
    if any(k in prompt for k in ["哲学与文化", "法律与生活", "逻辑与思维", "经济与社会", "经济的相关知识"]):
        return True
    if "自选角度" in prompt and "当代国际政治与经济" not in prompt and "国际政治与经济" not in prompt:
        return True
    return False


def side_module_label(atom: Atom) -> str:
    prompt = atom.prompt or ""
    if "经济与社会" in prompt or "经济的相关知识" in prompt:
        return "经济与社会"
    if "哲学与文化" in prompt:
        return "哲学与文化"
    if "法律与生活" in prompt:
        return "法律与生活"
    if "逻辑与思维" in prompt:
        return "逻辑与思维"
    if "政治与法治" in prompt:
        return "政治与法治"
    if atom.status in {"reference_only", "result_expression_only"}:
        return "选必一开放表达"
    if atom.status in {"boundary_only", "excluded_boundary_subpoint"}:
        return "选必一开放表达"
    return "选必一开放表达"


def question_trigger_specific(question: str, prompt: str, atoms: list[Atom]) -> str:
    if question in QUESTION_TRIGGER_OVERRIDES:
        return QUESTION_TRIGGER_OVERRIDES[question]
    if "正逢其时" in prompt and "指引方向" in prompt and "彰显担当" in prompt:
        return "本题设问自带三层：正逢其时看时代背景，指引方向看国际秩序和全球治理，彰显担当看中国方案与大国责任，三层不要合写。"
    if "重要关系" in prompt and "人工智能" in prompt:
        return "本题关键词是“重要关系”，看到不同同学的看法，就把答案分成自力更生与对外开放、发展与安全、中国发展与世界发展三组关系。"
    if "中国需要联合国" in prompt and "联合国也需要中国" in prompt:
        return "本题是双向论证：中国需要联合国时写联合国平台和作用；联合国需要中国时写中国身份、贡献和建设性作用。"
    if "变" in prompt and "不变" in prompt:
        return "本题要按“变”和“不变”分栏：变侧写时代背景、国力和外交实践的发展，不变侧写基本立场、宗旨、目标和准则。"
    seen: set[tuple[str, str]] = set()
    pairs: list[str] = []
    for atom in atoms:
        key = (atom.bucket, atom.core)
        if key in seen:
            continue
        seen.add(key)
        pairs.append(f"{atom.bucket}->{display_core(question, atom.core)}")
        if len(pairs) >= 5:
            break
    bucket_text = "；".join(pairs)
    return f"本题先按设问类型分层，再从材料里依次抓这些方向：{bucket_text}。卷面答案按“理论依据、材料对接、回扣设问”组织，同一术语不要重复写。"


def grouped_question_atoms(q_atoms: list[Atom]) -> list[list[Atom]]:
    grouped_atoms: list[list[Atom]] = []
    group_index: dict[tuple[str, str], int] = {}
    for atom in q_atoms:
        key = (atom.bucket, atom.core)
        if key not in group_index:
            group_index[key] = len(grouped_atoms)
            grouped_atoms.append([])
        grouped_atoms[group_index[key]].append(atom)
    return grouped_atoms


def first_answer_for_group(atom_group: list[Atom]) -> str:
    for atom in atom_group:
        if atom.answer:
            return atom.answer
    return display_core(atom_group[0].question, atom_group[0].core)


def side_reason(atom: Atom) -> str:
    if atom.question in SIDE_REASON_OVERRIDES:
        return SIDE_REASON_OVERRIDES[atom.question]
    if "2026石景山期末" in atom.question:
        return "整套不进入本册训练。"
    module = side_module_label(atom)
    if module == "经济与社会":
        return "主属模块：经济与社会；这里只作本册相关表达积累，正式练本册时不要当固定模板。"
    if is_cross_module(atom.prompt):
        return f"主属模块：{module}；这道题不是直接指定本册，适合做跨模块表达积累，正式练本册时不要当固定模板。"
    if atom.status in {"reference_only", "result_expression_only"}:
        return f"主属模块：{module}；这类表述适合积累语言，不宜当作稳定主答题点。"
    if atom.status in {"boundary_only", "excluded_boundary_subpoint"}:
        return f"主属模块：{module}；这类内容主要属于其他模块或开放表达，放在慎用区。"
    return f"主属模块：{module}；按设问和材料匹配后再使用，不能脱离题目硬套。"


def main() -> None:
    prompts = {r["source_question"].strip(): r["full_prompt"].strip() for r in read_csv_dict(PROMPTS_CSV)}
    prompts.update(PROMPT_OVERRIDES)

    clusters: dict[tuple[str, str], dict[str, str]] = {}
    for row in read_csv_dict(CLUSTERS_CSV):
        bucket = row["bucket"].strip()
        core = normalize_core(row["core_cluster"])
        clusters[(bucket, core)] = row

    atoms: list[Atom] = []
    teacher_rows: list[dict[str, str]] = []
    for source_seq, row in enumerate(read_csv_dict(ATOMS_CSV), 1):
        bucket = row.get("final_bucket") or row.get("bucket") or "理论"
        core = normalize_core(row.get("final_core_cluster") or row.get("core_point") or "")
        bucket, core = adjusted_bucket_core(row.get("atom_id", ""), bucket, core)
        q_list = split_questions(row.get("source_question", ""))
        for q_index, q in enumerate(q_list):
            prompt = prompts.get(q, "")
            atom = Atom(
                atom_id=row.get("atom_id", ""),
                seq=source_seq,
                question=q,
                prompt=prompt,
                bucket=bucket,
                core=core,
                expression=public(row.get("expression_variant", "")),
                material=question_specific_material(q, core, public(row.get("material_trigger_fusion", ""))),
                answer=question_specific_answer(q, core, polish_sentence(row.get("answer_sentence_fusion", ""))),
                status=row.get("promotion_status", ""),
                note=public(row.get("boundary_note", "")),
                scoring_position=parallel_piece(row.get("scoring_position", ""), q_index, len(q_list)),
                evidence_level=parallel_piece(row.get("evidence_level", ""), q_index, len(q_list)),
                source_boundary=parallel_piece(row.get("source_boundary", ""), q_index, len(q_list)),
                source_refs=parallel_piece(row.get("source_ledger_refs", ""), q_index, len(q_list)),
            )
            atoms.append(atom)
            teacher_rows.append(
                {
                    "question": q,
                    "bucket": bucket,
                    "core": core,
                    "atom_id": atom.atom_id,
                    "scoring_position": atom.scoring_position,
                    "evidence_level": evidence_level_for_atom(atom),
                    "status": atom.status,
                    "source_boundary": source_boundary_for_atom(atom),
                    "boundary_note": row.get("boundary_note", ""),
                }
            )

    unique: dict[tuple[str, str, str, str], Atom] = {}
    for atom in atoms:
        key = (atom.question, atom.bucket, atom.core, atom.answer)
        unique.setdefault(key, atom)
    atoms = list(unique.values())

    main_atoms: dict[str, list[Atom]] = defaultdict(list)
    side_atoms: dict[str, list[Atom]] = defaultdict(list)
    for atom in atoms:
        if "2026石景山期末" in atom.question:
            continue
        if atom.status in MAIN_STATUSES and (atom.question in QUESTION_FORCE_MAIN or not is_cross_module(atom.prompt)):
            main_atoms[atom.question].append(atom)
        else:
            side_atoms[atom.question].append(atom)

    for group in (main_atoms, side_atoms):
        for q in group:
            group[q].sort(key=lambda a: (BUCKET_ORDER.get(a.bucket, 99), a.core, a.atom_id))

    core_main_questions: dict[tuple[str, str], list[str]] = defaultdict(list)
    for q, q_atoms in main_atoms.items():
        for atom in q_atoms:
            key = (atom.bucket, atom.core)
            if q not in core_main_questions[key]:
                core_main_questions[key].append(q)
    for key in core_main_questions:
        core_main_questions[key].sort(key=district_key)

    for (bucket, core), row in MANUAL_CORE_OVERLAYS.items():
        clusters.setdefault((bucket, core), row)
        for q in split_questions(row.get("source_questions", "")):
            if q not in core_main_questions[(bucket, core)]:
                core_main_questions[(bucket, core)].append(q)
        core_main_questions[(bucket, core)].sort(key=district_key)

    lines: list[str] = []
    lines.append("# 选必一《当代国际政治与经济》主观题完整学生讲义")
    lines.append("")
    lines.append("这份讲义按“先整题训练，再六桶复盘”使用。面对一道新题，先看完整设问和材料关系，再把答案点放回六个框架：时代背景、理论、经济全球化、政治多极化、中国、联合国。")
    lines.append("")
    lines.append("## 使用路线")
    lines.append("")
    lines.append("- 第一步：先读每道题的“本题踩分点汇总”，红色词就是最该写出的踩分词，后面的句子是把这些词连成卷面答案。")
    lines.append("- 第二步：再看“本题命中框架”，把这些红色踩分词放回六个框架，不要只背孤立术语。")
    lines.append("- 第三步：再看“条目拆解”，把完整设问、设问触发、材料触发、框架落点、答题点自身积累（可替换表达，不必全背）和答案句变体连起来。")
    lines.append("- 第四步：最后背“整题汇总卷面答案”，练的是考场上真正要写出来的分层答案。")
    lines.append("- 边界提醒：“白话提醒”只负责告诉你何时能用、何时别误套；真正写到卷面上的，仍然看“答题点自身积累（可替换表达）”和“卷面答案句”。")
    lines.append("- 背诵顺序：先背整题汇总卷面答案；答题点自身积累只作替换词库，不要求全背。")
    lines.append("")
    lines.append("## 一页急救版")
    lines.append("")
    lines.append("新题先别急着背六桶。先用四步把题拆开：")
    lines.append("")
    lines.append("- 第一步：看设问动词，判断题目问原因、意义、做法、理解、关系还是短文。")
    lines.append("- 第二步：圈材料对象，看它是中国、合作方、世界秩序、全球治理、联合国，还是开放型经济。")
    lines.append("- 第三步：勾命中框架，一题常常跨好几个桶，六桶是地图，不是六选一。")
    lines.append("- 第四步：写成三句，先写核心术语，再接材料事实，最后回扣设问问的那个词。")
    lines.append("")
    lines.append("考场时间不够时，先保住“术语原词 + 材料对接 + 回扣设问”。长题先写3到4个最稳层次；可选补充只在材料和分值允许时加，别把所有熟词堆上去。")
    lines.append("")
    lines.append("## 题型触发对照表")
    lines.append("")
    lines.append("| 设问信号 | 先想什么 | 卷面怎么写 |")
    lines.append("| --- | --- | --- |")
    lines.append("| 为什么、为何、理论逻辑、深层逻辑 | 合作基础、能力来源、时代背景 | 用“因为……所以……”或“根源在于……”开头，不先写空泛做法 |")
    lines.append("| 如何、怎样、措施、路径 | 主体做法和作用机制 | 按“做法 -> 机制 -> 作用”写，别只列政策名 |")
    lines.append("| 意义、价值、贡献、彰显 | 对中国、合作方、世界秩序或全球治理的影响 | 分对象写，最后回扣题目里的意义词 |")
    lines.append("| 理解、说明、分析、谈谈 | 理论依据、材料信息、作用结论 | 每点都要有术语、有材料、有结论 |")
    lines.append("| 关系类、变与不变、双向论证 | 题目自带的对照关系 | 直接分栏或分层，不要写成一串平行句 |")
    lines.append("| 短文、短评、发言稿 | 中心论点和分段论证 | 先定中心句，再把核心术语变成段落 |")
    lines.append("")
    lines.append("## 高频误套风险表")
    lines.append("")
    lines.append("| 易误套核心 | 什么时候用 | 什么时候别硬套 |")
    lines.append("| --- | --- | --- |")
    lines.append("| 和平与发展仍是时代主题 | 设问问时代背景、世界大势、倡议为何正逢其时、外交变迁或全球合作必要性 | 企业具体经营建议、单一贸易维权、开放政策效果题，不一定先写时代主题 |")
    lines.append("| 霸权主义、强权政治、单边主义、零和博弈 | 材料描述世界乱象、旧式国际关系逻辑、强权霸凌、封闭排他、脱钩断链 | 如果设问问回应路径，要转写国际关系民主化、真正多边主义、公正合理国际秩序，不只停在批判 |")
    lines.append("| 推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展 | 自贸协定、零关税、全球南方受益、发展成果共享、开放合作反对保护主义 | 只讲企业内部经营、国内产业升级、个人奋斗时，不强行套五词 |")
    lines.append("| 推动建设相互尊重、公平正义、合作共赢的新型国际关系 | 材料有国家间关系、国际合作方式、互利共赢、非零和竞争 | 企业经营、技术标准、单一开放政策题慎用 |")
    lines.append("| 共商共建共享的全球治理观 | 全球治理体系改革、治理赤字、各国平等参与、共同协商建设分享 | 普通开放合作或共享发展成果，优先写互利共赢或共享发展 |")
    lines.append("| 推动构建人类命运共同体 | 共同挑战、共同前途、全球公共产品、共同安全或共同发展明确出现 | 不把它当所有“中国贡献题”的万能结尾 |")
    lines.append("| 贡献中国智慧、中国方案 | 材料有技术、经验、倡议、制度方案或国际公共产品 | 没有具体事实时不要空喊中国方案 |")
    lines.append("| 联合国和《巴黎协定》框架 | 明确出现联合国、宪章、安理会、联合国体系、巴黎协定或NDC（国家自主贡献目标） | 一般国际组织、WTO规则和普通国际规则不能自动写成联合国核心作用 |")
    lines.append("| 国家间共同利益是国家合作的基础 / 维护国家利益并兼顾他国合理关切，坚持正确义利观 | 前者解释合作为什么成立；后者解释中国怎样合作 | 不把“合作基础”和“中国合作方式”合并成一个点；材料同时出现两类信号时分两段写 |")
    lines.append("")

    lines.append("## 六桶总框架索引")
    lines.append("")
    lines.append("这一页是查地图用的：红色是框架里的核心踩分词，真正练答题仍然回到后面的“按题训练闭环”。六桶索引用来查地图，不用背题号；看到熟词不要直接套，先回到完整设问和材料关系。")
    lines.append("")
    for bucket in BUCKETS:
        bucket_cores = [
            (core, row)
            for (b, core), row in clusters.items()
            if b == bucket
        ]
        for b, core in core_main_questions:
            if b == bucket and (b, core) not in clusters:
                bucket_cores.append((core, {"distinct_source_count": str(len(core_main_questions[(b, core)]))}))
        if not bucket_cores:
            continue
        lines.append(f"### {bucket}")
        for core, row in sorted(bucket_cores, key=lambda x: (-int(x[1].get("distinct_source_count") or 0), x[0])):
            q_list = core_main_questions.get((bucket, core), [])
            if not q_list:
                continue
            sources = "；".join(q_list[:8])
            more = "等" if len(q_list) > 8 else ""
            note = CORE_INDEX_NOTES.get(core, "")
            lines.append(f"- **{red(core)}**{note}：{sources}{more}")
        lines.append("")

    lines.append("## 按题训练闭环")
    lines.append("")
    rubric_audit_rows: list[dict[str, str]] = []
    for idx, q in enumerate(sorted(main_atoms, key=district_key), 1):
        q_atoms = main_atoms[q]
        q_side_atoms = side_atoms.get(q, [])
        q_scoring_atoms = scoring_point_atoms(q, q_atoms, q_side_atoms)
        prompt = prompts.get(q, q)
        lines.append(f"### {idx}. {q}")
        lines.append("")
        lines.append(f"**完整设问**：{prompt}")
        if q in QUESTION_HEADER_NOTES:
            lines.append(f"**模块归属提醒**：{QUESTION_HEADER_NOTES[q]}")
        lines.append("")
        lines.append(f"**设问触发（题型通用）**：{question_trigger(prompt)}")
        lines.append(f"**设问触发（本题独有）**：{question_trigger_specific(q, prompt, q_atoms)}")
        lines.append("")
        grouped_atoms = grouped_question_atoms(q_atoms)
        exact_groups = QUESTION_EXACT_SCORING_GROUPS.get(q)
        if exact_groups:
            lines.append("**本题踩分点汇总**：")
            for n, group in enumerate(exact_groups, 1):
                terms = list(group["terms"])
                lines.append(f"{n}. **框架归类：{group['label']}**")
                lines.append(f"   - 卷面层级：{group['level']}")
                lines.append("   - 点位性质：本题踩分点（彩色细则）")
                lines.append(f"   - 踩分词：{format_scoring_terms(terms)}")
                alt_note = alternate_terms_note(terms, group["answer"])
                if alt_note:
                    lines.append(f"   - {alt_note}")
                lines.append(f"   - 卷面句：{highlight_scoring_terms(group['answer'], terms)}")
                rubric_audit_rows.append(
                    {
                        "question": q,
                        "point_no": str(n),
                        "basis": "user_provided_colored_rubric_regression",
                        "bucket": group["bucket"],
                        "framework_core": group["label"],
                        "scoring_position": group["level"],
                        "red_scoring_terms": "；".join(terms),
                        "answer_sentence": group["answer"],
                        "evidence_level": "user_confirmed_colored_scoring_image",
                        "promotion_status": "exact_override_after_user_regression",
                        "source_boundary": "colored_rubric_visual",
                        "source_refs": "2026海淀一模_Q20_SRC_14176e949dd0",
                        "student_summary_status": "included_exact",
                    }
                )
            lines.append("")
            lines.append("**本题命中框架**：")
            by_bucket_exact: dict[str, list[str]] = defaultdict(list)
            for group in exact_groups:
                if group["label"] not in by_bucket_exact[group["bucket"]]:
                    by_bucket_exact[group["bucket"]].append(group["label"])
            for bucket in BUCKETS:
                if by_bucket_exact.get(bucket):
                    lines.append(f"- {bucket}：{'；'.join(by_bucket_exact[bucket])}")
            lines.append("")
            lines.append("**整题汇总卷面答案**：")
            for group in exact_groups:
                lines.append(f"- {highlight_scoring_terms(group['answer'], list(group['terms']))}")
            lines.append("")
            lines.append("**条目拆解**：")
            lines.append("")
            for n, group in enumerate(exact_groups, 1):
                terms = list(group["terms"])
                lines.append(f"{n}. **{group['label']}**")
                lines.append(f"   - 卷面层级：{group['level']}")
                lines.append("   - 点位性质：本题踩分点（彩色细则）")
                lines.append(f"   - 材料触发：{group['material']}")
                lines.append(f"   - 框架落点：{group['bucket']} -> {group['label']}")
                lines.append(f"   - 踩分词：{format_scoring_terms(terms)}")
                alt_note = alternate_terms_note(terms, group["answer"])
                if alt_note:
                    lines.append(f"   - {alt_note}")
                lines.append(f"   - 答题点自身积累（可替换表达，不必全背）：{highlight_scoring_terms(group['accumulation'], terms)}")
                lines.append(f"   - 卷面答案句（答案句变体）：{highlight_scoring_terms(group['answer'], terms)}")
            lines.append("")
            continue
        lines.append("**本题踩分点汇总**：")
        main_atom_keys = {(atom.atom_id, atom.scoring_position, atom.answer) for atom in q_atoms}
        for n, atom in enumerate(q_scoring_atoms, 1):
            atom_label = display_core(q, atom.core)
            score_terms = scoring_terms_for_atom(atom)
            is_side = (atom.atom_id, atom.scoring_position, atom.answer) not in main_atom_keys
            lines.append(f"{n}. **框架归类：{atom_label}**")
            lines.append(f"   - 卷面层级：{scoring_position_public(atom)}")
            lines.append(f"   - 点位性质：{student_point_label(atom)}")
            boundary_label = atom_boundary_label(atom, is_side)
            if boundary_label:
                lines.append(f"   - 使用边界：{boundary_label}")
            lines.append(f"   - 踩分词：{format_scoring_terms(score_terms)}")
            alt_note = alternate_terms_note(score_terms, atom.answer)
            if alt_note:
                lines.append(f"   - {alt_note}")
            lines.append(f"   - 卷面句：{highlight_scoring_terms(atom.answer, score_terms)}")
            rubric_audit_rows.append(
                {
                    "question": q,
                    "point_no": str(n),
                    "basis": "atom_expression_variant_from_source_ledger",
                    "bucket": atom.bucket,
                    "framework_core": atom_label,
                    "scoring_position": atom.scoring_position,
                    "red_scoring_terms": "；".join(score_terms),
                    "answer_sentence": atom.answer,
                    "evidence_level": evidence_level_for_atom(atom),
                    "promotion_status": atom.status,
                    "source_boundary": source_boundary_for_atom(atom),
                    "source_refs": atom.source_refs,
                    "student_summary_status": "included_main" if not is_side else "included_as_question_auxiliary",
                }
            )
        lines.append("")
        lines.append("**本题命中框架**：")
        by_bucket: dict[str, list[str]] = defaultdict(list)
        for atom in q_atoms:
            label = display_core(q, atom.core)
            if label not in by_bucket[atom.bucket]:
                by_bucket[atom.bucket].append(label)
        for bucket in BUCKETS:
            if by_bucket.get(bucket):
                lines.append(f"- {bucket}：{'；'.join(by_bucket[bucket])}")
        if q == "2025海淀期中 Q21(2)":
            lines.append(f"- 本题红字落点：{red('国际影响力、话语权不断提升')}；综合国力框架在本题只落到这组卷面词，不把整段理论当本题红字硬背。")
        if q_side_atoms:
            aux_labels: list[str] = []
            for atom in q_side_atoms:
                label = f"{atom.bucket} -> {display_core(q, atom.core)}"
                if label not in aux_labels:
                    aux_labels.append(label)
            if aux_labels:
                lines.append(f"- 本题辅助/边界点：{'；'.join(aux_labels)}")
        lines.append("")
        lines.append("**整题汇总卷面答案**：")
        if q in QUESTION_PRIORITY_NOTES:
            lines.append(f"- {QUESTION_PRIORITY_NOTES[q]}")
        summary_override = QUESTION_SUMMARY_OVERRIDES.get(q)
        question_score_terms: list[str] = []
        for atom in q_scoring_atoms:
            for term in scoring_terms_for_atom(atom):
                if term not in question_score_terms:
                    question_score_terms.append(term)
        if summary_override:
            for answer in summary_override:
                lines.append(f"- {highlight_scoring_terms(answer, question_score_terms)}")
            override_text = "\n".join(summary_override)
            for atom in q_scoring_atoms:
                atom_terms = scoring_terms_for_atom(atom)
                if atom.answer and not any(term and term in override_text for term in atom_terms[:3]):
                    lines.append(f"- {highlight_scoring_terms(atom.answer, atom_terms)}")
        else:
            for atom in q_scoring_atoms:
                score_terms = scoring_terms_for_atom(atom)
                lines.append(f"- {highlight_scoring_terms(atom.answer, score_terms)}")
        summary_count = len(summary_override) if summary_override else len(q_scoring_atoms)
        core_count_for_question = len({(atom.bucket, atom.core) for atom in q_atoms})
        if q not in QUESTION_PRIORITY_NOTES and (summary_count >= 5 or core_count_for_question >= 6):
            lines.append("- 主干必写：先写3到4个最稳层次；可选补充看分值和材料；时间不足时删重复材料句，保留术语、材料对接和回扣设问。")
        lines.append("")
        lines.append("**条目拆解**：")
        lines.append("")
        for n, atom in enumerate(q_scoring_atoms, 1):
            row = clusters.get((atom.bucket, atom.core), {})
            accumulation = compact_accumulation(atom.core, row.get("expression_accumulation", atom.expression or atom.core))
            material = public(atom.material)
            material = material.replace("触发", "就要想到")
            material = material.replace("设问要求", "题目追问")
            material = material.replace("材料中", "材料里的")
            material = material.replace("材料里的的", "材料里的")
            material = material.replace("直接就要想到", "就要想到")
            material = material.replace("对应就要想到", "对应")
            material = material.replace("材料里的NDC", "NDC")
            material = material.replace("材料里的一带一路", "一带一路")
            material = material.replace("材料里的中欧", "中欧")
            material = material.replace("材料里的公共产品", "公共产品")
            material = material.replace("材料里的气候", "气候")
            material = material.replace("材料里的全球治理", "全球治理")
            material = material.replace("材料里的供应链", "供应链")
            material = material.replace(
                "独立自主和平外交政策只是同槽替代表述不并入理论核心",
                "独立自主和平外交政策属于外交政策表达，不能替代共同利益这个合作基础",
            )
            material = re.sub(r"\s+", " ", material).strip()
            atom_label = display_core(q, atom.core)
            score_terms = scoring_terms_for_atom(atom)
            is_side = (atom.atom_id, atom.scoring_position, atom.answer) not in main_atom_keys
            lines.append(f"{n}. **{atom_label}**")
            lines.append(f"   - 卷面层级：{scoring_position_public(atom)}")
            lines.append(f"   - 点位性质：{student_point_label(atom)}")
            boundary_label = atom_boundary_label(atom, is_side)
            if boundary_label:
                lines.append(f"   - 使用边界：{boundary_label}")
            lines.append(f"   - 材料触发：{material}")
            lines.append(f"   - 框架落点：{atom.bucket} -> {atom_label}")
            lines.append(f"   - 踩分词：{format_scoring_terms(score_terms)}")
            alt_note = alternate_terms_note(score_terms, atom.answer)
            if alt_note:
                lines.append(f"   - {alt_note}")
            subpath = QUESTION_CORE_SUBPATHS.get((q, atom.core))
            if subpath:
                lines.append(f"   - 路径分层：{subpath}")
            if atom.core in PLAIN_NOTES:
                lines.append(f"   - 白话提醒：{PLAIN_NOTES[atom.core]}")
            lines.append(f"   - 答题点自身积累（可替换表达，不必全背）：{highlight_scoring_terms(accumulation, score_terms)}")
            lines.append(f"   - 卷面答案句（答案句变体）：{highlight_scoring_terms(atom.answer, score_terms)}")
        lines.append("")

    if side_atoms:
        lines.append("## 慎用与跨模块表达积累")
        lines.append("")
        lines.append("下面内容可以帮助积累语言，但不作为本册主观题的固定逐点模板。")
        lines.append("")
        for q in sorted(side_atoms, key=district_key):
            atoms_for_q = [atom for atom in side_atoms[q] if atom.answer.strip()]
            if not atoms_for_q:
                continue
            prompt = prompts.get(q, q)
            lines.append(f"### {q}")
            lines.append("")
            lines.append(f"**题目锚点/设问**：{prompt}")
            lines.append("")
            for atom in atoms_for_q[:8]:
                lines.append(f"- **{atom.bucket} -> {display_core(q, atom.core)}**：{atom.answer} {side_reason(atom)}")
            lines.append("")

    lines.append("## 六桶术语积累复盘")
    lines.append("")
    for bucket in BUCKETS:
        bucket_cores = [(core, row) for (b, core), row in clusters.items() if b == bucket]
        for b, core in core_main_questions:
            if b == bucket and (b, core) not in clusters:
                bucket_cores.append((core, {"distinct_source_count": str(len(core_main_questions[(b, core)]))}))
        if not bucket_cores:
            continue
        lines.append(f"### {bucket}")
        for core, row in sorted(bucket_cores, key=lambda x: (-int(x[1].get("distinct_source_count") or 0), x[0])):
            q_list = core_main_questions.get((bucket, core), [])
            if not q_list:
                continue
            note = CORE_INDEX_NOTES.get(core, "")
            score_terms = scoring_terms_for_core(core, row)
            lines.append(f"#### {red(core)}")
            if note:
                lines.append(f"- 常见抓手：{note.strip('（）')}")
            accumulation = compact_accumulation(core, row.get('expression_accumulation', core))
            lines.append(f"- 踩分词：{format_scoring_terms(score_terms)}")
            lines.append(f"- 答题点自身积累（可替换表达，不必全背）：{highlight_scoring_terms(accumulation, score_terms)}")
            if core in PLAIN_NOTES:
                lines.append(f"- 白话提醒：{PLAIN_NOTES[core]}")
            questions = "；".join(q_list[:12])
            more = "等" if len(q_list) > 12 else ""
            lines.append(f"- 例题来源：{questions}{more}")
        lines.append("")

    OUT_MD.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

    with OUT_FREQ.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["bucket", "core_cluster", "question_count", "atom_count", "source_questions", "expression_accumulation"],
        )
        writer.writeheader()
        freq_rows = dict(clusters)
        for key, q_list in core_main_questions.items():
            if key not in freq_rows:
                freq_rows[key] = {
                    "distinct_source_count": str(len(q_list)),
                    "atom_count": "",
                    "source_questions": "；".join(q_list),
                    "expression_accumulation": key[1],
                }
        for (bucket, core), row in sorted(freq_rows.items(), key=lambda x: (BUCKET_ORDER.get(x[0][0], 99), x[0][1])):
            q_list = core_main_questions.get((bucket, core), [])
            writer.writerow(
                {
                    "bucket": bucket,
                    "core_cluster": core,
                    "question_count": str(len(q_list)),
                    "atom_count": row.get("atom_count", ""),
                    "source_questions": "；".join(q_list),
                    "expression_accumulation": compact_accumulation(core, row.get("expression_accumulation", core)),
                }
            )

    with OUT_TEACHER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "question",
                "bucket",
                "core",
                "atom_id",
                "scoring_position",
                "evidence_level",
                "status",
                "source_boundary",
                "boundary_note",
            ],
        )
        writer.writeheader()
        writer.writerows(teacher_rows)

    OUT_RUBRIC_REPAIR.parent.mkdir(parents=True, exist_ok=True)
    with OUT_RUBRIC_REPAIR.open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = [
            "question",
            "point_no",
            "basis",
            "bucket",
            "framework_core",
            "scoring_position",
            "red_scoring_terms",
            "answer_sentence",
            "evidence_level",
            "promotion_status",
            "source_boundary",
            "source_refs",
            "student_summary_status",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rubric_audit_rows)

    print(OUT_MD)
    print(OUT_FREQ)
    print(OUT_TEACHER)
    print(OUT_RUBRIC_REPAIR)


if __name__ == "__main__":
    main()
