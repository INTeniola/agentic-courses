import os
import json
from google import genai
from google.genai import types

try:
    client = genai.Client(vertexai=True, project="quizant", location="us-central1")
except Exception as e:
    print(f"Error initializing GenAI Client: {e}")
    exit(1)

def main():
    print("Reading Day 1 Primer and Notebook for video synthesis...")
    primer_text = ""
    if os.path.exists("day_1/Day_1_Primer.md"):
        with open("day_1/Day_1_Primer.md", "r") as f:
            primer_text = f.read()

    notebook_text = ""
    if os.path.exists("day_1/Day_1_Notebook.ipynb"):
        with open("day_1/Day_1_Notebook.ipynb", "r") as f:
            notebook_text = f.read()

    # 1. Generate Voiceover Script & Storyboard
    print("1/4: Generating Day 1 Video Script & Storyboard using Gemini 2.5 Pro...")
    script_prompt = f"""
    You are an elite AI course creator and video producer for AgenticLabs.ng.
    Create a complete, professional, word-for-word Video Voiceover Script and Storyboard for Day 1 of the AI Agents Bootcamp.
    
    Target Length: ~1,000 - 1,200 words (~8 to 10 minutes of spoken instruction).
    Tone: Engaging, authoritative, clear, and beginner-friendly (like a Google AI Dev Advocate).
    
    Structure the document into 4 sections:
    1. Introduction & Hook (Why passive LLMs are evolving into active Autonomous Agents).
    2. Conceptual Deep Dive (Agent architecture: Brain, Tools, Memory, Planning).
    3. Code Walkthrough (Explaining how we build an agent with Python and the Gemini SDK).
    4. Capstone Challenge & Recap (Introducing the Personal AI Research Assistant project).
    
    Format using Markdown. Include clear visual cues in brackets like:
    [VISUAL CUE: Show Slide 3 - Passive Model vs Autonomous Agent]
    [VISUAL CUE: Switch to Colab Notebook Cell 4 - Code execution]
    [VISUAL CUE: Show Veo B-Roll Prompt #2 - Neural Network connecting to APIs]
    
    Day 1 Primer Context:
    {primer_text[:15000]}
    
    Day 1 Notebook Context:
    {notebook_text[:15000]}
    """

    script_res = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=script_prompt,
        config=types.GenerateContentConfig(temperature=0.3)
    )
    
    script_content = script_res.text
    if script_content.startswith("```markdown"):
        script_content = script_content.replace("```markdown\n", "", 1).rstrip("`\n")
    elif script_content.startswith("```"):
        script_content = script_content.replace("```\n", "", 1).rstrip("`\n")

    with open("day_1/Day_1_Video_Script.md", "w") as f:
        f.write(script_content.strip())
    print("Saved day_1/Day_1_Video_Script.md")

    # 2. Generate Reveal.js HTML Slide Deck
    print("2/4: Generating Day 1 Reveal.js Interactive Slides (HTML) using Gemini 2.5 Pro...")
    slides_prompt = f"""
    You are an expert front-end web developer and presentation designer.
    Create a complete, single-file standalone HTML presentation using Reveal.js for Day 1 of the AI Agents Bootcamp: "Introduction to Autonomous Agents".
    
    Requirements:
    - Include full Reveal.js CDN scripts and styles:
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/dracula.min.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
    - Include modern custom CSS (Inter font from Google Fonts, sleek glassmorphism cards, glowing gradients, high contrast text).
    - 8 to 10 visual slides matching the Day 1 Video Script:
      Slide 1: Title & Welcome (Day 1: Introduction to Autonomous Agents)
      Slide 2: The Shift (Passive Chatbots vs. Active Agents)
      Slide 3: Anatomy of an Agent (Brain, Tools, Memory, Planning)
      Slide 4: ReAct Loop (Reasoning + Acting)
      Slide 5: Code Spotlight (Building your first Agent in Python)
      Slide 6: Google Search Grounding (Live Information Access)
      Slide 7: Multi-Agent Collaboration
      Slide 8: Mini-Capstone (Building a Personal AI Research Assistant)
      Slide 9: Recap & Next Steps
    - Provide complete, valid HTML containing `<!DOCTYPE html>...</html>`. Do NOT use backticks or markdown fences in the response.

    Day 1 Primer Context:
    {primer_text[:10000]}
    """

    slides_res = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=slides_prompt,
        config=types.GenerateContentConfig(temperature=0.2)
    )

    slides_html = slides_res.text
    if "```html" in slides_html:
        slides_html = slides_html.split("```html")[1].split("```")[0]
    elif "```" in slides_html:
        slides_html = slides_html.split("```")[1].split("```")[0]

    with open("day_1/Day_1_Slides.html", "w") as f:
        f.write(slides_html.strip())
    print("Saved day_1/Day_1_Slides.html")

    # 3. Generate Veo Prompts
    print("3/4: Generating Google Veo Cinematic Video Prompts...")
    veo_prompt = f"""
    Create a list of 5 high-impact, cinematic text-to-video prompts for Google Veo on Vertex AI to generate background B-roll clips for Day 1: Introduction to Agents.
    
    Each prompt must follow Google Veo best practices:
    - Include camera movement (e.g., slow pan, macro tracking, drone fly-through).
    - Specify lighting, style, resolution (4K, photorealistic / futuristic 3D render, dark mode aesthetics).
    - Provide a description of what audio section of Day 1 the clip accompanies.
    
    Output strictly in markdown format.
    """

    veo_res = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=veo_prompt,
        config=types.GenerateContentConfig(temperature=0.3)
    )

    veo_content = veo_res.text
    if veo_content.startswith("```markdown"):
        veo_content = veo_content.replace("```markdown\n", "", 1).rstrip("`\n")
    elif veo_content.startswith("```"):
        veo_content = veo_content.replace("```\n", "", 1).rstrip("`\n")

    with open("day_1/Day_1_Veo_Prompts.md", "w") as f:
        f.write(veo_content.strip())
    print("Saved day_1/Day_1_Veo_Prompts.md")

    # 4. Generate TTS Python Script
    print("4/4: Writing TTS Generation Script for Day 1...")
    tts_script_code = '''import os
from google.cloud import texttospeech

def synthesize_audio():
    print("Synthesizing Day 1 voiceover narration with Google Cloud Text-to-Speech...")
    
    if not os.path.exists("Day_1_Video_Script.md"):
        print("Error: Day_1_Video_Script.md not found.")
        return

    with open("Day_1_Video_Script.md", "r") as f:
        lines = f.readlines()

    # Extract spoken narration (filter out visual cues and headers)
    narration_text = []
    for line in lines:
        cleaned = line.strip()
        if cleaned.startswith("[VISUAL CUE") or cleaned.startswith("#"):
            continue
        if cleaned:
            narration_text.append(cleaned)

    full_narration = " ".join(narration_text)

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=full_narration[:4000]) # GCP TTS limit per call

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-D", # Natural, professional male voice
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.0,
        pitch=0.0
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("Day_1_Narration.mp3", "wb") as out:
        out.write(response.audio_content)
        print("✅ Saved day_1/Day_1_Narration.mp3 successfully!")

if __name__ == "__main__":
    synthesize_audio()
'''

    with open("day_1/generate_tts_day1.py", "w") as f:
        f.write(tts_script_code)
    print("Saved day_1/generate_tts_day1.py")

    print("\n🎉 Day 1 Video Asset Generation Complete!")

if __name__ == "__main__":
    main()
