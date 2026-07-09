import os
import json
import re
import time
import argparse
from google import genai
from google.genai import types
from google.genai.errors import APIError
from pydantic import BaseModel
from typing import List, Literal

# Initialize the Gemini Vertex AI Client
# Automatically picks up active gcloud auth and quota project 'quizant'
try:
    client = genai.Client(vertexai=True, project="quizant", location="us-central1")
except Exception as e:
    print(f"Error initializing GenAI Client: {e}")
    client = None

# Pydantic schema for structured output validation
class Cell(BaseModel):
    cell_type: Literal["markdown", "code"]
    source: str

class LessonNotebook(BaseModel):
    learning_objectives: List[str]
    cells: List[Cell]

def clean_filename(title):
    """Convert lesson title into a safe, clean string for filenames."""
    # Replace non-alphanumeric characters with underscores
    safe_title = re.sub(r"[^\w\s-]", "", title)
    safe_title = re.sub(r"[\s-]+", "_", safe_title).strip("_")
    return safe_title

def get_notebook_json(learning_objectives, cells):
    """Wrap raw cells into a valid Jupyter Notebook dictionary structure."""
    formatted_cells = []
    
    # 1. Add Objectives Markdown Cell at the beginning
    objectives_md = "## 🎯 Learning Objectives\n" + "\n".join([f"* {obj}" for obj in learning_objectives])
    formatted_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in objectives_md.split("\n")]
    })
    
    # 2. Add content cells
    for cell in cells:
        # Split source into lines for notebook compatibility
        source_lines = [line + "\n" for line in cell["source"].split("\n")]
        # Remove trailing newline from the very last line to prevent double spaces
        if source_lines and source_lines[-1] == "\n":
            source_lines = source_lines[:-1]
            
        formatted_cells.append({
            "cell_type": cell["cell_type"],
            "metadata": {},
            "source": source_lines,
            **({"execution_count": None, "outputs": []} if cell["cell_type"] == "code" else {})
        })
        
    return {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"}
        },
        "cells": formatted_cells
    }

def construct_prompt(course, section_title, lesson, next_lesson_info=None):
    """Generate the optimized prompt instructions for the lesson type."""
    l_type = lesson["type"]
    prompt = f"""
You are an expert AI Curriculum Writer at AgenticLabs.ng. 
Generate a world-class, educational Jupyter Notebook content for the following lesson:

- Track: {course.get('track_label', 'AI/ML Foundations')}
- Course: {course['id']} — {course['title']}
- Course Description: {course.get('description', '')}
- Audience: {course.get('audience', 'Developers & AI Practitioners')}
- Prerequisites: {course.get('prerequisites', 'Basic python')}
- Current Section: {section_title}
- Lesson ID: {lesson['id']}
- Lesson Title: {lesson['title']}
- Lesson Type: {l_type}

Ensure the content is:
1. World-Class Quality: Explanations must use clear logic, intuitive analogies, and clean formatting. Avoid fluffy content or placeholders.
2. Code-rich and Practical: If this lesson involves coding or concepts, provide actual, runnable, well-commented Python code blocks.
3. 2026 Ready: Refer to modern tools and ecosystem states as of 2026.
"""

    if l_type == "intro":
        prompt += """
Structure the cells as:
1. A welcome block setting expectations, explaining why this course matters, and how it fits into the track.
2. A prerequisites and tools check (e.g. library installations block, Colab environment setup guidance).
3. A simple code block that initializes the environment or runs a basic hello-world demo of the concepts to follow.
"""
    elif l_type == "concept":
        prompt += """
Structure the cells as:
1. A rich markdown block introducing the core concept, using analogies, real-world examples, and step-by-step descriptions.
2. A detailed code cell with fully functional, annotated Python code illustrating the concept in practice.
3. A markdown block explaining how to interpret the code output, details on performance trade-offs, and typical use cases.
4. A resource block with relevant documentation links (Google AI Studio, PyTorch, Hugging Face, etc.).
"""
    elif l_type == "exercise":
        prompt += """
Structure the cells as:
1. A markdown block detailing the exercise task, requirements, and evaluation criteria.
2. A code cell with setup code (e.g., loading a mock dataset, initializing parameters, defining helper functions).
3. A markdown block prompting the student to write their implementation code.
4. A code cell containing the full, high-quality reference solution with detailed comments explaining the implementation decisions.
"""
    elif l_type == "quiz":
        prompt += """
Structure the cells as:
1. A markdown block with 3-5 multiple-choice questions or short-answer concepts to test understanding.
2. A code or markdown block containing the correct answers and detailed explanations, clearly demarcated (e.g., inside an HTML details fold or at the bottom) so students don't see them immediately.
"""
    elif l_type == "final_assessment":
        prompt += """
Structure the cells as:
1. A markdown block giving a comprehensive overview of what the final assessment covers.
2. A list of 5-10 review questions.
3. A larger capstone-style coding problem description.
4. A starter template code block for the capstone task.
5. A detailed solution code block (commented) at the end.
"""
    
    prompt += "\nFormat the response strictly to the JSON schema. Start the generation immediately."
    return prompt

def generate_lesson(course, section_title, lesson, force_regenerate=False, model_name="gemini-2.5-flash"):
    """Fetch the notebook content from Gemini and save to disk."""
    if not client:
        print("GenAI client is not initialized. Skipping.")
        return False
        
    track_dir = "track1_aiml_foundations" if "track1" in course.get("track_id", "track1") else "track2_agentic_ai"
    course_slug = f"{course['id']}_{clean_filename(course['title'])}"
    output_dir = os.path.join(track_dir, course_slug)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = f"Lesson_{lesson['id']}_{clean_filename(lesson['title'])}.ipynb"
    filepath = os.path.join(output_dir, filename)
    
    if os.path.exists(filepath) and not force_regenerate:
        print(f"  [Skipped] {filename} already exists.")
        return True
        
    print(f"  [Generating] {filename} using {model_name}...")
    prompt = construct_prompt(course, section_title, lesson)
    
    # Retry logic for rate limits and transient errors
    retries = 3
    delay = 5
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=LessonNotebook,
                    temperature=0.2,
                )
            )
            
            # Parse response JSON structure
            content = json.loads(response.text)
            notebook_json = get_notebook_json(content["learning_objectives"], content["cells"])
            
            # Save to disk
            with open(filepath, "w") as f:
                json.dump(notebook_json, f, indent=2)
                
            print(f"  [Saved] {filepath}")
            return True
            
        except APIError as api_err:
            print(f"  [Error] API error on attempt {attempt + 1}: {api_err}")
            if "429" in str(api_err) or "Quota exceeded" in str(api_err):
                print(f"  Rate limit exceeded. Waiting {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                break
        except Exception as e:
            print(f"  [Error] Failed to generate {filename} on attempt {attempt + 1}: {e}")
            time.sleep(2)
            
    print(f"  [Failed] Could not generate {filename} after {retries} attempts.")
    return False

def main():
    parser = argparse.ArgumentParser(description="AgenticLabs Course Generation Script")
    parser.add_argument("--course_id", type=str, help="ID of specific course to generate (e.g. F-01)")
    parser.add_argument("--lesson_id", type=str, help="ID of specific lesson to generate (e.g. F01-L02)")
    parser.add_argument("--force", action="store_true", help="Force overwrite existing notebook files")
    parser.add_argument("--all", action="store_true", help="Generate all courses in the catalog")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash", help="Gemini model name to use")
    args = parser.parse_args()
    
    # Load parsed catalogue
    catalogue_path = "courses_catalogue.json"
    if not os.path.exists(catalogue_path):
        print("courses_catalogue.json not found! Run parse_courses.py first.")
        return
        
    with open(catalogue_path, "r") as f:
        catalogue = json.load(f)
        
    # Flatten structure for easy lookup and generation
    all_courses = []
    for track_id, track_info in catalogue.items():
        for course in track_info["courses"]:
            # Inject track info for prompts
            course["track_id"] = track_id
            course["track_label"] = track_info["label"]
            all_courses.append(course)
            
    if args.all:
        # Generate all courses headlessly
        print("Starting batch generation for all courses...")
        for course in all_courses:
            print(f"\nCourse: {course['id']} — {course['title']}")
            for section in course["sections"]:
                for lesson in section["lessons"]:
                    generate_lesson(course, section["title"], lesson, args.force, args.model)
                    time.sleep(1)
                    
    elif args.lesson_id:
        # Generate single lesson
        found = False
        for course in all_courses:
            for section in course["sections"]:
                for lesson in section["lessons"]:
                    if lesson["id"].lower() == args.lesson_id.lower():
                        generate_lesson(course, section["title"], lesson, args.force, args.model)
                        found = True
                        break
        if not found:
            print(f"Lesson with ID {args.lesson_id} not found.")
            
    elif args.course_id:
        # Generate single course
        found = False
        for course in all_courses:
            if course["id"].lower() == args.course_id.lower():
                print(f"Starting generation for Course: {course['id']} — {course['title']}")
                for section in course["sections"]:
                    print(f" Section: {section['title']}")
                    for lesson in section["lessons"]:
                        generate_lesson(course, section["title"], lesson, args.force, args.model)
                found = True
                break
        if not found:
            print(f"Course with ID {args.course_id} not found.")
            
    else:
        # Batch generation menu if run interactively or with no args
        print("=== AgenticLabs Course Generator ===")
        print("Select an option:")
        print("1. List all available courses")
        print("2. Generate a specific course")
        print("3. Generate all courses (WARNING: This will make a large number of API calls)")
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            print("\nTrack 1:")
            for c in [c for c in all_courses if "track1" in c["track_id"]]:
                print(f"  {c['id']} — {c['title']} ({len(c['sections'])} sections)")
            print("\nTrack 2:")
            for c in [c for c in all_courses if "track2" in c["track_id"]]:
                print(f"  {c['id']} — {c['title']} ({len(c['sections'])} sections)")
                
        elif choice == "2":
            c_id = input("Enter Course ID (e.g. F-01): ").strip()
            # Find and generate
            found = False
            for course in all_courses:
                if course["id"].lower() == c_id.lower():
                    print(f"Starting generation for Course: {course['id']} — {course['title']}")
                    for section in course["sections"]:
                        print(f" Section: {section['title']}")
                        for lesson in section["lessons"]:
                            generate_lesson(course, section["title"], lesson, args.force, args.model)
                            # Small throttle between calls to prevent rate limit spikes
                            time.sleep(1)
                    found = True
                    break
            if not found:
                print(f"Course with ID {c_id} not found.")
                
        elif choice == "3":
            confirm = input("Are you sure you want to generate all courses? (y/n): ").strip().lower()
            if confirm == "y":
                print("Starting batch generation for all courses...")
                for course in all_courses:
                    print(f"\nCourse: {course['id']} — {course['title']}")
                    for section in course["sections"]:
                        for lesson in section["lessons"]:
                            generate_lesson(course, section["title"], lesson, args.force, args.model)
                            time.sleep(1)
            else:
                print("Aborted.")

if __name__ == "__main__":
    main()
