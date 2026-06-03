#!/usr/bin/env python3
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

RUN_ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
MANIFEST = RUN_ROOT / "00_manifest" / "source_manifest.csv"
OUT_CAND = RUN_ROOT / "01_subjective_candidates"
OUT_MAT = RUN_ROOT / "02_material_atoms"
OUT_RUB = RUN_ROOT / "03_rubric_atoms"

LEGAL_PATTERNS = [
    "法律与生活", "民法典", "劳动法", "劳动合同法", "消费者权益保护法", "反不正当竞争法",
    "合同", "侵权", "违约", "欺诈", "可撤销", "无效", "赔偿", "责任", "权利", "义务",
    "诉讼", "法院", "人民法院", "判决", "诉讼请求", "起诉", "举证", "调解", "仲裁",
    "继承", "遗产", "赡养", "扶养", "抚养", "监护", "未成年人", "婚姻", "夫妻",
    "人格权", "名誉权", "肖像权", "隐私权", "著作权", "版权", "知识产权", "专利", "商标",
    "不正当竞争", "消费者", "经营者", "劳动者", "用人单位", "格式条款", "相邻关系",
    "物权", "所有权", "质权", "担保物权", "用益物权", "司法确认", "司法建议",
    "生命权", "健康权", "知情权", "自主选择权", "公平交易权", "惩罚性赔偿",
]

EXPLICIT_MODULE_PATTERNS = ["运用《法律与生活》", "运用“法律与生活”", "《法律与生活》知识", "法律与生活知识"]
STRONG_LEGAL_PATTERNS = [
    "法律与生活", "民法典", "劳动法", "劳动合同法", "消费者权益保护法", "反不正当竞争法",
    "合同", "侵权", "违约", "欺诈", "可撤销", "无效", "诉讼请求", "原告", "被告",
    "起诉", "举证", "仲裁", "调解协议", "继承", "遗产", "赡养", "扶养", "监护",
    "未成年人", "人格权", "名誉权", "肖像权", "隐私权", "著作权", "版权", "知识产权",
    "专利", "商标", "不正当竞争", "消费者", "经营者", "劳动者", "用人单位",
    "格式条款", "相邻关系", "物权", "质权", "担保物权", "用益物权", "司法确认",
    "惩罚性赔偿", "停止侵害", "排除妨碍", "赔偿损失",
]
OTHER_MODULE_MARKERS = {
    "必修三": ["《政治与法治》", "政治与法治知识", "法治政府", "全面依法治国", "基层治理"],
    "经济": ["《经济与社会》", "经济与社会知识"],
    "哲学": ["《哲学与文化》", "哲学与文化知识", "哲学"],
    "国政经": ["《当代国际政治与经济》", "当代国际政治与经济知识"],
    "逻辑": ["《逻辑与思维》", "逻辑与思维知识", "创新思维", "抽象思维"],
}
ASK_PATTERNS = ["说明", "评析", "论证", "建议", "意义", "原因", "启示", "分析", "谈谈", "理由", "认识"]
NON_XUANBIER_RISK_PATTERNS = ["全面依法治国", "法治政府", "基层治理", "人民代表大会", "人大", "政府", "全过程人民民主", "党的领导", "法治国家"]
SUBJECTIVE_QNO_MIN = 16
SUBJECTIVE_QNO_MAX = 22


def read_manifest():
    with MANIFEST.open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    return rows


def get_text_path(row):
    m = re.search(r"extracted_text=([^;]+)", row.get("notes", ""))
    if not m:
        return None
    p = Path(m.group(1))
    return p if p.exists() else None


def get_text(row):
    p = get_text_path(row)
    if not p:
        return ""
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def suite_key(row):
    return (row["year"], row["district"], row["exam_stage"])


def legal_score(text):
    score = 0
    hits = []
    for pat in LEGAL_PATTERNS:
        if pat in text:
            hits.append(pat)
            score += 3 if pat in EXPLICIT_MODULE_PATTERNS or pat in {"法律与生活", "民法典"} else 1
    return score, hits


def strong_legal_hits(text):
    return [pat for pat in STRONG_LEGAL_PATTERNS if pat in text]


def other_module_hits(text):
    hits = []
    for module, markers in OTHER_MODULE_MARKERS.items():
        for marker in markers:
            if marker in text:
                hits.append(module)
                break
    return hits


def page_or_slide_before(text, start):
    prefix = text[:start]
    markers = re.findall(r"\[(page|slide)\s+(\d+)\]", prefix, flags=re.I)
    if markers:
        kind, num = markers[-1]
        return f"{kind.lower()} {num}"
    return ""


def qno_from_filename(name):
    m = re.search(r"(?<!\d)(1[6-9]|2[0-2])\s*[题.]?\s*[\(（]?\s*([一二三四五六七八九0-9]*)", name)
    if m:
        return m.group(1), normalize_subq(m.group(2))
    return "", ""


def normalize_subq(raw):
    raw = (raw or "").strip()
    trans = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6"}
    return trans.get(raw, raw)


def segment_question_blocks(text, file_name):
    # Build question-like blocks. Works for papers, rubrics, and per-question marking reports.
    markers = []
    pattern = re.compile(r"(?m)(?:^|\n)\s*(1[6-9]|2[0-2])\s*(?:[\.．、]|[（(]\s*([一二三四五六七八九0-9])\s*[)）]|题)")
    for m in pattern.finditer(text):
        markers.append((m.start(), m.group(1), normalize_subq(m.group(2))))
    if not markers:
        qno, subq = qno_from_filename(file_name)
        if qno:
            return [(0, len(text), qno, subq, text)]
        return []
    blocks = []
    for i, (start, qno, subq) in enumerate(markers):
        end = markers[i + 1][0] if i + 1 < len(markers) else len(text)
        block = text[start:end].strip()
        if block:
            blocks.append((start, end, qno, subq, block))
    return blocks


def find_candidate_segments(rows):
    segments = []
    relevant_roles = {
        "paper", "answer", "subjective_rubric", "evaluation_standard", "marking_report", "lecture"
    }
    for row in rows:
        if row["suspected_role"] not in relevant_roles:
            continue
        text = get_text(row)
        if not text.strip():
            continue
        for start, end, qno, subq, block in segment_question_blocks(text, row["file_name"]):
            try:
                qnum = int(qno)
            except Exception:
                continue
            if not (SUBJECTIVE_QNO_MIN <= qnum <= SUBJECTIVE_QNO_MAX):
                continue
            score, hits = legal_score(block)
            strong_hits = strong_legal_hits(block)
            explicit = any(p in block for p in EXPLICIT_MODULE_PATTERNS)
            if len(strong_hits) < 2 and not explicit:
                # Single broad legal words such as rights/responsibility are too weak.
                if not (strong_hits and any(k in block for k in ["法院", "人民法院", "判决", "诉至", "仲裁", "诉讼"])):
                    continue
            if row["suspected_role"] == "lecture" and len(strong_hits) < 2 and not explicit:
                continue
            if len(block) < 40:
                continue
            segments.append({
                "file_id": row["file_id"],
                "file_path": row["original_file_path"],
                "file_name": row["file_name"],
                "year": row["year"],
                "district": row["district"],
                "exam_stage": row["exam_stage"],
                "role": row["suspected_role"],
                "qno": qno,
                "subq": subq,
                "text": block,
                "page": page_or_slide_before(text, start),
                "score": score,
                "hits": hits,
                "explicit_module": explicit,
                "locator": f"{row['file_id']}:{page_or_slide_before(text, start) or 'text'}",
            })
    return segments


def choose_best_segment(segments, roles):
    candidates = [s for s in segments if s["role"] in roles]
    if not candidates:
        return None
    role_rank = {
        "evaluation_standard": 0,
        "marking_report": 1,
        "subjective_rubric": 2,
        "lecture": 3,
        "answer": 4,
        "paper": 5,
    }
    return sorted(candidates, key=lambda s: (role_rank.get(s["role"], 9), -s["score"], len(s["text"])))[0]


def evidence_from_segment(seg):
    if not seg:
        return "missing", "missing"
    role = seg["role"]
    name = seg["file_name"]
    text = seg["text"]
    if role == "evaluation_standard":
        return "evaluation_standard", "formal"
    if role == "marking_report":
        return "marking_report", "formal"
    if role == "subjective_rubric":
        if any(k in name + text[:200] for k in ["细则", "评分", "评标", "阅卷"]):
            return "marking_rubric", "formal"
        return "teacher_reference_answer", "reference_only"
    if role == "lecture":
        if any(k in text for k in ["给分", "得分", "分）", "评分", "细则", "踩点", "扣分"]):
            return "lecture_explicit_scoring", "formal"
        return "grading_commentary", "reference_only"
    if role == "answer":
        return "teacher_reference_answer", "reference_only"
    return "missing", "missing"


def split_ask_material(text):
    ask_matches = list(re.finditer(r"(结合材料[\s\S]{0,260}?(?:。|？|\?|$)|运用《法律与生活》[\s\S]{0,180}?(?:。|？|\?|$)|请(?:你)?[\s\S]{0,180}?(?:说明|评析|论证|分析|谈谈|阐述|建议|理由|认识)[\s\S]{0,180}?(?:。|？|\?|$))", text))
    if ask_matches:
        m = ask_matches[-1]
        ask = m.group(1).strip()
        material = (text[:m.start()] + "\n" + text[m.end():]).strip()
        return material, ask
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    ask_lines = [ln for ln in lines if any(k in ln for k in ASK_PATTERNS) and ("?" in ln or "？" in ln or "结合" in ln or "运用" in ln)]
    ask = ask_lines[-1] if ask_lines else ""
    material = text.replace(ask, "", 1).strip() if ask else text
    return material, ask


def ask_function(ask):
    if "评析" in ask or "评价" in ask or "评议" in ask:
        return "评析"
    if "论证" in ask or "阐释" in ask or "阐明" in ask:
        return "论证"
    if "建议" in ask or "措施" in ask or "怎么办" in ask:
        return "建议"
    if "意义" in ask or "价值" in ask:
        return "意义"
    if "原因" in ask or "理由" in ask or "为什么" in ask:
        return "原因"
    if "启示" in ask:
        return "启示"
    if "说明" in ask or "分析" in ask:
        return "说明"
    if ask:
        return "综合"
    return "不确定"


def module_risk(full, ask):
    text = full + "\n" + ask
    explicit = any(p in text for p in EXPLICIT_MODULE_PATTERNS)
    strong_hits = strong_legal_hits(text)
    other_hits = other_module_hits(ask)
    non_hits = [p for p in NON_XUANBIER_RISK_PATTERNS if p in text]
    if explicit and other_hits:
        return "综合"
    if explicit:
        return "选必二"
    if other_hits:
        return other_hits[0]
    if len(strong_hits) >= 2:
        return "选必二"
    if strong_hits and any(k in text for k in ["法院", "人民法院", "判决", "诉至", "仲裁", "诉讼"]):
        return "选必二"
    if non_hits:
        return "必修三"
    if strong_hits:
        return "不确定"
    return "不确定"


def confidence_level(paper_seg, evidence_seg, risk):
    if paper_seg and evidence_seg and risk == "选必二":
        et, el = evidence_from_segment(evidence_seg)
        if el == "formal":
            return "high"
    if paper_seg or evidence_seg:
        return "medium" if risk in {"选必二", "综合"} else "low"
    return "low"


def split_sentences(text):
    text = re.sub(r"\s+", " ", text.strip())
    pieces = re.split(r"(?<=[。！？?；;])\s*|(?:\n+)", text)
    out = []
    for p in pieces:
        p = p.strip(" \t　")
        if 8 <= len(p) <= 260:
            out.append(p)
    return out


def split_rubric_points(text):
    points = []
    text = re.sub(r"\r\n?", "\n", text)
    # Prefer explicit numbered scoring lines.
    chunks = re.split(r"(?=(?:^|\n)\s*(?:[①②③④⑤⑥⑦⑧⑨]|\d+[\.、．]|\(\d+\)|（\d+）))", text)
    for c in chunks:
        c = c.strip()
        if not c:
            continue
        if any(k in c for k in ["分", "给分", "得分", "支持", "理由", "依据", "责任", "权利", "义务", "法院", "合同", "侵权", "消费者", "劳动", "民法典"]):
            points.append(c)
    if not points:
        points = split_sentences(text)
    cleaned = []
    for p in points:
        p = re.sub(r"\s+", " ", p).strip()
        if 6 <= len(p) <= 500:
            cleaned.append(p)
    return cleaned[:20]


def legal_signal(text):
    _, hits = legal_score(text)
    return "；".join(hits[:8])


def main():
    OUT_CAND.mkdir(parents=True, exist_ok=True)
    OUT_MAT.mkdir(parents=True, exist_ok=True)
    OUT_RUB.mkdir(parents=True, exist_ok=True)
    rows = read_manifest()
    segments = find_candidate_segments(rows)

    by_key = defaultdict(list)
    for s in segments:
        key = (s["year"], s["district"], s["exam_stage"], s["qno"], s["subq"])
        by_key[key].append(s)

    candidates = []
    material_atoms = []
    ask_atoms = []
    rubric_atoms = []
    missing = []
    uncertain = []
    rejected = []

    sorted_items = sorted(by_key.items(), key=lambda kv: kv[0])
    for idx, (key, segs) in enumerate(sorted_items, start=1):
        year, district, stage, qno, subq = key
        if not year or not district or not stage:
            continue
        paper_seg = choose_best_segment(segs, {"paper"})
        evidence_seg = choose_best_segment(segs, {"evaluation_standard", "marking_report", "subjective_rubric", "lecture", "answer"})
        answer_seg = choose_best_segment(segs, {"answer", "subjective_rubric", "lecture"})
        source_seg = paper_seg or evidence_seg or segs[0]
        full_text = source_seg["text"] if source_seg else ""
        material, ask = split_ask_material(full_text)
        exact_other_book_ask = any(
            marker in ask
            for marker in [
                "《政治与法治》", "《经济与社会》", "《哲学与文化》",
                "《当代国际政治与经济》", "《逻辑与思维》",
                "政治与法治知识", "经济与社会知识", "哲学与文化知识",
                "当代国际政治与经济知识", "逻辑与思维知识",
            ]
        )
        if exact_other_book_ask and not any(p in ask for p in EXPLICIT_MODULE_PATTERNS):
            rejected.append({
                "year": year,
                "district": district,
                "exam_stage": stage,
                "question_no": qno,
                "sub_question_no": subq,
                "reason": "ask explicitly names another module; excluded from main candidate pool",
                "ask_text": ask,
                "source_locator": " | ".join(sorted(set(s["locator"] for s in segs))),
            })
            continue
        risk = module_risk(full_text, ask)
        if risk in {"必修三", "经济", "哲学", "国政经", "逻辑"} and not any(p in full_text for p in EXPLICIT_MODULE_PATTERNS):
            if len(strong_legal_hits(full_text)) < 3:
                continue
        evidence_type, evidence_level = evidence_from_segment(evidence_seg)
        confidence = confidence_level(paper_seg, evidence_seg, risk)
        qid = f"Q{idx:04d}_{year}_{district}_{stage}_{qno}{('_' + subq) if subq else ''}"
        why_yes = []
        if any(p in full_text for p in EXPLICIT_MODULE_PATTERNS):
            why_yes.append("设问明确要求运用《法律与生活》知识")
        hits = legal_signal(full_text)
        if hits:
            why_yes.append(f"题面/证据含法律规则信号：{hits}")
        if evidence_level == "formal":
            why_yes.append(f"存在 formal 证据：{evidence_type}")
        why_no = []
        if risk != "选必二":
            why_no.append(f"模块边界不是强确定选必二：{risk}")
        if "法治" in full_text and "法律与生活" not in full_text:
            why_no.append("出现法治表达但未明确《法律与生活》，需防必修三化")
        if evidence_level in {"reference_only", "missing"}:
            why_no.append(f"证据等级为 {evidence_level}，不能单独支撑框架核心节点")
        if not paper_seg:
            why_no.append("未从原试卷文本层锁定题面，可能需回源/OCR")

        cand = {
            "question_id": qid,
            "year": year,
            "district": district,
            "exam_stage": stage,
            "source_paper_file": paper_seg["file_path"] if paper_seg else "",
            "paper_page": paper_seg["page"] if paper_seg else "",
            "question_no": qno,
            "sub_question_no": subq,
            "full_question_text": full_text,
            "material_text": material,
            "ask_text": ask,
            "answer_file": answer_seg["file_path"] if answer_seg else "",
            "answer_page": answer_seg["page"] if answer_seg else "",
            "answer_text": answer_seg["text"] if answer_seg else "",
            "rubric_file": evidence_seg["file_path"] if evidence_seg else "",
            "rubric_page": evidence_seg["page"] if evidence_seg else "",
            "rubric_text": evidence_seg["text"] if evidence_seg else "",
            "evidence_type": evidence_type,
            "evidence_level": evidence_level,
            "why_candidate_subjective_law_question": "；".join(why_yes) or "法律词较多，暂作候选",
            "why_maybe_not_subjective_law_question": "；".join(why_no) or "暂无明显排除理由，仍需 ClaudeCode 独立复核",
            "module_boundary_risk": risk,
            "confidence": confidence,
            "source_locator": " | ".join(sorted(set(s["locator"] for s in segs))),
            "notes": "Codex heuristic extraction; must be audited against original pages and formal rubrics.",
        }
        candidates.append(cand)
        if risk != "选必二" or confidence == "low":
            uncertain.append(cand)
        if evidence_level in {"missing", "reference_only"}:
            missing.append(cand)

        material_sentences = split_sentences(material)
        mat_ids = []
        for m_idx, sent in enumerate(material_sentences[:24], start=1):
            mat_id = f"M_{qid}_{m_idx:02d}"
            mat_ids.append(mat_id)
            material_atoms.append({
                "material_atom_id": mat_id,
                "question_id": qid,
                "material_phrase": sent,
                "plain_description": sent,
                "subject_or_actor": "",
                "action_or_event": "",
                "affected_party": "",
                "conflict_or_problem": "yes" if any(k in sent for k in ["纠纷", "争议", "诉", "赔", "侵权", "违约", "欺诈", "未履行"]) else "",
                "legal_signal_if_any": legal_signal(sent),
                "possible_relevance_to_answer": "contains legal/fact trigger" if legal_signal(sent) else "background or value context",
                "source_locator": cand["source_locator"],
                "uncertainty": "heuristic_sentence_split",
            })

        ask_id = f"A_{qid}_01"
        ask_atoms.append({
            "ask_atom_id": ask_id,
            "question_id": qid,
            "ask_text": ask,
            "ask_function_plain": ask_function(ask),
            "module_requirement": "法律与生活" if "法律与生活" in ask else ("法治知识" if "法治" in ask else "不确定"),
            "requires_material_connection": "yes" if "结合材料" in ask else "uncertain",
            "requires_value_discussion": "yes" if any(k in ask + full_text for k in ["意义", "价值", "现实", "社会", "引导"]) else "uncertain",
            "requires_behavior_evaluation": "yes" if any(k in ask for k in ["评析", "认识", "判断", "支持", "驳回"]) else "uncertain",
            "requires_solution_or_measure": "yes" if any(k in ask for k in ["建议", "措施", "怎么办"]) else "no",
            "student_task_plain": ask or "从材料和法律证据中判断作答任务",
            "source_locator": cand["source_locator"],
        })

        rubric_source = cand["rubric_text"] or cand["answer_text"]
        for r_idx, point in enumerate(split_rubric_points(rubric_source), start=1):
            rub_id = f"R_{qid}_{r_idx:02d}"
            related = []
            point_hits = set(legal_signal(point).split("；")) if legal_signal(point) else set()
            for atom in material_atoms:
                if atom["question_id"] != qid:
                    continue
                atom_hits = set(atom["legal_signal_if_any"].split("；")) if atom["legal_signal_if_any"] else set()
                if point_hits and atom_hits and point_hits.intersection(atom_hits):
                    related.append(atom["material_atom_id"])
            if not related:
                related = mat_ids[:2]
            kmv = "uncertain"
            has_knowledge = bool(legal_signal(point))
            has_material = any(k in point for k in ["材料", "本案", "王某", "公司", "法院", "被告", "原告", "当事人", "平台", "劳动者", "消费者"])
            has_value = any(k in point for k in ["维护", "促进", "引导", "规范", "公平", "正义", "秩序", "价值", "社会"])
            if has_knowledge and has_material and has_value:
                kmv = "knowledge+material+value"
            elif has_knowledge and has_material:
                kmv = "knowledge+material"
            elif has_knowledge and has_value:
                kmv = "knowledge+value"
            elif has_material and has_value:
                kmv = "material+value"
            elif has_knowledge:
                kmv = "knowledge"
            elif has_material:
                kmv = "material"
            elif has_value:
                kmv = "value"
            rubric_atoms.append({
                "rubric_atom_id": rub_id,
                "question_id": qid,
                "rubric_or_answer_phrase": point,
                "evidence_type": evidence_type,
                "evidence_level": evidence_level,
                "plain_reward_description": point,
                "related_material_atom_ids": "|".join(related),
                "what_expression_is_rewarded": point,
                "what_judgment_student_must_make_before_writing": "判断法律关系/行为性质/责任或程序路径，需回源细化",
                "legal_knowledge_or_rule_if_explicit": legal_signal(point),
                "value_expression_if_explicit": "；".join([k for k in ["维护", "促进", "引导", "规范", "公平", "正义", "秩序"] if k in point]),
                "knowledge_material_value_type": kmv,
                "can_be_written_without_material": "no" if has_material else "uncertain",
                "source_locator": cand["source_locator"],
                "uncertainty": "heuristic_atom_split; verify original rubric line",
            })

    # Suite-level no/uncertain reports.
    suites = defaultdict(list)
    for r in rows:
        if r["year"] and r["district"] and r["exam_stage"] and r["suspected_role"] == "paper":
            suites[suite_key(r)].append(r)
    candidate_suite_keys = {(c["year"], c["district"], c["exam_stage"]) for c in candidates}
    no_rows = []
    for sk, paper_rows in sorted(suites.items()):
        if sk in candidate_suite_keys:
            continue
        statuses = {r["text_layer_status"] for r in paper_rows}
        no_rows.append({
            "year": sk[0],
            "district": sk[1],
            "exam_stage": sk[2],
            "paper_files": "|".join(r["original_file_path"] for r in paper_rows),
            "status": "uncertain_no_text_or_ocr_gap" if statuses.intersection({"image_pdf", "no_text_layer", "corrupted"}) else "no_related_subjective_law_question_found_by_codex",
            "notes": "选择题忽略；仅基于文本层和法律主观题关键词保守判定",
        })

    write_csv_jsonl(
        OUT_CAND / "all_candidate_subjective_law_questions_codex.csv",
        OUT_CAND / "all_candidate_subjective_law_questions_codex.jsonl",
        candidates,
    )
    write_csv(OUT_CAND / "uncertain_subjective_cases_codex.csv", uncertain)
    write_csv(OUT_CAND / "missing_answer_or_rubric_codex.csv", missing)
    write_csv(OUT_CAND / "no_subjective_law_question_papers_codex.csv", no_rows)
    write_csv(OUT_CAND / "rejected_likely_non_xuanbier_subjective_codex.csv", rejected)
    write_csv(OUT_MAT / "material_atoms_subjective_codex.csv", material_atoms)
    write_csv(OUT_MAT / "ask_atoms_subjective_codex.csv", ask_atoms)
    write_csv(OUT_RUB / "rubric_atoms_subjective_codex.csv", rubric_atoms)

    print(json.dumps({
        "candidate_questions": len(candidates),
        "uncertain_cases": len(uncertain),
        "missing_or_reference_only": len(missing),
        "no_or_uncertain_suites": len(no_rows),
        "rejected_likely_non_xuanbier": len(rejected),
        "material_atoms": len(material_atoms),
        "ask_atoms": len(ask_atoms),
        "rubric_atoms": len(rubric_atoms),
    }, ensure_ascii=False, indent=2))


def write_csv(path, rows):
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_csv_jsonl(csv_path, jsonl_path, rows):
    write_csv(csv_path, rows)
    with jsonl_path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
