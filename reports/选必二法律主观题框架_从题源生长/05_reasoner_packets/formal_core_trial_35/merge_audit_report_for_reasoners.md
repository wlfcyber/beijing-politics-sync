# Merge Audit Report

generated_at: 2026-05-19T10:40:00+08:00

## Verdict

CONDITIONAL_PASS.

The merged evidence layer is sufficient to build a first reasoner packet from a restricted formal subset, but it is not sufficient for final framework closure.

## Counts

- Codex A candidate count: 103
- ClaudeCode B candidate count: 74
- Merged canonical candidates: 74
- Codex-only retained after B rejection filter: 0
- ClaudeCode-only candidates: 5
- Codex false positives rejected by B: 34
- Module boundary disputes: 35
- Evidence-level disputes: 12
- Locator/OCR risks: 22

## Evidence Level Counts

- formal: 54
- missing: 17
- reference_only: 3

## Merge Status Counts

- keep: 36
- pending_evidence: 17
- pending_locator_check: 21

## Decisions

1. 双方一致或 B 独立保留的候选进入 merged 主表。
2. Codex 独有且被 B 判定误收的候选不进入 merged 主表，保存在 `claudecode_false_positive_candidates.csv`。
3. B 独有候选进入 `claudecode_only_cases.csv`，并保留在 merged 主表。
4. 证据等级冲突按 ClaudeCode 较保守等级处理。
5. module boundary 或 locator/OCR 风险题保留在 merged 主表，但标记 pending，不进入第一轮 reasoner formal subset。
6. evidence_level=missing 不进入归纳，只进入待补证据清单。
7. reference_only 可以进入弱观察背景，但本轮 reasoner packet 只采用 formal 且 locator 可靠题。
8. 2026 石景山期末按硬规则继续 blocked。

## Can Enter First Open Observation

Reasoner formal subset count: 35.

This subset is written to `05_reasoner_packets/*_for_reasoners.csv`.

## Still Forbidden

Do not output a framework yet. This merge audit only authorizes a first open-observation packet for real GPT-5.5 Pro and Claude Opus, not a codebook, candidate framework, final framework, or baodian.
