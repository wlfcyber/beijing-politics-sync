#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
RUN = ROOT / "10_framework_validation" / "v7_method_first_zero_baseline_pressure_20260521"
ANS = RUN / "student_answers_v7_method_first_zero_baseline_20260521.md"
KEY = RUN / "internal_grading_key_v7_method_first_20260521.csv"
CSV_OUT = RUN / "grading_report_v7_method_first_zero_baseline_20260521.csv"
MD_OUT = RUN / "grading_report_v7_method_first_zero_baseline_20260521.md"
VERDICT = RUN / "V7_METHOD_FIRST_ZERO_BASELINE_VERDICT_20260521.md"

MANUAL = {
    "CC0143_2025_朝阳_一模_19": {
        "status": "PARTIAL",
        "score_note": "能进入消费者欺诈方向，能写知情权、自主选择权、公平交易权；但未稳定写出合同成立不等于有效、违背真实意思表示、消费者权益保护法第五十五条的三倍赔偿/最低赔偿精确句。",
        "patch": "在八门第1门增加消费者欺诈特例句：先写合同成立，再写搭售导致真实意思表示受影响，最后落三倍赔偿。",
    },
    "CC0054_2024_石景山_一模_17": {
        "status": "PASS",
        "score_note": "能跑合同链，写出报价内容具体明确、中标通知送达、合同成立、违约和诚信/绿色价值；对要约邀请不确定但答案主链未偏。",
        "patch": "在合同链前台加一句：公告多半是要约邀请，报价内容具体明确才是要约，中标通知送达是承诺。",
    },
    "CC0373_2026_顺义_一模_18": {
        "status": "PASS",
        "score_note": "能按多主体多请求拆开，闫某平等就业、张某竞业限制均能进入正确方向；材料短导致部分论证略保守。",
        "patch": "保留一人一段、一请求一段；补一句竞业限制题要写夫妻利益一致性/实质关联。",
    },
    "CC0244_2026_东城_期末_18": {
        "status": "PARTIAL",
        "score_note": "能同时写违约、侵权和维权准备；但销售者责任、生产者无过错责任、医疗费/商业损失分流仍不够精确，容易把销售者和生产者责任混在一起。",
        "patch": "在三档归责卡增加无人机/产品缺陷分流表：刘某销售者违约+有过错侵权，生产者产品责任另列，无过错不能随便套销售者。",
    },
    "RECOVER_2025_海淀_二模_18": {
        "status": "PARTIAL",
        "score_note": "能抓商标、在先权利、诚实信用和市场秩序；但因清洁题包没有表格空格，学生无法逐格补全，不能证明表格门已满分可启动。",
        "patch": "必须补回真实笔记表格或在宝典表格门写清：看列名、示例、空格功能；否则该题不能作为表格满分闭环样题。",
    },
    "CC0103_2025_丰台_一模_19": {
        "status": "PASS",
        "score_note": "能先写本案保护技术秘密和惩罚性赔偿，再写创新、竞争秩序、司法示范，价值不再裸奔。",
        "patch": "保持意义价值门，但加一句：典型案例意义题必须先复述本案法律处理。",
    },
    "RECOVER_2026_房山_一模_17_1": {
        "status": "PARTIAL",
        "score_note": "能写 AI 非民事主体、无实际损害、提示义务；但对 AI 输出是否代表公司意思表示仍不稳，未明确承诺不具有法律效力的标准句。",
        "patch": "在 AI 边界门加入三问：AI 是主体吗？公司授权了吗？有实际损害吗？并给固定满分句。",
    },
    "CC0325_2026_石景山_一模_18": {
        "status": "CONDITIONAL_PASS",
        "score_note": "在 ask_text 缺失情况下能主动降级，不假装闭合；行政诉讼举证和建筑物脱落过错推定方向正确，但表格具体格位未闭合。",
        "patch": "保留为待回源保分索引；回源补齐设问和表格格位前不进核心逐题满分示范。",
    },
    "CC0277_2026_房山_二模_18": {
        "status": "CONDITIONAL_PASS",
        "score_note": "能识别 AI 合规风险和哲学转出，法律风险四点基本齐；但因 canonical ask_text 为空，不能证明完整题目闭合。",
        "patch": "保留为待回源保分索引；在保险箱加入‘只答法律小问，哲学另开段或转出’。",
    },
    "CC0040_2024_海淀_一模_19": {
        "status": "PARTIAL",
        "score_note": "能写虚拟数字人视频、未经许可商业使用、影响消除和赔偿；但该题 evidence_level 为 reference_only，不得宣称满分闭合，且著作权/不正当竞争主次仍需教师确认。",
        "patch": "放入普通参考答案练笔容器；学生稿必须明确‘这类题练表达，不做核心细则样题’。",
    },
}


def read_key() -> list[dict[str, str]]:
    with KEY.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main() -> None:
    text = ANS.read_text(encoding="utf-8")
    rows = []
    for key in read_key():
        qid = key["question_id"]
        manual = MANUAL[qid]
        rows.append(
            {
                "sample_no": key["sample_no"],
                "question_id": qid,
                "evidence_level": key["evidence_level"],
                "expected_entry": key["expected_entry"],
                "pass_status": manual["status"],
                "score_note": manual["score_note"],
                "patch_needed": "yes" if manual["status"] != "PASS" or manual["patch"] else "no",
                "patch_suggestion": manual["patch"],
                "known_gate_risk": key["known_gate_risk"],
            }
        )

    with CSV_OUT.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "sample_no",
                "question_id",
                "evidence_level",
                "expected_entry",
                "pass_status",
                "score_note",
                "patch_needed",
                "patch_suggestion",
                "known_gate_risk",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["pass_status"]] = counts.get(row["pass_status"], 0) + 1

    md_rows = "\n".join(
        f"| {r['sample_no']} | `{r['question_id']}` | {r['pass_status']} | {r['score_note']} | {r['patch_suggestion']} |"
        for r in rows
    )
    MD_OUT.write_text(
        f"""# V7 方法先行零基础压力测试严判报告

学生答案文件：`{ANS}`

## 统计

- PASS: {counts.get('PASS', 0)}
- CONDITIONAL_PASS: {counts.get('CONDITIONAL_PASS', 0)}
- PARTIAL: {counts.get('PARTIAL', 0)}
- FAIL: {counts.get('FAIL', 0)}

## 逐题裁定

| 样题 | question_id | 裁定 | 严判理由 | 必修补丁 |
|---|---|---|---|---|
{md_rows}

## 总判断

V7 的“答案产品门”比 V6.9 更能让零基础学生启动：10 题全部没有跑偏到空泛法治或教材目录，说明大方向成立。

但不能封版。当前最硬的三个缺口是：

1. 合同链精确定位还要加“公告/报价/中标通知”的固定判别句。
2. 表格题和 ask_text 缺失题必须回源，否则只能降级为待回源保分索引。
3. AI/虚拟数字人题必须给更明确的边界分流，不然学生会在著作权、不正当竞争、意思表示之间摇摆。
""",
        encoding="utf-8",
    )

    verdict = "CONDITIONAL_PASS_TO_PATCH"
    VERDICT.write_text(
        f"""# V7 方法先行零基础压力测试结论

verdict: `{verdict}`

理由：V7 能让学生启动并避免大方向跑偏，但距离“学生看完稳定满分”还有补丁门槛。必须修补合同精确定位、表格格位、AI 边界、产品责任分流，并把 ask_text 缺失题维持在待回源保险箱。

生成文件：

- `{CSV_OUT}`
- `{MD_OUT}`
""",
        encoding="utf-8",
    )
    print(CSV_OUT)
    print(MD_OUT)
    print(VERDICT)
    print(counts)
    print("student_answer_chars", len(text))


if __name__ == "__main__":
    main()
