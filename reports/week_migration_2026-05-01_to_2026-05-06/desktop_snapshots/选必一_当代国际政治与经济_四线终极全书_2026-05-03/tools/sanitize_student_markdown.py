#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


RUN = Path("/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03")
SRC = RUN / "07_student_doc" / "选必一_完整学生讲义_融合稿_20260504.md"
OUT = RUN / "07_student_doc" / "选必一_完整学生讲义_干净候选稿_20260504.md"


FREQ_RE = re.compile(r"[（(]出现\d+题(?:，含等级题或边界表达)?[）)]")
IMAGE_RE = re.compile(r"内嵌图片image\d+")

CORE_CROSSREF_REMOVES = {
    "共商共建共享的全球治理观": {
        "人类命运共同体",
        "以人类命运共同体理念",
        "命运共同体",
        "正确义利观",
        "坚持正确义利观",
        "全人类共同价值",
        "真正的多边主义和互利共赢参与全球治理",
        "践行真正的多边主义",
        "坚持互利共赢",
        "全球发展倡议",
        "以发展促繁荣",
        "发展合作中共享机遇",
        "公平正义合作共赢的新型国际关系",
        "共同利益是国家合作的基础",
    },
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": {
        "贡献中国智慧和中国方案",
        "中国智慧",
        "中国方案",
        "完善全球治理",
        "全人类共同价值",
        "正确义利观",
        "构建人类命运共同体",
        "推动构建人类命运共同体",
        "人类命运共同体",
        "真正的多边主义",
        "全球治理变革",
    },
    "维护国家利益并兼顾他国合理关切，坚持正确义利观": {
        "在联合国宗旨和原则框架下构建人类命运共同体，加强国际交流合作，积极参与全球治理",
        "联合国宗旨原则",
        "HMC",
        "和平与发展",
    },
}

CORE_NOTES = {
    "共商共建共享的全球治理观": "人类命运共同体、正确义利观、真正的多边主义等常同题出现，但它们不是“共商共建共享”的同义词，作答时按设问分别落点。",
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": "新型国际关系可以和人类命运共同体、中国方案、真正的多边主义同题配合，但本核心自身要保留“相互尊重、公平正义、合作共赢”。",
    "维护国家利益并兼顾他国合理关切，坚持正确义利观": "国家利益、合理关切、义利相兼是本核心主干；联合国框架或人类命运共同体只能在材料明确出现时另起角度。",
}

CORE_CROSSREF_SUBSTRINGS = {
    "共商共建共享的全球治理观": (
        "人类命运共同体",
        "正确义利观",
        "全人类共同价值",
        "新型国际关系",
        "真正的多边主义",
        "共同利益",
        "负责任大国",
        "全球可持续发展",
    ),
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": (
        "人类命运共同体",
        "中国智慧",
        "中国方案",
        "正确义利观",
        "全人类共同价值",
        "全球治理",
        "真正的多边主义",
    ),
    "维护国家利益并兼顾他国合理关切，坚持正确义利观": (
        "联合国",
        "人类命运共同体",
        "全球治理",
        "和平与发展",
    ),
}


def strip_frequency(text: str) -> str:
    text = FREQ_RE.sub("", text)
    text = text.replace("，含等级题或边界表达", "")
    return text


def normalize_public_words(text: str) -> str:
    replacements = {
        "主观题细则术语与答题框架": "主观题核心术语与答题框架",
        "等级题": "开放题",
        "边界表达": "慎用表达",
        "主频": "常用框架",
        "评分细则": "答案口径",
        "评分位置": "答题位置",
        "评分得分位置提示": "题目提示",
        "评分标准说明": "答案说明",
        "讲评材料": "例题说明",
        "答案提示": "答题提示",
        "参考示例": "示例",
        "得分说明": "答题说明",
        "见点给分": "按要点展开",
        "可给分": "可写",
        "赋分": "作答",
        "分值": "作答层次",
        "采分": "答题",
        "HMC": "人类命运共同体",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = IMAGE_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip() if text.startswith("**") else text
    return text


def repair_globalization_direction(text: str) -> str:
    fixes = {
        "推动经济全球化朝着更加开放；包容；普惠；平衡；共赢的方向发展": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "推动经济全球化朝着更加开放；包容；普惠；平衡；共赢方向发展": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "开放包容普惠平衡共赢": "开放、包容、普惠、平衡、共赢",
        "普惠平衡共赢开放": "开放、包容、普惠、平衡、共赢",
    }
    for old, new in fixes.items():
        text = text.replace(old, new)
    return text


def split_terms(value: str) -> list[str]:
    raw = [x.strip(" 。；;、,，") for x in re.split(r"[；;]", value) if x.strip(" 。；;、,，")]
    terms: list[str] = []
    seen: set[str] = set()
    for item in raw:
        item = repair_globalization_direction(item)
        if item and item not in seen:
            terms.append(item)
            seen.add(item)
    return terms


def clean_accumulation(line: str, current_core: str) -> str:
    prefix, value = line.split("：", 1)
    value = normalize_public_words(repair_globalization_direction(value.rstrip("。")))
    terms = split_terms(value)
    removes = CORE_CROSSREF_REMOVES.get(current_core, set())
    substrings = CORE_CROSSREF_SUBSTRINGS.get(current_core, ())
    cleaned = [t for t in terms if t not in removes and not any(s in t for s in substrings)]
    if not cleaned:
        cleaned = terms
    return f"{prefix}：{'；'.join(cleaned)}。"


def main() -> None:
    text = SRC.read_text(encoding="utf-8-sig")
    out: list[str] = []
    current_core = ""

    for raw in text.splitlines():
        line = raw.rstrip()
        line = strip_frequency(line)

        if line.startswith("# "):
            line = normalize_public_words(line)

        if line.startswith("### ") and not line.startswith("#### "):
            current_core = strip_frequency(line.removeprefix("### ")).strip()
            line = f"### {current_core}"

        if line.startswith("- "):
            line = strip_frequency(normalize_public_words(line))

        if line.startswith("**得分位置**"):
            continue

        if line.startswith("**来源**"):
            line = line.replace("**来源**", "**例题来源**", 1)

        if line.startswith("**使用边界**"):
            line = "**使用边界**：本核心下有开放题或慎用表达，正式作答时先看设问和材料是否匹配。"

        if line.startswith("**慎用提醒**"):
            line = line.replace("慎用边界：", "")
            line = line.replace("本题可作表述积累或开放题训练，不能当固定逐点模板。", "本题适合积累表达，不能当固定逐点模板。")
            line = line.replace("本题只能作兜底表达，主答点应先服从本题具体材料和作答层次结构。", "本题只能作兜底表达，主答点应先服从本题具体材料和作答层次。")

        if line.startswith("**答题点自身积累**") or line.startswith("**表述积累**"):
            line = clean_accumulation(line, current_core)

        line = normalize_public_words(repair_globalization_direction(line))
        out.append(line)

        if raw.startswith("**答题点自身积累**") and current_core in CORE_NOTES:
            out.append(f"**搭配提醒**：{CORE_NOTES[current_core]}")

    final = "\n".join(out).strip() + "\n"
    OUT.write_text(final, encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
