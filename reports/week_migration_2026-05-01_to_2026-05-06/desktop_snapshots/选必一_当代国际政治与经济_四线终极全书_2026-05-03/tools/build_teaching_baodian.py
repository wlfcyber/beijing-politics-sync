#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path


RUN = Path("/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03")
BASE_SCRIPT = RUN / "tools" / "build_final_student_handout.py"
REBUILD = RUN / "10_teaching_rebuild_20260504"
OUT_MD = REBUILD / "04_delivery" / "选必一_当代国际政治与经济_触发宝典_可直接讲版_20260504.md"
OUT_TEACHER = REBUILD / "04_delivery" / "选必一_触发宝典_教师核查索引_20260504.csv"
OUT_FREQ = REBUILD / "04_delivery" / "选必一_触发宝典_核心点频次_20260504.csv"


def load_base():
    spec = importlib.util.spec_from_file_location("xby1_base_handout", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BASE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


B = load_base()


def load_data():
    prompts = {r["source_question"].strip(): r["full_prompt"].strip() for r in B.read_csv_dict(B.PROMPTS_CSV)}
    prompts.update(B.PROMPT_OVERRIDES)

    clusters: dict[tuple[str, str], dict[str, str]] = {}
    for row in B.read_csv_dict(B.CLUSTERS_CSV):
        bucket = row["bucket"].strip()
        core = B.normalize_core(row["core_cluster"])
        clusters[(bucket, core)] = row

    atoms: list[B.Atom] = []
    for source_seq, row in enumerate(B.read_csv_dict(B.ATOMS_CSV), 1):
        bucket = row.get("final_bucket") or row.get("bucket") or "理论"
        core = B.normalize_core(row.get("final_core_cluster") or row.get("core_point") or "")
        bucket, core = B.adjusted_bucket_core(row.get("atom_id", ""), bucket, core)
        q_list = B.split_questions(row.get("source_question", ""))
        for q_index, q in enumerate(q_list):
            atom = B.Atom(
                atom_id=row.get("atom_id", ""),
                seq=source_seq,
                question=q,
                prompt=prompts.get(q, ""),
                bucket=bucket,
                core=core,
                expression=B.public(row.get("expression_variant", "")),
                material=B.question_specific_material(q, core, B.public(row.get("material_trigger_fusion", ""))),
                answer=B.question_specific_answer(q, core, B.polish_sentence(row.get("answer_sentence_fusion", ""))),
                status=row.get("promotion_status", ""),
                note=B.public(row.get("boundary_note", "")),
                scoring_position=B.parallel_piece(row.get("scoring_position", ""), q_index, len(q_list)),
                evidence_level=B.parallel_piece(row.get("evidence_level", ""), q_index, len(q_list)),
                source_boundary=B.parallel_piece(row.get("source_boundary", ""), q_index, len(q_list)),
                source_refs=B.parallel_piece(row.get("source_ledger_refs", ""), q_index, len(q_list)),
            )
            atoms.append(atom)

    unique: dict[tuple[str, str, str, str], B.Atom] = {}
    for atom in atoms:
        unique.setdefault((atom.question, atom.bucket, atom.core, atom.answer), atom)
    atoms = list(unique.values())

    main_atoms: dict[str, list[B.Atom]] = defaultdict(list)
    side_atoms: dict[str, list[B.Atom]] = defaultdict(list)
    for atom in atoms:
        if "2026石景山期末" in atom.question:
            continue
        if atom.status in B.MAIN_STATUSES and (atom.question in B.QUESTION_FORCE_MAIN or not B.is_cross_module(atom.prompt)):
            main_atoms[atom.question].append(atom)
        else:
            side_atoms[atom.question].append(atom)

    for group in (main_atoms, side_atoms):
        for q in group:
            group[q].sort(key=lambda a: (B.BUCKET_ORDER.get(a.bucket, 99), a.core, a.atom_id))

    core_main_questions: dict[tuple[str, str], list[str]] = defaultdict(list)
    for q, q_atoms in main_atoms.items():
        for atom in q_atoms:
            key = (atom.bucket, atom.core)
            if q not in core_main_questions[key]:
                core_main_questions[key].append(q)
    for key in core_main_questions:
        core_main_questions[key].sort(key=B.district_key)

    for (bucket, core), row in B.MANUAL_CORE_OVERLAYS.items():
        clusters.setdefault((bucket, core), row)
        for q in B.split_questions(row.get("source_questions", "")):
            if q not in core_main_questions[(bucket, core)]:
                core_main_questions[(bucket, core)].append(q)
        core_main_questions[(bucket, core)].sort(key=B.district_key)

    return prompts, clusters, main_atoms, side_atoms, core_main_questions


def red(text: str) -> str:
    return B.red(text)


def strip_red(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "")


def clean_front_text(text: str) -> str:
    replacements = {
        "设问要求": "题目追问",
        "要落到": "要对应到",
        "同槽": "同层",
        "同一层择写提醒：": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def q_anchor(question: str) -> str:
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", question).strip("-")


def source_type_label(atom: B.Atom) -> str:
    label = B.student_point_label(atom)
    if "彩色细则" in label:
        return "彩色细则"
    if "正式细则" in label or "图片细则" in label:
        return "正式/题内细则"
    if "等级答案" in label or "讲评口径" in label:
        return "等级答案/讲评口径"
    return "按题表达"


def concise_position(atom: B.Atom) -> str:
    text = B.scoring_position_public(atom)
    text = text.replace("答案示例性质", "答案示例")
    text = text.replace("本题为等级说明，非逐点细则", "等级说明")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > 46:
        text = text[:46].rstrip("，；、 ") + "…"
    return text


def why_bridge(atom: B.Atom) -> str:
    core = B.display_core(atom.question, atom.core)
    material = B.public(atom.material)
    prompt = atom.prompt or ""
    if "制度型开放" in core or "开放型世界经济" in core or "规则制定" in core:
        return "看到材料写标准、规则、争端解决、对标国际规则或走出国门，就不能只写普通开放，要上收到制度型开放、开放型世界经济和全球经济治理规则制定。"
    if "两个市场" in core or "循环" in core:
        return "看到中国把国内发展同国际市场、资源、产业链连接起来，就要想到两个市场、两种资源和国内国际循环联动。"
    if "开放、包容、普惠、平衡、共赢" in core or "经济全球化" in core:
        return "看到开放合作、全球南方受益、发展成果共享、反对保护主义，就要把材料写成经济全球化的方向，五个词尽量完整保留。"
    if "霸权主义" in core or "强权政治" in core:
        return "看到强权霸凌、封闭排他、零和博弈、脱钩断链，先把它识别为时代背景里的旧逻辑；若设问问回应，再转到国际关系民主化和真正多边主义。"
    if "和平与发展" in core:
        return "看到合作为什么必要、倡议为什么正逢其时、外交为什么因势而变，就先判断它是不是在问当今时代主题和共同发展愿望。"
    if "共同利益" in core:
        return "看到两个或多个国家愿意合作，先问他们有什么共同利益；共同利益解释合作为什么成立，不等于中国怎样合作。"
    if "义利观" in core:
        return "看到中国既维护自身利益又照顾他国合理关切，就要写正确义利观，防止答案变成中国单向输出。"
    if "新型国际关系" in core:
        return "看到国家间合作方式从零和竞争转向平等、互利、共赢，就要对应到新型国际关系，而不是只写普通合作。"
    if "共商共建共享" in core:
        return "看到全球治理由各国一起讨论、一起建设、一起分享成果，就要写共商共建共享，别把它和普通互利合作混成一句。"
    if "人类命运共同体" in core:
        return "看到共同挑战、共同前途、全球公共产品或中国倡议的总目标，才能用人类命运共同体作收束。"
    if "联合国" in atom.bucket or "宪章" in core or "巴黎协定" in core:
        return "看到联合国、宪章、安理会、巴黎协定或NDC这类明确制度框架，才把答案落到联合国和多边治理框架。"
    if "意义" in prompt or "价值" in prompt or "贡献" in prompt:
        return f"本题问意义或贡献，材料触发的是“{core}”，卷面要写成对象影响，而不是只背概念。"
    if "如何" in prompt or "怎样" in prompt or "措施" in prompt:
        return f"本题问做法或路径，材料触发的是“{core}”，卷面要写成做法、机制和作用。"
    return f"材料中的关键信息和设问方向共同指向“{core}”，写作时要把术语、材料事实和设问回扣连成一条链。"


def answer_three_lines(atom: B.Atom, terms: list[str]) -> list[str]:
    answer = B.highlight_scoring_terms(atom.answer, terms)
    core = B.display_core(atom.question, atom.core)
    plain_answer = strip_red(answer)
    material_hint = B.public(atom.material)
    material_hint = material_hint.replace("题目追问", "").replace("就要想到", "对应")
    material_hint = re.sub(r"\s+", " ", material_hint).strip(" 。")
    if len(material_hint) > 78:
        material_hint = material_hint[:78].rstrip("，；、 ") + "…"
    scoring_terms = B.format_scoring_terms(terms[:4]) if terms else red(core)
    return [
        f"理论句：先写 {scoring_terms}。",
        f"材料对接：{material_hint}。",
        f"回扣设问：{answer if plain_answer else red(core)}",
    ]


def scoring_atoms_for_question(question: str, main_q_atoms: list[B.Atom], side_q_atoms: list[B.Atom]) -> list[B.Atom]:
    atoms = B.scoring_point_atoms(question, main_q_atoms, side_q_atoms)
    return [a for a in atoms if a.answer.strip()]


def question_summary_lines(question: str, scoring_atoms: list[B.Atom]) -> list[str]:
    question_score_terms: list[str] = []
    for atom in scoring_atoms:
        for term in B.scoring_terms_for_atom(atom):
            if term not in question_score_terms:
                question_score_terms.append(term)
    override = B.QUESTION_SUMMARY_OVERRIDES.get(question)
    if override:
        lines = [B.highlight_scoring_terms(answer, question_score_terms) for answer in override]
        override_text = "\n".join(override)
        for atom in scoring_atoms:
            atom_terms = B.scoring_terms_for_atom(atom)
            if atom.answer and not any(term and term in override_text for term in atom_terms[:3]):
                lines.append(B.highlight_scoring_terms(atom.answer, atom_terms))
        return lines
    return [B.highlight_scoring_terms(atom.answer, B.scoring_terms_for_atom(atom)) for atom in scoring_atoms]


def bucket_index_lines(clusters, core_main_questions) -> list[str]:
    lines: list[str] = []
    lines.append("## 第一部分：六桶读题总图")
    lines.append("")
    lines.append("六桶是读题地图，不是六选一。新题先看设问问什么，再看材料对象和动作，最后决定从哪些桶取点。")
    lines.append("")
    for bucket in B.BUCKETS:
        bucket_cores = [(core, row) for (b, core), row in clusters.items() if b == bucket]
        for b, core in core_main_questions:
            if b == bucket and (b, core) not in clusters:
                bucket_cores.append((core, {"distinct_source_count": str(len(core_main_questions[(b, core)]))}))
        if not bucket_cores:
            continue
        lines.append(f"### {bucket}")
        for core, row in sorted(bucket_cores, key=lambda x: (-int(x[1].get("distinct_source_count") or 0), x[0])):
            questions = core_main_questions.get((bucket, core), [])
            if not questions:
                continue
            score_terms = B.scoring_terms_for_core(core, row)
            note = B.CORE_INDEX_NOTES.get(core, "").strip("（）")
            lines.append(f"- **{red(core)}**")
            if note:
                lines.append(f"  - 常见抓手：{note}")
            lines.append(f"  - 踩分词：{B.format_scoring_terms(score_terms)}")
            lines.append(f"  - 来源题链：{'；'.join(questions)}")
            if core in B.PLAIN_NOTES:
                lines.append(f"  - 别误套：{B.PLAIN_NOTES[core]}")
        lines.append("")
    return lines


def core_baodian_lines(clusters, main_atoms, core_main_questions) -> list[str]:
    lines: list[str] = []
    lines.append("## 第二部分：按核心知识点触发宝典")
    lines.append("")
    lines.append("这一部分按哲学宝典的写法重排：先学会“看到什么材料就想到什么点”，再回到具体题。一个题如果命中多个点，就会在多个核心点下重复挂载。")
    lines.append("")
    atoms_by_core: dict[tuple[str, str], list[B.Atom]] = defaultdict(list)
    for q, atoms in main_atoms.items():
        for atom in atoms:
            atoms_by_core[(atom.bucket, atom.core)].append(atom)

    serial = 1
    for bucket in B.BUCKETS:
        lines.append(f"# {bucket}")
        keys = [key for key in atoms_by_core if key[0] == bucket]
        for overlay_key in core_main_questions:
            if overlay_key[0] == bucket and overlay_key not in keys:
                keys.append(overlay_key)
        keys.sort(key=lambda key: (-len(core_main_questions.get(key, [])), key[1]))
        for key in keys:
            core = key[1]
            questions = core_main_questions.get(key, [])
            if not questions:
                continue
            row = clusters.get(key, {"expression_accumulation": core, "distinct_source_count": str(len(questions))})
            score_terms = B.scoring_terms_for_core(core, row)
            lines.append(f"## {core}")
            lines.append("")
            lines.append(f"**一句话抓手**：看到材料能落到“{core}”，先写核心术语，再把材料事实接回来，最后回扣设问。")
            lines.append(f"**本核心踩分词**：{B.format_scoring_terms(score_terms)}")
            lines.append(f"**表述积累**：{B.highlight_scoring_terms(B.compact_accumulation(core, row.get('expression_accumulation', core)), score_terms)}")
            if core in B.PLAIN_NOTES:
                lines.append(f"**误套边界**：{B.PLAIN_NOTES[core]}")
            lines.append(f"**来源题链**：{'；'.join(questions)}")
            lines.append("")
            atoms = sorted(atoms_by_core.get(key, []), key=lambda a: B.district_key(a.question))
            if not atoms and key in B.MANUAL_CORE_OVERLAYS:
                overlay = B.MANUAL_CORE_OVERLAYS[key]
                lines.append(f"### {serial}. 时代背景补丁题链")
                serial += 1
                lines.append(f"【材料触发点】 {overlay.get('expression_accumulation', core)}")
                lines.append("【设问】 见对应题号。")
                lines.append(f"【为什么能想到】 {why_bridge(B.Atom('', 0, questions[0] if questions else '', '', bucket, core, core, '', core, '', '', '', '', '', ''))}")
                lines.append(f"【踩分词】 {B.format_scoring_terms(score_terms)}")
                lines.append("【答案落点】 先识别旧式国际关系逻辑；如果题目问回应路径，再转到国际关系民主化、真正多边主义和公正合理国际秩序。")
                lines.append("")
                continue
            for atom in atoms:
                terms = B.scoring_terms_for_atom(atom)
                lines.append(f"### {serial}. {atom.question}（主观题）")
                serial += 1
                lines.append(f"【材料触发点】 {B.public(atom.material)}")
                lines.append(f"【设问】 {atom.prompt or atom.question}")
                lines.append(f"【为什么能想到】 {why_bridge(atom)}")
                lines.append(f"【踩分词】 {B.format_scoring_terms(terms)}")
                alt_note = B.alternate_terms_note(terms, atom.answer)
                if alt_note:
                    lines.append(f"【同槽/备用提醒】 {alt_note.replace('同一层择写提醒：', '')}")
                lines.append(f"【答案落点】 {B.highlight_scoring_terms(atom.answer, terms)}")
                lines.append("")
        lines.append("")
    return lines


def question_training_lines(prompts, main_atoms, side_atoms) -> list[str]:
    lines: list[str] = []
    lines.append("## 第三部分：按题训练闭环")
    lines.append("")
    lines.append("这一部分按题号排。每道题先看细则踩分点，再看命中框架，最后看整题卷面答案。")
    lines.append("")
    for idx, q in enumerate(sorted(main_atoms, key=B.district_key), 1):
        q_atoms = main_atoms[q]
        q_side_atoms = side_atoms.get(q, [])
        q_scoring_atoms = scoring_atoms_for_question(q, q_atoms, q_side_atoms)
        prompt = prompts.get(q, q)
        lines.append(f"### {idx}. {q}")
        lines.append("")
        lines.append(f"**完整设问**：{prompt}")
        if q in B.QUESTION_HEADER_NOTES:
            lines.append(f"**模块归属提醒**：{B.QUESTION_HEADER_NOTES[q]}")
        lines.append("")
        lines.append("**本题踩分点清单**：")
        exact_groups = B.QUESTION_EXACT_SCORING_GROUPS.get(q)
        if exact_groups:
            for n, group in enumerate(exact_groups, 1):
                terms = list(group["terms"])
                lines.append(f"{n}. **{group['label']}**")
                lines.append(f"   - 点位性质：本题踩分点（彩色细则）")
                lines.append(f"   - 卷面层级：{group['level']}")
                lines.append(f"   - 踩分词：{B.format_scoring_terms(terms)}")
                lines.append(f"   - 卷面句：{B.highlight_scoring_terms(group['answer'], terms)}")
        else:
            for n, atom in enumerate(q_scoring_atoms, 1):
                terms = B.scoring_terms_for_atom(atom)
                lines.append(f"{n}. **{B.display_core(q, atom.core)}**")
                lines.append(f"   - 点位性质：{B.student_point_label(atom)}（{source_type_label(atom)}）")
                boundary = B.atom_boundary_label(atom, False)
                if boundary:
                    lines.append(f"   - 使用边界：{boundary}")
                lines.append(f"   - 卷面层级：{concise_position(atom)}")
                lines.append(f"   - 踩分词：{B.format_scoring_terms(terms)}")
                alt_note = B.alternate_terms_note(terms, atom.answer)
                if alt_note:
                    lines.append(f"   - 同槽/备用提醒：{alt_note.replace('同一层择写提醒：', '')}")
                lines.append(f"   - 卷面句：{B.highlight_scoring_terms(atom.answer, terms)}")
        lines.append("")
        lines.append("**本题命中框架**：")
        by_bucket: dict[str, list[str]] = defaultdict(list)
        for atom in q_atoms:
            label = B.display_core(q, atom.core)
            if label not in by_bucket[atom.bucket]:
                by_bucket[atom.bucket].append(label)
        for bucket in B.BUCKETS:
            if by_bucket.get(bucket):
                lines.append(f"- {bucket}：{'；'.join(by_bucket[bucket])}")
        lines.append("")
        lines.append("**为什么这道题这样取点**：")
        lines.append(f"- 题型通用触发：{B.question_trigger(prompt)}")
        lines.append(f"- 本题独有触发：{B.question_trigger_specific(q, prompt, q_atoms)}")
        lines.append("")
        lines.append("**核心点细拆**：")
        for n, atom in enumerate(q_scoring_atoms, 1):
            terms = B.scoring_terms_for_atom(atom)
            lines.append(f"{n}. **{B.display_core(q, atom.core)}**")
            lines.append(f"   - 材料触发点：{B.public(atom.material)}")
            lines.append(f"   - 为什么能想到：{why_bridge(atom)}")
            lines.append(f"   - 框架落点：{atom.bucket} -> {B.display_core(q, atom.core)}")
            lines.append(f"   - 踩分词：{B.format_scoring_terms(terms)}")
            for piece in answer_three_lines(atom, terms):
                lines.append(f"   - {piece}")
        lines.append("")
        lines.append("**整题汇总卷面答案**：")
        if q in B.QUESTION_PRIORITY_NOTES:
            lines.append(f"- {B.QUESTION_PRIORITY_NOTES[q]}")
        for answer in question_summary_lines(q, q_scoring_atoms):
            lines.append(f"- {answer}")
        lines.append("")
    return lines


def final_review_lines(side_atoms) -> list[str]:
    lines: list[str] = []
    lines.append("## 第四部分：慎用与跨模块表达积累")
    lines.append("")
    lines.append("下面内容可以帮学生积累语言，但不是本册主观题的固定逐点模板。看到类似题，先判断主属模块，再决定是否借用。")
    lines.append("")
    for q in sorted(side_atoms, key=B.district_key):
        atoms = [atom for atom in side_atoms[q] if atom.answer.strip()]
        if not atoms:
            continue
        lines.append(f"### {q}")
        lines.append("")
        lines.append(f"**题目锚点/设问**：{atoms[0].prompt or q}")
        lines.append(f"**主属模块**：{B.side_module_label(atoms[0])}")
        for atom in atoms[:8]:
            terms = B.scoring_terms_for_atom(atom)
            lines.append(f"- **{atom.bucket} -> {B.display_core(q, atom.core)}**：{B.highlight_scoring_terms(atom.answer, terms)} {B.side_reason(atom)}")
        lines.append("")
    return lines


def write_indexes(clusters, main_atoms, core_main_questions):
    OUT_TEACHER.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for q, atoms in main_atoms.items():
        for atom in atoms:
            rows.append(
                {
                    "question": q,
                    "bucket": atom.bucket,
                    "core": atom.core,
                    "atom_id": atom.atom_id,
                    "scoring_position": atom.scoring_position,
                    "evidence_level": B.evidence_level_for_atom(atom),
                    "status": atom.status,
                    "source_boundary": B.source_boundary_for_atom(atom),
                    "source_refs": atom.source_refs,
                }
            )
    with OUT_TEACHER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["question"])
        writer.writeheader()
        writer.writerows(rows)

    freq_rows = []
    for key, questions in sorted(core_main_questions.items(), key=lambda x: (B.BUCKET_ORDER.get(x[0][0], 99), x[0][1])):
        row = clusters.get(key, {})
        freq_rows.append(
            {
                "bucket": key[0],
                "core_cluster": key[1],
                "question_count": len(questions),
                "source_questions": "；".join(questions),
                "expression_accumulation": B.compact_accumulation(key[1], row.get("expression_accumulation", key[1])),
            }
        )
    with OUT_FREQ.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(freq_rows[0].keys()) if freq_rows else ["bucket"])
        writer.writeheader()
        writer.writerows(freq_rows)


def main():
    prompts, clusters, main_atoms, side_atoms, core_main_questions = load_data()
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# 选必一《当代国际政治与经济》全题触发宝典（可直接讲版）")
    lines.append("")
    lines.append("这版不再把学生先扔进题号流水里，而是先教他看材料触发：看到什么材料动作，就想到什么核心术语；每道题再回到细则踩分点和整题卷面答案。")
    lines.append("")
    lines.append("目录")
    lines.append("")
    lines.append("- 第一部分：六桶读题总图")
    lines.append("- 第二部分：按核心知识点触发宝典")
    lines.append("- 第三部分：按题训练闭环")
    lines.append("- 第四部分：慎用与跨模块表达积累")
    lines.append("")
    lines.append("## 0. 30 秒读题法")
    lines.append("")
    lines.append("第一步，圈设问动词：原因、意义、做法、理解、关系、短文。")
    lines.append("")
    lines.append("第二步，圈材料对象：中国、合作方、世界经济、国际秩序、全球治理、联合国、企业出海、开放政策。")
    lines.append("")
    lines.append("第三步，圈材料动作：走出国门、标准共通、规则制定、合作共赢、共同挑战、强权霸凌、联合国框架、NDC、自贸协定、技术共享。")
    lines.append("")
    lines.append("第四步，先列本题踩分词，再把它们放回六桶。不要先背框架名，框架名只是导航；红色踩分词才是卷面必须尽量写出的词。")
    lines.append("")
    lines.extend(bucket_index_lines(clusters, core_main_questions))
    lines.extend(core_baodian_lines(clusters, main_atoms, core_main_questions))
    lines.extend(question_training_lines(prompts, main_atoms, side_atoms))
    lines.extend(final_review_lines(side_atoms))
    OUT_MD.write_text(clean_front_text("\n".join(lines)).strip() + "\n", encoding="utf-8")
    write_indexes(clusters, main_atoms, core_main_questions)
    print(OUT_MD)
    print(OUT_TEACHER)
    print(OUT_FREQ)


if __name__ == "__main__":
    main()
