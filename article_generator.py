import os
import uuid
import requests

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from huggingface_hub import InferenceClient
from PIL import Image


load_dotenv()

UNIQUE_ID = uuid.uuid4()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7, api_key=os.getenv("GOOGLE_API_KEY"))

print("Reading content from content.txt...")
with open("content.txt", "r", encoding="utf-8") as file:
    text_content = file.read()
    print(f"Content read successfully. Length: {len(text_content)} characters.")

# Your instruction string
write_blog_article_instructions = f"""
Please write a blog article on the topic provided in the text below. The blog post should be around 2000 characters long and cover all the most important points from the material provided. You are a knowledgeable expert in the field, so please write in a professional tone, but make sure to keep it engaging, fun, and easy to read.
Use markdown formatting to structure the article with headings, bullet points, numbered lists, and other markdown features where appropriate. Make sure you only return the article in valid markdown format and do not include introduction statements that are not part of the article like "sure I can help you, here is the article:".
Please insert only a single ![image](image.png) tag in the article, at an appropriate location, where the image will be inserted later. You can just use 'image' and 'image.png' as placeholders for now. Make sure you insert only a single image tag and do not include any other images in the article. Do not use ```markdown code blocks``` in the article or anywhere in your response, I know that the response will be markdown, so you do not have to indicate that.

Text:
{text_content}

Blog Article:
"""

print("Generating blog article...")
# Equivalent to {"role": "user", "content": ...}
article_response = llm.invoke([
    HumanMessage(content=write_blog_article_instructions)
])


blog_article = article_response.content
if not blog_article:
    print("Something went wrong, please try again.")
    exit()

print(f"Blog article generated. Length: {len(blog_article)} characters.")

output_folder = f"output/{UNIQUE_ID}"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

blog_article_save_location = f"{output_folder}/article.md"
with open(blog_article_save_location, "w", encoding="utf-8") as file:
    file.write(blog_article)
    print(f"Article saved as {blog_article_save_location}")


create_image_description_instructions = f"""
I have a blog article that I would like to create an image for. Please read through the article provided below and then come up with a prompt for an image that would be suitable for the content. Make sure your prompt doesn't request for any text to be included in the image, we want to include only visual elements but no text in the image itself.

Your prompt is going to be fed into imagen-3.0-generate-002 to generate an image, so make sure that your prompt is descriptive enough to guide the model in creating a relevant image that goes well with the blog article provided.

Blog Article:
{blog_article}

Image Prompt:
"""

print("Getting prompt for image generation...")
image_prompt_response = llm.invoke([
    HumanMessage(content=create_image_description_instructions)
])

image_generation_prompt = image_prompt_response.content
if not image_generation_prompt:
    print("Something went wrong, please try again.")
    exit()


print(f"Generating image with prompt: {image_generation_prompt}")

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
client = InferenceClient(model_id, token=os.getenv("HF_TOKEN"))

image = client.text_to_image(image_generation_prompt)
    
image_save_location = f"{output_folder}/image.png"
image.save(image_save_location)

print(f"Image saved as {image_save_location}")


