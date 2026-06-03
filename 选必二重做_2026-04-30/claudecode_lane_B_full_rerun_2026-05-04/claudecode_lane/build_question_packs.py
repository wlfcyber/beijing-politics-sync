#!/usr/bin/env python3
"""
Round 6: 把 SUBJECTIVE_QUESTION_PACK.json + CHOICE_QUESTION_PACK.json 加工成
最终题卡（含情境分类、争点、知识链段、功能落点等字段，自动可填的填上）。
"""
import json, re
from pathlib import Path
from collections import defaultdict

PROJECT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04")
CTRL = PROJECT / "00_control"

# 情境分类规则：每条规则 = (一级类, 二级类, 关键词集合)
SITUATION_RULES = [
    # A 交易交换
    ("交易交换", "网络消费/平台欺诈", ["网购", "网络", "电商", "平台", "直播", "网店", "快递", "外卖", "搭售", "虚假宣传", "假一赔", "三倍赔偿", "十倍赔偿", "AIGC", "算法"]),
    ("交易交换", "格式条款/服务合同", ["格式条款", "格式合同", "租赁", "装修", "装饰", "施工", "服务合同", "代理"]),
    ("交易交换", "买卖合同/违约责任", ["买卖", "购买", "合同成立", "要约", "承诺", "违约", "继续履行", "解除合同"]),
    ("交易交换", "未成年/限制行为能力", ["未成年", "未满18", "17岁", "限制民事行为能力", "打赏", "充值", "监护", "法定代理"]),
    ("交易交换", "劳动用工/竞业限制", ["劳动合同", "用人单位", "劳动者", "竞业限制", "经济补偿", "工伤", "解除劳动", "劳动仲裁", "录用通知", "试用期"]),
    # B 身份财产
    ("身份财产", "婚姻家庭/夫妻共同", ["夫妻", "婚姻", "婚后", "婚前", "共同债务", "共同财产", "离婚", "彩礼"]),
    ("身份财产", "继承/遗赠扶养", ["继承", "遗嘱", "遗产", "遗赠", "扶养协议", "法定继承", "代位继承", "赡养"]),
    ("身份财产", "物权/不动产/相邻", ["宅基地", "用益物权", "相邻", "通行", "采光", "噪音", "房产", "不动产", "登记", "所有权", "质权", "抵押权", "担保物权"]),
    # C 人身权益
    ("人身权益", "肖像/声音/AIGC人格", ["肖像权", "声音权", "AIGC", "数字人", "深度合成", "AI生成", "生成式人工智能"]),
    ("人身权益", "名誉/隐私/个人信息", ["名誉权", "隐私权", "个人信息", "差评", "聊天记录", "监控", "包厢"]),
    ("人身权益", "一般侵权/特殊侵权", ["侵权责任", "过错", "因果关系", "高空抛物", "动物致害", "产品责任", "环境污染", "安全保障义务", "公共场所", "饲养"]),
    # D 创新竞争
    ("创新竞争", "著作权/AI作品", ["著作权", "作品", "署名权", "AI作品", "图片", "视频", "音乐"]),
    ("创新竞争", "商标/混淆/不正当竞争", ["商标", "包装装潢", "混淆", "搭便车", "商业诋毁", "不正当竞争", "企业名称", "商号"]),
    ("创新竞争", "商业秘密/数据/专利", ["商业秘密", "数据", "数据抓取", "专利", "技术秘密", "保密协议"]),
    # E 救济公共
    ("救济公共", "调解/仲裁/诉讼程序", ["人民调解", "诉讼调解", "司法确认", "仲裁", "二审", "审判监督", "执行", "失信"]),
    ("救济公共", "举证责任/诉讼时效", ["举证责任", "谁主张", "举证倒置", "诉讼时效"]),
    ("救济公共", "公益诉讼/生态/公共利益", ["公益诉讼", "检察机关", "检察院", "生态修复", "环境损害", "公共利益", "文物保护"]),
]

# 关键词→主题的快速反查
def classify_situation(qtext):
    """返回 [(L1, L2, hits)] 列表，按命中数降序。"""
    scores = []
    for l1, l2, kws in SITUATION_RULES:
        hits = sum(1 for kw in kws if kw in qtext)
        if hits > 0:
            scores.append((l1, l2, hits))
    scores.sort(key=lambda x: -x[2])
    return scores[:3]  # 最多 3 个候选

def extract_setting(qtext):
    """提取设问句"""
    lines = qtext.split("\n")
    settings = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.search(r"运用《?.{0,8}》?知识|结合.{0,10}材料|说明|分析|阐述|阐释|论证|说明.{0,4}的理由|分析.{0,4}的意义|谈谈.{0,5}认识|完成下表", line):
            if 8 < len(line) < 250:
                settings.append(line)
    return " ｜ ".join(settings[:3])

def compress_material(qtext, qnum):
    """把材料压成一句起因→经过→结果（粗版，自动）"""
    # 去掉设问、题号、选项标签
    text = qtext
    # 删除选项 ABCD（如果是选择题）
    text = re.sub(r"[\nA-D]\s*[．.](?=\s|\S)", " ", text)
    text = re.sub(r"^\d{1,2}\s*[．.]", "", text)
    text = re.sub(r"《.{0,15}》知识.*", "", text)
    text = re.sub(r"运用.{0,20}知识.*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    # 取前 350 字
    return text[:350]

def extract_arguable_points(qtext):
    """从设问反推争点（疑问句格式）"""
    settings = extract_setting(qtext)
    issues = []
    if "为什么" in settings or "理由" in settings:
        issues.append("法院/仲裁机构作出该处理的法律依据是什么？")
    if "意义" in settings:
        issues.append("该处理在法治建设/社会经济发展上的功能是什么？")
    if "支持" in settings or "驳回" in settings:
        issues.append("当事人的诉讼请求/主张是否应当被支持？")
    if "是否" in settings or "能否" in settings:
        issues.append("是否成立 / 是否有效 / 是否应承担责任？")
    if "如何" in settings or "怎样" in settings:
        issues.append("应当采取何种处理方式或救济路径？")
    if not issues:
        issues.append("依据《法律与生活》知识，本案的法律关系判断与处理结果是什么？")
    return issues

def main():
    with open(CTRL / "SUBJECTIVE_QUESTION_PACK.json", encoding="utf-8") as f:
        subj = json.load(f)
    with open(CTRL / "CHOICE_QUESTION_PACK.json", encoding="utf-8") as f:
        choice = json.load(f)

    # 加工主观题
    enriched_subj = []
    for e in subj:
        qtext = e["qtext"]
        situations = classify_situation(qtext)
        primary = situations[0] if situations else ("未分类", "未分类", 0)
        enriched_subj.append({
            **e,
            "situation_l1": primary[0],
            "situation_l2": primary[1],
            "situation_alt": [{"l1": s[0], "l2": s[1], "hits": s[2]} for s in situations[1:]],
            "setting_extracted": extract_setting(qtext),
            "material_compressed": compress_material(qtext, e["qnum"]),
            "issues": extract_arguable_points(qtext),
        })

    # 加工选择题
    enriched_choice = []
    for e in choice:
        qtext = e["qtext"]
        situations = classify_situation(qtext)
        primary = situations[0] if situations else ("未分类", "未分类", 0)
        # 提取选项 ABCD
        options = re.findall(r"([A-D])\s*[．.]\s*([^A-D\n]{5,200})", qtext)
        # 提取①②③④
        sub_opts = re.findall(r"([①②③④])\s*([^①②③④\n]{5,150})", qtext)
        enriched_choice.append({
            **e,
            "situation_l1": primary[0],
            "situation_l2": primary[1],
            "options_abcd": options[:4],
            "sub_options": sub_opts[:4],
        })

    # 写出
    with open(CTRL / "SUBJECTIVE_PACK_ENRICHED.json", "w", encoding="utf-8") as f:
        json.dump(enriched_subj, f, ensure_ascii=False, indent=2)
    with open(CTRL / "CHOICE_PACK_ENRICHED.json", "w", encoding="utf-8") as f:
        json.dump(enriched_choice, f, ensure_ascii=False, indent=2)

    # 统计
    from collections import Counter
    print("=== 主观题情境分布 ===")
    subj_dist = Counter(f"{e['situation_l1']} > {e['situation_l2']}" for e in enriched_subj)
    for k, v in subj_dist.most_common():
        print(f"  {v:3}  {k}")
    print(f"\n=== 选择题情境分布 ===")
    choice_dist = Counter(f"{e['situation_l1']} > {e['situation_l2']}" for e in enriched_choice)
    for k, v in choice_dist.most_common():
        print(f"  {v:3}  {k}")

    print(f"\nTotal subjective: {len(enriched_subj)}")
    print(f"Total choice:     {len(enriched_choice)}")

if __name__ == "__main__":
    main()
