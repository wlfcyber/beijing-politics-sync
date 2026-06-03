#!/usr/bin/env python3
"""把 Word 内容同步生成 Markdown 备份（便于打印/审稿）"""
import json
from pathlib import Path
from collections import defaultdict
import sys
sys.path.insert(0, str(Path(__file__).parent))
from build_word_docs import (
    DOMAIN_ORDER, DOMAIN_BLURB, CHOICE_CHAPTER_ORDER, HAND_CRAFTED, sanitize
)

PROJECT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04")
CTRL = PROJECT / "00_control"
DELIVERY = PROJECT / "delivery"

def md_subj_card(q, hand, level="####"):
    suite_label = q["suite"].replace("/", " · ")
    out = [f"\n{level} 【{suite_label}  第{q['qnum']}题】\n"]
    out.append(f"**设问**：{sanitize(q.get('setting_extracted','') or '（未提取到设问）')}\n")
    out.append(f"**材料一句话（起因→经过→结果）**：{sanitize(q.get('material_compressed','') or '')}\n")
    issues = q.get("issues") or []
    if issues:
        out.append("**争点**：")
        for i, iss in enumerate(issues, 1):
            out.append(f"  {i}. {iss}")
        out.append("")
    if hand:
        out.append(f"**命题路径**：{sanitize(hand['命题路径'])}\n")
        out.append(f"**知识链段**：{sanitize(hand['知识链段'])}\n")
        out.append(f"**功能落点段**：{sanitize(hand['功能落点段'])}\n")
        out.append(f"**🔴踩分硬卡口**：{sanitize(hand['踩分硬卡口'])}\n")
        out.append(f"**等价表达**：{sanitize(hand['等价表达'])}\n")
        out.append(f"**必修三化风险**：{sanitize(hand['必修三化风险'])}\n")
        out.append(f"*元层评注*：{sanitize(hand['元层评注'])}\n")
    else:
        rs = q.get("rubric_segments") or []
        if rs:
            out.append("**细则核心要点（命题人给分依据）**：\n")
            out.append("```")
            out.append(sanitize(rs[0]["snippet"][:1500]))
            out.append("```\n")
        else:
            out.append("*（本题未自动匹配到细则段，需回原卷查阅。）*\n")
        out.append("*命题路径 / 知识链段 / 功能落点 / 踩分硬卡口 / 等价表达 / 必修三化风险 / 元层评注：[本题示例暂缺，建议对照同情境已写题作答]*\n")
    return "\n".join(out)

def md_choice_card(q):
    suite_label = q["suite"].replace("/", " · ")
    out = [f"\n##### 【{suite_label}  第{q['qnum']}题】"]
    out.append(f"*情境分类： {q.get('situation_l1','')} > {q.get('situation_l2','')}*\n")
    qtext_short = sanitize(q['qtext'][:600].replace('\n',' ').strip())
    out.append(f"题面：{qtext_short}\n")
    options = q.get("options_abcd") or []
    if options:
        for letter, content in options[:4]:
            out.append(f"- {letter}．{content.strip()[:200]}")
    out.append("\n*正确答案 / 错项陷阱：[暂缺，将在后续手工补充]*\n")
    return "\n".join(out)

def write_framework_md(subj, choice):
    out = ["# 选必二《法律与生活》框架版\n"]
    out.append("## 一、命题总纲（先看这页，每次都看）\n")
    out.append("**两条主轴**：\n- 政治性 ↔ 学理性\n- 价值性 ↔ 知识性\n")
    out.append("**主观题答题结构（永远两段）**：")
    out.append("- 知识链段：法律关系判断 → 法定要件套用 → 规则援引 → 效力/责任判定 → 救济选择 → 程序落点。")
    out.append("- 功能落点段：论证这条法律规则如何推动 法治建设 / 社会经济发展 / 市场秩序 / 新业态规范。回扣本案再上升，不许写抽象口号。\n")
    out.append("**选择题考查重点**：\n- 考制度本身的内容乃至细节，不只考价值取向。\n")
    out.append("**两条永不可越的边界**：\n- 不法考化：不超纲，不出过多主体/法律关系/疑难问题。\n- 不必修三化：法律知识是答案主体，不能让宏观法治口号占主导。\n")

    out.append("\n## 二、主观题主干（按情境分组）\n")
    by_l1_l2 = defaultdict(lambda: defaultdict(list))
    for e in subj:
        by_l1_l2[e.get("situation_l1","未分类")][e.get("situation_l2","未分类")].append(e)
    for l1 in DOMAIN_ORDER:
        if l1 not in by_l1_l2: continue
        out.append(f"\n### {l1} 域\n")
        out.append(f"*{DOMAIN_BLURB.get(l1,'')}*\n")
        for l2, qs in by_l1_l2[l1].items():
            out.append(f"\n#### {l2}（{len(qs)} 道）\n")
            for q in qs:
                hand = HAND_CRAFTED.get(f"{q['suite']}::{q['qnum']}")
                out.append(md_subj_card(q, hand, level="#####"))

    out.append("\n## 三、横切工具层（六张表）\n")
    out.append("### 表 1：要件库（高频法律概念的要件组合）\n")
    out.append("| 法律概念 | 要件组合（缺一不可）|")
    out.append("|---|---|")
    rule_kit = [
        ("合同成立", "要约+承诺，承诺到达发生效力"),
        ("合同欺诈（可撤销）", "故意 + 欺诈行为 + 因果关系 + 违背真实意思表示"),
        ("消费者欺诈（三倍赔偿）", "经营者欺诈故意 + 误导消费 + 影响真实选择 + 属生活消费"),
        ("食品安全（十倍赔偿）", "食品不符合食品安全标准 + 消费者购买"),
        ("夫妻共同债务", "为夫妻共同生活 / 共同经营 / 共同意思表示之一"),
        ("一般侵权", "行为 + 损害 + 因果关系 + 过错"),
        ("肖像权侵权", "未经许可 + 使用可识别肖像 + 无法定免责事由"),
        ("惩罚性赔偿（知产）", "主观恶性强 + 社会危害大 + 已有赔偿不足以惩罚"),
        ("不正当竞争混淆", "有影响的标识近似 + 容易导致消费者误认 + 攀附商誉"),
        ("竞业限制", "高管/高级技术/保密义务人员 + 期限不超 2 年 + 范围合理 + 用人单位给经济补偿"),
        ("公益诉讼（民事）", "损害公共利益 + 起诉主体适格"),
        ("格式条款无效", "免除提供方主要责任 / 加重对方责任 / 排除对方主要权利 / 未尽提示说明义务"),
    ]
    for name, kit in rule_kit:
        out.append(f"| {name} | {kit} |")

    out.append("\n### 表 2：救济库\n")
    out.append("| 救济类型 | 具体救济方式 |")
    out.append("|---|---|")
    relief_kit = [
        ("合同救济", "继续履行 / 解除合同 / 赔偿损失 / 定金罚则 / 违约金"),
        ("消费者救济", "退还价款 / 三倍赔偿（消费欺诈）/ 十倍赔偿（食品）"),
        ("物权救济", "返还原物 / 排除妨害 / 消除危险 / 恢复原状"),
        ("人格权救济", "停止侵害 / 排除妨碍 / 消除危险 / 赔礼道歉 / 恢复名誉 / 消除影响 / 赔偿损失"),
        ("知产救济", "停止侵害 / 赔偿损失 / 惩罚性赔偿"),
        ("程序救济", "协商 / 调解 / 仲裁 / 诉讼 / 公益诉讼 / 司法确认"),
    ]
    for k, v in relief_kit:
        out.append(f"| {k} | {v} |")

    out.append("\n### 表 3：法律功能落点表（四向指南针）\n")
    out.append("**意义部分必须用具体功能话语，禁止抽象口号。**\n")
    out.append("| 方向 | 具体话语（可直接上卷面） |")
    out.append("|---|---|")
    fn_kit = [
        ("法治建设方向", "公正司法 / 以事实为依据以法律为准绳 / 司法裁判导向作用 / 明确权利行使界限"),
        ("社会经济发展方向", "市场秩序 / 营商环境 / 数字经济 / 新业态规范 / 行业规范化经营"),
        ("核心价值方向", "诚信原则 / 公平竞争 / 平等保护 / 弱势保护 / 和谐价值"),
        ("制度引导方向", "规范企业经营 / 警示侵权 / 激励创新 / 保护消费 / 维护行业秩序"),
    ]
    for k, v in fn_kit:
        out.append(f"| {k} | {v} |")

    out.append("\n### 表 4：法律精确性卡口表（学理性硬要求——术语不精确就丢分）\n")
    out.append("| 精确性方向 | 对照 |")
    out.append("|---|---|")
    out.append("| A1 法律名精确 | ✓ 消费者权益保护法 / 食品安全法 / 民法典 ／  ✗ 保护法 / 民法 / 经济法 |")
    out.append("| A2 法律概念精确 | ✓ 行使损害赔偿请求权 / 构成不正当竞争中的混淆行为 ／ ✗ 维权 / 违法 / 侵权（笼统） |")
    out.append("| A3 责任/秩序定位精确 | ✓ 违约责任 vs 侵权责任 / 司法秩序 vs 诉讼秩序 / 市场秩序 ／ ✗ 违法责任 / 社会秩序 |")

    out.append("\n### 表 5：答案内容主体卡口表（不必修三化）\n")
    out.append("**法律知识不能只是背景，答案内容均来自法治模块。**\n")
    out.append("| 层面 | 对照 |")
    out.append("|---|---|")
    out.append("| 答案主体 | ✓ 民法典 X 条 / 法定要件 / 责任落点 / 救济方式 ／ ✗ 全面依法治国 / 法治精神 / 科学立法严格执法（不能为答案主体）|")
    out.append("| 功能话语 | ✓ 维护消费者合法权益 / 规范企业经营 / 优化网络消费环境 / 促进数字经济发展 / 公正司法 / 保护创新激励 ／ ✗ 弘扬法治精神 / 推进依法治国 / 维护社会主义核心价值观（空洞收束）|")

    out.append("\n### 表 6：踩分边界禁区表（命题人画的硬规则）\n")
    out.append("| 边界规则 | 说明 |")
    out.append("|---|---|")
    boundaries = [
        ("不重复给分", "多案例题中相同价值话术只能给一次（如'诚信原则''节约司法资源'）"),
        ("材料触发完整性", "材料给的多个事实条件必须全部写出（如搭售欺诈三条件全写）"),
        ("案例独立性", "多案例题每个案例必须独立产出法律依据+责任落点，不能合并"),
        ("法律名硬卡口", "'消费者权益保护法'必须写完整名称，'保护法'不给分"),
        ("秩序定位硬卡口", "诉讼/司法秩序场景不写'社会秩序'"),
        ("反错位提醒", "案例三若为滥用诉讼权利，不能写成'商业诋毁'或'不正当竞争'"),
    ]
    for k, v in boundaries:
        out.append(f"| {k} | {v} |")

    out.append("\n## 四、选择题主干（独立于主观题）\n")
    out.append("选择题考'制度本身的内容乃至细节'。错项排除三件套：法律关系错位 / 制度细节错位 / 程序效力错位。\n")

    by_choice_l1 = defaultdict(list)
    for e in choice:
        by_choice_l1[e.get("situation_l1","未分类")].append(e)
    for chap_title, chap_l1s in CHOICE_CHAPTER_ORDER:
        items = []
        for l1 in chap_l1s:
            items.extend(by_choice_l1.get(l1, []))
        if not items: continue
        out.append(f"\n### {chap_title}（{len(items)} 道）\n")
        for q in items[:30]:
            out.append(md_choice_card(q))

    return "\n".join(out)

def write_situation_md(subj, choice):
    out = ["# 选必二《法律与生活》情境版\n"]
    out.append("*本册按【考过的情境】穷尽组织。每个主观题情境用一句话起因→经过→结果概括，列对应细则与作答动作。选择题情境单独一节，不与主观题混排。*\n")

    out.append(f"\n## 第一部分 主观题情境（{len(subj)} 道）\n")
    by_l1_l2 = defaultdict(lambda: defaultdict(list))
    for e in subj:
        by_l1_l2[e.get("situation_l1","未分类")][e.get("situation_l2","未分类")].append(e)
    for l1 in DOMAIN_ORDER:
        if l1 not in by_l1_l2: continue
        out.append(f"\n### {l1}\n")
        for l2, qs in by_l1_l2[l1].items():
            out.append(f"\n#### {l2}（{len(qs)} 道）\n")
            for q in qs:
                hand = HAND_CRAFTED.get(f"{q['suite']}::{q['qnum']}")
                suite_label = q["suite"].replace("/", " · ")
                out.append(f"\n**【{suite_label} 第{q['qnum']}题】**\n")
                out.append(f"- 情境一句话： {sanitize(q.get('material_compressed','')[:300])}")
                out.append(f"- 设问： {sanitize(q.get('setting_extracted',''))}")
                if q.get("issues"):
                    out.append(f"- 争点： {' / '.join(q['issues'][:2])}")
                if hand:
                    out.append(f"- 细则核心： {sanitize(hand.get('知识链段','')[:500])}")
                    out.append(f"- 🔴硬卡口： {sanitize(hand.get('踩分硬卡口','')[:500])}")
                    out.append(f"- 作答落点： {sanitize(hand.get('功能落点段','')[:300])}")
                else:
                    rs = q.get("rubric_segments") or []
                    if rs:
                        out.append(f"- 细则核心要点：")
                        out.append(f"  > {sanitize(rs[0]['snippet'][:600])}")
                    out.append("- *硬卡口 / 作答落点：[暂缺，将在后续手工补充]*")
                out.append("")

    out.append(f"\n## 第二部分 选择题情境（{len(choice)} 道）\n")
    out.append("*选择题情境只列：题源、情境关键词、题面要点、选项；正确答案与错项陷阱将在后续手工补充。*\n")
    by_l1 = defaultdict(list)
    for e in choice:
        by_l1[e.get("situation_l1","未分类")].append(e)
    for l1 in DOMAIN_ORDER + ["未分类"]:
        if l1 not in by_l1: continue
        out.append(f"\n### {l1}（{len(by_l1[l1])} 道）\n")
        for q in by_l1[l1]:
            suite_label = q["suite"].replace("/", " · ")
            out.append(f"\n**【{suite_label} 第{q['qnum']}题】** {q.get('situation_l2','')}")
            qtext_short = sanitize(q['qtext'][:300].replace('\n',' ').strip())
            out.append(f"\n  {qtext_short}\n")

    return "\n".join(out)

def post_sanitize_md(text):
    """对完整 MD 文本做最终清洗（兜底确保零禁词）"""
    repl = [
        ("阅卷前制定的", "本题"),
        ("阅卷反馈", "答题反馈"),
        ("阅卷总结", "答题总结"),
        ("阅卷人", "命题人"),
        ("阅卷组", "命题组"),
        ("阅卷前", "本题"),
        ("阅卷桌", "命题人桌"),
        ("阅卷细则", "答题细则"),
        ("阅卷", "命题"),
        ("评标", "给分依据"),
        ("参考答案", "答题要点"),
        ("讲评", "答题指引"),
        ("勿传", ""),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text

def main():
    with open(CTRL / "SUBJECTIVE_PACK_ENRICHED.json", encoding="utf-8") as f:
        subj = json.load(f)
    with open(CTRL / "CHOICE_PACK_ENRICHED.json", encoding="utf-8") as f:
        choice = json.load(f)
    md1 = post_sanitize_md(write_framework_md(subj, choice))
    md2 = post_sanitize_md(write_situation_md(subj, choice))
    p1 = DELIVERY / "选必二《法律与生活》框架版_2026-05-04.md"
    p2 = DELIVERY / "选必二《法律与生活》情境版_2026-05-04.md"
    p1.write_text(md1, encoding="utf-8")
    p2.write_text(md2, encoding="utf-8")
    print(f"框架版 MD: {p1}  ({p1.stat().st_size:,} bytes)")
    print(f"情境版 MD: {p2}  ({p2.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
