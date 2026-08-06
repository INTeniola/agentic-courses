import json
import os

def update_notebook(path):
    print(f"Updating {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' or cell['cell_type'] == 'markdown':
            new_source = []
            for line in cell['source']:
                # Common replacements
                line = line.replace('!pip install -q google-adk google-api-python-client', '!pip install -q google-adk wikipedia')
                line = line.replace('!pip install -q google-adk', '!pip install -q google-adk wikipedia')
                
                # Day 2 specific
                line = line.replace('from google.adk.tools import google_search, AgentTool, ToolContext', 'from google.adk.tools import AgentTool, ToolContext')
                line = line.replace('By giving it the `google_search` tool', 'By giving it the `search_wikipedia` tool')
                line = line.replace('the `google_search` tool', 'the `search_wikipedia` tool')
                line = line.replace('tools=[google_search]', 'tools=[search_wikipedia]')
                line = line.replace('--- Running Research Assistant with Google Search ---', '--- Running Research Assistant with Wikipedia Search ---')
                
                # Day 4 specific
                line = line.replace('from google.adk.tools.google_search_tool import google_search', 'import wikipedia\n\ndef search_wikipedia(topic: str) -> dict:\n    \"\"\"Searches Wikipedia for real-world facts and summaries.\"\"\"\n    print(f"[Agent is reading Wikipedia about: {topic}]")\n    try:\n        return {"status": "success", "result": wikipedia.summary(topic, sentences=3)}\n    except Exception:\n        return {"status": "error", "error_message": f"Could not find information on {topic}."}\n')
                
                new_source.append(line)
            cell['source'] = new_source

    # Special handling for Day 5 cell 12 (the google search tool setup)
    if 'Day_5_Notebook.ipynb' in path:
        for cell in nb['cells']:
            if cell['cell_type'] == 'code' and any('from google.adk.tools import google_search' in line for line in cell['source']):
                # Rewrite this entire cell
                cell['source'] = [
                    "import wikipedia\n",
                    "\n",
                    "def search_wikipedia(topic: str) -> dict:\n",
                    "    \"\"\"Searches Wikipedia for real-world facts and summaries.\"\"\"\n",
                    "    print(f\"\\n🔍 [Agent is searching Wikipedia for: {topic}]\")\n",
                    "    try:\n",
                    "        return {\"status\": \"success\", \"result\": wikipedia.summary(topic, sentences=3)}\n",
                    "    except Exception:\n",
                    "        return {\"status\": \"error\", \"error_message\": f\"Could not find information on {topic}.\"}\n",
                    "\n",
                    "research_assistant_agent = LlmAgent(\n",
                    "    model=Gemini(model=\"gemini-1.5-flash-latest\"),\n",
                    "    instruction=\"\"\"\n",
                    "    You are a world-class research assistant. Your goal is to answer the user's question accurately and concisely.\n",
                    "    Use the search_wikipedia tool to find the most relevant, up-to-date information.\n",
                    "    Synthesize the information from the search results into a clear answer.\n",
                    "    \"\"\",\n",
                    "    tools=[search_wikipedia]\n",
                    ")\n",
                    "print(\"✅ Personal Research Assistant agent created with Wikipedia Tool.\")\n",
                    "\n",
                    "# --- 3. Create the Final API Endpoint ---\n",
                    "def research_assistant_api(request: dict) -> dict:\n",
                    "    if not research_assistant_agent:\n",
                    "        return {\"error\": \"Agent not initialized. Check previous cell for errors.\"}\n",
                    "    \n",
                    "    print(f\"\\n▶️ Research API received query: '{request.get('query')}'\")\n",
                    "    query = request.get(\"query\")\n",
                    "    if not query:\n",
                    "        return {\"error\": \"'query' not found in request.\"}\n",
                    "\n",
                    "    response = research_assistant_agent.run(query)\n",
                    "    \n",
                    "    api_response = {\"answer\": response.content}\n",
                    "    print(f\"◀️ Research API sending response.\")\n",
                    "    return api_response\n",
                    "\n",
                    "# --- 4. Simulate a Final Client Call ---\n",
                    "if research_assistant_agent:\n",
                    "    print(\"\\n--- Calling the final Research Assistant API... ---\")\n",
                    "    final_client_request = {\"query\": \"What are the main benefits of using a multi-agent system in AI development?\"}\n",
                    "    final_answer = research_assistant_api(final_client_request)\n",
                    "\n",
                    "    print(\"\\n--- Final Answer from Research Assistant --- \")\n",
                    "    print(final_answer.get('answer'))\n"
                ]

    # Special handling for Day 2 to add wikipedia tool definition
    if 'Day_2_Notebook.ipynb' in path:
        # Find the cell that configures the research assistant (which has tools=[search_wikipedia])
        for cell in nb['cells']:
            if cell['cell_type'] == 'code' and any('tools=[search_wikipedia]' in line for line in cell['source']):
                # Prepend the tool definition to this cell
                tool_def = [
                    "import wikipedia\n",
                    "\n",
                    "def search_wikipedia(topic: str) -> dict:\n",
                    "    \"\"\"Searches Wikipedia for real-world facts and summaries.\"\"\"\n",
                    "    print(f\"[Agent is reading Wikipedia about: {topic}]\")\n",
                    "    try:\n",
                    "        return {\"status\": \"success\", \"result\": wikipedia.summary(topic, sentences=3)}\n",
                    "    except Exception:\n",
                    "        return {\"status\": \"error\", \"error_message\": f\"Could not find information on {topic}.\"}\n",
                    "\n"
                ]
                cell['source'] = tool_def + cell['source']

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)

update_notebook('day_2/Day_2_Notebook.ipynb')
update_notebook('day_4/Day_4_Notebook.ipynb')
update_notebook('day_5/Day_5_Notebook.ipynb')
