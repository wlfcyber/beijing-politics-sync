from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "v14_3_gpt_patch_framework_baodian"
OUT = ROOT / "v14_4_claude_student_patch_framework_baodian"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def replace_section(text: str, heading: str, next_heading: str, replacement: str) -> str:
    pattern = re.compile(rf"{re.escape(heading)}.*?(?=\n{re.escape(next_heading)})", re.S)
    if not pattern.search(text):
        raise RuntimeError(f"section not found: {heading}")
    return pattern.sub(replacement.rstrip() + "\n", text, count=1)


NEW_0B = """## 0B. C 轴：拆成两类，别再混

学生试读暴露了一个真问题：v14.3 把“规则触发”和“写法切换”都叫 C 轴，学生会不知道 C 到底是背规则还是换写法。v14.4 固定成两类：

- `C-rule`：看到特殊材料，必须启动一条具体法律规则。
- `C-write`：看到特殊设问，必须改变答案组织方式。

### C-rule：看到这些词，先补规则

| C-rule | 看到什么就启动 | 必写规则骨架 |
|---|---|---|
| C1 行为能力与追认 | 未成年人、老人、金额巨大、监护人不知情 | 年龄/智力/金额是否相适应 -> 是否同意或追认 -> 行为效力 -> 返还与过错分担。 |
| C2 劳动三从属性 | 平台派单、考勤、奖惩、结算、组织管理 | 不看协议名称，看人格从属性、经济从属性、组织从属性。 |
| C3 技术秘密三性 | 图纸、配方、数据、算法、研发资料 | 秘密性 -> 价值性 -> 保密措施 -> 不正当获取/使用 -> 责任。 |
| C4 欺诈与惩罚性赔偿 | 隐瞒、误导、虚假宣传、搭售、明知仍售 | 先证成欺诈或恶意，再写惩罚性赔偿；事实不足时只写退费或普通赔偿。 |
| C5 好意同乘 | 免费搭车、帮忙接送、非营运 | 无偿非营运 -> 驾驶人无故意/重大过失可减轻 -> 受害人过错相抵 -> 但不免责。 |
| C6 竞业限制 | 离职、竞业、补偿、商业秘密 | 劳动者就业权、单位秘密保护、限制范围、期限和补偿是否适度。 |
| C7 举证责任 | 举证、证明、谁承担、事实清楚证据充分 | 民事谁主张谁举证；行政诉讼行政机关证明行政行为合法；刑事公诉由检察机关证明；特殊侵权可倒置。 |

### C-write：看到这些设问，立刻换写法

| C-write | 看到什么就启动 | 写作动作 |
|---|---|---|
| C8 多主体分责 | 平台、监护人、本人、经营者、第三人 | 一个主体一条链：义务 -> 行为 -> 过错/履行 -> 责任。 |
| C9 维权路径 | 维权、调解、诉讼、建议、怎么办 | 争议焦点 -> 证据 -> 路径 -> 请求，不能只写“依法维权”。 |
| C10 表格 | 表格、补全、比较、三案 | 按表头答；看不到表头时默认“材料事实 -> 法律规则 -> 裁判要点”。 |
| C11 参照示范 | 参照案例一、仿照示例、任选其一 | 先抽出示范的四要素，再平移到本案。 |

用法只有一句：A 轴定大类，C 轴补特殊规则或换写法，C 不能取代 A。"""


NEW_0C = """## 0C. 混合设问拆分规则：先拆动词，再排顺序

题干有两个动词，就拆两个 B 动作。不要用一个标签吞全题。

| 设问组合 | 排序 | 答案形状 |
|---|---|---|
| 理由 + 意义 | B2 -> B5 | 先写为什么这样判，再写该判决保护了谁、规范了什么秩序。 |
| 评析 + 建议 | B4 -> B6 | 先评合理处和越界处，再给证据、协商、调解、诉讼或整改方案。 |
| 补全 + 任选展开 | B7 -> B6 | 先短句补全所有空，再任选一项写权利、侵害、证据、路径、请求。 |
| 责任 + 维权 | B2/B3 -> B6 | 先定谁担责或诉求是否支持，再写保存什么证据、走什么路、提什么请求。 |
| 判决 + 启示 | B2 -> B5 | 先写裁判依据，再把启示落到诚信、合规、保护对象或治理秩序。 |
| 案例分析 + 表格 | B2/B4 -> B1 | 先想清规则链，再压成表格列，不写散文。 |
| 法理依据 + 现实意义 | B2 -> B5 | 先写规则根据和事实适用，再写现实层面的行为引导。 |
| 问题识别 + 解决方案 | B7 -> B6 | 先叫准法律问题，再给具体处理路径。 |"""


NEW_0D = """## 0D. 反向筛查

落笔前用这十一条排错：

1. 看见法院，不等于写公正司法；先看实体法律关系。
2. 看见平台，不等于劳动关系；先查三从属性。
3. 看见消费者，不等于三倍赔偿；先查欺诈事实。
4. 看见未成年人消费，先查行为能力和追认。
5. 看见监控门铃，不能只写物权；同步查隐私、个人信息和相邻安宁。
6. 看见技术资料，先查秘密性、价值性、保密措施。
7. 看见好意同乘，减责不等于免责。
8. 看见表格，按原表头；看不见表头就用事实、规则、裁判要点三列。
9. 看见两个动词，先拆小问再落笔。
10. 看见意义，必须从本案具体规则推出，不能空喊价值。
11. 看见审批、公示、消防、勘查，不自动进 A10；它们多半是程序事实或证据，主入口仍看实体争议。"""


STUDENT_PATCH_BLOCK = """## 0E. A 轴入口决策树：5 秒内先别跑偏

```text
先问：题目核心是不是“行为有没有效”？
  是 -> 未成年/追认/意思表示/代理/时效直接决定诉求 -> A1 主脊柱
  否 -> 继续

有没有隐私、个人信息、名誉、肖像、生命健康？
  是 -> A2；若同时有门铃、采光、通行，再加 A3 副入口
  否 -> 继续

是不是房屋、车位、共有部分、相邻采光通行安全？
  是 -> A3；审批公示勘查只是证据，不抢 A10
  否 -> 继续

是不是买卖、服务、交付、质量、违约、损失？
  是 -> A4；若瑕疵又造成伤害，再叠 A6
  否 -> 继续

是不是作品、商标、商业秘密、数据抓取、虚假竞争？
  是 -> A5
  否 -> 继续

是不是人身财产损害、安全保障、产品致损、公共场所？
  是 -> A6
  否 -> 继续

是不是夫妻、亲子、赡养、扶养、继承、遗嘱？
  是 -> A7
  否 -> 继续

是不是入职、试用、解除、工资社保、竞业限制？
  是 -> A8
  否 -> 继续

是不是生活消费、知情权、公平交易、格式条款、欺诈？
  是 -> A9；但未成年大额消费先让 A1 定效力
  否 -> 继续

只问证据、调解、仲裁、诉讼、举证、起诉状？
  是 -> A10
```

### A1 什么时候是主脊柱

满足下面任意两条，并且“效力”直接决定诉求，A1 就是主脊柱：

1. 主体存在年龄、智力、精神状态、代理、意思表示或追认问题。
2. 金额、风险或行为后果明显超出该主体的一般判断能力。
3. 监护人、法定代理人或相对人是否同意/追认会直接改变结论。
4. 题目问的是返还、撤销、有效/无效、责任分担或诉求是否支持。

口诀：效力不清，先 A1；场景入口只补充，不抢主脊柱。

## 0F. 分值和篇幅映射

| 分值 | 建议结构 | 句数 | 不扣分重点 |
|---|---|---:|---|
| 4 分 | 结论 + 2 条理由 | 3-4 句 | 叫准入口，材料事实必须进规则。 |
| 6 分 | 结论 + 3 条规则事实链 | 4-5 句 | 每条链都有“规则+事实+结论”。 |
| 8 分 | 主入口 3 条 + 副入口/价值 1 条 | 5-7 句 | 有副入口时必须补边界，不要只写大标题。 |
| 10 分 | 分层或分主体作答 | 7-9 句 | 多主体、多请求、多阶段分开写。 |
| 表格题 | 一行一案或一行一要点 | 按表头 | 不写长段散文，列名决定内容。 |

考场上宁可少喊价值，也不能少写材料事实。价值句只在题目问意义、启示、价值时出现。

## 0G. 参照示范题写法

看到“参照案例一”“仿照示例”“任选其一展开”，按四步：

1. 先抽示范答案的四个格子：主体、权利义务、关键事实、结论/责任。
2. 再把本案材料逐格替换，不能照抄示范事实。
3. 若示范是表格，就保持同样列名；若示范是段落，就保持同样顺序。
4. 最后一格必须回到本案请求：支持、不支持、如何处理、走什么路径。

## 0H. 五张必背细节规则卡

### 1. 举证责任卡

- 民事诉讼：一般是谁主张谁举证。
- 行政诉讼：被告行政机关证明行政行为合法。
- 刑事公诉：检察机关承担证明被告人有罪的责任，被告人不负证明自己无罪的责任。
- 特殊侵权：法律规定时可举证责任倒置，例如建筑物、搁置物、悬挂物脱落坠落致害，所有人、管理人或使用人要证明自己没有过错。

### 2. 好意同乘卡

无偿、非营运搭乘中，驾驶人不是故意或重大过失造成损害的，可以减轻赔偿责任；但“减轻”不是“免除”。受害人未系安全带等自身过错，也要影响责任分担。

### 3. 惩罚性赔偿卡

消费者题先证欺诈：隐瞒、误导、虚假宣传、明知仍售等事实足够，才写惩罚性赔偿。知识产权或商业秘密题要看主观恶意、情节严重和法定适用条件；事实不足时写停止侵害、赔偿损失、消除影响，不硬写三倍或惩罚性赔偿。

### 4. 未成年打赏/大额消费卡

限制民事行为能力人实施与年龄、智力、经济认知明显不相适应的大额打赏或消费，未经监护人同意或追认的，行为效力不成立或不发生相应效力。返还时要分平台审核义务、未成年人绕限行为、监护人监管义务，不要只写平台全责。

### 5. 可预见商业损失卡

合同违约导致商业损失时，支持条件是：订约或履行前已告知特殊用途，损失有证据，违约与损失有因果关系，金额在可预见范围内。缺一项就写“需进一步证明”，不要直接全额支持。
"""


def patch_framework(text: str) -> str:
    text = text.replace("v14.3", "v14.4")
    text = text.replace("学生盲测后补上的十四条硬规则", "学生盲测后补上的十六条硬规则")
    text = text.replace("下面十四条", "下面十六条")
    text = replace_section(text, "## 0B. C 轴：题内开关，不增加大入口", "## 0C. 混合设问拆分规则", NEW_0B)
    text = replace_section(text, "## 0C. 混合设问拆分规则", "## 0D. 反向筛查", NEW_0C)
    text = re.sub(
        r"## 0D\. 反向筛查.*?\n\n所以所有题都按五步走：",
        NEW_0D + "\n\n所以所有题都按五步走：",
        text,
        count=1,
        flags=re.S,
    )
    marker = "## 1. 先会总流程，再背 A/B"
    if STUDENT_PATCH_BLOCK not in text:
        text = text.replace(marker, STUDENT_PATCH_BLOCK + "\n\n" + marker, 1)
    text = re.sub(
        r"本批 42 道锁定核心题的 A 轴分布：.*?\n\n",
        "学生不用背题量统计。A 轴只解决一个问题：先把生活冲突放进正确法律关系，防止整题跑偏。\n\n",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"本批 42 道锁定核心题的 B 轴分布：.*?\n\n",
        "学生不用背 B 轴题量统计。B 轴只解决一个问题：设问让我交出什么形状的答案。\n\n",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(r"（\d+题）", "", text)
    return text


def patch_common(text: str) -> str:
    return text.replace("v14.3", "v14.4").replace("v14_3", "v14_4")


def governance() -> str:
    return """# 05 GPT 与 Claude 补丁落实及治理边界 v14.4

## Real GPT Pro Gate

Status: `GPT_REVIEW_PASS_AFTER_PATCH_CAPTURED_AS_PATCH_SOURCE`

Evidence:

- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_PROMPT_v14_2_with_prior_framework.md`
- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md`

Boundary:

- GPT Pro did run in the user's Chrome Pro session and read the five uploaded files.
- Full raw transcript export failed after long output; the capture file records the visible verdict and patch list.
- v14.3 implemented GPT's minimum patch list.

## Real Claude Student Simulation Gate

Status: `CLAUDE_STUDENT_PASS_AFTER_PATCH_CAPTURED`

Evidence:

- `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_3_20260524.md`

Boundary:

- Claude Opus 4.7 Adaptive ran as a zero-baseline smart student.
- It saw only the v14.3 framework and 8-question blind test pack, not the 42-question answer cards.
- It judged v14.3 could prevent major direction errors but still lacked enough student-facing rule detail for high marks.

## v14.4 Patch List

1. Split C axis into `C-rule` and `C-write`.
2. Added A-axis decision tree.
3. Added explicit A1 main-spine threshold.
4. Expanded mixed-question combinations from 4 to 8.
5. Added reverse-screening rule for approval/public notice/inspection as evidence rather than A10.
6. Added score-to-length map.
7. Added reference-example writing method.
8. Added five legal-detail cards: burden of proof, good-faith ride, punitive damages, minor tipping/large consumption, foreseeable business loss.
9. Removed student-facing 42-question distribution noise from the main framework.

## Remaining Boundary

v14.4 is a Markdown candidate after GPT and Claude patch application. It is not a DOCX/PDF delivery. It still should be run through a second Claude zero-baseline student simulation before claiming final external pass.
"""


def governor() -> str:
    return """# 06 Final Governor Checklist v14.4

## Verdict

`MARKDOWN_FRAMEWORK_AND_42_QUESTION_BAODIAN_GPT_AND_CLAUDE_PATCH_APPLIED_PENDING_SECOND_CLAUDE_SIM_AND_DOCX_PDF`

## Gate Table

| Gate | Status | Evidence |
|---|---|---|
| v14.4 framework chapter exists | PASS | `01_先背这套_法律主观题不扣分框架_v14_4.md` |
| v14.4 42-question analysis exists | PASS | `02_42题按框架拆解与解析_v14_4.md` |
| Combined v14.4 baodian exists | PASS | `选必二法律与生活_法律宝典_v14_4_Claude学生补丁版.md` |
| GPT Pro review used | PASS_WITH_CAPTURE_LIMIT | `external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md` |
| Claude student simulation on v14.3 used | PASS_AFTER_PATCH | `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_3_20260524.md` |
| Claude-required patches applied | PASS | `05_GPT与Claude补丁落实及治理边界_v14_4.md` |
| Traceability matrix updated | PASS | `traceability/TRACEABILITY_MATRIX_v14_4.csv` |
| Second Claude zero-baseline student simulation on v14.4 | PENDING | must run next |
| DOCX delivery | NOT PRODUCED | no DOCX claimed |
| PDF delivery | NOT PRODUCED | no PDF claimed |

## Allowed Claim

v14.4 is the Markdown candidate after real GPT review and real Claude student-simulation patching. It contains the framework and all 42 locked core questions analysed by the framework.

## Not Allowed

- Do not claim final external PASS until the second v14.4 student simulation is captured.
- Do not claim full raw GPT/Claude transcript where copy/export failed.
- Do not claim DOCX/PDF delivery.
"""


def readme() -> str:
    return """# v14.4 Claude Student Patch Framework Baodian

This directory is the v14.4 Markdown candidate after:

- real GPT Pro review and GPT minimum patch application,
- real Claude Opus 4.7 Adaptive zero-baseline student simulation,
- student-facing framework repair based on Claude's `PASS_AFTER_PATCH` findings.

It includes the patched framework, all 42 locked core questions analysed by the framework, a combined Markdown baodian, open-container appendix, governance, traceability, and the Claude student simulation capture from v14.3.

Boundary: second Claude simulation on v14.4 and DOCX/PDF delivery are not yet complete.
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    framework = patch_framework(read(SRC / "01_先背这套_法律主观题不扣分框架_v14_3.md"))
    cards = patch_common(read(SRC / "02_42题按框架拆解与解析_v14_3.md"))
    appendix = patch_common(read(SRC / "04_开放容器与不晋升题附录_v14_3.md"))
    gov = governance()
    combined = "\n\n---\n\n".join(
        [
            "# 选必二法律与生活：法律宝典 v14.4 Claude学生补丁版",
            framework,
            cards,
            appendix,
            gov,
        ]
    )

    write(OUT / "00_READ_ME_FIRST.md", readme())
    write(OUT / "01_先背这套_法律主观题不扣分框架_v14_4.md", framework)
    write(OUT / "02_42题按框架拆解与解析_v14_4.md", cards)
    write(OUT / "04_开放容器与不晋升题附录_v14_4.md", appendix)
    write(OUT / "05_GPT与Claude补丁落实及治理边界_v14_4.md", gov)
    write(OUT / "06_FINAL_GOVERNOR_CHECKLIST_v14_4.md", governor())
    write(OUT / "选必二法律与生活_法律宝典_v14_4_Claude学生补丁版.md", combined)

    if (SRC / "external_gate_attempts").exists():
        shutil.copytree(SRC / "external_gate_attempts", OUT / "external_gate_attempts")
    if (SRC / "claude_student_simulation").exists():
        shutil.copytree(SRC / "claude_student_simulation", OUT / "claude_student_simulation")

    sim_dir = OUT / "claude_student_simulation"
    prompt_v14_3 = sim_dir / "CLAUDE_ZERO_BASELINE_STUDENT_PROMPT_v14_3.md"
    pack_v14_3 = sim_dir / "CLAUDE_BLIND_TEST_PACK_8Q_v14_3.md"
    if prompt_v14_3.exists():
        write(sim_dir / "CLAUDE_ZERO_BASELINE_STUDENT_PROMPT_v14_4.md", patch_common(read(prompt_v14_3)))
    if pack_v14_3.exists():
        write(sim_dir / "CLAUDE_BLIND_TEST_PACK_8Q_v14_4.md", patch_common(read(pack_v14_3)))

    trace_src = SRC / "traceability" / "TRACEABILITY_MATRIX_v14_3.csv"
    if trace_src.exists():
        write(OUT / "traceability" / "TRACEABILITY_MATRIX_v14_4.csv", patch_common(read(trace_src)))

    write(
        OUT / "build_manifest.txt",
        "built_by=build_v14_4_claude_student_patch.py\n"
        "status=claude_student_patch_applied_pending_second_claude_sim\n",
    )


if __name__ == "__main__":
    main()
