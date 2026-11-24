# 1.1 Intro to AI Capabilities and Limitations

> Source: Anthropic Academy, "AI Capabilities and Limitations" (Coursera). Copyright 2026 Anthropic, CC BY-NC-SA 4.0. Lesson video transcribed below.

### What you'll learn

By the end of this lesson you'll be able to:

- Understand what this course covers and how it's structured
- Explain why this material is durable even as models and products keep changing
- See how the Capabilities & Limitations framework and the 4D Framework work together

### Welcome to the AI Capabilities & Limitations Course

The 4D Framework teaches YOU how to collaborate with AI. This course teaches you how AI is able to work with you. Together they're one system: human competencies on one side and machine properties on the other.

### A mental model of the machine

**Interactive diagram (text content):**

> Course
> roadmap
> What we mean by AI
> What is generative AI and how does it differ from other types of AI?
> How AI is trained
> How do pretraining and fine tuning give AI its character?
> Properties of AI
> What are next token prediction, knowledge, working memory, and steerability?
> Putting it all together
> What happens when properties collide in real life situations?
> Next steps
> How do you use this knowledge to use AI safely, effectively, and ethically?

<!-- video transcript start -->
### Lesson video transcript (~4 min)

_Machine transcription (faster-whisper small.en); may contain small errors._

[00:07] Hi there, my name is Kristen and I'm on the education team at Anthropic. Welcome to AI Capabilities and Limitations. If you've taken our AI Fluency Framework and Foundations course, you already know the four Ds, delegation, description, discernment, and diligence. Those are human competencies. They're what you do when you collaborate with AI. This course is the companion piece. It's about what the machine does when a human prompts it and why. We're going to help you build a working mental model of where AI outputs actually come from. Importantly, this course centers on how AI is created, so it'll remain useful and relevant even as AI models and products change. You can't delegate a task to AI without knowing where the model is strong and

[00:55] where it's weak. You can't discern the quality of an output from AI without some picture of how that output was produced and what to look out for. Everything you learn in this course is actionable through the four Ds. Understanding that AI is a prediction engine changes how you describe tasks to it. Understanding the context window changes how you delegate long tasks. The two frameworks fit together. Here's the roadmap for the course. First, we'll look at the two training stages that give an AI its character and the fingerprints each one leaves on the finished system, pre-training and fine-tuning. Pre-training builds a document completer while fine-tuning shapes AI into an assistant. Both stages matter for understanding why the model behaves the way it does.

[01:43] And then we'll cover four core properties of generative AI, next token prediction, knowledge, working memory, and steerability. Each property is a continuum. You'll learn to evaluate where your task falls along the continuum for each property, whether it's in the capability zone or drifting towards the edge. Finally, we'll look at how everything interconnects. Most real world failures with AI are two properties meeting. A hallucinated citation is next token prediction meeting a knowledge gap. Drift over a long conversation is working memory meeting steerability. When you can name the combination, you know why it's happening and what to do about it. Models will keep changing. Context windows grow.

[02:29] Hallucination rates drop. New features ship every month. The specifics shift constantly. But the shape of these properties stays useful. Next token prediction will still be next token prediction a year from now. The knowledge cutoff might move, but there will still be one. The context window might get bigger, but it'll still be an edge. What you're building here is a durable mental model, one that survives daily product updates and model releases. As with all courses, the person doing the work is doing the learning. To get the most out of this course, spend time doing the exercises. The exercises are where the learning happens. You've designed them so you're testing each property against your own work in a domain where you're the expert. That's deliberate.

[03:14] You need to explore situations where you can actually tell if something's off. So bring real tasks, run real prompts. When we cover working memory, load in your actual long documents. When we cover next token prediction, ask about your actual niche topics. The goal is a calibration you can feel, not a list of terms you memorize. All right, I'm glad you're on this learning journey with me and the rest of our team. Together, we'll demystify how AI works and how you can use it to augment your thinking and your work.
<!-- video transcript end -->

### Key takeaways

- The AI Fluency Framework (4Ds) describes human competencies. This course describes the machine properties those competencies respond to.
- Generative AI has four core properties: Next Token Prediction, knowledge, working memory, and steerability.
- This material is durable because the properties stay stable even as models improve. Boundaries shift but the properties remain the same.

### Exercise: Mapping Your Current AI Use

1. List 4–6 tasks you've actually used AI for in the last two weeks. Be specific: "drafted a client email explaining a project delay" tells you something. "Writing" doesn't.
2. For each task, note one line: did the output land on the first try, or did you need to rework it before it was usable?
3. Share your list with Claude (or any AI assistant) and ask: "For each of these tasks, what's one way this could go wrong if I'm not paying attention?" If the failure modes don't match your experience, push back.

### Lesson reflection

- Which of your listed tasks felt "safe" to hand to AI, and which felt risky? Can you articulate why yet?
- What's one AI behavior you've noticed (good or bad) that you couldn't explain at the time?

### What's next

Before the four properties, we need to draw a line around what "AI" means in this course: specifically generative AI and how it's different from other forms of AI.
