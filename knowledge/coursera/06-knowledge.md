# 3.1 Knowledge

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Explain how an AI model's knowledge is formed during training and why it has a fixed cutoff
- Predict which topics sit in the capability zone (frequent, recent-in-training, consistent) versus the edge (rare, post-cutoff, niche, contested)
- Identify staleness, uneven coverage, inherited bias, and source amnesia as characteristic knowledge failures
- Recognize web search, retrieval/RAG, and tool use as the product features that address this limitation

### Understanding knowledge gaps in AI models

The model knows what it was exposed to during training, and only that. No real-time browsing by default, no lived experience, and a hard stop at the knowledge cutoff. The practical question isn't "does the AI know this?" but "how well-represented was this in what it read?"

### What the model read, and when it stopped reading

**Interactive diagram (text content):**

> Before you read
> You ask AI to explain a news event from last week. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.
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
### Lesson video transcript (~5 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Hi, my name is David, and I'm on the safety team here at Anthropik. Today I'm going to talk to you about what AI models actually know, and just as importantly, what they don't. We'll explore where AI's knowledge comes from, why it has sharp edges, and how you can predict which topics are going to be reliable for you, and which ones aren't. A model like Claude has been exposed to more data than any human could digest in many lifetimes. That makes it feel like it knows everything, but it doesn't. Generative AI models have predictable knowledge gaps. AI models learn by reading enormous quantities of text, mostly drawn from the internet, public data sets, and other written sources. Through billions of rounds of given everything so far, what comes next? The model builds internal representations of concepts, relationships, and facts. That's how it knows things.

[00:54] It's also the only way it knows things. The model doesn't have experiences, it doesn't browse the web in real time unless a product explicitly gives it a search tool. And critically, training ends on a specific date. That date's called the knowledge cutoff. Everything that happened after that moment simply isn't there. Let me show you why that matters in practice. I'm going to ask Claude two questions. First, explain how photosynthesis works. Watch the response. Detailed, accurate, confident. This is a topic that has appeared thousands of times in the training data, described consistently, and hasn't changed. Now a second question. Who's the current mayor of Toledo? The model might give me a name. It might be right. It might be the person who held that job two years ago. The model has no way to know the difference. Think of the model's knowledge as a continuum.

[01:39] On one end, the capability zone, mainstream science, popular programming languages, well-documented history, topics that showed up frequently, consistently, and before the cutoff. Here, the model is extraordinarily deep. On the other end, rare topics, post-cutoff events, niche domains, local knowledge, the further you drift towards this edge, the less you should trust the answer. The question to ask isn't, does the AI know this? It's, how well-represented was this in what it read? This training process produces some genuine strength. The model's general knowledge is extraordinarily broad. It's deeply competent in the domains that are well-represented in the training data. And it makes connections across fields, because concepts that appear together in text end up near each other in the model's internal representation. That's where embeddings are.

[02:25] Words and ideas mapped as points in a vast mathematical space where similar meetings cluster. Ask about a biology concept, and the model can pull in relevant chemistry and history and economics without being told to. But the same process creates characteristic limitations. Knowledge cutoff, anything after the training simply doesn't exist for the model. Staleness, information that was true at the time of training, may have changed. The model has no mechanism to know this. Uneven coverage, frequent topics are handled well. Rare topics are handled poorly. Minority languages, niche domains, recent developments all suffer. Inherited bias, the model's sense of what's normal or default reflects its training data's blind spots. That shows up in assumptions about what a doctor looks like, what a family looks like, or what counts as a professional.

[03:11] Source amnesia, the model usually can't tell you where a piece of knowledge came from. I read this somewhere isn't a citation. This is why modern AI products ship with features designed to work around these limits. Web search pulls current information at response time, routing around the cutoff. MCPs connect the model to documents it never trained on, like your company's wiki or a specialized database. Tools let the model call real-time calculators or databases instead of relying on absorbed patterns. Explicit cutoff disclosure just tells you when a training ended so you can know to double check. If you're using these features, you're extending the model's knowledge at runtime. If you're not, you're relying entirely on what it absorbed during training.

[03:58] Knowledge gaps are most likely to show up when the topic is time sensitive. Current events, recent research, who holds a position, what something costs. The domain is niche, local, or in a less represented language. The question post-dates the cutoff. You're relying on the model's sense of typical or normal, or web search is turned off. Here's how to protect yourself. Verify anything time sensitive. Assume the model may be out of date. Test before you trust in a new domain. Brilliance in one area doesn't transfer to the one next door. Watch for default assumptions that reflect training data rather than reality. When the tools exist, search, retrieval, use them. They're there specifically to patch these gaps. Understanding the knowledge property directly shapes two of the four AI fluency competencies.

[04:45] Delegation, before you hand a task to the model, ask yourself, is this a domain the model knows well, or one where you need to bring the knowledge yourself through context, documents, or search. Discernment, when you get an answer back, you now know which of these claims need independent verification. Anything in the model's weak zone, recent, rare, or local, warrants a second look. The model's knowledge is broad, deep, frozen, and imperfect all at once. Once you can see where the edges are, you stop being surprised by them.
<!-- video transcript end -->

### Key takeaways

- What generative AI knows comes entirely from training data and is frozen at the knowledge cutoff. Without tools, it has no access to any information after that date.
- Capability zone: topics that appeared frequently, recently (within training), and consistently in training data.
- Limitation zone: rare, post-cutoff, niche, local, or contested topics.
- Characteristic failures: staleness, uneven coverage, inherited bias in what counts as "default" or "normal," and inability to attribute where knowledge came from (source amnesia).
- Web search, retrieval (RAG/MCPs), and tool use exist specifically to patch these gaps by giving the model access to information it was never trained on.
- 4D connection: Knowledge unevenness is core to Delegation. Understanding where the model is well-stocked versus thin tells you when to hand off, when to supply context yourself, and when to go elsewhere.

### Exercise: The Outsider Test

For one task, write down two mainstream/stable topics, two niche/local/recent topics, and one "default assumption" outsiders to your field often get wrong. Then run three probes:

1. Probe 1: Coverage. Ask about one mainstream and one niche topic. Compare depth and accuracy, and whether the AI signals uncertainty differently or uses the same confident tone for both.
2. Probe 2: Staleness. Ask about something that changed recently in your field. Does the AI acknowledge the cutoff, present stale information as current, or decline?
3. Probe 3: Default assumptions. Ask a question that reveals whether the AI defaults to the outsider's view (e.g. describe the typical customer).

Then flag each task: can you lean on the model's knowledge, or do you need to bring the knowledge yourself via context, documents, or search? Stretch goal: re-run the staleness probe with web search enabled. This is retrieval in action.

### Lesson reflection

- Where in your work do you need to supply context rather than assume the model has it?
- Did the default-assumption probe surface anything surprising?

### What's next

Knowledge covers what the model absorbed during training. Working Memory covers what it's paying attention to right now: your prompt, your documents, your conversation. This property has the hardest edge of all four.
