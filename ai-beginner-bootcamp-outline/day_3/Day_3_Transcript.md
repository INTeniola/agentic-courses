# Day 3 Video Transcript: Give it Memory

[Open on instructor, centered, warm lighting]

Welcome back to Day Three of the Universal Knowledge Worker Bootcamp. Take a moment to appreciate where you are right now. On Day One, you built an agent that could think. On Day Two, you gave it tools, so it could actually go out and do things in the world. Today, we fix the one thing that has probably been quietly frustrating you since you started testing your agent.

Your agent has amnesia.

[Show slide 1: The words "Give It Memory" over a simple brain icon]

Here is what I mean. You ask your agent, "Summarize this report for me." It does a beautiful job. Then you follow up with, "Now make it shorter." And your agent responds with something like, "Make what shorter?" It has no idea what you are talking about, because the moment it finished that first response, everything vanished. Every conversation starts from zero.

This is not a bug in your code. This is simply how large language models work by default. They are stateless. Each request is a completely fresh start, like meeting someone for the first time, over and over again.

[Show slide 2: Two speech bubbles, the second one with a large question mark]

So today, we are building memory. And I want to reassure you before we even open the editor: this is far simpler than most beginners expect. Memory is not magic. Memory is a list.

[Switch to screen recording, code editor open]

Let me show you the core idea. When you send a message to your model, you are not really sending one message. You are sending a list of messages, and each message has two parts: a role and some content. The role tells the model who is speaking. It might be system, which sets the personality and rules. It might be user, which is your human. Or it might be assistant, which is your agent's own previous replies.

So the trick to memory is this. Instead of sending a list with a single user message every time, we keep that list alive between turns. When the user speaks, we append their message to the list. When the agent responds, we append the response to the list too. Then on the next turn, we send the entire list again. The model reads back through the history and understands context naturally, because it can literally see everything that was said before.

[Highlight the append lines in the editor]

Watch what happens now. I ask it to summarize the report. Then I say, make it shorter. And look, it knows exactly what I mean, because the earlier exchange is sitting right there in the conversation history. That is memory. That is the whole secret.

[Switch back to instructor]

But we are building a professional tool, not a toy, so let us go one step further. In real applications, you will have many users, and each user might have several separate conversations. You do not want your accountant's chat about tax records leaking into your marketing team's chat about campaign ideas. This is where sessions come in.

[Show slide 3: One database, three separate session threads branching out]

A session is simply a labelled conversation. We give each conversation a unique session identifier, and we store its message history under that label. When a request comes in, we look up the history for that session, add the new message, get a response, and save it back. Same list, just organised properly.

[Switch to screen recording, showing a session store]

In the notebook for today, we start with a simple dictionary in memory, which is perfect for learning. Then we upgrade to persistent storage, so your conversations survive after you shut down the program. Your agent can now pick up a discussion from yesterday.

There is one more thing I need you to understand, and this is what separates a good engineer from someone who just copies code. Conversation history is not free. Every message you send back counts toward the model's context window, and it costs tokens. A conversation that runs for hours will eventually get too long, too slow, and too expensive.

[Show slide 4: A long list being compressed into a short summary block]

So we manage it. Today we cover two practical strategies. The first is windowing, where we keep only the most recent turns, plus the system instructions. The second is summarising, where we ask the model to compress older parts of the conversation into a short recap, and we carry that recap forward instead of every single word.

That is genuinely how professional agent systems handle long conversations.

[Switch back to instructor, direct to camera]

So here is your assignment. Open today's notebook, add session memory to your agent, and then hold a conversation of at least ten turns without ever repeating context. Then push it. Try to break it. Find out what happens when the history gets long.

You now have an agent that thinks, acts, and remembers. Tomorrow, on Day Four, we give it knowledge, connecting it to your own documents so it can answer questions about things it was never trained on.

Excellent work today. I will see you in the next session.

[End screen: Day Four, Give It Knowledge]