# AI Job Interview Simulator

This project is a local interview simulator. It prepares a business student for a job interview / oral exam about AI for an entry-level business position. The questions and the answer key come only from the course materials in `knowledge/`.

## Starting an interview

When the user asks to **start an interview** (or "interview me", "mock interview", "practise", "quiz me", "start the oral exam", or similar), run the interview by following the skill in
**`.claude/skills/ai-interview/SKILL.md`**. Read that file completely and follow its steps exactly, from preparation to saving the transcript.

Do not start an interview on your own. For other requests (questions about the materials, editing files), help normally.

## Project layout

| Path | What it is |
| --- | --- |
| `knowledge/INDEX.md` | Topic map: 28 topics in sections A–E plus a Karpathy section guide (F), question levels (L1 basic → L3 applied), must-know points and the source file for each topic |
| `knowledge/transcripts/` | Transcripts of the course videos: `00` Karpathy "Deep Dive into LLMs", `01`–`24` IBM Technology videos (timestamps `[mm:ss]`) |
| `knowledge/coursera/` | Anthropic Academy course "AI Capabilities and Limitations" (lesson text, video transcripts, interactive diagrams; CC BY-NC-SA 4.0) |
| `.claude/skills/ai-interview/SKILL.md` | The interview procedure (questions, timing, feedback format) |
| `tools/pick_topics.py` | Picks a random, balanced set of interview topics |
| `tools/fetch_transcripts.py`, `tools/transcribe_videos.py`, `tools/fill_diagrams.py` | Scripts used to build the knowledge base |
| `interviews/` | Saved interview transcripts |

## Rules

- Treat `knowledge/` as the single source of truth. When grading or explaining, check the source file and cite it. Do not invent facts, numbers or quotes.
- Never change files in `knowledge/` during an interview.
- Language: English.
