import requests

API_KEY = "YOUR_DEEPSEEK_API_KEY"

API_URL = "https://api.deepseek.com/v1/chat/completions"  # Correct URL

def deepseek_chat(prompt, model="deepseek-chat", temperature=0.7):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a fun fact about the universe."
    reply = deepseek_chat(prompt)
    print("DeepSeek says:\n", reply)
