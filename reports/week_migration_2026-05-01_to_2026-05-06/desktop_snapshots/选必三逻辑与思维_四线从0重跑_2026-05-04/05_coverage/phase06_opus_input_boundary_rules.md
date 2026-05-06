# Phase06 Opus Input Boundary Rules

Status: `NO_ACTION_FOR_TEACHING_TEXT`

If a later GPT gate allows a locked Opus input packet, Opus must obey:

1. Opus can only rewrite locked entries explicitly provided in the packet.
2. Opus cannot add questions.
3. Opus cannot delete questions.
4. Opus cannot change answers.
5. Opus cannot change L3/L4 status.
6. Opus cannot single-mount cross rows.
7. Opus output must preserve `question_id` during internal draft review.
8. Opus final student-facing prose must not expose source locator, lane, Governor, Confucius, audit, or archive terms.

This file is a future boundary only. It does not authorize Opus prose now.
