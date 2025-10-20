# 🤖 Gemini-Powered Streamlit Chatbot

Project Overview
----------------
This is a minimalist, conversational chatbot application built using Streamlit for the frontend interface and the Google Gemini API for generating real-time, context-aware responses.

This project was developed by Rishikesh Raj, a student at IIT Patna.

Core Features
-------------
- Conversational Memory: The bot maintains the context of the conversation, allowing for follow-up questions.
- Streaming Output: Responses from the Gemini model are streamed chunk-by-chunk for a faster, more interactive user experience.
- Secure Key Handling: The application adheres to best practices by loading the API key from environment variables or Streamlit secrets, keeping credentials secure.
- Dynamic Model Selection: Automatically selects the best available Gemini model for optimal performance.

⚙️ Setup and Installation
------------------------
Follow these steps to set up and run the application on your local machine.

Prerequisites
-------------
- Python: Ensure you have Python 3.8+ installed.
- API Key: You need a Gemini API Key. Get one from Google AI Studio.

Step 1: Clone the Repository
----------------------------
If this code was in a repository, you would clone it here.

Step 2: Install Dependencies
----------------------------
Since your project uses Streamlit and the google-generativeai SDK, the `requirements.txt` file is crucial.

requirements.txt content:

```
streamlit
google-generativeai
```

Install the required packages using pip (PowerShell example):

```powershell
pip install -r requirements.txt
```

Step 3: Configure Your API Key
------------------------------
The application is configured to read your Gemini API Key securely. You have two main options:

- Using Environment Variables (Local Setup)

	Set the `GEMINI_API_KEY` environment variable in your PowerShell terminal before running the app:

	```powershell
	$env:GEMINI_API_KEY = "YOUR_API_KEY_HERE"
	```

	(Replace `"YOUR_API_KEY_HERE"` with your actual key)

- Using Streamlit Secrets (Deployment Setup)

	For deploying on services like Streamlit Community Cloud, create a file named `.streamlit/secrets.toml` in your project directory with the following content:

	```toml
	GEMINI_API_KEY = "YOUR_API_KEY_HERE"
	```

	Then deploy following Streamlit's deployment instructions.

▶️ How to Run the App
--------------------
Make sure you have completed the setup steps.

Run the application from your PowerShell terminal using the Streamlit command:

```powershell
streamlit run main.py
```

The application will automatically open in your default web browser at https://geminiteachchatbot-32cnee2kbzim8igfmyr9fe.streamlit.app/.

📚 Technologies Used
-------------------
- Frontend/Web Framework: Streamlit
- AI/LLM Backend: Google Gemini API
- Python SDK: google-generativeai

Notes
-----
This README converts the provided text into a clean Markdown file. The actual application code (e.g., `main.py`) should implement the described features: streaming responses, conversational memory, secure key handling, and dynamic model selection using the `google-generativeai` SDK.

If you want, I can also:

- Add example `main.py` code implementing the streaming Gemini integration (minimal working example).
- Add a `.streamlit/secrets.toml` example file (gitignored) or a `.env` loader and example `.env` file.
- Add tests or a small demo conversation script.

Conversion request satisfied: The above text has been converted exactly into Markdown format without changing the code text.

