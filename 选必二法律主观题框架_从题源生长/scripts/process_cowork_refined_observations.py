#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
OPEN = ROOT / "06_open_observations"
XVAL = ROOT / "07_cross_validation"
CODEBOOK = ROOT / "08_codebook"
SOURCE = ROOT / "04_merge_audit" / "suite_exhaustive_cowork_refined_20260519"

FIELDS = [
    "observation_id",
    "plain_observation",
    "question_ids",
    "rubric_atom_ids",
    "material_atom_ids",
    "ask_type",
    "evidence_type",
    "evidence_level",
    "what_student_must_judge",
    "material_trigger",
    "legal_knowledge_or_rule_triggered",
    "rubric_reward",
    "knowledge_material_value_type",
    "full_score_sentence_pattern",
    "must_have_keywords",
    "risk_of_empty_value_talk",
    "risk_of_legal_exam_overanalysis",
    "module_boundary_risk",
    "transfer_potential",
    "counterexamples",
    "confidence",
    "should_enter_codebook",
    "reason",
]

FIELD_SET = set(FIELDS)

QUESTION_RE = re.compile(r"(?:CC\d{4}|RECOVER)_[A-Za-z0-9_\u4e00-\u9fff]+")
RUBRIC_RE = re.compile(r"(?:R_(?:CC\d{4}|RECOVER)_[A-Za-z0-9_\u4e00-\u9fff]+|RECOVER_[A-Za-z0-9_\u4e00-\u9fff]+_R\d+)")
MATERIAL_RE = re.compile(r"(?:M_(?:CC\d{4}|RECOVER)_[A-Za-z0-9_\u4e00-\u9fff]+|RECOVER_[A-Za-z0-9_\u4e00-\u9fff]+_M\d+)")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def split_ids(raw: str, pattern: re.Pattern[str]) -> list[str]:
    ids = []
    for m in pattern.findall(raw or ""):
        item = m.strip().rstrip(".,;，；、)")
        if item and item not in ids:
            ids.append(item)
    return ids


def category_from_heading(line: str) -> str | None:
    s = line.strip()
    if not s.startswith("##"):
        return None
    if "强观察" in s:
        return "strong"
    if "弱观察" in s:
        return "weak"
    if "冲突观察" in s:
        return "conflict"
    if "不应上升" in s or "反框架" in s:
        return "do_not_promote"
    if "下一轮" in s:
        return "next_round"
    return None


def clean_field_name(raw: str) -> str:
    raw = raw.strip().strip("`").strip()
    return raw


def parse_md(path: Path, model: str) -> list[dict[str, str]]:
    observations: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_field: str | None = None
    category = ""

    def flush() -> None:
        nonlocal current, current_field
        if current and current.get("observation_id"):
            for f in FIELDS:
                current.setdefault(f, "")
                current[f] = norm(current[f])
            current["model"] = model
            current["category"] = current.get("category", category)
            current["question_id_list"] = "|".join(split_ids(current.get("question_ids", ""), QUESTION_RE))
            current["rubric_atom_id_list"] = "|".join(split_ids(current.get("rubric_atom_ids", ""), RUBRIC_RE))
            current["material_atom_id_list"] = "|".join(split_ids(current.get("material_atom_ids", ""), MATERIAL_RE))
            current["has_required_ids"] = "yes" if current["question_id_list"] and current["rubric_atom_id_list"] and current["material_atom_id_list"] else "no"
            observations.append(current)
        current = None
        current_field = None

    for line in path.read_text(encoding="utf-8").splitlines():
        cat = category_from_heading(line)
        if cat:
            category = cat

        stripped = line.strip()
        heading_match = re.match(r"^#{3,}\s*(?:observation_id:\s*)?([A-Za-z0-9_]+)", stripped)
        if heading_match:
            token = heading_match.group(1)
            if token.lower().startswith("observation_id"):
                token = stripped.split(":", 1)[1].strip() if ":" in stripped else token
            if token.startswith(("STRONG_", "WEAK_", "CONFLICT_", "NOFRAME_", "OBS", "NEXT_")):
                flush()
                current = {f: "" for f in FIELDS}
                current["observation_id"] = token
                current["category"] = category
                current_field = None
                continue

        field_match = re.match(r"^`?([A-Za-z_]+)`?\s*[:：]\s*(.*)$", stripped)
        if current is not None and field_match:
            field = clean_field_name(field_match.group(1))
            if field in FIELD_SET:
                if field == "observation_id" and current.get("observation_id") and current["observation_id"] != field_match.group(2).strip():
                    current["observation_id"] = field_match.group(2).strip()
                else:
                    current[field] = field_match.group(2).strip()
                current_field = field
                continue

        if current is not None and current_field and stripped:
            if not stripped.startswith("#") and stripped != "---":
                current[current_field] = (current.get(current_field, "") + " " + stripped).strip()

    flush()
    return observations


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_source_maps() -> dict[str, dict[str, list[str] | dict[str, str] | set[str]]]:
    question_ids: set[str] = set()
    material_by_q: dict[str, list[str]] = {}
    material_ids: set[str] = set()
    rubric_levels: dict[str, str] = {}
    rubric_by_q: dict[str, list[str]] = {}

    with (SOURCE / "merged_subjective_law_questions_cowork_refined.csv").open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            question_ids.add(row["question_id"])

    with (SOURCE / "merged_material_atoms_subjective_cowork_refined.csv").open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            mid = row["material_atom_id"]
            material_ids.add(mid)
            material_by_q.setdefault(row["question_id"], []).append(mid)

    with (SOURCE / "merged_rubric_atoms_subjective_cowork_refined.csv").open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            rid = row["rubric_atom_id"]
            rubric_levels[rid] = row.get("evidence_level", "")
            rubric_by_q.setdefault(row["question_id"], []).append(rid)

    return {
        "question_ids": question_ids,
        "material_by_q": material_by_q,
        "material_ids": material_ids,
        "rubric_levels": rubric_levels,
        "rubric_by_q": rubric_by_q,
    }


def enrich_with_source_ids(rows: list[dict[str, str]], maps: dict[str, dict[str, list[str] | dict[str, str] | set[str]]]) -> None:
    question_ids = maps["question_ids"]
    material_by_q = maps["material_by_q"]
    material_ids = maps["material_ids"]
    rubric_levels = maps["rubric_levels"]

    for row in rows:
        notes: list[str] = []
        qids = [q for q in row.get("question_id_list", "").split("|") if q in question_ids]
        if len(qids) != len([q for q in row.get("question_id_list", "").split("|") if q]):
            notes.append("some_question_ids_not_in_current_source")
        row["question_id_list"] = "|".join(qids)

        rids_raw = [r for r in row.get("rubric_atom_id_list", "").split("|") if r]
        rids = [r for r in rids_raw if r in rubric_levels]
        if len(rids) != len(rids_raw):
            notes.append("non_exact_rubric_ids_filtered")
        row["rubric_atom_id_list"] = "|".join(rids)

        mids_raw = [m for m in row.get("material_atom_id_list", "").split("|") if m]
        mids = [m for m in mids_raw if m in material_ids]
        if len(mids) != len(mids_raw):
            notes.append("non_exact_material_ids_filtered")

        raw_material_field = row.get("material_atom_ids", "")
        if not mids and qids and any(token in raw_material_field for token in ["全集", "各题", "对应案例", "任一", ".."]):
            expanded: list[str] = []
            for qid in qids:
                expanded.extend(material_by_q.get(qid, []))
            mids = list(dict.fromkeys(expanded))
            notes.append("material_ids_expanded_from_question_ids")
        row["material_atom_id_list"] = "|".join(mids)

        row["has_required_ids"] = "yes" if qids and rids and mids else "no"
        row["source_check_notes"] = ";".join(notes)


def words(text: str) -> set[str]:
    keys = [
        "判决", "法理依据", "现实意义", "表态", "诉讼请求", "表格", "民法基本原则",
        "消费者", "劳动", "知识产权", "争议解决", "调解", "仲裁", "诉讼", "侵权",
        "合同", "未成年人", "证据", "举证", "材料", "法考化", "必修三", "价值",
        "以事实为依据", "以法律为准绳", "格式条款", "相邻关系", "无过错", "起诉状",
    ]
    return {k for k in keys if k in text}


def tags(row: dict[str, str]) -> set[str]:
    # Use the observation's own thesis, not long evidence lists or counterexamples.
    # Otherwise broad observations inherit every legal term mentioned in examples and over-match.
    text = " ".join(row.get(k, "") for k in ["observation_id", "plain_observation"])
    patterns = {
        "table": ["表格", "完成下表", "补充完整", "每格", "空格"],
        "court_anchor": ["以事实为依据", "以法律为准绳", "法理依据", "法院判决"],
        "significance": ["现实意义", "社会价值", "典型意义", "意义层", "三角度"],
        "attitude": ["表态", "支持/不支持", "有效/无效", "诉讼请求", "裁判结果"],
        "contract": ["合同", "违约", "格式条款", "要约", "承诺", "可撤销"],
        "tort": ["侵权", "过错", "无过错", "过错推定", "安全保障", "自甘风险", "责任类型"],
        "case_chain": ["定性", "确权", "四步", "分析案例", "案例核心"],
        "procedure": ["维权", "纠纷解决", "起诉状", "举证", "程序", "程序路径"],
        "material_quote": ["引用材料", "材料原文", "具体词句", "日常出行规律", "近似但非材料原文"],
        "right_spelling": ["权利名称", "错字", "漏字", "术语近似", "限制民事行为能力人", "消费者权益保护法"],
        "module_boundary": ["模块边界", "必修三", "政治与法治", "不赋分", "法治政府", "法治社会"],
        "anti_template": ["模板", "套话", "照搬", "空泛"],
        "ip": ["知识产权", "新质生产力", "创新", "惩罚性赔偿", "不正当竞争", "商业秘密"],
        "ai": ["AI", "数字", "数据"],
        "labor": ["劳动", "竞业", "就业"],
        "family": ["赡养", "遗产", "扶养", "继承"],
        "ecology_neighbor": ["生态", "相邻", "绿色", "物权", "公共利益"],
        "consumer": ["消费者保护", "消费者权益", "知情权", "自主选择权"],
        "minor": ["未成年人", "法定代理人", "追认", "监护"],
    }
    return {tag for tag, needles in patterns.items() if any(n in text for n in needles)}


def idset(row: dict[str, str], key: str) -> set[str]:
    return {x for x in row.get(key, "").split("|") if x}


def scoped_ids(rows: list[dict[str, str]], key: str, qids: set[str]) -> list[str]:
    found: list[str] = []
    for row in rows:
        for item in row.get(key, "").split("|"):
            item = item.strip()
            if item and (not qids or any(qid in item for qid in qids)) and item not in found:
                found.append(item)
    return found


def score_pair(g: dict[str, str], c: dict[str, str]) -> tuple[float, dict[str, str]]:
    gq, cq = idset(g, "question_id_list"), idset(c, "question_id_list")
    gr, cr = idset(g, "rubric_atom_id_list"), idset(c, "rubric_atom_id_list")
    gm, cm = idset(g, "material_atom_id_list"), idset(c, "material_atom_id_list")
    shared_q = gq & cq
    shared_r = gr & cr
    shared_m = gm & cm
    text_g = " ".join(g.get(k, "") for k in ["plain_observation", "what_student_must_judge", "material_trigger", "legal_knowledge_or_rule_triggered", "rubric_reward", "must_have_keywords"])
    text_c = " ".join(c.get(k, "") for k in ["plain_observation", "what_student_must_judge", "material_trigger", "legal_knowledge_or_rule_triggered", "rubric_reward", "must_have_keywords"])
    kw = words(text_g) & words(text_c)
    tag_overlap = tags(g) & tags(c)
    score = len(shared_q) * 4 + len(shared_r) * 6 + len(shared_m) * 2 + len(kw) + len(tag_overlap) * 10
    if g.get("category") == c.get("category"):
        score += 2
    detail = {
        "shared_question_ids": "|".join(sorted(shared_q)),
        "shared_rubric_atom_ids": "|".join(sorted(shared_r)),
        "shared_material_atom_ids": "|".join(sorted(shared_m)),
        "keyword_overlap": "|".join(sorted(kw)),
        "tag_overlap": "|".join(sorted(tag_overlap)),
    }
    return score, detail


def source_formal_ok(detail: dict[str, str], g: dict[str, str], c: dict[str, str], rubric_levels: dict[str, str]) -> bool:
    rids = [r for r in detail.get("supporting_rubric_atom_ids_for_decision", detail.get("shared_rubric_atom_ids", "")).split("|") if r]
    if rids:
        return all(rubric_levels.get(r) == "formal" for r in rids)
    combined = (g.get("evidence_level", "") + " " + c.get("evidence_level", "")).lower()
    return "reference_only" not in combined and "missing" not in combined


def pair_observations(
    gpt: list[dict[str, str]],
    claude: list[dict[str, str]],
    maps: dict[str, dict[str, list[str] | dict[str, str] | set[str]]],
) -> tuple[list[dict[str, str]], list[str], list[str]]:
    candidates: list[tuple[float, int, int, dict[str, str]]] = []
    for i, g in enumerate(gpt):
        for j, c in enumerate(claude):
            score, detail = score_pair(g, c)
            if score >= 8 and detail.get("tag_overlap") and (detail.get("shared_question_ids") or detail.get("shared_rubric_atom_ids")):
                candidates.append((score, i, j, detail))
    candidates.sort(reverse=True, key=lambda x: x[0])
    used_g: set[int] = set()
    used_c: set[int] = set()
    rows: list[dict[str, str]] = []
    n = 1
    for score, i, j, detail in candidates:
        g, c = gpt[i], claude[j]
        used_g.add(i)
        used_c.add(j)
        match_type = "same" if score >= 18 and g.get("category") == c.get("category") else "similar"
        conflict = "conflict" in {g.get("category"), c.get("category")}
        if conflict:
            match_type = "conflict"
        shared_qids = idset({"ids": detail.get("shared_question_ids", "")}, "ids")
        support_rids = detail.get("shared_rubric_atom_ids") or "|".join(scoped_ids([g, c], "rubric_atom_id_list", shared_qids))
        support_mids = detail.get("shared_material_atom_ids") or "|".join(scoped_ids([g, c], "material_atom_id_list", shared_qids))
        detail["supporting_rubric_atom_ids_for_decision"] = support_rids
        detail["supporting_material_atom_ids_for_decision"] = support_mids
        support_ok = bool(shared_qids and support_rids and support_mids)
        formal_ok = source_formal_ok(detail, g, c, maps["rubric_levels"])
        both_strong = g.get("category") == "strong" and c.get("category") == "strong"
        gtags, ctags = tags(g), tags(c)
        asymmetric_meta_block = (
            ((("anti_template" in gtags) != ("anti_template" in ctags)) and "table" not in set(detail.get("tag_overlap", "").split("|")))
            or ("right_spelling" in gtags) != ("right_spelling" in ctags)
            or ((("labor" in gtags) != ("labor" in ctags)) and set(detail.get("tag_overlap", "").split("|")) <= {"contract"})
        )
        decision = "merge" if match_type in {"same", "similar"} and support_ok and formal_ok and both_strong and not asymmetric_meta_block else "pending"
        if match_type == "conflict":
            decision = "pending"
        rows.append({
            "comparison_id": f"CMP_COWORK_{n:03d}",
            "gpt_observation_id": g["observation_id"],
            "claude_observation_id": c["observation_id"],
            "match_type": match_type,
            **detail,
            "difference_description": f"score={score}; gpt_category={g.get('category')}; claude_category={c.get('category')}",
            "better_supported_side": "both" if support_ok else ("gpt" if g.get("has_required_ids") == "yes" else "claude" if c.get("has_required_ids") == "yes" else "neither"),
            "needs_source_check": "yes" if not support_ok or match_type == "conflict" or "reference_only" in (g.get("evidence_level", "") + c.get("evidence_level", "")) else "no",
            "decision": decision,
            "reason": "双模型强观察均发现且源表可核到共享题号/细则/材料；仅作为代码本观察，不直接等于框架节点。" if decision == "merge" else "需要回源或证据等级审查后再决定。",
            "gpt_plain_observation": g.get("plain_observation", ""),
            "claude_plain_observation": c.get("plain_observation", ""),
        })
        n += 1
    for i, g in enumerate(gpt):
        if i not in used_g:
            rows.append({
                "comparison_id": f"CMP_COWORK_{n:03d}",
                "gpt_observation_id": g["observation_id"],
                "claude_observation_id": "",
                "match_type": "gpt_only",
                "shared_question_ids": "",
                "shared_rubric_atom_ids": "",
                "shared_material_atom_ids": "",
                "keyword_overlap": "",
                "difference_description": f"gpt_category={g.get('category')}; no matched Claude observation above threshold",
                "better_supported_side": "gpt" if g.get("has_required_ids") == "yes" else "neither",
                "needs_source_check": "yes",
                "decision": "pending" if g.get("has_required_ids") == "yes" and g.get("category") in {"strong", "weak"} else "discard",
                "reason": "单模型观察，必须待下一轮或回源验证。",
                "gpt_plain_observation": g.get("plain_observation", ""),
                "claude_plain_observation": "",
            })
            n += 1
    for j, c in enumerate(claude):
        if j not in used_c:
            rows.append({
                "comparison_id": f"CMP_COWORK_{n:03d}",
                "gpt_observation_id": "",
                "claude_observation_id": c["observation_id"],
                "match_type": "claude_only",
                "shared_question_ids": "",
                "shared_rubric_atom_ids": "",
                "shared_material_atom_ids": "",
                "keyword_overlap": "",
                "difference_description": f"claude_category={c.get('category')}; no matched GPT observation above threshold",
                "better_supported_side": "claude" if c.get("has_required_ids") == "yes" else "neither",
                "needs_source_check": "yes",
                "decision": "pending" if c.get("has_required_ids") == "yes" and c.get("category") in {"strong", "weak"} else "discard",
                "reason": "单模型观察，必须待下一轮或回源验证。",
                "gpt_plain_observation": "",
                "claude_plain_observation": c.get("plain_observation", ""),
            })
            n += 1
    return rows, [g["observation_id"] for i, g in enumerate(gpt) if i not in used_g], [c["observation_id"] for j, c in enumerate(claude) if j not in used_c]


def build_codebook(comparisons: list[dict[str, str]], gpt_map: dict[str, dict[str, str]], claude_map: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    n = 1
    for cmp_row in comparisons:
        if cmp_row.get("decision") != "merge":
            continue
        g = gpt_map.get(cmp_row["gpt_observation_id"], {})
        c = claude_map.get(cmp_row["claude_observation_id"], {})
        if g.get("category") != "strong" or c.get("category") != "strong":
            continue
        code = {
            "code_id": f"CODE_COWORK_{n:03d}",
            "temporary_label": norm(c.get("plain_observation") or g.get("plain_observation"))[:80],
            "plain_description": norm(cmp_row.get("claude_plain_observation") or cmp_row.get("gpt_plain_observation")),
            "source_observation_ids": f"{cmp_row['gpt_observation_id']}|{cmp_row['claude_observation_id']}",
            "supporting_question_ids": cmp_row.get("shared_question_ids") or g.get("question_id_list") or c.get("question_id_list"),
            "supporting_rubric_atom_ids": cmp_row.get("supporting_rubric_atom_ids_for_decision") or cmp_row.get("shared_rubric_atom_ids") or g.get("rubric_atom_id_list") or c.get("rubric_atom_id_list"),
            "supporting_material_atom_ids": cmp_row.get("supporting_material_atom_ids_for_decision") or cmp_row.get("shared_material_atom_ids") or g.get("material_atom_id_list") or c.get("material_atom_id_list"),
            "evidence_level_summary": f"GPT: {g.get('evidence_level','')}; Claude: {c.get('evidence_level','')}",
            "ask_types_supported": f"GPT: {g.get('ask_type','')}; Claude: {c.get('ask_type','')}",
            "what_student_must_judge": c.get("what_student_must_judge") or g.get("what_student_must_judge", ""),
            "material_trigger_pattern": c.get("material_trigger") or g.get("material_trigger", ""),
            "legal_knowledge_or_rule_pattern": c.get("legal_knowledge_or_rule_triggered") or g.get("legal_knowledge_or_rule_triggered", ""),
            "rubric_reward_pattern": c.get("rubric_reward") or g.get("rubric_reward", ""),
            "full_score_sentence_pattern": c.get("full_score_sentence_pattern") or g.get("full_score_sentence_pattern", ""),
            "must_have_keywords": c.get("must_have_keywords") or g.get("must_have_keywords", ""),
            "module_boundary_risk": f"GPT: {g.get('module_boundary_risk','')}; Claude: {c.get('module_boundary_risk','')}",
            "risk_of_empty_value_talk": f"GPT: {g.get('risk_of_empty_value_talk','')}; Claude: {c.get('risk_of_empty_value_talk','')}",
            "risk_of_legal_exam_overanalysis": f"GPT: {g.get('risk_of_legal_exam_overanalysis','')}; Claude: {c.get('risk_of_legal_exam_overanalysis','')}",
            "transfer_potential": f"GPT: {g.get('transfer_potential','')}; Claude: {c.get('transfer_potential','')}",
            "counterexamples": f"GPT: {g.get('counterexamples','')}; Claude: {c.get('counterexamples','')}",
            "status": "provisional",
            "reason": "双模型强观察合并候选；进入代码本不等于最终框架节点，仍需全题压测。",
        }
        rows.append(code)
        n += 1
    return rows


def write_md_reports(gpt: list[dict[str, str]], claude: list[dict[str, str]], comparisons: list[dict[str, str]], codebook: list[dict[str, str]]) -> None:
    XVAL.mkdir(parents=True, exist_ok=True)
    lines = [
        "# GPT/Claude Observation Comparison - Cowork Refined Packet",
        "",
        "Input packet: `reasoner_packet_suite_exhaustive_cowork_refined_20260519.zip`.",
        "",
        f"- GPT observations parsed: {len(gpt)}",
        f"- Claude observations parsed: {len(claude)}",
        f"- Comparison rows: {len(comparisons)}",
        f"- Merge decisions: {sum(1 for r in comparisons if r['decision']=='merge')}",
        f"- Pending/source-check rows: {sum(1 for r in comparisons if r['needs_source_check']=='yes')}",
        "",
        "## Merge Candidates",
        "",
    ]
    for r in comparisons:
        if r["decision"] == "merge":
            lines.append(f"- `{r['comparison_id']}` `{r['gpt_observation_id']}` + `{r['claude_observation_id']}`: {r['match_type']}; shared_q={r['shared_question_ids'] or '-'}; reason={r['reason']}")
    lines += ["", "## Pending Or Conflicting", ""]
    for r in comparisons:
        if r["decision"] != "merge":
            lines.append(f"- `{r['comparison_id']}` {r['match_type']}: GPT=`{r['gpt_observation_id']}` Claude=`{r['claude_observation_id']}`; decision={r['decision']}; reason={r['reason']}")
    (XVAL / "gpt_claude_observation_comparison_cowork_refined_20260519.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    cb_lines = [
        "# Provisional Codebook v0 - Cowork Refined Packet",
        "",
        "This codebook is not a framework. It contains only merged strong observations from the fresh GPT-5.5 Pro and Claude Opus runs.",
        "",
    ]
    for row in codebook:
        cb_lines += [
            f"## {row['code_id']} - {row['temporary_label']}",
            "",
            f"- source_observation_ids: `{row['source_observation_ids']}`",
            f"- supporting_question_ids: `{row['supporting_question_ids']}`",
            f"- supporting_rubric_atom_ids: `{row['supporting_rubric_atom_ids']}`",
            f"- supporting_material_atom_ids: `{row['supporting_material_atom_ids']}`",
            f"- what_student_must_judge: {row['what_student_must_judge']}",
            f"- material_trigger_pattern: {row['material_trigger_pattern']}",
            f"- rubric_reward_pattern: {row['rubric_reward_pattern']}",
            f"- full_score_sentence_pattern: {row['full_score_sentence_pattern']}",
            f"- risk: empty_value={row['risk_of_empty_value_talk']}; legal_exam={row['risk_of_legal_exam_overanalysis']}",
            "",
        ]
    (CODEBOOK / "provisional_codebook_v0_cowork_refined_20260519.md").write_text("\n".join(cb_lines), encoding="utf-8")


def main() -> None:
    XVAL.mkdir(parents=True, exist_ok=True)
    CODEBOOK.mkdir(parents=True, exist_ok=True)
    maps = load_source_maps()
    gpt = parse_md(OPEN / "gpt55pro_open_observations_cowork_refined_20260519.md", "gpt55pro")
    claude = parse_md(OPEN / "claude_opus_open_observations_cowork_refined_20260519.md", "claude_opus")
    enrich_with_source_ids(gpt, maps)
    enrich_with_source_ids(claude, maps)
    obs_fields = ["model", "category", *FIELDS, "question_id_list", "rubric_atom_id_list", "material_atom_id_list", "has_required_ids", "source_check_notes"]
    write_csv(OPEN / "gpt55pro_open_observations_cowork_refined_20260519.csv", gpt, obs_fields)
    write_csv(OPEN / "claude_opus_open_observations_cowork_refined_20260519.csv", claude, obs_fields)
    write_jsonl(OPEN / "gpt55pro_open_observations_cowork_refined_20260519.jsonl", gpt)
    write_jsonl(OPEN / "claude_opus_open_observations_cowork_refined_20260519.jsonl", claude)

    comparisons, _, _ = pair_observations(gpt, claude, maps)
    cmp_fields = [
        "comparison_id", "gpt_observation_id", "claude_observation_id", "match_type",
        "shared_question_ids", "shared_rubric_atom_ids", "shared_material_atom_ids", "keyword_overlap", "tag_overlap",
        "supporting_rubric_atom_ids_for_decision", "supporting_material_atom_ids_for_decision",
        "difference_description", "better_supported_side", "needs_source_check", "decision", "reason",
        "gpt_plain_observation", "claude_plain_observation",
    ]
    write_csv(XVAL / "gpt_claude_observation_comparison_cowork_refined_20260519.csv", comparisons, cmp_fields)
    write_csv(XVAL / "strong_shared_observations_cowork_refined_20260519.csv", [r for r in comparisons if r["decision"] == "merge"], cmp_fields)
    write_csv(XVAL / "conflicting_observations_cowork_refined_20260519.csv", [r for r in comparisons if r["match_type"] == "conflict"], cmp_fields)
    write_csv(XVAL / "gpt_only_observations_cowork_refined_20260519.csv", [r for r in comparisons if r["match_type"] == "gpt_only"], cmp_fields)
    write_csv(XVAL / "claude_only_observations_cowork_refined_20260519.csv", [r for r in comparisons if r["match_type"] == "claude_only"], cmp_fields)
    write_csv(XVAL / "observations_needing_source_check_cowork_refined_20260519.csv", [r for r in comparisons if r["needs_source_check"] == "yes"], cmp_fields)

    gpt_map = {r["observation_id"]: r for r in gpt}
    claude_map = {r["observation_id"]: r for r in claude}
    codebook = build_codebook(comparisons, gpt_map, claude_map)
    cb_fields = [
        "code_id", "temporary_label", "plain_description", "source_observation_ids",
        "supporting_question_ids", "supporting_rubric_atom_ids", "supporting_material_atom_ids",
        "evidence_level_summary", "ask_types_supported", "what_student_must_judge",
        "material_trigger_pattern", "legal_knowledge_or_rule_pattern", "rubric_reward_pattern",
        "full_score_sentence_pattern", "must_have_keywords", "module_boundary_risk",
        "risk_of_empty_value_talk", "risk_of_legal_exam_overanalysis", "transfer_potential",
        "counterexamples", "status", "reason",
    ]
    write_csv(CODEBOOK / "provisional_codebook_v0_cowork_refined_20260519.csv", codebook, cb_fields)
    write_csv(CODEBOOK / "codebook_source_evidence_map_cowork_refined_20260519.csv", codebook, cb_fields)
    write_md_reports(gpt, claude, comparisons, codebook)
    risks = [
        "# Codebook Risks - Cowork Refined Packet",
        "",
        "- This codebook is provisional and not a final framework.",
        "- Observations using shorthand IDs like `..04`, `任一`, `全集`, or `略` must be source-checked before final promotion.",
        "- `reference_only` observations cannot independently support core nodes.",
        "- GPT and Claude both produced some high-level wording that resembles framework language; only ID-backed reward mechanisms are retained here.",
        "",
    ]
    (CODEBOOK / "codebook_risks_cowork_refined_20260519.md").write_text("\n".join(risks), encoding="utf-8")

    summary = {
        "gpt_observations": len(gpt),
        "claude_observations": len(claude),
        "comparisons": len(comparisons),
        "merge_decisions": sum(1 for r in comparisons if r["decision"] == "merge"),
        "pending_or_source_check": sum(1 for r in comparisons if r["needs_source_check"] == "yes"),
        "codebook_rows": len(codebook),
        "gpt_missing_required_ids": [r["observation_id"] for r in gpt if r["has_required_ids"] != "yes"],
        "claude_missing_required_ids": [r["observation_id"] for r in claude if r["has_required_ids"] != "yes"],
    }
    (XVAL / "cowork_refined_cross_validation_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
