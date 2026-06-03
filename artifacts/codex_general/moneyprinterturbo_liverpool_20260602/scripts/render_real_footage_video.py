from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
WORKSPACE_DIR = PROJECT_DIR.parents[1]
MPT_DIR = WORKSPACE_DIR / "MoneyPrinterTurbo"

sys.path.insert(0, str(MPT_DIR))

from imageio_ffmpeg import get_ffmpeg_exe  # noqa: E402
from moviepy.audio.io.AudioFileClip import AudioFileClip  # noqa: E402

from app.services import voice  # noqa: E402


SRC1 = PROJECT_DIR / "assets/source_clips/real_match/nbc_bournemouth_liverpool_gakpo_penalty_50-195_432p.mp4"
SRC2 = PROJECT_DIR / "assets/source_clips/real_match/nbc_bournemouth_liverpool_gakpo_penalty_195-240_432p.mp4"
AUDIO = PROJECT_DIR / "work/audio/gakpo_penalty_real_zh.mp3"
SUBS = PROJECT_DIR / "work/subtitles/liverpool_gakpo_penalty_real_v1.ass"
OUTPUT = PROJECT_DIR / "exports/liverpool_gakpo_penalty_real_footage_v1.mp4"
LOG = PROJECT_DIR / "work/render/ffmpeg_render_real_v1.log"
META = PROJECT_DIR / "work/audio/real_audio_meta.json"

NARRATION = (
    "这次直接看真实比赛画面。"
    "二零二五年二月一日，伯恩茅斯对利物浦。"
    "Gakpo 在禁区里和 Lewis Cook 接触后倒地，主裁 Darren England 指向点球点。"
    "VAR 随后检查犯规和越位，最终维持原判。"
    "英超官方解释是：Cook 的左腿接触，影响了 Gakpo 的动作，属于 careless contact。"
    "争议点在于：接触确实存在，但力度是不是足够？"
    "Gakpo 有没有主动寻找接触？"
    "所以这球不是一句黑哨能说清，它真正刺眼的是：规则解释成立，但球迷观感很不舒服。"
)

CAPTIONS = [
    ("这次直接看\n真实比赛画面", 3.0),
    ("2025年2月1日\n伯恩茅斯对利物浦", 4.0),
    ("Gakpo 在禁区里\n和 Lewis Cook 接触后倒地", 5.3),
    ("主裁 Darren England\n指向点球点", 4.1),
    ("VAR 随后检查\n犯规和越位", 4.0),
    ("最终维持原判", 2.5),
    ("英超官方解释：\nCook 的接触影响了动作", 5.1),
    ("这被认定为\ncareless contact", 3.3),
    ("争议点在于\n接触确实存在", 3.7),
    ("但力度是不是足够？", 3.0),
    ("Gakpo 有没有主动\n寻找接触？", 3.8),
    ("规则解释成立\n球迷观感很不舒服", 4.6),
]

TAGS = [
    (0, 8, "真实比赛画面"),
    (8, 17, "禁区接触"),
    (17, 25, "主裁判罚"),
    (25, 35, "VAR 检查"),
    (35, 999, "争议点"),
]


def ass_time(seconds: float) -> str:
    seconds = max(seconds, 0)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def esc_ass(text: str) -> str:
    return text.replace("\\", "\\\\").replace("\n", "\\N")


def ff_filter_path(path: Path) -> str:
    return str(path).replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")


def ensure_audio() -> float:
    AUDIO.parent.mkdir(parents=True, exist_ok=True)
    voice.tts(NARRATION, "zh-CN-XiaoxiaoNeural-Female", 1.08, str(AUDIO), voice_volume=1.0)
    with AudioFileClip(str(AUDIO)) as clip:
        duration = float(clip.duration)
    META.write_text(json.dumps({"duration": duration, "file": str(AUDIO)}, ensure_ascii=False, indent=2), encoding="utf-8")
    return duration


def write_subtitles(duration: float) -> None:
    SUBS.parent.mkdir(parents=True, exist_ok=True)
    total_weight = sum(weight for _, weight in CAPTIONS)
    scale = duration / total_weight
    events = []

    events.append(
        f"Dialogue: 1,{ass_time(0)},{ass_time(duration)},Small,,0,0,0,,"
        "真实比赛画面 | NBC Sports 公开集锦 | Premier League / PGMOL 解释"
    )
    events.append(
        f"Dialogue: 2,{ass_time(0)},{ass_time(min(4.2, duration))},Title,,0,0,0,,"
        "Gakpo 点球争议\\N官方解释 vs 球迷观感"
    )

    for start, end, text in TAGS:
        if start >= duration:
            continue
        events.append(
            f"Dialogue: 2,{ass_time(start)},{ass_time(min(end, duration))},Tag,,0,0,0,,{esc_ass(text)}"
        )

    cursor = 0.0
    for text, weight in CAPTIONS:
        end = min(cursor + weight * scale, duration)
        if end - cursor > 0.1:
            events.append(
                f"Dialogue: 3,{ass_time(cursor)},{ass_time(end)},Caption,,0,0,0,,{esc_ass(text)}"
            )
        cursor = end

    SUBS.write_text(
        """[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,STHeiti,46,&H00FFFFFF,&H000000FF,&H00000000,&HAA000000,1,0,0,0,100,100,0,0,1,4,1,2,50,50,90,1
Style: Title,STHeiti,58,&H00FFFFFF,&H000000FF,&H00000000,&HA0000000,1,0,0,0,100,100,0,0,1,5,1,5,36,36,34,1
Style: Small,STHeiti,24,&H00F0F0F0,&H000000FF,&H00000000,&H88000000,0,0,0,0,100,100,0,0,1,2,0,8,26,26,28,1
Style: Tag,STHeiti,30,&H0000E5FF,&H000000FF,&H00000000,&H88000000,1,0,0,0,100,100,0,0,1,3,0,8,32,32,82,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        + "\n".join(events)
        + "\n",
        encoding="utf-8",
    )


def segment_filter(idx: int, src_label: str, start: float, end: float) -> str:
    raw = f"raw{idx}"
    bg = f"bg{idx}"
    fg = f"fg{idx}"
    out = f"v{idx}"
    return (
        f"[{src_label}]trim=start={start}:end={end},setpts=PTS-STARTPTS[{raw}];"
        f"[{raw}]split=2[{raw}a][{raw}b];"
        f"[{raw}a]scale=720:1280:force_original_aspect_ratio=increase,"
        f"crop=720:1280,gblur=sigma=18,eq=brightness=-0.22:saturation=0.82[{bg}];"
        f"[{raw}b]scale=720:-1,setsar=1[{fg}];"
        f"[{bg}][{fg}]overlay=(W-w)/2:(H-h)/2,"
        f"drawbox=x=0:y=0:w=720:h=150:color=black@0.42:t=fill,"
        f"drawbox=x=0:y=1070:w=720:h=210:color=black@0.48:t=fill[{out}]"
    )


def render_video() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)

    segments = [
        ("s0", 5, 12),
        ("s1", 8, 14),
        ("s2", 96, 103),
        ("s3", 128, 136),
        ("t0", 5, 22),
    ]
    filters = ["[0:v]split=4[s0][s1][s2][s3]", "[1:v]split=1[t0]"]
    for idx, (label, start, end) in enumerate(segments):
        filters.append(segment_filter(idx, label, start, end))
    joined = "".join(f"[v{i}]" for i in range(len(segments)))
    filters.append(f"{joined}concat=n={len(segments)}:v=1:a=0[base]")
    filters.append(f"[base]subtitles='{ff_filter_path(SUBS)}'[vout]")

    ffmpeg = get_ffmpeg_exe()
    command = [
        ffmpeg,
        "-y",
        "-i",
        str(SRC1),
        "-i",
        str(SRC2),
        "-i",
        str(AUDIO),
        "-filter_complex",
        ";".join(filters),
        "-map",
        "[vout]",
        "-map",
        "2:a",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "20",
        "-c:a",
        "aac",
        "-b:a",
        "160k",
        "-movflags",
        "+faststart",
        "-shortest",
        str(OUTPUT),
    ]

    result = subprocess.run(command, cwd=str(WORKSPACE_DIR), text=True, capture_output=True)
    LOG.write_text(result.stdout + "\n" + result.stderr, encoding="utf-8")
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> None:
    if not SRC1.exists() or not SRC2.exists():
        raise SystemExit("Missing real match source clips.")
    duration = ensure_audio()
    write_subtitles(duration)
    render_video()
    print(json.dumps({"output": str(OUTPUT), "audio": str(AUDIO), "duration": duration}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
