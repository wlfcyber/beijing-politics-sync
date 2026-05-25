from __future__ import annotations

import csv
import re
import shutil
import zipfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH17_2025_MENTOUGOU_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH17_2025_MENTOUGOU_YIMO_CODEX_20260525.md"

FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"

PREPROCESSED = Path(r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus")
PAPER_TEXT = PREPROCESSED / "texts" / "1d8a23fe11f59810_2025北京门头沟高三一模政治_教师版.txt"
RUBRIC_TEXT = PREPROCESSED / "texts" / "26d9b228064053c1_2025门头沟一模细则.txt"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区一模__2025门头沟一模.md"
SUITE_BUNDLE = RUN / "01_source_inventory" / "suite_source_bundles" / "2025门头沟一模.md"
BASE_DOCX_TEXT = RUN / "01_source_inventory" / "accepted_base_docx_text.txt"

SUITE = "2025门头沟一模"
YEAR = "2025"
STAGE = "一模"
ANSWER_KEY = "1C 2A 3B 4A 5D 6C 7C 8B 9A 10A 11B 12B 13B 14D 15D"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def excerpt_between(text: str, start_marker: str, end_marker: str | None, max_len: int = 4200) -> str:
    start = text.find(start_marker)
    if start < 0:
        return f"[missing marker: {start_marker}]"
    end = text.find(end_marker, start + len(start_marker)) if end_marker else -1
    if end < 0:
        end = min(len(text), start + max_len)
    return text[start:end].strip()[:max_len]


def current_docx_text() -> tuple[Path, str]:
    docxs = [p for p in DELIVERY.glob("*.docx") if "backup" not in p.name.lower()]
    if len(docxs) != 1:
        raise RuntimeError(f"Expected exactly one current docx, found {len(docxs)}")
    docx = docxs[0]
    with zipfile.ZipFile(docx) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
    return docx, re.sub(r"<[^>]+>", "", xml)


def write_csv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def apply_matrix_updates() -> dict[str, int | str]:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = RECOVERY / f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch17_2025_mentougou_yimo_{stamp}.csv"
    shutil.copy2(MATRIX, backup)

    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    c_id, c_suite, c_q = headers[0], headers[2], headers[5]
    c_type, c_in, c_node = headers[6], headers[7], headers[8]
    c_rule, c_evidence = headers[9], headers[10]
    c_misplaced, c_thicken, c_action = headers[11], headers[12], headers[13]
    c_note, c_artifact = headers[14], headers[15]

    source_packet = (
        "BATCH17_2025_MENTOUGOU_YIMO_SOURCE_TRANSCRIPTION_20260525.md; "
        "C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/"
        "gpt_suite_bundles/2025各区模拟题__2025各区一模__2025门头沟一模.md; "
        "current DOCX text verified"
    )

    updates: dict[str, dict[str, str]] = {
        "M0095": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖该哲学节点；文化4分另走文化线",
            c_rule: "正式评分细则：哲学加2分可从联系的观点看问题、发展的观点看问题、对立统一、价值判断与价值选择任一结合材料作答。",
            c_evidence: "强细则+当前DOCX",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "旧blocked/culture_boundary行经源证据复核改闭合；不新增正文。",
        },
        "M0096": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖",
            c_rule: "正式评分细则支持价值判断和价值选择的标准：符合社会发展的需求，满足人们对文化生活的更高追求。",
            c_evidence: "强细则+当前DOCX",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "旧question_prompt_not_verified阻塞已由教师版试卷、细则和当前DOCX三方闭合。",
        },
        "M0097": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖该哲学节点；文化4分另走文化线",
            c_rule: "正式评分细则：哲学加2分可从发展的观点看问题等角度结合材料作答。",
            c_evidence: "强细则+当前DOCX",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "旧culture_boundary行中哲学加分点已闭合；不新增正文。",
        },
        "M0136": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖",
            c_rule: "正式评分细则支持价值判断与价值选择；当前DOCX已含对应条目。",
            c_evidence: "强细则+当前DOCX",
            c_action: "BATCH17_CONFIRMED_EXISTING_DOCX_COVERED",
            c_note: "保留既有resolved_by_final_docx结论并补充源证据口径。",
        },
        "M0187": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖",
            c_node: "联系的观点看问题 / 发展的观点看问题 / 对立统一 / 价值判断与价值选择",
            c_rule: "正式评分细则明确文化4分+哲学2分；哲学可从联系、发展、对立统一、价值判断与价值选择任一结合材料作答。",
            c_evidence: "强细则+当前DOCX",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "旧候选遗漏经当前DOCX 4处Q16条目闭合；不重复插入。",
        },
        "M0216": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖",
            c_node: "联系 / 发展 / 对立统一 / 价值判断与价值选择",
            c_rule: "正式评分细则支持上述哲学加分点；当前DOCX已有4条Q16覆盖。",
            c_evidence: "强细则+当前DOCX",
            c_action: "BATCH17_CONFIRMED_NO_ACTION",
            c_note: "NO_ACTION改为源证据闭合状态。",
        },
        "M0500": {
            c_type: "main_question_philosophy_addon_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖",
            c_node: "联系的观点看问题 / 发展的观点看问题 / 对立统一 / 价值判断与价值选择",
            c_rule: "Q16原题明确《哲学与文化》；正式细则支持哲学加2分四类落点。",
            c_evidence: "强细则+当前DOCX",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "生产线候选已回源；当前DOCX已有覆盖，不新增。",
        },
        "M0188": {
            c_type: "module_boundary_excluded_q21_1_scientific_thinking",
            c_in: "否：Q21第(1)问为选必三科学思维，不进必修四哲学宝典",
            c_node: "选必三科学思维 / 辩证思维 / 创新思维",
            c_rule: "设问明示“运用科学思维知识”；21(1)细则也按辩证思维、创新思维、科学思维给分。",
            c_evidence: "强细则-模块边界",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_MODULE_BOUNDARY_SOURCE_REVIEW",
            c_note: "不得把选必三科学思维细则升级为必修四哲学主链。",
        },
        "M0217": {
            c_type: "module_boundary_excluded_q21_1_scientific_thinking",
            c_in: "否：Q21第(1)问为选必三科学思维，不进必修四哲学宝典",
            c_node: "选必三科学思维 / 辩证思维 / 创新思维",
            c_rule: "设问明示“运用科学思维知识”；21(1)细则也按辩证思维、创新思维、科学思维给分。",
            c_evidence: "强细则-模块边界",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_MODULE_BOUNDARY_SOURCE_REVIEW",
            c_note: "边界排除结论经源证据确认。",
        },
        "M0492": {
            c_type: "choice_philosophy_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖（选择题答案链）",
            c_node: "认识受主客观因素影响 / 认识具有主体差异性",
            c_rule: "教师版答案键Q6=C；题干呈现支持者与反对者对AI著作权的不同看法，体现认识主体差异性。选择题只按客观答案链入宝典，非主观题细则。",
            c_evidence: "客观答案键+题干；非主观细则",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "当前DOCX已有1处Q6条目；不新增。",
        },
        "M0493": {
            c_type: "choice_philosophy_existing_docx_covered",
            c_in: "是：最终DOCX已覆盖（选择题答案链）",
            c_node: "人生价值的创造和实现 / 个人与社会的统一 / 主观能动性",
            c_rule: "教师版答案键Q7=C；②③正确，材料对应充分发挥主观能动性和在个人与社会统一中创造价值。",
            c_evidence: "客观答案键+题干；非主观细则",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_COVERED",
            c_note: "当前DOCX已有1处Q7条目；不新增。",
        },
        "M0505": {
            c_type: "q21_split_boundary_and_existing_docx_secondary_coverage",
            c_in: "第(1)问否：选必三科学思维；第(2)问是：最终DOCX已有次级模块覆盖",
            c_node: "一切从实际出发 / 意识能动作用 / 实践与认识具体历史统一 / 价值判断与价值选择",
            c_rule: "21(1)设问和细则均为科学思维；21-2评分细则与阅卷总结注明经济与社会模块优先，其他模块包括主观与客观、认识与实践具体历史统一，正确价值判断与选择，意识能动作用。",
            c_evidence: "正式细则/阅卷总结-次级模块支持+当前DOCX",
            c_misplaced: "否：第(2)问保留为次级细则支持，第(1)问排除",
            c_thicken: "否：已有DOCX 4处；不得升级为主链",
            c_action: "BATCH17_CLOSED_EXISTING_DOCX_SECONDARY_SUPPORT",
            c_note: "Q21不得被当作逐点必修四主观题细则；只能保留第(2)问综合设问的次级模块证据。",
        },
        "M0793": {
            c_action: "BATCH17_SUITE_SOURCE_REVIEW_CLOSED",
            c_note: "Batch17逐题回源：DOCX mentions=10；Q6/Q7/Q16/Q21覆盖确认；其他候选为模块边界或旧术语误报。",
            c_thicken: "否",
        },
        "M0836": {
            c_action: "BATCH17_SUITE_SOURCE_REVIEW_CLOSED",
            c_note: "Batch17逐题回源：正式细则/教师版答案/当前DOCX一致；无新增正文。",
            c_thicken: "否",
        },
    }

    module_boundary = {
        "M0487": ("Q1", "中国特色社会主义/历史与经济社会边界"),
        "M0488": ("Q2", "政治与法治/国家安全与实践活动边界"),
        "M0489": ("Q3", "法律与生活边界"),
        "M0490": ("Q4", "民族政策与政治边界"),
        "M0491": ("Q5", "文化模块选择题，非哲学主链"),
        "M0494": ("Q8", "经济与社会边界"),
        "M0495": ("Q9", "当代国际政治与经济边界"),
        "M0496": ("Q10", "当代国际政治与经济/国际组织边界"),
        "M0497": ("Q11", "当代国际政治与经济/开放型经济边界"),
        "M0498": ("Q13", "法律与生活边界"),
        "M0499": ("Q15", "选必三逻辑与思维边界"),
        "M0501": ("Q17", "政治与法治边界"),
        "M0502": ("Q18", "经济与社会边界"),
        "M0503": ("Q19", "当代国际政治与经济边界"),
        "M0504": ("Q20", "法律与生活边界"),
        "M0506": ("Qunknown", "整卷文本误切片/重复来源，不作为独立题目"),
    }

    for row_id, (question, reason) in module_boundary.items():
        updates[row_id] = {
            c_type: "module_boundary_or_false_positive_source_reviewed",
            c_in: "否：模块边界排除或旧术语误报",
            c_node: "不进入当前哲学宝典正文",
            c_rule: f"{question}经教师版题干/答案键回源，属于{reason}；不是必修四哲学可复用落点。",
            c_evidence: "题干+答案键源审；无必修四哲学细则",
            c_misplaced: "否",
            c_thicken: "否",
            c_action: "BATCH17_CLOSED_MODULE_BOUNDARY_SOURCE_REVIEW",
            c_note: "旧codex_a术语命中来自整卷/细则邻近文本，不作为入宝典证据。",
        }

    touched = 0
    for r in rows:
        if r.get(c_suite) != SUITE:
            continue
        row_id = r.get(c_id, "")
        if row_id in updates:
            r.update(updates[row_id])
            r[c_artifact] = source_packet
            touched += 1

    write_csv(MATRIX, headers, rows)

    suite_rows = [r for r in rows if r.get(c_suite) == SUITE]
    open_markers = ["待核", "疑似", "base_has", "possible_omission", "weak_hit", "BLOCKED_OR_SKIPPED", "HOLD", "TO_BE_PLACED"]
    open_rows = [
        r for r in suite_rows
        if any(marker in " | ".join(r.values()) for marker in open_markers)
    ]
    return {
        "backup": str(backup),
        "touched": touched,
        "suite_rows": len(suite_rows),
        "open_rows": len(open_rows),
    }


def build_reports(matrix_stats: dict[str, int | str]) -> dict[str, int | str]:
    paper = read_text(PAPER_TEXT)
    rubric = read_text(RUBRIC_TEXT)
    docx, docx_text = current_docx_text()
    pdf = next((p for p in DELIVERY.glob("*.pdf") if "backup" not in p.name.lower()), None)

    q6_q7 = excerpt_between(paper, "6. 关于AI", "8. 现代化")
    q16 = excerpt_between(paper, "16. 北京文旅", "17. 商以求同")
    q21 = excerpt_between(paper, "21. 从千年煤城", "参考答案")
    answer = excerpt_between(paper, "参考答案", None, 5200)
    rubric16 = excerpt_between(rubric, "16题评分细则", "17细则")
    rubric21 = excerpt_between(rubric, "21（1）细则", None, 5200)

    suite_mentions = docx_text.count(SUITE)
    counts = {
        "Q6": docx_text.count(f"{SUITE} 第6题"),
        "Q7": docx_text.count(f"{SUITE} 第7题"),
        "Q16": docx_text.count(f"{SUITE} 第16题"),
        "Q21": docx_text.count(f"{SUITE} 第21题"),
    }

    SOURCE_TRANSCRIPTION.write_text(
        f"""# Batch17 Source Transcription - 2025门头沟一模

status: source_review_closed_no_docx_insert

## Source Packet

- paper/answer text: `{PAPER_TEXT}`
- rubric text: `{RUBRIC_TEXT}`
- GPT suite bundle: `{GPT_BUNDLE}`
- suite inventory bundle: `{SUITE_BUNDLE}`
- current DOCX: `{docx}`
- current PDF: `{pdf}`

## Objective Answer Key

`{ANSWER_KEY}`

Evidence source: teacher-version PDF cached text, not a subjective scoring rubric. It is sufficient for choice-question placement only.

## Target Question Text

### Q6-Q7

```text
{q6_q7}
```

### Q16

```text
{q16}
```

### Q21

```text
{q21}
```

## Answer / Rubric Evidence

### Teacher-Version Answer Segment

```text
{answer}
```

### Q16 Formal Scoring Rule

```text
{rubric16}
```

### Q21 Formal Scoring Rule / Marking Summary

```text
{rubric21}
```

## Codex Source Judgment

| Question | Decision | Evidence grade | Placement |
|---|---|---|---|
| Q1-Q5 except Q5 culture | boundary/exclude | source-reviewed | no philosophy insert |
| Q5 | culture choice only | answer-key source | not philosophy mainline |
| Q6 | covered in current DOCX | answer-key + prompt | 认识受主客观因素影响 / 主体差异性 |
| Q7 | covered in current DOCX | answer-key + prompt | 人生价值创造、个人与社会统一、主观能动性 |
| Q8-Q15 except Q15 | boundary/exclude | source-reviewed | no philosophy insert |
| Q15 | selected compulsory 3 logic/thinking | source-reviewed | exclude from 必修四哲学宝典 |
| Q16 | covered in current DOCX | formal scoring rule + current DOCX | 联系、发展、对立统一、价值判断与价值选择 |
| Q17-Q20 | boundary/exclude | source-reviewed | no philosophy insert |
| Q21(1) | exclude | formal scoring rule module boundary | selected compulsory 3 scientific thinking |
| Q21(2) | keep existing DOCX coverage only | formal marking summary with secondary-module support | no upgrade to main-chain evidence |

## Current DOCX Coverage Count

- suite mentions: `{suite_mentions}`
- Q6/Q7/Q16/Q21 mentions: `{counts}`
""",
        encoding="utf-8",
    )

    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch17 - 2025门头沟一模

status: `BATCH17_CLOSED_SOURCE_REVIEW_NO_DOCX_CHANGE`

## Scope

This batch resolves the stale open/candidate rows for `2025门头沟一模` in `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.

No DOCX/PDF content was changed. The current DOCX already contains the necessary 2025门头沟 entries:

- suite mentions: `{suite_mentions}`
- Q6: `{counts['Q6']}`
- Q7: `{counts['Q7']}`
- Q16: `{counts['Q16']}`
- Q21: `{counts['Q21']}`

## Matrix Outcome

- suite rows after update: `{matrix_stats['suite_rows']}`
- rows updated: `{matrix_stats['touched']}`
- open-ish rows remaining for this suite: `{matrix_stats['open_rows']}`
- matrix backup: `{matrix_stats['backup']}`

## Decisions

1. Q6 is a choice-question philosophy entry supported by the objective answer key (`C`) and prompt text; it remains existing DOCX coverage, not a new insert.
2. Q7 is a choice-question philosophy entry supported by the objective answer key (`C`) and prompt text; it remains existing DOCX coverage, not a new insert.
3. Q16 has formal scoring-rule support for `联系的观点看问题`, `发展的观点看问题`, `对立统一`, and `价值判断与价值选择`; current DOCX already has four Q16 entries.
4. Q21(1) is excluded because the prompt and scoring rule are explicitly `科学思维` / selected compulsory 3.
5. Q21(2) remains existing DOCX coverage only under secondary-module support. Its marking summary prioritizes `经济与社会`; philosophy terms may be kept where the summary explicitly names them, but must not be upgraded into point-by-point main-chain scoring evidence.
6. Q1-Q5 except Q6/Q7, Q8-Q15, and Q17-Q20 are source-reviewed module boundaries or old term-hit false positives.

## No-New-Insert Rationale

The final DOCX already covers all justified philosophy placements for this suite. Adding duplicate entries would inflate the宝典 and weaken traceability.
""",
        encoding="utf-8",
    )

    append_recovery_reports(matrix_stats, docx, pdf, suite_mentions, counts)

    return {
        "suite_mentions": suite_mentions,
        "q6": counts["Q6"],
        "q7": counts["Q7"],
        "q16": counts["Q16"],
        "q21": counts["Q21"],
    }


def append_once(path: Path, marker: str, text: str) -> None:
    current = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    if marker in current:
        return
    path.write_text(current.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def append_recovery_reports(
    matrix_stats: dict[str, int | str],
    docx: Path,
    pdf: Path | None,
    suite_mentions: int,
    counts: dict[str, int],
) -> None:
    render_marker = "## Batch17 2025门头沟一模 QA - 2026-05-25"
    append_once(
        FORMAT_QA,
        render_marker,
        f"""{render_marker}

- status: `NO_DOCX_CHANGE_CURRENT_RENDER_STILL_CONTROLS`
- checked files: `{docx}`; `{pdf}`
- current DOCX mentions for `2025门头沟一模`: `{suite_mentions}`; Q6/Q7/Q16/Q21 = `{counts}`
- decision: Batch17 updated matrix/report files only. No new DOCX or PDF export was required.
- typography/render boundary: existing current DOCX/PDF sizes and Batch16 render evidence remain the controlling render QA until the next actual DOCX edit.
- blocker: external full-artifact GPTPro web / Claude Opus review remains `real_call_pending`.
""",
    )

    governor_marker = "## Batch17 Governor Recovery Check - 2025门头沟一模"
    append_once(
        GOVERNOR,
        governor_marker,
        f"""{governor_marker}

- status: `PASS_WITH_MODEL_GATE_PENDING`
- matrix rows touched: `{matrix_stats['touched']}`; suite rows: `{matrix_stats['suite_rows']}`; open-ish suite rows after update: `{matrix_stats['open_rows']}`
- source result: Q6/Q7 covered by objective answer key and current DOCX; Q16 covered by formal scoring rule and current DOCX; Q21(1) excluded as selected compulsory 3; Q21(2) kept only as secondary-module support.
- no forbidden final acceptance status is claimed.
- model evidence: ClaudeCode Opus 4.7 recheck still required for this batch.
- external review: GPTPro web / Claude Opus full-artifact review remains `real_call_pending`.
""",
    )

    confucius_marker = "## Batch17 Confucius Artifact Check - 2025门头沟一模"
    append_once(
        CONFUCIUS,
        confucius_marker,
        f"""{confucius_marker}

- student-facing artifact impact: no new DOCX entry; existing entries are kept because they are already present and source-supported.
- evidence discipline: Q21(2) is not promoted beyond its marking-summary wording; Q21(1) stays excluded.
- coverage discipline: stale candidate rows were closed with explicit source-review reasons instead of being left as `待核`.
- remaining blocker: Opus 4.7 model gate and external reviews are not closed.
""",
    )

    status_marker = "## Batch17 2025门头沟一模 - 2026-05-25"
    append_once(
        THREAD_STATUS,
        status_marker,
        f"""{status_marker}

- status: `RECOVERED_EXECUTION_IN_PROGRESS`
- batch state: `BATCH17_SOURCE_REVIEW_CLOSED_NO_DOCX_CHANGE`
- files created: `{SOURCE_TRANSCRIPTION.name}`, `{BATCH_REPORT.name}`, `{Path(__file__).name}`
- matrix state: `{matrix_stats['suite_rows']}` suite rows; `{matrix_stats['open_rows']}` open-ish rows after update.
- model state: ClaudeCode Opus 4.7 recheck pending for this batch.
""",
    )


def main() -> None:
    matrix_stats = apply_matrix_updates()
    coverage_stats = build_reports(matrix_stats)
    print(
        {
            "matrix": matrix_stats,
            "coverage": coverage_stats,
            "source_transcription": str(SOURCE_TRANSCRIPTION),
            "batch_report": str(BATCH_REPORT),
        }
    )


if __name__ == "__main__":
    main()
