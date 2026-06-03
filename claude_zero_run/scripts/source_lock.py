#!/usr/bin/env python3
"""Step 3: source-lock each candidate. For each, find the actual 选必二法律 sub-question (by 运用《法律与生活》 cue or strong-legal cue), pair with sub-rubric, write one .md card, and build the index."""
import csv, re, json
from pathlib import Path

EXTRACTED = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted")
MANIFEST = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/01_source_manifest.csv")
CANDIDATES = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_candidate_subjective_law_questions.csv")
CARDS_DIR = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/source_lock_cards")
INDEX_CSV = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/03_source_lock_index.csv")

CARDS_DIR.mkdir(exist_ok=True)

LAW_CUE_STRONG = re.compile(
    r"运用[《<]\s*(?:法律与生活|法律生活)\s*[》>]?[相关]?知识"
    r"|运用.{0,4}法律.{0,4}知识"
    r"|运用.{0,4}法治.{0,4}知识"
    r"|运用.{0,4}法治.{0,4}相关"
    r"|运用.{0,4}法律.{0,4}相关"
    r"|从法律.{0,4}角度"
    r"|阐释.{0,8}裁判"
    r"|分析判决.{0,5}理由"
    r"|说明.{0,5}裁判.{0,3}理由"
    r"|说明.{0,5}判决.{0,3}理由"
    r"|说明.{0,5}法律.{0,3}依据"
    r"|根据.{0,5}民法典"
    r"|结合.{0,5}民法典"
    r"|结合.{0,5}劳动合同法"
    r"|结合.{0,5}消费者权益保护法"
    r"|结合.{0,5}个人信息保护法"
    r"|是否.{0,3}承担.{0,3}法律责任"
)
LAW_CUE_WEAK = re.compile(  # need extra material-law evidence
    r"完成.{0,3}裁判.{0,3}理由"
    r"|完成.{0,3}下表"
    r"|完成.{0,3}下列.{0,3}表格"
    r"|以案说法"
    r"|法治价值"
    r"|法律价值"
    r"|分析.{0,5}案例"
    r"|阐释.{0,8}价值"
    r"|你认为.{0,8}是否合法"
    r"|从法治.{0,4}角度"
)
LAW_CUE = LAW_CUE_STRONG  # legacy alias
SUBQ_HEADER = re.compile(r"(?:[（(]\s*([1-9])\s*[）)])")
NEXT_MAIN_Q = re.compile(r"^\s*(\d{1,2})[\.\．、]", re.M)

# Concept categories used for framework cross-link later
CATEGORIES = [
    ("合同", ["合同","违约","履约","履行","格式条款","撤销合同","解除合同","买卖","服务合同","订立"]),
    ("消费者", ["消费者","经营者","知情权","欺诈","三倍赔偿","退一赔三","退一赔十","虚假宣传","假冒","公平交易"]),
    ("劳动/平台用工", ["劳动合同","劳动者","用人单位","试用期","竞业限制","经济补偿","工伤","新业态","外卖骑手","平台","网约工","骑手"]),
    ("人格权/隐私/个人信息", ["人格权","隐私权","名誉权","姓名权","肖像权","个人信息","知情同意"]),
    ("知识产权/不正当竞争", ["知识产权","著作权","版权","专利","商标","商业秘密","不正当竞争","署名"]),
    ("侵权/多主体/好意同乘", ["侵权","侵权责任","损害赔偿","公平责任","过错责任","无过错","好意同乘","共同侵权","机动车"]),
    ("物权/相邻关系/绿色原则", ["物权","所有权","用益物权","担保物权","相邻","邻里","通行","采光","通风","绿色原则","绿色"]),
    ("婚姻/继承/监护", ["婚姻","继承","遗嘱","法定继承","遗赠","赡养","监护","未成年人保护","收养"]),
    ("纠纷解决", ["调解","仲裁","诉讼","举证","证据","和解","判决"]),
    ("法律意义/规则", ["民法典","《法律与生活》","法律与生活","权利保护","规则","公平正义","社会主义核心价值观","诚信"]),
]

def category_of(text: str):
    out = []
    for name, kws in CATEGORIES:
        for k in kws:
            if k in text:
                out.append(name); break
    return out or ["未分类"]

def load_manifest():
    with MANIFEST.open() as f:
        return list(csv.DictReader(f))

def load_candidates():
    with CANDIDATES.open() as f:
        return list(csv.DictReader(f))

def _is_q_header_line(lines, i):
    """Return q or None. Strict detector that rejects '16.7%' table data
    but accepts '19. 2024 年6 月...' style headers (with space + year + Chinese)."""
    ln = lines[i]
    # Reject pure decimal like "16.7%" or "16.7" or "8.6%"
    if re.match(r"^\s*\d{1,2}[\.\．、]\d", ln):
        return None
    m = re.match(r"^\s*(\d{1,2})[\.\．、]\s*(.*)$", ln)
    if not m: return None
    q = int(m.group(1))
    if not (16 <= q <= 25): return None
    rest = m.group(2).strip()
    if rest:
        # If rest is purely digits + % or short data value (no Chinese in 30 chars), reject
        if re.match(r"^\d+\s*%", rest): return None
        # Acceptable: contains Chinese, opens a paren, or contains 分
        if re.search(r"[一-龥]|[（(]|分", rest):
            return q
        return None
    # rest empty — check next non-blank lines
    for j in range(i+1, min(i+6, len(lines))):
        s = lines[j].strip()
        if not s: continue
        if re.match(r"^\d+\s*%", s) or re.match(r"^\d+[\.\．]\d", s):
            return None
        if re.search(r"[一-龥]", s) and ("分" in s or len(s) > 8 or "（" in s or "(" in s):
            return q
        return None
    return None

def split_main_questions(text):
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
        page = "?"
        for j in range(max(0,i-30), i):
            mm = re.search(r"PAGE\s+(\d+)", lines[j])
            if mm:
                page = mm.group(1)
        chunks[q] = {"start": i, "end": end, "page": page, "text": "\n".join(lines[i:end])}
    return chunks

PROMPT_LINE_RE = re.compile(r"(结合材料|阅读材料|根据材料|依据材料|请运用|请结合|阐释|分析判决|从.{1,8}角度|谈谈|说明|评析|判断)")

def split_subquestions(qtext):
    """Return list of (subq_label, subq_text). Sub-Q headers like (1)/（2）/(3).
    If no sub-Q markers, return [("M", material_block), ("0", prompt_block)]."""
    starts = [(m.start(), m.group(1)) for m in re.finditer(r"[（(]\s*([1-9])\s*[）)]", qtext)]
    if not starts:
        # No sub-Q markers — find the last prompt line that begins with 结合/运用/阐释 etc.
        lines = qtext.split("\n")
        prompt_start = None
        for i in range(len(lines)-1, -1, -1):
            if PROMPT_LINE_RE.search(lines[i]):
                # walk up to capture multi-line prompt
                while i > 0 and lines[i-1].strip() and not lines[i-1].strip().endswith(("。","？","！")):
                    i -= 1
                prompt_start = i
                break
        if prompt_start is None or prompt_start == 0:
            return [("M", ""), ("0", qtext)]
        material = "\n".join(lines[:prompt_start]).strip()
        prompt = "\n".join(lines[prompt_start:]).strip()
        return [("M", material), ("0", prompt)]
    result = []
    for k, (pos, lbl) in enumerate(starts):
        endpos = starts[k+1][0] if k+1 < len(starts) else len(qtext)
        result.append((lbl, qtext[pos:endpos]))
    material = qtext[:starts[0][0]].strip()
    return [("M", material)] + result

NON_LAW_PROMPT_RE = re.compile(
    r"运用[《<]\s*(?:政治与法治|经济与社会|哲学与文化|当代国际政治与经济|逻辑与思维|思想政治|中国特色社会主义)\s*[》>]?知识"
    r"|《\s*(?:政治与法治|经济与社会|哲学与文化|当代国际政治与经济|逻辑与思维)\s*》[知识]?"
    r"|政府工作报告.*全过程人民民主"
    r"|全过程人民民主.*政府工作报告"
    r"|运用[^。]{0,15}思维方法"
    r"|运用[^。]{0,8}(?:归纳思维|演绎思维|联想思维|发散思维|逆向思维|超前思维|创新思维|形式逻辑|辩证思维|科学思维)"
    r"|运用[^。]{0,8}思维(?:工具|路径|方式)"
    r"|从.{0,8}哲学.{0,8}角度"
    r"|运用.{0,8}哲学.{0,8}知识"
    r"|运用.{0,8}唯物.{0,8}"
    r"|运用.{0,8}辩证.{0,8}知识"
    r"|说明.{0,5}全过程人民民主"
    r"|体现.{0,5}全过程人民民主"
    r"|运用.{0,8}中国共产党.{0,8}知识"
    r"|运用.{0,8}社会主义.{0,8}的知识"
    r"|说明.{0,8}是如何体现"
)

def prompt_is_non_law(prompt_text: str) -> bool:
    """Return True if the prompt explicitly declares a non-选必二 module."""
    return bool(NON_LAW_PROMPT_RE.search(prompt_text))

def find_law_subq(subqs, material_block: str = ""):
    """Return list of sub-Q labels where 选必二《法律与生活》 cues are found in prompt,
    OR a softer "material-rich + law task verb" fallback applies."""
    hits = []
    # Pre-score the material's law density
    material_cats = [t for cn, kws in CATEGORIES for t in [cn] if any(k in material_block for k in kws)]
    material_law_density = 0
    for cn, kws in CATEGORIES:
        for k in kws:
            if k in material_block:
                material_law_density += 1
                break  # one per category
    for lbl, txt in subqs:
        if lbl == "M":
            continue
        prompt = txt[:600]
        # Hard reject: explicit non-法律 module declaration
        if prompt_is_non_law(prompt):
            continue
        # Tier 1: STRONG cue — auto-accept
        if LAW_CUE_STRONG.search(prompt):
            hits.append((lbl, "explicit_cue"))
            continue
        if re.search(r"运用[《<].*[》>]?知识", prompt):
            mod = re.search(r"运用[《<](.*?)[》>]?知识", prompt)
            if mod and "法律" in mod.group(1):
                hits.append((lbl, "explicit_cue"))
                continue
        # Tier 2: WEAK cue — require material has >= 2 law categories
        if LAW_CUE_WEAK.search(prompt):
            if material_law_density >= 2:
                hits.append((lbl, f"weak_cue+material_law_density={material_law_density}"))
                continue
            else:
                continue  # weak cue without material support — skip
        # Tier 3: Material-rich + legal task verb fallback
        legal_task_verb = re.search(
            r"评析|分析判决|分析.{0,5}裁判|说明.{0,5}理由|说明.{0,5}依据|"
            r"是否合法|是否.{0,3}承担|是否.{0,3}成立|判断.{0,3}是否",
            prompt)
        prompt_cat = category_of(prompt)
        if material_law_density >= 3 and legal_task_verb:
            hits.append((lbl, f"inferred_material_rich+task_verb:{','.join(material_cats[:3])}"))
            continue
        if prompt_cat != ["未分类"] and legal_task_verb:
            hits.append((lbl, f"inferred_prompt_cat+task_verb:{','.join(prompt_cat)}"))
            continue
    return hits

def find_subrubric(rubric_text, qno, subq_lbl):
    """Look up the sub-rubric chunk for question qno sub-Q (subq_lbl)."""
    # Patterns: "19（1）" "19(1)" "第19题（1）" "19．（1）"
    pats = [
        rf"{qno}\s*[（(]\s*{subq_lbl}\s*[）)]",
        rf"第\s*{qno}\s*题\s*[（(]\s*{subq_lbl}\s*[）)]",
        rf"^\s*{qno}\.\s*\(?\s*{subq_lbl}\s*\)?",
        rf"^{qno}\s*[（(]\s*{subq_lbl}\s*[）)]",
    ]
    best = None
    for p in pats:
        m = re.search(p, rubric_text, re.M)
        if m and (best is None or m.start() < best.start()):
            best = m
    if not best:
        return None, "no subrubric block"
    start = best.start()
    # End at next subQ for same qno or next main question
    nextpat = re.compile(
        rf"{qno}\s*[（(]\s*{int(subq_lbl)+1}\s*[）)]"
        rf"|^{qno+1}[\.\．、]"
        rf"|第\s*{qno+1}\s*题",
        re.M)
    nm = nextpat.search(rubric_text, pos=start+5)
    end = nm.start() if nm else min(start+2500, len(rubric_text))
    return rubric_text[start:end].strip(), ""

def find_rubric_files(suite, recs):
    priority = {"rubric":0, "rubric_like":1, "supplement":2}
    return sorted([r for r in recs if r["role"] in priority and r["status"]=="ok"],
                  key=lambda r: (priority.get(r["role"],9), -int(r["chars"] or 0)))

def main():
    manifest = load_manifest()
    by_suite_recs = {}
    for r in manifest:
        by_suite_recs.setdefault(r["suite"], []).append(r)

    cands = load_candidates()
    index_rows = []
    written = 0
    cards_count_per_question = {}  # per-Q how many sub-cards we wrote
    for c in cands:
        qid = c["question_id"]
        suite = "_".join(qid.split("__")[0:1])  # qid like "2024朝阳一模__Q17"
        suite = qid.split("__")[0]
        qno_match = re.search(r"Q(\d+)", qid)
        if not qno_match:
            index_rows.append({**c, "decision":"excluded","reason":"no qno"})
            continue
        qno = int(qno_match.group(1))
        # Locate paper extract
        paper_text = ""
        page = c.get("paper_page","?")
        ext_path = EXTRACTED / c["paper_extract"]
        if ext_path.exists():
            paper_text = ext_path.read_text(encoding="utf-8", errors="ignore")
        chunks = split_main_questions(paper_text)
        if qno not in chunks:
            index_rows.append({"question_id":qid,"suite":suite,"qno":qno,
                "decision":"excluded","reason":"paper chunk not found",
                "paper_file":c["paper_file"],"rubric_file":"","evidence_level":"missing",
                "category":"", "subq":"", "card_file":""})
            continue
        qtext = chunks[qno]["text"]
        subqs = split_subquestions(qtext)
        mat_for_density = ""
        for lbl, txt in subqs:
            if lbl == "M":
                mat_for_density = txt
                break
        law_subqs = find_law_subq(subqs, mat_for_density)
        # Whole-question fallback: if no sub-Q triggered, check qtext-level cues
        if not law_subqs:
            # Check whether the ONLY identifiable prompt(s) declare non-law module — if all sub-Q prompts are non-law, do not resurrect with whole-Q fallback
            all_subq_prompts = [txt[:600] for lbl, txt in subqs if lbl != "M"]
            if all_subq_prompts and all(prompt_is_non_law(p) for p in all_subq_prompts):
                pass  # do not resurrect; this question is non-法律 module
            else:
                qtext_cues = ("民法原则" in qtext or "以案说法" in qtext or
                              "格式条款" in qtext or "完成下表" in qtext or
                              "法治价值" in qtext or "完成下列表格" in qtext or
                              "典型意义" in qtext or "案件事实" in qtext or
                              "法律依据" in qtext or "民事行为能力" in qtext or
                              "判决结果" in qtext)
                qtext_law_density = 0
                for cn, kws in CATEGORIES:
                    if any(k in qtext for k in kws):
                        qtext_law_density += 1
                if LAW_CUE.search(qtext) or (qtext_cues and qtext_law_density >= 3):
                    synthetic_lbl = "0"
                    best_prompt_density = -1
                    for lbl, txt in subqs:
                        if lbl == "M": continue
                        # don't resurrect non-law sub-prompts
                        if prompt_is_non_law(txt[:600]): continue
                        d = sum(1 for cn,kws in CATEGORIES if any(k in txt for k in kws))
                        if d > best_prompt_density:
                            best_prompt_density = d
                            synthetic_lbl = lbl
                    # Only resurrect if there's at least one non-NON_LAW sub-Q to pick
                    if best_prompt_density >= 0:
                        law_subqs = [(synthetic_lbl, f"whole_q_fallback:density={qtext_law_density},cues={qtext_cues}")]
        if not law_subqs:
            index_rows.append({"question_id":qid,"suite":suite,"qno":qno,
                "decision":"excluded","reason":"no law sub-Q found (not 选必二)",
                "paper_file":c["paper_file"],"rubric_file":"","evidence_level":"missing",
                "category":"", "subq":"", "card_file":""})
            continue
        # Find rubric files for this suite
        suite_recs = by_suite_recs.get(suite, [])
        rubric_files = find_rubric_files(suite, suite_recs)
        material_block = ""
        for lbl, txt in subqs:
            if lbl == "M":
                material_block = txt
                break

        for sub_lbl, kind in law_subqs:
            # find prompt text for this sub-Q
            subq_text = ""
            for lbl, txt in subqs:
                if lbl == sub_lbl:
                    subq_text = txt
                    break
            cat = category_of(subq_text + " " + material_block)
            # Find sub-rubric across rubric files
            best_rubric = None
            best_rubric_file = ""
            best_level = "missing"
            best_note = ""
            for rf in rubric_files:
                rpath = EXTRACTED / rf["extract_filename"]
                if not rpath.exists(): continue
                rtext = rpath.read_text(encoding="utf-8", errors="ignore")
                sub_rub, note = find_subrubric(rtext, qno, sub_lbl)
                if sub_rub:
                    best_rubric = sub_rub
                    best_rubric_file = rf["abs_path"]
                    best_level = "formal" if rf["role"]=="rubric" else "lecture_explicit_scoring" if rf["role"]=="rubric_like" else "reference_only"
                    best_note = ""
                    break
                else:
                    best_note = note
            if best_rubric is None:
                # try fallback: any rubric block mentioning the main question
                for rf in rubric_files:
                    rpath = EXTRACTED / rf["extract_filename"]
                    if not rpath.exists(): continue
                    rtext = rpath.read_text(encoding="utf-8", errors="ignore")
                    m = re.search(rf"第\s*{qno}\s*题|^\s*{qno}[\.\．、]", rtext, re.M)
                    if m:
                        start = m.start()
                        # Bound at next main Q number to prevent bleed
                        nm = re.search(rf"第\s*{qno+1}\s*题|^\s*{qno+1}[\.\．、]", rtext[start+5:], re.M)
                        end = (start + 5 + nm.start()) if nm else min(start+2500, len(rtext))
                        best_rubric = rtext[start:end].strip()
                        best_rubric_file = rf["abs_path"]
                        best_level = "formal" if rf["role"]=="rubric" else "lecture_explicit_scoring" if rf["role"]=="rubric_like" else "reference_only"
                        best_note = "matched whole-Q rubric (no sub-Q split)"
                        break
            # Decide
            if best_rubric is None:
                decision = "deferred"
                reason = "no rubric found"
                evlvl = "missing"
            else:
                if best_level == "formal":
                    decision = "core_candidate"
                    reason = "explicit law cue + formal rubric"
                elif best_level == "lecture_explicit_scoring":
                    decision = "core_candidate"
                    reason = "explicit law cue + lecture-explicit scoring"
                else:
                    decision = "reference_candidate"
                    reason = "reference-only answer; no formal rubric"
                evlvl = best_level

            # Card file id
            card_id = f"{qid}__sub{sub_lbl}".replace("/","_")
            card_path = CARDS_DIR / f"{card_id}.md"
            # Trim subq_text prompt at STRONG answer-content boundaries only.
            # NOTE: do NOT cut at "参考示例" or ①②③ — those often appear inside
            # 完成下表/参考示例 prompts as part of the legitimate task statement,
            # not as an answer marker.
            ANS_INLINE_CUT = re.compile(r"参考答案|评分细则|评分参考|【答案】|【详解】|【分析】|教师版", re.M)
            am = ANS_INLINE_CUT.search(subq_text)
            subq_text_clean = subq_text[:am.start()].strip() if am else subq_text.strip()
            # Hard guard: if the prompt is degenerate (too short to be a real 设问),
            # do not write a core card — demote to deferred with reason.
            stripped = re.sub(r"\s+", "", subq_text_clean)
            if len(stripped) < 12 or all(c in "阅读材料案件，。、 " for c in stripped):
                # Demote
                decision = "deferred"
                reason = "prompt_too_short_after_cleanup: 真实设问块过短，疑似截断；需要回原卷人工补全"
                evlvl = best_level if best_rubric else "missing"
            md_lines = [
                f"# Source Lock Card: {qid} 第{qno}题（{sub_lbl}）",
                "",
                f"- question_id: {qid}",
                f"- 年份区阶段题号: {c['year_region_stage_qno']} 第{qno}题（{sub_lbl}）",
                f"- 原始文件: {c['paper_file']}",
                f"- 页码/题号: page≈{page}，第{qno}题（{sub_lbl}）",
                f"- 设问识别方式: {kind}",
                f"- 法律类别（初判）: {', '.join(cat)}",
                f"- 证据等级: {evlvl}",
                f"- 决定: {decision}",
                f"- 原因: {reason}",
                "",
                "## 真实设问（来自原卷抽取，未润色）",
                "```",
                subq_text_clean[:1500],
                "```",
                "",
                "## 真实材料核心（题干材料，未润色）",
                "```",
                material_block.strip()[:3200],
                "```",
                "",
                "## 对应答案/细则/评标/讲评（原文摘录）",
                f"- 来源文件: {best_rubric_file}",
                f"- 备注: {best_note}",
                "```",
                (best_rubric or "[未匹配到细则块]")[:3500],
                "```",
                "",
                "## 是否进入核心题链",
                f"- 初判: {decision}",
                f"- 若不进入，原因: {reason if decision!='core_candidate' else ''}",
                "",
                "## 备注 / 待核验",
                "- 抽取来自 PDF/Word/PPTX 文本层；如出现乱码或异常分页，需在 STEP 4 复核。",
                "- 设问识别 inferred 类别需要人工二次确认，避免把'评析行为/分析判决'类政治与法治题混入。",
            ]
            card_path.write_text("\n".join(md_lines), encoding="utf-8")
            written += 1

            index_rows.append({
                "question_id": qid,
                "suite": suite,
                "qno": qno,
                "subq": sub_lbl,
                "decision": decision,
                "reason": reason,
                "paper_file": c["paper_file"],
                "rubric_file": best_rubric_file,
                "evidence_level": evlvl,
                "category": ", ".join(cat),
                "card_file": str(card_path.relative_to(card_path.parent.parent)),
            })

    fields = ["question_id","suite","qno","subq","decision","reason","category","evidence_level","paper_file","rubric_file","card_file"]
    with INDEX_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in index_rows:
            w.writerow(r)
    print(f"cards_written={written} index_rows={len(index_rows)}")

if __name__ == "__main__":
    main()
