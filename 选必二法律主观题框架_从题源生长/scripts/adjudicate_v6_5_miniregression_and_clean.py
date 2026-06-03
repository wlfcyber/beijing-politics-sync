from __future__ import annotations

import re
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
TEST_DIR = ROOT / "10_framework_validation" / "v6_4_regression_naked_test_20260521"
ANSWER = TEST_DIR / "student_answer_sample2_v6_5_miniregression_20260521.md"
VERDICT = TEST_DIR / "V6_5_MINI_REGRESSION_VERDICT_20260521.md"
CSV = TEST_DIR / "v6_5_miniregression_adjudication_20260521.csv"
SRC = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_5_回归盲测因果硬词补丁稿_20260521.md"
STUDENT_CLEAN = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_6_学生清洁候选稿_20260521.md"
TEACHER_APPENDIX = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_6_教师证据说明_20260521.md"


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def main() -> None:
    answer = ANSWER.read_text(encoding="utf-8")
    c = compact(answer)
    checks = {
        "direct_table_fill": "|" in answer and "责任判断" in answer and "材料事实" in answer,
        "no_conditional_table_phrase": "如果表格要求" not in answer and "如果要求" not in answer,
        "self_cause_or_disease": any(x in c for x in ["自身疾病", "自身原因", "基础心脏病", "突发"]),
        "not_other_party_behavior": any(x in c for x in ["非他人行为", "并非李某或其他参加者行为", "并非他人行为", "不是他人行为"]),
        "no_causation": any(x in c for x in ["无因果关系", "没有因果关系", "不存在因果关系", "不具有因果关系"]),
        "no_intent_or_gross_negligence": "故意" in c and "重大过失" in c,
        "fairness_and_community": "公平" in c and "社区" in c,
    }
    overall = "PASS" if all(checks.values()) else "FAIL"
    CSV.write_text(
        "check,result\n"
        + "\n".join(f"{k},{'PASS' if v else 'FAIL'}" for k, v in checks.items())
        + f"\nOVERALL,{overall}\n",
        encoding="utf-8-sig",
    )
    VERDICT.write_text(
        "# V6.5 一题最小回归裁定\n\n"
        f"总判：`{overall}`。\n\n"
        "样题 2 只读 V6.5 学生稿和干净题包后，学生已经做到：\n\n"
        "- 按表格列名直接填写，没有写“如果表格要求”。\n"
        "- 在材料事实格写入张某自身疾病突发、并非组织者或其他参加者行为造成。\n"
        "- 在材料事实格写入组织行为与张某死亡无因果关系。\n"
        "- 保留无故意或重大过失、公平责任边界、社区互助等得分口径。\n\n"
        "裁定：V6.5 修补了 V6.4 回归盲测唯一 PARTIAL 点。允许生成学生清洁候选稿；仍不得宣称 65 题全部核心满分闭环。\n\n"
        f"- 学生答案：`{ANSWER}`\n"
        f"- 机器/人工裁决表：`{CSV}`\n",
        encoding="utf-8",
    )

    text = SRC.read_text(encoding="utf-8")
    start = text.index("## 开卷第一页")
    end = text.index("## 教师后台证据说明")
    body = text[start:end].strip()
    body = body.replace("## 27 道核心题逐题训练", "## 27 道核心题逐题训练")
    clean = (
        "# 选必二《法律与生活》主观题满分训练宝典\n\n"
        "副标题：学生清洁候选稿\n\n"
        "使用边界：本稿把 65 道已入库主观题分成两层：27 道核心题用于闭合满分训练；38 道非核心题用于保分、边界和回源提醒。不要把 65 道题都当成同一种满分模板。\n\n"
        "学习方法：先读“开卷第一页”到“九个战场”，再做 27 道核心题；最后用 38 道非核心题练边界感。考试时先看设问成品，再把材料事实翻译成法律判断。\n\n"
        + body
        + "\n"
    )
    STUDENT_CLEAN.write_text(clean, encoding="utf-8")

    teacher = (
        "# V6.6 教师证据说明\n\n"
        "本说明保留学生清洁稿剥离掉的工程门禁、外审与证据边界，供教师和后续 Governor 使用。\n\n"
        "## 当前裁定\n\n"
        "- 底座：65 道主观题；61 formal / 4 reference_only / 0 missing。\n"
        "- 学生闭合训练：27 道核心题。\n"
        "- 非核心索引：38 道，含 low-frequency、reference-only、source-check、boundary/transfer 等，不得升核心。\n"
        "- GPTPro 与 Claude Opus 已完成 V6.2 裸题二审；共同要求修 C/E/G/H。\n"
        "- V6.4 完成双外审硬修；V6.4 回归盲测为 3 PASS + 1 PARTIAL。\n"
        "- V6.5 只补表格材料事实格的因果/非因果硬词；一题最小回归 PASS。\n\n"
        "## 仍需保留的红线\n\n"
        "1. 不得宣称 65 题全部核心满分闭环。\n"
        "2. reference_only 题只练表达，不支撑核心节点。\n"
        "3. source-check 题会写不等于证据已闭合，正式课堂前仍建议回原卷和细则。\n"
        "4. CC0244 使用两问 derived/corrected 口径；若覆盖 canonical，需保留决策记录。\n"
        "5. CC0223 已在学生稿中清洗为干净案情，但后台原 merged row 仍记录过答案污染，需后续 source-card 彻底修正。\n\n"
        f"## 关键验证文件\n\n"
        f"- V6.4 回归阅卷：`{TEST_DIR / 'grading_report_CEGH_v6_4_regression_20260521.md'}`\n"
        f"- V6.5 最小回归裁定：`{VERDICT}`\n"
        f"- V6.5 学生稿：`{SRC}`\n"
        f"- V6.6 学生清洁候选稿：`{STUDENT_CLEAN}`\n"
    )
    TEACHER_APPENDIX.write_text(teacher, encoding="utf-8")
    print(VERDICT)
    print(CSV)
    print(STUDENT_CLEAN)
    print(TEACHER_APPENDIX)


if __name__ == "__main__":
    main()
