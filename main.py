import requests    #pip install reguests

# Setup your API key and URL once
# API_KEY = "YOUR_DEEPSEEK_API_KEY"
API_KEY = "YOUR_DEEPSEEK_API_KEY"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def deepseek_chat(prompt, model="deepseek-llm", temperature=0.7):
    """
    Send a prompt to DeepSeek API and get the response.

    Args:
        prompt (str): The user's input to the AI model.
        model (str): The model name to use (default "deepseek-llm").
        temperature (float): Creativity level (0.0 - 1.0).

    Returns:
        str: The AI's response text.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Example usage
if __name__ == "__main__":
    prompt = "Write a funny two-line poem about coffee."
    reply = deepseek_chat(prompt)
    print("DeepSeek says:\n", reply)
