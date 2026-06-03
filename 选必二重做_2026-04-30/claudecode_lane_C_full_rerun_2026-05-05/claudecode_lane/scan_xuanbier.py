#!/usr/bin/env python3
"""
C 线独立扫题：从 B 线 OCR 解析文本中识别选必二法律题，输出题级切片与套级状态。

不读 B 线结论性产物（QUESTION_PACK / hand_crafted / 框架版 等），仅读 .txt 解析文本。
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_C_full_rerun_2026-05-05")
EXTRACTED = ROOT / "source_inventory" / "extracted_text_from_B"
OUT_DIR = ROOT / "question_packs"
OUT_SLICE_DIR = OUT_DIR / "question_slices"
OUT_SLICE_DIR.mkdir(parents=True, exist_ok=True)

# 选必二法律核心关键词（出现即强信号）
LEGAL_STRONG = [
    "民法典", "民事行为", "民事主体", "民事法律关系",
    "合同", "缔约", "违约", "解除合同", "合同效力",
    "侵权", "侵权责任", "无过错责任", "过错责任", "高度危险作业", "饲养动物", "网络侵权", "环境侵权", "产品责任",
    "物权", "所有权", "用益物权", "担保物权", "抵押", "质押", "留置", "宅基地", "土地承包",
    "婚姻家庭", "夫妻共同", "夫妻共同财产", "夫妻共同债务", "彩礼", "离婚", "抚养", "赡养",
    "继承", "法定继承", "遗嘱", "遗赠", "遗产",
    "知识产权", "著作权", "商标", "专利", "商业秘密", "不正当竞争", "商业诋毁",
    "消费者权益保护法", "经营者", "三倍赔偿", "十倍赔偿", "惩罚性赔偿",
    "劳动合同", "劳动报酬", "工伤", "经济补偿", "解雇", "试用期",
    "电子商务法", "电子合同", "平台经营者", "AIGC", "数字人格",
    "诉讼", "民事诉讼", "调解", "人民调解", "仲裁",
    "效力待定", "可撤销", "无效合同", "缔约过失", "情势变更",
    "肖像权", "名誉权", "隐私权", "个人信息保护",
    "监护", "监护人", "限制民事行为能力",
]

# 反信号：必修三 / 必修一二 / 选必一三典型词，单独出现不足以排除，但作为反向权重
ANTI_SIGNALS = [
    "依法治国", "法治建设", "法治国家", "法治政府", "法治社会", "法治体系",
    "人民代表大会", "全国人大", "立法机关", "国务院", "政协",
    "辩证唯物主义", "历史唯物主义", "矛盾", "同一性", "斗争性", "联系", "发展", "辩证否定",
    "经济全球化", "对外开放", "市场调节", "宏观调控", "供给侧",
    "中国共产党", "党的领导", "新时代",
    "传统文化", "中华文化", "文化交流", "文化自信",
    "归纳推理", "类比推理", "演绎推理", "三段论", "换位", "换质",
]

# 题号识别正则：行首"X."或"X、"或"X．"，X 为 1-25
QNUM_RE = re.compile(r"(?m)^\s*([1-9]|1[0-9]|2[0-5])[\.、．]\s")

# 文件命名约定：scope-year/year-suite/year-suite__type__...txt
FILE_TYPE_RE = re.compile(r"__(试卷|细则|分题细则|参考答案|阅卷总结|讲评|评标|补充材料)")


def split_questions(text: str) -> list[tuple[int, int, int, str]]:
    """切题：返回 [(qnum, start_offset, end_offset, body), ...]，按题号边界。"""
    matches = list(QNUM_RE.finditer(text))
    out = []
    for i, m in enumerate(matches):
        qnum = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        # 防 18.4 千克陷阱：题号后必须紧跟空格或换行后接有意义内容
        # 如果 body 太短（<30 字符）或以纯数字单位开头，跳过
        body_strip = body[len(m.group(0)):].lstrip()
        if len(body_strip) < 20:
            continue
        # 排除"18.4千克""18.5%"这类
        if re.match(r"^[\.\d]+\s*(千克|公斤|克|米|%|％|度|元|岁|吨|升|平方|立方)", body_strip):
            continue
        out.append((qnum, start, end, body))
    return out


def score_xuanbier(body: str) -> tuple[int, list[str], int, list[str]]:
    """返回 (legal_score, hit_legal, anti_score, hit_anti)。"""
    hit_legal = [k for k in LEGAL_STRONG if k in body]
    hit_anti = [k for k in ANTI_SIGNALS if k in body]
    return len(hit_legal), hit_legal, len(hit_anti), hit_anti


def classify(legal_n: int, anti_n: int, body: str) -> str:
    """分类：xuanbier_main / xuanbier_choice_only / not_xuanbier / uncertain。"""
    # 先看是不是选择题（出现 A．B．C．D． 或 A. B. C. D.）
    is_choice = bool(re.search(r"[\sA][．\.]\s*[^\n]{2,80}\s*[\sB][．\.]", body[:1500]))
    # 主观题特征：出现"运用..."、"结合材料"、"分析"、"指出"、"评析"、"驳斥"等设问词
    has_subjective_prompt = any(k in body for k in ["运用", "结合材料", "结合上述", "分析", "评析", "评价", "驳斥", "指出", "回答下列", "辨析", "请", "撰写"])
    # 长度：选择题通常 < 800 字，主观题通常 > 500 字
    L = len(body)

    # 强阈值：legal>=2 且 (anti==0 或 legal>anti+1)
    if legal_n >= 2 and (anti_n == 0 or legal_n > anti_n + 1):
        return "xuanbier_choice" if is_choice else "xuanbier_main"
    # 弱阈值：legal>=1 且 anti==0
    if legal_n >= 1 and anti_n == 0:
        return "xuanbier_choice_uncertain" if is_choice else "xuanbier_main_uncertain"
    return "not_xuanbier"


def process():
    suite_status = defaultdict(lambda: {
        "year": "", "suite": "", "files": 0, "main_q": [], "choice_q": [],
        "uncertain_q": [], "rubric_files": [], "no_xuanbier_signal": False,
    })
    question_index = []
    for year_dir in sorted(EXTRACTED.iterdir()):
        if not year_dir.is_dir():
            continue
        year = year_dir.name
        for suite_dir in sorted(year_dir.iterdir()):
            if not suite_dir.is_dir():
                continue
            suite = suite_dir.name
            key = f"{year}/{suite}"
            ss = suite_status[key]
            ss["year"], ss["suite"] = year, suite
            for txt in sorted(suite_dir.glob("*.txt")):
                ss["files"] += 1
                fname = txt.name
                m = FILE_TYPE_RE.search(fname)
                ftype = m.group(1) if m else "unknown"
                if ftype in ("细则", "分题细则", "评标", "阅卷总结", "讲评"):
                    ss["rubric_files"].append(fname)
                if ftype != "试卷":
                    continue
                try:
                    text = txt.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                questions = split_questions(text)
                for qnum, start, end, body in questions:
                    legal_n, hit_legal, anti_n, hit_anti = score_xuanbier(body)
                    cat = classify(legal_n, anti_n, body)
                    if cat.startswith("not_") or cat == "":
                        continue
                    qid = f"{year}__{suite}__Q{qnum}"
                    slice_path = OUT_SLICE_DIR / f"{qid}.txt"
                    slice_path.write_text(
                        f"# {qid}\n# legal_keywords: {','.join(hit_legal)}\n# anti_keywords: {','.join(hit_anti)}\n# classify: {cat}\n# source_file: {fname}\n\n{body}",
                        encoding="utf-8"
                    )
                    if "main" in cat:
                        ss["main_q"].append(qnum)
                    elif "choice" in cat:
                        ss["choice_q"].append(qnum)
                    if "uncertain" in cat:
                        ss["uncertain_q"].append(qnum)
                    question_index.append({
                        "qid": qid, "year": year, "suite": suite, "qnum": qnum,
                        "type": "main" if "main" in cat else "choice",
                        "category": cat,
                        "legal_keyword_count": legal_n,
                        "anti_keyword_count": anti_n,
                        "legal_keywords": ",".join(hit_legal[:10]),
                        "source_file": fname,
                        "body_length": len(body),
                    })
            if not (ss["main_q"] or ss["choice_q"]):
                ss["no_xuanbier_signal"] = True

    # 写 SUITE_STATUS.csv
    with (OUT_DIR / "SUITE_STATUS.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "suite", "files_total", "main_q_nums", "choice_q_nums",
                    "uncertain_q_nums", "rubric_files_count", "rubric_files_sample", "status"])
        for key, ss in sorted(suite_status.items()):
            status = "no_xuanbier" if ss["no_xuanbier_signal"] else (
                "has_xuanbier_main" if ss["main_q"] else "has_xuanbier_choice_only"
            )
            w.writerow([
                ss["year"], ss["suite"], ss["files"],
                ",".join(str(x) for x in sorted(set(ss["main_q"]))),
                ",".join(str(x) for x in sorted(set(ss["choice_q"]))),
                ",".join(str(x) for x in sorted(set(ss["uncertain_q"]))),
                len(ss["rubric_files"]),
                ";".join(ss["rubric_files"][:3]),
                status,
            ])
    # 写 QUESTION_INDEX.csv
    with (OUT_DIR / "QUESTION_INDEX.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "qid", "year", "suite", "qnum", "type", "category",
            "legal_keyword_count", "anti_keyword_count", "legal_keywords",
            "source_file", "body_length",
        ])
        w.writeheader()
        for row in sorted(question_index, key=lambda r: (r["year"], r["suite"], r["qnum"])):
            w.writerow(row)
    # 摘要
    total_main = sum(1 for r in question_index if r["type"] == "main")
    total_choice = sum(1 for r in question_index if r["type"] == "choice")
    total_uncertain = sum(1 for r in question_index if "uncertain" in r["category"])
    print(f"suites scanned: {len(suite_status)}")
    print(f"main questions identified: {total_main}")
    print(f"choice questions identified: {total_choice}")
    print(f"uncertain among them: {total_uncertain}")
    print(f"slices written to: {OUT_SLICE_DIR}")


if __name__ == "__main__":
    process()
