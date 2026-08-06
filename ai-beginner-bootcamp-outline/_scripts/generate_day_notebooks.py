import os
import json
import httpx
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AGENT_ROUTER_API_KEY")
if not api_key:
    print("Error: AGENT_ROUTER_API_KEY not found in .env")
    exit(1)

client = Anthropic(
    api_key=api_key,
    base_url="https://agentrouter.org",
    http_client=httpx.Client(
        headers={
            "User-Agent": "cline/2.0.0",
            "Accept": "application/json"
        },
        timeout=60.0
    )
)

def generate_theory_markdown(day_number, topic, focus):
    prompt = f"""
    You are an AI curriculum expert for AgenticLabs.ng.
    We are building a Jupyter Notebook for Day {day_number} of a beginner bootcamp.
    Topic: {topic}
    Focus: {focus}
    Capstone Goal: Building a "Universal Knowledge Worker" AI Agent.
    
    Write a 300-500 word "Theory Primer" in Markdown format that explains the core concepts 
    for this day before the student starts coding. 
    Use simple analogies and an encouraging tone.
    Do not use introductory conversational text, just output the raw markdown starting with '## Theory Primer: [Topic Name]'.
    """
    
    try:
        response = client.messages.create(
            model="claude-opus-5",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        content = ""
        for block in response.content:
            if getattr(block, "type", "") == "text":
                content = block.text
            elif hasattr(block, "text"):
                content = block.text
        return content.strip()
    except Exception as e:
        print(f"Error generating theory for Day {day_number}: {e}")
        return ""

def update_notebook(day_number, topic, focus):
    nb_path = f"../day_{day_number}/Day_{day_number}_Notebook.ipynb"
    if not os.path.exists(nb_path):
        print(f"Notebook not found: {nb_path}")
        return
        
    print(f"Updating Notebook for Day {day_number}...")
    theory_md = generate_theory_markdown(day_number, topic, focus)
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    # Find and replace terms in markdown cells
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            new_source = []
            for line in cell['source']:
                line = line.replace('Research Assistant', 'Universal Knowledge Worker')
                line = line.replace('research assistant', 'Universal Knowledge Worker')
                new_source.append(line)
            cell['source'] = new_source
            
    # Insert the theory markdown as the second cell (after title)
    if theory_md:
        new_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in theory_md.split("\n")]
        }
        # Insert after the first cell
        nb['cells'].insert(1, new_cell)
        
    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)
    print(f"Updated {nb_path}")

def main():
    days = [
        (1, "Hire the Brain", "Introduction to autonomous agents, the Think-Act-Observe loop, and configuring Google AI Studio."),
        (2, "Give it Hands", "Connecting the agent to tools like Web Search so it can access real-time information."),
        (3, "Give it Memory", "Implementing conversation sessions so the agent can remember past interactions and context."),
        (4, "Quality Control", "Introducing the temperature parameter, guardrails, and evaluating agent performance."),
        (5, "Multi-Agent Teams", "Creating a system where a Manager, Researcher, and Writer agent collaborate to build a report.")
    ]
    
    for day_num, topic, focus in days:
        update_notebook(day_num, topic, focus)

if __name__ == "__main__":
    main()
