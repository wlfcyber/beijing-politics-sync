#!/usr/bin/env python3
"""Codex supervisor repair pass for the 2026-05-02 ClaudeCode run.

This script does not rescan the whole corpus. It repairs the verified tail
failures found by the supervisor:
- clean audit/source wording out of student-facing fields;
- add the three missing suites that were proven non-empty by source review;
- write suite reports for those suites.
"""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02")
ENTRIES = ROOT / "audit" / "entries"
REPORTS = ROOT / "suite_reports"
AUDIT = ROOT / "audit"

STUDENT_FIELDS = ["材料触发点", "设问", "为什么能想到", "答案落点"]
FORBIDDEN_RE = re.compile(
    r"细则|评标|参考答案|答案写|答案核|答案/补充|可从.*角度|/Users/|\.pdf|\.docx|\.pptx|OCR|debug|slide|line id|file id|PASS|correct_option_chain|filled",
    re.I,
)


def backup_entries() -> None:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = AUDIT / f"codex_supervisor_backup_entries_{stamp}"
    if not dst.exists():
        shutil.copytree(ENTRIES, dst)
        print(f"backup entries -> {dst}")


def clean_field(entry_id: str, field: str, text: str) -> str:
    if not text:
        return ""
    s = text.strip()

    manual: dict[tuple[str, str], str] = {
        (
            "2024_朝阳_二模__Q16_2__价值观",
            "材料触发点",
        ): "材料围绕人工智能与人类未来关系展开：一方面看到人工智能技术推动社会进步的潜力，另一方面提醒技术风险、伦理边界和人类利益不能被忽视，强调人工智能应真正为人类发展服务。",
        (
            "2026_海淀_期末__Q16__两点论与重点论",
            "为什么能想到",
        ): "材料不只是让学生说 AI 有红利也有负面影响，而是在两面并存中追问应当把哪一面作为主要方面来抓。'恐怕''取代''弱化'等负向表达把'保有独立思考、深度思考、人的主体性'摆在重点位置。学生看到这种'两面同在但有明确价值取向'的材料，就要从两点论与重点论入手：既看到两面，又抓住主要方面。",
    }
    if (entry_id, field) in manual:
        return manual[(entry_id, field)]

    replacements = [
        ("（来自材料二/细则总览）", "（材料二）"),
        ("(细则)", ""),
        ("（细则）", ""),
        ("细则参考答案强调：", ""),
        ("细则核心考点列出", "材料中的关键词指向"),
        ("这正是细则7分加分项明确写出的'价值观具有导向作用'的原文等值表达。", "这正对应价值观具有导向作用。"),
        ("需注意细则规定'实践是认识的来源、目的'不给分，必须落到'唯一标准'或'认识发展的动力'。", "本题不是泛泛谈实践是认识的来源和目的，而要落到失败实践怎样检验认识、推动认识深化。"),
        ("注意细则给分关键是'量变是质变的前提和必要准备'，不能写成'必然前提'。", "这里要落到量的积累促成质的飞跃，不能把量变说成机械的必然前提。"),
    ]
    for old, new in replacements:
        s = s.replace(old, new)

    # Remove leading provenance sentences such as "细则Q16...。材料..."
    leading_patterns = [
        r"^细则[^。！？]*[。！？]\s*",
        r"^评分细则[^。！？]*[。！？]\s*",
        r"^参考答案[^。！？]*[。！？]\s*",
        r"^细则[^—]*——\s*",
        r"^细则[^：:]*[:：]\s*'[^']*'\s*。",
        r"^细则[^：:]*[:：]\s*“[^”]*”\s*。",
    ]
    changed = True
    while changed:
        changed = False
        for pat in leading_patterns:
            ns = re.sub(pat, "", s).strip()
            if ns != s and len(ns) >= 20:
                s = ns
                changed = True
                break

    # Remove residual "细则..." clause before a visible material explanation.
    s = re.sub(r"^细则[^。！？]*(材料[中里用把前后一二三四五六七八九十])", r"\1", s)
    s = re.sub(r"^细则[^。！？]*(学生看到)", r"\1", s)
    s = re.sub(r"^细则[^。！？]*(题目|本题|这道题)", r"\1", s)

    # Keep module-boundary content in audit fields, not student explanation.
    s = re.sub(r"本轮按必修四边界排除文化功能；", "", s)
    s = re.sub(r"【模块边界】[^。！？]*[。！？]", "", s)
    return s.strip()


def load_jsonl(path: Path) -> list[dict]:
    out: list[dict] = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def clean_existing_entries() -> None:
    changed = 0
    for path in sorted(ENTRIES.glob("*.jsonl")):
        rows = load_jsonl(path)
        if not rows:
            continue
        for e in rows:
            eid = e.get("entry_id", "")
            for fld in STUDENT_FIELDS:
                old = str(e.get(fld, ""))
                new = clean_field(eid, fld, old)
                if new != old:
                    e[fld] = new
                    changed += 1
        write_jsonl(path, rows)
    print(f"cleaned student fields: {changed}")


def entry(**kw: str | int | bool) -> dict:
    data = dict(kw)
    data.setdefault("user_hard_sample", False)
    return data


def add_missing_entries() -> None:
    missing: dict[str, list[dict]] = {
        "2026_朝阳_期中": [
            entry(
                entry_id="2026_朝阳_期中__Q4__联系多样性",
                suite_id="2026_朝阳_期中",
                year=2026,
                district="朝阳",
                stage="期中",
                question_no="4",
                sub_part="",
                question_type="choice",
                target_node_path="辩证法/联系的观点 / 联系的多样性",
                node_subtask="全球治理倡议中多边协作与共性问题治理",
                evidence_level="answer-key",
                correct_option="A",
                correct_option_text="①把握联系的多样性，加强团结协作，反对单边主义；③聚焦全球共性问题，坚持共商共建共享的全球治理观",
                wrong_options=[
                    {"label": "②", "text": "厘清矛盾主次方面，提升发展中国家话语权和主导权", "error_type": "哲学术语错配/政治方向拔高", "note": "材料强调治理理念与团结协作，不是主次方面；发展中国家话语权不能表述为主导权"},
                    {"label": "④", "text": "坚持辩证的否定观，重新构建国际关系基本准则", "error_type": "否定观误用/推倒重来", "note": "材料说五大理念与联合国宪章宗旨原则一脉相承，不是重新构建基本准则"},
                ],
                rubric_excerpt="试卷参考答案选择题答案表：第4题 A。",
                材料触发点="全球治理倡议的五大理念与联合国宪章宗旨和原则一脉相承，顺应绝大多数国家共同期待；题肢①说加强团结协作、反对单边主义，题肢③说聚焦全球共性问题、坚持共商共建共享。",
                设问="践行全球治理倡议要（   ）",
                为什么能想到="全球治理不是单个国家、单一领域、单向行动能解决的事，而是多个国家、多个议题、多个行动主体之间相互联系的治理过程。学生看到'团结协作''共同期待''全球共性问题''共商共建共享'，就应想到联系具有多样性，要在复杂联系中把握合作路径。",
                答案落点="答案 A。践行全球治理倡议要把握国际社会复杂多样的联系，通过团结协作反对单边主义，并围绕全球共性问题坚持共商共建共享。②把全球治理说成发展中国家主导，政治方向拔高；④把一脉相承的国际规则说成重新构建，误用辩证否定观。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf 第2页第4题与第8页选择题答案表",
                sort_priority="choice",
            ),
            entry(
                entry_id="2026_朝阳_期中__Q18__矛盾对立统一",
                suite_id="2026_朝阳_期中",
                year=2026,
                district="朝阳",
                stage="期中",
                question_no="18",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/矛盾就是对立统一",
                node_subtask="辩证看待 AI 提供情绪价值",
                evidence_level="rubric-formal",
                rubric_excerpt="Q18 阅卷细则：总说可用矛盾的普遍性/对立统一/一分为二/全面的观点；既要看到人工智能在提供情绪价值方面的长处，也要看到其缺陷和弊端。",
                材料触发点="支持者强调 AI 聊天机器人能几乎实时回应、避免等待冷场、让用户自由表达负面情绪；反对者指出 AI 在情感共情和动机共情方面存在缺陷，长期依赖会削弱个体与他人真实互动能力。",
                设问="结合材料，从哲学角度，针对“是否应该使用AI提供情绪价值”问题，谈谈你的思考。",
                为什么能想到="材料把 AI 情绪陪伴的便利与风险成对摆出：一面是及时回应、情绪疏导，一面是共情缺陷、现实交往能力削弱。学生看到这种'同一事物内部有利有弊并存'的结构，就应从矛盾对立统一和全面观点切入，不能只支持或只反对。",
                答案落点="要辩证看待 AI 提供情绪价值：AI 作为工具有及时回应、辅助疏导情绪的积极作用，但也存在不能真正理解人类情感、可能削弱现实交往能力的局限；因此应坚持一分为二、全面看问题，在承认其辅助价值的同时防止过度依赖。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf 第6页第18题；细则/细则.docx Q18",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_朝阳_期中__Q18__具体问题具体分析",
                suite_id="2026_朝阳_期中",
                year=2026,
                district="朝阳",
                stage="期中",
                question_no="18",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/矛盾的观点 / 矛盾的特殊性",
                node_subtask="按用户真实需求具体分析 AI 使用边界",
                evidence_level="rubric-formal",
                rubric_excerpt="Q18 阅卷细则：支持理由可用按规律办事/从实际出发/矛盾特殊性或具体问题具体分析；材料可写具体分析用户需求、调整对话模式。",
                材料触发点="材料说用户可根据自身需求调教对话模式，无需担心被批判或暴露隐私，可自由表达负面情绪，AI 还能提供一些情绪疏导方法。",
                设问="结合材料，从哲学角度，针对“是否应该使用AI提供情绪价值”问题，谈谈你的思考。",
                为什么能想到="AI 情绪陪伴是否适合使用，不能脱离具体对象、具体情境、具体需求来一刀切。学生看到'根据自身需求调教对话模式''无需担心暴露隐私''排解愤怒和压力'，就应想到矛盾具有特殊性，要具体分析何种需求、何种程度、何种场景下可以辅助使用。",
                答案落点="可以在具体需求和具体场景中适度使用 AI 提供情绪价值：对短时压力排解、低风险情绪倾诉等需求，可根据用户实际调整对话模式，让 AI 作辅助工具；但要具体问题具体分析，不能把所有现实情感问题都交给 AI 处理。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf 第6页第18题；细则/细则.docx Q18",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_朝阳_期中__Q18__主观能动性",
                suite_id="2026_朝阳_期中",
                year=2026,
                district="朝阳",
                stage="期中",
                question_no="18",
                sub_part="",
                question_type="subjective",
                target_node_path="唯物论/主观能动性 / 意识的能动作用",
                node_subtask="人不能把真实情感互动完全让渡给 AI",
                evidence_level="rubric-formal",
                rubric_excerpt="Q18 阅卷细则：反对理由可用主观能动性/意识依赖于物质/适度原则、实践等；材料可写过度依赖人工智能会削弱现实的交往能力。",
                材料触发点="材料指出 AI 在情感共情和动机共情方面存在缺陷，无法真正理解或共鸣人类情感；长期依赖会让人不愿面对复杂现实冲突，退回 AI 构建的安全情绪泡泡中。",
                设问="结合材料，从哲学角度，针对“是否应该使用AI提供情绪价值”问题，谈谈你的思考。",
                为什么能想到="情绪理解、现实沟通和价值判断都需要人真实地参与生活实践，而不是把主动处理关系的能力交给工具。学生看到'无法真正理解或共鸣''削弱真实互动能力''模糊现实与虚拟界限'，就应想到人要发挥主观能动性，主动面对现实关系、调适情绪和解决冲突。",
                答案落点="不能把 AI 情绪陪伴当成现实交往的替代品。人要发挥主观能动性，主动在真实生活中理解他人、表达情绪、解决冲突；如果过度依赖 AI 的即时安慰，就可能削弱现实互动能力，模糊虚拟与现实的边界。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf 第6页第18题；细则/细则.docx Q18",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_朝阳_期中__Q18__价值判断与价值选择",
                suite_id="2026_朝阳_期中",
                year=2026,
                district="朝阳",
                stage="期中",
                question_no="18",
                sub_part="",
                question_type="subjective",
                target_node_path="价值观 / 人生观/价值判断与价值选择",
                node_subtask="用科技伦理规范 AI 情绪价值使用",
                evidence_level="rubric-formal",
                rubric_excerpt="Q18 阅卷细则：如何做可用辩证否定观/正确价值观的导向作用、价值判断价值选择；材料可写用正确科技伦理规范人工智能提供情绪价值方面的使用。",
                材料触发点="材料既承认 AI 能帮助用户排解愤怒和压力，又提醒过度依赖会削弱现实交往能力、模糊现实与虚拟界限，核心问题是技术使用应朝向人的真实成长而不是逃避现实。",
                设问="结合材料，从哲学角度，针对“是否应该使用AI提供情绪价值”问题，谈谈你的思考。",
                为什么能想到="面对技术工具，关键不是能不能用，而是按什么价值标准用、为谁的长远发展服务。学生看到'情绪疏导'和'情感依赖'的冲突，就应想到要作出正确价值判断和价值选择，用科技伦理约束 AI 的边界，让技术服务人的真实生活。",
                答案落点="使用 AI 提供情绪价值时，应作出正确价值判断和价值选择，坚持以人的健康成长和真实交往能力为标准，用科技伦理规范 AI 使用边界；让 AI 作为辅助疏导工具，而不是让人沉溺于虚拟安慰、逃避现实关系。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf 第6页第18题；细则/细则.docx Q18",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_朝阳_期中__Q18__辩证否定",
                suite_id="2026_朝阳_期中",
                year=2026,
                district="朝阳",
                stage="期中",
                question_no="18",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/辩证否定 / 守正创新",
                node_subtask="对 AI 情绪陪伴既不全盘否定也不全盘肯定",
                evidence_level="rubric-formal",
                rubric_excerpt="Q18 阅卷细则：如何做可用辩证否定观。",
                材料触发点="材料中的支持者看到 AI 实时回应、自由倾诉、情绪疏导的积极作用；反对者指出 AI 无法真正共情、长期依赖削弱现实交往能力。",
                设问="结合材料，从哲学角度，针对“是否应该使用AI提供情绪价值”问题，谈谈你的思考。",
                为什么能想到="材料不是要求学生简单站队，而是让学生在 AI 情绪陪伴的积极功能与消极风险之间作扬弃式处理。学生看到'有帮助但不能替代真实情感关系'，就应想到辩证否定：保留合理功能，克服不合理依赖。",
                答案落点="对 AI 提供情绪价值应坚持辩证否定：保留其即时回应、辅助疏导、低压力表达等合理功能，同时克服把 AI 当作真实关系替代品的过度依赖，通过规范使用让技术更好服务人的情感健康。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf 第6页第18题；细则/细则.docx Q18",
                sort_priority="main_question",
            ),
        ],
        "2026_丰台_期末": [
            entry(
                entry_id="2026_丰台_期末__Q16__矛盾对立统一",
                suite_id="2026_丰台_期末",
                year=2026,
                district="丰台",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/矛盾就是对立统一",
                node_subtask="留白的疏密张弛",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 细则哲学角度：留白，于疏密间见张弛，于空白处藏深意，体现矛盾双方对立统一，相互对立、相互依存。",
                材料触发点="材料说留白'于疏密间见张弛，于空白处藏深意'，既能让山林溪谷、高楼绿地形成清润滋养的意境，也提醒过度留白可能以空旷无奈冲淡意境。",
                设问="结合材料，运用《哲学与文化》知识，谈谈你对留白的理解。",
                为什么能想到="留白的美感恰恰来自'有'与'无'、'疏'与'密'、'实'与'虚'之间的相互依存：没有实体内容，空白无所依托；没有空白，内容又会拥挤失去张弛。学生看到'疏密''空白处藏深意''过度留白'，就应想到矛盾双方对立统一。",
                答案落点="留白体现矛盾双方的对立统一。有形内容与空白空间相互对立又相互依存，适当留白能让山林溪谷、高楼绿地等元素形成张弛有度的整体意境；但过度留白又会走向空旷虚无，所以理解留白要看到对立双方的统一。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/试卷/试卷.pdf 第6页渲染图；细则/细则.pdf 第4页",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_丰台_期末__Q16__量变质变适度",
                suite_id="2026_丰台_期末",
                year=2026,
                district="丰台",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/量变与质变 / 适度原则",
                node_subtask="留白的度",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 细则哲学角度：量变是质变的必要准备，质变是量变的必然结果；留白的“度”是关键，适度留白涵养生机、积蓄力量，过度留白会化为空旷、走向虚无，要把握适度原则。",
                材料触发点="材料说留白能'滋养万物之灵'、'以方寸绿意涵养共生之美'，但又明确提醒过度留白可能让空间走向空旷无奈、冲淡意境。",
                设问="结合材料，运用《哲学与文化》知识，谈谈你对留白的理解。",
                为什么能想到="同样是留白，数量和程度不同，效果会发生变化：适度时是生机、张弛和深意，过度时变成空旷和虚无。学生看到'适度有美感，过度有反效果'，就应想到量变质变关系和适度原则。",
                答案落点="留白要坚持适度原则。适度留白能在空间中涵养生机、积蓄力量，形成张弛有度的审美效果；如果留白过度，就可能从含蓄深意转向空旷虚无。因此把握留白，关键是把握好量的界限。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/试卷/试卷.pdf 第6页渲染图；细则/细则.pdf 第4页",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_丰台_期末__Q16__整体与部分联系",
                suite_id="2026_丰台_期末",
                year=2026,
                district="丰台",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/整体与部分",
                node_subtask="留白与周围事物构成整体意境",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 细则哲学角度：留白体现立足整体、正确处理整体与部分关系；留白与周围事物相互联系、相互影响，营造和谐有序的整体意境之美。",
                材料触发点="材料把留白放在山林间的溪谷、高楼旁的绿地、方寸绿意与周围环境的关系中理解，强调它能让周边元素相互滋养、形成整体意境。",
                设问="结合材料，运用《哲学与文化》知识，谈谈你对留白的理解。",
                为什么能想到="留白不是孤立的一块空地，它的价值取决于它与山林、高楼、绿地、喧嚣、沉静等周围要素怎样配合。学生看到'留白与周边事物共同营造意境'，就应想到整体与部分的关系以及联系观点。",
                答案落点="留白体现立足整体、正确处理整体与部分关系。空白本身只是部分，只有与山林溪谷、高楼绿地等要素相互联系、相互影响，才能营造和谐有序的整体意境之美；因此理解留白要把它放进整体空间关系中把握。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/试卷/试卷.pdf 第6页渲染图；细则/细则.pdf 第4页",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_丰台_期末__Q16__规律与能动性",
                suite_id="2026_丰台_期末",
                year=2026,
                district="丰台",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="唯物论/尊重客观规律与发挥主观能动性相结合",
                node_subtask="营造和谐美好意境",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 细则哲学角度：留白需要人们在尊重客观规律的基础上充分发挥主观能动性，才能营造出和谐美好的整体意境。",
                材料触发点="材料把留白理解为'生态宜居'和'以虚无从容自在'，既涉及空间、生态、审美的客观规律，也需要设计者主动安排疏密、虚实和尺度。",
                设问="结合材料，运用《哲学与文化》知识，谈谈你对留白的理解。",
                为什么能想到="好的留白不是随意空出来，而是在尊重生态空间规律、审美规律和人的生活需要基础上进行主动设计。学生看到'生态宜居''疏密张弛''过度会破坏意境'，就应想到尊重客观规律与发挥主观能动性相结合。",
                答案落点="营造留白之美，要在尊重客观规律基础上发挥主观能动性：既尊重空间生态、审美和生活规律，又主动设计疏密、虚实和尺度，让留白服务生态宜居和整体意境，而不是随意制造空旷。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/试卷/试卷.pdf 第6页渲染图；细则/细则.pdf 第4页",
                sort_priority="main_question",
            ),
        ],
        "2026_通州_期末": [
            entry(
                entry_id="2026_通州_期末__Q16__一切从实际出发",
                suite_id="2026_通州_期末",
                year=2026,
                district="通州",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="唯物论/一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
                node_subtask="因地制宜、顺势而为修建都江堰",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 评标 pptx：唯物论角度可用一切从实际出发，实事求是；李冰利用当地北高东南低的地理条件修建都江堰，做到因地制宜、顺势而为。",
                材料触发点="材料写李冰利用当地西北高、东南低的地理条件，率领民众历经艰难、勇于开拓，修建都江堰，治水利民，彰显'因地制宜、顺势而为'。",
                设问="结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
                为什么能想到="'当地西北高、东南低'是修建都江堰必须面对的客观地理条件，'因地制宜、顺势而为'就是按真实地形和水势作安排。学生看到这种'先看客观条件，再设计治水工程'的材料，就应想到一切从实际出发、实事求是。",
                答案落点="都江堰治水智慧首先体现一切从实际出发、实事求是。李冰不是凭主观想象治水，而是利用当地西北高、东南低的地理条件，因地制宜、顺势而为修建工程，使治水方案符合客观地形水势并服务民生。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf 第5-6页第16题；细则/细则.pptx slide 2-4",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_通州_期末__Q16__规律与能动性",
                suite_id="2026_通州_期末",
                year=2026,
                district="通州",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="唯物论/尊重客观规律与发挥主观能动性相结合",
                node_subtask="顺应自然水势并勇于开拓",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 评标 pptx：唯物论角度可用尊重客观规律与发挥主观能动性相结合；李冰利用地理条件，体现物质决定意识、尊重客观规律，同时发挥人的主观能动性，实现人与自然和谐共生。",
                材料触发点="材料一面写李冰利用当地地势和水势，另一方面写他率领民众历经艰难、勇于开拓，修建都江堰，治水利民。",
                设问="结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
                为什么能想到="都江堰既不是消极顺水漂流，也不是违背水势硬干，而是在顺应自然水势的基础上主动设计、组织民众、修建工程。学生看到'利用地理条件'和'勇于开拓'同时出现，就应想到尊重客观规律与发挥主观能动性相结合。",
                答案落点="都江堰跨越千年的智慧在于尊重客观规律与发挥主观能动性相结合：一方面顺应地形水势和自然规律，另一方面发挥人的主动创造能力组织治水工程，实现治水利民和人与自然和谐共生。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf 第5-6页第16题；细则/细则.pptx slide 2-4",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_通州_期末__Q16__联系观点",
                suite_id="2026_通州_期末",
                year=2026,
                district="通州",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/联系的观点 / 普遍联系",
                node_subtask="防洪灌溉生态文化多重效益",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 评标 pptx：联系观可写治水并非单一工程，而是兼顾防洪、灌溉、生态等多重效益，体现联系的普遍性、客观性和多样性，把握事物之间的内在联系。",
                材料触发点="材料把都江堰写成仍在使用的古代水利工程，并连接防洪灌溉、生态文明教育、爱国主义教育、中华优秀传统文化教育、智慧水资源保护和游客互动体验等多重功能。",
                设问="结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
                为什么能想到="都江堰不是一个孤立的水利设施，它把水势、工程、民生、生态、文化教育和旅游体验联系在一起。学生看到'防洪灌溉+生态教育+文化传承+智慧保护'，就应想到联系具有普遍性、多样性，要用联系的观点看治水智慧。",
                答案落点="都江堰体现联系观点：治水工程兼顾防洪、灌溉、生态、文化教育和文旅体验等多重效益，把自然水系、人民生活、生态保护和文化传承联系成整体；正是把握这些内在联系，才形成跨越千年的治水智慧。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf 第5-6页第16题；细则/细则.pptx slide 2-4",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_通州_期末__Q16__发展的观点",
                suite_id="2026_通州_期末",
                year=2026,
                district="通州",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/发展的观点 / 发展的普遍性",
                node_subtask="历代接力维护与智水升级",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 评标 pptx：发展观可写都江堰并非一蹴而就，历代治水者接力维护，如今迈入“智水”时代，通过科技赋能、文化表达创新实现持续升级，体现事物不断变化发展，要与时俱进、开拓创新。",
                材料触发点="材料说都江堰的修建并非一蹴而就，历代治水者接力维护，使其千年至今仍焕发生机；如今建设者迈入'智水'时代，构建智慧水资源保护与污染防治体系、科技赋能文物保护。",
                设问="结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
                为什么能想到="'并非一蹴而就''历代接力维护''迈入智水时代''持续升级'是一条清楚的发展链。学生看到一个古代工程在不同时代不断维护、升级和转化，就应想到事物是变化发展的，要用发展的观点看问题。",
                答案落点="都江堰治水智慧体现发展的观点。它不是一次修好后静止不变，而是在历代治水者接力维护中延续，又在今天通过智慧水资源保护、污染防治和科技赋能实现持续升级；这说明要与时俱进、开拓创新，使古代工程在新时代继续焕发生机。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf 第5-6页第16题；细则/细则.pptx slide 2-4",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_通州_期末__Q16__辩证否定守正创新",
                suite_id="2026_通州_期末",
                year=2026,
                district="通州",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="辩证法/辩证否定 / 守正创新",
                node_subtask="守正创新升级都江堰",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 评标 pptx：辩证否定观可写守正创新是对传统治水智慧的继承与发展，既保留“因势利导”的核心智慧，又结合现代科技、文化传播实现升级，体现辩证否定是联系的环节、发展的环节，实质是扬弃。",
                材料触发点="材料明确写建设者守正创新，迈入'智水'时代，构建智慧水资源保护与污染防治体系、科技赋能文物保护，同时创新放水节文化表达和游客互动体验。",
                设问="结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
                为什么能想到="'守正创新'就是题眼：都江堰保留'因势利导、顺势而为'的传统治水智慧，又用智慧水资源保护、科技赋能、情景剧和互动体验等新方式升级。学生看到'保留核心智慧+现代科技文化表达'，就应想到辩证否定的扬弃。",
                答案落点="都江堰的持续发展体现辩证否定和守正创新：既继承'因势利导'等传统治水智慧，又结合现代科技保护、水资源治理和文化传播方式实现升级；这种既保留又发展的扬弃，使都江堰在新时代继续发挥价值。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf 第5-6页第16题；细则/细则.pptx slide 2-4",
                sort_priority="main_question",
            ),
            entry(
                entry_id="2026_通州_期末__Q16__人民群众",
                suite_id="2026_通州_期末",
                year=2026,
                district="通州",
                stage="期末",
                question_no="16",
                sub_part="",
                question_type="subjective",
                target_node_path="历史唯物主义/人民群众",
                node_subtask="治水智慧源于人民实践",
                evidence_level="rubric-formal",
                rubric_excerpt="Q16 评标 pptx：唯物史观可写人民群众是历史的创造者；李冰率领民众历经艰难修建都江堰，历代治水者接力维护，治水智慧源于人民实践。",
                材料触发点="材料写李冰率领民众历经艰难修建都江堰，历代治水者接力维护，使其千年至今仍焕发生机。",
                设问="结合材料，运用《哲学与文化》知识，阐释都江堰跨越千年的治水智慧。",
                为什么能想到="材料把都江堰的形成和延续都落到人的实践活动上：李冰率领民众修建，历代治水者接力维护。学生看到'民众修建+历代维护'，就应想到人民群众是历史的创造者，治水智慧来自人民实践。",
                答案落点="都江堰跨越千年的治水智慧也体现人民群众是历史的创造者。李冰率领民众修建都江堰，历代治水者持续维护和升级工程，正是人民群众的生产生活实践创造并延续了这一治水智慧。",
                evidence_path="/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf 第5-6页第16题；细则/细则.pptx slide 2-4",
                sort_priority="main_question",
            ),
        ],
    }

    for sid, rows in missing.items():
        path = ENTRIES / f"{sid}.jsonl"
        if path.exists() and path.read_text(encoding="utf-8").strip():
            print(f"skip existing nonempty entries: {sid}")
            continue
        write_jsonl(path, rows)
        print(f"added entries: {sid} ({len(rows)})")


def add_missing_reports() -> None:
    reports: dict[str, str] = {
        "2026_朝阳_期中": """# 2026_朝阳_期中 套卷报告

## 源文件

- 试卷：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf`
- 主观题阅卷细则：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/细则.docx`
- 补充细则：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/补充材料/细则.docx`

## 哲学闭环

- 第4题：选择题，可靠答案表给 A；保留为联系多样性/全球治理错项辨析。
- 第18题：主观题，AI 提供情绪价值，阅卷细则明确给出矛盾对立统一、具体问题具体分析、主观能动性/意识依赖于物质、辩证否定观、价值判断与价值选择等哲学角度，已入学生版 5 条。

## 排除/边界

- 第16题为《经济与社会》绿色金融。
- 第17题为《当代国际政治与经济》人工智能+关系。
- 第19题主要为文化/民族精神卷首语，哲学点只作附带可选，不进本轮哲学主链。
- 第20题设问为《逻辑与思维》辩证思维方法，哲学知识只作替换/弱边界，本轮不作为正式必修四主链。
- 第21题为经济/文化与创新思维。
""",
        "2026_丰台_期末": """# 2026_丰台_期末 套卷报告

## 源文件

- 试卷：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/试卷/试卷.pdf`
- 评分细则：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/细则/细则.pdf`
- 试卷 PDF 命令行抽文本为空，已渲染 `audit/render_missing/2026_丰台_期末/page_06.png` 核读第16题。

## 哲学闭环

- 第16题“留白”主观题，评分细则明确给出哲学角度：矛盾对立统一、量变质变/适度原则、整体与部分/联系观点、尊重客观规律与发挥主观能动性相结合。已入学生版 4 条。

## 排除/边界

- 第17题为《政治与法治》基层治理。
- 后续题按题面与细则不进入本轮必修四哲学主链。
""",
        "2026_通州_期末": """# 2026_通州_期末 套卷报告

## 源文件

- 试卷：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf`
- 评分细则：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/细则/细则.pptx`

## 哲学闭环

- 第16题“都江堰跨越千年的治水智慧”，评标 pptx 明确给出一切从实际出发、尊重客观规律与发挥主观能动性相结合、联系观点、发展观点、辩证否定观、人民群众等哲学角度。已入学生版 6 条。

## 排除/边界

- 同题文化角度（中华优秀传统文化、文化创新、文化作用）按本轮“只做哲学”排除，仅保留审计说明。
- 第17题政治与法治，第18题经济与社会，第19题法律/逻辑，第20题当代国际政治与经济，均不进入本轮必修四哲学主链。
- 第21题综合题含少量哲学替换角度，但主干为党的领导、高质量发展、对外开放等综合政治经济线，本轮不作为正式哲学主链。
""",
    }
    REPORTS.mkdir(parents=True, exist_ok=True)
    for sid, text in reports.items():
        path = REPORTS / f"{sid}.md"
        if not path.exists() or not path.read_text(encoding="utf-8").strip():
            path.write_text(text, encoding="utf-8")
            print(f"added report: {sid}")
        else:
            print(f"skip existing report: {sid}")


def assert_student_fields_clean() -> None:
    bad: list[str] = []
    for path in sorted(ENTRIES.glob("*.jsonl")):
        for i, e in enumerate(load_jsonl(path), 1):
            for fld in STUDENT_FIELDS:
                val = str(e.get(fld, ""))
                if FORBIDDEN_RE.search(val):
                    bad.append(f"{path.name}:{i}:{e.get('entry_id')}:{fld}:{val[:120]}")
    if bad:
        print("FORBIDDEN STUDENT FIELD RESIDUE:")
        for item in bad[:100]:
            print(item)
        raise SystemExit(1)
    print("student fields forbidden scan: 0")


def main() -> int:
    backup_entries()
    clean_existing_entries()
    add_missing_entries()
    add_missing_reports()
    assert_student_fields_clean()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
