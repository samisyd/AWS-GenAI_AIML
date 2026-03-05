# Financial AI Analyst

A sophisticated AI-powered financial analysis tool built using the Phi agent framework. This project demonstrates multi-agent systems for comprehensive financial data analysis, combining web search capabilities with specialized financial tools.

## Features

- **Multi-Agent Architecture**: Combines web search and financial analysis agents for comprehensive insights
- **Financial Tools**: Access to stock prices, analyst recommendations, company fundamentals, and news via YFinance
- **Web Search Integration**: DuckDuckGo-powered web search for additional context and information
- **Interactive Playground**: Web-based interface for easy interaction with agents
- **Multiple Model Support**: Compatible with OpenAI GPT models and Groq's Llama models
- **Real-time Data**: Live financial data and news updates

## Installation

### Prerequisites
- Python 3.13 or higher
- API keys for OpenAI and/or Groq

### Setup

1. Clone or download the project:
   ```bash
   cd "Financial AI analyst"
   ```

2. Install dependencies using uv (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   PHI_API_KEY=your_phi_api_key_here
   ```

## Usage

### Running the Playground (Interactive Web Interface)

The playground provides a web-based interface to interact with the AI agents:

```bash
uv run playground.py
```

Or with Python:
```bash
python playground.py
```

This will start a local web server. Open your browser and navigate to the provided URL to access the playground.

### Running Individual Scripts

#### Multi-Agent Version (OpenAI)
```bash
python financial_multiAgt.py
```

#### Single Agent Version (Groq)
```bash
python financial_agent_single.py
```

### Example Queries

- "Summarize analyst recommendations and share the latest news for NVDA"
- "Compare NVDA and TSLA stock performance"
- "What are the fundamentals of AAPL?"

## Project Structure

```
Financial AI analyst/
├── financial_agent_single.py    # Single agent using Groq
├── financial_multiAgt.py        # Multi-agent system using OpenAI
├── main.py                      # Main entry point (placeholder)
├── playground.py                # Web playground interface
├── pyproject.toml               # Project configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Dependencies

- **phidata**: Agent framework
- **yfinance**: Financial data tools
- **duckduckgo-search**: Web search functionality
- **openai**: OpenAI API integration
- **groq**: Groq API integration
- **fastapi**: Web framework for playground
- **uvicorn**: ASGI server
- **python-dotenv**: Environment variable management

## Configuration

The agents are configured with the following tools:

- **YFinanceTools**:
  - Stock prices
  - Analyst recommendations
  - Company fundamentals
  - Company news

- **DuckDuckGo**: Web search with source attribution

## Contributing

This is an educational project for building agentic AI systems. Feel free to experiment and extend the functionality.

## License

This project is for educational purposes. Please ensure compliance with API terms of service and data usage policies.