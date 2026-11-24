# 1.2 What We Mean by AI

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Distinguish generative AI from the classification and prediction AI you already encounter daily
- Understand that generative AI's properties exist on a continuum from capability to limitation
- Preview the four core properties you'll explore in depth: Next Token Prediction, knowledge, working memory, and steerability

### What we mean by generative AI

Most AI in the world (spam filters, recommendations, fraud detection) isn't generative. This course is about the kind that is: transformer-based text models that produce new content one token at a time.

### Building a mental model of the machine

**Interactive diagram (text content):**

> AI Capabilities & Limitations Framework
> Four properties that shape what AI can and can't do for you. Each sits on a spectrum — the further right, the more you should verify and compensate.
> Capability
> Limitation
> Next Token Prediction
> Where do AI answers come from?
> Well-worn paths: summarize, reformat, explain common conceptsNovel territory, sparse patterns, "true vs. sounds true"
> Knowledge
> What does AI actually know?
> Frequent, recent-in-training, consistent: mainstream topics, popular languagesRare, post-cutoff, niche, local, or contested topics
> Working Memory
> What is the AI paying attention to right now?
> Material fits comfortably, session is current, you supply relevant contextVery long docs/conversations, expecting cross-session continuity (the cliff)
> Steerability
> How much am I in control?
> Short, concrete, verifiable instructions ("respond as a table," "under 100 words")Long reasoning chains, abstract asks, native precision

<!-- video transcript start -->
### Lesson video transcript (~4 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Before we go anywhere, let's be clear about what we mean by AI, because it's actually a broad term that means many different things. The recommendation engine picking your next video, the spam filter in your inbox, the fraud model flagging a suspicious charge on your card, the system routing your customer service call. All of that is AI. None of it, however, is generative. These systems sort, rank, classify, and predict. They're enormously useful, and they're running in the background of your life constantly. They're also not what this series is about. What's changed recently is the rise of generative AI. These are systems that produce new content rather than categorizing existing content.

[00:54] Text, images, code, audio, video. Generative AI is created through two stages. First, it's trained on massive amounts of data to learn patterns. That's pre-training. Then it's refined to be broadly safe, ethical, and helpful. That's fine-tuning. You'll learn more about these in the next lesson. Generative AI at its core is a prediction system. AI isn't uniformly capable or uniformly unreliable. It's strong and weak along specific, predictable axes. And most of the time, the strength and weakness come from the same underlying property of the machine. An AI can write compellingly because it's a prediction engine. It also hallucinates because it's a prediction engine. On one end, a capability zone.

[01:41] On the other, a limitation zone. The mechanism itself is always operating the same way. What varies is where your specific task lands on that line. The skill you're building in this series is learning to feel out where those edges are. Let's do a quick overview of the four properties of generative AI you'll learn in this course. Next, token prediction. Where do the answers actually come from? Unless you've enabled or directed it to use an external source, the model isn't looking things up. It's writing what comes next based on the content it's been trained on, one fragment at a time. Knowledge. What does the model actually know? Its knowledge is broad but uneven, frozen at a training cutoff, and shaped by whatever was in the data it learned from.

[02:29] Working memory. What is the model paying attention to right now? Just like humans, models don't have unlimited memories. What's in the context window is what's available to the AI. Steerability. How much are you in control? These systems are remarkably directable, but there can be a gap between what you intended and what actually landed. We'll deep dive into each of these properties and how knowing about them can empower you to make good decisions when using AI. The goal here isn't to make you distrust AI. It's also not to make you fully delegate all your tasks. It's calibrated trust, neither granting it nor withholding it wholesale. By the end of the course, you'll be able to ask, where does my task sit on the continuum for each property of generative AI?

[03:15] Is this well trodden territory, or am I out near an edge? What are the stakes if I'm wrong? With this model, the behavior of generative AI starts feeling predictable, and that puts you in control.
<!-- video transcript end -->

### Key takeaways

- Generative AI produces new content rather than classifying existing content.
- AI isn't uniformly capable or uniformly unreliable. It's strong and weak along four predictable axes: Next Token Prediction, Knowledge, Working Memory, and Steerability.
- Each property is a continuum. The same mechanism gives you both the capability and the limitation.
- Calibrated trust means locating your task on the continuum, not granting or withholding trust wholesale.

### Exercise: Generative or Not?

1. List five AI-powered features you've interacted with this week (autocomplete, photo tagging, spam filtering, chatbot answers, translation, product recommendations, voice assistants).
2. For each one, decide: is it producing new content, or is it sorting, ranking, and classifying existing content?
3. Ask an AI to check your calls and explain any distinction you got wrong in one sentence.
4. Tag each task on your Lesson 1 list with the most relevant property question:
   - Where do the answers come from? (Next Token Prediction)
   - What does it know? (Knowledge)
   - What's it paying attention to? (Working Memory)
   - How much am I in control? (Steerability)

### Lesson reflection

- Did the generative/classification distinction change how you think about any tool you use?
- Did any task feel like it could belong under more than one property?

### What's next

One lesson on how an AI system ends up with a personality at all: why it's polite, helpful, honest, why it sometimes agrees too easily, why it declines certain things. That shaping process leaves fingerprints on everything that follows.
