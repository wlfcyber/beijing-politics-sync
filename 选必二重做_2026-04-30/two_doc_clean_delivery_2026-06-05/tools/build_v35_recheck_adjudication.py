#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_TSV = RUN_DIR / "qa" / "v34_recheck_raw_extract_20260605.tsv"
OUT_TSV = RUN_DIR / "qa" / "v35_recheck_adjudication_20260605.tsv"
OUT_MD = RUN_DIR / "qa" / "v35_recheck_adjudication_summary_20260605.md"


FIXED = {
    "2024·石景山·一模·第17题": "v35已把游离的违约责任句改入合同成立/履行责任背景，避免答案落点跑题。",
    "2024·西城·一模·第18题第3问": "v35重写细则段，拆开义务、个案理由、价值意义和可酌情采分。",
    "2025·东城·二模·第19题": "v35同步细则中的效力待定链条：限制民事行为能力人合同效力待定，拒绝追认后归于无效。",
    "2025·东城·期末·第19题第1问": "v35补明本问2分、每个法律问题1分，并统一共有部分表述。",
    "2025·昌平·二模·第20题第1问": "v35修正AI作者/著作权主体偏绝对表述，改为AI本身不能作为作品作者或享有著作权。",
    "2025·朝阳·二模·第20题第1问": "v35在细则中补入共有部位安装设备应顾及他人合法权益，强化与隐私权、相邻关系衔接。",
    "2025·石景山·一模·第20题": "v35把反不正当竞争责任表述改为停止侵害、赔偿损失等民事责任。",
    "2025·西城·一模·第20题": "v35删去整段式重复细则，保留公平/效率两组4分采点，并把劳动法表述改为重要立法宗旨和基本原则。",
    "2025·西城·二模·第18题": "v35重写细则，删除平台和小刘父母被判共同承担责任的误导表述，统一为平台返还部分款项、按过错分担。",
    "2026·东城·二模·第19题": "v35删除内部阅卷抬头；因卷面总分仍未回源核定，未臆造分值闭合。",
    "2026·海淀·一模·第18题第3问": "v35设问保留7分口径，坏词扫描确认原题图占位符已清理。",
    "2026·海淀·二模·第18题第2问": "v35把宝典B轴改为B5意义价值；正式点分布仍待PDF p54/p55回源。",
    "2026·石景山·一模·第18题": "v35把宝典B轴改为B1表格补链，匹配举证责任分配表格题形。",
    "2026·西城·一模·第17题": "v35把宝典B轴改为B5意义价值，匹配绿色发展作用题。",
    "2026·西城·二模·第18题第1问": "v35把宝典A轴改为A1民事主体与民事法律关系，和AI主体资格同型题对齐。",
    "2026·西城·二模·第18题第3问": "v35删去细则开头重复设问，只保留评分要点。",
    "2026·通州·一模·第20题": "v35坏词扫描确认原题图占位符已清理。",
    "2026·顺义·一模·第18题": "v35修正夫妻共同财产利益一致性过宽表述，改为结合社保缴纳、业务竞争和实际参与可能判断。",
    "2026·顺义·二模·第18题第2问": "v35在宝典轴线中补注含必修3国家治理/制度建设角度。",
}

SOURCE_RISK = {
    "2024·石景山·一模·第18题第2问": "正式点分布细则仍缺失；v35不臆造6分拆分。",
    "2024·顺义思政·二模·第17题": "原细则仅见三层要点，未定位7分具体分配；v35保留待回源。",
    "2025·延庆·一模·第19题": "两套7分切分仍需回源核对，v35未硬并。",
    "2025·海淀·二模·第18题": "民诉法条号争议需以原卷或现行法核定后再改，v35未擅改。",
    "2025·顺义·一模·第19题第2问": "5分封顶与三角度各2分的评分张力仍需源细则裁定。",
    "2026·丰台·一模·第20题": "仅定位到答案式文字，正式点分布细则仍待深挖。",
    "2026·海淀·期末·第19题": "题头总分与点分布仍未回源核定。",
    "2026·海淀·二模·第18题第2问": "B轴已修，正式点分布仍待PDF p54/p55回源。",
    "2026·顺义·一模·第18题": "法律表述已修，题目总分与闫某/张某/共同价值分配仍待回源。",
}


def locate(row: dict) -> str:
    return (row.get("题目定位/模块") or row.get("题目定位") or "").strip()


def adjudicate(row: dict) -> tuple[str, str]:
    title = locate(row)
    old_status = (row.get("v34状态") or "").strip()
    if title in FIXED and title in SOURCE_RISK:
        return "v35部分实改-仍留源证据风险", FIXED[title] + "；" + SOURCE_RISK[title]
    if title in FIXED:
        return "v35已实改", FIXED[title]
    if title in SOURCE_RISK:
        return "保留回源风险", SOURCE_RISK[title]
    if old_status == "已改":
        return "v34已通过-v35沿用", "复核表已判已改，v35沿用并纳入坏词/渲染回归。"
    if old_status == "原判不成立":
        return "原意见不采纳", "复核表判定原意见不成立，v35不作无源改动。"
    if "AB双轴" in (row.get("维度") or "") and (row.get("原severity") or row.get("严重程度") or "") == "低":
        return "编辑性增益暂缓", "低风险轴线增强建议，未影响学生作答主链；保留给后续教师审阅取舍。"
    return "待后续回源或人工取舍", "本轮未在无源状态下硬改；需结合原卷/细则或教师偏好决定。"


def main() -> None:
    rows = []
    with IN_TSV.open("r", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            status, note = adjudicate(row)
            row["v35处理结论"] = status
            row["v35说明"] = note
            rows.append(row)

    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    by_status = Counter(row["v35处理结论"] for row in rows)
    fixed_titles = sorted(FIXED)
    risk_titles = sorted(SOURCE_RISK)
    lines = [
        "# v35 对 v34 复核意见处理台账",
        "",
        f"- 输入意见：{len(rows)} 条",
        f"- 输出明细：`{OUT_TSV}`",
        "",
        "## 处理结论统计",
        "",
    ]
    for key, count in by_status.most_common():
        lines.append(f"- {key}: {count}")
    lines.extend(["", "## v35 已实改重点", ""])
    for title in fixed_titles:
        lines.append(f"- {title}: {FIXED[title]}")
    lines.extend(["", "## 保留回源风险", ""])
    for title in risk_titles:
        lines.append(f"- {title}: {SOURCE_RISK[title]}")
    lines.extend([
        "",
        "## 本轮原则",
        "",
        "- 法律表述、重复细则、内部抬头、坏词和轴线明显错配直接修。",
        "- 点分布、卷面总分、原卷条号等没有源证据的，不凭空补齐。",
        "- v35 仍需走 Claude Opus 4.8 Max 网页/应用复核和 GPT-5.5 Pro 网页/应用终审；不得用 CLI 冒充终审。",
        "",
    ])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(OUT_TSV)
    print(OUT_MD)


if __name__ == "__main__":
    main()
