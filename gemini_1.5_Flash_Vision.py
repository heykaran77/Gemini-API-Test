#Using Gemini API for Image to Text Generation
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image

load_dotenv('cred.env')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

myfile = genai.upload_file("pikachu.jpg")
# print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")

#using to Prompt with multi Images.
img1 = PIL.Image.open("gwagon.jpg")
img2 = PIL.Image.open("pikachu.jpg")
prompt = "give an advertising hook based on how the img2 can be used in img1"


result = model.generate_content(
    [prompt,img1,img2]
)
print(f"{result.text=}")
