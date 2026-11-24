"""Download the English captions of the course videos into knowledge/transcripts/.

Usage:  python3 tools/fetch_transcripts.py        (run from the interview-project folder)
Skips videos that already have a file, so it can be re-run safely.
"""
import re
import sys
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

OUT = Path(__file__).resolve().parent.parent / "knowledge" / "transcripts"

# (number, concept, title, video id) - order follows the case description
VIDEOS = [
    (0, "Foundations (Karpathy)", "Deep Dive into LLMs like ChatGPT - Andrej Karpathy", "7xTGNNLPyMI"),
    (1, "How LLMs work", "How Large Language Models Work", "5sLYAQS9sWQ"),
    (2, "AI, machine learning and generative AI", "AI, Machine Learning, Deep Learning and Generative AI Explained", "qYNweeDHiyU"),
    (3, "Transformers", "What are Transformers?", "ZXiruGOCn9s"),
    (4, "Context windows", "What is a Context Window? Unlocking LLM Secrets", "-QVoIxEpFkM"),
    (5, "Hallucinations", "Why Large Language Models Hallucinate", "cfqtFvWOfg0"),
    (6, "Probabilistic versus deterministic outcomes", "AI Agents vs Business Rules: Which Should Make Decisions?", "i1ZmNUbRGD4"),
    (7, "Embeddings", "What are Word Embeddings?", "wgfSDrqYMJ4"),
    (8, "Vector databases", "What is a Vector Database?", "t9IDoenf-lo"),
    (9, "Retrieval-augmented generation (RAG)", "What is Retrieval-Augmented Generation?", "T-D1OfcDW1M"),
    (10, "Prompt versus context engineering", "Context Engineering vs. Prompt Engineering", "vD0E3EUb8-8"),
    (11, "Tool calling", "What is Tool Calling? Connecting LLMs to Your Data", "h8gMhXYAv1k"),
    (12, "MCP and APIs", "MCP vs API: Simplifying AI Agent Integration with External Data", "7j1t3UZA1TY"),
    (13, "AI agents", "What are AI Agents?", "F8NKVhkZZWI"),
    (14, "Business workflows", "Building AI Agents for Real-World Problems & Workflows", "4Vg2aVtrX8k"),
    (15, "Agent skills", "What AI Agent Skills Are and How They Work", "Lg-meK5IU8Q"),
    (16, "Memory", "The Four Types of Memory Every AI Agent Needs", "BacJ6sEhqMo"),
    (17, "Reasoning models", "What Are Large Reasoning Models?", "enLbj0igyx4"),
    (18, "Complete AI systems", "What Is an AI Stack?", "RRKwmeyIc24"),
    (19, "Prompt injection", "What Is a Prompt Injection Attack?", "jrHRe9lSqqA"),
    (20, "Benchmarks", "What are Large Language Model Benchmarks?", "kDY4TodQwbg"),
    (21, "Evaluating AI outputs", "LLM as a Judge: Scaling AI Evaluation Strategies", "trfUBIDeI1Y"),
    (22, "Explainability", "What is Explainable AI?", "jFHPEQi55Ko"),
    (23, "Synthetic data", "What is Synthetic Data?", "HIusawrGBN4"),
    (24, "Selecting business applications", "Select the right AI use case for your business", "C1ecR-sIE1A"),
]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:50]


def to_paragraphs(snippets, every=60):
    """Join caption lines into paragraphs, one per ~minute, each with a [mm:ss] mark."""
    paras, current, start = [], [], 0.0
    for s in snippets:
        if not current:
            start = s.start
        current.append(s.text.replace("\n", " ").strip())
        if s.start - start >= every:
            paras.append((start, " ".join(current)))
            current = []
    if current:
        paras.append((start, " ".join(current)))
    return "\n\n".join(f"[{int(t // 60):02d}:{int(t % 60):02d}] {txt}" for t, txt in paras)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    api = YouTubeTranscriptApi()
    failed = []
    for num, concept, title, vid in VIDEOS:
        path = OUT / f"{num:02d}-{slug(concept)}.md"
        if path.exists():
            print(f"skip  {path.name} (exists)")
            continue
        try:
            fetched = api.fetch(vid, languages=["en", "en-US", "en-GB"])
        except Exception as e:  # noqa: BLE001 - report and continue
            print(f"FAIL  {num:02d} {title}: {type(e).__name__}")
            failed.append(num)
            continue
        snippets = list(fetched)
        minutes = (snippets[-1].start + snippets[-1].duration) / 60 if snippets else 0
        header = (
            f"# {title}\n\n"
            f"- Concept: {concept}\n"
            f"- Source: https://www.youtube.com/watch?v={vid}\n"
            f"- Length: ~{minutes:.0f} min\n"
            f"- Captions: {'auto-generated' if fetched.is_generated else 'uploaded'} ({fetched.language_code})\n\n"
            "## Transcript\n\n"
        )
        path.write_text(header + to_paragraphs(snippets) + "\n", encoding="utf-8")
        print(f"ok    {path.name}  ~{minutes:.0f} min, {len(snippets)} lines")
        time.sleep(1.5)  # be gentle with YouTube
    if failed:
        print("\nFailed:", failed)
        sys.exit(1)


if __name__ == "__main__":
    main()
