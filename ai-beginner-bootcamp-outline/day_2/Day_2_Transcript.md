# Day 2 Video Transcript: Give it Hands

[Show slide 1: Day 2 — Give It Hands]

Welcome back to Day 2 of the Second Brain Bootcamp. If you are here, it means you survived Day 1, and more importantly, it means you built something real. Take a moment to appreciate that. Yesterday, you gave your agent a brain. Today, we give it hands.

[Show slide 2: Recap of Day 1]

Let us quickly remember where we stopped. Yesterday, we connected to a language model and wrapped it in a simple loop so it could hold a conversation and remember what you told it within that session. It could reason. It could summarize. It could explain things back to you in your own words. That was the brain.

But here is the honest truth about that brain. It is trapped. Everything your agent knows was frozen at the moment its training finished. Ask it what happened in the news this morning, or what the current exchange rate is, or who won a match last night, and it will either guess confidently or apologize politely. Neither of those is useful.

[Show slide 3: A brain in a jar]

Think of it like a brilliant professor locked inside a windowless room. Extremely intelligent. Completely disconnected. Today, we open a window. In agent language, we call that window a tool.

[Show slide 4: What is a tool?]

A tool is simply a function your agent is allowed to call. That is it. It could be a web search. It could be a calculator. It could be a weather lookup, a database query, or an email sender. You write a normal function in code, you describe what it does in plain English, and you hand that description to the model.

Now here is the part that makes people smile the first time they see it. The model does not execute the function itself. It cannot. What it does is decide. It looks at your question, it looks at the list of tools available, and it says, I think I need the search tool for this, and here is what I want to search for. Your code then runs that search, collects the result, and hands it back to the model. The model reads the fresh information and writes the final answer.

Read the question. Pick the tool. Call the tool. Read the result. Answer. That loop is the heart of every serious AI agent you have ever heard about.

[Show slide 5: The agent loop diagram]

Let me point out something crucial before we touch code. The description you write for your tool is not decoration. It is instruction. The model chooses tools based on how you describe them. If you write a vague description like handles stuff, your agent will be confused. If you write something clear, like search the live web for current events, news, prices, and any information after the training cutoff, your agent becomes sharp and decisive. Write your descriptions like you are briefing a new intern on their first day.

[Switch to screen recording]

Alright, let us build. On your screen you can see the project from yesterday. First, we are going to sign up for a search provider and grab an API key. I am using a free tier here, so no card is required. Notice that I am putting that key inside my environment file, never directly in my code. Say it with me. Keys live in environment variables. Always.

Now we define our search function. Look how ordinary this is. It takes a query string, it calls the search service, and it returns the top results as clean text. There is no magic here. It is regular code.

Next, we register it with the agent. We give it a name, a clear description, and we tell the model what input it expects. Then we pass the tool list into our agent when we create it.

Let us test. I will ask, what are the top technology headlines today?

Watch the terminal carefully. Do you see that line? The model just requested the search tool and passed in its own query. It wrote that query by itself. Now our code runs the search, returns the results, and there it is. A fresh, current, accurate answer with today's information.

[Switch back to camera]

Pause here and let that sink in. Your agent just reached outside itself, gathered new information from the live internet, and reasoned over it. That is no longer a chatbot. That is an agent.

[Show slide 6: Today's assignment]

Your homework. First, get web search working end to end. Second, add one more tool of your choice, something as simple as a calculator or a date function. Third, and this is the fun part, ask your agent a question that forces it to use both tools in one answer.

Post your terminal screenshot in the community channel. I read every single one.

Tomorrow, on Day 3, we solve the memory problem properly. Your agent will start remembering you across sessions, not just within one conversation.

Excellent work today. Go give your agent some hands. I will see you tomorrow.