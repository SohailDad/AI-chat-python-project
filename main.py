from google import genai

client = genai.Client(api_key="")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="what is the capital of pakistan"
)
print(response.text)