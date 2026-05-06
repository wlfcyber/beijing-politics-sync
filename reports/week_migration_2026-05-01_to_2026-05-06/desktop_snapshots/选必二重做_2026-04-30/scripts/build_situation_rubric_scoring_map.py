#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import re
from collections import Counter, defaultdict
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30")
SCRIPTS = BASE / "scripts"
DELIVERY = BASE / "delivery"

MD = DELIVERY / "选必二考过情境穷尽与细则踩分表_教师备课版_2026-05-04.md"
DOCX = DELIVERY / "选必二考过情境穷尽与细则踩分表_教师备课版_2026-05-04.docx"
HTML = DELIVERY / "选必二考过情境穷尽与细则踩分表_教师备课版_2026-05-04.html"
CSV_OUT = DELIVERY / "选必二考过情境穷尽与细则踩分索引_教师备课版_2026-05-04.csv"


def load_final_builder():
    path = SCRIPTS / "build_final_delivery_clean.py"
    spec = importlib.util.spec_from_file_location("legal_final_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER = load_final_builder()


SITUATION_RULES: list[tuple[str, list[str], str]] = [
    ("平台用工与新就业形态劳动关系", ["平台", "骑手", "派单", "劳动关系", "劳动仲裁", "从属性", "经济补偿", "新就业"], "先看是否只是合作外观，再用人格、经济、组织从属性判断是否形成劳动关系。"),
    ("劳动合同解除、工资、录用通知与竞业限制", ["劳动合同", "用人单位", "工资", "辞退", "解除", "录用通知", "竞业限制", "商业秘密", "择业自由"], "先看劳动者保护和用人单位管理边界，再落解除、补偿、违约或协议效力。"),
    ("合同成立、合同效力与违约责任", ["合同", "要约", "承诺", "中标", "履行", "违约", "不可抗力", "差价款", "定金"], "先看意思表示是否一致、合同是否有效，再落继续履行、赔偿、解除或违约责任。"),
    ("消费者权益、虚假宣传、格式条款与平台规则", ["消费者", "经营者", "知情权", "公平交易权", "安全权", "欺诈", "虚假宣传", "格式条款", "惩罚性赔偿", "仅退款", "生鲜灯", "直播"], "先看经营者是否真实诚信、是否尽提示说明义务，再落退赔、赔偿或惩罚性赔偿。"),
    ("未成年交易、直播打赏与监护责任", ["未成年", "限制民事行为能力", "打赏", "监护", "父母", "平台"], "先看行为能力和交易数额是否相适应，再看追认、返还、平台责任和监护责任。"),
    ("物权归属、担保物权、登记交付与绿色物权", ["物权", "所有权", "他物权", "抵押", "质押", "担保", "登记", "交付", "碳排放", "绿色原则"], "先看权利种类和公示方式，再落归属、效力、担保或绿色边界。"),
    ("小区共有部分、相邻关系、物业与排除妨碍", ["小区", "共有部分", "通行", "相邻", "物业", "漏雨", "排除妨碍", "恢复"], "先看共有和相邻利益平衡，再落停止侵害、排除妨碍、恢复状态或赔偿。"),
    ("继承、遗嘱、遗赠扶养协议与赡养义务", ["继承", "遗嘱", "遗产", "遗赠扶养", "赡养", "扶养", "精神慰藉", "法定继承"], "先看身份和协议/遗嘱效力，再落遗产归属、赡养扶助和家庭伦理。"),
    ("公共场所受伤、安全保障义务与一般侵权", ["景区", "商场", "学校", "游客", "受伤", "安全保障义务", "医疗费", "伤残", "过错", "因果"], "先看行为、损害、因果和过错，再判断管理者是否尽到合理限度内安全保障义务。"),
    ("运动伤害、见义勇为、产品动物高空等特殊侵权", ["运动", "足球", "羽毛球", "见义勇为", "救助", "动物", "高空", "公平补偿", "无过错", "缺陷产品", "产品责任", "危险动物", "归责原则"], "先识别一般侵权还是特殊规则，再落免责、减责、补偿或无过错责任。"),
    ("肖像、名誉、隐私、个人信息与网络侵权", ["肖像", "名誉", "隐私", "个人信息", "照片", "视频", "匿名", "曝光", "评价", "未经同意"], "先说具体人格利益，再看是否未经同意、公开传播、歪曲贬损或泄露。"),
    ("著作权、AI作品、虚拟数字人与作品使用", ["著作权", "作品", "独创性", "AI", "人工智能", "虚拟数字人", "复制权", "信息网络传播权", "署名权", "图片", "摄影"], "先判断是否属于受保护作品和权利主体，再落未经许可使用、署名、报酬和侵权责任。"),
    ("商标、商业标识、混淆与不正当竞争", ["商标", "注册商标", "商业标识", "包装", "混淆", "不正当竞争", "假冒", "知名商品"], "先看标识是否足以导致混淆，再落商标侵权、不正当竞争和市场秩序。"),
    ("商业秘密、数据抓取、专利与创新司法保护", ["商业秘密", "数据", "抓取", "专利", "植物新品种", "恶意诉讼", "惩罚性赔偿", "创新", "知识产权"], "先看创新成果或竞争利益，再用司法救济保护权利、维护诚信竞争和创新秩序。"),
    ("调解、仲裁、诉讼、司法确认、执行与举证", ["调解", "仲裁", "诉讼", "司法确认", "强制执行", "举证", "二审", "上诉", "诉讼时效", "抗辩权"], "先看纠纷解决路径和程序效果，再落举证、执行力、诉讼时效或裁判理由。"),
    ("公益诉讼、生态修复、司法建议与公共利益", ["公益诉讼", "生态", "环境", "古树", "文物", "司法建议", "修复", "公共利益"], "先看适格主体和公共利益受损，再落公益诉讼、生态修复、司法建议或公共治理意义。"),
]


SCORING_TERMS = [
    "以事实为根据", "以法律为准绳", "定分止争", "劳动关系", "事实上的劳动关系", "人格从属性", "经济从属性", "组织从属性",
    "劳动者权益", "新就业形态劳动者", "和谐稳定的劳动关系", "经济补偿", "竞业限制", "商业秘密", "择业自由", "保密义务",
    "合同成立", "合同合法有效", "要约", "承诺", "意思表示一致", "诚信原则", "违约责任", "继续履行", "赔偿损失", "不可抗力",
    "消费者合法权益", "知情权", "公平交易权", "安全权", "自主选择权", "欺诈", "虚假宣传", "格式条款", "提示说明义务", "惩罚性赔偿",
    "限制民事行为能力人", "追认", "监护责任", "平台责任", "所有权", "物权", "共有部分", "共同管理", "相邻关系", "停止侵害",
    "排除妨碍", "恢复原状", "绿色原则", "公序良俗", "遗赠扶养协议", "遗嘱", "法定继承", "遗产归属", "赡养义务", "扶养义务",
    "精神慰藉", "家庭美德", "人格权", "肖像权", "名誉权", "隐私权", "个人信息", "侵权责任", "过错", "损害", "因果关系",
    "安全保障义务", "停止侵害", "消除影响", "赔礼道歉", "赔偿损失", "见义勇为", "公平补偿", "著作权", "作品", "独创性",
    "复制权", "信息网络传播权", "署名权", "保护作品完整权", "商标", "注册商标专用权", "不正当竞争", "混淆", "市场秩序",
    "知识产权", "保护创新", "创新活力", "惩罚性赔偿", "恶意诉讼", "滥用诉讼权利", "调解", "仲裁", "诉讼", "举证责任",
    "司法确认", "强制执行", "诉讼时效", "抗辩权", "公益诉讼", "生态修复", "公共利益", "司法建议", "合法权益", "公平正义",
    "核心价值观", "人文关怀", "社会公平正义",
]


def clean(value: str | None, limit: int | None = None) -> str:
    text = BUILDER.clean_text(value or "")
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[:limit].rstrip() + "……"
    return text


def strip_paths(value: str | None) -> str:
    text = value or ""
    text = re.sub(r"/Users/[^\n，。；;）)】]+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def source_label(record: dict) -> str:
    if record.get("question_type") == "choice":
        if record.get("answer_source"):
            return f"{record.get('suite_name') or record.get('year') + record.get('district') + record.get('stage')} 第{record.get('question_no')}题答案表/题肢来源"
        return f"{record.get('suite_name')} 第{record.get('question_no')}题客观题来源待锁定"
    return f"{record.get('suite_name')} 第{record.get('question_no')}题细则/给分依据"


def situation_for(record: dict) -> tuple[str, str]:
    hay = " ".join(
        [
            record.get("label", ""),
            record.get("framework_domain", ""),
            record.get("front_domain", ""),
            record.get("material_triggers", ""),
            record.get("complete_prompt", ""),
            record.get("question_text", ""),
            record.get("answer_points", ""),
        ]
    )
    best_name = "其他法律情境（保留待复核）"
    best_reason = "本题法律信号较分散，先保留在其他情境中，不强行改写成固定母题。"
    best_score = 0
    for name, kws, reason in SITUATION_RULES:
        score = sum(1 for kw in kws if kw in hay)
        if score > best_score:
            best_name, best_reason, best_score = name, reason, score
    if best_score == 0:
        return best_name, best_reason
    return best_name, best_reason


def scoring_terms(text: str) -> str:
    terms = [term for term in SCORING_TERMS if term in text]
    seen: list[str] = []
    for term in terms:
        if term not in seen:
            seen.append(term)
    return "；".join(seen[:16]) or "需按对应细则原句提取，暂不另造踩分词。"


def split_sentences(text: str, limit: int = 7) -> list[str]:
    text = clean(text)
    chunks = re.split(r"(?<=[。；;])\s*|(?<=）)\s*", text)
    out: list[str] = []
    for chunk in chunks:
        chunk = chunk.strip(" ；;。")
        if not chunk:
            continue
        if len(chunk) < 6:
            continue
        out.append(chunk + "。")
        if len(out) >= limit:
            break
    if not out and text:
        out.append(clean(text, 260))
    return out


def trim_to_legal_rubric(record: dict, text: str) -> str:
    text = clean(text)
    if not text:
        return ""
    qno = record.get("question_no", "")
    sub_nums = re.findall(r"[（(]\s*(\d+)\s*[）)]", record.get("complete_prompt", ""))
    if qno and sub_nums:
        sub = sub_nums[-1]
        qsub = re.search(rf"(?<!\d){re.escape(qno)}\s*[（(]\s*{sub}\s*[）)]", text)
        if qsub:
            text = text[qsub.start():]
    # Many PPT rubrics contain broad讲评方法 before the actual answer.
    # Prefer the first strong legal scoring marker, not the first slide.
    marker_patterns = [
        r"整体作答思路",
        r"具体[:：]",
        r"给分依据、答案变通说明",
        r"阅卷前制定的答案要点",
        r"答案要点[:：]",
        r"参考答案",
        r"评分细则",
        r"给分依据[:：]?",
        r"【违约逻辑",
        r"第一层[:：]",
        r"第二层[:：]",
        r"(?<!\d)[（(]\s*3\s*[）)]\s*①支持原告诉讼请求",
        r"①支持原告诉讼请求",
        r"甲公司参与比选",
        r"本案中，",
        r"调解理由[:：]",
        r"郑某利[用⽤]",
        r"AI不具备民事主体资格",
        r"小刘为限制民事行为能力人",
        r"经营者应依法",
        r"规范竞业限制",
        r"案例一[:：]",
        r"法理依据",
        r"“最严格的无过错责任”立法精神",
        r"权利义务\+利益考量",
        r"根据民法典规定",
        r"根据消费者权益保护法",
    ]
    positions: list[int] = []
    for pattern in marker_patterns:
        match = re.search(pattern, text)
        if match:
            positions.append(match.start())
    if positions:
        text = text[min(positions):]
    # If a mixed-module answer keeps earlier subquestions, cut to the legal subquestion.
    if sub_nums:
        sub = sub_nums[-1]
        sub_patterns = [
            rf"[（(]\s*{sub}\s*[）)]\s*①",
            rf"[（(]\s*{sub}\s*[）)]",
        ]
        sub_positions = []
        for pattern in sub_patterns:
            match = re.search(pattern, text)
            if match:
                sub_positions.append(match.start())
        if sub_positions:
            text = text[min(sub_positions):]
        next_sub = str(int(sub) + 1) if sub.isdigit() else ""
        if next_sub:
            next_match = re.search(rf"(?<!\d){re.escape(qno)}\s*[（(]\s*{next_sub}\s*[）)]", text) if qno else None
            if next_match and next_match.start() > 180:
                text = text[:next_match.start()]
    stop_patterns = [
        r"\s高三思想政治(?:参考答案|答案要点)?\s*第\s*\d+\s*页",
        r"\[slide\s+\d+\]\s*(?:公民公共参与|学生答题情况|复习建议|教学建议|反馈试题|问题[:：])",
        r"\s(?:公民公共参与|国家机关[:：]|社会团体[:：])",
        r"\s(?:学生答题情况|复习建议|教学建议|反馈试题|暴露的问题及建议)[:：]?",
    ]
    for pattern in stop_patterns:
        match = re.search(pattern, text)
        if match and match.start() > 80:
            text = text[:match.start()]
            break
    text = re.sub(r"\[slide\s+\d+\]\s*", "", text)
    text = re.sub(r"高三思想政治(?:参考答案|答案要点)?\s*第\s*\d+\s*页", "", text)
    return clean(text, 1400)


def rubric_for(record: dict) -> str:
    if record.get("question_type") == "choice":
        ans = clean(record.get("answer"))
        wrong = clean(record.get("wrong_option_sentences"), 520)
        points = clean(record.get("answer_points"), 260)
        if ans:
            return "；".join(x for x in [f"答案：{ans}", points, wrong] if x)
        return points or "答案源待核验。"
    raw = record.get("rubric_text") or record.get("answer_points")
    refined = BUILDER.refined_rubric(record)
    candidates = [trim_to_legal_rubric(record, raw), trim_to_legal_rubric(record, refined)]
    candidates = [c for c in candidates if c]
    if not candidates:
        return ""
    def quality_score(text: str) -> int:
        bad = sum(1 for pat in ["现实逻辑", "全国居民人均", "无人机起飞如何", "学生答题情况", "教学建议"] if pat in text[:160])
        good = sum(1 for term in SCORING_TERMS if term in text)
        good += len(re.findall(r"\d+\s*分|①|②|③|【.+?逻辑", text))
        return good * 10 - bad * 60 - max(0, len(text) - 1400) // 80
    return max(candidates, key=quality_score)


def is_suspect_subjective(record: dict, rubric: str) -> bool:
    if record.get("question_type") != "subjective":
        return False
    if record.get("include_status") == "included_needs_review":
        return True
    bad_tokens = ["政治与法治", "哲学与文化", "逻辑与思维", "公民公共参与", "全过程人民民主", "民营经济规模", "学生答题情况", "复习建议"]
    return any(token in rubric for token in bad_tokens)


def evidence_label(record: dict, rubric: str = "") -> str:
    qtype = record.get("question_type")
    etype = record.get("evidence_type", "")
    status = record.get("evidence_status", "")
    if qtype == "choice":
        if record.get("answer"):
            return "客观题答案已锁定；只能作为选择题判断与情境信号，不直接生成主观题踩分句。"
        return "客观题答案未锁定；只保留情境，不写死错项和采分词。"
    if "formal" in etype or "formal" in status or etype == "formal_or_scoring_source":
        if is_suspect_subjective(record, rubric):
            return "主观题有细则来源，但属于复合题/二次匹配/摘录需复核；先保留原句，不直接进入学生背诵核心。"
        return "主观题细则已锁定；可以提炼踩分词和上卷面句。"
    if etype in {"reference_answer", "support_lecture_or_review", "support_lecture"}:
        return "非正式细则或讲评来源；可作提示，不推动主观题踩分句。"
    return "主观题细则待核验；暂不推动确定踩分句。"


def score_sentence(record: dict, rubric: str) -> str:
    if record.get("question_type") == "choice":
        ans = clean(record.get("answer"))
        if ans:
            return f"本题客观落点是{ans}；训练价值在于排除主体错位、关系错位、责任错位或程序错位。"
        return "本题只保留为选择题情境，待答案源核验后再写锁分判断。"
    sentences = split_sentences(rubric, 4)
    if not sentences:
        return "待细则核验后再生成可上卷面的得分句。"
    # Prefer legal result sentences before value-only sentences.
    preferred = []
    for sentence in sentences:
        sentence = re.sub(r"^(?:给分依据|理由[:：]?|答案要点[:：]?).*?(甲公司|王某|本案中|根据|陈某|张某|小刘|AI|经营者)", r"\1", sentence)
        sentence = sentence.lstrip("：:；;，,。 ")
        if any(bad in sentence[:100] for bad in ["给分依据", "理由：理例结合", "采意给分", "整体作答思路", "具体："]):
            continue
        if any(key in sentence for key in ["应", "属于", "存在", "构成", "有效", "无效", "责任", "义务", "权利", "支持", "不予支持", "合同成立", "侵害", "承担", "具有"]):
            if not any(bad in sentence[:80] for bad in ["现实逻辑", "全国居民人均", "无人机起飞"]):
                preferred.append(sentence)
    chosen = [s.lstrip("：:；;，,。 ") for s in (preferred[:3] or sentences[:3])]
    return clean(" ".join(chosen), 520)


def load_all_ledger_records() -> list[dict]:
    with BUILDER.LEDGER.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        qid = row.get("question_id", "")
        if qid in BUILDER.DOMAIN_OVERRIDES:
            row.update(BUILDER.DOMAIN_OVERRIDES[qid])
        BUILDER.normalize_record_domains(row)
    return rows


def delivery_records() -> list[dict]:
    # Reuse the final delivery boundary, then add explicit pending/excluded context rows in a later appendix.
    return BUILDER.load_records()


def pending_records(all_rows: list[dict], final_rows: list[dict]) -> list[dict]:
    final_ids = {r["question_id"] for r in final_rows}
    pending = [r for r in all_rows if r.get("question_id") not in final_ids]
    pending.sort(key=lambda r: (r.get("year", ""), r.get("district", ""), r.get("stage", ""), int(r.get("question_no") or 0)))
    return pending


def build_index_rows(final_rows: list[dict], pending: list[dict]) -> list[dict]:
    rows = []
    for pool, record in [("已入框可用情境", r) for r in final_rows] + [("待核验/不入主线情境", r) for r in pending]:
        situation, reason = situation_for(record)
        rubric = rubric_for(record) if pool == "已入框可用情境" else clean(record.get("rubric_text"), 700)
        rows.append(
            {
                "pool": pool,
                "situation": situation,
                "label": record.get("label", ""),
                "question_type": "主观题" if record.get("question_type") == "subjective" else "选择题",
                "front_domain": record.get("front_domain", ""),
                "framework_domain": record.get("framework_domain", ""),
                "evidence": evidence_label(record, rubric),
                "source_label": source_label(record),
                "material_triggers": clean(record.get("material_triggers"), 260),
                "prompt": clean(record.get("complete_prompt"), 500),
                "rubric_or_answer": rubric,
                "scoring_terms": scoring_terms(rubric),
                "score_sentence": score_sentence(record, rubric),
                "situation_reason": reason,
                "source_path": record.get("rubric_source") or record.get("answer_source") or "",
                "include_status": record.get("include_status", ""),
                "curation_status": record.get("curation_status", ""),
            }
        )
    return rows


def write_csv(rows: list[dict]) -> None:
    fields = [
        "pool", "situation", "label", "question_type", "front_domain", "framework_domain", "evidence", "source_label",
        "material_triggers", "prompt", "rubric_or_answer", "scoring_terms", "score_sentence", "situation_reason",
        "source_path", "include_status", "curation_status",
    ]
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_md(rows: list[dict]) -> None:
    final_rows = [r for r in rows if r["pool"] == "已入框可用情境"]
    pending = [r for r in rows if r["pool"] != "已入框可用情境"]
    by_situation: dict[str, list[dict]] = defaultdict(list)
    for row in final_rows:
        by_situation[row["situation"]].append(row)
    situation_order = [name for name, _, _ in SITUATION_RULES] + ["其他法律情境（保留待复核）"]
    type_counts = Counter(r["question_type"] for r in final_rows)
    formal_subjective = sum(1 for r in final_rows if r["question_type"] == "主观题" and r["evidence"].startswith("主观题细则已锁定"))
    review_subjective = sum(1 for r in final_rows if r["question_type"] == "主观题" and "需复核" in r["evidence"])
    lines: list[str] = [
        "# 选必二《法律与生活》考过情境穷尽与细则踩分表",
        "",
        "这份是教师备课和踩分训练版，目标不是让学生泛泛知道“归哪类”，而是看清每个考过情境对应哪些细则句、哪些词能踩分、哪些句子能直接写上卷面。",
        "",
        "## 使用规则",
        "",
        "- 主观题：以对应细则/给分依据为准，提炼“踩分词”和“可写得分句”。",
        "- 选择题：只作为情境池和题肢排错训练；如果只有答案表，不把它伪装成主观题细则。",
        "- 待核验题：保留在附录，不推动主观题踩分句。",
        "",
        "## 总览",
        "",
        f"- 已入框可用情境题目：{len(final_rows)} 道",
        f"- 主观题：{type_counts['主观题']} 道，其中高置信可直接提炼踩分句：{formal_subjective} 道，复合题/二次匹配需回看细则复核：{review_subjective} 道",
        f"- 选择题：{type_counts['选择题']} 道，用于补齐“不太敢考主观题但常考选择题”的情境细节",
        f"- 待核验/不入主线情境：{len(pending)} 道，附录保留，不直接生成踩分句",
        "",
        "### 情境簇频次",
        "",
    ]
    for name in situation_order:
        if name in by_situation:
            group = by_situation[name]
            subj = sum(1 for r in group if r["question_type"] == "主观题")
            choice = sum(1 for r in group if r["question_type"] == "选择题")
            lines.append(f"- {name}：{len(group)} 道（主观 {subj}，选择 {choice}）")
    lines.append("")

    card_no = 1
    for name in situation_order:
        group = by_situation.get(name)
        if not group:
            continue
        rule = next((reason for situation, _, reason in SITUATION_RULES if situation == name), "先保留情境，再回题面和细则判断。")
        lines.extend([f"## {name}", "", f"读题抓手：{rule}", ""])
        # Subjective cards first, then choice cards.
        group = sorted(group, key=lambda r: (0 if r["question_type"] == "主观题" else 1, r["label"]))
        for row in group:
            lines.extend(
                [
                    f"### {card_no}. {row['label']}",
                    "",
                    f"- 题型：{row['question_type']}",
                    f"- 框架归位：{row['front_domain']} / {row['framework_domain']}",
                    f"- 细则状态：{row['evidence']}",
                    f"- 对应细则：{row['source_label']}",
                    f"- 材料触发：{row['material_triggers']}",
                    "",
                    "设问：",
                    "",
                    row["prompt"] or "题干型选择题，按题肢判断。",
                    "",
                ]
            )
            if row["question_type"] == "主观题":
                lines.extend(["细则原句/给分结构：", ""])
                for sentence in split_sentences(row["rubric_or_answer"], 8):
                    lines.append(f"- {sentence}")
                lines.extend(
                    [
                        "",
                        f"踩分词：{row['scoring_terms']}",
                        "",
                        f"可写得分句：{row['score_sentence']}",
                        "",
                    ]
                )
            else:
                lines.extend(
                    [
                        "客观题锁分信息：",
                        "",
                        f"- {row['rubric_or_answer']}",
                        f"- 可迁移边界：这类题补充情境识别和题肢排错，不直接推出主观题固定采分句。",
                        "",
                    ]
                )
            card_no += 1

    if pending:
        lines.extend(["## 附录：待核验或不推动主线的情境", "", "这些题保留是为了防漏，但不能直接当成确定踩分句来源。", ""])
        for row in pending:
            lines.extend(
                [
                    f"### {row['label']}",
                    "",
                    f"- 题型：{row['question_type']}",
                    f"- 状态：{row['include_status']} / {row['curation_status']}",
                    f"- 情境暂归：{row['situation']}",
                    f"- 处理：{row['evidence']}",
                    f"- 材料触发：{row['material_triggers']}",
                    "",
                ]
            )

    MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    DELIVERY.mkdir(parents=True, exist_ok=True)
    final = delivery_records()
    all_rows = load_all_ledger_records()
    pending = pending_records(all_rows, final)
    rows = build_index_rows(final, pending)
    write_csv(rows)
    write_md(rows)
    BUILDER.md_to_docx(MD, DOCX, "选必二《法律与生活》考过情境穷尽与细则踩分表")
    BUILDER.md_to_html(MD, HTML, "选必二《法律与生活》考过情境穷尽与细则踩分表")
    print(MD)
    print(DOCX)
    print(HTML)
    print(CSV_OUT)
    print(f"usable={len(final)} pending={len(pending)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
