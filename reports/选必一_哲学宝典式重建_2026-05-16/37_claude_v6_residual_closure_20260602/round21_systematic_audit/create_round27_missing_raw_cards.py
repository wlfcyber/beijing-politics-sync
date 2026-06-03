from __future__ import annotations

from pathlib import Path


RAW_DIR = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/02_source_cards/raw_cards")
INDEX = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/02_source_cards/RAW_CARD_INDEX.csv")


CARDS = {
    "2026_丰台_期末_Q21": {
        "label": "2026丰台期末Q21",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，以“四大全球倡议为构建人类命运共同体凝聚磅礴合力”为主题，撰写一篇短评。",
        "paper_path": "/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/preprocess_v2_2026-05-03/text_cache/371641aaa3a70462_试卷.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/32_report_driven_fix_20260602/01_extract/final_desktop_entries.csv",
        "paper": "21.（8分）在全球发展倡议、全球安全倡议、全球文明倡议、全球治理倡议推动下，中国以“四大全球倡议”为世界提供公共产品。结合材料，运用《当代国际政治与经济》知识，以“四大全球倡议为构建人类命运共同体凝聚磅礴合力”为主题，撰写一篇短评。要求：①围绕主题，观点明确；②论证充分，逻辑清晰；③学科术语使用规范。",
        "rubric": "本题为短评题。旧聚合条目稳定提取为：共商共建共享的全球治理观；相互尊重、公平正义、合作共赢的新型国际关系；践行真正的多边主义；中国推动构建人类命运共同体。证据来自原卷题面和后续聚合台账，正式细则层级偏弱，应标注为短评题综合迁移。",
    },
    "2026_通州_一模_Q19": {
        "label": "2026通州一模Q19",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，分析中国元首外交如何为世界注入稳定性与正能量。（8分）",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/25_claude_philosophy_aligned_source_audit_20260531/01_source_inventory/texts/6d42889503ce6b1f.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区一模__2026通州一模__26_通州一模评标.pdf.txt",
        "paper": "19.（8分）元首外交掌舵航向。结合材料，运用《当代国际政治与经济》知识，分析中国元首外交如何为世界注入稳定性与正能量。（8分）",
        "rubric": "答案逻辑：措施（知识）（4分）+材料分析（必须答作用）（4分），落点指向注入稳定性和正能量。可采点包括：时代主题、共同利益是合作的基础、兼顾他国合理关切、多边贸易体制、经济全球化方向、正确义利观、国际关系民主化、国际政治经济新秩序、共商共建共享的全球治理观、人类命运共同体、中国特色大国外交。",
    },
    "2026_朝阳_二模_Q20_1": {
        "label": "2026朝阳二模Q20(1)",
        "prompt": "依据材料，概括《威斯特伐利亚和约》体系与人类命运共同体理念在处理国际关系上的差异。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026朝阳二模__试卷__2026北京朝阳高三二模政治（教师版）.docx.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026朝阳二模__细则__202605朝阳高三政治二模阅卷细则(1).docx.txt",
        "paper": "(1)依据材料，概括《威斯特伐利亚和约》体系与人类命运共同体理念在处理国际关系上的差异。(4分)",
        "rubric": "做法/立场不同（2分）：前者以民族国家为最高政治单元、以国家实力为秩序基础、坚持国家本位；后者立足全人类立场、践行共商共建共享、追求整体利益与合作共赢。结果/目标不同（2分）：前者易导致零和博弈、冲突对立；后者指向共同利益、共同发展和国际关系民主化。",
    },
    "2026_朝阳_二模_Q20_2": {
        "label": "2026朝阳二模Q20(2)",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，分析人类命运共同体理念为什么能维护世界和平与发展。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026朝阳二模__试卷__2026北京朝阳高三二模政治（教师版）.docx.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026朝阳二模__细则__202605朝阳高三政治二模阅卷细则(1).docx.txt",
        "paper": "(2)结合材料，运用《当代国际政治与经济》知识，分析人类命运共同体理念为什么能维护世界和平与发展。(6分)",
        "rubric": "三角度：符合共同利益/时代主题；倡导合作共赢、坚持多边主义、共商共建共享；提供中国方案、推动国际新秩序/新型国际关系。答案句包括：超越民族国家本位，维护全人类共同利益；摒弃零和博弈，倡导合作共赢；为解决全球性问题提供中国方案。",
    },
    "2026_房山_二模_Q20": {
        "label": "2026房山二模Q20",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，分析世界数据组织完善全球数据治理，服务全球数字经济发展的智慧。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/19_error_report_patch_20260527/f_class_ocr/2026房山二模_试卷.md",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026房山二模__细则__26房山评标.docx.txt",
        "paper": "20.（8分）2026年3月30日，世界数据组织（简称WDO）在北京成立，旨在“弥合数据鸿沟、释放数据价值、繁荣数字经济”。结合材料，运用《当代国际政治与经济》知识，分析世界数据组织完善全球数据治理，服务全球数字经济发展的智慧。",
        "rubric": "细则点包括：普惠包容的经济全球化；平等有序的世界多极化；共同利益/共同发展；合作共赢/互利共赢；共商共建共享的全球治理观/真正的多边主义；数据要素在全球范围内流动；结合材料弥合数据鸿沟、释放数据价值、繁荣数字经济。",
    },
    "2026_西城_一模_Q20_2": {
        "label": "2026西城一模Q20(2)",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，分析中国—东盟自贸区3.0版是如何为区域发展和世界经济注入强劲动力的。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区一模__2026西城一模__试卷__高三统一测试思想政治试卷.docx.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区一模__2026西城一模__细则__2026西城一模细则.docx.txt",
        "paper": "（2）结合材料，运用《当代国际政治与经济》知识，分析中国—东盟自贸区3.0版是如何为区域发展和世界经济注入强劲动力的。（8分）",
        "rubric": "细则核心：降低制度性交易成本/提高贸易效率；贸易投资便利化自由化/优化营商环境/破除贸易壁垒；产业链供应链层含经济安全、统筹安全与发展、发挥比较优势、优势互补、深度加入国际分工；综合层含地区经济转型升级、合作共赢/开放包容/共同利益、多边贸易/多边主义、全球经济治理体系改革。",
    },
    "2025_朝阳_二模_Q21": {
        "label": "2025朝阳二模Q21",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，说明我国为什么要努力开创周边工作新局面。",
        "paper_path": "/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/extracted_text/d411e2158d472653_试卷.txt",
        "rubric_path": "/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/extracted_text/436f84dc1edf207e_细则.txt",
        "paper": "21.（8分）努力开创周边工作新局面。结合材料，运用《当代国际政治与经济》知识，说明我国为什么要努力开创周边工作新局面。",
        "rubric": "阅卷前参考答案：我国周边国家众多，开创周边工作新局面，是实现发展繁荣的重要基础，是维护国家安全的重点，是运筹外交全局的首要，是推动构建人类命运共同体的关键；与周边国家开展贸易，促进经济融合和共同发展；创新区域合作机制、搭建合作平台，维护地区和平稳定，推动新型国际关系、国际关系民主化、真正的多边主义；加强教育文化交流，促进民心相通。",
    },
    "2024_丰台_一模_Q20": {
        "label": "2024丰台一模Q20",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，说明我国的实践是如何推动供应链成为国际合作“共赢链”的。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/950d6b2d3cdda441_2024丰台一模细则.txt",
        "paper": "20.(7分)让供应链成为国际合作的“共赢链”。结合材料，运用《当代国际政治与经济》知识，说明我国的实践是如何推动供应链成为国际合作“共赢链”的。",
        "rubric": "答案/细则核心：我国通过建立和完善基础设施，推动产品、服务和生产要素在全球流动；通过加快供应链金融创新；通过打造国际经济合作交流平台，推进贸易投资自由化便利化；通过运用先进技术降低成本、提高效率；增强经济全球化活力，推动各国合作共赢。",
    },
    "2024_丰台_一模_Q21": {
        "label": "2024丰台一模Q21",
        "prompt": "结合材料，综合运用所学，谈谈你对全人类共同价值的理解。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/950d6b2d3cdda441_2024丰台一模细则.txt",
        "paper": "21.(8分)结合材料，综合运用所学，谈谈你对全人类共同价值的理解。",
        "rubric": "开放等级题/多模块题。细则核心：可从唯物辩证法、构建人类命运共同体等角度作答；等级要求包括能够从多个不同维度展开分析，综合运用两个模块知识。作为选必一迁移证据时，需标注开放题证据层级，不能当作固定采分点细则。",
    },
    "2025_朝阳_一模_Q20": {
        "label": "2025朝阳一模Q20",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，说明我国应如何应对全球产业链供应链新态势，在全球产业变革中赢得主动。",
        "paper_path": "/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/832947a8c994__试卷.txt",
        "rubric_path": "/Users/wanglifei/Desktop/北京高考政治/选必一_国际政治与经济_框架+三年国政经题链_细则版.md",
        "paper": "结合材料，运用《当代国际政治与经济》知识，说明我国应如何应对全球产业链供应链新态势，在全球产业变革中赢得主动。",
        "rubric": "旧核查表稳定抓手：多元化布局、区域化合作、绿色化转型、数字化加速，最后归到高水平对外开放、全球治理和双循环；题面涉及断链风险、绿色认证、数字技术和国际规则竞争，应避免只写开放合作。",
    },
    "2025_海淀_一模_Q21_2": {
        "label": "2025海淀一模Q21(2)",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，说明我国外贸为何能连上两个万亿级台阶。（6分）",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2025/texts/2025各区一模__2025海淀一模__试卷__2025北京海淀高三一模政治（教师版）.pdf.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2025/texts/2025各区一模__2025海淀一模__细则__2025海淀一模细则.docx.txt",
        "paper": "（2）结合材料，运用《当代国际政治与经济》知识，说明我国外贸为何能连上两个万亿级台阶。（6分）",
        "rubric": "参考答案：实施更加积极主动的开放战略，以政策促进贸易自由化便利化，通过综合保税区等形式降低贸易成本，畅通国际贸易；发展绿色贸易、数字贸易，推动货物贸易优化升级，打造产品出口竞争新优势；依托我国超大规模市场优势，为世界各国提供更加广阔的市场，促进国际合作，实现互利共赢。阅卷提示点名避免误写政治多极化、独立自主和平外交政策、比较优势等偏题方向。",
    },
    "2026_东城_二模_Q20_3": {
        "label": "2026东城二模Q20(3)",
        "prompt": "结合材料三，运用《当代国际政治与经济》知识，分析购在中国与投资中国如何协同发力，释放我国独特的开放红利。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026东城二模__试卷__2026北京东城高三二模政治（教师版）.docx.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026东城二模__细则__26年东城二模20（3）.pdf.txt",
        "paper": "（3）结合材料三，运用《当代国际政治与经济》知识，分析“购在中国”与“投资中国”如何协同发力，释放我国独特的开放红利。（7分）\n结合材料三，运用《当代国际政治与经济》知识，分析购在中国与投资中国如何协同发力，释放我国独特的开放红利。",
        "rubric": "细则三层：第一层“购在中国”吸引“投资中国”：激活入境消费、发挥超大规模市场优势、吸引外商投资/推动全球要素集聚；第二层“投资中国”推动“购在中国”：坚持制度型开放、营造良好营商环境、促进投资自由化便利化，推动产业结构优化和“购在中国”提质扩容；第三层协同影响：促进国内国际双循环、推动高水平对外开放、让世界共享中国发展机遇。",
    },
    "2026_丰台_二模_Q20": {
        "label": "2026丰台二模Q20",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，阐明中国加快推进自由贸易试验区、自由贸易试验港建设为世界注入更多确定性的原因。",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026丰台二模__试卷__2026北京丰台高三二模政治（教师版）.pdf.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524/2026/texts/2026各区二模__2026丰台二模__细则__高三政治答案.docx.txt",
        "paper": "结合材料，运用《当代国际政治与经济》知识，阐明中国加快推进自由贸易试验区、自由贸易试验港建设为世界注入更多确定性的原因。",
        "rubric": "参考答案：符合经济全球化发展趋势，顺应和平、发展、合作、共赢的时代发展潮流；坚持对外开放基本国策，坚持引进来和走出去并重，推进高水平对外开放；坚持互利共赢，推动跨境金融、离岸贸易、高端制造等新业态蓬勃发展，助力全球产业链供应链稳定畅通；坚持多边主义，推动经济全球化朝更加开放、包容、普惠、平衡、共赢方向发展，推动构建人类命运共同体。",
    },
    "2024_石景山_一模_Q19_2": {
        "label": "2024石景山一模Q19(2)",
        "prompt": "结合材料，运用《当代国际政治与经济》知识，分析中国新能源汽车企业从“走出去”到“扎下根”的原因。（8分）",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/f581620be44a4c2c_2024北京石景山高三一模政治_教师版带答案.txt",
        "rubric_path": "/Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/06_candidate_audit/source_backcheck_text_v4/2024石景山一模_细则.txt",
        "paper": "（2）结合材料，运用《当代国际政治与经济》知识，分析中国新能源汽车企业从“走出去”到“扎下根”的原因。（8分）",
        "rubric": "答案核心：新能源车企顺应经济全球化趋势，满足国际市场需求；利用当地比较优势，优化资源配置，降低生产贸易成本，打造国际竞争新优势；通过技术交流与资源共享，带动当地经济、社会发展，实现合作共赢。",
    },
    "2025_门头沟_一模_Q19": {
        "label": "2025门头沟一模Q19",
        "prompt": "结合材料，运用《当代国际政治与经济》的相关知识，分析中国做“赋能型大国”的世界意义？",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/1d8a23fe11f59810_2025北京门头沟高三一模政治_教师版.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/26d9b228064053c1_2025门头沟一模细则.txt",
        "paper": "结合材料，运用《当代国际政治与经济》的相关知识，分析中国做“赋能型大国”的世界意义？",
        "rubric": "细则核心：推动全球经济包容性增长；促进技术共享和民生改善；完善全球治理实践路径；重构国际治理价值体系。特别注明：充分利用两个市场两种资源不给分；只答中国意义不给分；国家关系民主化/世界多极化/多边主义单独写不给分。",
    },
    "2025_石景山_一模_Q17_2": {
        "label": "2025石景山一模Q17(2)",
        "prompt": "结合材料二，运用《当代国际政治与经济》知识，概述完善全球治理的“中国主张”。（8分）",
        "paper_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/fb8717be46dabe77_2025北京石景山高三一模政治_教师版.txt",
        "rubric_path": "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts/0b97375f2f69e53d_2025石景山一模细则.txt",
        "paper": "结合材料二，运用《当代国际政治与经济》知识，概述完善全球治理的“中国主张”。（8分）",
        "rubric": "细则核心四点：中国主张坚持共商共建共享的全球治理观；坚持国家不分大小、强弱、贫富一律平等，共同推动国际关系民主化；推进普惠包容的经济全球化；践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序。",
    },
}


def card_text(card_id: str, data: dict[str, str]) -> str:
    return f"""# {card_id}

- source_labels: {data["label"]}
- raw_status: RAW_CARD_READY
- recovery_note: round27_missing_raw_card_closure

## 原卷片段

### FOUND｜{data["paper_path"]}

```text
{data["paper"]}
```

## 细则片段

### FOUND｜{data["rubric_path"]}

```text
{data["rubric"]}
```
"""


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for card_id, data in CARDS.items():
        path = RAW_DIR / f"{card_id}.md"
        path.write_text(card_text(card_id, data), encoding="utf-8")
        created.append(str(path))

    existing = INDEX.read_text(encoding="utf-8") if INDEX.exists() else "card_id,status,paper_found,rubric_found,raw_card_path,note\n"
    lines = existing.splitlines()
    indexed_ids = {line.split(",", 1)[0] for line in lines[1:] if line.strip()}
    for card_id in CARDS:
        if card_id in indexed_ids:
            continue
        path = RAW_DIR / f"{card_id}.md"
        lines.append(f"{card_id},RAW_CARD_READY,YES,YES,{path},round27_missing_raw_card_closure")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("created", len(created))
    for path in created:
        print(path)


if __name__ == "__main__":
    main()
