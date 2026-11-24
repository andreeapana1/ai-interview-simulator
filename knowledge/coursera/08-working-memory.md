# 4.1 Working Memory

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Explain the context window as a fixed-size container and what that implies for long documents, long conversations, and cross-session memory
- Recognize the "cliff" nature of this property compared to the gradual degradation of others
- Apply context-as-leverage strategies: front-loading important material, chunking long work, re-supplying critical context
- Recognize memory, compaction, projects/workspaces, and larger windows as product features addressing this limitation

### How the context window affects generative AI outputs

Everything the AI is paying attention to lives inside a fixed-size workspace called the context window. It can attend to what's in there. It can't attend to anything outside it. That constraint is hard-edged in a way the other properties aren't: things work until they don't.

### The context window: AI's working memory

**Interactive diagram (text content):**

> Before you read
> You ask AI to review a 50-page contract. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.
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
### Lesson video transcript (~6 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Hi there. My name's Matt, and I'm on the user research team at Enthropic. Today, I'm here to talk to you about the context window, which is how AI models manage what they're paying attention to right now. We'll look at what actually fits inside that window, what happens when it fills up or empties out, and how to structure your work so you stay on the good side of those limits. It's a lot like how working memory functions in humans. When you're working with AI, everything sits inside one fixed-sized workspace called the context window. Your instructions, Claude's prior responses, the documents you uploaded, the back and forth conversation. All of it lives in one finite container, and the model can only attend to what's inside.

[00:53] Importantly, the context window has a hard size limit. Once a conversation or a set of documents exceeds what the window can hold, something falls off. Usually it's the oldest material, and usually it happens silently. The model doesn't stop and announce that it dropped your first three messages. It just keeps going with whatever's left. By default, the window empties between sessions. When you close a chat and open a new one tomorrow, you're starting from zero. Yesterday's conversation is gone unless a product feature, like memory or a Claude.md file, has deliberately carried something forward. Like the other core properties of AI systems, working memory runs as a continuum. When your material fits comfortably in the window and you're working inside the current session,

[01:39] you're in the capability zone. The model is working with your documents, your constraints, your context. As documents get longer, as the conversation runs on, as you start expecting the model to remember things from last week, you slide toward the limitation zone. Unlike the other three properties, though, this one has a cliff. Next token prediction degrades gradually. Knowledge gets thinner gradually, but working memory tends to work right up until it doesn't. You won't always get a warning. And while you're in the capability zone, context is genuine leverage. Watch what happens when I upload a short style guide and ask Claude to draft something. No retraining, no setup. The model adapts to my material immediately inside this one session.

[02:26] So why is the window fixed at all? Because the model processes your entire context as a single block every time it generates a response. It's reading all of it, start to finish, to decide what to write next. There's a ceiling on how much it can hold and still produce a coherent reply. And even inside that ceiling, attention isn't perfectly uniform. Research on long context behavior has found a lost in the middle effect. Material buried deep in the middle of a very long input tends to carry less weight than material at the beginning or the end. What does this mean in practice? You can have rapid in session adaptation. Give a glossary, a voice sample, a set of constraints, and it applies them on the spot.

[03:12] You get precision through specificity. The more relevant context you supply, the more tailored the output. But when the context window runs out, your experience degrades. AI won't remember things from the beginning of the conversation or things from the middle of your exchange might get fuzzy. Products layer features on top of the raw window to soften these edges. Memory saves selected facts across sessions so you're not starting from zero every time. Compaction or summarization condenses your conversation history to free up room when a conversation runs long. Projects and workspaces keep standing documents reliably in context without re-uploading. Skills keep instructions minimal until a specific task actually needs them.

[03:57] Multi-agent workflows allow for multiple agents to have different specialties in their own context windows, expanding the total amount of context the workflow can have. Larger context windows push the cliff further out. Here are some signs you're approaching the edge of the context window. A very long conversation where quality has started to slip. A very long document where details from the middle aren't showing up in responses and expecting the model to recall something from a prior session without a memory feature enabled. Here are some techniques to stay on the good side of the cliff. Lead with what matters. For long documents, put the most important material near the top rather than burying it on page 12. Chunk long work into passes.

[04:43] Process a big document in sections rather than one giant upload. Use product features that save your context. Use things like projects or skills that save your context for common areas you want to work in. If quality degrades over a long conversation, start fresh. That slippage is often a context limit rather than a capability limit. A new chat with a short summary of where you were can outperform pushing through. Working memory is the mechanism that makes description work. Everything you describe to an AI, your instructions, your constraints, your examples, has to live inside this window to have any effect. Understanding the window's size, its edges, and its reset behavior is what tells you how to structure a prompt, when to restate critical context,

[05:30] and what's actually worth uploading versus what you can leave out.
<!-- video transcript end -->

### Key takeaways

- Working Memory is the fact that the AI model has a fixed context window that it can attend to.
- Capability zone: your material fits comfortably, the session is current, you're supplying relevant context.
- Limitation zone: very long documents or conversations, expecting continuity across sessions, burying critical info in the middle of long input.
- This property has a cliff rather than a gradient. Silent truncation is the failure mode, and you won't always be warned.
- The model doesn't learn from your corrections. It only responds to what's currently in context.
- Memory features, compaction, projects, larger windows, and multi-agent workflows all exist to push this cliff further out.
- 4D connection: Working Memory is what Description acts on. Knowing how the window works tells you how to structure context, when to front-load, and when to start fresh.

### Exercise: The Before-and-After

Context is leverage: the same task, with the right context supplied, can go from a mediocre first draft to something genuinely useful. Pick a task that benefits from context only you hold (a style guide, a past example, constraints) and write two or three lines on what "good" looks like. Then run three probes:

1. Probe 1: Cold start vs. context. Run the bare request, then in a fresh conversation the same task with your context supplied upfront. Measure the gap against your "good" definition.
2. Probe 2: Lost in the middle. Bury one important instruction in the middle of a long document and ask a question that depends on it. Then move it to the very top and ask again. Compare.
3. Probe 3: The blank slate. Teach or correct the AI on something, then open a brand-new conversation that assumes it remembers. Watch it start from zero.

Then note which tasks need standing context (a project, saved instructions, uploaded reference docs) and which work fine cold. Stretch goal: set up memory or a project with your context and compare effort and quality.

### Lesson reflection

- How much did front-loading context change output quality?
- What's one piece of standing context you'll set up to stop re-explaining yourself?

### What's next

The final property: Steerability. How much are you actually in control when you give instructions, and where does that control break down?
