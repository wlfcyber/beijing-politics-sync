# DEVELOPMENT_PLAN

## Phase Gates

1. Source manifest must exist before candidate extraction.
2. Codex candidate extraction and evidence atoms must exist before ClaudeCode merge audit.
3. Merged questions and merged rubric atoms must exist before reasoner packets.
4. Real GPT-5.5 Pro and real Claude Opus outputs must exist before codebook.
5. Cross-validation must exist before provisional codebook.
6. Codebook must exist before candidate framework.
7. Full question-by-question pressure test must exist before final framework.
8. Full question-by-question framework runs must exist before final baodian.

## Work Plan

- STEP_00_GATE: pass three-layer SOP and create run controls.
- STEP_01_SOURCE_MANIFEST: scan raw source roots, unpack archives if any, extract metadata/text where possible.
- STEP_02_CODEX_CANDIDATES: extract subjective law-question candidates only.
- STEP_03_CODEX_ATOMS: split material, ask, and rubric atoms.
- STEP_04_CLAUDECODE_HANDOFF: call Claude Code if available; otherwise save prompt and mark real_call_pending.
- STEP_05_MERGE_AUDIT: merge Codex and ClaudeCode evidence after B output exists.
- STEP_06_REASONER_PACKET: create unified packet for GPT and Claude.
- STEP_07_OPEN_OBSERVATION: call real GPT-5.5 Pro and Claude Opus; otherwise save prompts and block framework promotion.
- STEP_08_CROSS_VALIDATION: compare model observations.
- STEP_09_CODEBOOK: write provisional codebook.
- STEP_10_CANDIDATE_FRAMEWORKS: ask both models for codebook-bound candidate frameworks.
- STEP_11_FRAMEWORK_V1: synthesize and evidence-map framework v1.
- STEP_12_PRESSURE_TEST: run framework v1 on every included subjective question.
- STEP_13_FRAMEWORK_V2: revise only from evidence and pressure-test failures.
- STEP_14_FINAL_BAODIAN: produce final Markdown and convertible document.

## Local Execution Rule

Each phase writes artifacts first, then updates PROGRESS.md and governor_board.md.

