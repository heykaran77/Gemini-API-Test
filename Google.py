import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv("cred.env")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

response = chat_session.send_message(
    "give me a letter with reason for a holiday of 5 days to Mumbai!")

print(response.text)
