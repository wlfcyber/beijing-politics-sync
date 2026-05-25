# GitHub checkpoint status - 2026-05-25

## Status

This directory is a staged V2 convergence checkpoint, not a final V2 closure claim.

Closed in this checkpoint:

- Current final handbook SHA was audited: `9963553832C57091832BC446326DE802FFD459B0FE1897C3247398EA02D7648A`.
- Current-SHA coverage audit was generated against the 104-row P0 candidate/adjudication universe.
- Coverage audit result: 104 candidates audited, 136 core sections, 362 expected examples, 362 actual examples, 0 frequency mismatches, 0 unresolved rows after current scan plus adjudication.
- GPT Pro was run as the V2 main fusion editor and returned `V2_STRICT_ACCEPTED`.
- GPT Pro found no must-fix patch and accepted the wording that the artifact may be registered as a Codex + ClaudeCode Opus double-thick-draft, GPT Pro main-fusion, Claude Opus second-review, Codex evidence-check final candidate, subject to the stated coverage limit.

Still open:

- Claude Opus 4.7 Adaptive V2 second review has not returned a fresh V2 verdict in this run.
- The old Claude review chat accepted the message and attachments but returned network/response-environment errors.
- A fresh Claude page was opened and the model selector displayed `Opus 4.7 Adaptive`, but automated file submission hit a file-chooser timeout during the checkpoint push window.

## Cause of the apparent regression

The earlier afternoon state had already closed the weaker final-quality external review. The stricter V2 workflow requires GPT Pro to act as the main fusion editor after the Codex and ClaudeCode Opus production lanes, then requires a fresh Claude Opus 4.7 Adaptive second review. The missing evidence was the strict V2 chain, not the existence of a readable final handbook.

## Next action after checkpoint

Resume Claude Opus 4.7 Adaptive second review from a fresh Claude chat, capture the returned verdict into `CLAUDE_OPUS47_V2_SECOND_REVIEW_RESULT_20260525.md`, then run the final Codex evidence check and push the closure update.
