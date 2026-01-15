import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image

load_dotenv()

from huggingface_hub import HfApi
api = HfApi()
for model in api.list_models(author="stabilityai", filter="text-to-image"):
    print(model.modelId)

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
client = InferenceClient(model_id, token=os.getenv("HF_TOKEN"))

prompt = "A small cute kitten"
image = client.text_to_image(prompt)
    
image.save("output.png")
print("✅ Image saved as output.png")