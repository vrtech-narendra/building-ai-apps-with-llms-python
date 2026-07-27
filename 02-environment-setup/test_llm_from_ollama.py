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

# user_request = input("\nEnter your request :  ")
# answer = chat_with_ollama(user_request)

# print("\nResponse:")
# print(answer)

while True:

    user_request = input("\nEnter your request (0 to Exit): ")

    if user_request == "0":
        print("\nThank You!")
        break

    answer = chat_with_ollama(user_request)

    print("\nResponse:")
    print(answer)
