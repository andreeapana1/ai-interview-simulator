# 5.1 Steerability

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Explain why steerability works (fine-tuning taught the model instruction-following) and why it has limits (instructions are followed via pattern-matching, not understanding)
- Predict where control is tightest (short, concrete, verifiable instructions) versus loosest (long reasoning chains, abstract asks, native precision tasks)
- Identify reasoning drift, letter-over-spirit, and brittle arithmetic as characteristic steerability failures
- Recognize system prompts, code execution, visible reasoning, and structured outputs as product features addressing this limitation

### How steerability affects generative AI outputs

The model follows your instructions the same way it does everything else: by continuing a pattern. That makes it remarkably steerable. It also means there's always a gap between what you intended and what landed, and most of the interesting failures live in that gap.

### How much are you actually in control?

**Interactive diagram (text content):**

> Before you read
> You ask AI to write exactly 100 words, no more. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.
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

[00:07] Hi there, my name's Matt and I'm on the user research team at Enthropic. Today I'm here to talk to you about steerability in AI models. We'll look at why instructions work so well most of the time, why they sometimes land in a way that's technically correct but totally useless, and what you can do to keep the model pointed at what you actually want. If you've ever told an AI, be concise, and it dutifully trimmed the response, but cut the one part you cared about, you've already encountered this topic. Steerability is the model's ability to follow your directions. You say, respond with a table, and you get a table. You say, write this from a skeptic's point of view, and it shifts perspective. Specify a role, a tone, a format, a word limit, a set of rules, and

[00:52] the model applies them, often on the first try. This didn't happen automatically. Out of the box, a pre-trained model is a document completer with no concept of helping. Fine tuning is a second round of training, where the model learns from curated examples of good assistant behavior. That's where it picks up the habit of treating your text as a request, breaking tasks into steps, and following the rules you set. But steerability isn't the same thing as understanding. The model follows your instructions through the same pattern completion engine it uses for everything else. There's always some gap between the words you typed and the intent you had in mind. And many interesting AI limitations live in that gap. Let me show you what that gap looks like. I'll ask Claude, summarize this report in under 100 words and make it punchy.

[01:44] So that's 100 words. It's punchy. The instruction was followed to the letter. But the one qualified finding I actually needed made the summary less punchy, so it got cut. The model honored what I said and missed what I meant. It helps to picture your instructions on a spectrum. On one end, you've got directions that are short, concrete, and easy to check. Respond as a table, under 100 words. Use this exact schema. These sit firmly in the capability zone. The pattern is simple to match and you can verify it at a glance. Slide toward the other end and control starts to thin out. Long chains of reasoning where a small mistake in step two quietly carries through steps three, four, and five.

[02:29] Abstract directions like be insightful where the model has to guess what you mean. So the question to ask yourself isn't, did I write a good prompt? It's more like, how much room is there between what I typed and what I actually want? When you're in the capability zone, steerability gives you a lot. Type control over format and style, the ability to set a persona and have the model hold it across a whole conversation. Multi-step task execution where you lay out a process and it works through it, and iterative refinement where shorter, more formal, try the opposite angle, all land. Drift toward the edge and you'll see reasoning drift. Small errors compound over long chains and the model doesn't notice. Letter over spirit, like we just saw,

[03:15] the instruction is honored literally but uselessly. Instructions as an attack surface. Because the model follows instructions embedded in text, a malicious instruction hidden inside a document or webpage can be followed too. This is called prompt injection, more of a security concern than a daily one, but worth knowing exists. A few product features are built specifically to narrow these gaps. System prompts and custom instructions give you standing directions that don't dilute as the conversation gets longer. Visible reasoning lets you catch drift at step two rather than discovering it in the final answer. And structured output modes, JSON schemas, function calling, narrow the room for letter over spirit wandering.

[04:01] State the goal alongside the steps. I'm trying to persuade a skeptical audience, gives the model more to work with than a format spec alone. Break long chains with checkpoints. Ask for an intermediate result you can verify before the model keeps going. When an instruction lands literally but uselessly, restate the goal rather than the instruction. Repeating be concise louder doesn't fix a concision problem that was really an intent problem. Keep concrete verifiable instructions near the task. Short and checkable beats long and ambiguous. In the 4D framework, steerability is both the thing description exploits and the constraint it operates inside. Good description narrows the gap between your words and your intent. And it shapes delegation too.

[04:47] Tasks that need long reasoning chains or native numeric precision need either tighter human check points or different tool entirely. The model will follow you. Your job is to make sure following you and doing what you actually need point in the same direction.
<!-- video transcript end -->

### Key takeaways

- Steerability means the model follows instructions via Next Token Prediction.
- Capability zone: short, concrete, verifiable instructions. Format specs, length limits, explicit roles.
- Limitation zone: long chains of reasoning, abstract or ambiguous instructions, anything requiring native numerical or logical precision.
- Characteristic failures: reasoning drift (small errors compound) and letter-over-spirit (the instruction was honored but the intent wasn't).
- System prompts, code execution, visible reasoning, and structured output modes exist to keep your intent from diluting.
- When an instruction is followed literally but uselessly, restate the goal. Repeating the instruction with more force won't close the gap.
- 4D connection: Steerability is what makes Description powerful and what bounds it. Understanding the gap between words and intent changes how you write prompts and where you insert checkpoints.

### Exercise: The Goal Rewrite

Write the goal of a multi-step task in one sentence ("Convince my team this timeline is realistic" is a goal; "three bullet points" is a format). Then run three probes:

1. Probe 1: Tight control. Give a short, concrete, verifiable instruction ("exactly five bullet points"). Check whether it held precisely: the capability zone.
2. Probe 2: Reasoning drift. Ask for a version of the task with 4–5 dependent steps. Did a small early error carry through? Retry, asking the AI to stop and show step 2 before continuing. Compare running with a checkpoint versus without.
3. Probe 3: Letter vs. spirit. Give an instruction that can be satisfied literally but uselessly ("Make this shorter" when the real problem is structure). Then re-prompt with the goal stated alongside the instruction ("Make this shorter. My goal is to keep the executive's attention through the key finding on page two."). Compare.

### Lesson reflection

- How often have you been stating format but not goal? What changes when you include both?
- What's one recurring task where you'll add a mid-process checkpoint?

### What's next

You've met all four properties individually. Next: how they interact, because most real-world failures are two properties meeting.
