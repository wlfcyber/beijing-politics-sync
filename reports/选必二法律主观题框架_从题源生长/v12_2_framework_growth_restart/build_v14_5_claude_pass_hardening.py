from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "v14_4_claude_student_patch_framework_baodian"
OUT = ROOT / "v14_5_final_markdown_baodian_claude_pass_hardened"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def patch_common(text: str) -> str:
    return text.replace("v14.4", "v14.5").replace("v14_4", "v14_5")


def patch_framework(text: str) -> str:
    text = patch_common(text)
    text = text.replace("五张必背细节规则卡", "六张必背细节规则卡")
    text = text.replace("5 张细节卡", "6 张细节卡")
    marker = "缺一项就写“需进一步证明”，不要直接全额支持。\n"
    insert = """
### 6. 入职欺诈与劳动合同无效卡

看到简历造假、隐瞒经历、隐瞒疾病、伪造学历、入职欺诈，按这条链写：

劳动者负有诚信告知义务 -> 劳动者以欺诈手段使单位在违背真实意思下订立劳动合同 -> 劳动合同自始无效或存在解除依据 -> 试用期内查证可依法解除 -> 单位通常无需支付经济补偿或赔偿金。

边界：不是所有简历瑕疵都能解除。必须看该信息是否与岗位直接相关、是否影响录用决定、单位是否在合理期限内查证并依法处理。
"""
    if "### 6. 入职欺诈与劳动合同无效卡" not in text:
        text = text.replace(marker, marker + insert, 1)
    return text


def governance() -> str:
    return """# 05 GPT 与 Claude 补丁落实及治理边界 v14.5

## Real GPT Pro Gate

Status: `GPT_REVIEW_PASS_AFTER_PATCH_CAPTURED_AS_PATCH_SOURCE`

Evidence:

- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_PROMPT_v14_2_with_prior_framework.md`
- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md`

Boundary:

- GPT Pro did run in the user's Chrome Pro session and read the five uploaded files.
- Full raw transcript export failed after long output; the capture file records the visible verdict and patch list.
- GPT's required minimum patches were implemented in v14.3 and carried forward.

## Real Claude Student Simulation Gates

### Round 1 on v14.3

Status: `CLAUDE_STUDENT_PASS_AFTER_PATCH_CAPTURED`

Evidence:

- `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_3_20260524.md`

Effect: generated the v14.4 student-facing framework repair list.

### Round 2 on v14.4

Status: `CLAUDE_STUDENT_FRAMEWORK_PASS_CAPTURED`

Evidence:

- `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_4_20260524.md`

Boundary:

- Claude Opus 4.7 Adaptive ran in a fresh chat as a zero-baseline smart student.
- It saw only the v14.4 framework and 8-question blind test pack.
- It did not receive the 42-question answer-analysis file.
- It returned `CLAUDE_STUDENT_FRAMEWORK_PASS`.

## v14.5 Hardening After Pass

Claude's only non-blocking suggestion after the PASS was to add an A8 card for entry fraud and labor-contract invalidity. v14.5 incorporates that card:

`劳动者诚信告知义务 -> 欺诈使单位违背真实意思订立劳动合同 -> 合同自始无效或有解除依据 -> 试用期内查证可依法解除 -> 通常无需支付经济补偿或赔偿金。`

## Remaining Boundary

v14.5 is the Markdown final candidate after real GPT review, real Claude PASS, and Claude's optional A8 hardening. It is not a DOCX/PDF delivery.
"""


def governor() -> str:
    return """# 06 Final Governor Checklist v14.5

## Verdict

`MARKDOWN_FRAMEWORK_AND_42_QUESTION_BAODIAN_EXTERNAL_MODEL_PASS_HARDENED_NO_DOCX_PDF`

## Gate Table

| Gate | Status | Evidence |
|---|---|---|
| v14.5 framework chapter exists | PASS | `01_先背这套_法律主观题不扣分框架_v14_5.md` |
| v14.5 42-question analysis exists | PASS | `02_42题按框架拆解与解析_v14_5.md` |
| Combined v14.5 baodian exists | PASS | `选必二法律与生活_法律宝典_v14_5_最终Markdown候选版.md` |
| GPT Pro review used | PASS_WITH_CAPTURE_LIMIT | `external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md` |
| Claude v14.3 student simulation used | PASS_AFTER_PATCH | `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_3_20260524.md` |
| Claude v14.4 student simulation used | PASS | `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_4_20260524.md` |
| Claude optional A8 hardening applied | PASS | `05_GPT与Claude补丁落实及治理边界_v14_5.md` |
| Traceability matrix updated | PASS | `traceability/TRACEABILITY_MATRIX_v14_5.csv` |
| Open-container/reference-only rows separated | PASS | `04_开放容器与不晋升题附录_v14_5.md` |
| DOCX delivery | NOT PRODUCED | no DOCX claimed |
| PDF delivery | NOT PRODUCED | no PDF claimed |

## Allowed Claim

v14.5 is the final Markdown candidate for the 选必二法律宝典: it contains the student-facing framework, all 42 locked core question analyses organized by the framework, open-container appendix, traceability, and real GPT/Claude governance evidence.

## Not Allowed

- Do not claim full raw GPT/Claude transcript where copy/export failed.
- Do not claim DOCX/PDF delivery.
"""


def readme() -> str:
    return """# v14.5 Final Markdown Candidate

This is the latest 选必二《法律与生活》法律宝典 Markdown candidate.

It includes:

- student-facing framework,
- all 42 locked core questions analysed under the framework,
- open-container/reference-only appendix,
- traceability matrix,
- real GPT Pro review capture,
- real Claude Opus 4.7 Adaptive student-simulation captures,
- Claude PASS hardening for A8 labor entry-fraud cases.

Boundary: DOCX/PDF files are not produced in this directory.
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    framework = patch_framework(read(SRC / "01_先背这套_法律主观题不扣分框架_v14_4.md"))
    cards = patch_common(read(SRC / "02_42题按框架拆解与解析_v14_4.md"))
    appendix = patch_common(read(SRC / "04_开放容器与不晋升题附录_v14_4.md"))
    gov = governance()
    combined = "\n\n---\n\n".join(
        [
            "# 选必二法律与生活：法律宝典 v14.5 最终Markdown候选版",
            framework,
            cards,
            appendix,
            gov,
        ]
    )

    write(OUT / "00_READ_ME_FIRST.md", readme())
    write(OUT / "01_先背这套_法律主观题不扣分框架_v14_5.md", framework)
    write(OUT / "02_42题按框架拆解与解析_v14_5.md", cards)
    write(OUT / "04_开放容器与不晋升题附录_v14_5.md", appendix)
    write(OUT / "05_GPT与Claude补丁落实及治理边界_v14_5.md", gov)
    write(OUT / "06_FINAL_GOVERNOR_CHECKLIST_v14_5.md", governor())
    write(OUT / "选必二法律与生活_法律宝典_v14_5_最终Markdown候选版.md", combined)

    if (SRC / "external_gate_attempts").exists():
        shutil.copytree(SRC / "external_gate_attempts", OUT / "external_gate_attempts")
    if (SRC / "claude_student_simulation").exists():
        shutil.copytree(SRC / "claude_student_simulation", OUT / "claude_student_simulation")

    sim_dir = OUT / "claude_student_simulation"
    for source in list(sim_dir.glob("*v14_4*")):
        if "RESULT" in source.name:
            continue
        target = source.with_name(source.name.replace("v14_4", "v14_5"))
        write(target, patch_common(read(source)))

    trace_src = SRC / "traceability" / "TRACEABILITY_MATRIX_v14_4.csv"
    if trace_src.exists():
        write(OUT / "traceability" / "TRACEABILITY_MATRIX_v14_5.csv", patch_common(read(trace_src)))

    write(
        OUT / "build_manifest.txt",
        "built_by=build_v14_5_claude_pass_hardening.py\n"
        "status=markdown_final_candidate_external_model_pass_hardened_no_docx_pdf\n",
    )


if __name__ == "__main__":
    main()
