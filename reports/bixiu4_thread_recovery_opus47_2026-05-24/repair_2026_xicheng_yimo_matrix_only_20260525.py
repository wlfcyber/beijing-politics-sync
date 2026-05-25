from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = RECOVERY / "XICHENG_2026_YIMO_MATRIX_ONLY_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "XICHENG_2026_YIMO_MATRIX_ONLY_REPAIR_20260525.json"

SUITE = "2026西城一模"
YEAR = "2026"
STAGE = "一模"
ROW_SOURCE = "codex_recovery_20260525_xicheng_2026_yimo_matrix_only"
BUNDLE = "data\\preprocessed_corpus\\gpt_suite_bundles\\2026各区模拟题__2026各区一模__2026西城一模.md"


def source(lines: str) -> str:
    return f"{BUNDLE}:{lines}"


def load_matrix() -> tuple[list[str], list[dict[str, str]]]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def write_matrix(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def next_matrix_id(rows: list[dict[str, str]]) -> int:
    nums: list[int] = []
    for row in rows:
        rid = row.get("matrix_row_id", "")
        if rid.startswith("M") and rid[1:].isdigit():
            nums.append(int(rid[1:]))
    return max(nums, default=0) + 1


def update_row(row: dict[str, str], **values: str) -> dict[str, str]:
    row.update(values)
    return row


def new_row(fieldnames: list[str], mid: int, question: str, question_type: str, in_book: str, node: str,
            support: str, evidence: str, misplaced: str, need_thick: str, current: str,
            note: str, artifact: str) -> dict[str, str]:
    row = {name: "" for name in fieldnames}
    row.update({
        "matrix_row_id": f"M{mid:04d}",
        "row_source": ROW_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": question,
        "题型或模块判断": question_type,
        "是否进宝典": in_book,
        "宝典节点": node,
        "细则支持原理": support,
        "证据等级": evidence,
        "是否误放": misplaced,
        "是否需补厚": need_thick,
        "当前处理": current,
        "备注": note,
        "source_artifact": artifact,
    })
    return row


def upsert_missing(rows: list[dict[str, str]], fieldnames: list[str], mid: int, question: str, node: str,
                   question_type: str, in_book: str, support: str, evidence: str, misplaced: str,
                   need_thick: str, current: str, note: str, artifact: str) -> tuple[int, str | None]:
    for row in rows:
        if row.get("题源") == SUITE and row.get("题号") == question and row.get("宝典节点") == node and row.get("当前处理") == current:
            return mid, None
    row = new_row(fieldnames, mid, question, question_type, in_book, node, support, evidence, misplaced, need_thick, current, note, artifact)
    rows.append(row)
    return mid + 1, row["matrix_row_id"]


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2026_xicheng_yimo_matrix_only_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    fieldnames, rows = load_matrix()
    by_id = {row.get("matrix_row_id", ""): row for row in rows}

    updated: list[str] = []
    added: list[str] = []

    formal_in_body = "是：已进入当前DOCX/PDF正文"
    no_body = "否：不进入当前哲学宝典正文"
    no_choice_key = "题干术语命中-无官方选择题答案键，非评分细则"
    no_choice_support = "缓存包仅见试卷题干，未见选择题官方答案键；不得把题干术语命中冒充正确选项链或主观题评分细则。"
    choice_status = "SOURCE_REVIEWED_NO_DOCX_ACTION"

    existing_updates = {
        "M0058": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="主观能动性 / 意识的能动作用",
            细则支持原理="Q16正式阅卷细则哲学与思维观点明确：发挥正确意识的促进作用（着眼阅读）。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="2026-05-25回源确认：当前DOCX已在该节点保留Q16正文条目。",
            source_artifact=source("22-31;280-283"),
        ),
        "M0059": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="联系的普遍性 / 联系的观点（总）",
            细则支持原理="Q16正式阅卷细则哲学与思维观点明确：联系观点（着眼全民）。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="2026-05-25回源确认：当前DOCX已在联系观点节点保留Q16正文条目。",
            source_artifact=source("22-31;280-283"),
        ),
        "M0060": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="发展的观点 / 发展的普遍性",
            细则支持原理="Q16正式阅卷细则哲学与思维观点明确：发展观点（着眼战略投资）。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="2026-05-25回源确认：当前DOCX已在发展观点节点保留Q16正文条目。",
            source_artifact=source("22-31;280-283"),
        ),
        "M0061": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="价值观的导向作用",
            细则支持原理="Q16正式阅卷细则哲学与思维观点明确：正确价值观的导向作用（着眼入法彰显国家导向）；辩证思维、超前思维另属选必三边界，不带入本节点。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="纠正旧矩阵误判：价值观是必修四哲学节点，当前DOCX已有Q16价值观正文条目；仅排除辩证思维/超前思维。",
            source_artifact=source("22-31;280-283"),
        ),
        "M0062": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="实践与认识（总）",
            细则支持原理="Q21正式阅卷细则明确可用实践观；当前DOCX已有实践与认识总论条目，围绕长期探索和实践生成中国式现代化道路展开。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="纠正旧矩阵误判：实践观属于必修四哲学；仅辩证思维、创新思维/超前思维排除。",
            source_artifact=source("100-110;334-358"),
        ),
        "M0063": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="矛盾的特殊性 / 具体问题具体分析",
            细则支持原理="Q21正式阅卷细则明确可用矛盾观；当前DOCX用中国式现代化不同于西式现代化、关键领域具体矛盾作答。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="2026-05-25回源确认：当前DOCX已保留Q21具体问题具体分析正文条目。",
            source_artifact=source("100-110;334-358"),
        ),
        "M0064": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="发展的观点 / 发展的普遍性",
            细则支持原理="Q21正式阅卷细则明确可用发展观；当前DOCX围绕承前启后、全面发力、攻坚突破展开。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="2026-05-25回源确认：当前DOCX已保留Q21发展观点正文条目。",
            source_artifact=source("100-110;334-358"),
        ),
        "M0065": dict(
            题型或模块判断="必修四哲学主观题正文条目",
            是否进宝典=formal_in_body,
            宝典节点="尊重客观规律与发挥主观能动性相结合",
            细则支持原理="Q21正式阅卷细则明确可用规律与主观能动性的关系；当前DOCX围绕关键时期尊重规律并主动探索展开。",
            证据等级="强细则",
            是否误放="否",
            是否需补厚="否",
            当前处理="KEEP_IN_BODY_VERIFIED",
            备注="2026-05-25回源确认：当前DOCX已保留Q21规律与主观能动性正文条目。",
            source_artifact=source("100-110;334-358"),
        ),
    }

    for rid, values in existing_updates.items():
        if rid in by_id:
            update_row(by_id[rid], **values)
            updated.append(rid)

    term_rows = {
        "M0618": ("Q1", "选择题边界", no_choice_support, source("142-147")),
        "M0619": ("Q4", "选择题政治治理边界", "Q4围绕政协提案、政府答复与国家治理，属于政治与法治选择题；缓存包未见官方答案键，不进入必修四哲学正文。", source("161-171")),
        "M0620": ("Q5", "选择题文化/意识边界", no_choice_support + " Q5虽含便利店文学、意识活动和人民群众文化创造等信号，但无官方答案键时不得新增正确选项链。", source("172-177")),
        "M0621": ("Q6", "选择题哲学边界", no_choice_support + " Q6虽含联系形式、价值转化等信号，但无官方答案键时不得新增正确选项链。", source("178-182")),
        "M0622": ("Q7", "选择题哲学边界", no_choice_support + " Q7虽含实践社会历史性和价值取向等信号，但无官方答案键时不得新增正确选项链。", source("183-188")),
        "M0623": ("Q11", "经济与社会选择题边界", "Q11是养老服务制度设计与资源配置题，属于经济与社会选择题；不进入当前哲学宝典正文。", source("234-239")),
        "M0624": ("Q12", "经济与社会选择题边界", "Q12是宏观经济读图与三大需求题，属于经济与社会选择题；不进入当前哲学宝典正文。", source("241-248")),
        "M0625": ("Q14", "选必三逻辑选择题边界", "Q14是北京中轴线建筑遗存的形式逻辑判断题，属于逻辑与思维边界；不进入必修四哲学正文。", source("260-272")),
        "M0626": ("Q15", "选必一国际政治经济选择题边界", "Q15围绕世贸组织改革与全球经济治理，属于当代国际政治与经济边界；不进入当前哲学宝典正文。", source("273-277")),
        "M0627": ("Q16", "正式细则主观题候选已承接", "Q16正式细则已由M0058-M0061及新增联系细化行承接，生产线术语候选行不再作为待补风险。", source("22-31;280-283")),
        "M0628": ("Q17", "法律与生活主观题边界", "Q17正式细则为民法典物权编、绿色原则、权利界限与法律责任，属于法律与生活；不进入当前哲学宝典正文。", source("38-48;286-294")),
        "M0629": ("Q18", "经济与社会主观题边界", "Q18正式细则为财政贴息、担保、风险补偿、资源配置和实体经济，属于经济与社会；不进入当前哲学宝典正文。", source("51-60;297-303")),
        "M0630": ("Q20", "选必一国际政治经济主观题边界", "Q20正式细则围绕东盟贸易、自贸区3.0、标准规则、供应链和全球经济治理，属于当代国际政治与经济；不进入当前哲学宝典正文。", source("81-99;319-331")),
        "M0631": ("Q21", "正式细则主观题候选已承接", "Q21正式细则已由实践观、矛盾观、发展观、规律与主观能动性、改革等正文行承接；辩证思维、创新思维/超前思维仍排除。", source("100-110;334-358")),
        "M0632": ("Qunknown", "抽取残留行", "该行是试卷抽取残留片段，不是独立题号；逐题覆盖已由Q1-Q21行承接。", source("127-358")),
    }
    for rid, (question, qtype, support, artifact) in term_rows.items():
        if rid in by_id:
            update_row(
                by_id[rid],
                题型或模块判断=qtype,
                是否进宝典=no_body if question != "Q16" and question != "Q21" else "否：生产线候选已由逐题正文行承接",
                宝典节点="不进入当前哲学宝典正文" if question != "Q16" and question != "Q21" else "候选行已由逐题正文矩阵承接",
                细则支持原理=support,
                证据等级=no_choice_key if question in {"Q1", "Q5", "Q6", "Q7"} else ("强细则" if question in {"Q16", "Q17", "Q18", "Q20", "Q21"} else "模块边界/题干边界"),
                是否误放="否",
                是否需补厚="否",
                当前处理=choice_status if question in {"Q1", "Q5", "Q6", "Q7"} else ("SUPERSEDED_BY_ROW_LEVEL_REPAIR" if question in {"Q16", "Q21", "Qunknown"} else "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED"),
                备注="2026-05-25回源闭合：不作为当前DOCX新增依据。",
                source_artifact=artifact,
            )
            updated.append(rid)

    superseded = {
        "M0165": ("Q16", "Q16生产线候选已由M0058-M0061及新增联系细化行承接。", source("22-31;280-283")),
        "M0166": ("Q21", "Q21生产线候选已由M0062-M0065及新增发展/实践/改革细化行承接。", source("100-110;334-358")),
        "M0228": ("Q16", "Q16母版覆盖口径已由本轮逐题矩阵核定。", source("22-31;280-283")),
        "M0229": ("Q21", "Q21母版覆盖口径已由本轮逐题矩阵核定。", source("100-110;334-358")),
        "M0230": ("Q19(3)", "Q19(3)正式细则为形式逻辑判断，属于选必三逻辑与思维，边界排除。", source("75-79;313-318")),
        "M0802": ("SUITE_LEVEL", "套卷级覆盖口径已由2026-05-25逐题矩阵修复承接。", source("22-110;142-358")),
        "M0859": ("SUITE_LEVEL", "套卷级覆盖口径已由2026-05-25逐题矩阵修复承接。", source("22-110;142-358")),
    }
    for rid, (question, support, artifact) in superseded.items():
        if rid in by_id:
            update_row(
                by_id[rid],
                题号=question,
                题型或模块判断="套卷/候选口径已由逐题矩阵修复承接" if question == "SUITE_LEVEL" else by_id[rid].get("题型或模块判断", ""),
                是否进宝典="候选已核：由逐题矩阵承接" if question != "SUITE_LEVEL" else "套卷级行已被逐题矩阵承接",
                宝典节点="SUPERSEDED_BY_ROW_LEVEL_MATRIX",
                细则支持原理=support,
                证据等级="强细则" if question in {"Q16", "Q21"} else "模块边界/套卷级承接",
                是否误放="否",
                是否需补厚="否",
                当前处理="SUPERSEDED_BY_ROW_LEVEL_REPAIR",
                备注="2026-05-25本轮回源闭合。",
                source_artifact=artifact,
            )
            updated.append(rid)

    mid = next_matrix_id(rows)
    additions = [
        ("Q2", "不进入当前哲学宝典正文", "选择题政治/公共治理边界", no_body, "Q2围绕文旅部门规划公共路线、公共利益保护与群众文化创意平衡，缓存包未见官方答案键；不进入当前哲学宝典正文。", "模块边界/无官方答案键", "否", "否", "SOURCE_REVIEWED_NO_DOCX_ACTION", "逐题覆盖补齐。", source("148-153")),
        ("Q3", "不进入当前哲学宝典正文", "政治与法治选择题边界", no_body, "Q3围绕基层干部、党员先锋模范和基层党组织群众组织力，属于政治与法治选择题；不进入当前哲学宝典正文。", "模块边界/无官方答案键", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("155-160")),
        ("Q8", "不进入当前哲学宝典正文", "经济与社会选择题边界", no_body, "Q8围绕企业、合作社、农户收益分配与乡村产业发展，属于经济与社会选择题；不进入当前哲学宝典正文。", "模块边界/无官方答案键", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("189-222")),
        ("Q9", "不进入当前哲学宝典正文", "法律与生活选择题边界", no_body, "Q9是合同履行与不可抗力题，属于法律与生活；不进入当前哲学宝典正文。", "模块边界/无官方答案键", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("223-227")),
        ("Q10", "不进入当前哲学宝典正文", "法律与生活选择题边界", no_body, "Q10是加装电梯、业主决议与相邻权益题，属于法律与生活；不进入当前哲学宝典正文。", "模块边界/无官方答案键", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("228-233")),
        ("Q13", "不进入当前哲学宝典正文", "法律/逻辑选择题边界", no_body, "Q13围绕商标法条和形式逻辑推理，属于法律与生活/选必三逻辑边界；不进入当前哲学宝典正文。", "模块边界/无官方答案键", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("249-258")),
        ("Q16", "整体与部分", "必修四哲学主观题正文条目", formal_in_body, "Q16正式阅卷细则写明联系观点（着眼全民）；当前DOCX用政府、社会、家庭和个人共同承担阅读责任细化为整体与部分关系。", "强细则", "否", "否", "KEEP_IN_BODY_VERIFIED", "新增矩阵行以覆盖当前DOCX已有整体与部分条目。", source("22-31;280-283")),
        ("Q19(1)", "不进入当前哲学宝典正文", "政治与法治主观题边界", no_body, "Q19(1)正式细则为民主监督相关环节补充，属于政治与法治；不进入当前哲学宝典正文。", "强细则-模块边界", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("63-65;306-313")),
        ("Q19(2)", "不进入当前哲学宝典正文", "政治与法治主观题边界", no_body, "Q19(2)正式细则为党的领导、线上线下收集民意、多元主体参与、民主协商民主决策等政治与法治内容；不进入当前哲学宝典正文。", "强细则-模块边界", "否", "否", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "逐题覆盖补齐。", source("66-74;306-315")),
        ("Q21", "量变与质变 / 适度原则", "必修四哲学主观题正文条目", formal_in_body, "Q21正式阅卷细则明确可用发展观；当前DOCX用关键时期、攻坚突破、条件积累和发展跃升展开量变质变链条。", "强细则", "否", "否", "KEEP_IN_BODY_VERIFIED", "新增矩阵行以覆盖当前DOCX已有量变质变条目。", source("100-110;334-358")),
        ("Q21", "实践是认识的基础", "必修四哲学主观题正文条目", formal_in_body, "Q21正式阅卷细则明确可用实践观；当前DOCX用新的探索实践产生新认识并检验修正方案展开。", "强细则", "否", "否", "KEEP_IN_BODY_VERIFIED", "新增矩阵行以覆盖当前DOCX已有实践是认识基础条目。", source("100-110;334-358")),
        ("Q21", "改革 / 改革的实质", "必修四哲学主观题正文条目", formal_in_body, "Q21正式阅卷细则明确可用改革知识；当前DOCX用改革是社会主义制度自我完善和发展、破解体制机制障碍展开。", "强细则", "否", "否", "KEEP_IN_BODY_VERIFIED", "新增矩阵行以覆盖当前DOCX已有改革条目。", source("100-110;334-358")),
    ]
    for question, node, qtype, in_book, support, evidence, misplaced, need_thick, current, note, artifact in additions:
        mid, rid = upsert_missing(rows, fieldnames, mid, question, node, qtype, in_book, support, evidence, misplaced, need_thick, current, note, artifact)
        if rid:
            added.append(rid)

    write_matrix(fieldnames, rows)

    summary = {
        "status": "XICHENG_2026_YIMO_MATRIX_ONLY_REPAIR_COMPLETE_NO_DOCX_CHANGE",
        "timestamp": ts,
        "matrix_backup": str(backup),
        "updated_rows": updated,
        "added_rows": added,
        "docx_changed": False,
        "decisions": [
            "Q16 value-guidance row corrected from module-boundary exclusion to in-body strong-rubric support.",
            "Q21 practice row corrected from module-boundary exclusion to in-body strong-rubric support.",
            "Current DOCX Q16/Q21 entries were mapped to explicit row-level matrix support.",
            "Choice-question term hits without official answer key were closed as no-DOCX-action, not promoted to correct-option chains.",
            "Q17/Q18/Q19/Q20 non-B4 main questions were closed as module-boundary exclusions.",
        ],
        "open_model_gates": [
            "GPTPro web artifact review real_call_pending",
            "Claude Opus web/app artifact review through direct https://claude.ai real_call_pending",
            "ClaudeCode model confirmation BLOCKED_MODEL_CONFIRMATION_REQUIRED",
        ],
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# XICHENG_2026_YIMO_MATRIX_ONLY_REPAIR_20260525",
        "",
        "Status: `XICHENG_2026_YIMO_MATRIX_ONLY_REPAIR_COMPLETE_NO_DOCX_CHANGE_MODEL_GATES_OPEN`",
        "",
        f"- Timestamp: `{ts}`.",
        f"- Matrix backup: `{backup.name}`.",
        f"- Updated existing matrix rows: `{len(updated)}`.",
        f"- Added explicit coverage rows: `{len(added)}`.",
        "- DOCX/PDF changed: `NO`.",
        "- Render rerun required by this repair: `NO_DOCX_CHANGE_USE_LATEST_RENDER_QA`.",
        "",
        "## Key Decisions",
        "",
        "- Q16 value-guidance support is corrected to in-body strong-rubric support; the old boundary-exclusion row was wrong because value guidance is a 必修四哲学 node.",
        "- Q21 practice support is corrected to in-body strong-rubric support; only 辩证思维/创新思维/超前思维 stay outside this book boundary.",
        "- Choice-question term hits are not promoted to correct-option chains because the cache packet does not contain an official answer key for Q1-Q15.",
        "- Q17/Q18/Q19/Q20 are closed as law/economics/politics/international/logic module boundaries, not as philosophy omissions.",
        "- No ordinary reference answer was used as scoring-rule evidence.",
        "",
        "## Added Rows",
        "",
    ]
    for rid in added:
        lines.append(f"- `{rid}`")
    lines.extend([
        "",
        "## Model Gate Boundary",
        "",
        "- No new external model evidence was created by this local matrix repair.",
        "- GPTPro web review remains `real_call_pending`.",
        "- Claude Opus web/app full artifact review remains `real_call_pending` through direct `https://claude.ai` auto-login path.",
        "- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
    ])
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
