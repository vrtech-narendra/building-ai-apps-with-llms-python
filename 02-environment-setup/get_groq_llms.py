import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/models"

response = requests.get(
    url=URL,
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

response.raise_for_status()

models = response.json()["data"]

print("\nAvailable Models:\n")

for model in models:
    print(model["id"])