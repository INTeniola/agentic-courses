from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List, Literal

class Cell(BaseModel):
    cell_type: Literal["markdown", "code"]
    source: str

class LessonNotebook(BaseModel):
    learning_objectives: List[str]
    cells: List[Cell]

def test():
    client = genai.Client(vertexai=True, project="quizant", location="us-central1")
    
    prompt = """
    Generate a short beginner-friendly notebook content for:
    Course: Explore the GenAI Universe (F-01)
    Lesson: F01-L02 - From discriminative to generative models
    Type: concept
    
    Make it 2-3 cells maximum for the test. Ensure code cells have runnable Python code.
    """
    
    print("Generating test lesson...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LessonNotebook,
            temperature=0.2,
        ),
    )
    print("Response received:")
    print(response.text)

if __name__ == "__main__":
    test()
