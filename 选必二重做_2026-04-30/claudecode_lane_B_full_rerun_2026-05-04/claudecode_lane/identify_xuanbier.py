#!/usr/bin/env python3
"""
Round 4+5 联合脚本：
- 扫每套卷的试卷文本，切题号，识别选必二题
- 为每道选必二题在同套 L1 文件中找对应的细则段
- 输出 SUBJECTIVE_QUESTION_PACK.json / CHOICE_QUESTION_PACK.json + CSV
"""
import csv, json, re, os
from pathlib import Path
from collections import defaultdict

PROJECT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04")
LEDGER = PROJECT / "00_control" / "SOURCE_LEDGER_v2.csv"
OUT_DIR = PROJECT / "00_control"

# 选必二识别关键词
LF_EXPLICIT = re.compile(r"《\s*法律与生活\s*》|法律与生活")

# A 级法律强信号（命中至少 1 个就有资格进入选必二筛选）
LF_STRONG_KW = [
    # 民法/合同 — 强信号
    r"民法典", r"格式条款", r"可撤销", r"惩罚性赔偿", r"三倍赔偿", r"十倍赔偿", r"质权", r"抵押权", r"担保物权",
    r"用益物权", r"宅基地", r"相邻关系", r"夫妻共同债务", r"遗赠扶养", r"遗嘱继承", r"法定继承",
    # 人格权 — 强信号
    r"肖像权", r"声音权", r"姓名权", r"名誉权", r"隐私权", r"人格权", r"个人信息保护",
    # 侵权 — 强信号
    r"侵权责任", r"过错责任", r"无过错责任", r"过错推定", r"特殊侵权", r"产品责任", r"高空抛物", r"安全保障义务",
    # 知产竞争 — 强信号
    r"知识产权", r"著作权", r"商标权", r"专利权", r"商业秘密", r"不正当竞争", r"商业诋毁",
    # 劳动 — 强信号
    r"劳动合同", r"劳动关系", r"竞业限制", r"经济补偿", r"工伤", r"劳动仲裁",
    # 程序 — 强信号
    r"民事诉讼", r"司法确认", r"举证责任", r"公益诉讼", r"人民调解", r"诉讼调解", r"行政公益诉讼", r"民事公益诉讼",
    # 新业态法律 — 强信号
    r"AIGC", r"生成式人工智能", r"虚拟数字人",
]
LF_STRONG_PAT = re.compile("|".join(LF_STRONG_KW))

# B 级法律辅助信号（命中 ≥ 2 个 + A 级 ≥ 1 才算）
LF_AUX_KW = [
    r"合同", r"要约", r"承诺", r"违约", r"欺诈", r"消费者", r"经营者", r"知情权", r"公平交易权",
    r"虚假宣传", r"自主选择权", r"物权", r"继承", r"遗嘱", r"婚姻", r"侵权", r"商标", r"专利",
    r"调解", r"仲裁", r"诉讼", r"法院", r"民事", r"赔偿", r"判决",
]
LF_AUX_PAT = re.compile("|".join(LF_AUX_KW))

# 模块明示（命中即排除）
NON_LF_MODULE_PAT = re.compile(r"《\s*经济与社会\s*》|《\s*哲学与文化\s*》|《\s*中国特色社会主义\s*》|《\s*政治与法治\s*》|《\s*当代国际政治与经济\s*》|《\s*逻辑与思维\s*》")

# 非选必二专属强信号（命中 ≥ 2 个则强烈排除，即使有法律词也不算）
NON_LF_HEAVY_KW = [
    # 必修四哲学
    r"主要矛盾", r"主次矛盾", r"矛盾的主要方面", r"对立统一", r"质变量变", r"否定之否定", r"辩证否定",
    r"实践是认识的基础", r"认识的反复性", r"真理", r"客观规律", r"意识能动作用", r"上层建筑", r"经济基础",
    # 必修四文化
    r"中华文化", r"文化自信", r"精神标识", r"中华民族精神", r"社会主义核心价值观", r"文化软实力",
    # 必修三政治法治
    r"全过程人民民主", r"人民当家作主", r"依法治国", r"全面依法治国", r"科学立法", r"严格执法", r"良法之治",
    r"公民参与管理国家", r"基层群众自治", r"人民代表大会", r"政治协商",
    # 必修二经济
    r"高质量发展", r"新发展理念", r"市场机制", r"反垄断执法", r"营商环境", r"民营经济", r"新质生产力",
    r"货币政策", r"宏观调控", r"财政政策", r"再分配", r"GDP",
    # 选必一国政经
    r"经济全球化", r"逆全球化", r"全球治理", r"南南合作", r"金砖", r"一带一路", r"国际秩序",
    # 选必三逻辑思维
    r"概念外延", r"概念内涵", r"换质位", r"矛盾律", r"排中律", r"同一律", r"科学思维",
    r"分析与综合", r"思维抽象", r"思维具体", r"演绎推理", r"归纳推理", r"类比推理",
    r"超前思维", r"逆向思维", r"发散思维", r"聚合思维",
]
NON_LF_HEAVY_PAT = re.compile("|".join(NON_LF_HEAVY_KW))

# 题号切分（防 18.4 千克陷阱：题号必须在行首或前面是空白/换行/页号，且后面跟"."、"、"、"．"、"题"、"（"或空格）
QNUM_PAT = re.compile(r"(?:^|\n)\s{0,4}(\d{1,2})[．.、](?!\d)\s*(?=\S)", re.MULTILINE)

# 选择题题号通常是 1-15，主观题题号 16-21（北京高考政治格式）
CHOICE_NUM_RANGE = range(1, 16)
SUBJECTIVE_NUM_RANGE = range(16, 22)

# 子小问标识（1）（2）等
SUBQ_PAT = re.compile(r"[（\(]\s*([1-5])\s*[）\)]")

def load_ledger():
    with open(LEDGER, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def find_paper_text(suite_files):
    """从套卷文件里挑'试卷'类文本，按字符量优先（防扫描件 OCR 残缺）"""
    candidates = []
    for r in suite_files:
        if not r.get("out_txt"):
            continue
        out = Path(r["out_txt"])
        if not out.exists():
            continue
        if "试卷" in r["filename"] or "原卷" in r["filename"] or "试题" in r["filename"]:
            candidates.append((int(r["char_count"] or 0), out, r))
    if not candidates:
        # fallback: any L1 / SOURCE_PAPER with high char count
        for r in suite_files:
            if not r.get("out_txt"):
                continue
            out = Path(r["out_txt"])
            if out.exists() and int(r["char_count"] or 0) > 3000:
                candidates.append((int(r["char_count"] or 0), out, r))
    candidates.sort(reverse=True)
    return candidates[0][1] if candidates else None

def split_questions(text):
    """按题号切分。返回 dict[qnum] = qtext"""
    matches = list(QNUM_PAT.finditer(text))
    questions = {}
    for i, m in enumerate(matches):
        qnum = int(m.group(1))
        if qnum > 25 or qnum < 1:  # 异常题号
            continue
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        qtext = text[start:end].strip()
        # 取最后一次出现的题号块（防止每页页眉重复"1."）
        if len(qtext) > 80:  # 至少要有真内容
            questions[qnum] = qtext
    return questions

def is_xuanbier(qtext):
    """识别一道题是否为选必二（严格版）"""
    # 模块明示排除
    if NON_LF_MODULE_PAT.search(qtext) and not LF_EXPLICIT.search(qtext):
        return False

    # 法律与生活模块明示
    if LF_EXPLICIT.search(qtext):
        return True

    # 非选必二专属重信号 ≥ 2 → 强烈排除
    non_lf_hits = len(set(NON_LF_HEAVY_PAT.findall(qtext)))
    strong_hits = len(set(LF_STRONG_PAT.findall(qtext)))
    aux_hits = len(set(LF_AUX_PAT.findall(qtext)))

    # 决策表
    if non_lf_hits >= 2 and strong_hits == 0:
        return False  # 哲学/经济/必修三/选必三 等
    if non_lf_hits >= 3:
        return False  # 即使有 1 个法律强词也排（很可能是法律材料考其他模块）
    if strong_hits >= 1 and non_lf_hits == 0:
        return True  # 干净的法律强信号
    if strong_hits >= 1 and aux_hits >= 2:
        return True  # 强信号 + 辅助信号 ≥ 2
    if strong_hits == 0 and aux_hits >= 3 and non_lf_hits == 0:
        return "PROBABLE"  # 没强词但辅助词足够，且无干扰
    return False

def get_setting(qtext):
    """提取设问句（typically 含'结合材料'/'运用'/'说明'/'分析'等）"""
    # find sentences containing setting markers
    lines = qtext.split("\n")
    setting_lines = []
    for line in lines:
        if re.search(r"运用.{0,15}知识|结合.{0,10}材料|说明.{0,8}|分析.{0,8}|阐述|阐释|论证", line):
            if len(line) < 200 and len(line) > 5:
                setting_lines.append(line.strip())
    return " | ".join(setting_lines[:3]) if setting_lines else ""

def find_rubric_for_question(suite_files, qnum):
    """为题号 qnum 在套内 L1 文件里找细则段"""
    rubric_segments = []
    for r in suite_files:
        if r["evidence_level_hypothesis"] != "L1":
            continue
        if not r.get("out_txt"):
            continue
        out = Path(r["out_txt"])
        if not out.exists():
            continue
        # 文件名里含题号 / 内容里含"X题"或"X."开头
        name_hit = re.search(rf"[^\d]{qnum}[^\d]", r["filename"]) is not None
        try:
            content = out.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # 在文件内查 "{qnum}题" 或 "第{qnum}题" 块
        block_pat = re.compile(rf"(?:第\s*{qnum}\s*题|{qnum}\s*题|^{qnum}\s*[．.])", re.MULTILINE)
        block_matches = list(block_pat.finditer(content))
        if name_hit and not block_matches:
            # 整文件相关
            rubric_segments.append({
                "source": r["filename"],
                "match_type": "filename",
                "snippet": content[:3000],
            })
        elif block_matches:
            for m in block_matches:
                start = m.start()
                # 取从匹配开始到下一个题号或文件末尾
                next_block = re.search(r"(?:第\s*\d{1,2}\s*题|^\d{1,2}\s*[．.])", content[start+5:], re.MULTILINE)
                end = start + 5 + next_block.start() if next_block else min(start + 4000, len(content))
                rubric_segments.append({
                    "source": r["filename"],
                    "match_type": "content",
                    "snippet": content[start:end],
                })
                break  # 只取第一处匹配
    return rubric_segments

def main():
    rows = load_ledger()
    by_suite = defaultdict(list)
    for r in rows:
        if r["status"] not in ("ok", "excluded"):
            continue
        if r["evidence_level_hypothesis"] == "SOURCE_INDEX":
            continue
        if r["excluded"] == "Y":
            continue
        key = f"{r['year']}/{r['suite']}"
        by_suite[key].append(r)

    print(f"Suites: {len(by_suite)}")

    subjective_pack = []
    choice_pack = []
    suite_status = []
    no_paper = []

    for suite_key, files in sorted(by_suite.items()):
        year, suite = suite_key.split("/", 1)
        paper_path = find_paper_text(files)
        if not paper_path:
            no_paper.append(suite_key)
            suite_status.append({"suite": suite_key, "status": "NO_PAPER_TEXT", "n_choice": 0, "n_subj": 0})
            continue
        try:
            text = paper_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            no_paper.append(suite_key)
            continue

        questions = split_questions(text)
        n_choice = 0
        n_subj = 0
        for qnum in sorted(questions.keys()):
            qtext = questions[qnum]
            xb = is_xuanbier(qtext)
            if not xb:
                continue
            is_subj = qnum in SUBJECTIVE_NUM_RANGE
            is_choice = qnum in CHOICE_NUM_RANGE
            if not (is_subj or is_choice):
                continue

            entry = {
                "suite": suite_key,
                "year": year,
                "qnum": qnum,
                "type": "subjective" if is_subj else "choice",
                "xb_status": "confirmed" if xb is True else xb,
                "qtext": qtext[:5000],
                "qtext_len": len(qtext),
                "setting": get_setting(qtext) if is_subj else "",
                "paper_file": paper_path.name,
            }

            if is_subj:
                # 找细则段
                rubric_segs = find_rubric_for_question(files, qnum)
                entry["rubric_segments"] = rubric_segs
                entry["has_rubric"] = bool(rubric_segs)
                subjective_pack.append(entry)
                n_subj += 1
            else:
                choice_pack.append(entry)
                n_choice += 1

        suite_status.append({
            "suite": suite_key,
            "status": "has_xuanbier" if (n_subj + n_choice) else "no_xuanbier_detected",
            "n_choice": n_choice,
            "n_subj": n_subj,
        })

    # Write outputs
    with open(OUT_DIR / "SUBJECTIVE_QUESTION_PACK.json", "w", encoding="utf-8") as f:
        json.dump(subjective_pack, f, ensure_ascii=False, indent=2)
    with open(OUT_DIR / "CHOICE_QUESTION_PACK.json", "w", encoding="utf-8") as f:
        json.dump(choice_pack, f, ensure_ascii=False, indent=2)

    # CSVs (lighter)
    with open(OUT_DIR / "SUBJECTIVE_QUESTION_PACK.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["suite", "year", "qnum", "xb_status", "qtext_len", "setting", "has_rubric", "rubric_n", "paper_file"])
        w.writeheader()
        for e in subjective_pack:
            w.writerow({
                "suite": e["suite"], "year": e["year"], "qnum": e["qnum"],
                "xb_status": e["xb_status"], "qtext_len": e["qtext_len"],
                "setting": e["setting"][:200], "has_rubric": e["has_rubric"],
                "rubric_n": len(e.get("rubric_segments", [])),
                "paper_file": e["paper_file"],
            })

    with open(OUT_DIR / "CHOICE_QUESTION_PACK.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["suite", "year", "qnum", "xb_status", "qtext_len", "paper_file"])
        w.writeheader()
        for e in choice_pack:
            w.writerow({
                "suite": e["suite"], "year": e["year"], "qnum": e["qnum"],
                "xb_status": e["xb_status"], "qtext_len": e["qtext_len"],
                "paper_file": e["paper_file"],
            })

    with open(OUT_DIR / "SUITE_STATUS.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["suite", "status", "n_choice", "n_subj"])
        w.writeheader()
        w.writerows(suite_status)

    print(f"\nSubjective questions: {len(subjective_pack)}")
    print(f"  with rubric matched: {sum(1 for e in subjective_pack if e['has_rubric'])}")
    print(f"Choice questions: {len(choice_pack)}")
    print(f"\nNo-paper suites: {len(no_paper)}")
    for k in no_paper:
        print(f"  {k}")
    print(f"\nWrote to {OUT_DIR}/")

if __name__ == "__main__":
    main()
