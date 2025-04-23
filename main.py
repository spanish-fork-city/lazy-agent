import os
import requests
from dotenv import load_dotenv
from app.router import get_relevant_filename  # NEW

load_dotenv()
REPO_RAW_BASE = os.getenv("REPO_RAW_BASE")

def fetch_html_from_github(filename: str) -> str:
    url = f"{REPO_RAW_BASE}/{filename}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching file from GitHub: {url}")
    return response.text

def build_prompt(question: str, html_content: str) -> str:
    return f"""You are a legal assistant. Use the municipal code below to answer the question.

Municipal Code Content:
-----------------------
{html_content}

Question: {question}
Answer:
"""

def main():
    question = input("Ask a legal question: ")
    filename = get_relevant_filename(question)
    html_content = fetch_html_from_github(filename)
    prompt = build_prompt(question, html_content)

    print("\nGenerated Prompt:\n")
    print(prompt)

if __name__ == "__main__":
    main()
