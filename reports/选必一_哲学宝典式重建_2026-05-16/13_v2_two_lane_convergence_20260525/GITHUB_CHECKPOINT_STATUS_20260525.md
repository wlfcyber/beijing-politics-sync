# GitHub checkpoint status - 2026-05-25

## Status

This directory is a staged V2 convergence checkpoint, not a final V2 closure claim.

Closed in this checkpoint:

- Current final handbook SHA was audited: `9963553832C57091832BC446326DE802FFD459B0FE1897C3247398EA02D7648A`.
- Current-SHA coverage audit was generated against the 104-row P0 candidate/adjudication universe.
- Coverage audit result: 104 candidates audited, 136 core sections, 362 expected examples, 362 actual examples, 0 frequency mismatches, 0 unresolved rows after current scan plus adjudication.
- GPT Pro was run as the V2 main fusion editor and returned `V2_STRICT_ACCEPTED`.
- GPT Pro found no must-fix patch and accepted the wording that the artifact may be registered as a Codex + ClaudeCode Opus double-thick-draft, GPT Pro main-fusion, Claude Opus second-review, Codex evidence-check final candidate, subject to the stated coverage limit.

Closed after the checkpoint:

- Claude Opus 4.7 Adaptive V2 second review was rerun in a fresh Claude chat after the checkpoint push.
- Result file: `CLAUDE_OPUS47_V2_SECOND_REVIEW_RESULT_20260525.md`.
- Claude returned `STRICT_V2_ACCEPTED`.
- Claude found no must-fix patch.
- Claude accepted the GPT Pro main-fusion role and accepted the coverage limitation wording.

Still open for the larger final-goal upgrade:

- This V2 second-review closure proves the current SHA within the 104-row P0 candidate/adjudication universe.
- It still does not prove a fresh recrawl of every Desktop source file across all 2024-2026 materials.

## Cause of the apparent regression

The earlier afternoon state had already closed the weaker final-quality external review. The stricter V2 workflow requires GPT Pro to act as the main fusion editor after the Codex and ClaudeCode Opus production lanes, then requires a fresh Claude Opus 4.7 Adaptive second review. The missing evidence was the strict V2 chain, not the existence of a readable final handbook.

## Next action after checkpoint

Run the next P1 hardening task: full-source recrawl / all-source inventory audit against every 2024-2026 Desktop source, then compare that source universe with the 104-row P0 candidate/adjudication universe and current final SHA.
