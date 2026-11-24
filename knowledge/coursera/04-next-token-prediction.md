# 2.1 Next Token Prediction

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Explain Next Token Prediction as the core mechanism of generative AI and why it produces both fluency and hallucination
- Locate tasks on the Next Token Prediction continuum (well-worn path vs. novel territory)
- Identify specificity (names, dates, citations, statistics) as the zone where fabrication concentrates
- Recognize product features (citations, uncertainty signaling, constrained generation, generator-verifier pattern) that are mitigations for this limitation

### How AI models use next token prediction

Generative AI is closer to a vastly sophisticated autocomplete than to a search engine. It writes answers word by word based on what tends to follow what. That single property gives you both the fluency and the hallucination.

### Autocomplete at scale

**Interactive diagram (text content):**

> Before you read
> You ask AI to summarize a long report. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.
> Next Token Prediction
> Knowledge
> Working Memory
> Steerability
> Capability Limitation
> Trust it
> Spot-check
> Check details
> Verify carefully
> High risk
> Your guess
> Typical
> What this enables
> Where it characteristically fails
> Product features that push the edge out
> Pick a stop, then lock in your guess. The lesson opens up once you do.
> Lock in my guess
> Check your intuition
> Lock in your guess above to compare against the typical placement.
> Customize
> Bar height
> Pictogram size
> Palette
> Sky → Clay Olive → Clay Cactus → Fig Slate → Clay

<!-- video transcript start -->
### Lesson video transcript (~4 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Hi, my name is David and I'm on the safety team here in anthropic today I'm here to talk to you about next token prediction Which is a core property that determines where AI answers actually come from We'll look at what's really happening when AI responds to you and why the same mechanism that produces fluent writing Can also produce fabricated facts and how to tell which zone your tasks lands in If you understand one thing about how generative AI works Let it be this the operation at the heart of these systems is prediction given everything that's been written so far Predict what comes next one fragment at a time Generative AI is generating an answer composing it word by word based on what tends to follow what it's closer to an extraordinarily sophisticated autocomplete than to a search engine and that distinction matters because a Citation that looks like a real citation can satisfy a pattern just as well as one point to a paper that actually exists

[00:55] Let me show you this in action. I'll ask Claude to summarize an argument in a well-known essay Notice how quickly it produces clean coherent prose This is a well-worn path. The model has encountered this task thousands of times Now watch what happens when I ask for something at the edge Let's say I ask it to list three research papers by a mid-level researcher in a niche subfield with publication years Same confident tone same fluent prose, but the path is thin here and the models generating what looks like a good answer Some of these may be real some may be fabrications You have to check the output The same generative process is always running when you're working with AI what changes is how well-worn the path is Tasks the model has seen in countless variations land in the capability zone

[01:44] Summarizing reformatting explaining common concepts drafting in a familiar style next token prediction shines here because the patterns are dense and consistent as You move towards the edge the patterns thin out novel territory obscure topics those drift right the model keeps generating fluently But the ground underneath gets shakier The strength and weakness are the same property broadly relevant concept fluency comes from next token prediction The hallucination also comes from next token prediction You experience one or the other depending on where your tasks fall in that line on the strength side We see fluent text in any register rapid synthesis across fields strong performance on anything resembling what the model has seen before and Coherent continuation of any thread you hand it on the failure side. We see hallucinations inconsistency and misplaced confidence

[02:33] Frontier labs have built product features to help here citations and source grounding lets you trace what's back versus what's generated Trained uncertainty signaling like when the model says I'm not sure about this helps the model flag its own shakiness constrained generation and skills narrow the space where fabrication can sneak in a Generator verifier agent loop ensures output meets checks from an outside source These features exist precisely because the underlying behavior is always generative next token prediction When working with AI outputs keep these in mind a confident tone does not signal accuracy smoothness and correctness are independent variables Specificity is where fabrication concentrates names dates statistics citations quotes URLs the more precise acclaim the more it warrants a check

[03:21] Treat outputs as drafts to verify particularly when stakes are high or the domains unfamiliar to you Ask where on the continuum your task sits well-worn paths are safer handoffs thin paths need more scrutiny Lean on product surfaces if your tool offers citations or source grounding use them The model can't reliably tell grounded from invented you have to do that part Understanding next token prediction sits at the heart of discernment in the 4d framework You can't evaluate an output well without understanding that it was generated or composed to fit a shape It also informs delegation tasks deep in the capability zone are safer handoffs Tasks near the edge deserve more of your attention on the back end with this knowledge at hand AI becomes predictable rather than surprising
<!-- video transcript end -->

### Key takeaways

- Next Token Prediction refers to the fact that generative AI writes answers word by word based on what tends to follow what.
- Capability zone: tasks that resemble patterns the model has seen many times (summarizing, reformatting, explaining common concepts).
- Limitation zone: novel or sparse territory, and anywhere the task requires distinguishing "true" from "sounds true."
- Fabrication concentrates in specificity: names, dates, statistics, citations, URLs, quotes. The more precise a claim, the more it warrants verification.
- Product features like citations, uncertainty signaling, constrained generation, and generator-verifier loops exist specifically to push this limitation further out.
- 4D connection: Next Token Prediction is the foundation of Discernment. Knowing the output was generated tells you exactly what kind of scrutiny to apply.

### Exercise: The Verification Test

Pick the task where you're most confident in your domain expertise and write down five specific, checkable facts (a job title, a publication date, a statistic, a product spec, a quote, a URL). Then run three probes:

1. Probe 1: The capability zone. Ask the AI to explain a well-known concept in your domain. Smooth, confident, and largely accurate.
2. Probe 2: Specificity under pressure. Ask for five checkable specifics (sources, an author, exact figures, a URL). Verify every one and score it out of five. If it fabricates, note how confident it sounded doing it.
3. Probe 3: Sampling in action. Run the same request in a fresh conversation and compare. The variation you see is Next Token Prediction's sampling at work.

Stretch goal: re-run Probe 2 with citations enabled (e.g. Research mode). Does having sources to check change the score?

### Lesson reflection

- Would you have caught fabrications in a domain you didn't know well?
- Which tasks sit mostly in the capability zone, and which push into specificity that needs verification?

### What's next

Next Token Prediction explains how the AI generates. Next: the Knowledge property. What does the model actually know, where does that knowledge come from, and where are the gaps?
