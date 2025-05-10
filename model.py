import google.generativeai as genai



# Initialize the client directly from the genai module
genai.configure(api_key="api key ?")

# Now you can access the models
model = genai.GenerativeModel("gemini-2.0-flash")

def gemini_model(user_input):
    response = model.generate_content(
        contents=f"{user_input}",
    )
    return response.text




