#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""STEP_04 Phase B: assemble 习题与细则汇编 md + csv from question packets."""
import re, csv, glob, os, sys

RUN = "/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/opus48_dynamic_workflow_subjective_compilation_2026-05-29"
PK = os.path.join(RUN, "03_source_packets")
MATRIX = os.path.join(RUN, "00_control/QUESTION_COVERAGE_MATRIX.csv")
LEDGER = os.path.join(RUN, "00_control/RUBRIC_SEARCH_LEDGER.csv")
OUT_MD = os.path.join(RUN, "04_outputs/选必二法律主观题_习题与细则汇编_20260529.md")
OUT_CSV = os.path.join(RUN, "04_outputs/选必二法律主观题_习题与细则汇编_20260529.csv")

def load_csv(p):
    with open(p, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

mat = {r["question_id"]: r for r in load_csv(MATRIX)}
led = {r["question_id"]: r for r in load_csv(LEDGER)}

def sections(txt):
    parts = re.split(r'(?m)^(## \d+\..*)$', txt)
    d = {}
    for i in range(1, len(parts), 2):
        hdr = parts[i].strip()
        body = parts[i+1] if i+1 < len(parts) else ""
        m = re.match(r'## (\d+)\.', hdr)
        if m:
            d[int(m.group(1))] = (hdr, body.strip("\n"))
    return d

def first(body, label):
    m = re.search(r'(?m)^-\s*%s\s*[:：]\s*(.*)$' % re.escape(label), body)
    return m.group(1).strip() if m else ""

def rubric_text(sec5body):
    m = re.search(r'细则原文（[^）]*）\s*[:：]\s*\n+(.*?)(?:\n-\s*抓取说明|\Z)', sec5body, re.S)
    return (m.group(1).strip() if m else sec5body.strip())

def rubric_note(sec5body):
    m = re.search(r'(?m)^-\s*抓取说明\s*[:：]\s*(.*)', sec5body)
    if not m: return ""
    # capture to end (single bullet, may be multiline)
    note = sec5body[m.start():].strip()
    return re.sub(r'(?m)^-\s*抓取说明\s*[:：]\s*', '', note, count=1).strip()

CANON = {'法律关系':'法律关系','争点':'争点/诉讼请求','规则要件':'规则要件',
         '事实匹配':'事实匹配','责任':'责任/程序/落点','法治价值':'法治价值'}
ORDER = ['法律关系','争点/诉讼请求','规则要件','事实匹配','责任/程序/落点','法治价值']

def parse_sec6(body):
    # anchor on label keyword at column 0 (indented sub-bullets ignored), tolerant of
    # bold markers and parenthetical qualifiers before the colon. Capture each block verbatim.
    pat = re.compile(r'(?m)^-\s*\*{0,2}(法律关系|争点|规则要件|事实匹配|责任|法治价值)')
    ms = list(pat.finditer(body))
    blocks = {}
    for i, mm in enumerate(ms):
        key = CANON[mm.group(1)]
        start = mm.start()
        end = ms[i+1].start() if i+1 < len(ms) else len(body)
        blocks[key] = body[start:end].strip()
    preamble = body[:ms[0].start()].strip() if ms else body.strip()
    return blocks, preamble

def strip_label(block):
    # for CSV: drop one leading "- ", then the label plus an optional （…）/(…) qualifier
    # (which may itself contain colons) and the terminating colon, if cleanly on first line.
    s = re.sub(r'^-\s*', '', block.lstrip())
    s = re.sub(r'^\*{0,2}(法律关系|争点|规则要件|事实匹配|责任|法治价值)(?:[^：:（(\n]*[（(][^）)]*[）)])?\*{0,2}\s*[:：]\s*',
               '', s, count=1)
    return s.strip()

def suite_num(qid):
    m = re.match(r'S(\d+)', qid)
    return int(m.group(1)) if m else 999

# collect question packets (non-NOTFOUND)
files = [f for f in sorted(glob.glob(os.path.join(PK, "*.md"))) if "NOTFOUND" not in f]
recs = []
for f in files:
    qid = os.path.basename(f)[:-3]
    txt = open(f, encoding="utf-8").read()
    sec = sections(txt)
    s1 = sec.get(1, ("",""))[1]
    s2 = sec.get(2, ("",""))[1]
    s3 = sec.get(3, ("",""))[1]
    s5 = sec.get(5, ("",""))[1]
    s6 = sec.get(6, ("",""))[1]
    m = mat.get(qid, {})
    l = led.get(qid, {})
    a, pre6 = parse_sec6(s6)
    recs.append({
        "qid": qid, "year": m.get("year",""), "district": m.get("district",""),
        "stage": m.get("stage",""), "qno": m.get("question_no",""),
        "sub": m.get("subquestion",""), "module": m.get("module_decision",""),
        "src_file": first(s1, "原始试卷文件"), "pos": first(s1, "题面位置"),
        "material": s2, "prompt": s3, "rubric": rubric_text(s5), "rubric_note": rubric_note(s5),
        "rubric_src": l.get("rubric_source_path",""), "rubric_fmt": l.get("rubric_format",""),
        "evidence": l.get("evidence_type",""), "method": l.get("rubric_extract_method",""),
        "rstatus": l.get("rubric_status",""), "notes": m.get("notes",""),
        "blocks": a, "pre6": pre6,
        "fa": a.get("法律关系",""), "zd": a.get("争点/诉讼请求",""),
        "gz": a.get("规则要件",""), "sm": a.get("事实匹配",""),
        "zr": a.get("责任/程序/落点",""), "fz": a.get("法治价值",""),
        "sec6_filled": "（STEP_04 完成）" in sec.get(6, ("",""))[0],
    })

recs.sort(key=lambda r: (r["year"], suite_num(r["qid"]), r["qno"]))

# diagnostics
filled = sum(1 for r in recs if r["sec6_filled"])
def missing_labels(r): return [k for k in ORDER if not r["blocks"].get(k)]
empty_analysis = [r["qid"] for r in recs if missing_labels(r)]
print("packets:", len(recs), "| sec6 filled-header:", filled, "| empty-rubric:", [r["qid"] for r in recs if not r["rubric"]])
print("packets with >=1 empty analysis bullet:", len(empty_analysis))
if empty_analysis and "--final" in sys.argv:
    for r in recs:
        if missing_labels(r):
            print("  STILL EMPTY:", r["qid"], "->", missing_labels(r))

if "--dryrun" in sys.argv:
    # show one sample's parsed fields
    s = recs[0]
    print("--- SAMPLE", s["qid"], "---")
    for k in ("src_file","pos","rubric_src","evidence","method","rstatus"):
        print(f"  {k}: {s[k][:80]}")
    print("  material[:60]:", s["material"][:60].replace("\n"," "))
    print("  rubric[:60]:", s["rubric"][:60].replace("\n"," "))
    sys.exit(0)

# ---- build MD ----
def sub_label(r):
    return "" if r["sub"] in ("none","","-") else r["sub"]

md = []
md.append("# 选必二《法律与生活》法律主观题 习题与细则汇编（2024–2026 北京区级模拟题）\n")
md.append("> 生成日期 2026-05-29 · 本文件为 STEP_04 汇编产物。\n")
md.append(f"> 共 {len(recs)} 道法律主观题，横跨 57 套卷（2026海淀期末 S61 含两道：18(1)、19）。\n")
md.append("> 源目录：`/Users/wanglifei/Desktop/{2024,2025,2026}模拟题`。\n")
md.append("> 证据规则：每题“对应细则原文”均为 `formal_rubric`（正式评分细则/评标/阅卷总结/讲评/分题细则），逐字转录；试卷普通参考答案仅作 support，不充当细则。\n")
md.append("> 模块判定以设问括号书名为决定性依据；`needs_review` 题为设问未标书名、按民事内容+同卷排除法判定，已在该题注明。\n")
md.append("> 诚实性标记：2026-05-29 残项复核后，S33_Q20 案件三结果④已由同套讲评 PPT 补全；S42_Q18 图表无逐年精确数值标签且不影响第(3)问；S18_Q19 已核为正式细则8分、原题页未印分值；S62_Q17 已在同步镜像教师版原卷中补回题面与设问。S16_Q19 仍保留真实分值冲突：试卷参考答案页8分 vs 正式细则6分。\n")
md.append("> 旧选必二成果全部作废；本汇编“选必二法理分析”由题源+细则反推，未继承旧结论/旧框架。\n")
md.append("\n## 目录\n")
md.append("| # | question_id | 年份 | 区 | 阶段 | 题号 | 模块 | 证据 | 备注 |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for i, r in enumerate(recs, 1):
    qn = f"第{r['qno']}题" + (f" {sub_label(r)}" if sub_label(r) else "")
    flag = "需复核" if "needs_review" in r["notes"] else ""
    if r["qid"] == "S62_Q17": flag = "镜像原卷已核"
    md.append(f"| {i} | {r['qid']} | {r['year']} | {r['district']} | {r['stage']} | {qn} | {r['module']} | {r['evidence']} | {flag} |")
md.append("")

cur_year = None
for r in recs:
    if r["year"] != cur_year:
        cur_year = r["year"]
        md.append(f"\n---\n\n# {cur_year} 年\n")
    qn = f"第{r['qno']}题" + (f"{sub_label(r)}" if sub_label(r) else "")
    md.append(f"\n## {r['qid']} ｜ {r['year']} {r['district']}{r['stage']} {qn} ｜ {r['module']}\n")
    md.append("**一、题目编号与来源**\n")
    md.append(f"- 题源：{r['year']} {r['district']} {r['stage']} {qn}")
    md.append(f"- 原始试卷文件：{r['src_file'] or '见题源包'}")
    if r["pos"]:
        md.append(f"- 题面位置：{r['pos']}")
    md.append(f"- 题源包：`03_source_packets/{r['qid']}.md`")
    if "needs_review" in r["notes"] or r["qid"] == "S62_Q17":
        md.append(f"- 判定备注：{r['notes']}")
    md.append("\n**二、完整材料**\n")
    md.append(r["material"])
    md.append("\n**三、完整设问**\n")
    md.append(r["prompt"])
    md.append("\n**四、对应细则原文（formal_rubric，逐字）**\n")
    md.append(r["rubric"])
    md.append("\n**五、细则来源与证据类型**\n")
    md.append(f"- 细则来源文件：`{r['rubric_src']}`")
    md.append(f"- 证据类型：`{r['evidence']}` ｜ 提取方式：`{r['method']}` ｜ 细则状态：`{r['rstatus']}`")
    if r["rubric_note"]:
        md.append(f"- 抓取说明：{r['rubric_note']}")
    md.append("\n**六、选必二法理分析**\n")
    if r["pre6"]:
        md.append(r["pre6"] + "\n")
    for lbl in ORDER:
        blk = r["blocks"].get(lbl)
        md.append(blk if blk else f"- **{lbl}**：（待补）")
    md.append("")

with open(OUT_MD, "w", encoding="utf-8") as fh:
    fh.write("\n".join(md))

# ---- build CSV ----
cols = ["question_id","year","district","stage","question_no","target_subquestion","module_decision",
        "source_file","question_position","question_packet",
        "完整材料","完整设问","对应细则原文","细则来源文件","rubric_format","evidence_type","extract_method","rubric_status",
        "法律关系","争点诉讼请求","规则要件","事实匹配","责任程序落点","法治价值","判定备注","抓取说明"]
with open(OUT_CSV, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(cols)
    for r in recs:
        w.writerow([r["qid"],r["year"],r["district"],r["stage"],r["qno"],r["sub"],r["module"],
                    r["src_file"],r["pos"],f"03_source_packets/{r['qid']}.md",
                    r["material"],r["prompt"],r["rubric"],r["rubric_src"],r["rubric_fmt"],r["evidence"],r["method"],r["rstatus"],
                    strip_label(r["blocks"].get("法律关系","")),strip_label(r["blocks"].get("争点/诉讼请求","")),
                    strip_label(r["blocks"].get("规则要件","")),strip_label(r["blocks"].get("事实匹配","")),
                    strip_label(r["blocks"].get("责任/程序/落点","")),strip_label(r["blocks"].get("法治价值","")),
                    r["notes"],r["rubric_note"]])

print("WROTE md:", OUT_MD)
print("WROTE csv:", OUT_CSV)
print("md bytes:", os.path.getsize(OUT_MD), "| csv rows:", len(recs)+1)
