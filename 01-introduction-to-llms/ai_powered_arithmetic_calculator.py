import os
import requests
"""
API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {   "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def chat_with_groq(user_request):
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "user",
                "content": user_request
            }
        ]
    }

    response = requests.post(
        url=URL,
        headers=HEADERS,
        json=payload
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]


##########################################################
# Main Program
##########################################################

while True:

    user_request = input("\nEnter your request (0 to Exit): ")

    if user_request == "0":
        print("\nThank You!")
        break

    answer = chat_with_groq(user_request)

    print("\nResponse:")
    print(answer)


##########################################################
# Local LLM (Ollama)
##########################################################

"""
import requests

URL = "http://localhost:11434/api/generate"


def chat_with_ollama(user_request):

    payload = {
        "model": "llama3.2",
        "prompt": user_request,
        "stream": False
    }

    response = requests.post(
        url=URL,
        json=payload
    )

    return response.json()["response"]


while True:

    user_request = input("\nEnter your request (0 to Exit): ")

    if user_request == "0":
        print("\nThank You!")
        break

    answer = chat_with_ollama(user_request)

    print("\nResponse:")
    print(answer)
