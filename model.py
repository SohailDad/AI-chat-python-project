from google import genai


def gemini_model(user_input):
    client = genai.Client(api_key="api key?")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"what is the capital of pakistan"
    )
    print(response.text)