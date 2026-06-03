# Football Video Workflow Reference

## Intake Questions

Ask only what is needed to avoid making a fake-looking video.

- Is this a real highlight from actual match footage, or commentary using general football visuals?
- What platform and shape: Douyin/TikTok 9:16, Bilibili/YouTube 16:9, or square?
- Target length: 30 seconds, 60 seconds, or longer?
- Do we have local clips? If yes, where are they?
- Should the tone be neutral analysis, fan commentary, accusation/controversy, or funny edit?

## Folder Layout

```text
project-name/
  assets/
    raw/
    source_clips/
    music/
  planning/
    event_ledger.csv
    edit_decision_list.csv
    narration.md
    fact_check.md
  work/
    cuts/
    audio/
    subtitles/
  exports/
```

## Automated Material Search

Use `scripts/search_materials.py` whenever the user expects Codex to find素材 automatically.

Example:

```bash
python3 /Users/wanglifei/.codex/skills/football-video-workflow/scripts/search_materials.py \
  /path/to/project \
  --queries "soccer referee,football referee,football stadium crowd" \
  --limit 8 \
  --orientation portrait \
  --config /path/to/MoneyPrinterTurbo/config.toml
```

Rules:

- Run broad searches as `--dry-run` if the query quality is uncertain.
- Keep `--limit` small for first pass, usually 5-12 clips.
- Put exact match footage in a separate verified folder; do not mix it with stock footage.
- After download, read `planning/stock_materials.csv` and choose clips for the EDL.
- If the user asks for real match highlights, use stock search only for transitions, intro, crowd, referee cutaways, or commentary backgrounds.

## Event Ledger Columns

```csv
event_id,match,date,team_or_player,event_label,source_file,start_time,end_time,evidence_status,claim_for_script,notes
```

Use `evidence_status` values:

- `verified`: checked against the clip and/or reliable source.
- `user-provided`: user says this clip/event is the intended source.
- `commentary-only`: acceptable opinion or contextual remark, not a factual incident claim.
- `unverified`: keep out of final narration or phrase as uncertain.

## Edit Decision List Columns

```csv
clip_id,event_id,source_file,in_time,out_time,visual_action,crop,voiceover,subtitle,sfx_or_music,notes
```

Good EDL rows are specific:

- `in_time=00:01:12.400`
- `out_time=00:01:17.800`
- `visual_action=VAR line appears, then player reaction`
- `voiceover=This call became the center of the argument.`

Bad EDL rows are vague:

- `source_file=some football clip`
- `visual_action=controversial moment`
- `voiceover=Liverpool always gets calls`

## Tool Path Selection

Use local clips plus FFmpeg when the user wants actual match highlights.

Use MoneyPrinterTurbo when the task is a commentary short and needs quick narration, subtitles, and assembly. In that mode:

- Prefer local/custom materials for exact match footage.
- Use Pexels only for generic football background shots.
- Keep generated script factual and short.
- Do not let AI invent event details.

Use HyperFrames or Remotion-style rendering when the user wants charts, scoreboards, timelines, annotations, or graphic-heavy explainers.

## Minimum Delivery Pack

For a serious football video, deliver or keep these artifacts:

- `planning/event_ledger.csv`
- `planning/edit_decision_list.csv`
- `planning/narration.md`
- final rendered MP4 in `exports/`
- a short note listing unverified claims removed or softened
