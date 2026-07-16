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
    print("Reading Kaggle Day 3 resources...")
    pdf_path = "day_3/2025_Day_3_Rewrite_v1_ContextEngineering.pdf"
    whitepaper_text = extract_pdf_text(pdf_path)
    
    nb_3a_text = ""
    if os.path.exists("day_3/day-3a-agent-sessions.ipynb"):
        with open("day_3/day-3a-agent-sessions.ipynb", "r") as f:
            nb_3a_text = f.read()

    nb_3b_text = ""
    if os.path.exists("day_3/day-3b-agent-memory.ipynb"):
        with open("day_3/day-3b-agent-memory.ipynb", "r") as f:
            nb_3b_text = f.read()

    # 1. Generate Primer
    print("Generating Day 3 Primer (Markdown) using Gemini 2.5 Pro...")
    primer_prompt = f"""
    You are an expert AI Curriculum Writer at AgenticLabs.ng.
    I am providing you with the text of the Kaggle Context Engineering: Sessions & Memory Whitepaper.
    
    Distill its core concepts into a 3-page beginner-friendly Concept Primer (markdown format) for an audience of absolute beginners.
    Focus on:
    - Why models are inherently "stateless" (amnesiac) and what Context Engineering is.
    - Short-Term vs. Long-Term Memory: The difference between a conversation window (Session) and permanent facts stored about a user (Memory/Profile).
    - Context Compaction: How to prevent the context window from overflowing.
    - End with a section introducing the next step for their Mini-Capstone: upgrading their Personal Research Assistant to have persistent memory.
    
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
            
    with open("day_3/Day_3_Primer.md", "w") as f:
        f.write(content.strip())
    print("Saved day_3/Day_3_Primer.md")

    # 2. Generate Notebook
    print("Generating Day 3 Interactive Notebook (JSON) using Gemini 2.5 Pro...")
    nb_prompt = f"""
    You are an expert AI Curriculum Writer. 
    Based on the two Kaggle Day 3 Codelabs provided below, generate an interactive Google Colab notebook for absolute beginners.
    
    We ARE using `google-adk` in this notebook. Keep the code simple and beginner-friendly, abstracting away complex database initialization where possible.
    Requirements for the cells:
    1. A markdown header and introduction to Context Engineering.
    2. Setup code cell installing `google-adk` and configuring GOOGLE_API_KEY.
    3. Markdown: Explaining Sessions.
    4. Code cell: Demonstrate using `SessionService` to track a multi-turn conversation (showing how the agent remembers previous turns).
    5. Markdown: Explaining Session State (Manual Memory).
    6. Code cell: Show how to manually extract and store structured data (like a user's name or preference) into session state.
    7. Markdown: Explaining Automatic Memory (Long-term Profile).
    8. Code cell: Demonstrate the ADK Memory system that automatically extracts user preferences across sessions.
    9. Markdown: Mini-Capstone update.
    10. Code cell: Give the Research Assistant a persistent memory so it remembers the user's research preferences (e.g., "always summarize in bullet points").
    
    Kaggle Reference Codelab (Day 3a):
    {nb_3a_text}
    
    Kaggle Reference Codelab (Day 3b):
    {nb_3b_text}
    
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
    
    with open("day_3/Day_3_Notebook.ipynb", "w") as f:
        json.dump(notebook_json, f, indent=2)
    print("Saved day_3/Day_3_Notebook.ipynb")

if __name__ == "__main__":
    main()
