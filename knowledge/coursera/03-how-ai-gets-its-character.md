# 1.3 How AI Gets Its Character

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Explain the two-stage training process for generative AI (pretraining and fine-tuning) in plain language
- Recognize the behavioral fingerprints each stage leaves: sycophancy, verbosity, over-caution, loose confidence calibration
- Apply this understanding to interpret behaviors you see in your own AI interactions

### How AI gets its character

An AI's politeness, helpfulness, and caution aren't emergent magic. They're trained in, layer by layer, and each training stage leaves specific, predictable fingerprints on how the system interacts with you.

### Pretraining, fine-tuning, and the fingerprints they leave

**Interactive diagram (text content):**

> How AI Gets Its Character
> Two training stages turn raw prediction into the helpful assistant you interact with — and each stage leaves fingerprints on its behavior.
> Stage 1
> Pretraining
> The model reads vast amounts of text and learns one thing: predict what comes next. It becomes a powerful document completer — but has no concept of helping you.
> Stage 2
> Fine-tuning
> Human preferences shape the document completer into an assistant — one that treats your input as a request, answers helpfully, and declines harmful asks.
> Help me improve this paragraph.
> Of course! Here are three specific suggestions to strengthen your argument and tighten the prose…
> I think my strategy is bulletproof.
> I appreciate the confidence! That said, I see two risks worth stress-testing before you commit…
> How do I pick a lock?
> I can’t help with that. If you’re locked out, I’d suggest contacting a licensed locksmith in your area.
> Helpful
> Honest
> Harmless

<!-- video transcript start -->
### Lesson video transcript (~4 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Hi there, my name is Maggie and I lead the education team at Anthropic. Today I'm here to talk to you about how AI assistants end up with a disposition. We'll look at the two training stages that turn raw prediction into something useful, the fingerprints those stages leave behind, and how knowing those fingerprints help you get better results. Why does an AI try to be helpful in the first place? Why is it polite? Why does it refuse certain things? Knowing that an AI predicts the next word doesn't really answer any of that. Helpfulness is built deliberately, in layers, and each layer influences your experiences with AI each day. Modern AI assistants are built in two stages. Stage 1 is pre-training. The model sees enormous amounts of data and learns one thing.

[00:56] Given everything so far, guess what comes next? That's it, repeated billions of times. Stage 2 is fine-tuning. The document completer from stage 1 gets trained again, this time on curated examples of helpful behavior and reward signals shaped by human preferences. This is the layer that turns the AI model into an assistant. Imagine you could talk to a model that had only been through stage 1. No fine-tuning at all. You type, what is the capital of France? A raw pre-trained model doesn't answer your question. It continues your document. Maybe it outputs Paris. What's the capital of Germany? Berlin. What's the capital of Spain? And so on, because it's seen that pattern in quizzes. Maybe it writes a paragraph from a geography textbook.

[01:44] Maybe it generates more questions. It has no concept of you, no concept of helping. It's purely continuing a document in whatever direction seems statistically likely. The assistant behavior you actually experience with AI tools today is a trained overlay on top of that. Fine-tuning is what makes generative AI systems usable and useful. But because it relies on human judgments about what good looks like, the texture of those judgments shows up in these models' personality. Often these personality traits are what make generative AI so effective. But there can be a shadow side to AI's helpfulness. Four shadow areas are, one, sycophancy. When people prefer agreeable responses, the model learns to validate readily and back down under light pushback,

[02:32] even when it was right the first time. Two, verbosity. When thoroughness scores better during training, the model defaults to longer answers, even when brevity could serve you better for a specific situation. Three, overcaution. When safety training leans conservative, the model can hedge heavily or refuse requests that are actually safe. And four, loose confidence calibration. The model stated confidence is only loosely tied to its actual liability. Confidence is genuinely hard to train, so it's particularly important to be vigilant here. These aren't bugs in one particular model. They're things that show up in all AI models. However, the quality and type of fine tuning done on a model directly shapes how these things manifest, and it will likely be different from model to model.

[03:17] At Anthropic, we train Claude to be broadly safe, ethical, and helpful. You can even read Claude's entire constitution to see how we train Claude and how we intentionally shape Claude's personality. Why does this matter to you? Understanding how AI is made and why it behaves the way it does puts you in control when it comes to AI. If your AI assistant caves the moment you push back, that's sycophancy, and you should factor that in when assessing responses. If you're getting essays when you want bullets, that's the verbosity default kicking in. If you're getting heavy caveats on a harmless question, that's overcaution. We'll address what to do about this in the upcoming lessons. The assistant you talked to wasn't born helpful. That behavior was built layer by layer

[04:02] and sometimes the seams show. Learning to spot these seams is part of using AI well.
<!-- video transcript end -->

### Key takeaways

- Pretraining produces a document completer by predicting "what comes next" across vast amounts of data. After this stage, it has no concept of helping you.
- Fine-tuning layers assistant behavior on top: treating your input as a request, answering rather than rambling, declining harmful asks.
- Fine-tuning uses human judgments about good responses, and those judgments leave fingerprints: a pull toward sycophancy, a default toward verbosity, occasional over-caution, and loose calibration between stated confidence and actual reliability.

### Exercise: Fingerprints on Your Own Work

Pick one task you have run through AI before and know what a good output looks like. Run it three times with slight variations:

1. Run 1: Straight. Prompt the task as you normally would. Save the output.
2. Run 2: Sycophancy test. Preface the same task with a wrong assumption (e.g. "I think this strategy is bulletproof."). Does the AI validate your framing or push back? Then try again with "I want you to genuinely disagree with me if you think I'm wrong." Compare.
3. Run 3: Verbosity test. Ask a question with a one-sentence answer, note the length, then re-ask with "Answer in one sentence." The gap is the verbosity default at work.
4. Optional: Caution test. Ask something at the edge of what should be fine (a medication interaction, a legal nuance). Is the hedging proportionate to the actual risk, or reflexive?

### Lesson reflection

- Where in your own work is sycophancy most likely to cost you? (Anywhere you're hoping for honest feedback.)
- Where is verbosity most likely to cost you? (Anywhere you need concision under time pressure.)

### What's next

The four properties themselves, beginning with Next Token Prediction: where do AI answers actually come from?
