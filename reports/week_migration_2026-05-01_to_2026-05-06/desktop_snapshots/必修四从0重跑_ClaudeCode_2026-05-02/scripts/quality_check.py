#!/usr/bin/env python3
"""扫描所有 audit/entries/*.jsonl，找出违反硬性规则的条目。

检查：
- 必备字段非空（材料触发点/设问/为什么能想到/答案落点）
- 答案落点不含元话术（回应设问/服务设问/PASS/yes/correct_option_chain 等）
- 为什么能想到不与材料触发点完全重复
- 设问字段不含审计/答案来源话术
- 高风险词（辩证否定/量变质变/两点论与重点论/主次矛盾/矛盾主次方面/价值观导向）需 rubric_excerpt 含原文等值
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02")
ENTRIES_DIR = ROOT / "audit" / "entries"
STUDENT_MD = ROOT / "outputs" / "2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md"

REQUIRED_FIELDS = ["材料触发点", "设问", "为什么能想到", "答案落点"]
STUDENT_FORBIDDEN_RE = re.compile(
    r"细则|评标|参考答案|答案写|答案核|答案/补充|可从.*角度|/Users/|\.pdf|\.docx|\.pptx|OCR|debug|slide|line id|file id|PASS|correct_option_chain|filled",
    re.I,
)
FORBIDDEN_IN_ANSWER = [
    "回应设问", "服务设问", "可从某角度作答", "可从…角度作答", "可从……角度作答",
    "把材料事实同原理连接起来", "答案可以落在",
    "PASS", "yes", "filled", "correct_option_chain", "PASS_OBJECTIVE",
    "评标", "答案写", "答案/补充", "答案核",
]
FORBIDDEN_IN_TRIGGER = [
    "PASS", "yes", "filled", "correct_option_chain",
    "/Users/", "page_", ".pdf", ".docx", ".pptx", "OCR", "ocr-",
]

# 这些话术不能出现在"为什么能想到"——它们是审计/答案来源话术，不是知识解释链
FORBIDDEN_IN_WHY_PREFIX = [
    "细则在", "细则要求", "细则明确", "细则给出", "细则把",
    "评分细则要求", "评分细则给出", "评分细则把",
    "因为细则", "因为评分细则",
    "评标在", "评标要求", "评标给出",
    "参考答案给出",
]

HIGH_RISK_TERMS = {
    "辩证否定": ["辩证否定", "辩证的否定", "扬弃", "否定之否定", "守正创新", "否定观"],
    "量变质变": ["量变", "质变", "量的积累", "量积累", "适度"],
    "两点论与重点论": ["两点论", "重点论", "主要矛盾", "次要矛盾", "主次", "矛盾的主要方面",
                      "矛盾主要方面", "矛盾次要方面", "主流", "支流"],
    "价值观导向": ["价值观", "导向", "价值导向", "树立正确"],
}

# 哲学线学生版禁止出现的"纯文化"节点关键词（target_node 中不能含）
CULTURE_NODE_TOKENS = ["文化的功能", "文化功能", "文化交流交融", "传统文化", "文化自信",
                       "民族精神", "社会主义核心价值观", "文化传承", "中华文化", "文化创新",
                       "中华优秀传统文化", "文化强国"]


def main():
    issues = []
    total = 0
    for f in sorted(ENTRIES_DIR.glob("*.jsonl")):
        with open(f, "r", encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                total += 1
                try:
                    e = json.loads(line)
                except Exception as ex:
                    issues.append((f.name, ln, "JSON_PARSE", str(ex)))
                    continue
                eid = e.get("entry_id", f"{f.name}#{ln}")

                # 必备字段（选择题对设问放宽）
                qtype = e.get("question_type", "subjective")
                for fld in REQUIRED_FIELDS:
                    val = str(e.get(fld, ""))
                    min_len = 5 if (qtype in {"objective", "choice"} and fld == "设问") else 10
                    if not val or len(val.strip()) < min_len:
                        issues.append((f.name, ln, "EMPTY_OR_SHORT_FIELD",
                                       f"{eid} 字段 {fld} 为空或过短"))

                ans = str(e.get("答案落点", ""))
                trig = str(e.get("材料触发点", ""))
                why = str(e.get("为什么能想到", ""))
                ask = str(e.get("设问", ""))
                for fld_name, val in [("材料触发点", trig), ("设问", ask), ("为什么能想到", why), ("答案落点", ans)]:
                    m = STUDENT_FORBIDDEN_RE.search(val)
                    if m:
                        issues.append((f.name, ln, "FORBIDDEN_STUDENT_FIELD",
                                       f"{eid} {fld_name} 含学生版禁词 '{m.group(0)}'"))

                for tok in FORBIDDEN_IN_ANSWER:
                    if tok in ans:
                        issues.append((f.name, ln, "FORBIDDEN_IN_ANSWER",
                                       f"{eid} 答案落点含禁用词 '{tok}'"))
                # 为什么能想到 不能开头就讲"细则给出/要求"
                for tok in FORBIDDEN_IN_WHY_PREFIX:
                    if tok in why:
                        issues.append((f.name, ln, "WHY_HAS_RUBRIC_CITATION",
                                       f"{eid} 为什么能想到含 '{tok}'（审计话术，应转入 rubric_excerpt）"))
                for tok in FORBIDDEN_IN_TRIGGER:
                    for fld_name, val in [("材料触发点", trig), ("设问", ask), ("为什么能想到", why), ("答案落点", ans)]:
                        if tok in val:
                            issues.append((f.name, ln, "FORBIDDEN_GENERAL",
                                           f"{eid} {fld_name} 含 '{tok}'"))

                # 重复检查
                if trig and why and trig.strip() == why.strip():
                    issues.append((f.name, ln, "WHY_DUP_TRIGGER",
                                   f"{eid} 为什么能想到 与 材料触发点 完全重复"))

                # 高风险词：节点含某高风险词时，rubric_excerpt 必须含其同义表述之一
                node = str(e.get("target_node_path", ""))
                rub = str(e.get("rubric_excerpt", ""))
                for term, equivs in HIGH_RISK_TERMS.items():
                    if term in node:
                        if not any(eq in rub for eq in equivs):
                            issues.append((f.name, ln, "HIGH_RISK_NO_RUBRIC",
                                           f"{eid} 节点含高风险词 '{term}'，rubric_excerpt 缺等值表述（任一：{equivs}）"))
                # 文化节点不应进哲学链
                for tok in CULTURE_NODE_TOKENS:
                    if tok in node:
                        issues.append((f.name, ln, "CULTURE_LEAK",
                                       f"{eid} target_node 含文化关键词 '{tok}'，本轮不做文化线，应排除或重置节点"))

                # 设问字段不应含审计话术
                for tok in ["评分细则", "细则要求", "可从…角度", "可从……角度"]:
                    if tok in ask:
                        issues.append((f.name, ln, "ASK_HAS_AUDIT_TOK",
                                       f"{eid} 设问含 '{tok}'"))

    if STUDENT_MD.exists():
        text = STUDENT_MD.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            m = STUDENT_FORBIDDEN_RE.search(line)
            if m:
                issues.append((STUDENT_MD.name, i, "FORBIDDEN_STUDENT_MD",
                               f"学生版 Markdown 含禁词 '{m.group(0)}': {line[:120]}"))

    print(f"扫描共 {total} 条，发现 {len(issues)} 个问题")
    for f, ln, code, msg in issues:
        print(f"  [{code}] {f}:{ln} {msg}")
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
