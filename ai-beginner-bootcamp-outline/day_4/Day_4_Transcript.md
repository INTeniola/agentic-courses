# Day 4 Video Transcript: Quality Control

[Open on instructor, centre frame]

Welcome back to Day Four of the AgenticLabs Bootcamp. Take a moment and look at what you have already built. On Day One you understood what an agent really is. On Day Two you gave it a brain and a personality. On Day Three you handed it tools and memory, and it started doing real work for you. That is genuinely impressive, and you should feel good about it.

But today we do something that separates hobby projects from professional systems. Today we talk about quality control.

[Show slide 1: Day Four – Quality Control]

Here is the honest truth about AI agents. A working agent is easy. A trustworthy agent is hard. Anyone can get a model to respond. The real skill is getting it to respond correctly, consistently, and safely, even when nobody is watching. That is what today is about, and by the end of this session your Universal Knowledge Worker will be far more reliable than it was this morning.

Let us start with a dial you have probably heard of but may not fully understand. Temperature.

[Show slide 2: The Temperature Dial]

Think of temperature as a creativity dial on your model. It usually runs from zero to one, and sometimes higher. When you set temperature close to zero, the model becomes focused and predictable. Ask it the same question ten times and you will get almost the same answer ten times. When you push temperature higher, toward zero point eight or one, the model becomes more adventurous. It takes more risks with word choice, it explores unusual ideas, and its answers vary each time.

Now here is the part beginners often get wrong. Higher temperature is not better, and lower temperature is not safer in every case. It depends entirely on the job.

[Switch to screen recording: temperature comparison in the notebook]

Watch this. I am asking our agent to summarise a financial report at temperature zero point one. Notice the output. Clean, factual, tightly anchored to the source document. Now the exact same prompt at temperature zero point nine. See the difference? More colourful language, more interpretation, and if you look closely, a claim that is not actually in the document. That is the trade-off in one screen.

So here is your practical rule. For extraction, summarisation, data handling, and anything involving numbers or compliance, keep temperature low. For brainstorming, drafting marketing copy, or generating ideas, raise it. Your Universal Knowledge Worker does both kinds of jobs, which means you may want different temperature settings for different tools inside the same agent. We will implement exactly that in today's lab.

[Show slide 3: Guardrails]

Next, guardrails. A guardrail is simply a rule that constrains what your agent is allowed to do or say. Think of the barriers on the Third Mainland Bridge. They do not slow the traffic down. They stop cars from going into the lagoon.

We will build three types today. First, input guardrails, which check the user's request before it ever reaches the model. If someone asks your finance assistant for medical advice, you catch it at the door. Second, output guardrails, which inspect the agent's answer before the user sees it. Here we check for hallucinated figures, missing citations, or leaked private data. Third, scope guardrails, which live in your system prompt and clearly define what the agent must refuse.

[Switch to screen recording: adding a validation function]

Notice that this guardrail is just a small function. It is not magic and it is not complicated. It reads the output, checks it against a rule, and either approves it or sends it back for a retry. That is the entire concept. Simple code, enormous impact on reliability.

[Show slide 4: Evaluation – How Do You Know It Works?]

Finally, evaluation. And this is the discipline that will make you stand out professionally.

Right now, most people test their agents by vibes. They type a question, read the answer, and think, yes, that looks fine. That is not engineering. That is hoping.

Instead, we build a small evaluation set. Twenty test questions with known correct answers. Then we score our agent on three things. Accuracy, meaning did it get the facts right. Groundedness, meaning did it stick to the source material instead of inventing. And format compliance, meaning did it follow the structure we asked for.

Run that set before and after every change you make. Suddenly you are not guessing anymore. You have evidence.

[Return to instructor, centre frame]

So today's mission is clear. Tune your temperature per task, wrap your agent in guardrails, and build your first evaluation set.

Take your time with the lab. This is the day your project becomes something you can confidently put in front of a client or an employer.

I will see you in Day Five, where we deploy. Let us get to work.