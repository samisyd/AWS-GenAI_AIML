# Financial AI Analyst

A multi-agent financial analysis project built with **Phidata** and **Groq** models.

It includes:
- a **web search agent** (DuckDuckGo)
- a **finance agent** (Yahoo Finance tools)
- a **team agent** that combines both for richer responses
- a **Playground app** for interactive usage

## Project Structure

```text
.
├── financial_agent.py   # Team agent example (CLI response)
├── playground.py        # Playground web app
├── main.py              # Basic entry script
├── pyproject.toml       # Project metadata and dependencies
├── requirements.txt     # Pip-style dependencies
└── README.md
```

## Requirements

- Python **3.13+**
- API keys in environment variables (see below)

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
PHI_API_KEY=your_phi_api_key
GROQ_API_KEY=your_groq_api_key
```

## Installation

### Option 1: Using `uv` (recommended)

```bash
uv sync
```

If you prefer your existing requirements file:

```bash
uv add -r requirements.txt
```

### Option 2: Using `pip`

```bash
pip install -r requirements.txt
```

## Run the Project

### 1) Run agent script

This executes the team agent query defined in `financial_agent.py`:

```bash
python financial_agent.py
```

### 2) Run Playground app

Start the interactive UI:

```bash
python playground.py
```

The app is served by Uvicorn via `serve_playground_app`.

### 3) Run baseline script

```bash
python main.py
```

## What the Agents Do

- **Web Search Agent**: finds current web information and returns sources.
- **Finance AI Agent**: fetches stock price, fundamentals, analyst recommendations, and news with `YFinanceTools`.
- **Multi Agent Team**: combines outputs to answer financial questions with sources and tabular formatting.

## Example Prompt

The current script includes:

`Summarize analyst recommendation and share the latest news for NVDA`

You can modify this prompt in `financial_agent.py`.

## Notes

- Ensure `.env` is loaded before running scripts.
- If model/provider credentials are missing, agent calls will fail.

