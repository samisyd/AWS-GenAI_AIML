import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()
# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7, api_key=os.getenv("GOOGLE_API_KEY"))

# Your instruction string
duck_instructions = """
You are a duck. You will answer the question in a helpful manner but do not forget to quack every few words.
My question is: What is the fastest animal on Earth?
"""
print("Asking DuckGPT...")
#Equivalent to {"role": "user", "content": ...}
duck_response = llm.invoke([
    HumanMessage(content=duck_instructions)
])

quack_talk = duck_response.content
print(f"The duck says: {quack_talk}")


import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for m in genai.list_models():
    print(m.name)

