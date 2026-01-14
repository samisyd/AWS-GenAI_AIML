# Gemini Chatbot with Streamlit

A conversational question-answer chatbot built with Streamlit and Google's Gemini gemini-2.5-flash API. The chatbot automatically saves all conversations and displays them in a beautiful chat interface.
Features

    💬 Conversational Q&A chatbot using Gemini Pro    
    📜 Display complete chat history in the UI        
    🔒 Secure API key management

Setup
1. Install Dependencies

First, activate your virtual environment and install the required packages:

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
uv add -r requirements.txt

2. Get Gemini API Key

    Visit Google AI Studio
    Sign in with your Google account
    Click "Create API Key"
    Copy your API key

3. Configure API Key

Environment Variable 
    Create a .env file in the project root
    Add your API key:

    GOOGLE_API_KEY=your_api_key_here

4. Run the Application

streamlit run Chatbot.py

The app will open in your default web browser at http://localhost:8501
Usage
    
    Start chatting by typing your question in the chat input
    The chatbot will respond using Gemini Pro    
    Chat history persists across sessions

   

```
Project1/
├── .venv/              # Virtual environment
├── chatbot.py          # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # API key configuration (optional)
└── README.md          # This file
```

Requirements

    Python 3.8+
    Streamlit
    google-generativeai
    python-dotenv


    The chatbot uses Gemini gemini-2.5-flash model with optimized settings
    All conversations include timestamps
