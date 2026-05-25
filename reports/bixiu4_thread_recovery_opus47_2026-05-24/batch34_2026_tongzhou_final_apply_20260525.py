from __future__ import annotations

import csv
import importlib.util
import json
import re
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


CORE_PATH = Path(__file__).with_name("batch33_2026_xicheng_final_apply_20260525.py")
spec = importlib.util.spec_from_file_location("batch33_core", CORE_PATH)
core = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(core)

W = core.W
NS = core.NS

ROOT = core.ROOT
RECOVERY = core.RECOVERY
RUN = core.RUN
DELIVERY = core.DELIVERY
MATRIX = core.MATRIX
LEDGER = core.LEDGER
ACCEPTED = core.ACCEPTED
GLOBAL_AUDIT_CSV = core.GLOBAL_AUDIT_CSV
GLOBAL_AUDIT_MD = core.GLOBAL_AUDIT_MD
FORMAT_QA = core.FORMAT_QA
THREAD_STATUS = core.THREAD_STATUS
GOVERNOR = core.GOVERNOR
CONFUCIUS = core.CONFUCIUS
MODEL_LEDGER = core.MODEL_LEDGER

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026通州期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "44537714bd68a7c1_2026通州期末细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "7f3083ea306ea1e9_2026北京通州高三_上_期末政治_教师版.md"
RAW_RUBRIC_PPTX = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026通州期末\细则\2026通州期末细则.pptx")
RAW_TEACHER_PDF = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026通州期末\试卷\2026北京通州高三（上）期末政治（教师版）.pdf")
RAW_LECTURE_PPTX = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026通州期末\2026通州期末试卷讲评.pptx")

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH34_2026_TONGZHOU_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH34_2026_TONGZHOU_FINAL_CODEX_20260525.md"

SUITE = "2026通州期末"
YEAR = "2026"
STAGE = "期末"
BATCH_ID = "batch34_2026_tongzhou_final"
MATRIX_SOURCE = "codex_batch34_2026_tongzhou_final"
EXPECTED_ENTRIES = 29
REMOVE_EXISTING_SIGNATURES = {
    ("Q21", "两点论与重点论"),
    ("Q21", "主要矛盾和次要矛盾"),
}
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    f"raw formal rubric PPTX: {RAW_RUBRIC_PPTX}; raw teacher PDF: {RAW_TEACHER_PDF}; "
    f"lecture/marking PPTX: {RAW_LECTURE_PPTX}; "
    "formal answer key: 1A,2D,3B,4D,5C,6A,7B,8D,9D,10B,11C,12A,13C,14A,15B."
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "人民群众",
        "question_no": "Q5",
        "question_label": "第5题（选择题）",
        "material_trigger": "正式答案键为5C；正确组合包含“基层问题的治理必须坚持群众观念，要有系统思维和辩证思维”。",
        "question_prompt": "判断基层问题治理中“群众观念、系统思维和辩证思维”的合理性。",
        "why_trigger": "正确选项直接点名群众观念，但它来自客观选择题答案键，只能作人民群众观点的选择题挂点。",
        "answer_landing": "基层治理要尊重群众主体地位，从群众需要和群众参与中形成治理合力，不能把基层问题割裂、孤立处理。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q5",
        "question_label": "第5题（选择题）",
        "material_trigger": "正式答案键为5C；正确选项要求基层治理“要有系统思维和辩证思维”。",
        "question_prompt": "判断基层问题是否应在多主体、多关系、多环节中系统治理。",
        "why_trigger": "正确选项直接使用系统思维，支持系统观念的客观选择题挂点，但不替代主观题评分细则。",
        "answer_landing": "基层治理要把多元主体、治理环节和现实问题作为系统来把握，统筹优化而不是孤立处理。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q7",
        "question_label": "第7题（选择题）",
        "material_trigger": "正式答案键为7B；正确选项①把“凡益之道，与时偕行”对应为“事物是不断变化发展的”。",
        "question_prompt": "判断中华优秀传统文化名句与哲学道理的对应关系。",
        "why_trigger": "正确选项明示发展观点，但属于客观选择题证据，只登记为选择题挂点。",
        "answer_landing": "事物处于变化发展过程中，认识和行动要与时俱进，在变化中把握发展方向。",
    },
    {
        "canonical_node": "量变与质变 / 适度原则",
        "question_no": "Q7",
        "question_label": "第7题（选择题）",
        "material_trigger": "正式答案键为7B；正确选项④把“图难于其易，为大于其细”对应为“量变是质变的必要准备，要重视量的积累”。",
        "question_prompt": "判断传统名句中的量变质变关系。",
        "why_trigger": "正确选项直接给出量变是质变必要准备，证据来自正式答案键和试卷原题。",
        "answer_landing": "解决难事、大事要从容易处、细微处积累条件，在量的积累中促成质的飞跃。",
    },
    {
        "canonical_node": "根据固有联系建立新的具体联系",
        "question_no": "Q8",
        "question_label": "第8题（选择题）",
        "material_trigger": "正式答案键为8D；正确选项③认为刺绣作品建立了承载家国情怀的人为事物联系。",
        "question_prompt": "判断“记忆地图”汴绣作品中家国情怀与人为事物联系的关系。",
        "why_trigger": "正确选项直接指向人为事物联系，适合进入联系观下的客观挂点。",
        "answer_landing": "人们可以依据历史记忆、地名、抗战场景等固有联系，通过刺绣这一实践活动建立新的具体联系。",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q8",
        "question_label": "第8题（选择题）",
        "material_trigger": "正式答案键为8D；正确选项④写明“个体差异性与民族记忆整体性在作品中对立统一”。",
        "question_prompt": "判断个体差异性与民族记忆整体性在作品中的关系。",
        "why_trigger": "正确选项直接使用“对立统一”，但仍是客观选择题证据，不能升级为主观题细则。",
        "answer_landing": "作品把个体参与的差异性和共同民族记忆的整体性统一起来，体现矛盾双方既区别又联系。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q9",
        "question_label": "第9题（选择题）",
        "material_trigger": "正式答案键为9D；正确选项认为清分结算中心运用系统化、数字化模式整合保障资源，形成新机制。",
        "question_prompt": "判断医保与商保数据整合对民生服务机制的意义。",
        "why_trigger": "正确选项直接出现系统化整合资源，是系统观念的客观选择题挂点。",
        "answer_landing": "通过系统化、数字化方式统筹医保、商保和数据资源，可以优化服务流程，形成协同保障机制。",
    },
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题哲学角度写明“坚持一切从实际出发，实事求是”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则把李冰利用地理条件、因地制宜、顺势而为直接落到一切从实际出发和实事求是。",
        "answer_landing": "都江堰治水智慧首先体现从当地地势、水势和民生需要出发，把主观方案同客观实际统一起来。",
    },
    {
        "canonical_node": "物质决定意识",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题唯物论角度写明“体现了物质决定意识”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则把当地地理条件对治水方案的制约作为物质决定意识的明确得分点。",
        "answer_landing": "治水方案不是主观臆造，而是由当地自然条件和水利实际所规定，体现物质决定意识。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题写明“要尊重客观规律”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则把顺势而为、因地制宜直接归入尊重客观规律。",
        "answer_landing": "治水必须尊重水流、地势和生态规律，在规律允许的范围内进行工程设计和维护。",
    },
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题写明“尊重客观规律与发挥主观能动性相结合”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "评分细则同时要求规律和能动性，且材料有李冰率民修建、历代维护和现代智慧水利。",
        "answer_landing": "都江堰既顺应自然条件，又通过人的工程实践、技术维护和制度传承发挥能动作用。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题写明“同时发挥人的主观能动性，实现人与自然的和谐共生”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则明确把人的能动实践和正确治水理念列为哲学落点。",
        "answer_landing": "人在尊重规律基础上能动设计、修建、维护并创新表达治水智慧，推动工程持续发挥作用。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题联系观部分写明“治水并非单一工程，而是兼顾防洪、灌溉、生态等多重效益”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则直接要求用联系观分析都江堰多重功能和内在联系。",
        "answer_landing": "都江堰要从防洪、灌溉、生态、文化传承等相互联系的方面整体理解。",
    },
    {
        "canonical_node": "联系的客观性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题联系观部分写明“体现了联系的普遍性、客观性和多样性”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则直接点名联系的客观性，且材料中的水势、地势、工程功能联系不以人的意志为转移。",
        "answer_landing": "都江堰的治水功能建立在客观水文地理联系之上，必须按照这些客观联系组织工程。",
    },
    {
        "canonical_node": "联系的多样性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题联系观部分写明“体现了联系的普遍性、客观性和多样性”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则直接点名联系的多样性，材料兼含防洪、灌溉、生态、教育和文化表达。",
        "answer_landing": "治水智慧要把握不同类型联系，统筹自然工程、民生效益、生态保护和文化传承。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题联系观括注“系统观念/整体部分”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则在联系观下明确给出系统观念，材料也呈现多功能、多时代、多主体的系统治理。",
        "answer_landing": "都江堰的持续运行依赖系统优化，把工程保护、水资源治理、污染防治和文化传播统筹起来。",
    },
    {
        "canonical_node": "整体与部分",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题联系观括注“系统观念/整体部分”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则以括注形式支持整体部分角度，属于正式细则宽角度支持。",
        "answer_landing": "都江堰各工程环节和治理措施要服务整体治水目标，整体功能又通过各部分协同实现。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题发展观部分写明“体现了事物是不断变化发展的，要与时俱进、开拓创新”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则直接点名发展观，并把历代维护和“智水”时代升级作为材料分析。",
        "answer_landing": "都江堰不是静止遗产，而是在历代维护和现代科技赋能中持续发展、不断焕发生机。",
    },
    {
        "canonical_node": "事物发展是前进性与曲折性的统一",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题发展观括注“前途光明道路曲折”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则以括注形式给出前进性与曲折性，材料也有“艰难曲折不能阻挡历史前进”的提示。",
        "answer_landing": "都江堰跨越千年说明发展方向具有前进性，但维护、治理和升级过程也会经历艰难曲折。",
    },
    {
        "canonical_node": "量变与质变 / 适度原则",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题发展观括注“质变量变”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则以括注形式给出量变质变，适合登记为正式细则宽角度支持。",
        "answer_landing": "历代持续维护、技术迭代和文化表达创新不断积累，推动都江堰保护利用水平提升。",
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题写明“辩证否定观：守正创新是对传统治水智慧的继承与发展”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则明确辩证否定是联系和发展的环节，实质是扬弃。",
        "answer_landing": "守正创新既保留因势利导等核心智慧，又结合现代科技和传播方式实现升级。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题唯物史观部分写明“人民群众是历史的创造者”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "细则把李冰率领民众和历代治水者接力维护直接落到人民群众创造历史。",
        "answer_landing": "治水智慧源于人民实践，人民群众既创造工程和物质财富，也创造并传承治水文化。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式细则第16题价值观部分写明“自觉站在最广大人民群众的立场上”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
        "why_trigger": "站在最广大人民群众立场上是价值判断与价值选择的正式教材落点，且出自评分细则。",
        "answer_landing": "治水利民体现正确价值判断和价值选择，把人民利益作为治理、维护和创新的根本尺度。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式细则第21题写明“坚守人民立场”“以人民为中心，增进民生福祉”。",
        "question_prompt": "结合材料，综合运用所学，阐释我国是如何为中国式现代化建设谱写宏伟篇章的。",
        "why_trigger": "细则把发展成果转化为群众获得感、幸福感并增强人民参与积极性列为得分点。",
        "answer_landing": "中国式现代化建设要坚持人民主体地位，使发展成果更多更公平惠及人民并激发人民参与。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式细则第21题思维方法角度列明“尊重客观规律”。",
        "question_prompt": "结合材料，综合运用所学，阐释我国是如何为中国式现代化建设谱写宏伟篇章的。",
        "why_trigger": "细则明确把尊重客观规律作为可得分的思维方法角度。",
        "answer_landing": "谋划和推进中国式现代化要把握经济社会发展规律，根据实际形势制定和实施规划。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式细则第21题思维方法角度列明“运用系统观念”。",
        "question_prompt": "结合材料，综合运用所学，阐释我国是如何为中国式现代化建设谱写宏伟篇章的。",
        "why_trigger": "细则明确系统观念可给分，材料涉及科技、开放、民生、发展等多维统筹。",
        "answer_landing": "推进中国式现代化要系统统筹创新、开放、民生和发展安全，把多方面建设协同起来。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式细则第21题写明“坚持联系观，国内协同与内外联动，推动中国式现代化进程”。",
        "question_prompt": "结合材料，综合运用所学，阐释我国是如何为中国式现代化建设谱写宏伟篇章的。",
        "why_trigger": "细则直接点名联系观，并要求分析国内协同与内外联动。",
        "answer_landing": "中国式现代化建设要坚持联系观点，把国内发展、科技自立、对外开放和民生改善联动起来。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式细则第21题写明“坚持实践观，勇于探索中国式现代化理论、道路”。",
        "question_prompt": "结合材料，综合运用所学，阐释我国是如何为中国式现代化建设谱写宏伟篇章的。",
        "why_trigger": "细则直接给出实践观，材料也有理论创新引领实践创新和规划实施。",
        "answer_landing": "中国式现代化道路在实践探索中形成并发展，理论创新又引领新的实践推进。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式细则第21题写明“坚持正确的价值判断，价值选择”。",
        "question_prompt": "结合材料，综合运用所学，阐释我国是如何为中国式现代化建设谱写宏伟篇章的。",
        "why_trigger": "细则直接点名价值判断和价值选择，是正式评分源，不是普通参考答案替代。",
        "answer_landing": "推进中国式现代化要作出符合人民利益和社会发展规律的价值判断与价值选择。",
    },
]


BOUNDARY_ROWS = [
    ("Q1", "政治选择题", "党的领导/人民立场", "正式答案键1A；题干考查党的性质宗旨、使命任务和人民性，作为政治模块边界排除。", "正式答案键+试卷原题", "POLITICAL_MODULE_BOUNDARY_EXCLUDED"),
    ("Q2", "经济选择题", "新型城镇化/公共服务", "正式答案键2D；题干考查城镇化与基本公共服务，属于经济与社会/政策模块。", "正式答案键+试卷原题", "ECONOMICS_POLICY_BOUNDARY_EXCLUDED"),
    ("Q3", "经济选择题", "企业经营/市场定位", "正式答案键3B；题干考查企业差异化、市场定位与经营策略，不进入必修四哲学正文。", "正式答案键+试卷原题", "ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q4", "政治法治选择题", "公共法律服务/法治建设", "正式答案键4D；公共法律服务与法治建设语境，不转换为哲学价值观正文。", "正式答案键+试卷原题", "POLITICAL_LAW_BOUNDARY_EXCLUDED"),
    ("Q5-nonphilosophy", "基层治理选择题非哲学点", "基层治理/多元主体/政治治理", "本题只把正确选项中的群众观念、系统思维登记为客观哲学挂点，其余基层治理制度与主体协同内容作为政治治理边界。", "正式答案键+试卷原题", "PARTIAL_BODY_PARTIAL_BOUNDARY"),
    ("Q6", "文化选择题", "文明交流互鉴/文化认同", "正式答案键6A；汤莎同台启示属于文化交流互鉴，不进入哲学正文。", "正式答案键+试卷原题", "CULTURE_BOUNDARY_EXCLUDED"),
    ("Q10", "逻辑与法律选择题", "逻辑思维/法学研究", "正式答案键10B；题干明确为逻辑思维在法学研究和实践中的方法工具，选必三逻辑边界。", "正式答案键+试卷原题", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q11", "逻辑与思维选择题", "感性具体/思维抽象/思维具体", "正式答案键11C；虽含认识过程词汇，但考查选必三思维抽象路径，不作必修四实践认识正文。", "正式答案键+试卷原题", "XUANBISAN_THINKING_BOUNDARY_EXCLUDED"),
    ("Q12", "法律选择题", "遗嘱/遗赠扶养协议", "正式答案键12A；法律与生活继承规则，边界排除。", "正式答案键+试卷原题", "LEGAL_BOUNDARY_EXCLUDED"),
    ("Q13", "法律选择题", "著作权/举证责任", "正式答案键13C；著作权侵权与举证规则，边界排除。", "正式答案键+试卷原题", "LEGAL_BOUNDARY_EXCLUDED"),
    ("Q14", "经济开放选择题", "海南自由贸易港/制度型开放", "正式答案键14A；高水平对外开放和开放型经济，边界排除。", "正式答案键+试卷原题", "ECONOMICS_OPENING_BOUNDARY_EXCLUDED"),
    ("Q15", "国际经济选择题", "企业出海/伙伴国家发展", "正式答案键15B；国际经济合作与企业价值链，不进入哲学正文。", "正式答案键+试卷原题", "INTERNATIONAL_ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q16-culture", "哲学文化主观题中的文化点", "民族精神/优秀传统文化/文化创新/文化作用", "正式细则第16题文化角度支持民族精神、优秀传统文化创造性转化和创新性发展等，本批只登记哲学节点，文化模块作为边界。", "正式评分细则", "CULTURE_POINTS_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q17", "政治与法治主观题", "中轴线法治保护/人大政府司法", "正式细则第17题限定政治与法治，考查科学立法、依法行政、法治宣传等，不进入哲学正文。", "正式评分细则", "POLITICAL_LAW_BOUNDARY_EXCLUDED"),
    ("Q18", "经济主观题", "快递业/创新驱动/消费/乡村振兴", "正式细则第18题限定经济与社会，虽有以人民为中心等词，但服务经济高质量发展分析，不偷换为哲学正文。", "正式评分细则", "ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q19(1)", "法律与生活主观题", "相邻权/加装电梯/核心价值观", "正式细则第19(1)题为民法典相邻关系与判决意义，核心价值观处于法律评价意义中，边界排除。", "正式评分细则", "LEGAL_BOUNDARY_EXCLUDED"),
    ("Q19(2)", "逻辑与思维主观题", "充分条件/必要条件假言推理", "正式细则第19(2)题限定逻辑与思维假言推理规则，边界排除。", "正式评分细则", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q20", "当代国际政治与经济主观题", "全球治理倡议/国际秩序/人类命运共同体", "正式细则第20题限定当代国际政治与经济，国际治理语境不进入必修四哲学正文。", "正式评分细则", "XUANBIYI_BOUNDARY_EXCLUDED"),
    ("Q21-nonphilosophy", "综合主观题非哲学点", "党的领导/高质量发展/对外开放/科技自立自强", "正式细则第21题还支持党的领导、高质量发展、高水平对外开放和科技自立等，本批只登记细则明确支持的哲学思维节点。", "正式评分细则", "NON_PHILOSOPHY_POINTS_BOUNDARY_EXCLUDED"),
    ("Q21-broad-thinking", "综合主观题宽泛思维点", "科学思维/辩证思维/矛盾观", "正式细则第21题宽泛列出科学思维、辩证思维、矛盾观；由于未落到具体矛盾节点，本批不把宽词强行放入某个矛盾正文节点。", "正式评分细则宽角度", "BROAD_TERM_NOT_FORCED_INTO_BODY"),
]


def current_docx() -> Path:
    return core.current_docx()


def para_text(p) -> str:
    return core.para_text(p)


def style_val(p) -> str:
    return core.style_val(p)


def parse_question_no(heading: str) -> str:
    m = re.search(r"第(\d+)题(?:第（(\d+)）问)?", heading)
    if not m:
        return "Q?"
    return f"Q{m.group(1)}" + (f"({m.group(2)})" if m.group(2) else "")


def extract_entries_from_root(root) -> list[dict[str, str]]:
    entries = []
    current_node = ""
    current = None
    parts = []
    for p in root.xpath("//w:p", namespaces=NS):
        text = para_text(p)
        if not text:
            continue
        style = style_val(p)
        if style in {"3", "4", "5"}:
            if current is not None:
                current["student_facing_text"] = "\n".join(parts)
                entries.append(current)
                current = None
                parts = []
            if style == "4":
                current_node = text
            if style == "5" and SUITE in text:
                current = {
                    "canonical_node": current_node,
                    "registered_heading": text,
                    "question_no": parse_question_no(text),
                }
                parts = [text]
        elif current is not None:
            parts.append(text)
    if current is not None:
        current["student_facing_text"] = "\n".join(parts)
        entries.append(current)
    entries.sort(key=lambda e: (int(re.sub(r"\D", "", e["question_no"]) or "999"), e["canonical_node"], e["registered_heading"]))
    return entries


def set_para_text(p, text: str) -> None:
    texts = p.xpath(".//w:t", namespaces=NS)
    if not texts:
        r = etree.SubElement(p, f"{W}r")
        t = etree.SubElement(r, f"{W}t")
        t.text = text
        return
    texts[0].text = text
    for t in texts[1:]:
        t.text = ""


def clone_with_text(template, text: str):
    p = etree.fromstring(etree.tostring(template))
    set_para_text(p, text)
    return p


def load_docx_xml(docx: Path):
    with zipfile.ZipFile(docx, "r") as zf:
        return etree.fromstring(zf.read("word/document.xml"))


def remove_unsupported_existing_entries(body) -> int:
    paras = body.findall(f"{W}p")
    current_node = ""
    remove_indexes: set[int] = set()
    idx = 0
    while idx < len(paras):
        p = paras[idx]
        text = para_text(p)
        style = style_val(p)
        if style == "4":
            current_node = text
        if style == "5" and SUITE in text and (parse_question_no(text), current_node) in REMOVE_EXISTING_SIGNATURES:
            remove_indexes.add(idx)
            j = idx + 1
            while j < len(paras) and style_val(paras[j]) not in {"3", "4", "5"}:
                remove_indexes.add(j)
                j += 1
            idx = j
            continue
        idx += 1
    for idx in sorted(remove_indexes, reverse=True):
        body.remove(paras[idx])
    return len([i for i in remove_indexes if style_val(paras[i]) == "5"])


def update_docx(timestamp: str) -> tuple[Path, int, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch34_2026_tongzhou_final_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
    root = etree.fromstring(xml)
    body = root.find(f"{W}body")
    removed = remove_unsupported_existing_entries(body)
    paras = body.findall(f"{W}p")
    existing_signature = {(e["canonical_node"], e["question_no"]) for e in extract_entries_from_root(root)}
    inserted = 0
    for spec_item in NEW_ENTRY_SPECS:
        signature = (spec_item["canonical_node"], spec_item["question_no"])
        if signature in existing_signature:
            continue
        node = spec_item["canonical_node"]
        heading = f"{core.base.next_heading_number(paras, node)}. {SUITE} {spec_item['question_label']}"
        heading_template, body_template = core.base.template_paragraphs(paras, node)
        _start, end = core.base.find_node_bounds(paras, node)
        insert_index = body.index(paras[end - 1]) + 1
        new_paras = [
            clone_with_text(heading_template, heading),
            clone_with_text(body_template, f"【材料触发点】{spec_item['material_trigger']}"),
            clone_with_text(body_template, f"【设问】{spec_item['question_prompt']}"),
            clone_with_text(body_template, f"【为什么能想到】{spec_item['why_trigger']}"),
            clone_with_text(body_template, f"【答案落点】{spec_item['answer_landing']}"),
        ]
        for offset, p in enumerate(new_paras):
            body.insert(insert_index + offset, p)
        inserted += 1
        existing_signature.add(signature)
        paras = body.findall(f"{W}p")
    with tempfile.TemporaryDirectory() as td:
        tmp_docx = Path(td) / docx.name
        with zipfile.ZipFile(docx, "r") as zin, zipfile.ZipFile(tmp_docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
                zout.writestr(item, data)
        shutil.copy2(tmp_docx, docx)
    return backup, inserted, removed


def evidence_for(entry: dict[str, str]) -> tuple[str, str]:
    return EVIDENCE_BY_KEY.get((entry["question_no"], entry["canonical_node"]), ("NEED_EVIDENCE_REVIEW", "unmapped-current-docx-entry"))


EVIDENCE_BY_KEY = {
    ("Q5", "人民群众"): ("正式答案键5C；正确选项含“基层问题的治理必须坚持群众观念”，仅作客观选择题挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q5", "系统观念 / 系统优化"): ("正式答案键5C；正确选项含“系统思维和辩证思维”，仅作客观选择题挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q7", "发展的观点 / 发展的普遍性"): ("正式答案键7B；正确选项①对应“事物是不断变化发展的”，仅作客观选择题挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q7", "量变与质变 / 适度原则"): ("正式答案键7B；正确选项④对应“量变是质变的必要准备，要重视量的积累”，仅作客观选择题挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q8", "根据固有联系建立新的具体联系"): ("正式答案键8D；正确选项③写明通过刺绣建立承载家国情怀的人为事物联系。", "objective-choice-only-teacher-answer-key"),
    ("Q8", "矛盾就是对立统一"): ("正式答案键8D；正确选项④写明个体差异性与民族记忆整体性在作品中对立统一。", "objective-choice-only-teacher-answer-key"),
    ("Q9", "系统观念 / 系统优化"): ("正式答案键9D；正确选项写明运用系统化、数字化模式整合保障资源，形成新机制。", "objective-choice-only-teacher-answer-key"),
    ("Q16", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("正式细则第16题哲学角度写明“坚持一切从实际出发，实事求是”。", "formal-rubric"),
    ("Q16", "物质决定意识"): ("正式细则第16题唯物论角度写明“体现了物质决定意识”。", "formal-rubric"),
    ("Q16", "规律的客观性"): ("正式细则第16题写明“要尊重客观规律”。", "formal-rubric"),
    ("Q16", "尊重客观规律与发挥主观能动性相结合"): ("正式细则第16题写明“尊重客观规律与发挥主观能动性相结合”。", "formal-rubric"),
    ("Q16", "主观能动性 / 意识的能动作用"): ("正式细则第16题写明“同时发挥人的主观能动性，实现人与自然的和谐共生”。", "formal-rubric"),
    ("Q16", "联系的普遍性 / 联系的观点（总）"): ("正式细则第16题联系观部分写明“体现了联系的普遍性、客观性和多样性”。", "formal-rubric"),
    ("Q16", "联系的客观性"): ("正式细则第16题联系观部分直接点名联系的客观性。", "formal-rubric"),
    ("Q16", "联系的多样性"): ("正式细则第16题联系观部分直接点名联系的多样性。", "formal-rubric"),
    ("Q16", "系统观念 / 系统优化"): ("正式细则第16题联系观括注“系统观念/整体部分”。", "formal-rubric-term-support"),
    ("Q16", "整体与部分"): ("正式细则第16题联系观括注“系统观念/整体部分”。", "formal-rubric-broad-angle"),
    ("Q16", "发展的观点 / 发展的普遍性"): ("正式细则第16题发展观部分写明事物不断变化发展、与时俱进、开拓创新。", "formal-rubric"),
    ("Q16", "事物发展是前进性与曲折性的统一"): ("正式细则第16题发展观括注“前途光明道路曲折”。", "formal-rubric-broad-angle"),
    ("Q16", "量变与质变 / 适度原则"): ("正式细则第16题发展观括注“质变量变”。", "formal-rubric-broad-angle"),
    ("Q16", "辩证否定 / 守正创新"): ("正式细则第16题写明辩证否定观、守正创新、扬弃。", "formal-rubric"),
    ("Q16", "人民群众"): ("正式细则第16题唯物史观部分写明“人民群众是历史的创造者”。", "formal-rubric"),
    ("Q16", "价值判断与价值选择"): ("正式细则第16题价值观部分写明“自觉站在最广大人民群众的立场上”。", "formal-rubric-term-support"),
    ("Q21", "人民群众"): ("正式细则第21题写明坚守人民立场、以人民为中心、增进民生福祉。", "formal-rubric"),
    ("Q21", "规律的客观性"): ("正式细则第21题思维方法角度列明“尊重客观规律”。", "formal-rubric-term-support"),
    ("Q21", "系统观念 / 系统优化"): ("正式细则第21题思维方法角度列明“运用系统观念”。", "formal-rubric"),
    ("Q21", "联系的普遍性 / 联系的观点（总）"): ("正式细则第21题写明“坚持联系观，国内协同与内外联动”。", "formal-rubric"),
    ("Q21", "实践与认识（总）"): ("正式细则第21题写明“坚持实践观，勇于探索中国式现代化理论、道路”。", "formal-rubric"),
    ("Q21", "价值判断与价值选择"): ("正式细则第21题直接写明“坚持正确的价值判断，价值选择”。", "formal-rubric"),
}


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        ledger_rows = list(reader)
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch34_2026_tongzhou_final_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    existing_keys = {(r.get("canonical_node"), r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in ledger_rows}
    added_ledger = 0
    for e in entries:
        row = {"canonical_node": e["canonical_node"], "source_suite": SUITE, "question_no": e["question_no"], "inserted_heading": e["registered_heading"]}
        key = (row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in existing_keys:
            ledger_rows.append(row)
            existing_keys.add(key)
            added_ledger += 1
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(ledger_rows)

    accepted_records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch34_2026_tongzhou_final_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup_accepted)
    accepted_keys = {(r.get("source_suite"), r.get("question_no"), r.get("canonical_node"), r.get("registered_heading")) for r in accepted_records}
    added_accepted = 0
    with ACCEPTED.open("a", encoding="utf-8") as f:
        for e in entries:
            evidence, boundary = evidence_for(e)
            record = {
                "source_suite": SUITE,
                "question_no": e["question_no"],
                "framework_node": e["canonical_node"],
                "canonical_node": e["canonical_node"],
                "student_facing_text": e["student_facing_text"],
                "evidence_level": evidence,
                "boundary_note": boundary,
                "source_lane": "Codex Batch34 Tongzhou final registration and insertion",
                "source_repair_basis": SOURCE_PACKET,
                "source_lines": SOURCE_PACKET,
                "batch": BATCH_ID,
                "registered_heading": e["registered_heading"],
            }
            key = (record["source_suite"], record["question_no"], record["canonical_node"], record["registered_heading"])
            if key in accepted_keys:
                continue
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            accepted_keys.add(key)
            added_accepted += 1
    return {"ledger_added": added_ledger, "accepted_added": added_accepted, "ledger_backup": str(backup), "accepted_backup": str(backup_accepted)}


def matrix_body_row(next_id: int, entry: dict[str, str]) -> dict[str, str]:
    evidence, boundary = evidence_for(entry)
    is_objective = boundary.startswith("objective-choice-only")
    is_broad = boundary in {"formal-rubric-broad-angle", "formal-rubric-term-support"}
    return {
        "matrix_row_id": f"M{next_id:04d}",
        "row_source": MATRIX_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": entry["question_no"],
        "题型或模块判断": "必修四哲学选择题客观挂点" if is_objective else "必修四哲学正文条目",
        "是否进宝典": "是：客观选择题挂点，已在当前DOCX正文登记" if is_objective else "是：已进入当前DOCX/PDF正文",
        "宝典节点": entry["canonical_node"],
        "细则支持原理": evidence,
        "证据等级": "正式答案键+试卷原题（客观选择题）" if is_objective else ("正式评分标准宽角度/术语支持" if is_broad else "正式评分标准"),
        "是否误放": "否：保留但标注宽角度或客观挂点" if (is_objective or is_broad) else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch34登记；普通参考答案只作题面/答案键核对，未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch34_2026_tongzhou_final_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    rows = [r for r in rows if not (r.get("题源") == SUITE and r.get("row_source") == MATRIX_SOURCE)]
    max_id = 0
    for r in rows:
        m = re.match(r"M(\d+)", r.get("matrix_row_id", ""))
        if m:
            max_id = max(max_id, int(m.group(1)))
    new_rows = []
    next_id = max_id + 1
    for e in entries:
        new_rows.append(matrix_body_row(next_id, e))
        next_id += 1
    for q, qtype, node, support, evidence, status in BOUNDARY_ROWS:
        new_rows.append({
            "matrix_row_id": f"M{next_id:04d}",
            "row_source": MATRIX_SOURCE,
            "题源": SUITE,
            "年份": YEAR,
            "阶段": STAGE,
            "题号": q,
            "题型或模块判断": qtype,
            "是否进宝典": "否：模块边界排除",
            "宝典节点": node,
            "细则支持原理": support,
            "证据等级": evidence,
            "是否误放": "否",
            "是否需补厚": "否" if status != "BROAD_TERM_NOT_FORCED_INTO_BODY" else "是：若后续要进矛盾节点，必须补充更具体细则落点",
            "当前处理": status,
            "备注": "本题或本点不作为当前哲学宝典正文；不把法律、文化、逻辑与思维、政治经济或普通参考答案偷换为哲学原理。",
            "source_artifact": SOURCE_PACKET,
        })
        next_id += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    body_rows = sum(1 for r in new_rows if r["是否进宝典"].startswith("是"))
    return {
        "matrix_rows_total": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "body_rows": body_rows,
        "boundary_rows": len(new_rows) - body_rows,
        "matrix_backup": str(backup),
    }


def update_global_audit(docx_entries: int, matrix_rows_for_suite: int) -> dict[str, int]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        raw = row.get("raw_suite", "")
        normalized = row.get("normalized_suite", "")
        if normalized == SUITE or raw == SUITE:
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = str(matrix_rows_for_suite)
            row["current_docx_mentions"] = str(docx_entries)
            row["current_status"] = "covered_by_batch34_recovery_matrix"
            row["blocker_or_next_action"] = "Batch34 inserted/registered formal-rubric and objective-choice entries plus question-level boundary rows; render/model gates pending."
        if normalized == "2026石景山期末" or raw == "2026石景山期末":
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = row.get("matrix_rows") or "0"
            row["current_docx_mentions"] = row.get("current_docx_mentions") or "0"
            row["current_status"] = "special_excluded_no_usable_scoring_rubric_user_confirmed"
            row["blocker_or_next_action"] = "User confirmed no usable scoring rubric; do not process unless a real scoring/rubric source is supplied."
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    missing = [r for r in rows if r.get("current_status") == "missing_from_current_47_suite_audit_scope"]
    covered_or_excluded = [r for r in rows if r.get("current_status") != "missing_from_current_47_suite_audit_scope"]
    missing_table = "\n".join(f"| {r['normalized_suite']} | {r['stage_dir']} | {r['current_status']} | {r['blocker_or_next_action']} |" for r in missing)
    if not missing_table:
        missing_table = "| none | none | none | all processable midterm/final raw suites are covered locally or special-excluded |"
    GLOBAL_AUDIT_MD.write_text(f"""# Global Raw Suite Exhaustion Audit 2026-05-25

status: `GLOBAL_SOURCE_SCOPE_LOCAL_COVERAGE_CLOSED_RENDER_MODEL_GATES_REMAIN`

## Summary

- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(rows)}`
- current covered or special-excluded by recovery matrix/audit: `{len(covered_or_excluded)}`
- remaining processable midterm/final raw suites outside current coverage: `{len(missing)}`

## Remaining Missing Midterm/Final Suites

| suite | stage_dir | status | next action |
|---|---|---|---|
{missing_table}

## Batch34 Update

- `2026通州期末` is now covered locally by `COVERAGE_FUSION_BATCH34_2026_TONGZHOU_FINAL_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX governed entries for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` is special-excluded because no usable scoring rubric has been confirmed.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered_or_excluded), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch34 Source Transcription - 2026通州期末

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- formal scoring/rubric cache: `{RUBRIC_SOURCE}`
- teacher PDF cache: `{TEACHER_SOURCE}`
- raw rubric PPTX: `{RAW_RUBRIC_PPTX}`
- raw teacher PDF: `{RAW_TEACHER_PDF}`
- lecture/marking PPTX: `{RAW_LECTURE_PPTX}`

## Key Evidence

- Formal answer key: `1A, 2D, 3B, 4D, 5C, 6A, 7B, 8D, 9D, 10B, 11C, 12A, 13C, 14A, 15B`.
- Q5, Q7, Q8 and Q9 enter only as objective-choice hooks where the correct option text explicitly carries a philosophy trigger.
- Q16 formal scoring supports唯物论、联系观、发展观、辩证否定观、人民群众 and价值判断与价值选择；文化点 remain boundary rows.
- Q21 formal scoring supports人民立场、系统观念、尊重客观规律、联系观、实践观 and价值判断与价值选择；党的领导、经济发展、开放 and broad矛盾观 terms remain boundary rows unless later rubric detail is supplied.
- Q1-Q4, Q6, Q10-Q15, Q17-Q20 and non-philosophy parts are boundary-excluded.

## Governed DOCX Body Entries

{body_list}

## Evidence Guardrail

- 普通参考答案没有冒充评分细则。
- 选择题只登记为客观答案键证据。
- 主观题正文条只使用正式评分标准/细则支持。
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, removed: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch34 Local Application: 2026通州期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- New DOCX entries inserted: `{inserted}`.
- Unsupported pre-existing Tongzhou contradiction-node entries removed: `{removed}`.
- Governed DOCX entries after Batch34: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global processable raw-suite remaining gap after Batch34: `{global_result['remaining_missing']}`.
- `2026石景山期末` remains special-excluded because no usable scoring rubric is available.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch34 Local Application: 2026通州期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch34 Pending Render QA: 2026通州期末"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch34 Pending Render QA: 2026通州期末
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch34 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH34_TONGZHOU_FINAL_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH34_TONGZHOU_FINAL_RECHECK

status: `real_call_pending`

- Batch: `2026通州期末`.
- Prompt: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, removed: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch34 - 2026通州期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch34 edit: `{backup}`.
- New DOCX entries inserted: `{inserted}`.
- Unsupported pre-existing Tongzhou contradiction-node entries removed: `{removed}`.
- Governed DOCX entries for `2026通州期末` after Batch34: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026通州期末`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global processable raw-suite remaining gap after Batch34: `{global_result['remaining_missing']}`.

## Placement Verdict

- Q5, Q7, Q8 and Q9 enter only as objective-choice body hooks with evidence level `正式答案键+试卷原题（客观选择题）`.
- Q16 enters through formal scoring support for materialism, law/respect, subjective initiative, connection, development, dialectical negation, people and value stance.
- Q21 enters through formal scoring support for people, law/respect, system view, connection view, practice view and value judgment/choice.
- Q1-Q4, Q6, Q10-Q15, Q17-Q20 and non-philosophy parts of Q16/Q21 are boundary-excluded.
- Broad `矛盾观` in Q21 is not forced into a specific contradiction node without a more precise scoring landing.
- Ordinary teacher reference answers are kept as context only and do not substitute for formal scoring text.

## Remaining Gates

- Render QA is pending because Batch34 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""", encoding="utf-8", newline="\n")


def main() -> None:
    for required in [
        GPT_BUNDLE,
        RUBRIC_SOURCE,
        TEACHER_SOURCE,
        RAW_RUBRIC_PPTX,
        RAW_TEACHER_PDF,
        RAW_LECTURE_PPTX,
        MATRIX,
        LEDGER,
        ACCEPTED,
    ]:
        if not required.exists():
            raise FileNotFoundError(required)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted, removed = update_docx(timestamp)
    root = load_docx_xml(current_docx())
    entries = extract_entries_from_root(root)
    if len(entries) != EXPECTED_ENTRIES:
        raise RuntimeError(f"Expected {EXPECTED_ENTRIES} governed {SUITE} entries after Batch34, found {len(entries)}")
    unmapped = [e for e in entries if evidence_for(e)[0] == "NEED_EVIDENCE_REVIEW"]
    if unmapped:
        raise RuntimeError(f"Unmapped evidence rows: {unmapped}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), matrix_result["batch_rows"])
    write_source_transcription(entries)
    append_control_reports(inserted, removed, entries, matrix_result, global_result)
    write_batch_report(backup, inserted, removed, entries, ledger_result, matrix_result, global_result)
    print(json.dumps({
        "status": "batch34_local_applied_render_pending_model_pending",
        "inserted": inserted,
        "removed": removed,
        "entries": len(entries),
        "matrix": matrix_result,
        "global": global_result,
        "report": str(BATCH_REPORT),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
