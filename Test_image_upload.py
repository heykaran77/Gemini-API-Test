import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("cred.env")

GEMINI_API = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API)

my_img = genai.upload_file("pikachu.jpg")
file_name = my_img.name

# print(f"{file_name}")
uploaded = genai.get_file(file_name)
print(f"{uploaded}")
