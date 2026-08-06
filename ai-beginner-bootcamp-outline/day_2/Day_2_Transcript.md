# Day 2 Video Transcript: Give it Hands

[Open on instructor, facing camera]

Welcome back to Day Two of the Universal Knowledge Worker Bootcamp. If you completed yesterday's build, take a moment to appreciate what you did. You gave your agent a brain. You gave it a personality, a system prompt, and the ability to hold a conversation. That is genuinely impressive for one day of work.

But today, we confront a hard truth about that brain.

[Show slide one: a brilliant professor sitting alone in a windowless room]

Imagine the most brilliant professor you have ever met. She has read millions of books. She can reason, summarize, and explain almost anything. Now imagine we lock her in a room with no windows, no phone, and no internet. You slide a question under the door: what is the exchange rate today? What did the Central Bank announce this morning? Is my flight delayed?

She cannot answer. Not because she is unintelligent, but because she is disconnected. Her knowledge stopped on the day her training ended.

That is your agent right now. Brilliant, but trapped.

[Cut back to instructor]

Today we open the door. Today, we give it hands.

[Show slide two: the words Tool Use in large text]

In agent engineering, the word for a hand is a tool. A tool is simply a function, a small piece of code, that your agent is allowed to call when it decides it needs help from the outside world. A web search tool. A calculator. A weather lookup. A database query. Anything you can write in code, your agent can learn to reach for.

Here is the part that surprises most beginners. You do not tell the agent when to use the tool. You describe the tool, and the agent decides.

[Show slide three: the loop diagram with four boxes labelled Thought, Action, Observation, Answer]

This is the loop that powers every serious AI agent in production today. First, Thought. The agent reads your question and reasons about whether it can answer from memory. Second, Action. If it cannot, it selects a tool and writes the input for it, for example a search query. Third, Observation. Your code runs the tool and hands the result back. Fourth, Answer. The agent reads the fresh information and composes a proper response.

And here is the beautiful part. That loop can repeat. Search, read, search again, refine, then answer. That repetition is the difference between a chatbot and an agent.

[Switch to screen recording, code editor open]

Let us build it. In your project folder, we are creating a new file for tools. We will start with a web search tool using a search API designed for agents. You will sign up, copy your key, and store it safely in your environment file, never inside your code and never pushed to a public repository. Say that with me: keys live in the environment.

Now watch this function carefully. It takes one input, a query string. It calls the search service. It returns clean text. That is all. A tool is not magic. It is a normal function.

[Zoom in on the description line above the function]

Now, the single most important line in this entire lesson. This description. This docstring. This is what your agent actually reads when it is deciding whether to use the tool. If you write something vague like "does searching", your agent will use it badly. If you write "Search the live internet for current events, recent news, prices, and any information after the training cutoff", your agent will use it precisely.

Tool descriptions are prompt engineering. Treat them with respect.

[Switch to terminal, run the agent]

Let us register the tool with our agent and run it. I will ask a question no language model could possibly know from memory. Watch the logs.

There. Do you see it? Thought. Then Action, calling web search with a query it wrote by itself. Then Observation, real results flowing back. Then a clean, grounded answer with the source.

[Pause, cut back to instructor]

Take a breath. Your agent just reached into the live world and pulled back the truth. Yesterday it could only talk. Today it can act.

[Show slide four: Your Assignment]

Your assignment. First, get the web search tool running end to end. Second, add one more tool of your own choosing, perhaps a calculator or a currency converter. Third, and this is the fun part, ask your agent a question that forces it to use both tools in a single answer. Post your terminal output in the community channel. I want to see those loops.

One warning before you go. Tools fail. The internet times out. Keys expire. Wrap your tool code in error handling and return a friendly message instead of crashing. Professional agents do not panic. They report and continue.

[Instructor smiles]

Tomorrow, on Day Three, we give your agent a memory of its own documents, so it can answer questions about your files, your reports, your business. Hands today. Long term memory tomorrow.

Go build. I will see you in the next lesson.