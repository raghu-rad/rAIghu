# Client to call LLM API

import requests

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat.")
            break

        host = "http://localhost"
        port = 8000
        url = f"{host}:{port}/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        data = {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            response_json = response.json()
            message = response_json["choices"][0]["message"]["content"]
            print(f"LLM: {message}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()