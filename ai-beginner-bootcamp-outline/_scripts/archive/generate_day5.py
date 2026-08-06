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
    print("Reading Kaggle Day 5 resources...")
    pdf_path = "day_5/2025_Day_5_Rewrite_v1_Prototype.pdf"
    whitepaper_text = extract_pdf_text(pdf_path)
    
    nb_5a_text = ""
    if os.path.exists("day_5/day-5a-agent2agent-communication.ipynb"):
        with open("day_5/day-5a-agent2agent-communication.ipynb", "r") as f:
            nb_5a_text = f.read()

    nb_5b_text = ""
    if os.path.exists("day_5/day-5b-agent-deployment.ipynb"):
        with open("day_5/day-5b-agent-deployment.ipynb", "r") as f:
            nb_5b_text = f.read()

    # 1. Generate Primer
    print("Generating Day 5 Primer (Markdown) using Gemini 2.5 Pro...")
    primer_prompt = f"""
    You are an expert AI Curriculum Writer at AgenticLabs.ng.
    I am providing you with the text of the Kaggle "Prototype to Production" Whitepaper.
    
    Distill its core concepts into a 3-page beginner-friendly Concept Primer (markdown format) for an audience of absolute beginners.
    Focus on:
    - The "Last Mile" Gap: Why 80% of the work happens *after* the prototype is finished (security, infrastructure, validation).
    - Agent2Agent (A2A) Communication: How different specialized agents talk to each other to solve massive problems.
    - Deployment: The high-level concepts of hosting an agent via CI/CD pipelines so it runs 24/7.
    
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
            
    with open("day_5/Day_5_Primer.md", "w") as f:
        f.write(content.strip())
    print("Saved day_5/Day_5_Primer.md")

    # 2. Generate Notebook
    print("Generating Day 5 Interactive Notebook (JSON) using Gemini 2.5 Pro...")
    nb_prompt = f"""
    You are an expert AI Curriculum Writer. 
    Based on the two Kaggle Day 5 Codelabs provided below, generate an interactive Google Colab notebook for absolute beginners.
    
    We ARE using `google-adk` in this notebook. Abstract away heavy dev-ops Docker/Kubernetes code and focus on the architecture of exposing an agent.
    Requirements for the cells:
    1. A markdown header and introduction to Prototype to Production.
    2. Setup code cell installing `google-adk` and configuring GOOGLE_API_KEY.
    3. Markdown: Explaining Agent2Agent Interoperability.
    4. Code cell: Demonstrate how to configure two distinct agents to communicate (e.g., a delegator agent asking a researcher agent a question).
    5. Markdown: Explaining Deployment.
    6. Code cell: Simulate a deployment scenario by wrapping an agent in a mock Python function that acts like a REST API endpoint (e.g. `def api_route_chat(request): ...`).
    7. Markdown: The Grand Finale (Mini-Capstone completion).
    8. Code cell: The Personal Research Assistant is finalized. Bring together `google_search` tool, a system instruction, and a mock deployment endpoint to show the final product.
    
    Kaggle Reference Codelab (Day 5a):
    {nb_5a_text}
    
    Kaggle Reference Codelab (Day 5b):
    {nb_5b_text}
    
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
    
    with open("day_5/Day_5_Notebook.ipynb", "w") as f:
        json.dump(notebook_json, f, indent=2)
    print("Saved day_5/Day_5_Notebook.ipynb")

if __name__ == "__main__":
    main()
