# 选必一哲学宝典式重建 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans if this plan is delegated. In this run Codex executes inline, with five-question review gates.

**Goal:** 重建一份类似“哲学宝典”的选必一《当代国际政治与经济》学生可用术语宝典。

**Architecture:** 旧版只作为错误样本和定位索引；新稿以原题、评分细则、阅卷报告和用户确认细则为证据源。每 5 道主观题形成一个批次，Codex 与 ClaudeCode 先分别生成独立初稿，再把源证据和双稿交 Claude 与 GPT 做外部诊断，最后由 Codex 回到源证据裁决。

**Tech Stack:** Markdown 控制文件、CSV 证据台账、缓存文本与原始 PDF/PPT/DOCX 源、后续 DOCX 交付与渲染检查。

---

## Hard Rules

- 不再以 5.4、5.9、V4 任何旧成品为底稿。
- 每个正文条目必须含：术语、完整设问、细则位置、来源、材料触发、答案句。
- 术语必须来自评分细则、评标、阅卷细则、阅卷总结或用户确认细则；普通参考答案不能冒充细则。
- 六大要素为主线：时代背景、理论、经济全球化、政治多极化、中国、联合国。
- 同类项先合并，再做表述积累；相似表述不得并列成多个伪术语。
- 每 5 题必须形成 Claude 审核包、GPT 审核包、Codex 裁决表。
- Claude/GPT 意见不得直接进正文，必须回到原题和细则裁决。
- 2026 石景山期末全模块排除，除非用户提供新可用评分细则。

## Phase Tasks

### Task 1: Build Run Skeleton

**Files:**
- `00_control/IMPLEMENTATION_PLAN.md`
- `00_control/ERROR_TAXONOMY.md`
- `00_control/SOURCE_LEDGER_BATCH_001.csv`
- `01_source_packets/BATCH_001_SOURCE_PACKET.md`
- `02_codex_batches/BATCH_001_CODEX_DRAFT.md`
- `02_claudecode_batches/BATCH_001_CLAUDECODE_DRAFT.md`
- `03_fusion/BATCH_001_DOUBLE_DRAFT_REVIEW_PACKET.md`
- `03_external_review/BATCH_001_CLAUDE_REVIEW_PACKET.md`
- `03_external_review/BATCH_001_GPT_REVIEW_PACKET.md`
- `04_adjudication/EXTERNAL_REVIEW_DECISION_LOG.csv`
- `05_governor/BATCH_001_SELF_AUDIT.md`

- [x] Create the run folder under the GitHub sync repo.
- [x] Freeze old versions as audit-only material.
- [x] Select first high-risk batch of 5 questions.

### Task 2: Batch 001 Evidence Lock

- [x] Record exact source paths and line/page evidence.
- [x] Separate question text from rubric text.
- [x] Mark boundary risks, especially mixed-book questions and reference-answer-only material.

### Task 3: Batch 001 Codex Draft

- [x] Draft entries under the six-bucket framework.
- [x] Preserve scoring wording in `术语`.
- [x] Write answer-sheet style `答案句`, not production notes.
- [x] Add boundary notes where a scoring source is mixed-module.

### Task 4: Batch 001 ClaudeCode Independent Draft

- [x] Create ClaudeCode production prompt.
- [x] Run ClaudeCode against source packet and rules, without using Codex draft.
- [x] Save independent ClaudeCode draft.
- [x] Create double-draft review packet.

### Task 5: Batch 001 External Review Gate

- [x] Produce Claude review packet.
- [x] Produce GPT review packet.
- [x] Run Claude double-draft review after ClaudeCode production draft.
- [x] Run GPT double-draft review after ClaudeCode production draft.
- [x] Record external comments in the decision log.
- [x] Codex adjudicates each comment with source evidence.

### Task 6: Batch 001 Governor Gate

- [x] Check every entry against the field contract.
- [x] Check no invented term entered the main table.
- [x] Check mixed-module and 必修二 terms are not falsely promoted.
- [x] Decide whether Batch 001 may enter the cumulative宝典 draft.

## First Batch

1. 2026 通州期末 Q20
2. 2026 朝阳期中 Q17
3. 2025 海淀期中 Q16(2)
4. 2025 海淀期中 Q21(2)
5. 2024 东城一模 Q16

2024 东城一模 Q20 is queued as Batch 002 Question 1 because it is also user-pinned but the first gate must stay exactly five questions.
