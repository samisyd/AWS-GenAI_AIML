# FinancialAssistant Blog Generator

A Python script that generates a **blog article from provided content** using **Google Gemini (Gemini 2.5 Flash)** and then creates a **relevant image** for the article using **Hugging Face Stable Diffusion XL**. The output includes a **markdown file** for the article and a **corresponding image**.

---

## Features

- Reads content from `content.txt`
- Generates a **2000-character blog article** with **markdown formatting**
- Automatically inserts a **placeholder for one image** in the article
- Generates an **image prompt** based on the article using Gemini
- Creates an **image using Stable Diffusion XL** (v1.0)
- Saves output in a unique folder: `output/<unique_id>/`

---

## Requirements

- Python 3.10+
- Virtual environment recommended
- Environment variables:

# Required in .env
- GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
- HF_TOKEN=<YOUR_HUGGINGFACE_TOKEN>

## Install required Python packages:
pip install python-dotenv langchain langchain-google-genai huggingface-hub Pillow requests


# Usage
Prepare content
Create a content.txt file in the root directory with the text you want to turn into a blog article.

Example folder structure:

output/

└── <unique_id>/

    ├── article.md
    └── image.png


## How it Works

- Blog Generation (Text)
Uses Google Gemini 2.5 Flash to read your content.txt and generate a professional, engaging blog article. Markdown formatting is applied, and a single image placeholder is inserted.

- Image Prompt Generation
Gemini is then used again to create a prompt for an image relevant to the article content.

- Image Generation
The prompt is sent to Stable Diffusion XL (Hugging Face) to generate a high-quality image.

## Notes

- The blog article will contain exactly one image placeholder: ![image](image.png)
- Make sure your Hugging Face token (HF_TOKEN) has access to Stable Diffusion XL.
- Google Gemini API requires a valid GOOGLE_API_KEY
- Pillow is required to save images locally.

## Optional Improvements

- Automatically insert the generated image into the markdown
- Allow choosing different LLM or image generation models
- Add CLI arguments for content file, output folder, or image model
- Batch processing for multiple articles