import os
import requests
from dotenv import load_dotenv

# Load API keys and base URL from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_RAW_BASE = os.getenv("REPO_RAW_BASE")

# --- Step 1: Simple router (expand as needed)
def get_relevant_filename(question: str) -> str:
    q = question.lower()
    if "zoning" in q or "land use" in q or "adu" in q:
        return "title15_land_use.html"
    elif "mayor" in q or "city council" in q:
        return "title02_government.html"
    return "title01_general_provisions.html"

# --- Step 2: Fetch raw HTML from GitHub
def fetch_html_from_github(filename: str) -> str:
    url = f"{REPO_RAW_BASE}/{filename}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching file from GitHub: {url}")
    return response.text

# --- Step 3: Build a simple GPT prompt
def build_prompt(question: str, html_content: str) -> str:
    return f"""You are a legal assistant. Use the municipal code below to answer the question.

Municipal Code Content:
-----------------------
{html_content}

Question: {question}
Answer:
"""

# --- Main CLI entry point
def main():
    question = input("Ask a legal question: ")
    filename = get_relevant_filename(question)
    html_content = fetch_html_from_github(filename)
    prompt = build_prompt(question, html_content)
    
    print("\nGenerated Prompt:\n")
    print(prompt)

if __name__ == "__main__":
    main()
