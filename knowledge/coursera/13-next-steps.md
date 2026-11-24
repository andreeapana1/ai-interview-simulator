# 6.2 Next Steps

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Synthesize the four properties and training fingerprints into a working mental model
- Connect the Capabilities & Limitations framework to the 4D Framework as two halves of one system
- Identify one concrete change to make in your AI practice this week

### Applying the 4D framework to get better AI outputs

Fluent AI use isn't about memorizing every failure mode. It's about holding a small, clear model of the machine in your head, so that when something goes wrong you can recognize which kind of wrong it is and respond accordingly.

### A small model of the machine

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
### Lesson video transcript (~5 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Hi again, it's Kristen from the education team at Anthropic. When you started this series, you probably had some version of one question. Why does AI do that? But you're leaving with something better than a list of answers. You're leaving with a structure that lets you answer the next. Why does it do that yourself? Models change, features ship, edge cases surprise people, these properties remain. What you've built in this course is the ability to stop being surprised. Let's take a quick tour back through what you're taking with you. First, models are trained in two stages. Pre-training builds a document completer, fine-tuning layers and assistant on top. Every behavior you see, helpful or strange,

[00:54] traces back to one of those two fingerprints. Once models are created, they exhibit four properties, next token prediction, knowledge, working memory, and steerability. Each one is a continuum with a capability zone, a limitation zone, and product features that push the edge further out. The same mechanism is always running. The only thing that changes is where your task lands on the line. When something goes wrong, it's almost always two of these properties meeting. A fabricated citation is next token prediction, meeting a knowledge gap. Drift over a long conversation is working memory fading, while steerability takes new instructions too literally. That's how you diagnose and adjust. It's not what broke, but which two things collided. Now, here's what ties all of this together

[01:42] with the 4D framework you may already know. These two frameworks aren't separate things you have to juggle. The 4Ds are what you do, delegation, description, discernment, and diligence. The four properties we discussed in this course are what you're responding to when you do them. Understanding next token prediction makes you better at discernment because you know that fluency and accuracy are independent variables. Understanding working memory makes you better at description because you know context is leverage and you stop assuming the model remembers everything. Understanding steerability makes you better at delegation because you know where control is high and where it's less precise. The machine layer sharpens the human layer. It's not two different systems.

[02:28] It's just opposite sides of the same coin. Calibrated trust with AI gets talked about like it's an attitude, but it's actually a habit. It means that before you hand something to an AI, you run a quick internal check. Is this well-worn territory or sparse? Is this topic recent or stable? Is my context window comfortably inside the window? Are my instructions concrete or is there room between my words and my intent? And then you adjust. More verification where fabrication can concentrate. More context where the model can't guess what you mean. More checkpoints when reasoning chains run too long. You look for features that can help you extend the capabilities of the models.

[03:14] You don't trust the AI, but you don't distrust it either. You locate the task and you set your habits accordingly. That's the true essence of AI fluency. So where do you go from here? Practice on real work. The model in your head gets sharper the more you test it against actual output. Pay attention to where your predictions about AI behavior are right and where they're off. Revisit the 4D framework with fresh eyes. If you've already taken that course, the four properties give you a new lens on it. If you haven't, it's the natural next step. Keep testing the edges. The models get better. The context windows get bigger. Features close gaps that used to be open. The edges move and you find them by pushing on them.

[04:02] The specific numbers will change. The exact location of each edge will shift as models improve. But the shape of these properties hold. AI will keep being a predictor whose fluency may run ahead of its accuracy. It will keep having uneven knowledge with a cutoff. It will keep working inside a finite window. It will keep following your instructions despite a gap between words and intent. Those facts don't expire when the number version goes up. You've built a mental model that's durable on purpose. The target keeps moving and now you know how to track it.
<!-- video transcript end -->

### Key takeaways

- You now hold a working mental model: four properties as continuums, characteristic failures as property intersections.
- This framework and the 4D Framework (Delegation, Description, Discernment, Diligence) are two sides of one system. The properties explain what the 4D competencies are responding to.
- Calibrated trust means locating your task on each continuum and matching your verification and context habits to where it sits.
- Models will keep changing. The shape of these properties stays useful even as the exact boundaries shift.

### Exercise: Your Commitment

For each task on your Lesson 1 list, note where it lands on each property's continuum and which mitigations you might need. Then pick one task and one change you'll make this week (a verification step, a standing-context setup, a checkpoint, a goal-stated-not-just-format habit).

### Lesson reflection

- What's the single biggest shift in how you think about AI behavior from Lesson 1 to now?
- Which of the 4Ds feels most immediately sharpened by what you've learned here?

### What's next

The AI Fluency Framework & Foundations course goes deep on the human competencies. Keep testing edges: the properties stay stable, but where the lines sit will keep moving as models improve.
