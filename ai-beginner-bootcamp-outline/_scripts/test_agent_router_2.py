import os
import httpx
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AGENT_ROUTER_API_KEY")

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

models_to_test = ["claude-3-opus-20240229", "claude-opus-5", "claude-3-5-sonnet-20240620"]

for m in models_to_test:
    print(f"Testing model: {m}")
    try:
        message = client.messages.create(
            model=m,
            max_tokens=50,
            messages=[
                {"role": "user", "content": "Reply 'OK'"}
            ]
        )
        print(f"Success with {m}: {message.content[0].text}")
        break
    except Exception as e:
        print(f"Failed {m}: {e}")
