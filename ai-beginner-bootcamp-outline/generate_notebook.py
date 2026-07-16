import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🚀 Day 1 — AI Foundations, Prompting & Your First AI Interaction\n",
    "### Agentic Labs 5-Day AI Bootcamp\n",
    "\n",
    "Welcome! This is your interactive session notebook for Day 1.\n",
    "\n",
    "You don't need to understand all the code. Just follow the instructions, \n",
    "run each cell one at a time by clicking ▶️, and watch the AI respond in real time.\n",
    "\n",
    "> ⚠️ Run cells ONE AT A TIME, top to bottom. Do NOT click \"Run All\"."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## ⚙️ Section 1: Setup (5 minutes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.1 Install the Gemini library\n",
    "\n",
    "Run the cell below to install the google-generativeai library.\n",
    "You only need to do this once per session."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -q google-generativeai\n",
    "print(\"✅ Library installed.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.2 Add your API Key\n",
    "\n",
    "**Step 1:** Go to https://aistudio.google.com and sign in with your Google account.\n",
    "**Step 2:** Click \"Get API Key\" → \"Create API Key\" → copy the key.\n",
    "**Step 3:** In this Colab notebook, click the 🔑 key icon in the left sidebar.\n",
    "**Step 4:** Click \"+ Add new secret\", name it `GOOGLE_API_KEY`, paste your key, save.\n",
    "**Step 5:** Run the cell below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import google.generativeai as genai\n",
    "from google.colab import userdata\n",
    "\n",
    "try:\n",
    "    GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')\n",
    "    genai.configure(api_key=GOOGLE_API_KEY)\n",
    "    print(\"✅ API key configured. You're ready to talk to Gemini!\")\n",
    "except Exception as e:\n",
    "    print(f\"🔑 Error: Could not find your API key. Please follow the steps above. Details: {e}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 🤖 Section 2: Your First AI Conversation\n",
    "### What is a Language Model, really?\n",
    "\n",
    "Before we write fancy prompts, let's just talk to the AI.\n",
    "Run the cell below — it sends a simple message to Gemini and prints the reply."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = genai.GenerativeModel('gemini-1.5-flash')\n",
    "\n",
    "response = model.generate_content(\"Hello! Tell me one surprising fact about Nigeria in one sentence.\")\n",
    "print(response.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What just happened?\n",
    "\n",
    "You just made your first API call! Here's the journey your message took:\n",
    "\n",
    "1. 🖊️  Your text was sent to Google's servers\n",
    "2. 🧠  The Gemini language model read it and predicted the most useful response\n",
    "3. 📡  The response was sent back and printed above\n",
    "\n",
    "This is the core of every AI product you've ever used — ChatGPT, Claude, Gemini Chat.\n",
    "The difference is: when you connect this to tools and give it goals, it becomes an *agent*."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## ✍️ Section 3: The Prompting Blueprint\n",
    "### Weak prompts get weak results. Let's fix that."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The 4-Part Blueprint: Role · Task · Context · Format\n",
    "\n",
    "Compare these two prompts:\n",
    "- ❌ Weak: \"Write me an email\"\n",
    "- ✅ Strong: \"You are a professional consultant. Write a 3-sentence follow-up\n",
    "  email to a client who missed our Monday meeting. Keep the tone warm.\n",
    "  Suggest 3 new times using bullet points.\"\n",
    "\n",
    "The difference is structure. Use this formula every time:\n",
    "| Part | Question to ask yourself | Example |\n",
    "|------|--------------------------|---------|\n",
    "| Role | Who is the AI acting as? | \"You are a senior financial advisor\" |\n",
    "| Task | What should it do? | \"Write a summary of...\" |\n",
    "| Context | What background info does it need? | \"The client is a small business owner...\" |\n",
    "| Format | How should it look? | \"Use bullet points, max 5\" |"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ❌ WEAK PROMPT — run this first\n",
    "weak_response = model.generate_content(\"Write me an email\")\n",
    "print(\"=== WEAK PROMPT RESULT ===\")\n",
    "print(weak_response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ✅ STRONG PROMPT — same task, structured using the blueprint\n",
    "strong_prompt = \"\"\"\n",
    "You are a professional business consultant.\n",
    "Write a short follow-up email (3 sentences max) to a client named Emeka who missed \n",
    "our Monday project kickoff meeting.\n",
    "Keep the tone warm but professional.\n",
    "End with 3 bullet points suggesting new meeting times this week.\n",
    "\"\"\"\n",
    "\n",
    "strong_response = model.generate_content(strong_prompt)\n",
    "print(\"=== STRONG PROMPT RESULT ===\")\n",
    "print(strong_response.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 🤔 Notice the difference?\n",
    "\n",
    "The second response is more:\n",
    "- **Focused** — it addresses a specific person and situation\n",
    "- **Structured** — it uses the format we specified\n",
    "- **Usable** — you could send this email with minimal editing\n",
    "\n",
    "This is \"context engineering\" — filling the AI's window with just the right information."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 🚀 Your Turn!\n",
    "\n",
    "Edit the cell below. Replace the `[...]` placeholders with your own task.\n",
    "Run it and see what you get."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ✏️ EDIT THIS CELL — fill in the brackets with your own details\n",
    "my_prompt = \"\"\"\n",
    "You are a [role — e.g. marketing expert, career coach, teacher].\n",
    "[Task — e.g. Write a LinkedIn post, Explain a concept, Create a plan].\n",
    "Context: [Any background the AI needs].\n",
    "Format: [How it should look — bullet points, paragraphs, table, etc.]\n",
    "\"\"\"\n",
    "\n",
    "my_response = model.generate_content(my_prompt)\n",
    "print(my_response.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 🎛️ Section 4: The Temperature Dial\n",
    "### Controlling how creative (or cautious) the AI is"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Every AI model has a \"temperature\" setting — a number between 0 and 2.\n",
    "\n",
    "| Temperature | Behaviour | Best for |\n",
    "|-------------|-----------|----------|\n",
    "| 0.0 – 0.3   | Precise, logical, consistent | Research, summaries, code |\n",
    "| 0.4 – 0.7   | Balanced | Emails, reports |\n",
    "| 0.8 – 2.0   | Creative, varied, surprising | Brainstorming, storytelling |\n",
    "\n",
    "Run the two cells below with the SAME prompt and notice how differently the AI responds."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# LOW TEMPERATURE — precise and factual\n",
    "low_temp_model = genai.GenerativeModel(\n",
    "    'gemini-1.5-flash',\n",
    "    generation_config=genai.GenerationConfig(temperature=0.1)\n",
    ")\n",
    "\n",
    "prompt = \"Give me 3 ways AI could help a small business owner in Lagos save time.\"\n",
    "\n",
    "response_low = low_temp_model.generate_content(prompt)\n",
    "print(\"🥶 LOW TEMPERATURE (0.1) — Precise & Predictable\")\n",
    "print(\"=\"*50)\n",
    "print(response_low.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HIGH TEMPERATURE — creative and varied\n",
    "high_temp_model = genai.GenerativeModel(\n",
    "    'gemini-1.5-flash',\n",
    "    generation_config=genai.GenerationConfig(temperature=1.5)\n",
    ")\n",
    "\n",
    "response_high = high_temp_model.generate_content(prompt)\n",
    "print(\"🔥 HIGH TEMPERATURE (1.5) — Creative & Varied\")\n",
    "print(\"=\"*50)\n",
    "print(response_high.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Key insight\n",
    "\n",
    "If you run the high-temperature cell multiple times, you'll get a *different* answer \n",
    "each time. The low-temperature cell gives nearly the same answer every time.\n",
    "\n",
    "For business tasks (summaries, emails, reports) → keep temperature LOW.\n",
    "For creative tasks (brainstorming, naming, storytelling) → go HIGH."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 🏗️ Section 5: Mini-Capstone — Your Personal AI Research Assistant\n",
    "\n",
    "### The project that runs through all 5 days\n",
    "\n",
    "By the end of Day 5, you will have built a Personal AI Research Assistant — \n",
    "an agent that:\n",
    "- Takes a topic you give it\n",
    "- Searches for current information\n",
    "- Summarises it into a clean daily briefing\n",
    "\n",
    "**Today's job: write the core prompt for this assistant.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This is the core \"brain\" of your Research Assistant.\n",
    "# Edit the system_instruction to match your use case.\n",
    "\n",
    "research_assistant = genai.GenerativeModel(\n",
    "    'gemini-1.5-flash',\n",
    "    system_instruction=\"\"\"\n",
    "    You are a personal research assistant. Your job is to help the user\n",
    "    understand any topic quickly and clearly.\n",
    "\n",
    "    When given a topic:\n",
    "    1. Give a 2-sentence plain-language explanation of what it is\n",
    "    2. List 3 key things the user should know about it\n",
    "    3. End with one practical thing they could do with this knowledge today\n",
    "\n",
    "    Keep your language simple. Avoid jargon. Use Nigerian examples where relevant.\n",
    "    \"\"\"\n",
    ")\n",
    "\n",
    "# Test your assistant — change the topic below!\n",
    "topic = \"Retrieval-Augmented Generation (RAG) in AI\"\n",
    "\n",
    "response = research_assistant.generate_content(f\"Research this topic for me: {topic}\")\n",
    "print(response.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ✅ Well done!\n",
    "\n",
    "You have:\n",
    "- ✅ Connected to a real AI model using an API key\n",
    "- ✅ Seen the difference between weak and strong prompts\n",
    "- ✅ Controlled the AI's creativity using temperature\n",
    "- ✅ Built the first version of your Personal Research Assistant\n",
    "\n",
    "**Save your `system_instruction` — you'll upgrade it on each day of the bootcamp.**\n",
    "\n",
    "### 📚 Resources\n",
    "- [Google AI Studio](https://aistudio.google.com) — where you got your API key\n",
    "- [Gemini API Docs](https://ai.google.dev/gemini-api/docs) — full documentation\n",
    "- [NotebookLM](https://notebooklm.google.com) — drop the Day 1 Primer PDF here for your podcast\n",
    "\n",
    "### 💬 Community\n",
    "Post a screenshot of your Research Assistant's first output in the Discord/WhatsApp group!\n",
    "Tag it: **#day1-output**\n",
    "\n",
    "### 👀 Tomorrow — Day 2: Search Grounding, RAG & Memory\n",
    "You'll learn how to make your Research Assistant fetch real, current information\n",
    "instead of relying only on what Gemini already knows."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open('day_1/Day_1_Notebook.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook generated successfully.")
