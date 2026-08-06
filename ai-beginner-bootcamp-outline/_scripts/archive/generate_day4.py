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
    print("Reading Kaggle Day 4 resources...")
    pdf_path = "day_4/2025_Day_4_Rewrite_v1_AgentQuality.pdf"
    whitepaper_text = extract_pdf_text(pdf_path)
    
    nb_4a_text = ""
    if os.path.exists("day_4/day-4a-agent-observability.ipynb"):
        with open("day_4/day-4a-agent-observability.ipynb", "r") as f:
            nb_4a_text = f.read()

    nb_4b_text = ""
    if os.path.exists("day_4/day-4b-agent-evaluation.ipynb"):
        with open("day_4/day-4b-agent-evaluation.ipynb", "r") as f:
            nb_4b_text = f.read()

    # 1. Generate Primer
    print("Generating Day 4 Primer (Markdown) using Gemini 2.5 Pro...")
    primer_prompt = f"""
    You are an expert AI Curriculum Writer at AgenticLabs.ng.
    I am providing you with the text of the Kaggle Agent Quality Whitepaper.
    
    Distill its core concepts into a 3-page beginner-friendly Concept Primer (markdown format) for an audience of absolute beginners.
    Focus on:
    - The Non-Determinism Problem: Why agents can't be tested like traditional software.
    - Observability: Why logging the Think-Act-Observe loop is critical for debugging (X-Raying the agent).
    - Evaluations (Evals): Creating test datasets and using "LLM-as-a-Judge" to grade an agent's performance.
    - End with a section introducing the next step for their Mini-Capstone: writing a basic evaluation test for the Personal Research Assistant.
    
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
            
    with open("day_4/Day_4_Primer.md", "w") as f:
        f.write(content.strip())
    print("Saved day_4/Day_4_Primer.md")

    # 2. Generate Notebook
    print("Generating Day 4 Interactive Notebook (JSON) using Gemini 2.5 Pro...")
    nb_prompt = f"""
    You are an expert AI Curriculum Writer. 
    Based on the two Kaggle Day 4 Codelabs provided below, generate an interactive Google Colab notebook for absolute beginners.
    
    We ARE using `google-adk` in this notebook. Keep the evaluation concepts focused on simple LLM-as-a-Judge scripts rather than complex third-party tools.
    Requirements for the cells:
    1. A markdown header and introduction to Agent Quality.
    2. Setup code cell installing `google-adk` and configuring GOOGLE_API_KEY.
    3. Markdown: Explaining Observability.
    4. Code cell: Demonstrate how to hook into the agent's event stream (or use ADK's built-in observability) to print out exactly what tools the agent is calling behind the scenes.
    5. Markdown: Explaining Evaluations (LLM-as-a-Judge).
    6. Code cell: Set up a small test dataset (e.g., 2-3 questions) and run the agent against them.
    7. Code cell: Create a simple evaluator agent that grades the primary agent's responses as "Pass" or "Fail" based on criteria.
    8. Markdown: Mini-Capstone update.
    9. Code cell: Write a basic evaluation test for the Personal Research Assistant to ensure it is actually adhering to the user's formatting preferences (from Day 3).
    
    Kaggle Reference Codelab (Day 4a):
    {nb_4a_text}
    
    Kaggle Reference Codelab (Day 4b):
    {nb_4b_text}
    
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
    
    with open("day_4/Day_4_Notebook.ipynb", "w") as f:
        json.dump(notebook_json, f, indent=2)
    print("Saved day_4/Day_4_Notebook.ipynb")

if __name__ == "__main__":
    main()
