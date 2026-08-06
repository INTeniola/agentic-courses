# Day 5 Video Transcript: Multi-Agent Teams

[Open on instructor, facing camera]

Welcome back, and congratulations. You have made it to Day Five. Take a second to appreciate that, because the person who started this bootcamp on Monday could not do what you are about to do today.

Let me remind you of the journey. On Day One, you built your first agent. On Day Two, you gave it memory. On Day Three, you handed it tools, so it could search, calculate, and reach out into the real world. On Day Four, you gave it a knowledge base of your own documents. Today, we do the final thing. Today, we stop building one worker and start building a team.

[Show slide one: One agent versus three agents]

Here is the core idea, and it is simpler than it sounds. A single agent trying to do everything is like one person running an entire consulting firm alone. They research, they analyse, they write, they edit, they format the final report. They can do it, but quality drops as the workload grows. The context gets crowded. The instructions get confused.

So we do what every good organisation does. We divide the labour.

Today we are building a three-person team. A Manager, a Researcher, and a Writer. Each one has one job, one clear identity, and one clear standard of success. And when they work together, the output is dramatically better than anything a single agent produced this week.

[Show slide two: The three roles]

Let us meet them.

First, the Manager. The Manager does not do the research and does not write the report. The Manager receives the goal from the user, breaks that goal into tasks, decides who does what, and reviews the work that comes back. If the research is thin, the Manager sends it back. Think of the Manager as your project lead.

Second, the Researcher. The Researcher has one obsession: finding accurate, relevant, current information. This agent gets the search tools we built on Day Three and the document knowledge base we built on Day Four. The Researcher does not worry about beautiful writing. The Researcher worries about facts, sources, and completeness.

Third, the Writer. The Writer receives the research findings and turns them into something a human being actually wants to read. Clear structure, clean language, a strong opening, a useful conclusion. The Writer does not go looking for new information. The Writer shapes what already exists.

Notice the pattern. Narrow role, clear goal, specific tools. That is the whole philosophy of multi-agent design.

[Switch to screen recording: code editor]

Now let us build it together. On screen you can see we define each agent with three things. A role, which is the job title. A goal, which is the single outcome that agent is responsible for. And a backstory, which is the personality and expertise we want the model to adopt. Do not skip the backstory. It genuinely changes the quality of the output.

Next, we define the tasks. Task one, research the topic. Task two, write the report using the research. And here is the important line, right here. We tell task two that it depends on the output of task one. That dependency is the handoff. That is how the Researcher passes work to the Writer.

Finally, we assemble them into a crew and we set the process to sequential, which simply means one after the other, coordinated by our Manager.

[Show terminal running]

Let us run it. Watch the logs. You can see the Manager assigning the task. Now the Researcher is calling the search tool. It is gathering sources. And now, look, the Writer receives that research and begins drafting.

[Show final report output]

And there it is. A structured, sourced, readable report, produced by a team of agents you designed.

[Return to instructor on camera]

Three quick warnings before I let you go.

One, do not add too many agents. Beginners get excited and build teams of ten. Start with three. Complexity is a cost, not a feature.

Two, be specific. Vague goals produce vague output. Every agent should be able to answer clearly what success looks like.

Three, always define your final deliverable. Tell the system exactly what the last output should look like, or you will get a beautiful conversation and no report.

Your final assignment is this. Take the agent team we built today and point it at a topic in your own industry. Fintech, agriculture, education, health, whatever you care about. Generate a real report. Then share it in the community channel.

You started this week not knowing what an agent was. You are finishing it as someone who can design a team of them. That is a genuine skill, and the market is looking for it right now.

Well done. Go and build. I will see you at graduation.