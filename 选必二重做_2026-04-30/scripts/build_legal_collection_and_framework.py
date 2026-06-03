#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30")
RUN = BASE / "preprocess_v2_2026-05-03"
CURATED = RUN / "curated"
CACHE = RUN / "text_cache"
OUT = BASE / "final_legal_outputs"
SUPPLEMENTAL_ANSWER_LOCKS_PATH = RUN / "supplemental_answer_sources" / "SUPPLEMENTAL_CHOICE_ANSWER_LOCKS_2026-05-04.csv"


LEGAL_TERMS = [
    "民法典", "民事", "合同", "要约", "承诺", "格式条款", "违约", "定金", "赔偿", "侵权", "过错",
    "消费者", "经营者", "知情权", "自主选择权", "公平交易权", "惩罚性赔偿", "劳动合同", "劳动关系",
    "劳动仲裁", "用人单位", "竞业限制", "经济补偿", "工伤", "知识产权", "著作权", "专利", "商标",
    "商业秘密", "不正当竞争", "人格权", "名誉权", "肖像权", "隐私权", "个人信息", "所有权", "物权",
    "质权", "抵押", "相邻关系", "不动产", "继承", "遗嘱", "遗赠扶养", "婚姻", "夫妻", "监护",
    "质押", "担保物权", "担保", "调解", "仲裁", "诉讼", "举证责任", "司法确认", "人民法院", "法院", "判决", "裁判", "公益诉讼",
    "生态环境", "碳排放权", "新就业形态", "平台", "人工智能", "AI", "虚拟数字人",
]

FORMAL_HINTS = ["细则", "评标", "阅卷", "评分", "给分", "答案变通", "分题细则"]
SUPPORT_HINTS = ["讲评", "实录", "总结"]
ANSWER_HINTS = ["答案", "参考"]
NOISE_MODULE_HINTS = ["政治与法治", "经济与社会", "逻辑与思维", "哲学", "文化", "当代国际政治与经济"]

FRAMEWORK_DOMAINS = [
    ("合同交易与消费者保护", ["合同", "要约", "承诺", "格式条款", "违约", "定金", "消费者", "经营者", "公平交易权", "知情权", "退款", "养老卡"]),
    ("劳动就业与职业边界", ["劳动", "用人单位", "劳动合同", "劳动关系", "劳动仲裁", "竞业限制", "经济补偿", "工伤", "新就业形态", "骑手", "外卖"]),
    ("人格权与侵权责任", ["人格权", "名誉权", "肖像权", "隐私权", "个人信息", "侵权", "赔偿", "过错", "受伤", "损害", "骨折", "健康权", "身体权", "体育", "羽毛球", "足球"]),
    ("财产权、物权与相邻关系", ["所有权", "物权", "不动产", "质权", "质押", "抵押", "担保物权", "担保", "相邻关系", "财产", "碳排放权", "配额", "漏水", "排除妨碍", "机动车"]),
    ("婚姻家庭与继承扶养", ["继承", "遗嘱", "遗赠扶养", "婚姻", "夫妻", "家庭", "赡养", "监护", "遗产", "房产"]),
    ("知识产权与竞争秩序", ["知识产权", "著作权", "专利", "商标", "商业秘密", "不正当竞争", "AI", "人工智能", "虚拟数字人", "萝卜快跑"]),
    ("纠纷解决与程序救济", ["调解", "仲裁", "诉讼", "举证责任", "司法确认", "人民法院", "法院", "判决", "裁判", "回避制度", "诉讼代理"]),
    ("生态公益、新业态与法治价值", ["公益诉讼", "生态环境", "碳排放", "平台", "新业态", "文物", "司法建议", "法治护航", "枫桥经验"]),
]

STUDENT_FRONT_DOMAINS = [
    ("合同消费者劳动", ["合同交易与消费者保护", "劳动就业与职业边界"], "看交易/用工关系、意思表示或劳动关系是否成立，再落履行守信、弱势保护、解除补偿和责任边界。"),
    ("物权相邻继承家庭", ["财产权、物权与相邻关系", "婚姻家庭与继承扶养"], "看财产或身份关系，落到物权归属、相邻边界、夫妻/监护/扶养/继承安排。"),
    ("人格权侵权", ["人格权与侵权责任"], "看人格利益或身体财产受损，再抓过错、损害、因果、免责和责任承担方式。"),
    ("知识产权不正当竞争", ["知识产权与竞争秩序"], "先分作品/标识/竞争行为，再落著作权、商标、商业混淆或不正当竞争边界。"),
    ("纠纷解决生态公益与新业态", ["纠纷解决与程序救济", "生态公益、新业态与法治价值"], "看适格主体、程序路径、公共利益或新场景，再按具体法律关系回流，价值必须后置。"),
]

BACKEND_TO_FRONT_DOMAIN = {
    backend: (front, action)
    for front, backends, action in STUDENT_FRONT_DOMAINS
    for backend in backends
}
BACKEND_TO_FRONT_DOMAIN.update(
    {
        "纠纷解决与程序救济": ("纠纷解决生态公益与新业态", "第5域是方法/容器域；回到当事人处境、程序节点和救济效果。"),
        "生态公益、新业态与法治价值": ("纠纷解决生态公益与新业态", "第5域是开放容器；先判断更接近侵权、程序、合同、劳动或知识产权，再作价值后置。"),
    }
)

OFFICIAL_CHOICE_ANSWER_OVERRIDES = {
    (
        "2024_东城_一模_001",
        "9",
    ): {
        "answer": "B",
        "source": "/Users/wanglifei/Desktop/2024模拟题/2024东城一模/细则/补充材料/北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治答案(1).pdf",
        "method": "official_answer_table_visual_verified",
        "note": "官方答案表可见：第9题 B。OCR 表格顺序打散，故用渲染页人工核验锁定。",
    },
}

LOCAL_CHOICE_ANSWER_CANDIDATES = {
    ("2024_丰台_二模_009", "5"): ("A", "①②对应条例中的经营者守法、政府监管和共同治理；③“避免投诉举报”、④“确保扩大”均绝对化。"),
    ("2024_丰台_二模_009", "6"): ("B", "①③对应协作配合和源头预防；②“全链条保障体系”过满，④把工会说成检察监督职能。"),
    ("2025_海淀_二模_029", "5"): ("D", "题干要求“不正确”，商场责任并非无过错侵权责任。"),
    ("2025_海淀_二模_029", "6"): ("B", "①④符合未成年人利益和父母平等监护；②让6岁儿童自行决定、③父亲单方按意愿改变居住地均错误。"),
    ("2025_海淀_二模_029", "7"): ("A", "①③符合票根经济的跨行业联动和权益兑换；②抑制竞争、④政府主导均不当。"),
    ("2026_丰台_一模_038", "11"): ("D", "录用通知书属于明确意思表示，可按要约/诚信规则判断；法院判决重在守信保护劳动者，①②法律关系错位。"),
    ("2026_房山_一模_040", "11"): ("D", "A把失信执行错认违约补救，B错认用益物权，C“自愿原则”表述偏离司法集中清偿制度，D概括司法平衡最稳。"),
    ("2026_丰台_期末_048", "11"): ("D", "四个案例共同指向公正司法与法治德治结合；①②不能覆盖全部案例。"),
    ("2026_朝阳_期末_050", "11"): ("B", "虚拟数字人形象按著作权法保护，B对应复制权和信息网络传播权；A商标法、C法定许可、D上诉期限均错。"),
}

ANSWER_CHAR_MAP = str.maketrans(
    {
        "Ａ": "A",
        "Ｂ": "B",
        "Ｃ": "C",
        "Ｄ": "D",
        "ａ": "A",
        "ｂ": "B",
        "ｃ": "C",
        "ｄ": "D",
        "Α": "A",
        "А": "A",
        "В": "B",
        "в": "B",
        "Β": "B",
        "С": "C",
        "с": "C",
        "Ϲ": "C",
        "Д": "D",
        "д": "D",
    }
)


@dataclass
class CacheItem:
    cache_path: Path
    source_path: str
    status: str
    text: str
    suite_id: str = ""
    role: str = ""
    evidence_type: str = ""


def clean(text: str) -> str:
    text = (text or "").replace("\u3000", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def normalize_answer_chars(text: str) -> str:
    return (text or "").translate(ANSWER_CHAR_MAP)


def short(text: str, limit: int) -> str:
    text = clean(text)
    return text if len(text) <= limit else text[:limit].rstrip() + "……"


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def is_included(record: dict) -> bool:
    return record.get("include_status") not in {"excluded_by_curation", "excluded_by_module_boundary"}


def evidence_status(record: dict) -> str:
    etype = record.get("evidence_type", "")
    if record.get("question_type") == "choice":
        if record.get("answer") and etype in {"formal_or_scoring_source", "official_answer_key"}:
            return "objective_answer_locked"
        if record.get("answer"):
            return "objective_answer_locked_needs_source_review"
        return "answer_pending_official"
    if etype == "formal_or_scoring_source":
        return "formal_scoring_matched"
    if etype in {"paper_source", "unknown", "rubric_not_found_yet"}:
        return "rubric_match_pending"
    if etype == "reference_answer":
        return "reference_only_not_trunk"
    if etype == "support_lecture_or_review":
        return "support_source_needs_local_check"
    if etype == "answer_not_locked":
        return "answer_pending_official"
    return etype or "evidence_uncertain"


def front_domain_for(backend_domain: str) -> tuple[str, str]:
    return BACKEND_TO_FRONT_DOMAIN.get(
        backend_domain,
        ("开放容器（待本地核验）", "后台八域暂未能稳定回流到学生五域，需本地核验。"),
    )


def parse_cache_file(path: Path) -> CacheItem:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    lines = raw.splitlines()
    source = ""
    status = ""
    if lines and lines[0].startswith("source: "):
        source = lines[0].replace("source: ", "", 1).strip()
    if len(lines) > 1 and lines[1].startswith("status: "):
        status = lines[1].replace("status: ", "", 1).strip()
    text = raw.split("\n\n", 1)[1] if "\n\n" in raw else raw
    return CacheItem(path, source, status, text)


def role_for_path(source_path: str) -> str:
    if "/细则/" in source_path:
        return "rubric"
    if "/其他材料/" in source_path:
        return "support"
    if "/试卷/" in source_path:
        return "paper"
    return "unknown"


def evidence_for_path(source_path: str) -> str:
    name = Path(source_path).name
    if "supplemental_answer_sources" in source_path:
        return "official_answer_key"
    if any(hint in source_path for hint in FORMAL_HINTS):
        return "formal_or_scoring_source"
    if any(hint in name for hint in SUPPORT_HINTS):
        return "support_lecture_or_review"
    if any(hint in name for hint in ANSWER_HINTS):
        return "reference_answer"
    if "/试卷/" in source_path:
        return "paper_source"
    return "unknown"


def has_answer_key_cue(text: str) -> bool:
    compact = flat(text)
    if not compact:
        return False
    cues = ["参考答案", "答案及评分", "评分标准", "第一部分 选择题", "选择题答案", "题号 答案"]
    if any(cue in compact for cue in cues) and "答案" in compact:
        return True
    return False


def load_supplemental_answer_locks() -> dict[tuple[str, str], dict]:
    locks: dict[tuple[str, str], dict] = {}
    for row in read_csv(SUPPLEMENTAL_ANSWER_LOCKS_PATH):
        suite_id = row.get("suite_id", "").strip()
        qno = row.get("question_no", "").strip()
        answer = normalize_answer_chars(row.get("answer", "").strip().upper())
        if not suite_id or not qno or answer not in {"A", "B", "C", "D"}:
            continue
        locks[(suite_id, qno)] = row
    return locks


SUPPLEMENTAL_CHOICE_ANSWER_LOCKS = load_supplemental_answer_locks()


def answer_key_region(text: str) -> str:
    if not has_answer_key_cue(text):
        return ""
    compact = flat(normalize_answer_chars(text))
    starts = [compact.rfind(cue) for cue in ["参考答案", "答案及评分", "评分标准", "第一部分 选择题", "选择题答案"]]
    start = max(starts)
    if start < 0:
        return ""
    return compact[start:start + 30000]


def load_cache_items(suite_rows: list[dict]) -> list[CacheItem]:
    suite_paths = [(row["suite_id"], row["suite_path"]) for row in suite_rows]
    items = []
    for path in sorted(CACHE.glob("*.txt")):
        item = parse_cache_file(path)
        item.role = role_for_path(item.source_path)
        item.evidence_type = evidence_for_path(item.source_path)
        for suite_id, suite_path in suite_paths:
            if item.source_path.startswith(suite_path):
                item.suite_id = suite_id
                break
        items.append(item)
    return items


def merge_curation_status() -> dict[tuple[str, str], tuple[str, str]]:
    status: dict[tuple[str, str], tuple[str, str]] = {}
    for filename in [
        "ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv",
        "FORMAL_ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv",
        "DEFERRED_LEGAL_QUESTION_INDEX_V2.csv",
        "REJECTED_LEGAL_QUESTION_INDEX_V2.csv",
    ]:
        for row in read_csv(CURATED / filename):
            key = (row.get("suite_id", ""), row.get("question_no", ""))
            status[key] = (row.get("curation_status", ""), row.get("curation_reason", ""))
    return status


def legal_term_hits(text: str) -> list[str]:
    hits = [term for term in LEGAL_TERMS if term in (text or "")]
    return list(dict.fromkeys(hits))


def extract_keywords(question_text: str) -> list[str]:
    text = flat(question_text)
    terms = legal_term_hits(text)
    quoted = re.findall(r"[“《]([^”》]{2,18})[”》]", text)
    names = re.findall(r"[\u4e00-\u9fa5A-Za-z]{0,3}[某][\u4e00-\u9fa5A-Za-z]{0,3}", text)
    special = re.findall(r"(?:[A-Z]公司|[甲乙丙丁]公司|[甲乙丙丁]某|小[\u4e00-\u9fa5]|[\u4e00-\u9fa5]{1,3}法院|[\u4e00-\u9fa5]{1,6}平台)", text)
    phrases = []
    for term in terms:
        pos = text.find(term)
        if pos >= 0:
            phrases.append(text[max(0, pos - 8): pos + len(term) + 8])
    words = terms + quoted + names + special + phrases
    bad = {"法律与生活", "人民法院", "法院", "判决", "裁判", "材料", "结合", "运用"}
    unique = []
    for word in words:
        word = clean(word)
        if len(word) < 2 or word in bad:
            continue
        if word not in unique:
            unique.append(word)
    return unique[:18]


def window_around(text: str, start: int, radius: int = 1800) -> str:
    return text[max(0, start - radius): min(len(text), start + radius)]


def qno_patterns(qno: str) -> list[str]:
    return [
        rf"第\s*{re.escape(qno)}\s*题",
        rf"(?<!\d){re.escape(qno)}\s*[\.．、]",
        rf"(?<!\d){re.escape(qno)}\s*题",
        rf"\({re.escape(qno)}\)",
        rf"（{re.escape(qno)}）",
    ]


def candidate_windows(item: CacheItem, qno: str, keywords: list[str]) -> list[tuple[str, int, str]]:
    text = item.text or ""
    windows: list[tuple[str, int, str]] = []
    for pat in qno_patterns(qno):
        for match in re.finditer(pat, text):
            windows.append((window_around(text, match.start()), match.start(), f"qno:{pat}"))
    for keyword in keywords[:8]:
        if len(keyword) < 2:
            continue
        for match in re.finditer(re.escape(keyword), text):
            windows.append((window_around(text, match.start()), match.start(), f"kw:{keyword}"))
            if len(windows) > 40:
                break
    return windows


def score_window(window: str, item: CacheItem, qno: str, keywords: list[str], qtype: str) -> int:
    score = 0
    if item.evidence_type == "formal_or_scoring_source":
        score += 80
    elif item.evidence_type == "support_lecture_or_review":
        score += 55
    elif item.evidence_type == "reference_answer":
        score += 35
    elif item.role == "paper":
        score += 5
    if any(re.search(pat, window) for pat in qno_patterns(qno)):
        score += 35
    score += 8 * sum(1 for keyword in keywords if keyword and keyword in window)
    score += 3 * sum(1 for term in legal_term_hits(window))
    if any(h in window for h in ["评分", "给分", "等级", "层次", "答案", "解析", "评标", "阅卷", "观点", "可从"]):
        score += 12
    if qtype == "subjective" and any(h in window for h in ["结合材料", "运用", "说明", "分析", "阐释", "理由"]):
        score += 8
    if qtype == "choice" and any(h in window for h in ["A", "B", "C", "D", "选项", "答案"]):
        score += 8
    if any(noise in window for noise in NOISE_MODULE_HINTS) and len(legal_term_hits(window)) < 2:
        score -= 30
    return score


def find_best_evidence(row: dict, suite_items: list[CacheItem], qtext: str) -> dict:
    current_text = row.get("rubric_excerpt") or row.get("rubric_original_text") or ""
    current_file = row.get("source_rubric_file") or row.get("rubric_source") or ""
    current_ev = row.get("evidence_type", "")
    if current_text and current_ev != "missing":
        inferred_ev = current_ev
        if inferred_ev in {"", "unknown", "rubric_not_found_yet", "paper_source"} and re.search(r"评分|给分|参考答案|（\s*\d+\s*分\s*）|\d+\s*分", current_text):
            inferred_ev = "formal_or_scoring_source"
        return {
            "rubric_text": current_text,
            "rubric_source": current_file,
            "evidence_type": inferred_ev,
            "rubric_match_method": row.get("rubric_match_method", "v2_current"),
            "secondary_score": "kept_current",
        }
    qno = row.get("question_no", "")
    qtype = row.get("question_type") or ("subjective" if int(qno or 0) >= 16 else "choice")
    keywords = extract_keywords(qtext)
    candidates = []
    for item in suite_items:
        if not (item.text or "").strip():
            continue
        if item.role == "paper" and qtype == "subjective":
            # Prefer scoring sources for subjective rubrics; use paper only if nothing else survives.
            pass
        for window, pos, method in candidate_windows(item, qno, keywords):
            sc = score_window(window, item, qno, keywords, qtype)
            if sc >= 45:
                candidates.append((sc, item, window, method, pos))
    if not candidates:
        return {
            "rubric_text": "",
            "rubric_source": "",
            "evidence_type": "rubric_not_found_yet",
            "rubric_match_method": "secondary_search_no_hit",
            "secondary_score": "0",
        }
    if qtype == "subjective":
        evidence_candidates = [cand for cand in candidates if cand[1].evidence_type != "paper_source"]
        if evidence_candidates:
            candidates = evidence_candidates
    sc, item, window, method, pos = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
    return {
        "rubric_text": short(window, 4200),
        "rubric_source": item.source_path,
        "evidence_type": item.evidence_type,
        "rubric_match_method": f"secondary_{method}@{pos}",
        "secondary_score": str(sc),
    }


def parse_answer_table(text: str) -> dict[str, str]:
    answers: dict[str, str] = {}

    text = answer_key_region(text)
    if not text:
        return answers
    text = normalize_answer_chars(text)
    lines = [clean(normalize_answer_chars(line)) for line in text.splitlines() if clean(line)]
    for idx, line in enumerate(lines):
        if "题号" not in line:
            continue
        next_line = ""
        for cand in lines[idx + 1: idx + 4]:
            if "答案" in cand:
                next_line = cand
                break
        if not next_line:
            continue
        nums = re.findall(r"(?<!\d)([1-9]|1[0-5])(?!\d)", line)
        letters = re.findall(r"(?<![A-Z])([ABCD])(?![A-Z])", next_line)
        if len(nums) >= 1 and len(letters) >= len(nums):
            for num, letter in zip(nums, letters[:len(nums)]):
                answers.setdefault(num, letter)

    for idx, line in enumerate(lines[:-1]):
        nums = re.findall(r"(?<!\d)([1-9]|1[0-5])(?!\d)", line)
        if len(nums) < 3 or len(nums) > 15:
            continue
        next_line = lines[idx + 1]
        letters = re.findall(r"(?<![A-Z])([ABCD])(?![A-Z])", next_line)
        if len(letters) == len(nums):
            for num, letter in zip(nums, letters):
                answers.setdefault(num, letter)

    compact = flat(text)
    choice_part = compact.split("第二部分", 1)[0]
    for match in re.finditer(r"1\s*[-—至]\s*15\s*([ABCD\s]{15,40})", choice_part):
        letters = re.findall(r"[ABCD]", match.group(1))
        if len(letters) >= 15:
            for idx, letter in enumerate(letters[:15], start=1):
                answers.setdefault(str(idx), letter)
    for match in re.finditer(
        r"题号\s+((?:(?:[1-9]|1[0-5])\s+){4,14}(?:[1-9]|1[0-5]))\s+答案\s+((?:[ABCD4]\s+){4,14}[ABCD4])",
        choice_part,
    ):
        nums = re.findall(r"(?<!\d)([1-9]|1[0-5])(?!\d)", match.group(1))
        letters = re.findall(r"(?<![A-Z0-9])([ABCD4])(?![A-Z0-9])", match.group(2))
        if len(nums) == len(letters):
            for num, letter in zip(nums, letters):
                answers.setdefault(num, "A" if letter == "4" else letter)
    for match in re.finditer(
        r"((?:(?:[1-9]|1[0-5])\s+){4,14}(?:[1-9]|1[0-5]))\s+((?:[ABCD4]\s+){4,14}[ABCD4])",
        choice_part,
    ):
        nums = re.findall(r"(?<!\d)([1-9]|1[0-5])(?!\d)", match.group(1))
        letters = re.findall(r"(?<![A-Z0-9])([ABCD4])(?![A-Z0-9])", match.group(2))
        if len(nums) == len(letters):
            for num, letter in zip(nums, letters):
                answers.setdefault(num, "A" if letter == "4" else letter)
    for match in re.finditer(r"(?<!\d)([1-9]|1[0-5])\s*[\.．、:：]\s*4(?=\s|[0-9]|$)", compact):
        # Some OCR layers read answer letter A as the digit 4 in compact answer keys, e.g. "11.4".
        answers.setdefault(match.group(1), "A")
    for match in re.finditer(r"(?<!\d)([1-9]|1[0-5])\s*[\.．、]\s*(?:【\s*答案\s*】|答案[:：]?)\s*([ABCD])", compact):
        answers.setdefault(match.group(1), match.group(2))
    for match in re.finditer(r"(?<!\d)([1-9]|1[0-5])\s*[\.．、:：]?\s*([ABCD])", compact):
        answers.setdefault(match.group(1), match.group(2))
    for match in re.finditer(r"第\s*([1-9]|1[0-5])\s*题[^ABCD]{0,80}([ABCD])", compact):
        answers.setdefault(match.group(1), match.group(2))
    for segment_match in re.finditer(r"(?:题号|答案).{0,260}", compact):
        segment = segment_match.group(0)
        nums = re.findall(r"(?<!\d)([1-9]|1[0-5])(?!\d)", segment)
        letters = re.findall(r"\b([ABCD])\b", segment)
        if len(nums) >= 3 and len(letters) >= len(nums) and len(nums) <= 15:
            for num, letter in zip(nums, letters[:len(nums)]):
                answers.setdefault(num, letter)
    for match in re.finditer(r"([1-5])\s*[-—至]\s*([1-5])\s*[:：]?\s*([ABCD]{5})", compact):
        start = int(match.group(1))
        letters = match.group(3)
        for offset, letter in enumerate(letters):
            answers.setdefault(str(start + offset), letter)
    for match in re.finditer(r"(?<!\d)([1-9]|1[0-5])\s*[．.]\s*(?:【分析】)?.{0,2600}?故选[:：]\s*([ABCD])", compact):
        answers.setdefault(match.group(1), match.group(2))
    return answers


def find_choice_answer(row: dict, suite_items: list[CacheItem], qtext: str, evidence_text: str) -> tuple[str, str, str]:
    if row.get("answer") and (
        row.get("answer_source") and ("/细则/" in row.get("answer_source", "") or row.get("answer_method", "").startswith("official"))
    ):
        return row.get("answer", ""), row.get("answer_source", ""), "kept_current"
    qno = row.get("question_no", "")
    override = OFFICIAL_CHOICE_ANSWER_OVERRIDES.get((row.get("suite_id", ""), qno))
    if override:
        return override["answer"], override["source"], override["method"]
    supplemental = SUPPLEMENTAL_CHOICE_ANSWER_LOCKS.get((row.get("suite_id", ""), qno))
    if supplemental:
        source = supplemental.get("source_path") or supplemental.get("source_url") or "supplemental_answer_lock"
        method = supplemental.get("method") or "supplemental_official_answer_lock"
        return supplemental["answer"], source, method
    search_items = sorted(
        suite_items,
        key=lambda item: 0 if item.evidence_type in {"formal_or_scoring_source", "reference_answer", "support_lecture_or_review"} else 1,
    )
    for item in search_items:
        if not has_answer_key_cue(item.text):
            continue
        answers = parse_answer_table(item.text)
        if qno in answers:
            return answers[qno], item.source_path, "parsed_answer_table"
    for text, source in [(evidence_text, "matched_evidence"), (qtext, "question_text")]:
        patterns = [
            rf"(?:第\s*{qno}\s*题|{qno}\s*[\.．、]).{{0,180}}?答案[:：]?\s*([ABCD])",
            rf"(?:第\s*{qno}\s*题|{qno}\s*[\.．、]).{{0,180}}?([ABCD])\s*项?正确",
        ]
        for pat in patterns:
            m = re.search(pat, flat(text))
            if m:
                return m.group(1), source, "local_answer_pattern"
    return "", "", "answer_not_locked"


def choice_answer_candidate(row: dict, answer: str) -> tuple[str, str]:
    if answer:
        return "", ""
    candidate = LOCAL_CHOICE_ANSWER_CANDIDATES.get((row.get("suite_id", ""), row.get("question_no", "")))
    if not candidate:
        return "", ""
    return candidate


def source_text_for(items: list[CacheItem], source_path: str) -> str:
    for item in items:
        if item.source_path == source_path:
            return item.text
    path = Path(source_path)
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""


def choice_evidence_from_answer(
    evidence: dict,
    answer: str,
    answer_source: str,
    suite_items: list[CacheItem],
) -> dict:
    if evidence["evidence_type"] in {"formal_or_scoring_source", "support_lecture_or_review", "reference_answer"} and evidence["rubric_text"]:
        return evidence
    if answer and answer_source and answer_source not in {"matched_evidence", "question_text", "rubric_explanation"}:
        text = source_text_for(suite_items, answer_source)
        etype = evidence_for_path(answer_source)
        if has_answer_key_cue(text):
            etype = "official_answer_key"
        return {
            "rubric_text": f"选择题答案锁定：{answer}。来源文本摘录：{short(text, 800)}",
            "rubric_source": answer_source,
            "evidence_type": etype,
            "rubric_match_method": "choice_answer_source",
            "secondary_score": "answer_locked",
        }
    if answer:
        return {
            "rubric_text": f"选择题答案锁定：{answer}。来源：{answer_source or '局部解析'}",
            "rubric_source": answer_source,
            "evidence_type": "reference_answer",
            "rubric_match_method": "choice_answer_pattern",
            "secondary_score": "answer_locked",
        }
    return {
        "rubric_text": "",
        "rubric_source": "",
        "evidence_type": "answer_not_locked",
        "rubric_match_method": "choice_answer_not_locked",
        "secondary_score": "0",
    }


def option_map(block: str) -> dict[str, str]:
    block = normalize_answer_chars(block)
    matches = list(re.finditer(r"([ABCDabcd])\s*[\.．、]\s*", block))
    opts: dict[str, str] = {}
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else min(len(block), match.end() + 700)
        opts[match.group(1).upper()] = short(block[match.end():end], 300)
    return opts


NON_LEGAL_BOOKS = ["政治与法治", "当代国际政治与经济", "经济与社会", "哲学与文化", "逻辑与思维"]


def strip_ocr_footer(text: str) -> str:
    text = re.sub(r"\s+高三[^[]{0,80}\[ocr page \d+\].*$", "", text or "")
    text = re.sub(r"\s+\[ocr page \d+\].*$", "", text)
    return clean(text)


def trim_choice_text(text: str) -> str:
    text = strip_ocr_footer(normalize_answer_chars(text))
    d_match = list(re.finditer(r"([Dd])\s*[\.．、]\s*", text))
    if d_match:
        match = d_match[-1]
        tail = text[match.end():]
        compact_answer = re.match(r"\s*([①②③④]{1,4}|[0-4O]{1,4})([）)]?)", tail)
        if compact_answer and len(tail[compact_answer.end():].strip()) > 50:
            text = text[: match.end() + compact_answer.end()]
    return clean(text)


def trim_next_question_bleed(text: str, qno: str, qtype: str) -> str:
    if qtype == "choice":
        try:
            next_no = str(int(qno) + 1)
        except ValueError:
            next_no = ""
        if next_no:
            match = re.search(rf"\s(?={re.escape(next_no)}\s*[\.．、])", text[60:])
            if match:
                text = text[: 60 + match.start()]
        return trim_choice_text(text)
    try:
        next_no = str(int(qno) + 1)
    except ValueError:
        return clean(text)
    pattern = rf"\s(?={re.escape(next_no)}\s*[\.．、][^0-9])"
    match = re.search(pattern, text[80:])
    if match:
        return clean(text[: 80 + match.start()])
    return clean(text)


def legal_scope_prompt(qtext: str, fallback_prompt: str, qtype: str) -> tuple[str, str, bool]:
    if qtype == "choice":
        return fallback_prompt, "choice_whole_question", False
    text = clean(qtext)
    candidates: list[tuple[int, str]] = []
    # Prefer explicit 法律与生活 / 法律知识 / 法治知识 subquestions. Keep the material
    # in question_text, but make the operative prompt the legal small question only.
    for match in re.finditer(
        r"([（(]\d+[）)][^（(]{0,420}?(?:运用《法律与生活》|运用法律知识|运用法治知识)[^（(]{0,420}?(?:[。？?](?:\s*[（(]\s*\d+\s*分\s*[）)])?|\s*[（(]\s*\d+\s*分\s*[）)]))",
        text,
    ):
        prompt = clean(match.group(1))
        if "政治与法治" in prompt:
            continue
        score = 0
        if "法律与生活" in prompt:
            score += 30
        if "法律知识" in prompt:
            score += 20
        if "法治知识" in prompt:
            score += 10
        score += min(10, len(legal_term_hits(text)))
        candidates.append((score, prompt))
    if candidates:
        return sorted(candidates, reverse=True)[0][1], "legal_subquestion_extracted", False
    if fallback_prompt and ("法律与生活" in fallback_prompt or "运用法律知识" in fallback_prompt or "运用法治知识" in fallback_prompt):
        return clean(fallback_prompt), "fallback_legal_prompt", False
    explicit_non_legal = any(f"《{book}》" in text or f"运用{book}" in text for book in NON_LEGAL_BOOKS)
    if explicit_non_legal and "法律与生活" not in text and "运用法律知识" not in text and "运用法治知识" not in text:
        return clean(fallback_prompt or short(text[-260:], 260)), "explicit_non_legal_module", True
    return clean(fallback_prompt or short(text[-260:], 260)), "whole_question_no_explicit_legal_small_question", False


def material_triggers(text: str) -> str:
    hits = legal_term_hits(text)
    names = re.findall(r"[甲乙丙丁]公司|[A-Z]公司|[\u4e00-\u9fa5A-Za-z]某|小[\u4e00-\u9fa5]", text)
    pieces = list(dict.fromkeys(names + hits))
    if pieces:
        return "、".join(pieces[:12])
    return short(text, 120)


def classify_domain(text: str) -> tuple[str, str]:
    generic_procedure_terms = {"人民法院", "法院", "判决", "裁判"}
    strong_procedure_terms = {"调解", "仲裁", "举证责任", "司法确认", "回避制度", "诉讼代理", "审判监督", "上诉", "诉讼"}
    ecology_terms = {"公益诉讼", "生态环境", "碳排放", "文物", "司法建议"}
    scores = []
    for domain, terms in FRAMEWORK_DOMAINS:
        score = 0.0
        for term in terms:
            count = text.count(term)
            if not count:
                continue
            weight = 1.0
            if domain == "纠纷解决与程序救济":
                if term in generic_procedure_terms:
                    weight = 0.15
                elif term in strong_procedure_terms:
                    weight = 3.0
            if domain == "生态公益、新业态与法治价值" and term in ecology_terms:
                weight = 2.0
            score += count * weight
        scores.append((score, domain, [term for term in terms if term in text]))
    non_procedure = [row for row in scores if row[1] not in {"纠纷解决与程序救济"}]
    procedure = next(row for row in scores if row[1] == "纠纷解决与程序救济")
    score, domain, terms = sorted(non_procedure, key=lambda x: x[0], reverse=True)[0]
    if procedure[0] >= 3 and score < 3 and procedure[0] > score + 1:
        score, domain, terms = procedure
    elif procedure[0] >= 3 and procedure[0] > score + 3:
        score, domain, terms = procedure
    if score <= 0:
        return "纠纷解决与程序救济", "未出现稳定专门法域词，先按程序/法治判断开放归位"
    return domain, "命中：" + "、".join(terms[:8])


def result_landing(text: str, qtype: str, answer: str = "") -> str:
    if qtype == "choice":
        return f"客观判断落点：{answer or '答案未锁定'}；判断依据应扣住主体关系、权利义务和法律后果。"
    anchors = []
    for key, label in [
        ("赔偿", "责任承担/赔偿"),
        ("补偿", "补偿或经济补偿"),
        ("有效", "效力确认"),
        ("无效", "效力否定"),
        ("归", "权利/财产/遗产归属"),
        ("仲裁", "劳动仲裁或纠纷解决路径"),
        ("诉讼", "诉讼救济"),
        ("举证", "举证责任"),
        ("价值", "价值意义"),
        ("意义", "价值意义"),
    ]:
        if key in text and label not in anchors:
            anchors.append(label)
    return "、".join(anchors[:6]) if anchors else "法律关系判断、事实规则匹配、处理结果或价值说明。"


def proposition_path(qtext: str, rubric: str, domain: str) -> str:
    text = qtext + " " + rubric
    carrier = "生活案例"
    if re.search(r"[ABCD]\s*[\.．、]", qtext):
        carrier = "法律选择题案例/法律现象"
    elif "典型案例" in text:
        carrier = "司法/仲裁典型案例"
    elif "最高人民法院" in text or "民法典" in text:
        carrier = "法条解释或司法案例"
    elif "平台" in text or "AI" in text or "人工智能" in text:
        carrier = "新业态/新技术场景"
    elif "表" in text or "下表" in text:
        carrier = "案例表格/规则对照"
    pattern = "裁判依据题"
    route = "事实 -> 主体关系 -> 规则条件 -> 责任/效力"
    reward = "写清谁对谁、依何规则、承担何种责任或确认何种效力"
    if re.search(r"[ABCD]\s*[\.．、]", qtext):
        pattern = "选择题"
        route = "题干事实 -> 题肢关键词 -> 排除偷换主体、错位关系或绝对化后果"
        reward = "识别题肢中的绝对化、主体错位、关系错位和责任错位"
    elif "表" in text or "下表" in text or "完成下表" in text:
        pattern = "表格补全题"
        route = "看示例 -> 比照案例 -> 裁判理由栏写规则适用 -> 意义栏回到本案"
        reward = "裁判理由有具体规则和事实适用，意义先回本案再上升"
    elif "评析" in text or "观点" in text or "谈谈你对" in text:
        pattern = "观点评析题"
        route = "拆观点 -> 找规则依据 -> 判断合理/不合理 -> 本案价值收束"
        reward = "分层评价观点，并给出法律依据和本案结论"
    elif "假如你是法官" in text or "专业指导" in text or "仲裁" in text or "调解" in text or "诉讼" in text:
        pattern = "程序救济题"
        route = "当事人处境 -> 可走程序节点 -> 节点法律效果"
        reward = "写出可用程序、条件和效果，避免只写公平正义"
    elif "意义" in text or "价值" in text or "美德" in text:
        pattern = "意义认识题"
        route = "本案处理结果 -> 制度意图 -> 权利/秩序/价值"
        reward = "价值必须后置，先说本案权利义务和处理结果"
    return f"题型：{pattern}。命题人以{carrier}切入{domain}；路径：{route}；细则奖励动作：{reward}。"


def why_think(qtext: str, rubric: str, domain: str) -> str:
    triggers = material_triggers(qtext)
    if re.search(r"[ABCD]\s*[\.．、]", qtext):
        return f"看到{triggers}，先把题放入“{domain}”；选择题不完整展开四步，但仍要先判主体关系，再排除错位规则和错误法律后果。"
    landing = result_landing(rubric, "subjective")
    return f"看到{triggers}，先把题放入“{domain}”；再按“主体关系 -> 争点事实 -> 规则条件 -> {landing}”展开。"


def answer_points(rubric: str, qtype: str, answer: str = "") -> str:
    if qtype == "choice":
        return result_landing(rubric, qtype, answer)
    if not rubric:
        return "细则仍待二次 OCR/原文件核验；本题先保留题面和框架归位，不虚构答案点。"
    parts = re.split(r"(?<=[。；;])\s+|\n+", clean(rubric))
    keep = []
    for part in parts:
        if any(key in part for key in ["答案", "评分", "给分", "法院", "应", "可以", "不能", "因为", "依据", "意义", "有效", "责任", "赔偿", "补偿", "权利", "义务"]):
            keep.append(part)
    if not keep:
        keep = parts[:4]
    return "\n".join(f"- {short(part, 240)}" for part in keep[:8])


def build_choice_wrong_sentences(qtext: str, answer: str) -> str:
    opts = option_map(qtext)
    if not answer or answer not in opts:
        return "答案未锁定，暂不生成实质错项句。"
    wrongs = []
    for label in ["A", "B", "C", "D"]:
        if label == answer or label not in opts:
            continue
        hint = "主体关系、事实条件或法律后果没有扣准"
        if any(k in opts[label] for k in ["一律", "必然", "直接", "无需", "都", "均", "只能"]):
            hint = "把有条件的法律判断说绝对"
        elif any(k in opts[label] for k in ["仲裁", "调解", "诉讼", "司法确认"]):
            hint = "纠纷解决方式或程序效力错位"
        elif any(k in opts[label] for k in ["著作权", "专利", "商标"]):
            hint = "知识产权类型或权利边界错位"
        elif any(k in opts[label] for k in ["劳动", "用人单位"]):
            hint = "劳动关系或用工责任边界错位"
        wrongs.append(f"{label}项不对在{hint}，因为“{short(opts[label], 90)}”与题面事实或法律规则不匹配。")
    return "；".join(wrongs)


def build_candidate_wrong_sentences(qtext: str, candidate_answer: str, candidate_reason: str) -> str:
    if not candidate_answer:
        return ""
    base = build_choice_wrong_sentences(qtext, candidate_answer)
    return f"本地法律推理候选答案：{candidate_answer}。候选理由：{candidate_reason}。{base}"


def question_label(row: dict) -> str:
    return f"{row.get('year')} {row.get('district')} {row.get('stage')} {row.get('suite_name')} 第{row.get('question_no')}题"


def load_question_texts() -> tuple[list[dict], dict[tuple[str, str], dict], dict[tuple[str, str], dict]]:
    index_rows = read_csv(RUN / "LEGAL_QUESTION_INDEX_V2.csv")
    subj_rows = {(r["suite_id"], r["question_no"]): r for r in read_csv(RUN / "SUBJECTIVE_SOURCE_PACKS_V2.csv")}
    choice_rows = {(r["suite_id"], r["question_no"]): r for r in read_csv(RUN / "CHOICE_LEGAL_KNOWLEDGE_V2.csv")}
    return index_rows, subj_rows, choice_rows


def build_records() -> tuple[list[dict], dict[str, list[dict]], list[str]]:
    OUT.mkdir(parents=True, exist_ok=True)
    suite_rows = read_csv(RUN / "SOURCE_MATCH_LEDGER_V2.csv")
    items = load_cache_items(suite_rows)
    items_by_suite: dict[str, list[CacheItem]] = defaultdict(list)
    for item in items:
        if item.suite_id:
            items_by_suite[item.suite_id].append(item)
    index_rows, subj_map, choice_map = load_question_texts()
    curation = merge_curation_status()
    records: list[dict] = []
    for row in index_rows:
        key = (row["suite_id"], row["question_no"])
        qtype = row["question_type"]
        source_row = subj_map.get(key, {}) if qtype == "subjective" else choice_map.get(key, {})
        qtext = source_row.get("question_material") or source_row.get("question_excerpt") or row.get("question_excerpt", "")
        qtext = qtext or row.get("question_excerpt", "")
        qtext = trim_next_question_bleed(qtext, row.get("question_no", ""), qtype)
        raw_prompt = source_row.get("complete_prompt") or short(qtext[-260:], 260)
        legal_prompt, legal_scope_method, module_exclusion = legal_scope_prompt(qtext, raw_prompt, qtype)
        evidence = find_best_evidence({**row, **source_row}, items_by_suite[row["suite_id"]], qtext)
        answer, answer_source, answer_method = ("", "", "")
        candidate_answer, candidate_reason = ("", "")
        if qtype == "choice":
            answer, answer_source, answer_method = find_choice_answer({**row, **source_row}, items_by_suite[row["suite_id"]], qtext, evidence["rubric_text"])
            candidate_answer, candidate_reason = choice_answer_candidate({**row, **source_row}, answer)
            evidence = choice_evidence_from_answer(evidence, answer, answer_source, items_by_suite[row["suite_id"]])
        classification_text = qtext if qtype == "choice" or evidence["evidence_type"] == "paper_source" else qtext + " " + evidence["rubric_text"]
        domain, domain_reason = classify_domain(classification_text)
        front_domain, front_domain_reason = front_domain_for(domain)
        cstatus, creason = curation.get(key, ("", ""))
        include_status = "included"
        if cstatus.startswith("reject"):
            include_status = "excluded_by_curation"
        elif module_exclusion:
            include_status = "excluded_by_module_boundary"
        elif cstatus == "defer_answer_missing" and qtype == "choice" and answer:
            include_status = "included"
        elif cstatus.startswith("defer") and qtype == "choice":
            include_status = "included"
        elif cstatus.startswith("defer"):
            include_status = "included_needs_review"
        elif evidence["evidence_type"] in {"rubric_not_found_yet", "answer_not_locked"}:
            include_status = "included_rubric_not_found_yet"
        if is_included({"include_status": include_status}) and qtype == "choice" and not answer:
            include_status = "included_answer_candidate_only" if candidate_answer else "included_answer_not_locked"
        apoints = answer_points(evidence["rubric_text"], qtype, answer)
        if qtype == "choice" and not answer and candidate_answer:
            apoints = f"官方答案未锁定；本地法律推理候选：{candidate_answer}。理由：{candidate_reason}。不得把候选答案写成官方细则。"
        if legal_scope_method == "legal_subquestion_extracted" and evidence["evidence_type"] == "paper_source":
            evidence["rubric_match_method"] += "|legal_small_question_only"
        record = {
            "question_id": f"{row['suite_id']}_Q{row['question_no']}",
            "label": question_label(row),
            "suite_id": row["suite_id"],
            "year": row["year"],
            "district": row["district"],
            "stage": row["stage"],
            "suite_name": row["suite_name"],
            "question_no": row["question_no"],
            "question_type": qtype,
            "include_status": include_status,
            "curation_status": cstatus,
            "curation_reason": creason,
            "legal_scope_method": legal_scope_method,
            "front_domain": front_domain,
            "front_domain_reason": front_domain_reason,
            "framework_domain": domain,
            "framework_domain_reason": domain_reason,
            "material_triggers": material_triggers(qtext),
            "complete_prompt": legal_prompt,
            "question_text": short(qtext, 3500 if qtype == "subjective" else 1600),
            "rubric_source": evidence["rubric_source"],
            "evidence_type": evidence["evidence_type"],
            "evidence_status": "",
            "rubric_match_method": evidence["rubric_match_method"],
            "secondary_score": evidence["secondary_score"],
            "rubric_text": evidence["rubric_text"],
            "answer": answer,
            "answer_source": answer_source,
            "answer_method": answer_method,
            "candidate_answer": candidate_answer,
            "candidate_answer_reason": candidate_reason,
            "wrong_option_sentences": build_choice_wrong_sentences(qtext, answer) if qtype == "choice" else "",
            "candidate_wrong_option_sentences": build_candidate_wrong_sentences(qtext, candidate_answer, candidate_reason) if qtype == "choice" else "",
            "answer_points": apoints,
            "result_landing": result_landing(evidence["rubric_text"] + " " + qtext, qtype, answer),
            "why_think": why_think(qtext, evidence["rubric_text"], domain),
            "proposition_path": proposition_path(qtext, evidence["rubric_text"], domain),
        }
        record["evidence_status"] = evidence_status(record)
        records.append(record)
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        if is_included(record):
            by_domain[record["framework_domain"]].append(record)
    diagnostics = []
    suite_with_records = {r["suite_id"] for r in records if is_included(r)}
    for suite in suite_rows:
        if suite["suite_id"] not in suite_with_records:
            diagnostics.append(f"- `{suite['suite_id']} {suite['suite_name']}` 未进入法律题合集：{suite['xuanbier_status']}，{suite['notes']}")
    return records, by_domain, diagnostics


def status_badge(record: dict) -> str:
    suffix = ""
    if record.get("evidence_status") == "rubric_match_pending":
        suffix = "｜细则待锁"
    elif record.get("evidence_status") == "answer_pending_official":
        suffix = "｜官方答案待锁"
    if record["include_status"] == "included":
        return "已归位" + suffix
    if record["include_status"] == "included_needs_review":
        return "待拆分/复核后归位" + suffix
    if record["include_status"] == "included_answer_not_locked":
        return "客观题答案待锁定"
    if record["include_status"] == "included_answer_candidate_only":
        return "仅有本地候选答案｜官方答案待锁"
    if record["include_status"] == "included_rubric_not_found_yet":
        return "细则待补锁"
    if record["include_status"] == "excluded_by_module_boundary":
        return "非法律模块排除"
    return record["include_status"]


def write_collection(records: list[dict], diagnostics: list[str]) -> Path:
    path = OUT / "选必二法律题全量处理合集_2026-05-03.md"
    included = [r for r in records if is_included(r)]
    formal_count = sum(1 for r in included if r["evidence_status"] == "formal_scoring_matched")
    rubric_pending = [r for r in included if r["evidence_status"] == "rubric_match_pending"]
    answer_pending = [r for r in included if r["evidence_status"] == "answer_pending_official"]
    needs_review = [r for r in included if r["include_status"] == "included_needs_review"]
    lines = [
        "# 选必二《法律与生活》法律题全量处理合集",
        "",
        "说明：本合集从 v2 原始题源重新汇总，并对“未找到细则”的题做同套卷二次检索。`rubric_match_pending` 表示当前文本层仍未锁定正式细则/评标/阅卷证据，不等于原题没有细则。",
        "",
        f"- 入册法律题：{len(included)}",
        f"- 主观题：{sum(1 for r in included if r['question_type'] == 'subjective')}",
        f"- 选择题：{sum(1 for r in included if r['question_type'] == 'choice')}",
        f"- 已有 formal/评标/阅卷/评分证据：{formal_count}",
        f"- 仍待正式细则锁定：{len(rubric_pending)}",
        f"- 混合/特殊题待拆分复核：{len(needs_review)}",
        f"- 客观题官方答案待锁定：{len(answer_pending)}",
        f"- 客观题仅有本地推理候选：{sum(1 for r in included if r['question_type'] == 'choice' and not r['answer'] and r.get('candidate_answer'))}",
        "",
        "## 使用闸门",
        "",
        "- 细则来源优先级：正式细则/评标/阅卷/评分 > 讲评/阅卷总结 > 参考答案 > 题面推断。",
        "- 参考答案、讲评和题面推断可以帮助归位，但不能单独推动最终主干。",
        "- 混合模块题必须看小问；当前无法拆清的小问保留为待复核，不硬塞进稳定主干。",
        "- 官方答案未锁选择题只保留本地候选，不能生成正式错项判断。",
        "",
    ]
    for record in included:
        lines.extend([
            f"## {record['label']}（{record['question_type']}｜{status_badge(record)}）",
            "",
            f"- 框架归位：{record['framework_domain']}（{record['framework_domain_reason']}）",
            f"- 学生前台归位：{record['front_domain']}（{record['front_domain_reason']}）",
            f"- 证据状态：{record['evidence_status']}",
            f"- 证据等级：{record['evidence_type']}",
            f"- 细则来源：{record['rubric_source'] or '未锁定'}",
            f"- 匹配方式：{record['rubric_match_method']}",
            f"- 法律小问处理：{record.get('legal_scope_method', '')}",
            "",
            "【设问】",
            "",
            record["complete_prompt"],
            "",
            "【材料触发】",
            "",
            record["material_triggers"],
            "",
            "【题面摘录】",
            "",
            record["question_text"],
            "",
            "【细则/答案锚点】",
            "",
            record["rubric_text"] or "当前可读文本层未锁定对应细则，需回原文件/OCR 复核。",
            "",
            "【答案落点】",
            "",
            record["answer_points"],
            "",
            "【命题逻辑】",
            "",
            record["proposition_path"],
            "",
            "【完整解释链】",
            "",
            record["why_think"],
            "",
        ])
        if record["question_type"] == "choice":
            lines.extend([
                "【选择题错项处理】",
                "",
                f"- 答案：{record['answer'] or '未锁定'}",
                f"- 答案来源：{record['answer_source'] or '未锁定'}",
                f"- 错项句：{record['wrong_option_sentences']}",
                f"- 本地候选：{record.get('candidate_answer') or '无'}",
                f"- 候选说明：{record.get('candidate_answer_reason') or '无'}",
                f"- 候选错项句：{record.get('candidate_wrong_option_sentences') or '无'}",
                "",
            ])
    lines.extend([
        "## 待补正式细则清单",
        "",
        *([f"- {r['label']}：{r['evidence_type']}｜{r['rubric_source'] or '未锁定'}" for r in rubric_pending] or ["- 暂无。"]),
        "",
        "## 官方答案待锁清单",
        "",
        *([f"- {r['label']}：本地候选 {r.get('candidate_answer') or '无'}；{r.get('candidate_answer_reason') or '待核'}" for r in answer_pending] or ["- 暂无。"]),
        "",
        "## 未入册/待 OCR 套卷提示",
        "",
        *(diagnostics or ["- 暂无。"]),
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_framework(records: list[dict], by_domain: dict[str, list[dict]]) -> Path:
    path = OUT / "选必二法律与生活最终进化框架_2026-05-03.md"
    included = [r for r in records if is_included(r)]
    formal_included = [r for r in included if r["evidence_status"] == "formal_scoring_matched"]
    rubric_pending = [r for r in included if r["evidence_status"] == "rubric_match_pending"]
    answer_pending = [r for r in included if r["evidence_status"] == "answer_pending_official"]
    needs_review = [r for r in included if r["include_status"] == "included_needs_review"]
    domain_counts = Counter(r["framework_domain"] for r in included)
    formal_domain_counts = Counter(r["framework_domain"] for r in formal_included)
    front_domain_counts = Counter(r["front_domain"] for r in included)
    action_counts = Counter(r["result_landing"] for r in included)
    lines = [
        "# 选必二《法律与生活》最终进化框架",
        "",
        "> 状态：四线审议已回收并进入 Codex 本地融合稿。真实 Claude Opus 4.7 Adaptive 网页初评/交叉批判、ChatGPT 网页 Pro 模式初评/交叉批判、ClaudeCode B 独立生产线均已留痕；但 26 道细则待锁、9 道选择题官方答案待锁、14 道混合/特殊题待复核未清零前，不写最终 Governor PASS。",
        "",
        "## 四线输入与本地裁决",
        "",
        "- Codex A：完成 148 条记录处理，入框 113 题，其中 formal/评标/阅卷/评分证据 78 题。",
        "- ClaudeCode B：独立复核支持现有主干，但提示 26 题仍需细则锁定，不得用参考答案补主干。",
        "- Claude Opus 4.7 Adaptive：认可一核、三问、四步，要求五域只作学生前台，八域降为后台索引，并压制法考化与口号化。",
        "- ChatGPT 网页 Pro：认可候选框架可推进，但要求命题路径分成 6 类，未锁选择题和 included_needs_review 不能进正式学生答案。",
        "- Codex 本地裁决：保留用户的一核二线三问四步五域；吸收两边都同意的 6 题型命题路径、3 必 + 3 选解释链、选择题四排除和宏观口号黑名单；所有新事实仍回本地证据锁定。",
        "",
        "## 总框架",
        "",
        "### 一核",
        "",
        "以事实为根据、以法律为准绳，通过具体法律关系中的规则适用实现定分止争。",
        "",
        "### 二线",
        "",
        "1. 权利保护与权利边界：先保护合法权益，再识别权利行使的事实条件、程序条件、诚信边界和他人边界。",
        "2. 规则适用与程序救济：先把事实放进规则条件，再落到调解、仲裁、诉讼、举证、判决、执行等救济效果。",
        "",
        "价值不单独成线：凡问意义，必须先回到本案法律关系和处理结果，再上升到公平、诚信、家庭伦理、劳动保护、创新秩序等价值。",
        "",
        "### 三问",
        "",
        "1. 判什么/怎么处理：本案应确认什么关系、效力、责任、归属或救济路径。",
        "2. 凭什么：材料事实如何对应教材规则、法定条件、制度要求或程序要求。",
        "3. 有什么意义：本案处理如何保护权利、划清边界、维护秩序、弘扬价值。",
        "",
        "### 四步",
        "",
        "定主体关系 -> 找争点事实 -> 对规则条件 -> 按题型落结果。",
        "",
        "第四步不写成五个并列词，而是按题型选落点：合同题落效力/责任，侵权题落责任方式，物权/继承题落归属，程序题落程序节点和效果，评析/意义题落本案结果再上升制度意图。",
        "",
        "### 3必+3选解释链",
        "",
        "- 3 必：关系句、规则句、结论句。每道主观题至少要回答谁和谁、依据什么规则、最后怎么处理。",
        "- 3 选：争点句、适用句、价值句。争点和适用按分值展开；价值句只在意义/认识/作用/启示题展开。",
        "- 意义题双段：先写“本案中怎样保护权利/划清边界/落实处理结果”，再写“由此维护什么秩序或价值”。",
        "",
        "### 六类命题路径",
        "",
        "1. 裁判依据题：案例事实 -> 双方争议 -> 法院/仲裁处理；奖励关系、事实、规则、责任或效力。",
        "2. 程序救济题：当事人处境 -> 程序节点 -> 法律效果；奖励适格主体、救济路径、程序效果。",
        "3. 表格补全题：看示例 -> 比照案例 -> 补裁判理由/结果/意义；奖励事实和规则对应，不能写空泛话。",
        "4. 观点评析题：拆观点 -> 判合理与片面 -> 给法律依据和本案结论。",
        "5. 意义认识题：本案结果 -> 权利保护 -> 秩序价值；价值后置，先案后升。",
        "6. 选择题：题干事实 -> 题肢关键词 -> 排绝对化、排主体错位、排关系错位、排责任错位。",
        "",
        "### 五域（学生可背版）",
        "",
        "五域沿用用户原始主框架，按“学生第一眼能识别的生活关系 + 高频题量 + 答题动作差异”来切，不按法考章节目录来切。后台八域只是教师备课索引，最后必须回到这五域。",
        "",
        "划分依据：合同/消费/劳动都先判断交易或用工关系与弱势方保护；物权/相邻/继承/家庭都围绕财产归属、身份关系和扶养监护；人格权/侵权围绕损害与责任；知识产权/不正当竞争围绕创新成果、标识和竞争边界；纠纷解决/生态公益/新业态属于程序、公共利益和新场景容器，必须按具体关系回流。",
        "",
    ]
    for name, backend_domains, action in STUDENT_FRONT_DOMAINS:
        count = sum(domain_counts[d] for d in backend_domains)
        formal_count = sum(formal_domain_counts[d] for d in backend_domains)
        lines.append(f"- {name}：{count}题，其中 formal {formal_count}题。抓手：{action}")
    lines.extend([
        "- 注：第5域不是新的实体法目录，而是程序/公共利益/新场景容器；遇题仍要回到主体关系和具体规则。",
        "",
        "### 八域（后台索引版）",
        "",
        "八域只用于 Codex/教师后台做题库标签和回填索引，不作为学生前台背诵主干。",
        "",
        "## 高频主干",
        "",
        f"- 入框法律题：{len(included)}",
        f"- formal/评标/阅卷/评分证据题：{len(formal_included)}",
        f"- 待正式细则锁定题：{len(rubric_pending)}",
        f"- 官方答案待锁选择题：{len(answer_pending)}",
        f"- 混合/特殊题待拆分复核：{len(needs_review)}",
        "- 高频动作一：法律关系判断。没有关系判断，权利、义务、责任、程序和价值都会漂。",
        "- 高频动作二：事实触发规则。材料细节不是背景故事，而是评分条件。",
        "- 高频动作三：结果落点。答案必须落到责任、效力、归属、救济路径、裁判理由或价值意义。",
        "- 高频动作四：价值后置。凡意义题，先回到本案法律关系和处理结果，再谈制度、秩序、价值。",
        "",
        "## 学生答题黑名单",
        "",
        "以下词可以作为题面背景理解，但不能替代本案法律分析：全面依法治国、国家治理体系、社会公平正义、新质生产力、营商环境、织密法治网、彰显司法温度、弘扬文明新风、公正司法的生动实践、法治与德治相结合。出现这些词前，必须先写清本案主体关系、规则依据和处理结果。",
        "",
        "## 题域频次",
        "",
    ])
    lines.append("### 学生前台五域/横切方法口径")
    lines.append("")
    for domain, count in front_domain_counts.most_common():
        lines.append(f"- {domain}：{count}题")
    lines.extend([
        "",
        "### 后台八域索引口径",
        "",
    ])
    for domain, count in domain_counts.most_common():
        lines.append(f"- {domain}：{count}题")
    lines.extend([
        "",
        "## 结果落点观测",
        "",
    ])
    for landing, count in action_counts.most_common(12):
        lines.append(f"- {landing}：{count}题")
    lines.extend(["", "## 框架节点与题目回填", ""])
    ordered_domains = [name for name, _ in FRAMEWORK_DOMAINS]
    for domain in ordered_domains:
        domain_records = by_domain.get(domain, [])
        if not domain_records:
            continue
        lines.extend([
            f"## {domain}",
            "",
            f"本节点当前回填 {len(domain_records)} 道题。核心方法：先定本域的主体关系，再抓事实触发，最后落到法律后果和价值边界。",
            "",
        ])
        for record in sorted(domain_records, key=lambda r: (r["year"], r["district"], r["stage"], int(r["question_no"]))):
            lines.extend([
                f"### {record['label']}（{record['question_type']}｜{status_badge(record)}）",
                "",
                "【材料触发点】",
                "",
                record["material_triggers"],
                "",
                "【学生前台归位】",
                "",
                f"{record['front_domain']}：{record['front_domain_reason']}",
                "",
                "【设问】",
                "",
                record["complete_prompt"],
                "",
                "【为什么能想到】",
                "",
                record["why_think"],
                "",
                "【答案落点】",
                "",
                record["answer_points"],
                "",
                "【命题逻辑】",
                "",
                record["proposition_path"],
                "",
                "【证据闸门】",
                "",
                record["evidence_status"],
                "",
                "【细则锚点】",
                "",
                f"{record['evidence_type']}｜{record['rubric_source'] or '未锁定'}",
                "",
            ])
    blockers = [
        "- `local_source_lock_pending`：真实 GPT/Claude 只能给框架建议，具体答案、题域、采分点仍必须由 Codex 回本地题面和细则核验。",
        f"- `rubric_match_pending`：{len(rubric_pending)} 道题仍待从正式细则/评标/阅卷/评分来源中锁定或人工复核。",
        "- `included_needs_review_pending`：14 道混合/特殊题仍需拆分法律小问或确认是否进入频次。",
        "- `docx_render_word_qa_pending`：DOCX 可生成，但未完成 render/Word 级视觉验收前不写 Word/PDF PASS。",
    ]
    if any(r["question_type"] == "choice" and not r["answer"] for r in included):
        blockers.append("- `choice_answer_lock_pending`：部分选择题答案表仍未从可靠来源锁定；本地推理候选只作课堂复核线索，不作官方答案。")
    lines.extend([
        "## 待补正式细则清单",
        "",
        *([f"- {r['label']}：{r['evidence_type']}｜{r['rubric_source'] or '未锁定'}" for r in rubric_pending] or ["- 暂无。"]),
        "",
        "## 模块边界排除清单",
        "",
        *([f"- {r['label']}：{r['curation_status']}｜{r['curation_reason'] or '非选必二显性设问'}" for r in records if r["include_status"] == "excluded_by_module_boundary"] or ["- 暂无。"]),
        "",
        "## 自我进化流程",
        "",
        "1. 每跑完一个批次，更新题目归位矩阵、题域频次、结果落点频次和无法归位题。",
        "2. Codex 生成本地证据包，只写题面、细则、答案落点、命题路径和硬问题，不让参考答案推动主干。",
        "3. 真实 GPT-5.5 Pro 网页端独立审议主干是否高频、是否覆盖所有题、是否有法考化风险。",
        "4. 真实 Claude Opus 4.7 Adaptive Thinking 网页端独立审议学生可学性、表达压缩度、迁移性和过度抽象风险。",
        "5. GPT 与 Claude 互读对方报告做交叉批判；Codex 只做本地证据裁决，证据不支持的建议进入 defer/reject。",
        "6. 每个 accepted 改动必须说明：解决了哪类题、提升了哪个高频动作、是否增加学生负担、证据等级是什么。",
        "",
        "## 当前阻塞",
        "",
        *blockers,
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_advisor_pack(records: list[dict]) -> Path:
    path = OUT / "真实GPT55Pro_ClaudeOpus47框架审议证据包_2026-05-03.md"
    included = [r for r in records if is_included(r)]
    lines = [
        "# 选必二《法律与生活》真实模型审议证据包",
        "",
        "用途：复制到 GPT-5.5 Pro 网页端和 Claude Opus 4.7 Adaptive Thinking 网页端新对话。不得复用其他项目线程。",
        "",
        "请基于下列本地证据审议框架：主干是否高频、覆盖是否全面、是否过度法考化、是否过度宏观法治化、每个题是否能自然归位。",
        "",
        "硬规则：reference_answer 不能推动主干；没有本地 formal/评标/阅卷/评分证据的新节点只能 candidate/defer。",
        "",
    ]
    for record in included:
        lines.extend([
            f"## {record['label']}",
            f"- 类型：{record['question_type']}",
                f"- 框架归位：{record['framework_domain']}",
                f"- 学生前台归位：{record['front_domain']}",
                f"- 证据等级：{record['evidence_type']}",
            f"- 材料触发：{record['material_triggers']}",
            f"- 设问：{record['complete_prompt']}",
            f"- 答案落点：{short(record['answer_points'], 500)}",
            f"- 命题逻辑：{record['proposition_path']}",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    records, by_domain, diagnostics = build_records()
    ledger_fields = [
        "question_id", "label", "suite_id", "year", "district", "stage", "suite_name", "question_no",
        "question_type", "include_status", "curation_status", "curation_reason", "legal_scope_method", "framework_domain",
        "front_domain", "front_domain_reason", "framework_domain_reason", "material_triggers", "complete_prompt", "question_text", "rubric_source",
        "evidence_type", "evidence_status", "rubric_match_method", "secondary_score", "rubric_text", "answer", "answer_source",
        "answer_method", "candidate_answer", "candidate_answer_reason", "wrong_option_sentences",
        "candidate_wrong_option_sentences", "answer_points", "result_landing", "why_think",
        "proposition_path",
    ]
    write_csv(OUT / "legal_question_chain_ledger_2026-05-03.csv", records, ledger_fields)
    matrix_fields = [
        "question_id", "label", "question_type", "include_status", "legal_scope_method",
        "front_domain", "framework_domain", "result_landing", "evidence_type", "evidence_status", "answer", "candidate_answer", "rubric_source",
    ]
    write_csv(OUT / "FRAMEWORK_PLACEMENT_MATRIX_2026-05-03.csv", records, matrix_fields)
    collection = write_collection(records, diagnostics)
    framework = write_framework(records, by_domain)
    advisor = write_advisor_pack(records)
    included = [r for r in records if is_included(r)]
    print(f"records={len(records)} included={len(included)}")
    print(f"formal={sum(1 for r in included if r['evidence_status']=='formal_scoring_matched')}")
    print(f"rubric_pending={sum(1 for r in included if r['evidence_status']=='rubric_match_pending')}")
    print(f"choice_answer_pending={sum(1 for r in included if r['question_type']=='choice' and not r['answer'])}")
    print(f"choice_answer_candidate_only={sum(1 for r in included if r['question_type']=='choice' and not r['answer'] and r.get('candidate_answer'))}")
    print(collection)
    print(framework)
    print(advisor)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
