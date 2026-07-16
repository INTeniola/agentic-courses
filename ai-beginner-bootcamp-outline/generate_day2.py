import os
import json
import PyPDF2
from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List, Literal

try:
    client = genai.Client(vertexai=True, project="quizant", location="us-central1")
except Exception as e:
    print(f"Error initializing GenAI Client: {e}")
    exit(1)

# Pydantic schemas for the notebook
class Cell(BaseModel):
    cell_type: Literal["markdown", "code"]
    source: str

class LessonNotebook(BaseModel):
    cells: List[Cell]

def extract_pdf_text(filepath):
    text = ""
    if not os.path.exists(filepath):
        print(f"Warning: PDF {filepath} not found.")
        return text
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def main():
    print("Reading Kaggle Day 2 resources...")
    pdf_path = "day_2/2025_Day_2_Rewrite_v1_AgentTools.pdf"
    whitepaper_text = extract_pdf_text(pdf_path)
    
    nb_2a_text = ""
    if os.path.exists("day_2/day-2a-agent-tools.ipynb"):
        with open("day_2/day-2a-agent-tools.ipynb", "r") as f:
            nb_2a_text = f.read()

    nb_2b_text = ""
    if os.path.exists("day_2/day-2b-agent-tools-best-practices.ipynb"):
        with open("day_2/day-2b-agent-tools-best-practices.ipynb", "r") as f:
            nb_2b_text = f.read()

    # 1. Generate Primer
    print("Generating Day 2 Primer (Markdown) using Gemini 2.5 Pro...")
    primer_prompt = f"""
    You are an expert AI Curriculum Writer at AgenticLabs.ng.
    I am providing you with the text of the Kaggle Agent Tools & Interoperability Whitepaper.
    
    Distill its core concepts into a 3-page beginner-friendly Concept Primer (markdown format) for an audience of absolute beginners.
    Focus on:
    - Why Language Models need "Hands" (Tools) to interact with the real world.
    - The difference between Custom Function Tools (doing math) and Multi-Agent delegation.
    - Explain Model Context Protocol (MCP) like a universal "USB-C cable" that lets AI plug into any database or app securely.
    - End with a section introducing the next step for their Mini-Capstone: upgrading their Personal Research Assistant to use a search tool.
    
    Output strictly in markdown format. Do not include JSON wrappers.
    
    Whitepaper Text Context (Extract):
    {whitepaper_text[:30000]} # taking first 30k chars
    """
    
    primer_res = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=primer_prompt,
        config=types.GenerateContentConfig(temperature=0.3)
    )
    
    # Strip markdown fences if present
    content = primer_res.text
    if content.startswith("```markdown"):
        content = content.replace("```markdown\n", "", 1)
        if content.endswith("```"):
            content = content[:-3]
    elif content.startswith("```"):
        content = content.replace("```\n", "", 1)
        if content.endswith("```"):
            content = content[:-3]
            
    with open("day_2/Day_2_Primer.md", "w") as f:
        f.write(content.strip())
    print("Saved day_2/Day_2_Primer.md")

    # 2. Generate Notebook
    print("Generating Day 2 Interactive Notebook (JSON) using Gemini 2.5 Pro...")
    nb_prompt = f"""
    You are an expert AI Curriculum Writer. 
    Based on the two Kaggle Codelabs provided below, generate an interactive Google Colab notebook for absolute beginners.
    
    We ARE using `google-adk` in this notebook, just like the Kaggle course.
    Requirements for the cells:
    1. A markdown header and introduction.
    2. Setup code cell installing `google-adk` and getting GOOGLE_API_KEY from `google.colab.userdata`.
    3. Code cell: Import necessary modules (`google.adk.agents.LlmAgent`, `google.adk.models.google_llm.Gemini`, etc).
    4. Markdown: Explain Function Tools.
    5. Code cell: Define a simple python function tool (e.g., currency converter or simple lookup).
    6. Code cell: Create an `LlmAgent` that uses this tool, and run it.
    7. Markdown: Explain Multi-Agent Delegation (using one agent as a tool).
    8. Code cell: Create a `calculation_agent` and pass it as an `AgentTool` to another agent. Run it.
    9. Markdown: Explain MCP & Human-in-the-loop (pausing for approval).
    10. Code cell: Implement a simple approval flow using `ToolContext.request_confirmation` as shown in the day-2b codelab.
    11. Markdown: Mini-Capstone update.
    12. Code cell: Configure the Research Assistant from Day 1, but now pass it `google_search` as a built-in tool.
    
    Kaggle Reference Codelab (Day 2a):
    {nb_2a_text}
    
    Kaggle Reference Codelab (Day 2b):
    {nb_2b_text}
    
    Output must match the JSON schema perfectly. Do not include markdown code block syntax around the JSON output.
    """
    
    nb_res = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=nb_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LessonNotebook,
            temperature=0.2
        )
    )
    
    nb_data = json.loads(nb_res.text)
    
    formatted_cells = []
    for cell in nb_data["cells"]:
        source_lines = [line + "\n" for line in cell["source"].split("\n")]
        if source_lines and source_lines[-1] == "\n":
            source_lines[-1] = source_lines[-1].rstrip("\n")
            
        formatted_cells.append({
            "cell_type": cell["cell_type"],
            "metadata": {},
            "source": source_lines,
            **({"execution_count": None, "outputs": []} if cell["cell_type"] == "code" else {})
        })
        
    notebook_json = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"}
        },
        "cells": formatted_cells
    }
    
    with open("day_2/Day_2_Notebook.ipynb", "w") as f:
        json.dump(notebook_json, f, indent=2)
    print("Saved day_2/Day_2_Notebook.ipynb")

if __name__ == "__main__":
    main()
