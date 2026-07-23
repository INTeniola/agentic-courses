Here is the complete, professional, word-for-word Video Voiceover Script and Storyboard for Day 1 of the AI Agents Bootcamp.

---

## AI Agents Bootcamp: Day 1 - Your First AI Agent

**Video Title:** AI Agents Bootcamp | Day 1: From Passive Prompts to Active Agents
**Video Length:** ~9 minutes
**Presenter:** An engaging, clear-speaking AI Dev Advocate for AgenticLabs.ng

---

### **Section 1: Introduction & Hook**

**(0:00 - 1:15)**

[VISUAL CUE: Opening title card with the AgenticLabs.ng logo and "AI AGENTS BOOTCAMP - DAY 1". Upbeat, modern, tech-focused music fades in and then softens to a background hum.]

**VOICEOVER:**
Hello and welcome to Day 1 of the AgenticLabs.ng AI Agents Bootcamp! My name is [Presenter's Name], and over the next five days, we're going to take you on a journey from being a user of AI to becoming a director of AI.

[VISUAL CUE: Presenter appears on screen, full-frame, in a clean, modern studio setting. A lower-third graphic appears: "Presenter Name, AI Dev Advocate, AgenticLabs.ng".]

You’ve probably used a chatbot. You ask a question, you get an answer. It's a powerful but fundamentally passive experience. You are the one in the driver's seat, doing all the work, one prompt at a time.

[VISUAL CUE: Show Slide - "The Old Way: Passive AI". A simple diagram shows a user typing a prompt into a box labeled "LLM", which then outputs text. The user then has to take that text and manually use it in another application (e.g., a browser, a code editor).]

But the entire field is undergoing a massive shift. We're moving from these passive language models to something far more powerful: active, autonomous agents.

[VISUAL CUE: The slide animates. The "LLM" box gains a "Brain" icon. New boxes labeled "Tools (Search, Code, etc.)" and "Memory" appear, connecting to the brain. The diagram is now labeled "The New Way: Autonomous Agent". The user gives a single "Goal" and the agent system works in a loop.]

Imagine hiring a brilliant, incredibly fast intern. You wouldn't tell them exactly what to type into Google or which lines of code to write. You'd give them a high-level goal, like, "Hey, please research our top competitors and summarize their latest product launches."

That’s an AI Agent. It's a system that can understand a goal, reason about the steps needed, use tools to gather information or take action, and work autonomously until the job is done.

Today, you'll take your first step. You'll learn the core concepts that define an agent, and you'll write the code to "hire" the brain for your very first one. Let's get started.

[VISUAL CUE: Quick transition to a title card: "Section 2: The Anatomy of an Agent".]

---

### **Section 2: Conceptual Deep Dive**

**(1:15 - 3:30)**

**VOICEOVER:**
So, what makes an agent... an agent? Based on foundational research, we can break any agent down into three core components. Think of it like the anatomy of your new AI intern.

[VISUAL CUE: Show Slide - "The Anatomy of an Agent". A central human silhouette with three labels pointing to it: Brain, Hands, Nervous System.]

First, and most importantly, is the **Brain**.

[VISUAL CUE: The "Brain" part of the slide highlights. An animation shows data flowing into a glowing neural network icon.]

This is the Large Language Model, or LLM, at its core—a model like Google's Gemini or OpenAI's GPT-4. This is the reasoning engine. It's what allows the agent to understand your goal, to think, to strategize, and to make decisions. It’s your intern’s intelligence and common sense. But a brain alone is trapped. It can think, but it can't *do*. For that, it needs hands.

[VISUAL CUE: The "Hands" part of the slide highlights. The neural network icon now connects out to various API logos: Google Search, Calendar, a generic code symbol `{;}`.]

The **Hands** are the **Tools** the agent can use. These aren't physical hands, but connections to the outside world—APIs, databases, or other software. A tool could be a function that lets the agent search the web, write a file, or send an email. Tools give the brain the ability to act and to perceive the world beyond its own knowledge.

[VISUAL CUE: The "Nervous System" part of the slide highlights, showing looping arrows connecting the Brain and Hands.]

Finally, you have the **Nervous System**, or the **Orchestration Layer**. This is the code that connects the Brain and the Hands. It manages the entire process, running what we call the **Think-Act-Observe loop**.

[VISUAL CUE: Show a new, clear diagram of the "Think-Act-Observe Loop".]

Let's break that down.
1.  **Think:** The Brain analyzes the goal and the current situation, and forms a plan. "My first step should be to search for X."
2.  **Act:** The Nervous System executes that plan, calling the appropriate Tool. It actually performs the web search.
3.  **Observe:** The agent receives the result of that action—the search results. This new information is fed back to the Brain.

And the loop repeats. The brain thinks about the new information and decides the next step. This cycle of Think, Act, Observe continues until the overall goal is achieved. It’s how an agent breaks down a huge, complex problem into small, manageable steps.

[VISUAL CUE: Quick transition to a title card: "Section 3: Code Walkthrough - Hiring the Brain".]

---

### **Section 3: Code Walkthrough**

**(3:30 - 7:00)**

**VOICEOVER:**
Alright, enough theory. Let's make this real. For the rest of this video, we'll be working in a Google Colab notebook, which you can find linked below. This is your interactive lab for the entire bootcamp.

[VISUAL CUE: Screen transitions to a screen recording of the Day 1 Colab Notebook. The presenter's voice continues, and their face might appear in a small circle in the corner.]

The first thing we need to do is set up our environment. This involves installing Google's Generative AI library and configuring our API key. The key is like a password that gives our code access to the Gemini models.

[VISUAL CUE: Mouse scrolls to Cell 2 and Cell 3 in the Colab notebook. The mouse highlights the `!pip install` and `genai.configure` lines.]

We'll run this cell, which installs the library and securely loads our API key. And with that... we're ready to hire our agent's Brain.

[VISUAL CUE: Scroll down to Cell 5. The code is highlighted as the presenter speaks.]

In this cell, we're doing three simple things. First, we instantiate the model. `model = genai.GenerativeModel('gemini-1.5-flash')`. This line of code *is* us hiring the Brain. We're choosing Gemini 1.5 Flash—a fast, powerful, and efficient model perfect for our needs.

Next, we create our prompt: `"Tell me a fun fact about Nigeria."` And finally, we send that prompt to the model and print the response. Let's run it.

[VISUAL CUE: The cell executes, and the output appears below it. For example: "Nigeria is home to Nollywood, the second largest film industry in the world by volume."]

And there you have it. Our first interaction with the Brain. But to get reliable results, especially as our tasks get more complex, we need to be better at giving instructions.

[VISUAL CUE: Scroll down to Cell 6, the markdown for "The Prompting Blueprint".]

We use a simple but powerful framework called the **RTCF Prompting Blueprint**: Role, Task, Context, and Format.

[VISUAL CUE: Scroll down to Cell 10, showing the "Strong Prompt" code.]

Look at this example. Instead of just "Explain AI," we give it a **Role**: "You are a science communicator." A **Task**: "Explain the concept of AI." Crucial **Context**: "Your explanation is for a 10-year-old." And a specific **Format**: "Structure your answer in two short paragraphs."

By providing this structure, we transform a vague request into a precise directive, and the quality of the output is night and day.

[VISUAL CUE: Scroll down to Cell 11, the markdown for "Controlling Creativity with Temperature".]

Now, let's talk about the **Temperature Dial**. This is a parameter that controls the creativity or randomness of the model's output. Think of it as a creativity dial.

A low temperature, like 0.1, makes the model very predictable and factual.

[VISUAL CUE: Highlight the code in Cell 12, showing `temperature: 0.1` and the prompt "What is the capital of France?"]

If you ask it for the capital of France, you want one, correct answer. You want low temperature.

A high temperature, like 1.5, makes the model more creative and surprising.

[VISUAL CUE: Highlight the code in Cell 14, showing `temperature: 1.5` and the prompt "Write a one-sentence slogan for a new brand of coffee."]

If you're brainstorming slogans, you want variety and imagination. You want high temperature. Mastering this dial is key to getting the right output for your specific task.

[VISUAL CUE: Quick transition to a title card: "Section 4: Your Capstone Challenge".]

---

### **Section 4: Capstone Challenge & Recap**

**(7:00 - 8:45)**

**VOICEOVER:**
We've covered the core concepts of agents and the fundamentals of interacting with an LLM. Now, it's time to put it all together and introduce your mission for this bootcamp.

[VISUAL CUE: Show a slick graphic with the title "5-DAY CAPSTONE CHALLENGE" and below it, "Build a Personal AI Research Assistant".]

Over the next five days, you are going to build your very first agent: a Personal AI Research Assistant. You'll give it a research topic, and it will autonomously use a web search tool to find relevant information and provide you with a structured summary.

Today, we've already completed Day 1: We hired the Brain.

[VISUAL CUE: Return to the Colab Notebook, scrolling to the final cell, Cell 16.]

Let's look at this final piece of code. Here, we're not just giving a one-off prompt. We are giving the model a `system_instruction`. This is a powerful feature that sets the agent's core personality and purpose for an entire session.

[VISUAL CUE: Highlight the `system_instruction` string in the code.]

We've told it: "You are a world-class research assistant. You MUST follow this format exactly: Topic, Summary, and Keywords." We've essentially hard-coded its job description into its virtual DNA.

Now, when we ask it a simple question like, "What are the benefits of learning a new language?"...

[VISUAL CUE: Execute Cell 16. The structured output appears, perfectly formatted.]

Look at that. It follows our instructions to the letter. It restates the topic, gives a three-point summary, and lists keywords. It didn't just answer the question; it completed the task according to our precise specifications. This is the first, crucial step toward building a true agent.

[VISUAL CUE: Presenter appears back on screen, full-frame.]

So, to recap today:
You learned that agents are a leap beyond passive chatbots.
You understand the core anatomy: the Brain, the Tools, and the Think-Act-Observe loop.
And you've written the code to configure the Brain of your first agent, mastering prompts and temperature.

Your homework is to play with this notebook. Change the system instruction. Try different questions. See how adjusting the temperature affects the research assistant's tone.

Tomorrow, we give our agent its Hands. We’ll connect it to a live web search tool, and your research assistant will take its first look at the real, live internet. It’s going to be an exciting day.

Thank you for joining. I'll see you in Day 2.

[VISUAL CUE: Outro screen with AgenticLabs.ng logo. Links to the Colab notebook and course website appear. Upbeat music swells and fades out.]