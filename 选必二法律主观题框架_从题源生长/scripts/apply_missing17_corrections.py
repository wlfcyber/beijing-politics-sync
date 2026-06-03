#!/usr/bin/env python3
"""Apply the missing-17 evidence audit corrections.

This script is intentionally narrow: it only implements the audited correction
decisions recorded in 04_merge_audit/missing_evidence_17_review.*.
"""

import csv
import json
import shutil
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path

RUN_ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
TS = datetime.now().strftime("%Y%m%d_%H%M%S")


def read_csv(rel):
    path = RUN_ROOT / rel
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(rel, rows, fieldnames=None):
    path = RUN_ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(rel, rows):
    path = RUN_ROOT / rel
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def text_file(fid):
    return RUN_ROOT / "00_manifest" / "extracted_text" / f"{fid}.txt"


def manifest_by_id():
    out = {}
    for row in read_csv("00_manifest/source_manifest.csv"):
        out[row["file_id"]] = row
    return out


def joined_paths(fids, manifest):
    return "; ".join(
        f'{fid}: {manifest.get(fid, {}).get("original_file_path", "")}'
        for fid in fids
    )


def load_excerpt(fid, start, end):
    path = text_file(fid)
    if not path.exists():
        return ""
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    return "\n".join(lines[max(0, start - 1):end]).strip()


def backup_current():
    backup = RUN_ROOT / "04_merge_audit" / f"pre_missing17_correction_backup_{TS}"
    backup.mkdir(parents=True, exist_ok=True)
    rels = [
        "04_merge_audit/merged_subjective_law_questions.csv",
        "04_merge_audit/merged_subjective_law_questions.jsonl",
        "04_merge_audit/merged_material_atoms_subjective.csv",
        "04_merge_audit/merged_ask_atoms_subjective.csv",
        "04_merge_audit/merged_rubric_atoms_subjective.csv",
        "05_reasoner_packets/REASONER_INPUT_PACKET.md",
        "05_reasoner_packets/merged_subjective_law_questions_for_reasoners.csv",
        "05_reasoner_packets/merged_material_atoms_subjective_for_reasoners.csv",
        "05_reasoner_packets/merged_ask_atoms_subjective_for_reasoners.csv",
        "05_reasoner_packets/merged_rubric_atoms_subjective_for_reasoners.csv",
        "05_reasoner_packets/merge_audit_report_for_reasoners.md",
    ]
    for rel in rels:
        src = RUN_ROOT / rel
        if src.exists():
            dst = backup / rel.replace("/", "__")
            shutil.copy2(src, dst)
    return backup


def correction_data(manifest):
    return {
        "CC0002_2024_丰台_一模_17": {
            "level": "formal",
            "etype": "evaluation_standard",
            "rubric_file": joined_paths(["F0268", "F0044"], manifest),
            "rubric_text": load_excerpt("F0268", 16, 26),
            "answer_file": joined_paths(["F0045", "F0267"], manifest),
            "answer_text": load_excerpt("F0045", 173, 181) + "\n" + load_excerpt("F0045", 313, 313),
            "locator": "F0268:text lines 16-26; F0045:pages 4/8",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：丰台一模评标细则明确8分评分结构。",
            "atoms": [
                "法理依据5分：法院判决应以事实为依据，以法律为准绳，为必踩点1分。",
                "法理依据：双方形成好意同乘，需明确权利义务；涉及侵权责任一般规定，2分。",
                "法理依据：结合好意同乘事故减轻赔偿责任的条件和案件事实进行说明，2分。",
                "现实意义：维护双方合法权益，1分。",
                "现实意义：保障公正司法，1分。",
                "现实意义：弘扬社会主义核心价值观、促进社会和谐或绿色出行，1分。",
            ],
        },
        "CC0054_2024_石景山_一模_17": {
            "level": "formal",
            "etype": "lecture_explicit_scoring",
            "rubric_file": joined_paths(["F0055", "F0277", "F0276"], manifest),
            "rubric_text": load_excerpt("F0055", 308, 309),
            "answer_file": joined_paths(["F0056", "F0276"], manifest),
            "answer_text": load_excerpt("F0056", 98, 131),
            "locator": "F0055:slides/extracted lines 308-309; F0056:text lines 98-131",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：石景山一模讲评/教师版明确合同成立3分、判决意义5分。",
            "atoms": [
                "甲公司参与比选并向乙公司报价，内容具体确定，属于要约。",
                "乙公司确认甲公司中标并送达中标通知，属于承诺。",
                "中标通知书送达甲公司，双方合同成立，合同成立部分共3分。",
                "法院判决引导碳排放配额交易主体遵循诚信原则、公平原则、绿色原则。",
                "判决有利于推动企业转型升级，兼顾经济效益和社会效益。",
                "判决有利于维护碳排放权交易市场正常秩序、推动要素市场化改革、落实双碳决策。",
            ],
        },
        "CC0091_2025_东城_期末_19": {
            "level": "formal",
            "etype": "lecture_explicit_scoring",
            "rubric_file": joined_paths(["F0128", "F0129", "F0338", "F0340"], manifest),
            "rubric_text": load_excerpt("F0129", 46, 100),
            "answer_file": joined_paths(["F0130", "F0339"], manifest),
            "answer_text": load_excerpt("F0130", 208, 238),
            "locator": "F0129:slides 11-15; F0130:text around question 19",
            "status": "keep",
            "boundary": "综合",
            "confidence": "high",
            "reason": "missing17回源修正：东城期末19题为法律与政治法治综合主观题，讲评给出明确给分口径。",
            "atoms": [
                "19(1)：能指出设置充电柜是否违反消防规定等依法依规问题，每个具体问题1分。",
                "19(1)：能指出改变共有部分用途的法律程序问题，涉及民法典公共区域功能改变规定。",
                "19(1)：能指出公共区域设置充电柜可能涉及侵权、业主共有权、相邻权或人身财产权问题。",
                "19(2)：利益相关方需具体到充电设施供应商、街道或政府、居委会、消防部门等主体，每个主体1分。",
                "19(3)：法律与生活层面要写相邻关系、相邻关系原则、权利义务相统一或权利有界限，2分。",
                "19(3)：政治与法治层面要写民主协商、共同商讨、汇集民意集中民智或知情参与表达权，2分。",
            ],
        },
        "CC0119_2025_丰台_期末_19": {
            "level": "formal",
            "etype": "lecture_explicit_scoring",
            "rubric_file": joined_paths(["F0131", "F0342"], manifest),
            "rubric_text": load_excerpt("F0131", 220, 240),
            "answer_file": joined_paths(["F0132", "F0341"], manifest),
            "answer_text": load_excerpt("F0131", 220, 230),
            "locator": "F0131:slides 45-47",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：丰台期末细则PPT明确劳动裁判理由7分口径。",
            "atoms": [
                "法理依据：法院判决应以事实为依据、以法律为准绳，或写出相关法律规定，为必踩点1分。",
                "法理依据：劳动者应完成劳动任务，遵守劳动纪律和职业道德，1分。",
                "法理依据：尹某没有履行劳动者义务，违反法律规定或不符合敬业价值要求，2分。",
                "法理依据：购物中心根据劳动合同法规定解除劳动合同，1分。",
                "现实意义：保护用人单位合理用工自主权，1分。",
                "现实意义：引导劳动者坚持权利义务相统一，1分。",
                "现实意义：构建合理健康劳动关系或促进社会公平正义，1分。",
            ],
        },
        "CC0125_2025_延庆_一模_19": {
            "level": "formal",
            "etype": "evaluation_standard",
            "rubric_file": joined_paths(["F0077", "F0296"], manifest),
            "rubric_text": load_excerpt("F0296", 38, 48),
            "answer_file": joined_paths(["F0295", "F0296"], manifest),
            "answer_text": load_excerpt("F0295", 363, 370),
            "locator": "F0296:text around Q19; F0295:page 10",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：延庆一模答案细则明确调解方案与理由给分。",
            "atoms": [
                "调解结果：本案标的较小，本着以和为贵原则适用调解，1分。",
                "调解理由：消费者维权应遵循诚实信用原则，不能损害他人利益和社会经济秩序，诚信原则1分、材料分析1分。",
                "调解理由：杨某收到退款后买卖合同已解除，应依法退还货物，合同解除1分、材料分析1分。",
                "调解理由：杨某主张商品质量不合格但已丢弃商品，缺乏证据意识；证据意识1分、材料分析1分。",
                "商家角度：经营者应保证商品质量，若商品确有问题则不应追究消费者责任，可酌情给分。",
            ],
        },
        "CC0157_2025_朝阳_期末_20": {
            "level": "formal",
            "etype": "evaluation_standard",
            "rubric_file": joined_paths(["F0133", "F0345", "F0344"], manifest),
            "rubric_text": load_excerpt("F0133", 253, 304),
            "answer_file": joined_paths(["F0135", "F0343"], manifest),
            "answer_text": load_excerpt("F0343", 219, 288),
            "locator": "F0133:slides around Q20; F0343:teacher answer Q20",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：朝阳期末PPT/评标明确裁判要点给分。",
            "atoms": [
                "案件二裁判理由：根据反不正当竞争法，1分。",
                "案件二裁判理由：被告抓取并使用数据，损害原告数据合法权益和消费者利益，构成不正当竞争，1分。",
                "案件二裁判理由：破坏市场竞争秩序，违背商业道德和诚实信用原则，1分。",
                "案件二裁判结果：被告停止侵权或消除影响，1分。",
                "案件二裁判结果：被告赔偿原告经济损失及维权合理开支，1分。",
                "案件三裁判理由：根据民法典或消费者权益保护法，1分。",
                "案件三裁判理由：旅游公司工作人员过度摇晃桥面与甲摔落受伤存在因果关系，1分。",
                "案件三裁判理由：旅游公司有过错，应承担侵权责任，或侵犯身体权健康权，1分。",
                "案件三替代路径：旅游公司与甲构成合同关系，未提供充分有效安全保障，应承担违约责任。",
                "案件三裁判结果：乙旅游公司赔偿甲经济损失；甲自身存在一定过错时承担次要责任。",
            ],
        },
        "CC0162_2025_海淀_一模_18": {
            "level": "reference_only",
            "etype": "teacher_reference_answer",
            "rubric_file": joined_paths(["F0089", "F0305", "F0306"], manifest),
            "rubric_text": load_excerpt("F0305", 358, 360),
            "answer_file": joined_paths(["F0089", "F0305", "F0306"], manifest),
            "answer_text": load_excerpt("F0305", 358, 360),
            "locator": "F0305:text lines 358-360; no formal scoring source located in F0088/F0307",
            "status": "weak_reference_only",
            "boundary": "选必二",
            "confidence": "medium",
            "reason": "missing17二次保守修正：有教师版参考答案，但未找到正式评分细则；不得冒充formal。",
            "atoms": [
                "小黄与主题乐园签订的格式合同意思表示真实，条款符合公平原则，合同有效。",
                "小黄利用审查漏洞不当获利，违反合同约定，违背诚信原则。",
                "主题乐园可以根据合同约定采取撤销年卡方式解除合同。",
                "法院判决保护主题乐园合法权益，有利于营造公平公正市场环境。",
            ],
        },
        "CC0180_2025_海淀_期末_20": {
            "level": "formal",
            "etype": "lecture_explicit_scoring",
            "rubric_file": joined_paths(["F0138", "F0349"], manifest),
            "rubric_text": load_excerpt("F0138", 261, 280),
            "answer_file": joined_paths(["F0139", "F0348"], manifest),
            "answer_text": load_excerpt("F0139", 124, 154),
            "locator": "F0138:slides 39-41; F0139:text Q20",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：海淀期末20题讲评PPT给出侵权责任编解释评分口径。",
            "atoms": [
                "第十九条案例：生产者产品责任是无过错侵权责任，法理解释2分。",
                "第十九条案例：从消费者权利、安全消费权角度展开解释可替代得分。",
                "第十九条案例：意义部分写维护消费者合法权益等双方任一角度，1分。",
                "第二十五条案例：禁止饲养烈性犬等危险动物致害适用无过错侵权责任，法理解释2分。",
                "第二十五条案例：意义部分写强化饲养人责任、维护秩序、保障生命财产安全等，1分。",
                "若通篇没有无过错侵权责任，不能得满分；把烈性犬案例写成过错推定，法理部分不给分。",
            ],
        },
        "CC0181_2025_海淀_期末_21": {
            "level": "formal",
            "etype": "lecture_explicit_scoring",
            "rubric_file": joined_paths(["F0138", "F0349"], manifest),
            "rubric_text": load_excerpt("F0138", 299, 332),
            "answer_file": joined_paths(["F0139", "F0348"], manifest),
            "answer_text": load_excerpt("F0139", 127, 176),
            "locator": "F0138:slides 46-47; F0139:text Q21",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：海淀期末21题讲评PPT给出竞业限制6+2评分细则。",
            "atoms": [
                "规范竞业限制的意义：有利于企业商业秘密保护、保护知识产权、推动社会创新，任意两条给2分。",
                "限制竞业限制的意义：保护劳动者基本劳动权利或有利于人才资源合理配置，2分。",
                "总结：平衡劳动者合法权益与企业商业秘密保护，2分；维护市场公平竞争等可替代1分。",
                "案例一分析：李某作为负有保密义务的劳动者，泄露商业秘密或违反协议，应承担违约责任，1分。",
                "案例二分析：刘某为普通员工、并非负有保密义务人员，竞业限制协议违法无效，1分。",
            ],
        },
        "CC0213_2025_门头沟_一模_20": {
            "level": "formal",
            "etype": "evaluation_standard",
            "rubric_file": joined_paths(["F0095", "F0313"], manifest),
            "rubric_text": load_excerpt("F0095", 38, 55),
            "answer_file": joined_paths(["F0096", "F0312"], manifest),
            "answer_text": load_excerpt("F0096", 300, 350),
            "locator": "F0095:text lines 38-55; F0096:text Q20",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：门头沟一模旧Word细则经文本抽取可用，明确裁判要点分值。",
            "atoms": [
                "裁判结果：驳回或不支持孙某诉讼请求，1分。",
                "裁判结果：甲公司无需支付赔偿金，1分。",
                "裁判理由：根据劳动合同法，订立劳动合同应遵循诚实信用原则，1分。",
                "裁判理由：孙某违反诚实信用原则、劳动者基本职业道德或侵犯甲公司知情权，1分。",
                "裁判理由：甲公司在违背真实意思情况下签订劳动合同，或劳动合同无效，1分。",
                "裁判理由：甲公司解除劳动关系符合法律规定、解除行为无过错，1分。",
                "现实意义：维护用人单位合法权益，1分。",
                "现实意义：约束劳动者行为或有利于劳动者遵守职业道德，1分。",
                "现实意义：有利于和谐劳动关系构建、弘扬诚信核心价值观或维护公平正义，1分。",
            ],
        },
        "CC0223_2025_顺义_一模_19": {
            "level": "formal",
            "etype": "evaluation_standard",
            "rubric_file": joined_paths(["F0097", "F0315"], manifest),
            "rubric_text": load_excerpt("F0097", 46, 55),
            "answer_file": joined_paths(["F0098", "F0314"], manifest),
            "answer_text": load_excerpt("F0314", 271, 292),
            "locator": "F0097:text lines 46-55; F0314:text Q19",
            "status": "keep",
            "boundary": "综合",
            "confidence": "high",
            "reason": "missing17回源修正：顺义一模19题评分细则明确诉讼调解、相邻关系与定分止争价值。",
            "atoms": [
                "案例1解决纠纷方式：法院坚持诉讼调解实现邻里和谐、实质化解纠纷，1分。",
                "案例1理由：通道属于建筑物共有部分，应合理限度恰当使用；堆放垃圾杂物影响通行并违反民法典相邻权规定，1分。",
                "案例1要求：相邻各方按有利生产、方便生活、团结互助、公平合理原则正确处理相邻关系，1分。",
                "材料二价值：民事主体行使权利不得超过正当界限，不得损害国家、社会和他人合法权益。",
                "价值：选择适当途径解决纠纷，践行文明、和谐等社会主义核心价值观。",
                "价值：多元纠纷解决机制协调运行，能协调利益、化解社会矛盾、实现社会和谐、提升治理水平。",
            ],
        },
        "CC0238_2026_东城_二模_19": {
            "level": "formal",
            "etype": "marking_rubric",
            "rubric_file": joined_paths(["F0184"], manifest),
            "rubric_text": load_excerpt("F0184", 1, 20),
            "answer_file": joined_paths(["F0186"], manifest),
            "answer_text": load_excerpt("F0186", 136, 145),
            "locator": "F0184:pages 1-3; F0186:text around answer",
            "status": "keep",
            "boundary": "选必二",
            "confidence": "high",
            "reason": "missing17回源修正：东城二模19题阅卷细则为formal。",
            "atoms": [
                "乙公司以商业诋毁获取竞争优势，2分；构成不正当竞争或违背诚信原则可替代1分。",
                "乙公司未全面履行合同，构成违约，1分。",
                "乙公司应承担赔偿损失等违约责任，为必出点1分。",
                "张某未遵守或违反劳动纪律与职业道德，2分。",
                "应然表达：市场主体应依法诚信经营，或劳动者权利与义务相统一、应履行义务，1分。",
                "总结：市场经济就是法治经济，或共同营造公平竞争的市场环境，必出1分。",
            ],
        },
        "CC0311_2026_海淀_二模_18": {
            "level": "reference_only",
            "etype": "teacher_reference_answer",
            "rubric_file": joined_paths(["F0197", "F0196"], manifest),
            "rubric_text": load_excerpt("F0197", 175, 185),
            "answer_file": joined_paths(["F0197"], manifest),
            "answer_text": load_excerpt("F0197", 116, 154),
            "locator": "F0197:text Q18 answer; F0196 lecture mostly watermark/OCR risk",
            "status": "weak_reference_only",
            "boundary": "选必二",
            "confidence": "medium",
            "reason": "missing17回源修正：教师版有8分参考答案，但未取得明确评分细则。",
            "atoms": [
                "知识产权是财产权的重要组成部分，也是企业重要的无形资产。",
                "民法典将知识产权中的财产权纳入可质押权利范围，有利于拓宽融资渠道、缓解资金压力。",
                "公司法确认知识产权可以作价出资，促进技术要素转化资本，鼓励创业创新。",
                "专利法规定对发明人给予奖励和合理报酬，尊重创新主体权益，调动员工创新积极性。",
                "法律规定保护知识产权权利人合法权益，促进知识产权流通使用，为企业创新发展提供法治保障。",
            ],
        },
    }


DELETE_IDS = {
    "CC0096_2025_东城_期末_21",
    "CC0121_2025_丰台_期末_21",
    "CC0226_2025_顺义_一模_21",
    "CC0314_2026_海淀_二模_21",
}


def atom_type(phrase):
    has_knowledge = any(x in phrase for x in ["民法典", "法律", "合同", "侵权", "权利", "义务", "责任", "原则", "竞业", "著作权", "知识产权", "劳动", "相邻", "不正当竞争", "证据", "调解", "法治"])
    has_value = any(x in phrase for x in ["意义", "有利于", "维护", "弘扬", "促进", "保障", "公平", "和谐", "市场环境", "核心价值观"])
    has_material = any(x in phrase for x in ["本案", "甲", "乙", "小黄", "李某", "刘某", "杨某", "孙某", "张某", "公司", "法院", "充电", "旅游", "主题乐园", "案例"])
    if has_knowledge and has_material and has_value:
        return "knowledge+material+value"
    if has_knowledge and has_material:
        return "knowledge+material"
    if has_knowledge and has_value:
        return "knowledge+value"
    if has_material and has_value:
        return "material+value"
    if has_knowledge:
        return "knowledge"
    if has_material:
        return "material"
    if has_value:
        return "value"
    return "uncertain"


def build_rubric_atoms(qid, cfg, material_ids):
    atoms = []
    related = "|".join(material_ids[:4])
    for idx, phrase in enumerate(cfg["atoms"], 1):
        kt = atom_type(phrase)
        atoms.append({
            "rubric_atom_id": f"R_{qid}_M17_{idx:02d}",
            "question_id": qid,
            "rubric_or_answer_phrase": phrase,
            "evidence_type": cfg["etype"],
            "evidence_level": cfg["level"],
            "plain_reward_description": phrase,
            "related_material_atom_ids": related,
            "what_expression_is_rewarded": phrase,
            "what_judgment_student_must_make_before_writing": "判断材料中的主体关系、行为性质、权利义务或责任/制度作用，再按细则落句。",
            "legal_knowledge_or_rule_if_explicit": "；".join([x for x in ["合同", "侵权", "诚信原则", "公平原则", "相邻关系", "竞业限制", "知识产权", "劳动合同", "调解", "不正当竞争"] if x in phrase]),
            "value_expression_if_explicit": "；".join([x for x in ["公平", "和谐", "社会主义核心价值观", "市场环境", "法治保障", "公平竞争", "合法权益"] if x in phrase]),
            "knowledge_material_value_type": kt,
            "can_be_written_without_material": "no" if "material" in kt else "uncertain",
            "source_locator": cfg["locator"],
            "uncertainty": "missing17_correction_atom; formal/reference level follows source audit",
        })
    return atoms


def main():
    backup = backup_current()
    manifest = manifest_by_id()
    corrections = correction_data(manifest)

    merged = read_csv("04_merge_audit/merged_subjective_law_questions.csv")
    material = read_csv("04_merge_audit/merged_material_atoms_subjective.csv")
    ask = read_csv("04_merge_audit/merged_ask_atoms_subjective.csv")
    rubric = read_csv("04_merge_audit/merged_rubric_atoms_subjective.csv")

    merged_fields = list(merged[0].keys())
    material_fields = list(material[0].keys())
    ask_fields = list(ask[0].keys())
    rubric_fields = list(rubric[0].keys())

    before_counts = Counter(row.get("evidence_level", "") for row in merged)

    excluded = [row for row in merged if row["question_id"] in DELETE_IDS]
    merged = [row for row in merged if row["question_id"] not in DELETE_IDS]
    material = [row for row in material if row["question_id"] not in DELETE_IDS]
    ask = [row for row in ask if row["question_id"] not in DELETE_IDS]
    rubric = [row for row in rubric if row["question_id"] not in DELETE_IDS and row["question_id"] not in corrections]

    material_ids_by_qid = {}
    for row in material:
        material_ids_by_qid.setdefault(row["question_id"], []).append(row["material_atom_id"])

    for row in merged:
        qid = row["question_id"]
        if qid not in corrections:
            continue
        cfg = corrections[qid]
        row["answer_file"] = cfg["answer_file"]
        row["answer_text"] = cfg["answer_text"]
        row["rubric_file"] = cfg["rubric_file"]
        row["rubric_text"] = cfg["rubric_text"]
        row["evidence_type"] = cfg["etype"]
        row["evidence_level"] = cfg["level"]
        row["module_boundary_risk"] = cfg["boundary"]
        row["confidence"] = cfg["confidence"]
        row["source_locator"] = (row.get("source_locator", "") + " | " + cfg["locator"]).strip(" |")
        row["merge_status"] = cfg["status"]
        row["merge_decision_reason"] = cfg["reason"]
        notes = row.get("notes", "")
        row["notes"] = (notes + " | missing17_corrected_20260519").strip(" |")

    for qid, cfg in corrections.items():
        rubric.extend(build_rubric_atoms(qid, cfg, material_ids_by_qid.get(qid, [])))

    write_csv("04_merge_audit/merged_subjective_law_questions.csv", merged, merged_fields)
    write_jsonl("04_merge_audit/merged_subjective_law_questions.jsonl", merged)
    write_csv("04_merge_audit/merged_material_atoms_subjective.csv", material, material_fields)
    write_csv("04_merge_audit/merged_ask_atoms_subjective.csv", ask, ask_fields)
    write_csv("04_merge_audit/merged_rubric_atoms_subjective.csv", rubric, rubric_fields)
    write_csv("04_merge_audit/missing17_deleted_false_positives.csv", excluded, merged_fields)

    missing_after = [row for row in merged if row.get("evidence_level") == "missing" or row.get("merge_status") == "pending_evidence"]
    write_csv("04_merge_audit/missing_evidence_after_missing17_correction.csv", missing_after, merged_fields)

    reasoner_qids = {
        row["question_id"]
        for row in merged
        if row.get("evidence_level") in {"formal", "reference_only", "user_confirmed"}
        and row.get("merge_status") not in {"blocked", "deleted", "pending_evidence"}
    }
    reasoner_rows = [row for row in merged if row["question_id"] in reasoner_qids]
    reasoner_material = [row for row in material if row["question_id"] in reasoner_qids]
    reasoner_ask = [row for row in ask if row["question_id"] in reasoner_qids]
    reasoner_rubric = [row for row in rubric if row["question_id"] in reasoner_qids]

    write_csv("05_reasoner_packets/merged_subjective_law_questions_for_reasoners.csv", reasoner_rows, merged_fields)
    write_csv("05_reasoner_packets/merged_material_atoms_subjective_for_reasoners.csv", reasoner_material, material_fields)
    write_csv("05_reasoner_packets/merged_ask_atoms_subjective_for_reasoners.csv", reasoner_ask, ask_fields)
    write_csv("05_reasoner_packets/merged_rubric_atoms_subjective_for_reasoners.csv", reasoner_rubric, rubric_fields)

    level_counts = Counter(row.get("evidence_level", "") for row in merged)
    status_counts = Counter(row.get("merge_status", "") for row in merged)
    reasoner_level_counts = Counter(row.get("evidence_level", "") for row in reasoner_rows)

    report = f"""# Merge Audit Report

generated_at: 2026-05-19T{datetime.now().strftime('%H:%M:%S')}+08:00

## Verdict

CONDITIONAL_PASS_AFTER_MISSING17_CORRECTION.

The missing-17 review corrected stale evidence links before official external-model observation. No codebook or framework is authorized yet.

## Counts

- Merged canonical candidates after false-positive removal: {len(merged)}
- Deleted false positives from missing17: {len(excluded)}
- Missing/pending evidence after correction: {len(missing_after)}
- Reasoner packet rows: {len(reasoner_rows)}
- Reasoner material atoms: {len(reasoner_material)}
- Reasoner ask atoms: {len(reasoner_ask)}
- Reasoner rubric/answer atoms: {len(reasoner_rubric)}

## Evidence Level Counts

{chr(10).join(f'- {k}: {v}' for k, v in sorted(level_counts.items()))}

## Reasoner Evidence Level Counts

{chr(10).join(f'- {k}: {v}' for k, v in sorted(reasoner_level_counts.items()))}

## Merge Status Counts

{chr(10).join(f'- {k}: {v}' for k, v in sorted(status_counts.items()))}

## Missing17 Correction

- upgrade_formal: 11
- upgrade_reference_only: 2
- delete_false_positive: 4

`CC0162_2025_海淀_一模_18` was downgraded from the preliminary review's formal plan to `reference_only` because a formal scoring source was not located; the teacher answer is usable only for weak observation.

## Still Forbidden

Do not output a framework yet. GPT-5.5 Pro and Claude Opus must be rerun with the corrected v3 packet and their outputs must be cross-validated before any codebook or framework work.
"""
    (RUN_ROOT / "04_merge_audit/merge_audit_report.md").write_text(report, encoding="utf-8")
    (RUN_ROOT / "05_reasoner_packets/merge_audit_report_for_reasoners.md").write_text(report, encoding="utf-8")

    packet = f"""# REASONER_INPUT_PACKET

generated_at: 2026-05-19T{datetime.now().strftime('%H:%M:%S')}+08:00
packet_version: v3_corrected_missing17

## 工程目标

从 2024-2026 北京各区选必二《法律与生活》主观题与评分证据中，开放归纳命题机制、判分机制和学生作答机制。本轮只做观察，不写框架。

## Scope

- 只研究主观题。
- 选择题不进入框架，不分析错项。
- 不预设“一核二线三问四步五域”“动作库”“故事卡”“法律关系路由”。
- 不按教材目录先搭框架。
- 参考答案不得冒充评分细则。

## Missing17 Correction Notice

旧 v2 包中的 `missing=17` 已复核：

- 11 条升级为 formal。
- 2 条保守升级为 reference_only。
- 4 条选择题解析/非法律主观题误抓已剔除。
- 修正后 merged candidates = {len(merged)}。
- 修正后 missing/pending evidence = {len(missing_after)}。

## Data Range

- reasoner packet rows: {len(reasoner_rows)}
- formal rows in packet: {reasoner_level_counts.get('formal', 0)}
- reference_only rows in packet: {reasoner_level_counts.get('reference_only', 0)}
- material atoms: {len(reasoner_material)}
- ask atoms: {len(reasoner_ask)}
- rubric/answer atoms: {len(reasoner_rubric)}

Reference_only rows may support weak observations only and cannot independently support core codebook nodes.

## Input Files

- merged_subjective_law_questions_for_reasoners.csv
- merged_material_atoms_subjective_for_reasoners.csv
- merged_ask_atoms_subjective_for_reasoners.csv
- merged_rubric_atoms_subjective_for_reasoners.csv
- merge_audit_report_for_reasoners.md

## Unified Task

基于每一道题的 question_id、rubric_atom_id、material_atom_id，逐题分析模块边界、设问任务、最小必要判断、材料事实与细则触发、得分机制、满分句生成、迁移与代码本资格。

## Output Requirement

每条 observation 必须包含 evidence ids；没有 question_id、rubric_atom_id、material_atom_id 的观察不得进入下一轮。最后分为强观察、弱观察、冲突观察、不应上升为框架的观察、下一轮需补充题型。

本轮禁止输出总框架。
"""
    (RUN_ROOT / "05_reasoner_packets/REASONER_INPUT_PACKET.md").write_text(packet, encoding="utf-8")

    zip_path = RUN_ROOT / "05_reasoner_packets" / "reasoner_packet_v3_corrected_missing17_20260519.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for rel in [
            "05_reasoner_packets/REASONER_INPUT_PACKET.md",
            "05_reasoner_packets/merged_subjective_law_questions_for_reasoners.csv",
            "05_reasoner_packets/merged_material_atoms_subjective_for_reasoners.csv",
            "05_reasoner_packets/merged_ask_atoms_subjective_for_reasoners.csv",
            "05_reasoner_packets/merged_rubric_atoms_subjective_for_reasoners.csv",
            "05_reasoner_packets/merge_audit_report_for_reasoners.md",
            "04_merge_audit/missing_evidence_17_review.csv",
            "04_merge_audit/missing_evidence_17_review.md",
            "04_merge_audit/missing17_deleted_false_positives.csv",
            "04_merge_audit/missing_evidence_after_missing17_correction.csv",
        ]:
            zf.write(RUN_ROOT / rel, arcname=Path(rel).name)
    shutil.copy2(zip_path, RUN_ROOT / "05_reasoner_packets" / "reasoner_packet_20260519.zip")

    summary = {
        "backup": str(backup),
        "before_level_counts": dict(before_counts),
        "after_level_counts": dict(level_counts),
        "after_status_counts": dict(status_counts),
        "merged_after": len(merged),
        "reasoner_rows": len(reasoner_rows),
        "reasoner_material_atoms": len(reasoner_material),
        "reasoner_ask_atoms": len(reasoner_ask),
        "reasoner_rubric_atoms": len(reasoner_rubric),
        "missing_after": len(missing_after),
        "deleted_false_positives": len(excluded),
        "zip": str(zip_path),
    }
    (RUN_ROOT / "tool_outputs" / "missing17_correction_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
