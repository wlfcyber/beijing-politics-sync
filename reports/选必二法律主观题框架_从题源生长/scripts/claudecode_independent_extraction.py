#!/usr/bin/env python3
"""Claude Code B: independent re-extraction and audit of 选必二 法律与生活 subjective candidates.

Independently re-reads extracted text files (which are the only currently
available textualization of the source corpus) and applies stricter rules than
Codex's heuristic script, especially around:

  * module boundary (必修三 / 经济与社会 / 哲学与文化 / 当代国际政治与经济 / 逻辑与思维 → reject)
  * evidence level (only true marking rubrics / evaluation standards become
    formal; reference answers stay reference_only)
  * the 2026 石景山 期末 exclusion (rule 12)
  * question segmentation (16-22 subjective slot in Beijing politics paper)

Then it diffs against Codex's candidate file and produces the required audit
CSVs and Markdown report.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

RUN_ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
MANIFEST = RUN_ROOT / "00_manifest" / "source_manifest.csv"
EXTRACTED_DIR = RUN_ROOT / "00_manifest" / "extracted_text"

OUT_CAND = RUN_ROOT / "01_subjective_candidates"
OUT_MAT = RUN_ROOT / "02_material_atoms"
OUT_RUB = RUN_ROOT / "03_rubric_atoms"
OUT_AUDIT = RUN_ROOT / "04_merge_audit"

# ---------------------------------------------------------------------------
# 选必二《法律与生活》-anchored vocabulary.  The book covers:
#   民事法律基础(民法典)/合同/民事权利/婚姻继承/家庭/人格权
#   就业创业(劳动合同法/劳动法/劳动争议)
#   消费者权益/反不正当竞争/产品责任
#   解决纠纷(民事诉讼/调解/仲裁/和解)
#
# Tokens here are intentionally specific to 选必二.  Generic "法律/权利/责任/法治"
# alone are forbidden — they trigger 必修三 false positives.

STRONG_XB2_TOKENS = [
    # 民法 / 合同
    "民法典", "民事主体", "民事法律行为", "民事行为能力", "民事责任",
    "合同的订立", "要约", "承诺", "格式条款", "违约责任", "违约金", "定金",
    "解除合同", "可撤销", "可变更", "重大误解", "欺诈", "胁迫", "显失公平",
    # 物权 / 用益
    "物权", "所有权", "用益物权", "担保物权", "质权", "抵押权", "相邻关系",
    "占有", "添附",
    # 人格权
    "人格权", "生命权", "身体权", "健康权", "姓名权", "肖像权", "名誉权",
    "隐私权", "个人信息保护", "荣誉权",
    # 婚姻家庭继承
    "夫妻共同财产", "夫妻共同债务", "彩礼", "扶养", "赡养", "抚养",
    "法定继承", "遗嘱继承", "代位继承", "转继承", "遗产", "遗赠",
    "监护", "监护人", "未成年人监护",
    # 知识产权
    "著作权", "版权", "邻接权", "专利权", "商标权", "知识产权",
    # 劳动 / 就业
    "劳动合同法", "劳动法", "劳动合同", "劳动者", "用人单位", "试用期",
    "劳动报酬", "经济补偿", "工伤", "社会保险", "劳动争议", "劳动仲裁",
    # 消费者 / 经营者
    "消费者权益保护法", "反不正当竞争法", "消费者协会", "经营者",
    "惩罚性赔偿", "三倍赔偿", "退一赔三", "产品责任", "知情权", "自主选择权",
    "公平交易权", "九条龙",
    # 侵权
    "侵权责任", "侵权责任法", "停止侵害", "排除妨害", "消除危险",
    "返还财产", "恢复原状", "赔礼道歉", "消除影响", "恢复名誉", "赔偿损失",
    # 民事诉讼 / ADR
    "民事诉讼", "起诉", "立案", "原告", "被告", "第三人", "举证责任",
    "诉讼请求", "诉讼时效", "管辖", "上诉", "再审", "调解书",
    "调解协议", "司法确认", "和解", "仲裁裁决",
    # 模块自身
    "法律与生活",
]

# Higher-priority tokens that almost guarantee 选必二 framing if the verb is in
# 16-22 subjective slot.
ANCHOR_XB2_TOKENS = [
    "法律与生活", "民法典", "劳动合同法", "消费者权益保护法",
    "反不正当竞争法", "侵权责任", "劳动合同", "格式条款",
    "肖像权", "名誉权", "隐私权", "著作权", "继承", "监护",
    "诉讼请求", "举证责任", "仲裁",
]

# Explicit instruction phrases that name 选必二 as the required knowledge frame.
EXPLICIT_XB2_INSTRUCTIONS = [
    "运用《法律与生活》", "运用“法律与生活”", "运用法律与生活",
    "结合《法律与生活》", "结合法律与生活",
    "《法律与生活》知识", "法律与生活的知识",
    "运用《法律与生活》模块", "运用《法律与生活》中的",
]

# Other-module instruction phrases — if the ask explicitly names them, reject.
OTHER_MODULE_INSTRUCTIONS = {
    "必修三": [
        "运用《政治与法治》", "结合《政治与法治》", "《政治与法治》知识",
        "政治与法治知识", "运用政治与法治",
    ],
    "经济与社会": [
        "运用《经济与社会》", "结合《经济与社会》", "《经济与社会》知识",
        "经济与社会知识",
    ],
    "哲学与文化": [
        "运用《哲学与文化》", "结合《哲学与文化》", "《哲学与文化》知识",
        "哲学与文化知识", "唯物辩证法", "认识论", "矛盾分析",
    ],
    "当代国际政治与经济": [
        "运用《当代国际政治与经济》", "当代国际政治与经济知识",
    ],
    "逻辑与思维": [
        "运用《逻辑与思维》", "逻辑与思维知识", "辩证思维", "创新思维",
        "抽象思维", "形式逻辑",
    ],
}

# 必修三-flavored frames that pull the question away from 选必二 even when the
# word "法律" appears.
BIZHU3_FRAMES = [
    "全面依法治国", "法治政府", "法治国家", "法治社会", "法治建设",
    "依法行政", "依法执政", "基层治理", "人民代表大会", "全过程人民民主",
    "党的领导", "公民有序政治参与", "立法权", "立法机关", "中国特色社会主义法律体系",
]

ASK_VERBS = [
    "评析", "评价", "评议", "说明", "分析", "阐述", "阐释", "论证",
    "建议", "措施", "理由", "原因", "认识", "意义", "启示", "谈谈",
    "判断", "结合材料", "如何", "怎样",
]

SUBJ_QNO_MIN = 16
SUBJ_QNO_MAX = 22


def read_manifest():
    with MANIFEST.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def get_text_path(row):
    m = re.search(r"extracted_text=([^;]+)", row.get("notes", ""))
    if not m:
        return None
    p = Path(m.group(1))
    return p if p.exists() else None


def read_text(row):
    p = get_text_path(row)
    if not p:
        return ""
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def page_marker_before(text, idx):
    prefix = text[:idx]
    marks = re.findall(r"\[(page|slide)\s+(\d+)\]", prefix, flags=re.I)
    if marks:
        kind, num = marks[-1]
        return f"{kind.lower()} {num}"
    return ""


# ---------------------------------------------------------------------------

def segment_subjective_blocks(text, file_name):
    """Cut text into question-numbered blocks within 16-22.

    Also handle papers where the subjective section uses bare numbers without
    a trailing 题/.
    """
    pattern = re.compile(
        r"(?m)(?:^|\n|\s)\s*(1[6-9]|2[0-2])\s*(?:[\.．、]|[（(]\s*([一二三四五六七八九12345])\s*[)）])"
    )
    markers = [
        (m.start(), m.group(1), _norm_subq(m.group(2)))
        for m in pattern.finditer(text)
    ]
    if not markers:
        return []
    blocks = []
    for i, (start, qno, subq) in enumerate(markers):
        end = markers[i + 1][0] if i + 1 < len(markers) else len(text)
        block = text[start:end].strip()
        if not block or len(block) < 40:
            continue
        blocks.append({
            "start": start,
            "end": end,
            "qno": qno,
            "subq": subq,
            "text": block,
            "page": page_marker_before(text, start),
        })
    return blocks


def _norm_subq(raw):
    raw = (raw or "").strip()
    table = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5"}
    return table.get(raw, raw)


def strong_token_hits(text):
    return [t for t in STRONG_XB2_TOKENS if t in text]


def anchor_token_hits(text):
    return [t for t in ANCHOR_XB2_TOKENS if t in text]


def explicit_xb2(text):
    return any(p in text for p in EXPLICIT_XB2_INSTRUCTIONS)


def explicit_other_module(text):
    for mod, pats in OTHER_MODULE_INSTRUCTIONS.items():
        for p in pats:
            if p in text:
                return mod, p
    return None, None


def bizhu3_frame_hits(text):
    return [k for k in BIZHU3_FRAMES if k in text]


def classify_module(full_text, ask_text):
    """Returns (verdict, reason_str).  verdict ∈ {选必二, 必修三, 经济, 哲学, 国政, 逻辑, 综合, 不确定}."""
    explicit_x = explicit_xb2(ask_text) or explicit_xb2(full_text[:1200])
    other_mod, other_marker = explicit_other_module(ask_text)
    if explicit_x and other_mod:
        return "综合", f"both explicit 法律与生活 and {other_mod}"
    if other_mod and not explicit_x:
        return other_mod, f"ask names other module: {other_marker}"
    if explicit_x:
        return "选必二", "explicit 法律与生活 instruction"
    anchors = anchor_token_hits(full_text)
    strong = strong_token_hits(full_text)
    bizhu3 = bizhu3_frame_hits(full_text)
    # ask-text containing only 必修三 frames blocks 选必二 claim
    ask_bizhu3 = bizhu3_frame_hits(ask_text)
    if ask_bizhu3 and not anchors:
        return "必修三", f"ask contains 必修三 frame {ask_bizhu3}, no 选必二 anchor"
    if len(anchors) >= 1 and not (ask_bizhu3 and not strong):
        return "选必二", f"anchor tokens: {anchors[:5]}"
    if len(strong) >= 3 and not bizhu3:
        return "选必二", f"≥3 strong 选必二 tokens: {strong[:5]}"
    if len(strong) >= 2 and any(k in full_text for k in ["法院", "起诉", "诉讼", "判决", "仲裁"]):
        return "选必二", f"strong tokens + 司法/ADR signal: {strong[:5]}"
    if bizhu3 and len(strong) < 2:
        return "必修三", f"必修三 frame {bizhu3[:3]}, weak 选必二 signal"
    if strong:
        return "不确定", f"only weak 选必二 tokens: {strong[:5]}"
    return "不确定", "no clear module signal"


# ---------------------------------------------------------------------------

def split_ask_and_material(block_text):
    """Best-effort split of material vs ask text."""
    candidates = list(re.finditer(
        r"((?:结合材料|结合上述材料|结合本案|运用《[^》]+》|运用[一-龥、，,]{0,40}知识|依据材料|根据材料)[\s\S]{0,400}?(?:。|\?|？|$))",
        block_text,
    ))
    if candidates:
        m = candidates[-1]
        ask = m.group(1).strip()
        material = (block_text[: m.start()] + "\n" + block_text[m.end():]).strip()
        return material, ask
    # Fallback: trailing question
    lines = [ln.strip() for ln in block_text.splitlines() if ln.strip()]
    for ln in reversed(lines):
        if ("?" in ln or "？" in ln) and any(v in ln for v in ASK_VERBS):
            return block_text.replace(ln, "", 1).strip(), ln
    return block_text, ""


def ask_function(ask):
    for v in ["评析", "评价", "评议"]:
        if v in ask:
            return "评析"
    for v in ["论证", "阐释", "阐述"]:
        if v in ask:
            return "论证"
    if "建议" in ask or "措施" in ask:
        return "建议"
    if "意义" in ask or "价值" in ask:
        return "意义"
    if "原因" in ask or "理由" in ask or "为什么" in ask:
        return "原因"
    if "启示" in ask:
        return "启示"
    if "说明" in ask or "分析" in ask:
        return "说明"
    return "综合" if ask else "不确定"


# ---------------------------------------------------------------------------

def evidence_assess(role, file_name, block_text):
    name_text = (file_name or "") + " " + block_text[:300]
    has_scoring_words = any(k in name_text for k in [
        "评分细则", "评分标准", "阅卷细则", "评标", "阅卷报告",
        "评分参考", "踩点", "评分细化", "答题示例分析", "评卷",
    ])
    has_levelled_rubric = bool(re.search(r"水平[1-4一二三四]\s*\|", block_text)) or "等级赋分" in block_text
    has_score_points = bool(re.search(r"\d+\s*分\s*[。；,，]|每点\s*\d+\s*分|\(\s*\d+\s*分\s*\)", block_text))

    if role == "evaluation_standard":
        if has_levelled_rubric or has_score_points or has_scoring_words:
            return "evaluation_standard", "formal"
        return "evaluation_standard", "reference_only"
    if role == "marking_report":
        if has_score_points or "阅卷" in name_text or "答题情况" in name_text:
            return "marking_report", "formal"
        return "grading_commentary", "reference_only"
    if role == "subjective_rubric":
        if "细则" in name_text or "评分" in name_text or "评标" in name_text or has_levelled_rubric:
            return "marking_rubric", "formal"
        return "teacher_reference_answer", "reference_only"
    if role == "lecture":
        if has_score_points and ("评分" in block_text or "细则" in block_text or "得分" in block_text or "踩点" in block_text):
            return "lecture_explicit_scoring", "formal"
        return "grading_commentary", "reference_only"
    if role == "answer":
        return "teacher_reference_answer", "reference_only"
    return "missing", "missing"


# ---------------------------------------------------------------------------

def is_shijing_2026_qm(year, district, stage):
    return year == "2026" and district == "石景山" and stage == "期末"


def collect_segments(rows):
    relevant_roles = {
        "paper", "answer", "subjective_rubric",
        "evaluation_standard", "marking_report", "lecture",
    }
    segments = []
    for row in rows:
        role = row["suspected_role"]
        if role not in relevant_roles:
            continue
        if not row["year"] or not row["district"] or not row["exam_stage"]:
            continue
        text = read_text(row)
        if not text.strip():
            continue
        for blk in segment_subjective_blocks(text, row["file_name"]):
            qno = blk["qno"]
            try:
                qnum = int(qno)
            except ValueError:
                continue
            if not SUBJ_QNO_MIN <= qnum <= SUBJ_QNO_MAX:
                continue
            seg = dict(blk)
            seg.update({
                "file_id": row["file_id"],
                "file_path": row["original_file_path"],
                "file_name": row["file_name"],
                "year": row["year"],
                "district": row["district"],
                "exam_stage": row["exam_stage"],
                "role": role,
                "locator": f"{row['file_id']}:{blk['page'] or 'text'}",
            })
            segments.append(seg)
    return segments


def best_by_role(segs, role_set, rank_map):
    cands = [s for s in segs if s["role"] in role_set]
    if not cands:
        return None
    return sorted(cands, key=lambda s: (rank_map.get(s["role"], 9), -len(s["text"])))[0]


def split_rubric_points(text):
    text = re.sub(r"\r\n?", "\n", text)
    points = []
    chunks = re.split(
        r"(?=(?:^|\n)\s*(?:[①②③④⑤⑥⑦⑧⑨⑩]|\d+[\.、．)]|\(\d+\)|（\d+）|第\d+))",
        text,
    )
    for c in chunks:
        c = re.sub(r"\s+", " ", c).strip()
        if 8 <= len(c) <= 600:
            points.append(c)
    if not points:
        for s in re.split(r"(?<=[。！？?；;])\s*", text):
            s = re.sub(r"\s+", " ", s).strip()
            if 10 <= len(s) <= 600:
                points.append(s)
    return points[:25]


def split_material_sentences(text):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[。！？?；;])\s*", text)
    out = []
    for p in parts:
        p = p.strip(" \t　")
        if 10 <= len(p) <= 300:
            out.append(p)
    return out


def signal_summary(text):
    hits = strong_token_hits(text)
    return "；".join(hits[:8])


# ---------------------------------------------------------------------------

def main():
    OUT_CAND.mkdir(parents=True, exist_ok=True)
    OUT_MAT.mkdir(parents=True, exist_ok=True)
    OUT_RUB.mkdir(parents=True, exist_ok=True)
    OUT_AUDIT.mkdir(parents=True, exist_ok=True)

    rows = read_manifest()
    segments = collect_segments(rows)

    role_rank = {
        "evaluation_standard": 0,
        "marking_report": 1,
        "subjective_rubric": 2,
        "lecture": 3,
        "answer": 4,
        "paper": 5,
    }

    grouped = defaultdict(list)
    for s in segments:
        grouped[(s["year"], s["district"], s["exam_stage"], s["qno"], s["subq"])].append(s)

    candidates = []
    material_atoms = []
    ask_atoms = []
    rubric_atoms = []

    rejected_module = []  # non-选必二 found in same paper slot
    risky_locator = []
    suspended_shijing = []

    for idx, (key, segs) in enumerate(sorted(grouped.items()), start=1):
        year, district, stage, qno, subq = key
        paper_seg = best_by_role(segs, {"paper"}, role_rank)
        evidence_seg = best_by_role(
            segs, {"evaluation_standard", "marking_report", "subjective_rubric", "lecture"}, role_rank,
        )
        answer_seg = best_by_role(segs, {"answer", "subjective_rubric", "lecture"}, role_rank)
        source_seg = paper_seg or evidence_seg or answer_seg or segs[0]
        full_text = source_seg["text"]
        material, ask = split_ask_and_material(full_text)

        verdict, reason = classify_module(full_text, ask)
        if verdict != "选必二":
            rejected_module.append({
                "year": year, "district": district, "exam_stage": stage,
                "question_no": qno, "sub_question_no": subq,
                "verdict": verdict, "reason": reason,
                "ask_text": ask[:300],
                "source_locator": " | ".join(sorted({s["locator"] for s in segs})),
            })
            continue

        # Hard rule 12: 2026 石景山 期末 excluded unless an explicit usable
        # 评分细则 was supplied for this very law question — we conservatively
        # treat *no* rubric file we have today as "user-confirmed", so this
        # always lands in the suspended list.
        if is_shijing_2026_qm(year, district, stage):
            suspended_shijing.append({
                "year": year, "district": district, "exam_stage": stage,
                "question_no": qno, "sub_question_no": subq,
                "reason": "rule 12: 2026 石景山 期末 excluded; no confirmed user-supplied formal rubric available in current corpus",
                "source_locator": " | ".join(sorted({s["locator"] for s in segs})),
            })
            continue

        evidence_type, evidence_level = evidence_assess(
            evidence_seg["role"] if evidence_seg else "",
            evidence_seg["file_name"] if evidence_seg else "",
            evidence_seg["text"] if evidence_seg else "",
        )
        if not evidence_seg:
            evidence_type, evidence_level = "missing", "missing"

        qid = f"CC{idx:04d}_{year}_{district}_{stage}_{qno}{('_' + subq) if subq else ''}"
        anchors = anchor_token_hits(full_text)
        bizhu3 = bizhu3_frame_hits(full_text)

        why_yes_parts = [reason]
        if anchors:
            why_yes_parts.append(f"anchor 法律与生活 tokens: {anchors[:6]}")
        if evidence_level == "formal":
            why_yes_parts.append(f"formal 证据: {evidence_type}")

        why_no_parts = []
        if not paper_seg:
            why_no_parts.append("未在 role=paper 文本层中定位到题面（仅通过证据文档间接重建）")
            risky_locator.append({
                "question_id_candidate": qid,
                "year": year, "district": district, "exam_stage": stage,
                "question_no": qno, "sub_question_no": subq,
                "issue": "no paper-role segment for this question; locator derived from rubric/answer file",
                "source_locator": " | ".join(sorted({s["locator"] for s in segs})),
            })
        if bizhu3:
            why_no_parts.append(f"题面出现必修三框架词 {bizhu3[:3]}，需复核是否综合题")
        if evidence_level == "reference_only":
            why_no_parts.append("证据等级 reference_only，不得单独支撑框架核心节点")
        if evidence_level == "missing":
            why_no_parts.append("无评分细则/阅卷报告，需补充证据后再纳入归纳")

        confidence = "high" if (paper_seg and evidence_level == "formal") else (
            "medium" if (paper_seg or evidence_seg) else "low"
        )

        cand = {
            "question_id": qid,
            "year": year, "district": district, "exam_stage": stage,
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
            "why_candidate_subjective_law_question": "；".join(why_yes_parts),
            "why_maybe_not_subjective_law_question": "；".join(why_no_parts) or "暂无显著疑点",
            "module_boundary_risk": "选必二",
            "confidence": confidence,
            "source_locator": " | ".join(sorted({s["locator"] for s in segs})),
            "notes": "ClaudeCode B independent extraction from text-layer corpus; PDF OCR not regenerated this pass.",
        }
        candidates.append(cand)

        # ---- material atoms ----
        mat_ids = []
        for m_idx, sent in enumerate(split_material_sentences(material)[:24], start=1):
            mid = f"M_{qid}_{m_idx:02d}"
            mat_ids.append(mid)
            material_atoms.append({
                "material_atom_id": mid,
                "question_id": qid,
                "material_phrase": sent,
                "plain_description": sent,
                "subject_or_actor": "",
                "action_or_event": "",
                "affected_party": "",
                "conflict_or_problem": "yes" if any(k in sent for k in ["纠纷","争议","诉","赔","侵权","违约","欺诈","拒不","未履行"]) else "",
                "legal_signal_if_any": signal_summary(sent),
                "possible_relevance_to_answer": "carries 法律事实/规则信号" if signal_summary(sent) else "背景或价值铺垫",
                "source_locator": cand["source_locator"],
                "uncertainty": "heuristic_sentence_split_from_text_layer",
            })

        # ---- ask atoms ----
        ask_atoms.append({
            "ask_atom_id": f"A_{qid}_01",
            "question_id": qid,
            "ask_text": ask,
            "ask_function_plain": ask_function(ask),
            "module_requirement": "法律与生活" if explicit_xb2(ask) else ("法律与生活(默认)" if anchors else "不确定"),
            "requires_material_connection": "yes" if "结合材料" in ask or "结合本案" in ask or "结合上述材料" in ask else "uncertain",
            "requires_value_discussion": "yes" if any(k in ask + full_text for k in ["意义","价值","引导","规范","促进","公平","正义","秩序"]) else "uncertain",
            "requires_behavior_evaluation": "yes" if any(k in ask for k in ["评析","评价","判断","支持","驳回","认识"]) else "uncertain",
            "requires_solution_or_measure": "yes" if any(k in ask for k in ["建议","措施","怎么办","如何"]) else "no",
            "student_task_plain": ask or "从材料与法律证据中判断作答任务",
            "source_locator": cand["source_locator"],
        })

        # ---- rubric atoms ----
        rubric_text = cand["rubric_text"] or cand["answer_text"]
        for r_idx, point in enumerate(split_rubric_points(rubric_text), start=1):
            rid = f"R_{qid}_{r_idx:02d}"
            point_signal = signal_summary(point)
            related = []
            for atom in material_atoms:
                if atom["question_id"] != qid:
                    continue
                inter = set(point_signal.split("；")) & set(atom["legal_signal_if_any"].split("；"))
                if point_signal and atom["legal_signal_if_any"] and inter:
                    related.append(atom["material_atom_id"])
            if not related:
                related = mat_ids[:2]
            has_kn = bool(point_signal)
            has_mat = any(k in point for k in ["材料","本案","王某","李某","张某","公司","法院","被告","原告","当事人","平台","劳动者","消费者"])
            has_val = any(k in point for k in ["维护","促进","引导","规范","公平","正义","秩序","价值","社会"])
            kmv = {
                (True, True, True): "knowledge+material+value",
                (True, True, False): "knowledge+material",
                (True, False, True): "knowledge+value",
                (False, True, True): "material+value",
                (True, False, False): "knowledge",
                (False, True, False): "material",
                (False, False, True): "value",
            }.get((has_kn, has_mat, has_val), "uncertain")
            rubric_atoms.append({
                "rubric_atom_id": rid,
                "question_id": qid,
                "rubric_or_answer_phrase": point,
                "evidence_type": evidence_type,
                "evidence_level": evidence_level,
                "plain_reward_description": point,
                "related_material_atom_ids": "|".join(related),
                "what_expression_is_rewarded": point,
                "what_judgment_student_must_make_before_writing": "判断法律关系/行为性质/责任承担或程序路径(回源细化)",
                "legal_knowledge_or_rule_if_explicit": point_signal,
                "value_expression_if_explicit": "；".join(k for k in ["维护","促进","引导","规范","公平","正义","秩序"] if k in point),
                "knowledge_material_value_type": kmv,
                "can_be_written_without_material": "no" if has_mat else "uncertain",
                "source_locator": cand["source_locator"],
                "uncertainty": "heuristic_atom_split_from_text_layer; needs回源核细则原文",
            })

    # --- write claudecode primary outputs ---
    _write_csv_jsonl(
        OUT_CAND / "all_candidate_subjective_law_questions_claudecode.csv",
        OUT_CAND / "all_candidate_subjective_law_questions_claudecode.jsonl",
        candidates,
    )
    _write_csv(OUT_MAT / "material_atoms_subjective_claudecode.csv", material_atoms)
    _write_csv(OUT_MAT / "ask_atoms_subjective_claudecode.csv", ask_atoms)
    _write_csv(OUT_RUB / "rubric_atoms_subjective_claudecode.csv", rubric_atoms)

    # ---- diff vs Codex ----
    codex_path = OUT_CAND / "all_candidate_subjective_law_questions_codex.csv"
    with codex_path.open(encoding="utf-8-sig") as f:
        codex = list(csv.DictReader(f))

    def k(r):
        return (r["year"], r["district"], r["exam_stage"], r["question_no"], r.get("sub_question_no", ""))

    cc_keys = {k(r): r for r in candidates}
    cx_keys = {k(r): r for r in codex}

    missing_from_codex = []
    for kk, ccr in cc_keys.items():
        if kk not in cx_keys:
            missing_from_codex.append({
                "year": kk[0], "district": kk[1], "exam_stage": kk[2],
                "question_no": kk[3], "sub_question_no": kk[4],
                "claudecode_question_id": ccr["question_id"],
                "reason": "Found by ClaudeCode independent extraction; absent in Codex output",
                "evidence_level": ccr["evidence_level"],
                "source_locator": ccr["source_locator"],
            })
    _write_csv(OUT_AUDIT / "claudecode_missing_from_codex.csv", missing_from_codex)

    false_positive = []
    for kk, cxr in cx_keys.items():
        if kk not in cc_keys:
            # Why did ClaudeCode reject it?
            reason_bits = []
            for rj in rejected_module:
                if (rj["year"], rj["district"], rj["exam_stage"], rj["question_no"], rj["sub_question_no"]) == kk:
                    reason_bits.append(f"ClaudeCode 模块判定为 {rj['verdict']}：{rj['reason']}")
                    break
            else:
                if is_shijing_2026_qm(kk[0], kk[1], kk[2]):
                    reason_bits.append("ClaudeCode 按硬规则12 剔除 2026石景山期末")
                else:
                    reason_bits.append("ClaudeCode 在题号16-22主观槽位未识别到该题或证据全部缺失")
            false_positive.append({
                "codex_question_id": cxr["question_id"],
                "year": kk[0], "district": kk[1], "exam_stage": kk[2],
                "question_no": kk[3], "sub_question_no": kk[4],
                "codex_module_risk": cxr.get("module_boundary_risk", ""),
                "codex_evidence_type": cxr.get("evidence_type", ""),
                "codex_evidence_level": cxr.get("evidence_level", ""),
                "claudecode_reason_for_rejection": "; ".join(reason_bits),
                "codex_ask_text": cxr.get("ask_text", "")[:300],
            })
    _write_csv(OUT_AUDIT / "claudecode_false_positive_candidates.csv", false_positive)

    evidence_disagreements = []
    for kk, ccr in cc_keys.items():
        cxr = cx_keys.get(kk)
        if not cxr:
            continue
        if ccr["evidence_level"] != cxr["evidence_level"] or ccr["evidence_type"] != cxr["evidence_type"]:
            evidence_disagreements.append({
                "year": kk[0], "district": kk[1], "exam_stage": kk[2],
                "question_no": kk[3], "sub_question_no": kk[4],
                "codex_evidence_type": cxr["evidence_type"],
                "codex_evidence_level": cxr["evidence_level"],
                "claudecode_evidence_type": ccr["evidence_type"],
                "claudecode_evidence_level": ccr["evidence_level"],
                "direction": (
                    "codex_upgraded" if cxr["evidence_level"] == "formal" and ccr["evidence_level"] != "formal"
                    else ("codex_downgraded" if ccr["evidence_level"] == "formal" and cxr["evidence_level"] != "formal" else "type_differ")
                ),
                "claudecode_question_id": ccr["question_id"],
                "codex_question_id": cxr["question_id"],
            })
    _write_csv(OUT_AUDIT / "claudecode_evidence_level_disagreements.csv", evidence_disagreements)

    module_disagreements = []
    for kk, cxr in cx_keys.items():
        if kk in cc_keys:
            if cxr.get("module_boundary_risk") != "选必二":
                module_disagreements.append({
                    "year": kk[0], "district": kk[1], "exam_stage": kk[2],
                    "question_no": kk[3], "sub_question_no": kk[4],
                    "codex_module_risk": cxr["module_boundary_risk"],
                    "claudecode_verdict": "选必二",
                    "note": "ClaudeCode 上调为 选必二，但仍需仔细复核",
                })
            continue
        # codex says 选必二 but claudecode rejects
        if cxr.get("module_boundary_risk") == "选必二":
            reject_match = next(
                (rj for rj in rejected_module
                 if (rj["year"], rj["district"], rj["exam_stage"], rj["question_no"], rj["sub_question_no"]) == kk),
                None,
            )
            module_disagreements.append({
                "year": kk[0], "district": kk[1], "exam_stage": kk[2],
                "question_no": kk[3], "sub_question_no": kk[4],
                "codex_module_risk": cxr["module_boundary_risk"],
                "claudecode_verdict": reject_match["verdict"] if reject_match else "rejected/not-found",
                "note": (reject_match["reason"] if reject_match else "ClaudeCode 未识别此题为选必二主观题"),
            })
    _write_csv(OUT_AUDIT / "claudecode_module_boundary_disagreements.csv", module_disagreements)

    _write_csv(OUT_AUDIT / "claudecode_locator_or_ocr_risks.csv", risky_locator)

    # ---- audit report ----
    report = _build_report(
        candidates=candidates, codex=codex,
        missing=missing_from_codex, false_positives=false_positive,
        evidence_disagreements=evidence_disagreements,
        module_disagreements=module_disagreements,
        risky_locator=risky_locator,
        suspended_shijing=suspended_shijing,
        rejected_module=rejected_module,
    )
    (OUT_AUDIT / "claudecode_independent_audit_report.md").write_text(report, encoding="utf-8")

    summary = {
        "claudecode_candidates": len(candidates),
        "codex_candidates": len(codex),
        "missing_from_codex": len(missing_from_codex),
        "codex_false_positives": len(false_positive),
        "evidence_disagreements": len(evidence_disagreements),
        "module_disagreements": len(module_disagreements),
        "risky_locator": len(risky_locator),
        "suspended_shijing": len(suspended_shijing),
        "material_atoms": len(material_atoms),
        "ask_atoms": len(ask_atoms),
        "rubric_atoms": len(rubric_atoms),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def _build_report(*, candidates, codex, missing, false_positives, evidence_disagreements,
                  module_disagreements, risky_locator, suspended_shijing, rejected_module):
    formal_count = sum(1 for c in candidates if c["evidence_level"] == "formal")
    ref_count = sum(1 for c in candidates if c["evidence_level"] == "reference_only")
    miss_count = sum(1 for c in candidates if c["evidence_level"] == "missing")
    codex_formal = sum(1 for c in codex if c["evidence_level"] == "formal")
    upgrade_n = sum(1 for d in evidence_disagreements if d["direction"] == "codex_upgraded")
    downgrade_n = sum(1 for d in evidence_disagreements if d["direction"] == "codex_downgraded")
    fp_serious = [fp for fp in false_positives if "非选必二" in fp["claudecode_reason_for_rejection"] or "模块" in fp["claudecode_reason_for_rejection"] or "rule 12" in fp["claudecode_reason_for_rejection"] or "石景山" in fp["claudecode_reason_for_rejection"]]

    if formal_count == 0:
        verdict = "FAIL"
    elif (upgrade_n + len(fp_serious)) > 0 or miss_count > 0 or risky_locator or suspended_shijing:
        verdict = "CONDITIONAL_PASS"
    else:
        verdict = "PASS"

    lines = [
        "# ClaudeCode B 独立审计报告 — 选必二《法律与生活》主观题",
        "",
        "_本报告全部基于 ClaudeCode 在 00_manifest/extracted_text/ 文本层语料上独立再抽取的结果，"
        "与 Codex A 的 01_subjective_candidates/all_candidate_subjective_law_questions_codex.csv 做对照。_",
        "",
        f"**审计裁定 (Verdict): `{verdict}`**",
        "",
        "## 1. 总体指标",
        "",
        f"- Codex 候选题数: **{len(codex)}**（formal={codex_formal}）",
        f"- ClaudeCode 候选题数: **{len(candidates)}**（formal={formal_count}, reference_only={ref_count}, missing={miss_count}）",
        f"- Codex 有但 ClaudeCode 拒收: **{len(false_positives)}**",
        f"- ClaudeCode 有但 Codex 漏收: **{len(missing)}**",
        f"- 证据等级分歧（含 Codex 升级/降级）: **{len(evidence_disagreements)}**（codex 升级为 formal 共 {upgrade_n} 条；codex 偏低 {downgrade_n} 条）",
        f"- 模块边界分歧: **{len(module_disagreements)}**",
        f"- 题面回源风险（仅在证据文件中重建出 16-22 槽位、未在 role=paper 命中）: **{len(risky_locator)}**",
        f"- 2026 石景山 期末 按硬规则 12 暂挂题数: **{len(suspended_shijing)}**",
        f"- 经模块边界判定剔除的 16-22 主观槽位段落: **{len(rejected_module)}**",
        "",
        "## 2. Codex 是否漏题？",
        "",
        f"独立抽取发现 **{len(missing)}** 处 Codex 未收的 16-22 主观槽段。请见 `claudecode_missing_from_codex.csv`。",
        "主要漏题原因猜想（基于 Codex 脚本逻辑 `extract_codex_candidates_and_atoms.py` 的阈值）：",
        "- 在多模块合编 docx 中段落跨模块且 strong_legal_hits<2，Codex 未保留；",
        "- 部分题面没有“运用《法律与生活》”等显式短语，Codex 凭关键词数量阈值收紧后丢弃。",
        "",
        "## 3. Codex 是否误收？",
        "",
        f"ClaudeCode 对 Codex 候选中 **{len(false_positives)}** 条做出拒收判定，其中模块边界类拒收 **{len(fp_serious)}** 条。",
        "代表性误收风险：",
        "- 多模块合编 docx（如必修1/必修2/必修3/选必二混排）中，靠近“运用《法律与生活》”字样的题段被错误吸附；",
        "- ask_text 实质属于经济与社会/政治与法治/哲学与文化，但因为材料附近散落 “权利/责任/义务/法治” 而被 Codex 误收；",
        "- 例：`Q0001_2024_东城_一模_16` ask 实为“资源优化配置/区域协调”——属经济与社会题，Codex 仍标 evaluation_standard formal。",
        "",
        "## 4. Codex 是否把 reference_only 升级为 formal？",
        "",
        f"评级冲突共 **{len(evidence_disagreements)}** 条，其中 codex 把 reference 升为 formal 的有 **{upgrade_n}** 条，"
        f"codex 把本应是 formal 的判低有 **{downgrade_n}** 条。",
        "Codex 评级风险来自其规则：",
        "- 把 role=evaluation_standard / marking_report 一律视为 formal，未要求文本本身含等级量表/分点扣分；",
        "- 把 role=subjective_rubric 文件名含 “细则/评分/评标/阅卷” 即一律 formal，未要求级别赋分模板；",
        "- 这会把 “参考答案+评分要点提示” 性质的文件升格为 formal。",
        "ClaudeCode 改为：必须文本中含等级量表(水平1-4)或显式 X 分扣分点或文件名带“评分细则/评标/阅卷”才标 formal。",
        "",
        "## 5. 必须降级的题",
        "",
        f"按 ClaudeCode 评级规则，下列 **{upgrade_n}** 条 Codex 标为 formal 的应降级为 reference_only —— 详见 `claudecode_evidence_level_disagreements.csv` 中 direction=codex_upgraded 行。",
        "在这些题获得真正的官方评分细则/阅卷报告/等级量表之前，不得作为框架核心节点支撑证据。",
        "",
        "## 6. 不能进入第一轮归纳的题",
        "",
        "- 所有 evidence_level=missing 的题（共 {0} 条 Codex；{1} 条 ClaudeCode）。".format(
            sum(1 for c in codex if c["evidence_level"] == "missing"), miss_count,
        ),
        "- 所有被 ClaudeCode 模块边界判定剔除的 Codex 候选（见 `claudecode_module_boundary_disagreements.csv`）。",
        "- 2026 石景山 期末 全部题目，直至用户给出可用 formal 评分细则（硬规则 12，本批次共 {} 题暂挂）。".format(len(suspended_shijing)),
        "- 题面回源风险题（见 `claudecode_locator_or_ocr_risks.csv`），需先回试卷原 PDF 校核 page/题号后再纳入。",
        "",
        "## 7. 可以进入第一轮开放归纳的题",
        "",
        f"在 ClaudeCode 候选 {len(candidates)} 题中，evidence_level=formal 且 paper-role 文本同时定位到题面者为 "
        f"**{sum(1 for c in candidates if c['evidence_level']=='formal' and c['source_paper_file'])}** 题，"
        "建议作为第一轮 GPT/Claude 开放归纳的最小可信集。其余 formal 但题面来自证据文件重建的题，"
        "需先解决 `claudecode_locator_or_ocr_risks.csv` 列出的回源缺口。",
        "",
        "## 8. 主要数据完整性 / OCR / 题号风险",
        "",
        f"- 题面未在 role=paper 文本层命中、仅靠证据文件重建定位：{len(risky_locator)} 条。",
        "- 当前批次未对 image_pdf / corrupted / no_text_layer 的原始 PDF 进行重新 OCR；这部分材料对应的题面与细则可能整体缺席于本审计。",
        "- 所有 source_locator 字段以 `Fxxxx:page/slide N` 形式记录，可回查 00_manifest/source_manifest.csv 与 extracted_text/Fxxxx.txt 的页/幻灯片标记。",
        "",
        "## 9. 旧选必二成果",
        "",
        "本次审计未引用任何旧选必二框架/题库/错肢库结论；ClaudeCode 候选完全由本批 extracted_text 现场抽取生成，符合 D003 与硬规则 11。",
        "",
        "## 10. 建议下一步",
        "",
        "1. 优先补齐 ClaudeCode 候选中 `evidence_level∈{reference_only, missing}` 的题对应的 *官方* 评分细则或阅卷报告；",
        "2. 对 `claudecode_locator_or_ocr_risks.csv` 列出的题回原始 PDF 校页/校题号；",
        "3. 对 `claudecode_false_positive_candidates.csv` 中“模块边界拒收”的 Codex 候选，"
        "由用户/人工最终裁定是否确属其他模块；",
        "4. 在硬规则 12 解除前，2026 石景山 期末 整套不进入归纳。",
        "",
    ]
    return "\n".join(lines)


def _write_csv(path, rows):
    if not rows:
        path.write_text("", encoding="utf-8-sig")
        return
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def _write_csv_jsonl(csv_path, jsonl_path, rows):
    _write_csv(csv_path, rows)
    with jsonl_path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
