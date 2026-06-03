---
name: football-video-workflow
description: Build grounded football highlight or commentary videos from real match footage or user-provided clips. Use when the user asks for football or soccer match highlights, referee-decision compilations, sports commentary shorts, clip selection, edit decision lists, narration, captions, or MoneyPrinterTurbo-assisted video creation, especially when stock footage would be misleading.
---

# Football Video Workflow

Use this skill to turn football topics into controlled video projects. Treat "one theme directly makes a video" as a draft-only path. For real match highlights, require real footage, explicit user-provided clips, or a clearly stated stock-footage commentary format.

## Core Rule

Do not let generic stock clips impersonate real match footage. If the user wants a real highlight, first lock the source clips and event timestamps. If only stock media is available, frame the output as commentary or explainer video, not an actual match compilation.

Do not present AI-generated claims about referee decisions, goals, cards, VAR calls, dates, players, or matches as fact unless the claim is verified from user-provided material or a reliable source. When unsure, say what is unverified and keep it out of the final narration.

## Workflow

1. Classify the requested video.
   - Real highlight: needs local footage or user-approved source clips.
   - Commentary over football visuals: can use stock or generated visuals, but must not imply the visuals are the exact incident.
   - Research-only plan: produce source list, event ledger, script, and EDL without rendering.

2. Create a project folder.
   - Prefer `scripts/new_project.py` to create a standard folder under the current workspace or the user-selected output directory.
   - Store original videos in `assets/raw/`.
   - Store downloaded or user-approved reference clips in `assets/source_clips/`.
   - Store working plans in `planning/`.
   - Store finished renders in `exports/`.

3. Search and register usable materials.
   - Prefer `scripts/search_materials.py` for stock football/referee B-roll. It searches Pexels, downloads clips, validates non-empty files, and writes `planning/stock_materials.csv`.
   - Use stock materials only as generic visuals. Keep exact-match footage separate in `assets/raw/` or `assets/source_clips/verified_match/`.
   - Use web research for factual reference links and official explanations, but do not download copyrighted league broadcasts unless the user has rights or supplies the footage.
   - Save reference links and footage status in `planning/source_candidates.md`.

4. Build an event ledger before scripting.
   - One row per moment: match, date, team, event label, source file, start time, end time, evidence status, notes.
   - Mark each row as `verified`, `user-provided`, `commentary-only`, or `unverified`.
   - Remove or soften unverified claims before narration.

5. Build an edit decision list.
   - Use exact clip ranges rather than broad topic words.
   - Prefer 5-12 short cuts for a 30-60 second social video.
   - Include crop/aspect, subtitle text, voiceover line, sound cue, and confidence notes.

6. Decide the tool path.
   - Use FFmpeg directly for deterministic cuts, speed changes, crops, subtitles, and concat.
   - Use MoneyPrinterTurbo for narration, subtitles, and simple assembly only after source clips are locked.
   - For true highlights in MoneyPrinterTurbo, avoid auto Pexels stock search. Use local materials or custom assets.
   - If using the local MoneyPrinterTurbo on this Mac, the known project path is `/Users/wanglifei/Documents/Codex/2026-06-01/moneyprinterturbo-github/MoneyPrinterTurbo`; WebUI is usually `http://127.0.0.1:8501/` and API docs `http://127.0.0.1:8080/docs`. Re-check ports before claiming services are running.

7. Write narration last.
   - Match voiceover to visible clips.
   - Use short factual sentences.
   - Separate opinion from fact with phrases like "the controversy is..." or "fans argued that...".
   - For Chinese narration in the local MoneyPrinterTurbo setup, prefer Azure TTS V1 with a Chinese voice such as `zh-CN-XiaoxiaoNeural-Female` unless the user requests another voice.

8. Quality check before delivery.
   - Confirm the render opens and plays.
   - Confirm audio exists and is not silent.
   - Confirm subtitles do not cover the ball, score bug, or key action.
   - Confirm every factual claim in the narration appears in the event ledger or is marked as opinion.
   - Confirm no stock footage is presented as the real match incident.

## Resources

Read `references/workflow.md` when creating a new football video plan, building an event ledger, or deciding whether MoneyPrinterTurbo is appropriate.

Run `scripts/new_project.py` to create a clean project scaffold with CSV/Markdown templates.

Run `scripts/search_materials.py` to search and download stock football B-roll into an existing project. Use `--dry-run` first for broad queries, then run a capped download.
