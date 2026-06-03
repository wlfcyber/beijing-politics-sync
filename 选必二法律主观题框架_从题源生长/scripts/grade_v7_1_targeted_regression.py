#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
RUN = ROOT / "10_framework_validation" / "v7_method_first_zero_baseline_pressure_20260521"
ANS = RUN / "student_answers_v7_1_targeted_regression_20260521.md"
CSV_OUT = RUN / "grading_report_v7_1_targeted_regression_20260521.csv"
MD_OUT = RUN / "grading_report_v7_1_targeted_regression_20260521.md"
VERDICT = RUN / "V7_1_TARGETED_REGRESSION_VERDICT_20260521.md"

ROWS = [
    {
        "sample": "1",
        "question_id": "CC0143_2025_朝阳_一模_19",
        "status": "PASS",
        "reason": "补丁后学生写出消费合同成立、擅自搭售、不能清楚知悉、无法拒绝、构成欺诈、消费者权益保护法和三倍赔偿，上一轮缺口已修。",
        "residual": "未写最低五百元，但高中评分核心不一定要求；可在句库补一条选写。",
    },
    {
        "sample": "4",
        "question_id": "CC0244_2026_东城_期末_18",
        "status": "PASS",
        "reason": "补丁后能区分销售者过错、违约责任、人身侵权和商业拍摄合同损失，没有乱套生产者无过错责任；维权证据路径清楚。",
        "residual": "若原细则要求生产者无过错责任，本题学生只写销售者路径仍需教师版另补。",
    },
    {
        "sample": "5",
        "question_id": "RECOVER_2025_海淀_二模_18",
        "status": "CONDITIONAL_PASS",
        "reason": "学生已按表格补全纪律降级，并能写在先权利、相近商标、混淆、诚实信用和市场秩序；但因压力包仍无真实空格，不能证明逐格满分。",
        "residual": "必须回源补真实笔记表格空格，之后再做一题回归。",
    },
    {
        "sample": "7",
        "question_id": "RECOVER_2026_房山_一模_17_1",
        "status": "PASS",
        "reason": "补丁后三问有效：AI 非民事主体、输出不当然代表公司真实意思表示、无实际损害，能稳定否定赔偿请求。",
        "residual": "可在教师版补生成式 AI 服务提供者注意义务边界。",
    },
    {
        "sample": "10",
        "question_id": "CC0040_2024_海淀_一模_19",
        "status": "CONDITIONAL_PASS",
        "reason": "学生能写虚拟数字人数字内容成果、未经许可商业使用、误认关联、竞争秩序和创新价值，并明确本题只能练表达。",
        "residual": "reference_only 证据限制仍在，不能进入核心满分闭环。",
    },
]


def main() -> None:
    with CSV_OUT.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["sample", "question_id", "status", "reason", "residual"])
        writer.writeheader()
        writer.writerows(ROWS)

    counts = {}
    for row in ROWS:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    table = "\n".join(
        f"| {r['sample']} | `{r['question_id']}` | {r['status']} | {r['reason']} | {r['residual']} |"
        for r in ROWS
    )
    MD_OUT.write_text(
        f"""# V7.1 定向回归严判报告

学生答案文件：`{ANS}`

## 统计

- PASS: {counts.get('PASS', 0)}
- CONDITIONAL_PASS: {counts.get('CONDITIONAL_PASS', 0)}
- PARTIAL: {counts.get('PARTIAL', 0)}
- FAIL: {counts.get('FAIL', 0)}

## 逐题裁定

| 样题 | question_id | 裁定 | 已修复点 | 残余限制 |
|---|---|---|---|---|
{table}

## 裁定

V7.1 补丁有效。上一轮 5 个 PARTIAL 中，3 个提升为 PASS，2 个因证据等级或题面空格问题维持 CONDITIONAL_PASS。没有新增 FAIL。
""",
        encoding="utf-8",
    )
    VERDICT.write_text(
        f"""# V7.1 定向回归结论

verdict: `CONDITIONAL_PASS_TO_SOURCE_REPAIR_AND_DOCX_DRAFT`

理由：V7.1 已证明能修复学生在消费欺诈、产品责任分流、AI 意思表示边界上的主要失分。剩余不属于框架方法本身，而是源题卡/证据限制：海淀二模表格真实空格未入压力包，海淀一模虚拟数字人题为普通参考答案题。

下一步：

1. 保持 V7.1 作为当前候选学生稿。
2. 对 19 个空设问、CC0223、CC0150、CC0244 做 source-card repair。
3. 生成教师证据说明和 DOCX 草稿时，把普通参考答案题、待回源题明确放入保险箱。
""",
        encoding="utf-8",
    )
    print(CSV_OUT)
    print(MD_OUT)
    print(VERDICT)
    print(counts)


if __name__ == "__main__":
    main()
