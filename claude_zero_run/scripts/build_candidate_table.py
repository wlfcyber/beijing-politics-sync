#!/usr/bin/env python3
"""Step 2 (proper): per-question candidate table with real prompt/material/rubric excerpts."""
import csv, re
from pathlib import Path

EXTRACTED = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted")
MANIFEST = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/01_source_manifest.csv")
HITS = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_paper_hit_dump.md")
OUT_CSV = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_candidate_subjective_law_questions.csv")
OUT_MD = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_uncertain_or_boundary_cases.md")

LEGAL_TERMS = [
    "民法典","合同","违约","履约","履行合同","买卖合同","服务合同",
    "格式条款","撤销合同","解除合同","无效合同",
    "侵权","侵权责任","损害赔偿","精神损害",
    "消费者权益","消费者","经营者","三倍赔偿","退一赔三","退一赔十","知情权","欺诈","假冒","虚假宣传",
    "劳动合同","劳动关系","劳动者","用人单位","试用期","竞业限制","经济补偿","工伤","新业态劳动者",
    "平台用工","外卖骑手","网约工","灵活就业",
    "人格权","隐私权","名誉权","姓名权","肖像权","个人信息保护","个人信息",
    "知识产权","著作权","专利权","商标权","商业秘密","不正当竞争",
    "婚姻","继承","遗嘱","法定继承","遗赠扶养","监护","未成年人保护","赡养",
    "相邻关系","物权","所有权","用益物权","担保物权","绿色原则",
    "调解","仲裁","诉讼","举证责任","举证","证据规则",
    "好意同乘","公平责任","过错责任","无过错责任",
    "民事行为能力","限制民事行为能力","无民事行为能力",
]
NEG_TERMS = ["人民代表大会","全国人大","国务院","依法治国","公正司法",
             "立法机关","行政复议","行政诉讼","宪法宣誓","民族区域自治",
             "基层群众自治","村民委员会","居民委员会"]

def load_manifest():
    with MANIFEST.open() as f:
        return list(csv.DictReader(f))

ANS_SECTION_HEADERS = re.compile(r"参考答案|【答案】|答案[:：]|评分细则|参考示例|教师版答案|考点考查")

def _is_q_header_line(lines, i):
    ln = lines[i]
    if re.match(r"^\s*\d{1,2}[\.\．、]\d", ln):
        return None
    m = re.match(r"^\s*(\d{1,2})[\.\．、]\s*(.*)$", ln)
    if not m: return None
    q = int(m.group(1))
    if not (16 <= q <= 25): return None
    rest = m.group(2).strip()
    if rest:
        if re.match(r"^\d+\s*%", rest): return None
        if re.search(r"[一-龥]|[（(]|分", rest):
            return q
        return None
    for j in range(i+1, min(i+6, len(lines))):
        s = lines[j].strip()
        if not s: continue
        if re.match(r"^\d+\s*%", s) or re.match(r"^\d+[\.\．]\d", s):
            return None
        if re.search(r"[一-龥]", s) and ("分" in s or len(s) > 8 or "（" in s or "(" in s):
            return q
        return None
    return None

def split_questions(text):
    lines = text.split("\n")
    answer_start = len(lines)
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s == "参考答案" or s.startswith("参考答案") or "【答案】" in ln or s == "【参考答案】":
            answer_start = i
            break
    indices = []
    seen_q = set()
    for i in range(answer_start):
        q = _is_q_header_line(lines, i)
        if q is not None and q not in seen_q:
            indices.append((i, q))
            seen_q.add(q)
    chunks = {}
    for k, (i, q) in enumerate(indices):
        end = indices[k+1][0] if k+1 < len(indices) else answer_start
        # detect page anchor near i if pymupdf inserted "===== PAGE n ====="
        page_no = "?"
        for j in range(max(0,i-30), i):
            mm = re.search(r"PAGE\s+(\d+)", lines[j])
            if mm:
                page_no = mm.group(1)
        chunks[q] = {"start": i, "end": end, "page": page_no, "text": "\n".join(lines[i:end])}
    return chunks

def extract_prompt(chunk_text: str) -> str:
    """Pull out the 设问 portion — typically (1)(2)(3) tail and instructions."""
    # Heuristic: take any line that contains a 设问 cue
    lines = chunk_text.split("\n")
    cues = ["（1）","（2）","（3）","（4）","(1)","(2)","(3)","(4)",
            "运用","结合","简要","分析","说明","谈谈","评析","判断"]
    captured = []
    for ln in lines:
        if any(c in ln for c in cues):
            captured.append(ln.strip())
    # If too long, take last ~25 lines (the prompts at end of material)
    if not captured:
        return ""
    return "\n".join(captured)[:2500]

ANSWER_MARKERS = [
    r"参考答案", r"参考示例", r"答案要点", r"细则", r"评分细则", r"评分参考",
    r"评分标准", r"评分说明", r"等级水平", r"水平[1-4]", r"考点考查",
    r"【分析】", r"【详解】", r"参考答", r"分值",
    r"[（(][0-9]{1,2}\s*分[）)]",   # (N分) scoring annotation
    r"^[①②③④⑤⑥⑦⑧⑨⑩]",          # bullet points typical to answer body
    r"^[一二三四五六七八九十][\.\．、]",  # 一. 二. 三.
    r"得分要点",
    r"答案[:：]",
    r"教师版",
]
ANS_RE = re.compile("|".join(ANSWER_MARKERS), re.M)
PROMPT_MOD_RE = re.compile(r"运用[《<]\s*([^》>]+?)\s*[》>]?\s*知识")
SCORE_TOKEN_RE = re.compile(r"[（(][0-9]{1,2}\s*分[）)]")

def extract_material(chunk_text: str) -> str:
    """Material is the case/situation before 设问. Stop at first answer/rubric marker."""
    m = ANS_RE.search(chunk_text)
    text = chunk_text[:m.start()] if m else chunk_text
    return text[:3500]

def is_paper_with_answer_text(chunk_text: str) -> bool:
    return bool(ANS_RE.search(chunk_text))

def find_rubric_for(suite: str, qno: int, manifest_recs, manifest_by_suite) -> dict:
    """Search rubric/rubric_like files in the suite for chunk matching this question."""
    if qno is None:
        return {"file":"", "page":"", "excerpt":"", "level":"missing", "note":"no qno"}
    recs = manifest_by_suite.get(suite, [])
    # rubric > rubric_like > supplement
    priority = {"rubric":0, "rubric_like":1, "supplement":2}
    cands = [r for r in recs if r["role"] in priority and r["status"]=="ok"]
    cands.sort(key=lambda r: (priority.get(r["role"],9), -int(r["chars"] or 0)))
    qpatterns = [
        rf"第\s*{qno}\s*题",
        rf"^\s*{qno}\s*[\.\．、]",
        rf"[（(]\s*{qno}\s*[）)]",
    ]
    qpatterns_re = [re.compile(p, re.M) for p in qpatterns]
    for r in cands:
        path = EXTRACTED / r["extract_filename"]
        if not path.exists(): continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        # locate the first match
        best = None
        for pat in qpatterns_re:
            m = pat.search(text)
            if m and (best is None or m.start() < best.start()):
                best = m
        if best:
            start = best.start()
            # bound to the next question header
            next_pat = re.compile(rf"第\s*{qno+1}\s*题|^\s*{qno+1}\s*[\.\．、]", re.M)
            nm = next_pat.search(text, pos=start+10)
            end = nm.start() if nm else min(start+2500, len(text))
            excerpt = text[start:end].strip()
            level = "formal" if r["role"]=="rubric" else "lecture_explicit_scoring" if r["role"]=="rubric_like" else "reference_only"
            return {"file": r["abs_path"], "page": "", "excerpt": excerpt[:3000], "level": level, "note": ""}
    return {"file":"", "page":"", "excerpt":"", "level":"missing", "note":"no rubric chunk matched"}

def reason_legal(chunk_text: str) -> tuple[str,str,str]:
    """Return (why_yes, why_maybe_not, boundary_risk)."""
    hits = [t for t in LEGAL_TERMS if t in chunk_text]
    negs = [t for t in NEG_TERMS if t in chunk_text]
    yes = "材料/设问触及：" + "、".join(sorted(set(hits))[:8]) if hits else ""
    maybe = ""
    if negs:
        maybe = "同时出现必修三/政治制度信号：" + "、".join(sorted(set(negs))[:5])
    boundary = ""
    if negs and len(hits) <= 2:
        boundary = "信号弱：法律词只擦边出现，可能是政治与法治题；需读完整设问再判。"
    elif negs and len(hits) >= 3:
        boundary = "混合模块风险：可能是政治与法治+法律与生活混合，要分小问拆。"
    elif not hits:
        boundary = "无明显法律信号，疑似误命中。"
    return yes, maybe, boundary

def main():
    rows = load_manifest()
    by_suite = {}
    for r in rows:
        by_suite.setdefault(r["suite"], []).append(r)

    # Load candidate list from hit dump - simpler: re-derive from manifest+keyword
    # We will iterate over every paper, find chunks with strong legal signal, build rows.
    output_rows = []
    boundary_notes = []
    for suite, recs in sorted(by_suite.items()):
        # Prefer pure 'paper' over 'paper_with_answer'; if no pure paper, fall back
        pure_papers = [r for r in recs if r["role"]=="paper" and r["status"]=="ok"]
        combined = [r for r in recs if r["role"]=="paper_with_answer" and r["status"]=="ok"]
        paper_recs = pure_papers if pure_papers else combined
        paper_recs.sort(key=lambda r: int(r["chars"] or 0), reverse=True)
        for prec in paper_recs:
            ppath = EXTRACTED / prec["extract_filename"]
            if not ppath.exists(): continue
            text = ppath.read_text(encoding="utf-8", errors="ignore")
            chunks = split_questions(text)
            if not chunks:
                continue
            for qno, info in sorted(chunks.items()):
                ctext = info["text"]
                # Decision: at least one strong legal term, or 3+ legal terms.
                hits = [t for t in LEGAL_TERMS if t in ctext]
                strong_present = any(t in ctext for t in [
                    "民法典","合同","违约","侵权责任","消费者权益","退一赔三",
                    "格式条款","劳动合同","竞业限制","人格权","隐私权",
                    "个人信息保护","知识产权","著作权","专利权","商标权","商业秘密",
                    "继承","遗嘱","好意同乘","民事行为能力","新业态"
                ])
                if not (strong_present or len(hits) >= 3):
                    continue
                # length sanity
                if len(ctext) < 250:
                    continue
                qid = f"{suite}__Q{qno}"
                rubric = find_rubric_for(suite, qno, recs, by_suite)
                prompt = extract_prompt(ctext)
                material = extract_material(ctext)
                why_yes, why_maybe_not, boundary = reason_legal(ctext)
                source_kind = prec["role"]
                contamination_flag = ""
                if source_kind == "paper_with_answer" or is_paper_with_answer_text(ctext):
                    contamination_flag = "needs_manual_source_lock: 试题/答案合一或讲评/教师版文件，已用 ANS_RE 截断材料；STEP 3 需复核 prompt/material 是否真为题面"
                # Check if material excerpt itself still contains scoring tokens (contamination)
                if SCORE_TOKEN_RE.search(material):
                    contamination_flag = (contamination_flag + "; " if contamination_flag else "") + "material_has_score_tokens: 截断后材料中仍出现 (N分) 评分标记，说明源文件未清晰区分题面与答案"
                # Check prompt for cross-module cues that disqualify as 选必二
                mod_m = PROMPT_MOD_RE.search(prompt)
                if mod_m:
                    mod_name = mod_m.group(1)
                    if "法律" not in mod_name and "权利" not in mod_name:
                        why_maybe_not = (why_maybe_not + "； " if why_maybe_not else "") + f"设问指定模块为《{mod_name}》，不是《法律与生活》"
                # Filename hints
                fname = (prec.get("paper_extract","") or "").lower()
                if "教师版" in fname or "讲评" in fname or "答案" in fname:
                    contamination_flag = (contamination_flag + "; " if contamination_flag else "") + f"filename_says_teacher_version_or_lecture: {fname}"
                row = {
                    "question_id": qid,
                    "year_region_stage_qno": f"{prec['year']}_{suite}_Q{qno}",
                    "paper_file": prec["abs_path"],
                    "paper_page": info["page"],
                    "paper_source_kind": source_kind,
                    "contamination_flag": contamination_flag,
                    "real_prompt_excerpt": prompt.replace("\n"," / "),
                    "real_material_excerpt": material.replace("\n"," / "),
                    "rubric_file": rubric["file"],
                    "rubric_excerpt": rubric["excerpt"].replace("\n"," / "),
                    "evidence_level": rubric["level"],
                    "why_xuanbier_subjective_law": why_yes,
                    "why_maybe_not": why_maybe_not,
                    "boundary_risk": boundary,
                    "rubric_note": rubric["note"],
                    "source_id": prec["source_id"],
                    "paper_extract": prec["extract_filename"],
                }
                output_rows.append(row)
                if boundary:
                    boundary_notes.append(f"- {qid} → {boundary}  hits={len(hits)} neg-mix={why_maybe_not}")
            break  # one paper per suite

    # Dedup by question_id (in case multiple paper files in one suite produced same qid)
    seen = set()
    dedup = []
    for r in output_rows:
        if r["question_id"] in seen: continue
        seen.add(r["question_id"]); dedup.append(r)

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        fields = ["question_id","year_region_stage_qno","paper_file","paper_page",
                  "paper_source_kind","contamination_flag",
                  "real_prompt_excerpt","real_material_excerpt","rubric_file","rubric_excerpt",
                  "evidence_level","why_xuanbier_subjective_law","why_maybe_not","boundary_risk",
                  "rubric_note","source_id","paper_extract"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in dedup:
            w.writerow(r)

    md = ["# 02 Uncertain / boundary cases (auto-derived; final triage in STEP 3-4)", ""]
    md += boundary_notes
    md += ["", "## Format note",
           "- 关键词扫描原始 hit dump 留在 `02_paper_hit_dump.md`，只作定位用。",
           "- 本表 `02_candidate_subjective_law_questions.csv` 是逐题候选表：每行一道题，含真实设问/材料摘录、对应细则摘录。",
           "- evidence_level 取值：formal（来自细则正本）、lecture_explicit_scoring（讲评/评标/阅卷总结）、reference_only（仅参考答案，未见细则）、missing（未匹配到细则块）。",
           "- 表内每个 excerpt 都已用 ` / ` 替换换行以便 CSV 单行可读；进入 STEP 3 source lock 时再恢复原文换行。"]
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"rows={len(dedup)} boundary={len(boundary_notes)}")

if __name__ == "__main__":
    main()
