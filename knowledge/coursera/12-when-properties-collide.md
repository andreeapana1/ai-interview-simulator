# 6.1 When Properties Collide

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Recognize that most AI failures involve two or more properties interacting
- Diagnose common failure patterns (hallucinated citations, long-conversation drift, confidently wrong math, agreeable bad premises) by identifying which properties are at play
- Apply a targeted fix based on which property is the limiting factor

### Diagnosing AI failures

The four properties don't operate in isolation. Most real failures are two of them intersecting. Once you can name which two, you know which fix to reach for.

### Two properties meeting: diagnosing what went wrong

**Interactive diagram (text content):**

> When Properties Collide
> Most real-world AI failures are two properties meeting at the same time.
> Next Token Prediction
> Generates what sounds right
> Knowledge
> Knows what it was trained on
> Working Memory
> Attends to what's nearby
> Steerability
> Follows the loudest instruction
> drag two properties near each other to see what happens when they collide

<!-- video transcript start -->
### Lesson video transcript (~3 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Over the last few lessons, we've covered four properties that shape how AI systems behave. Next token prediction, knowledge, working memory, and steerability. Now you have four lenses, but they don't exist in isolation. They're interconnected. Most real world AI surprises aren't single property failures, they're two properties, meaning at the same time. And when you can name which two, the fix becomes obvious. You asked Claude about a niche topic and it gave you a paper title, author names, sounds great. Then you go to look it up and it doesn't exist. This is next token prediction meeting knowledge. Next token prediction is doing what it always does, generating what a plausible answer looks like. A good citation has a title on the right cadence,

[00:54] a journal that sounds real, names that fit the field. Meanwhile, there's a knowledge gap underneath and the model doesn't know the gap is there. It can't tell the difference between what it knows and what it's generating. When you observe this, verify specifics independently or better use a tool with source grounding so the model is retrieving real documents rather than generating citation shaped text. You set up careful constraints at the start of a long conversation. 20 messages later, Claude is ignoring half of them. This is working memory meeting steerability. Your early context has faded, either pushed out of the window or just receiving less attention than what you said recently. And because steerability works by following whatever instructions are most salient right now, your later messages are quietly overwriting the earlier ones.

[01:42] Resupply critical context or if the conversation has gotten unwieldy, start a fresh one and put the essentials upfront. Even before starting your conversation with AI, ask which properties am I looking at with the task I'm trying to accomplish? That question comes first because the diagnosis determines the fix. A knowledge problem and a working memory problem can produce outputs that look similar on the surface but they need completely different responses. If you jump straight to how do I fix my prompt, you're guessing. If you name the properties first, you're operating strategically. This diagnostic step is discernment in action. Naming the property level failure is exactly what turns vague dissatisfaction into a targeted iteration.

[02:29] You move from that wasn't quite right to I need to reground this in a source or I need to invite pushback. And it feeds back into delegation. If you keep seeing the same compound failure on the same kind of task, that signal, it tells you which task types to restructure, which to break into smaller pieces, which to keep for yourself. The patterns you diagnose today shape how you delegate tomorrow.
<!-- video transcript end -->

### Key takeaways

- Real-world failures are usually two properties interacting, not one.
- Diagnostic pairs to recognize:
  - Next Token Prediction + Knowledge (hallucinated specifics)
  - Working Memory + Steerability (long-conversation drift)
- Naming the properties at play points you straight to the fix: verify specifics, re-supply context, offload to code execution, or invite pushback.
- This diagnostic move is Discernment applied. You evaluate better when you know what kind of wrong you're looking at.

### Exercise: The Failure Diagnosis

Identify two or three times an AI output genuinely disappointed or surprised you. For each:

1. Ask an AI: "Based on the four properties (Next Token Prediction, Knowledge, Working Memory, Steerability), which ones were likely at play here, and why?"
2. Evaluate its diagnosis. If you disagree, push back (remember the sycophancy fingerprint: the AI may agree with your framing too readily).
3. Ask: "Given that diagnosis, what's the most targeted fix?" and test it on a similar task.

Then, for the tasks on your list that gave you the most trouble, name which two properties were colliding.

### Lesson reflection

- Did naming the property pair change what fix you'd reach for?
- Which property pairing will you encounter most often in your day-to-day work?

### What's next

The final lesson consolidates the model, connects it back to the 4D Framework as a complete system, and points to where to go deeper.
