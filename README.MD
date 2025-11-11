# Feedback Agent - Streamlit Application

A Streamlit-based feedback analysis agent application that processes and analyzes feedback data using AI capabilities.

## Prerequisites

- Python 3.11.5
- pip (Python package installer)

## Installation

1. **Clone or download this repository** to your local machine

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **LLM keys & config: ***
- create .env file with openAI/AzureOpenAI config according to .env.example in FeedbackAgent folder

## Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run main.py
```

The application will start and automatically open in your default web browser. If it doesn't open automatically, you can access it at:
- Local URL: `http://localhost:8501`
- Network URL: `http://[your-ip]:8501`

## Project Structure

```
agent/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── Feedback.csv           # Feedback data file
├── FeedbackAgent/         # Core application modules
│   ├── __init__.py
│   ├── AzureOpenAIAdaptor.py
│   ├── DataProcess.py
│   ├── GenericLLM.py
│   ├── LLMFactory.py
│   ├── main.py
│   ├── PromptFactory.py
└── README.MD              # This file
```



