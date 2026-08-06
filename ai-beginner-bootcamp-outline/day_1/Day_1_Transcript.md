# Day 1 Video Transcript: Hire the Brain

[Open on instructor, centre frame, warm lighting]

Welcome to Day One of the AgenticLabs Second Brain Bootcamp. My name is your instructor, and over the next five days, you and I are going to build something that most people still believe is out of reach for a beginner. We are going to build an autonomous AI agent that remembers what you tell it, thinks through problems on your behalf, and takes action without you holding its hand every step of the way.

If you have never written a line of code in your life, you are still in the right room. Take a breath. I have taught this to founders, students, civil servants, and complete beginners, and by Friday you will have something working that you can show your friends. That is a promise.

[Show slide 1: Day 1 — Hire the Brain]

Today's topic is called Hire the Brain, and I chose that title very deliberately. Think about how a company works. When a business wants to get things done, it hires a person. That person has intelligence, but intelligence alone is not enough. The company also gives that person a job description, access to tools, and a way to report back on progress.

An AI agent works exactly the same way. Today, we are doing the hiring. We are choosing the brain that will power your Second Brain agent, and we are setting up the workspace where that brain will live.

[Show slide 2: What is an autonomous agent?]

So let us answer the first big question. What actually is an autonomous agent, and how is it different from a chatbot?

When you open a normal chatbot and ask a question, it gives you an answer. One question in, one answer out. It is a very smart conversation partner, but it is passive. It waits for you.

An agent is different. An agent is given a goal, not a question. You might say, find me the three most recent articles on solar energy in West Africa and summarise them into a briefing note. A chatbot would tell you it cannot browse the internet. An agent would go and do it. It would break that goal into steps, use the tools available to it, check its own work, and come back with a finished product.

The difference is not intelligence. The difference is autonomy.

[Show slide 3: The Think, Act, Observe loop]

Now, how does an agent actually pull that off? Every agent you will ever build, no matter how complex, runs on one simple cycle. We call it the Think, Act, Observe loop. Write those three words down, because everything else this week hangs on them.

Step one is Think. The agent looks at the goal you gave it and asks itself, what is the very next step I need to take? It reasons. It plans. It picks a direction.

Step two is Act. The agent uses a tool. That tool might be a web search, a calculator, a database, or a file on your computer. This is the moment the agent reaches out and touches the world.

Step three is Observe. The agent looks at what came back from that action. Did the search return useful results? Did the file open correctly? Was there an error?

And then the loop repeats. It thinks again, acts again, observes again, over and over, until the goal is complete. That is it. That is the entire secret. Every impressive agent demo you have ever seen online is just this loop, running fast.

[Switch to screen recording: Google AI Studio homepage]

Alright, let us get practical. Open your browser and go to Google AI Studio. Sign in with any Google account. You do not need a paid plan to follow this bootcamp, and you do not need a credit card.

[Highlight the Get API Key button]

On the left side of your screen, look for the option that says Get API Key. Click it, then select Create API Key. Google will generate a long string of characters for you. That string is the key to your agent's brain. Copy it, and paste it somewhere safe on your device, like a plain text file. Please do not share it publicly or post it in the community chat. Treat it like your bank PIN.

[Return to instructor on camera]

That single key is what connects the code we write to the intelligence that powers it. Tomorrow, on Day Two, we will write our first few lines of Python and watch your agent think out loud for the very first time.

Your homework tonight is simple. Get your API key created and saved. Then post in the community channel and tell us one task you want your Second Brain to take off your plate this week.

You have officially hired the brain. Tomorrow, we put it to work. I will see you on Day Two.