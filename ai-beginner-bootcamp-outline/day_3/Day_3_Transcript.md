# Day 3 Video Transcript: Give it Memory

[Open on instructor, facing camera]

Welcome back to Day 3. Take a second and look at what you have already built. On Day 1 you stood up a working agent that could answer questions. On Day 2 you gave it a knowledge base, so it could pull real information out of your own notes and documents. That is genuinely impressive work for two days, and I want you to sit with that for a moment before we go further.

But if you have been testing your agent, you have probably noticed something frustrating.

[Show slide one, titled The Goldfish Problem]

You ask your agent, what did I write about project deadlines last week. It gives you a solid answer. Then you follow up with, can you summarize that in three bullet points. And it has no idea what you are talking about. Every single message starts from zero. Your agent has knowledge, but it has no continuity. We call this the goldfish problem, and today we fix it.

[Show slide two, titled Two Kinds of Memory]

Here is the key idea, and it is simpler than most people expect. Your agent needs two different kinds of memory, and they do different jobs.

The first is long term memory. That is what you built yesterday. Your documents, your notes, your knowledge base. It is stable, it is searchable, and it does not change much from minute to minute.

The second is short term memory, and that is today's work. Short term memory is the conversation itself. It is the running thread of what you just said, what the agent just replied, and what the two of you are currently working on together. In practice, we call this a session.

[Show slide three, titled What Is a Session]

A session is nothing more than a container with an identity. You give each conversation an ID, and every message that belongs to that conversation gets stored against it. The user says something, you save it. The agent replies, you save that too. Over time, that session becomes an ordered list of messages, and that list is the agent's sense of where it is in the conversation.

Now here is the part that surprises almost every beginner. Large language models do not actually remember anything between calls. Not one thing. The illusion of memory comes entirely from us. Every time we send a request, we resend the relevant conversation history along with the new message. The model reads it fresh, every single time, and responds as though it had been paying attention all along.

So memory, at the engineering level, is a retrieval and packaging job. You store the history, you fetch the right slice of it, and you include it in the next request. That is the whole trick.

[Switch to screen recording]

Let me show you this in code. I am starting with the agent we finished yesterday, and I am adding three things.

First, a session store. For today, a simple dictionary keyed by session ID is completely fine. We are not optimizing for scale yet, we are optimizing for understanding. Later you can swap this for Redis or a database, and nothing else in your design has to change.

Second, an append step. Before we call the model, we append the user's new message to the session. After we get a reply, we append that too. Notice how small this function is. Memory is not complicated code, it is disciplined code.

Third, and this is the part that matters most, we pass the history into the prompt. Watch the order here. System instructions first, then the conversation history, then any retrieved documents from our knowledge base, then the user's new question. That structure gives the model everything it needs to answer in context.

[Pause on the terminal output]

Now watch this. I ask about project deadlines. I get an answer. And now I say, summarize that in three bullets. And there it is. It knows exactly what I meant. Same model, same knowledge base, one new capability.

One caution before you go. Sessions grow, and every message you resend costs tokens and money. So we cap it. In the recording I keep the most recent ten exchanges and summarize anything older into a short paragraph that rides along at the top. Your agent stays coherent, and your bill stays reasonable.

[Return to instructor, facing camera]

Your assignment for today. Add session handling to your agent, hold a real six turn conversation with it, and confirm it can answer a follow up question that only makes sense in context. Then try breaking it. Start a second session and make sure the two do not leak into each other.

Take your time with this one. When you finish, your agent stops being a search box and starts being a collaborator.

Tomorrow, on Day 4, we give it tools, so it can actually do things in the world. I will see you there.