import os
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

def generate_transcript(day_number, topic, focus):
    prompt = f"""
    You are writing the official video presentation script for an AI instructor at AgenticLabs.ng.
    This is for a 5-Day Bootcamp where students build a "Universal Knowledge Worker" AI Agent.
    
    Day {day_number} Topic: {topic}
    Focus: {focus}
    
    Write a 500-800 word spoken-word transcript that the instructor will read to the camera.
    - Keep the tone highly encouraging, professional, and accessible to beginners.
    - Do NOT use markdown symbols that a Text-to-Speech (TTS) engine would read aloud (like asterisks, hash marks, or backticks). Just write clean prose.
    - Include simple visual cues in brackets like [Show slide 1] or [Switch to screen recording].
    
    Start directly with the script. Do not add any conversational padding before or after.
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
        print(f"Error generating transcript for Day {day_number}: {e}")
        return ""

def main():
    days = [
        (1, "Hire the Brain", "Introduction to autonomous agents, the Think-Act-Observe loop, and configuring Google AI Studio."),
        (2, "Give it Hands", "Connecting the agent to tools like Web Search so it can access real-time information."),
        (3, "Give it Memory", "Implementing conversation sessions so the agent can remember past interactions and context."),
        (4, "Quality Control", "Introducing the temperature parameter, guardrails, and evaluating agent performance."),
        (5, "Multi-Agent Teams", "Creating a system where a Manager, Researcher, and Writer agent collaborate to build a report.")
    ]
    
    for day_num, topic, focus in days:
        print(f"Generating transcript for Day {day_num}...")
        transcript = generate_transcript(day_num, topic, focus)
        
        if transcript:
            out_dir = f"../day_{day_num}"
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"Day_{day_num}_Transcript.md")
            
            with open(out_path, "w") as f:
                f.write(f"# Day {day_num} Video Transcript: {topic}\n\n")
                f.write(transcript)
            print(f"Saved {out_path}")

if __name__ == "__main__":
    main()
