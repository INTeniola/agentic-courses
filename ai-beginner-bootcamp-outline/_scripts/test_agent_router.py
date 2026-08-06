import os
import httpx
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AGENT_ROUTER_API_KEY")

if not api_key:
    print("Please set AGENT_ROUTER_API_KEY in your .env file.")
    exit(1)

client = Anthropic(
    api_key=api_key,
    base_url="https://agentrouter.org",
    http_client=httpx.Client(
        headers={
            "User-Agent": "cline/2.0.0",
            "Accept": "application/json"
        }
    )
)

try:
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=50,
        messages=[
            {"role": "user", "content": "Reply with 'Agent Router connection successful' and nothing else."}
        ]
    )
    print(message.content[0].text)
except Exception as e:
    print(f"Error connecting to Agent Router: {e}")
