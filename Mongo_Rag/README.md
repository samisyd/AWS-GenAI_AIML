# Mongo RAG (MongoDB Atlas + OpenAI)

This project demonstrates a simple Retrieval-Augmented Generation (RAG) workflow using:
- MongoDB Atlas Vector Search
- OpenAI embeddings (`text-embedding-3-large`)
- OpenAI chat completion (`gpt-4o`)
- PDF ingestion and chunking with LangChain

The current implementation is primarily in `test.ipynb` (notebook-based workflow).

## What this project does

1. Loads a PDF file.
2. Splits the text into chunks.
3. Generates embeddings for each chunk using OpenAI.
4. Stores text + vectors in MongoDB.
5. Creates a MongoDB Atlas Vector Search index.
6. Runs vector search for a user query.
7. Sends retrieved context to an LLM for final answer generation.

## Project structure

- `test.ipynb` - end-to-end RAG pipeline (main implementation)
- `main.py` - placeholder script entry point
- `requirements.txt` - pip dependency list
- `pyproject.toml` - project metadata + dependencies

## Prerequisites

- Python 3.13+
- MongoDB Atlas cluster with Vector Search enabled
- OpenAI API key

## Setup

### 1) Create and activate environment

You can use `uv` (recommended in this repo) or regular `pip`.

Using uv:

```powershell
uv sync
```

or install from requirements:

```powershell
uv add -r .\requirements.txt
```

Using pip:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2) Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_atlas_connection_string
MONGODB_DB=sample_mflix
MONGODB_COLLECTION=ragpdf
MONGODB_VECTOR_INDEX=vector_index
```

## Run the notebook workflow

1. Open `test.ipynb`.
2. Ensure your PDF file exists at the expected path (currently `cold_and_flu_r.pdf`).
3. Run cells in order:
	- load env and initialize OpenAI client
	- load/split PDF
	- generate embeddings and insert documents
	- create vector index and wait for readiness
	- query with `$vectorSearch`
	- generate final response using retrieved context

## Security notes

- Do not hardcode API keys or MongoDB credentials in notebook cells.
- Move all secrets to `.env` and never commit `.env` to source control.

## Dependencies used

- `pymongo`
- `openai`
- `langchain`
- `langchain_community`
- `langchain_openai`
- `langchain_groq`
- `python-dotenv`
- `ipykernel`
- `pypdf`

## Next suggested improvement

Refactor notebook logic into Python modules (ingestion, indexing, retrieval, generation) and make `main.py` run the full pipeline with command-line arguments.
