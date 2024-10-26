import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv('cred.env')

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Give me 5 names for my second hand luxury cars brand")
print(response.text)
