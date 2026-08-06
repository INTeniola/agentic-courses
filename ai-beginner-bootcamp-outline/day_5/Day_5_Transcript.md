# Day 5 Video Transcript: Multi-Agent Teams

[Show slide 1: Day 5, Multi-Agent Teams]

Welcome back, and congratulations. You have made it to Day 5 of the AgenticLabs bootcamp. Take a second to appreciate that. On Monday, you were writing your first prompt. Today, you are going to build a team of AI agents that work together like colleagues. That is real progress, and you earned it.

[Show slide 2: One agent versus a team]

Let me start with the why. Up to now, your Second Brain has been a single agent. It searches your notes, it answers your questions, and honestly, it does a decent job. But you have probably noticed something. When you ask it to do too much at once, the quality drops. Ask it to research a topic, organise the findings, and write a polished report in one go, and the results feel rushed. Shallow research. Generic writing. Instructions quietly forgotten.

That is not a flaw in the model. It is a flaw in the design. We are asking one worker to do three different jobs at the same time.

Think about how a real consulting team operates. A manager breaks the project down and decides who does what. A researcher goes deep on the facts. A writer turns raw material into something a human actually wants to read. Nobody tries to be all three at once, because focus produces quality. That is exactly the principle we are applying today.

[Show slide 3: The three roles]

So let us meet our team. First, the Manager. This agent does not research and does not write. Its only job is to understand the request, break it into clear tasks, hand those tasks to the right specialist, and review what comes back. Think of it as the project lead.

Second, the Researcher. This agent has the tools. It can search your knowledge base, pull from your notes, and gather external sources if you have given it web access. Its output is not a beautiful report. Its output is accurate raw material, with sources attached.

Third, the Writer. This agent has no search tools at all, and that is deliberate. It receives the Researcher's findings and shapes them into a structured, readable report. Because it cannot go looking for new facts, it stays grounded in what the Researcher actually found. That single constraint does a lot of work in reducing hallucination.

[Switch to screen recording]

Let us build it. I am in our project folder from yesterday, and you can see the agent file we have been growing all week.

The first thing I am doing is defining each agent with three ingredients. A role, which is the job title. A goal, which is what success looks like for that agent. And a backstory, which gives the model context about how it should think. Notice how specific I am being here. I am not writing, you are a helpful assistant. I am writing, you are a research analyst who values primary sources and flags uncertainty rather than guessing. Specificity is what turns a generic model into a specialist.

Now watch the tools line. The Researcher gets the knowledge base tool. The Writer gets nothing. The Manager gets delegation ability. Who holds which tool is one of the most important design decisions you will make in a multi-agent system.

Next, the tasks. Each task needs a clear description and, just as importantly, an expected output. This is where beginners often lose time, so let me be direct. If you tell an agent to summarise the research, you will get something vague. If you tell it to produce five bullet points, each with a source and a confidence level, you get something you can actually use downstream. Be explicit about the shape of the output, because the next agent depends on it.

Finally, I am wiring them into a crew and setting the process to run in sequence. Research first, writing second, review last. Let us run it.

[Zoom in on the terminal output]

Look at what is happening in the logs. The Manager is assigning the task. The Researcher is calling your knowledge base and pulling real passages from your own notes. Now the handoff. The Writer picks up those findings and starts drafting. And there it is, a structured report with sections and citations, built by three agents that each did one thing well.

[Return to camera]

Your assignment for today is straightforward. Add a fourth agent to this crew. Maybe a Critic that reviews the report for weak claims, or an Editor that tightens the language. You have everything you need to do it.

One last thought. Today you stopped being someone who prompts AI and became someone who designs AI systems. That is a genuinely valuable skill, and it is yours now. Post your report in the community channel so we can all see what you built. I am proud of the work you have done this week. Let us finish strong.