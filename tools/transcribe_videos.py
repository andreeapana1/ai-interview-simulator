"""Transcribe the Coursera lesson videos (downloaded separately) with faster-whisper
and insert each transcript into the matching knowledge/coursera/<name>.md file.

Usage:  python3 tools/transcribe_videos.py <folder with 01-intro.mp4, ...>
The video file name must start with the same 2-digit number as the lesson file.
"""
import sys
from pathlib import Path

from faster_whisper import WhisperModel

COURSERA = Path(__file__).resolve().parent.parent / "knowledge" / "coursera"
MARK_START = "<!-- video transcript start -->"
MARK_END = "<!-- video transcript end -->"


def load_audio(path, rate=16000):
    """Decode a video's audio track to 16 kHz mono float32 (what Whisper expects).
    Done here because faster-whisper's own decoder clashes with the installed PyAV version."""
    import av
    import numpy as np

    chunks = []
    with av.open(str(path)) as container:
        resampler = av.AudioResampler(format="s16", layout="mono", rate=rate)
        for frame in container.decode(audio=0):
            for out in resampler.resample(frame):
                chunks.append(out.to_ndarray().reshape(-1))
        for out in resampler.resample(None):
            chunks.append(out.to_ndarray().reshape(-1))
    return np.concatenate(chunks).astype(np.float32) / 32768.0


def paragraphs(segments, every=45):
    out, cur, start = [], [], None
    for s in segments:
        if start is None:
            start = s.start
        cur.append(s.text.strip())
        if s.end - start >= every:
            out.append((start, " ".join(cur)))
            cur, start = [], None
    if cur:
        out.append((start, " ".join(cur)))
    return "\n\n".join(f"[{int(t // 60):02d}:{int(t % 60):02d}] {txt}" for t, txt in out)


def main(video_dir):
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    for video in sorted(Path(video_dir).glob("*.mp4")):
        lesson = next(COURSERA.glob(video.name[:2] + "-*.md"))
        segments, info = model.transcribe(load_audio(video), vad_filter=True)
        segments = list(segments)
        text = paragraphs(segments)
        block = (
            f"{MARK_START}\n### Lesson video transcript (~{info.duration / 60:.0f} min)\n\n"
            "_Machine transcription (faster-whisper small.en); may contain small errors._\n\n"
            f"{text}\n{MARK_END}\n\n"
        )
        md = lesson.read_text(encoding="utf-8")
        if MARK_START in md:  # replace an older transcript
            pre, rest = md.split(MARK_START, 1)
            md = pre + rest.split(MARK_END, 1)[1].lstrip("\n")
        md = md.replace("### Key takeaways", block + "### Key takeaways", 1)
        md = md.replace("Lesson video not included (no captions available).", "Lesson video transcribed below.")
        lesson.write_text(md, encoding="utf-8")
        print(f"{video.name} -> {lesson.name}: {info.duration / 60:.1f} min, {len(text.split())} words", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
