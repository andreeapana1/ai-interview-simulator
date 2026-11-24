# AI Job Interview Simulator (project version)

A local interview simulator for an entry-level business position involving AI. It runs inside an AI coding agent (built and tested with Claude Code) using an `AGENTS.md` file and an agent skill (`SKILL.md`). The course materials in `knowledge/` are both its question bank and its answer key.

Built for Assignment 3, Case 5 "Simulation", in *AI in Accounting and Business* (SDU, MSc).

## How to use it

1. Open this folder as a project in Claude Code (desktop app, CLI or IDE extension).
2. Start a new chat and type **"Start an interview"**.
3. Answer each question in your own words. The interview takes about five minutes (six questions, easy → hard).
4. At the end you get feedback: a score table, strengths, knowledge gaps, incorrect answers with the correct version and its source, and what to review.
5. The full transcript is saved in `interviews/`.

Each interview picks a new random set of topics (`tools/pick_topics.py`).

## How it works

| File | Role |
| --- | --- |
| `AGENTS.md` | Project instructions: a request to start an interview launches the interview skill. (`CLAUDE.md` imports it, because Claude Code reads `CLAUDE.md`.) |
| `.claude/skills/ai-interview/SKILL.md` | The interview procedure: preparation, one question at a time, level progression L1 → L3, timing, no hints during the interview, grading against the sources, the feedback format, saving the transcript. |
| `knowledge/INDEX.md` | Topic map: 28 topics with must-know points, three question levels and the source files, plus a section guide to the Karpathy video. |
| `knowledge/transcripts/` | Transcripts of Karpathy's "Deep Dive into LLMs like ChatGPT" and the 24 IBM Technology videos from the course list. |
| `knowledge/coursera/` | The Anthropic Academy course "AI Capabilities and Limitations": lesson text, interactive-diagram text and lesson-video transcripts. |
| `tools/` | Scripts used to build the knowledge base (`fetch_transcripts.py`, `fill_diagrams.py`, `transcribe_videos.py`) and the topic picker. |
| `interviews/` | Saved interview transcripts. |

Design choices:
- **Grounded grading:** before judging an answer, the interviewer opens the topic's source file and checks the answer against it, so the feedback matches the course rather than the model's general knowledge. Every correction cites a file and, where possible, a `[mm:ss]` timestamp.
- **Exam-like:** no hints or corrections during the interview; at most one follow-up per question; honest verdicts (correct / partly correct / incorrect).
- **Progressive disclosure:** the skill is loaded only when an interview is requested, and the knowledge files are opened only for the topics being asked.

## Sources and licences

- Andrej Karpathy, *Deep Dive into LLMs like ChatGPT* (YouTube) and IBM Technology videos (YouTube): captions fetched with `youtube-transcript-api` for private study use. All rights remain with the creators.
- Anthropic Academy, *AI Capabilities and Limitations* (Coursera): © 2026 Anthropic, licensed CC BY-NC-SA 4.0. The lesson-video transcripts are machine transcriptions (faster-whisper, `small.en`) and may contain small errors.
