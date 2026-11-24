"""Pick a random, balanced question plan for one interview from knowledge/INDEX.md.

Usage:  python3 tools/pick_topics.py
Prints 6 slots (2 x L1, 2 x L2, 2 x L3), each a different topic and spread over
different sections (A-E), plus 3 spare topics in case the candidate moves fast.
"""
import random
import re
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "knowledge" / "INDEX.md"
LEVELS = ["L1", "L1", "L2", "L2", "L3", "L3"]


def topics():
    out = []
    for m in re.finditer(r"^### ([A-E]\d+)\. (.+)$", INDEX.read_text(encoding="utf-8"), re.M):
        out.append((m.group(1), m.group(2).strip()))
    return out


def main():
    rng = random.SystemRandom()
    pool = topics()
    rng.shuffle(pool)
    chosen, sections = [], set()
    for code, name in pool:  # first pass: one topic per section
        if code[0] not in sections:
            chosen.append((code, name))
            sections.add(code[0])
    for item in pool:  # fill up to 9 (6 + 3 spares)
        if len(chosen) >= 9:
            break
        if item not in chosen:
            chosen.append(item)
    rng.shuffle(chosen)
    print("Question plan (ask in this order; levels go up):")
    for i, ((code, name), level) in enumerate(zip(chosen, LEVELS), 1):
        print(f"  Q{i}  {level}  {code} {name}")
    print("Spare topics:", "; ".join(f"{c} {n}" for c, n in chosen[6:9]))


if __name__ == "__main__":
    main()
