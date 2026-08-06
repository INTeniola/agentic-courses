# Day 4 Video Transcript: Quality Control

[Open on instructor, facing camera]

Welcome back to Day Four of the AgenticLabs Second Brain Bootcamp. Take a moment and look at what you have already built. On Day One you had an idea. Today you have a working agent that ingests your notes, stores them as embeddings, retrieves the right chunks, and answers your questions in your own words. That is a real engineering achievement, and you should be proud of it.

But here is the honest truth that separates a demo from a product. A demo works when you are watching. A product works when you are not. Today we make your Second Brain trustworthy. Today is Quality Control.

[Show slide one: The three pillars of Quality Control — Temperature, Guardrails, Evaluation]

We are going to cover three things. First, the temperature parameter, which controls how your agent thinks. Second, guardrails, which control what your agent is allowed to do. And third, evaluation, which tells you whether any of it is actually working.

Let us start with temperature.

[Show slide two: A simple dial, from zero on the left to one on the right]

Every time your language model generates a word, it is choosing from a list of possible next words, each with a probability. Temperature is the dial that decides how adventurous that choice is. Turn the dial down toward zero, and the model almost always picks the most likely word. The output becomes focused, consistent, and repeatable. Turn the dial up toward one, and the model starts considering less likely options. The output becomes more varied, more surprising, more creative.

Now, which one do you want for a Second Brain? Think about it for a second. Your agent's job is to tell you what is actually in your notes. It is not writing poetry. It is not brainstorming startup names. It is reporting facts. So we want a low temperature. For retrieval-based question answering, I recommend starting at zero point one or zero point two.

[Switch to screen recording: the agent code, highlighting the temperature setting]

Here in our generation function, you can see the temperature parameter. Right now it may be sitting at the default, which is often zero point seven. I want you to change it to zero point two and then run the same question three times.

[Show side by side output comparison]

Notice what happened. At the higher temperature, the answers drift. The agent adds flourishes. Sometimes it invents a detail that is not in your notes at all. At zero point two, the answers are tight, consistent, and grounded. That consistency is not boring. That consistency is trust.

[Return to instructor]

Now, temperature alone is not enough. Even a low temperature model will confidently answer a question it has no information about. That is where guardrails come in.

[Show slide three: Guardrails checklist]

A guardrail is simply a boundary you build into your system so the agent fails safely instead of failing loudly. We are going to add three today.

The first is the grounding instruction. In your system prompt, you will tell the agent plainly: answer only using the context provided. If the context does not contain the answer, say that you do not know. Do not guess.

The second is the fallback response. Instead of leaving that to chance, give your agent an exact sentence to use, something like: I could not find that information in your notes. That single line turns a hallucination into a helpful signal.

The third is scope control. Your Second Brain is a notes assistant. If someone asks it to write malicious code or wander far outside its purpose, it should politely decline and redirect.

[Switch to screen recording: updating the system prompt with the three guardrails]

Watch how few lines this takes. Guardrails are not complicated engineering. They are clear thinking, written down.

[Return to instructor]

Finally, evaluation. This is the skill that will make you stand out.

[Show slide four: The golden question set]

Create a simple table with ten questions. Five should have clear answers inside your notes. Three should be questions your notes only partially cover. And two should be questions your notes definitely do not cover. Now run all ten and score each answer on three things: Is it correct? Is it grounded in the retrieved text? Did it refuse appropriately when it should have?

That is your baseline. Every time you change a prompt, a chunk size, or a temperature setting, you rerun those ten questions. If the score goes up, keep the change. If it goes down, revert. That is how professional AI teams work, and now it is how you work.

[Show slide five: Today's assignment]

Your assignment: lower your temperature, add all three guardrails, and build and run your ten question evaluation set. Post your before and after scores in the community channel.

[Return to instructor, closing]

You are no longer just building something that works. You are building something you can defend. Tomorrow, on Day Five, we deploy your Second Brain and put it in front of real users.

Excellent work today. I will see you tomorrow.