## AWS Bedrock RAG – Chat with Your PDFs

This project is a simple Retrieval-Augmented Generation (RAG) demo using **AWS Bedrock**, **LangChain**, **FAISS**, and **Streamlit**.  
It lets you upload PDF documents into a local vector store and then **chat with their contents** using Bedrock-hosted LLMs (Claude and Llama 3).

---

## Features

- **PDF ingestion** from a local `data` folder.
- **Text chunking** using `RecursiveCharacterTextSplitter`.
- **Vector store** built with `FAISS` and `BedrockEmbeddings` (`amazon.titan-embed-text-v1`).
- **RAG question answering** pipeline using LangChain retrieval chains.
- **Streamlit UI** to:
  - Update/create the FAISS index from PDFs.
  - Ask questions about the indexed documents.
  - Get answers from:
    - Claude (`us.anthropic.claude-3-haiku-20240307-v1:0`)
    - Llama 3 (`us.meta.llama3-2-1b-instruct-v1:0`)

---

## Project Structure

- `app.py` – Main Streamlit app (RAG pipeline and UI).
- `main.py` – Minimal CLI entry point printing a greeting.
- `data/` – Folder for your PDF files (created automatically if missing).
- `faiss_index/` – Folder where the FAISS vector index is stored (created after indexing).
- `pyproject.toml` / `requirements.txt` – Python dependencies and project metadata.

---

## Prerequisites

- **Python** `>= 3.13` (as specified in `pyproject.toml`).
- An **AWS account** with access to:
  - **Amazon Bedrock**.
  - The specific models used in this project:
    - `amazon.titan-embed-text-v1`
    - `us.anthropic.claude-3-haiku-20240307-v1:0`
    - `us.meta.llama3-2-1b-instruct-v1:0`
- AWS credentials configured locally so `boto3` can talk to Bedrock.  
  The app uses the **default AWS configuration**, so any of the following work:
  - `~/.aws/credentials` and `~/.aws/config`
  - Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` (or `AWS_DEFAULT_REGION`)

Make sure the AWS region you configure supports Amazon Bedrock and the selected models.

---

## Installation

From the project root (`AWS_Bedrock_Rag`):

```bash
# (Optional) create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate  # on Windows
# source .venv/bin/activate  # on macOS / Linux

# Install dependencies (choose one)
pip install -r requirements.txt
# or, if using uv / pyproject.toml
uv sync
```

---

## Preparing Your Data

1. Ensure there is a `data` folder in the project root:
   - The app will create it automatically if it does not exist.
2. Put one or more **PDF files** into the `data` folder.
3. These PDFs will be loaded, split into chunks, and embedded when you update the vector store from the UI.

---

## Running the Streamlit App

From the project root:

```bash
streamlit run app.py
```

Then open the URL that Streamlit prints in your terminal (usually `http://localhost:8501`).

### Using the UI

- **Sidebar → "Vectors Update" button**  
  - Click this to:
    - Load all PDFs from `data/`.
    - Split them into text chunks.
    - Create/update the FAISS index under `faiss_index/`.
  - Wait for the "Done" message.

- **Ask a question**  
  - In the main page, type a natural-language question in the input box
    `"Ask a Question from the PDF Files"`.

- **Choose an LLM**
  - Click **"Claude Output"** to query Claude via Bedrock.
  - Click **"Llama Output"** to query Llama 3 via Bedrock.
  - If you have not yet built the vector store, the app will prompt you to update vectors first.

The model is prompted to produce a detailed answer (around 150 words) **grounded strictly in the retrieved context**; if the answer is not present in the documents, it should say it does not know.

---

## Running the Simple CLI Script (Optional)

There is a minimal entry point in `main.py`. You can run it with:

```bash
python main.py
```

This is mostly a placeholder and not related to the Streamlit RAG app.

---

## Configuration Notes

- **Models**  
  The model IDs are currently hard-coded in `app.py`:
  - Embeddings: `amazon.titan-embed-text-v1`
  - Chat models:
    - `us.anthropic.claude-3-haiku-20240307-v1:0`
    - `us.meta.llama3-2-1b-instruct-v1:0`

  If you want to use different models or regions, update the IDs and ensure your AWS account has access.

- **Vector store location**  
  The FAISS index is saved locally in the `faiss_index/` directory.  
  You can delete this folder any time to force a full re-index of your PDFs.

---

## Troubleshooting

- **No such host / AccessDeniedException**  
  - Verify that:
    - Your AWS region supports Amazon Bedrock and the specific models.
    - Your IAM user/role has permissions to invoke Bedrock models.

- **Index errors / empty answers**  
  - Ensure you have at least one PDF in the `data/` folder.
  - Rebuild the index from the sidebar `"Vectors Update"` button.

- **Environment / dependency issues**  
  - Confirm you are using **Python 3.13+**.
  - Reinstall dependencies:
    - `pip install -r requirements.txt`

---


