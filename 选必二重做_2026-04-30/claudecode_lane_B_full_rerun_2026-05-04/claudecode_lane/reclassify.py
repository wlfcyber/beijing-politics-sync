#!/usr/bin/env python3
"""
Round 3.5 — 二次扫描升级 L1 等级
- 文件名规则扩宽（"细则" / "试卷" 单字也匹配）
- 文件内容规则升级 UNKNOWN → L1（看到阅卷桌话语就升）
- 过滤 ~$ Word 锁文件
"""
import csv, re
from pathlib import Path

PROJECT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04")
LEDGER_IN = PROJECT / "00_control" / "SOURCE_LEDGER.csv"
LEDGER_OUT = PROJECT / "00_control" / "SOURCE_LEDGER_v2.csv"

# 扩宽后的文件名规则
L1_NAME_PAT = re.compile(r"评分细则|评标|阅卷|讲评|分题细则|答案变通|主观题细则|勿传|监控|细则")
L2_NAME_PAT = re.compile(r"答案及评分参考|参考答案|评分参考")
L3_NAME_PAT = re.compile(r"选择题答案|客观题答案")
SRC_NAME_PAT = re.compile(r"试卷|原卷|原题")

# 文件内容关键词：阅卷桌专属话语（去掉通用"（X分）"，仅保留独占性强的 rubric-only 标志）
L1_CONTENT_PATS = [
    re.compile(r"评分细则"),
    re.compile(r"答案变通"),
    re.compile(r"不重复给"),
    re.compile(r"不给分"),
    re.compile(r"才得分"),
    re.compile(r"选\s*\d+\s*个[,，]?\s*给\s*\d+\s*分"),  # "选3个给3分"
    re.compile(r"满分卷|7分卷|6分卷|3分卷|2分卷"),        # 评标样卷
    re.compile(r"阅卷[人组]|阅卷总结|阅卷反馈"),
    re.compile(r"踩分点"),
    re.compile(r"替代知识"),
    re.compile(r"等级水平|水平[1234]|等级赋分|等级描述"),  # 论述题等级表（L1 独有）
    re.compile(r"主观题细则|分题细则|评标实录|主观题评标"),
    re.compile(r"必须有.{1,10}字样"),                    # 法律名精确性卡口
]

L2_CONTENT_PATS = [
    re.compile(r"参考答案[:：]"),
]

INDEX_NAME_PAT = re.compile(r"分类汇编|汇编")

def classify_by_name(path_str: str) -> str:
    # 汇编最高优先级 — 不计入独立证据
    if INDEX_NAME_PAT.search(path_str):
        return "SOURCE_INDEX"
    if SRC_NAME_PAT.search(path_str) and not L1_NAME_PAT.search(path_str):
        return "SOURCE_PAPER"
    if L1_NAME_PAT.search(path_str):
        return "L1"
    if L3_NAME_PAT.search(path_str):
        return "L3"
    if L2_NAME_PAT.search(path_str):
        return "L2"
    return "UNKNOWN"

def classify_by_content(text):
    for p in L1_CONTENT_PATS:
        if p.search(text):
            return "L1"
    for p in L2_CONTENT_PATS:
        if p.search(text):
            return "L2"
    return None

def main():
    with open(LEDGER_IN, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    upgrades = []
    locks_filtered = 0
    new_rows = []
    for r in rows:
        # 锁文件过滤
        if r["filename"].startswith("~$"):
            locks_filtered += 1
            continue

        # 重新按扩宽规则给文件名级假设
        name_hyp = classify_by_name(r["full_path"])
        old_hyp = r["evidence_level_hypothesis"]

        # 文件内容升级（仅对 ok 状态）
        content_hyp = None
        if r["status"] == "ok" and r["out_txt"]:
            try:
                text = Path(r["out_txt"]).read_text(encoding="utf-8")
                content_hyp = classify_by_content(text)
            except Exception:
                pass

        # 最终等级（取最强信号；SOURCE_INDEX 永远锁定）
        if name_hyp == "SOURCE_INDEX":
            r["evidence_level_hypothesis"] = "SOURCE_INDEX"
            r["upgrade_reason"] = "index_locked"
            new_rows.append(r)
            continue
        priority = {"L1": 4, "L2": 3, "L3": 2, "SOURCE_PAPER": 1, "UNKNOWN": 0, "SOURCE_INDEX": -1}
        candidates = [name_hyp]
        if content_hyp:
            candidates.append(content_hyp)
        # 文件名匹配 SOURCE_PAPER 但内容含细则话语（讲评 PDF 包含分级表）→ 升 L1
        final = max(candidates, key=lambda x: priority.get(x, 0))

        if final != old_hyp:
            upgrades.append({
                "path": r["full_path"],
                "from": old_hyp,
                "to": final,
                "reason": "name+content" if content_hyp == final else "name_widened" if name_hyp == final else "content_only",
            })

        r["evidence_level_hypothesis"] = final
        # 加一列说明升级原因
        r["upgrade_reason"] = "name+content" if content_hyp == final and final != "UNKNOWN" else ("name" if name_hyp == final and final != "UNKNOWN" else "")
        new_rows.append(r)

    # 写 v2
    fieldnames = list(new_rows[0].keys())
    with open(LEDGER_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(new_rows)

    # 统计
    from collections import Counter
    print(f"=== Round 3.5 reclassification ===")
    print(f"Input rows:  {len(rows)}")
    print(f"Lock files filtered: {locks_filtered}")
    print(f"Output rows: {len(new_rows)}")
    print(f"Upgrades:    {len(upgrades)}")
    print()
    print(f"Old level distribution:  {Counter(r['evidence_level_hypothesis'] for r in rows)}")
    print(f"New level distribution:  {Counter(r['evidence_level_hypothesis'] for r in new_rows)}")
    print()
    print("=== Sample upgrades (first 30) ===")
    for u in upgrades[:30]:
        print(f"  {u['from']:<12} → {u['to']:<6} [{u['reason']:<14}] {Path(u['path']).name}")

    # 套卷级 L1 覆盖
    from collections import defaultdict
    suite_l1 = defaultdict(list)
    suite_total = defaultdict(int)
    for r in new_rows:
        key = f"{r['year']}/{r['suite']}"
        suite_total[key] += 1
        if r['evidence_level_hypothesis'] == 'L1':
            suite_l1[key].append(r['filename'])

    print()
    print("=== 套卷级 L1 覆盖（v2 后）===")
    no_l1 = []
    for key in sorted(suite_total.keys()):
        if not suite_l1.get(key):
            no_l1.append(key)
    print(f"无 L1 的套卷: {len(no_l1)} 套")
    for k in no_l1:
        print(f"  {k}  (共 {suite_total[k]} 文件)")

if __name__ == "__main__":
    main()
