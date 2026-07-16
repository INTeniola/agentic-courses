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
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def main():
    print("Reading Kaggle resources...")
    pdf_path = "day_1/2025_Day_1_Rewrite_v1_IntroductionToAgents.pdf"
    whitepaper_text = extract_pdf_text(pdf_path)
    
    with open("day_1/day-1a-from-prompt-to-action.ipynb", "r") as f:
        kaggle_nb_text = f.read()

    with open("Module_00_Intro_to_AI.ipynb", "r") as f:
        outline_text = f.read()

    # 1. Generate Primer
    print("Generating Day 1 Primer (Markdown) using Gemini 2.5 Pro...")
    primer_prompt = f"""
    You are an expert AI Curriculum Writer at AgenticLabs.ng.
    I am providing you with the text of the Kaggle Introduction to Agents Whitepaper.
    
    Distill its core architectural concepts (Brain, Hands, Nervous System, Think-Act-Observe loop) into a 3-page beginner-friendly Concept Primer (markdown format) for an audience of absolute beginners.
    Use intuitive analogies (like an intern or restaurant manager) instead of heavy developer jargon. 
    Explain the Prompting Blueprint (Role, Task, Context, Format) and Temperature (Creativity Dial).
    End with a section introducing their 'Mini-Capstone': building a Personal AI Research Assistant over the next 5 days.
    
    Output strictly in markdown format. Do not include JSON wrappers.
    
    Whitepaper Text Context (Extract):
    {whitepaper_text}
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
            
    with open("day_1/Day_1_Primer.md", "w") as f:
        f.write(content.strip())
    print("Saved day_1/Day_1_Primer.md")

    # 2. Generate Notebook
    print("Generating Day 1 Interactive Notebook (JSON) using Gemini 2.5 Pro...")
    nb_prompt = f"""
    You are an expert AI Curriculum Writer. 
    Based on the Kaggle Codelab and the Bootcamp Outline provided below, generate an interactive Google Colab notebook for absolute beginners.
    
    Instead of using the complex `google-adk`, use the standard `google-generativeai` library.
    Requirements for the cells:
    1. A markdown header and introduction.
    2. Setup code cell installing `google-generativeai` and getting GOOGLE_API_KEY from `google.colab.userdata`.
    3. A markdown explanation of how Language Models work.
    4. A simple hello world code cell calling `gemini-1.5-flash` with a fun fact about Nigeria.
    5. Markdown explaining the Prompting Blueprint (Role, Task, Context, Format).
    6. Code cells demonstrating a Weak Prompt vs Strong Prompt (Role, Task, Context, Format).
    7. Markdown explaining Temperature.
    8. Code cells demonstrating Temperature (one cell at 0.1, one at 1.5).
    9. A markdown cell introducing their Mini-Capstone.
    10. A code cell configuring the system_instruction for a Research Assistant using `gemini-1.5-flash`.
    
    Kaggle Reference Codelab:
    {kaggle_nb_text}
    
    Bootcamp Outline:
    {outline_text}
    
    Output must match the JSON schema perfectly.
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
    
    with open("day_1/Day_1_Notebook.ipynb", "w") as f:
        json.dump(notebook_json, f, indent=2)
    print("Saved day_1/Day_1_Notebook.ipynb")

if __name__ == "__main__":
    main()
