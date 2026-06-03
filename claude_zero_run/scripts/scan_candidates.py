#!/usr/bin/env python3
"""Step 2: scan extracted text, find subjective law questions, pair with rubric."""
import csv, re
from pathlib import Path

EXTRACTED = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted")
MANIFEST = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/01_source_manifest.csv")
OUT_CSV = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_candidate_subjective_law_questions.csv")
OUT_MD = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_uncertain_or_boundary_cases.md")
HIT_DUMP = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_paper_hit_dump.md")

# 选必二《法律与生活》关键概念 — 必须在材料/设问/细则一带出现才算法律题
LEGAL_TERMS = [
    "民法典", "合同", "违约", "履约", "履行合同", "买卖合同", "服务合同",
    "格式条款", "撤销合同", "解除合同", "无效合同",
    "侵权", "侵权责任", "损害赔偿", "精神损害",
    "消费者权益", "消费者", "经营者", "三倍赔偿", "退一赔三", "退一赔十", "知情权", "欺诈", "假冒", "虚假宣传",
    "劳动合同", "劳动关系", "劳动者", "用人单位", "试用期", "竞业限制", "经济补偿", "工伤", "新业态劳动者",
    "平台用工", "外卖骑手", "网约工", "灵活就业",
    "人格权", "隐私权", "名誉权", "姓名权", "肖像权", "个人信息保护", "个人信息",
    "知识产权", "著作权", "专利权", "商标权", "商业秘密", "不正当竞争",
    "婚姻", "继承", "遗嘱", "法定继承", "遗赠扶养", "监护", "未成年人保护", "赡养",
    "相邻关系", "物权", "所有权", "用益物权", "担保物权", "绿色原则",
    "调解", "仲裁", "诉讼", "举证责任", "举证", "证据规则",
    "好意同乘", "公平责任", "过错责任", "无过错责任",
    "民事行为能力", "限制民事行为能力", "无民事行为能力",
]
# 极强信号：直接命中选必二判断
STRONG_TERMS = [
    "民法典", "合同法", "消费者权益保护法", "个人信息保护法",
    "劳动合同法", "新业态", "外卖骑手", "网约车", "退一赔三",
    "格式条款", "竞业限制", "好意同乘", "侵权责任", "人格权",
    "知识产权", "著作权", "商标权", "专利", "商业秘密",
    "未成年人保护法", "民事行为能力",
]

# 反向词 — 政治与法治/必修三 不是选必二
NEG_TERMS = ["人民代表大会", "全国人大", "国务院", "依法治国", "公正司法",
             "立法机关", "行政复议", "行政诉讼", "宪法宣誓", "民族区域自治",
             "基层群众自治", "村民委员会", "居民委员会"]

# 主观题题号识别
QID_RE = re.compile(r"^\s*(?:第\s*)?(\d{1,2})\s*[\.\．、]")

def load_manifest():
    rows = []
    with MANIFEST.open() as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows

def split_questions(text):
    """Split paper text into chunks by question number 16..21 (Beijing main questions)."""
    # Find positions of lines starting with 16. 17. ... 21.
    lines = text.split("\n")
    indices = []
    for i, line in enumerate(lines):
        m = re.match(r"^\s*(\d{1,2})[\.\．、\s]", line)
        if m:
            q = int(m.group(1))
            if 16 <= q <= 25:
                indices.append((i, q))
    chunks = {}
    for k, (i, q) in enumerate(indices):
        end = indices[k+1][0] if k+1 < len(indices) else len(lines)
        chunks[q] = "\n".join(lines[i:end])
    return chunks

def score_legal(chunk: str) -> dict:
    hits = [t for t in LEGAL_TERMS if t in chunk]
    strong = [t for t in STRONG_TERMS if t in chunk]
    neg = [t for t in NEG_TERMS if t in chunk]
    return {
        "n_hits": len(hits),
        "hits": hits,
        "n_strong": len(strong),
        "strong": strong,
        "n_neg": len(neg),
        "neg": neg,
    }

def main():
    rows = load_manifest()
    candidate_rows = []
    boundary_notes = []
    hit_dump = ["# Paper-by-paper question hits", ""]
    by_suite = {}
    for row in rows:
        if row["role"] != "paper":
            continue
        if row["status"] != "ok":
            continue
        by_suite.setdefault(row["suite"], []).append(row)

    for suite, recs in sorted(by_suite.items()):
        hit_dump.append(f"## {suite}")
        for rec in recs:
            ext_path = EXTRACTED / rec["extract_filename"]
            if not ext_path.exists():
                continue
            text = ext_path.read_text(encoding="utf-8", errors="ignore")
            if len(text) < 200:
                continue
            chunks = split_questions(text)
            if not chunks:
                # If we cannot split, treat whole paper as one blob to grep
                whole = score_legal(text)
                if whole["n_strong"] >= 1:
                    hit_dump.append(f"- {rec['extract_filename']}: whole-paper hits strong={whole['strong'][:5]} (no qid split)")
                    candidate_rows.append({
                        "question_id": f"{suite}__whole",
                        "suite": suite,
                        "year": rec["year"],
                        "qno": "?",
                        "source_id": rec["source_id"],
                        "paper_file": rec["abs_path"],
                        "paper_extract": rec["extract_filename"],
                        "n_hits": whole["n_hits"],
                        "n_strong": whole["n_strong"],
                        "hits": ";".join(whole["hits"][:15]),
                        "strong": ";".join(whole["strong"]),
                        "neg": ";".join(whole["neg"]),
                        "needs_review": "yes_no_qid_split",
                    })
                continue
            for qno, chunk in sorted(chunks.items()):
                sc = score_legal(chunk)
                # Decision rule:
                # - n_strong >= 1, OR n_hits >= 2 AND len(chunk) >= 300 AND no overpowering 必修三 signal
                if sc["n_strong"] >= 1 or (sc["n_hits"] >= 2 and len(chunk) >= 300):
                    line = f"- {rec['extract_filename']} Q{qno} chars={len(chunk)} hits={sc['n_hits']} strong={sc['strong']} neg={sc['neg']}"
                    hit_dump.append(line)
                    candidate_rows.append({
                        "question_id": f"{suite}__Q{qno}",
                        "suite": suite,
                        "year": rec["year"],
                        "qno": qno,
                        "source_id": rec["source_id"],
                        "paper_file": rec["abs_path"],
                        "paper_extract": rec["extract_filename"],
                        "n_hits": sc["n_hits"],
                        "n_strong": sc["n_strong"],
                        "hits": ";".join(sc["hits"][:15]),
                        "strong": ";".join(sc["strong"]),
                        "neg": ";".join(sc["neg"]),
                        "needs_review": "yes" if sc["n_neg"] >= 2 else "",
                    })
                    if sc["n_neg"] >= 2:
                        boundary_notes.append(f"- {rec['extract_filename']} Q{qno}: mixed signals (legal hits + 必修三 hits); read full to decide.")
        hit_dump.append("")

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        fields = ["question_id","suite","year","qno","source_id","paper_file","paper_extract","n_hits","n_strong","hits","strong","neg","needs_review"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in candidate_rows:
            w.writerow(r)

    OUT_MD.write_text("# 02 Uncertain / boundary cases\n\n" + "\n".join(boundary_notes), encoding="utf-8")
    HIT_DUMP.write_text("\n".join(hit_dump), encoding="utf-8")
    print(f"candidate_rows={len(candidate_rows)} suites={len(by_suite)} boundary_notes={len(boundary_notes)}")

if __name__ == "__main__":
    main()
