#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
PACKET = ROOT / "05_reasoner_packets" / "v7_method_learning_batched_rebuild_20260521"
BATCH_DIR = PACKET / "batches"
OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分宝典_v7_1_压测补丁候选稿_20260521.md"
REPORT = ROOT / "12_final_baodian" / "V7_1_PRESSURE_PATCH_BAODIAN_BUILD_REPORT_20260521.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def clean(text: str | None, limit: int | None = None) -> str:
    s = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    s = "\n".join(line.rstrip() for line in s.splitlines())
    if limit and len(s) > limit:
        return s[:limit].rstrip() + "……"
    return s


def bullet_lines(text: str, prefix: str = "- ") -> str:
    text = clean(text)
    if not text:
        return prefix + "待回源补齐"
    parts = [p.strip(" ；;。\n") for p in text.replace("；", "\n").replace("。", "\n").split("\n")]
    parts = [p for p in parts if p]
    return "\n".join(prefix + p for p in parts[:8])


def new_entry(row: dict[str, str]) -> str:
    qid = row.get("question_id", "")
    batch = row.get("batch_id", "")
    ask = row.get("ask_text", "")
    if "BATCH_02" in batch:
        if "表" in ask or "补充" in ask or "划线" in ask:
            return "表格补全型：先看列名和示例，一格一句"
        if "起诉状" in ask:
            return "维权建议型：先写请求，再写事实理由和证据"
        if "避免" in ask:
            return "预防建议型：先找问题根源，再写可操作做法"
        return "维权/程序型：请求 + 证据 + 路径"
    if "BATCH_03" in batch:
        if "AI" in ask or "人工智能" in ask:
            return "AI 边界型：先排主体和意思表示，再看过错、损害、因果"
        if "意义" in ask or "价值" in ask or "典型" in ask:
            return "意义价值型：先写本案处理，再写价值"
        if "评析" in ask:
            return "评析型：逐主体分别表态"
        return "创新竞争型：保护对象 + 越界行为 + 责任/价值"
    if qid in {"CC0143_2025_朝阳_一模_19", "CC0200_2025_西城_二模_18", "CC0373_2026_顺义_一模_18"}:
        return "判断型：先表态，再一诉求一争点"
    if qid in {"CC0054_2024_石景山_一模_17", "RECOVER_2026_朝阳_期末_18_1"}:
        return "理由依据型：合同成立有效链"
    if qid == "CC0025_2024_朝阳_二模_17":
        return "理由 + 意义型：三从属性逐条嵌材料，再写劳动价值"
    return "实体判断型：先定争点，再走责任链，价值只作尾句"


def clean_student_judgment(text: str) -> str:
    s = clean(text)
    if "先判：" in s:
        s = s.split("先判：", 1)[1].strip()
    s = re.sub(r"主卡=[^；;。]*[；;。]?", "", s)
    s = re.sub(r"辅卡=[^；;。]*[；;。]?", "", s)
    s = s.replace("分关系·定责任", "定争点并走责任链")
    s = s.replace("推价值", "价值尾句")
    s = s.replace("排维权步骤", "请求证据路径")
    s = s.replace("一格一答", "表格逐格作答")
    s = s.replace("认产权·抓侵权", "认保护对象并抓越界行为")
    s = s.replace("划风险边界", "划清法律边界")
    return s.strip(" ；;。") + ("。" if s and not s.endswith(("。", "！", "？")) else "")


def strip_internal_id(text: str) -> str:
    return re.sub(r"（[A-Z0-9_]+(?:_[^）]*)?）", "", text or "").strip()


def student_category(text: str, evidence: str = "") -> str:
    s = clean(text)
    replacements = {
        "source_check_pending": "设问需教师确认",
        "SOURCE-CHECK": "设问需教师确认",
        "reference_only": "普通参考答案练笔",
        "boundary": "综合边界",
        "transfer": "转出本书",
    }
    for old, new in replacements.items():
        s = s.replace(old, new)
    if evidence == "reference_only" and "普通参考答案" not in s:
        s = "普通参考答案练笔"
    return s or "保分练习"


def question_block(row: dict[str, str]) -> str:
    qid = row["question_id"]
    title = f"{row.get('year','')} {row.get('district','')} {row.get('exam_stage','')} 第{row.get('question_no','')}题"
    ask = clean(row.get("ask_text"), 300)
    trigger = clean(row.get("material_trigger"), 450)
    judgment = clean_student_judgment(row.get("minimum_judgment") or row.get("student_first_judgment_v5_5"))
    keywords = clean(row.get("must_have_keywords"), 350)
    atoms = clean(row.get("clean_rubric_atom_ids"), 450)
    sentence_bank = clean(row.get("full_score_sentence_bank"), 900)
    answer = clean(row.get("clean_exam_answer") or row.get("complete_answer_generated"), 1200)
    cautions = clean(row.get("rewrite_cautions"), 500)
    entry = new_entry(row)
    return f"""### {title}

**框架入口**：{entry or "按设问成品先分流"}

**设问**：{ask or "待回源补齐真实设问；本题暂按细则成品训练。"}

**第一判断**：{judgment or "先判断材料中的主体、行为、争点与答案成品。"}

**材料触发**：
{bullet_lines(trigger)}

**必写关键词**：
{bullet_lines(keywords)}

**对应细则原子**：`{atoms or "待回源确认"}`

**满分句库**：
{sentence_bank or "待按干净细则补写。"}

**考场版答案**：

{answer or "本题暂不写完整答案，先进入教师回源清单。"}

**易错提醒**：
{bullet_lines(cautions)}
"""


def container_block(row: dict[str, str]) -> str:
    qid = row["question_id"]
    title = strip_internal_id(row.get("title_with_id") or row.get("source_label") or qid)
    category = student_category(row.get("student_category") or row.get("audit_category") or "容器题", row.get("evidence_level") or "")
    evidence = row.get("evidence_level") or "unknown"
    reliability = student_category(row.get("reliability") or "", evidence)
    lines = [row.get("minimum_sentence_1", ""), row.get("minimum_sentence_2", ""), row.get("minimum_sentence_3", "")]
    lines = [clean(x) for x in lines if clean(x)]
    do_not = clean(row.get("do_not_write"), 500)
    memo = clean(row.get("memorization_status"), 300)
    return f"""### {title}

**学习定位**：{category}

**使用提醒**：{reliability or "先按最低可写句保分，不升为核心模板。"}

**最低可写句**：
{chr(10).join(f"{i+1}. {line}" for i, line in enumerate(lines)) if lines else "1. 待回源补齐。"}

**不要这样写**：{do_not or "待补。"}

**记忆定位**：{memo or "待补。"}
"""


def main() -> None:
    b1 = read_csv(BATCH_DIR / "BATCH_01_HIGH_FREQ_CORE_JUDGMENT.csv")
    b2 = read_csv(BATCH_DIR / "BATCH_02_PROCEDURE_TABLE.csv")
    b3 = read_csv(BATCH_DIR / "BATCH_03_INNOVATION_AI_VALUE.csv")
    b4 = read_csv(BATCH_DIR / "BATCH_04_NON_CORE_OPEN_CONTAINER.csv")

    core_rows = b1 + b2 + b3
    core_sections = "\n".join(question_block(r) for r in core_rows)
    container_sections = "\n".join(container_block(r) for r in b4)

    md = f"""# 选必二《法律与生活》主观题满分宝典 V7.1（压测补丁候选稿）

> 本稿不是 V6.9 修补稿，而是按“先学先前优秀框架方法 -> 再分批吃 65 道法律题 -> 再重建学生可启动框架”的路线生成，并根据零基础压力测试修补后的 V7.1 候选稿。  
> 已并入 Claude Opus 与 GPTPro 的方法学习、分批处理和最终建议；少数只有普通参考答案的题只作练笔，不支撑核心满分闭环。

## 第一部分 这本书到底在考什么

选必二法律主观题不是让你背一堆法条，也不是让你写“法治中国、公平正义”的大作文。

它本质上只考一件事：

```text
把材料里的生活冲突，翻译成法律判断，再写成细则给分句。
```

所以你每次看到题，先按这个顺序动笔：

```text
看设问要我交什么成品
圈主体：谁和谁
抓行为：谁做了什么
定争点：到底争什么
套规则：合同、侵权、不正当竞争、程序、价值还是边界
落成品：判断、理由、表格、建议、价值或转出
```

## 第二部分 30 秒八个答案产品门

| 门 | 看到什么词 | 第一笔 |
|---|---|---|
| 门 1 判断表态 | 能否支持、是否有效、是否构成、判决结果 | `XX 的诉求应/不应得到支持，因为……` |
| 门 2 合同链 | 合同成立、合同效力、履行责任 | `先跑要约 -> 承诺 -> 成立/有效 -> 履行或违约。` |
| 门 3 多主体多请求 | 两个主体、两个诉求、几个案例 | `对 A 先表态；对 B 另起一段。` |
| 门 4 证据请求路径 | 怎么办、维权、起诉状、诉讼请求、调解 | `先写请求，再写证据，最后写路径。` |
| 门 5 表格补全 | 完成表格、补全笔记、划线处 | `先看列名，再看示例，一格一句。` |
| 门 6 意义价值 | 意义、价值、作用、典型案例、定分止争 | `本案通过……处理，保护了……` |
| 门 7 创新与 AI 边界 | 技术秘密、AI、算法、生成式、数字员工 | `先判保护对象、主体资格、意思表示或责任边界。` |
| 门 8 非核心保险箱 | 涉外、治理、逻辑、哲学、普通参考答案题、设问需教师确认题 | `先降级，不把它硬写成核心母题。` |

## 第三部分 三大责任逻辑链

### 1. 违约链

```text
合同成立 -> 合同有效 -> 未按约履行 -> 违约责任
```

满分句：

> 本案中，XX 的表示内容具体确定，属于要约；XX 作出承诺后，双方合同成立。合同主体适格、意思表示真实、内容不违反法律法规强制性规定，合同有效。XX 未按合同约定履行义务，构成违约，应承担继续履行、赔偿损失等违约责任。

合同题最容易卡在三个词：

| 材料动作 | 法律定位 | 考场句 |
|---|---|---|
| 发布公告、比选公告、招标公告 | 通常先看作要约邀请 | 乙公司发布比选公告，是希望他人向自己发出报价。 |
| 报价内容具体明确，写明标的、数量、价款、违约后果 | 要约 | 甲公司的报价内容具体明确，属于要约。 |
| 中标通知、同意报价、立即付款、确认订单 | 承诺 | 中标通知送达或付款确认时，双方意思表示一致，合同成立。 |

消费者欺诈题也会先出现合同，但不能停在合同成立：

> 平台出票、付款成功，说明消费合同成立；但经营者隐蔽搭售，使消费者不能清楚知悉费用并无法拒绝支付，影响消费者真实意思表示，构成欺诈。经营者提供商品或服务有欺诈行为的，应按消费者权益保护法承担增加赔偿责任，可支持三倍赔偿等请求。

### 2. 侵权链

```text
权利受保护 -> 行为越界 -> 造成损害 -> 因果关系 -> 按归责档承担责任
```

满分句：

> XX 享有……权利。材料中，XX 实施了……行为，超出合理限度，损害了……权益，与损害结果之间存在因果关系，应依法承担侵权责任。

### 3. 不正当竞争 / 知识产权链

```text
保护对象或竞争关系 -> 不正当行为 -> 损害权利或竞争秩序 -> 责任 + 创新价值
```

满分句：

> XX 与 XX 存在竞争关系。材料中，XX 通过……方式实施混淆、虚假宣传、商业诋毁或侵犯商业秘密等行为，扰乱市场竞争秩序，损害经营者合法权益，构成不正当竞争，应承担相应责任。

## 第四部分 三档归责卡

| 档位 | 典型场景 | 不能写错 |
|---|---|---|
| 合同违约档 | 要约、承诺、成立、有效、履行不合约定 | 不要用侵权四要件分析违约 |
| 一般过错侵权档 | 销售者、隐私权、名誉权、一般损害 | 不要直接写无过错 |
| 过错推定 / 无过错档 | 生产者产品责任、饲养动物、建筑物坠落、个人信息 | 不要写“无过错推定” |

硬背：

```text
销售者不是生产者。
产品缺陷找生产者，重点写无过错责任。
销售者有过错才走销售者责任。
建筑物坠落、个人信息等可能走过错推定。
```

产品责任题必须再分一刀：

| 对象 | 先写什么 | 不能乱写 |
|---|---|---|
| 销售者 | 是否交付不合格商品、是否有过错、是否违约或侵权 | 不能直接把销售者写成无过错责任 |
| 生产者 | 产品是否存在缺陷、缺陷是否造成损害 | 产品缺陷造成他人人身财产损害时，生产者承担无过错侵权责任 |
| 同一案件有违约又有侵权 | 医疗费、人身损害多走侵权；合同目的损失多走违约 | 不要把所有损失塞进同一条责任链 |

## 第五部分 材料翻译三步

| 材料事实 | 法律语言 | 得分句 |
|---|---|---|
| 报价内容具体确定 | 要约 | 甲公司的报价内容具体确定，属于要约。 |
| 中标通知送达 | 承诺、合同成立 | 中标通知书送达，双方合同成立。 |
| 派单、奖惩、签到 | 从属性 | 平台对劳动者管理和奖惩，体现人格从属性。 |
| 擅自搭售、不能知悉、无法拒绝 | 欺诈 | 经营者擅自搭售，消费者不能清楚知悉并无法拒绝，构成欺诈。 |
| 拍到日常出行规律 | 隐私权 | 摄像头拍摄日常出行规律及其他动态信息，侵犯隐私权。 |
| 捏造事实贬损对手 | 商业诋毁 | 该行为损害竞争对手商业信誉，构成商业诋毁。 |
| AI 生成赔偿承诺 | AI 不是民事主体 | AI 不具备民事主体资格，不能独立作出有效意思表示。 |

三条铁律：

1. 材料给几个条件，就译几个条件。
2. 细则要材料原词，就带材料原词。
3. 法律名称要准，欺诈不要写成诈骗。

## 第六部分 表格补全三看

表格题不是小作文。你只做三件事：

```text
看列名 -> 看示例 -> 看空格功能
```

| 题面给你的东西 | 你该做什么 |
|---|---|
| 列名问“举证责任分配方式” | 只写谁承担证明责任 |
| 列名问“理由” | 只写为什么这样分配，不展开成整段价值 |
| 示例已经写了一个案例 | 模仿示例长度和句式 |
| 题包或训练材料缺真实空格 | 先降级为待回源，不假装满分闭合 |

表格题保命句：

> 本格只回答本格功能。若格子问“分配方式”，就写谁举证；若格子问“理由”，再写诉讼类型、证明难度、法律特别规定或公平对抗。

## 第七部分 价值四层卡

价值句永远不要裸奔。

```text
先写本案怎样处理，再推出价值。
```

| 层次 | 可写句 |
|---|---|
| 当事人权利 | 本案通过……处理，维护了……合法权益。 |
| 行业秩序 | 有利于规范……秩序，营造公平竞争/交易环境。 |
| 司法审判 | 为同类案件提供裁判示范，提高司法公信力。 |
| 法治社会 | 引导公民依法办事，增强法治信仰。 |

别裸写：

```text
维护公平正义。
推动法治中国建设。
弘扬社会主义核心价值观。
```

要写也必须前面有本案铺垫。

## 第八部分 AI 与虚拟数字人三问

看到 AI、算法、数字员工、虚拟数字人，先不要急着喊“新技术保护”。先问三句：

```text
它是不是民事主体？
公司有没有授权或真实意思表示？
有没有实际损害、越界使用或竞争秩序损害？
```

四种常见落点：

| 材料信号 | 法律落点 | 满分句 |
|---|---|---|
| AI 自己生成赔偿承诺 | AI 不是民事主体，不能独立作有效意思表示 | AI 不具备民事主体资格，其输出不能当然等同于公司真实有效的承诺。 |
| AI 内容错误但无实际损害 | 侵权责任不成立或责任不足 | 原告未证明实际损害，侵权责任链不完整。 |
| 数字员工生成虚假负面文章 | 商业诋毁、名誉权风险 | 经营者利用数字员工发布虚假负面信息，可能损害他人商业信誉并构成商业诋毁。 |
| 未经许可使用虚拟数字人视频或图案 | 著作权/不正当竞争边界 | 未经许可商业使用他人数字内容成果，可能侵犯著作权并扰乱公平竞争秩序。 |

## 第九部分 五类保险箱

| 保险箱 | 你该怎么用 |
|---|---|
| 低频规则容器 | 写少见规则 + 材料路径 + 一句价值，保分，不升母题。 |
| 待回源保分索引 | 只在设问匹配时用最低句，未回源前不进核心。 |
| 综合边界 | 法律层写最低句，其他模块另开段。 |
| 转出本书 | 主任务是逻辑/哲学就转出，不硬套法律模板。 |
| 普通参考答案练笔 | 只练表达，不当正式细则，不支撑核心满分句。 |

## 第十部分 一页总流程

```text
生活冲突 -> 答案产品门 -> 主体行为争点 -> 法律规则 -> 得分句 -> 必要价值尾句。
```

## 第十一部分 27 个核心题逐题运行

{core_sections}

## 第十二部分 38 个容器题索引

{container_sections}

## 第十三部分 使用纪律

1. 先分成品，不先背目录。
2. 先定争点，不先铺价值。
3. 先翻材料，不空抄法条。
4. 多主体、多案例、多诉求必须拆开。
5. 表格题看列名和示例，不写长作文。
6. 普通参考答案题只练表达，不写入核心满分闭环。
7. 没有真实设问的题，最终宝典前必须回源补齐。
"""

    OUT.write_text(md, encoding="utf-8")
    report = f"""# V7 方法先行宝典候选稿生成报告

- output: `{OUT}`
- core_question_sections: {len(core_rows)}
- container_question_sections: {len(b4)}
- status: v7_1_candidate_after_zero_baseline_pressure_patch
- pressure_test: PASS=3; CONDITIONAL_PASS=2; PARTIAL=5; FAIL=0
- note: generated from split V7 batch packets, merged with captured GPTPro final proposal plus Claude Opus V7 proposal, then patched from zero-baseline pressure-test failures. This is still not final until source-card repair and full artifact QA pass.
"""
    REPORT.write_text(report, encoding="utf-8")
    print(OUT)
    print(REPORT)


if __name__ == "__main__":
    main()
