from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RUN = next((REPO / "reports").glob("*2026-05-16/11_strict_final_rebuild_2026-05-23"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_codex_summary(text: str) -> str:
    lines = []
    current_bucket = ""
    current_heading = ""
    current_term = ""
    current_source = ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## ") and "风险" not in line:
            current_bucket = line[3:]
        elif line.startswith("### "):
            current_heading = line[4:]
            current_term = ""
            current_source = ""
        elif line.startswith("【细则术语】"):
            current_term = line.replace("【细则术语】", "").strip()
        elif line.startswith("【来源】"):
            current_source = line.replace("【来源】", "").strip()
            if current_heading and current_term:
                lines.append(f"- {current_bucket} | {current_heading} | {current_term} | {current_source}")
    risk = text.split("## Codex 风险与降级意见", 1)[-1].strip() if "## Codex 风险与降级意见" in text else ""
    return "\n".join(lines) + "\n\n## Codex 风险与降级意见\n\n" + risk


def main() -> None:
    out_dir = RUN / "07_gpt_pro_fusion"
    out_dir.mkdir(parents=True, exist_ok=True)

    codex = read(RUN / "05_codex_drafts" / "CODEX_INDEPENDENT_THICK_DRAFT.md")
    claude = read(RUN / "06_claudecode_independent_opus47" / "CLAUDECODE_INDEPENDENT_THICK_DRAFT.md")
    claude_risk = read(RUN / "06_claudecode_independent_opus47" / "CLAUDECODE_INDEPENDENT_RISK_LOG.md")

    prompt = f"""# GPT Pro 主融合任务（压缩版）

上一轮完整包在网页端卡死，只输出“我”。现在请基于压缩输入完成主融合。请不要等待更多文件，不要解释流程，直接给结果。

## 任务

你是 GPT Pro 主融合线。下面给出：
1. Codex 独立厚稿的入表清单和风险意见。
2. ClaudeCode Opus 独立厚稿全文。
3. ClaudeCode 风险日志。

请按源证据和规则裁决，输出最终可合入学生宝典的版本。

## 硬规则

- 只收选必一《当代国际政治与经济》主观题采分点。
- 主表条目必须有评分细则/评标/阅卷/讲评或用户确认细则；普通参考答案只能降级。
- 题例层面绝不合并两题。每个条目只能对应一个来源题。
- “新型国际关系/合作共赢的新型国际关系/国际关系民主化/真正的多边主义/国际秩序公正合理”归“政治多极化”。
- “独立自主和平外交政策/和平共处五项原则/独立自主基本立场”归“中国”。
- 经济全球化内部按细则表述和卷面可替代性细分，不能把开放型世界经济、开放型经济、全球经济治理规则、贸易自由化、普惠包容全球化远距离合并。
- 证据不足就写 `NEEDS_EVIDENCE`，不要硬收。

## 输出格式

### A. 主融合裁决总表
用简洁表格列：来源题、Codex意见、ClaudeCode意见、GPT Pro裁决、归桶、理由。

### B. 可直接合入学生宝典的融合条目
按六桶组织。每条保留：
【细则术语】、【卷面使用】、【材料触发点】、【设问】、【为什么能想到】、【答案落点】、【细则位置】、【来源】

### C. 驳回与降级清单
列出驳回、降级、NEEDS_EVIDENCE。

### D. 合入注意事项
重点说明不能合并的点、归桶边界和经济全球化内部拆分。

---

# Codex 独立厚稿压缩清单

{extract_codex_summary(codex)}

---

# ClaudeCode Opus 独立厚稿全文

{claude}

---

# ClaudeCode 风险日志

{claude_risk}
"""
    out = out_dir / "GPT_PRO_FUSION_COMPACT_PROMPT.md"
    out.write_text(prompt, encoding="utf-8")
    print(out)
    print(len(prompt))


if __name__ == "__main__":
    main()
